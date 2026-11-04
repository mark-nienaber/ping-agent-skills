---
title: Add a DaVinci Flow Version Alias
description: Add a user-friendly alias to a PingOne DaVinci flow version specified by its ID
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flow-versions/add-flow-version-alias
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flow-versions/add-flow-version-alias.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Add a DaVinci Flow Version Alias

##

Required permission:

* [davinci:update:flowVersions](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-update-flowVersions "Learn more about this permission")

```none
PUT {{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias
```

The `PUT {{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias` updates the flow version specified by its ID in the request URL to add an alias. The request body uses the `alias` property to specify a user friendly name for the flow version.

### Prerequisites

* Refer to [Create DaVinci Flow](../admin-flows/create-flow.html) for important overview information.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "alias": "someUserFriendlyName"
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
curl --location --globoff --request PUT '{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "alias": "someUserFriendlyName"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Put);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""alias"": ""someUserFriendlyName""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias"
  method := "PUT"

  payload := strings.NewReader(`{
    "alias": "someUserFriendlyName"
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
PUT /v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "alias": "someUserFriendlyName"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"alias\": \"someUserFriendlyName\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias",
  "method": "PUT",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "alias": "someUserFriendlyName"
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': '{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "alias": "someUserFriendlyName"
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

url = "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias"

payload = json.dumps({
  "alias": "someUserFriendlyName"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias');
$request->setMethod(HTTP_Request2::METHOD_PUT);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "alias": "someUserFriendlyName"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Put.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "alias": "someUserFriendlyName"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"alias\": \"someUserFriendlyName\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "PUT"
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
    "_links": {
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/a79d1931573009379f0691befa538d97/versions/0/alias"
        },
        "flowVersion": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/a79d1931573009379f0691befa538d97/versions/0"
        }
    },
    "alias": "someUserFriendlyName"
}
```

---

---
title: Clone a DaVinci Flow
description: Clone an existing PingOne DaVinci flow specified by its ID to create a new flow
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flows/clone-flow
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flows/clone-flow.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Clone a DaVinci Flow

##

Required permission:

* [davinci:create:dvFlows](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-dvFlows "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}
```

The `POST {{apiPath}}/v1/environments/{{envID}}/flows/{{flowID}}` endpoint uses the `application/vnd.pingidentity.flow.clone+json` custom `Content-Type` value to initiate an action to clone the flow specified by its ID in the request URL.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.flow\.clone+json

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
curl --location --globoff --request POST '{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}' \
--header 'Content-Type: application/vnd.pingidentity.flow.clone+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.flow.clone+json");
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

  url := "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.flow.clone+json")
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
POST /v1/environments/{{envID}}/flows/{{davinciFlowID}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.flow.clone+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.flow.clone+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.flow.clone+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.flow.clone+json",
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
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.flow.clone+json',
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
import json

url = "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}"

payload = {}
headers = {
  'Content-Type': 'application/vnd.pingidentity.flow.clone+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.flow.clone+json',
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
require "json"
require "net/http"

url = URI("{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.flow.clone+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.flow.clone+json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"

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

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/08d8c276ea2ab7533b7fa9e9ee4529f9"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "connectorInstances": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/connectorInstances"
        },
        "flow.deploy": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/08d8c276ea2ab7533b7fa9e9ee4529f9"
        },
        "flow.clone": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/08d8c276ea2ab7533b7fa9e9ee4529f9"
        },
        "flow.enabled": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/08d8c276ea2ab7533b7fa9e9ee4529f9/enabled"
        }
    },
    "id": "08d8c276ea2ab7533b7fa9e9ee4529f9",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "[cloned] 1713556525773 - DV-Flow_1713556322",
    "description": "Cloned on Fri Apr 19 2024 19:55:25 GMT+0000 (Coordinated Universal Time). \nTest Description - created via CREATE Flow request",
    "enabled": true,
    "currentVersion": 0,
    "createdAt": "2024-04-19T19:55:25.778Z",
    "updatedAt": "2024-04-19T19:55:25.792Z"
}
```

---

---
title: Clone DaVinci Connector Instance
description: Clone an existing PingOne DaVinci connector instance to create a new connector instance resource
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connections/clone-connection
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connections/clone-connection.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Clone DaVinci Connector Instance

##

Required permission:

* [davinci:create:connections](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-connections "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}
```

The `POST {{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}` clones the connector instance resource specified by its ID in the request URL.

### Prerequisites

* [Create DaVinci Connector Instance](create-connection.html) to get a `connectorInstanceID` for the request URL.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.connectorInstance.clone+json

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
curl --location --globoff --request POST '{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}' \
--header 'Content-Type: application/vnd.pingidentity.connectorInstance.clone+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.connectorInstance.clone+json");
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

  url := "{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.connectorInstance.clone+json")
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
POST /v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.connectorInstance.clone+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.connectorInstance.clone+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.connectorInstance.clone+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.connectorInstance.clone+json",
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
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.connectorInstance.clone+json',
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
import json

url = "{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}"

payload = {}
headers = {
  'Content-Type': 'application/vnd.pingidentity.connectorInstance.clone+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.connectorInstance.clone+json',
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
require "json"
require "net/http"

url = URI("{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.connectorInstance.clone+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.connectorInstance.clone+json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "POST"

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

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/connectorInstances/5e07e45a30ce10b8cbba65e6047d48df"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "connectorInstance.clone": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/connectorInstances/5e07e45a30ce10b8cbba65e6047d48df"
        }
    },
    "id": "5e07e45a30ce10b8cbba65e6047d48df",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "connector": {
        "id": "pingOneSSOConnector"
    },
    "name": "HTTP_Connection clone dc1d",
    "createdAt": "2024-04-19T22:43:01.161Z",
    "updatedAt": "2024-04-19T22:43:01.161Z"
}
```

---

---
title: Create DaVinci Application
description: Create a new PingOne DaVinci application resource in the specified environment
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-applications/create-davinci-application
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-applications/create-davinci-application.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Application

##

Required permission:

* [davinci:create:applications](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-applications "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/davinciApplications
```

The `POST {{apiPath}}/v1/environments/{{envID}}/davinciApplications` endpoint creates a new DaVinci application resource.

> **Collapse: Request Model**
>
> | Property             | Type    | Required |
> | -------------------- | ------- | -------- |
> | `apiKey`             | Object  | Optional |
> | `apiKey.enabled`     | Boolean | Optional |
> | `apiKey.value`       | String  | Optional |
> | `name`               | String  | Required |
> | `oauth`              | Object  | Optional |
> | `oauth.clientSecret` | String  | Optional |
> | `oauth.redirectUris` | Array   | Optional |
> | `oauth.logoutURIs`   | Array   | Optional |
> | `oauth.scopes`       | Array   | Optional |
> | `oauth.grantTypes`   | Array   | Optional |
> | `oauth.spjwksUrl`    | String  | Optional |
> | `oauth.spJwksOpenid` | String  | Optional |
>
> Refer to [DaVinci Admin Applications data model](index.html#davinci-admin-applications-data-model) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
"name": "dv_Application"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/davinciApplications' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
"name": "dv_Application"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/davinciApplications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"""name"": ""dv_Application""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/davinciApplications"
  method := "POST"

  payload := strings.NewReader(`{
"name": "dv_Application"
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
POST /v1/environments/{{envID}}/davinciApplications HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
"name": "dv_Application"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n\"name\": \"dv_Application\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/davinciApplications")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/davinciApplications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "dv_Application"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/davinciApplications',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "dv_Application"
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

url = "{{apiPath}}/v1/environments/{{envID}}/davinciApplications"

payload = json.dumps({
  "name": "dv_Application"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/davinciApplications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n"name": "dv_Application"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/davinciApplications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "dv_Application"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n\"name\": \"dv_Application\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/davinciApplications")!,timeoutInterval: Double.infinity)
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

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/davinciApplications/5d095e405e2354ecfdbea600f66e03be"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "flowPolicies": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/davinciApplications/5d095e405e2354ecfdbea600f66e03be/flowPolicies"
        },
        "davinciApplication.rotateKey": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/davinciApplications/5d095e405e2354ecfdbea600f66e03be/key"
        },
        "davinciApplication.rotateSecret": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/davinciApplications/5d095e405e2354ecfdbea600f66e03be/secret"
        }
    },
    "id": "5d095e405e2354ecfdbea600f66e03be",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "dv_Application",
    "apiKey": {
        "enabled": true,
        "value": "7d5352770ff"
    },
    "oauth": {
        "clientSecret": "f74bbc9fdf9",
        "scopes": [
            "openid",
            "profile"
        ],
        "grantTypes": [
            "authorizationCode"
        ]
    },
    "createdAt": "2024-06-14T23:19:41.152Z",
    "updatedAt": "2024-06-14T23:19:41.152Z"
}
```

---

---
title: Create DaVinci Application Flow Policies
description: Create a new PingOne DaVinci application flow policy resource for an application
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-application-flow-policies/create-davinci-application-flow-policies
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-application-flow-policies/create-davinci-application-flow-policies.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Application Flow Policies

##

Required permission:

* [davinci:create:flowPolicies](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-flowPolicies "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies
```

The `POST {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies` endpoint creates a new DaVinci application flow policy resource.

> **Collapse: Request Model**
>
> | Property                            | Type   | Required |
> | ----------------------------------- | ------ | -------- |
> | `name`                              | String | Required |
> | `flowDistributions`                 | Array  | Optional |
> | `flowDistributions.id`              | String | Optional |
> | `flowDistributions.weight`          | Number | Optional |
> | `flowDistributions.version`         | String | Optional |
> | `flowDistributions.successNodes`    | Array  | Optional |
> | `flowDistributions.successNodes.id` | Array  | Optional |
> | `status`                            | String | Optional |
> | `trigger`                           | Object | Optional |
> | `trigger.type`                      | String | Optional |
>
> Refer to [DaVinci Admin Application Flow Policies data model](index.html#davinci-admin-application-flow-policies-data-model) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Sample DaVinci Flow Policy",
    "flowDistributions": [
        {
            "id": "{{davinciFlowID}}",
            "version": 0,
            "weight": 100
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Sample DaVinci Flow Policy",
    "flowDistributions": [
        {
            "id": "{{davinciFlowID}}",
            "version": 0,
            "weight": 100
        }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Sample DaVinci Flow Policy""," + "\n" +
@"    ""flowDistributions"": [" + "\n" +
@"        {" + "\n" +
@"            ""id"": ""{{davinciFlowID}}""," + "\n" +
@"            ""version"": 0," + "\n" +
@"            ""weight"": 100" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Sample DaVinci Flow Policy",
    "flowDistributions": [
        {
            "id": "{{davinciFlowID}}",
            "version": 0,
            "weight": 100
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
POST /v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Sample DaVinci Flow Policy",
    "flowDistributions": [
        {
            "id": "{{davinciFlowID}}",
            "version": 0,
            "weight": 100
        }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Sample DaVinci Flow Policy\",\n    \"flowDistributions\": [\n        {\n            \"id\": \"{{davinciFlowID}}\",\n            \"version\": 0,\n            \"weight\": 100\n        }\n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Sample DaVinci Flow Policy",
    "flowDistributions": [
      {
        "id": "{{davinciFlowID}}",
        "version": 0,
        "weight": 100
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Sample DaVinci Flow Policy",
    "flowDistributions": [
      {
        "id": "{{davinciFlowID}}",
        "version": 0,
        "weight": 100
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

url = "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies"

payload = json.dumps({
  "name": "Sample DaVinci Flow Policy",
  "flowDistributions": [
    {
      "id": "{{davinciFlowID}}",
      "version": 0,
      "weight": 100
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Sample DaVinci Flow Policy",\n    "flowDistributions": [\n        {\n            "id": "{{davinciFlowID}}",\n            "version": 0,\n            "weight": 100\n        }\n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Sample DaVinci Flow Policy",
  "flowDistributions": [
    {
      "id": "{{davinciFlowID}}",
      "version": 0,
      "weight": 100
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Sample DaVinci Flow Policy\",\n    \"flowDistributions\": [\n        {\n            \"id\": \"{{davinciFlowID}}\",\n            \"version\": 0,\n            \"weight\": 100\n        }\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies")!,timeoutInterval: Double.infinity)
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

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/davinciApplications/c529ef171357b2a41faf939f47bf0ff7/flowPolicies/f56e33bb4eb1e05a1de5db5282aacbf1"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "f56e33bb4eb1e05a1de5db5282aacbf1",
    "name": "Sample DaVinci Flow Policy",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "status": "enabled",
    "flowDistributions": [
        {
            "id": "a79d1931573009379f0691befa538d97",
            "version": 0,
            "weight": 100
        }
    ],
    "createdAt": "2024-06-17T16:08:04.224Z",
    "updatedAt": "2024-06-17T16:08:04.224Z"
}
```

---

---
title: Create DaVinci Connector Instance
description: Create a new PingOne DaVinci connector instance resource in the specified environment
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connections/create-connection
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connections/create-connection.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Connector Instance

##

Required permission:

* [davinci:create:connections](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-connections "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/connectorInstances
```

The `POST {{apiPath}}/v1/environments/{{envID}}/connectorInstances` creates a new connector instance resource in the specified environment.

> **Collapse: Request Model**
>
> | Property       | Type   | Required |
> | -------------- | ------ | -------- |
> | `connector`    | Object | Required |
> | `connector.id` | String | Required |
> | `name`         | String | Required |
> | `properties`   | Object | Optional |
>
> Refer to the [DaVinci admin connector instances data model](index.html) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "API_HTTP_Connection",
    "connector": {
        "id": "httpConnector"
    }
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/connectorInstances' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "API_HTTP_Connection",
    "connector": {
        "id": "httpConnector"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/connectorInstances")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""API_HTTP_Connection""," + "\n" +
@"    ""connector"": {" + "\n" +
@"        ""id"": ""httpConnector""" + "\n" +
@"    }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/connectorInstances"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "API_HTTP_Connection",
    "connector": {
        "id": "httpConnector"
    }
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
POST /v1/environments/{{envID}}/connectorInstances HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "API_HTTP_Connection",
    "connector": {
        "id": "httpConnector"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"API_HTTP_Connection\",\n    \"connector\": {\n        \"id\": \"httpConnector\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/connectorInstances")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/connectorInstances",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "API_HTTP_Connection",
    "connector": {
      "id": "httpConnector"
    }
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/connectorInstances',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "API_HTTP_Connection",
    "connector": {
      "id": "httpConnector"
    }
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

url = "{{apiPath}}/v1/environments/{{envID}}/connectorInstances"

payload = json.dumps({
  "name": "API_HTTP_Connection",
  "connector": {
    "id": "httpConnector"
  }
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/connectorInstances');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "API_HTTP_Connection",\n    "connector": {\n        "id": "httpConnector"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/connectorInstances")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "API_HTTP_Connection",
  "connector": {
    "id": "httpConnector"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"API_HTTP_Connection\",\n    \"connector\": {\n        \"id\": \"httpConnector\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/connectorInstances")!,timeoutInterval: Double.infinity)
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

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/connectorInstances/e8b26b2703ce91678e768fdb048a4b51"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "connectorInstance.clone": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/connectorInstances/e8b26b2703ce91678e768fdb048a4b51"
        }
    },
    "id": "e8b26b2703ce91678e768fdb048a4b51",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "connector": {
        "id": "httpConnector"
    },
    "name": "API_HTTP_Connection",
    "createdAt": "2024-04-19T22:27:51.226Z",
    "updatedAt": "2024-04-19T22:27:51.226Z"
}
```

---

---
title: Create DaVinci Flow
description: Create a new PingOne DaVinci flow in the specified environment
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flows/create-flow
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flows/create-flow.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Flow

##

Required permission:

* [davinci:create:dvFlows](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-dvFlows "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/flows
```

The `POST {{apiPath}}/v1/environments/{{envID}}/flows` endpoint when used with a `Content-Type` header value of `application/json` creates a new DaVinci flow.

> **Collapse: Request Model**
>
> Refer to the [DaVinci Admin Flows data model](index.html) for full property descriptions.
>
> | Property           | Type           | Required |
> | ------------------ | -------------- | -------- |
> | `color`            | String         | Optional |
> | `connectors`       | Array\[object] | Optional |
> | `connectors.id`    | String         | Optional |
> | `currentVersion`   | Integer        | Optional |
> | `description`      | String         | Optional |
> | `enabled`          | Boolean        | Optional |
> | `graphData`        | Object         | Optional |
> | `inputSchema`      | Array\[object] | Optional |
> | `name`             | String         | Required |
> | `outputSchema`     | Object         | Optional |
> | `publishedVersion` | Integer        | Optional |
> | `settings`         | Object         | Optional |
> | `trigger`          | Object         | Optional |
> | `trigger.type`     | String         | Optional |
>
> **Flow settings properties**
>
> The following table lists the supported flow settings properties that can be used in the `settings` property.
>
> | Property                          | Type    | Required |
> | --------------------------------- | ------- | -------- |
> | `csp`                             | String  | Optional |
> | `css`                             | String  | Optional |
> | `cssLinks`                        | Array   | Optional |
> | `customErrorScreenBrandLogoUrl`   | String  | Optional |
> | `customErrorShowFooter`           | Boolean | Optional |
> | `customFaviconLink`               | String  | Optional |
> | `customLogoUrlSelection`          | String  | Optional |
> | `customTitle`                     | String  | Optional |
> | `doNotSubstituteUnreplacedFields` | Boolean | Optional |
> | `flowHttpTimeoutInSeconds`        | Number  | Optional |
> | `flowTimeoutInSeconds`            | Number  | Optional |
> | `intermediateLoadingScreenCss`    | String  | Optional |
> | `intermediateLoadingScreenHtml`   | String  | Optional |
> | `jsLinks`                         | Array   | Optional |
> | `logLevel`                        | String  | Optional |
> | `pingOneFlow`                     | Boolean | Optional |
> | `requireAuthenticationToInitiate` | Boolean | Optional |
> | `scrubSensitiveInfo`              | Boolean | Optional |
> | `sensitiveInfoFields`             | Array   | Optional |
> | `useCsp`                          | Boolean | Optional |
> | `useCustomCss`                    | Boolean | Optional |
> | `useCustomScript`                 | Boolean | Optional |
> | `useIntermediateLoadingScreen`    | Boolean | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "DaV-Flow_{{$timestamp}}",
    "description": "This is a demo flow",
    "color": "#00FF00",
    "graphData": {
        "elements": {
            "nodes": [
                {
                    "data": {
                        "id": "8bnj41592a",
                        "nodeType": "CONNECTION",
                        "connectionId": "94141bf2f1b9b59a5f5365ff135e02bb",
                        "connectorId": "pingOneSSOConnector",
                        "name": "PingOne",
                        "label": "PingOne",
                        "status": "configured",
                        "capabilityName": "userLookup",
                        "type": "action",
                        "properties": {
                            "additionalUserProperties": {
                                "value": []
                            },
                            "username": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            },
                            "population": {
                                "value": "c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418"
                            },
                            "userIdentifierForFindUser": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            }
                        }
                    },
                    "position": {
                        "x": 420,
                        "y": 360
                    },
                    "group": "nodes",
                    "removed": false,
                    "selected": false,
                    "selectable": true,
                    "locked": false,
                    "grabbable": true,
                    "pannable": false,
                    "classes": ""
                }
            ]
        },
        "data": {},
        "zoomingEnabled": true,
        "userZoomingEnabled": true,
        "zoom": 1,
        "minZoom": 1e-50,
        "maxZoom": 1e+50,
        "panningEnabled": true,
        "userPanningEnabled": true,
        "pan": {
            "x": 0,
            "y": 0
        },
        "boxSelectionEnabled": true,
        "renderer": {
            "name": "null"
        }
    },
    "settings": {
        "csp": "worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';",
        "intermediateLoadingScreenCSS": "",
        "intermediateLoadingScreenHTML": "",
        "logLevel": 2
        // "pingOneFlow": true
    },
    "inputSchema": [
        {
            "description": "",
            "preferredControlType": "textField",
            "preferredDataType": "object",
            "propertyName": "flowParameters",
            "required": false
        }
    ],
    "outputSchema": {
        "output": {
            "type": "object",
            "properties": {},
            "additionalProperties": true
        }
    },
    "trigger": {
        "type": "AUTHENTICATION"
    }
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/flows' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "DaV-Flow_{{$timestamp}}",
    "description": "This is a demo flow",
    "color": "#00FF00",
    "graphData": {
        "elements": {
            "nodes": [
                {
                    "data": {
                        "id": "8bnj41592a",
                        "nodeType": "CONNECTION",
                        "connectionId": "94141bf2f1b9b59a5f5365ff135e02bb",
                        "connectorId": "pingOneSSOConnector",
                        "name": "PingOne",
                        "label": "PingOne",
                        "status": "configured",
                        "capabilityName": "userLookup",
                        "type": "action",
                        "properties": {
                            "additionalUserProperties": {
                                "value": []
                            },
                            "username": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            },
                            "population": {
                                "value": "c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418"
                            },
                            "userIdentifierForFindUser": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            }
                        }
                    },
                    "position": {
                        "x": 420,
                        "y": 360
                    },
                    "group": "nodes",
                    "removed": false,
                    "selected": false,
                    "selectable": true,
                    "locked": false,
                    "grabbable": true,
                    "pannable": false,
                    "classes": ""
                }
            ]
        },
        "data": {},
        "zoomingEnabled": true,
        "userZoomingEnabled": true,
        "zoom": 1,
        "minZoom": 1e-50,
        "maxZoom": 1e+50,
        "panningEnabled": true,
        "userPanningEnabled": true,
        "pan": {
            "x": 0,
            "y": 0
        },
        "boxSelectionEnabled": true,
        "renderer": {
            "name": "null"
        }
    },
    "settings": {
        "csp": "worker-src '\''self'\'' blob:; script-src '\''self'\'' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com '\''unsafe-inline'\'' '\''unsafe-eval'\'';",
        "intermediateLoadingScreenCSS": "",
        "intermediateLoadingScreenHTML": "",
        "logLevel": 2
        // "pingOneFlow": true
    },
    "inputSchema": [
        {
            "description": "",
            "preferredControlType": "textField",
            "preferredDataType": "object",
            "propertyName": "flowParameters",
            "required": false
        }
    ],
    "outputSchema": {
        "output": {
            "type": "object",
            "properties": {},
            "additionalProperties": true
        }
    },
    "trigger": {
        "type": "AUTHENTICATION"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/flows")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""DaV-Flow_{{$timestamp}}""," + "\n" +
@"    ""description"": ""This is a demo flow""," + "\n" +
@"    ""color"": ""#00FF00""," + "\n" +
@"    ""graphData"": {" + "\n" +
@"        ""elements"": {" + "\n" +
@"            ""nodes"": [" + "\n" +
@"                {" + "\n" +
@"                    ""data"": {" + "\n" +
@"                        ""id"": ""8bnj41592a""," + "\n" +
@"                        ""nodeType"": ""CONNECTION""," + "\n" +
@"                        ""connectionId"": ""94141bf2f1b9b59a5f5365ff135e02bb""," + "\n" +
@"                        ""connectorId"": ""pingOneSSOConnector""," + "\n" +
@"                        ""name"": ""PingOne""," + "\n" +
@"                        ""label"": ""PingOne""," + "\n" +
@"                        ""status"": ""configured""," + "\n" +
@"                        ""capabilityName"": ""userLookup""," + "\n" +
@"                        ""type"": ""action""," + "\n" +
@"                        ""properties"": {" + "\n" +
@"                            ""additionalUserProperties"": {" + "\n" +
@"                                ""value"": []" + "\n" +
@"                            }," + "\n" +
@"                            ""username"": {" + "\n" +
@"                                ""value"": ""[\n  {\n    \""children\"": [\n      {\n        \""text\"": \""5282e30d-6e05-499c-ae68-0069fba776f1\""\n      }\n    ]\n  }\n]""" + "\n" +
@"                            }," + "\n" +
@"                            ""population"": {" + "\n" +
@"                                ""value"": ""c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418""" + "\n" +
@"                            }," + "\n" +
@"                            ""userIdentifierForFindUser"": {" + "\n" +
@"                                ""value"": ""[\n  {\n    \""children\"": [\n      {\n        \""text\"": \""5282e30d-6e05-499c-ae68-0069fba776f1\""\n      }\n    ]\n  }\n]""" + "\n" +
@"                            }" + "\n" +
@"                        }" + "\n" +
@"                    }," + "\n" +
@"                    ""position"": {" + "\n" +
@"                        ""x"": 420," + "\n" +
@"                        ""y"": 360" + "\n" +
@"                    }," + "\n" +
@"                    ""group"": ""nodes""," + "\n" +
@"                    ""removed"": false," + "\n" +
@"                    ""selected"": false," + "\n" +
@"                    ""selectable"": true," + "\n" +
@"                    ""locked"": false," + "\n" +
@"                    ""grabbable"": true," + "\n" +
@"                    ""pannable"": false," + "\n" +
@"                    ""classes"": """"" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""data"": {}," + "\n" +
@"        ""zoomingEnabled"": true," + "\n" +
@"        ""userZoomingEnabled"": true," + "\n" +
@"        ""zoom"": 1," + "\n" +
@"        ""minZoom"": 1e-50," + "\n" +
@"        ""maxZoom"": 1e+50," + "\n" +
@"        ""panningEnabled"": true," + "\n" +
@"        ""userPanningEnabled"": true," + "\n" +
@"        ""pan"": {" + "\n" +
@"            ""x"": 0," + "\n" +
@"            ""y"": 0" + "\n" +
@"        }," + "\n" +
@"        ""boxSelectionEnabled"": true," + "\n" +
@"        ""renderer"": {" + "\n" +
@"            ""name"": ""null""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""settings"": {" + "\n" +
@"        ""csp"": ""worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';""," + "\n" +
@"        ""intermediateLoadingScreenCSS"": """"," + "\n" +
@"        ""intermediateLoadingScreenHTML"": """"," + "\n" +
@"        ""logLevel"": 2" + "\n" +
@"        // ""pingOneFlow"": true" + "\n" +
@"    }," + "\n" +
@"    ""inputSchema"": [" + "\n" +
@"        {" + "\n" +
@"            ""description"": """"," + "\n" +
@"            ""preferredControlType"": ""textField""," + "\n" +
@"            ""preferredDataType"": ""object""," + "\n" +
@"            ""propertyName"": ""flowParameters""," + "\n" +
@"            ""required"": false" + "\n" +
@"        }" + "\n" +
@"    ]," + "\n" +
@"    ""outputSchema"": {" + "\n" +
@"        ""output"": {" + "\n" +
@"            ""type"": ""object""," + "\n" +
@"            ""properties"": {}," + "\n" +
@"            ""additionalProperties"": true" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""trigger"": {" + "\n" +
@"        ""type"": ""AUTHENTICATION""" + "\n" +
@"    }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/flows"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "DaV-Flow_{{$timestamp}}",
    "description": "This is a demo flow",
    "color": "#00FF00",
    "graphData": {
        "elements": {
            "nodes": [
                {
                    "data": {
                        "id": "8bnj41592a",
                        "nodeType": "CONNECTION",
                        "connectionId": "94141bf2f1b9b59a5f5365ff135e02bb",
                        "connectorId": "pingOneSSOConnector",
                        "name": "PingOne",
                        "label": "PingOne",
                        "status": "configured",
                        "capabilityName": "userLookup",
                        "type": "action",
                        "properties": {
                            "additionalUserProperties": {
                                "value": []
                            },
                            "username": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            },
                            "population": {
                                "value": "c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418"
                            },
                            "userIdentifierForFindUser": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            }
                        }
                    },
                    "position": {
                        "x": 420,
                        "y": 360
                    },
                    "group": "nodes",
                    "removed": false,
                    "selected": false,
                    "selectable": true,
                    "locked": false,
                    "grabbable": true,
                    "pannable": false,
                    "classes": ""
                }
            ]
        },
        "data": {},
        "zoomingEnabled": true,
        "userZoomingEnabled": true,
        "zoom": 1,
        "minZoom": 1e-50,
        "maxZoom": 1e+50,
        "panningEnabled": true,
        "userPanningEnabled": true,
        "pan": {
            "x": 0,
            "y": 0
        },
        "boxSelectionEnabled": true,
        "renderer": {
            "name": "null"
        }
    },
    "settings": {
        "csp": "worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';",
        "intermediateLoadingScreenCSS": "",
        "intermediateLoadingScreenHTML": "",
        "logLevel": 2
        // "pingOneFlow": true
    },
    "inputSchema": [
        {
            "description": "",
            "preferredControlType": "textField",
            "preferredDataType": "object",
            "propertyName": "flowParameters",
            "required": false
        }
    ],
    "outputSchema": {
        "output": {
            "type": "object",
            "properties": {},
            "additionalProperties": true
        }
    },
    "trigger": {
        "type": "AUTHENTICATION"
    }
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
POST /v1/environments/{{envID}}/flows HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "DaV-Flow_{{$timestamp}}",
    "description": "This is a demo flow",
    "color": "#00FF00",
    "graphData": {
        "elements": {
            "nodes": [
                {
                    "data": {
                        "id": "8bnj41592a",
                        "nodeType": "CONNECTION",
                        "connectionId": "94141bf2f1b9b59a5f5365ff135e02bb",
                        "connectorId": "pingOneSSOConnector",
                        "name": "PingOne",
                        "label": "PingOne",
                        "status": "configured",
                        "capabilityName": "userLookup",
                        "type": "action",
                        "properties": {
                            "additionalUserProperties": {
                                "value": []
                            },
                            "username": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            },
                            "population": {
                                "value": "c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418"
                            },
                            "userIdentifierForFindUser": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            }
                        }
                    },
                    "position": {
                        "x": 420,
                        "y": 360
                    },
                    "group": "nodes",
                    "removed": false,
                    "selected": false,
                    "selectable": true,
                    "locked": false,
                    "grabbable": true,
                    "pannable": false,
                    "classes": ""
                }
            ]
        },
        "data": {},
        "zoomingEnabled": true,
        "userZoomingEnabled": true,
        "zoom": 1,
        "minZoom": 1e-50,
        "maxZoom": 1e+50,
        "panningEnabled": true,
        "userPanningEnabled": true,
        "pan": {
            "x": 0,
            "y": 0
        },
        "boxSelectionEnabled": true,
        "renderer": {
            "name": "null"
        }
    },
    "settings": {
        "csp": "worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';",
        "intermediateLoadingScreenCSS": "",
        "intermediateLoadingScreenHTML": "",
        "logLevel": 2
        // "pingOneFlow": true
    },
    "inputSchema": [
        {
            "description": "",
            "preferredControlType": "textField",
            "preferredDataType": "object",
            "propertyName": "flowParameters",
            "required": false
        }
    ],
    "outputSchema": {
        "output": {
            "type": "object",
            "properties": {},
            "additionalProperties": true
        }
    },
    "trigger": {
        "type": "AUTHENTICATION"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"DaV-Flow_{{$timestamp}}\",\n    \"description\": \"This is a demo flow\",\n    \"color\": \"#00FF00\",\n    \"graphData\": {\n        \"elements\": {\n            \"nodes\": [\n                {\n                    \"data\": {\n                        \"id\": \"8bnj41592a\",\n                        \"nodeType\": \"CONNECTION\",\n                        \"connectionId\": \"94141bf2f1b9b59a5f5365ff135e02bb\",\n                        \"connectorId\": \"pingOneSSOConnector\",\n                        \"name\": \"PingOne\",\n                        \"label\": \"PingOne\",\n                        \"status\": \"configured\",\n                        \"capabilityName\": \"userLookup\",\n                        \"type\": \"action\",\n                        \"properties\": {\n                            \"additionalUserProperties\": {\n                                \"value\": []\n                            },\n                            \"username\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            },\n                            \"population\": {\n                                \"value\": \"c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418\"\n                            },\n                            \"userIdentifierForFindUser\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            }\n                        }\n                    },\n                    \"position\": {\n                        \"x\": 420,\n                        \"y\": 360\n                    },\n                    \"group\": \"nodes\",\n                    \"removed\": false,\n                    \"selected\": false,\n                    \"selectable\": true,\n                    \"locked\": false,\n                    \"grabbable\": true,\n                    \"pannable\": false,\n                    \"classes\": \"\"\n                }\n            ]\n        },\n        \"data\": {},\n        \"zoomingEnabled\": true,\n        \"userZoomingEnabled\": true,\n        \"zoom\": 1,\n        \"minZoom\": 1e-50,\n        \"maxZoom\": 1e+50,\n        \"panningEnabled\": true,\n        \"userPanningEnabled\": true,\n        \"pan\": {\n            \"x\": 0,\n            \"y\": 0\n        },\n        \"boxSelectionEnabled\": true,\n        \"renderer\": {\n            \"name\": \"null\"\n        }\n    },\n    \"settings\": {\n        \"csp\": \"worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';\",\n        \"intermediateLoadingScreenCSS\": \"\",\n        \"intermediateLoadingScreenHTML\": \"\",\n        \"logLevel\": 2\n        // \"pingOneFlow\": true\n    },\n    \"inputSchema\": [\n        {\n            \"description\": \"\",\n            \"preferredControlType\": \"textField\",\n            \"preferredDataType\": \"object\",\n            \"propertyName\": \"flowParameters\",\n            \"required\": false\n        }\n    ],\n    \"outputSchema\": {\n        \"output\": {\n            \"type\": \"object\",\n            \"properties\": {},\n            \"additionalProperties\": true\n        }\n    },\n    \"trigger\": {\n        \"type\": \"AUTHENTICATION\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/flows")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/flows",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": "{\n    \"name\": \"DaV-Flow_{{$timestamp}}\",\n    \"description\": \"This is a demo flow\",\n    \"color\": \"#00FF00\",\n    \"graphData\": {\n        \"elements\": {\n            \"nodes\": [\n                {\n                    \"data\": {\n                        \"id\": \"8bnj41592a\",\n                        \"nodeType\": \"CONNECTION\",\n                        \"connectionId\": \"94141bf2f1b9b59a5f5365ff135e02bb\",\n                        \"connectorId\": \"pingOneSSOConnector\",\n                        \"name\": \"PingOne\",\n                        \"label\": \"PingOne\",\n                        \"status\": \"configured\",\n                        \"capabilityName\": \"userLookup\",\n                        \"type\": \"action\",\n                        \"properties\": {\n                            \"additionalUserProperties\": {\n                                \"value\": []\n                            },\n                            \"username\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            },\n                            \"population\": {\n                                \"value\": \"c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418\"\n                            },\n                            \"userIdentifierForFindUser\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            }\n                        }\n                    },\n                    \"position\": {\n                        \"x\": 420,\n                        \"y\": 360\n                    },\n                    \"group\": \"nodes\",\n                    \"removed\": false,\n                    \"selected\": false,\n                    \"selectable\": true,\n                    \"locked\": false,\n                    \"grabbable\": true,\n                    \"pannable\": false,\n                    \"classes\": \"\"\n                }\n            ]\n        },\n        \"data\": {},\n        \"zoomingEnabled\": true,\n        \"userZoomingEnabled\": true,\n        \"zoom\": 1,\n        \"minZoom\": 1e-50,\n        \"maxZoom\": 1e+50,\n        \"panningEnabled\": true,\n        \"userPanningEnabled\": true,\n        \"pan\": {\n            \"x\": 0,\n            \"y\": 0\n        },\n        \"boxSelectionEnabled\": true,\n        \"renderer\": {\n            \"name\": \"null\"\n        }\n    },\n    \"settings\": {\n        \"csp\": \"worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';\",\n        \"intermediateLoadingScreenCSS\": \"\",\n        \"intermediateLoadingScreenHTML\": \"\",\n        \"logLevel\": 2\n        // \"pingOneFlow\": true\n    },\n    \"inputSchema\": [\n        {\n            \"description\": \"\",\n            \"preferredControlType\": \"textField\",\n            \"preferredDataType\": \"object\",\n            \"propertyName\": \"flowParameters\",\n            \"required\": false\n        }\n    ],\n    \"outputSchema\": {\n        \"output\": {\n            \"type\": \"object\",\n            \"properties\": {},\n            \"additionalProperties\": true\n        }\n    },\n    \"trigger\": {\n        \"type\": \"AUTHENTICATION\"\n    }\n}",
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/flows',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: '{\n    "name": "DaV-Flow_{{$timestamp}}",\n    "description": "This is a demo flow",\n    "color": "#00FF00",\n    "graphData": {\n        "elements": {\n            "nodes": [\n                {\n                    "data": {\n                        "id": "8bnj41592a",\n                        "nodeType": "CONNECTION",\n                        "connectionId": "94141bf2f1b9b59a5f5365ff135e02bb",\n                        "connectorId": "pingOneSSOConnector",\n                        "name": "PingOne",\n                        "label": "PingOne",\n                        "status": "configured",\n                        "capabilityName": "userLookup",\n                        "type": "action",\n                        "properties": {\n                            "additionalUserProperties": {\n                                "value": []\n                            },\n                            "username": {\n                                "value": "[\\n  {\\n    \\"children\\": [\\n      {\\n        \\"text\\": \\"5282e30d-6e05-499c-ae68-0069fba776f1\\"\\n      }\\n    ]\\n  }\\n]"\n                            },\n                            "population": {\n                                "value": "c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418"\n                            },\n                            "userIdentifierForFindUser": {\n                                "value": "[\\n  {\\n    \\"children\\": [\\n      {\\n        \\"text\\": \\"5282e30d-6e05-499c-ae68-0069fba776f1\\"\\n      }\\n    ]\\n  }\\n]"\n                            }\n                        }\n                    },\n                    "position": {\n                        "x": 420,\n                        "y": 360\n                    },\n                    "group": "nodes",\n                    "removed": false,\n                    "selected": false,\n                    "selectable": true,\n                    "locked": false,\n                    "grabbable": true,\n                    "pannable": false,\n                    "classes": ""\n                }\n            ]\n        },\n        "data": {},\n        "zoomingEnabled": true,\n        "userZoomingEnabled": true,\n        "zoom": 1,\n        "minZoom": 1e-50,\n        "maxZoom": 1e+50,\n        "panningEnabled": true,\n        "userPanningEnabled": true,\n        "pan": {\n            "x": 0,\n            "y": 0\n        },\n        "boxSelectionEnabled": true,\n        "renderer": {\n            "name": "null"\n        }\n    },\n    "settings": {\n        "csp": "worker-src \'self\' blob:; script-src \'self\' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com \'unsafe-inline\' \'unsafe-eval\';",\n        "intermediateLoadingScreenCSS": "",\n        "intermediateLoadingScreenHTML": "",\n        "logLevel": 2\n        // "pingOneFlow": true\n    },\n    "inputSchema": [\n        {\n            "description": "",\n            "preferredControlType": "textField",\n            "preferredDataType": "object",\n            "propertyName": "flowParameters",\n            "required": false\n        }\n    ],\n    "outputSchema": {\n        "output": {\n            "type": "object",\n            "properties": {},\n            "additionalProperties": true\n        }\n    },\n    "trigger": {\n        "type": "AUTHENTICATION"\n    }\n}'

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/v1/environments/{{envID}}/flows"

payload = "{\n    \"name\": \"DaV-Flow_{{$timestamp}}\",\n    \"description\": \"This is a demo flow\",\n    \"color\": \"#00FF00\",\n    \"graphData\": {\n        \"elements\": {\n            \"nodes\": [\n                {\n                    \"data\": {\n                        \"id\": \"8bnj41592a\",\n                        \"nodeType\": \"CONNECTION\",\n                        \"connectionId\": \"94141bf2f1b9b59a5f5365ff135e02bb\",\n                        \"connectorId\": \"pingOneSSOConnector\",\n                        \"name\": \"PingOne\",\n                        \"label\": \"PingOne\",\n                        \"status\": \"configured\",\n                        \"capabilityName\": \"userLookup\",\n                        \"type\": \"action\",\n                        \"properties\": {\n                            \"additionalUserProperties\": {\n                                \"value\": []\n                            },\n                            \"username\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            },\n                            \"population\": {\n                                \"value\": \"c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418\"\n                            },\n                            \"userIdentifierForFindUser\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            }\n                        }\n                    },\n                    \"position\": {\n                        \"x\": 420,\n                        \"y\": 360\n                    },\n                    \"group\": \"nodes\",\n                    \"removed\": false,\n                    \"selected\": false,\n                    \"selectable\": true,\n                    \"locked\": false,\n                    \"grabbable\": true,\n                    \"pannable\": false,\n                    \"classes\": \"\"\n                }\n            ]\n        },\n        \"data\": {},\n        \"zoomingEnabled\": true,\n        \"userZoomingEnabled\": true,\n        \"zoom\": 1,\n        \"minZoom\": 1e-50,\n        \"maxZoom\": 1e+50,\n        \"panningEnabled\": true,\n        \"userPanningEnabled\": true,\n        \"pan\": {\n            \"x\": 0,\n            \"y\": 0\n        },\n        \"boxSelectionEnabled\": true,\n        \"renderer\": {\n            \"name\": \"null\"\n        }\n    },\n    \"settings\": {\n        \"csp\": \"worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';\",\n        \"intermediateLoadingScreenCSS\": \"\",\n        \"intermediateLoadingScreenHTML\": \"\",\n        \"logLevel\": 2\n        // \"pingOneFlow\": true\n    },\n    \"inputSchema\": [\n        {\n            \"description\": \"\",\n            \"preferredControlType\": \"textField\",\n            \"preferredDataType\": \"object\",\n            \"propertyName\": \"flowParameters\",\n            \"required\": false\n        }\n    ],\n    \"outputSchema\": {\n        \"output\": {\n            \"type\": \"object\",\n            \"properties\": {},\n            \"additionalProperties\": true\n        }\n    },\n    \"trigger\": {\n        \"type\": \"AUTHENTICATION\"\n    }\n}"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/flows');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "DaV-Flow_{{$timestamp}}",\n    "description": "This is a demo flow",\n    "color": "#00FF00",\n    "graphData": {\n        "elements": {\n            "nodes": [\n                {\n                    "data": {\n                        "id": "8bnj41592a",\n                        "nodeType": "CONNECTION",\n                        "connectionId": "94141bf2f1b9b59a5f5365ff135e02bb",\n                        "connectorId": "pingOneSSOConnector",\n                        "name": "PingOne",\n                        "label": "PingOne",\n                        "status": "configured",\n                        "capabilityName": "userLookup",\n                        "type": "action",\n                        "properties": {\n                            "additionalUserProperties": {\n                                "value": []\n                            },\n                            "username": {\n                                "value": "[\\n  {\\n    \\"children\\": [\\n      {\\n        \\"text\\": \\"5282e30d-6e05-499c-ae68-0069fba776f1\\"\\n      }\\n    ]\\n  }\\n]"\n                            },\n                            "population": {\n                                "value": "c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418"\n                            },\n                            "userIdentifierForFindUser": {\n                                "value": "[\\n  {\\n    \\"children\\": [\\n      {\\n        \\"text\\": \\"5282e30d-6e05-499c-ae68-0069fba776f1\\"\\n      }\\n    ]\\n  }\\n]"\n                            }\n                        }\n                    },\n                    "position": {\n                        "x": 420,\n                        "y": 360\n                    },\n                    "group": "nodes",\n                    "removed": false,\n                    "selected": false,\n                    "selectable": true,\n                    "locked": false,\n                    "grabbable": true,\n                    "pannable": false,\n                    "classes": ""\n                }\n            ]\n        },\n        "data": {},\n        "zoomingEnabled": true,\n        "userZoomingEnabled": true,\n        "zoom": 1,\n        "minZoom": 1e-50,\n        "maxZoom": 1e+50,\n        "panningEnabled": true,\n        "userPanningEnabled": true,\n        "pan": {\n            "x": 0,\n            "y": 0\n        },\n        "boxSelectionEnabled": true,\n        "renderer": {\n            "name": "null"\n        }\n    },\n    "settings": {\n        "csp": "worker-src \'self\' blob:; script-src \'self\' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com \'unsafe-inline\' \'unsafe-eval\';",\n        "intermediateLoadingScreenCSS": "",\n        "intermediateLoadingScreenHTML": "",\n        "logLevel": 2\n        // "pingOneFlow": true\n    },\n    "inputSchema": [\n        {\n            "description": "",\n            "preferredControlType": "textField",\n            "preferredDataType": "object",\n            "propertyName": "flowParameters",\n            "required": false\n        }\n    ],\n    "outputSchema": {\n        "output": {\n            "type": "object",\n            "properties": {},\n            "additionalProperties": true\n        }\n    },\n    "trigger": {\n        "type": "AUTHENTICATION"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/flows")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = "{\n    \"name\": \"DaV-Flow_{{\\$timestamp}}\",\n    \"description\": \"This is a demo flow\",\n    \"color\": \"\\#00FF00\",\n    \"graphData\": {\n        \"elements\": {\n            \"nodes\": [\n                {\n                    \"data\": {\n                        \"id\": \"8bnj41592a\",\n                        \"nodeType\": \"CONNECTION\",\n                        \"connectionId\": \"94141bf2f1b9b59a5f5365ff135e02bb\",\n                        \"connectorId\": \"pingOneSSOConnector\",\n                        \"name\": \"PingOne\",\n                        \"label\": \"PingOne\",\n                        \"status\": \"configured\",\n                        \"capabilityName\": \"userLookup\",\n                        \"type\": \"action\",\n                        \"properties\": {\n                            \"additionalUserProperties\": {\n                                \"value\": []\n                            },\n                            \"username\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            },\n                            \"population\": {\n                                \"value\": \"c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418\"\n                            },\n                            \"userIdentifierForFindUser\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            }\n                        }\n                    },\n                    \"position\": {\n                        \"x\": 420,\n                        \"y\": 360\n                    },\n                    \"group\": \"nodes\",\n                    \"removed\": false,\n                    \"selected\": false,\n                    \"selectable\": true,\n                    \"locked\": false,\n                    \"grabbable\": true,\n                    \"pannable\": false,\n                    \"classes\": \"\"\n                }\n            ]\n        },\n        \"data\": {},\n        \"zoomingEnabled\": true,\n        \"userZoomingEnabled\": true,\n        \"zoom\": 1,\n        \"minZoom\": 1e-50,\n        \"maxZoom\": 1e+50,\n        \"panningEnabled\": true,\n        \"userPanningEnabled\": true,\n        \"pan\": {\n            \"x\": 0,\n            \"y\": 0\n        },\n        \"boxSelectionEnabled\": true,\n        \"renderer\": {\n            \"name\": \"null\"\n        }\n    },\n    \"settings\": {\n        \"csp\": \"worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';\",\n        \"intermediateLoadingScreenCSS\": \"\",\n        \"intermediateLoadingScreenHTML\": \"\",\n        \"logLevel\": 2\n        // \"pingOneFlow\": true\n    },\n    \"inputSchema\": [\n        {\n            \"description\": \"\",\n            \"preferredControlType\": \"textField\",\n            \"preferredDataType\": \"object\",\n            \"propertyName\": \"flowParameters\",\n            \"required\": false\n        }\n    ],\n    \"outputSchema\": {\n        \"output\": {\n            \"type\": \"object\",\n            \"properties\": {},\n            \"additionalProperties\": true\n        }\n    },\n    \"trigger\": {\n        \"type\": \"AUTHENTICATION\"\n    }\n}"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"DaV-Flow_{{$timestamp}}\",\n    \"description\": \"This is a demo flow\",\n    \"color\": \"#00FF00\",\n    \"graphData\": {\n        \"elements\": {\n            \"nodes\": [\n                {\n                    \"data\": {\n                        \"id\": \"8bnj41592a\",\n                        \"nodeType\": \"CONNECTION\",\n                        \"connectionId\": \"94141bf2f1b9b59a5f5365ff135e02bb\",\n                        \"connectorId\": \"pingOneSSOConnector\",\n                        \"name\": \"PingOne\",\n                        \"label\": \"PingOne\",\n                        \"status\": \"configured\",\n                        \"capabilityName\": \"userLookup\",\n                        \"type\": \"action\",\n                        \"properties\": {\n                            \"additionalUserProperties\": {\n                                \"value\": []\n                            },\n                            \"username\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            },\n                            \"population\": {\n                                \"value\": \"c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418\"\n                            },\n                            \"userIdentifierForFindUser\": {\n                                \"value\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"5282e30d-6e05-499c-ae68-0069fba776f1\\\"\\n      }\\n    ]\\n  }\\n]\"\n                            }\n                        }\n                    },\n                    \"position\": {\n                        \"x\": 420,\n                        \"y\": 360\n                    },\n                    \"group\": \"nodes\",\n                    \"removed\": false,\n                    \"selected\": false,\n                    \"selectable\": true,\n                    \"locked\": false,\n                    \"grabbable\": true,\n                    \"pannable\": false,\n                    \"classes\": \"\"\n                }\n            ]\n        },\n        \"data\": {},\n        \"zoomingEnabled\": true,\n        \"userZoomingEnabled\": true,\n        \"zoom\": 1,\n        \"minZoom\": 1e-50,\n        \"maxZoom\": 1e+50,\n        \"panningEnabled\": true,\n        \"userPanningEnabled\": true,\n        \"pan\": {\n            \"x\": 0,\n            \"y\": 0\n        },\n        \"boxSelectionEnabled\": true,\n        \"renderer\": {\n            \"name\": \"null\"\n        }\n    },\n    \"settings\": {\n        \"csp\": \"worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';\",\n        \"intermediateLoadingScreenCSS\": \"\",\n        \"intermediateLoadingScreenHTML\": \"\",\n        \"logLevel\": 2\n        // \"pingOneFlow\": true\n    },\n    \"inputSchema\": [\n        {\n            \"description\": \"\",\n            \"preferredControlType\": \"textField\",\n            \"preferredDataType\": \"object\",\n            \"propertyName\": \"flowParameters\",\n            \"required\": false\n        }\n    ],\n    \"outputSchema\": {\n        \"output\": {\n            \"type\": \"object\",\n            \"properties\": {},\n            \"additionalProperties\": true\n        }\n    },\n    \"trigger\": {\n        \"type\": \"AUTHENTICATION\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/flows")!,timeoutInterval: Double.infinity)
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

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/8bb2d660716fe912d7b782b7ced66158"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "connectorInstances": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/connectorInstances"
        },
        "connectors": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/connectors"
        },
        "flow.deploy": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/8bb2d660716fe912d7b782b7ced66158"
        },
        "flow.clone": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/8bb2d660716fe912d7b782b7ced66158"
        },
        "flow.validate": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/8bb2d660716fe912d7b782b7ced66158"
        },
        "flow.enabled": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/8bb2d660716fe912d7b782b7ced66158/enabled"
        }
    },
    "id": "8bb2d660716fe912d7b782b7ced66158",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "DaV-Flow_1733959029",
    "description": "This is a demo flow",
    "enabled": true,
    "settings": {
        "csp": "worker-src 'self' blob:; script-src 'self' https://cdn.jsdelivr.net https://code.jquery.com https://devsdk.singularkey.com http://cdnjs.cloudflare.com 'unsafe-inline' 'unsafe-eval';",
        "intermediateLoadingScreenCSS": "",
        "intermediateLoadingScreenHTML": "",
        "logLevel": 2
    },
    "color": "#00FF00",
    "graphData": {
        "elements": {
            "nodes": [
                {
                    "data": {
                        "id": "8bnj41592a",
                        "nodeType": "CONNECTION",
                        "connectionId": "94141bf2f1b9b59a5f5365ff135e02bb",
                        "connectorId": "pingOneSSOConnector",
                        "name": "PingOne",
                        "label": "PingOne",
                        "status": "configured",
                        "capabilityName": "userLookup",
                        "type": "action",
                        "properties": {
                            "additionalUserProperties": {
                                "value": []
                            },
                            "username": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            },
                            "population": {
                                "value": "c9f3fb3f-11e9-4eb0-b4ba-9fb7789a8418"
                            },
                            "userIdentifierForFindUser": {
                                "value": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"5282e30d-6e05-499c-ae68-0069fba776f1\"\n      }\n    ]\n  }\n]"
                            }
                        }
                    },
                    "position": {
                        "x": 420,
                        "y": 360
                    },
                    "group": "nodes",
                    "removed": false,
                    "selected": false,
                    "selectable": true,
                    "locked": false,
                    "grabbable": true,
                    "pannable": false,
                    "classes": ""
                }
            ]
        },
        "data": {},
        "zoomingEnabled": true,
        "userZoomingEnabled": true,
        "zoom": 1,
        "minZoom": 1e-50,
        "maxZoom": 1e+50,
        "panningEnabled": true,
        "userPanningEnabled": true,
        "pan": {
            "x": 0,
            "y": 0
        },
        "boxSelectionEnabled": true,
        "renderer": {
            "name": "null"
        }
    },
    "inputSchema": [
        {
            "description": "",
            "preferredControlType": "textField",
            "preferredDataType": "object",
            "propertyName": "flowParameters",
            "required": false
        }
    ],
    "outputSchema": {
        "output": {
            "type": "object",
            "properties": {},
            "additionalProperties": true
        }
    },
    "trigger": {
        "type": "AUTHENTICATION"
    },
    "createdAt": "2024-12-11T23:17:09.121Z",
    "updatedAt": "2024-12-11T23:17:09.121Z"
}
```

---

---
title: Create DaVinci UI Template
description: Create a new PingOne DaVinci UI template resource for branding flows
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-ui-templates/create-davinci-template
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-ui-templates/create-davinci-template.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci UI Template

##

Required permission:

* [davinci:create:uiTemplates](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-uiTemplates "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/uiTemplates
```

The `POST {{apiPath}}/v1/environments/{{envID}}/uiTemplates` endpoint creates a new DaVinci UI template resource.

> **Collapse: Request Model**
>
> | Property                          | Type   | Required |
> | --------------------------------- | ------ | -------- |
> | `description`                     | String | Optional |
> | `name`                            | String | Required |
> | `inputSchema`                     | String | Optional |
> | `outputSchema`                    | String | Optional |
> | `script`                          | String | Optional |
> | `style`                           | String | Optional |
> | `template`                        | String | Optional |
> | `validationRules`                 | Array  | Optional |
> | `validationRules.propertyName`    | String | Required |
> | `validationRules.rules`           | Array  | Required |
> | `validationRules.rules.ruleName`  | String | Required |
> | `validationRules.rules.message`   | String | Optional |
> | `validationRules.rules.attribute` | String | Optional |
> | `validationRules.rules.pattern`   | String | Optional |
>
> Refer to [DaVinci Admin UI Templates data model](index.html#davinci-admin-ui-templates-data-model) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
  "name": "DaVinci_UITemplate No 3",
  "description": "A DaVinci UI Template",
  "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
    "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
    "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
    "script": "console.log()",
    "style": "p {}",
    "validationRules": [
        {
            "propertyName": "Hello",
            "rules": [
                {
                    "ruleName": "presence",
                    "message": "There"
                }
            ]
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/uiTemplates' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "name": "DaVinci_UITemplate No 3",
  "description": "A DaVinci UI Template",
  "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
    "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
    "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
    "script": "console.log()",
    "style": "p {}",
    "validationRules": [
        {
            "propertyName": "Hello",
            "rules": [
                {
                    "ruleName": "presence",
                    "message": "There"
                }
            ]
        }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/uiTemplates")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""name"": ""DaVinci_UITemplate No 3""," + "\n" +
@"  ""description"": ""A DaVinci UI Template""," + "\n" +
@"  ""inputSchema"": ""{\n\t\""type\"": \""object\"",\n\t\""properties\"": {\n\t\t\""first\"": \""val1\"",\n\t\t\""second\"": \""val2\""\n\t}\n}""," + "\n" +
@"    ""outputSchema"": ""{\n\t\""type\"": \""object\"",\n\t\""properties\"": {\n\t\t\""first\"": \""val2\"",\n\t\t\""second\"": \""val1\""\n\t}\n}""," + "\n" +
@"    ""template"": ""[\n  {\n    \""children\"": [\n      {\n        \""text\"": \""\""\n      }\n    ]\n  }\n]""," + "\n" +
@"    ""script"": ""console.log()""," + "\n" +
@"    ""style"": ""p {}""," + "\n" +
@"    ""validationRules"": [" + "\n" +
@"        {" + "\n" +
@"            ""propertyName"": ""Hello""," + "\n" +
@"            ""rules"": [" + "\n" +
@"                {" + "\n" +
@"                    ""ruleName"": ""presence""," + "\n" +
@"                    ""message"": ""There""" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        }" + "\n" +
@"    ]" + "\n" +
@"}" + "\n" +
@"";
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

  url := "{{apiPath}}/v1/environments/{{envID}}/uiTemplates"
  method := "POST"

  payload := strings.NewReader(`{
  "name": "DaVinci_UITemplate No 3",
  "description": "A DaVinci UI Template",
  "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
    "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
    "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
    "script": "console.log()",
    "style": "p {}",
    "validationRules": [
        {
            "propertyName": "Hello",
            "rules": [
                {
                    "ruleName": "presence",
                    "message": "There"
                }
            ]
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
POST /v1/environments/{{envID}}/uiTemplates HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "DaVinci_UITemplate No 3",
  "description": "A DaVinci UI Template",
  "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
    "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
    "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
    "script": "console.log()",
    "style": "p {}",
    "validationRules": [
        {
            "propertyName": "Hello",
            "rules": [
                {
                    "ruleName": "presence",
                    "message": "There"
                }
            ]
        }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"DaVinci_UITemplate No 3\",\n  \"description\": \"A DaVinci UI Template\",\n  \"inputSchema\": \"{\\n\\t\\\"type\\\": \\\"object\\\",\\n\\t\\\"properties\\\": {\\n\\t\\t\\\"first\\\": \\\"val1\\\",\\n\\t\\t\\\"second\\\": \\\"val2\\\"\\n\\t}\\n}\",\n    \"outputSchema\": \"{\\n\\t\\\"type\\\": \\\"object\\\",\\n\\t\\\"properties\\\": {\\n\\t\\t\\\"first\\\": \\\"val2\\\",\\n\\t\\t\\\"second\\\": \\\"val1\\\"\\n\\t}\\n}\",\n    \"template\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"\\\"\\n      }\\n    ]\\n  }\\n]\",\n    \"script\": \"console.log()\",\n    \"style\": \"p {}\",\n    \"validationRules\": [\n        {\n            \"propertyName\": \"Hello\",\n            \"rules\": [\n                {\n                    \"ruleName\": \"presence\",\n                    \"message\": \"There\"\n                }\n            ]\n        }\n    ]\n}\n");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/uiTemplates")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/uiTemplates",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "DaVinci_UITemplate No 3",
    "description": "A DaVinci UI Template",
    "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
    "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
    "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
    "script": "console.log()",
    "style": "p {}",
    "validationRules": [
      {
        "propertyName": "Hello",
        "rules": [
          {
            "ruleName": "presence",
            "message": "There"
          }
        ]
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/uiTemplates',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "DaVinci_UITemplate No 3",
    "description": "A DaVinci UI Template",
    "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
    "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
    "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
    "script": "console.log()",
    "style": "p {}",
    "validationRules": [
      {
        "propertyName": "Hello",
        "rules": [
          {
            "ruleName": "presence",
            "message": "There"
          }
        ]
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

url = "{{apiPath}}/v1/environments/{{envID}}/uiTemplates"

payload = json.dumps({
  "name": "DaVinci_UITemplate No 3",
  "description": "A DaVinci UI Template",
  "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
  "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
  "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
  "script": "console.log()",
  "style": "p {}",
  "validationRules": [
    {
      "propertyName": "Hello",
      "rules": [
        {
          "ruleName": "presence",
          "message": "There"
        }
      ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/uiTemplates');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "name": "DaVinci_UITemplate No 3",\n  "description": "A DaVinci UI Template",\n  "inputSchema": "{\\n\\t\\"type\\": \\"object\\",\\n\\t\\"properties\\": {\\n\\t\\t\\"first\\": \\"val1\\",\\n\\t\\t\\"second\\": \\"val2\\"\\n\\t}\\n}",\n    "outputSchema": "{\\n\\t\\"type\\": \\"object\\",\\n\\t\\"properties\\": {\\n\\t\\t\\"first\\": \\"val2\\",\\n\\t\\t\\"second\\": \\"val1\\"\\n\\t}\\n}",\n    "template": "[\\n  {\\n    \\"children\\": [\\n      {\\n        \\"text\\": \\"\\"\\n      }\\n    ]\\n  }\\n]",\n    "script": "console.log()",\n    "style": "p {}",\n    "validationRules": [\n        {\n            "propertyName": "Hello",\n            "rules": [\n                {\n                    "ruleName": "presence",\n                    "message": "There"\n                }\n            ]\n        }\n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/uiTemplates")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "DaVinci_UITemplate No 3",
  "description": "A DaVinci UI Template",
  "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
  "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
  "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
  "script": "console.log()",
  "style": "p {}",
  "validationRules": [
    {
      "propertyName": "Hello",
      "rules": [
        {
          "ruleName": "presence",
          "message": "There"
        }
      ]
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"name\": \"DaVinci_UITemplate No 3\",\n  \"description\": \"A DaVinci UI Template\",\n  \"inputSchema\": \"{\\n\\t\\\"type\\\": \\\"object\\\",\\n\\t\\\"properties\\\": {\\n\\t\\t\\\"first\\\": \\\"val1\\\",\\n\\t\\t\\\"second\\\": \\\"val2\\\"\\n\\t}\\n}\",\n    \"outputSchema\": \"{\\n\\t\\\"type\\\": \\\"object\\\",\\n\\t\\\"properties\\\": {\\n\\t\\t\\\"first\\\": \\\"val2\\\",\\n\\t\\t\\\"second\\\": \\\"val1\\\"\\n\\t}\\n}\",\n    \"template\": \"[\\n  {\\n    \\\"children\\\": [\\n      {\\n        \\\"text\\\": \\\"\\\"\\n      }\\n    ]\\n  }\\n]\",\n    \"script\": \"console.log()\",\n    \"style\": \"p {}\",\n    \"validationRules\": [\n        {\n            \"propertyName\": \"Hello\",\n            \"rules\": [\n                {\n                    \"ruleName\": \"presence\",\n                    \"message\": \"There\"\n                }\n            ]\n        }\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/uiTemplates")!,timeoutInterval: Double.infinity)
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

201 Created

```json
{
    "_links": {
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/uiTemplates/b129691952dc8eae8eaec93268886a78"
        }
    },
    "id": "b129691952dc8eae8eaec93268886a78",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "DaVinci_UITemplate No 3",
    "description": "A DaVinci UI Template",
    "inputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val1\",\n\t\t\"second\": \"val2\"\n\t}\n}",
    "outputSchema": "{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"first\": \"val2\",\n\t\t\"second\": \"val1\"\n\t}\n}",
    "script": "console.log()",
    "style": "p {}",
    "template": "[\n  {\n    \"children\": [\n      {\n        \"text\": \"\"\n      }\n    ]\n  }\n]",
    "validationRules": [
        {
            "propertyName": "Hello",
            "rules": [
                {
                    "ruleName": "presence",
                    "message": "There"
                }
            ]
        }
    ],
    "createdAt": "2024-08-30T21:42:24.653Z"
}
```

---

---
title: Create DaVinci Variable
description: Create a new PingOne DaVinci variable with a name, data type, and context
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-variables/create-variable
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-variables/create-variable.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Variable

##

Required permission:

* [davinci:create:constructs](../../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-davinci-create-constructs "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/variables
```

The `POST {{apiPath}}/v1/environments/{{envID}}/variables` endpoint creates a new DaVinci variable resource. You must specify a `name`, `dataType`, and `context` for the variable.

> **Collapse: Request Model**
>
> | Property      | Type    | Required |
> | ------------- | ------- | -------- |
> | `context`     | String  | Required |
> | `dataType`    | String  | Required |
> | `displayName` | String  | Optional |
> | `flow`        | Object  | Optional |
> | `flow.id`     | String  | Optional |
> | `max`         | Integer | Optional |
> | `min`         | Integer | Optional |
> | `mutable`     | Boolean | Optional |
> | `name`        | String  | Required |
> | `value`       | String  | Optional |
>
> Refer to [DaVinci Admin Variables data model](index.html) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "continue",
    "dataType": "string",
    "context": "flowInstance",
    "mutable": true,
    "min": 0,
    "max": 2000
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/variables' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "continue",
    "dataType": "string",
    "context": "flowInstance",
    "mutable": true,
    "min": 0,
    "max": 2000
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/variables")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""continue""," + "\n" +
@"    ""dataType"": ""string""," + "\n" +
@"    ""context"": ""flowInstance""," + "\n" +
@"    ""mutable"": true," + "\n" +
@"    ""min"": 0," + "\n" +
@"    ""max"": 2000" + "\n" +
@"}                ";
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

  url := "{{apiPath}}/v1/environments/{{envID}}/variables"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "continue",
    "dataType": "string",
    "context": "flowInstance",
    "mutable": true,
    "min": 0,
    "max": 2000
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
POST /v1/environments/{{envID}}/variables HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "continue",
    "dataType": "string",
    "context": "flowInstance",
    "mutable": true,
    "min": 0,
    "max": 2000
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"continue\",\n    \"dataType\": \"string\",\n    \"context\": \"flowInstance\",\n    \"mutable\": true,\n    \"min\": 0,\n    \"max\": 2000\n}                ");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/variables")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/variables",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "continue",
    "dataType": "string",
    "context": "flowInstance",
    "mutable": true,
    "min": 0,
    "max": 2000
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/variables',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "continue",
    "dataType": "string",
    "context": "flowInstance",
    "mutable": true,
    "min": 0,
    "max": 2000
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

url = "{{apiPath}}/v1/environments/{{envID}}/variables"

payload = json.dumps({
  "name": "continue",
  "dataType": "string",
  "context": "flowInstance",
  "mutable": True,
  "min": 0,
  "max": 2000
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/variables');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "continue",\n    "dataType": "string",\n    "context": "flowInstance",\n    "mutable": true,\n    "min": 0,\n    "max": 2000\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/variables")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "continue",
  "dataType": "string",
  "context": "flowInstance",
  "mutable": true,
  "min": 0,
  "max": 2000
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"continue\",\n    \"dataType\": \"string\",\n    \"context\": \"flowInstance\",\n    \"mutable\": true,\n    \"min\": 0,\n    \"max\": 2000\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/variables")!,timeoutInterval: Double.infinity)
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

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/variables/90bd6871-58ff-455e-a48d-77923fd299cd"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "90bd6871-58ff-455e-a48d-77923fd299cd",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "continue",
    "dataType": "string",
    "context": "flowInstance",
    "mutable": true,
    "min": 0,
    "max": 2000,
    "createdAt": "2024-05-06T22:34:13.422Z",
    "updatedAt": "2024-05-06T22:34:13.422Z"
}
```

---

---
title: DaVinci Admin APIs
description: Lists the PingOne DaVinci Admin API services available through the PingOne API resource server for managing DaVinci flows, variables, connectors, and applications
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# DaVinci Admin APIs

The PingOne DaVinci Admin APIs provide access to DaVinci operations through the PingOne API resource server. These services are called using the `api.pingone.com` domain (or `api.pingone.ca`, `api.pingone.eu`, `api.pingone.com.au`, `api.pingone.sg`, and `api.pingone.asia` for other geographic domains) to manage DaVinci workflow configuration.

At this time, the following services are supported on the PingOne API resource server:

* [**DaVinci Admin Variables**](admin-variables/index.html)

  Endpoints for managing DaVinci variables and their context.

* [**DaVinci Admin Flows**](admin-flows/index.html)

  Endpoints for creating and managing DaVinci flows.

* [**DaVinci Admin Flow Versions**](admin-flow-versions/index.html)

  Endpoints for managing DaVinci flow versions.

* [**DaVinci Admin Connector Instances**](admin-connections/index.html)

  Endpoints for managing DaVinci connector instances, which provide access to DaVinci connector capabilities.

* [**DaVinci Admin Applications**](davinci-admin-applications/index.html)

  Endpoints for managing DaVinci applications.

* [**DaVinci Admin Application Flow Policies**](davinci-admin-application-flow-policies/index.html)

  Endpoints for managing DaVinci application flow policies.

* [**DaVinci Admin Connectors**](admin-connectors/index.html)

  Endpoints for managing DaVinci connectors.

* [**DaVinci Admin UI Templates**](admin-ui-templates/index.html)

  Endpoints for managing DaVinci UI templates.

---

---
title: DaVinci Admin Application Flow Policies
description: Describes the PingOne DaVinci Admin Application Flow Policies service for creating, reading, updating, and deleting policies that specify which flows run through an application
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-application-flow-policies/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-application-flow-policies/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-application-flow-policies-data-model: DaVinci Admin application flow policies data model properties
  davinci-admin-application-flow-policy-event-data-model: DaVinci Admin application flow policy event data model properties
  response-codes: Response codes
  davinci-application-flow-policy-errors: DaVinci application flow policy errors
---

# DaVinci Admin Application Flow Policies

The PingOne DaVinci Admin Application Flow Policies service provides endpoints to create, read, update, and delete DaVinci application flow policies. Application flow policies specify which flows are run through the application. A flow policy is an entity that points to one or more flows or versions of flows.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci Admin application flow policies data model properties

| Property                            | Type   | Required | Mutable   | Description                                                                                                           |
| ----------------------------------- | ------ | -------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| `createdAt`                         | Date   | N/A      | Read only | The time when the flow policy was created.                                                                            |
| `environment`                       | Object | N/A      | Read only | The DaVinci company ID (environment ID) object.                                                                       |
| `environment.id`                    | String | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID.                                                          |
| `id`                                | String | N/A      | Read only | The flow policy ID.                                                                                                   |
| `name`                              | String | Required | Mutable   | The flow policy name.                                                                                                 |
| `flowDistributions`                 | Array  | Optional | Immutable | An array of flow distribution properties that are a part of this flow policy.                                         |
| `flowDistributions.id`              | String | Optional | Immutable | The flow ID associated with this flow policy.                                                                         |
| `flowDistributions.weight`          | Number | Optional | Mutable   | The weight that is assigned to the current flow in the flow policy.                                                   |
| `flowDistributions.version`         | String | Optional | Mutable   | The version of the flow to be used in the flow policy.                                                                |
| `flowDistributions.successNodes`    | Array  | Optional | Mutable   | An array of node IDs in the flow that indicate a successful execution of the flow policy.                             |
| `flowDistributions.successNodes.id` | Array  | Optional | Mutable   | The node ID.                                                                                                          |
| `flowDistributions.ip`              | Array  | Optional | Mutable   | An array of IP addresses to create a whitelist of IP addresses from which flow executions can be performed.           |
| `status`                            | String | Optional | Mutable   | The status of the flow policy. Options are `Enabled` and `Disabled`.                                                  |
| `trigger`                           | Object | Optional | Immutable | The trigger associated with the flow.                                                                                 |
| `trigger.type`                      | String | Optional | Immutable | If the trigger type is set to `AUTHENTICATION`, you invoke the flow through PingOne OpenID Connect or SAML endpoints. |
| `updatedAt`                         | Date   | N/A      | Read only | The time when the flow policy was modified.                                                                           |

## DaVinci Admin application flow policy event data model properties

| Property           | Type   | Required | Mutable   | Description                                                  |
| ------------------ | ------ | -------- | --------- | ------------------------------------------------------------ |
| `environment`      | Object | N/A      | Read only | The environment object.                                      |
| `environment.id`   | String | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID. |
| `events`           | Object | N/A      | Read only | The DaVinci event object.                                    |
| `events.id`        | String | N/A      | Read only | The DaVinci event ID.                                        |
| `events.timestamp` | Date   | N/A      | Read only | A UTC timestamp that specifies when the event was logged.    |
| `flow`             | Object | N/A      | Read only | The DaVinci flow object.                                     |
| `flow.id`          | String | N/A      | Read only | The DaVinci flow ID.                                         |
| `flow.version`     | Number | N/A      | Read only | The DaVinci flow version number.                             |
| `totalCount`       | Number | N/A      | Read only | The total number of flow executions.                         |
| `successCount`     | Number | N/A      | Read only | The total count of success nodes reached in flow executions. |

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci application flow policy errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci application flow policy operations can return the following errors:

| HTTP status | Top‑level code     | Detail code                                                         | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | ------------------ | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/davinciApplications/{davinciApplicationID}/flowPolicies` or a `PUT /environments/{envID}/davinciApplications/{davinciApplicationID}/flowPolicies/{davinciAppFlowPolicyID}` request supplies a body that violates the data model: an omitted `flowDistributions` array, an omitted `name` on update, a flow distribution entry without an `id` or `version`, an empty `flowDistributions` array on create, an empty `successNodes` array, a blank `name`, a blank `trigger.subtype`, a blank success node ID, a `name` longer than 256 characters, a `trigger.type` longer than 50 characters, more than 100 `flowDistributions` entries, an unknown `status` value, a `name`, `status`, or `trigger.type` value that is not a string, a `name` that starts with an unsupported character or contains a `<` or a `${` sequence, a property inside a flow distribution entry that the entry schema does not allow, or a flow distribution or success node ID that contains characters outside its allowed set
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'flowDistributions'` with target `flowDistributions` when the create request omits `flowDistributions`. `must have required property 'name'` with target `name` when an update request omits `name`. `must have required property 'id'` or `must have required property 'version'` with the flow distribution entry path as the target, for example `flowDistributions.0`, when an entry omits either property. `must NOT have fewer than 1 items` with target `flowDistributions` when the create request supplies an empty `flowDistributions` array, and with the `successNodes` path as the target, for example `flowDistributions.0.successNodes`, for an empty `successNodes` array. `must not be empty or blank` for a blank `name`, a blank `trigger.subtype`, or a blank success node ID, for example with target `flowDistributions.0.successNodes.0.id`. `must NOT have more than 256 characters` for a `name` longer than 256 characters and `must NOT have more than 50 characters` for a `trigger.type` longer than 50 characters. `must NOT have more than 100 items` for more than 100 `flowDistributions` entries. `must be one of the values: enabled or disabled` for an unknown `status` value. `must NOT have additional properties` for a property inside a flow distribution entry that the entry schema does not allow. `must match pattern "<pattern>"`, where the pattern is the JSON schema pattern for the property, for a `name` that starts with an unsupported character or contains a `<` or a `${` sequence, or for a flow distribution or success node ID that contains characters outside its allowed set. `must be string` for a property of the wrong JSON type, for example with target `name`. |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER` or `INVALID_VALUE`                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET` all flow policies request supplies a `page`, `limit`, `filter`, or `expand` query parameter longer than 256 characters, a `GET` flow policy events request includes any query parameter, or a `DELETE` flow policy request includes any query parameter
>
> **Details:** For an overlong query parameter on a `GET` all flow policies request, detail code `INVALID_PARAMETER` with message `must NOT have more than 256 characters` and the overlong query parameter as the target. For a `GET` flow policy events request or a `DELETE` flow policy request that includes a query parameter, detail code `INVALID_VALUE` with message `must NOT have additional properties` and the rejected query parameter as the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST`, `PUT`, or `DELETE` request targets an application that is read-only, or a `POST` or `PUT` request includes a read-only flow in `flowDistributions`
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `The request violates a constraint imposed by the service.` No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT` request references flows that fail flow policy validation, for example a flow ID or flow version that does not exist, or a schedule-triggered policy that references more than one flow or a flow version that is not deployed
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `Flow validation failed. Please add valid flows.` No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT` request includes flows whose trigger types do not resolve to a single trigger type, for example a PingOne authentication flow combined with a non-PingOne flow, or a flow reference that does not exist
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `This policy does not allow flows created with Ping and non-Ping triggers to be part of the same policy.` No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT` request includes a `trigger.configuration` object for a policy whose flows do not resolve to the `AUTHENTICATION` trigger type
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `Non-PingOne Flow Policies do not support the configuration property.` No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT` request includes flows that share a trigger type but resolve to different trigger subtypes
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `This policy does not allow flows with different trigger subtypes.` No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 400         | `REQUEST_FAILED`   | `INVALID_PARAMETER` or `INVALID_FILTER`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `GET` all flow policies request supplies a `filter` query parameter that references an attribute other than `createdBy.user.id`, `createdBy.client.id`, `updatedBy.user.id`, or `updatedBy.client.id`, or an operator other than `eq`, `and`, or `or`, when actor metadata is enabled for the environment. When actor metadata is disabled, the filter parameter is ignored
>
> **Details:** Detail code `INVALID_PARAMETER` with message `The filter attribute was invalid or does not support filtering.` and the invalid attribute as the target, or message `The filter operator was invalid or not supported.` and the invalid operator as the target. A filter that is not a well-formed SCIM expression returns detail code `INVALID_FILTER` with message `The specified filter was invalid.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 403         | `ACCESS_FAILED`    | None                                                                | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:create:flowPolicies` permission (`POST` operations), the `davinci:read:flowPolicies` permission (`GET` operations, including the events endpoint), the `davinci:update:flowPolicies` permission (`PUT` operations), or the `davinci:delete:flowPolicies` permission (`DELETE` operations)
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 404         | `NOT_FOUND`        | None                                                                | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** Any operation references a DaVinci application ID that does not exist in the environment, or a `GET` one, `PUT`, or `DELETE` flow policy request or a `GET` flow policy events request references a flow policy ID that does not exist in the application
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 500         | `UNEXPECTED_ERROR` | None                                                                | **Message:** `There was an unexpected error with the service. Please try again later.`> **Collapse: When and details**
>
> **When:** A `DELETE` request targets an existing flow policy but the service cannot remove the policy from the application's stored policy list, or the service encounters an unexpected internal failure while processing any flow policy operation
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

---

---
title: DaVinci Admin Applications
description: Describes the PingOne DaVinci Admin Applications service for creating, reading, updating, deleting, and rotating keys and secrets for DaVinci applications
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-applications/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-applications/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-applications-data-model: DaVinci Admin applications data model properties
  response-codes: Response codes
  davinci-application-errors: DaVinci application errors
---

# DaVinci Admin Applications

The PingOne DaVinci Admin Applications service provides endpoints to create, read, update, and delete DaVinci applications. This service also includes endpoints to rotate the application key and application secret values.

A DaVinci application configuration is the link between your site and the sign-on flows you have created in DaVinci. The application configuration contains settings to determine how external sites can send requests for flows, what flows can be requested, and how users and resources from other sites are managed.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci Admin applications data model properties

| Property             | Type    | Required | Mutable   | Description                                                                                                                                           |
| -------------------- | ------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apiKey`             | Object  | Optional | Mutable   | The collection of API keys associated with this application resource.                                                                                 |
| `apiKey.enabled`     | Boolean | Optional | Mutable   | Specifies whether the API key for this appliction is enabled.                                                                                         |
| `apiKey.value`       | String  | Optional | Mutable   | The value of the API key.                                                                                                                             |
| `createdAt`          | Date    | N/A      | Read only | The time when the application was created.                                                                                                            |
| `environment`        | Object  | N/A      | Read only | The DaVinci company ID (environment ID) object.                                                                                                       |
| `environment.id`     | String  | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID.                                                                                          |
| `id`                 | String  | N/A      | Read only | The application ID.                                                                                                                                   |
| `name`               | String  | Required | Mutable   | The application name.                                                                                                                                 |
| `oauth`              | Object  | Optional | Mutable   | The OAuth configuration for this application resource.                                                                                                |
| `oauth.clientSecret` | String  | Optional | Mutable   | The client secret used by this application resource.                                                                                                  |
| `oauth.redirectUris` | Array   | Optional | Mutable   | The list of redirect URIs configured for this application resource.                                                                                   |
| `oauth.logoutURIs`   | Array   | Optional | Mutable   | The list of logout URIs configured for this application resource.                                                                                     |
| `oauth.scopes`       | Array   | Optional | Mutable   | The list of OAuth scopes configured for this application resource.                                                                                    |
| `oauth.grantTypes`   | Array   | Optional | Mutable   | The list of OAuth grant types configured for this application resource.                                                                               |
| `oauth.spjwksUrl`    | String  | Optional | Mutable   | A URL to retrieve JWKS keys to verify the authorization request signature. This option takes precedence over `spjwksOpenid` property if both are set. |
| `oauth.spJwksOpenid` | String  | Optional | Mutable   | A set of JWKS keys to verify the authorization request signature. This property is ignored if `spjwksUrl` is set.                                     |
| `updatedAt`          | Date    | N/A      | Read only | The time when the application was last modified.                                                                                                      |

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci application errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci application operations can return the following errors:

| HTTP status | Top‑level code     | Detail code                                                         | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/davinciApplications` or a `PUT /environments/{envID}/davinciApplications/{davinciApplicationID}` request supplies a body that violates the data model: an omitted `name`, a blank or null `name`, a `name` longer than 256 characters, a `name` whose first non-whitespace character is outside the allowed set or that contains a `<` or a `${` sequence, an `apiKeyEnabled` value that is not a boolean, an `oauth` value that is not an object, or an unknown `oauth.scopes` or `oauth.grantTypes` value
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'name'` with target `name` when the request omits `name`. `must not be empty or blank` for a blank `name`. `must be string`, `must be boolean`, or `must be object` for a property of the wrong JSON type. `must NOT have more than 256 characters` for a `name` longer than 256 characters. `must match pattern "<pattern>"`, where the pattern is the JSON schema pattern for the property, for a `name` whose first non-whitespace character is outside the allowed set or that contains a `<` or a `${` sequence. `must be one of the values: <allowed values joined by or>`, for example `must be one of the values: openid or profile or flow_analytics or offline_access` with target `oauth.scopes.2` for an unknown `oauth.scopes` entry. |
| 400         | `INVALID_DATA`     | `UNIQUENESS_VIOLATION`                                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/davinciApplications` request fails with a duplicate-key storage error, for example when the request specifies an application name that already exists
>
> **Details:** `App record already exists`. No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET` all applications request supplies a `page`, `limit`, `filter`, or `expand` query parameter longer than 256 characters
>
> **Details:** Detail code `INVALID_PARAMETER` with message `must NOT have more than 256 characters` and the overlong query parameter as the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT`, `DELETE`, key rotation `POST`, or secret rotation `POST` targets an application that is read-only
>
> **Details:** `Application is read-only.` The target is `readOnly`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 400         | `REQUEST_FAILED`   | `INVALID_PARAMETER` or `INVALID_FILTER`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `GET` all applications request supplies a `filter` query parameter that references an attribute other than `createdBy.user.id`, `createdBy.client.id`, `updatedBy.user.id`, or `updatedBy.client.id`, or an operator other than `eq`, `and`, or `or`, when actor metadata is enabled for the environment. When actor metadata is disabled, the filter parameter is ignored
>
> **Details:** Detail code `INVALID_PARAMETER` with message `The filter attribute was invalid or does not support filtering.` and the invalid attribute as the target, or message `The filter operator was invalid or not supported.` and the invalid operator as the target. A filter that is not a well-formed SCIM expression returns detail code `INVALID_FILTER` with message `The specified filter was invalid.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 400         | `REQUEST_FAILED`   | `ITEM_LIMIT_EXCEEDED`                                               | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/davinciApplications` request creates an application after the environment has reached the maximum number of applications allowed for the environment
>
> **Details:** `Cannot create more than <resourceLimit> applications.` No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 403         | `ACCESS_FAILED`    | None                                                                | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:create:applications` permission (`POST` operations), the `davinci:read:applications` permission (`GET` operations), the `davinci:update:applications` permission (`PUT` or the key or secret rotation `POST`), or the `davinci:delete:applications` permission (`DELETE`)
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 404         | `NOT_FOUND`        | None                                                                | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `GET` one, `PUT`, `DELETE`, key rotation, or secret rotation request references a DaVinci application ID that does not exist in the environment
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 415         | `INVALID_REQUEST`  | None                                                                | **Message:**```
The server is refusing to service the request because the entity of the request is in a format not supported by the requested resource for the requested method.
```> **Collapse: When and details**
>
> **When:** A key rotation request does not use the `application/vnd.pingidentity.davinciApplication.rotateKey+json` content type, or a secret rotation request does not use the `application/vnd.pingidentity.davinciApplication.rotateSecret+json` content type
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 500         | `UNEXPECTED_ERROR` | None                                                                | **Message:** `There was an unexpected error with the service. Please try again later.`> **Collapse: When and details**
>
> **When:** The service encounters an unexpected internal failure while processing the request, for example a `GET` all applications request that cannot read the application list
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: DaVinci Admin Connector Instances
description: Describes the PingOne DaVinci Admin Connector Instances service for creating, reading, updating, deleting, and cloning DaVinci connector instances
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connections/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connections/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-connector-instances-data-model-properties: DaVinci admin connector instances data model properties
  response-codes: Response codes
  davinci-connector-instance-errors: DaVinci connector instance errors
---

# DaVinci Admin Connector Instances

The PingOne DaVinci Admin Connector Instances service provides endpoints to create, read, update, and delete DaVinci connector instances. A DaVinci connector instance is one instance of a DaVinci connector (the connection configuration specifies a connector by name). You can then use the capabilities provided by the connector inside a flow, and launch the flow through an application.

This service also includes an action to clone connector instance resources.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci admin connector instances data model properties

| Property         | Type   | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                |
| ---------------- | ------ | -------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connector`      | Object | Required | Immutable | The connector object.                                                                                                                                                                                                                                                                                                      |
| `connector.id`   | String | Required | Immutable | The connector object name (for example, `httpConnector`).                                                                                                                                                                                                                                                                  |
| `createdAt`      | Date   | N/A      | Read only | The time when the connection was created.                                                                                                                                                                                                                                                                                  |
| `environment`    | Object | N/A      | Read only | The DaVinci company ID (environment ID) object.                                                                                                                                                                                                                                                                            |
| `environment.id` | String | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID.                                                                                                                                                                                                                                                               |
| `id`             | String | N/A      | Read only | The connector instance resource ID.                                                                                                                                                                                                                                                                                        |
| `name`           | String | Required | Mutable   | The connector instance name.                                                                                                                                                                                                                                                                                               |
| `properties`     | Object | Optional | Mutable   | The configuration of the connector object. This field is not applicable to all connectors and is omitted in the output if empty or null. If the specified connector requires configuration, refer to the **Connector configuration** section of the connector documentation for the connector specified in `connector.id`. |
| `updatedAt`      | Date   | N/A      | Read only | The time when the connector instance was updated.                                                                                                                                                                                                                                                                          |

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci connector instance errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci connector instance operations can return the following errors:

| HTTP status | Top‑level code    | Detail code                                                         | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------- | ----------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`    | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/connectorInstances` or a `PUT /environments/{envID}/connectorInstances/{connectorInstanceID}` request supplies a body that violates the data model: an omitted `name` property, an omitted `connector` object or an omitted `connector.id` property on create, an empty or blank `name`, a `name` or `connector.id` value longer than 256 characters, a `name` or `connector.id` value that starts with an unsupported character or contains a `<` or a `${` sequence, or a property whose value is not of the documented JSON type
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'name'` with target `name` and `must have required property 'connector'` with target `connector` when the create request omits either property, and `must have required property 'id'` with target `connector` when the `connector` object omits `id`. `must not be empty or blank` for an empty or blank `name`. `must NOT have more than 256 characters` for a `name` or `connector.id` value longer than 256 characters. `must match pattern "<pattern>"`, where \<pattern> is the schema pattern, for a `name` or `connector.id` value that starts with an unsupported character or contains a `<` or a `${` sequence. `must be string` for a property of the wrong JSON type, for example with target `name`. |
| 400         | `INVALID_DATA`    | `INVALID_PARAMETER`                                                 | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/connectorInstances` or a `GET /environments/{envID}/connectorInstances/{connectorInstanceID}` request supplies a `page`, `limit`, `expand`, or `filter` query parameter longer than 256 characters
>
> **Details:** Detail code `INVALID_PARAMETER` with message `must NOT have more than 256 characters` and the overlong query parameter as the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`                                                     | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/connectorInstances` request specifies a `connector.id` value that does not identify a connector available to the environment
>
> **Details:** Detail code `INVALID_VALUE` with message `Invalid connector id` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 400         | `INVALID_DATA`    | `UNIQUENESS_VIOLATION`                                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/connectorInstances` or a `POST /environments/{envID}/connectorInstances/{connectorInstanceID}` clone request uses a name that is already associated with a connector instance in the environment
>
> **Details:** Detail code `UNIQUENESS_VIOLATION` with message `The connector name entered is already associated with another connector. Enter a different name.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 400         | `INVALID_DATA`    | `UNIQUENESS_VIOLATION`                                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `PUT /environments/{envID}/connectorInstances/{connectorInstanceID}` request renames the connector instance to a name that another connector instance in the environment already uses
>
> **Details:** Detail code `UNIQUENESS_VIOLATION` with message `A resource with the specified name already exists` and target `name`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 400         | `REQUEST_FAILED`  | `INVALID_PARAMETER` or `INVALID_FILTER`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/connectorInstances` request supplies a `filter` query parameter that references any attribute other than the six actor identifier attributes `createdBy.user.id`, `createdBy.client.id`, `createdBy.environment.id`, `updatedBy.user.id`, `updatedBy.client.id`, or `updatedBy.environment.id` when actor metadata is enabled for the environment, or supplies any `filter` query parameter when actor metadata is disabled. When actor metadata is enabled, actor attributes support only `eq` combined through `and` or `or`
>
> **Details:** Detail code `INVALID_PARAMETER` with message `The filter attribute was invalid or does not support filtering.` and the invalid attribute as the target, or message `The filter operator was invalid or not supported.` and the attribute that does not support the supplied operator as the target. A filter that is not a well-formed SCIM expression returns detail code `INVALID_FILTER` with message `The specified filter was invalid.` and no target.                                                                                                                                                                                                                                                                                                                                                                                       |
| 403         | `ACCESS_FAILED`   | None                                                                | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:create:connections` permission (`POST` operations), the `davinci:read:connections` permission (`GET` operations), the `davinci:update:connections` permission (`PUT` operations), or the `davinci:delete:connections` permission (`DELETE` operations)
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 404         | `NOT_FOUND`       | None                                                                | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `GET`, `PUT`, or `DELETE` request references a connector instance ID that does not exist in the environment, or a `POST` clone request references a source connector instance ID that does not exist or could not be read
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 415         | `INVALID_REQUEST` | None                                                                | **Message:**```
The server is refusing to service the request because the entity of the request is in a format not supported by the requested resource for the requested method.
```> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/connectorInstances/{connectorInstanceID}` clone request does not set the `Content-Type` header to `application/vnd.pingidentity.connectorInstance.clone+json`
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

---

---
title: DaVinci Admin Connectors
description: Describes the PingOne DaVinci Admin Connector service for reading DaVinci connector resources that define the capabilities available to use as nodes in a flow
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connectors/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connectors/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-connector-data-model-properties: DaVinci admin connector data model properties
  davinci-admin-connectors-details-data-model-properties: DaVinci admin connectors details data model properties
  response-codes: Response codes
  davinci-connector-errors: DaVinci connector errors
---

# DaVinci Admin Connectors

The PingOne DaVinci Admin Connector service provides endpoints to read DaVinci connector resources. Connectors give DaVinci the ability to integrate third party technologies, HTML pages, and other tools to create a sign-on flow. They define the capabilities that you can use as nodes in a flow. For example, an HTTP connector provides the capability to present an HTML form to collect and submit user information or make REST API calls.

|   |                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is recommended that you review the [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html) topic in the *PingOne DaVinci* admin guide before assigning connectors to your workflow. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci admin connector data model properties

| Property                       | Type   | Required | Mutable   | Description                                                                             |
| ------------------------------ | ------ | -------- | --------- | --------------------------------------------------------------------------------------- |
| `description`                  | String | Optional | Mutable   | The connector description.                                                              |
| `environment`                  | Object | N/A      | Read only | The DaVinci company ID (environment ID) object.                                         |
| `environment.id`               | String | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID.                            |
| `id`                           | String | N/A      | Read only | The connector ID (for example, `httpConnector`).                                        |
| `metadata`                     | Object | N/A      | Read only | Represents the metadata information about the connector, such as type, color, and logo. |
| `metadata.type`                | String | N/A      | Read only | The type of connector. Options are `core`, `ping`, or `service`.                        |
| `metadata.vendor`              | String | N/A      | Read only | The ID of a vendor (for example,`microsoft` or `amazon`).                               |
| `metadata.colors`              | Object | N/A      | Read only | An object that specifies the colors on the canvas.                                      |
| `metadata.colors.canvas`       | String | N/A      | Read only | A hexadecimal representation of the canvas color.                                       |
| `metadata.colors.canvasText`   | String | N/A      | Read only | A hexadecimal representation of the canvas text color.                                  |
| `metadata.colors.dark`         | String | N/A      | Read only | A hexadecimal representation of the shade of darkness.                                  |
| `metadata.logos`               | String | N/A      | Read only | The image name of the connector logo file.                                              |
| `metadata.logos.canvas`        | Object | N/A      | Read only | An object that specifies the canvas.                                                    |
| `metadata.logos.imageFileName` | String | N/A      | Read only | The name of the connector logo image.                                                   |
| `name`                         | String | Required | Mutable   | The connector name (for example, `HTTP`).                                               |
| `version`                      | String | N/A      | Read only | The version number of the connector.                                                    |

## DaVinci admin connectors details data model properties

| Property                                     | Type      | Required | Mutable   | Description                                                                                                                                                                                       |
| -------------------------------------------- | --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accountConfigView`                          | Object\[] | Optional | Mutable   | Represents the account configuration of the connector. For details, refer to [Core connectors](https://docs.pingidentity.com/davinci/connectors/davinci_core_connectors.html).                    |
| `accountConfigView.componentViewSize`        | String    | Optional | Mutable   | The size of the configuration window.                                                                                                                                                             |
| `accountConfigView.items`                    | Array     | Optional | Mutable   | An array of configurable properties.                                                                                                                                                              |
| `accountConfigView.items.propertyName`       | String    | Optional | Mutable   | The name of the configurable property.                                                                                                                                                            |
| `accountConfigView.items.items`              | Array     | Optional | Mutable   | An array of sub-property names under the top level property.                                                                                                                                      |
| `accountConfigView.items.items.propertyName` | Array     | Optional | Mutable   | The name of the sub-property under the top level property.                                                                                                                                        |
| `capabilities`                               | Object\[] | Optional | Mutable   | A list of all connector capabilities and their input properties. For more information, refer to [Core connectors](https://docs.pingidentity.com/davinci/connectors/davinci_core_connectors.html). |
| `createdAt`                                  | Date      | N/A      | Read only | The time when the connector was created.                                                                                                                                                          |
| `credentialsView`                            | Object    | Optional | Mutable   | Represents the credentials view of the connector.                                                                                                                                                 |
| `credentialsView`                            | Object    | Optional | Mutable   | The fields that will be part of the connector configuration specific to credentials.                                                                                                              |
| `credentialsView.items`                      | Array     | Optional | Mutable   | An array of configurable properties.                                                                                                                                                              |
| `credentialsView.items.propertyName`         | String    | Optional | Mutable   | The name of the property.                                                                                                                                                                         |
| `flowSections`                               | Object\[] | Optional | Mutable   | Represents the flow section to which the connector can be categorized.                                                                                                                            |
| `flowSections.name`                          | String    | Optional | Mutable   | The name of the section being shown.                                                                                                                                                              |
| `flowSections.value`                         | String    | Optional | Mutable   | A pointer to the flow section name referenced by other sections in the manifest.                                                                                                                  |
| `properties`                                 | Object    | Optional | Mutable   | A list of properties that will be used by the capabilities. For more information, refer to [Core connectors](https://docs.pingidentity.com/davinci/connectors/davinci_core_connectors.html).      |
| `sections`                                   | Object\[] | Optional | Mutable   | An array of sections shown in Connector Configuration. For more information, refer to [Core connectors](https://docs.pingidentity.com/davinci/connectors/davinci_core_connectors.html).           |

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci connector errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci connector operations can return the following errors:

| HTTP status | Top‑level code  | Detail code             | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------- | --------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400         | `INVALID_DATA`  | `INVALID_PARAMETER`     | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/connectors`, a `GET /environments/{envID}/connectors/{davinciConnectorID}`, or a `GET /environments/{envID}/connectors/{davinciConnectorID}/details` request supplies any query parameter
>
> **Details:** Detail code `INVALID_PARAMETER` with message `must NOT have additional properties` and the rejected query parameter as the target. |
| 403         | `ACCESS_FAILED` | None                    | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:read:connectors` permission, which every connector read operation requires
>
> **Details:** None                                                                                                                                                                                                                                                        |
| 404         | `NOT_FOUND`     | `INVALID_VALUE` or None | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** Any connector request targets an environment ID that does not exist, or a `GET` one connector or a `GET` connector details request references a connector ID that does not exist
>
> **Details:** `Company not found` with detail code `INVALID_VALUE` for an unknown environment ID. No details for an unknown connector ID.                                                           |

---

---
title: DaVinci Admin Flow Versions
description: Describes the PingOne DaVinci Admin Flow Versions service for reading, updating, deleting, exporting, and reverting DaVinci flow versions
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flow-versions/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flow-versions/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  flow-versions-data-model: DaVinci admin flow versions data model properties
  flow-versions-details-data-model: Flow versions details property data model
  flow-versions-graph-data-model: Flow versions graph data property data model
  response-codes: Response codes
  davinci-flow-version-errors: DaVinci flow version errors
---

# DaVinci Admin Flow Versions

The PingOne DaVinci Admin Flow Versions service provides endpoints to read, update, and delete DaVinci flow versions. This service also includes endpoints to export, revert, and see details about a flow version.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The flow version update operation applies only to the `alias` property to add or change the user-friendly name associated with the flow version. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci admin flow versions data model properties

| Property                | Type           | Required | Mutable   | Description                                                                                                                                                                    |
| ----------------------- | -------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `alias`                 | String         | Optional | Mutable   | The user defined flow version alias.                                                                                                                                           |
| `clonedFrom`            | Number         | Optional | Immutable | The version number from which this flow version was cloned or created.                                                                                                         |
| `connectors`            | Array\[object] | Optional | Mutable   | An array of connectors that apply to the flow.                                                                                                                                 |
| `connectors[].id`       | String         | Optional | Mutable   | The connector ID (or IDs) associated with the flow. Example connectors are `httpConnector`, `functionsConnector`, `pingOneVerifyConnector`, and `annotationConnector`.         |
| `createdAt`             | Time           | N/A      | Read only | The timestamp when the flow was created.                                                                                                                                       |
| `deployedAt`            | Time           | N/A      | Read only | The stamp when the flow was last deployed.                                                                                                                                     |
| `description`           | String         | Optional | Mutable   | The description of the flow.                                                                                                                                                   |
| `enabled`               | Boolean        | Optional | Immutable | Specifies the state of the flow. This can be stored as its own value in the database or it can reflect an existing `flowStatus`.                                               |
| `environment`           | Object         | N/A      | Read only | The DaVinci company ID (environment ID) object.                                                                                                                                |
| `environment.id`        | String         | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID.                                                                                                                   |
| `graphData`             | Object         | Optional | Mutable   | The graph-based representation of the flow depicted in the UI. Refer to the [Flow versions graph data property data model](#flow-versions-graph-data-model) table for details. |
| `flow`                  | Object         | Required | Immutable | The flow object associated with this flow version.                                                                                                                             |
| `flow.id`               | String         | Required | Immutable | The flow ID of the flow associated with this flow version.                                                                                                                     |
| `flow.name`             | String         | Required | Immutable | The name of the flow associated with this flow version.                                                                                                                        |
| `includeSubFlows`       | Boolean        | Optional | Mutable   | Specifies whether the exported flow version should include subflows.                                                                                                           |
| `includeVariableValues` | Boolean        | Optional | Mutable   | Specifies whether the exported flow version should include variable values.                                                                                                    |
| `outputSchema`          | Object         | Required | Mutable   | The `JSONschema` output object of the flow.                                                                                                                                    |
| `updatedAt`             | Date           | N/A      | Read only | The timestamp when the flow was updated or saved.                                                                                                                              |
| `version`               | Number         | Required | Mutable   | The version number of the flow instance represented by this object.                                                                                                            |

### Flow versions details property data model

The following table lists the supported flow versions details settings properties.

| Property                               | Type           | Required | Mutable   | Description                                                                                                                                                                    |
| -------------------------------------- | -------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `color`                                | String         | Optional | Mutable   | The color of the flow.                                                                                                                                                         |
| `connectors`                           | Array\[object] | Optional | Mutable   | An array of connectors that apply to the flow.                                                                                                                                 |
| `connectors.id`                        | String         | Optional | Mutable   | The connector ID (or IDs) associated with the flow.                                                                                                                            |
| `description`                          | String         | Optional | Mutable   | The description of the flow.                                                                                                                                                   |
| `enabled`                              | Boolean        | Optional | Immutable | Specifies the state of the flow.                                                                                                                                               |
| `graphData`                            | Object         | Optional | Mutable   | The graph-based representation of the flow depicted in the UI. Refer to the [Flow versions graph data property data model](#flow-versions-graph-data-model) table for details. |
| `inputSchema`                          | Array\[object] | Optional | Mutable   | The flow input parameters in an array of `JSONschema` objects.                                                                                                                 |
| `name`                                 | String         | Required | Mutable   | The name of the flow.                                                                                                                                                          |
| `outputSchema`                         | Object         | Required | Mutable   | The `JSONschema` output object of the flow.                                                                                                                                    |
| `settings`                             | Object         | Optional | Mutable   | Flow settings saved by the user. Refer to the [Settings property data model](../admin-flows/index.html#settings-property-data-model) table for details.                        |
| `trigger`                              | Object         | Optional | Mutable   | The flow trigger object.                                                                                                                                                       |
| `trigger.type`                         | String         | Optional | Mutable   | If the trigger type is set to `AUTHENTICATION`, you invoke the flow through PingOne OpenID Connect or SAML endpoints.                                                          |
| `trigger.configuration`                | Object         | Optional | Mutable   | The configuration object for session reuse.                                                                                                                                    |
| `trigger.configuration.pwd`            | Object         | Optional | Mutable   | The configuration object for password session reuse.                                                                                                                           |
| `trigger.configuration.pwd.enabled`    | Boolean        | Optional | Mutable   | Specifies whether this configuration must be used to check for existing sessions.                                                                                              |
| `trigger.configuration.pwd.lastSignOn` | Integer        | Optional | Mutable   | An integer that specifies the duration (in seconds) that an active session can be reused.                                                                                      |
| `trigger.configuration.mfa`            | Object         | Optional | Mutable   | The configuration object for MFA session reuse.                                                                                                                                |
| `trigger.configuration.mfa.enabled`    | Boolean        | Optional | Mutable   | Specifies whether this configuration must be used to check for existing sessions.                                                                                              |
| `trigger.configuration.mfa.lastSignOn` | Integer        | Optional | Mutable   | An integer that specifies the duration (in seconds) that an active session can be reused.                                                                                      |
| `updates`                              | Array          | N/A      | Read only | String of actions taken to generate this version from the previous version.                                                                                                    |

### Flow versions graph data property data model

The following table lists the supported flow versions graph data settings properties.

| Property                                                              | Type           | Required | Mutable | Description                                                                                                                                                 |
| --------------------------------------------------------------------- | -------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `graphData`                                                           | Object         | Optional | Mutable | The graph-based representation of the flow depicted in the UI.                                                                                              |
| `graphData.elements`                                                  | Object         | Required | Mutable | If `graphData` is set, the `graphData.elements` object must be defined.                                                                                     |
| `graphData.elements.nodes[]`                                          | Array\[Object] | Required | Mutable | If `graphData.elements` is set, the `graphData.elements.nodes[]` object must be defined.                                                                    |
| `graphData.elements.nodes[].data`                                     | Object         | Required | Mutable | The node item data associated with the flow version. If `graphData.elements.nodes[]` is set, the `graphData.elements.nodes[]].data` object must be defined. |
| `graphData.elements.nodes[].data.nodeType`                            | String         | Required | Mutable | The node type associated with the node item.                                                                                                                |
| `graphData.elements.nodes[].data.connectionId`                        | String         | Optional | Mutable | The connection ID associated with the node item.                                                                                                            |
| `graphData.elements.nodes[].data.connectorId`                         | String         | Optional | Mutable | The connector ID associated with the node item.                                                                                                             |
| `graphData.elements.nodes[].data.name`                                | String         | Optional | Mutable | The name of the node item.                                                                                                                                  |
| `graphData.elements.nodes[].data.label`                               | String         | Optional | Mutable | The label associated with the node item.                                                                                                                    |
| `graphData.elements.nodes[].data.status`                              | String         | Optional | Mutable | The status of the node item.                                                                                                                                |
| `graphData.elements.nodes[].data.capabilityName`                      | String         | Optional | Mutable | The name of the capability associated with the node item.                                                                                                   |
| `graphData.elements.nodes[].data.type`                                | String         | Optional | Mutable | The type associated with the node item.                                                                                                                     |
| `graphData.elements.nodes[].data.properties`                          | Object         | Optional | Mutable | The properties associated with the node item.                                                                                                               |
| `graphData.elements.nodes[].data.properties.nodeTitle`                | Object         | Optional | Mutable | The node title object.                                                                                                                                      |
| `graphData.elements.nodes[].data.properties.nodeTitle.value`          | String         | Required | Mutable | The node title text.                                                                                                                                        |
| `graphData.elements.nodes[].data.properties.code`                     | Object         | Optional | Mutable | The node item code object.                                                                                                                                  |
| `graphData.elements.nodes[].data.properties.code.value`               | String         | Required | Mutable | The code associated with the node item.                                                                                                                     |
| `graphData.elements.nodes[].data.properties.type`                     | Object         | Optional | Mutable | The node type object.                                                                                                                                       |
| `graphData.elements.nodes[].data.properties.type.value`               | String         | Required | Mutable | The node type.                                                                                                                                              |
| `graphData.elements.nodes[].data.properties.customCSS`                | Object         | Optional | Mutable | The node's stylesheet object.                                                                                                                               |
| `graphData.elements.nodes[].data.properties.customCSS.value`          | String         | Required | Mutable | The node's CSS.                                                                                                                                             |
| `graphData.elements.nodes[].data.properties.customHTML`               | Object         | Optional | Mutable | The node's HTML object.                                                                                                                                     |
| `graphData.elements.nodes[].data.properties.customHTML.value`         | String         | Required | Mutable | The node's custom HTML.                                                                                                                                     |
| `graphData.elements.nodes[].data.properties.customScript`             | Object         | Optional | Mutable | The node's script object.                                                                                                                                   |
| `graphData.elements.nodes[].data.properties.customScript.value`       | String         | Required | Mutable | The node's custom scripts.                                                                                                                                  |
| `graphData.elements.nodes[].data.properties.backgroundColor`          | Object         | Optional | Mutable | The node's background color object.                                                                                                                         |
| `graphData.elements.nodes[].data.properties.backgroundColor.value`    | String         | Required | Mutable | The node's background color.                                                                                                                                |
| `graphData.elements.nodes[].data.properties.inputSchema`              | Object         | Optional | Mutable | The node's input schema object.                                                                                                                             |
| `graphData.elements.nodes[].data.properties.inputSchema.value`        | String         | Required | Mutable | The node's input schema.                                                                                                                                    |
| `graphData.elements.nodes[].data.properties.outputSchema`             | Object         | Optional | Mutable | The node's output schema object.                                                                                                                            |
| `graphData.elements.nodes[].data.properties.outputSchema.value`       | String         | Required | Mutable | The node's output schema.                                                                                                                                   |
| `graphData.elements.nodes[].data.properties.message`                  | Object         | Optional | Mutable | The node's message object.                                                                                                                                  |
| `graphData.elements.nodes[].data.properties.message.value`            | String         | Required | Mutable | The node's message text.                                                                                                                                    |
| `graphData.elements.nodes[].data.properties.showContinueButton`       | Object         | Optional | Mutable | The node's show continue button object.                                                                                                                     |
| `graphData.elements.nodes[].data.properties.showContinueButton.value` | Boolean        | Required | Mutable | Specifies whether to show the node's continue text.                                                                                                         |
| `graphData.elements.nodes[].data.properties.saveVariables`            | Object         | Optional | Mutable | The node's save variables object.                                                                                                                           |
| `graphData.elements.nodes[].data.properties.saveVariables.value`      | Array\[Object] | Required | Mutable | An array of variables that are saved.                                                                                                                       |
| `graphData.elements.nodes[].data.properties.formFieldList`            | Object         | Optional | Mutable | The node's form fields object.                                                                                                                              |
| `graphData.elements.nodes[].data.properties.formFieldsList.value`     | Array\[Object] | Required | Mutable | An array of form fields associated with the node.                                                                                                           |
| `graphData.elements.nodes[].data.properties.variableInputList`        | Object         | Optional | Mutable | The node's variable input list object.                                                                                                                      |
| `graphData.elements.nodes[].data.properties.variableInputList.value`  | Array\[Object] | Required | Mutable | An array of input variables associated with the node.                                                                                                       |
| `graphData.elements.nodes[].data.properties.additionalProperties`     | Array\[Object] | Optional | Mutable | An array of additional properties allowed by the node.                                                                                                      |
| `graphData.elements.nodes[].data.additionalProperties`                | Array\[Object] | Optional | Mutable | An array of additional properties allowed in the `Item` definition.                                                                                         |
| `graphData.elements.nodes[].position`                                 | Object         | Required | Mutable | The node's position object.                                                                                                                                 |
| `graphData.elements.nodes[].position.x`                               | Number         | Required | Mutable | The node's x-axis position.                                                                                                                                 |
| `graphData.elements.nodes[].position.y`                               | Number         | Required | Mutable | The node's y-axis position.                                                                                                                                 |
| `graphData.elements.nodes[].group`                                    | String         | Required | Mutable | The node's group.                                                                                                                                           |
| `graphData.elements.nodes[].removed`                                  | Boolean        | Required | Mutable | Specifies whether the node can be removed.                                                                                                                  |
| `graphData.elements.nodes[].selected`                                 | Boolean        | Required | Mutable | Specifies whether the node can be selected.                                                                                                                 |
| `graphData.elements.nodes[].selectable`                               | Boolean        | Required | Mutable | Specifies whether the node is selectable.                                                                                                                   |
| `graphData.elements.nodes[].locked`                                   | Boolean        | Required | Mutable | Specifies whether the node is locked.                                                                                                                       |
| `graphData.elements.nodes[].grabbable`                                | Boolean        | Required | Mutable | Specifies whether the node is grabbable.                                                                                                                    |
| `graphData.elements.nodes[].pannable`                                 | Boolean        | Required | Mutable | Specifies whether the node can be moved.                                                                                                                    |
| `graphData.elements.nodes[].classes`                                  | String         | Optional | Mutable | The classes associated with the node.                                                                                                                       |
| `graphData.elements.edges[]`                                          | Array\[Object] | Required | Mutable | The object that describes the graph data element edges.                                                                                                     |
| `graphData.elements.edges[].data`                                     | Object         | Required | Mutable | The object that describes the edges data.                                                                                                                   |
| `graphData.elements.edges[].data.id`                                  | String         | Required | Mutable | The edges element ID.                                                                                                                                       |
| `graphData.elements.edges[].data.source`                              | String         | Required | Mutable | The edges element source.                                                                                                                                   |
| `graphData.elements.edges[].data.target`                              | String         | Required | Mutable | The edges element target.                                                                                                                                   |
| `graphData.elements.edges[].position`                                 | Object         | Required | Mutable | The edge's position object.                                                                                                                                 |
| `graphData.elements.edges[].position.x`                               | Number         | Required | Mutable | The edge's x-axis position.                                                                                                                                 |
| `graphData.elements.edges[].position.y`                               | Number         | Required | Mutable | The edge's y-axis position.                                                                                                                                 |
| `graphData.elements.edges[].group`                                    | String         | Required | Mutable | The edge's group.                                                                                                                                           |
| `graphData.elements.edges[].removed`                                  | Boolean        | Required | Mutable | Specifies whether the edge can be removed.                                                                                                                  |
| `graphData.elements.edges[].selected`                                 | Boolean        | Required | Mutable | Specifies whether the edge can be selected.                                                                                                                 |
| `graphData.elements.edges[].selectable`                               | Boolean        | Required | Mutable | Specifies whether the node is selectable.                                                                                                                   |
| `graphData.elements.edges[].locked`                                   | Boolean        | Required | Mutable | Specifies whether the edge is locked.                                                                                                                       |
| `graphData.elements.edges[].grabbable`                                | Boolean        | Required | Mutable | Specifies whether the edge is grabbable.                                                                                                                    |
| `graphData.elements.edges[].pannable`                                 | Boolean        | Required | Mutable | Specifies whether the edge can be moved.                                                                                                                    |
| `graphData.elements.edges[].classes`                                  | String         | Optional | Mutable | The classes associated with the item.                                                                                                                       |
| `graphData.data`                                                      | String         | Required | Mutable | The data associated with the element.                                                                                                                       |
| `graphData.zoomingEnabled`                                            | Boolean        | Required | Mutable | Specifies whether zooming is enabled for the element.                                                                                                       |
| `graphData.userZoomingEnabled`                                        | Boolean        | Required | Mutable | Specifies whether user zooming is enabled for the element.                                                                                                  |
| `graphData.zoom`                                                      | Number         | Required | Mutable | The zoom number.                                                                                                                                            |
| `graphData.minZoom`                                                   | Number         | Optional | Mutable | The minimum zoom number.                                                                                                                                    |
| `graphData.maxZoom`                                                   | Number         | Optional | Mutable | The maximum zoom number.                                                                                                                                    |
| `graphData.panningEnabled`                                            | Boolean        | Required | Mutable | Specifies whether the element can be moved.                                                                                                                 |
| `graphData.userPanningEnabled`                                        | Boolean        | Required | Mutable | Specifies whether the element can be moved by the user.                                                                                                     |
| `graphData.pan`                                                       | Object         | Required | Mutable | The panning object.                                                                                                                                         |
| `graphData.pan.x`                                                     | Number         | Required | Mutable | The element's x-axis position.                                                                                                                              |
| `graphData.pan.y`                                                     | Number         | Required | Mutable | The element's y-axis position.                                                                                                                              |
| `graphData.boxSelectionEnabled`                                       | Boolean        | Required | Mutable | Specifies whether box selection is enabled.                                                                                                                 |
| `graphData.renderer`                                                  | Object         | Required | Mutable | The renderer object.                                                                                                                                        |
| `graphData.renderer.name`                                             | String         | Required | Mutable | The renderer name.                                                                                                                                          |

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci flow version errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci flow version operations can return the following errors:

| HTTP status | Top‑level code     | Detail code                                                         | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ------------------ | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows/{davinciFlowID}/versions` or a `PUT /environments/{envID}/flows/{davinciFlowID}/versions/{davinciFlowVersionID}` request supplies a body that violates the data model: an omitted `version` on create, a `name` longer than 256 characters, a blank or null `name`, a `name` whose first non-whitespace character is outside the allowed set or that contains a `<` or a `${` sequence, a `trigger` that is not an object or that omits `type`, a `trigger.type` value other than `AUTHENTICATION`, or a `name`, `description`, `color`, `graphData`, `inputSchema`, `outputSchema`, `settings`, `skcomponents`, or `enabled` value of the wrong JSON type
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'version'` with target `version` when the create request omits `version`. `must not be empty or blank` for a blank `name`. `must be string`, `must be object`, `must be array`, or `must be boolean` for a property of the wrong JSON type, for example `must be string` for a null `name`. `must NOT have more than 256 characters` for a `name` longer than 256 characters. `must match pattern "<pattern>"`, where the pattern is the JSON schema pattern for the property, for a `name` whose first non-whitespace character is outside the allowed set or that contains a `<` or a `${` sequence. `must be object` for a `trigger` that is not an object. `must have required property 'type'` with target `trigger` when `trigger` omits `type`. `must be one of the values: AUTHENTICATION` with target `trigger.type` for an unknown or unsupported `trigger.type` value. |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `PUT /environments/{envID}/flows/{davinciFlowID}/versions/{davinciFlowVersionID}/alias` request supplies a body that violates the data model: an omitted `alias`, a blank `alias`, an `alias` longer than 256 characters, an `alias` that starts with a whitespace or unsupported character or that contains a `<` or a `${` sequence, or an `alias` value that is not a string
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'alias'` with target `alias` when the request omits `alias`. `must not be empty or blank` for a blank `alias`. `must be string` for an `alias` that is not a string. `must NOT have more than 256 characters` for an `alias` longer than 256 characters. `must match pattern "<pattern>"`, where the pattern is the JSON schema pattern for the property, for an `alias` that starts with a whitespace or unsupported character or that contains a `<` or a `${` sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`                                                     | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A request to a flow version endpoint other than the create `POST` supplies a `versionId` path parameter that the service cannot parse as a version number, for example a value that is not a number or a `<flowId>-<version>` value whose flow ID does not match the flow ID in the request path
>
> **Details:** `must be a number` for a `versionId` value that is not a number, or `Flow ID in the version ID does not match the flow ID in the request path` when the flow ID embedded in the `versionId` value does not match the `flowId` path parameter. The target is `versionId`, or `version` when the request body includes a `version` property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`                                                     | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` export request supplies `includeSubFlows`, `includeVariableValues`, or `includeForms` with a value that is not a boolean, a `POST` revert request includes a request body property, or a `DELETE` request includes a query parameter
>
> **Details:** `must be boolean` with the property name as the target for an export property that is not a boolean, or `must NOT have additional properties` with the rejected body property or query parameter as the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET` all flow versions request or a `GET` one flow version request includes any query parameter, or a `GET` flow version details request includes an `expand` value other than `skcomponents` or a query parameter other than `expand`
>
> **Details:** `must NOT have additional properties` with the rejected query parameter as the target, or `must be one of the values: skcomponents` with target `expand` for an unsupported `expand` value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` create or `PUT` update request specifies a version number that is less than zero
>
> **Details:** `Flow version should be zero or greater than zero`. The target is `version` on create and `versionId` on update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` create request specifies a version number that already exists for the flow
>
> **Details:** `Flow version already exists`. The target is `version`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `DELETE` request targets the flow's current version
>
> **Details:** `Can not delete current flow version`. No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `REQUEST_FAILED`   | `ITEM_LIMIT_EXCEEDED`                                               | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` create, `PUT` update, or `POST` revert request creates a new flow version after the flow has reached the maximum number of flow versions allowed and the service cannot free an existing version
>
> **Details:** `Flow version limit is exceeded`. No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 403         | `ACCESS_FAILED`    | None                                                                | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:read:flowVersions` permission (`GET` operations), the `davinci:update:flowVersions` permission (the create `POST`, the update `PUT`, or the alias `PUT`), the `davinci:delete:flowVersions` permission (`DELETE`), the `davinci:export:flowVersions` permission (the export `POST`), or the `davinci:revert:flowVersions` permission (the revert `POST`)
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 404         | `NOT_FOUND`        | None                                                                | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** Any operation references a DaVinci flow ID that does not exist in the environment, or a `GET` one, `GET` details, update `PUT`, alias `PUT`, `DELETE`, revert, or export request references a flow version that does not exist for the flow
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 415         | `INVALID_REQUEST`  | None                                                                | **Message:**```
The server is refusing to service the request because the entity of the request is in a format not supported by the requested resource for the requested method.
```> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows/{davinciFlowID}/versions/{davinciFlowVersionID}` request uses a `Content-Type` header value other than `application/vnd.pingidentity.flowversion.revert+json` or `application/vnd.pingidentity.flowversion.export+json`, or omits the header
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 500         | `UNEXPECTED_ERROR` | None                                                                | **Message:** `There was an unexpected error with the service. Please try again later.`> **Collapse: When and details**
>
> **When:** The service encounters an unexpected internal failure while processing the request, for example a revert that cannot create the new flow version
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

---
title: DaVinci Admin Flows
description: Describes the PingOne DaVinci Admin Flows service for creating, reading, updating, deleting, enabling, deploying, importing, and cloning DaVinci flows
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flows/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flows/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-flow-data-model-properties: DaVinci admin flow data model properties
  settings-property-data-model: Settings property data model
  input-schema-for-non-pingone-flows-data-model: Input schema for non-PingOne flows data model properties
  limiting-and-filtering-data: Limiting and filtering data
  scim-operators: SCIM operators
  response-codes: Response codes
  davinci-flow-errors: DaVinci flow errors
---

# DaVinci Admin Flows

DaVinci flows are constructed, logical paths that specify the workflow for the user's authorization and authentication experiences.

Flows consist of one or more nodes joined together. Each node performs a specific task, using one of the capabilities of your connectors. After completing the task, the flow determines which task to perform next until the flow is complete.

The PingOne DaVinci Admin Flows service provides endpoints to create, read, update, and delete DaVinci flows. This service also includes endpoints to enable, deploy, import, and clone flows.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci admin flow data model properties

| Property                                           | Type           | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------- | -------------- | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `color`                                            | String         | Optional | Mutable   | The color of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `connectors`                                       | Array\[object] | Optional | Mutable   | An array of connectors that apply to the flow. An optional query parameter can toggle behavior, either the names of the connectors are returned or the connection objects themselves are returned as embedded objects.                                                                                                                                                                                                                                                 |
| `connectors.id`                                    | String         | Optional | Mutable   | The connector ID (or IDs) associated with the flow. Example connectors are `httpConnector`, `functionsConnector`, `pingOneVerifyConnector`, and `annotationConnector`.                                                                                                                                                                                                                                                                                                 |
| `createdAt`                                        | Time           | N/A      | Read only | The timestamp when the flow was created.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `currentVersion`                                   | Integer        | Optional | Immutable | The saved version of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `deployedAt`                                       | Time           | N/A      | Read only | The stamp when the flow was last deployed.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `description`                                      | String         | Optional | Mutable   | The description of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `enabled`                                          | Boolean        | Optional | Immutable | The state of the flow. This can be stored as its own value in the database or it can reflect an existing `flowStatus`.                                                                                                                                                                                                                                                                                                                                                 |
| `environment`                                      | Object         | N/A      | Read only | The DaVinci company ID (environment ID) object.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `environment.id`                                   | String         | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `graphData`                                        | Object         | Optional | Mutable   | The graph-based representation of the flow depicted in the UI.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `id`                                               | String         | N/A      | Read only | The flow ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `inputSchema`                                      | Array\[object] | Optional | Mutable   | The flow input parameters in an array of `JSONschema` objects. If the `trigger.type` property is `AUTHENTICATION`, then the flow is a PingOne flow, and the input schema properties are listed in this table. If the `trigger.type` property is not `AUTHENTICATION`, then the flow is not a PingOne flow and the input schema properties are described in [Input schema for non-PingOne flows data model properties](#input-schema-for-non-pingone-flows-data-model). |
| `inputSchema.propertyName`                         | String         | Required | Mutable   | If `inputSchema` is set, the input schema property name is a required property.                                                                                                                                                                                                                                                                                                                                                                                        |
| `inputSchema.description`                          | String         | Optional | Mutable   | The description for an input schema property.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `inputSchema.isExpanded`                           | Boolean        | Optional | Mutable   | Specifies whether the input schema is expanded in the response.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `inputSchema.preferredDataType`                    | String         | Required | Mutable   | If `inputSchema` is set, the data type of the input schema property is required. Options are `string`, `number`, `integer`, `boolean`, `array`, and `object`.                                                                                                                                                                                                                                                                                                          |
| `inputSchema.preferredControlType`                 | String         | Optional | Mutable   | The control type of the input schema property. Options are `textField`.                                                                                                                                                                                                                                                                                                                                                                                                |
| `inputSchema.required`                             | Boolean        | Optional | Mutable   | Specifies whether the input schema property is required for the flow.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `name`                                             | String         | Required | Mutable   | The name of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `outputSchema`                                     | Object         | Optional | Mutable   | The `JSONschema` output object of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `outputSchema.output`                              | Object         | Optional | Mutable   | The output object of the output schema.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `outputSchema.output.type`                         | String         | Optional | Mutable   | The output type.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `outputSchema.output.additionalProperties`         | Boolean        | Optional | Mutable   | Specifies whether the output has additional properties.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `outputSchema.output.properties`                   | Object         | Optional | Mutable   | A JSON object that specifies the output schema's properties.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `outputSchema.output.properties.{{propName}}`      | Object         | Optional | Mutable   | An output schema property definition.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `outputSchema.output.properties.{{propName}}.type` | Object         | Optional | Mutable   | An output schema property's data type.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `publishedVersion`                                 | Integer        | Optional | Immutable | The currently deployed version of the flow.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `settings`                                         | Object         | Optional | Mutable   | Flow settings saved by the user. Refer to the [Settings property data model](#settings-property-data-model) table for details.                                                                                                                                                                                                                                                                                                                                         |
| `trigger`                                          | Object         | Optional | Mutable   | The flow trigger object.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `trigger.type`                                     | String         | Optional | Mutable   | If the trigger type is set to `AUTHENTICATION`, you invoke the flow through PingOne OpenID Connect or SAML endpoints. The `AUTHENTICATION` trigger type overwrites the `inputSchema` values with the default authentication schema.                                                                                                                                                                                                                                    |
| `trigger.configuration`                            | Object         | Optional | Mutable   | The configuration object for session reuse.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `trigger.configuration.pwd`                        | Object         | Optional | Mutable   | The configuration object for password session reuse.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `trigger.configuration.pwd.enabled`                | Boolean        | Optional | Mutable   | Specifies whether this configuration must be used to check for existing sessions.                                                                                                                                                                                                                                                                                                                                                                                      |
| `trigger.configuration.pwd.lastSignOn`             | Integer        | Optional | Mutable   | An integer that specifies the duration (in seconds) that an active session can be reused.                                                                                                                                                                                                                                                                                                                                                                              |
| `trigger.configuration.mfa`                        | Object         | Optional | Mutable   | The configuration object for MFA session reuse.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `trigger.configuration.mfa.enabled`                | Boolean        | Optional | Mutable   | Specifies whether this configuration must be used to check for existing sessions.                                                                                                                                                                                                                                                                                                                                                                                      |
| `trigger.configuration.mfa.lastSignOn`             | Integer        | Optional | Mutable   | An integer that specifies the duration (in seconds) that an active session can be reused.                                                                                                                                                                                                                                                                                                                                                                              |
| `updatedAt`                                        | Date           | N/A      | Read only | The timestamp when the flow was updated or saved.                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Settings property data model

The following table lists the supported flow settings properties that can be used in the `settings` property.

| Property                          | Type    | Required | Mutable | Description                                                                                                                                                                                  |
| --------------------------------- | ------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `csp`                             | String  | Optional | Mutable | Content Security Policy content to which a `Content-Security-Policy` meta tag will be added. If you use a custom Javascript flow player, it is required.                                     |
| `css`                             | String  | Optional | Mutable | The CSS styling rules to be applied to the flow version.                                                                                                                                     |
| `cssLinks`                        | Array   | Optional | Mutable | A list of URL locations of CSS files to apply to the flow version.                                                                                                                           |
| `customErrorScreenBrandLogoUrl`   | String  | Optional | Mutable | The URL of the logo to use for the error page, such as "https\://example.com/logo.png".                                                                                                      |
| `customErrorShowFooter`           | Boolean | Optional | Mutable | Show footer in the error screen.                                                                                                                                                             |
| `customFaviconLink`               | String  | Optional | Mutable | The URL of the favicon image to use for the page. This image is displayed in the title bar of the browser and in saved bookmarks.                                                            |
| `customLogoUrlSelection`          | String  | Optional | Mutable | The URL location of the logo to show on error pages.                                                                                                                                         |
| `customTitle`                     | String  | Optional | Mutable | The title of the page. This title is displayed in the title bar of the browser and used for the page title in search engine results.                                                         |
| `doNotSubstituteUnreplacedFields` | Boolean | Optional | Mutable | By default, unreplaced parameterized fields will be substituted with an empty string. This parameter overrides that behavior if set to true.                                                 |
| `flowHttpTimeoutInSeconds`        | Number  | Optional | Mutable | Timeout period for every node's execution time. A response must be returned by a node before this timeout. The default value is 15 seconds. If set to 0, the default timeout value is used.  |
| `flowTimeoutInSeconds`            | Number  | Optional | Mutable | The period after which a particular flow execution becomes inactive. The default value is 300 seconds. If set to 0, the default timeout value is used.                                       |
| `intermediateLoadingScreenCss`    | String  | Optional | Mutable | The CSS rules to use for the intermediate page. This setting applies only when the show intermediate page setting is enabled (`useIntermediateLoadingScreen`).                               |
| `intermediateLoadingScreenHtml`   | String  | Optional | Mutable | The HTML content of the intermediate page. Applies only when the show intermediate page is enabled (`useIntermediateLoadingScreen`).                                                         |
| `jsLinks`                         | Array   | Optional | Mutable | The location of JavaScript files to apply to the flow.                                                                                                                                       |
| `logLevel`                        | String  | Optional | Mutable | The log level for flow analytics. Options are `None`, `Info`, or `Debug`.                                                                                                                    |
| `pingOneFlow`                     | Boolean | Optional | Mutable | PingOne runs this flow for OIDC or SAML authentication. When a flow is invoked, PingOne sends input parameters to be made available for any node in the flow.                                |
| `requireAuthenticationToInitiate` | Boolean | Optional | Mutable | Flow invocation via OpenID requires authentication. Use the `/sdktoken` endpoint to retrieve the `accessToken` value, which can be sent in the query parameter `&accessToken=<accessToken>`. |
| `scrubSensitiveInfo`              | Boolean | Optional | Mutable | Remove sensitive information from analytics.                                                                                                                                                 |
| `sensitiveInfoFields`             | Array   | Optional | Mutable | These fields will be masked with **\***\* in Flow analytics.                                                                                                                                 |
| `useCsp`                          | Boolean | Optional | Mutable | Enable and add a content security policy if you are adding additional scripts.                                                                                                               |
| `useCustomCss`                    | Boolean | Optional | Mutable | When enabled, DaVinci uses the CSS rules in the custom CSS field.                                                                                                                            |
| `useCustomScript`                 | Boolean | Optional | Mutable | When enabled, DaVinci uses the JavaScript files in the JavaScript files field.                                                                                                               |
| `useIntermediateLoadingScreen`    | Boolean | Optional | Mutable | When enabled, DaVinci shows a custom user-facing page between each node in the flow.                                                                                                         |

### Input schema for non-PingOne flows data model properties

| Property                           | Type    | Required | Mutable | Description                                                                                                              |
| ---------------------------------- | ------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------ |
| `inputSchema.propertyName`         | String  | Required | Mutable | An input schema property name.                                                                                           |
| `inputSchema.description`          | String  | Optional | Mutable | The description for an input schema property.                                                                            |
| `inputSchema.isExpanded`           | Boolean | Optional | Mutable | Specifies whether the input schema is expanded in the response.                                                          |
| `inputSchema.preferredDataType`    | String  | Required | Mutable | The data type of the input schema property. Options are `string`, `number`, `integer`, `boolean`, `array`, and `object`. |
| `inputSchema.preferredControlType` | String  | Optional | Mutable | The control type of the input schema property. Options are `textField`.                                                  |
| `inputSchema.required`             | Boolean | Optional | Mutable | Specifies whether the input schema property is required for the flow.                                                    |

## Limiting and filtering data

You can limit the number of results returned on the [Read DaVinci Flows](read-flows.html) and [Read One DaVinci Flow](read-one-flow.html) requests with the `attributes` parameter. This parameter filters the response data returned by the request. The query accepts top-level DaVinci admin flow data model properties as a list of comma separated values. The query returns only the specified property values; it removes all other properties from the response. For example, the following request uses the `attributes` query parameter:

`/v1/environments/{{envID}}/flows/{{davinciFlowID}}?attributes=name,description`

The response returns the following flow data:

```json
{
   "_links": {...},
   "id": "{{resourceID}}",
   "name": "SomeFlow,
   "description": "A brief description"
}
```

### SCIM operators

These SCIM operators can be applied to the following attributes:

* `eq` (equals)

  Supports attributes of type `STRING`, `DATE`, `NUMBER`, and `BOOLEAN`.

* `gt` (greater than)

  Supports attributes of type `DATE` and `NUMBER`.

* `ge` (greater than or equal to)

  Supports attributes of type `DATE` and `NUMBER`.

* `lt` (less than)

  Supports attributes of type `DATE` and `NUMBER`.

* `le` (less than or equal to)

  Supports attributes of type `DATE` and `NUMBER`.

* `sw` (starts with)

  Supports attributes of type `STRING`.

* `ew` (ends with)

  Supports attributes of type `STRING`.

* `co` (contains)

  Supports attributes of type `STRING`.

* `within` (within a specified date)

  Supports attributes of type `DATE`.

* `and` (logical AND)

  Logical AND for building compound expressions in which both expressions are true.

* `or` (logical OR)

  Logical OR for building compound expressions if either expression is true.

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci flow errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci flow operations can return the following errors:

| HTTP status | Top‑level code     | Detail code                                                         | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------- | ------------------ | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows`, a `PUT /environments/{envID}/flows/{davinciFlowID}`, or a `PUT /environments/{envID}/flows/{davinciFlowID}/enabled` request supplies a body that violates the data model: an omitted `name` property on create or update, an omitted `enabled` property on enable or disable, a `trigger` object without a `type` property, an `inputSchema` entry without a `propertyName` or `preferredDataType` property, an empty or blank `name`, a `name` or `description` value longer than 256 or 1024 characters respectively, a `name` value that starts with an unsupported character or contains a `<` or a `${` sequence, a `trigger.type` value other than `AUTHENTICATION` or `SCHEDULE` on create or update, a `trigger.subtype` value other than `CIBA`, an `inputSchema.preferredDataType` value other than `string`, `number`, `boolean`, `array`, or `object`, an `inputSchema.preferredControlType` value outside the supported control type list, an `enabled` value that is not a boolean, or a property whose value is not of the documented JSON type
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'name'` with target `name` when a create or update request omits `name`, and `must have required property 'enabled'` with target `enabled` when an enable or disable request omits `enabled`. `must have required property 'type'` with target `trigger` when the `trigger` object omits `type`, and `must have required property 'propertyName'` or `must have required property 'preferredDataType'` with the entry path as the target, for example `inputSchema.0`, when an `inputSchema` entry omits either property. `must not be empty or blank` for an empty or blank `name`. `must NOT have more than 256 characters` for a `name` longer than 256 characters and `must NOT have more than 1024 characters` for a `description` longer than 1024 characters. `must match pattern "<pattern>"`, where \<pattern> is the schema pattern for the property, for a `name` or `description` value that starts with an unsupported character or contains a `<` or a `${` sequence. `must be one of the values: AUTHENTICATION or SCHEDULE` for an unknown `trigger.type` value, `must be one of the values: CIBA` for an unknown `trigger.subtype` value, `must be one of the values: string or number or boolean or array or object` for an unknown `inputSchema.preferredDataType` value, and the analogous `must be one of the values: <allowed control types>` literal for an unknown `inputSchema.preferredControlType` value. `must be boolean` for a non-boolean `enabled` or `inputSchema.required` value, `must not be empty or blank` for an `enabled` value of null, and `must be string` for a property of the wrong JSON type, for example with target `name`. |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/flows` or a `GET /environments/{envID}/flows/{davinciFlowID}` request supplies an `attributes` query parameter longer than 500 characters or an `expand` query parameter longer than 100 characters
>
> **Details:** Detail code `INVALID_PARAMETER` with message `must NOT have more than 500 characters` and target `attributes` for an overlong `attributes` parameter, or message `must NOT have more than 100 characters` and target `expand` for an overlong `expand` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `Invalid attribute provided for sorting`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/flows` request supplies an `order` query parameter that names an attribute other than `name`, `updatedAt`, `createdAt`, `deployedAt`, `enabled`, `trigger.type`, `settings.logLevel`, `publishedVersion`, or `currentVersion`
>
> **Details:** Detail code `INVALID_PARAMETER` with message:
>
> ```
> Invalid attribute provided for sorting: valid parameters are name, updatedAt, createdAt, deployedAt, enabled, trigger.type, settings.logLevel, publishedVersion, currentVersion
> ```
>
> and target `order`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `Invalid page size provided`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/flows` request supplies a `limit` query parameter that is not a positive integer or is greater than 100
>
> **Details:** Detail code `INVALID_PARAMETER` with message `Invalid page size provided: page size ranges from 1 to 100` and target `limit`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`                                                     | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows` or a `PUT /environments/{envID}/flows/{davinciFlowID}` request sets `trigger.type` to `SCHEDULE` or `BATCH_PROCESSING_SUBFLOW` in an environment where the corresponding scheduled flows or batch processing feature flag is disabled
>
> **Details:** Detail code `INVALID_VALUE` with message `must be one of the values: AUTHENTICATION` and target `trigger.type` for a scheduled flow in an environment where scheduled flows are not enabled, or message `must be one of the values: AUTHENTICATION, SCHEDULE` and target `trigger.type` for a batch processing subflow in an environment where batch processing is not enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 400         | `INVALID_DATA`     | `UNIQUENESS_VIOLATION`                                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows`, a `POST /environments/{envID}/flows/{davinciFlowID}` clone request with a `name` property, or a flow import request uses a flow name that already exists in the environment. Import requests additionally return this error when two flows in the same import payload share a name, when a payload subflow name collides with the main flow name, or when a payload subflow name matches a flow that already exists in the environment
>
> **Details:** Detail code `UNIQUENESS_VIOLATION`. Create, clone, and main-flow import collisions return message `A flow with that name already exists, or the provided name isn't valid. Check the flow names and try again.` An import payload with two subflows of the same name returns message `The import contains more than one subflow with the same name: "<name>". Rename one of the subflows and try again.` A subflow whose name matches the main flow returns message `The import contains a subflow with the same name as the main flow: "<name>". Rename one of them and try again.` A subflow colliding with an existing environment flow returns message `A flow with the name "<name>" already exists. Rename the subflow and try again.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 400         | `REQUEST_FAILED`   | `INVALID_PARAMETER` or `INVALID_FILTER`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/flows` request supplies a `filter` query parameter that references an attribute outside the filterable set, an operator that the filtered attribute does not support, or an actor attribute such as `createdBy.user.id` when actor metadata is disabled for the environment. The filterable attributes are `name`, `description`, `currentVersionAlias`, `publishedVersionAlias`, `enabled`, `trigger.type`, `createdAt`, `updatedAt`, `deployedAt`, and `settings.logLevel`, plus the actor identifier attributes when actor metadata is enabled. String attributes support `eq`, `and`, `or`, `sw`, `co`, and `ew`, date attributes support `eq`, `and`, `or`, `gt`, `ge`, `lt`, and `le`, and boolean attributes and actor attributes support only `eq` combined through `and` or `or`
>
> **Details:** Detail code `INVALID_PARAMETER` with message `The filter attribute was invalid or does not support filtering.` and the invalid attribute as the target, or message `The filter operator was invalid or not supported.` and the attribute that does not support the supplied operator as the target. A filter that is not a well-formed SCIM expression returns detail code `INVALID_FILTER` with message `The specified filter was invalid.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 400         | `REQUEST_FAILED`   | `ITEM_LIMIT_EXCEEDED`                                               | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows` create, clone, or import request runs after the environment has reached the maximum number of flows allowed for the environment
>
> **Details:** Detail code `ITEM_LIMIT_EXCEEDED` with message `Flow limit is exceeded` and no target. The limit preflight runs ahead of the duplicate-name check, so an over-limit environment returns this error even when the request also reuses an existing flow name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `DELETE /environments/{envID}/flows/{davinciFlowID}` request targets a flow that an application flow policy currently references
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `This Flow is in a Application Flow Policy` and no target. Remove the flow from the application's flow policy before deleting it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows/{davinciFlowID}` validate request targets a flow that has no `graphData`, or a `PUT /environments/{envID}/flows/{davinciFlowID}` request includes a flow graph whose subflow node references the flow being updated. A `PUT` request also returns this error when the stored previous flow version or the flow's current version record cannot be found during the version diff
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `Flow is empty` for a validate request on a flow without `graphData`, message `Flow validation error` for a self-referencing subflow graph, and message `Flow version not found` for a missing previous version record. None of these details carry a target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT /environments/{envID}/flows/{davinciFlowID}` update request or a `POST /environments/{envID}/flows/{davinciFlowID}/versions/{davinciFlowVersionID}` revert request is rejected on schedule-trigger transition grounds: a scheduled flow cannot be changed to a non-scheduled flow and a non-scheduled flow cannot be changed to a scheduled flow. A create, update, or import request that sets `trigger.type` to `SCHEDULE` also returns this error when the flow graph has no `graphData`, when the graph has no single START node, or when the START node has more than one connected edge
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `A schedule flow cannot be changed to a non-schedule flow` or `A non-schedule flow cannot be changed to a schedule flow` and no target, or with message `The flow graph cannot be empty` with target `graphData` for a scheduled flow whose graph has no nodes, message `There can only be one start node` with target `graphData` for a graph whose START node count is not one, or message `The start node can only have one edge connected to it` with target `graphData` for a START node with more than one edge.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT /environments/{envID}/flows/{davinciFlowID}` request changes the trigger type of a batch processing subflow away from `BATCH_PROCESSING_SUBFLOW`, or changes any other flow's trigger type to `BATCH_PROCESSING_SUBFLOW`
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `A batch processing flow cannot be changed to a non-batch processing flow.` or `A non-batch processing flow cannot be changed to a batch processing flow.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `DELETE /environments/{envID}/flows/{davinciFlowID}` or a `PUT /environments/{envID}/flows/{davinciFlowID}` request targets a flow whose `readOnly` attribute is set, such as a flow exported by Ping Identity for a customer
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `Flow is read-only.` and target `readOnly`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED`   | `INVALID_VALUE`                                                     | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT /environments/{envID}/flows/{davinciFlowID}` request supplies flow settings that violate content security policy validation: enabling `shouldEnforceCsp` without an `enforcedCsp` value, enabling `shouldReportCspViolations` without a valid HTTPS `cspReportUri`, omitting `reportOnlyCsp` when violation reporting is enabled, supplying an `enforcedCsp` or `reportOnlyCsp` value that fails CSP linting, or supplying any CSP setting when the environment has no custom domain configured
>
> **Details:** Detail code `INVALID_VALUE` with message `A custom domain is required to modify content security policy settings.` and target `settings` when the environment has no custom domain, with message `Report destination URL must be a valid HTTPS URL or relative path when reporting CSP violations is enabled.` and target `settings.cspReportUri`, with message `Enforced CSP value is invalid: CSP linting failed.` and target `settings.enforcedCsp`, or with message `Report-only CSP value is invalid: CSP linting failed.` and target `settings.reportOnlyCsp`. Detail code `EMPTY_VALUE` with message `Enforced CSP Value is required when Enforce Content Security Policy is enabled.` and target `settings.enforcedCsp`, or with message `Report-only CSP value cannot be empty when reporting CSP violations is enabled.` and target `settings.reportOnlyCsp`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`                                                     | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows` create or import request or a `PUT /environments/{envID}/flows/{davinciFlowID}` update request includes a flow graph node whose variable name is the reserved JavaScript name `proto`, `prototype`, or `constructor`
>
> **Details:** Detail code `INVALID_VALUE` with message `Cannot create variable with this name` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`                                                    | **Message:** `The request is missing a required value.`> **Collapse: When and details**
>
> **When:** A flow import request supplies a payload without a `flow` object on the `application/vnd.pingidentity.flow.import+json` content type, or without a `flowInfo` or `flowNameMapping` object on the `application/vnd.pingidentity.flow.import.legacy+json` content type
>
> **Details:** Detail code `REQUIRED_VALUE` with message `must have required property 'flow'` for the standard import content type, or `must have required property 'flowInfo'` or `must have required property 'flowNameMapping'` for the legacy import content type, each with the omitted property as the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE` or `INVALID_VALUE`                                 | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A flow import request fails against the imported flow's contents: a connector ID listed in the payload does not identify a connector present in the environment, or the payload omits the `connectorIds` list
>
> **Details:** Detail code `REQUIRED_VALUE` with message `Flow template - no connectorIds found` when the payload omits `connectorIds`. Detail code `INVALID_VALUE` with message `Error importing flow. The Connectors are not present in environment [<connector id list>]` for unavailable connectors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 400         | `INVALID_DATA`     | `UNIQUENESS_VIOLATION`                                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A flow import request includes a form whose name matches a form that already exists in the environment
>
> **Details:** Detail code `UNIQUENESS_VIOLATION` with message `Failed to import form: uniqueness violation` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED`   | `ITEM_LIMIT_EXCEEDED`                                               | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A flow import request would push the environment past the maximum number of forms allowed for the environment
>
> **Details:** Detail code `ITEM_LIMIT_EXCEEDED` with message `Failed to import forms: the maximum number of forms permitted in this environment would be exceeded.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 403         | `ACCESS_FAILED`    | `INSUFFICIENT_PERMISSIONS`                                          | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows` create or import request sets `trigger.type` to `SCHEDULE` or `BATCH_PROCESSING_SUBFLOW` in an environment that is not licensed for scheduled flows. The create and import paths check the license; update, clone, and deploy requests do not
>
> **Details:** Detail code `INSUFFICIENT_PERMISSIONS` with message `You do not have permissions or are not licensed to make this request.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 403         | `ACCESS_FAILED`    | `INSUFFICIENT_PERMISSIONS`                                          | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** A flow import request includes forms that the environment lacks the permissions to import
>
> **Details:** Detail code `INSUFFICIENT_PERMISSIONS` with message `Failed to import flow with form(s): invalid permissions` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 403         | `ACCESS_FAILED`    | None                                                                | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:create:dvFlows` permission (`POST` operations), the `davinci:read:dvFlows` permission (`GET` operations), the `davinci:update:dvFlows` permission (`PUT` operations), or the `davinci:delete:dvFlows` permission (`DELETE` operations)
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 404         | `NOT_FOUND`        | None                                                                | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `GET` one, `PUT`, `DELETE`, `POST` clone, deploy, or validate request, or a `PUT /environments/{envID}/flows/{davinciFlowID}/enabled` request, references a flow ID that does not exist in the environment
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 415         | `INVALID_REQUEST`  | None                                                                | **Message:**```
The server is refusing to service the request because the entity of the request is in a format not supported by the requested resource for the requested method.
```> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/flows/{davinciFlowID}` request does not set the `Content-Type` header to one of `application/vnd.pingidentity.flow.clone+json` for clone, `application/vnd.pingidentity.flow.deploy+json` for deploy, or `application/vnd.pingidentity.flow.validate+json` for validate
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 500         | `UNEXPECTED_ERROR` | None                                                                | **Message:** `There was an unexpected error with the service. Please try again later.`> **Collapse: When and details**
>
> **When:** The service encounters an unexpected internal failure while processing a flow operation, including a create, clone, import, or update whose internal processing fails after validation, a `POST` validate request whose DV Linter evaluation returns no lint results, and a flow import request that supplies batch processing subflows or streaming capability nodes while the batch processing feature flag is disabled for the environment
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

---

---
title: DaVinci Admin UI Templates
description: Describes the PingOne DaVinci Admin UI Templates service for creating, reading, and deleting custom branded UI templates used in DaVinci flows
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-ui-templates/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-ui-templates/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-ui-templates-data-model: DaVinci Admin UI templates data model properties
  response-codes: Response codes
  davinci-ui-template-errors: DaVinci UI template errors
---

# DaVinci Admin UI Templates

You can create user interface (UI) templates that match your company style and branding, which you can include in flows using an HTTP connector. The PingOne DaVinci Admin UI Templates service provides endpoints to create, read, and delete DaVinci UI templates.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci Admin UI templates data model properties

| Property                          | Type   | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | ------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `createdAt`                       | Date   | N/A      | Read only | A UTC string that specifies the time when the DaVinci UI template was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `description`                     | String | Optional | Mutable   | The UI template description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `environment`                     | Object | N/A      | Read only | The DaVinci company ID (environment ID) object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `environment.id`                  | String | N/A      | Read only | The DaVinci company ID, which is the PingOne environment ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `id`                              | String | N/A      | Read only | The DaVinci UI template ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `name`                            | String | Required | Mutable   | The UI template name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `inputSchema`                     | String | Optional | Mutable   | A JSON representation of the input schema defined in this template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `outputSchema`                    | String | Optional | Mutable   | A JSON representation of the output schema defined in this template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `script`                          | String | Optional | Mutable   | Javascript code utilized by this template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `style`                           | String | Optional | Mutable   | The CSS used in flows that are associated with this template.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `template`                        | String | Optional | Mutable   | The HTML template to me rendered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `updatedAt`                       | Date   | N/A      | Read only | A UTC string that specifies the time when the UI template was last modified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `validationRules`                 | Array  | Optional | Mutable   | The validation rules object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `validationRules.propertyName`    | String | Required | Mutable   | The name of the property to which the validation rule applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `validationRules.rules`           | Array  | Required | Mutable   | The rules object in which the validation rules elements are defined.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `validationRules.rules.ruleName`  | String | Required | Mutable   | The name of the rule. Options are `presence`, `email`, `length`, `format`, and `equality`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `validationRules.rules.message`   | String | Optional | Mutable   | The rule message that displays if the required property is not present or if the property is not a valid email. For `length` rules, enter a minimum, maximum, or exact value for the property and a validation message that is displayed for each length restriction that is not met. For `format` rules, enter the regex that defines the required format and the validation message that displays if the property does not match the format. For `equality` rules, enter the other property that this property must match, and the validation message that displays if the properties do not match. |
| `validationRules.rules.attribute` | String | Optional | Mutable   | The property to check when applying the `equality` rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `validationRules.rules.pattern`   | String | Optional | Mutable   | The pattern to match when applying the `format` rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci UI template errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci UI template operations can return the following errors:

| HTTP status | Top‑level code   | Detail code                                                         | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | ---------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400         | `INVALID_DATA`   | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/uiTemplates` or a `PUT /environments/{envID}/uiTemplates/{davinciTemplateID}` request supplies a body that violates the data model: an omitted `name`, a `name` or a `validationRules` entry `propertyName` longer than 100 characters, a blank `name`, a `name` or `propertyName` whose first non-whitespace character is outside the allowed set or that contains a `<` or a `${` sequence, a `description` longer than 3000 characters, a `name` or `description` value that is not a string, a `validationRules` entry without a `propertyName`, a `validationRules.rules` array with no entries, or a `validationRules.rules` entry without a `ruleName` or with a `ruleName` other than `presence`, `email`, `length`, `format`, or `equality`
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'name'` with target `name` when the request omits `name`. `must NOT have more than 100 characters` for a `name` or `propertyName` longer than 100 characters and `must NOT have more than 3000 characters` for a `description` longer than 3000 characters. `must not be empty or blank` for a blank `name`. `must match pattern "<pattern>"`, where the pattern is the JSON schema pattern for the property, for a `name` or a `validationRules` entry `propertyName` whose first non-whitespace character is outside the allowed set or that contains a `<` or a `${` sequence. `must be string` for a property of the wrong JSON type. `must have required property 'propertyName'` with the entry path as the target, for example `validationRules.0`, when an entry omits `propertyName`. `must NOT have fewer than 1 items` for an empty `validationRules.rules` array. `must have required property 'ruleName'` with the rule path as the target, for example `validationRules.0.rules.0`, when a rule omits `ruleName`. `must be one of the values: presence or email or length or format or equality` for an unknown `ruleName` value. |
| 400         | `INVALID_DATA`   | `INVALID_PARAMETER` or `INVALID_VALUE`                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET` all UI templates request or a `GET` one UI template request supplies an `expand` query parameter longer than 100 characters or a `filter` query parameter longer than 256 characters, or a `DELETE` request includes any query parameter
>
> **Details:** For an overlong query parameter on a `GET` request, detail code `INVALID_PARAMETER` with message `must NOT have more than 100 characters` for `expand` or `must NOT have more than 256 characters` for `filter`, with the overlong parameter as the target. For any query parameter on a `DELETE` request, detail code `INVALID_VALUE` with message `must NOT have additional properties` and the rejected parameter as the target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED` | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` request creates a UI template after the environment has reached the maximum number of UI templates allowed for the environment
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `Cannot create more than 100 UI templates.` No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 400         | `REQUEST_FAILED` | `INVALID_PARAMETER` or `INVALID_FILTER`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `GET` all UI templates request supplies a `filter` query parameter that references an attribute other than `createdBy.user.id`, `createdBy.client.id`, `createdBy.environment.id`, `updatedBy.user.id`, `updatedBy.client.id`, or `updatedBy.environment.id`, or an operator other than `eq`, `and`, or `or`, when actor metadata is enabled for the environment. When actor metadata is disabled, every `filter` value is rejected
>
> **Details:** Detail code `INVALID_PARAMETER` with message `The filter attribute was invalid or does not support filtering.` and the invalid attribute as the target, or message `The filter operator was invalid or not supported.` and the invalid operator as the target. A filter that is not a well-formed SCIM expression returns detail code `INVALID_FILTER` with message `The specified filter was invalid.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 403         | `ACCESS_FAILED`  | None                                                                | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:create:uiTemplates` permission (`POST` operations), the `davinci:read:uiTemplates` permission (`GET` operations), the `davinci:update:uiTemplates` permission (`PUT` operations), or the `davinci:delete:uiTemplates` permission (`DELETE` operations)
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 404         | `NOT_FOUND`      | None                                                                | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `GET` one, a `PUT`, or a `DELETE` request references a UI template ID that does not exist in the environment
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

---

---
title: DaVinci Admin Variables
description: Describes the PingOne DaVinci Admin Variables service for creating, reading, updating, and deleting DaVinci variables and their context types
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-variables/index
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-variables/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-variable-data-model-properties: DaVinci Admin variable data model properties
  limiting-and-filtering-data: Limiting and filtering data
  response-codes: Response codes
  davinci-variable-errors: DaVinci variable errors
---

# DaVinci Admin Variables

The PingOne DaVinci Admin Variables service provides endpoints to create, read, update, and delete DaVinci variables. Variables are values that can be read and modified during a flow. Every variable has a context, which determines how widely its value is shared.

The options for the variable's context types are:

* `flow`

  The variable is tied to a specific flow and has a single, persistent value until that value is changed.

* `flowInstance`

  The variable can be used in multiple flows.

  * If the variable's value is set within a flow, the variable instance in that flow gets the value set by the flow's execution.

  * If the variable's value is not set within a flow, the variable instance in that flow inherits the value.

* `user`

  The variable has a separate value for each user. If you use a variable with this context in a flow, the user must be identified.

* `company`

  The variable has a single value for the company. This value is used in all flows and for all users.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../../platform/roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../../../platform/group-role-assignments/index.html).

* [User Role Assignments](../../../platform/users/user-role-assignments/index.html).

Refer to [Roles Management](../../../platform/roles/index.html) for more information.

## DaVinci Admin variable data model properties

| Property         | Type                         | Required  | Mutable   | Description                                                                                                                                                                                         |
| ---------------- | ---------------------------- | --------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `createdAt`      | Date                         | N/A       | Read only | The time when the variable was created.                                                                                                                                                             |
| `context`        | String                       | Required  | Immutable | The context or type of the variable. Options are `flow`, `flowInstance`, `user`, or `company`.                                                                                                      |
| `dataType`       | String                       | Required  | Mutable   | Data type of the variable. Can be `STRING`, `BOOLEAN`, `NUMBER`, `SECRET`, or `OBJECT`. The `context` property must be set to `company` to use `SECRET` as the value for the `dataType` property.   |
| `displayName`    | String                       | Optional  | Mutable   | A human-readable variable name set in the request.                                                                                                                                                  |
| `environment`    | Object                       | N/A       | Read only | The DaVinci company ID (environment ID) object.                                                                                                                                                     |
| `environment.id` | String                       | N/A       | Read only | The DaVinci company ID, which is the PingOne environment ID.                                                                                                                                        |
| `flow`           | Object                       | Immutable | Optional  | The flow object specifying the DaVinci flow associated with the variable. This is a required property when `context` is set to `flow`. It is ignored when `context` is set to any other option.     |
| `flow.id`        | String                       | Immutable | Optional  | The flow ID of the DaVinci flow associated with the variable. This is a required property when `context` is set to `flow`. It is ignored when `context` is set to any other option.                 |
| `id`             | String                       | N/A       | Read only | The variable ID.                                                                                                                                                                                    |
| `max`            | Integer                      | Optional  | Mutable   | The maximum value of the variable. The default value is 2000.                                                                                                                                       |
| `min`            | Integer                      | Optional  | Mutable   | The minimum value of the variable. The default value is 0.                                                                                                                                          |
| `mutable`        | Boolean                      | Optional  | Mutable   | Specifies whether the variable is mutable, which allows nodes within a flow to change the value of the variable. If the `value` property is null, this property is required.                        |
| `name`           | String                       | Required  | Immutable | The variable name.                                                                                                                                                                                  |
| `updatedAt`      | Date                         | N/A       | Read only | The time when the variable was modified.                                                                                                                                                            |
| `value`          | String/Number/Boolean/Object | Optional  | Mutable   | An internally stored value that is part of a HashMap/Object. If the `mutable` property is set to `false`, this property is required. If `mutable` is not set on the request, it defaults to `true`. |

## Limiting and filtering data

These SCIM operators can be applied to the following attributes:

* `eq` (equals)

  Supports attributes of type `STRING` and `BOOLEAN`.

* `sw` (starts with)

  Supports attributes of type `STRING`.

* `ew` (ends with)

  Supports attributes of type `STRING`.

* `co` (contains)

  Supports attributes of type `STRING`.

* `and` (logical AND)

  Logical AND for building compound expressions in which both expressions are true.

* `or` (logical OR)

  Logical OR for building compound expressions if either expression is true.

For information about paging and ordering the response for [Read All DaVinci Variables](read-variables.html), refer to [Paging and ordering collections](../../../platform/reference/paging-ordering-collections.html).

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## DaVinci variable errors

In addition to the general [error codes](../../../platform/reference/error-codes.html), DaVinci variable operations can return the following errors:

| HTTP status | Top‑level code     | Detail code                                                         | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------- | ------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`, `EMPTY_VALUE`, `INVALID_VALUE`, or `OUT_OF_RANGE` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /environments/{envID}/variables` or a `PUT /environments/{envID}/variables/{davinciVariableID}` request supplies a body that violates the data model: an omitted `name`, `context`, `dataType`, or `mutable` property, a `flow` object without an `id` property, a `name` or `displayName` longer than 256 characters, an empty or blank `name` or `displayName`, a `name`, `displayName`, or `flow.id` value that starts with an unsupported character or contains a `<` or a `${` sequence, a `context` value other than `flow`, `flowInstance`, `company`, or `user`, a `dataType` value other than `string`, `number`, `object`, `boolean`, or `secret`, or a property whose value is not of the documented JSON type
>
> **Details:** One detail per validation error, each with the failing property path as the target. `must have required property 'name'`, `must have required property 'context'`, `must have required property 'dataType'`, or `must have required property 'mutable'` with the omitted property as the target when the request omits that property, and `must have required property 'id'` with target `flow` when the request supplies a `flow` object without an `id` property. `must NOT have more than 256 characters` for a `name` or `displayName` longer than 256 characters. `must not be empty or blank` for an empty or blank `name` or `displayName`. `must match pattern "<pattern>"`, where \<pattern> is the schema pattern, for a `name`, `displayName`, or `flow.id` value that starts with an unsupported character or contains a `<` or a `${` sequence. `must be one of the values: flow or flowInstance or company or user` for an unknown `context` value and `must be one of the values: string or number or object or boolean or secret` for an unknown `dataType` value. `must be string` for a property that must be a string, for example with target `name`, `must be boolean` for a `mutable` value that is not a boolean, `must be integer` for a `min` or `max` value that is not an integer, and `must be string,number,boolean,object` for a `value` that is not one of those types. |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/variables` or a `GET /environments/{envID}/variables/{davinciVariableID}` request supplies an `expand` query parameter longer than 100 characters or a `filter` query parameter longer than 256 characters
>
> **Details:** Detail code `INVALID_PARAMETER` with message `must NOT have more than 100 characters` and target `expand` for an overlong `expand` parameter, or message `must NOT have more than 256 characters` and target `filter` for an overlong `filter` parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `Invalid attribute provided for sorting`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/variables` request supplies an `order` query parameter that names an attribute other than `name`, `createdAt`, `context`, `value`, `dataType`, or `updatedAt`
>
> **Details:** Detail code `INVALID_PARAMETER` with message `Invalid attribute provided for sorting: valid parameters are name, createdAt, context, value, dataType, updatedAt` and target `order`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 400         | `INVALID_DATA`     | `INVALID_PARAMETER`                                                 | **Message:** `Invalid page size provided`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/variables` request supplies a `limit` query parameter that is not a positive integer or is greater than 100
>
> **Details:** Detail code `INVALID_PARAMETER` with message `Invalid page size provided: page size ranges from 1 to 100` and target `limit`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`                                                     | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` request that sets `dataType` to `secret` while `context` is anything other than `company`, a `PUT` request that sets `dataType` to `secret` for a variable whose context is not `company`, or a `POST` request that uses the reserved variable name `proto`, `prototype`, or `constructor`
>
> **Details:** Detail code `INVALID_VALUE` with message `'Secret' type is only available for company variables` for a secret data type outside the company context, or message `Cannot create variable with this name` for a reserved name. No target is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 400         | `INVALID_DATA`     | `REQUIRED_VALUE`                                                    | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` request sets `context` to `flow` without a `flow.id` property in the request body
>
> **Details:** Detail code `REQUIRED_VALUE` with message `must have required property 'flow.id'` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 400         | `INVALID_DATA`     | `UNIQUENESS_VIOLATION`                                              | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` request creates a variable whose name and context combination already exists in the environment
>
> **Details:** Detail code `UNIQUENESS_VIOLATION` with message `Construct already exists` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `REQUEST_FAILED`   | `INVALID_PARAMETER` or `INVALID_FILTER`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `GET /environments/{envID}/variables` request supplies a `filter` query parameter that references an attribute other than `context`, `name`, `value`, `createdAt`, or `updatedAt`, an operator that the filtered attribute does not support, or an actor attribute such as `createdBy.user.id` when actor metadata is disabled for the environment. When actor metadata is enabled, actor attributes support only `eq` combined through `and` or `or`
>
> **Details:** Detail code `INVALID_PARAMETER` with message `The filter attribute was invalid or does not support filtering.` and the invalid attribute as the target, or message `The filter operator was invalid or not supported.` and the invalid operator or the attribute that does not support it as the target. A filter that is not a well-formed SCIM expression returns detail code `INVALID_FILTER` with message `The specified filter was invalid.` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                                              | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` request creates a variable after the environment has reached the maximum number of variables allowed for the environment
>
> **Details:** Detail code `CONSTRAINT_VIOLATION` with message `Cannot create more constructs due to resource limit` and no target.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 403         | `ACCESS_FAILED`    | None                                                                | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** The actor lacks the `davinci:create:constructs` permission (`POST` operations), the `davinci:read:constructs` permission (`GET` operations), the `davinci:update:constructs` permission (`PUT` operations), or the `davinci:delete:constructs` permission (`DELETE` operations)
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 404         | `NOT_FOUND`        | None                                                                | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `GET` one, `PUT`, or `DELETE` request references a variable ID that does not exist in the environment
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 500         | `UNEXPECTED_ERROR` | None                                                                | **Message:** `There was an unexpected error with the service. Please try again later.`> **Collapse: When and details**
>
> **When:** The service encounters an unexpected internal failure while processing a variable operation, including a create or update whose variable value exceeds the 1 MB per-variable size limit when size-limit enforcement is enabled for the environment
>
> **Details:** None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

---

---
title: DaVinci and backend flows
description: For backend-initiated PingOne DaVinci flows, you use the direct API method to trigger flow orchestration without any user interface components. This is ideal for actions such as automated risk checks or account provisioning. You configure the flow to accept and return JSON data from the API. The flow terminates with an HTTP Connector node using the Send Success JSON Response capability to return data back to your backend.
component: pingone-api
page_id: pingone-api:davinci:getting-started-with-davinci/backend-flows
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/getting-started-with-davinci/backend-flows.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why-use-davinci-backend-flows: Why use DaVinci backend flows
  backend-use-cases: Backend use cases
---

# DaVinci and backend flows

For backend-initiated PingOne DaVinci flows, you use the direct API method to trigger flow orchestration without any user interface components. This is ideal for actions such as automated risk checks or account provisioning. You configure the flow to accept and return JSON data from the API. The flow terminates with an HTTP Connector node using the `Send Success JSON Response` capability to return data back to your backend.

If the flow requires further steps or is part of a larger journey, the response could include a `flowResponse` object with instructions for the next action.

## Why use DaVinci backend flows

DaVinci backend flows (initiated through API calls) are designed for automation and background processing. The benefits include:

* **Security:** Running logic on the backend protects sensitive business rules and data consistency, ensuring that critical security decisions are not exposed to or manipulated by the frontend environment.

* **Consistency:** A single backend flow can serve multiple different frontends (web, mobile), providing consistency for identity logic regardless of the device.

* **Integration:** Backend flows can connect incompatible systems or custom databases to orchestrate complex security responses across an entire environment.

* **Headless Operations:** You can perform migrations or background account updates without interrupting a user session or forcing users to complete specific UI actions.

## Backend use cases

The following table provides guidance on when to implement a backend orchestration solution compared to frontend solutions.

| Use case                    | Recommended method              |
| --------------------------- | ------------------------------- |
| User login and registration | Frontend (UI is required)       |
| Syncing data                | Backend (No UI needed)          |
| Risk Scoring in background  | Backend (invisible to the user) |

---

---
title: DaVinci and frontend flows
description: DaVinci flows designated as PingOne flows (triggered by a PingOne authorize request) use the redirect method to launch and execute the flow in a new browser tab. These flows identify a DaVinci flow policy by its ID and use PingOne endpoints to associate the flow policy with the application. After the user completes all sign-on actions, the flow terminates with specific nodes such as Return a Success Response or Return an Error Response to redirect back to the application.
component: pingone-api
page_id: pingone-api:davinci:getting-started-with-davinci/frontend-flows
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/getting-started-with-davinci/frontend-flows.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why-use-davinci-frontend-flows: Why use DaVinci frontend flows
  frontend-implementation-method-comparison: Frontend implementation method comparison
---

# DaVinci and frontend flows

DaVinci flows designated as PingOne flows (triggered by a PingOne authorize request) use the redirect method to launch and execute the flow in a new browser tab. These flows identify a DaVinci flow policy by its ID and use PingOne endpoints to associate the flow policy with the application. After the user completes all sign-on actions, the flow terminates with specific nodes such as `Return a Success Response` or `Return an Error Response` to redirect back to the application.

|   |                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | DaVinci frontend flows that use the widget integration method are not initiated through a call to the PingOne authorization server. These flows require the inclusion of the DaVinci widget JavaScript file (`davinci.js`) into your application's code. This integration method will not be covered in this document. |

## Why use DaVinci frontend flows

DaVinci frontend flows (using the redirect method) is a more efficient, easier to use integration method than the widget or API methods. The benefits include:

* **No-code/low-code implementation**: The redirect method provides a fast integration because it requires minimal or no development skills compared to embedding widgets or building API calls.

* **Protocol support:** The redirect method supports both OpenID Connect (OIDC) and Security Assertion Markup Language (SAML) application types.

* **Versatile user experience:** It supports complex, multi-step flows such as registration, profile management, or step-up authentication.

* **Session management:** Using the PingOne Authentication Connector with a redirect creates a PingOne user authentication session upon successful completion of the authentication flow, simplifying session handling.

## Frontend implementation method comparison

The following table provides guidance on frontend implementation method features and when to use the supported DaVinci methods.

| Feature          | Redirect           | Widget           | SDK                         |
| ---------------- | ------------------ | ---------------- | --------------------------- |
| User experience  | Full-page redirect | Embedded in page | Completely native or custom |
| Developer effort | None to low        | Minimal          | Medium                      |
| Domain           | PingOne domain     | Your domain      | Your domain                 |
| Speed            | Fastest setup      | Fast             | Slower setup                |
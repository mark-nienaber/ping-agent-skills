---
title: Add a DaVinci Flow Version Alias
description: The PUT {{apiPath}}/v1/environments/{{envID}}/flows/{{davinciFlowID}}/versions/{{davinciFlowVersionID}}/alias updates the flow version specified by its ID in the request URL to add an alias. The request body uses the alias property to specify a user friendly name for the flow version.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flow-versions/add-flow-version-alias
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flow-versions/add-flow-version-alias.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Add a DaVinci Flow Version Alias

##

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
description: The POST {{apiPath}}/v1/environments/{{envID}}/flows/{{flowID}} endpoint uses the application/vnd.pingidentity.flow.clone+json custom Content-Type value to initiate an action to clone the flow specified by its ID in the request URL.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flows/clone-flow
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flows/clone-flow.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Clone a DaVinci Flow

##

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
description: The POST {{apiPath}}/v1/environments/{{envID}}/connectorInstances/{{connectorInstanceID}} clones the connector instance resource specified by its ID in the request URL.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connections/clone-connection
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connections/clone-connection.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Clone DaVinci Connector Instance

##

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
description: The POST {{apiPath}}/v1/environments/{{envID}}/davinciApplications endpoint creates a new DaVinci application resource.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-applications/create-davinci-application
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-applications/create-davinci-application.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Application

##

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
> Refer to [DaVinci Admin Applications data model](../davinci-admin-applications.html#davinci-admin-applications-data-model) for full property descriptions.

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
description: The POST {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies endpoint creates a new DaVinci application flow policy resource.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-application-flow-policies/create-davinci-application-flow-policies
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-application-flow-policies/create-davinci-application-flow-policies.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Application Flow Policies

##

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
> Refer to [DaVinci Admin Application Flow Policies data model](../davinci-admin-application-flow-policies.html#davinci-admin-application-flow-policies-data-model) for full property descriptions.

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
description: The POST {{apiPath}}/v1/environments/{{envID}}/connectorInstances creates a new connector instance resource in the specified environment.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connections/create-connection
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connections/create-connection.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Connector Instance

##

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
> Refer to the [DaVinci admin connector instances data model](../admin-connections.html) for full property descriptions.

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
description: The POST {{apiPath}}/v1/environments/{{envID}}/flows endpoint when used with a Content-Type header value of application/json creates a new DaVinci flow.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flows/create-flow
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flows/create-flow.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Flow

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/flows
```

The `POST {{apiPath}}/v1/environments/{{envID}}/flows` endpoint when used with a `Content-Type` header value of `application/json` creates a new DaVinci flow.

> **Collapse: Request Model**
>
> Refer to the [DaVinci Admin Flows data model](../admin-flows.html) for full property descriptions.
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
description: The POST {{apiPath}}/v1/environments/{{envID}}/uiTemplates endpoint creates a new DaVinci UI template resource.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-ui-templates/create-davinci-template
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-ui-templates/create-davinci-template.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci UI Template

##

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
> Refer to [DaVinci Admin UI Templates data model](../admin-ui-templates.html#davinci-admin-ui-templates-data-model) for full property descriptions.

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
description: The POST {{apiPath}}/v1/environments/{{envID}}/variables endpoint creates a new DaVinci variable resource. You must specify a name, dataType, and context for the variable.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-variables/create-variable
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-variables/create-variable.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create DaVinci Variable

##

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
> Refer to [DaVinci Admin Variables data model](../admin-variables.html) for full property descriptions.

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
description: The PingOne DaVinci Admin APIs provide access to DaVinci operations through the PingOne API resource server. These services are called using the api.pingone.com domain (or api.pingone.ca, api.pingone.eu, api.pingone.com.au, api.pingone.sg, and api.pingone.asia for other geographic domains) to manage DaVinci workflow configuration.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# DaVinci Admin APIs

The PingOne DaVinci Admin APIs provide access to DaVinci operations through the PingOne API resource server. These services are called using the `api.pingone.com` domain (or `api.pingone.ca`, `api.pingone.eu`, `api.pingone.com.au`, `api.pingone.sg`, and `api.pingone.asia` for other geographic domains) to manage DaVinci workflow configuration.

At this time, the following services are supported on the PingOne API resource server:

* [**DaVinci Admin Variables**](davinci-admin-apis/admin-variables.html)

  Endpoints for managing DaVinci variables and their context.

* [**DaVinci Admin Flows**](davinci-admin-apis/admin-flows.html)

  Endpoints for creating and managing DaVinci flows.

* [**DaVinci Admin Flow Versions**](davinci-admin-apis/admin-flow-versions.html)

  Endpoints for managing DaVinci flow versions.

* [**DaVinci Admin Connector Instances**](davinci-admin-apis/admin-connections.html)

  Endpoints for managing DaVinci connector instances, which provide access to DaVinci connector capabilities.

* [**DaVinci Admin Applications**](davinci-admin-apis/davinci-admin-applications.html)

  Endpoints for managing DaVinci applications.

* [**DaVinci Admin Application Flow Policies**](davinci-admin-apis/davinci-admin-application-flow-policies.html)

  Endpoints for managing DaVinci application flow policies.

* [**DaVinci Admin Connectors**](davinci-admin-apis/admin-connectors.html)

  Endpoints for managing DaVinci connectors.

* [**DaVinci Admin UI Templates**](davinci-admin-apis/admin-ui-templates.html)

  Endpoints for managing DaVinci UI templates.

---

---
title: DaVinci Admin Application Flow Policies
description: The PingOne DaVinci Admin Application Flow Policies service provides endpoints to create, read, update, and delete DaVinci application flow policies. Application flow policies specify which flows are run through the application. A flow policy is an entity that points to one or more flows or versions of flows.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-application-flow-policies
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-application-flow-policies.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-application-flow-policies-data-model: DaVinci Admin application flow policies data model properties
  davinci-admin-application-flow-policy-event-data-model: DaVinci Admin application flow policy event data model properties
  response-codes: Response codes
---

# DaVinci Admin Application Flow Policies

The PingOne DaVinci Admin Application Flow Policies service provides endpoints to create, read, update, and delete DaVinci application flow policies. Application flow policies specify which flows are run through the application. A flow policy is an entity that points to one or more flows or versions of flows.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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

---

---
title: DaVinci Admin Applications
description: The PingOne DaVinci Admin Applications service provides endpoints to create, read, update, and delete DaVinci applications. This service also includes endpoints to rotate the application key and application secret values.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-applications
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-applications.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-applications-data-model: DaVinci Admin applications data model properties
  response-codes: Response codes
---

# DaVinci Admin Applications

The PingOne DaVinci Admin Applications service provides endpoints to create, read, update, and delete DaVinci applications. This service also includes endpoints to rotate the application key and application secret values.

A DaVinci application configuration is the link between your site and the sign-on flows you have created in DaVinci. The application configuration contains settings to determine how external sites can send requests for flows, what flows can be requested, and how users and resources from other sites are managed.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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

---

---
title: DaVinci Admin Connector Instances
description: The PingOne DaVinci Admin Connector Instances service provides endpoints to create, read, update, and delete DaVinci connector instances. A DaVinci connector instance is one instance of a DaVinci connector (the connection configuration specifies a connector by name). You can then use the capabilities provided by the connector inside a flow, and launch the flow through an application.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connections
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connections.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-connector-instances-data-model-properties: DaVinci admin connector instances data model properties
  response-codes: Response codes
---

# DaVinci Admin Connector Instances

The PingOne DaVinci Admin Connector Instances service provides endpoints to create, read, update, and delete DaVinci connector instances. A DaVinci connector instance is one instance of a DaVinci connector (the connection configuration specifies a connector by name). You can then use the capabilities provided by the connector inside a flow, and launch the flow through an application.

This service also includes an action to clone connector instance resources.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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

---

---
title: DaVinci Admin Connectors
description: The PingOne DaVinci Admin Connector service provides endpoints to read DaVinci connector resources. Connectors give DaVinci the ability to integrate third party technologies, HTML pages, and other tools to create a sign-on flow. They define the capabilities that you can use as nodes in a flow. For example, an HTTP connector provides the capability to present an HTML form to collect and submit user information or make REST API calls.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-connectors
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-connectors.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-connector-data-model-properties: DaVinci admin connector data model properties
  davinci-admin-connectors-details-data-model-properties: DaVinci admin connectors details data model properties
  response-codes: Response codes
---

# DaVinci Admin Connectors

The PingOne DaVinci Admin Connector service provides endpoints to read DaVinci connector resources. Connectors give DaVinci the ability to integrate third party technologies, HTML pages, and other tools to create a sign-on flow. They define the capabilities that you can use as nodes in a flow. For example, an HTTP connector provides the capability to present an HTML form to collect and submit user information or make REST API calls.

|   |                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is recommended that you review the [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html) topic in the *PingOne DaVinci* admin guide before assigning connectors to your workflow. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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

---

---
title: DaVinci Admin Flow Versions
description: The PingOne DaVinci Admin Flow Versions service provides endpoints to read, update, and delete DaVinci flow versions. This service also includes endpoints to export, revert, and see details about a flow version.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flow-versions
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flow-versions.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  flow-versions-data-model: DaVinci admin flow versions data model properties
  flow-versions-details-data-model: Flow versions details property data model
  flow-versions-graph-data-model: Flow versions graph data property data model
  response-codes: Response codes
---

# DaVinci Admin Flow Versions

The PingOne DaVinci Admin Flow Versions service provides endpoints to read, update, and delete DaVinci flow versions. This service also includes endpoints to export, revert, and see details about a flow version.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The flow version update operation applies only to the `alias` property to add or change the user-friendly name associated with the flow version. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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
| `settings`                             | Object         | Optional | Mutable   | Flow settings saved by the user. Refer to the [Settings property data model](admin-flows.html#settings-property-data-model) table for details.                                 |
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

---

---
title: DaVinci Admin Flows
description: DaVinci flows are constructed, logical paths that specify the workflow for the user's authorization and authentication experiences.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-flows
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flows.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-flow-data-model-properties: DaVinci admin flow data model properties
  settings-property-data-model: Settings property data model
  input-schema-for-non-pingone-flows-data-model: Input schema for non-PingOne flows data model properties
  limiting-and-filtering-data: Limiting and filtering data
  scim-operators: SCIM operators
  response-codes: Response codes
---

# DaVinci Admin Flows

DaVinci flows are constructed, logical paths that specify the workflow for the user's authorization and authentication experiences.

Flows consist of one or more nodes joined together. Each node performs a specific task, using one of the capabilities of your connectors. After completing the task, the flow determines which task to perform next until the flow is complete.

The PingOne DaVinci Admin Flows service provides endpoints to create, read, update, and delete DaVinci flows. This service also includes endpoints to enable, deploy, import, and clone flows.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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

You can limit the number of results returned on the [Read DaVinci Flows](admin-flows/read-flows.html) and [Read One DaVinci Flow](admin-flows/read-one-flow.html) requests with the `attributes` parameter. This parameter filters the response data returned by the request. The query accepts top-level DaVinci admin flow data model properties as a list of comma separated values. The query returns only the specified property values; it removes all other properties from the response. For example, the following request uses the `attributes` query parameter:

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

---

---
title: DaVinci Admin UI Templates
description: You can create user interface (UI) templates that match your company style and branding, which you can include in flows using an HTTP connector. The PingOne DaVinci Admin UI Templates service provides endpoints to create, read, and delete DaVinci UI templates.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-ui-templates
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-ui-templates.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-ui-templates-data-model: DaVinci Admin UI templates data model properties
  response-codes: Response codes
---

# DaVinci Admin UI Templates

You can create user interface (UI) templates that match your company style and branding, which you can include in flows using an HTTP connector. The PingOne DaVinci Admin UI Templates service provides endpoints to create, read, and delete DaVinci UI templates.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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

---

---
title: DaVinci Admin Variables
description: The PingOne DaVinci Admin Variables service provides endpoints to create, read, update, and delete DaVinci variables. Variables are values that can be read and modified during a flow. Every variable has a context, which determines how widely its value is shared.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/admin-variables
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-variables.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  davinci-admin-variable-data-model-properties: DaVinci Admin variable data model properties
  limiting-and-filtering-data: Limiting and filtering data
  response-codes: Response codes
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

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../../platform/users/user-role-assignments.html).

Refer to [Roles Management](../../platform/roles.html) for more information.

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

For information about paging and ordering the response for [Read All DaVinci Variables](admin-variables/read-variables.html), refer to [Paging and ordering collections](../../platform/reference/paging-ordering-collections.html).

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

---

---
title: Delete DaVinci Application
description: The DELETE {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}} operation deletes the DaVinci application resource specified by its ID in the request URL.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-applications/delete-davinci-application
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-applications/delete-davinci-application.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete DaVinci Application

##

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}
```

The `DELETE {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}` operation deletes the DaVinci application resource specified by its ID in the request URL.

When successful, the `DELETE` request returns a code `204 No Content` message.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
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

  url := "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}"
  method := "DELETE"

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
DELETE /v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}",
  "method": "DELETE",
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
  'method': 'DELETE',
  'url': '{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "DELETE"

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

204 No Content

---

---
title: Delete DaVinci Application Flow Policy
description: The DELETE {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}} operation deletes the DaVinci application flow policy resource specified by its ID in the request URL.
component: pingone-api
page_id: pingone-api:davinci:davinci-admin-apis/davinci-admin-application-flow-policies/delete-davinci-application-flow-policy
canonical_url: https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/davinci-admin-application-flow-policies/delete-davinci-application-flow-policy.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete DaVinci Application Flow Policy

##

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}
```

The `DELETE {{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}` operation deletes the DaVinci application flow policy resource specified by its ID in the request URL.

When successful, the `DELETE` request returns a code `204 No Content` message.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
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

  url := "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}"
  method := "DELETE"

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
DELETE /v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}",
  "method": "DELETE",
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
  'method': 'DELETE',
  'url': '{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}"

payload = {}
headers = {
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/davinciApplications/{{davinciApplicationID}}/flowPolicies/{{davinciAppFlowPolicyID}}")!,timeoutInterval: Double.infinity)
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "DELETE"

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

204 No Content
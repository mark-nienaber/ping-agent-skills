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

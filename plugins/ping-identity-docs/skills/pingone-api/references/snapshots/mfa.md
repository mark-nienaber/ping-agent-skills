---
title: Activate MFA User Device
description: Devices with a status of ACTIVATION_REQUIRED are activated using a valid one-time password (OTP). The OTP is sent to the phone number or email address specified in the device resource's properties.
component: pingone-api
page_id: pingone-api:mfa:users/mfa-devices/activate-mfa-user-device
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/mfa-devices/activate-mfa-user-device.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
---

# Activate MFA User Device

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}
```

Devices with a `status` of `ACTIVATION_REQUIRED` are activated using a valid one-time password (OTP). The OTP is sent to the phone number or email address specified in the device resource's properties.

The sample shows the `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}` operation to activate the device specified in the request URL. This operation uses the `application/vnd.pingidentity.device.activate+json` custom content type in the request header to specify the activation action.

When the activation action is completed successfully, the response returns a `200 OK` message and the device `status` property is changed to `ACTIVE`.

### Prerequisites

* Refer to [MFA Devices](#mfa-devices) for important overview information.

* [Create a user](/pingone/platform/v1/api/#post-create-user) to get a `{{userID}}` for the endpoint. For more information, refer to [Users](/pingone/platform/v1/api/#users).

* Use [Read All MFA User Devices](#get-read-all-mfa-user-devices) to retrieve a list of all device resources associated with the specified user and select the specific `deviceID` for the endpoint. For more information, refer to [MFA Devices](#mfa-devices).

> **Collapse: Request Model**
>
> | Property          | Type   | Required |
> | ----------------- | ------ | -------- |
> | `otp`             | String | Required |
> | `block.status`    | String | Optional |
> | `block.blockedAt` | Date   | Optional |
> | `lock.status`     | String | Optional |
> | `lock.expiresAt`  | Date   | Optional |
> | `policy.id`       | String | Optional |
> | `policy.type`     | String | Optional |
> | `nickname`        | String | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.device.activate+json

### Body

raw ( application/vnd.pingidentity.device.activate+json )

```json
{
    "otp": "xxxxxx"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}' \
--header 'Content-Type: application/vnd.pingidentity.device.activate+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "otp": "xxxxxx"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.device.activate+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""otp"": ""xxxxxx""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}"
  method := "POST"

  payload := strings.NewReader(`{
    "otp": "xxxxxx"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.device.activate+json")
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
POST /v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.device.activate+json
Authorization: Bearer {{accessToken}}

{
    "otp": "xxxxxx"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.device.activate+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"otp\": \"xxxxxx\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.device.activate+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.device.activate+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "otp": "xxxxxx"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.device.activate+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "otp": "xxxxxx"
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}"

payload = json.dumps({
  "otp": "xxxxxx"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.device.activate+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.device.activate+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "otp": "xxxxxx"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.device.activate+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "otp": "xxxxxx"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"otp\": \"xxxxxx\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.device.activate+json", forHTTPHeaderField: "Content-Type")
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

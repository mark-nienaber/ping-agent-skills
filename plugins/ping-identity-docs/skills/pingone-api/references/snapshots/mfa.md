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

---

---
title: Activate MFA User Device (FIDO2)
description: Devices with a status of ACTIVATION_REQUIRED are activated with a valid attestation and origin. The attestation is generated by the browser as a response to a user action, such as a fingerprint or clicks on the security key.
component: pingone-api
page_id: pingone-api:mfa:users/mfa-devices/fido2-biometrics-devices/activate-mfa-user-device-fido2
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/mfa-devices/fido2-biometrics-devices/activate-mfa-user-device-fido2.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
---

# Activate MFA User Device (FIDO2)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}
```

Devices with a `status` of `ACTIVATION_REQUIRED` are activated with a valid attestation and origin. The attestation is generated by the browser as a response to a user action, such as a fingerprint or clicks on the security key.

The sample shows the `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}` operation to activate the device specified in the request URL. This operation uses the `application/vnd.pingidentity.device.activate+json` custom content type in the request header to specify the activation action.

The `attestation` property passes in the attestation JSON from the browser. The JSON looks like this:

```none
"{\"id\":\"ARacmDOuRE7DJV6L7w\",
\"type\":\"public-key\",
\"rawId\":\"ARacmDOuRE7DJV6L7w=\",
\"response\":
{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\", \"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"}
,
\"clientExtensionResults\":{}}"
```

When the activation action is completed successfully, the response returns a `200 OK` message and the device `status` property is changed to `ACTIVE`.

> **Collapse: Request Model**
>
> | Property          | Type   | Required  |
> | ----------------- | ------ | --------- |
> | `attestation`     | String | Read-only |
> | `origin`          | String | Read-only |
> | `block.status`    | String | Optional  |
> | `block.blockedAt` | Date   | Optional  |
> | `lock.status`     | String | Optional  |
> | `lock.expiresAt`  | Date   | Optional  |
> | `policy.id`       | String | Optional  |
> | `policy.type`     | String | Optional  |
> | `nickname`        | String | Optional  |
>
> Refer to the [Device properties](#device-properties) and [FIDO2 devices](#fido2-devices) data models for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.device.activate+json

### Body

raw ( application/vnd.pingidentity.device.activate+json )

```json
{
    "origin": "https://app.pingone.com",
    "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
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
    "origin": "https://app.pingone.com",
    "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
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
@"    ""origin"": ""https://app.pingone.com""," + "\n" +
@"    ""attestation"": ""{\""id\"":\""ARacmDOuRE7DJV6L7w\"",\""type\"":\""public-key\"",\""rawId\"":\""ARacmDOuRE7DJV6L7w=\"",\""response\"":{\""clientDataJSON\"":\""eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\"",\""attestationObject\"":\""o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\""},\""clientExtensionResults\"":{}}""" + "\n" +
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
    "origin": "https://app.pingone.com",
    "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
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
    "origin": "https://app.pingone.com",
    "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.device.activate+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"origin\": \"https://app.pingone.com\",\n    \"attestation\": \"{\\\"id\\\":\\\"ARacmDOuRE7DJV6L7w\\\",\\\"type\\\":\\\"public-key\\\",\\\"rawId\\\":\\\"ARacmDOuRE7DJV6L7w=\\\",\\\"response\\\":{\\\"clientDataJSON\\\":\\\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\\\",\\\"attestationObject\\\":\\\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\\\"},\\\"clientExtensionResults\\\":{}}\"\n}");
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
    "origin": "https://app.pingone.com",
    "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
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
    "origin": "https://app.pingone.com",
    "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
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
  "origin": "https://app.pingone.com",
  "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
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
$request->setBody('{\n    "origin": "https://app.pingone.com",\n    "attestation": "{\\"id\\":\\"ARacmDOuRE7DJV6L7w\\",\\"type\\":\\"public-key\\",\\"rawId\\":\\"ARacmDOuRE7DJV6L7w=\\",\\"response\\":{\\"clientDataJSON\\":\\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\\",\\"attestationObject\\":\\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\\"},\\"clientExtensionResults\\":{}}"\n}');
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
  "origin": "https://app.pingone.com",
  "attestation": "{\"id\":\"ARacmDOuRE7DJV6L7w\",\"type\":\"public-key\",\"rawId\":\"ARacmDOuRE7DJV6L7w=\",\"response\":{\"clientDataJSON\":\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\",\"attestationObject\":\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\"},\"clientExtensionResults\":{}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"origin\": \"https://app.pingone.com\",\n    \"attestation\": \"{\\\"id\\\":\\\"ARacmDOuRE7DJV6L7w\\\",\\\"type\\\":\\\"public-key\\\",\\\"rawId\\\":\\\"ARacmDOuRE7DJV6L7w=\\\",\\\"response\\\":{\\\"clientDataJSON\\\":\\\"eyJ0eXBlIjoid2ViYXV0aG4uY3JlYXRYWxzZX0=\\\",\\\"attestationObject\\\":\\\"o2NmbXRmcGFja2VkZ2F0dFFO29h8n6WKBn6tHCQ=\\\"},\\\"clientExtensionResults\\\":{}}\"\n}"
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

---

---
title: Activate MFA User Device (OATH token)
description: This example uses the devices endpoint to activate an OATH token device:
component: pingone-api
page_id: pingone-api:mfa:users/mfa-devices/activate_device_oath_token
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/mfa-devices/activate_device_oath_token.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Activate MFA User Device (OATH token)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}
```

This example uses the `devices` endpoint to activate an OATH token device:

`{{apiPathTest}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}`

Devices with a `status` of `ACTIVATION_REQUIRED` are activated using a valid one-time password (OTP) that was sent to the user.

In addition to the `otp` parameter, which is used for activation of all device types, this example includes the OATH token-specific parameter `oathResync`. When this parameter is set to `true`, it instructs PingOne to resync the OATH token that is to be activated if a resync is required.

If a resync is necessary, the response to the activation request is an error message indicating that you must provide an additional OTP to complete the process (refer to the response for this example.) When this message is returned, run the activate request again, this time including the next OTP for the token as well as the `oathResync` parameter. This second request completes the pairing process, and the status of the device is changed to `ACTIVE`.

Note that for activation requests, the Content-Type header must be set to `application/vnd.pingidentity.device.activate+json`.

> **Collapse: Request Model**
>
> | Property     | Type    | Required |
> | ------------ | ------- | -------- |
> | `otp`        | String  | Required |
> | `oathResync` | Boolean | Optional |
>
> Refer to the [Device properties](#device-properties) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.device.activate+json

### Body

raw ( application/vnd.pingidentity.device.activate+json )

```json
{
    "otp": "71053192",
    "oathResync": true
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
    "otp": "71053192",
    "oathResync": true
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
@"    ""otp"": ""71053192""," + "\n" +
@"    ""oathResync"": true" + "\n" +
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
    "otp": "71053192",
    "oathResync": true
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
    "otp": "71053192",
    "oathResync": true
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.device.activate+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"otp\": \"71053192\",\n    \"oathResync\": true\n}");
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
    "otp": "71053192",
    "oathResync": true
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
    "otp": "71053192",
    "oathResync": true
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
  "otp": "71053192",
  "oathResync": True
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
$request->setBody('{\n    "otp": "71053192",\n    "oathResync": true\n}');
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
  "otp": "71053192",
  "oathResync": true
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"otp\": \"71053192\",\n    \"oathResync\": true\n}"
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

### Example Response

400 Bad Request

```json
{
    "id": "b8ee5b23-ac72-4655-bb86-7ba3f6e4a7c1",
    "code": "INVALID_DATA",
    "message": "The request could not be completed. One or more validation errors were in the request.",
    "details": [
        {
            "code": "EXTRA_OTP_REQUIRED",
            "target": "otp",
            "message": "An extra OTP is required"
        }
    ]
}
```

---

---
title: Activate MFA User Device (PingID Desktop)
component: pingone-api
page_id: pingone-api:mfa:users/mfa-devices/activate-mfa-user-device-desktop
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/mfa-devices/activate-mfa-user-device-desktop.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Activate MFA User Device (PingID Desktop)

##

   

```none
POST {{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}
```

The creation and pairing of a PingID Desktop device involves a sequence of requests and responses, including interaction with the Desktop API

This example shows the final step in this process, sending a POST request to the `devices` endpoint:

`{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}`

`deviceID` in the URL represents the ID that was included in the response from the PingOne server in [the initial device creation request](create-mfa-user-device-desktop.html) .

The body consists of a single field, `attestation`, and its value is the JWT that you received after the call to the PingID Desktop API, described in the description of [the initial device creation request](create-mfa-user-device-desktop.html).

The `Content-Type` header must be set to `application/vnd.pingidentity.device.activate+json`.

> **Collapse: Request Model**
>
> | Property      | Type   | Required? |
> | ------------- | ------ | --------- |
> | `attestation` | String | Required  |
>
> Refer to [PingID Desktop device properties](../mfa-devices.html#pingid-desktop-device-properties) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.device.activate+json

### Body

raw ( application/vnd.pingidentity.device.activate+json )

```json
{
    "attestation":
        "{{attestationValue}}"
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
curl --location --globoff '{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}' \
--header 'Content-Type: application/vnd.pingidentity.device.activate+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "attestation":
        "{{attestationValue}}"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.device.activate+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{   " + "\n" +
@"    ""attestation"": " + "\n" +
@"        ""{{attestationValue}}""" + "\n" +
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

  url := "{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}"
  method := "POST"

  payload := strings.NewReader(`{
    "attestation":
        "{{attestationValue}}"
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
POST /environments/{{envID}}/users/{{userID}}/devices/{{deviceID}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.device.activate+json
Authorization: Bearer {{accessToken}}

{
    "attestation":
        "{{attestationValue}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.device.activate+json");
RequestBody body = RequestBody.create(mediaType, "{   \n    \"attestation\": \n        \"{{attestationValue}}\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.device.activate+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.device.activate+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "attestation": "{{attestationValue}}"
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
  'url': '{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.device.activate+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "attestation": "{{attestationValue}}"
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

url = "{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}"

payload = json.dumps({
  "attestation": "{{attestationValue}}"
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
$request->setUrl('{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.device.activate+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{   \n    "attestation": \n        "{{attestationValue}}"\n}');
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

url = URI("{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.device.activate+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "attestation": "{{attestationValue}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{   \n    \"attestation\": \n        \"{{attestationValue}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")!,timeoutInterval: Double.infinity)
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

### Example Response

200 OK

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/d4543f69-e508-4cc6-bd16-b61baa4b3caf/devices/0783541c-a172-8d40-0783-541ca1728d40"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/d4543f69-e508-4cc6-bd16-b61baa4b3caf"
        }
    },
    "rp": {
        "id": "pingone.eu",
        "name": "pingone.eu"
    },
    "id": "0783541c-a172-8d40-0783-541ca1728d40",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "d4543f69-e508-4cc6-bd16-b61baa4b3caf"
    },
    "type": "PINGID_DESKTOP_GEN2",
    "nickname": "Desktop Mac 1",
    "lock": {
        "status": "UNLOCKED"
    },
    "block": {
        "status": "UNBLOCKED"
    },
    "status": "ACTIVE",
    "createdAt": "2026-02-17T13:34:34.840Z",
    "updatedAt": "2026-02-17T13:36:33.257Z",
    "os": {
        "version": "15.7.3",
        "type": "MAC"
    },
    "model": {},
    "application": {
        "id": "941d6390-ec3a-4bf4-858a-949c47ccd36e",
        "nativeName": "PingID Desktop",
        "version": "1.0.0",
        "pushSandbox": false
    },
    "unitId": "4d764d06-6aa5-4c15-ac8c-4df655cbf867"
}
```

---

---
title: Add Custom FIDO Device - fido2
description: Use POST {{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata to add a custom FIDO device to the Global Authenticators table.
component: pingone-api
page_id: pingone-api:mfa:fido-policies/add_custom_fido_device_fido2
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/fido-policies/add_custom_fido_device_fido2.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Add Custom FIDO Device - fido2

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata
```

Use `POST {{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata` to add a custom FIDO device to the Global Authenticators table.

The data included in the request should comform with the [Metadata Statement Format](https://fidoalliance.org/specs/mds/fido-metadata-statement-v3.0-ps-20210518.html#metadata-statement-format) provided by the FIDO Alliance.

If you are using JSON data provided by a manufacturer, verify that it conforms to the following details expected by the PingOne API:

* The metadata outlined in the standard should be enclosed in an object called `metadataStatement`.

* The `metadataStatement` should be enclosed in an object that also includes the relevant key identifier. This example adds a device that is compliant with the FIDO2 protocol so the relevant identifier is the `aaguid` field.

### Prerequisites

* Refer to [FIDO Policies](#fido-policies) for important overview information.

> **Collapse: Request Model**
>
> | Property            | Type   | Required |
> | ------------------- | ------ | -------- |
> | `aaguid`            | String | Required |
> | `metadataStatement` | Object | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "aaguid": "{{aaguid}}",
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "aaguid": "{{aaguid}}",
        "description": "ATKey.Pro CTAP2.0",
        "authenticatorVersion": 2,
        "protocolFamily": "fido2",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 0
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "cose"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "fingerprint_internal",
                    "baDesc": {
                        "selfAttestedFRR": 0,
                        "selfAttestedFAR": 0,
                        "maxTemplates": 0,
                        "maxRetries": 0,
                        "blockSlowdown": 0
                    }
                },
                {
                    "userVerificationMethod": "presence_internal"
                },
                {
                    "userVerificationMethod": "passcode_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": true,
        "matcherProtection": [
            "on_chip"
        ],
        "attachmentHint": [
            "external"
        ],
        "attestationRootCertificates": [
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
        ],
        "icon": "data:image/png;base64,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",
        "authenticatorGetInfo": {
            "versions": [
                "U2F_V2",
                "FIDO_2_0",
                "FIDO_2_1_PRE"
            ],
            "extensions": [
                "credBlob",
                "credProtect",
                "hmac-secret"
            ],
            "aaguid": "{{aaguid}}",
            "options": {
                "uv": true,
                "userVerificationMgmtPreview": true,
                "credMgmt": true,
                "uvBioEnroll": true,
                "rk": true,
                "plat": false,
                "clientPin": false,
                "up": true,
                "bioEnroll": true,
                "credentialMgmtPreview": true
            },
            "maxMsgSize": 2048,
            "pinUvAuthProtocols": [
                1
            ],
            "maxCredentialCountInList": 20,
            "maxCredentialIdLength": 128,
            "transports": [
                "usb"
            ],
            "algorithms": [
                {
                    "type": "public-key",
                    "alg": -7
                },
                {
                    "type": "public-key",
                    "alg": -8
                }
            ],
            "firmwareVersion": 10013
        }
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "aaguid": "{{aaguid}}",
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "aaguid": "{{aaguid}}",
        "description": "ATKey.Pro CTAP2.0",
        "authenticatorVersion": 2,
        "protocolFamily": "fido2",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 0
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "cose"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "fingerprint_internal",
                    "baDesc": {
                        "selfAttestedFRR": 0,
                        "selfAttestedFAR": 0,
                        "maxTemplates": 0,
                        "maxRetries": 0,
                        "blockSlowdown": 0
                    }
                },
                {
                    "userVerificationMethod": "presence_internal"
                },
                {
                    "userVerificationMethod": "passcode_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": true,
        "matcherProtection": [
            "on_chip"
        ],
        "attachmentHint": [
            "external"
        ],
        "attestationRootCertificates": [
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
        ],
        "icon": "data:image/png;base64,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",
        "authenticatorGetInfo": {
            "versions": [
                "U2F_V2",
                "FIDO_2_0",
                "FIDO_2_1_PRE"
            ],
            "extensions": [
                "credBlob",
                "credProtect",
                "hmac-secret"
            ],
            "aaguid": "{{aaguid}}",
            "options": {
                "uv": true,
                "userVerificationMgmtPreview": true,
                "credMgmt": true,
                "uvBioEnroll": true,
                "rk": true,
                "plat": false,
                "clientPin": false,
                "up": true,
                "bioEnroll": true,
                "credentialMgmtPreview": true
            },
            "maxMsgSize": 2048,
            "pinUvAuthProtocols": [
                1
            ],
            "maxCredentialCountInList": 20,
            "maxCredentialIdLength": 128,
            "transports": [
                "usb"
            ],
            "algorithms": [
                {
                    "type": "public-key",
                    "alg": -7
                },
                {
                    "type": "public-key",
                    "alg": -8
                }
            ],
            "firmwareVersion": 10013
        }
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""aaguid"": ""{{aaguid}}""," + "\n" +
@"    ""metadataStatement"": {" + "\n" +
@"        ""legalHeader"": ""https://fidoalliance.org/metadata/metadata-statement-legal-header/""," + "\n" +
@"        ""aaguid"": ""{{aaguid}}""," + "\n" +
@"        ""description"": ""ATKey.Pro CTAP2.0""," + "\n" +
@"        ""authenticatorVersion"": 2," + "\n" +
@"        ""protocolFamily"": ""fido2""," + "\n" +
@"        ""schema"": 3," + "\n" +
@"        ""upv"": [" + "\n" +
@"            {" + "\n" +
@"                ""major"": 1," + "\n" +
@"                ""minor"": 0" + "\n" +
@"            }" + "\n" +
@"        ]," + "\n" +
@"        ""authenticationAlgorithms"": [" + "\n" +
@"            ""secp256r1_ecdsa_sha256_raw""" + "\n" +
@"        ]," + "\n" +
@"        ""publicKeyAlgAndEncodings"": [" + "\n" +
@"            ""cose""" + "\n" +
@"        ]," + "\n" +
@"        ""attestationTypes"": [" + "\n" +
@"            ""basic_full""" + "\n" +
@"        ]," + "\n" +
@"        ""userVerificationDetails"": [" + "\n" +
@"            [" + "\n" +
@"                {" + "\n" +
@"                    ""userVerificationMethod"": ""fingerprint_internal""," + "\n" +
@"                    ""baDesc"": {" + "\n" +
@"                        ""selfAttestedFRR"": 0," + "\n" +
@"                        ""selfAttestedFAR"": 0," + "\n" +
@"                        ""maxTemplates"": 0," + "\n" +
@"                        ""maxRetries"": 0," + "\n" +
@"                        ""blockSlowdown"": 0" + "\n" +
@"                    }" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""userVerificationMethod"": ""presence_internal""" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""userVerificationMethod"": ""passcode_internal""" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        ]," + "\n" +
@"        ""keyProtection"": [" + "\n" +
@"            ""hardware""" + "\n" +
@"        ]," + "\n" +
@"        ""isKeyRestricted"": false," + "\n" +
@"        ""isFreshUserVerificationRequired"": true," + "\n" +
@"        ""matcherProtection"": [" + "\n" +
@"            ""on_chip""" + "\n" +
@"        ]," + "\n" +
@"        ""attachmentHint"": [" + "\n" +
@"            ""external""" + "\n" +
@"        ]," + "\n" +
@"        ""attestationRootCertificates"": [" + "\n" +
@"            ""MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=""," + "\n" +
@"            ""MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk=""" + "\n" +
@"        ]," + "\n" +
@"        ""icon"": ""data:image/png;base64,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""," + "\n" +
@"        ""authenticatorGetInfo"": {" + "\n" +
@"            ""versions"": [" + "\n" +
@"                ""U2F_V2""," + "\n" +
@"                ""FIDO_2_0""," + "\n" +
@"                ""FIDO_2_1_PRE""" + "\n" +
@"            ]," + "\n" +
@"            ""extensions"": [" + "\n" +
@"                ""credBlob""," + "\n" +
@"                ""credProtect""," + "\n" +
@"                ""hmac-secret""" + "\n" +
@"            ]," + "\n" +
@"            ""aaguid"": ""{{aaguid}}""," + "\n" +
@"            ""options"": {" + "\n" +
@"                ""uv"": true," + "\n" +
@"                ""userVerificationMgmtPreview"": true," + "\n" +
@"                ""credMgmt"": true," + "\n" +
@"                ""uvBioEnroll"": true," + "\n" +
@"                ""rk"": true," + "\n" +
@"                ""plat"": false," + "\n" +
@"                ""clientPin"": false," + "\n" +
@"                ""up"": true," + "\n" +
@"                ""bioEnroll"": true," + "\n" +
@"                ""credentialMgmtPreview"": true" + "\n" +
@"            }," + "\n" +
@"            ""maxMsgSize"": 2048," + "\n" +
@"            ""pinUvAuthProtocols"": [" + "\n" +
@"                1" + "\n" +
@"            ]," + "\n" +
@"            ""maxCredentialCountInList"": 20," + "\n" +
@"            ""maxCredentialIdLength"": 128," + "\n" +
@"            ""transports"": [" + "\n" +
@"                ""usb""" + "\n" +
@"            ]," + "\n" +
@"            ""algorithms"": [" + "\n" +
@"                {" + "\n" +
@"                    ""type"": ""public-key""," + "\n" +
@"                    ""alg"": -7" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""type"": ""public-key""," + "\n" +
@"                    ""alg"": -8" + "\n" +
@"                }" + "\n" +
@"            ]," + "\n" +
@"            ""firmwareVersion"": 10013" + "\n" +
@"        }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata"
  method := "POST"

  payload := strings.NewReader(`{
    "aaguid": "{{aaguid}}",
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "aaguid": "{{aaguid}}",
        "description": "ATKey.Pro CTAP2.0",
        "authenticatorVersion": 2,
        "protocolFamily": "fido2",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 0
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "cose"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "fingerprint_internal",
                    "baDesc": {
                        "selfAttestedFRR": 0,
                        "selfAttestedFAR": 0,
                        "maxTemplates": 0,
                        "maxRetries": 0,
                        "blockSlowdown": 0
                    }
                },
                {
                    "userVerificationMethod": "presence_internal"
                },
                {
                    "userVerificationMethod": "passcode_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": true,
        "matcherProtection": [
            "on_chip"
        ],
        "attachmentHint": [
            "external"
        ],
        "attestationRootCertificates": [
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
        ],
        "icon": "data:image/png;base64,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",
        "authenticatorGetInfo": {
            "versions": [
                "U2F_V2",
                "FIDO_2_0",
                "FIDO_2_1_PRE"
            ],
            "extensions": [
                "credBlob",
                "credProtect",
                "hmac-secret"
            ],
            "aaguid": "{{aaguid}}",
            "options": {
                "uv": true,
                "userVerificationMgmtPreview": true,
                "credMgmt": true,
                "uvBioEnroll": true,
                "rk": true,
                "plat": false,
                "clientPin": false,
                "up": true,
                "bioEnroll": true,
                "credentialMgmtPreview": true
            },
            "maxMsgSize": 2048,
            "pinUvAuthProtocols": [
                1
            ],
            "maxCredentialCountInList": 20,
            "maxCredentialIdLength": 128,
            "transports": [
                "usb"
            ],
            "algorithms": [
                {
                    "type": "public-key",
                    "alg": -7
                },
                {
                    "type": "public-key",
                    "alg": -8
                }
            ],
            "firmwareVersion": 10013
        }
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
POST /v1/environments/{{envID}}/fidoDevicesMetadata HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "aaguid": "{{aaguid}}",
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "aaguid": "{{aaguid}}",
        "description": "ATKey.Pro CTAP2.0",
        "authenticatorVersion": 2,
        "protocolFamily": "fido2",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 0
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "cose"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "fingerprint_internal",
                    "baDesc": {
                        "selfAttestedFRR": 0,
                        "selfAttestedFAR": 0,
                        "maxTemplates": 0,
                        "maxRetries": 0,
                        "blockSlowdown": 0
                    }
                },
                {
                    "userVerificationMethod": "presence_internal"
                },
                {
                    "userVerificationMethod": "passcode_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": true,
        "matcherProtection": [
            "on_chip"
        ],
        "attachmentHint": [
            "external"
        ],
        "attestationRootCertificates": [
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
        ],
        "icon": "data:image/png;base64,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",
        "authenticatorGetInfo": {
            "versions": [
                "U2F_V2",
                "FIDO_2_0",
                "FIDO_2_1_PRE"
            ],
            "extensions": [
                "credBlob",
                "credProtect",
                "hmac-secret"
            ],
            "aaguid": "{{aaguid}}",
            "options": {
                "uv": true,
                "userVerificationMgmtPreview": true,
                "credMgmt": true,
                "uvBioEnroll": true,
                "rk": true,
                "plat": false,
                "clientPin": false,
                "up": true,
                "bioEnroll": true,
                "credentialMgmtPreview": true
            },
            "maxMsgSize": 2048,
            "pinUvAuthProtocols": [
                1
            ],
            "maxCredentialCountInList": 20,
            "maxCredentialIdLength": 128,
            "transports": [
                "usb"
            ],
            "algorithms": [
                {
                    "type": "public-key",
                    "alg": -7
                },
                {
                    "type": "public-key",
                    "alg": -8
                }
            ],
            "firmwareVersion": 10013
        }
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"aaguid\": \"{{aaguid}}\",\n    \"metadataStatement\": {\n        \"legalHeader\": \"https://fidoalliance.org/metadata/metadata-statement-legal-header/\",\n        \"aaguid\": \"{{aaguid}}\",\n        \"description\": \"ATKey.Pro CTAP2.0\",\n        \"authenticatorVersion\": 2,\n        \"protocolFamily\": \"fido2\",\n        \"schema\": 3,\n        \"upv\": [\n            {\n                \"major\": 1,\n                \"minor\": 0\n            }\n        ],\n        \"authenticationAlgorithms\": [\n            \"secp256r1_ecdsa_sha256_raw\"\n        ],\n        \"publicKeyAlgAndEncodings\": [\n            \"cose\"\n        ],\n        \"attestationTypes\": [\n            \"basic_full\"\n        ],\n        \"userVerificationDetails\": [\n            [\n                {\n                    \"userVerificationMethod\": \"fingerprint_internal\",\n                    \"baDesc\": {\n                        \"selfAttestedFRR\": 0,\n                        \"selfAttestedFAR\": 0,\n                        \"maxTemplates\": 0,\n                        \"maxRetries\": 0,\n                        \"blockSlowdown\": 0\n                    }\n                },\n                {\n                    \"userVerificationMethod\": \"presence_internal\"\n                },\n                {\n                    \"userVerificationMethod\": \"passcode_internal\"\n                }\n            ]\n        ],\n        \"keyProtection\": [\n            \"hardware\"\n        ],\n        \"isKeyRestricted\": false,\n        \"isFreshUserVerificationRequired\": true,\n        \"matcherProtection\": [\n            \"on_chip\"\n        ],\n        \"attachmentHint\": [\n            \"external\"\n        ],\n        \"attestationRootCertificates\": [\n            \"MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=\",\n            \"MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk=\"\n        ],\n        \"icon\": \"data:image/png;base64,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\",\n        \"authenticatorGetInfo\": {\n            \"versions\": [\n                \"U2F_V2\",\n                \"FIDO_2_0\",\n                \"FIDO_2_1_PRE\"\n            ],\n            \"extensions\": [\n                \"credBlob\",\n                \"credProtect\",\n                \"hmac-secret\"\n            ],\n            \"aaguid\": \"{{aaguid}}\",\n            \"options\": {\n                \"uv\": true,\n                \"userVerificationMgmtPreview\": true,\n                \"credMgmt\": true,\n                \"uvBioEnroll\": true,\n                \"rk\": true,\n                \"plat\": false,\n                \"clientPin\": false,\n                \"up\": true,\n                \"bioEnroll\": true,\n                \"credentialMgmtPreview\": true\n            },\n            \"maxMsgSize\": 2048,\n            \"pinUvAuthProtocols\": [\n                1\n            ],\n            \"maxCredentialCountInList\": 20,\n            \"maxCredentialIdLength\": 128,\n            \"transports\": [\n                \"usb\"\n            ],\n            \"algorithms\": [\n                {\n                    \"type\": \"public-key\",\n                    \"alg\": -7\n                },\n                {\n                    \"type\": \"public-key\",\n                    \"alg\": -8\n                }\n            ],\n            \"firmwareVersion\": 10013\n        }\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "aaguid": "{{aaguid}}",
    "metadataStatement": {
      "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
      "aaguid": "{{aaguid}}",
      "description": "ATKey.Pro CTAP2.0",
      "authenticatorVersion": 2,
      "protocolFamily": "fido2",
      "schema": 3,
      "upv": [
        {
          "major": 1,
          "minor": 0
        }
      ],
      "authenticationAlgorithms": [
        "secp256r1_ecdsa_sha256_raw"
      ],
      "publicKeyAlgAndEncodings": [
        "cose"
      ],
      "attestationTypes": [
        "basic_full"
      ],
      "userVerificationDetails": [
        [
          {
            "userVerificationMethod": "fingerprint_internal",
            "baDesc": {
              "selfAttestedFRR": 0,
              "selfAttestedFAR": 0,
              "maxTemplates": 0,
              "maxRetries": 0,
              "blockSlowdown": 0
            }
          },
          {
            "userVerificationMethod": "presence_internal"
          },
          {
            "userVerificationMethod": "passcode_internal"
          }
        ]
      ],
      "keyProtection": [
        "hardware"
      ],
      "isKeyRestricted": false,
      "isFreshUserVerificationRequired": true,
      "matcherProtection": [
        "on_chip"
      ],
      "attachmentHint": [
        "external"
      ],
      "attestationRootCertificates": [
        "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
        "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
      ],
      "icon": "data:image/png;base64,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",
      "authenticatorGetInfo": {
        "versions": [
          "U2F_V2",
          "FIDO_2_0",
          "FIDO_2_1_PRE"
        ],
        "extensions": [
          "credBlob",
          "credProtect",
          "hmac-secret"
        ],
        "aaguid": "{{aaguid}}",
        "options": {
          "uv": true,
          "userVerificationMgmtPreview": true,
          "credMgmt": true,
          "uvBioEnroll": true,
          "rk": true,
          "plat": false,
          "clientPin": false,
          "up": true,
          "bioEnroll": true,
          "credentialMgmtPreview": true
        },
        "maxMsgSize": 2048,
        "pinUvAuthProtocols": [
          1
        ],
        "maxCredentialCountInList": 20,
        "maxCredentialIdLength": 128,
        "transports": [
          "usb"
        ],
        "algorithms": [
          {
            "type": "public-key",
            "alg": -7
          },
          {
            "type": "public-key",
            "alg": -8
          }
        ],
        "firmwareVersion": 10013
      }
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "aaguid": "{{aaguid}}",
    "metadataStatement": {
      "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
      "aaguid": "{{aaguid}}",
      "description": "ATKey.Pro CTAP2.0",
      "authenticatorVersion": 2,
      "protocolFamily": "fido2",
      "schema": 3,
      "upv": [
        {
          "major": 1,
          "minor": 0
        }
      ],
      "authenticationAlgorithms": [
        "secp256r1_ecdsa_sha256_raw"
      ],
      "publicKeyAlgAndEncodings": [
        "cose"
      ],
      "attestationTypes": [
        "basic_full"
      ],
      "userVerificationDetails": [
        [
          {
            "userVerificationMethod": "fingerprint_internal",
            "baDesc": {
              "selfAttestedFRR": 0,
              "selfAttestedFAR": 0,
              "maxTemplates": 0,
              "maxRetries": 0,
              "blockSlowdown": 0
            }
          },
          {
            "userVerificationMethod": "presence_internal"
          },
          {
            "userVerificationMethod": "passcode_internal"
          }
        ]
      ],
      "keyProtection": [
        "hardware"
      ],
      "isKeyRestricted": false,
      "isFreshUserVerificationRequired": true,
      "matcherProtection": [
        "on_chip"
      ],
      "attachmentHint": [
        "external"
      ],
      "attestationRootCertificates": [
        "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
        "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
      ],
      "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAA9CAIAAADAuAeYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAABGuSURBVHhe7ZwJfBPV9sczS/Y03Rco3XcKBVwRBHkiT58LqxvCE3AtoIICBQTZ2gItUigtVGihKPoXAR+yyPLhARZZ1EdVoPoQpKW0BVq6Zc9klvxPMrfQliZNl7QPP/l+LnTmnDuTyfzuvefcm0kws9kscHEvg6O/Lu5ZUC/8z4BnNL8WYYSIt3Y7HGsIeH5M/M4stO/CNkjCswPHan/5HRf/r0jI6gz+45/t/fkatO/CNmggxXhwHLbMNGM20d1TaEaAWy4DwzG4Ev7aXNgH9cLCR8ZBL8TEIjPHyWLCcYLo+jQHpDPTtO7iFUxIcnqD38vP9t6WgXwubNNUQpFQQDODq88Schnv7mKoylunAu4nlZ4uCR2neUYKirJaPdrpcjidAW25cJgWJxVdPYQ2ohtf+l7FNS+85+lMCVmDkTOZOBPF0TSHbC6cTqdJqP/vle9k0af8HjrpBJZT+mph45XDiZTpPwYuICAhebWVbAmVmjoWSxa1beRXSOhPristoTx3GFDCMIjMAJhdv1TdtpjRa5XTiTzpHw8rSFBOmBYRirN3IUIyAwAU2XLs5EbhfOpBMkNJTdqD58hJBKYELpN/455cN9zRRNKOTlG75g9K55ntPpBAkvTV9MkAoBJmBYTVTWorDUObSxDoZTjjJeS3Z91OB0OiQhzMMN16uq9x3CZVJOb/AZMUKodPMYfL8iKp6jaFIuL1+/jaNMqLYL59AhCTGB4MrMFIIQwzbNqGJyV/D2yDULGGM9dETIaErTN/JGF06iQxJSlbeqdu63dEGD0XvIMGlIIG/3eeZvssgYmOALZfKyNfkczfB2F86gQxJeSUrDcEIAiSitjtmYiqxWIlfOZQxqgZBg62rL1my22lzrn06h/RJS1bVVn+8l5FLOSHkMHCSPi0QOK77jnpKFRppNDC5TlGVsZs2cddx10fm0X8KShRlmM2vpgib17SjYmLC0JMagwUjCVHmrYt1nyOqis2mnhHS96mb+LkIuMzOMcsADsqhQqqoaQuPtYrpV6/X4I9KgYAHLEVJZ+apc1zDqJNopYcmSdWYTDTknRpLG4rKTnv1/CB7yQ8jQ2+VM0OAzIY8yKq2AwHEhaaiouL7pS3Swi06lPRIyWv3N3O3WhzMsz0yZIc6RJCYSNi8EASkMVIBapFR+bcUn6HgXnUrzZ2egbz1SekLk78u7W+TSe0uvZX1Ckm5oH4HhMgnIBVsgKmegmqWgNFPXOyczMPEVtN8ShuLSMxFD7n52JjdvS0HBCYlYrKeopYsWRkU1SZ2akZyS+uefxUJSCNdSr6p/8IEH5ibNrqmpfStxuqe7u9FkHDjw4XemTd29ZOr3bI5Qo7mbKJNvVLSJg1a2ZxcfGsOfO8Pb04M0eQRO7GHFTDNnq94d0ZM+FO4BheW1+/MSfb19feXW03JPrrMGaW5erUPV56wdrJGoC+JiKrvtwvEAlBQFws9h33pOWJwkZ3hzPRhj+uoJ02cuHChf3fHpDL5VqdbuZ77yBrSyTNnb8pb7NcJocrUqnU8fFxu3ZsBztFGffs3Rvg76/T6iRiCVj+vHxl7/4Dnh4eZtsaGg1GygRtURAeHn6hqEij1pAkWa9SjRk9+ul/PMnXscXWrZ/u3Pm1m9LNaKDuG9DfSfoBbZYQlIvdthrtNOVG/g5S5G5mWDLQIy5/FbJ2BiKxWCqXQWEFHMRWZL2LufPm5+bn+/j6gn5wo/sPSPj+u2O8C7qCVGo5A2c2w9nAIhTC6G6x2JEQw3GRxKI3kJaaMuXtRH8Pd5wkl6eltSohtCRPH2+RUKjRaFNSliCrE2hbLKQp09Xl60tXbLianFX+yd3pScO9YFm0YQWspatyr6Zml8KxGVts3rCOMW/wo15+d5e3tb+p4qLir6tX4vo9LqayltVllJtp6jrVXz9cc+PVcjkLMeKxaLffv+9sLCQt7fI9q92lJVXCIVCiqL6D+j38EMPIYcTaJuEFRn5lxYsvvLhqouL5pEyS1t2BAiPdFXNHws/urJg1aVZc27tOYIcnceChR/lbMr18bHqp1ZHhoefKDiKfDaY9f7M2pqbZSWXym2XqhulX2zbig6AV5k3R1WngpdQSGXJKSuRtSXWZa9XKOTwxuvqVR8mzUFW59AGCSEKlmfkSWQBhETqHv5gwKtjkcMBwlLel7gFEQo3kcjvqvWj4E7si/MXfJSVs9HX1wdurlqtjouOPn2yAPlsI5FIPD09le7udoqHh4dCoUAHCATTp0/DMYzjOJFEeurMqeLiEuRoysFDhy/+cVkoEtE0HR0R8dRTrQy5HaQNEpZnfWaqrhIICcaoDkttU8syE2Jx0MwprFaNSUTac+dqDp3orNW2JUuTczZu8rPGP7VaA8lqwfF/I1+LYB1qPW8ZpGq8NxTCgUp6V/jKxNWbs2SyaXwfVAPJ71wQxkdRoOS8iZyz7OJaQKs4mRBocFvPwMsjuERa+g2a8TCqWA4wiRvLMejlqyNGVt9nofH0v/02g08bGxJ+3GPwtm69W0l6SkOSajEWZikBvtP3CgtrYGORo4feaHs7/+AvMfhmEC/QNeGf8ycjgNRyUsz/vSWFGOCUnaoA5b0p6WJVQqA6e+wmo1mESs+qmw9vgZ5Ggvy9PSIeT4eFviH6T70VFRR44cRD7bgH4dkdDDXTl2zCiY8+E4TjPsuqwNyNHA2rWZoB8/JCQmvoWszsQhCSG/LFu50dIFaUYaGNRjyvPI0UaCkt7GYSoNHVEo4yNiO8AJyzUvX5m+Kn21l7cXTEmh//WOiz125JCd+cZtYBTlB9Kqqqpfz50v+u13O+X8+aKSq80D3sL583RaLXRESFi2/d+XEPCQQyAoKvr9u+9PSqVSlmXdPZSvTZmMHM7EIQmrtn6tLymB4Z81aEI+nIasbUfs49VzygssxBKpuP770/WnLXl5myITZBNKN7fs9TnpqzO8fX1APxNFxcfFHT64HybdqJJj5OZtGTDggUFDhw0aYrPcP3DQjPdnowMaCI8If2zoECNF4QShUqnzNm9BDoEgMysLjPyo/uqECfIu+YKYQ822dHmOUCI3M4w4oGfPt+2tkLVK0PxEHCbLHIeT0pJFa5HVYWRSacrytOQVK72t46fAbGYoU+7GHJiBoRqt0jCMKuQKH39/fz8/+GerBPj7QVaKDmjEgg/nqVUqzCyQK2Sb8pCEpdeuHThwSC6TQcoqkYindckoCrQuYeX2/frLlwUiEavXBs15gx/H2ge0BklPf/+JY1itHpdJ6o6eUJ0tcjwyWTTD8CPHjrkpFNAdeQtGEnOS5vMVHKKh1xuNhrq6OlV9fX1dnZ2i17XwQPPDDz2Y0LcPRZuEpLC8vGL3N9+AEcYGmmUgRmp1urGjR/n5+fGVnU3ry9w/9n3K+Oc1DOKMTDqw7CRpXZ1qkWNYCKn0gHgp7uU/8JLNzNBQWvFj9HBcJOSMlOcTg/sdzEcO28vcs5PmffHl9sZTNJPJRJtoyN1Bxprq6pRlS6ZPTUS+lrh542ZUXN+AHv56rW7UqJEbsjNPnjp17Ph3MDtENVqCppnIiPCXXnwB7Tdiz779r05+3c/P12g0xsXE7Nvzr9j4BMtXzDFMr9OdPHEsIjwCVXUyrcSP6/m76otOkQIvRqCOmZ9sRz/ALGAt39NnoDRZYGuGNCTQ78Wnb37+L0Iqu3XosOb8RbeEWORzDK1W2yc+ftjQIZmZ2UovD08vr2Upy0cMHx4dHYVq2OZ26H108GAoaKftjHru2eBegRqdXiwWXy4uHj9xEs0wkMjAtT054gk7+jEMu/2rrwICAmBI0Wg1JpoOCw3pl9BPJHI4FjTF3qgI7xb6ZUxKWlT6gtjlK3rOfB05bCD08hX6+wgDfElfL2SyQcjiGeLAQKG/r8SvV1nGnXTAEeAeBQf12v/N1xCQ+t3Xz6DXwwAhEgqnvN5Fsec2774zXaW2rLcROFb488+gHwxpDM3MnPEuqtESJGn5HYORY55/dvSYc+fOUxQ1aswLUbG9YUhANdoKnA44O3Dsd+LYAre+8D91s4o3QljmNxyhWVXHj4RXuV1Zf+XqUUFQgTLhOBn128T3kdVsnjVnbkCvkMjY+KCwyEGPPgZvm7eXlpUFBoeFRcZExMZ7+/VY8NFi3n43N67fULj7wBl69AqdOv09ZO0Y0IFCw6PComIjY3tHxMTDyQNDwkeNGYfcdomK66P08r106RJsnzx1WqrwCI+MNRgsiwZtxV4vtKQPDtOsapuSFAcrw+VC/FuXmSESod/HCe7VKzV5aX29Cnwenp7Z2Rts9Z3tUFCEnytSmTNCoNbFuzYzNo8MFMx9c9MMpo+TAyNjbGTeEGg2p5RTnvqKyqgv9rqmsqypEFKDz787Lk1G2ffwF5ADJZaUnC2+Gi62n1pTEzhjW55kmv/nPE8L/pNFpoCR5enhP+OQk5bNGxNdJmvPfuOxKZGMYR2IY727dvn6FDh/Au+6BrsLZevV5nNBkJgoQZTlb2+lDo1PH9Pv1sG/xNGPAQTDGhDnTuF1+Z8NLLL3762RdePgGNW2oLElp+tqe7aO2l4Z3DyIt2Gsjfslkmk9E0DbNDlUrTSlDs2BppM9zd3UNDQlnWEgogSM98dzpytAZcA8jHT2cXLlisrq2bNHGCm5sbxNeQ4F6EULh9567nnntu0KCHwThn3od7v9m7Oj0tJipqS94nQrF45Og7HxM1l9AMN9Fu2ulUMMsI2eY7LJNJczZkq1QquI/u7sodu3btP2BzsdRy79BmJ3D06PFz5y+AEtCAIsMjRo8aiRwOIJfLZ8+bHx0bf/HS5d27v165Ej0Ob2mOFJW1ZvVn+Xn79uxmaPrbAweU3l49A3uCNzg42MfbS6XWnDmDFpmbTipgkCLIH8MfE9zV0rsCGOLg9d2U/DNUbeLvI4ZPGP/Sjl27QULI1ye/9sa1kssyaQvrW5Z+bN1Yty47dWU61LfutYyRMj4+bNjWLXlo/y5WpKd7KJVmgaULLl20EFkdQ6fVZa/JCAkNQfsNQEOE9w9hld/V6Q0URYMFJqC8BaYxkARTDRGxSS+0JBY4xplojmG7odCs5QF+jGhfN8lelxkY4A/JKg5zDLF47LhWPuVhOY6GGQDL2ingpps+RNKYwsKff/zprEgqgXo9/QNenTgROVri0OHDGzbc+ZIXNFNoSTp9C7/SxLfg20keNLIe8L5MpqtXr/IWPajLsv0T+vO7SEKYj1uUo0yW37Jj2O4rcBkmuAyOsVwGf20AwzCQLJggiwev7R+Hy9+SB00bWivkiscLCrLX33lUEJq2CQ62nMMEZ7NYODPrAHyq0iIr0lYplW5wp7V63eTJk+wsPUIfhSY1fXpiQcEJZNGooYlUVlbyu43R6XQmFhrXna+DLVu8iMDwzMxs2D59+oeSPy/PTZrt4enOe9EC24WxibqiyzCR562OA2/A5h1tzWsHzkD5jBwetQYNTanLV36zd59UKoHhZfOmjQkJfXj73axavWbnrq8lUgm8r5qa2u+PHfX2sawzVFZVPv7EP7y9vYwGw99HjEhJXrJly9bsnE8UbncW7e4G+vSgRx5Z83E62m9EcXHJfQ8O9PH1AY2hw5wvPCtXyJGvJd6b8UHRb7/t27tbr9O+ea0G7cqhYQQJ7DRI0d+8P6decjSZckHDh3GCcLT3X3a1MRnn3mat//yy6/LV6ykGAYXYONffrHxmp9FQhCxodf+1YD7C+Mq2ulU3nhr6rcHDyoUCrVa/cZrk1OTlyFHl2OV0Npd2of9Yzty5v9lbt2qjo1PgGkoDNAmiir86UyXfS5xN5YW2pG7bP/Yv6R+wKqMNaSQxDEM8hEY67pRPwDFQheOYzAawyOiZdZPviD1OH3ieHh4OO/qFpwSJ/7awIQSkkkIsaDlsKFDulc/wNUL20yv0AiRSAQSqupVRw7t699/AHJ0E65e2DbSV62uKC2rq62/XnGjT5/4btcPcPXCtnHu3HmaoaELMgwbFhrivK+cOY5Lwnse10B6jyMQ/D/exLg8R/4sQAAAAABJRU5ErkJggg==",
      "authenticatorGetInfo": {
        "versions": [
          "U2F_V2",
          "FIDO_2_0",
          "FIDO_2_1_PRE"
        ],
        "extensions": [
          "credBlob",
          "credProtect",
          "hmac-secret"
        ],
        "aaguid": "{{aaguid}}",
        "options": {
          "uv": true,
          "userVerificationMgmtPreview": true,
          "credMgmt": true,
          "uvBioEnroll": true,
          "rk": true,
          "plat": false,
          "clientPin": false,
          "up": true,
          "bioEnroll": true,
          "credentialMgmtPreview": true
        },
        "maxMsgSize": 2048,
        "pinUvAuthProtocols": [
          1
        ],
        "maxCredentialCountInList": 20,
        "maxCredentialIdLength": 128,
        "transports": [
          "usb"
        ],
        "algorithms": [
          {
            "type": "public-key",
            "alg": -7
          },
          {
            "type": "public-key",
            "alg": -8
          }
        ],
        "firmwareVersion": 10013
      }
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

url = "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata"

payload = json.dumps({
  "aaguid": "{{aaguid}}",
  "metadataStatement": {
    "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
    "aaguid": "{{aaguid}}",
    "description": "ATKey.Pro CTAP2.0",
    "authenticatorVersion": 2,
    "protocolFamily": "fido2",
    "schema": 3,
    "upv": [
      {
        "major": 1,
        "minor": 0
      }
    ],
    "authenticationAlgorithms": [
      "secp256r1_ecdsa_sha256_raw"
    ],
    "publicKeyAlgAndEncodings": [
      "cose"
    ],
    "attestationTypes": [
      "basic_full"
    ],
    "userVerificationDetails": [
      [
        {
          "userVerificationMethod": "fingerprint_internal",
          "baDesc": {
            "selfAttestedFRR": 0,
            "selfAttestedFAR": 0,
            "maxTemplates": 0,
            "maxRetries": 0,
            "blockSlowdown": 0
          }
        },
        {
          "userVerificationMethod": "presence_internal"
        },
        {
          "userVerificationMethod": "passcode_internal"
        }
      ]
    ],
    "keyProtection": [
      "hardware"
    ],
    "isKeyRestricted": False,
    "isFreshUserVerificationRequired": True,
    "matcherProtection": [
      "on_chip"
    ],
    "attachmentHint": [
      "external"
    ],
    "attestationRootCertificates": [
      "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
      "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
    ],
    "icon": "data:image/png;base64,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",
    "authenticatorGetInfo": {
      "versions": [
        "U2F_V2",
        "FIDO_2_0",
        "FIDO_2_1_PRE"
      ],
      "extensions": [
        "credBlob",
        "credProtect",
        "hmac-secret"
      ],
      "aaguid": "{{aaguid}}",
      "options": {
        "uv": True,
        "userVerificationMgmtPreview": True,
        "credMgmt": True,
        "uvBioEnroll": True,
        "rk": True,
        "plat": False,
        "clientPin": False,
        "up": True,
        "bioEnroll": True,
        "credentialMgmtPreview": True
      },
      "maxMsgSize": 2048,
      "pinUvAuthProtocols": [
        1
      ],
      "maxCredentialCountInList": 20,
      "maxCredentialIdLength": 128,
      "transports": [
        "usb"
      ],
      "algorithms": [
        {
          "type": "public-key",
          "alg": -7
        },
        {
          "type": "public-key",
          "alg": -8
        }
      ],
      "firmwareVersion": 10013
    }
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "aaguid": "{{aaguid}}",\n    "metadataStatement": {\n        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",\n        "aaguid": "{{aaguid}}",\n        "description": "ATKey.Pro CTAP2.0",\n        "authenticatorVersion": 2,\n        "protocolFamily": "fido2",\n        "schema": 3,\n        "upv": [\n            {\n                "major": 1,\n                "minor": 0\n            }\n        ],\n        "authenticationAlgorithms": [\n            "secp256r1_ecdsa_sha256_raw"\n        ],\n        "publicKeyAlgAndEncodings": [\n            "cose"\n        ],\n        "attestationTypes": [\n            "basic_full"\n        ],\n        "userVerificationDetails": [\n            [\n                {\n                    "userVerificationMethod": "fingerprint_internal",\n                    "baDesc": {\n                        "selfAttestedFRR": 0,\n                        "selfAttestedFAR": 0,\n                        "maxTemplates": 0,\n                        "maxRetries": 0,\n                        "blockSlowdown": 0\n                    }\n                },\n                {\n                    "userVerificationMethod": "presence_internal"\n                },\n                {\n                    "userVerificationMethod": "passcode_internal"\n                }\n            ]\n        ],\n        "keyProtection": [\n            "hardware"\n        ],\n        "isKeyRestricted": false,\n        "isFreshUserVerificationRequired": true,\n        "matcherProtection": [\n            "on_chip"\n        ],\n        "attachmentHint": [\n            "external"\n        ],\n        "attestationRootCertificates": [\n            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",\n            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="\n        ],\n        "icon": "data:image/png;base64,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",\n        "authenticatorGetInfo": {\n            "versions": [\n                "U2F_V2",\n                "FIDO_2_0",\n                "FIDO_2_1_PRE"\n            ],\n            "extensions": [\n                "credBlob",\n                "credProtect",\n                "hmac-secret"\n            ],\n            "aaguid": "{{aaguid}}",\n            "options": {\n                "uv": true,\n                "userVerificationMgmtPreview": true,\n                "credMgmt": true,\n                "uvBioEnroll": true,\n                "rk": true,\n                "plat": false,\n                "clientPin": false,\n                "up": true,\n                "bioEnroll": true,\n                "credentialMgmtPreview": true\n            },\n            "maxMsgSize": 2048,\n            "pinUvAuthProtocols": [\n                1\n            ],\n            "maxCredentialCountInList": 20,\n            "maxCredentialIdLength": 128,\n            "transports": [\n                "usb"\n            ],\n            "algorithms": [\n                {\n                    "type": "public-key",\n                    "alg": -7\n                },\n                {\n                    "type": "public-key",\n                    "alg": -8\n                }\n            ],\n            "firmwareVersion": 10013\n        }\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "aaguid": "{{aaguid}}",
  "metadataStatement": {
    "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
    "aaguid": "{{aaguid}}",
    "description": "ATKey.Pro CTAP2.0",
    "authenticatorVersion": 2,
    "protocolFamily": "fido2",
    "schema": 3,
    "upv": [
      {
        "major": 1,
        "minor": 0
      }
    ],
    "authenticationAlgorithms": [
      "secp256r1_ecdsa_sha256_raw"
    ],
    "publicKeyAlgAndEncodings": [
      "cose"
    ],
    "attestationTypes": [
      "basic_full"
    ],
    "userVerificationDetails": [
      [
        {
          "userVerificationMethod": "fingerprint_internal",
          "baDesc": {
            "selfAttestedFRR": 0,
            "selfAttestedFAR": 0,
            "maxTemplates": 0,
            "maxRetries": 0,
            "blockSlowdown": 0
          }
        },
        {
          "userVerificationMethod": "presence_internal"
        },
        {
          "userVerificationMethod": "passcode_internal"
        }
      ]
    ],
    "keyProtection": [
      "hardware"
    ],
    "isKeyRestricted": false,
    "isFreshUserVerificationRequired": true,
    "matcherProtection": [
      "on_chip"
    ],
    "attachmentHint": [
      "external"
    ],
    "attestationRootCertificates": [
      "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
      "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
    ],
    "icon": "data:image/png;base64,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",
    "authenticatorGetInfo": {
      "versions": [
        "U2F_V2",
        "FIDO_2_0",
        "FIDO_2_1_PRE"
      ],
      "extensions": [
        "credBlob",
        "credProtect",
        "hmac-secret"
      ],
      "aaguid": "{{aaguid}}",
      "options": {
        "uv": true,
        "userVerificationMgmtPreview": true,
        "credMgmt": true,
        "uvBioEnroll": true,
        "rk": true,
        "plat": false,
        "clientPin": false,
        "up": true,
        "bioEnroll": true,
        "credentialMgmtPreview": true
      },
      "maxMsgSize": 2048,
      "pinUvAuthProtocols": [
        1
      ],
      "maxCredentialCountInList": 20,
      "maxCredentialIdLength": 128,
      "transports": [
        "usb"
      ],
      "algorithms": [
        {
          "type": "public-key",
          "alg": -7
        },
        {
          "type": "public-key",
          "alg": -8
        }
      ],
      "firmwareVersion": 10013
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"aaguid\": \"{{aaguid}}\",\n    \"metadataStatement\": {\n        \"legalHeader\": \"https://fidoalliance.org/metadata/metadata-statement-legal-header/\",\n        \"aaguid\": \"{{aaguid}}\",\n        \"description\": \"ATKey.Pro CTAP2.0\",\n        \"authenticatorVersion\": 2,\n        \"protocolFamily\": \"fido2\",\n        \"schema\": 3,\n        \"upv\": [\n            {\n                \"major\": 1,\n                \"minor\": 0\n            }\n        ],\n        \"authenticationAlgorithms\": [\n            \"secp256r1_ecdsa_sha256_raw\"\n        ],\n        \"publicKeyAlgAndEncodings\": [\n            \"cose\"\n        ],\n        \"attestationTypes\": [\n            \"basic_full\"\n        ],\n        \"userVerificationDetails\": [\n            [\n                {\n                    \"userVerificationMethod\": \"fingerprint_internal\",\n                    \"baDesc\": {\n                        \"selfAttestedFRR\": 0,\n                        \"selfAttestedFAR\": 0,\n                        \"maxTemplates\": 0,\n                        \"maxRetries\": 0,\n                        \"blockSlowdown\": 0\n                    }\n                },\n                {\n                    \"userVerificationMethod\": \"presence_internal\"\n                },\n                {\n                    \"userVerificationMethod\": \"passcode_internal\"\n                }\n            ]\n        ],\n        \"keyProtection\": [\n            \"hardware\"\n        ],\n        \"isKeyRestricted\": false,\n        \"isFreshUserVerificationRequired\": true,\n        \"matcherProtection\": [\n            \"on_chip\"\n        ],\n        \"attachmentHint\": [\n            \"external\"\n        ],\n        \"attestationRootCertificates\": [\n            \"MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=\",\n            \"MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk=\"\n        ],\n        \"icon\": \"data:image/png;base64,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\",\n        \"authenticatorGetInfo\": {\n            \"versions\": [\n                \"U2F_V2\",\n                \"FIDO_2_0\",\n                \"FIDO_2_1_PRE\"\n            ],\n            \"extensions\": [\n                \"credBlob\",\n                \"credProtect\",\n                \"hmac-secret\"\n            ],\n            \"aaguid\": \"{{aaguid}}\",\n            \"options\": {\n                \"uv\": true,\n                \"userVerificationMgmtPreview\": true,\n                \"credMgmt\": true,\n                \"uvBioEnroll\": true,\n                \"rk\": true,\n                \"plat\": false,\n                \"clientPin\": false,\n                \"up\": true,\n                \"bioEnroll\": true,\n                \"credentialMgmtPreview\": true\n            },\n            \"maxMsgSize\": 2048,\n            \"pinUvAuthProtocols\": [\n                1\n            ],\n            \"maxCredentialCountInList\": 20,\n            \"maxCredentialIdLength\": 128,\n            \"transports\": [\n                \"usb\"\n            ],\n            \"algorithms\": [\n                {\n                    \"type\": \"public-key\",\n                    \"alg\": -7\n                },\n                {\n                    \"type\": \"public-key\",\n                    \"alg\": -8\n                }\n            ],\n            \"firmwareVersion\": 10013\n        }\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")!,timeoutInterval: Double.infinity)
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
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "aaguid": "e1a96183-5016-4f24-b55b-e3ae23614cc6",
    "metadataStatement": {
        "aaguid": "e1a96183-5016-4f24-b55b-e3ae23614cc6",
        "description": "ATKey.Pro CTAP2.0",
        "protocolFamily": "fido2",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 0
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "cose"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "fingerprint_internal",
                    "baDesc": {
                        "selfAttestedFRR": 0,
                        "selfAttestedFAR": 0,
                        "maxTemplates": 0,
                        "maxRetries": 0,
                        "blockSlowdown": 0
                    }
                },
                {
                    "userVerificationMethod": "presence_internal"
                },
                {
                    "userVerificationMethod": "passcode_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware"
        ],
        "matcherProtection": [
            "on_chip"
        ],
        "attachmentHint": [
            "external"
        ],
        "attestationRootCertificates": [
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAf8CAQAwCgYIKoZIzj0EAwIDSQAwRgIhAPuVS4Pm2KFXdUMi5Pb/Xy+gCROOuRPZ6I57vWc0EvkBAiEA8aRCnXppAffCEOQBJ7vlgwiiHMXA2tpWX+ObvVKxXbM=",
            "MIIBzDCCAXGgAwIBAgIBATAKBggqhkjOPQQDAjBiMQswCQYDVQQGEwJTRTESMBAGA1UECgwJQVRLZXlDQTAwMSIwIAYDVQQLDBlBdXRoZW50aWNhdG9yIEF0dGVzdGF0aW9uMRswGQYDVQQDExJBdXRoZW50cmVuZCBDQSAwMDAwIBcNMTYwMjI2MDgxMTA2WhgPMjA1MDAyMjUwODExMDZaMGIxCzAJBgNVBAYTAlNFMRIwEAYDVQQKDAlBVEtleUNBMDAxIjAgBgNVBAsMGUF1dGhlbnRpY2F0b3IgQXR0ZXN0YXRpb24xGzAZBgNVBAMTEkF1dGhlbnRyZW5kIENBIDAwMDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABAJcWqeCxga9KJbFO2TZdjcgrtZAgfi8TXKu+v5lcR5ceb5GJYxyoCjhueESL3ddmMIkpGyhsEEtfFUyBwsyFVCjFjAUMBIGA1UdEwEB/wQIMAYBAQECAQAwCgYIKoZIzj0EAwIDSQAwRgIhAMqIc/Qtr+jZbnrJB7g7W8r/DHmDe+IyFvzwpzdSrxEXAiEAtXcixZznhcDzlnIqFqkIJRGmvL9Yr6lVoP1ZkDeqmjk="
        ],
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAA9CAIAAADAuAeYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAABGuSURBVHhe7ZwJfBPV9sczS/Y03Rco3XcKBVwRBHkiT58LqxvCE3AtoIICBQTZ2gItUigtVGihKPoXAR+yyPLhARZZ1EdVoPoQpKW0BVq6Zc9klvxPMrfQliZNl7QPP/l+LnTmnDuTyfzuvefcm0kws9kscHEvg6O/Lu5ZUC/8z4BnNL8WYYSIt3Y7HGsIeH5M/M4stO/CNkjCswPHan/5HRf/r0jI6gz+45/t/fkatO/CNmggxXhwHLbMNGM20d1TaEaAWy4DwzG4Ev7aXNgH9cLCR8ZBL8TEIjPHyWLCcYLo+jQHpDPTtO7iFUxIcnqD38vP9t6WgXwubNNUQpFQQDODq88Schnv7mKoylunAu4nlZ4uCR2neUYKirJaPdrpcjidAW25cJgWJxVdPYQ2ohtf+l7FNS+85+lMCVmDkTOZOBPF0TSHbC6cTqdJqP/vle9k0af8Hjrp++BJZT+mph45XDiZTpPwYuICAhebWVbAmVmjoWSxa1beRXSOhPristoTx3GFDCMIjMAJhdv1TdtpjRa5XTiTzpHw8rSFBOmBYRirN3IUIyAwAU2XLs5EbhfOpBMkNJTdqD58hJBKYELpN/455cN9zRRNKOTlG75g9K55ntPpBAkvTV9MkAoBJmBYTVTWorDUObSxDoZTjjJeS3Z91OB0OiQhzMMN16uq9x3CZVJOb/AZMUKodPMYfL8iKp6jaFIuL1+/jaNMqLYL59AhCTGB4MrMFIIQwzbNqGJyV/D2yDULGGM9dETIaErTN/JGF06iQxJSlbeqdu63dEGD0XvIMGlIIG/3eeZvssgYmOALZfKyNfkczfB2F86gQxJeSUrDcEIAiSitjtmYiqxWIlfOZQxqgZBg62rL1my22lzrn06h/RJS1bVVn+8l5FLOSHkMHCSPi0QOK77jnpKFRppNDC5TlGVsZs2cddx10fm0X8KShRlmM2vpgib17SjYmLC0JMagwUjCVHmrYt1nyOqis2mnhHS96mb+LkIuMzOMcsADsqhQqqoaQuPtYrpV6/X4I9KgYAHLEVJZ+apc1zDqJNopYcmSdWYTDTknRpLG4rKTnv1/CB7yQ8jQ2+VM0OAzIY8yKq2AwHEhaaiouL7pS3Swi06lPRIyWv3N3O3WhzMsz0yZIc6RJCYSNi8EASkMVIBapFR+bcUn6HgXnUrzZ2egbz1SekLk78u7W+TSe0uvZX1Ckm5oH4HhMgnIBVsgKmegmqWgNFPXOyczMPEVtN8ShuLSMxFD7n52JjdvS0HBCYlYrKeopYsWRkU1SZ2akZyS+uefxUJSCNdSr6p/8IEH5ibNrqmpfStxuqe7u9FkHDjw4XemTd29Z++Or3bI5Qo7mbKJNvVLSJg1a2ZxcfGsOfO8Pb04M0eQRO7GHFTDNnq94d0ZM+FO4BheW1+/MSfb19feXW03JPrrMGaW5erUPV56wdrJGoC+JiKrvtwvEAlBQFws9h33pOWJwkZ3hzPRhj+uoJ02cuHChf3fHpDL5VqdbuZ77yBrSyTNnb8pb7NcJocrUqnU8fFxu3ZsBztFGffs3Rvg76/T6iRiCVj+vHxl7/4Dnh4eZtsaGg1GygRtURAeHn6hqEij1pAkWa9SjRk9+ul/PMnXscXWrZ/u3Pm1m9LNaKDuG9DfSfoBbZYQlIvdthrtNOVG/g5S5G5mWDLQIy5/FbJ2BiKxWCqXQWEFHMRWZL2LufPm5+bn+/j6gn5wo/sPSPj+u2O8C7qCVGo5A2c2w9nAIhTC6G6x2JEQw3GRxKI3kJaaMuXtRH8Pd5wkl6eltSohtCRPH2+RUKjRaFNSliCrE2hbLKQp09Xl60tXbLianFX+yd3pScO9YFm0YQWspatyr6Zml8KxGVts3rCOMW/+wo15+d5e3tb+p4qLir6tX4vo9LqayltVllJtp6jrVXz9cc+PVcjkLMeKxaLffv+9sLCQt7fI9q92lJVXCIVCiqL6D+j38EMPIYcTaJuEFRn5lxYsvvLhqouL5pEyS1t2BAiPdFXNHws/urJg1aVZc27tOYIcnceChR/lbMr18bHqp1ZHhoefKDiKfDaY9f7M2pqbZSWXym2XqhulX2zbig6AV5k3R1WngpdQSGXJKSuRtSXWZa9XKOTwxuvqVR8mzUFW59AGCSEKlmfkSWQBhETqHv5gwKtjkcMBwlLel7gFEQo3kcjvqvWj4E7si/MXfJSVs9HX1wdurlqtjouOPn2yAPlsI5FIPD09le7udoqHh4dCoUAHCATTp0/DMYzjOJFEeurMqeLiEuRoysFDhy/+cVkoEtE0HR0R8dRTrQy5HaQNEpZnfWaqrhIICcaoDkttU8syE2Jx0MwprFaNSUTac+dqDp3orNW2JUuTczZu8rPGP7VaA8lqwfF/I1+LYB1qPW++8ZpGq8NxTCgUp6V/jKxNWbs2SyaXwfVAPJ71wQxkdRoOS8iZyz7OJaQKs4mRBocFvPwMsjuERa+g2a8TCqWA4wiRvLMejlqyNGVt9nofH0v/02g08bGxJ+3GPwtm69W0l6SkOSajEWZikBvtP3CgtrYGORo4feaHs7/+AvMfhmEC/QNeGf8ycjgNRyUsz/vSWFGOCUnaoA5b0p6WJVQqA6e+wmo1mESs+qmw9vgZ5Ggvy9PSIeT4eFviH6T70VFRR44cRD7bgH4dkdDDXTl2zCiY8+E4TjPsuqwNyNHA2rWZoB8/JCQmvoWszsQhCSG/LFu50dIFaUYaGNRjyvPI0UaCkt7GYSoNHVEo4yNiO8AJyzUvX5m+Kn21l7cXTEmh//WOiz125JCd+cZtYBTlB9Kqqqpfz50v+u13O+X8+aKSq80D3sL583RaLXRESFi2/d+XEPCQQyAoKvr9u+9PSqVSlmXdPZSvTZmMHM7EIQmrtn6tLymB4Z81aEI+nIasbUfs49VzygssxBKpuP770/WnLXl5myITZBNKN7fs9TnpqzO8fX1APxNFxcfFHT64HybdqJJj5OZtGTDggUFDhw0aYrPcP3DQjPdnowMaCI8If2zoECNF4QShUqnzNm9BDoEgMysLjPyo/uqECfIu+YKYQ822dHmOUCI3M4w4oGfPt+2tkLVK0PxEHCbLHIeT0pJFa5HVYWRSacrytOQVK72t46fAbGYoU+7GHJiBoRqt0jCMKuQKH39/fz8/+GerBPj7QVaKDmjEgg/nqVUqzCyQK2Sb8pCEpdeuHThwSC6TQcoqkYindckoCrQuYeX2/frLlwUiEavXBs15gx/H2ge0BklPf/+JY1itHpdJ6o6eUJ0tcjwyWTTD8CPHjrkpFNAdeQtGEnOS5vMVHKKh1xuNhrq6OlV9fX1dnZ2i17XwQPPDDz2Y0LcPRZuEpLC8vGL3N9+AEcYGmmUgRmp1urGjR/n5+fGVnU3ry9w/9n3K+Oc1DOKMTDqw7CRpXZ1qkWNYCKn0gHgp7uU/8JLNzNBQWvFj9HBcJOSMlOcTg/sdzEcO28vcs5PmffHl9sZTNJPJRJtoyN1Bxprq6pRlS6ZPTUS+lrh542ZUXN+AHv56rW7UqJEbsjNPnjp17Ph3MDtENVqCppnIiPCXXnwB7Tdiz779r05+3c/P12g0xsXE7Nvzr9j4BMtXzDFMr9OdPHEsIjwCVXUyrcSP6/m76otOkQIvRqCOmZ9sRz/ALGAt39NnoDRZYGuGNCTQ78Wnb37+L0Iqu3XosOb8RbeEWORzDK1W2yc+ftjQIZmZ2UovD08vr2Upy0cMHx4dHYVq2OZ26H108GAoaKftjHru2eBegRqdXiwWXy4uHj9xEs0wkMjAtT054gk7+jEMu/2rrwICAmBI0Wg1JpoOCw3pl9BPJHI4FjTF3qgI7xb6ZUxKWlT6gtjlK3rOfB05bCD08hX6+wgDfElfL2SyQcjiGeLAQKG/r8SvV1nGnXTAEeAeBQf12v/N1xCQ+t3Xz6DXwwAhEgqnvN5Fsec2774zXaW2rLcROFb488+gHwxpDM3MnPEuqtESJGn5HYORY55/dvSYc+fOUxQ1aswLUbG9YUhANdoKnA44O3Dsd+LYAre+8D91s4o3QljmNxyhWVXHj4RXuV1Zf+XqUUFQgTLhOBn128T3kdVsnjVnbkCvkMjY+KCwyEGPPgZvm7eXlpUFBoeFRcZExMZ7+/VY8NFi3n43N67fULj7wBl69AqdOv09ZO0Y0IFCw6PComIjY3tHxMTDyQNDwkeNGYfcdomK66P08r106RJsnzx1WqrwCI+MNRgsiwZtxV4vtKQPDtOsapuSFAcrw+VC/FuXmSESod/HCe7VKzV5aX29Cnwenp7Z2Rt++s9Z3tUFCEnytSmTNCoNbFuzYzNo8MFMx9c9MMpo+TAyNjbGTeEGg2p5RTnvqKyqgv9rqmsqypEFKDz787Lk1G2ffwF5ADJZaUnC2+Gi62n1pTEzhjW55kmv/nPE8L/pNFpoCR5enhP+OQk5bNGxNdJmvPfuOxKZGMYR2IY727dvn6FDh/Au+6BrsLZevV5nNBkJgoQZTlb2+lDo1PH9Pv1sG/xNGPAQTDGhDnTuF1+Z8NLLL3762RdePgGNW2oLElp+tqe7aO2l4Z3DyIt2Gsjfslkmk9E0DbNDlUrTSlDs2BppM9zd3UNDQlnWEgogSM98dzpytAZcA8jHT2cXLlisrq2bNHGCm5sbxNeQ4F6EULh9567nnntu0KCHwThn3od7v9m7Oj0tJipqS94nQrF45Og7HxM1l9AMN9Fu2ulUMMsI2eY7LJNJczZkq1QquI/u7sodu3btP2BzsdRy79BmJ3D06PFz5y+AEtCAIsMjRo8aiRwOIJfLZ8+bHx0bf/HS5d27v165Ej0Ob2mOFJW1ZvVn+Xn79uxmaPrbAweU3l49A3uCNzg42MfbS6XWnDmDFpmbTipgkCLIH8MfE9zV0rsCGOLg9d2U/DNUbeLvI4ZPGP/Sjl27QULI1ye/9sa1kssyaQvrW5Z+bN1Yty47dWU61LfutYyRMj4+bNjWLXlo/y5WpKd7KJVmgaULLl20EFkdQ6fVZa/JCAkNQfsNQEOE9w9hld/V6Q0URYMFJqC8BaYxkARTDRGxSS+0JBY4xplojmG7odCs5QF+jGhfN8lelxkY4A/JKg5zDLF47LhWPuVhOY6GGQDL2ingpps+RNKYwsKff/zprEgqgXo9/QNenTgROVri0OHDGzbc+ZIXNFNoSTp9C7/SxLfg20keNLIe8L5MpqtXr/IWPajLsv0T+vO7SEKYj1uUo0yW37Jj2O4rcBkmuAyOsVwGf20AwzCQLJggiwev7R+Hy9+SB00bWivkiscLCrLX33lUEJq2CQ62nMMEZ7NYODPrAHyq0iIr0lYplW5wp7V63eTJk+wsPUIfhSY1fXpiQcEJZNGooYlUVlbyu43R6XQmFhrXna+DLVu8iMDwzMxs2D59+oeSPy/PTZrt4enOe9EC24WxibqiyzCR562OA2/A5h1tzWsHzkD5jBwetQYNTanLV36zd59UKoHhZfOmjQkJfXj73axavWbnrq8lUgm8r5qa2u+PHfX2sawzVFZVPv7EP7y9vYwGw99HjEhJXrJly9bsnE8UbncW7e4G+vSgRx5Z83E62m9EcXHJfQ8O9PH1AY2hw5wvPCtXyJGvJd6b8UHRb7/t27tbr9O++ea0G7cqhYQQJ7DRI0d+8P6decjSZckHDh3GCcLT3X3a1MRnn3mat//yy6/LV6ykGAYXYONffrHxmp9FQhCxodf+1YD7C+Mq2ulU3nhr6rcHDyoUCrVa/cZrk1OTlyFHl2OV0Npd2of9Yzty5v9lbt2qjo1PgGkoDNAmiir86UyXfS5xN5YW2pG7bP/Yv6R+wKqMNaSQxDEM8hEY67pRPwDFQheOYzAawyOiZdZPviD1OH3ieHh4OO/qFpwSJ/7awIQSkkkIsaDlsKFDulc/wNUL20yv0AiRSAQSqupVRw7t699/AHJ0E65e2DbSV62uKC2rq62/XnGjT5/4btcPcPXCtnHu3HmaoaELMgwbFhrivK+cOY5Lwnse10B6jyMQ/D/exLg8R/4sQAAAAABJRU5ErkJggg==",
        "authenticatorGetInfo": {
            "versions": [
                "U2F_V2",
                "FIDO_2_0",
                "FIDO_2_1_PRE"
            ],
            "extensions": [
                "credBlob",
                "credProtect",
                "hmac-secret"
            ],
            "aaguid": "e1a9618350164f24b55be3ae23614cc6",
            "options": {
                "uv": true,
                "userVerificationMgmtPreview": true,
                "credMgmt": true,
                "uvBioEnroll": true,
                "rk": true,
                "plat": false,
                "clientPin": false,
                "up": true,
                "bioEnroll": true,
                "credentialMgmtPreview": true
            },
            "maxMsgSize": 2048,
            "pinUvAuthProtocols": [
                1
            ],
            "maxCredentialCountInList": 20,
            "maxCredentialIdLength": 128,
            "transports": [
                "usb"
            ],
            "algorithms": [
                {
                    "type": "public-key",
                    "alg": -7
                },
                {
                    "type": "public-key",
                    "alg": -8
                }
            ],
            "firmwareVersion": 10013
        },
        "keyRestricted": false,
        "freshUserVerificationRequired": false
    },
    "createdAt": "2022-07-26T13:22:25.846Z",
    "updatedAt": "2022-07-26T13:22:25.846Z"
}
```

---

---
title: Add Custom FIDO Device - u2f
description: Use POST {{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata to add a custom FIDO device to the Global Authenticators table.
component: pingone-api
page_id: pingone-api:mfa:fido-policies/add_custom_fido_device_utf
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/fido-policies/add_custom_fido_device_utf.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Add Custom FIDO Device - u2f

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata
```

Use `POST {{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata` to add a custom FIDO device to the Global Authenticators table.

The data included in the request should comform with the [Metadata Statement Format](https://fidoalliance.org/specs/mds/fido-metadata-statement-v3.0-ps-20210518.html#metadata-statement-format) provided by the FIDO Alliance.

If you are using JSON data provided by a manufacturer, verify that it conforms to the following details expected by the PingOne API:

* The metadata outlined in the standard should be enclosed in an object called `metadataStatement`.

* The `metadataStatement` should be enclosed in an object that also includes the relevant key identifier. This example adds a device that is compliant with the U2F protocol so the relevant identifier is the `attestationCertificateKeyIdentifiers` array.

### Prerequisites

* Refer to [FIDO Policies](#fido-policies) for important overview information.

> **Collapse: Request Model**
>
> | Property                               | Type   | Required |
> | -------------------------------------- | ------ | -------- |
> | `attestationCertificateKeyIdentifiers` | Array  | Required |
> | `metadataStatement`                    | Object | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "attestationCertificateKeyIdentifiers": [
        "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "attestationCertificateKeyIdentifiers": [
            "31116a647069d1493f58fc5b54e5449e2a52d43e"
        ],
        "description": "Yubikey Edge",
        "authenticatorVersion": 1,
        "protocolFamily": "u2f",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 1
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "ecc_x962_raw"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "presence_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware",
            "secure_element",
            "remote_handle"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": false,
        "matcherProtection": [
            "on_chip"
        ],
        "cryptoStrength": 128,
        "attachmentHint": [
            "external",
            "wired"
        ],
        "attestationRootCertificates": [
            "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
        ],
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAfCAYAAACGVs+MAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAHYYAAB2GAV2iE4EAAAbNSURBVFhHpVd7TNV1FD/3d59weQSIgS9AQAXcFLAQZi9fpeVz1tY/WTZr5Wxpc7W5knLa5jI3Z85srS2nM2sjtWwZS7IUH4H4xCnEQx4DAZF74V7us885v9/lInBvVJ/B4Pv9nu/5nu/5nvM556fzA/Qv0Hb/IrX3VFKPo45cnm4inUIWYwLFRmZQUuwjFG/N1iRHh1EZ0NRVRudqt1Bd+2nSKyS/Ohys0+lk3e/3kQ9qvD4ZUta4VVSUuY0eipyiThAfocoORVgDuuw3qKRiAd3rbcEtjTjYIof6WaHsCmzVPWCMx+cgh8tLqWMKaMWsUjLqo2RtJIQ0oOzmerpQu4esZgsONkGxH7d0kdvTT17s4OMU7VI8ZhjgGaM+Aq9iENu8Pif1udz07MwvKWf8GlVoCEY04PC5WdTaXYFbR8vNvL5+3Kgfb5xNMya9RamJiynaMlGTVtFlr6ba9u+pqnEX4uMuRRgjSYEhrN7utFFe6lqal7Nfkw5imAGHynPpbk8VmY0xstnptlFCVCYtzTuBN83QpMLjTtevdPzSUnJ7e8mkjxZ39fXbKDfldZqbvU+TUgGnBVF6fQ2iPHg4W16UWUwvzbk16sMZE+Pn0pvz7JSeuAyes8lcpCmaKuo/p+qWr2UcwIAHWrvP0YEzhXAtLAbssHhp7iGamvyijP8ryqrXUWX9XoowxyAufNBrp43POBFXZlkf8MDRiqcpyowAwpuz2x+fWvz/Dtde9smszygtcR6C1wbdzBl6Olq5WNYY4oGathJMrkTEx0jARSHAVs+5rYkQNXb+QgfPLsQ6gXyInsreQfmpm7RVFYfL86n1fiUOkYvShkUPxvbukzoy6K1ihM1ho3XzW6EvSfXA+dpiWGaWd+doXzLzmGwKYFLCAsRAlPBAhMlCFXU7tBUVPr8HgVcJHWq+F00plr+DMTdrP4zvxY11kNMhxT+SeTGg+d4V5LQJityUGJNB8VFZsjgYBZM/II/XCTkj0qyDOpF2AVQ17CIjUp/DnT1UkL5F5gdj+sS1wg1gE3gigm60fCXzSnPXbyAPbIXv+IDpE16ThaHIS9skyhlmME5F3cfqAKhq2C0E5PH1gYaXaLPDkZG0HDJOnKWHp51I0z5SOux8e1WAuZzdHQrTkp8TmjXoI+la0wGZszubqbO3ifQ6A/W7vVSYsV3mR0JKwkKc4WHiBkmR8I3CCgI87oOL4qzT5P+RUJBejEOgAPK8hYPzatM+eITp2IO9yTQmeromPRxx1qxAcsile/ubSeEbcWQGYECghcLY2HyKjogjH25hMpjpUv1Ougli4eh2eRw0O32bJjkyuCgNzg0vzlYMSiSs0uoo4MG7hMOjCEaX1yFE0nSvjBzuTnEpK86Z8IoqFAIubw8kg9ArEaREWSZI+jH4Xbp6g9E9EnJT3oaRzDN+MUJBQDHn56a8oUmEBusOxBs/N5+tJEbPkAFDj8UGvOs/IWvcSglGBhvS7/FTYfpWGYdDY8fPAxWSA35sTC4p4+Lm4AaqIoPeQtfufK6Jh0ZhxlbsUXOSmXNifD5ZTAkyDofbbcclxnA8WNAqxCbRNykhXxQpaDw67fXUYbsiG0Khtv2oeIvh8rhQMYOcEAqXG/eI+zngOc5yxr8q82IAM1c/FLFOplqu5eFQXrMZzGcVCjYbLWG5I4BT1euRrlbxtNOtMitDDEhLXIIynAAvuOEWE3X3NdAft94VgaG42XIQt0ZX6PeCE/qQFe9rK6Hx7YU50KvH7fW4fS+q7KKBJxsggBX5pSAGh1jIrVh5zQ6w3RfaahBXm/aCbCZTjCUFUTyWZqW9p62MjJPXVqOrPgMO4Nv74Gkf+owftNVBDQnjFJqHSw17pXvhWW5KZqe/Q49N/USTCAVWoQXFIHBHXXe3FPrUDsuGDmtF/hHKTHpekxhiAOPI+SJq6S6HF4I9YWzkBJTo46iUMzWp8Pir/RiduLxKYsSksV8vLlOQvhGX2YlR0OBhBjC+u/gEcvY0ApK7Yk41NxjPSQnWFHTF66UrjgevB8Cu5a+l2vYSRPtuVDo73hhdMSHnUX7tTjsVZGxAl/WptiOIEQ1gnL29mX6/tR1tmlkYj8W4X+CSjWcUDGY1NpS/C7hSKqiMLM/l2QmSWZ73Ddz+gio8BCENYPQ46qnkzwXUbqvBkxjUQsWfZFgbuo3rAf+wN7jOO90+ynx4Pi3L+0nYL1SchDUgAP4gPV/7Id1q+1HShmuGkIqWRPgyxMFqP8HfjTnjXwY5bQfbJct6OIzKgMHotF/He1egsaxHSqG6wfdmQ5x8NyTFFqBcp2iSowHR3yk5+36hF7vXAAAAAElFTkSuQmCC"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "attestationCertificateKeyIdentifiers": [
        "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "attestationCertificateKeyIdentifiers": [
            "31116a647069d1493f58fc5b54e5449e2a52d43e"
        ],
        "description": "Yubikey Edge",
        "authenticatorVersion": 1,
        "protocolFamily": "u2f",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 1
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "ecc_x962_raw"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "presence_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware",
            "secure_element",
            "remote_handle"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": false,
        "matcherProtection": [
            "on_chip"
        ],
        "cryptoStrength": 128,
        "attachmentHint": [
            "external",
            "wired"
        ],
        "attestationRootCertificates": [
            "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
        ],
        "icon": "data:image/png;base64,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"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""attestationCertificateKeyIdentifiers"": [" + "\n" +
@"        ""31116a647069d1493f58fc5b54e5449e2a52d43e""" + "\n" +
@"    ]," + "\n" +
@"    ""metadataStatement"": {" + "\n" +
@"        ""legalHeader"": ""https://fidoalliance.org/metadata/metadata-statement-legal-header/""," + "\n" +
@"        ""attestationCertificateKeyIdentifiers"": [" + "\n" +
@"            ""31116a647069d1493f58fc5b54e5449e2a52d43e""" + "\n" +
@"        ]," + "\n" +
@"        ""description"": ""Yubikey Edge""," + "\n" +
@"        ""authenticatorVersion"": 1," + "\n" +
@"        ""protocolFamily"": ""u2f""," + "\n" +
@"        ""schema"": 3," + "\n" +
@"        ""upv"": [" + "\n" +
@"            {" + "\n" +
@"                ""major"": 1," + "\n" +
@"                ""minor"": 1" + "\n" +
@"            }" + "\n" +
@"        ]," + "\n" +
@"        ""authenticationAlgorithms"": [" + "\n" +
@"            ""secp256r1_ecdsa_sha256_raw""" + "\n" +
@"        ]," + "\n" +
@"        ""publicKeyAlgAndEncodings"": [" + "\n" +
@"            ""ecc_x962_raw""" + "\n" +
@"        ]," + "\n" +
@"        ""attestationTypes"": [" + "\n" +
@"            ""basic_full""" + "\n" +
@"        ]," + "\n" +
@"        ""userVerificationDetails"": [" + "\n" +
@"            [" + "\n" +
@"                {" + "\n" +
@"                    ""userVerificationMethod"": ""presence_internal""" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        ]," + "\n" +
@"        ""keyProtection"": [" + "\n" +
@"            ""hardware""," + "\n" +
@"            ""secure_element""," + "\n" +
@"            ""remote_handle""" + "\n" +
@"        ]," + "\n" +
@"        ""isKeyRestricted"": false," + "\n" +
@"        ""isFreshUserVerificationRequired"": false," + "\n" +
@"        ""matcherProtection"": [" + "\n" +
@"            ""on_chip""" + "\n" +
@"        ]," + "\n" +
@"        ""cryptoStrength"": 128," + "\n" +
@"        ""attachmentHint"": [" + "\n" +
@"            ""external""," + "\n" +
@"            ""wired""" + "\n" +
@"        ]," + "\n" +
@"        ""attestationRootCertificates"": [" + "\n" +
@"            ""MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw==""" + "\n" +
@"        ]," + "\n" +
@"        ""icon"": ""data:image/png;base64,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""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata"
  method := "POST"

  payload := strings.NewReader(`{
    "attestationCertificateKeyIdentifiers": [
        "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "attestationCertificateKeyIdentifiers": [
            "31116a647069d1493f58fc5b54e5449e2a52d43e"
        ],
        "description": "Yubikey Edge",
        "authenticatorVersion": 1,
        "protocolFamily": "u2f",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 1
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "ecc_x962_raw"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "presence_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware",
            "secure_element",
            "remote_handle"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": false,
        "matcherProtection": [
            "on_chip"
        ],
        "cryptoStrength": 128,
        "attachmentHint": [
            "external",
            "wired"
        ],
        "attestationRootCertificates": [
            "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
        ],
        "icon": "data:image/png;base64,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"
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
POST /v1/environments/{{envID}}/fidoDevicesMetadata HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "attestationCertificateKeyIdentifiers": [
        "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "metadataStatement": {
        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
        "attestationCertificateKeyIdentifiers": [
            "31116a647069d1493f58fc5b54e5449e2a52d43e"
        ],
        "description": "Yubikey Edge",
        "authenticatorVersion": 1,
        "protocolFamily": "u2f",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 1
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "ecc_x962_raw"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "presence_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware",
            "secure_element",
            "remote_handle"
        ],
        "isKeyRestricted": false,
        "isFreshUserVerificationRequired": false,
        "matcherProtection": [
            "on_chip"
        ],
        "cryptoStrength": 128,
        "attachmentHint": [
            "external",
            "wired"
        ],
        "attestationRootCertificates": [
            "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
        ],
        "icon": "data:image/png;base64,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"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"attestationCertificateKeyIdentifiers\": [\n        \"31116a647069d1493f58fc5b54e5449e2a52d43e\"\n    ],\n    \"metadataStatement\": {\n        \"legalHeader\": \"https://fidoalliance.org/metadata/metadata-statement-legal-header/\",\n        \"attestationCertificateKeyIdentifiers\": [\n            \"31116a647069d1493f58fc5b54e5449e2a52d43e\"\n        ],\n        \"description\": \"Yubikey Edge\",\n        \"authenticatorVersion\": 1,\n        \"protocolFamily\": \"u2f\",\n        \"schema\": 3,\n        \"upv\": [\n            {\n                \"major\": 1,\n                \"minor\": 1\n            }\n        ],\n        \"authenticationAlgorithms\": [\n            \"secp256r1_ecdsa_sha256_raw\"\n        ],\n        \"publicKeyAlgAndEncodings\": [\n            \"ecc_x962_raw\"\n        ],\n        \"attestationTypes\": [\n            \"basic_full\"\n        ],\n        \"userVerificationDetails\": [\n            [\n                {\n                    \"userVerificationMethod\": \"presence_internal\"\n                }\n            ]\n        ],\n        \"keyProtection\": [\n            \"hardware\",\n            \"secure_element\",\n            \"remote_handle\"\n        ],\n        \"isKeyRestricted\": false,\n        \"isFreshUserVerificationRequired\": false,\n        \"matcherProtection\": [\n            \"on_chip\"\n        ],\n        \"cryptoStrength\": 128,\n        \"attachmentHint\": [\n            \"external\",\n            \"wired\"\n        ],\n        \"attestationRootCertificates\": [\n            \"MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw==\"\n        ],\n        \"icon\": \"data:image/png;base64,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\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "attestationCertificateKeyIdentifiers": [
      "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "metadataStatement": {
      "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
      "attestationCertificateKeyIdentifiers": [
        "31116a647069d1493f58fc5b54e5449e2a52d43e"
      ],
      "description": "Yubikey Edge",
      "authenticatorVersion": 1,
      "protocolFamily": "u2f",
      "schema": 3,
      "upv": [
        {
          "major": 1,
          "minor": 1
        }
      ],
      "authenticationAlgorithms": [
        "secp256r1_ecdsa_sha256_raw"
      ],
      "publicKeyAlgAndEncodings": [
        "ecc_x962_raw"
      ],
      "attestationTypes": [
        "basic_full"
      ],
      "userVerificationDetails": [
        [
          {
            "userVerificationMethod": "presence_internal"
          }
        ]
      ],
      "keyProtection": [
        "hardware",
        "secure_element",
        "remote_handle"
      ],
      "isKeyRestricted": false,
      "isFreshUserVerificationRequired": false,
      "matcherProtection": [
        "on_chip"
      ],
      "cryptoStrength": 128,
      "attachmentHint": [
        "external",
        "wired"
      ],
      "attestationRootCertificates": [
        "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
      ],
      "icon": "data:image/png;base64,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"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "attestationCertificateKeyIdentifiers": [
      "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "metadataStatement": {
      "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
      "attestationCertificateKeyIdentifiers": [
        "31116a647069d1493f58fc5b54e5449e2a52d43e"
      ],
      "description": "Yubikey Edge",
      "authenticatorVersion": 1,
      "protocolFamily": "u2f",
      "schema": 3,
      "upv": [
        {
          "major": 1,
          "minor": 1
        }
      ],
      "authenticationAlgorithms": [
        "secp256r1_ecdsa_sha256_raw"
      ],
      "publicKeyAlgAndEncodings": [
        "ecc_x962_raw"
      ],
      "attestationTypes": [
        "basic_full"
      ],
      "userVerificationDetails": [
        [
          {
            "userVerificationMethod": "presence_internal"
          }
        ]
      ],
      "keyProtection": [
        "hardware",
        "secure_element",
        "remote_handle"
      ],
      "isKeyRestricted": false,
      "isFreshUserVerificationRequired": false,
      "matcherProtection": [
        "on_chip"
      ],
      "cryptoStrength": 128,
      "attachmentHint": [
        "external",
        "wired"
      ],
      "attestationRootCertificates": [
        "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
      ],
      "icon": "data:image/png;base64,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"
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

url = "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata"

payload = json.dumps({
  "attestationCertificateKeyIdentifiers": [
    "31116a647069d1493f58fc5b54e5449e2a52d43e"
  ],
  "metadataStatement": {
    "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
    "attestationCertificateKeyIdentifiers": [
      "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "description": "Yubikey Edge",
    "authenticatorVersion": 1,
    "protocolFamily": "u2f",
    "schema": 3,
    "upv": [
      {
        "major": 1,
        "minor": 1
      }
    ],
    "authenticationAlgorithms": [
      "secp256r1_ecdsa_sha256_raw"
    ],
    "publicKeyAlgAndEncodings": [
      "ecc_x962_raw"
    ],
    "attestationTypes": [
      "basic_full"
    ],
    "userVerificationDetails": [
      [
        {
          "userVerificationMethod": "presence_internal"
        }
      ]
    ],
    "keyProtection": [
      "hardware",
      "secure_element",
      "remote_handle"
    ],
    "isKeyRestricted": False,
    "isFreshUserVerificationRequired": False,
    "matcherProtection": [
      "on_chip"
    ],
    "cryptoStrength": 128,
    "attachmentHint": [
      "external",
      "wired"
    ],
    "attestationRootCertificates": [
      "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
    ],
    "icon": "data:image/png;base64,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"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "attestationCertificateKeyIdentifiers": [\n        "31116a647069d1493f58fc5b54e5449e2a52d43e"\n    ],\n    "metadataStatement": {\n        "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",\n        "attestationCertificateKeyIdentifiers": [\n            "31116a647069d1493f58fc5b54e5449e2a52d43e"\n        ],\n        "description": "Yubikey Edge",\n        "authenticatorVersion": 1,\n        "protocolFamily": "u2f",\n        "schema": 3,\n        "upv": [\n            {\n                "major": 1,\n                "minor": 1\n            }\n        ],\n        "authenticationAlgorithms": [\n            "secp256r1_ecdsa_sha256_raw"\n        ],\n        "publicKeyAlgAndEncodings": [\n            "ecc_x962_raw"\n        ],\n        "attestationTypes": [\n            "basic_full"\n        ],\n        "userVerificationDetails": [\n            [\n                {\n                    "userVerificationMethod": "presence_internal"\n                }\n            ]\n        ],\n        "keyProtection": [\n            "hardware",\n            "secure_element",\n            "remote_handle"\n        ],\n        "isKeyRestricted": false,\n        "isFreshUserVerificationRequired": false,\n        "matcherProtection": [\n            "on_chip"\n        ],\n        "cryptoStrength": 128,\n        "attachmentHint": [\n            "external",\n            "wired"\n        ],\n        "attestationRootCertificates": [\n            "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="\n        ],\n        "icon": "data:image/png;base64,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"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "attestationCertificateKeyIdentifiers": [
    "31116a647069d1493f58fc5b54e5449e2a52d43e"
  ],
  "metadataStatement": {
    "legalHeader": "https://fidoalliance.org/metadata/metadata-statement-legal-header/",
    "attestationCertificateKeyIdentifiers": [
      "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "description": "Yubikey Edge",
    "authenticatorVersion": 1,
    "protocolFamily": "u2f",
    "schema": 3,
    "upv": [
      {
        "major": 1,
        "minor": 1
      }
    ],
    "authenticationAlgorithms": [
      "secp256r1_ecdsa_sha256_raw"
    ],
    "publicKeyAlgAndEncodings": [
      "ecc_x962_raw"
    ],
    "attestationTypes": [
      "basic_full"
    ],
    "userVerificationDetails": [
      [
        {
          "userVerificationMethod": "presence_internal"
        }
      ]
    ],
    "keyProtection": [
      "hardware",
      "secure_element",
      "remote_handle"
    ],
    "isKeyRestricted": false,
    "isFreshUserVerificationRequired": false,
    "matcherProtection": [
      "on_chip"
    ],
    "cryptoStrength": 128,
    "attachmentHint": [
      "external",
      "wired"
    ],
    "attestationRootCertificates": [
      "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
    ],
    "icon": "data:image/png;base64,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"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"attestationCertificateKeyIdentifiers\": [\n        \"31116a647069d1493f58fc5b54e5449e2a52d43e\"\n    ],\n    \"metadataStatement\": {\n        \"legalHeader\": \"https://fidoalliance.org/metadata/metadata-statement-legal-header/\",\n        \"attestationCertificateKeyIdentifiers\": [\n            \"31116a647069d1493f58fc5b54e5449e2a52d43e\"\n        ],\n        \"description\": \"Yubikey Edge\",\n        \"authenticatorVersion\": 1,\n        \"protocolFamily\": \"u2f\",\n        \"schema\": 3,\n        \"upv\": [\n            {\n                \"major\": 1,\n                \"minor\": 1\n            }\n        ],\n        \"authenticationAlgorithms\": [\n            \"secp256r1_ecdsa_sha256_raw\"\n        ],\n        \"publicKeyAlgAndEncodings\": [\n            \"ecc_x962_raw\"\n        ],\n        \"attestationTypes\": [\n            \"basic_full\"\n        ],\n        \"userVerificationDetails\": [\n            [\n                {\n                    \"userVerificationMethod\": \"presence_internal\"\n                }\n            ]\n        ],\n        \"keyProtection\": [\n            \"hardware\",\n            \"secure_element\",\n            \"remote_handle\"\n        ],\n        \"isKeyRestricted\": false,\n        \"isFreshUserVerificationRequired\": false,\n        \"matcherProtection\": [\n            \"on_chip\"\n        ],\n        \"cryptoStrength\": 128,\n        \"attachmentHint\": [\n            \"external\",\n            \"wired\"\n        ],\n        \"attestationRootCertificates\": [\n            \"MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw==\"\n        ],\n        \"icon\": \"data:image/png;base64,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\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/fidoDevicesMetadata")!,timeoutInterval: Double.infinity)
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
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "attestationCertificateKeyIdentifiers": [
        "31116a647069d1493f58fc5b54e5449e2a52d43e"
    ],
    "metadataStatement": {
        "attestationCertificateKeyIdentifiers": [
            "31116a647069d1493f58fc5b54e5449e2a52d43e"
        ],
        "description": "Yubikey Edge",
        "protocolFamily": "u2f",
        "schema": 3,
        "upv": [
            {
                "major": 1,
                "minor": 1
            }
        ],
        "authenticationAlgorithms": [
            "secp256r1_ecdsa_sha256_raw"
        ],
        "publicKeyAlgAndEncodings": [
            "ecc_x962_raw"
        ],
        "attestationTypes": [
            "basic_full"
        ],
        "userVerificationDetails": [
            [
                {
                    "userVerificationMethod": "presence_internal"
                }
            ]
        ],
        "keyProtection": [
            "hardware",
            "secure_element",
            "remote_handle"
        ],
        "matcherProtection": [
            "on_chip"
        ],
        "cryptoStrength": 128,
        "attachmentHint": [
            "external",
            "wired"
        ],
        "attestationRootCertificates": [
            "MIIDHjCCAgagAwIBAgIEG0BT9zANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDEyNZdWJpY28gVTJGIFJvb3QgQ0EgU2VyaWFsIDQ1NzIwMDYzMTAgFw0xNDA4MDEwMDAwMDBaGA8yMDUwMDkwNDAwMDAwMFowLjEsMCoGA1UEAxMjWXViaWNvIFUyRiBSb290IENBIFNlcmlhbCA0NTcyMDA2MzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC/jwYuhBVlqaiYWEMsrWFisgJ+PtM91eSrpI4TK7U53mwCIawSDHy8vUmk5N2KAj9abvT9NP5SMS1hQi3usxoYGonXQgfO6ZXyUA9a+KAkqdFnBnlyugSeCOep8EdZFfsaRFtMjkwz5Gcz2Py4vIYvCdMHPtwaz0bVuzneueIEz6TnQjE63Rdt2zbwnebwTG5ZybeWSwbzy+BJ34ZHcUhPAY89yJQXuE0IzMZFcEBbPNRbWECRKgjq//qT9nmDOFVlSRCt2wiqPSzluwn+v+suQEBsUjTGMEd25tKXXTkNW21wIWbxeSyUoTXwLvGS6xlwQSgNpk2qXYwf8iXg7VWZAgMBAAGjQjBAMB0GA1UdDgQWBBQgIvz0bNGJhjgpToksyKpP9xv9oDAPBgNVHRMECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAjvjuOMDSa+JXFCLyBKsycXtBVZsJ4Ue3LbaEsPY4MYN/hIQ5ZM5p7EjfcnMG4CtYkNsfNHc0AhBLdq45rnT87q/6O3vUEtNMafbhU6kthX7Y+9XFN9NpmYxr+ekVY5xOxi8h9JDIgoMP4VB1uS0aunL1IGqrNooL9mmFnL2kLVVee6/VR6C5+KSTCMCWppMuJIZII2v9o4dkoZ8Y7QRjQlLfYzd3qGtKbw7xaF1UsG/5xUb/Btwb2X2g4InpiB/yt/3CpQXpiWX/K4mBvUKiGn05ZsqeY1gx4g0xLBqcU9psmyPzK+Vsgw2jeRQ5JlKDyqE0hebfC1tvFu0CCrJFcw=="
        ],
        "icon": "data:image/png;base64,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",
        "keyRestricted": false,
        "freshUserVerificationRequired": false
    },
    "createdAt": "2022-07-26T13:00:13.135Z",
    "updatedAt": "2022-07-26T13:00:13.135Z"
}
```

---

---
title: Allow MFA Bypass for User
description: This example uses the bypassMFA endpoint to define a period during which the specified user can bypass MFA:
component: pingone-api
page_id: pingone-api:mfa:users/users-1/allow_mfa_bypass
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/users-1/allow_mfa_bypass.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Allow MFA Bypass for User

##

```none
PUT {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA
```

This example uses the `bypassMFA` endpoint to define a period during which the specified user can bypass MFA:

`PUT {{apiPathTest}}/environments/{{envID}}/users/{{userID}}/bypassMFA`

The request takes a single parameter, `bypassMFAEnabledUntil`, which is used to set the date and time at which the bypass period is to end. The date format used in the example is the only date format that can be used.

Note that the response includes both a boolean field that indicates whether MFA can currently be bypassed and the end date for the bypass period.

> **Collapse: Request Model**
>
> | Property                | Type | Required |
> | ----------------------- | ---- | -------- |
> | `bypassMFAEnabledUntil` | Date | Required |
>
> Refer to the [User operations](/pingone/platform/v1/api/#user-operations) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
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
curl --location --globoff --request PUT '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Put);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""bypassMFAEnabledUntil"": ""2025-11-30T00:00:00.000Z""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA"
  method := "PUT"

  payload := strings.NewReader(`{
    "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
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
PUT /v1/environments/{{envID}}/users/{{userID}}/bypassMFA HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"bypassMFAEnabledUntil\": \"2025-11-30T00:00:00.000Z\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA",
  "method": "PUT",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA"

payload = json.dumps({
  "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA');
$request->setMethod(HTTP_Request2::METHOD_PUT);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Put.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "bypassMFAEnabledUntil": "2025-11-30T00:00:00.000Z"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"bypassMFAEnabledUntil\": \"2025-11-30T00:00:00.000Z\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")!,timeoutInterval: Double.infinity)
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
        "self": {
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/7e94b96e-0364-463b-a059-d97d1e4cb1d5/bypassMFA"
        },
        "user": {
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/7e94b96e-0364-463b-a059-d97d1e4cb1d5"
        }
    },
    "bypassMFAEnabledUntil": "2025-11-26T00:00:00.000Z",
    "canBypassMFA": true
}
```

---

---
title: Block MFA User Device
description: Use POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}} to block a specific MFA user device.
component: pingone-api
page_id: pingone-api:mfa:users/mfa-devices/block_mfa_user_device
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/mfa-devices/block_mfa_user_device.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Block MFA User Device

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}
```

Use `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}` to block a specific MFA user device.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.device.block+json

### Body

raw ( application/vnd.pingidentity.device.block+json )

```json
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
curl --location --globoff --request POST '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}' \
--header 'Content-Type: application/vnd.pingidentity.device.block+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data ''
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.device.block+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"";
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

  payload := strings.NewReader(``)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.device.block+json")
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
Content-Type: application/vnd.pingidentity.device.block+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.device.block+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.device.block+json")
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
    "Content-Type": "application/vnd.pingidentity.device.block+json",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.device.block+json',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}"

payload = ""
headers = {
  'Content-Type': 'application/vnd.pingidentity.device.block+json',
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
  'Content-Type' => 'application/vnd.pingidentity.device.block+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('');
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
request["Content-Type"] = "application/vnd.pingidentity.device.block+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/devices/{{deviceID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.device.block+json", forHTTPHeaderField: "Content-Type")
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

200 OK

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b30ac647-e33e-464f-a6ea-0275082d4c26/devices/6697f628-7712-4e71-b52b-920ba0635020"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b30ac647-e33e-464f-a6ea-0275082d4c26"
        }
    },
    "id": "6697f628-7712-4e71-b52b-920ba0635020",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "b30ac647-e33e-464f-a6ea-0275082d4c26"
    },
    "type": "SMS",
    "lock": {
        "status": "UNLOCKED"
    },
    "block": {
        "status": "BLOCKED",
        "blockedAt": "2022-11-20T14:25:07.044Z"
    },
    "status": "ACTIVE",
    "createdAt": "2022-09-22T13:07:15.115Z",
    "updatedAt": "2022-11-20T14:25:07.045Z",
    "phone": "+14135550150",
    "testMode": true
}
```

---

---
title: Cancel Device Authentication
description: This example shows how to cancel an authentication process that has begun. You can use this in situations where the user wants to authenticate from a different device. Note that this feature requires version 2.0 or higher of the PingOne MFA SDK.
component: pingone-api
page_id: pingone-api:mfa:mfa-authentication/mfa-device-authentications/cancel_authentication
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/mfa-authentication/mfa-device-authentications/cancel_authentication.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Cancel Device Authentication

##

```none
POST {{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}
```

This example shows how to cancel an authentication process that has begun. You can use this in situations where the user wants to authenticate from a different device. Note that this feature requires version 2.0 or higher of the PingOne MFA SDK.

The ID of the device authentication attempt is included in the URL: `{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}`

The value of the Content-Type header must be set to: `application/vnd.pingidentity.cancel.push.authentication+json`

The body consists of a single field, `reason`, which is set to CHANGE\_DEVICE.

> **Collapse: Request Model**
>
> | Property | Type   | Required |
> | -------- | ------ | -------- |
> | `reason` | String | Required |
>
> Refer to the [Device authentications](#device-authentications-data-model) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.cancel.push.authentication+json

### Body

raw ( application/vnd.pingidentity.cancel.push.authentication+json )

```json
{
    "reason": "CHANGE_DEVICE"
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
curl --location --globoff '{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}' \
--header 'Content-Type: application/vnd.pingidentity.cancel.push.authentication+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "reason": "CHANGE_DEVICE"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.cancel.push.authentication+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""reason"": ""CHANGE_DEVICE""" + "\n" +
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

  url := "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}"
  method := "POST"

  payload := strings.NewReader(`{
    "reason": "CHANGE_DEVICE"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.cancel.push.authentication+json")
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
POST /{{envID}}/deviceAuthentications/{{deviceAuthID}} HTTP/1.1
Host: {{authPath}}
Content-Type: application/vnd.pingidentity.cancel.push.authentication+json
Authorization: Bearer {{accessToken}}

{
    "reason": "CHANGE_DEVICE"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.cancel.push.authentication+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"reason\": \"CHANGE_DEVICE\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.cancel.push.authentication+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.cancel.push.authentication+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "reason": "CHANGE_DEVICE"
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
  'url': '{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.cancel.push.authentication+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "reason": "CHANGE_DEVICE"
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

url = "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}"

payload = json.dumps({
  "reason": "CHANGE_DEVICE"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.cancel.push.authentication+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.cancel.push.authentication+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "reason": "CHANGE_DEVICE"\n}');
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

url = URI("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.cancel.push.authentication+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "reason": "CHANGE_DEVICE"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"reason\": \"CHANGE_DEVICE\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.cancel.push.authentication+json", forHTTPHeaderField: "Content-Type")
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
    "_links": {
        "self": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthentications/004fd27a-c7e7-4e63-8644-0563e43dcd02"
        },
        "device.select": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthentications/004fd27a-c7e7-4e63-8644-0563e43dcd02"
        }
    },
    "_embedded": {
        "devices": [
            {
                "id": "3c325a86-283d-4fdf-bfda-239900d1ce8d",
                "type": "MOBILE",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "nickname": "AsafAuth1",
                "os": {
                    "version": "11",
                    "type": "ANDROID"
                },
                "apiVersion": "1.0",
                "locale": "en-IL",
                "model": {
                    "name": "IN2023",
                    "marketingName": "IN2023"
                },
                "application": {
                    "id": "edb09bb3-fc85-438b-a025-25a444e276e6",
                    "nativeName": "AsafAuth",
                    "version": "1.0.0",
                    "name": "AsafAuth",
                    "pushSandbox": false,
                    "passcodeRefreshDuration": {
                        "duration": 30,
                        "timeUnit": "SECONDS"
                    }
                },
                "pushEnabled": true,
                "manufacturer": "OnePlus",
                "sdkVersion": "1.2.0(5509)",
                "rooted": false,
                "lockEnabled": true,
                "notification": "enabled",
                "background": "unknown",
                "pushStatus": {
                    "status": "ENABLED"
                },
                "otpEnabled": false,
                "otpStatus": {
                    "status": "DISABLED",
                    "reason": "OTP_NOT_SUPPORTED_BY_SDK_VERSION"
                },
                "pushFails": [
                    1730814224932
                ]
            },
            {
                "id": "a8ccb1b3-0809-43c2-881b-f624a417e8aa",
                "type": "FIDO2",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "attributes": {
                    "previousDeviceType": "PLATFORM",
                    "isCrossPlatform": false
                },
                "rp": {
                    "id": "pingone.com",
                    "name": "PingOne"
                },
                "credentialId": "AejegVUIW1cbhyL0zIBsD44lZsb--PkKwK9ydrDMcL-rHx3_u9jGLyMSuMn7DAgDlB5pl1TSkmTSziTh8bpbgzo",
                "displayName": "fidoPolicy.deviceDisplayName01"
            },
            {
                "id": "259e5a50-46bb-4696-883b-ea14bb36bdf9",
                "type": "MOBILE",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "deviceIntegrityState": {
                    "compromised": "UNKNOWN",
                    "reason": "PLAY_MISSING_CONFIGURATION",
                    "timestamp": 1686050056879
                },
                "os": {
                    "version": "13",
                    "type": "ANDROID"
                },
                "apiVersion": "2.0",
                "locale": "en-IL",
                "model": {
                    "name": "IN2023",
                    "marketingName": "IN2023"
                },
                "application": {
                    "id": "15810c80-21a0-4e0e-9fc4-d95e951147c1",
                    "nativeName": "PingOneInternal",
                    "version": "1.10.0",
                    "name": "NativeAppForInternalApp",
                    "pushSandbox": false,
                    "passcodeRefreshDuration": {
                        "duration": 30,
                        "timeUnit": "SECONDS"
                    }
                },
                "pushEnabled": true,
                "manufacturer": "OnePlus",
                "sdkVersion": "1.10.0(9224)",
                "rooted": false,
                "lockEnabled": true,
                "notificationProvider": "FCM",
                "notification": "enabled",
                "background": "available",
                "allowPushNotification": true,
                "pushStatus": {
                    "status": "ENABLED"
                },
                "otpEnabled": false,
                "otpStatus": {
                    "status": "DISABLED",
                    "reason": "OTP_NOT_SUPPORTED"
                },
                "pushFails": []
            },
            {
                "id": "39edc3b1-8d69-4788-acbb-3cf2fe1c9897",
                "type": "FIDO2",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "attributes": {
                    "isCrossPlatform": false
                },
                "rp": {
                    "id": "pingone.com",
                    "name": "PingOne"
                },
                "credentialId": "tPb8yfpRxX7cbW3gEVzRKSRwKxXCq5tl0dOByCvbviY",
                "fidoRegistrationArtifacts": {
                    "attestationType": "NONE"
                },
                "backup": {
                    "backupEligibility": false,
                    "backupState": false
                },
                "displayName": "fidoPolicy.deviceDisplayName01"
            },
            {
                "id": "daba8c2b-5f01-42fa-91a5-ee91e58b0b26",
                "type": "EMAIL",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "email": "ad****@pingidentity.com"
            }
        ],
        "blockedDevices": []
    },
    "id": "004fd27a-c7e7-4e63-8644-0563e43dcd02",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "status": "DEVICE_SELECTION_REQUIRED",
    "policy": {
        "id": "6ad97c12-cfa6-0f90-1332-0274be07e414"
    },
    "selectedDevice": {
        "id": "3c325a86-283d-4fdf-bfda-239900d1ce8d"
    },
    "user": {
        "id": "8f8a6354-6153-4430-964e-e10d4e5deed3"
    },
    "bypassAllowed": false,
    "createdAt": "2024-11-05T13:43:27.272Z",
    "updatedAt": "2024-11-05T13:43:44.939Z",
    "aggregateFido2Devices": false,
    "userBypassEnabled": false
}
```

---

---
title: Check Assertion (FIDO Device)
description: The multi-factor authentication flow for a FIDO device checks the authenticator assertion response, which contains the signed challenge needed to complete the MFA flow. The MFA actions service validates the challenge.
component: pingone-api
page_id: pingone-api:mfa:mfa-authentication/mfa-device-authentications/check-assertion-device-authentication
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/mfa-authentication/mfa-device-authentications/check-assertion-device-authentication.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  device-authentication: Device authentication
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
---

# Check Assertion (FIDO Device)

##

```none
POST {{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}
```

The multi-factor authentication flow for a FIDO device checks the authenticator assertion response, which contains the signed challenge needed to complete the MFA flow. The MFA actions service validates the challenge.

The following sample shows the `POST /{{envID}}/deviceAuthentications/{{deviceAuthID}}` operation to validate the assertion used in the multi-factor authentication flow. This operation uses the `application/vnd.pingidentity.assertion.check+json` custom media type as the content type in the request header.

|   |                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `ASSERTION_REQUIRED` flow state includes the `publicKeyCredentialRequestOptions` response property that specifies the public key credential request options object generated for the selected device that is used to call the `navigator.credentials.get()` on the browser to generate the assertion. |

### Device authentication

A FIDO2 biometrics device flow uses functions from the Web Authentication API (webauthn API) to manage device authentication. The following sample JavaScript code will help you implement the webauthn API for browser-based operations.

For more information about the Web Authentication API, refer to [Web Authentication: An API for accessing Public Key Credentials](https://www.w3.org/TR/webauthn/).

Call the `navigator.credentials.get` method using the `publicKeyCredentialOptions` returned from the `assertion.check` action of the Flows service (refer to [Assertion Check](/pingone/auth/v1/api/#post-check-assertion)). As an example, refer to the `WebAuthnAuthentication` function in the following code sample:

```none
var authAbortController = window.PublicKeyCredential ? new AbortController() : null;
var authAbortSignal = window.PublicKeyCredential ? authAbortController.signal : null;

window.abortWebAuthnSignal = function abortWebAuthnSignal() {
    authAbortController.abort();
    authAbortController = new AbortController();
    authAbortSignal = authAbortController.signal;
}

window.IsWebAuthnSupported = function IsWebAuthnSupported() {
    if (!window.PublicKeyCredential) {
        console.log("Web Authentication API is not supported on this browser.");
        return false;
    }
    return true;
}

window.isWebAuthnPlatformAuthenticatorAvailable = function isWebAuthnPlatformAuthenticatorAvailable() {
    var timer;
    var p1 = new Promise(function(resolve) {
        timer = setTimeout(function() {
            resolve(false);
        }, 1000);
    });
    var p2 = new Promise(function(resolve) {
        if (IsWebAuthnSupported() && window.PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable) {
            resolve(
	            window.PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable().catch(function(err) {
                    console.log(err);
                    return false;
                }));
        }
        else {
            resolve(false);
        }
    });
    return Promise.race([p1, p2]).then(function (res) {
        clearTimeout(timer);
        console.log("isWebAuthnPlatformAuthenticatorAvailable - " +  res);
        return res;
    });
}

window.WebAuthnPlatformAuthentication = function WebAuthnPlatformAuthentication(publicKeyCredentialRequestOptions) {
    return new Promise(function(resolve, reject) {
        isWebAuthnPlatformAuthenticatorAvailable().then(function (result) {
            if (result) {
                resolve(Authenticate(publicKeyCredentialRequestOptions));
            }
            reject(Error("UnSupportedBrowserError"));
        });
    });
}

function Authenticate(publicKeyCredentialRequestOptions) {
    return new Promise(function(resolve, reject) {
        var options = JSON.parse(publicKeyCredentialRequestOptions);
        var publicKeyCredential = {};
        publicKeyCredential.challenge = new Uint8Array(options.challenge);
        if ('allowCredentials' in options) {
            publicKeyCredential.allowCredentials = credentialListConversion(options.allowCredentials);
        }
        if ('rpId' in options) {
            publicKeyCredential.rpId = options.rpId;
        }
        if ('timeout' in options) {
            publicKeyCredential.timeout = options.timeout;
        }
        if ('userVerification' in options) {
            publicKeyCredential.userVerification = options.userVerification;
        }
        console.log(publicKeyCredential);
        navigator.credentials.get({"publicKey": publicKeyCredential})
            .then(function (assertion) {
                // Send new credential info to server for verification and registration.
                console.log(assertion);
                var publicKeyCredential = {};
                if ('id' in assertion) {
                    publicKeyCredential.id = assertion.id;
                }
                if ('rawId' in assertion) {
                    publicKeyCredential.rawId = toBase64Str(assertion.rawId);
                }
                if ('type' in assertion) {
                    publicKeyCredential.type = assertion.type;
                }
                var response = {};
                response.clientDataJSON = toBase64Str(assertion.response.clientDataJSON);
                response.authenticatorData = toBase64Str(assertion.response.authenticatorData);
                response.signature = toBase64Str(assertion.response.signature);
                response.userHandle = toBase64Str(assertion.response.userHandle);
                publicKeyCredential.response = response;
                resolve(JSON.stringify(publicKeyCredential));
            }).catch(function (err) {
            // No acceptable authenticator or user refused consent. Handle appropriately.
            console.log(err);
            reject(Error(err.name));
        });
    });
}

function credentialListConversion(list) {
    var credList = [];
    for (var i=0; i < list.length; i++) {
        var cred = {
            type: list[i].type,
            id: new Uint8Array(list[i].id)
        };
        if (list[i].transports) {
            cred.transports = list[i].transports;
        }
        credList.push(cred);
    }
    return credList;
}

function toBase64Str(bin){
    return btoa(String.fromCharCode.apply(null, new Uint8Array(bin)));
}

const isWebAuthnSupported = () => {
  if (!window.PublicKeyCredential) {
    return false;
  }
  return true;
};

function getCompatibility() {
  return isWebAuthnPlatformAuthenticatorAvailable()
      .then((result) => {
        if (result) {
          return 'FULL';
        } else if (isWebAuthnSupported()) {
          return 'SECURITY_KEY_ONLY';
        } else {
          return 'NONE';
        }
      })
      .catch(() => {
        if (isWebAuthnSupported()) {
          return 'SECURITY_KEY_ONLY';
        } else {
          return 'NONE';
        }
      });
}
```

#### Prerequisites

* [Initialize device authentication](#post-initialize-device-authentication) to get a `{{deviceAuthID}}` for the endpoint. For more information, refer to [MFA Device Authentications](#mfa-device-authentications).

> **Collapse: Request Model**
>
> | Property        | Type   | Required |
> | --------------- | ------ | -------- |
> | `origin`        | String | Required |
> | `assertion`     | String | Required |
> | `compatibility` | String | Optional |
>
> Refer to the [Device authentications](#device-authentications-data-model) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.assertion.check+json

### Body

raw ( application/vnd.pingidentity.assertion.check+json )

```json
{
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility" : "FULL"
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
curl --location --globoff '{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}' \
--header 'Content-Type: application/vnd.pingidentity.assertion.check+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility" : "FULL"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.assertion.check+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""origin"": ""https://app.pingone.com""," + "\n" +
@"    ""assertion"": ""{{assertionFromBrowser}}""," + "\n" +
@"    ""compatibility"" : ""FULL""" + "\n" +
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

  url := "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}"
  method := "POST"

  payload := strings.NewReader(`{
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility" : "FULL"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.assertion.check+json")
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
POST /{{envID}}/deviceAuthentications/{{deviceAuthID}} HTTP/1.1
Host: {{authPath}}
Content-Type: application/vnd.pingidentity.assertion.check+json
Authorization: Bearer {{accessToken}}

{
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility" : "FULL"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.assertion.check+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"origin\": \"https://app.pingone.com\",\n    \"assertion\": \"{{assertionFromBrowser}}\",\n    \"compatibility\" : \"FULL\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.assertion.check+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.assertion.check+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility": "FULL"
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
  'url': '{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.assertion.check+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility": "FULL"
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

url = "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}"

payload = json.dumps({
  "origin": "https://app.pingone.com",
  "assertion": "{{assertionFromBrowser}}",
  "compatibility": "FULL"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.assertion.check+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.assertion.check+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "origin": "https://app.pingone.com",\n    "assertion": "{{assertionFromBrowser}}",\n    "compatibility" : "FULL"\n}');
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

url = URI("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.assertion.check+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "origin": "https://app.pingone.com",
  "assertion": "{{assertionFromBrowser}}",
  "compatibility": "FULL"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"origin\": \"https://app.pingone.com\",\n    \"assertion\": \"{{assertionFromBrowser}}\",\n    \"compatibility\" : \"FULL\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.assertion.check+json", forHTTPHeaderField: "Content-Type")
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

---

---
title: Check Assertion (PingID Desktop)
component: pingone-api
page_id: pingone-api:mfa:mfa-authentication/mfa-device-authentications/check-assertion-desktop
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/mfa-authentication/mfa-device-authentications/check-assertion-desktop.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Check Assertion (PingID Desktop)

##

 

```none
POST {{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}
```

Authentication with a PingID Desktop device involves a sequence of requests and responses, including interaction with the Desktop API.

This example shows the final step in this process, sending a POST request to the `deviceAuthentications` endpoint to check the assertion:

`POST {{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}`

`deviceAuthID` in the URL represents the ID that was included in the response from the PingOne server in [the request to initiate the device authentication](initiate-device-authentication-desktop.html).

The body includes the `assertion` field whose value shoud be the JWT that you received in response to the request sent to the PingID Desktop API, described in the description of [the request to initiate the device authentication](initiate-device-authentication-desktop.html).

The value of the `origin` field should be a subdomain of the domain that was specified as the Relying Party ID in the MFA policy or the domain that was specified with `rp.id` in the initial call to the PingOne server. The format used should be a complete URL, for example, `https://app.pingone.eu`.

The `Content-Type` header must be set to `application/vnd.pingidentity.assertion.check+json`.

> **Collapse: Request Model**
>
> | Property    | Type   | Required? |
> | ----------- | ------ | --------- |
> | `assertion` | String | Required  |
> | `origin`    | String | Required  |
>
> Refer to the [Device authentications data model](../mfa-device-authentications.html#device-authentications-data-model) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.assertion.check+json

### Body

raw ( application/vnd.pingidentity.assertion.check+json )

```json
{
    "origin":"https://app.pingone.eu",
    "assertion": "{{assertionValue}}"
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
curl --location --globoff '{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}' \
--header 'Content-Type: application/vnd.pingidentity.assertion.check+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "origin":"https://app.pingone.eu",
    "assertion": "{{assertionValue}}"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.assertion.check+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""origin"":""https://app.pingone.eu""," + "\n" +
@"    ""assertion"": ""{{assertionValue}}""" + "\n" +
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

  url := "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}"
  method := "POST"

  payload := strings.NewReader(`{
    "origin":"https://app.pingone.eu",
    "assertion": "{{assertionValue}}"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.assertion.check+json")
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
POST /{{envID}}/deviceAuthentications/{{deviceAuthID}} HTTP/1.1
Host: {{authPath}}
Content-Type: application/vnd.pingidentity.assertion.check+json
Authorization: Bearer {{accessToken}}

{
    "origin":"https://app.pingone.eu",
    "assertion": "{{assertionValue}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.assertion.check+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"origin\":\"https://app.pingone.eu\",\n    \"assertion\": \"{{assertionValue}}\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.assertion.check+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.assertion.check+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "origin": "https://app.pingone.eu",
    "assertion": "{{assertionValue}}"
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
  'url': '{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.assertion.check+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "origin": "https://app.pingone.eu",
    "assertion": "{{assertionValue}}"
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

url = "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}"

payload = json.dumps({
  "origin": "https://app.pingone.eu",
  "assertion": "{{assertionValue}}"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.assertion.check+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.assertion.check+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "origin":"https://app.pingone.eu",\n    "assertion": "{{assertionValue}}"\n}');
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

url = URI("{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.assertion.check+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "origin": "https://app.pingone.eu",
  "assertion": "{{assertionValue}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"origin\":\"https://app.pingone.eu\",\n    \"assertion\": \"{{assertionValue}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/deviceAuthentications/{{deviceAuthID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.assertion.check+json", forHTTPHeaderField: "Content-Type")
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
    "_links": {
        "self": {
            "href": "https://auth.pingone.eu/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthentications/0fa68b44-1e4d-430d-8c79-9e90553e228b"
        }
    },
    "_embedded": {
        "devices": [
            {
                "id": "001f74e8-b024-1df0-001f-74e8b0241df0",
                "type": "PINGID_DESKTOP_GEN2",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "nickname": "PingId Desktop new 2",
                "os": {
                    "version": "15.7.3",
                    "type": "MAC"
                },
                "model": {},
                "application": {
                    "id": "941d6390-ec3a-4bf4-858a-949c47ccd36e",
                    "nativeName": "PingID Desktop",
                    "version": "1.0.0",
                    "pushSandbox": false
                },
                "rp": {
                    "id": "pingone.eu",
                    "name": "pingone.eu"
                },
                "credentialId": "68d0d592-33ea-43da-a113-44996999a593",
                "unitId": "4d764d06-6aa5-4c15-ac8c-4df655cbf867"
            },
            {
                "id": "03ed6f11-c4fc-71d8-03ed-6f11c4fc71d8",
                "type": "EMAIL",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "nickname": "Email 1",
                "email": "sh****@pingidentity.com"
            },
            {
                "id": "0783541c-a172-8d40-0783-541ca1728d40",
                "type": "PINGID_DESKTOP_GEN2",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "nickname": "Desktop Mac 1",
                "os": {
                    "version": "15.7.3",
                    "type": "MAC"
                },
                "model": {},
                "application": {
                    "id": "941d6390-ec3a-4bf4-858a-949c47ccd36e",
                    "nativeName": "PingID Desktop",
                    "version": "1.0.0",
                    "pushSandbox": false
                },
                "rp": {
                    "id": "pingone.eu",
                    "name": "pingone.eu"
                },
                "credentialId": "eb003515-06bb-4fe0-b1a1-09d98550e55f",
                "unitId": "4d764d06-6aa5-4c15-ac8c-4df655cbf867"
            }
        ],
        "blockedDevices": []
    },
    "id": "0fa68b44-1e4d-430d-8c79-9e90553e228b",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "status": "COMPLETED",
    "policy": {
        "id": "f27e5149-92e2-011a-08da-d93f80db818b"
    },
    "selectedDevice": {
        "id": "0783541c-a172-8d40-0783-541ca1728d40"
    },
    "user": {
        "id": "d4543f69-e508-4cc6-bd16-b61baa4b3caf"
    },
    "pingIdDesktopCredentialRequestOptions": "{{credentialRequestOptionsValue}}",
    "bypassAllowed": false,
    "authenticators": [
        "desktop",
        "mfa",
        "user"
    ],
    "createdAt": "2026-02-17T14:44:09.650Z",
    "updatedAt": "2026-02-17T14:45:36.473Z",
    "userBypassEnabled": false
}
```

---

---
title: Check MFA Bypass Status for User
description: This example uses the bypassMFA endpoint to check whether the specified user can currently bypass MFA:
component: pingone-api
page_id: pingone-api:mfa:users/users-1/check_mfa_bypass_status
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/users-1/check_mfa_bypass_status.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Check MFA Bypass Status for User

##

```none
GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA
```

This example uses the `bypassMFA` endpoint to check whether the specified user can currently bypass MFA:

`GET {{apiPathTest}}/environments/{{envID}}/users/{{userID}}/bypassMFA`

Note that the response includes both a boolean field that indicates whether MFA can currently be bypassed and the end date for the bypass period.

If the user does not currently have bypass status, the response does not contain either of these fields.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data ''
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"";
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA"
  method := "GET"

  payload := strings.NewReader(``)

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
GET /v1/environments/{{envID}}/users/{{userID}}/bypassMFA HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")
  .method("GET", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA',
  'headers': {
    'Content-Type': 'application/json',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA"

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/bypassMFA")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
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
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/7e94b96e-0364-463b-a059-d97d1e4cb1d5/bypassMFA"
        },
        "user": {
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/7e94b96e-0364-463b-a059-d97d1e4cb1d5"
        }
    },
    "bypassMFAEnabledUntil": "2025-11-26T00:00:00.000Z",
    "canBypassMFA": true
}
```

---

---
title: Check Remember Me Device
description: This example uses a POST {{authPath}}/{{envID}}/deviceAuthentications request to check if the accessing device that the user is currently using is a remembered device.
component: pingone-api
page_id: pingone-api:mfa:users/remembered-devices/check_remembered_device
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/remembered-devices/check_remembered_device.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Check Remember Me Device

##

```none
POST {{authPath}}/{{envID}}/deviceAuthentications
```

This example uses a `POST {{authPath}}/{{envID}}/deviceAuthentications` request to check if the accessing device that the user is currently using is a remembered device.

For this request, the Content-Type header must be set to `application/vnd.pingidentity.payload.check+json`.

You must also include the Cookie header in the request, using the cookie that was returned in the `set-cookie` header when you created the remembered device.

The body of the request includes the ID of the MFA policy used so that it can be verified that the policy allows use of the "remember me" feature. However, it is recommended that you get the details of the MFA policy first so that you can check the remember me settings before sending the request to check if the device is a remembered device.

This example also includes the PingOne session ID in the body of the request. If you included the optional session ID parameter when creating the remembered device (`session.id`), you must also include the session ID (`deviceSession.id`) when you try checking if the device is remembered.

If the device is a remembered device, the the value of the `status` field in the response will be COMPLETED. If it is not a remembered device, the value of the field will be FAILED.

> **Collapse: Request Model**
>
> | Property           | Type   | Required |
> | ------------------ | ------ | -------- |
> | `deviceSession.id` | String | Optional |
> | `payload.type`     | String | Required |
> | `payload.value`    | String | Required |
> | `policy.id`        | String | Required |
> | `user.id`          | String | Required |
>
> Refer to the [Remembered Devices](#remembered-devices) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.payload.check+json

Cookie      {{cookieReturnedWhenCreatingRememberedDevice}}

### Body

raw ( application/vnd.pingidentity.payload.check+json )

```json
{
    "user": {
        "id": "{{userID}}"
    },
    "policy": {
        "id": "{{mfaPolicyID}}"
    },
    "payload": {
        "type": "BROWSER",
        "value": "{{signalsSdkOutput}}"
    },
    "deviceSession": {
        "id": "{{sessionID}}"
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
curl --location --globoff '{{authPath}}/{{envID}}/deviceAuthentications' \
--header 'Content-Type: application/vnd.pingidentity.payload.check+json' \
--header 'Cookie: {{cookieReturnedWhenCreatingRememberedDevice}}' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "user": {
        "id": "{{userID}}"
    },
    "policy": {
        "id": "{{mfaPolicyID}}"
    },
    "payload": {
        "type": "BROWSER",
        "value": "{{signalsSdkOutput}}"
    },
    "deviceSession": {
        "id": "{{sessionID}}"
    }
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/deviceAuthentications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.payload.check+json");
request.AddHeader("Cookie", "{{cookieReturnedWhenCreatingRememberedDevice}}");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""user"": {" + "\n" +
@"        ""id"": ""{{userID}}""" + "\n" +
@"    }, " + "\n" +
@"    ""policy"": {" + "\n" +
@"        ""id"": ""{{mfaPolicyID}}""" + "\n" +
@"    }," + "\n" +
@"    ""payload"": {" + "\n" +
@"        ""type"": ""BROWSER""," + "\n" +
@"        ""value"": ""{{signalsSdkOutput}}""" + "\n" +
@"    }," + "\n" +
@"    ""deviceSession"": {" + "\n" +
@"        ""id"": ""{{sessionID}}""" + "\n" +
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

  url := "{{authPath}}/{{envID}}/deviceAuthentications"
  method := "POST"

  payload := strings.NewReader(`{
    "user": {
        "id": "{{userID}}"
    },
    "policy": {
        "id": "{{mfaPolicyID}}"
    },
    "payload": {
        "type": "BROWSER",
        "value": "{{signalsSdkOutput}}"
    },
    "deviceSession": {
        "id": "{{sessionID}}"
    }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.payload.check+json")
  req.Header.Add("Cookie", "{{cookieReturnedWhenCreatingRememberedDevice}}")
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
POST /{{envID}}/deviceAuthentications HTTP/1.1
Host: {{authPath}}
Content-Type: application/vnd.pingidentity.payload.check+json
Cookie: {{cookieReturnedWhenCreatingRememberedDevice}}
Authorization: Bearer {{accessToken}}

{
    "user": {
        "id": "{{userID}}"
    },
    "policy": {
        "id": "{{mfaPolicyID}}"
    },
    "payload": {
        "type": "BROWSER",
        "value": "{{signalsSdkOutput}}"
    },
    "deviceSession": {
        "id": "{{sessionID}}"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.payload.check+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"user\": {\n        \"id\": \"{{userID}}\"\n    }, \n    \"policy\": {\n        \"id\": \"{{mfaPolicyID}}\"\n    },\n    \"payload\": {\n        \"type\": \"BROWSER\",\n        \"value\": \"{{signalsSdkOutput}}\"\n    },\n    \"deviceSession\": {\n        \"id\": \"{{sessionID}}\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/deviceAuthentications")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.payload.check+json")
  .addHeader("Cookie", "{{cookieReturnedWhenCreatingRememberedDevice}}")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/deviceAuthentications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.payload.check+json",
    "Cookie": "{{cookieReturnedWhenCreatingRememberedDevice}}",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "user": {
      "id": "{{userID}}"
    },
    "policy": {
      "id": "{{mfaPolicyID}}"
    },
    "payload": {
      "type": "BROWSER",
      "value": "{{signalsSdkOutput}}"
    },
    "deviceSession": {
      "id": "{{sessionID}}"
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
  'url': '{{authPath}}/{{envID}}/deviceAuthentications',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.payload.check+json',
    'Cookie': '{{cookieReturnedWhenCreatingRememberedDevice}}',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "user": {
      "id": "{{userID}}"
    },
    "policy": {
      "id": "{{mfaPolicyID}}"
    },
    "payload": {
      "type": "BROWSER",
      "value": "{{signalsSdkOutput}}"
    },
    "deviceSession": {
      "id": "{{sessionID}}"
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

url = "{{authPath}}/{{envID}}/deviceAuthentications"

payload = json.dumps({
  "user": {
    "id": "{{userID}}"
  },
  "policy": {
    "id": "{{mfaPolicyID}}"
  },
  "payload": {
    "type": "BROWSER",
    "value": "{{signalsSdkOutput}}"
  },
  "deviceSession": {
    "id": "{{sessionID}}"
  }
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.payload.check+json',
  'Cookie': '{{cookieReturnedWhenCreatingRememberedDevice}}',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/deviceAuthentications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.payload.check+json',
  'Cookie' => '{{cookieReturnedWhenCreatingRememberedDevice}}',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "user": {\n        "id": "{{userID}}"\n    }, \n    "policy": {\n        "id": "{{mfaPolicyID}}"\n    },\n    "payload": {\n        "type": "BROWSER",\n        "value": "{{signalsSdkOutput}}"\n    },\n    "deviceSession": {\n        "id": "{{sessionID}}"\n    }\n}');
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

url = URI("{{authPath}}/{{envID}}/deviceAuthentications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.payload.check+json"
request["Cookie"] = "{{cookieReturnedWhenCreatingRememberedDevice}}"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "user": {
    "id": "{{userID}}"
  },
  "policy": {
    "id": "{{mfaPolicyID}}"
  },
  "payload": {
    "type": "BROWSER",
    "value": "{{signalsSdkOutput}}"
  },
  "deviceSession": {
    "id": "{{sessionID}}"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"user\": {\n        \"id\": \"{{userID}}\"\n    }, \n    \"policy\": {\n        \"id\": \"{{mfaPolicyID}}\"\n    },\n    \"payload\": {\n        \"type\": \"BROWSER\",\n        \"value\": \"{{signalsSdkOutput}}\"\n    },\n    \"deviceSession\": {\n        \"id\": \"{{sessionID}}\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/deviceAuthentications")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.payload.check+json", forHTTPHeaderField: "Content-Type")
request.addValue("{{cookieReturnedWhenCreatingRememberedDevice}}", forHTTPHeaderField: "Cookie")
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
    "_links": {
        "self": {
            "href": "https://auth.pingone.eu/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthentications/0f44908a-65e9-4652-93ad-1bc93a220995"
        }
    },
    "_embedded": {
        "devices": [
            {
                "id": "e112c96d-d165-45c5-8061-87ff268fd520",
                "type": "SMS",
                "status": "ACTIVE",
                "usableStatus": {
                    "status": "ENABLED"
                },
                "phone": "*******44"
            },
            {
                "id": "a837a752-714f-4fcb-9963-902c9e31ce67",
                "type": "BROWSER",
                "status": "ACTIVE",
                "block": {
                    "status": "UNBLOCKED"
                },
                "lock": {
                    "status": "UNLOCKED",
                    "reason": "OTP"
                },
                "usableStatus": {
                    "status": "ENABLED"
                },
                "nickname": "Chrome(133.0.0.0)",
                "name": "Chrome",
                "version": "133.0.0.0",
                "operatingSystem": {
                    "name": "Mac OS",
                    "version": "10.15.7"
                },
                "session": {
                    "id": "e7992c24-0df6-4c71-ad38-6950f4829290"
                },
                "lastRememberedAt": 1739880564347
            }
        ],
        "blockedDevices": []
    },
    "id": "0f44908a-65e9-4652-93ad-1bc93a220995",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "status": "COMPLETED",
    "policy": {
        "id": "f0b2b3b2-72d3-4573-84d9-52a85479445c"
    },
    "deviceSession": {
        "id": "e7992c24-0df6-4c71-ad38-6950f4829290"
    },
    "selectedDevice": {
        "id": "a837a752-714f-4fcb-9963-902c9e31ce67"
    },
    "user": {
        "id": "b30ac647-e33e-464f-a6ea-0275082d4c26"
    },
    "bypassAllowed": false,
    "authenticators": [
        "rm"
    ],
    "createdAt": "2025-02-18T12:18:26.976Z",
    "updatedAt": "2025-02-18T12:18:27.208Z",
    "payload": {
        "value": "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.eDE=",
        "type": "BROWSER"
    },
    "userBypassEnabled": false
}
```

---

---
title: Check status of OATH token creation job
description: "This example uses the oathJobs endpoint to check the status of an OATH token creation job by including the job ID in the URL: {{apiPathTest}}/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}. The same URL structure is used when checking the status of an OATH token revoking job."
component: pingone-api
page_id: pingone-api:mfa:oath-tokens/check_status_of_oath_token_creation_job
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/oath-tokens/check_status_of_oath_token_creation_job.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Check status of OATH token creation job

##

```none
GET {{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}
```

This example uses the `oathJobs` endpoint to check the status of an OATH token creation job by including the job ID in the URL: `{{apiPathTest}}/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}`. The same URL structure is used when checking the status of an OATH token revoking job.

The ID to include in the URL is the value that was returned in the `id` field of the response when the job was submitted.

A status of `DONE` in the response indicates that the job has been completed.

If the job status is `FAILED`, the `reason` field in the response provides the reason for the failure.

The `result.created` field indicates how many tokens were created.

If the list of tokens submitted included tokens with serial numbers that already exist in the environment, the `result.duplicates` object contains information about the duplicates token.

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}"
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
GET /v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/jobs/61c96614-ff99-47cd-aae9-ee7959eea0cf"
        },
        "environment": {
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "61c96614-ff99-47cd-aae9-ee7959eea0cf",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "type": "CREATE_OATH_TOKENS",
    "async": true,
    "status": "DONE",
    "result": {
        "created": 6,
        "duplicates": [
            {
                "serialNumber": "2308734700412",
                "maskedSecret": "6E******"
            },
            {
                "serialNumber": "2300004700388",
                "maskedSecret": "6E******"
            }
        ]
    }
}
```

---

---
title: Check status of OATH token revoke job
description: "This example uses the oathJobs endpoint to check the status of an OATH token revoke job by including the job ID in the URL: {{apiPathTest}}/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}."
component: pingone-api
page_id: pingone-api:mfa:oath-tokens/check_status_of_oath_token_revoke_job
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/oath-tokens/check_status_of_oath_token_revoke_job.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Check status of OATH token revoke job

##

```none
GET {{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}
```

This example uses the `oathJobs` endpoint to check the status of an OATH token revoke job by including the job ID in the URL: `{{apiPathTest}}/environments/{{envID}}/oathJobs/{{oathTokenCreationJobID}}`.

The ID to include in the URL is the value that was returned in the `id` field of the response when the job was submitted.

A status of `DONE` in the response indicates that the job has been completed.

If the job status is `FAILED`, the `reason` field in the response provides the reason for the failure.

The `result.revoked` field indicates how many tokens were revoked.

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}"
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
GET /v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/oathJobs/{{oathTokenRevokeJobID}}")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/jobs/f445e588-1963-47de-b5e4-ce3cf0d58f11"
        },
        "environment": {
            "href": "https://api.test-one-pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "f445e588-1963-47de-b5e4-ce3cf0d58f11",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "type": "REVOKE_OATH_TOKENS",
    "async": true,
    "status": "DONE",
    "result": {
        "revoked": 5
    }
}
```

---

---
title: Create Authentication Code
description: The POST /{{envID}}/authenticationCodes operation creates an authentication code for use in an MFA device authentication flow. The request body requires an application.id property value to associate an application with the MFA flow. The request also supports optional clientContext, lifeTime, and userApproval properties to provide relevant information to the mobile application. For example, the following message can be provided through the clientContext property:
component: pingone-api
page_id: pingone-api:mfa:mfa-authentication/mfa-authentication-code/create-authentication-code
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/mfa-authentication/mfa-authentication-code/create-authentication-code.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Authentication Code

##

```none
POST {{authPath}}/{{envID}}/authenticationCodes
```

The `POST /{{envID}}/authenticationCodes` operation creates an authentication code for use in an MFA device authentication flow. The request body requires an `application.id` property value to associate an application with the MFA flow. The request also supports optional `clientContext`, `lifeTime`, and `userApproval` properties to provide relevant information to the mobile application. For example, the following message can be provided through the `clientContext` property:

```none
"clientContext": {
        "header" : "Authentication process",
        "body": "Do you want to approve this transaction?"
    }
```

The response returns the code and several other properties, including a `status` property to specify the status of the code. When the resouce is first created, the code's status is `UNCLAIMED`.

> **Collapse: Request Model**
>
> | Property            | Type    | Required |
> | ------------------- | ------- | -------- |
> | `application.id`    | String  | Required |
> | `clientContext`     | String  | Optional |
> | `lifeTime.duration` | Integer | Optional |
> | `lifeTime.timeUnit` | String  | Optional |
> | `userApproval`      | String  | Optional |
>
> Refer to the [Device authentications request](#mfa-authentication-code) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "application": {
        "id": "{{appID}}"
    },
    "clientContext": {
        "header": "Authentication process",
        "body": "Do you want to approve this transaction?"
    },
    "lifeTime": {
        "duration": 2,
        "timeUnit": "MINUTES"
    },
    "userApproval": "NOT_REQUIRED"
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
curl --location --globoff '{{authPath}}/{{envID}}/authenticationCodes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "application": {
        "id": "{{appID}}"
    },
    "clientContext": {
        "header": "Authentication process",
        "body": "Do you want to approve this transaction?"
    },
    "lifeTime": {
        "duration": 2,
        "timeUnit": "MINUTES"
    },
    "userApproval": "NOT_REQUIRED"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/authenticationCodes")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""application"": {" + "\n" +
@"        ""id"": ""{{appID}}""" + "\n" +
@"    }," + "\n" +
@"    ""clientContext"": {" + "\n" +
@"        ""header"": ""Authentication process""," + "\n" +
@"        ""body"": ""Do you want to approve this transaction?""" + "\n" +
@"    }," + "\n" +
@"    ""lifeTime"": {" + "\n" +
@"        ""duration"": 2," + "\n" +
@"        ""timeUnit"": ""MINUTES""" + "\n" +
@"    }," + "\n" +
@"    ""userApproval"": ""NOT_REQUIRED""" + "\n" +
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

  url := "{{authPath}}/{{envID}}/authenticationCodes"
  method := "POST"

  payload := strings.NewReader(`{
    "application": {
        "id": "{{appID}}"
    },
    "clientContext": {
        "header": "Authentication process",
        "body": "Do you want to approve this transaction?"
    },
    "lifeTime": {
        "duration": 2,
        "timeUnit": "MINUTES"
    },
    "userApproval": "NOT_REQUIRED"
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
POST /{{envID}}/authenticationCodes HTTP/1.1
Host: {{authPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "application": {
        "id": "{{appID}}"
    },
    "clientContext": {
        "header": "Authentication process",
        "body": "Do you want to approve this transaction?"
    },
    "lifeTime": {
        "duration": 2,
        "timeUnit": "MINUTES"
    },
    "userApproval": "NOT_REQUIRED"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"application\": {\n        \"id\": \"{{appID}}\"\n    },\n    \"clientContext\": {\n        \"header\": \"Authentication process\",\n        \"body\": \"Do you want to approve this transaction?\"\n    },\n    \"lifeTime\": {\n        \"duration\": 2,\n        \"timeUnit\": \"MINUTES\"\n    },\n    \"userApproval\": \"NOT_REQUIRED\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/authenticationCodes")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/authenticationCodes",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "application": {
      "id": "{{appID}}"
    },
    "clientContext": {
      "header": "Authentication process",
      "body": "Do you want to approve this transaction?"
    },
    "lifeTime": {
      "duration": 2,
      "timeUnit": "MINUTES"
    },
    "userApproval": "NOT_REQUIRED"
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
  'url': '{{authPath}}/{{envID}}/authenticationCodes',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "application": {
      "id": "{{appID}}"
    },
    "clientContext": {
      "header": "Authentication process",
      "body": "Do you want to approve this transaction?"
    },
    "lifeTime": {
      "duration": 2,
      "timeUnit": "MINUTES"
    },
    "userApproval": "NOT_REQUIRED"
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

url = "{{authPath}}/{{envID}}/authenticationCodes"

payload = json.dumps({
  "application": {
    "id": "{{appID}}"
  },
  "clientContext": {
    "header": "Authentication process",
    "body": "Do you want to approve this transaction?"
  },
  "lifeTime": {
    "duration": 2,
    "timeUnit": "MINUTES"
  },
  "userApproval": "NOT_REQUIRED"
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
$request->setUrl('{{authPath}}/{{envID}}/authenticationCodes');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "application": {\n        "id": "{{appID}}"\n    },\n    "clientContext": {\n        "header": "Authentication process",\n        "body": "Do you want to approve this transaction?"\n    },\n    "lifeTime": {\n        "duration": 2,\n        "timeUnit": "MINUTES"\n    },\n    "userApproval": "NOT_REQUIRED"\n}');
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

url = URI("{{authPath}}/{{envID}}/authenticationCodes")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "application": {
    "id": "{{appID}}"
  },
  "clientContext": {
    "header": "Authentication process",
    "body": "Do you want to approve this transaction?"
  },
  "lifeTime": {
    "duration": 2,
    "timeUnit": "MINUTES"
  },
  "userApproval": "NOT_REQUIRED"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"application\": {\n        \"id\": \"{{appID}}\"\n    },\n    \"clientContext\": {\n        \"header\": \"Authentication process\",\n        \"body\": \"Do you want to approve this transaction?\"\n    },\n    \"lifeTime\": {\n        \"duration\": 2,\n        \"timeUnit\": \"MINUTES\"\n    },\n    \"userApproval\": \"NOT_REQUIRED\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/authenticationCodes")!,timeoutInterval: Double.infinity)
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
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/authenticationCodes/39743070-2f4c-4b26-a4ab-12287d0187dc"
        }
    },
    "id": "39743070-2f4c-4b26-a4ab-12287d0187dc",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "code": "B4D04NQR",
    "uri": "pingonesdk?authentication_code=B4D04NQR",
    "application": {
        "id": "7d8797b7-a097-46a9-841f-88f531d1d99b"
    },
    "clientContext": {
        "header": "Authentication process",
        "body": "Do you want to approve this transaction?"
    },
    "lifeTime": {
        "duration": 2,
        "timeUnit": "MINUTES"
    },
    "userApproval": "NOT_REQUIRED",
    "status": "UNCLAIMED",
    "expiresAt": "2022-02-22T21:03:08.132Z",
    "updatedAt": "2022-02-22T21:01:08.118Z",
    "createdAt": "2022-02-22T21:01:08.118Z"
}
```

---

---
title: Create Device Authentication Policy
description: The POST {{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies operation creates a new device authentication policy for the environment.
component: pingone-api
page_id: pingone-api:mfa:device-authentication-policy/create-device-authentication-policy
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/device-authentication-policy/create-device-authentication-policy.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
  example-response-2: Example Response
---

# Create Device Authentication Policy

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies
```

The `POST {{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies` operation creates a new device authentication policy for the environment.

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | To create new MFA policies, you must have a license that includes MFA. |

### Prerequisites

* Refer to [Device Authentication Policies](../device-authentication-policy.html) for important overview information.

* Use [Read All Applications](../../platform/applications/applications-1/read-all-applications.html) to retrieve a list of all applications associated with the specified environment and select the specific `appID` for the body. For more information, refer to [Application Management](../../platform/applications/application-management.html), specifically [Application Operations](../../platform/applications/applications-1.html).

* Use [Read All FIDO Policies](../fido-policies/read_all_fido_policies.html) to retrieve all the FIDO policies for an environment and select the specific `fidoPolicyID` for the body. For more information, refer to [FIDO Policies](../fido-policies.html).

> **Collapse: Request Model**
>
> | Property                    | Type    | Required |
> | --------------------------- | ------- | -------- |
> | `blockDisabledUsers`        | Boolean | Optional |
> | `blockUsersWithDisabledMfa` | Boolean | Optional |
> | `default`                   | Boolean | Required |
> | `email`                     | Object  | Required |
> | `fido2`                     | Object  | Required |
> | `mobile`                    | Object  | Required |
> | `name`                      | String  | Required |
> | `newDeviceNotification`     | String  | Optional |
> | `sms`                       | Object  | Required |
> | `totp`                      | Object  | Required |
> | `voice`                     | Object  | Required |
> | `whatsApp`                  | Object  | Optional |
>
> Refer to the [Device authentication policy](../device-authentication-policy.html#device-authentication-policy-data-model) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "MFA policy created on {{$timestamp}}",
    "blockDisabledUsers": true,
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true,
                    "numberMatching": {
                        "enabled":true
                    }

                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "passcodeGracePeriod" : 3,
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "whatsApp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 5,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "pairingDisabled":true,
        "promptForNicknameOnPairing":true
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "notificationsPolicy":{
        "id":"{{notificationPolicyID}}"
    },
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "failure":{
            "count":"4",
            "coolDown":{
                "timeUnit":"SECONDS",
                "duration":150
            }
        },
        "promptForNicknameOnPairing": true
    },
    "blockUsersWithDisabledMfa": false,
    "default": false
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "MFA policy created on {{$timestamp}}",
    "blockDisabledUsers": true,
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true,
                    "numberMatching": {
                        "enabled":true
                    }

                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "passcodeGracePeriod" : 3,
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "whatsApp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 5,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "pairingDisabled":true,
        "promptForNicknameOnPairing":true
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "notificationsPolicy":{
        "id":"{{notificationPolicyID}}"
    },
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "failure":{
            "count":"4",
            "coolDown":{
                "timeUnit":"SECONDS",
                "duration":150
            }
        },
        "promptForNicknameOnPairing": true
    },
    "blockUsersWithDisabledMfa": false,
    "default": false
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""MFA policy created on {{$timestamp}}""," + "\n" +
@"    ""blockDisabledUsers"": true," + "\n" +
@"    ""sms"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 0," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 30," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""otpLength"":6" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""email"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 0," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 30," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""otpLength"": 8" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""mobile"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 2," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""window"": {" + "\n" +
@"                ""stepSize"": {" + "\n" +
@"                    ""duration"": 30," + "\n" +
@"                    ""timeUnit"": ""SECONDS""" + "\n" +
@"                }" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""applications"": [" + "\n" +
@"            {" + "\n" +
@"                ""id"": ""{{appID}}""," + "\n" +
@"                ""push"": {" + "\n" +
@"                    ""enabled"": true," + "\n" +
@"                    ""numberMatching"": {" + "\n" +
@"                        ""enabled"":true" + "\n" +
@"                    }" + "\n" +
@"" + "\n" +
@"                }," + "\n" +
@"                ""otp"": {" + "\n" +
@"                    ""enabled"": true" + "\n" +
@"                }," + "\n" +
@"                ""pushTimeout"": {" + "\n" +
@"                    ""duration"": 120," + "\n" +
@"                    ""timeUnit"": ""SECONDS""" + "\n" +
@"                }," + "\n" +
@"                ""pushLimit"": {" + "\n" +
@"                    ""count"": 4," + "\n" +
@"                    ""timePeriod"": {" + "\n" +
@"                        ""duration"": 20," + "\n" +
@"                        ""timeUnit"": ""MINUTES""" + "\n" +
@"                    }," + "\n" +
@"                    ""lockDuration"": {" + "\n" +
@"                        ""duration"": 30," + "\n" +
@"                        ""timeUnit"": ""MINUTES""" + "\n" +
@"                    }" + "\n" +
@"                }," + "\n" +
@"                ""pairingKeyLifetime"": {" + "\n" +
@"                    ""duration"": 24," + "\n" +
@"                    ""timeUnit"": ""HOURS""" + "\n" +
@"                }," + "\n" +
@"                ""deviceAuthorization"": {" + "\n" +
@"                    ""enabled"": true," + "\n" +
@"                    ""extraVerification"": ""permissive""" + "\n" +
@"                }," + "\n" +
@"                ""autoEnrollment"": {" + "\n" +
@"                    ""enabled"": true" + "\n" +
@"                }," + "\n" +
@"                ""integrityDetection"": ""permissive""" + "\n" +
@"            }" + "\n" +
@"        ]" + "\n" +
@"    }," + "\n" +
@"    ""totp"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 2," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""passcodeGracePeriod"" : 3," + "\n" +
@"        ""uriParameters"": {" + "\n" +
@"            ""issuer"": ""Corporate spreadsheet app""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""voice"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 0," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 30," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""otpLength"": 6" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""whatsApp"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 5," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 15," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""pairingDisabled"":true," + "\n" +
@"        ""promptForNicknameOnPairing"":true" + "\n" +
@"    }," + "\n" +
@"    ""newDeviceNotification"": ""SMS_THEN_EMAIL""," + "\n" +
@"    ""notificationsPolicy"":{" + "\n" +
@"        ""id"":""{{notificationPolicyID}}""" + "\n" +
@"    }," + "\n" +
@"    ""forSignOnPolicy"": false," + "\n" +
@"    ""fido2"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""failure"":{" + "\n" +
@"            ""count"":""4""," + "\n" +
@"            ""coolDown"":{" + "\n" +
@"                ""timeUnit"":""SECONDS""," + "\n" +
@"                ""duration"":150" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""promptForNicknameOnPairing"": true" + "\n" +
@"    }," + "\n" +
@"    ""blockUsersWithDisabledMfa"": false," + "\n" +
@"    ""default"": false" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "MFA policy created on {{$timestamp}}",
    "blockDisabledUsers": true,
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true,
                    "numberMatching": {
                        "enabled":true
                    }

                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "passcodeGracePeriod" : 3,
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "whatsApp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 5,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "pairingDisabled":true,
        "promptForNicknameOnPairing":true
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "notificationsPolicy":{
        "id":"{{notificationPolicyID}}"
    },
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "failure":{
            "count":"4",
            "coolDown":{
                "timeUnit":"SECONDS",
                "duration":150
            }
        },
        "promptForNicknameOnPairing": true
    },
    "blockUsersWithDisabledMfa": false,
    "default": false
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
POST /v1/environments/{{envID}}/deviceAuthenticationPolicies HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "MFA policy created on {{$timestamp}}",
    "blockDisabledUsers": true,
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true,
                    "numberMatching": {
                        "enabled":true
                    }

                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "passcodeGracePeriod" : 3,
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "whatsApp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 5,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "pairingDisabled":true,
        "promptForNicknameOnPairing":true
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "notificationsPolicy":{
        "id":"{{notificationPolicyID}}"
    },
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "failure":{
            "count":"4",
            "coolDown":{
                "timeUnit":"SECONDS",
                "duration":150
            }
        },
        "promptForNicknameOnPairing": true
    },
    "blockUsersWithDisabledMfa": false,
    "default": false
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"MFA policy created on {{$timestamp}}\",\n    \"blockDisabledUsers\": true,\n    \"sms\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\":6\n        }\n    },\n    \"email\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 8\n        }\n    },\n    \"mobile\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"window\": {\n                \"stepSize\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            }\n        },\n        \"applications\": [\n            {\n                \"id\": \"{{appID}}\",\n                \"push\": {\n                    \"enabled\": true,\n                    \"numberMatching\": {\n                        \"enabled\":true\n                    }\n\n                },\n                \"otp\": {\n                    \"enabled\": true\n                },\n                \"pushTimeout\": {\n                    \"duration\": 120,\n                    \"timeUnit\": \"SECONDS\"\n                },\n                \"pushLimit\": {\n                    \"count\": 4,\n                    \"timePeriod\": {\n                        \"duration\": 20,\n                        \"timeUnit\": \"MINUTES\"\n                    },\n                    \"lockDuration\": {\n                        \"duration\": 30,\n                        \"timeUnit\": \"MINUTES\"\n                    }\n                },\n                \"pairingKeyLifetime\": {\n                    \"duration\": 24,\n                    \"timeUnit\": \"HOURS\"\n                },\n                \"deviceAuthorization\": {\n                    \"enabled\": true,\n                    \"extraVerification\": \"permissive\"\n                },\n                \"autoEnrollment\": {\n                    \"enabled\": true\n                },\n                \"integrityDetection\": \"permissive\"\n            }\n        ]\n    },\n    \"totp\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            }\n        },\n        \"passcodeGracePeriod\" : 3,\n        \"uriParameters\": {\n            \"issuer\": \"Corporate spreadsheet app\"\n        }\n    },\n    \"voice\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 6\n        }\n    },\n    \"whatsApp\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 5,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 15,\n                \"timeUnit\": \"MINUTES\"\n            }\n        },\n        \"pairingDisabled\":true,\n        \"promptForNicknameOnPairing\":true\n    },\n    \"newDeviceNotification\": \"SMS_THEN_EMAIL\",\n    \"notificationsPolicy\":{\n        \"id\":\"{{notificationPolicyID}}\"\n    },\n    \"forSignOnPolicy\": false,\n    \"fido2\": {\n        \"enabled\": true,\n        \"failure\":{\n            \"count\":\"4\",\n            \"coolDown\":{\n                \"timeUnit\":\"SECONDS\",\n                \"duration\":150\n            }\n        },\n        \"promptForNicknameOnPairing\": true\n    },\n    \"blockUsersWithDisabledMfa\": false,\n    \"default\": false\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "MFA policy created on {{$timestamp}}",
    "blockDisabledUsers": true,
    "sms": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "email": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 8
      }
    },
    "mobile": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        },
        "window": {
          "stepSize": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        }
      },
      "applications": [
        {
          "id": "{{appID}}",
          "push": {
            "enabled": true,
            "numberMatching": {
              "enabled": true
            }
          },
          "otp": {
            "enabled": true
          },
          "pushTimeout": {
            "duration": 120,
            "timeUnit": "SECONDS"
          },
          "pushLimit": {
            "count": 4,
            "timePeriod": {
              "duration": 20,
              "timeUnit": "MINUTES"
            },
            "lockDuration": {
              "duration": 30,
              "timeUnit": "MINUTES"
            }
          },
          "pairingKeyLifetime": {
            "duration": 24,
            "timeUnit": "HOURS"
          },
          "deviceAuthorization": {
            "enabled": true,
            "extraVerification": "permissive"
          },
          "autoEnrollment": {
            "enabled": true
          },
          "integrityDetection": "permissive"
        }
      ]
    },
    "totp": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        }
      },
      "passcodeGracePeriod": 3,
      "uriParameters": {
        "issuer": "Corporate spreadsheet app"
      }
    },
    "voice": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "whatsApp": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 5,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 15,
          "timeUnit": "MINUTES"
        }
      },
      "pairingDisabled": true,
      "promptForNicknameOnPairing": true
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "notificationsPolicy": {
      "id": "{{notificationPolicyID}}"
    },
    "forSignOnPolicy": false,
    "fido2": {
      "enabled": true,
      "failure": {
        "count": "4",
        "coolDown": {
          "timeUnit": "SECONDS",
          "duration": 150
        }
      },
      "promptForNicknameOnPairing": true
    },
    "blockUsersWithDisabledMfa": false,
    "default": false
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "MFA policy created on {{$timestamp}}",
    "blockDisabledUsers": true,
    "sms": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "email": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 8
      }
    },
    "mobile": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        },
        "window": {
          "stepSize": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        }
      },
      "applications": [
        {
          "id": "{{appID}}",
          "push": {
            "enabled": true,
            "numberMatching": {
              "enabled": true
            }
          },
          "otp": {
            "enabled": true
          },
          "pushTimeout": {
            "duration": 120,
            "timeUnit": "SECONDS"
          },
          "pushLimit": {
            "count": 4,
            "timePeriod": {
              "duration": 20,
              "timeUnit": "MINUTES"
            },
            "lockDuration": {
              "duration": 30,
              "timeUnit": "MINUTES"
            }
          },
          "pairingKeyLifetime": {
            "duration": 24,
            "timeUnit": "HOURS"
          },
          "deviceAuthorization": {
            "enabled": true,
            "extraVerification": "permissive"
          },
          "autoEnrollment": {
            "enabled": true
          },
          "integrityDetection": "permissive"
        }
      ]
    },
    "totp": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        }
      },
      "passcodeGracePeriod": 3,
      "uriParameters": {
        "issuer": "Corporate spreadsheet app"
      }
    },
    "voice": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "whatsApp": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 5,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 15,
          "timeUnit": "MINUTES"
        }
      },
      "pairingDisabled": true,
      "promptForNicknameOnPairing": true
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "notificationsPolicy": {
      "id": "{{notificationPolicyID}}"
    },
    "forSignOnPolicy": false,
    "fido2": {
      "enabled": true,
      "failure": {
        "count": "4",
        "coolDown": {
          "timeUnit": "SECONDS",
          "duration": 150
        }
      },
      "promptForNicknameOnPairing": true
    },
    "blockUsersWithDisabledMfa": false,
    "default": false
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

url = "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies"

payload = json.dumps({
  "name": "MFA policy created on {{$timestamp}}",
  "blockDisabledUsers": True,
  "sms": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "email": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 8
    }
  },
  "mobile": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      },
      "window": {
        "stepSize": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      }
    },
    "applications": [
      {
        "id": "{{appID}}",
        "push": {
          "enabled": True,
          "numberMatching": {
            "enabled": True
          }
        },
        "otp": {
          "enabled": True
        },
        "pushTimeout": {
          "duration": 120,
          "timeUnit": "SECONDS"
        },
        "pushLimit": {
          "count": 4,
          "timePeriod": {
            "duration": 20,
            "timeUnit": "MINUTES"
          },
          "lockDuration": {
            "duration": 30,
            "timeUnit": "MINUTES"
          }
        },
        "pairingKeyLifetime": {
          "duration": 24,
          "timeUnit": "HOURS"
        },
        "deviceAuthorization": {
          "enabled": True,
          "extraVerification": "permissive"
        },
        "autoEnrollment": {
          "enabled": True
        },
        "integrityDetection": "permissive"
      }
    ]
  },
  "totp": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      }
    },
    "passcodeGracePeriod": 3,
    "uriParameters": {
      "issuer": "Corporate spreadsheet app"
    }
  },
  "voice": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "whatsApp": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 5,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 15,
        "timeUnit": "MINUTES"
      }
    },
    "pairingDisabled": True,
    "promptForNicknameOnPairing": True
  },
  "newDeviceNotification": "SMS_THEN_EMAIL",
  "notificationsPolicy": {
    "id": "{{notificationPolicyID}}"
  },
  "forSignOnPolicy": False,
  "fido2": {
    "enabled": True,
    "failure": {
      "count": "4",
      "coolDown": {
        "timeUnit": "SECONDS",
        "duration": 150
      }
    },
    "promptForNicknameOnPairing": True
  },
  "blockUsersWithDisabledMfa": False,
  "default": False
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "MFA policy created on {{$timestamp}}",\n    "blockDisabledUsers": true,\n    "sms": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 0,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "lifeTime": {\n                "duration": 30,\n                "timeUnit": "MINUTES"\n            },\n            "otpLength":6\n        }\n    },\n    "email": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 0,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "lifeTime": {\n                "duration": 30,\n                "timeUnit": "MINUTES"\n            },\n            "otpLength": 8\n        }\n    },\n    "mobile": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 2,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "window": {\n                "stepSize": {\n                    "duration": 30,\n                    "timeUnit": "SECONDS"\n                }\n            }\n        },\n        "applications": [\n            {\n                "id": "{{appID}}",\n                "push": {\n                    "enabled": true,\n                    "numberMatching": {\n                        "enabled":true\n                    }\n\n                },\n                "otp": {\n                    "enabled": true\n                },\n                "pushTimeout": {\n                    "duration": 120,\n                    "timeUnit": "SECONDS"\n                },\n                "pushLimit": {\n                    "count": 4,\n                    "timePeriod": {\n                        "duration": 20,\n                        "timeUnit": "MINUTES"\n                    },\n                    "lockDuration": {\n                        "duration": 30,\n                        "timeUnit": "MINUTES"\n                    }\n                },\n                "pairingKeyLifetime": {\n                    "duration": 24,\n                    "timeUnit": "HOURS"\n                },\n                "deviceAuthorization": {\n                    "enabled": true,\n                    "extraVerification": "permissive"\n                },\n                "autoEnrollment": {\n                    "enabled": true\n                },\n                "integrityDetection": "permissive"\n            }\n        ]\n    },\n    "totp": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 2,\n                    "timeUnit": "MINUTES"\n                }\n            }\n        },\n        "passcodeGracePeriod" : 3,\n        "uriParameters": {\n            "issuer": "Corporate spreadsheet app"\n        }\n    },\n    "voice": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 0,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "lifeTime": {\n                "duration": 30,\n                "timeUnit": "MINUTES"\n            },\n            "otpLength": 6\n        }\n    },\n    "whatsApp": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 5,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "lifeTime": {\n                "duration": 15,\n                "timeUnit": "MINUTES"\n            }\n        },\n        "pairingDisabled":true,\n        "promptForNicknameOnPairing":true\n    },\n    "newDeviceNotification": "SMS_THEN_EMAIL",\n    "notificationsPolicy":{\n        "id":"{{notificationPolicyID}}"\n    },\n    "forSignOnPolicy": false,\n    "fido2": {\n        "enabled": true,\n        "failure":{\n            "count":"4",\n            "coolDown":{\n                "timeUnit":"SECONDS",\n                "duration":150\n            }\n        },\n        "promptForNicknameOnPairing": true\n    },\n    "blockUsersWithDisabledMfa": false,\n    "default": false\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "MFA policy created on {{\$timestamp}}",
  "blockDisabledUsers": true,
  "sms": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "email": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 8
    }
  },
  "mobile": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      },
      "window": {
        "stepSize": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      }
    },
    "applications": [
      {
        "id": "{{appID}}",
        "push": {
          "enabled": true,
          "numberMatching": {
            "enabled": true
          }
        },
        "otp": {
          "enabled": true
        },
        "pushTimeout": {
          "duration": 120,
          "timeUnit": "SECONDS"
        },
        "pushLimit": {
          "count": 4,
          "timePeriod": {
            "duration": 20,
            "timeUnit": "MINUTES"
          },
          "lockDuration": {
            "duration": 30,
            "timeUnit": "MINUTES"
          }
        },
        "pairingKeyLifetime": {
          "duration": 24,
          "timeUnit": "HOURS"
        },
        "deviceAuthorization": {
          "enabled": true,
          "extraVerification": "permissive"
        },
        "autoEnrollment": {
          "enabled": true
        },
        "integrityDetection": "permissive"
      }
    ]
  },
  "totp": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      }
    },
    "passcodeGracePeriod": 3,
    "uriParameters": {
      "issuer": "Corporate spreadsheet app"
    }
  },
  "voice": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "whatsApp": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 5,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 15,
        "timeUnit": "MINUTES"
      }
    },
    "pairingDisabled": true,
    "promptForNicknameOnPairing": true
  },
  "newDeviceNotification": "SMS_THEN_EMAIL",
  "notificationsPolicy": {
    "id": "{{notificationPolicyID}}"
  },
  "forSignOnPolicy": false,
  "fido2": {
    "enabled": true,
    "failure": {
      "count": "4",
      "coolDown": {
        "timeUnit": "SECONDS",
        "duration": 150
      }
    },
    "promptForNicknameOnPairing": true
  },
  "blockUsersWithDisabledMfa": false,
  "default": false
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"MFA policy created on {{$timestamp}}\",\n    \"blockDisabledUsers\": true,\n    \"sms\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\":6\n        }\n    },\n    \"email\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 8\n        }\n    },\n    \"mobile\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"window\": {\n                \"stepSize\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            }\n        },\n        \"applications\": [\n            {\n                \"id\": \"{{appID}}\",\n                \"push\": {\n                    \"enabled\": true,\n                    \"numberMatching\": {\n                        \"enabled\":true\n                    }\n\n                },\n                \"otp\": {\n                    \"enabled\": true\n                },\n                \"pushTimeout\": {\n                    \"duration\": 120,\n                    \"timeUnit\": \"SECONDS\"\n                },\n                \"pushLimit\": {\n                    \"count\": 4,\n                    \"timePeriod\": {\n                        \"duration\": 20,\n                        \"timeUnit\": \"MINUTES\"\n                    },\n                    \"lockDuration\": {\n                        \"duration\": 30,\n                        \"timeUnit\": \"MINUTES\"\n                    }\n                },\n                \"pairingKeyLifetime\": {\n                    \"duration\": 24,\n                    \"timeUnit\": \"HOURS\"\n                },\n                \"deviceAuthorization\": {\n                    \"enabled\": true,\n                    \"extraVerification\": \"permissive\"\n                },\n                \"autoEnrollment\": {\n                    \"enabled\": true\n                },\n                \"integrityDetection\": \"permissive\"\n            }\n        ]\n    },\n    \"totp\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            }\n        },\n        \"passcodeGracePeriod\" : 3,\n        \"uriParameters\": {\n            \"issuer\": \"Corporate spreadsheet app\"\n        }\n    },\n    \"voice\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 6\n        }\n    },\n    \"whatsApp\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 5,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 15,\n                \"timeUnit\": \"MINUTES\"\n            }\n        },\n        \"pairingDisabled\":true,\n        \"promptForNicknameOnPairing\":true\n    },\n    \"newDeviceNotification\": \"SMS_THEN_EMAIL\",\n    \"notificationsPolicy\":{\n        \"id\":\"{{notificationPolicyID}}\"\n    },\n    \"forSignOnPolicy\": false,\n    \"fido2\": {\n        \"enabled\": true,\n        \"failure\":{\n            \"count\":\"4\",\n            \"coolDown\":{\n                \"timeUnit\":\"SECONDS\",\n                \"duration\":150\n            }\n        },\n        \"promptForNicknameOnPairing\": true\n    },\n    \"blockUsersWithDisabledMfa\": false,\n    \"default\": false\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthenticationPolicies/701e3591-4bbf-493e-ab3d-a96ba7fd5b66"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "applications": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthenticationPolicies/701e3591-4bbf-493e-ab3d-a96ba7fd5b66/applications"
        },
        "fido2": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/fido2Policies/8401cfde-1d39-4c7c-b886-d861614929e9"
        }
    },
    "id": "701e3591-4bbf-493e-ab3d-a96ba7fd5b66",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "MFA policy created on 1780240751",
    "authentication": {
        "deviceSelection": "DEFAULT_TO_FIRST"
    },
    "notificationsPolicy": {},
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "applications": [
            {
                "id": "28e07e36-63d2-46d3-8743-dbdd51c58ee0",
                "push": {
                    "enabled": true,
                    "numberMatching": {
                        "enabled": true
                    }
                },
                "otp": {
                    "enabled": true
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        },
        "passcodeGracePeriod": 3
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "whatsApp": {
        "enabled": true,
        "pairingDisabled": true,
        "promptForNicknameOnPairing": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 5,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 15,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "fido2": {
        "enabled": true,
        "promptForNicknameOnPairing": true,
        "failure": {
            "count": 4,
            "coolDown": {
                "duration": 150,
                "timeUnit": "SECONDS"
            }
        }
    },
    "oathToken": {
        "enabled": false,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        }
    },
    "rememberMe": {
        "web": {
            "enabled": false,
            "lifeTime": {
                "duration": 30,
                "timeUnit": "DAYS"
            }
        }
    },
    "pingIdDesktopGen2": {
        "enabled": false,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        }
    },
    "forSignOnPolicy": false,
    "blockDisabledUsers": true,
    "bypassBlockedWhenMfaDisabled": true,
    "updatedAt": "2026-05-31T15:19:11.307Z",
    "createdAt": "2026-05-31T15:19:11.307Z",
    "default": false
}
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthenticationPolicies/17932921-8131-4772-836b-0e72312dea9b"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "applications": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthenticationPolicies/17932921-8131-4772-836b-0e72312dea9b/applications"
        },
        "fido2": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/fido2Policies/8401cfde-1d39-4c7c-b886-d861614929e9"
        }
    },
    "id": "17932921-8131-4772-836b-0e72312dea9b",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "MFA policy created on 1782392221",
    "authentication": {
        "deviceSelection": "DEFAULT_TO_FIRST"
    },
    "notificationsPolicy": {},
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "applications": [
            {
                "id": "28e07e36-63d2-46d3-8743-dbdd51c58ee0",
                "push": {
                    "enabled": true,
                    "numberMatching": {
                        "enabled": true
                    }
                },
                "otp": {
                    "enabled": true
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        },
        "passcodeGracePeriod": 3
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "whatsApp": {
        "enabled": true,
        "pairingDisabled": true,
        "promptForNicknameOnPairing": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 5,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 15,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "fido2": {
        "enabled": true,
        "promptForNicknameOnPairing": true,
        "failure": {
            "count": 4,
            "coolDown": {
                "duration": 150,
                "timeUnit": "SECONDS"
            }
        }
    },
    "oathToken": {
        "enabled": false,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        }
    },
    "rememberMe": {
        "web": {
            "enabled": false,
            "lifeTime": {
                "duration": 30,
                "timeUnit": "DAYS"
            }
        }
    },
    "pingIdDesktopGen2": {
        "enabled": false,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        }
    },
    "forSignOnPolicy": false,
    "blockUsersWithDisabledMfa": false,
    "updatedAt": "2026-06-25T12:57:01.574Z",
    "createdAt": "2026-06-25T12:57:01.574Z",
    "default": false
}
```

---

---
title: Create Device Authentication Policy (with Remember Me enabled)
description: "This example uses a POST {{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies request to create a new MFA policy, and includes the rememberMe object to specify that the MFA policy allows users to skip the MFA step on remembered devices if you have implemented a \"remember me\" option using the PingOne API."
component: pingone-api
page_id: pingone-api:mfa:users/remembered-devices/create_mfa_policy_with_remember_me
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/users/remembered-devices/create_mfa_policy_with_remember_me.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Device Authentication Policy (with Remember Me enabled)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies
```

This example uses a `POST {{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies` request to create a new MFA policy, and includes the `rememberMe` object to specify that the MFA policy allows users to skip the MFA step on remembered devices if you have implemented a "remember me" option using the PingOne API.

|   |                                                                        |
| - | ---------------------------------------------------------------------- |
|   | To create new MFA policies, you must have a license that includes MFA. |

### Prerequisites

* Refer to [Device Authentication Policies](#device-authentication-policies) for important overview information.

* Use [Read All Applications](/pingone/platform/v1/api/#get-read-all-applications) to retrieve a list of all applications associated with the specified environment and select the specific `appID` for the body. For more information, refer to [Application Management](/pingone/platform/v1/api/#application-management), specifically [Application Operations](/pingone/platform/v1/api/#application-operations).

* Use [Read All FIDO Policies](#get-read-all-fido-policies) to retrieve all the FIDO policies for an environment and select the specific `fidoPolicyID` for the body. For more information, refer to [FIDO Policies](#fido-policies).

> **Collapse: Request Model**
>
> | Property                           | Type     | Required |
> | ---------------------------------- | -------- | -------- |
> | `default`                          | Boolean  | Required |
> | `email`                            | Object   | Required |
> | `fido2`                            | Object   | Optional |
> | `forSignOnPolicy`                  | Boolean  | Optional |
> | `mobile`                           | Object   | Required |
> | `name`                             | String   | Required |
> | `newDeviceNotification`            | Optional | Required |
> | `rememberMe`                       | Object   | Optional |
> | `rememberMe.web`                   | Object   | Optional |
> | `rememberMe.web.enabled`           | Boolean  | Optional |
> | `rememberMe.web.lifeTime`          | Object   | Optional |
> | `rememberMe.web.lifeTime.timeUnit` | String   | Optional |
> | `rememberMe.web.lifeTime.duration` | Integer  | Optional |
> | `sms`                              | Object   | Required |
> | `totp`                             | Object   | Required |
> | `voice`                            | Object   | Required |
>
> Refer to the [Device authentication policy](#device-authentication-policies) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "deviceAuthPolicy__{{$timestamp}}",
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true
                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "promptForNicknameOnPairing": true
    },
    "rememberMe":{
        "web":{
            "enabled":true,
            "lifeTime":{
                "timeUnit":"DAYS",
                "duration":60
            }
        }
    },
    "default": false
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "deviceAuthPolicy__{{$timestamp}}",
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true
                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "promptForNicknameOnPairing": true
    },
    "rememberMe":{
        "web":{
            "enabled":true,
            "lifeTime":{
                "timeUnit":"DAYS",
                "duration":60
            }
        }
    },
    "default": false
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""deviceAuthPolicy__{{$timestamp}}""," + "\n" +
@"    ""sms"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 0," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 30," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""otpLength"":6" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""email"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 0," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 30," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""otpLength"": 8" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""mobile"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 2," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""window"": {" + "\n" +
@"                ""stepSize"": {" + "\n" +
@"                    ""duration"": 30," + "\n" +
@"                    ""timeUnit"": ""SECONDS""" + "\n" +
@"                }" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""applications"": [" + "\n" +
@"            {" + "\n" +
@"                ""id"": ""{{appID}}""," + "\n" +
@"                ""push"": {" + "\n" +
@"                    ""enabled"": true" + "\n" +
@"                }," + "\n" +
@"                ""otp"": {" + "\n" +
@"                    ""enabled"": true" + "\n" +
@"                }," + "\n" +
@"                ""pushTimeout"": {" + "\n" +
@"                    ""duration"": 120," + "\n" +
@"                    ""timeUnit"": ""SECONDS""" + "\n" +
@"                }," + "\n" +
@"                ""pushLimit"": {" + "\n" +
@"                    ""count"": 4," + "\n" +
@"                    ""timePeriod"": {" + "\n" +
@"                        ""duration"": 20," + "\n" +
@"                        ""timeUnit"": ""MINUTES""" + "\n" +
@"                    }," + "\n" +
@"                    ""lockDuration"": {" + "\n" +
@"                        ""duration"": 30," + "\n" +
@"                        ""timeUnit"": ""MINUTES""" + "\n" +
@"                    }" + "\n" +
@"                }," + "\n" +
@"                ""pairingKeyLifetime"": {" + "\n" +
@"                    ""duration"": 24," + "\n" +
@"                    ""timeUnit"": ""HOURS""" + "\n" +
@"                }," + "\n" +
@"                ""deviceAuthorization"": {" + "\n" +
@"                    ""enabled"": true," + "\n" +
@"                    ""extraVerification"": ""permissive""" + "\n" +
@"                }," + "\n" +
@"                ""autoEnrollment"": {" + "\n" +
@"                    ""enabled"": true" + "\n" +
@"                }," + "\n" +
@"                ""integrityDetection"": ""permissive""" + "\n" +
@"            }" + "\n" +
@"        ]" + "\n" +
@"    }," + "\n" +
@"    ""totp"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 2," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""uriParameters"": {" + "\n" +
@"            ""issuer"": ""Corporate spreadsheet app""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""voice"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""failure"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""coolDown"": {" + "\n" +
@"                    ""duration"": 0," + "\n" +
@"                    ""timeUnit"": ""MINUTES""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 30," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""otpLength"": 6" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""newDeviceNotification"": ""SMS_THEN_EMAIL""," + "\n" +
@"    ""forSignOnPolicy"": false," + "\n" +
@"    ""fido2"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""promptForNicknameOnPairing"": true" + "\n" +
@"    }," + "\n" +
@"    ""rememberMe"":{" + "\n" +
@"        ""web"":{" + "\n" +
@"            ""enabled"":true," + "\n" +
@"            ""lifeTime"":{" + "\n" +
@"                ""timeUnit"":""DAYS""," + "\n" +
@"                ""duration"":60" + "\n" +
@"            }" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""default"": false" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "deviceAuthPolicy__{{$timestamp}}",
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true
                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "promptForNicknameOnPairing": true
    },
    "rememberMe":{
        "web":{
            "enabled":true,
            "lifeTime":{
                "timeUnit":"DAYS",
                "duration":60
            }
        }
    },
    "default": false
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
POST /v1/environments/{{envID}}/deviceAuthenticationPolicies HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "deviceAuthPolicy__{{$timestamp}}",
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength":6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            },
            "window": {
                "stepSize": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            }
        },
        "applications": [
            {
                "id": "{{appID}}",
                "push": {
                    "enabled": true
                },
                "otp": {
                    "enabled": true
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "forSignOnPolicy": false,
    "fido2": {
        "enabled": true,
        "promptForNicknameOnPairing": true
    },
    "rememberMe":{
        "web":{
            "enabled":true,
            "lifeTime":{
                "timeUnit":"DAYS",
                "duration":60
            }
        }
    },
    "default": false
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"deviceAuthPolicy__{{$timestamp}}\",\n    \"sms\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\":6\n        }\n    },\n    \"email\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 8\n        }\n    },\n    \"mobile\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"window\": {\n                \"stepSize\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            }\n        },\n        \"applications\": [\n            {\n                \"id\": \"{{appID}}\",\n                \"push\": {\n                    \"enabled\": true\n                },\n                \"otp\": {\n                    \"enabled\": true\n                },\n                \"pushTimeout\": {\n                    \"duration\": 120,\n                    \"timeUnit\": \"SECONDS\"\n                },\n                \"pushLimit\": {\n                    \"count\": 4,\n                    \"timePeriod\": {\n                        \"duration\": 20,\n                        \"timeUnit\": \"MINUTES\"\n                    },\n                    \"lockDuration\": {\n                        \"duration\": 30,\n                        \"timeUnit\": \"MINUTES\"\n                    }\n                },\n                \"pairingKeyLifetime\": {\n                    \"duration\": 24,\n                    \"timeUnit\": \"HOURS\"\n                },\n                \"deviceAuthorization\": {\n                    \"enabled\": true,\n                    \"extraVerification\": \"permissive\"\n                },\n                \"autoEnrollment\": {\n                    \"enabled\": true\n                },\n                \"integrityDetection\": \"permissive\"\n            }\n        ]\n    },\n    \"totp\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            }\n        },\n        \"uriParameters\": {\n            \"issuer\": \"Corporate spreadsheet app\"\n        }\n    },\n    \"voice\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 6\n        }\n    },\n    \"newDeviceNotification\": \"SMS_THEN_EMAIL\",\n    \"forSignOnPolicy\": false,\n    \"fido2\": {\n        \"enabled\": true,\n        \"promptForNicknameOnPairing\": true\n    },\n    \"rememberMe\":{\n        \"web\":{\n            \"enabled\":true,\n            \"lifeTime\":{\n                \"timeUnit\":\"DAYS\",\n                \"duration\":60\n            }\n        }\n    },\n    \"default\": false\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "deviceAuthPolicy__{{$timestamp}}",
    "sms": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "email": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 8
      }
    },
    "mobile": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        },
        "window": {
          "stepSize": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        }
      },
      "applications": [
        {
          "id": "{{appID}}",
          "push": {
            "enabled": true
          },
          "otp": {
            "enabled": true
          },
          "pushTimeout": {
            "duration": 120,
            "timeUnit": "SECONDS"
          },
          "pushLimit": {
            "count": 4,
            "timePeriod": {
              "duration": 20,
              "timeUnit": "MINUTES"
            },
            "lockDuration": {
              "duration": 30,
              "timeUnit": "MINUTES"
            }
          },
          "pairingKeyLifetime": {
            "duration": 24,
            "timeUnit": "HOURS"
          },
          "deviceAuthorization": {
            "enabled": true,
            "extraVerification": "permissive"
          },
          "autoEnrollment": {
            "enabled": true
          },
          "integrityDetection": "permissive"
        }
      ]
    },
    "totp": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        }
      },
      "uriParameters": {
        "issuer": "Corporate spreadsheet app"
      }
    },
    "voice": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "forSignOnPolicy": false,
    "fido2": {
      "enabled": true,
      "promptForNicknameOnPairing": true
    },
    "rememberMe": {
      "web": {
        "enabled": true,
        "lifeTime": {
          "timeUnit": "DAYS",
          "duration": 60
        }
      }
    },
    "default": false
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "deviceAuthPolicy__{{$timestamp}}",
    "sms": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "email": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 8
      }
    },
    "mobile": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        },
        "window": {
          "stepSize": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        }
      },
      "applications": [
        {
          "id": "{{appID}}",
          "push": {
            "enabled": true
          },
          "otp": {
            "enabled": true
          },
          "pushTimeout": {
            "duration": 120,
            "timeUnit": "SECONDS"
          },
          "pushLimit": {
            "count": 4,
            "timePeriod": {
              "duration": 20,
              "timeUnit": "MINUTES"
            },
            "lockDuration": {
              "duration": 30,
              "timeUnit": "MINUTES"
            }
          },
          "pairingKeyLifetime": {
            "duration": 24,
            "timeUnit": "HOURS"
          },
          "deviceAuthorization": {
            "enabled": true,
            "extraVerification": "permissive"
          },
          "autoEnrollment": {
            "enabled": true
          },
          "integrityDetection": "permissive"
        }
      ]
    },
    "totp": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 2,
            "timeUnit": "MINUTES"
          }
        }
      },
      "uriParameters": {
        "issuer": "Corporate spreadsheet app"
      }
    },
    "voice": {
      "enabled": true,
      "otp": {
        "failure": {
          "count": 3,
          "coolDown": {
            "duration": 0,
            "timeUnit": "MINUTES"
          }
        },
        "lifeTime": {
          "duration": 30,
          "timeUnit": "MINUTES"
        },
        "otpLength": 6
      }
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "forSignOnPolicy": false,
    "fido2": {
      "enabled": true,
      "promptForNicknameOnPairing": true
    },
    "rememberMe": {
      "web": {
        "enabled": true,
        "lifeTime": {
          "timeUnit": "DAYS",
          "duration": 60
        }
      }
    },
    "default": false
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

url = "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies"

payload = json.dumps({
  "name": "deviceAuthPolicy__{{$timestamp}}",
  "sms": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "email": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 8
    }
  },
  "mobile": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      },
      "window": {
        "stepSize": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      }
    },
    "applications": [
      {
        "id": "{{appID}}",
        "push": {
          "enabled": True
        },
        "otp": {
          "enabled": True
        },
        "pushTimeout": {
          "duration": 120,
          "timeUnit": "SECONDS"
        },
        "pushLimit": {
          "count": 4,
          "timePeriod": {
            "duration": 20,
            "timeUnit": "MINUTES"
          },
          "lockDuration": {
            "duration": 30,
            "timeUnit": "MINUTES"
          }
        },
        "pairingKeyLifetime": {
          "duration": 24,
          "timeUnit": "HOURS"
        },
        "deviceAuthorization": {
          "enabled": True,
          "extraVerification": "permissive"
        },
        "autoEnrollment": {
          "enabled": True
        },
        "integrityDetection": "permissive"
      }
    ]
  },
  "totp": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      }
    },
    "uriParameters": {
      "issuer": "Corporate spreadsheet app"
    }
  },
  "voice": {
    "enabled": True,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "newDeviceNotification": "SMS_THEN_EMAIL",
  "forSignOnPolicy": False,
  "fido2": {
    "enabled": True,
    "promptForNicknameOnPairing": True
  },
  "rememberMe": {
    "web": {
      "enabled": True,
      "lifeTime": {
        "timeUnit": "DAYS",
        "duration": 60
      }
    }
  },
  "default": False
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "deviceAuthPolicy__{{$timestamp}}",\n    "sms": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 0,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "lifeTime": {\n                "duration": 30,\n                "timeUnit": "MINUTES"\n            },\n            "otpLength":6\n        }\n    },\n    "email": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 0,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "lifeTime": {\n                "duration": 30,\n                "timeUnit": "MINUTES"\n            },\n            "otpLength": 8\n        }\n    },\n    "mobile": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 2,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "window": {\n                "stepSize": {\n                    "duration": 30,\n                    "timeUnit": "SECONDS"\n                }\n            }\n        },\n        "applications": [\n            {\n                "id": "{{appID}}",\n                "push": {\n                    "enabled": true\n                },\n                "otp": {\n                    "enabled": true\n                },\n                "pushTimeout": {\n                    "duration": 120,\n                    "timeUnit": "SECONDS"\n                },\n                "pushLimit": {\n                    "count": 4,\n                    "timePeriod": {\n                        "duration": 20,\n                        "timeUnit": "MINUTES"\n                    },\n                    "lockDuration": {\n                        "duration": 30,\n                        "timeUnit": "MINUTES"\n                    }\n                },\n                "pairingKeyLifetime": {\n                    "duration": 24,\n                    "timeUnit": "HOURS"\n                },\n                "deviceAuthorization": {\n                    "enabled": true,\n                    "extraVerification": "permissive"\n                },\n                "autoEnrollment": {\n                    "enabled": true\n                },\n                "integrityDetection": "permissive"\n            }\n        ]\n    },\n    "totp": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 2,\n                    "timeUnit": "MINUTES"\n                }\n            }\n        },\n        "uriParameters": {\n            "issuer": "Corporate spreadsheet app"\n        }\n    },\n    "voice": {\n        "enabled": true,\n        "otp": {\n            "failure": {\n                "count": 3,\n                "coolDown": {\n                    "duration": 0,\n                    "timeUnit": "MINUTES"\n                }\n            },\n            "lifeTime": {\n                "duration": 30,\n                "timeUnit": "MINUTES"\n            },\n            "otpLength": 6\n        }\n    },\n    "newDeviceNotification": "SMS_THEN_EMAIL",\n    "forSignOnPolicy": false,\n    "fido2": {\n        "enabled": true,\n        "promptForNicknameOnPairing": true\n    },\n    "rememberMe":{\n        "web":{\n            "enabled":true,\n            "lifeTime":{\n                "timeUnit":"DAYS",\n                "duration":60\n            }\n        }\n    },\n    "default": false\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "deviceAuthPolicy__{{\$timestamp}}",
  "sms": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "email": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 8
    }
  },
  "mobile": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      },
      "window": {
        "stepSize": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      }
    },
    "applications": [
      {
        "id": "{{appID}}",
        "push": {
          "enabled": true
        },
        "otp": {
          "enabled": true
        },
        "pushTimeout": {
          "duration": 120,
          "timeUnit": "SECONDS"
        },
        "pushLimit": {
          "count": 4,
          "timePeriod": {
            "duration": 20,
            "timeUnit": "MINUTES"
          },
          "lockDuration": {
            "duration": 30,
            "timeUnit": "MINUTES"
          }
        },
        "pairingKeyLifetime": {
          "duration": 24,
          "timeUnit": "HOURS"
        },
        "deviceAuthorization": {
          "enabled": true,
          "extraVerification": "permissive"
        },
        "autoEnrollment": {
          "enabled": true
        },
        "integrityDetection": "permissive"
      }
    ]
  },
  "totp": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 2,
          "timeUnit": "MINUTES"
        }
      }
    },
    "uriParameters": {
      "issuer": "Corporate spreadsheet app"
    }
  },
  "voice": {
    "enabled": true,
    "otp": {
      "failure": {
        "count": 3,
        "coolDown": {
          "duration": 0,
          "timeUnit": "MINUTES"
        }
      },
      "lifeTime": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "otpLength": 6
    }
  },
  "newDeviceNotification": "SMS_THEN_EMAIL",
  "forSignOnPolicy": false,
  "fido2": {
    "enabled": true,
    "promptForNicknameOnPairing": true
  },
  "rememberMe": {
    "web": {
      "enabled": true,
      "lifeTime": {
        "timeUnit": "DAYS",
        "duration": 60
      }
    }
  },
  "default": false
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"deviceAuthPolicy__{{$timestamp}}\",\n    \"sms\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\":6\n        }\n    },\n    \"email\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 8\n        }\n    },\n    \"mobile\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"window\": {\n                \"stepSize\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            }\n        },\n        \"applications\": [\n            {\n                \"id\": \"{{appID}}\",\n                \"push\": {\n                    \"enabled\": true\n                },\n                \"otp\": {\n                    \"enabled\": true\n                },\n                \"pushTimeout\": {\n                    \"duration\": 120,\n                    \"timeUnit\": \"SECONDS\"\n                },\n                \"pushLimit\": {\n                    \"count\": 4,\n                    \"timePeriod\": {\n                        \"duration\": 20,\n                        \"timeUnit\": \"MINUTES\"\n                    },\n                    \"lockDuration\": {\n                        \"duration\": 30,\n                        \"timeUnit\": \"MINUTES\"\n                    }\n                },\n                \"pairingKeyLifetime\": {\n                    \"duration\": 24,\n                    \"timeUnit\": \"HOURS\"\n                },\n                \"deviceAuthorization\": {\n                    \"enabled\": true,\n                    \"extraVerification\": \"permissive\"\n                },\n                \"autoEnrollment\": {\n                    \"enabled\": true\n                },\n                \"integrityDetection\": \"permissive\"\n            }\n        ]\n    },\n    \"totp\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 2,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            }\n        },\n        \"uriParameters\": {\n            \"issuer\": \"Corporate spreadsheet app\"\n        }\n    },\n    \"voice\": {\n        \"enabled\": true,\n        \"otp\": {\n            \"failure\": {\n                \"count\": 3,\n                \"coolDown\": {\n                    \"duration\": 0,\n                    \"timeUnit\": \"MINUTES\"\n                }\n            },\n            \"lifeTime\": {\n                \"duration\": 30,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"otpLength\": 6\n        }\n    },\n    \"newDeviceNotification\": \"SMS_THEN_EMAIL\",\n    \"forSignOnPolicy\": false,\n    \"fido2\": {\n        \"enabled\": true,\n        \"promptForNicknameOnPairing\": true\n    },\n    \"rememberMe\":{\n        \"web\":{\n            \"enabled\":true,\n            \"lifeTime\":{\n                \"timeUnit\":\"DAYS\",\n                \"duration\":60\n            }\n        }\n    },\n    \"default\": false\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/deviceAuthenticationPolicies")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/deviceAuthenticationPolicies/15d0474a-9271-489f-9eb6-de48f3284d47"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "fido2": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/fido2Policies/8401cfde-1d39-4c7c-b886-d861614929e9"
        }
    },
    "id": "15d0474a-9271-489f-9eb6-de48f3284d47",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "deviceAuthPolicy__1738511919",
    "authentication": {
        "deviceSelection": "DEFAULT_TO_FIRST"
    },
    "newDeviceNotification": "SMS_THEN_EMAIL",
    "sms": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "email": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 8
        }
    },
    "mobile": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "applications": [
            {
                "id": "28e07e36-63d2-46d3-8743-dbdd51c58ee0",
                "push": {
                    "enabled": true
                },
                "otp": {
                    "enabled": true
                },
                "autoEnrollment": {
                    "enabled": true
                },
                "deviceAuthorization": {
                    "enabled": true,
                    "extraVerification": "permissive"
                },
                "pushTimeout": {
                    "duration": 120,
                    "timeUnit": "SECONDS"
                },
                "pairingKeyLifetime": {
                    "duration": 24,
                    "timeUnit": "HOURS"
                },
                "pushLimit": {
                    "count": 4,
                    "timePeriod": {
                        "duration": 20,
                        "timeUnit": "MINUTES"
                    },
                    "lockDuration": {
                        "duration": 30,
                        "timeUnit": "MINUTES"
                    }
                },
                "integrityDetection": "permissive"
            }
        ]
    },
    "totp": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 2,
                    "timeUnit": "MINUTES"
                }
            }
        },
        "uriParameters": {
            "issuer": "Corporate spreadsheet app"
        }
    },
    "voice": {
        "enabled": true,
        "otp": {
            "failure": {
                "count": 3,
                "coolDown": {
                    "duration": 0,
                    "timeUnit": "MINUTES"
                }
            },
            "lifeTime": {
                "duration": 30,
                "timeUnit": "MINUTES"
            },
            "otpLength": 6
        }
    },
    "fido2": {
        "enabled": true,
        "promptForNicknameOnPairing": true
    },
    "rememberMe": {
        "web": {
            "enabled": true,
            "lifeTime": {
                "duration": 60,
                "timeUnit": "DAYS"
            }
        }
    },
    "forSignOnPolicy": false,
    "updatedAt": "2025-02-02T15:58:40.516Z",
    "createdAt": "2025-02-02T15:58:40.516Z",
    "default": false
}
```

---

---
title: Create FIDO Policy - all FIDO-certified authenticators
description: Use POST {{apiPath}}/v1/environments/{{envID}}/fido2Policies to create a new FIDO policy for an environment.
component: pingone-api
page_id: pingone-api:mfa:fido-policies/create_fido_policy_certified
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/fido-policies/create_fido_policy_certified.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create FIDO Policy - all FIDO-certified authenticators

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/fido2Policies
```

Use `POST {{apiPath}}/v1/environments/{{envID}}/fido2Policies` to create a new FIDO policy for an environment.

This example sets `attestationRequirements` to CERTIFIED to allow only FIDO-certified authenticators.

### Prerequisites

* Refer to [FIDO Policies](#fido-policies) for important overview information.

> **Collapse: Request Model**
>
> | Property                       | Type    | Required |
> | ------------------------------ | ------- | -------- |
> | `attestationRequirements`      | String  | Required |
> | `default`                      | Boolean | Optional |
> | `description`                  | String  | Optional |
> | `enforceDuringAuthentication`  | Boolean | Optional |
> | `name`                         | String  | Required |
> | `publicKeyCredentialHints`     | Array   | Optional |
> | `residentKeyRequirement`       | String  | Required |
> | `userPresenceTimeout`          | Object  | Optional |
> | `userPresenceTimeout.duration` | Integer | Optional |
> | `userPresenceTimeout.timeUnit` | String  | Optional |
>
> Refer to the [FIDO Policies](#fido-policies) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "FIDO Policy - allow only FIDO-certified authenticators",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ]
    },
    "attestationRequirements": "DIRECT",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/fido2Policies' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "FIDO Policy - allow only FIDO-certified authenticators",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ]
    },
    "attestationRequirements": "DIRECT",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/fido2Policies")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""FIDO Policy - allow only FIDO-certified authenticators""," + "\n" +
@"    ""description"": ""FIDO Policy that specifies that only FIDO-certified authenticators can be used""," + "\n" +
@"    ""deviceDisplayName"": ""Fido2 device""," + "\n" +
@"    ""discoverableCredentials"": ""REQUIRED""," + "\n" +
@"    ""authenticatorAttachment"": ""BOTH""," + "\n" +
@"    ""userVerification"": {" + "\n" +
@"        ""enforceDuringAuthentication"": true," + "\n" +
@"        ""option"": ""REQUIRED""" + "\n" +
@"    }," + "\n" +
@"    ""userPresenceTimeout"" : {" + "\n" +
@"        ""duration"" : 4," + "\n" +
@"        ""timeUnit"" : ""MINUTES""" + "\n" +
@"    }," + "\n" +
@"    ""backupEligibility"": {" + "\n" +
@"        ""enforceDuringAuthentication"": true," + "\n" +
@"        ""allow"": true" + "\n" +
@"    }," + "\n" +
@"    ""userDisplayNameAttributes"": {" + "\n" +
@"        ""attributes"": [" + "\n" +
@"            {" + "\n" +
@"                ""name"": ""username""" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""name"": ""email""" + "\n" +
@"            }" + "\n" +
@"        ]" + "\n" +
@"    }," + "\n" +
@"    ""attestationRequirements"": ""DIRECT""," + "\n" +
@"    ""mdsAuthenticatorsRequirements"": {" + "\n" +
@"        ""allowedAuthenticators"": null," + "\n" +
@"        ""option"": ""CERTIFIED""," + "\n" +
@"        ""enforceDuringAuthentication"": true" + "\n" +
@"    }," + "\n" +
@"    ""publicKeyCredentialHints"" : [" + "\n" +
@"        ""SECURITY_KEY"", ""CLIENT_DEVICE"",""HYBRID""" + "\n" +
@"    ]," + "\n" +
@"    ""relyingPartyId"": ""relyingpartydomain.example.com""," + "\n" +
@"    ""default"": false" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/fido2Policies"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "FIDO Policy - allow only FIDO-certified authenticators",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ]
    },
    "attestationRequirements": "DIRECT",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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
POST /v1/environments/{{envID}}/fido2Policies HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "FIDO Policy - allow only FIDO-certified authenticators",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ]
    },
    "attestationRequirements": "DIRECT",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"FIDO Policy - allow only FIDO-certified authenticators\",\n    \"description\": \"FIDO Policy that specifies that only FIDO-certified authenticators can be used\",\n    \"deviceDisplayName\": \"Fido2 device\",\n    \"discoverableCredentials\": \"REQUIRED\",\n    \"authenticatorAttachment\": \"BOTH\",\n    \"userVerification\": {\n        \"enforceDuringAuthentication\": true,\n        \"option\": \"REQUIRED\"\n    },\n    \"userPresenceTimeout\" : {\n        \"duration\" : 4,\n        \"timeUnit\" : \"MINUTES\"\n    },\n    \"backupEligibility\": {\n        \"enforceDuringAuthentication\": true,\n        \"allow\": true\n    },\n    \"userDisplayNameAttributes\": {\n        \"attributes\": [\n            {\n                \"name\": \"username\"\n            },\n            {\n                \"name\": \"email\"\n            }\n        ]\n    },\n    \"attestationRequirements\": \"DIRECT\",\n    \"mdsAuthenticatorsRequirements\": {\n        \"allowedAuthenticators\": null,\n        \"option\": \"CERTIFIED\",\n        \"enforceDuringAuthentication\": true\n    },\n    \"publicKeyCredentialHints\" : [\n        \"SECURITY_KEY\", \"CLIENT_DEVICE\",\"HYBRID\"\n    ],\n    \"relyingPartyId\": \"relyingpartydomain.example.com\",\n    \"default\": false\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/fido2Policies")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/fido2Policies",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "FIDO Policy - allow only FIDO-certified authenticators",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
      "enforceDuringAuthentication": true,
      "option": "REQUIRED"
    },
    "userPresenceTimeout": {
      "duration": 4,
      "timeUnit": "MINUTES"
    },
    "backupEligibility": {
      "enforceDuringAuthentication": true,
      "allow": true
    },
    "userDisplayNameAttributes": {
      "attributes": [
        {
          "name": "username"
        },
        {
          "name": "email"
        }
      ]
    },
    "attestationRequirements": "DIRECT",
    "mdsAuthenticatorsRequirements": {
      "allowedAuthenticators": null,
      "option": "CERTIFIED",
      "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints": [
      "SECURITY_KEY",
      "CLIENT_DEVICE",
      "HYBRID"
    ],
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/fido2Policies',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "FIDO Policy - allow only FIDO-certified authenticators",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
      "enforceDuringAuthentication": true,
      "option": "REQUIRED"
    },
    "userPresenceTimeout": {
      "duration": 4,
      "timeUnit": "MINUTES"
    },
    "backupEligibility": {
      "enforceDuringAuthentication": true,
      "allow": true
    },
    "userDisplayNameAttributes": {
      "attributes": [
        {
          "name": "username"
        },
        {
          "name": "email"
        }
      ]
    },
    "attestationRequirements": "DIRECT",
    "mdsAuthenticatorsRequirements": {
      "allowedAuthenticators": null,
      "option": "CERTIFIED",
      "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints": [
      "SECURITY_KEY",
      "CLIENT_DEVICE",
      "HYBRID"
    ],
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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

url = "{{apiPath}}/v1/environments/{{envID}}/fido2Policies"

payload = json.dumps({
  "name": "FIDO Policy - allow only FIDO-certified authenticators",
  "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
  "deviceDisplayName": "Fido2 device",
  "discoverableCredentials": "REQUIRED",
  "authenticatorAttachment": "BOTH",
  "userVerification": {
    "enforceDuringAuthentication": True,
    "option": "REQUIRED"
  },
  "userPresenceTimeout": {
    "duration": 4,
    "timeUnit": "MINUTES"
  },
  "backupEligibility": {
    "enforceDuringAuthentication": True,
    "allow": True
  },
  "userDisplayNameAttributes": {
    "attributes": [
      {
        "name": "username"
      },
      {
        "name": "email"
      }
    ]
  },
  "attestationRequirements": "DIRECT",
  "mdsAuthenticatorsRequirements": {
    "allowedAuthenticators": None,
    "option": "CERTIFIED",
    "enforceDuringAuthentication": True
  },
  "publicKeyCredentialHints": [
    "SECURITY_KEY",
    "CLIENT_DEVICE",
    "HYBRID"
  ],
  "relyingPartyId": "relyingpartydomain.example.com",
  "default": False
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/fido2Policies');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "FIDO Policy - allow only FIDO-certified authenticators",\n    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",\n    "deviceDisplayName": "Fido2 device",\n    "discoverableCredentials": "REQUIRED",\n    "authenticatorAttachment": "BOTH",\n    "userVerification": {\n        "enforceDuringAuthentication": true,\n        "option": "REQUIRED"\n    },\n    "userPresenceTimeout" : {\n        "duration" : 4,\n        "timeUnit" : "MINUTES"\n    },\n    "backupEligibility": {\n        "enforceDuringAuthentication": true,\n        "allow": true\n    },\n    "userDisplayNameAttributes": {\n        "attributes": [\n            {\n                "name": "username"\n            },\n            {\n                "name": "email"\n            }\n        ]\n    },\n    "attestationRequirements": "DIRECT",\n    "mdsAuthenticatorsRequirements": {\n        "allowedAuthenticators": null,\n        "option": "CERTIFIED",\n        "enforceDuringAuthentication": true\n    },\n    "publicKeyCredentialHints" : [\n        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"\n    ],\n    "relyingPartyId": "relyingpartydomain.example.com",\n    "default": false\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/fido2Policies")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "FIDO Policy - allow only FIDO-certified authenticators",
  "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
  "deviceDisplayName": "Fido2 device",
  "discoverableCredentials": "REQUIRED",
  "authenticatorAttachment": "BOTH",
  "userVerification": {
    "enforceDuringAuthentication": true,
    "option": "REQUIRED"
  },
  "userPresenceTimeout": {
    "duration": 4,
    "timeUnit": "MINUTES"
  },
  "backupEligibility": {
    "enforceDuringAuthentication": true,
    "allow": true
  },
  "userDisplayNameAttributes": {
    "attributes": [
      {
        "name": "username"
      },
      {
        "name": "email"
      }
    ]
  },
  "attestationRequirements": "DIRECT",
  "mdsAuthenticatorsRequirements": {
    "allowedAuthenticators": "__RUBY\#%0NULL__",
    "option": "CERTIFIED",
    "enforceDuringAuthentication": true
  },
  "publicKeyCredentialHints": [
    "SECURITY_KEY",
    "CLIENT_DEVICE",
    "HYBRID"
  ],
  "relyingPartyId": "relyingpartydomain.example.com",
  "default": false
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"FIDO Policy - allow only FIDO-certified authenticators\",\n    \"description\": \"FIDO Policy that specifies that only FIDO-certified authenticators can be used\",\n    \"deviceDisplayName\": \"Fido2 device\",\n    \"discoverableCredentials\": \"REQUIRED\",\n    \"authenticatorAttachment\": \"BOTH\",\n    \"userVerification\": {\n        \"enforceDuringAuthentication\": true,\n        \"option\": \"REQUIRED\"\n    },\n    \"userPresenceTimeout\" : {\n        \"duration\" : 4,\n        \"timeUnit\" : \"MINUTES\"\n    },\n    \"backupEligibility\": {\n        \"enforceDuringAuthentication\": true,\n        \"allow\": true\n    },\n    \"userDisplayNameAttributes\": {\n        \"attributes\": [\n            {\n                \"name\": \"username\"\n            },\n            {\n                \"name\": \"email\"\n            }\n        ]\n    },\n    \"attestationRequirements\": \"DIRECT\",\n    \"mdsAuthenticatorsRequirements\": {\n        \"allowedAuthenticators\": null,\n        \"option\": \"CERTIFIED\",\n        \"enforceDuringAuthentication\": true\n    },\n    \"publicKeyCredentialHints\" : [\n        \"SECURITY_KEY\", \"CLIENT_DEVICE\",\"HYBRID\"\n    ],\n    \"relyingPartyId\": \"relyingpartydomain.example.com\",\n    \"default\": false\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/fido2Policies")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/fido2Policies/916195d3-1039-42b2-a4fa-8cabab16b86f"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "916195d3-1039-42b2-a4fa-8cabab16b86f",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "updatedAt": "2024-12-09T12:19:56.814Z",
    "createdAt": "2024-12-09T12:19:56.814Z",
    "name": "FIDO Policy - allow only FIDO-certified authenticators",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout": {
        "duration": 2,
        "timeUnit": "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ]
    },
    "attestationRequirements": "DIRECT",
    "mdsAuthenticatorsRequirements": {
        "enforceDuringAuthentication": true,
        "option": "CERTIFIED"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "publicKeyCredentialHints": [
        "SECURITY_KEY",
        "CLIENT_DEVICE",
        "HYBRID"
    ],
    "aggregateDevices": false,
    "default": false
}
```

---

---
title: Create FIDO Policy - FIDO-certified and enterprise
description: This example uses POST {{apiPath}}/v1/environments/{{envID}}/fido2Policies to create a new FIDO policy that requires enterprise attestation to verify that the authenticator being used was provided by the organization.
component: pingone-api
page_id: pingone-api:mfa:fido-policies/create_fido_policy_certified_w_enterprise_attestation
canonical_url: https://developer.pingidentity.com/pingone-api/mfa/fido-policies/create_fido_policy_certified_w_enterprise_attestation.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create FIDO Policy - FIDO-certified and enterprise

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/fido2Policies
```

This example uses `POST {{apiPath}}/v1/environments/{{envID}}/fido2Policies` to create a new FIDO policy that requires enterprise attestation to verify that the authenticator being used was provided by the organization.

The body of the request specifies that enterprise attestation is required by setting the `attestationRequirements` field to `ENTERPRISE`.

For an additional layer of security, the request also includes the `eaUniqueIdentifierAttribute.name` field to specify the name of a PingOne custom attribute that represents the unique identifier for the authenticator so that it can be validated.

### Prerequisites

* Refer to [FIDO Policies](#fido-policies) for important overview information.

> **Collapse: Request Model**
>
> | Property                                                    | Type    | Required |
> | ----------------------------------------------------------- | ------- | -------- |
> | `attestationRequirements`                                   | String  | Required |
> | `authenticatorAttachment`                                   | String  | Required |
> | `backupEligibility.allow`                                   | Boolean | Required |
> | `backupEligibility.enforceDuringAuthentication`             | Boolean | Required |
> | `default`                                                   | Boolean | Optional |
> | `description`                                               | String  | Optional |
> | `deviceDisplayName`                                         | String  | Required |
> | `discoverableCredentials`                                   | String  | Required |
> | `eaUniqueIdentifierAttribute.name`                          | String  | Optional |
> | `mdsAuthenticatorsRequirements.allowedAuthenticators`       | Array   | Required |
> | `mdsAuthenticatorsRequirements.enforceDuringAuthentication` | Boolean | Required |
> | `mdsAuthenticatorsRequirements.option`                      | String  | Required |
> | `name`                                                      | String  | Required |
> | `publicKeyCredentialHints`                                  | Array   | Optional |
> | `relyingPartyId`                                            | String  | Required |
> | `residentKeyRequirement`                                    | String  | Required |
> | `userDisplayNameAttributes.attributes`                      | String  | Optional |
> | `userDisplayNameAttributes.suffix`                          | String  | Optional |
> | `userPresenceTimeout`                                       | Object  | Optional |
> | `userPresenceTimeout.duration`                              | Integer | Optional |
> | `userPresenceTimeout.timeUnit`                              | String  | Optional |
> | `userVerification.enforceDuringAuthentication`              | String  | Optional |
> | `userVerification.option`                                   | String  | Optional |
>
> Refer to the [FIDO Policies](#fido-policies) data model for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "FIDO Policy - require FIDO-certified and enterprise",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ],
        "suffix": "ORG_NAME_AND_ENV_NAME"
    },
    "attestationRequirements": "ENTERPRISE",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "eaUniqueIdentifierAttribute": {
        "name": "deviceIdentifier"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/fido2Policies' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "FIDO Policy - require FIDO-certified and enterprise",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ],
        "suffix": "ORG_NAME_AND_ENV_NAME"
    },
    "attestationRequirements": "ENTERPRISE",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "eaUniqueIdentifierAttribute": {
        "name": "deviceIdentifier"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/fido2Policies")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""FIDO Policy - require FIDO-certified and enterprise""," + "\n" +
@"    ""description"": ""FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used""," + "\n" +
@"    ""deviceDisplayName"": ""Fido2 device""," + "\n" +
@"    ""discoverableCredentials"": ""REQUIRED""," + "\n" +
@"    ""authenticatorAttachment"": ""BOTH""," + "\n" +
@"    ""userVerification"": {" + "\n" +
@"        ""enforceDuringAuthentication"": true," + "\n" +
@"        ""option"": ""REQUIRED""" + "\n" +
@"    }," + "\n" +
@"    ""userPresenceTimeout"" : {" + "\n" +
@"        ""duration"" : 4," + "\n" +
@"        ""timeUnit"" : ""MINUTES""" + "\n" +
@"    }," + "\n" +
@"    ""backupEligibility"": {" + "\n" +
@"        ""enforceDuringAuthentication"": true," + "\n" +
@"        ""allow"": true" + "\n" +
@"    }," + "\n" +
@"    ""userDisplayNameAttributes"": {" + "\n" +
@"        ""attributes"": [" + "\n" +
@"            {" + "\n" +
@"                ""name"": ""username""" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""name"": ""email""" + "\n" +
@"            }" + "\n" +
@"        ]," + "\n" +
@"        ""suffix"": ""ORG_NAME_AND_ENV_NAME""" + "\n" +
@"    }," + "\n" +
@"    ""attestationRequirements"": ""ENTERPRISE""," + "\n" +
@"    ""mdsAuthenticatorsRequirements"": {" + "\n" +
@"        ""allowedAuthenticators"": null," + "\n" +
@"        ""option"": ""CERTIFIED""," + "\n" +
@"        ""enforceDuringAuthentication"": true" + "\n" +
@"    }," + "\n" +
@"    ""publicKeyCredentialHints"" : [" + "\n" +
@"        ""SECURITY_KEY"", ""CLIENT_DEVICE"",""HYBRID""" + "\n" +
@"    ]," + "\n" +
@"    ""eaUniqueIdentifierAttribute"": {" + "\n" +
@"        ""name"": ""deviceIdentifier""" + "\n" +
@"    }," + "\n" +
@"    ""relyingPartyId"": ""relyingpartydomain.example.com""," + "\n" +
@"    ""default"": false" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/fido2Policies"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "FIDO Policy - require FIDO-certified and enterprise",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ],
        "suffix": "ORG_NAME_AND_ENV_NAME"
    },
    "attestationRequirements": "ENTERPRISE",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "eaUniqueIdentifierAttribute": {
        "name": "deviceIdentifier"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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
POST /v1/environments/{{envID}}/fido2Policies HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "FIDO Policy - require FIDO-certified and enterprise",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout" : {
        "duration" : 4,
        "timeUnit" : "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ],
        "suffix": "ORG_NAME_AND_ENV_NAME"
    },
    "attestationRequirements": "ENTERPRISE",
    "mdsAuthenticatorsRequirements": {
        "allowedAuthenticators": null,
        "option": "CERTIFIED",
        "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints" : [
        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"
    ],
    "eaUniqueIdentifierAttribute": {
        "name": "deviceIdentifier"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"FIDO Policy - require FIDO-certified and enterprise\",\n    \"description\": \"FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used\",\n    \"deviceDisplayName\": \"Fido2 device\",\n    \"discoverableCredentials\": \"REQUIRED\",\n    \"authenticatorAttachment\": \"BOTH\",\n    \"userVerification\": {\n        \"enforceDuringAuthentication\": true,\n        \"option\": \"REQUIRED\"\n    },\n    \"userPresenceTimeout\" : {\n        \"duration\" : 4,\n        \"timeUnit\" : \"MINUTES\"\n    },\n    \"backupEligibility\": {\n        \"enforceDuringAuthentication\": true,\n        \"allow\": true\n    },\n    \"userDisplayNameAttributes\": {\n        \"attributes\": [\n            {\n                \"name\": \"username\"\n            },\n            {\n                \"name\": \"email\"\n            }\n        ],\n        \"suffix\": \"ORG_NAME_AND_ENV_NAME\"\n    },\n    \"attestationRequirements\": \"ENTERPRISE\",\n    \"mdsAuthenticatorsRequirements\": {\n        \"allowedAuthenticators\": null,\n        \"option\": \"CERTIFIED\",\n        \"enforceDuringAuthentication\": true\n    },\n    \"publicKeyCredentialHints\" : [\n        \"SECURITY_KEY\", \"CLIENT_DEVICE\",\"HYBRID\"\n    ],\n    \"eaUniqueIdentifierAttribute\": {\n        \"name\": \"deviceIdentifier\"\n    },\n    \"relyingPartyId\": \"relyingpartydomain.example.com\",\n    \"default\": false\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/fido2Policies")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/fido2Policies",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "FIDO Policy - require FIDO-certified and enterprise",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
      "enforceDuringAuthentication": true,
      "option": "REQUIRED"
    },
    "userPresenceTimeout": {
      "duration": 4,
      "timeUnit": "MINUTES"
    },
    "backupEligibility": {
      "enforceDuringAuthentication": true,
      "allow": true
    },
    "userDisplayNameAttributes": {
      "attributes": [
        {
          "name": "username"
        },
        {
          "name": "email"
        }
      ],
      "suffix": "ORG_NAME_AND_ENV_NAME"
    },
    "attestationRequirements": "ENTERPRISE",
    "mdsAuthenticatorsRequirements": {
      "allowedAuthenticators": null,
      "option": "CERTIFIED",
      "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints": [
      "SECURITY_KEY",
      "CLIENT_DEVICE",
      "HYBRID"
    ],
    "eaUniqueIdentifierAttribute": {
      "name": "deviceIdentifier"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/fido2Policies',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "FIDO Policy - require FIDO-certified and enterprise",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
      "enforceDuringAuthentication": true,
      "option": "REQUIRED"
    },
    "userPresenceTimeout": {
      "duration": 4,
      "timeUnit": "MINUTES"
    },
    "backupEligibility": {
      "enforceDuringAuthentication": true,
      "allow": true
    },
    "userDisplayNameAttributes": {
      "attributes": [
        {
          "name": "username"
        },
        {
          "name": "email"
        }
      ],
      "suffix": "ORG_NAME_AND_ENV_NAME"
    },
    "attestationRequirements": "ENTERPRISE",
    "mdsAuthenticatorsRequirements": {
      "allowedAuthenticators": null,
      "option": "CERTIFIED",
      "enforceDuringAuthentication": true
    },
    "publicKeyCredentialHints": [
      "SECURITY_KEY",
      "CLIENT_DEVICE",
      "HYBRID"
    ],
    "eaUniqueIdentifierAttribute": {
      "name": "deviceIdentifier"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "default": false
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

url = "{{apiPath}}/v1/environments/{{envID}}/fido2Policies"

payload = json.dumps({
  "name": "FIDO Policy - require FIDO-certified and enterprise",
  "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
  "deviceDisplayName": "Fido2 device",
  "discoverableCredentials": "REQUIRED",
  "authenticatorAttachment": "BOTH",
  "userVerification": {
    "enforceDuringAuthentication": True,
    "option": "REQUIRED"
  },
  "userPresenceTimeout": {
    "duration": 4,
    "timeUnit": "MINUTES"
  },
  "backupEligibility": {
    "enforceDuringAuthentication": True,
    "allow": True
  },
  "userDisplayNameAttributes": {
    "attributes": [
      {
        "name": "username"
      },
      {
        "name": "email"
      }
    ],
    "suffix": "ORG_NAME_AND_ENV_NAME"
  },
  "attestationRequirements": "ENTERPRISE",
  "mdsAuthenticatorsRequirements": {
    "allowedAuthenticators": None,
    "option": "CERTIFIED",
    "enforceDuringAuthentication": True
  },
  "publicKeyCredentialHints": [
    "SECURITY_KEY",
    "CLIENT_DEVICE",
    "HYBRID"
  ],
  "eaUniqueIdentifierAttribute": {
    "name": "deviceIdentifier"
  },
  "relyingPartyId": "relyingpartydomain.example.com",
  "default": False
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/fido2Policies');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "FIDO Policy - require FIDO-certified and enterprise",\n    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",\n    "deviceDisplayName": "Fido2 device",\n    "discoverableCredentials": "REQUIRED",\n    "authenticatorAttachment": "BOTH",\n    "userVerification": {\n        "enforceDuringAuthentication": true,\n        "option": "REQUIRED"\n    },\n    "userPresenceTimeout" : {\n        "duration" : 4,\n        "timeUnit" : "MINUTES"\n    },\n    "backupEligibility": {\n        "enforceDuringAuthentication": true,\n        "allow": true\n    },\n    "userDisplayNameAttributes": {\n        "attributes": [\n            {\n                "name": "username"\n            },\n            {\n                "name": "email"\n            }\n        ],\n        "suffix": "ORG_NAME_AND_ENV_NAME"\n    },\n    "attestationRequirements": "ENTERPRISE",\n    "mdsAuthenticatorsRequirements": {\n        "allowedAuthenticators": null,\n        "option": "CERTIFIED",\n        "enforceDuringAuthentication": true\n    },\n    "publicKeyCredentialHints" : [\n        "SECURITY_KEY", "CLIENT_DEVICE","HYBRID"\n    ],\n    "eaUniqueIdentifierAttribute": {\n        "name": "deviceIdentifier"\n    },\n    "relyingPartyId": "relyingpartydomain.example.com",\n    "default": false\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/fido2Policies")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "FIDO Policy - require FIDO-certified and enterprise",
  "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
  "deviceDisplayName": "Fido2 device",
  "discoverableCredentials": "REQUIRED",
  "authenticatorAttachment": "BOTH",
  "userVerification": {
    "enforceDuringAuthentication": true,
    "option": "REQUIRED"
  },
  "userPresenceTimeout": {
    "duration": 4,
    "timeUnit": "MINUTES"
  },
  "backupEligibility": {
    "enforceDuringAuthentication": true,
    "allow": true
  },
  "userDisplayNameAttributes": {
    "attributes": [
      {
        "name": "username"
      },
      {
        "name": "email"
      }
    ],
    "suffix": "ORG_NAME_AND_ENV_NAME"
  },
  "attestationRequirements": "ENTERPRISE",
  "mdsAuthenticatorsRequirements": {
    "allowedAuthenticators": "__RUBY\#%0NULL__",
    "option": "CERTIFIED",
    "enforceDuringAuthentication": true
  },
  "publicKeyCredentialHints": [
    "SECURITY_KEY",
    "CLIENT_DEVICE",
    "HYBRID"
  ],
  "eaUniqueIdentifierAttribute": {
    "name": "deviceIdentifier"
  },
  "relyingPartyId": "relyingpartydomain.example.com",
  "default": false
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"FIDO Policy - require FIDO-certified and enterprise\",\n    \"description\": \"FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used\",\n    \"deviceDisplayName\": \"Fido2 device\",\n    \"discoverableCredentials\": \"REQUIRED\",\n    \"authenticatorAttachment\": \"BOTH\",\n    \"userVerification\": {\n        \"enforceDuringAuthentication\": true,\n        \"option\": \"REQUIRED\"\n    },\n    \"userPresenceTimeout\" : {\n        \"duration\" : 4,\n        \"timeUnit\" : \"MINUTES\"\n    },\n    \"backupEligibility\": {\n        \"enforceDuringAuthentication\": true,\n        \"allow\": true\n    },\n    \"userDisplayNameAttributes\": {\n        \"attributes\": [\n            {\n                \"name\": \"username\"\n            },\n            {\n                \"name\": \"email\"\n            }\n        ],\n        \"suffix\": \"ORG_NAME_AND_ENV_NAME\"\n    },\n    \"attestationRequirements\": \"ENTERPRISE\",\n    \"mdsAuthenticatorsRequirements\": {\n        \"allowedAuthenticators\": null,\n        \"option\": \"CERTIFIED\",\n        \"enforceDuringAuthentication\": true\n    },\n    \"publicKeyCredentialHints\" : [\n        \"SECURITY_KEY\", \"CLIENT_DEVICE\",\"HYBRID\"\n    ],\n    \"eaUniqueIdentifierAttribute\": {\n        \"name\": \"deviceIdentifier\"\n    },\n    \"relyingPartyId\": \"relyingpartydomain.example.com\",\n    \"default\": false\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/fido2Policies")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/fido2Policies"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "24345935-0ec1-456a-8503-91c6ee2b84cc",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "updatedAt": "2025-05-05T15:37:50.045Z",
    "createdAt": "2025-05-05T15:37:50.045Z",
    "name": "FIDO Policy - require FIDO-certified and enterprise",
    "description": "FIDO Policy that specifies that only FIDO-certified authenticators issues by enterprise can be used",
    "deviceDisplayName": "Fido2 device",
    "discoverableCredentials": "REQUIRED",
    "authenticatorAttachment": "BOTH",
    "userVerification": {
        "enforceDuringAuthentication": true,
        "option": "REQUIRED"
    },
    "userPresenceTimeout": {
        "duration": 4,
        "timeUnit": "MINUTES"
    },
    "backupEligibility": {
        "enforceDuringAuthentication": true,
        "allow": true
    },
    "userDisplayNameAttributes": {
        "attributes": [
            {
                "name": "username"
            },
            {
                "name": "email"
            }
        ],
        "suffix": "ORG_NAME_AND_ENV_NAME"
    },
    "attestationRequirements": "ENTERPRISE",
    "mdsAuthenticatorsRequirements": {
        "enforceDuringAuthentication": true,
        "option": "CERTIFIED"
    },
    "relyingPartyId": "relyingpartydomain.example.com",
    "publicKeyCredentialHints": [
        "SECURITY_KEY",
        "CLIENT_DEVICE",
        "HYBRID"
    ],
    "aggregateDevices": false,
    "eaUniqueIdentifierAttribute": {
        "name": "deviceIdentifier"
    },
    "default": false
}
```
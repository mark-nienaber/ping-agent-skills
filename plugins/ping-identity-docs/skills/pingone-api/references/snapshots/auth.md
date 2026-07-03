---
title: Accept Admin Invite
description: The POST /{{envID}}/flows/{{flowID}} operation is used to accept an admin invitation.
component: pingone-api
page_id: pingone-api:auth:flows/flows-1/admin-invitations/accept-admin-invite
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/flows-1/admin-invitations/accept-admin-invite.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Accept Admin Invite

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

The `POST /{{envID}}/flows/{{flowID}}` operation is used to accept an admin invitation.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This endpoint requires the environment to be configured with admin security enabled and the authentication source must be either PingOne or Hybrid. |

This operation uses the `application/vnd.pingidentity.user.acceptInvite+json` custom media type as the content type in the request header.

In the request body:

* The `inviteCode`, `password`, and `accept` attributes are required. The `accept` attribute must be set to true.

If successful, the response returns a `200 OK` message. The user is valid and able to authenticate with PingOne.

### Prerequisites

* Send an admin invitation to a user: [Send Admin Invite](../../../../platform/users/user-admin-invitations/send-admin-invite.html).

* Send an authorize request to get a flow ID: [Authorize](../../../openid-connect-oauth-2/authorize-intro.html).

> **Collapse: Request Model**
>
> | Property     | Type    | Required |
> | ------------ | ------- | -------- |
> | `accept`     | Boolean | Required |
> | `inviteCode` | String  | Required |
> | `password`   | String  | Required |
>
> Refer to the [Users data model](../../../../platform/users/users-1.html#users-data-model) data model for full property descriptions.

### Headers

Content-Type      application/vnd.pingidentity.user.acceptInvite+json

### Body

raw ( application/vnd.pingidentity.user.acceptInvite+json )

```json
{
    "inviteCode": "{{inviteCode}}",
    "password": "{{userPassword}}",
    "accept": "true"
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
curl --location --globoff '{{authPath}}/{{envID}}/flows/{{flowID}}' \
--header 'Content-Type: application/vnd.pingidentity.user.acceptInvite+json' \
--data '{
    "inviteCode": "{{inviteCode}}",
    "password": "{{userPassword}}",
    "accept": "true"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/flows/{{flowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.user.acceptInvite+json");
var body = @"{" + "\n" +
@"    ""inviteCode"": ""{{inviteCode}}""," + "\n" +
@"    ""password"": ""{{userPassword}}""," + "\n" +
@"    ""accept"": ""true""" + "\n" +
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

  url := "{{authPath}}/{{envID}}/flows/{{flowID}}"
  method := "POST"

  payload := strings.NewReader(`{
    "inviteCode": "{{inviteCode}}",
    "password": "{{userPassword}}",
    "accept": "true"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.user.acceptInvite+json")

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
POST /{{envID}}/flows/{{flowID}} HTTP/1.1
Host: {{authPath}}
Content-Type: application/vnd.pingidentity.user.acceptInvite+json

{
    "inviteCode": "{{inviteCode}}",
    "password": "{{userPassword}}",
    "accept": "true"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.user.acceptInvite+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"inviteCode\": \"{{inviteCode}}\",\n    \"password\": \"{{userPassword}}\",\n    \"accept\": \"true\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/flows/{{flowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.user.acceptInvite+json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/flows/{{flowID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.user.acceptInvite+json"
  },
  "data": JSON.stringify({
    "inviteCode": "{{inviteCode}}",
    "password": "{{userPassword}}",
    "accept": "true"
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
  'url': '{{authPath}}/{{envID}}/flows/{{flowID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.user.acceptInvite+json'
  },
  body: JSON.stringify({
    "inviteCode": "{{inviteCode}}",
    "password": "{{userPassword}}",
    "accept": "true"
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

url = "{{authPath}}/{{envID}}/flows/{{flowID}}"

payload = json.dumps({
  "inviteCode": "{{inviteCode}}",
  "password": "{{userPassword}}",
  "accept": "true"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.user.acceptInvite+json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/flows/{{flowID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.user.acceptInvite+json'
));
$request->setBody('{\n    "inviteCode": "{{inviteCode}}",\n    "password": "{{userPassword}}",\n    "accept": "true"\n}');
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

url = URI("{{authPath}}/{{envID}}/flows/{{flowID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.user.acceptInvite+json"
request.body = JSON.dump({
  "inviteCode": "{{inviteCode}}",
  "password": "{{userPassword}}",
  "accept": "true"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"inviteCode\": \"{{inviteCode}}\",\n    \"password\": \"{{userPassword}}\",\n    \"accept\": \"true\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/flows/{{flowID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.user.acceptInvite+json", forHTTPHeaderField: "Content-Type")

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
  "_links" : {
    "self" : {
      "href" : "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/297ec011-2e86-4574-8154-06acf5fec33c"
    }
  },
  "id" : "5282e30d-6e05-499c-ae68-0069fba776f1",
  "session" : {
    "id" : "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
  },
  "resumeUrl" : "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=297ec011-2e86-4574-8154-06acf5fec33c",
  "status" : "COMPLETED",
  "createdAt" : "2024-09-16T17:14:56.830Z",
  "expiresAt" : "2024-09-16T17:32:13.859Z",
  "adminApp" : true,
  "_embedded" : {
    "user" : {
      "id" : "297ec011-2e86-4574-8154-06acf5fec33c",
      "username" : "someone@example.com",
      "name" : {
        "given" : "Mary",
        "family" : "Sample"
      }
    },
    "application" : {
      "name" : "PingOne Admin Console Example",
      "icon" : {
        "id" : "dba694dc-c9b0-433d-a7f5-8aafac7b4306",
        "href" : "https://assets.example.com/ux/ui-library/4.11.0/images/logo.png"
      }
    }
  }
}
```

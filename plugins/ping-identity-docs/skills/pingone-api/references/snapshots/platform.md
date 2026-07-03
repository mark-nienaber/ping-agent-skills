---
title: Accept Agreement
description: The POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}} operation gives the actor the ability to accept an agreement for the specified user. This operation uses the application/vnd.pingidentity.consent.accept+json custom content type in the request header.
component: pingone-api
page_id: pingone-api:platform:users/user-agreement-consents/accept-agreement
canonical_url: https://developer.pingidentity.com/pingone-api/platform/users/user-agreement-consents/accept-agreement.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
---

# Accept Agreement

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}
```

The `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}` operation gives the actor the ability to accept an agreement for the specified user. This operation uses the `application/vnd.pingidentity.consent.accept+json` custom content type in the request header.

The request body specifies the language ID and the revision ID associated with the agreement ID specified in the request URL. The request also supports the `consentedAt` property to designate the timestamp to set for the time of consent. If this property is not provided, a value of `Date.now` is used by default.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For information about importing external consents into PingOne, refer to [Migrate Existing External Agreement Consents to PingOne](../../agreement-management/migrate-existing-external-agreement-consents-to-pingone.html). |

### Prerequisites

* Refer to [User Operations](../users-1.html) for important overview information.

* Create a user to get a `userID`. Refer to [Create User](../users-1/create-user.html).

* Create an agreement to get an `agreementID`. Refer to [Create Agreement](../../agreement-management/agreements-resources/create-agreement.html).

* Create a language to get a `language.id`. Refer to [Create Language](../../agreement-management/agreement-languages-resources/create-language.html).

* Create a revision to get a `revision.id`. Refer to [Create Revision](../../agreement-management/agreement-revisions-resources/create-revision.html).

> **Collapse: Request Model**
>
> | Property      | Type   | Required |
> | ------------- | ------ | -------- |
> | `language.id` | String | Required |
> | `revision.id` | String | Required |
> | `consentedAt` | String | Optional |
>
> Refer to the [User agreement consents data model](../user-agreement-consents.html#user-agreement-consents-data-model) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.consent.accept+json

### Body

raw ( application/vnd.pingidentity.consent.accept+json )

```json
{
    "language": {
        "id": "{{languageID}}"
    },
    "revision": {
        "id": "{{revisionID}}"
    },
    "consentedAt": {{date}}
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}' \
--header 'Content-Type: application/vnd.pingidentity.consent.accept+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "language": {
        "id": "{{languageID}}"
    },
    "revision": {
        "id": "{{revisionID}}"
    },
    "consentedAt": {{date}}
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.consent.accept+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""language"": {" + "\n" +
@"        ""id"": ""{{languageID}}""" + "\n" +
@"    }," + "\n" +
@"    ""revision"": {" + "\n" +
@"        ""id"": ""{{revisionID}}""" + "\n" +
@"    }," + "\n" +
@"    ""consentedAt"": {{date}}" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}"
  method := "POST"

  payload := strings.NewReader(`{
    "language": {
        "id": "{{languageID}}"
    },
    "revision": {
        "id": "{{revisionID}}"
    },
    "consentedAt": {{date}}
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.consent.accept+json")
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
POST /v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.consent.accept+json
Authorization: Bearer {{accessToken}}

{
    "language": {
        "id": "{{languageID}}"
    },
    "revision": {
        "id": "{{revisionID}}"
    },
    "consentedAt": {{date}}
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.consent.accept+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"language\": {\n        \"id\": \"{{languageID}}\"\n    },\n    \"revision\": {\n        \"id\": \"{{revisionID}}\"\n    },\n    \"consentedAt\": {{date}}\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.consent.accept+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.consent.accept+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": "{\n    \"language\": {\n        \"id\": \"{{languageID}}\"\n    },\n    \"revision\": {\n        \"id\": \"{{revisionID}}\"\n    },\n    \"consentedAt\": {{date}}\n}",
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.consent.accept+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: '{\n    "language": {\n        "id": "{{languageID}}"\n    },\n    "revision": {\n        "id": "{{revisionID}}"\n    },\n    "consentedAt": {{date}}\n}'

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}"

payload = "{\n    \"language\": {\n        \"id\": \"{{languageID}}\"\n    },\n    \"revision\": {\n        \"id\": \"{{revisionID}}\"\n    },\n    \"consentedAt\": {{date}}\n}"
headers = {
  'Content-Type': 'application/vnd.pingidentity.consent.accept+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.consent.accept+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "language": {\n        "id": "{{languageID}}"\n    },\n    "revision": {\n        "id": "{{revisionID}}"\n    },\n    "consentedAt": {{date}}\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.consent.accept+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = "{\n    \"language\": {\n        \"id\": \"{{languageID}}\"\n    },\n    \"revision\": {\n        \"id\": \"{{revisionID}}\"\n    },\n    \"consentedAt\": {{date}}\n}"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"language\": {\n        \"id\": \"{{languageID}}\"\n    },\n    \"revision\": {\n        \"id\": \"{{revisionID}}\"\n    },\n    \"consentedAt\": {{date}}\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.consent.accept+json", forHTTPHeaderField: "Content-Type")
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

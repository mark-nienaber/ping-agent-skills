---
title: Apply Credential Issuance Rule Staged Changes
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges operation to apply the changes staged by the specified credential issuance rule for the specified credential type in the specified environment.
component: pingone-api
page_id: pingone-api:credentials:credential-issuance-rules/apply-credential-issuance-rule
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-issuance-rules/apply-credential-issuance-rule.html
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

# Apply Credential Issuance Rule Staged Changes

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges` operation to apply the changes staged by the specified credential issuance rule for the specified credential type in the specified environment.

If an action is set to `PERIODIC` and the service has not yet reached the end of the period, this operation performs staged changes for actions set to `PERIODIC` and for actions set to `ON_DEMAND`. The reverse is not true. If an action is set to `ON_DEMAND`, you must use this operation to perform staged changes for those actions.

The first example shows the response to a request with a body identifying specific actions. The second example shows the response to a request without a request body.

For each staged credential, the credential service uses a notification template appropriate to the action, `credential_issued`, `credential_updated`, or `credential_revoked`, to send notice of the action taken to the user via email or SMS text using notification templates defined in [Create Credential Issuance Rule](create-credential-issuance-rule.html) or [Update Credential Issuance Rule](update-credential-issuance-rule.html).

### Prerequisites

* [Create a credential type (automated)](../credential-types/create-credential-type-automated.html) or [Create a credential type (managed)](../credential-types/create-credential-type-managed.html) to get a `credentialTypeID` for the endpoint. Refer also to [Credential Types](../credential-types.html).

* [Create a credential issuance rule](create-credential-issuance-rule.html) to get a `credentialIssuanceRuleID` for the endpoint. Refer also to [Credential Issuance Rules](../credential-issuance-rules.html).

> **Collapse: Request Model**
>
> Refer to [Credential Issuance Rules staged changes data model](../credential-issuance-rules.html#credential-issuance-rules-staged-changes-data-model) for full property descriptions.
>
> | Property | Type      | Required |
> | -------- | --------- | -------- |
> | `issue`  | String\[] | Optional |
> | `revoke` | String\[] | Optional |
> | `update` | String\[] | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.credentials.applyStagedChanges+json

### Body

raw ( application/vnd.pingidentity.credentials.applyStagedChanges+json )

```json
{
    "revoke": [
        "{{userID}}",
        "{{userID_2}}"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges' \
--header 'Content-Type: application/vnd.pingidentity.credentials.applyStagedChanges+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "revoke": [
        "{{userID}}",
        "{{userID_2}}"
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.credentials.applyStagedChanges+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""revoke"": [" + "\n" +
@"        ""{{userID}}""," + "\n" +
@"        ""{{userID_2}}""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges"
  method := "POST"

  payload := strings.NewReader(`{
    "revoke": [
        "{{userID}}",
        "{{userID_2}}"
    ]
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.credentials.applyStagedChanges+json")
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
POST /v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.credentials.applyStagedChanges+json
Authorization: Bearer {{accessToken}}

{
    "revoke": [
        "{{userID}}",
        "{{userID_2}}"
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.credentials.applyStagedChanges+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"revoke\": [\n        \"{{userID}}\",\n        \"{{userID_2}}\"\n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.credentials.applyStagedChanges+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.credentials.applyStagedChanges+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "revoke": [
      "{{userID}}",
      "{{userID_2}}"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.credentials.applyStagedChanges+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "revoke": [
      "{{userID}}",
      "{{userID_2}}"
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

url = "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges"

payload = json.dumps({
  "revoke": [
    "{{userID}}",
    "{{userID_2}}"
  ]
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.credentials.applyStagedChanges+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.credentials.applyStagedChanges+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "revoke": [\n        "{{userID}}",\n        "{{userID_2}}"\n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.credentials.applyStagedChanges+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "revoke": [
    "{{userID}}",
    "{{userID_2}}"
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"revoke\": [\n        \"{{userID}}\",\n        \"{{userID_2}}\"\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules/{{credentialIssuanceRuleID}}/stagedChanges")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.credentials.applyStagedChanges+json", forHTTPHeaderField: "Content-Type")
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
    "revoked": [
        {
            "user": {
                "id": "1760140c-8e2b-4eaa-a335-a8d49760fed3"
            },
            "credential": {
                "id": "6d2c1417-a387-42c5-802e-3663f39baa4b"
            },
            "createdAt": "2023-03-01T20:40:04.094Z"
        },
        {
            "user": {
                "id": "2315958f-c910-42a4-b421-f11eaf146bc2"
            },
            "credential": {
                "id": "3eef9bc1-06d9-4c8b-b76e-91da4389fa79"
            },
            "createdAt": "2023-03-01T20:40:04.184Z"
        }
    ]
}
```

### Example Response

200 OK

```json
{
    "issued": [
        {
            "user": {
                "id": "10e01013-5c58-4eb1-8073-d814c274c6dd"
            },
            "credential": {
                "id": "0d6a032c-a5e7-471a-89a4-14ce5497b9ee"
            },
            "createdAt": "2023-06-01T20:20:07.495Z"
        }
    ],
    "errors": [
        {
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "credentialType": {
                "id": "ac39e146-622a-4956-b04e-44d6ea73114c"
            },
            "issuanceRule": {
                "id": "2efb66cc-67c5-4589-9c25-8d13b693a6ff"
            },
            "user": {
                "id": "1b7837ff-c8d2-42f9-94b4-acfa0aedcb61"
            },
            "action": "ISSUE",
            "scheduled": false,
            "errors": [
                {
                    "recordedAt": "2023-06-01T20:20:07.828Z",
                    "errorDetail": {
                        "code": "FILE_RESOLUTION_ERROR",
                        "target": "image",
                        "message": "File exceeds max file size restriction. File size: 29,638,516 bytes. Maximum size: 2,097,152 bytes."
                    }
                }
            ],
            "id": "35835133-af17-4770-8891-21e9bc7e6d9e",
            "createdAt": "2023-06-01T20:19:33.803Z",
            "updatedAt": "2023-06-01T20:20:07.828Z"
        }
    ]
}
```

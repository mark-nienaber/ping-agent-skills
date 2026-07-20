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

---

---
title: Create a User Credential
description: The POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials request creates a user credential from a managed credential type.
component: pingone-api
page_id: pingone-api:credentials:user-credentials/create-user-credential
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/user-credentials/create-user-credential.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create a User Credential

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials
```

The `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials` request creates a user credential from a managed credential type.

This request requires a `credentialType.id` with a `management.mode` of `MANAGED` in the body.

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users.html), especially [User operations](../../platform/users/users-1.html).

* [Create a credential type (managed)](../credential-types/create-credential-type-managed.html) to get a ``credentialType.id`with a `management.mode`` of `MANAGED` for the body.

> **Collapse: Request Model**
>
> Refer to [User Credentials data model](../user-credentials.html#user-credentials-data-model) for full property descriptions.
>
> | Property                           | Type      | Required          |
> | ---------------------------------- | --------- | ----------------- |
> | `credentialType.id`                | String    | Required          |
> | `data`                             | Object    | Optional          |
> | `data.<field>`                     | String    | Required/Optional |
> | `demoDataStorage`                  | Object    | Optional          |
> | `demoDataStorage.storeUntilIssued` | Boolean   | Optional          |
> | `expiresAt`                        | DateTime  | Optional          |
> | `notification`                     | Object    | Optional          |
> | `notification.template`            | Object    | Optional          |
> | `notification.template.locale`     | String    | Required          |
> | `notification.template.variant`    | String    | Required          |
> | `notification.template.variables`  | Object\[] | Required/Optional |

After receipt of this request, if the optional `notification` object is present, the credential service uses the `credential_issued` notification template to send notice of the issuance to the user via email or SMS text. The `notification.template` object can define a variant and locale for the notifications, if needed.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "credentialType": {
        "id": "{{credentialTypeID}}"
    },
    "demoDataStorage": {
        "storeUntilIssued": true
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "credentialType": {
        "id": "{{credentialTypeID}}"
    },
    "demoDataStorage": {
        "storeUntilIssued": true
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""credentialType"": {" + "\n" +
@"        ""id"": ""{{credentialTypeID}}""" + "\n" +
@"    }," + "\n" +
@"    ""demoDataStorage"": {" + "\n" +
@"        ""storeUntilIssued"": true" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials"
  method := "POST"

  payload := strings.NewReader(`{
    "credentialType": {
        "id": "{{credentialTypeID}}"
    },
    "demoDataStorage": {
        "storeUntilIssued": true
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
POST /v1/environments/{{envID}}/users/{{userID}}/credentials HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "credentialType": {
        "id": "{{credentialTypeID}}"
    },
    "demoDataStorage": {
        "storeUntilIssued": true
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"credentialType\": {\n        \"id\": \"{{credentialTypeID}}\"\n    },\n    \"demoDataStorage\": {\n        \"storeUntilIssued\": true\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "credentialType": {
      "id": "{{credentialTypeID}}"
    },
    "demoDataStorage": {
      "storeUntilIssued": true
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "credentialType": {
      "id": "{{credentialTypeID}}"
    },
    "demoDataStorage": {
      "storeUntilIssued": true
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials"

payload = json.dumps({
  "credentialType": {
    "id": "{{credentialTypeID}}"
  },
  "demoDataStorage": {
    "storeUntilIssued": True
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "credentialType": {\n        "id": "{{credentialTypeID}}"\n    },\n    "demoDataStorage": {\n        "storeUntilIssued": true\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "credentialType": {
    "id": "{{credentialTypeID}}"
  },
  "demoDataStorage": {
    "storeUntilIssued": true
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"credentialType\": {\n        \"id\": \"{{credentialTypeID}}\"\n    },\n    \"demoDataStorage\": {\n        \"storeUntilIssued\": true\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/credentials")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/23f1c64b-f8b6-48f6-b55d-b56924126df7/credentials/2d95ee85-5765-44e6-8f64-6baede8320b0"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/23f1c64b-f8b6-48f6-b55d-b56924126df7"
        },
        "credentialType": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialTypes/01fb0a05-4f45-431f-891e-2605f2e0a48f"
        },
        "credentialTypeVersion": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialTypes/01fb0a05-4f45-431f-891e-2605f2e0a48f/versions/9511cae5-b072-4c4c-bcb6-9200043781f6"
        }
    },
    "id": "2d95ee85-5765-44e6-8f64-6baede8320b0",
    "createdAt": "2026-06-09T15:40:08.609561124Z",
    "updatedAt": "2026-06-09T15:40:08.609562904Z",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "23f1c64b-f8b6-48f6-b55d-b56924126df7"
    },
    "credentialType": {
        "id": "01fb0a05-4f45-431f-891e-2605f2e0a48f",
        "version": {
            "number": 1,
            "uri": "https://api.pingone.com/v1/distributedid/credentialTypes/01fb0a05-4f45-431f-891e-2605f2e0a48f/v1",
            "id": "9511cae5-b072-4c4c-bcb6-9200043781f6"
        }
    },
    "demoDataStorage": {
        "storeUntilIssued": true,
        "hasData": true
    },
    "title": "Card Developers",
    "status": "PENDING"
}
```

---

---
title: Create Credential Issuance Rule
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules operation to create a credential issuance rule for the specified credential type in the specified environment.
component: pingone-api
page_id: pingone-api:credentials:credential-issuance-rules/create-credential-issuance-rule
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-issuance-rules/create-credential-issuance-rule.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Credential Issuance Rule

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules` operation to create a credential issuance rule for the specified credential type in the specified environment.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You cannot create an issuance rule for a credential type if that credential type has `management.mode` set to `MANAGED`. |

### Prerequisites

[Create a credential type (automated)](../credential-types/create-credential-type-automated.html) or [Create a credential type (managed)](../credential-types/create-credential-type-managed.html) to get a `credentialTypeId` for the endpoint. Refer also to [Credential Types](../credential-types.html).

> **Collapse: Request Model**
>
> Refer to [Credential Issuance Rules data model](../credential-issuance-rules.html#credential-issuance-rules-data-model) for full property descriptions.
>
> | Property                          | Type      | Required          |
> | --------------------------------- | --------- | ----------------- |
> | `automation`                      | Object    | Required          |
> | `automation.issue`                | String    | Required          |
> | `automation.revoke`               | String    | Required          |
> | `automation.update`               | String    | Required          |
> | `digitalWalletApplication.id`     | String    | Optional          |
> | `filter`                          | Object    | Optional          |
> | `filter.groupIds`                 | String\[] | Required/Optional |
> | `filter.populationIds`            | String\[] | Required/Optional |
> | `filter.scim`                     | String    | Required/Optional |
> | `notification`                    | Object    | Optional          |
> | `notification.template`           | Object    | Optional          |
> | `notification.template.locale`    | String    | Required          |
> | `notification.template.variant`   | String    | Required          |
> | `notification.template.variables` | Object\[] | Required/Optional |
> | `status`                          | String    | Required          |

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If `filter.groupIds` or `filter.populationIds` is used, a user can belong to any group or population in the array and the issuance rule applies to that user. |

When an action in `automation` is set to `PERIODIC` and the period arrives, the credential service uses a notification template appropriate to the action, `credential_issued`, `credential_updated`, or `credential_revoked`, to send notice of the action taken to the user via email or SMS text. The `notification.template` object can define a variant and locale for the notifications, if needed, and applies to actions initiated periodically and actions initiated by an [Apply Credential Issuance Rule Staged Changes](apply-credential-issuance-rule.html) request.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `notification.template` object applies a variant and locale to all three credential notification templates: `credential_issued`, `credential_updated`, and `credential_revoked`. When adding a variant or locale to any of the three notification templates, consider adding the same variant or locale to the other notification templates. If a matching variant is not defined, the default notification template is used. If a locale is not defined the notification template uses the user's preferred language or, if the user has no preferred language, the default language of the environment. |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "status": "ACTIVE",
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "filter": {
        "populationIds": [
            "{{popID}}"
        ]
    },
    "automation": {
        "issue": "PERIODIC",
        "update": "ON_DEMAND",
        "revoke": "ON_DEMAND"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "status": "ACTIVE",
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "filter": {
        "populationIds": [
            "{{popID}}"
        ]
    },
    "automation": {
        "issue": "PERIODIC",
        "update": "ON_DEMAND",
        "revoke": "ON_DEMAND"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""status"": ""ACTIVE""," + "\n" +
@"    ""digitalWalletApplication"": {" + "\n" +
@"        ""id"": ""{{digitalWalletApplicationID}}""" + "\n" +
@"    }," + "\n" +
@"    ""filter"": {" + "\n" +
@"        ""populationIds"": [" + "\n" +
@"            ""{{popID}}""" + "\n" +
@"        ]" + "\n" +
@"    }," + "\n" +
@"    ""automation"": {" + "\n" +
@"        ""issue"": ""PERIODIC""," + "\n" +
@"        ""update"": ""ON_DEMAND""," + "\n" +
@"        ""revoke"": ""ON_DEMAND""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules"
  method := "POST"

  payload := strings.NewReader(`{
    "status": "ACTIVE",
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "filter": {
        "populationIds": [
            "{{popID}}"
        ]
    },
    "automation": {
        "issue": "PERIODIC",
        "update": "ON_DEMAND",
        "revoke": "ON_DEMAND"
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
POST /v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "status": "ACTIVE",
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "filter": {
        "populationIds": [
            "{{popID}}"
        ]
    },
    "automation": {
        "issue": "PERIODIC",
        "update": "ON_DEMAND",
        "revoke": "ON_DEMAND"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"status\": \"ACTIVE\",\n    \"digitalWalletApplication\": {\n        \"id\": \"{{digitalWalletApplicationID}}\"\n    },\n    \"filter\": {\n        \"populationIds\": [\n            \"{{popID}}\"\n        ]\n    },\n    \"automation\": {\n        \"issue\": \"PERIODIC\",\n        \"update\": \"ON_DEMAND\",\n        \"revoke\": \"ON_DEMAND\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "status": "ACTIVE",
    "digitalWalletApplication": {
      "id": "{{digitalWalletApplicationID}}"
    },
    "filter": {
      "populationIds": [
        "{{popID}}"
      ]
    },
    "automation": {
      "issue": "PERIODIC",
      "update": "ON_DEMAND",
      "revoke": "ON_DEMAND"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "status": "ACTIVE",
    "digitalWalletApplication": {
      "id": "{{digitalWalletApplicationID}}"
    },
    "filter": {
      "populationIds": [
        "{{popID}}"
      ]
    },
    "automation": {
      "issue": "PERIODIC",
      "update": "ON_DEMAND",
      "revoke": "ON_DEMAND"
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

url = "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules"

payload = json.dumps({
  "status": "ACTIVE",
  "digitalWalletApplication": {
    "id": "{{digitalWalletApplicationID}}"
  },
  "filter": {
    "populationIds": [
      "{{popID}}"
    ]
  },
  "automation": {
    "issue": "PERIODIC",
    "update": "ON_DEMAND",
    "revoke": "ON_DEMAND"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "status": "ACTIVE",\n    "digitalWalletApplication": {\n        "id": "{{digitalWalletApplicationID}}"\n    },\n    "filter": {\n        "populationIds": [\n            "{{popID}}"\n        ]\n    },\n    "automation": {\n        "issue": "PERIODIC",\n        "update": "ON_DEMAND",\n        "revoke": "ON_DEMAND"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "status": "ACTIVE",
  "digitalWalletApplication": {
    "id": "{{digitalWalletApplicationID}}"
  },
  "filter": {
    "populationIds": [
      "{{popID}}"
    ]
  },
  "automation": {
    "issue": "PERIODIC",
    "update": "ON_DEMAND",
    "revoke": "ON_DEMAND"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"status\": \"ACTIVE\",\n    \"digitalWalletApplication\": {\n        \"id\": \"{{digitalWalletApplicationID}}\"\n    },\n    \"filter\": {\n        \"populationIds\": [\n            \"{{popID}}\"\n        ]\n    },\n    \"automation\": {\n        \"issue\": \"PERIODIC\",\n        \"update\": \"ON_DEMAND\",\n        \"revoke\": \"ON_DEMAND\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/credentialTypes/{{credentialTypeID}}/issuanceRules")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialTypes/8a3a6157-5fb9-40b7-96c0-909331858248/issuanceRules/7888a5ed-ae7b-482c-973d-afd27973099c"
        }
    },
    "id": "7888a5ed-ae7b-482c-973d-afd27973099c",
    "createdAt": "2023-03-01T20:29:51.912Z",
    "updatedAt": "2023-03-01T20:29:51.912Z",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "credentialType": {
        "id": "8a3a6157-5fb9-40b7-96c0-909331858248"
    },
    "status": "ACTIVE",
    "digitalWalletApplication": {
        "id": "6815c8a6-bc0b-4105-8f37-50f6c35583d7"
    },
    "filter": {
        "populationIds": [
            "e85091a0-ddca-422e-935e-d1faf139df3d"
        ]
    },
    "automation": {
        "issue": "PERIODIC",
        "update": "ON_DEMAND",
        "revoke": "ON_DEMAND"
    }
}
```

---

---
title: Create Credential Type (automated)
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes operation to create a new type of credential for issuance. A credential type corresponds to the Card type presented by the compatible wallet app.
component: pingone-api
page_id: pingone-api:credentials:credential-types/create-credential-type-automated
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-types/create-credential-type-automated.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Credential Type (automated)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes` operation to create a new type of credential for issuance. A credential type corresponds to the Card type presented by the compatible wallet app.

In this request, `management.mode` is `AUTOMATED`. Such credential types are only issued by its associated [credential issuance rule](../credential-issuance-rules.html). An `expiration` object can be used to set the date when the credential will expire.

### Prerequisites

Refer to [Credential Types](../credential-types.html) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Credential Types data model](../credential-types.html#credential-types-data-model) for full property descriptions.
>
> | Property                           | Type     | Required          |
> | ---------------------------------- | -------- | ----------------- |
> | `cardDesignTemplate` (deprecated)  | String   | Required          |
> | `cardType`                         | String   | Optional          |
> | `description`                      | String   | Optional          |
> | `expiration`                       | Object   | Optional          |
> | `expiration.after`                 | Object   | Required/Optional |
> | `expiration.after.duration`        | Integer  | Required          |
> | `expiration.after.timeUnit`        | String   | Required          |
> | `expiration.expression`            | String   | Required/Optional |
> | `expiration.fieldName`             | String   | Required/Optional |
> | `expiration.timestamp`             | DateTime | Required/Optional |
> | `expiration.type`                  | String   | Required          |
> | `issuerName`                       | String   | Optional          |
> | `management.mode`                  | String   | Optional          |
> | `metadata`                         | Object   | Required          |
> | `multiple`                         | Object   | Optional          |
> | `multiple.expression`              | String   | Required          |
> | `onDelete.revokeIssuedCredentials` | Boolean  | Optional          |
> | `openid4VCI`                       | Object   | Optional          |
> | `openid4VCI.enabled`               | Boolean  | Required          |
> | `openid4VCI.scope`                 | String   | Required          |
> | `title`                            | String   | Required          |
> | `version`                          | String   | Optional          |
>
> **metadata object data model**
>
> | Property                        | Type      | Required          |
> | ------------------------------- | --------- | ----------------- |
> | `backgroundImage`               | String    | Optional          |
> | `bgOpacityPercent`              | String    | Optional          |
> | `cardColor`                     | String    | Optional          |
> | `description`                   | String    | Optional          |
> | `fields`                        | Object\[] | Optional          |
> | `fields.attribute`              | String    | Required/Optional |
> | `fields.fileSupport`            | String    | Optional          |
> | `fields.id`                     | String    | Required          |
> | `fields.isVisible` (deprecated) | Boolean   | Required          |
> | `fields.required`               | Boolean   | Optional          |
> | `fields.title`                  | String    | Required          |
> | `fields.type`                   | String    | Required          |
> | `fields.values`                 | String\[] | Required/Optional |
> | `logoImage`                     | String    | Optional          |
> | `name`                          | String    | Optional          |
> | `textColor`                     | String    | Optional          |
> | `version`                       | String    | Optional          |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "title": "Title",
    "description": "Subtitle",
    "metadata": {
        "logoImage": "",
        "backgroundImage": "",
        "name": "Alphanumeric Text Example",
        "description": "Alphanumeric Text Attribute",
        "cardColor": "#9997bf",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Alphanumeric Text -> Account",
                "title": "Account",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Name",
                "title": "Name",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Number",
                "title": "Number",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            }
        ],
        "textColor": "#253746",
        "version": 4
    },
    "expiration": {
        "type": "HARD",
        "after": {
            "duration": 1826,
            "timeUnit": "DAYS"
        }
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData" : {
        "showTitle" : true,
        "displayFields" : [
            {
                "dataFieldName" : "Account",
                "showFieldName": false
            },
            {
                "dataFieldName" : "Name",
                "showFieldName": false
            }
        ]
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/credentialTypes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "title": "Title",
    "description": "Subtitle",
    "metadata": {
        "logoImage": "",
        "backgroundImage": "",
        "name": "Alphanumeric Text Example",
        "description": "Alphanumeric Text Attribute",
        "cardColor": "#9997bf",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Alphanumeric Text -> Account",
                "title": "Account",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Name",
                "title": "Name",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Number",
                "title": "Number",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            }
        ],
        "textColor": "#253746",
        "version": 4
    },
    "expiration": {
        "type": "HARD",
        "after": {
            "duration": 1826,
            "timeUnit": "DAYS"
        }
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData" : {
        "showTitle" : true,
        "displayFields" : [
            {
                "dataFieldName" : "Account",
                "showFieldName": false
            },
            {
                "dataFieldName" : "Name",
                "showFieldName": false
            }
        ]
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/credentialTypes")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""title"": ""Title""," + "\n" +
@"    ""description"": ""Subtitle""," + "\n" +
@"    ""metadata"": {" + "\n" +
@"        ""logoImage"": """"," + "\n" +
@"        ""backgroundImage"": """"," + "\n" +
@"        ""name"": ""Alphanumeric Text Example""," + "\n" +
@"        ""description"": ""Alphanumeric Text Attribute""," + "\n" +
@"        ""cardColor"": ""#9997bf""," + "\n" +
@"        ""bgOpacityPercent"": 20," + "\n" +
@"        ""fields"": [" + "\n" +
@"            {" + "\n" +
@"                ""id"": ""Alphanumeric Text -> Account""," + "\n" +
@"                ""title"": ""Account""," + "\n" +
@"                ""isVisible"": true," + "\n" +
@"                ""required"" : true," + "\n" +
@"                ""type"": ""Alphanumeric Text""," + "\n" +
@"                ""value"": ""Value""" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""id"": ""Alphanumeric Text -> Name""," + "\n" +
@"                ""title"": ""Name""," + "\n" +
@"                ""isVisible"": true," + "\n" +
@"                ""required"" : true," + "\n" +
@"                ""type"": ""Alphanumeric Text""," + "\n" +
@"                ""value"": ""Value""" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""id"": ""Alphanumeric Text -> Number""," + "\n" +
@"                ""title"": ""Number""," + "\n" +
@"                ""isVisible"": true," + "\n" +
@"                ""required"" : true," + "\n" +
@"                ""type"": ""Alphanumeric Text""," + "\n" +
@"                ""value"": ""Value""" + "\n" +
@"            }" + "\n" +
@"        ]," + "\n" +
@"        ""textColor"": ""#253746""," + "\n" +
@"        ""version"": 4" + "\n" +
@"    }," + "\n" +
@"    ""expiration"": {" + "\n" +
@"        ""type"": ""HARD""," + "\n" +
@"        ""after"": {" + "\n" +
@"            ""duration"": 1826," + "\n" +
@"            ""timeUnit"": ""DAYS""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""openid4VCI"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""scope"": ""p1:provision:credentials""" + "\n" +
@"    }," + "\n" +
@"    ""visualizationTemplateData"" : {" + "\n" +
@"        ""showTitle"" : true," + "\n" +
@"        ""displayFields"" : [" + "\n" +
@"            { " + "\n" +
@"                ""dataFieldName"" : ""Account""," + "\n" +
@"                ""showFieldName"": false" + "\n" +
@"            }," + "\n" +
@"            { " + "\n" +
@"                ""dataFieldName"" : ""Name""," + "\n" +
@"                ""showFieldName"": false" + "\n" +
@"            }" + "\n" +
@"        ]" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/credentialTypes"
  method := "POST"

  payload := strings.NewReader(`{
    "title": "Title",
    "description": "Subtitle",
    "metadata": {
        "logoImage": "",
        "backgroundImage": "",
        "name": "Alphanumeric Text Example",
        "description": "Alphanumeric Text Attribute",
        "cardColor": "#9997bf",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Alphanumeric Text -> Account",
                "title": "Account",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Name",
                "title": "Name",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Number",
                "title": "Number",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            }
        ],
        "textColor": "#253746",
        "version": 4
    },
    "expiration": {
        "type": "HARD",
        "after": {
            "duration": 1826,
            "timeUnit": "DAYS"
        }
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData" : {
        "showTitle" : true,
        "displayFields" : [
            {
                "dataFieldName" : "Account",
                "showFieldName": false
            },
            {
                "dataFieldName" : "Name",
                "showFieldName": false
            }
        ]
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
POST /v1/environments/{{envID}}/credentialTypes HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "title": "Title",
    "description": "Subtitle",
    "metadata": {
        "logoImage": "",
        "backgroundImage": "",
        "name": "Alphanumeric Text Example",
        "description": "Alphanumeric Text Attribute",
        "cardColor": "#9997bf",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Alphanumeric Text -> Account",
                "title": "Account",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Name",
                "title": "Name",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            },
            {
                "id": "Alphanumeric Text -> Number",
                "title": "Number",
                "isVisible": true,
                "required" : true,
                "type": "Alphanumeric Text",
                "value": "Value"
            }
        ],
        "textColor": "#253746",
        "version": 4
    },
    "expiration": {
        "type": "HARD",
        "after": {
            "duration": 1826,
            "timeUnit": "DAYS"
        }
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData" : {
        "showTitle" : true,
        "displayFields" : [
            {
                "dataFieldName" : "Account",
                "showFieldName": false
            },
            {
                "dataFieldName" : "Name",
                "showFieldName": false
            }
        ]
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"title\": \"Title\",\n    \"description\": \"Subtitle\",\n    \"metadata\": {\n        \"logoImage\": \"\",\n        \"backgroundImage\": \"\",\n        \"name\": \"Alphanumeric Text Example\",\n        \"description\": \"Alphanumeric Text Attribute\",\n        \"cardColor\": \"#9997bf\",\n        \"bgOpacityPercent\": 20,\n        \"fields\": [\n            {\n                \"id\": \"Alphanumeric Text -> Account\",\n                \"title\": \"Account\",\n                \"isVisible\": true,\n                \"required\" : true,\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"Value\"\n            },\n            {\n                \"id\": \"Alphanumeric Text -> Name\",\n                \"title\": \"Name\",\n                \"isVisible\": true,\n                \"required\" : true,\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"Value\"\n            },\n            {\n                \"id\": \"Alphanumeric Text -> Number\",\n                \"title\": \"Number\",\n                \"isVisible\": true,\n                \"required\" : true,\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"Value\"\n            }\n        ],\n        \"textColor\": \"#253746\",\n        \"version\": 4\n    },\n    \"expiration\": {\n        \"type\": \"HARD\",\n        \"after\": {\n            \"duration\": 1826,\n            \"timeUnit\": \"DAYS\"\n        }\n    },\n    \"openid4VCI\": {\n        \"enabled\": true,\n        \"scope\": \"p1:provision:credentials\"\n    },\n    \"visualizationTemplateData\" : {\n        \"showTitle\" : true,\n        \"displayFields\" : [\n            { \n                \"dataFieldName\" : \"Account\",\n                \"showFieldName\": false\n            },\n            { \n                \"dataFieldName\" : \"Name\",\n                \"showFieldName\": false\n            }\n        ]\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/credentialTypes")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/credentialTypes",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "title": "Title",
    "description": "Subtitle",
    "metadata": {
      "logoImage": "",
      "backgroundImage": "",
      "name": "Alphanumeric Text Example",
      "description": "Alphanumeric Text Attribute",
      "cardColor": "#9997bf",
      "bgOpacityPercent": 20,
      "fields": [
        {
          "id": "Alphanumeric Text -> Account",
          "title": "Account",
          "isVisible": true,
          "required": true,
          "type": "Alphanumeric Text",
          "value": "Value"
        },
        {
          "id": "Alphanumeric Text -> Name",
          "title": "Name",
          "isVisible": true,
          "required": true,
          "type": "Alphanumeric Text",
          "value": "Value"
        },
        {
          "id": "Alphanumeric Text -> Number",
          "title": "Number",
          "isVisible": true,
          "required": true,
          "type": "Alphanumeric Text",
          "value": "Value"
        }
      ],
      "textColor": "#253746",
      "version": 4
    },
    "expiration": {
      "type": "HARD",
      "after": {
        "duration": 1826,
        "timeUnit": "DAYS"
      }
    },
    "openid4VCI": {
      "enabled": true,
      "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
      "showTitle": true,
      "displayFields": [
        {
          "dataFieldName": "Account",
          "showFieldName": false
        },
        {
          "dataFieldName": "Name",
          "showFieldName": false
        }
      ]
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/credentialTypes',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "title": "Title",
    "description": "Subtitle",
    "metadata": {
      "logoImage": "",
      "backgroundImage": "",
      "name": "Alphanumeric Text Example",
      "description": "Alphanumeric Text Attribute",
      "cardColor": "#9997bf",
      "bgOpacityPercent": 20,
      "fields": [
        {
          "id": "Alphanumeric Text -> Account",
          "title": "Account",
          "isVisible": true,
          "required": true,
          "type": "Alphanumeric Text",
          "value": "Value"
        },
        {
          "id": "Alphanumeric Text -> Name",
          "title": "Name",
          "isVisible": true,
          "required": true,
          "type": "Alphanumeric Text",
          "value": "Value"
        },
        {
          "id": "Alphanumeric Text -> Number",
          "title": "Number",
          "isVisible": true,
          "required": true,
          "type": "Alphanumeric Text",
          "value": "Value"
        }
      ],
      "textColor": "#253746",
      "version": 4
    },
    "expiration": {
      "type": "HARD",
      "after": {
        "duration": 1826,
        "timeUnit": "DAYS"
      }
    },
    "openid4VCI": {
      "enabled": true,
      "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
      "showTitle": true,
      "displayFields": [
        {
          "dataFieldName": "Account",
          "showFieldName": false
        },
        {
          "dataFieldName": "Name",
          "showFieldName": false
        }
      ]
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

url = "{{apiPath}}/v1/environments/{{envID}}/credentialTypes"

payload = json.dumps({
  "title": "Title",
  "description": "Subtitle",
  "metadata": {
    "logoImage": "",
    "backgroundImage": "",
    "name": "Alphanumeric Text Example",
    "description": "Alphanumeric Text Attribute",
    "cardColor": "#9997bf",
    "bgOpacityPercent": 20,
    "fields": [
      {
        "id": "Alphanumeric Text -> Account",
        "title": "Account",
        "isVisible": True,
        "required": True,
        "type": "Alphanumeric Text",
        "value": "Value"
      },
      {
        "id": "Alphanumeric Text -> Name",
        "title": "Name",
        "isVisible": True,
        "required": True,
        "type": "Alphanumeric Text",
        "value": "Value"
      },
      {
        "id": "Alphanumeric Text -> Number",
        "title": "Number",
        "isVisible": True,
        "required": True,
        "type": "Alphanumeric Text",
        "value": "Value"
      }
    ],
    "textColor": "#253746",
    "version": 4
  },
  "expiration": {
    "type": "HARD",
    "after": {
      "duration": 1826,
      "timeUnit": "DAYS"
    }
  },
  "openid4VCI": {
    "enabled": True,
    "scope": "p1:provision:credentials"
  },
  "visualizationTemplateData": {
    "showTitle": True,
    "displayFields": [
      {
        "dataFieldName": "Account",
        "showFieldName": False
      },
      {
        "dataFieldName": "Name",
        "showFieldName": False
      }
    ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/credentialTypes');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "title": "Title",\n    "description": "Subtitle",\n    "metadata": {\n        "logoImage": "",\n        "backgroundImage": "",\n        "name": "Alphanumeric Text Example",\n        "description": "Alphanumeric Text Attribute",\n        "cardColor": "#9997bf",\n        "bgOpacityPercent": 20,\n        "fields": [\n            {\n                "id": "Alphanumeric Text -> Account",\n                "title": "Account",\n                "isVisible": true,\n                "required" : true,\n                "type": "Alphanumeric Text",\n                "value": "Value"\n            },\n            {\n                "id": "Alphanumeric Text -> Name",\n                "title": "Name",\n                "isVisible": true,\n                "required" : true,\n                "type": "Alphanumeric Text",\n                "value": "Value"\n            },\n            {\n                "id": "Alphanumeric Text -> Number",\n                "title": "Number",\n                "isVisible": true,\n                "required" : true,\n                "type": "Alphanumeric Text",\n                "value": "Value"\n            }\n        ],\n        "textColor": "#253746",\n        "version": 4\n    },\n    "expiration": {\n        "type": "HARD",\n        "after": {\n            "duration": 1826,\n            "timeUnit": "DAYS"\n        }\n    },\n    "openid4VCI": {\n        "enabled": true,\n        "scope": "p1:provision:credentials"\n    },\n    "visualizationTemplateData" : {\n        "showTitle" : true,\n        "displayFields" : [\n            { \n                "dataFieldName" : "Account",\n                "showFieldName": false\n            },\n            { \n                "dataFieldName" : "Name",\n                "showFieldName": false\n            }\n        ]\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/credentialTypes")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "title": "Title",
  "description": "Subtitle",
  "metadata": {
    "logoImage": "",
    "backgroundImage": "",
    "name": "Alphanumeric Text Example",
    "description": "Alphanumeric Text Attribute",
    "cardColor": "\#9997bf",
    "bgOpacityPercent": 20,
    "fields": [
      {
        "id": "Alphanumeric Text -> Account",
        "title": "Account",
        "isVisible": true,
        "required": true,
        "type": "Alphanumeric Text",
        "value": "Value"
      },
      {
        "id": "Alphanumeric Text -> Name",
        "title": "Name",
        "isVisible": true,
        "required": true,
        "type": "Alphanumeric Text",
        "value": "Value"
      },
      {
        "id": "Alphanumeric Text -> Number",
        "title": "Number",
        "isVisible": true,
        "required": true,
        "type": "Alphanumeric Text",
        "value": "Value"
      }
    ],
    "textColor": "\#253746",
    "version": 4
  },
  "expiration": {
    "type": "HARD",
    "after": {
      "duration": 1826,
      "timeUnit": "DAYS"
    }
  },
  "openid4VCI": {
    "enabled": true,
    "scope": "p1:provision:credentials"
  },
  "visualizationTemplateData": {
    "showTitle": true,
    "displayFields": [
      {
        "dataFieldName": "Account",
        "showFieldName": false
      },
      {
        "dataFieldName": "Name",
        "showFieldName": false
      }
    ]
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"title\": \"Title\",\n    \"description\": \"Subtitle\",\n    \"metadata\": {\n        \"logoImage\": \"\",\n        \"backgroundImage\": \"\",\n        \"name\": \"Alphanumeric Text Example\",\n        \"description\": \"Alphanumeric Text Attribute\",\n        \"cardColor\": \"#9997bf\",\n        \"bgOpacityPercent\": 20,\n        \"fields\": [\n            {\n                \"id\": \"Alphanumeric Text -> Account\",\n                \"title\": \"Account\",\n                \"isVisible\": true,\n                \"required\" : true,\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"Value\"\n            },\n            {\n                \"id\": \"Alphanumeric Text -> Name\",\n                \"title\": \"Name\",\n                \"isVisible\": true,\n                \"required\" : true,\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"Value\"\n            },\n            {\n                \"id\": \"Alphanumeric Text -> Number\",\n                \"title\": \"Number\",\n                \"isVisible\": true,\n                \"required\" : true,\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"Value\"\n            }\n        ],\n        \"textColor\": \"#253746\",\n        \"version\": 4\n    },\n    \"expiration\": {\n        \"type\": \"HARD\",\n        \"after\": {\n            \"duration\": 1826,\n            \"timeUnit\": \"DAYS\"\n        }\n    },\n    \"openid4VCI\": {\n        \"enabled\": true,\n        \"scope\": \"p1:provision:credentials\"\n    },\n    \"visualizationTemplateData\" : {\n        \"showTitle\" : true,\n        \"displayFields\" : [\n            { \n                \"dataFieldName\" : \"Account\",\n                \"showFieldName\": false\n            },\n            { \n                \"dataFieldName\" : \"Name\",\n                \"showFieldName\": false\n            }\n        ]\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/credentialTypes")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialTypes/6d031a6d-ca39-40a5-bd51-098db3774082"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "credentialIssuerProfile": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialIssuerProfile"
        },
        "issuanceRules": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialTypes/6d031a6d-ca39-40a5-bd51-098db3774082/issuanceRules"
        }
    },
    "id": "6d031a6d-ca39-40a5-bd51-098db3774082",
    "createdAt": "2025-02-28T20:46:59.406852884Z",
    "updatedAt": "2025-02-28T20:46:59.406852884Z",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "issuer": {
        "id": "824c722c-254a-4b2d-9b50-17e2abdf5f8a"
    },
    "management": {
        "mode": "AUTOMATED"
    },
    "title": "Title",
    "description": "Subtitle",
    "cardType": "Title",
    "uri": "https://api.pingone.com/v1/distributedid/credentialTypes/6d031a6d-ca39-40a5-bd51-098db3774082",
    "version": {
        "number": 1,
        "uri": "https://api.pingone.com/v1/distributedid/credentialTypes/6d031a6d-ca39-40a5-bd51-098db3774082/v1",
        "id": "76fecf21-313a-49d4-b4d5-ec17281bdd20"
    },
    "metadata": {
        "name": "Alphanumeric Text Example",
        "description": "Alphanumeric Text Attribute",
        "textColor": "#253746",
        "cardColor": "#9997bf",
        "backgroundImage": "",
        "logoImage": "",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Alphanumeric Text -> Account",
                "title": "Account",
                "isVisible": true,
                "type": "Alphanumeric Text",
                "value": "Value",
                "required": true
            },
            {
                "id": "Alphanumeric Text -> Name",
                "title": "Name",
                "isVisible": true,
                "type": "Alphanumeric Text",
                "value": "Value",
                "required": true
            },
            {
                "id": "Alphanumeric Text -> Number",
                "title": "Number",
                "isVisible": true,
                "type": "Alphanumeric Text",
                "value": "Value",
                "required": true
            }
        ],
        "version": 4
    },
    "onDelete": {
        "revokeIssuedCredentials": true
    },
    "expiration": {
        "type": "HARD",
        "after": {
            "duration": 1826,
            "timeUnit": "DAYS"
        }
    },
    "visualizationTemplateData": {
        "showTitle": true,
        "displayFields": [
            {
                "showFieldName": false,
                "dataFieldName": "Account"
            },
            {
                "showFieldName": false,
                "dataFieldName": "Name"
            }
        ]
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    }
}
```

---

---
title: Create Credential Type (managed)
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes operation to create a new type of credential for issuance. A credential type corresponds to the Card type presented by the compatible wallet app.
component: pingone-api
page_id: pingone-api:credentials:credential-types/create-credential-type-managed
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-types/create-credential-type-managed.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Credential Type (managed)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/credentialTypes` operation to create a new type of credential for issuance. A credential type corresponds to the Card type presented by the compatible wallet app.

In this request, `management.mode` is `MANAGED`. Such credential types are only issued by [Create a User Credential](../user-credentials/create-user-credential.html) or [Update a User Credential](../user-credentials/update-a-user-credential.html) API requests. An `expiration` object cannot be used to set the date when the credential will expire. Instead, you must use [Create a User Credential](../user-credentials/create-user-credential.html) or [Update a User Credential](../user-credentials/update-a-user-credential.html) to set `expiresAt` to a specific date in ISO 8601 YYYY-MM-DDTHH:MM:SS.sssZ format (milliseconds optional) on the user's credential.

### Prerequisites

* Refer to [Credential Types](../credential-types.html) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Credential Types data model](../credential-types.html#credential-types-data-model) for full property descriptions.
>
> | Property                           | Type     | Required          |
> | ---------------------------------- | -------- | ----------------- |
> | `cardDesignTemplate` (deprecated)  | String   | Required          |
> | `cardType`                         | String   | Optional          |
> | `description`                      | String   | Optional          |
> | `expiration`                       | Object   | Optional          |
> | `expiration.after`                 | Object   | Required/Optional |
> | `expiration.after.duration`        | Integer  | Required          |
> | `expiration.after.timeUnit`        | String   | Required          |
> | `expiration.expression`            | String   | Required/Optional |
> | `expiration.fieldName`             | String   | Required/Optional |
> | `expiration.timestamp`             | DateTime | Required/Optional |
> | `expiration.type`                  | String   | Required          |
> | `issuerName`                       | String   | Optional          |
> | `management.mode`                  | String   | Optional          |
> | `metadata`                         | Object   | Required          |
> | `multiple`                         | Object   | Optional          |
> | `multiple.expression`              | String   | Required          |
> | `onDelete.revokeIssuedCredentials` | Boolean  | Optional          |
> | `openid4VCI`                       | Object   | Optional          |
> | `openid4VCI.enabled`               | Boolean  | Required          |
> | `openid4VCI.scope`                 | String   | Required          |
> | `title`                            | String   | Required          |
> | `version`                          | String   | Optional          |
>
> **metadata object data model**
>
> | Property                        | Type      | Required          |
> | ------------------------------- | --------- | ----------------- |
> | `backgroundImage`               | String    | Optional          |
> | `bgOpacityPercent`              | String    | Optional          |
> | `cardColor`                     | String    | Optional          |
> | `description`                   | String    | Optional          |
> | `fields`                        | Object\[] | Optional          |
> | `fields.attribute`              | String    | Required/Optional |
> | `fields.fileSupport`            | String    | Optional          |
> | `fields.id`                     | String    | Required          |
> | `fields.isVisible` (deprecated) | Boolean   | Required          |
> | `fields.required`               | Boolean   | Optional          |
> | `fields.title`                  | String    | Required          |
> | `fields.type`                   | String    | Required          |
> | `fields.values`                 | String\[] | Required/Optional |
> | `logoImage`                     | String    | Optional          |
> | `name`                          | String    | Optional          |
> | `textColor`                     | String    | Optional          |
> | `version`                       | String    | Optional          |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "title": "Card Developers",
    "description": "Card Developers Employee Credentials",
    "management": {
        "mode": "MANAGED"
    },
    "cardType": "Card Developers",
    "metadata": {
        "name": "Card Developers Employee Credentials",
        "description": "Card Developers Employee Credentials",
        "textColor": "#000000",
        "cardColor": "#FFFFFF",
        "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
        "logoImage": "",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Directory Attribute -> Name",
                "title": "Name",
                "type": "Directory Attribute",
                "attribute": "name.formatted",
                "required": true
            },
            {
                "id": "Directory Attribute -> Address",
                "title": "Address",
                "type": "Directory Attribute",
                "attribute": "address",
                "required": true
            },
            {
                "id": "Directory Attribute -> ID",
                "title": "User ID",
                "type": "Directory Attribute",
                "attribute": "id",
                "required": true
            },
            {
                "id": "Alphanumeric Text -> Clearance",
                "title": "Clearance",
                "type": "Alphanumeric Text",
                "value": "None",
                "required": true
            }
        ],
        "version": 1
    },
    "onDelete": {
        "revokeIssuedCredentials": true
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
        "displayFields": [
            {
                "dataFieldName": "Name",
                "showFieldName": true
            },
            {
                "dataFieldName": "User ID",
                "showFieldName": true
            }
        ]
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/credentialTypes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "title": "Card Developers",
    "description": "Card Developers Employee Credentials",
    "management": {
        "mode": "MANAGED"
    },
    "cardType": "Card Developers",
    "metadata": {
        "name": "Card Developers Employee Credentials",
        "description": "Card Developers Employee Credentials",
        "textColor": "#000000",
        "cardColor": "#FFFFFF",
        "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
        "logoImage": "",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Directory Attribute -> Name",
                "title": "Name",
                "type": "Directory Attribute",
                "attribute": "name.formatted",
                "required": true
            },
            {
                "id": "Directory Attribute -> Address",
                "title": "Address",
                "type": "Directory Attribute",
                "attribute": "address",
                "required": true
            },
            {
                "id": "Directory Attribute -> ID",
                "title": "User ID",
                "type": "Directory Attribute",
                "attribute": "id",
                "required": true
            },
            {
                "id": "Alphanumeric Text -> Clearance",
                "title": "Clearance",
                "type": "Alphanumeric Text",
                "value": "None",
                "required": true
            }
        ],
        "version": 1
    },
    "onDelete": {
        "revokeIssuedCredentials": true
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
        "displayFields": [
            {
                "dataFieldName": "Name",
                "showFieldName": true
            },
            {
                "dataFieldName": "User ID",
                "showFieldName": true
            }
        ]
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/credentialTypes")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""title"": ""Card Developers""," + "\n" +
@"    ""description"": ""Card Developers Employee Credentials""," + "\n" +
@"    ""management"": {" + "\n" +
@"        ""mode"": ""MANAGED""" + "\n" +
@"    }," + "\n" +
@"    ""cardType"": ""Card Developers""," + "\n" +
@"    ""metadata"": {" + "\n" +
@"        ""name"": ""Card Developers Employee Credentials""," + "\n" +
@"        ""description"": ""Card Developers Employee Credentials""," + "\n" +
@"        ""textColor"": ""#000000""," + "\n" +
@"        ""cardColor"": ""#FFFFFF""," + "\n" +
@"        ""backgroundImage"": ""data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==""," + "\n" +
@"        ""logoImage"": """"," + "\n" +
@"        ""bgOpacityPercent"": 20," + "\n" +
@"        ""fields"": [" + "\n" +
@"            {" + "\n" +
@"                ""id"": ""Directory Attribute -> Name""," + "\n" +
@"                ""title"": ""Name""," + "\n" +
@"                ""type"": ""Directory Attribute""," + "\n" +
@"                ""attribute"": ""name.formatted""," + "\n" +
@"                ""required"": true" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""id"": ""Directory Attribute -> Address""," + "\n" +
@"                ""title"": ""Address""," + "\n" +
@"                ""type"": ""Directory Attribute""," + "\n" +
@"                ""attribute"": ""address""," + "\n" +
@"                ""required"": true" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""id"": ""Directory Attribute -> ID""," + "\n" +
@"                ""title"": ""User ID""," + "\n" +
@"                ""type"": ""Directory Attribute""," + "\n" +
@"                ""attribute"": ""id""," + "\n" +
@"                ""required"": true" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""id"": ""Alphanumeric Text -> Clearance""," + "\n" +
@"                ""title"": ""Clearance""," + "\n" +
@"                ""type"": ""Alphanumeric Text""," + "\n" +
@"                ""value"": ""None""," + "\n" +
@"                ""required"": true" + "\n" +
@"            }" + "\n" +
@"        ]," + "\n" +
@"        ""version"": 1" + "\n" +
@"    }," + "\n" +
@"    ""onDelete"": {" + "\n" +
@"        ""revokeIssuedCredentials"": true" + "\n" +
@"    }," + "\n" +
@"    ""openid4VCI"": {" + "\n" +
@"        ""enabled"": true," + "\n" +
@"        ""scope"": ""p1:provision:credentials""" + "\n" +
@"    }," + "\n" +
@"    ""visualizationTemplateData"": {" + "\n" +
@"        ""displayFields"": [" + "\n" +
@"            {" + "\n" +
@"                ""dataFieldName"": ""Name""," + "\n" +
@"                ""showFieldName"": true" + "\n" +
@"            }," + "\n" +
@"            {" + "\n" +
@"                ""dataFieldName"": ""User ID""," + "\n" +
@"                ""showFieldName"": true" + "\n" +
@"            }" + "\n" +
@"        ]" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/credentialTypes"
  method := "POST"

  payload := strings.NewReader(`{
    "title": "Card Developers",
    "description": "Card Developers Employee Credentials",
    "management": {
        "mode": "MANAGED"
    },
    "cardType": "Card Developers",
    "metadata": {
        "name": "Card Developers Employee Credentials",
        "description": "Card Developers Employee Credentials",
        "textColor": "#000000",
        "cardColor": "#FFFFFF",
        "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
        "logoImage": "",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Directory Attribute -> Name",
                "title": "Name",
                "type": "Directory Attribute",
                "attribute": "name.formatted",
                "required": true
            },
            {
                "id": "Directory Attribute -> Address",
                "title": "Address",
                "type": "Directory Attribute",
                "attribute": "address",
                "required": true
            },
            {
                "id": "Directory Attribute -> ID",
                "title": "User ID",
                "type": "Directory Attribute",
                "attribute": "id",
                "required": true
            },
            {
                "id": "Alphanumeric Text -> Clearance",
                "title": "Clearance",
                "type": "Alphanumeric Text",
                "value": "None",
                "required": true
            }
        ],
        "version": 1
    },
    "onDelete": {
        "revokeIssuedCredentials": true
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
        "displayFields": [
            {
                "dataFieldName": "Name",
                "showFieldName": true
            },
            {
                "dataFieldName": "User ID",
                "showFieldName": true
            }
        ]
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
POST /v1/environments/{{envID}}/credentialTypes HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "title": "Card Developers",
    "description": "Card Developers Employee Credentials",
    "management": {
        "mode": "MANAGED"
    },
    "cardType": "Card Developers",
    "metadata": {
        "name": "Card Developers Employee Credentials",
        "description": "Card Developers Employee Credentials",
        "textColor": "#000000",
        "cardColor": "#FFFFFF",
        "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
        "logoImage": "",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Directory Attribute -> Name",
                "title": "Name",
                "type": "Directory Attribute",
                "attribute": "name.formatted",
                "required": true
            },
            {
                "id": "Directory Attribute -> Address",
                "title": "Address",
                "type": "Directory Attribute",
                "attribute": "address",
                "required": true
            },
            {
                "id": "Directory Attribute -> ID",
                "title": "User ID",
                "type": "Directory Attribute",
                "attribute": "id",
                "required": true
            },
            {
                "id": "Alphanumeric Text -> Clearance",
                "title": "Clearance",
                "type": "Alphanumeric Text",
                "value": "None",
                "required": true
            }
        ],
        "version": 1
    },
    "onDelete": {
        "revokeIssuedCredentials": true
    },
    "openid4VCI": {
        "enabled": true,
        "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
        "displayFields": [
            {
                "dataFieldName": "Name",
                "showFieldName": true
            },
            {
                "dataFieldName": "User ID",
                "showFieldName": true
            }
        ]
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"title\": \"Card Developers\",\n    \"description\": \"Card Developers Employee Credentials\",\n    \"management\": {\n        \"mode\": \"MANAGED\"\n    },\n    \"cardType\": \"Card Developers\",\n    \"metadata\": {\n        \"name\": \"Card Developers Employee Credentials\",\n        \"description\": \"Card Developers Employee Credentials\",\n        \"textColor\": \"#000000\",\n        \"cardColor\": \"#FFFFFF\",\n        \"backgroundImage\": \"data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==\",\n        \"logoImage\": \"\",\n        \"bgOpacityPercent\": 20,\n        \"fields\": [\n            {\n                \"id\": \"Directory Attribute -> Name\",\n                \"title\": \"Name\",\n                \"type\": \"Directory Attribute\",\n                \"attribute\": \"name.formatted\",\n                \"required\": true\n            },\n            {\n                \"id\": \"Directory Attribute -> Address\",\n                \"title\": \"Address\",\n                \"type\": \"Directory Attribute\",\n                \"attribute\": \"address\",\n                \"required\": true\n            },\n            {\n                \"id\": \"Directory Attribute -> ID\",\n                \"title\": \"User ID\",\n                \"type\": \"Directory Attribute\",\n                \"attribute\": \"id\",\n                \"required\": true\n            },\n            {\n                \"id\": \"Alphanumeric Text -> Clearance\",\n                \"title\": \"Clearance\",\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"None\",\n                \"required\": true\n            }\n        ],\n        \"version\": 1\n    },\n    \"onDelete\": {\n        \"revokeIssuedCredentials\": true\n    },\n    \"openid4VCI\": {\n        \"enabled\": true,\n        \"scope\": \"p1:provision:credentials\"\n    },\n    \"visualizationTemplateData\": {\n        \"displayFields\": [\n            {\n                \"dataFieldName\": \"Name\",\n                \"showFieldName\": true\n            },\n            {\n                \"dataFieldName\": \"User ID\",\n                \"showFieldName\": true\n            }\n        ]\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/credentialTypes")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/credentialTypes",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "title": "Card Developers",
    "description": "Card Developers Employee Credentials",
    "management": {
      "mode": "MANAGED"
    },
    "cardType": "Card Developers",
    "metadata": {
      "name": "Card Developers Employee Credentials",
      "description": "Card Developers Employee Credentials",
      "textColor": "#000000",
      "cardColor": "#FFFFFF",
      "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
      "logoImage": "",
      "bgOpacityPercent": 20,
      "fields": [
        {
          "id": "Directory Attribute -> Name",
          "title": "Name",
          "type": "Directory Attribute",
          "attribute": "name.formatted",
          "required": true
        },
        {
          "id": "Directory Attribute -> Address",
          "title": "Address",
          "type": "Directory Attribute",
          "attribute": "address",
          "required": true
        },
        {
          "id": "Directory Attribute -> ID",
          "title": "User ID",
          "type": "Directory Attribute",
          "attribute": "id",
          "required": true
        },
        {
          "id": "Alphanumeric Text -> Clearance",
          "title": "Clearance",
          "type": "Alphanumeric Text",
          "value": "None",
          "required": true
        }
      ],
      "version": 1
    },
    "onDelete": {
      "revokeIssuedCredentials": true
    },
    "openid4VCI": {
      "enabled": true,
      "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
      "displayFields": [
        {
          "dataFieldName": "Name",
          "showFieldName": true
        },
        {
          "dataFieldName": "User ID",
          "showFieldName": true
        }
      ]
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/credentialTypes',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "title": "Card Developers",
    "description": "Card Developers Employee Credentials",
    "management": {
      "mode": "MANAGED"
    },
    "cardType": "Card Developers",
    "metadata": {
      "name": "Card Developers Employee Credentials",
      "description": "Card Developers Employee Credentials",
      "textColor": "#000000",
      "cardColor": "#FFFFFF",
      "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
      "logoImage": "",
      "bgOpacityPercent": 20,
      "fields": [
        {
          "id": "Directory Attribute -> Name",
          "title": "Name",
          "type": "Directory Attribute",
          "attribute": "name.formatted",
          "required": true
        },
        {
          "id": "Directory Attribute -> Address",
          "title": "Address",
          "type": "Directory Attribute",
          "attribute": "address",
          "required": true
        },
        {
          "id": "Directory Attribute -> ID",
          "title": "User ID",
          "type": "Directory Attribute",
          "attribute": "id",
          "required": true
        },
        {
          "id": "Alphanumeric Text -> Clearance",
          "title": "Clearance",
          "type": "Alphanumeric Text",
          "value": "None",
          "required": true
        }
      ],
      "version": 1
    },
    "onDelete": {
      "revokeIssuedCredentials": true
    },
    "openid4VCI": {
      "enabled": true,
      "scope": "p1:provision:credentials"
    },
    "visualizationTemplateData": {
      "displayFields": [
        {
          "dataFieldName": "Name",
          "showFieldName": true
        },
        {
          "dataFieldName": "User ID",
          "showFieldName": true
        }
      ]
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

url = "{{apiPath}}/v1/environments/{{envID}}/credentialTypes"

payload = json.dumps({
  "title": "Card Developers",
  "description": "Card Developers Employee Credentials",
  "management": {
    "mode": "MANAGED"
  },
  "cardType": "Card Developers",
  "metadata": {
    "name": "Card Developers Employee Credentials",
    "description": "Card Developers Employee Credentials",
    "textColor": "#000000",
    "cardColor": "#FFFFFF",
    "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
    "logoImage": "",
    "bgOpacityPercent": 20,
    "fields": [
      {
        "id": "Directory Attribute -> Name",
        "title": "Name",
        "type": "Directory Attribute",
        "attribute": "name.formatted",
        "required": True
      },
      {
        "id": "Directory Attribute -> Address",
        "title": "Address",
        "type": "Directory Attribute",
        "attribute": "address",
        "required": True
      },
      {
        "id": "Directory Attribute -> ID",
        "title": "User ID",
        "type": "Directory Attribute",
        "attribute": "id",
        "required": True
      },
      {
        "id": "Alphanumeric Text -> Clearance",
        "title": "Clearance",
        "type": "Alphanumeric Text",
        "value": "None",
        "required": True
      }
    ],
    "version": 1
  },
  "onDelete": {
    "revokeIssuedCredentials": True
  },
  "openid4VCI": {
    "enabled": True,
    "scope": "p1:provision:credentials"
  },
  "visualizationTemplateData": {
    "displayFields": [
      {
        "dataFieldName": "Name",
        "showFieldName": True
      },
      {
        "dataFieldName": "User ID",
        "showFieldName": True
      }
    ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/credentialTypes');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "title": "Card Developers",\n    "description": "Card Developers Employee Credentials",\n    "management": {\n        "mode": "MANAGED"\n    },\n    "cardType": "Card Developers",\n    "metadata": {\n        "name": "Card Developers Employee Credentials",\n        "description": "Card Developers Employee Credentials",\n        "textColor": "#000000",\n        "cardColor": "#FFFFFF",\n        "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",\n        "logoImage": "",\n        "bgOpacityPercent": 20,\n        "fields": [\n            {\n                "id": "Directory Attribute -> Name",\n                "title": "Name",\n                "type": "Directory Attribute",\n                "attribute": "name.formatted",\n                "required": true\n            },\n            {\n                "id": "Directory Attribute -> Address",\n                "title": "Address",\n                "type": "Directory Attribute",\n                "attribute": "address",\n                "required": true\n            },\n            {\n                "id": "Directory Attribute -> ID",\n                "title": "User ID",\n                "type": "Directory Attribute",\n                "attribute": "id",\n                "required": true\n            },\n            {\n                "id": "Alphanumeric Text -> Clearance",\n                "title": "Clearance",\n                "type": "Alphanumeric Text",\n                "value": "None",\n                "required": true\n            }\n        ],\n        "version": 1\n    },\n    "onDelete": {\n        "revokeIssuedCredentials": true\n    },\n    "openid4VCI": {\n        "enabled": true,\n        "scope": "p1:provision:credentials"\n    },\n    "visualizationTemplateData": {\n        "displayFields": [\n            {\n                "dataFieldName": "Name",\n                "showFieldName": true\n            },\n            {\n                "dataFieldName": "User ID",\n                "showFieldName": true\n            }\n        ]\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/credentialTypes")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "title": "Card Developers",
  "description": "Card Developers Employee Credentials",
  "management": {
    "mode": "MANAGED"
  },
  "cardType": "Card Developers",
  "metadata": {
    "name": "Card Developers Employee Credentials",
    "description": "Card Developers Employee Credentials",
    "textColor": "\#000000",
    "cardColor": "\#FFFFFF",
    "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
    "logoImage": "",
    "bgOpacityPercent": 20,
    "fields": [
      {
        "id": "Directory Attribute -> Name",
        "title": "Name",
        "type": "Directory Attribute",
        "attribute": "name.formatted",
        "required": true
      },
      {
        "id": "Directory Attribute -> Address",
        "title": "Address",
        "type": "Directory Attribute",
        "attribute": "address",
        "required": true
      },
      {
        "id": "Directory Attribute -> ID",
        "title": "User ID",
        "type": "Directory Attribute",
        "attribute": "id",
        "required": true
      },
      {
        "id": "Alphanumeric Text -> Clearance",
        "title": "Clearance",
        "type": "Alphanumeric Text",
        "value": "None",
        "required": true
      }
    ],
    "version": 1
  },
  "onDelete": {
    "revokeIssuedCredentials": true
  },
  "openid4VCI": {
    "enabled": true,
    "scope": "p1:provision:credentials"
  },
  "visualizationTemplateData": {
    "displayFields": [
      {
        "dataFieldName": "Name",
        "showFieldName": true
      },
      {
        "dataFieldName": "User ID",
        "showFieldName": true
      }
    ]
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"title\": \"Card Developers\",\n    \"description\": \"Card Developers Employee Credentials\",\n    \"management\": {\n        \"mode\": \"MANAGED\"\n    },\n    \"cardType\": \"Card Developers\",\n    \"metadata\": {\n        \"name\": \"Card Developers Employee Credentials\",\n        \"description\": \"Card Developers Employee Credentials\",\n        \"textColor\": \"#000000\",\n        \"cardColor\": \"#FFFFFF\",\n        \"backgroundImage\": \"data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==\",\n        \"logoImage\": \"\",\n        \"bgOpacityPercent\": 20,\n        \"fields\": [\n            {\n                \"id\": \"Directory Attribute -> Name\",\n                \"title\": \"Name\",\n                \"type\": \"Directory Attribute\",\n                \"attribute\": \"name.formatted\",\n                \"required\": true\n            },\n            {\n                \"id\": \"Directory Attribute -> Address\",\n                \"title\": \"Address\",\n                \"type\": \"Directory Attribute\",\n                \"attribute\": \"address\",\n                \"required\": true\n            },\n            {\n                \"id\": \"Directory Attribute -> ID\",\n                \"title\": \"User ID\",\n                \"type\": \"Directory Attribute\",\n                \"attribute\": \"id\",\n                \"required\": true\n            },\n            {\n                \"id\": \"Alphanumeric Text -> Clearance\",\n                \"title\": \"Clearance\",\n                \"type\": \"Alphanumeric Text\",\n                \"value\": \"None\",\n                \"required\": true\n            }\n        ],\n        \"version\": 1\n    },\n    \"onDelete\": {\n        \"revokeIssuedCredentials\": true\n    },\n    \"openid4VCI\": {\n        \"enabled\": true,\n        \"scope\": \"p1:provision:credentials\"\n    },\n    \"visualizationTemplateData\": {\n        \"displayFields\": [\n            {\n                \"dataFieldName\": \"Name\",\n                \"showFieldName\": true\n            },\n            {\n                \"dataFieldName\": \"User ID\",\n                \"showFieldName\": true\n            }\n        ]\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/credentialTypes")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialTypes/8923a0ea-c3f8-4ff2-b47c-658657b27100"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "credentialIssuerProfile": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialIssuerProfile"
        },
        "version": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialTypes/8923a0ea-c3f8-4ff2-b47c-658657b27100/versions/961a133b-1226-43bf-a754-2ba2c786d6f8"
        }
    },
    "id": "8923a0ea-c3f8-4ff2-b47c-658657b27100",
    "createdAt": "2026-06-09T16:32:01.752406909Z",
    "updatedAt": "2026-06-09T16:32:01.752406909Z",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "issuer": {
        "id": "43b3e256-8bcd-4eae-bbd8-48471bb1014e"
    },
    "management": {
        "mode": "MANAGED"
    },
    "title": "Card Developers",
    "description": "Card Developers Employee Credentials",
    "cardType": "Card Developers",
    "uri": "https://api.pingone.com/v1/distributedid/credentialTypes/8923a0ea-c3f8-4ff2-b47c-658657b27100",
    "version": {
        "number": 1,
        "uri": "https://api.pingone.com/v1/distributedid/credentialTypes/8923a0ea-c3f8-4ff2-b47c-658657b27100/v1",
        "id": "961a133b-1226-43bf-a754-2ba2c786d6f8"
    },
    "metadata": {
        "name": "Card Developers Employee Credentials",
        "description": "Card Developers Employee Credentials",
        "textColor": "#000000",
        "cardColor": "#FFFFFF",
        "backgroundImage": "data:image/jpeg;base64,R0lGODlhIAAgAPEAAAAAAAAAM8wzMwAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQJCgABACwAAAAAIAAgAAACc4yPqcvtD6OcNIiLsxZg7o91EgiKShYA6sq27Ymm7swumsHRLgfHOXuZ8RKkn6YVHBU3pscRUIRGntDSxSJoZICfzoZBLWFjvRBJdLMtQ4d0edkkE9dJDz1bQXzyNiK/1/bXRoaRd2d4SHGHJ0gi+Ai5UAAAOw==",
        "logoImage": "",
        "bgOpacityPercent": 20,
        "fields": [
            {
                "id": "Directory Attribute -> Name",
                "title": "Name",
                "isVisible": false,
                "type": "Directory Attribute",
                "attribute": "name.formatted",
                "required": true
            },
            {
                "id": "Directory Attribute -> Address",
                "title": "Address",
                "isVisible": false,
                "type": "Directory Attribute",
                "attribute": "address",
                "required": true
            },
            {
                "id": "Directory Attribute -> ID",
                "title": "User ID",
                "isVisible": false,
                "type": "Directory Attribute",
                "attribute": "id",
                "required": true
            },
            {
                "id": "Alphanumeric Text -> Clearance",
                "title": "Clearance",
                "isVisible": false,
                "type": "Alphanumeric Text",
                "value": "None",
                "required": true
            }
        ],
        "version": 1
    },
    "onDelete": {
        "revokeIssuedCredentials": true
    },
    "visualizationTemplateData": {
        "displayFields": [
            {
                "showFieldName": true,
                "dataFieldName": "Name"
            },
            {
                "showFieldName": true,
                "dataFieldName": "User ID"
            }
        ]
    },
    "systemProvided": false,
    "openid4VCI": {
        "enabled": false,
        "scope": "p1:provision:credentials"
    }
}
```

---

---
title: Create Credential Verification Session (NATIVE - Push Notification)
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions to initiate verification of a user credential using the native protocol of the PingOne Credentials service and use a push notification to the user's digital wallet. Each credential verification session silently times out after 5 minutes.
component: pingone-api
page_id: pingone-api:credentials:credential-verifications/create-credential-verification-presentation-session-native-push-notification
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-verifications/create-credential-verification-presentation-session-native-push-notification.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Credential Verification Session (NATIVE - Push Notification)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions` to initiate verification of a user credential using the native protocol of the PingOne Credentials service and use a push notification to the user's digital wallet. Each credential verification session silently times out after 5 minutes.

### Prerequisites

* Refer to [Credential Verifications](../credential-verifications.html) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Credential Verifications session data model](../credential-verifications.html#credential-verifications-session-data-model) for full property descriptions.
>
> | Property                          | Type      | Required          |
> | --------------------------------- | --------- | ----------------- |
> | `applicationInstance.id`          | String    | N/A               |
> | `digitalWalletApplication.id`     | String    | N/A               |
> | `issuerFilter.environmentIds`     | String\[] | Optional          |
> | `message`                         | String    | Optional          |
> | `notification`                    | Object    | Optional          |
> | `notification.template`           | Object    | Optional          |
> | `notification.template.locale`    | String    | Optional          |
> | `notification.template.variables` | Object\[] | Required/Optional |
> | `notification.template.variant`   | String    | Optional          |
> | `protocol`                        | String    | Optional          |
> | `requestedCredentials`            | Object\[] | Required          |
> | `requestedCredentials.keys`       | String\[] | Optional          |
> | `requestedCredentials.type`       | String    | Required          |
> | `timeoutSeconds`                  | Integer   | Optional          |

After receipt of this request, the credential service uses the `credential_verification` notification template to send a push notification to a digital wallet. The `notification.template` object can define a variant and locale for the notifications, if needed.

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Content of `requestedCredentials` differs by `protocol`. The `protocol` of `NATIVE` permits multiple credential types per request and uses `requestedCredentials.keys` to return only those selected data fields for each credential type. |

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service searches all environments listed in `issuerFilter.environmentIds` for the issuer of the presented credential. If the user presents a credential that is not from one of these issuers, the verification fails with `status` of `VERIFICATION_FAILED`. |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "protocol": "NATIVE",
    "message": "Requesting a Verifiable Credential",
    "applicationInstance": {
        "id": "{{applicationInstanceID}}"
    },
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
        }
    },
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/presentationSessions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "protocol": "NATIVE",
    "message": "Requesting a Verifiable Credential",
    "applicationInstance": {
        "id": "{{applicationInstanceID}}"
    },
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
        }
    },
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""protocol"": ""NATIVE""," + "\n" +
@"    ""message"": ""Requesting a Verifiable Credential""," + "\n" +
@"    ""applicationInstance"": {" + "\n" +
@"        ""id"": ""{{applicationInstanceID}}""" + "\n" +
@"    }," + "\n" +
@"    ""digitalWalletApplication"": {" + "\n" +
@"        ""id"": ""{{digitalWalletApplicationID}}""" + "\n" +
@"    }," + "\n" +
@"    ""notification"": {" + "\n" +
@"        ""template"": {" + "\n" +
@"            ""locale"": ""en""," + "\n" +
@"            ""variant"": ""variant_B""," + "\n" +
@"            ""variables"": {}" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""requestedCredentials"": [" + "\n" +
@"        {" + "\n" +
@"            ""type"": ""Driver License""," + "\n" +
@"            ""keys"": [" + "\n" +
@"                ""First Name""," + "\n" +
@"                ""Last Name""" + "\n" +
@"            ]" + "\n" +
@"        }" + "\n" +
@"    ]," + "\n" +
@"    ""timeoutSeconds"" : 30" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/presentationSessions"
  method := "POST"

  payload := strings.NewReader(`{
    "protocol": "NATIVE",
    "message": "Requesting a Verifiable Credential",
    "applicationInstance": {
        "id": "{{applicationInstanceID}}"
    },
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
        }
    },
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
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
POST /v1/environments/{{envID}}/presentationSessions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "protocol": "NATIVE",
    "message": "Requesting a Verifiable Credential",
    "applicationInstance": {
        "id": "{{applicationInstanceID}}"
    },
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
        }
    },
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"protocol\": \"NATIVE\",\n    \"message\": \"Requesting a Verifiable Credential\",\n    \"applicationInstance\": {\n        \"id\": \"{{applicationInstanceID}}\"\n    },\n    \"digitalWalletApplication\": {\n        \"id\": \"{{digitalWalletApplicationID}}\"\n    },\n    \"notification\": {\n        \"template\": {\n            \"locale\": \"en\",\n            \"variant\": \"variant_B\",\n            \"variables\": {}\n        }\n    },\n    \"requestedCredentials\": [\n        {\n            \"type\": \"Driver License\",\n            \"keys\": [\n                \"First Name\",\n                \"Last Name\"\n            ]\n        }\n    ],\n    \"timeoutSeconds\" : 30\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/presentationSessions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "protocol": "NATIVE",
    "message": "Requesting a Verifiable Credential",
    "applicationInstance": {
      "id": "{{applicationInstanceID}}"
    },
    "digitalWalletApplication": {
      "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
      "template": {
        "locale": "en",
        "variant": "variant_B",
        "variables": {}
      }
    },
    "requestedCredentials": [
      {
        "type": "Driver License",
        "keys": [
          "First Name",
          "Last Name"
        ]
      }
    ],
    "timeoutSeconds": 30
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/presentationSessions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "protocol": "NATIVE",
    "message": "Requesting a Verifiable Credential",
    "applicationInstance": {
      "id": "{{applicationInstanceID}}"
    },
    "digitalWalletApplication": {
      "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
      "template": {
        "locale": "en",
        "variant": "variant_B",
        "variables": {}
      }
    },
    "requestedCredentials": [
      {
        "type": "Driver License",
        "keys": [
          "First Name",
          "Last Name"
        ]
      }
    ],
    "timeoutSeconds": 30
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

url = "{{apiPath}}/v1/environments/{{envID}}/presentationSessions"

payload = json.dumps({
  "protocol": "NATIVE",
  "message": "Requesting a Verifiable Credential",
  "applicationInstance": {
    "id": "{{applicationInstanceID}}"
  },
  "digitalWalletApplication": {
    "id": "{{digitalWalletApplicationID}}"
  },
  "notification": {
    "template": {
      "locale": "en",
      "variant": "variant_B",
      "variables": {}
    }
  },
  "requestedCredentials": [
    {
      "type": "Driver License",
      "keys": [
        "First Name",
        "Last Name"
      ]
    }
  ],
  "timeoutSeconds": 30
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/presentationSessions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "protocol": "NATIVE",\n    "message": "Requesting a Verifiable Credential",\n    "applicationInstance": {\n        "id": "{{applicationInstanceID}}"\n    },\n    "digitalWalletApplication": {\n        "id": "{{digitalWalletApplicationID}}"\n    },\n    "notification": {\n        "template": {\n            "locale": "en",\n            "variant": "variant_B",\n            "variables": {}\n        }\n    },\n    "requestedCredentials": [\n        {\n            "type": "Driver License",\n            "keys": [\n                "First Name",\n                "Last Name"\n            ]\n        }\n    ],\n    "timeoutSeconds" : 30\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "protocol": "NATIVE",
  "message": "Requesting a Verifiable Credential",
  "applicationInstance": {
    "id": "{{applicationInstanceID}}"
  },
  "digitalWalletApplication": {
    "id": "{{digitalWalletApplicationID}}"
  },
  "notification": {
    "template": {
      "locale": "en",
      "variant": "variant_B",
      "variables": {}
    }
  },
  "requestedCredentials": [
    {
      "type": "Driver License",
      "keys": [
        "First Name",
        "Last Name"
      ]
    }
  ],
  "timeoutSeconds": 30
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"protocol\": \"NATIVE\",\n    \"message\": \"Requesting a Verifiable Credential\",\n    \"applicationInstance\": {\n        \"id\": \"{{applicationInstanceID}}\"\n    },\n    \"digitalWalletApplication\": {\n        \"id\": \"{{digitalWalletApplicationID}}\"\n    },\n    \"notification\": {\n        \"template\": {\n            \"locale\": \"en\",\n            \"variant\": \"variant_B\",\n            \"variables\": {}\n        }\n    },\n    \"requestedCredentials\": [\n        {\n            \"type\": \"Driver License\",\n            \"keys\": [\n                \"First Name\",\n                \"Last Name\"\n            ]\n        }\n    ],\n    \"timeoutSeconds\" : 30\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/presentationSessions")!,timeoutInterval: Double.infinity)
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

202 Accepted

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/presentationSessions/365d18f0-ab78-4f02-9791-a6ff27cff02d"
        },
        "qr": {
            "href": "https://api.pingone.com/v1/distributedid/requests/9be6b3ff-eb8d-4615-bd14-7bd3d8ebfdad"
        },
        "appOpenUrl": {
            "href": "https://credentials.customer.com?u=https%3A%2F%2Fapi.pingone.com%2Fv1%2Fdistributedid%2Frequests%2F9be6b3ff-eb8d-4615-bd14-7bd3d8ebfdad"
        }
    },
    "id": "365d18f0-ab78-4f02-9791-a6ff27cff02d",
    "createdAt": "2024-10-24T16:39:52.991303314Z",
    "expiresAt": "2024-10-24T16:40:22.991301494Z",
    "status": "INITIAL",
    "notification": {
        "template": {
            "locale": "en",
            "variant": "variant_B"
        },
        "result": {
            "sent": true,
            "notification": {
                "id": "001004bc-989b-48eb-a911-bdc1301c2765"
            }
        }
    }
}
```

---

---
title: Create Credential Verification Session (NATIVE)
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions to initiate verification of a user credential using the native protocol of the PingOne Credentials service. Each credential verification session silently times out after 5 minutes.
component: pingone-api
page_id: pingone-api:credentials:credential-verifications/create-credential-verification-presentation-session-native
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-verifications/create-credential-verification-presentation-session-native.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Credential Verification Session (NATIVE)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions` to initiate verification of a user credential using the native protocol of the PingOne Credentials service. Each credential verification session silently times out after 5 minutes.

### Prerequisites

* Refer to [Credential Verifications](../credential-verifications.html) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Credential Verifications session data model](../credential-verifications.html#credential-verifications-session-data-model) for full property descriptions.
>
> | Property                      | Type      | Required |
> | ----------------------------- | --------- | -------- |
> | `issuerFilter.dids`           | String\[] | Optional |
> | `issuerFilter.environmentIds` | String\[] | Optional |
> | `message`                     | String    | Optional |
> | `protocol`                    | String    | Optional |
> | `requestedCredentials`        | Object\[] | Required |
> | `requestedCredentials.keys`   | String\[] | Optional |
> | `requestedCredentials.type`   | String    | Required |
> | `timeoutSeconds`              | Integer   | Optional |

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Content of `requestedCredentials` differs by `protocol`. The `protocol` of `NATIVE` permits multiple credential types per request and uses `requestedCredentials.keys` to return only those selected data fields for each credential type. |

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service searches all environments listed in `issuerFilter.environmentIds` for the issuer of the presented credential. If the user presents a credential that is not from one of these issuers, the verification fails with `status` of `VERIFICATION_FAILED`. |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "message": "Some custom message for the user.",
    "protocol": "NATIVE",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/presentationSessions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "message": "Some custom message for the user.",
    "protocol": "NATIVE",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""message"": ""Some custom message for the user.""," + "\n" +
@"    ""protocol"": ""NATIVE""," + "\n" +
@"    ""requestedCredentials"": [" + "\n" +
@"        {" + "\n" +
@"            ""type"": ""Driver License""," + "\n" +
@"            ""keys"": [" + "\n" +
@"                ""First Name""," + "\n" +
@"                ""Last Name""" + "\n" +
@"            ]" + "\n" +
@"        }" + "\n" +
@"    ]," + "\n" +
@"    ""timeoutSeconds"" : 30" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/presentationSessions"
  method := "POST"

  payload := strings.NewReader(`{
    "message": "Some custom message for the user.",
    "protocol": "NATIVE",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
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
POST /v1/environments/{{envID}}/presentationSessions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "message": "Some custom message for the user.",
    "protocol": "NATIVE",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"message\": \"Some custom message for the user.\",\n    \"protocol\": \"NATIVE\",\n    \"requestedCredentials\": [\n        {\n            \"type\": \"Driver License\",\n            \"keys\": [\n                \"First Name\",\n                \"Last Name\"\n            ]\n        }\n    ],\n    \"timeoutSeconds\" : 30\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/presentationSessions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "message": "Some custom message for the user.",
    "protocol": "NATIVE",
    "requestedCredentials": [
      {
        "type": "Driver License",
        "keys": [
          "First Name",
          "Last Name"
        ]
      }
    ],
    "timeoutSeconds": 30
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/presentationSessions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "message": "Some custom message for the user.",
    "protocol": "NATIVE",
    "requestedCredentials": [
      {
        "type": "Driver License",
        "keys": [
          "First Name",
          "Last Name"
        ]
      }
    ],
    "timeoutSeconds": 30
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

url = "{{apiPath}}/v1/environments/{{envID}}/presentationSessions"

payload = json.dumps({
  "message": "Some custom message for the user.",
  "protocol": "NATIVE",
  "requestedCredentials": [
    {
      "type": "Driver License",
      "keys": [
        "First Name",
        "Last Name"
      ]
    }
  ],
  "timeoutSeconds": 30
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/presentationSessions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "message": "Some custom message for the user.",\n    "protocol": "NATIVE",\n    "requestedCredentials": [\n        {\n            "type": "Driver License",\n            "keys": [\n                "First Name",\n                "Last Name"\n            ]\n        }\n    ],\n    "timeoutSeconds" : 30\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "message": "Some custom message for the user.",
  "protocol": "NATIVE",
  "requestedCredentials": [
    {
      "type": "Driver License",
      "keys": [
        "First Name",
        "Last Name"
      ]
    }
  ],
  "timeoutSeconds": 30
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"message\": \"Some custom message for the user.\",\n    \"protocol\": \"NATIVE\",\n    \"requestedCredentials\": [\n        {\n            \"type\": \"Driver License\",\n            \"keys\": [\n                \"First Name\",\n                \"Last Name\"\n            ]\n        }\n    ],\n    \"timeoutSeconds\" : 30\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/presentationSessions")!,timeoutInterval: Double.infinity)
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

202 Accepted

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/presentationSessions/16bab70c-32c1-41ca-9c84-d062aedd095f"
        },
        "qr": {
            "href": "https://api.pingone.com/v1/distributedid/requests/e4974bd1-0094-4586-8e43-28c4409d4bd7"
        },
        "appOpenUrl": {
            "href": "https://shocard.pingone.com/appopen?u=https%3A%2F%2Fapi.pingone.com%2Fv1%2Fdistributedid%2Frequests%2Fe4974bd1-0094-4586-8e43-28c4409d4bd7"
        }
    },
    "id": "16bab70c-32c1-41ca-9c84-d062aedd095f",
    "createdAt": "2024-10-24T16:39:52.991303314Z",
    "expiresAt": "2024-10-24T16:40:22.991301494Z",
    "status": "INITIAL"
}
```

---

---
title: Create Credential Verification Session (OPENID4VP)
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions to initiate verification of a user credential using the OpenID for Verifiable Presentations (OPENID4VP) protocol of JSON Web Token Verifiable Credentials (JWT-VC). Each credential verification session silently times out after 5 minutes.
component: pingone-api
page_id: pingone-api:credentials:credential-verifications/create-credential-verification-presentation-session-openid4vp
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-verifications/create-credential-verification-presentation-session-openid4vp.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Credential Verification Session (OPENID4VP)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/presentationSessions` to initiate verification of a user credential using the OpenID for Verifiable Presentations (OPENID4VP) protocol of JSON Web Token Verifiable Credentials (JWT-VC). Each credential verification session silently times out after 5 minutes.

### Prerequisites

* Refer to [Credential Verifications](../credential-verifications.html) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Credential Verifications session data model](../credential-verifications.html#credential-verifications-session-data-model) for full property descriptions.
>
> | Property                      | Type      | Required |
> | ----------------------------- | --------- | -------- |
> | `didMethod`                   | String    | Optional |
> | `issuerFilter.dids`           | String\[] | Optional |
> | `issuerFilter.environmentIds` | String\[] | Optional |
> | `message`                     | String    | Optional |
> | `protocol`                    | String    | Optional |
> | `protocolVersion`             | String    | Optional |
> | `requestedCredentials`        | Object\[] | Required |
> | `requestedCredentials.keys`   | String\[] | Optional |
> | `requestedCredentials.type`   | String    | Required |
> | `timeoutSeconds`              | Integer   | Optional |

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Content of `requestedCredentials` differs by `protocol`. The `protocol` of `OPENID4VP` permits only one credential type per request and ignores `requestedCredentials.keys` if present. |

Using the [PingOne Wallet Native SDKs](../../native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks.html), a wallet app retrieves verification information from the returned `_links.appOpenURL.href`. The information retrieved varies depending on the `didMethod` in the request.

If `issuerFilter.dids` is submitted and `protocol` is `OPENID4VP`, the service searches all listed decentralized identifiers for the issuer of the presented credential. If the user presents a credential that is not from one of these issuers, the verification fails with `status` of `VERIFICATION_FAILED`.

This `issuerFilter.dids` typically contains decentralized identifiers for issuers that are not using PingOne Credentials for JWT-VC issuance. The service supports these three DID methods:

* did:web, <https://w3c-ccg.github.io/did-method-web/>

* did:jwk, <https://github.com/quartzjer/did-jwk/blob/main/spec.md>

* did:ion, <https://identity.foundation/ion/> (The service supports only [long-form URIs](https://identity.foundation/sidetree/spec/#long-form-did-uris) for this method)

If `issuerFilter.environmentIds` is submitted, the service searches all listed environments for the issuer of the presented credential. If the user presents a credential that is not from one of these issuers, the verification fails with `status` of `VERIFICATION_FAILED`.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "message": "Some custom message for the user.",
    "protocol": "OPENID4VP",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30,
    "issuerFilter": {
        "dids": [
            "did:web:auth.pingone.com:{{envID}}:issuer"
        ]
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/presentationSessions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "message": "Some custom message for the user.",
    "protocol": "OPENID4VP",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30,
    "issuerFilter": {
        "dids": [
            "did:web:auth.pingone.com:{{envID}}:issuer"
        ]
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""message"": ""Some custom message for the user.""," + "\n" +
@"    ""protocol"": ""OPENID4VP""," + "\n" +
@"    ""requestedCredentials"": [" + "\n" +
@"        {" + "\n" +
@"            ""type"": ""Driver License""," + "\n" +
@"            ""keys"": [" + "\n" +
@"                ""First Name""," + "\n" +
@"                ""Last Name""" + "\n" +
@"            ]" + "\n" +
@"        }" + "\n" +
@"    ]," + "\n" +
@"    ""timeoutSeconds"" : 30," + "\n" +
@"    ""issuerFilter"": {" + "\n" +
@"        ""dids"": [" + "\n" +
@"            ""did:web:auth.pingone.com:{{envID}}:issuer""" + "\n" +
@"        ]" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/presentationSessions"
  method := "POST"

  payload := strings.NewReader(`{
    "message": "Some custom message for the user.",
    "protocol": "OPENID4VP",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30,
    "issuerFilter": {
        "dids": [
            "did:web:auth.pingone.com:{{envID}}:issuer"
        ]
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
POST /v1/environments/{{envID}}/presentationSessions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "message": "Some custom message for the user.",
    "protocol": "OPENID4VP",
    "requestedCredentials": [
        {
            "type": "Driver License",
            "keys": [
                "First Name",
                "Last Name"
            ]
        }
    ],
    "timeoutSeconds" : 30,
    "issuerFilter": {
        "dids": [
            "did:web:auth.pingone.com:{{envID}}:issuer"
        ]
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"message\": \"Some custom message for the user.\",\n    \"protocol\": \"OPENID4VP\",\n    \"requestedCredentials\": [\n        {\n            \"type\": \"Driver License\",\n            \"keys\": [\n                \"First Name\",\n                \"Last Name\"\n            ]\n        }\n    ],\n    \"timeoutSeconds\" : 30,\n    \"issuerFilter\": {\n        \"dids\": [\n            \"did:web:auth.pingone.com:{{envID}}:issuer\"\n        ]\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/presentationSessions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "message": "Some custom message for the user.",
    "protocol": "OPENID4VP",
    "requestedCredentials": [
      {
        "type": "Driver License",
        "keys": [
          "First Name",
          "Last Name"
        ]
      }
    ],
    "timeoutSeconds": 30,
    "issuerFilter": {
      "dids": [
        "did:web:auth.pingone.com:{{envID}}:issuer"
      ]
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/presentationSessions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "message": "Some custom message for the user.",
    "protocol": "OPENID4VP",
    "requestedCredentials": [
      {
        "type": "Driver License",
        "keys": [
          "First Name",
          "Last Name"
        ]
      }
    ],
    "timeoutSeconds": 30,
    "issuerFilter": {
      "dids": [
        "did:web:auth.pingone.com:{{envID}}:issuer"
      ]
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

url = "{{apiPath}}/v1/environments/{{envID}}/presentationSessions"

payload = json.dumps({
  "message": "Some custom message for the user.",
  "protocol": "OPENID4VP",
  "requestedCredentials": [
    {
      "type": "Driver License",
      "keys": [
        "First Name",
        "Last Name"
      ]
    }
  ],
  "timeoutSeconds": 30,
  "issuerFilter": {
    "dids": [
      "did:web:auth.pingone.com:{{envID}}:issuer"
    ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/presentationSessions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "message": "Some custom message for the user.",\n    "protocol": "OPENID4VP",\n    "requestedCredentials": [\n        {\n            "type": "Driver License",\n            "keys": [\n                "First Name",\n                "Last Name"\n            ]\n        }\n    ],\n    "timeoutSeconds" : 30,\n    "issuerFilter": {\n        "dids": [\n            "did:web:auth.pingone.com:{{envID}}:issuer"\n        ]\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/presentationSessions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "message": "Some custom message for the user.",
  "protocol": "OPENID4VP",
  "requestedCredentials": [
    {
      "type": "Driver License",
      "keys": [
        "First Name",
        "Last Name"
      ]
    }
  ],
  "timeoutSeconds": 30,
  "issuerFilter": {
    "dids": [
      "did:web:auth.pingone.com:{{envID}}:issuer"
    ]
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"message\": \"Some custom message for the user.\",\n    \"protocol\": \"OPENID4VP\",\n    \"requestedCredentials\": [\n        {\n            \"type\": \"Driver License\",\n            \"keys\": [\n                \"First Name\",\n                \"Last Name\"\n            ]\n        }\n    ],\n    \"timeoutSeconds\" : 30,\n    \"issuerFilter\": {\n        \"dids\": [\n            \"did:web:auth.pingone.com:{{envID}}:issuer\"\n        ]\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/presentationSessions")!,timeoutInterval: Double.infinity)
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

202 Accepted

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/presentationSessions/ac18c46b-03b8-4293-a9c9-ef4877c84d5c"
        },
        "qr": {
            "href": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAIAAAAiOjnJAAAE5ElEQVR42u3dwXEbMQwFUBeSMtKC+y/JaSAHScAHIOthfNJkNivyaQYLkNyvHyEC8WUIBFgCLAGWEGAJsARYQoAlwBJg/Tf+/P1u/3vktp69zrP/17PXfPaeE2N44R4evx+wwAILLLDAAuuVG302KpNX+ZKTk10Zq8r1K+PQNY9ggQUWWGCBBVYPrMSgJ5LWrkhcPzFuF+YRLLDAAgsssMDah1UpeCaKh13F267vlbgmWGCBBRZYYIElea82ZdP3kG54p4u3YIEFFlhggQXWLViJJnQ6+U0n8l0PDeli7MetbgALLLDAAgus47AmF8f5PPf5R+zS8TlYYIEFls+Pw5qMdEO6a7NruvhZGbf0gsfHAyywwAILLLDASiXvlUJo1yCmG8/pzbTpucgVbMECCyywwAILrCtNzQTK9AEeW8349ANEfX7BAgsssMACC6zqQHRNxtahapWB3nooSYxtb3EVLLDAAgsssMBKwdo68CN9aFu6Ud2VvO++0AAssMACCyywwKoWMycBJSYvgSaRyE8uKqwXS8ECCyywwAILrM4GagJE7xfeTfYvFIHTPwywwAILLLDAAqsH1haaCxsW0k30O03l5iY0WGCBBRZYYIEVTd4TSWsC2YUfXvpBZPQFAmCBBRZYYIEFVkth7domha2i4mSBtJLsjxZIwQILLLDAAusDYW0t7ptMxtMHaVxYoPeWb6YACyywwAILrA+E1TUoW4l/ItGeLMxu3T9YYIEFFlhggbVzKEhi4tON8AsHyN5sJFca7WCBBRZYYIEFVhXWhQT8pykS9791P/NFUbDAAgsssMAC61FYuQJabxEvMUm9yexu4zz9QwILLLDAAgsssOaS98mBuHb/ic0L6fvs/RmDBRZYYIEFFlipRDjdAJ48qK3r36cfYrZ+qGCBBRZYYIEF1uuwJjcyTBZjrzXRry0qHH2BAFhggQUWWGB9IKzJxDOxmG4SQeJgt8ki8NuvbgALLLDAAgus47Amv1gitjbHpjd6TF5zdJcOWGCBBRZYYH0IrHTDNd2oTkCZTK4nD0zrXQwIFlhggQUWWGBNFC23GqvplwMkCsWTyfjaQj+wwAILLLDAAuvUBtQE+gsPCumXG6TBgQUWWGCBBRZYPbAqA51e5D9zeGs9oU78ALYWS4IFFlhggQUWWP0F0snNApMvHkpvLk0XV9PXBAsssMACCyywXofV9QUmF68lkt90A7s+kbmi6OlDQcACCyywwALrTWFNLna7dv2uYmbXeE5ep57sgwUWWGCBBRZYnXFhYq41obvGarKoW3+AAAsssMACCyywqsXJmRutJ5sXIE5ulN09UA4ssMACCyywwJooWk4WMy8k/tcWJyZekgUWWGCBBRZYYM0VSLcKqokXEiUeaCZfFJV4GAILLLDAAgsssPY3rKaT3K1rbk3q/aIoWGCBBRZYYIHVWSBNFDwnD2pLF10TDzG/KnkHCyywwAILLLDGksfJZHProSRdWN69f7DAAgsssMAC6zqs9IK19KaJaygTBVuwwAILLLDAAuu9YSWKrlsQ0xtPdhGDBRZYYIEFFlibTej05oiuCUg3tidf0jSz2QQssMACCyywwJpo0CYSzPQ1J//SReP0hguwwAILLLDAAus5WEJECqRCgCXAEmAJAZYAS4AlBFgCLPF74x/OB65c5GBm8gAAAABJRU5ErkJggg=="
        },
        "appOpenUrl": {
            "href": "openid-vc://?request_uri=https://api.pingone.com/v1/distributedid/verifications/presentation_sessions/ac18c46b-03b8-4293-a9c9-ef4877c84d5c/request"
        }
    },
    "id": "ac18c46b-03b8-4293-a9c9-ef4877c84d5c",
    "createdAt": "2024-10-24T16:39:52.991303314Z",
    "expiresAt": "2024-10-24T16:40:22.991301494Z",
    "status": "INITIAL"
}
```

---

---
title: Create Customer Signing Public Key
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys operation to create a new credential signing public key. Set enabled to true to use the key for signing credentials and to be available for verifying credentials. Set it to false to make it available only for verifying credentials.
component: pingone-api
page_id: pingone-api:credentials:credential-signing-keys/create-customer-signing-public-key
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-signing-keys/create-customer-signing-public-key.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Customer Signing Public Key

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys` operation to create a new credential signing public key. Set `enabled` to `true` to use the key for signing credentials and to be available for verifying credentials. Set it to `false` to make it available only for verifying credentials.

> **Collapse: Request Model**
>
> Refer to [Credential signing key data model](../credential-signing-keys.html#customer-credential-signing-request-data-model) for full property descriptions.
>
> | Property  | Type   | Required          |
> | --------- | ------ | ----------------- |
> | `enabled` | String | Required          |
> | `jwk`     | Object | Required/Optional |
> | `jwk.alg` | String | Required          |
> | `jwk.crv` | String | Required/Optional |
> | `jwk.e`   | String | Required/Optional |
> | `jwk.kid` | String | Required          |
> | `jwk.kty` | String | Required          |
> | `jwk.n`   | String | Required/Optional |
> | `jwk.x`   | String | Required/Optional |
> | `jwk.y`   | String | Required/Optional |
> | `name`    | String | Optional          |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "enabled": true,
    "jwk": {
        "kid": "customer-specified-key-id",
        "kty": "RSA",
        "alg": "RS256",
        "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
        "e": "AQAB"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "enabled": true,
    "jwk": {
        "kid": "customer-specified-key-id",
        "kty": "RSA",
        "alg": "RS256",
        "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
        "e": "AQAB"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""enabled"": true," + "\n" +
@"    ""jwk"": {" + "\n" +
@"        ""kid"": ""customer-specified-key-id""," + "\n" +
@"        ""kty"": ""RSA""," + "\n" +
@"        ""alg"": ""RS256""," + "\n" +
@"        ""n"": ""jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw""," + "\n" +
@"        ""e"": ""AQAB""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys"
  method := "POST"

  payload := strings.NewReader(`{
    "enabled": true,
    "jwk": {
        "kid": "customer-specified-key-id",
        "kty": "RSA",
        "alg": "RS256",
        "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
        "e": "AQAB"
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
POST /v1/environments/{{envID}}/credentialSigningKeys HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "enabled": true,
    "jwk": {
        "kid": "customer-specified-key-id",
        "kty": "RSA",
        "alg": "RS256",
        "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
        "e": "AQAB"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"enabled\": true,\n    \"jwk\": {\n        \"kid\": \"customer-specified-key-id\",\n        \"kty\": \"RSA\",\n        \"alg\": \"RS256\",\n        \"n\": \"jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw\",\n        \"e\": \"AQAB\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "enabled": true,
    "jwk": {
      "kid": "customer-specified-key-id",
      "kty": "RSA",
      "alg": "RS256",
      "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
      "e": "AQAB"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "enabled": true,
    "jwk": {
      "kid": "customer-specified-key-id",
      "kty": "RSA",
      "alg": "RS256",
      "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
      "e": "AQAB"
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

url = "{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys"

payload = json.dumps({
  "enabled": True,
  "jwk": {
    "kid": "customer-specified-key-id",
    "kty": "RSA",
    "alg": "RS256",
    "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
    "e": "AQAB"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "enabled": true,\n    "jwk": {\n        "kid": "customer-specified-key-id",\n        "kty": "RSA",\n        "alg": "RS256",\n        "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",\n        "e": "AQAB"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "enabled": true,
  "jwk": {
    "kid": "customer-specified-key-id",
    "kty": "RSA",
    "alg": "RS256",
    "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
    "e": "AQAB"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"enabled\": true,\n    \"jwk\": {\n        \"kid\": \"customer-specified-key-id\",\n        \"kty\": \"RSA\",\n        \"alg\": \"RS256\",\n        \"n\": \"jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw\",\n        \"e\": \"AQAB\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/credentialSigningKeys")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/credentialSigningKeys/34ab57dc-8c7b-4377-95b2-a24672e8b70c"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "34ab57dc-8c7b-4377-95b2-a24672e8b70c",
    "createdAt": "2025-06-27T13:56:20.046015831Z",
    "updatedAt": "2025-06-27T13:56:20.046015831Z",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "customer-specified-key-id",
    "enabled": true,
    "jwk": {
        "kty": "RSA",
        "kid": "customer-specified-key-id",
        "alg": "RS256",
        "n": "jFfJCBv199-wMuUcW3MKaRH-DItx0xGji7JD2Agrm4JtiAJKD_g2xD4SwnQIkQdidTRnoAQ1UvUc7PlYNL7CaHCyzUw08E6QhbDxzbG2_lhDl7Y6Cljp23pkZ-40rBezqYuqOwgQv21FiiuA5LNSckH8ojdC_nvFUy4x2jKIFDAh_xEgdcTXZELrVbIdrqR2oFZXR_zIXPaoKl-67tQY1ttUopXqewzM31mKfj6JDfkbeGdaRhiBH_jlFTDbIE7metwsBnxucpQbDk1XlPmgsu8yZfbjJN19rhie7BTDS7BA5oYWizy8LBI6kUPkUTgqRRRhtyuVrWV1CXvpARrZvw",
        "e": "AQAB"
    }
}
```

---

---
title: Create Digital Wallet
description: The POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets operation creates a digital wallet for the specified user in the specified environment.
component: pingone-api
page_id: pingone-api:credentials:digital-wallets/create-digital-wallet
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/digital-wallets/create-digital-wallet.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Digital Wallet

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets
```

The `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets` operation creates a digital wallet for the specified user in the specified environment.

A request body is required to create a digital wallet.

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users.html), especially [User operations](../../platform/users/users-1.html).

* [Create Digital Wallet App](../digital-wallet-apps/create-digital-wallet-app.html) to get a `digitalWalletApplication.id` for the body. Refer also to [Digital Wallets](../digital-wallets.html).

> **Collapse: Request Model**
>
> Refer to [Digital wallet data model](../digital-wallets.html#digital-wallet-data-model) for full property descriptions.
>
> | Property                          | Type      | Required          |
> | --------------------------------- | --------- | ----------------- |
> | `digitalWalletApplication.id`     | String    | Required          |
> | `applicationInstance.id`          | String    | Optional          |
> | `notification`                    | Object    | Optional          |
> | `notification.template`           | Object    | Optional          |
> | `notification.template.locale`    | String    | Required          |
> | `notification.template.variant`   | String    | Required          |
> | `notification.template.variables` | Object\[] | Required/Optional |

After receipt of this request, the digital wallet service uses the `digital_wallet_pairing` notification template to send the pairing session URL to the user via email or SMS text. The `notification.template` object can define a variant and locale for the notification, if needed.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You must include a `notification` object in this create request if you want to use a custom notification template. You cannot use [Update Digital Wallet](update-digital-wallet.html) to add it later. |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "methods": [
            "EMAIL",
            "SMS"
        ],
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "methods": [
            "EMAIL",
            "SMS"
        ],
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
        }
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""digitalWalletApplication"": {" + "\n" +
@"        ""id"": ""{{digitalWalletApplicationID}}""" + "\n" +
@"    }," + "\n" +
@"    ""notification"": {" + "\n" +
@"        ""methods"": [" + "\n" +
@"            ""EMAIL""," + "\n" +
@"            ""SMS""" + "\n" +
@"        ]," + "\n" +
@"        ""template"": {" + "\n" +
@"            ""locale"": ""en""," + "\n" +
@"            ""variant"": ""variant_B""," + "\n" +
@"            ""variables"": {}" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets"
  method := "POST"

  payload := strings.NewReader(`{
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "methods": [
            "EMAIL",
            "SMS"
        ],
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
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
POST /v1/environments/{{envID}}/users/{{userID}}/digitalWallets HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "digitalWalletApplication": {
        "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
        "methods": [
            "EMAIL",
            "SMS"
        ],
        "template": {
            "locale": "en",
            "variant": "variant_B",
            "variables": {}
        }
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"digitalWalletApplication\": {\n        \"id\": \"{{digitalWalletApplicationID}}\"\n    },\n    \"notification\": {\n        \"methods\": [\n            \"EMAIL\",\n            \"SMS\"\n        ],\n        \"template\": {\n            \"locale\": \"en\",\n            \"variant\": \"variant_B\",\n            \"variables\": {}\n        }\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "digitalWalletApplication": {
      "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
      "methods": [
        "EMAIL",
        "SMS"
      ],
      "template": {
        "locale": "en",
        "variant": "variant_B",
        "variables": {}
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "digitalWalletApplication": {
      "id": "{{digitalWalletApplicationID}}"
    },
    "notification": {
      "methods": [
        "EMAIL",
        "SMS"
      ],
      "template": {
        "locale": "en",
        "variant": "variant_B",
        "variables": {}
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets"

payload = json.dumps({
  "digitalWalletApplication": {
    "id": "{{digitalWalletApplicationID}}"
  },
  "notification": {
    "methods": [
      "EMAIL",
      "SMS"
    ],
    "template": {
      "locale": "en",
      "variant": "variant_B",
      "variables": {}
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "digitalWalletApplication": {\n        "id": "{{digitalWalletApplicationID}}"\n    },\n    "notification": {\n        "methods": [\n            "EMAIL",\n            "SMS"\n        ],\n        "template": {\n            "locale": "en",\n            "variant": "variant_B",\n            "variables": {}\n        }\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "digitalWalletApplication": {
    "id": "{{digitalWalletApplicationID}}"
  },
  "notification": {
    "methods": [
      "EMAIL",
      "SMS"
    ],
    "template": {
      "locale": "en",
      "variant": "variant_B",
      "variables": {}
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"digitalWalletApplication\": {\n        \"id\": \"{{digitalWalletApplicationID}}\"\n    },\n    \"notification\": {\n        \"methods\": [\n            \"EMAIL\",\n            \"SMS\"\n        ],\n        \"template\": {\n            \"locale\": \"en\",\n            \"variant\": \"variant_B\",\n            \"variables\": {}\n        }\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/digitalWallets")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/digitalWallets/46e7018d-b2d5-482f-a44c-3fa9dd34e7d9"
        },
        "appOpen": {
            "href": "https://credentials.customer.com?u=https%3A%2F%2Fapi.pingone.com%2Fv1%2Fdistributedid%2Frequests%2F4766467d-2dd8-4cba-a9b7-10ba09b97354"
        },
        "qrUrl": {
            "href": "https://api.pingone.com/v1/distributedid/requests/4766467d-2dd8-4cba-a9b7-10ba09b97354"
        }
    },
    "id": "46e7018d-b2d5-482f-a44c-3fa9dd34e7d9",
    "createdAt": "2023-02-10T14:46:24.669Z",
    "updatedAt": "2023-02-10T14:46:24.669Z",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "49825b76-e1df-4cdc-b973-0c580f1cb049"
    },
    "digitalWalletApplication": {
        "id": "9f698462-21d5-4fd6-8599-c2b56683eb57"
    },
    "status": "PAIRING_REQUIRED",
    "pairingSession": {
        "id": "37d2b506-0ea7-4697-8884-c66ada3f4c48",
        "createdAt": "2023-02-10T14:46:24.669Z",
        "updatedAt": "2023-02-10T14:46:24.669Z",
        "environment": {
            "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "id": "49825b76-e1df-4cdc-b973-0c580f1cb049"
        },
        "digitalWallet": {
            "id": "46e7018d-b2d5-482f-a44c-3fa9dd34e7d9"
        },
        "challenge": "48p16h6eouv734ob",
        "qrUrl": "https://api.pingone.com/v1/distributedid/requests/4766467d-2dd8-4cba-a9b7-10ba09b97354",
        "status": "INITIAL"
    },
    "notification": {
        "methods": [
            "EMAIL",
            "SMS"
        ],
        "template": {
            "locale": "en",
            "variant": "variant_B"
        },
        "results": [
            {
                "method": "EMAIL",
                "sent": true,
                "notification": {
                    "id": "00a9e836-c339-4763-ab69-fcd3aa9c5417"
                }
            },
            {
                "method": "SMS",
                "sent": false,
                "error": {
                    "id": "17c006ef-9e5f-443b-b883-86f0855aa936",
                    "code": "INVALID_DATA",
                    "message": "The request could not be completed. One or more validation errors were in the request.",
                    "details": [
                        {
                            "code": "INVALID_VALUE",
                            "message": "Could not find phone attribute for user 49825b76-e1df-4cdc-b973-0c580f1cb049."
                        }
                    ]
                }
            }
        ]
    }
}
```

---

---
title: Create Digital Wallet App
description: The POST {{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications operation creates a digital wallet app in the specified environment.
component: pingone-api
page_id: pingone-api:credentials:digital-wallet-apps/create-digital-wallet-app
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/digital-wallet-apps/create-digital-wallet-app.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Digital Wallet App

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications
```

The `POST {{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications` operation creates a digital wallet app in the specified environment.

A request body is required to create a digital wallet app.

### Prerequisites

[Create Application (OIDC Mobile App)](../../platform/applications/applications-1/create-application-oidc-mobile-app.html) to get an `application.id` for the body. Refer also to [Application Management](../../platform/application-management.html), especially [Application Operations](../../platform/applications/applications-1.html).

> **Collapse: Request Model**
>
> Refer to [Digital wallet app data model](../digital-wallet-apps.html#digital-wallet-app-data-model) for full property descriptions.
>
> | Property               | Type    | Required |
> | ---------------------- | ------- | -------- |
> | `application.id`       | String  | Required |
> | `appOpenUrl`           | String  | Required |
> | `name`                 | String  | Required |
> | `usesPingOneWalletSDK` | Boolean | Optional |

The PingOne application identified by `application.id` must be a native application (`type` set to `NATIVE_APP`) and have either a mobile bundle ID (`mobile.bundleId`) or a package name (`mobile.packageName`).

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Customer Wallet App",
    "application": {
        "id": "{{appID}}"
    },
    "appOpenUrl": "{{appOpenUrl}}"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Customer Wallet App",
    "application": {
        "id": "{{appID}}"
    },
    "appOpenUrl": "{{appOpenUrl}}"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Customer Wallet App""," + "\n" +
@"    ""application"": {" + "\n" +
@"        ""id"": ""{{appID}}""" + "\n" +
@"    }," + "\n" +
@"    ""appOpenUrl"": ""{{appOpenUrl}}""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Customer Wallet App",
    "application": {
        "id": "{{appID}}"
    },
    "appOpenUrl": "{{appOpenUrl}}"
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
POST /v1/environments/{{envID}}/digitalWalletApplications HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Customer Wallet App",
    "application": {
        "id": "{{appID}}"
    },
    "appOpenUrl": "{{appOpenUrl}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Customer Wallet App\",\n    \"application\": {\n        \"id\": \"{{appID}}\"\n    },\n    \"appOpenUrl\": \"{{appOpenUrl}}\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Customer Wallet App",
    "application": {
      "id": "{{appID}}"
    },
    "appOpenUrl": "{{appOpenUrl}}"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Customer Wallet App",
    "application": {
      "id": "{{appID}}"
    },
    "appOpenUrl": "{{appOpenUrl}}"
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

url = "{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications"

payload = json.dumps({
  "name": "Customer Wallet App",
  "application": {
    "id": "{{appID}}"
  },
  "appOpenUrl": "{{appOpenUrl}}"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Customer Wallet App",\n    "application": {\n        "id": "{{appID}}"\n    },\n    "appOpenUrl": "{{appOpenUrl}}"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Customer Wallet App",
  "application": {
    "id": "{{appID}}"
  },
  "appOpenUrl": "{{appOpenUrl}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Customer Wallet App\",\n    \"application\": {\n        \"id\": \"{{appID}}\"\n    },\n    \"appOpenUrl\": \"{{appOpenUrl}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/digitalWalletApplications")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/digitalWalletApplications/9f698462-21d5-4fd6-8599-c2b56683eb57"
        }
    },
    "id": "9f698462-21d5-4fd6-8599-c2b56683eb57",
    "createdAt": "2023-02-09T19:43:00.817Z",
    "updatedAt": "2023-02-09T19:43:00.817Z",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Customer Wallet App",
    "application": {
        "id": "84cb89a4-fc4f-4422-b4ae-56b0109a9dbb"
    },
    "appOpenUrl": "https://credentials.customer.com",
    "usesPingOneWalletSDK": true
}
```

---

---
title: Credential Issuance Rules
description: Use the Credentials Issuance Rules operations to create, read, and update rules for issuing, updating, and revoking credentials by credential type. Rules are defined for:
component: pingone-api
page_id: pingone-api:credentials:credential-issuance-rules
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-issuance-rules.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  credential-issuance-rules-data-model: Credential Issuance Rules data model
  credential-issuance-rules-staged-changes-data-model: Credential Issuance Rules staged changes data model
  credential-issuance-rules-apply-staged-changes-data-model: Credential Issuance Rules apply staged changes data model
  credential-issuance-rules-usage-counts-data-model: Credential Issuance Rules usage counts data model
  credential-issuance-rules-usage-details-data-model: Credential Issuance Rules usage details data model
  credential-issuance-rules-errors-object: Credential Issuance Rules errors object
  credential-issuance-rules-staged-changes-error-codes: Credential Issuance Rules staged changes error codes
  response-codes: Response codes
---

# Credential Issuance Rules

Use the Credentials Issuance Rules operations to create, read, and update rules for issuing, updating, and revoking credentials by credential type. Rules are defined for:

* A specific [Credential Type](credential-types.html) in the endpoint

* A specific [Digital Wallet App](digital-wallet-apps.html) in the request body

* A specific set of users defined by one, and only one, of these filters in the request body:

  * Membership in one or more [Groups](../platform/groups.html).

  * Membership in one or more [Populations](../platform/populations.html).

  * Satisfying a SCIM query. For information about SCIM syntax and operators, refer to [SCIM operators](../platform/users/users-1.html#users-scim-operators).

A credential rule contains an `automation` object with available actions as keys: `issue`, `revoke`, and `update`. If an action is set to `PERIODIC`, the service performs the action at the end of the period. If an action is set to `ON_DEMAND`, you must use [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html) to perform staged changes for those `ON_DEMAND` actions.

The general procedure for rules is:

1. [Create](credential-issuance-rules/create-credential-issuance-rule.html): create a new rule to stage actions for for the credential by user

2. [Update](credential-issuance-rules/update-credential-issuance-rule.html): update an existing rule to stage actions for the credential by user

3. [Staged Changes](credential-issuance-rules/read-all-credential-issuance-rule-staged-changes.html): show actions staged for execution

4. [Apply](credential-issuance-rules/apply-credential-issuance-rule.html): act upon credentials staged for actions.

You can also monitor credential rules:

* [All Rules](credential-issuance-rules/read-all-credential-issuance-rules.html): view all rules defined for a credential type

* [One Rule](credential-issuance-rules/read-one-credential-issuance-rule.html): view a specific rule for a credential

* [Usage Counts](credential-issuance-rules/read-credential-issuance-rule-usage-counts.html): show counts by action applied to the credential by user

* [Usage Details](credential-issuance-rules/read-credential-issuance-rule-usage-details.html): show details by action applied to the credential by user

You can, finally, remove a rule for a credential type:

* [Delete](credential-issuance-rules/delete-credential-issuance-rule.html): remove a rule from a credential type

For actions set to `PERIODIC`, an improper credential could cause endless repetitious errors. The service monitors staged changes for errors. When an error occurs during processing, the service adds details of the error to the staged change so that errors can be tracked, counted, and returned to the user. If more than 3 errors occur for the same scheduled staged change, the service unschedules (changes `stagedChanges.scheduled` from `true` to `false`) that staged change so that the service no longer attempts to process it. The user can manually trigger the staged change with [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html).

Credentials unscheduled due to errors are reported. Some errors are known but there can also be unexpected errors. The `errors.errorDetail` object provides an error [code and message](#credential-issuance-rules-staged-changes-error-codes). If the error was related to processing a specific credential field, the field name will be in `errors.errorDetail.target`. This includes the staged changes that exist when the request is made with 1 or more errors. It does not include a staged change that was failed in the past, but has since completed successfully or was deleted (because the user no longer matches the issuance rule). Requests that report errors include:

* [Read Credential Issuance Rule Staged Changes](credential-issuance-rules/read-all-credential-issuance-rule-staged-changes.html)

* [Read Credential Issuance Rule Usage Counts](credential-issuance-rules/read-credential-issuance-rule-usage-counts.html)

* [Read Credential Issuance Rule Usage Details](credential-issuance-rules/read-credential-issuance-rule-usage-details.html)

* [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html)

|   |                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - For a [credential type](credential-types.html) with `management.mode` set to `AUTOMATED` and no credential issuance rule exists for that credential type, no error occurs. That credential type is simply never issued.

- For a [credential type](credential-types.html) with `management.mode` set to `MANAGED`, you cannot create an issuance rule for that credential type. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Credential Issuance Rules data model

| Property                          | Type      | Required          | Mutable   | Description                                                                                                                                                                                                                                                                                                                              |
| --------------------------------- | --------- | ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `automation`                      | Object    | Required          | Mutable   | Contains a list of actions, as key names, and the update method for each action.                                                                                                                                                                                                                                                         |
| `automation.issue`                | String    | Required          | Mutable   | The method the service uses to issue credentials with the credential issuance rule. Can be `PERIODIC` or `ON_DEMAND`.                                                                                                                                                                                                                    |
| `automation.revoke`               | String    | Required          | Mutable   | The method the service uses to revoke credentials with the credential issuance rule. Can be `PERIODIC` or `ON_DEMAND`.                                                                                                                                                                                                                   |
| `automation.update`               | String    | Required          | Mutable   | The method the service uses to update credentials with the credential issuance rule. Can be `PERIODIC` or `ON_DEMAND`.                                                                                                                                                                                                                   |
| `createdAt`                       | DateTime  | N/A               | Read-only | Date and time the credential issuance rule was created.                                                                                                                                                                                                                                                                                  |
| `credentialType.id`               | String    | N/A               | Read-only | Identifier (UUID) of the credential type with which this credential issuance rule is associated.                                                                                                                                                                                                                                         |
| `digitalWalletApplication.id`     | String    | Optional          | Mutable   | Identifier (UUID) of the customer's [Digital Wallet App](digital-wallet-apps.html) that will interact with the user's [Digital Wallet](digital-wallets.html). Optional, and if present, digital wallet pairing automatically starts when a user matches the credential issuance rule.                                                    |
| `environment.id`                  | String    | N/A               | Read-only | PingOne environment identifier (UUID) in which the credential issuance rule exists.                                                                                                                                                                                                                                                      |
| `filter`                          | Object    | Optional          | Mutable   | Contains one and only one filter (`.groupIds`, `.populationIds`, or `.scim`) that selects the users to which the credential issuance rule applies.                                                                                                                                                                                       |
| `filter.groupIds`                 | String\[] | Required/Optional | Mutable   | Array of one or more identifiers (UUIDs) of groups, any of which a user must belong for the credential issuance rule to apply. One and only one filter is required in `filter`, others are optional and cause an error if used.                                                                                                          |
| `filter.populationIds`            | String\[] | Required/Optional | Mutable   | Array of one or more identifiers (UUIDs) of populations, any of which a user must belong for the credential issuance rule to apply. One and only one filter is required in `filter`, others are optional and cause an error if used.                                                                                                     |
| `filter.scim`                     | String    | Required/Optional | Mutable   | A SCIM query that selects users to which the credential issuance rule applies. One and only one filter is required in `filter`, others are optional and cause an error if used. For more information about SCIM syntax and operators, refer to [SCIM operators](../platform/users/users-1.html#users-scim-operators).                    |
| `id`                              | String    | N/A               | Read-only | Identifier (UUID) of the credential issuance rule.                                                                                                                                                                                                                                                                                       |
| `notification`                    | Object    | Optional          | Immutable | Contains notification information. When this property is supplied, the information within is used to create a custom notification.                                                                                                                                                                                                       |
| `notification.methods`            | String\[] | Optional          | Immutable | Array of methods for notifying the user. Can be `EMAIL`, `SMS`, or both.                                                                                                                                                                                                                                                                 |
| `notification.template`           | Object    | Optional          | Immutable | Contains template parameters.                                                                                                                                                                                                                                                                                                            |
| `notification.template.locale`    | String    | Optional          | Immutable | The ISO 2-character language code used for the notification, for example: `en` for English.                                                                                                                                                                                                                                              |
| `notification.template.variables` | Object\[] | Required/Optional | Immutable | An object of name-value pairs that defines the dynamic variables used by the content variant. Required if the template requires variables, otherwise ignored. For more information on dynamic variables, refer to [Dynamic variables](../platform/notifications/notifications-templates.html#notifications-templates-dynamic-variables). |
| `notification.template.variant`   | String    | Optional          | Immutable | The unique user-defined name for the content variant that contains the message text used for the notification. For more information on variants, refer to [Creating custom contents](../platform/notifications/notifications-templates.html#notifications-templates-creating-custom-contents).                                           |
| `status`                          | String    | Required          | Mutable   | Status of the credential issuance rule. Can be `ACTIVE` or `DISABLED`.                                                                                                                                                                                                                                                                   |
| `updatedAt`                       | DateTime  | N/A               | Read-only | Date and time the credential issuance rule was last updated. Can be null.                                                                                                                                                                                                                                                                |

Actions within `automation` (`.issue`, `.update`, and `.revoke`) can be `PERIODIC`, the service applies the rule frequently every hour, or `ON_DEMAND`, the service applies the rule only with an [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html) request. For `ON_DEMAND`, use [Read Credential Issuance Rule Staged Changes](credential-issuance-rules/read-all-credential-issuance-rule-staged-changes.html) to determine staged changes.

The one `notification.template` object applies a variant and locale to all three credential notification templates: `credential_issued`, `credential_updated`, and `credential_revoked`. When adding a variant or locale to any of the three notification templates, consider adding the same variant or locale to the other notification templates. If a requested variant is not defined, the notification uses the default notification template. If a requested locale is not defined, the notification uses the user's preferred language or, if the user has no preferred language, the default language of the environment.

## Credential Issuance Rules staged changes data model

| Property                          | Type      | Required | Mutable   | Description                                                                                                                                                                              |
| --------------------------------- | --------- | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stagedChanges.action`            | String    | N/A      | Read-only | Action determined by the service that should be taken for the credential based on the request that staged it. Can be `ISSUE`, `UPDATE`, or `REVOKE`.                                     |
| `stagedChanges.createdAt`         | DateTime  | N/A      | Read-only | Date and time the change was staged by the service.                                                                                                                                      |
| `stagedChanges.credentialType.id` | String    | N/A      | Read-only | Identifier (UUID) of the credential type with which this credential issuance rule is associated.                                                                                         |
| `stagedChanges.environment.id`    | String    | N/A      | Read-only | PingOne environment identifier (UUID) in which the credential issuance rule exists.                                                                                                      |
| `stagedChanges.issuanceRule.id`   | String    | N/A      | Read-only | Identifier (UUID) of the credential issuance rule.                                                                                                                                       |
| `stagedChanges.scheduled`         | String    | N/A      | Read-only | Whether or not the staged change is scheduled: `true` if the action on the credential issuance rule is set to `PERIODIC` and `false` if the action is set to `ON_DEMAND`.                |
| `stagedChanges.user.id`           | String    | N/A      | Read-only | Identifier (UUID) of the user identified by the filter on the credential issuance rule.                                                                                                  |
| `stagedChanges.errors`            | Object\[] | N/A      | Read-only | Array of objects representing credentials that had errors when attempting an action on it. Refer to [Credential Issuance Rules errors object](#credential-issuance-rules-errors-object). |

## Credential Issuance Rules apply staged changes data model

This data model applies only to [Read Credential Issuance Rule Staged Changes](credential-issuance-rules/read-all-credential-issuance-rule-staged-changes.html) and [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html).

| Property | Type      | Required | Mutable   | Description                                                                                                                                                                                                                                                         |
| -------- | --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `issue`  | String\[] | Optional | Mutable   | Array of one or more identifiers (UUIDs) of users whose credentials are in an `issue` action state and should be issued.                                                                                                                                            |
| `revoke` | String\[] | Optional | Mutable   | Array of one or more identifiers (UUIDs) of users whose credentials are in a `revoke` action state and should be revoked. Used only in the body of [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html).  |
| `update` | String\[] | Optional | Mutable   | Array of one or more identifiers (UUIDs) of users whose credentials are in an `update` action state and should be updated. Used only in the body of [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html). |
| `errors` | Object\[] | N/A      | Read-only | Array of objects representing credentials that had errors when attempting an action on it. Refer to [Credential Issuance Rules errors object](#credential-issuance-rules-errors-object).                                                                            |

## Credential Issuance Rules usage counts data model

| Property   | Type    | Required | Mutable   | Description                                                                                                                                           |
| ---------- | ------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `issued`   | Integer | N/A      | Read-only | Count of credentials issued by the rule since the time the credential issuance rule was created.                                                      |
| `accepted` | Integer | N/A      | Read-only | Count of credentials accepted by users of credentials issued by the credential issuance rule since the time the credential issuance rule was created. |
| `updated`  | Integer | N/A      | Read-only | Count of credentials updated by the rule since the time the credential issuance rule was created.                                                     |
| `revoked`  | Integer | N/A      | Read-only | Count of credentials revoked by the rule since the time the credential issuance rule was created.                                                     |
| `errors`   | Integer | N/A      | Read-only | Count of credentials that caused errors since the time the credential issuance rule was created.                                                      |

## Credential Issuance Rules usage details data model

| Property                | Type      | Required | Mutable   | Description                                                                                                                                                                              |
| ----------------------- | --------- | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `issued`                | Object\[] | N/A      | Read-only | Credentials issued by the rule since the time the credential issuance rule was created.                                                                                                  |
| `issued.user.id`        | String    | N/A      | Read-only | Identifier (UUID) of the user identified by the filter on the credential issuance rule.                                                                                                  |
| `issued.credential.id`  | String    | N/A      | Read-only | Identifier (UUID) of the credential subject to the issue action identified by the credential issuance rule.                                                                              |
| `issued.createdAt`      | DateTime  | N/A      | Read-only | Date and time the credential was issued by the service.                                                                                                                                  |
| `updated`               | Object\[] | N/A      | Read-only | Credentials updated by the rule since the time the credential issuance rule was created.                                                                                                 |
| `updated.user.id`       | String    | N/A      | Read-only | Identifier (UUID) of the user identified by the filter on the credential issuance rule.                                                                                                  |
| `updated.credential.id` | String    | N/A      | Read-only | Identifier (UUID) of the credential subject to the update action identified by the credential issuance rule.                                                                             |
| `updated.createdAt`     | DateTime  | N/A      | Read-only | Date and time the credential was updated by the service.                                                                                                                                 |
| `revoked`               | Object\[] | N/A      | Read-only | Credentials revoked by the rule since the time the credential issuance rule was created.                                                                                                 |
| `revoked.user.id`       | String    | N/A      | Read-only | Identifier (UUID) of the user identified by the filter on the credential issuance rule.                                                                                                  |
| `revoked.credential.id` | String    | N/A      | Read-only | Identifier (UUID) of the credential subject to the revoke action identified by the credential issuance rule.                                                                             |
| `revoked.createdAt`     | DateTime  | N/A      | Read-only | Date and time the credential was revoked by the service.                                                                                                                                 |
| `errors`                | Object\[] | N/A      | Read-only | Array of objects representing credentials that had errors when attempting an action on it. Refer to [Credential Issuance Rules errors object](#credential-issuance-rules-errors-object). |

## Credential Issuance Rules errors object

| Property                     | Type      | Required | Mutable   | Description                                                                                                                                                                         |
| ---------------------------- | --------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `errors`                     | Object\[] | N/A      | Read-only | Array of objects representing errors recorded when attempting an action on a credential.                                                                                            |
| `errors.recordedAt`          | DateTime  | N/A      | Read-only | Date and time the error was recorded by the service.                                                                                                                                |
| `errors.errorDetail.code`    | String    | N/A      | Read-only | A code that indicates the error encountered by the service. Refer to [Credential Issuance Rules staged changes error codes](#credential-issuance-rules-staged-changes-error-codes). |
| `errors.errorDetail.target`  | String    | N/A      | Read-only | The part of the credential that caused the error encountered by the service.                                                                                                        |
| `errors.errorDetail.message` | String    | N/A      | Read-only | A message that describes the error encountered by the service.                                                                                                                      |
| `credentialType.id`          | String    | N/A      | Read-only | Identifier (UUID) of the credential type with which this credential issuance rule is associated.                                                                                    |
| `environment.id`             | String    | N/A      | Read-only | PingOne environment identifier (UUID) in which the credential issuance rule exists.                                                                                                 |
| `issuanceRule.id`            | String    | N/A      | Read-only | Identifier (UUID) of the credential issuance rule.                                                                                                                                  |
| `user.id`                    | String    | N/A      | Read-only | Identifier (UUID) of the user identified by the filter on the credential issuance rule.                                                                                             |
| `id`                         | String    | N/A      | Read-only | Identifier (UUID) of the error.                                                                                                                                                     |
| `action`                     | String    | N/A      | Read-only | Action determined by the service that should be taken for the credential based on the request that staged it. Can be `ISSUE`, `UPDATE`, or `REVOKE`.                                |
| `scheduled`                  | String    | N/A      | Read-only | Whether or not the staged change is scheduled: `true` if the action on the credential issuance rule is set to `PERIODIC` and `false` if the action is set to `ON_DEMAND`.           |
| `createdAt`                  | DateTime  | N/A      | Read-only | Date and time the error was created by the service.                                                                                                                                 |
| `updatedAt`                  | DateTime  | N/A      | Read-only | Date and time the error was updated by the service.                                                                                                                                 |

### Credential Issuance Rules staged changes error codes

| Error Code                | Description                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TEMPLATE_ERROR`          | An error in the template placeholders of the `cardDesignTemplate` SVG.                                                                               |
| `SVG_ERROR`               | An error in the syntax of the `cardDesignTemplate` SVG.                                                                                              |
| `CREDENTIAL_TYPE_INVALID` | Credential Type was invalid when the staged change was performed.                                                                                    |
| `FILE_RESOLUTION_ERROR`   | User attribute for a field with `fileSupport` did not reference a supported file, such as an unsupported URL, file too large, or error reading file. |
| `CREDENTIAL_TOO_LARGE`    | Size of data collected for the credential exceeds the maximum that can be stored in a credential.                                                    |
| `UNEXPECTED_ERROR`        | An unexpected error occurred.                                                                                                                        |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | Unexpected server error.                                              |

---

---
title: Credential Issuer Decentralized Identifiers
description: W3C defines Decentralized IDs (DIDs) as a means to identify an entity in a decentralized ecosystem. See the W3C DIDs spec for details. An entities DID is represented as a string and used in the different ID fields, such as issuer, subject, audience, or holder, for Java Web Tokens (JWTs), Verifiable Credentials (VCs), and other JSON objects. The DID is used to find public keys for the entity as well as optional information about how to interact with the entity.
component: pingone-api
page_id: pingone-api:credentials:credential-issuer-decentralized-identifiers
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-issuer-decentralized-identifiers.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingone-hosted-issuer-didweb: PingOne hosted issuer did:web
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  credential-did-data-models: Credential issuer DID data models
---

# Credential Issuer Decentralized Identifiers

W3C defines Decentralized IDs (DIDs) as a means to identify an entity in a decentralized ecosystem. See the [W3C DIDs spec](https://www.w3.org/TR/did-core/) for details. An entities DID is represented as a string and used in the different ID fields, such as issuer, subject, audience, or holder, for Java Web Tokens (JWTs), Verifiable Credentials (VCs), and other JSON objects. The DID is used to find public keys for the entity as well as optional information about how to interact with the entity.

The DID specification supports multiple ways to store and represent the DID. Every DID is a colon-separated string with the literal `did`, a method name, and method-specific data. W3C maintains a list of all of the [current DID methods](https://www.w3.org/TR/did-spec-registries/#did-methods).

When PingOne Credentials issues a credential, it uses the Ping Native format as a delivery mechanism to provision the credential to the Wallet SDK app. The credential contains the data in two formats: the Ping Native format and the [W3C Verifiable Credential](https://www.w3.org/TR/vc-data-model/) format. The W3CVC format uses DIDs as identifiers for the issuer and for the holder or subject.

PingOne Credentials uses `did:web` for the issuer and verifier and `did:ion` for the holder or subject. PingOne also supports `did:ion` for all parties for backwards compatibility.

## PingOne hosted issuer did:web

The service supports retrieving the `did:web` documents of issuers hosted by PingOne on both the standard `auth.pingone.com` domain (and regional variants by top level domain, TLD) and custom domains. The DID document contains the public keys for the issuer and optional information about how to interact with the issuer. To retrieve the DID document:

1. The DID of an issuer hosted on the standard `auth.pingone.com` domain is in the format:

   * `did:web:`

   * `auth.pingone.com:`

   * UUID of the issuer's environment

   * `#`

   * UUID of the signing key

     For an environment UUID `8fd6a2f0-c568-4de8-a319-eb8ddff49dff`, the corresponding URL to retrieve the DID document is:

     ```none
     https://auth.pingone.com/8fd6a2f0-c568-4de8-a319-eb8ddff49dff/did.json
     ```

2. The DID of an issuer hosted on a custom domain is in the format:

   * `did:web:`

   * the issuer's custom domain

   * `#`

   * UUID of the signing key

     For a custom domain `issuer.customerdomain.com`, the corresponding URL to retrieve the DID document is:

     ```none
     https://issuer.customerdomain.com/.well-known/did.json
     ```

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Credential issuer DID data models

| Property                          | Type   | Required | Mutable   | Description                                                                                                                                                                                                       |
| --------------------------------- | ------ | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@context`                        | String | N/A      | Read-only | URL to the DID scheme                                                                                                                                                                                             |
| `id`                              | String | N/A      | Read-only | A unique identifier that conforms to [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax)                                                                                                                     |
| `verificationMethod.id`           | String | N/A      | Read-only | A unique identifier that conforms to [DID URL Syntax](https://www.w3.org/TR/did-core/#did-url-syntax)                                                                                                             |
| `verificationMethod.controller`   | String | N/A      | Read-only | The entity that controls the DID in [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax). In PingOne Credentials, the method-specific data is always equal to the domain part of the request URL              |
| `verificationMethod.type`         | String | N/A      | Read-only | Name for the type of JWK represented                                                                                                                                                                              |
| `verificationMethod.publicKeyJwk` | String | N/A      | Read-only | A JSON Web Key that conforms to [JSON Web Key (JWK)](https://www.rfc-editor.org/rfc/rfc7517). The contents vary by algorithm as discussed in [JSON Web Algorithms (JWA)](https://www.rfc-editor.org/rfc/rfc7518). |
| `authentication`                  | String | N/A      | Read-only | A unique identifier that conforms to [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax) including in its fragment a UUID for the key of the `verificationMethod.publicKeyJwk`                               |
| `assertionMethod`                 | String | N/A      | Read-only | A unique identifier that conforms to [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax) including in its fragment a UUID for the key of the `verificationMethod.publicKeyJwk`                               |

---

---
title: Credential Issuers
description: Use the Credential Issuers operations to retrieve or update the credential issuer information. A default credential issuer profile, which enables issuance of credentials, is automatically created when the credential service is added to an environment.
component: pingone-api
page_id: pingone-api:credentials:credential-profiles
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-profiles.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  credential-issuers-data-model: Credential Issuers data model
  did-webvh-didwebvh: DID WEBVH (did:webvh)
  response-codes: Response codes
---

# Credential Issuers

Use the Credential Issuers operations to retrieve or update the credential issuer information. A default credential issuer profile, which enables issuance of credentials, is automatically created when the credential service is added to an environment.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Credential Issuers data model

| Property                            | Type     | Required | Mutable   | Description                                                                                                                                                                                                                                  |
| ----------------------------------- | -------- | -------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `applicationInstance.id`            | String   | N/A      | Read-only | Identifier (UUID) of the application instance registered with the PingOne platform service. This enables the client to send messages to the service.                                                                                         |
| `credentialSigning`                 | Object   | Optional | Mutable   | Object with the configuration for sending verifiable credentials (VC-JWT or SD-JWT) to the customer's remote signing service at `credentialSigning.url` for signing with their private key.                                                  |
| `credentialSigning.url`             | String   | Required | Mutable   | URL to which to send verifiable credentials (VC-JWT or SD-JWT) for signing with their private key. Must be a valid URL with a protocol of HTTPS.                                                                                             |
| `credentialSigning.headers`         | Object   | Optional | Mutable   | Object of headers as key-value pairs, where the key is the name of a header field and the value is the value of the header field, to send with the verifiable credentials (VC-JWT or SD-JWT) for signing.                                    |
| `credentialSigning.headers.<field>` | String   | Required | Mutable   | The placeholder, `<field>`, is the name of the header field to add to the request. The value assigned to this becomes the value of the header field created.                                                                                 |
| `createdAt`                         | DateTime | N/A      | Read-only | Date and time the issuer profile was created.                                                                                                                                                                                                |
| `did.method`                        | String   | Optional | Mutable   | Decentralized Identifier (DID) method for the issuer. Can be `WEB` or `WEBVH`. Initially set to `WEB`. Refer to [DID WEBVH (did:webvh)](#did-webvh-didwebvh).                                                                                |
| `did.value`                         | String   | N/A      | Read-only | The entity that controls the DID in [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax). In PingOne Credentials, the method-specific data is always equal to the domain part of the request URL                                         |
| `did.web.host`                      | String   | N/A      | Read-only | The hosting provider. Always "PING"                                                                                                                                                                                                          |
| `did.web.useCustomDomain`           | Boolean  | Optional | Mutable   | Whether or not the credential issuer uses its custom domain in its DID when the issuer has [Custom Domains](../platform/custom-domains.html) enabled. Defaults to `true` and uses the custom domain, whereas `false` uses `auth.pingone.com` |
| `id`                                | String   | N/A      | Read-only | Identifier (UUID) of the credential issuer.                                                                                                                                                                                                  |
| `logo`                              | String   | Optional | Mutable   | A URI containing the logo for the issuer. Restricted to a valid URL with a scheme of `https:` or a scheme of `data:` with a base64-encoded image. Included in credentials issued.                                                            |
| `name`                              | String   | Required | Immutable | The name of the credential issuer. Included in credentials issued.                                                                                                                                                                           |
| `siteUrl`                           | String   | Optional | Mutable   | URL, chosen by the issuer, that references the issuer in issued credentials.                                                                                                                                                                 |
| `updatedAt`                         | DateTime | N/A      | Read-only | Date and time the credential issuer profile was last updated. Can be null.                                                                                                                                                                   |

In the `credentialSigning` object, the `credentialSigning.headers` object defines headers to add to the signing request sent to the customer's `credentialSigning.url`. For example:

```none
    "headers": {
        "ClientID": "016e1474-7c62-b944-0a96-b467731ef0bd"
    }
```

Creates a header on the signing request such as:

```none
ClientID: 016e1474-7c62-b944-0a96-b467731ef0bd
```

The `logo` and `name` can be shown to the user when indicating the credential issuer by the wallet app using using the [PingOne Neo Native SDKs](../native-sdks/pingone-neo-native-sdks.html) with [getIssuerMetadata](https://pingidentity.github.io/pingone-wallet-mobile-sdk-android/com/pingidentity/sdk/pingonewallet/utils/CredentialUtils.html#getIssuerMetadata\(com.pingidentity.did.sdk.types.Claim\)) for Android and [getCredentialIssuerMetadataFromClaim(\_:)](https://pingidentity.github.io/pingone-wallet-mobile-sdk-ios/documentation/pingonewallet/credentialutils/getcredentialissuermetadatafromclaim\(_:\)/) for iOS.

## DID WEBVH (did:webvh)

The `WEBVH` DID method, where `VH` stands for Verifiable History, extends `did:web`. It maintains simple domain-to-DID resolution (via HTTPS) of `did:web` while adding a cryptographically verifiable history to the DID without blockchains or ledgers. The Verifiable History records all changes (DID Document versions) in a JSON Lines log (did.jsonl), chained via hashes and signed proofs, allowing anyone to verify the full lifecycle from creation to deactivation. A unique, history-bound identifier, called a Self-Certifying Identifier (SCID), derived from the first DID log entry ensures tamper-resistance and enables portability. The SCID appears between `did:webvh` and the domain in the DID identifier. For example:

1. The DID of an issuer hosted on the standard auth.pingone.com domain is in the format:

   * `did:webvh:`

   * SCID of the `did:webvh`

   * `auth.pingone.com:`

   * UUID of the issuer's environment

   * `#`

   * UUID of the signing key

2. The DID of an issuer hosted on a custom domain is in the format:

   * `did:webvh:`

   * SCID of the `did:webvh`

   * `:`

   * issuer's custom domain

   * `#`

   * UUID of the signing key

The shortcoming of `did:webvh` is that it is not as widely accepted by verifiers as `did:web`.

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | Unexpected server error.                                              |

---

---
title: Credential Signing Keys
description: You can choose to sign credentials before issuance using your private keys maintained within your infrastructure. However, to properly build the JWT header, Ping Identity requires your public key.
component: pingone-api
page_id: pingone-api:credentials:credential-signing-keys
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-signing-keys.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  credential-signing-key-data-model: Credential signing key data model
  available-algorithms-for-jwk: Available algorithms for JWK
---

# Credential Signing Keys

You can choose to sign credentials before issuance using your private keys maintained within your infrastructure. However, to properly build the JWT header, Ping Identity requires your public key.

Use the Credential Signing Keys operations to store, retrieve, update, or delete the public signing keys used when communicating credentials between you and Ping Identity for signing before issuing.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Credential signing key data model

| Property         | Type     | Required          | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------- | -------- | ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `createdAt`      | DateTime | N/A               | Read-only | Date and time the credential signing key was created.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `enabled`        | String   | Required          | Mutable   | Whether the key is available for use in signing. Allows you to change the key that is used by the credentialing service for signing but retain the key for verification. Can be `true` or `false`.                                                                                                                                                                                                                                                                     |
| `environment.id` | String   | N/A               | Read-only | PingOne environment identifier (UUID) in which the credential signing key exists.                                                                                                                                                                                                                                                                                                                                                                                      |
| `jwk`            | Object   | Required/Optional | Immutable | JSON Web Key as defined in [RFC 7517](https://datatracker.ietf.org/doc/html/rfc7517). Required for [Create Customer Signing Public Key](credential-signing-keys/create-customer-signing-public-key.html), but optional (because it is immutable) for [Update Customer Signing Public Key](credential-signing-keys/update-customer-signing-public-key.html). Used when sending unsigned credentials to your signing endpoint and verifying returned signed credentials. |
| `jwk.alg`        | String   | Required          | Immutable | Algorithm, identifies the algorithm intended for use with the key. Refer to [Available algorithms for JWK](#available-algorithms-for-jwk).                                                                                                                                                                                                                                                                                                                             |
| `jwk.crv`        | String   | Required/Optional | Immutable | Curve of the Elliptic Curve (EC) or Octet Key Pair (OKP) public key. Required for EC- and OKP-based algorithms, optional and ignored if present for other algorithms.                                                                                                                                                                                                                                                                                                  |
| `jwk.e`          | String   | Required/Optional | Immutable | RSA exponent of the RSA public key. Required for RSA-based algorithms, optional and ignored if present for other algorithms.                                                                                                                                                                                                                                                                                                                                           |
| `jwk.kid`        | String   | Required          | Immutable | Key ID, a unique identifier for the key that helps when selecting a key.                                                                                                                                                                                                                                                                                                                                                                                               |
| `jwk.kty`        | String   | Required          | Immutable | Key Type, identifies the cryptographic algorithm family used with the key. Can be `RSA`, `EC`, or `OKP`.                                                                                                                                                                                                                                                                                                                                                               |
| `jwk.n`          | String   | Required/Optional | Immutable | RSA modulus of the RSA public key. Required for RSA-based algorithms, optional and ignored if present for other algorithms.                                                                                                                                                                                                                                                                                                                                            |
| `jwk.x`          | String   | Required/Optional | Immutable | Elliptic curve x-coordinate of the EC public key or OKP public key. Required for EC-based algorithms and OKP-based algorithms, optional and ignored if present for other algorithms.                                                                                                                                                                                                                                                                                   |
| `jwk.y`          | String   | Required/Optional | Immutable | Elliptic curve y-coordinate of the EC public key. Required for EC-based algorithms, optional and ignored if present for other algorithms.                                                                                                                                                                                                                                                                                                                              |
| `name`           | String   | Optional          | Mutable   | A friendly name shown in the admin console for the key. Optional and defaults to `jwk.kid`.                                                                                                                                                                                                                                                                                                                                                                            |
| `updatedAt`      | DateTime | N/A               | Read-only | Date and time the credential signing key was last updated. Can be null.                                                                                                                                                                                                                                                                                                                                                                                                |

The `jwk` object must not contain private key material. If you perform a POST request and the `jwk` object includes private key material, the service returns an HTTP 400 error.

The key ID, `jwk.kid`, accepts up to 256 characters from the set: a-z, 0-9, A-Z, -, and \_ and must be unique within an environment. Attempted reuse of a `kid` returns an error.

The service allows multiple keys with `enabled` set to `true`. However, the service selects a key to use from the available keys.

All keys, regardless of `enabled` state, are included in `did:web` responses so that the key can be used for verifying an issued credential.

## Available algorithms for JWK

The service does not allow `none`.

| Key Management Algorithm                                                                        | jwk.alg        |
| ----------------------------------------------------------------------------------------------- | -------------- |
| RSAES-PKCS1-V1\_5 key encryption                                                                | RSA1\_5        |
| RSAES using OAEP key encryption                                                                 | RSA-OAEP       |
|                                                                                                 | RSA-OAEP-256   |
| AES key wrap                                                                                    | A128KW         |
|                                                                                                 | A192KW         |
|                                                                                                 | A256KW         |
| AES GCM key encryption                                                                          | A128GCMKW      |
|                                                                                                 | A192GCMKW      |
|                                                                                                 | A256GCMKW      |
| Elliptic Curve Diffie-Hellman Ephemeral Static key agreement using Concat KDF                   | ECDH-ES        |
| Elliptic Curve Diffie-Hellman Ephemeral Static key agreement using Concat KDF with AES key wrap | ECDH-ES+A128KW |
|                                                                                                 | ECDH-ES+A192KW |
|                                                                                                 | ECDH-ES+A256KW |

---

---
title: Credential Types
description: Use the Credentials Types operations to create, read, and update the credential types used by compatible wallet apps.
component: pingone-api
page_id: pingone-api:credentials:credential-types
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-types.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  credential-type-management-modes: Credential Type management modes
  credential-type-issuance-method: Issuance method
  credential-type-data-source: Data source
  credential-type-issuance-protocol: Issuance protocol
  credential-type-openid4vci-protocol: OpenID4VCI protocol
  credential-type-native-protocol: Native protocol
  credentials-versioning: Versioning
  credentialing-automatic-deletion-and-revocation: Automatic deletion and revocation
  credential-schema: Credential schema
  credential-types-data-model: Credential Types data model
  credentialing-metadata-object-data-model: metadata object data model
  credentialing-fields-attribute-definition: fields.attribute definition
  credentialing-fields-filesupport-types: fields.fileSupport types
  credentialing-fields-type-types: fields.type types
  credentialing-fields-value-restrictions: fields.value restrictions
  credentialing-visualizationtemplatedata-object-data-model: visualizationTemplateData object data model
  credentialing-issue-multiple-credentials-to-a-user-based-on-a-directory-attribute: Issue multiple credentials to a user based on a directory attribute
  credential-types-example-data-object: Example data object
  credential-types-example-api: Example API
  credential-types-important-considerations: Important considerations
  response-codes: Response codes
---

# Credential Types

Use the Credentials Types operations to create, read, and update the credential types used by compatible wallet apps.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Credential Type management modes

Credential Types supports two modes of management identified in `management.mode` as `AUTOMATED` or `MANAGED`. The two modes differ by [issuance method](#credential-type-issuance-method) and [data source](#credential-type-data-source).

### Issuance method

if `management.mode` is `AUTOMATIC`, you [create a credential issuance rule](credential-issuance-rules/create-credential-issuance-rule.html) and the service issues the credential to all users who match the rule.

if `management.mode` is `MANAGED`, you [create a user credential](user-credentials/create-user-credential.html) or [update a user credential](user-credentials/update-a-user-credential.html) and the service issues the credential to that user.

### Data source

if `management.mode` is `AUTOMATIC`, you can define `Alphanumeric Text` fields, but the value of the field is fixed when you [create the credential type (automated)](credential-types/create-credential-type-automated.html). For dynamic values, where the value is assigned at the time a [credential issuance rule](credential-issuance-rules/create-credential-issuance-rule.html) issues the credential, you can define `Directory Attribute` fields where the value is obtained from either standard attributes or custom attributes in the user directory.

if `management.mode` is `MANAGED`, you can define `Alphanumeric Text` fields and you can optionally assign a value when you [create a credential type (managed)](credential-types/create-credential-type-managed.html). However, the key difference of `MANAGED` is that you can assign a value when you [create a user credential](user-credentials/create-user-credential.html) or [update a user credential](user-credentials/update-a-user-credential.html), which overrides any value in the credential type. You can also define `Directory Attribute` fields where the value is obtained from either standard attributes or custom attributes in the user directory and are assigned when you create or update a user credential.

## Issuance protocol

Credential Types support two issuance protocols. By setting `openid4VCI.enabled` to `true`, you can use the [OpenID4VCI protocol](#credential-type-openid4vci-protocol). The default is [Native protocol](#credential-type-native-protocol). Note that [issuance method](#credential-type-issuance-method) and [data source](#credential-type-data-source) are independent of protocol. You can use either protocol with either management mode and any data source.

### OpenID4VCI protocol

The Credentials service receives, and responds to, requests for credential issuance using [OpenID for Verifiable Credential Issuance (OpenID4VCI)](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html) API. For authentication this open standard API uses [OAuth 2.0 (RFC6749)](https://www.rfc-editor.org/info/rfc6749). For data models it uses [IETF SD-JWT VC](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0-final.html#I-D.ietf-oauth-sd-jwt-vc). The `openid4VCI` protocol is available only if `openid4VCI.enabled` is `true` on the credential type when you [create an automated credential type](credential-types/create-credential-type-automated.html) or [create a managed credential type](credential-types/create-credential-type-managed.html).

If `management.mode` is `AUTOMATED`, its associated [credential issuance rule](credential-issuance-rules.html) creates the credentials and issues them to all users who match the rule. For OpenID4VCI credentials, the credential remains in the staged queue until the user retrieves it with their wallet using OpenID4VCI.

If `management.mode` is `MANAGED`, you [create a user credential](user-credentials/create-user-credential.html) or [update a user credential](user-credentials/update-a-user-credential.html) to create the credential and the user retrieves it with their wallet using OpenID4VCI.

### Native protocol

The service can also use PingOne `native` protocol. The PingOne native protocol only works with apps that use the [PingOne Neo Native SDKs](../native-sdks/pingone-neo-native-sdks.html), which has more features but is restricted to only supported apps.

If the user's wallet is paired with a PingOne digital wallet app, you use the `native` protocol. The `native` protocol is always available. You can [create an automated credential type](credential-types/create-credential-type-automated.html), and its associated [credential issuance rule](credential-issuance-rules.html) creates and pushes the credential to the paired wallet. Or you can [create a managed credential type](credential-types/create-credential-type-managed.html), or [update a credential type](credential-types/update-a-credential-type.html) and use [create a user credential](user-credentials/create-user-credential.html) or [update a user credential](user-credentials/update-a-user-credential.html) to push it to the paired wallet.

## Versioning

If the updated credential type differs from the existing credential type, the service saves the existing credential type as a Credential Type Version and increments `version.number` in the updated credential type. Credential Type Versions can be read with [Read All Credential Type Versions](credential-types/read-all-credential-types-versions.html).

## Automatic deletion and revocation

Typical behavior for credential types is to automatically revoke user credentials when a credential type, user, or environment is deleted. However, some credential types, such as birth certificates, university degrees, or marriage certificates, should never be automatically revoked even if the user or environment is deleted. You control this using `onDelete.revokeIssuedCredentials` on the [credential type](#credential-types-data-model).

The two revocation behaviors are as follows.

If `onDelete.revokeIssuedCredentials` is true:

* User credentials are revoked and deleted when the credential type is deleted.

* Provisioned credentials are revoked when a user credential is deleted, its credential type is deleted, or its digital wallet is disabled or deleted.

If `onDelete.revokeIssuedCredentials` is false:

* User credentials are only revoked if the issuance rule causes it to be revoked or if [Update a User Credential](user-credentials/update-a-user-credential.html) sets the expiration date.

* Provisioned credentials are revoked if the user credential is revoked (refer to previous item).

The selected deletion and revocation behavior cascades over all resources managed by the service: credential types, issuance rules, staged changes, digital wallet applications, digital wallets, and user credentials.

Environment deleted:

* Delete all credential types

* Delete all issuance rules

* Delete all staged changes

* Delete all digital wallet applications

* Delete all digital wallets

* Delete all user credentials

* Delete all provisioned credentials

* Delete all credential type counts

* Delete environment credential count

Population deleted:

* Remove population from existing issuance rules

Group deleted:

* Remove group from existing issuance rules

User deleted:

* Delete user credential

* Delete digital wallets

Application (associated with digital wallet applications) deleted:

* No impact

Credential type deleted:

* Revoke issued credentials based on delete flag

* Delete issuance rule

Issuance rule deleted

* Delete staged changes

Digital wallet application deleted:

* Disable digital wallets that are of this type

Digital wallet deleted:

* Revoke credentials that were provisioned to the digital wallet based on credential type delete flag

User credential deleted:

* Revoke provisioned credentials based on credential type delete flag

Regardless of the setting of `onDelete.revokeIssuedCredentials`, the service always deletes any pending credentials. (Pending credentials are staged for issue but not provisioned to a wallet because no paired digital wallet exists.)

## Credential schema

When the service creates a credential from a credential type, it maintains the full credential schema, including attributes without corresponding values in the [Create a User Credential](user-credentials/create-user-credential.html) request, so that the credential structure is consistent and predictable. It assigns an empty string (`""`) to any attribute without a value in the request body.

## Credential Types data model

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | **Deprecation notice:** PingOne credentials no longer support `cardDesignTemplate`, which is replaced by fixed templates, and is deprecated. The property `metadata.fields.isVisible`, which controls visibility of fields in `cardDesignTemplate`, is no longer required and is also deprecated. Existing credential types defined by a `cardDesignTemplate` will continue to work, but `cardDesignTemplate` cannot be updated. You can use [Update a Credential Type](credential-types/update-a-credential-type.html) to remove `cardDesignTemplate` and add `visualizationTemplateData` to such credential types. |

| Property                              | Type     | Required          | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | -------- | ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cardDesignTemplate` (deprecated)     | String   | Required          | Immutable | Deprecated, do not use. An SVG formatted image containing placeholders for the credentials fields that need to be displayed in the image. Refer to warning following this table. Not returned with [Read All Credential Types](credential-types/read-all-credential-types.html). You must [Read One Credential Type](credential-types/read-one-credential-type.html) with the `id` of the credential type you want to review.                                                                  |
| `cardType`                            | String   | Optional          | Mutable   | A descriptor of the credential type. Can be non-identity types such as proof of employment or proof of insurance.                                                                                                                                                                                                                                                                                                                                                                              |
| `createdAt`                           | DateTime | N/A               | Read-only | Date and time the credential type was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `deletedAt`                           | DateTime | N/A               | Read-only | Date and time the credential type was deleted. Returned only with [Read One Credential Type](credential-types/read-one-credential-type.html).                                                                                                                                                                                                                                                                                                                                                  |
| `description`                         | String   | Optional          | Mutable   | A description of the credential type.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `environment.id`                      | String   | N/A               | Read-only | PingOne environment identifier (UUID) in which the credential type exists.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `expiration`                          | Object   | Optional          | Mutable   | Object that identifies how to evaluate the expiration date. Requires one and only one of `after`, `timestamp`, or `expression`. Permitted only when `management.mode` is `AUTOMATED`.                                                                                                                                                                                                                                                                                                          |
| `expiration.after`                    | Object   | Required/Optional | Mutable   | Contains the numeric duration and its time unit for calculating an expiration date.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `expiration.after.duration`           | Integer  | Required          | Mutable   | Length of time before transaction timeout expires. Range is from a 1 hour minimum (or equivalent) to an (effectively) unbounded maximum.                                                                                                                                                                                                                                                                                                                                                       |
| `expiration.after.timeUnit`           | String   | Required          | Mutable   | Time unit of transaction timeout. Can be `SECONDS`, `MINUTES`, `HOURS`, or `DAYS`.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `expiration.expression`               | String   | Required/Optional | Mutable   | PingOne Expression Language (PEL) expression that evaluates to an ISO 8601 date. For more information on PEL, refer to [PingOne expression language](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expression_language.html).                                                                                                                                                                                                                                           |
| `expiration.fieldName`                | String   | Required/Optional | Mutable   | On issuance, name of the field in the credential to hold the `expiration` that, when evaluated, returns an expiration date. Must be unique from all fields defined in the `metadata` object of [Create Credential Type](#credentialing-metadata-object-data-model). Required when `expiration.type` is `SOFT`. Optional when `expiration.type` is `HARD` and ignored if used.                                                                                                                  |
| `expiration.timestamp`                | DateTime | Required/Optional | Mutable   | The date and time to expire in ISO 8601 YYYY-MM-DDTHH:MM:SS.sssZ format (milliseconds optional).                                                                                                                                                                                                                                                                                                                                                                                               |
| `expiration.type`                     | String   | Required          | Mutable   | Indicates how expiration of the credential is presented. Can be `SOFT` or `HARD`. A `SOFT` expiration appears as a user-defined field (named in `fieldName`) in the credential but returns no expiration date in [Read One User Credential](user-credentials/read-one-user-credential.html). A `HARD` expiration appears as a standards-based expiration field in the credential and returns an expiration date in [Read One User Credential](user-credentials/read-one-user-credential.html). |
| `id`                                  | String   | N/A               | Read-only | Identifier (UUID) associated with the credential type.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `issuer.id`                           | String   | N/A               | Read-only | The identifier (UUID) of the issuer.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `issuerName`                          | String   | Optional          | Mutable   | Issuer name associated with the card, can differ from title.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `management.mode`                     | String   | Optional          | Mutable   | Management mode of the credential type. Can be `AUTOMATED` (the default) or `MANAGED`. Refer to the note following this table.                                                                                                                                                                                                                                                                                                                                                                 |
| `metadata`                            | Object   | Required          | Mutable   | Contains the names, data types, and other metadata related to the credential. Refer to [metadata object data model](#credentialing-metadata-object-data-model).                                                                                                                                                                                                                                                                                                                                |
| `multiple`                            | Object   | Optional          | Mutable   | Object containing directives that enable you to [Issue multiple credentials to a user based on a directory attribute](#credentialing-issue-multiple-credentials-to-a-user-based-on-a-directory-attribute).                                                                                                                                                                                                                                                                                     |
| `multiple.expression`                 | String   | Required          | Mutable   | A [PingOne Expression Language (PEL)](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expression_language.html) expression that evaluates to a number or array. If an array, calculates the array length for the count. Populates the limit to a variable, `ITERATOR`, available to PEL expressions in `metadata.fields.attribute`.                                                                                                                                       |
| `onDelete.` `revokeIssuedCredentials` | Boolean  | Optional          | Mutable   | Whether user credentials are automatically revoked when a credential type, user, or environment is deleted. Defaults to `true`. For credential types (such as birth certificates, university degrees, or marriage certificates) that should never be automatically revoked even if the user or environment is deleted, set this to `false`.                                                                                                                                                    |
| `openid4VCI`                          | Object   | Optional          | Mutable   | Object containing directives that enable you to configure OpenID for Verifiable Credentials Issuance as an issuance protocol.                                                                                                                                                                                                                                                                                                                                                                  |
| `openid4VCI.enabled`                  | Boolean  | Required          | Mutable   | Whether or not the credential type can use OpenID for Verifiable Credentials Issuance protocol to issue a user's credential.                                                                                                                                                                                                                                                                                                                                                                   |
| `openid4VCI.scope`                    | String   | Required          | Immutable | Scope of the credential type. The scope required of a wallet to request issuance of that credential type. Defaults to `p1:provision:credentials`. Can be a custom scope defined in your environment, but must begin with `p1:provision:credentials:` to be recognized by the service as a valid scope.                                                                                                                                                                                         |
| `title`                               | String   | Required          | Immutable | Title of the credential. Verification sites are expected to be able to request the issued credential from the compatible wallet app using the title.                                                                                                                                                                                                                                                                                                                                           |
| `updatedAt`                           | DateTime | N/A               | Read-only | Date and time the credential type was last updated. Can be null.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `version.id`                          | String   | N/A               | Read-only | Identifier (UUID) of this version of the credential type. The service assigns identifiers.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `version.number`                      | Integer  | N/A               | Read-only | Version of this credential type. The service assigns versions.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `version.uri`                         | String   | N/A               | Read-only | A URI to of this version of the credential type. The service assigns URIs.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `visualizationTemplateData`           | Object   | Optional          | Mutable   | Describes fields in the credential as it appears in the wallet. Refer to [visualizationTemplateData object data model](#credentialing-visualizationtemplatedata-object-data-model).                                                                                                                                                                                                                                                                                                            |

|   |                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Multiple credential issuance is limited to 10 credentials issued for one user for one credential type. You must ensure that the content of the directory attribute will not exceed the 10 credential limit when using your PEL expressions in `multiple.expression` and `metadata.fields.attribute`. |

If `management.mode` is `AUTOMATED`, the credential type is only issued by its associated [credential issuance rule](credential-issuance-rules.html). If `management.mode` is `MANAGED`, the credential type is only issued by [Create a User Credential](user-credentials/create-user-credential.html) or [Update a User Credential](user-credentials/update-a-user-credential.html) API requests. If you change `management.mode` from `AUTOMATED` to `MANAGED` and an associated issuance rule exists, the rule is disabled, but not deleted.

If `management.mode` is `AUTOMATED`, you can value one and only one of the three properties in the `expiration` object and the associated credential issuance rule automatically assigns an expiration date when it issues the credential. If `management.mode` is `MANAGED` and an `expiration` object is present, it causes an error.

If you want to change `management.mode` from `AUTOMATED` to `MANAGED`, but one of the three properties in the `expiration` object is valued, you must remove the `expiration` object. Use [Update the Credential Type](credential-types/update-a-credential-type.html) with no `expiration` object, which removes it from the credential type, and with `management.mode` set to `MANAGED`.

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a credential type, if `management.mode` is `AUTOMATED` and no [credential issuance rule](credential-issuance-rules.html) exists for that credential type, no error occurs. That credential type is simply never issued. |

* If `openid4VCI.enabled` is `true`, you can issue a credential using the `openid4VCI` protocol or the `native` protocol.

* If `openid4VCI` is absent, or `openid4VCI.enabled` is `false`, you can issue a credential only by using the `native` protocol, the `openid4VCI` protocol cannot be used.

### metadata object data model

The `metadata` object is not returned with [Read All Credential Types](credential-types/read-all-credential-types.html). You must [Read One Credential Type](credential-types/read-one-credential-type.html) with the `id` of the credential type you want to review.

| Property                        | Type      | Required          | Mutable | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------- | --------- | ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `backgroundImage`               | String    | Optional          | Mutable | URL to an image of the background to show in the credential. Must be no more than 50 KB in size.                                                                                                                                                                                                                                                                                                       |
| `bgOpacityPercent`              | String    | Optional          | Mutable | Percent opacity of the background image in the credential. High percentage opacity can make reading text difficult.                                                                                                                                                                                                                                                                                    |
| `cardColor`                     | String    | Optional          | Mutable | Color to show on the credential.                                                                                                                                                                                                                                                                                                                                                                       |
| `columns`                       | Integer   | Optional          | Mutable | Number of columns of visible fields to use when displaying the credential. Must be between 1 and 3. Defaults to 1.                                                                                                                                                                                                                                                                                     |
| `description`                   | String    | Optional          | Mutable | Description of the credential.                                                                                                                                                                                                                                                                                                                                                                         |
| `fields`                        | Object\[] | Optional          | Mutable | Array of objects representing the fields.                                                                                                                                                                                                                                                                                                                                                              |
| `fields.attribute`              | String    | Required/Optional | Mutable | Name of the PingOne Directory attribute. Required if `field.type` is `Directory Attribute`, otherwise optional and ignored if used. Refer to [fields.attribute definition](#credentialing-fields-attribute-definition).                                                                                                                                                                                |
| `fields.default`                | String    | Optional          | Mutable | Assigns a default value if a [PingOne Expression Language (PEL)](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expression_language.html) in the `fields.attribute` evaluates to no value.                                                                                                                                                                                       |
| `fields.id`                     | String    | Required          | Mutable | Identifier of the field. Ping Identity recommends that `id` is text formatted as `"<fields.type> → <fields.title>"` to show the type of data expected as well as for what it is used. Examples include: `"Alphanumeric Text → Department"` or `"Directory Attribute → Username"`.                                                                                                                      |
| `fields.fileSupport`            | String    | Optional          | Mutable | Specifies how an image is stored in the credential. Refer to [fields.fileSupport types](#credentialing-fields-filesupport-types).                                                                                                                                                                                                                                                                      |
| `fields.isVisible` (deprecated) | Boolean   | Required          | Mutable | Deprecated, do not use. Whether the field should be visible to viewers of the credential.                                                                                                                                                                                                                                                                                                              |
| `fields.required`               | Boolean   | Optional          | Mutable | Whether the field is required for the credential. An unavailable value when `true` causes an error. An unavailable value when `false` successfully issues the credential with the field empty. Defaults to `false`.                                                                                                                                                                                    |
| `fields.title`                  | String    | Required          | Mutable | Descriptive text when showing the field.                                                                                                                                                                                                                                                                                                                                                               |
| `fields.type`                   | String    | Required          | Mutable | Type of data in the field. Refer to [fields.type types](#credentialing-fields-type-types).                                                                                                                                                                                                                                                                                                             |
| `fields.value`                  | String    | Required/Optional | Mutable | The text to appear on the credential for a `type` of `Alphanumeric Text`. Required if `type` is `Alphanumeric Text` and `management.mode` is `AUTOMATED`, optional if `type` is `Alphanumeric Text` and `management.mode` is `MANAGED`, not allowed if `type` is `Issued Timestamp`, and otherwise ignored if present. Refer to [fields.value restrictions](#credentialing-fields-value-restrictions). |
| `logoImage`                     | String    | Optional          | Mutable | URL to an image of the logo to show in the credential. Must be no more than 25 KB in size.                                                                                                                                                                                                                                                                                                             |
| `name`                          | String    | Optional          | Mutable | Name of the credential.                                                                                                                                                                                                                                                                                                                                                                                |
| `textColor`                     | String    | Optional          | Mutable | Color of the text to show on the credential.                                                                                                                                                                                                                                                                                                                                                           |
| `version`                       | Integer   | Optional          | Mutable | Version of this credential metadata. If not provided, the service assigns a version.                                                                                                                                                                                                                                                                                                                   |

In a wallet, `name` (title) and `description` (subtitle) appear on the credential as submitted to the service. Title always appears because `name` is a required field. Subtitle might or might not appear because `description` is optional. To show title but suppress subtitle, simply do not value `description`. You cannot show subtitle without title.

|   |                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In a credential, the information is stored as name-value pairs where `fields` defines those name-value pairs. Effectively, `fields.title` is the key and its value is: `fields.value`, extracted from the PingOne Directory attribute named in `fields.attribute`, or returned by the PEL expression in `fields.attribute`. |

#### fields.attribute definition

Although `fields.attribute` is always a string type, the service supports two interpretations of its string.

If the string begins with `${` and ends with `}`, the string is interpreted as a [PingOne Expression Language (PEL)](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expression_language.html) expression. As a PEL expression, the string must have `user.` before any attribute names. A PEL expression is essential to [Issue multiple credentials to a user based on a directory attribute](#credentialing-issue-multiple-credentials-to-a-user-based-on-a-directory-attribute). The PEL expression extracts specific elements from the multiple potential credentials found in the attribute.

If the string does not have `${` and `}`, the string is interpreted as the traditional pointer to an attribute name in the directory. That is, you supply an attribute name as the string and the service supplies the value of that attribute to the credential. When used as a pointer, the string does not need `user.` to reference an attribute.

#### fields.fileSupport types

A credential `field` that uses a `type` of `Directory Attribute` can contain a URL that references a JPEG, PNG, or GIF image file uploaded with [Create Image](../platform/images/create-image.html). The credential type is limited to 5 fields that have `fileSupport` set to `BASE64_STRING` or `INCLUDE_FILE`. For credentials, an image file has a maximum size of 2 MB. A credential cannot exceed 2.5 MB including all images.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If an image field is in the credential type, before issuing a credential you must:1) If a suitable standard attribute is unavailable, use [Create Attribute](../platform/schemas/create-attribute.html) to create a custom directory attribute in the user schema that can be referenced by the credential field.

2) Use [Create Image](../platform/images/create-image.html) to make the image available to the service.

3) Use [Update User](../platform/users/users-1/update-user-patch.html) to place the URL returned by [Create Image](../platform/images/create-image.html) in the attribute in the user schema. |

| Type            | Description                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| BASE64\_STRING  | Image is base64-encoded to a string in the credential.                                                             |
| INCLUDE\_FILE   | Image binary is included in the credential.                                                                        |
| REFERENCE\_FILE | Only a URL referencing the image is in the credential. The image binary remains stored external to the credential. |

#### fields.type types

A credential type can have a `fields` with any combination of any number of types.

| Type                | Description                                                                                                                                                                                                                        |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alphanumeric Text   | A static text string of letters, numbers, or punctuation set on `fields.value`.                                                                                                                                                    |
| Issued Timestamp    | Date and time the credential was issued.                                                                                                                                                                                           |
| Directory Attribute | Any PingOne Directory standard or custom attribute. When used in a credential for a user, the service reads that attribute from the user and puts the value in the credential. The name of the attribute is in `fields.attribute`. |

#### fields.value restrictions

The `fields.value` of a credential type has these restrictions based on `management.mode` and `fields.type`:

* If `management.mode` is `AUTOMATED` and `fields.type` is `Alphanumeric Text`, then `fields.value` is required and is assigned the string provided in `fields.value` when the credential type is created.

* if `management.mode` is `MANAGED` and `type` is `Alphanumeric Text`, then `fields.value` is optional and any string provided in `fields.value` is effectively a default that can be replaced by a `data` value in [Create a User Credential](user-credentials/create-user-credential.html) or [Update a User Credential](user-credentials/update-a-user-credential.html).

* Regardless of `management.mode`, if `type` is `Issued Timestamp`, then `fields.value` is not allowed.

### visualizationTemplateData object data model

| Property                      | Type      | Required | Mutable | Description                                                                                                                                                                                                                             |
| ----------------------------- | --------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `displayFields`               | Object\[] | Required | Mutable | Array of fields to show on the credential by the wallet. Must have at least 1 and no more than 3 child objects.                                                                                                                         |
| `displayFields.dataFieldName` | String    | Required | Mutable | The `metadata.fields.title` of a field to show in the credential.                                                                                                                                                                       |
| `displayFields.showFieldName` | Boolean   | Optional | Mutable | Whether the `metadata.fields.name` of the field in `displayFields.dataFieldName` is shown on the credential by the wallet (`metadata.fields.value` of the field in `displayFields.dataFieldName` is always shown). Defaults to `false`. |

## Issue multiple credentials to a user based on a directory attribute

Some customers must issue multiple credentials to a user based on a directory attribute. For example, a bank might issue credit cards in their own name while also issuing credit cards branded for their customers. A user might have more than one of these credit cards in their wallet. The directory service requires an attribute that contains all the credit cards for that user and the service must support credential issuance to any or all of that user's credit cards.

The customer can define a single directory attribute for each user to hold a data object that contains the different accounts owned by the user. Our hypothetical bank wants to support the end user being able to present a verifiable credential that contains only the information from one of these accounts. Although issuance of multiple credentials is initiated by a single directory attribute, definition of the credential type can reference any directory attributes for its `fields`.

The definition of the data object is up to the customer. They then use [PingOne Expression Language (PEL)](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expression_language.html) expressions to retrieve any information as required. The [Credential Types `multiple.expression`](#credential-types-data-model) contains a PEL expression that counts qualifying entries in the data object. The [Credential Types `metadata.fields.attribute`](#credentialing-metadata-object-data-model) contains a PEL expression to retrieve individual data elements that populates a field in the credit type definition.

When you [Apply Credential Issuance Rule Staged Changes](credential-issuance-rules/apply-credential-issuance-rule.html) for a user for a credential type that has multiple configured, the service creates multiple, separate user credentials for the credential type.

An example might better illustrate applying these concepts.

### Example data object

Our hypothetical bank customer, *BigBank*, uses this JSON object, stored as a JSON binary large object (blob), as the source for credit card information.

```json
{
  "credit_cards": {
    "branded": [
      {
        "oem_merchant": "ChainRetailer",
        "customer_id": "0010380",
        "user_id": "1506980157738"
      },
      {
        "oem_merchant": "GlobalOil",
        "customer_id": "0475932",
        "user_id": "1506980157739"
      }
    ],
    "owned": [
      {
        "customer_id": "0010380",
        "int_id" : "03918203198"
      },
      {
        "customer_id": "0475932",
        "int_id" : "03918203100"
      }
    ]
  }
}
```

An administrator at BigBank creates two different credential types, one each for `branded` and `owned`. Each credential type is configured to issue a credential for each JSON object in that array.

### Example API

This demonstrates the API using the `branded` array. An administrator at BigBank created this credential type for `branded`.

A body for [Create a credential type (automated)](credential-types/create-credential-type-automated.html) that creates multiple credentials from the [data object](#credential-types-example-data-object) for the `credit_cards.branded` is:

```json
{
    "title": "Branded Cards",
    "description": "Example for branded cards attribute for BigBank",
    "metadata": {
        "fields": [
            {
                "id": "title",
                "title": "oem_merchant",
                "attribute": "${user.credit_cards['branded'][__ITERATOR__].oem_merchant}",
                "isVisible": true,
                "type": "Directory Attribute",
                "default": "Use this if missing"
            },
            {
                "id": "Directory Attribute -> user_id",
                "title": "user_id",
                "attribute": "${user.credit_cards['branded'][__ITERATOR__].user_id}",
                "isVisible": true,
                "type": "Directory Attribute"
            },
            {
                "id": "Directory Attribute -> customer_id",
                "title": "customer_id",
                "attribute": "${user.credit_cards['branded'][__ITERATOR__].customer_id}",
                "isVisible": true,
                "type": "Directory Attribute"
            }
        ]
    },
    "visualizationTemplateData" : {
        "showTitle" : true,
        "displayFields" : [
            {
                "dataFieldName" : "oem_merchant",
                "showFieldName": true
            },
            {
                "dataFieldName" : "customer_id",
                "showFieldName": true
            }
        ]
    },
    "multiple": {
        "expression": "${user.credit_cards['branded']}"
    }
}
```

The PEL expression in `multiple.expression` returns the count of objects in the `credit_cards.branded` object array of the [data object](#credential-types-example-data-object). This populates the iteration limit of the system `ITERATOR` variable seen in the PEL expressions of the three `metadata.fields.attribute` values.

A body for [Create a credential type (automated)](credential-types/create-credential-type-automated.html) that creates multiple credentials from the [data object](#credential-types-example-data-object) for the `credit_cards.owned` is:

```json
{
    "title": "Owned",
    "description": "Example for owned attribute for BigBank",
    "metadata": {
        "fields": [
            {
                "id": "Directory Attribute -> int_id",
                "title": "int_id",
                "attribute": "${user.credit_cards['owned'][__ITERATOR__].int_id}",
                "isVisible": true,
                "type": "Directory Attribute"
            },
            {
                "id": "Directory Attribute -> customer_id",
                "title": "customer_id",
                "attribute": "${user.credit_cards['owned'][__ITERATOR__].customer_id}",
                "isVisible": true,
                "type": "Directory Attribute"
            }
        ],
        "textColor": "#000000",
        "version": 4
    },
    "visualizationTemplateData" : {
        "showTitle" : true,
        "displayFields" : [
            {
                "dataFieldName" : "customer_id",
                "showFieldName": true
            }
        ]
    },
    "multiple": {
        "expression": "${user.credit_cards['owned']}"
    }
}
```

The PEL expression in `multiple.expression` returns the count of objects in the `credit_cards.owned` object array of the [data object](#credential-types-example-data-object). This populates the iteration limit of the system `ITERATOR` variable seen in the PEL expressions of the two `metadata.fields.attribute` values.

### Important considerations

1. Do not use a multi-valued attribute type. Use a single JSON attribute that contains the necessary arrays.

   When configuring a custom JSON attribute for issuing multiple credentials for a user, the administrator can set it to a multi-valued type, which allows the attribute to be an array of JSON blobs. The PingOne Directory does not guarantee ordering for multi-valued attributes. Multi-valued attributes values are treated as a set rather than a list. This conflicts with how the service determines if a credential has changed, where order is essential. For example, a user has three credentials issued using a multi-valued type of \[A, B, C]. If you add another JSON blob to the user attribute, one might expect the change to look like \[A, B, C, D] (where each letter is a different credential) and issue one more credential to the user. However, with a multi-valued custom JSON attribute, the change might look like \[A, C, D, B]. When the service compares the order, it interprets that two credentials have been updated and one more credential has been added.

   Due to this involuntary re-ordering behavior, multi-valued custom JSON attributes are strongly discouraged.

2. Revocation can be affected by re-ordering.

   If the user has an array like \[A, B, C] so that the service issues three credentials and an administrator then revokes the credential B, credential B remains revoked. If the user is updated to change some values in A, B, and C, A and C update while B remains revoked. However, if the user is updated with a new object or value added to the array such that it becomes \[A, D, B, C], credential C updates to the values of B and a new credential issues for C. No credential will be issued or updated to have the values of D because it is in the second place and the credential for second place was revoked.

   To mitigate this behavior, always add new entries to the end of the arrays in the JSON blob.

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | Unexpected server error.                                              |

---

---
title: Credential Verifications
description: The Credential Verification service receives, and responds to, requests for credential verification using Decentralized Identity Foundation Java Web Token Verifiable Credentials Presentation Profile (DIF JWT-VC Profile). The profile uses such open standards as:
component: pingone-api
page_id: pingone-api:credentials:credential-verifications
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-verifications.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  credential-verifications-session-data-model: Credential Verifications session data model
  credential-verifications-credential-data-data-model: Credential Verifications credential data data model
  credential-verifications-session-data-data-model: Credential Verifications session data data model
  credential-verifications-error-object-data-model: Credential Verifications errors object data model
  credential-verifications-error-codes: Credential Verifications error codes
  response-codes: Response codes
---

# Credential Verifications

The Credential Verification service receives, and responds to, requests for credential verification using Decentralized Identity Foundation Java Web Token Verifiable Credentials Presentation Profile (DIF JWT-VC Profile). The profile uses such open standards as:

* World Wide Web Consortium (W3C) Decentralized Identifiers (DID) for core architecture, data model, and representations

* W3C Verifiable Credentials Data Model for the presentation data model

* DIF Presentation Exchange for credential request

* OpenID for Verifiable Presentations (OpenID4VP ID1) as the base protocol for transportation

Use of [these standards](https://identity.foundation/jwt-vc-presentation-profile/#normative-references) provides interoperability with any app that complies with DIF JWT-VC Profile.

The service can also use PingOne native protocols. The PingOne native protocol only works with apps that use the [PingOne Neo Native SDKs](../native-sdks/pingone-neo-native-sdks.html), which has more features but is restricted to only supported apps.

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Credential Verifications session data model

| Property                          | Type      | Required          | Mutable   | Description                                                                                                                                                                                                                                                                                                                              |
| --------------------------------- | --------- | ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_links.appOpenURL.href`          | String    | N/A               | Read-only | URL to use in a mobile browser to open a compatible wallet app, such as the PingOne Neo Sample App.                                                                                                                                                                                                                                      |
| `_links.qr.href`                  | String    | N/A               | Read-only | URL to return a QR code that, when evaluated, opens the compatible wallet app to this verification.                                                                                                                                                                                                                                      |
| `_links.self.href`                | String    | N/A               | Read-only | URL to return this same response.                                                                                                                                                                                                                                                                                                        |
| `applicationInstance.id`          | String    | Required/Optional | Immutable | Identifier (UUID) of the application running the Wallet SDK on the user's device and registered with the service. When set and `protocol` is `NATIVE`, the service sends a push notification to the application instance using the settings of the digital wallet application.                                                           |
| `createdAt`                       | DateTime  | N/A               | Read-only | Date and time the credential verifications session was created.                                                                                                                                                                                                                                                                          |
| `didMethod`                       | String    | Optional          | Immutable | The decentralized identifier method to use during the credential verification session. Can be `JWK`, the default, or `ION`.                                                                                                                                                                                                              |
| `digitalWalletApplication.id`     | String    | Optional          | Immutable | Identifier (UUID) of the customer's digital wallet app that interacts with the user's digital wallet. When set and `protocol` is `NATIVE`, the service uses the `appOpenURL` defined on the [Digital Wallet App](digital-wallet-apps.html) instead of `shocard.pingone.com`.                                                             |
| `errors`                          | Object\[] | N/A               | Read-only | Array of objects representing errors recorded when attempting an action on a credential. Refer to [Credential Verifications errors object data model](#credential-verifications-error-object-data-model).                                                                                                                                |
| `expiresAt`                       | DateTime  | N/A               | Read-only | Date and time the credential verifications session will expire.                                                                                                                                                                                                                                                                          |
| `id`                              | String    | N/A               | Read-only | Identifier (UUID) of the credential verification session.                                                                                                                                                                                                                                                                                |
| `issuerFilter.dids`               | String\[] | Optional          | Immutable | Array of unique [Decentralized Identifiers (DID)](https://www.w3.org/TR/did-core/). Ignored if `protocol` is `NATIVE`. Refer to the note following this table.                                                                                                                                                                           |
| `issuerFilter.environmentIds`     | String\[] | Optional          | Immutable | Array of PingOne environment identifiers. Refer to the note following this table.                                                                                                                                                                                                                                                        |
| `message`                         | String    | Optional          | Immutable | A message shown to the user by the compatible wallet app to alert the user.                                                                                                                                                                                                                                                              |
| `notification`                    | Object    | Optional          | Immutable | Contains notification information. When `protocol` is `NATIVE` and `applicationInstance.id` is set, permits administrators to customize their push notification.                                                                                                                                                                         |
| `notification.template`           | Object    | Optional          | Immutable | Contains template parameters.                                                                                                                                                                                                                                                                                                            |
| `notification.template.locale`    | String    | Optional          | Immutable | The ISO 2-character language code used for the notification, for example, `en` for English.                                                                                                                                                                                                                                              |
| `notification.template.variables` | Object\[] | Required/Optional | Immutable | An object of name-value pairs that defines the dynamic variables used by the content variant. Required if the template requires variables, otherwise ignored. For more information on dynamic variables, refer to [Dynamic variables](../platform/notifications/notifications-templates.html#notifications-templates-dynamic-variables). |
| `notification.template.variant`   | String    | Optional          | Immutable | The unique user-defined name for the content variant that contains the message text used for the notification. For more information on variants, refer to [Creating custom contents](../platform/notifications/notifications-templates.html#notifications-templates-creating-custom-contents).                                           |
| `protocol`                        | String    | Optional          | Immutable | Protocol to use for verification. Can be `OPENID4VP` or `NATIVE`. If not present, defaults to `NATIVE`.                                                                                                                                                                                                                                  |
| `protocolVersion`                 | String    | Optional          | Immutable | Protocol version. Only applicable to `OPENID4VP`. If not present, defaults to `JWT-VC-Presentation-Profile-v0.0.1`.                                                                                                                                                                                                                      |
| `requestedCredentials`            | Object\[] | Required          | Immutable | Array of objects that contain the type of credentials to verify and the keys to return from the credential. Refer to the important note following this table.                                                                                                                                                                            |
| `requestedCredentials.keys`       | String\[] | Optional          | Immutable | Array of strings that identify the key names for selective disclosure to return from the credential.                                                                                                                                                                                                                                     |
| `requestedCredentials.type`       | String    | Required          | Immutable | Type of credential to verify. Must be the name of a PingOne credential type issued by the credential issuer.                                                                                                                                                                                                                             |
| `status`                          | String    | N/A               | Read-only | Status of the verification request. Can be `INITIAL`, `WAITING`, `EXPIRED` (verification session expired),`VERIFICATION_SUCCESSFUL`, or `VERIFICATION_FAILED`.                                                                                                                                                                           |
| `timeoutSeconds`                  | Integer   | Optional          | Immutable | Maximum number of seconds the presentation session is active. Must be in the range of 30 to 600 seconds. Default is 300 seconds.                                                                                                                                                                                                         |

The service uses `timeoutSeconds` to determine the `expiresAt` timestamp during presentation session creation. The user must receive the push notification or scan the QR code and then share the requested credential before this time. The service returns `status` of `EXPIRED` if the user attempts to share a credential after the `expiresAt` time. The service also returns `status` of `EXPIRED` if the user does not share a credential before the `expiresAt` time.

The digital wallet service uses the `credential_verification` notification template to send a push notification to a digital wallet when a [Create Credential Verification Session (NATIVE - Push Notification)](credential-verifications/create-credential-verification-presentation-session-native-push-notification.html) is created. The `notification.template` object can define a variant and locale for the notification, if needed.

|   |                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Content of `requestedCredentials` differs by `protocol`:- The `protocol` of `OPENID4VP` permits only one credential type per request and ignores `requestedCredentials.keys` if present.

- The `protocol` of `NATIVE` permits multiple credential types per request and uses `requestedCredentials.keys` to return only those selected data fields for each credential type. |

If `issuerFilter.environmentIds` is submitted, the service searches all listed environments for the issuer of the presented credential. If the user presents a credential that is not from one of these issuers, the verification fails with `status` of `VERIFICATION_FAILED`.

If `issuerFilter.dids` is submitted and `protocol` is `OPENID4VP`, the service searches all listed decentralized identifiers (DID) for the issuer of the presented credential. If the user presents a credential that is not from one of these issuers, the verification fails with `status` of `VERIFICATION_FAILED`.

This `issuerFilter.dids` typically contains decentralized identifiers for issuers that are not using PingOne Credentials for JWT-VC issuance. The service supports these three DID methods:

* did:web, <https://w3c-ccg.github.io/did-method-web/>, used for the issuer and verifier

* did:jwk, <https://github.com/quartzjer/did-jwk/blob/main/spec.md>, used for the holder or subject

* did:ion, <https://identity.foundation/ion/> (The service supports only [long-form URIs](https://identity.foundation/sidetree/spec/#long-form-did-uris) for this method)

## Credential Verifications credential data data model

| Property                    | Type      | Required | Mutable   | Description                                                                                                                                                                                               |
| --------------------------- | --------- | -------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_links.self.href`          | String    | N/A      | Read-only | URL to return this verification credential data.                                                                                                                                                          |
| `credentialData`            | Object\[] | N/A      | Read-only | Array of objects containing the data found on the credential.                                                                                                                                             |
| `credentialData.data`       | Object\[] | N/A      | Read-only | Array of objects containing the name-value pairs found on the credential. If a credential has not yet been shared, `status` is `INITIAL` or `WAITING`, then returns as an empty array.                    |
| `credentialData.data.key`   | String    | N/A      | Read-only | Name of the key of a name-value pair found on the credential.                                                                                                                                             |
| `credentialData.data.value` | String    | N/A      | Read-only | Value of a name-value pair found on the credential.                                                                                                                                                       |
| `credentialData.issuerId`   | String    | N/A      | Read-only | Identifier (UUID) of the issuer of the credential verified in the format from the credential issuer.                                                                                                      |
| `credentialData.issuerLogo` | String    | N/A      | Read-only | Base64-encoded logo of the issuer of the credential.                                                                                                                                                      |
| `credentialData.issuerName` | String    | N/A      | Read-only | Name of the issuer of the credential verified.                                                                                                                                                            |
| `credentialData.type`       | String    | N/A      | Read-only | Space-delimited list of the types of credential verified.                                                                                                                                                 |
| `credentialData.types`      | String\[] | N/A      | Read-only | Array of the types of credential verified.                                                                                                                                                                |
| `errors`                    | Object\[] | N/A      | Read-only | Array of objects representing errors recorded when attempting an action on a credential. Refer to [Credential Verifications errors object data model](#credential-verifications-error-object-data-model). |
| `id`                        | String    | N/A      | Read-only | Identifier (UUID) of the verification credential data.                                                                                                                                                    |
| `status`                    | String    | N/A      | Read-only | Status of the verification request. Can be `INITIAL`, `WAITING`, `EXPIRED` (verification session expired), `VERIFICATION_SUCCESSFUL`, or `VERIFICATION_FAILED`.                                           |

## Credential Verifications session data data model

| Property                                   | Type      | Required | Mutable   | Description                                                                                                                                                                                               |
| ------------------------------------------ | --------- | -------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_links.appOpenURL.href`                   | String    | N/A      | Read-only | URL to use in a mobile browser to open a compatible wallet app, such as the PingOne Neo Sample App.                                                                                                       |
| `_links.qr.href`                           | String    | N/A      | Read-only | URL to return a QR code that, when evaluated, opens the compatible wallet app to this verification.                                                                                                       |
| `_links.self.href`                         | String    | N/A      | Read-only | URL to return this verification session data.                                                                                                                                                             |
| `applicationInstance.id`                   | String    | N/A      | Read-only | Identifier (UUID) of the application running the Wallet SDK on the user's device and registered with the service.                                                                                         |
| `errors`                                   | Object\[] | N/A      | Read-only | Array of objects representing errors recorded when attempting an action on a credential. Refer to [Credential Verifications errors object data model](#credential-verifications-error-object-data-model). |
| `id`                                       | String    | N/A      | Read-only | Identifier (UUID) of the verification session data.                                                                                                                                                       |
| `status`                                   | String    | N/A      | Read-only | Status of the verification request. Can be `INITIAL`, `WAITING`, `EXPIRED` (verification session expired), `VERIFICATION_SUCCESSFUL`, or `VERIFICATION_FAILED`.                                           |
| `verifiedData`                             | Object\[] | N/A      | Read-only | Array of objects containing the data found on the credential.                                                                                                                                             |
| `verifiedData.data`                        | Object    | N/A      | Read-only | Object containing the name-value pairs found on the credential. If a credential has not yet been shared, `status` is `INITIAL` or `WAITING`, then returns as an empty array.                              |
| `verifiedData.data.key`                    | String    | N/A      | Read-only | Name of the key of a name-value pair found on the credential.                                                                                                                                             |
| `verifiedData.data.value`                  | String    | N/A      | Read-only | Value of a name-value pair found on the credential.                                                                                                                                                       |
| `verifiedData.metaData`                    | Object    | N/A      | Read-only | Contains metadata associated with the credential.                                                                                                                                                         |
| `verifiedData.metaData.issuanceDate`       | String    | N/A      | Read-only | The date and time the credential was issued in ISO 8601 YYYY-MM-DDTHH:MM:SS.sssZ format (milliseconds optional).                                                                                          |
| `verifiedData.metaData.issuerId`           | String    | N/A      | Read-only | Identifier (UUID) of the issuer of the credential verified in the format from the credential issuer.                                                                                                      |
| `verifiedData.metaData.issuerLogo`         | String    | N/A      | Read-only | Base64-encoded logo of the issuer of the credential.                                                                                                                                                      |
| `verifiedData.metaData.issuerName`         | String    | N/A      | Read-only | Name of the issuer of the credential verified.                                                                                                                                                            |
| `verifiedData.metaData.verificationStatus` | String    | N/A      | Read-only | Verification status of the credential. Can be `VALID` or `INVALID`.                                                                                                                                       |
| `verifiedData.type`                        | String    | N/A      | Read-only | Space-delimited list of the types of credential verified.                                                                                                                                                 |
| `verifiedData.types`                       | String\[] | N/A      | Read-only | Array of the types of credential verified.                                                                                                                                                                |

### Credential Verifications errors object data model

| Property         | Type   | Required | Mutable   | Description                                                                                                                                         |
| ---------------- | ------ | -------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `errors.code`    | String | N/A      | Read-only | A code that indicates the error encountered by the service. Refer to [Credential Verifications error codes](#credential-verifications-error-codes). |
| `errors.target`  | String | N/A      | Read-only | The part of the credential that caused the error encountered by the service.                                                                        |
| `errors.message` | String | N/A      | Read-only | A message that describes the error encountered by the service.                                                                                      |

## Credential Verifications error codes

| Code                           | Message                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REQUESTED\_CREDENTIAL\_MISSING | One or more of the requested credential types is not included in the presentation from the user.                                                                                                                                                                                                                                                                                                                                             |
| REQUESTED\_FIELD\_MISSING      | One or more of the requested fields for one or more credential types is not included in the presentation from the user.                                                                                                                                                                                                                                                                                                                      |
| INVALID\_TOKEN                 | The `idToken` presented by the user's wallet is not valid (format or signature error).                                                                                                                                                                                                                                                                                                                                                       |
| INVALID\_CREDENTIAL            | One or more of the credentials presented by the user could not be validated. Many different errors can cause this. A more specific error is returned in the errors array of the [Read Credential Verification Credential Data](credential-verifications/read-credential-verification-credential-data.html) or [Read Credential Verification Session Data](credential-verifications/read-credential-verification-session-data.html) response. |
| UNEXPECTED\_ERROR              | An unexpected error occurred during credential verification.                                                                                                                                                                                                                                                                                                                                                                                 |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | Unexpected server error.                                              |

---

---
title: Credential Verifier Decentralized Identifiers
description: W3C defines Decentralized IDs (DIDs) as a means to identify an entity in a decentralized ecosystem. See the W3C DIDs spec for details. An entities DID is represented as a string and used in the different ID fields, such as issuer, subject, audience, or holder, for Java Web Tokens (JWTs), Verifiable Credentials (VCs), and other JSON objects. The DID is used to find public keys for the entity as well as optional information about how to interact with the entity.
component: pingone-api
page_id: pingone-api:credentials:credential-verifier-decentralized-identifiers
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-verifier-decentralized-identifiers.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingone-hosted-verifier-didweb: PingOne hosted verifier did:web
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  credential-verifier-did-data-models: Credential verifier DID data models
---

# Credential Verifier Decentralized Identifiers

W3C defines Decentralized IDs (DIDs) as a means to identify an entity in a decentralized ecosystem. See the W3C DIDs spec for details. An entities DID is represented as a string and used in the different ID fields, such as issuer, subject, audience, or holder, for Java Web Tokens (JWTs), Verifiable Credentials (VCs), and other JSON objects. The DID is used to find public keys for the entity as well as optional information about how to interact with the entity.

The DID specification supports multiple ways to store and represent the DID. Every DID is a colon-separated string with the literal did, a method name, and method-specific data. W3C maintains a list of all of the current DID methods.

A `did:web` identifier is used in the signed JWT that is returned by Credentials Verifications when the wallet requests the Authorization Request. The wallet then resolves the `did:web` to get the public keys and verify the JSON Web Token (JWT) signature. This supports environments with and without custom domains.

Unlike in Credentials Issuance, a different DID identifier is used for every presentation session because the JSON Web Key Set (JWKS) used is different for each session.

PingOne Credentials uses `did:web` for the issuer and verifier and `did:ion` for the holder or subject. PingOne also supports `did:ion` for all parties for backwards compatibility.

## PingOne hosted verifier did:web

The service supports retrieving the `did:web` documents of verifiers hosted by PingOne on both the standard `auth.pingone.com` domain (and regional variants by top level domain, TLD) and custom domains. The DID document contains the public keys for the verifier and optional information about how to interact with the verifier. To retrieve the DID document:

1. The DID of a verifier hosted on the standard `auth.pingone.com` domain is in the format:

   * `did:web:`

   * `auth.pingone.com:`

   * UUID of the verifier's environment

   * `:verifier:`

   * UUID of the presentation session

   * `#`

   * UUID of the signing key

     For an environment UUID `8fd6a2f0-c568-4de8-a319-eb8ddff49dff` and presentation session UUID `d08008f2-d9dc-4d93-8eeb-9d2f7f50b620`, the corresponding URL to retrieve the DID document is:

     ```none
     https://auth.pingone.com/8fd6a2f0-c568-4de8-a319-eb8ddff49dff/verifier/d08008f2-d9dc-4d93-8eeb-9d2f7f50b620/did.json
     ```

2. The DID of a verifier hosted on a custom domain is in the format:

   * `did:web:`

   * the verifier's custom domain

   * `:verifier:`

   * UUID of the presentation session

   * `#`

   * UUID of the signing key

     For a custom domain `verifier.customerdomain.com` and presentation session UUID `d08008f2-d9dc-4d93-8eeb-9d2f7f50b620`, the corresponding URL to retrieve the DID document is:

     ```none
     https://verifier.customerdomain.com/d08008f2-d9dc-4d93-8eeb-9d2f7f50b620/did.json
     ```

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Credential verifier DID data models

| Property                          | Type   | Required | Mutable   | Description                                                                                                                                                                                                                           |
| --------------------------------- | ------ | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `@context`                        | String | N/A      | Read-only | URL to the DID scheme                                                                                                                                                                                                                 |
| `id`                              | String | N/A      | Read-only | A unique identifier that conforms to [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax)                                                                                                                                         |
| `verificationMethod.id`           | String | N/A      | Read-only | A unique identifier that conforms to [DID URL Syntax](https://www.w3.org/TR/did-core/#did-url-syntax)                                                                                                                                 |
| `verificationMethod.controller`   | String | N/A      | Read-only | The entity that controls the DID in [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax). In PingOne Credentials, the method-specific data is always equal to the domain part of the request URL                                  |
| `verificationMethod.type`         | String | N/A      | Read-only | Name for the type of JWK represented                                                                                                                                                                                                  |
| `verificationMethod.publicKeyJwk` | String | N/A      | Read-only | A JSON Web Key that conforms to RFC 7517, [JSON Web Key (JWK)](https://www.rfc-editor.org/rfc/rfc7517). The contents vary by algorithm as discussed in RFC 7518, [JSON Web Algorithms (JWA)](https://www.rfc-editor.org/rfc/rfc7518). |
| `authentication`                  | String | N/A      | Read-only | A unique identifier that conforms to [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax) including in its fragment a UUID for the key of the `verificationMethod.publicKeyJwk`                                                   |
| `assertionMethod`                 | String | N/A      | Read-only | A unique identifier that conforms to [DID Syntax](https://www.w3.org/TR/did-core/#did-syntax) including in its fragment a UUID for the key of the `verificationMethod.publicKeyJwk`                                                   |

---

---
title: Customer Credential Signing API Definition
description: If you choose to sign your credentials with your private key, you must implement an API that conforms to this design. You must Update Credential Issuer Profile and provide the URL of your API in credentialSigning.url.
component: pingone-api
page_id: pingone-api:credentials:credential-signing-keys/customer-credential-signing-api-definition
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-signing-keys/customer-credential-signing-api-definition.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  customer-credential-signing-request-data-model: Customer credential signing request data model
  customer-credential-signing-response-data-model: Customer credential signing response data model
---

# Customer Credential Signing API Definition

If you choose to sign your credentials with your private key, you must implement an API that conforms to this design. You must [Update Credential Issuer Profile](../credential-profiles/update-credential-issuer-profile.html) and provide the URL of your API in `credentialSigning.url`.

The request for signing contains an array of payloads that you must sign. Each payload has a key ID and a corresponding credential signing key ID. The key ID, `kid`, you define in the public signing key submitted in the request to [Create Customer Signing Public Key](create-customer-signing-public-key.html). The credential signing key ID, `credentialSigningKeyId`, the PingOne service assigns in the response to [Create Customer Signing Public Key](create-customer-signing-public-key.html).

## Customer credential signing request data model

| Property                          | Type      | Required | Mutable   | Description                                                                                                                                                                                                               |
| --------------------------------- | --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `purpose`                         | String    | Optional | Immutable | A free-format string for auditing.                                                                                                                                                                                        |
| `payloads`                        | Object\[] | Required | Immutable | Array of payload objects that you must sign.                                                                                                                                                                              |
| `payloads.payload`                | String    | Required | Immutable | Opaque data to be individually signed by your service using your private key.                                                                                                                                             |
| `payloads.kid`                    | String    | Required | Immutable | The key ID in the public credential signing key JWK, submitted to the credential signing service, to use to sign the payload.                                                                                             |
| `payloads.credentialSigningKeyId` | String    | Required | Immutable | Unique identifier (UUID) of the credential signing key to use to sign the payload. PingOne credentialing service generates this UUID for each public credential signing key you submit to the credential signing service. |

In `payloads.payload`, the service supplies the base64-encoded JWT header, derived from the public key the service expects you to use, and the base64-encoded payload, the opaque credential object to sign, separated by a literal period.

You can use either `payloads.kid` or `payloads.credentialSigningKeyId` to find the correct private key for signing.

## Customer credential signing response data model

| Property             | Type      | Required | Mutable   | Description                                                                           |
| -------------------- | --------- | -------- | --------- | ------------------------------------------------------------------------------------- |
| `signedData`         | Object\[] | Required | Immutable | Array of signed payload objects.                                                      |
| `payloads.payload`   | String    | Required | Immutable | The `payload` sent in the request.                                                    |
| `payloads.signature` | String    | Required | Immutable | The base64-encoded signature you generated using your private credential signing key. |

Learn more about Java Web Tokens (JWT) in [Introduction to JSON Web Tokens (JWT)](https://docs.pingidentity.com/developer-resources/dev_jwt_jose_overview.html).

---

---
title: Customer Credential Signing Request
description: The credential signing service uses the POST {{customerCredentialSigningApiUrl}} operation to send credentials for signing. You must define your credential signing API URL to the service in credentialSigning.url when you Update Credential Issuer Profile.
component: pingone-api
page_id: pingone-api:credentials:credential-signing-keys/customer-credential-signing-api-definition/customer-credential-signing-request
canonical_url: https://developer.pingidentity.com/pingone-api/credentials/credential-signing-keys/customer-credential-signing-api-definition/customer-credential-signing-request.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Customer Credential Signing Request

##

```none
POST {{customerCredentialSigningApiUrl}}
```

The credential signing service uses the POST `{{customerCredentialSigningApiUrl}}` operation to send credentials for signing. You must define your credential signing API URL to the service in `credentialSigning.url` when you [Update Credential Issuer Profile](../../credential-profiles/update-credential-issuer-profile.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity makes available linkcredentials:working-with-pingone-apis/postman-and-pingone/download-the-pingone-postman-collections.adoc#credentials-collection\[The PingOne Credentials API collections] to download. In those Postman collections for this request, **Auth Type** on the *Authorization* tab is set to `Noauth` solely for testing.In your implementation, select the authorization suitable to your requirements. |

> **Collapse: Request Model**
>
> Refer to [Customer credential signing request data model](../customer-credential-signing-api-definition.html#customer-credential-signing-request-data-model) for full property descriptions.
>
> | `purpose`                         | String    | Optional |
> | --------------------------------- | --------- | -------- |
> | `payloads`                        | Object\[] | Required |
> | `payloads.payload`                | String    | Required |
> | `payloads.kid`                    | String    | Required |
> | `payloads.credentialSigningKeyId` | String    | Required |

### Headers

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "purpose": "Sign Credential payload",
    "payloads": [
        {
            "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
            "kid": "{{credentialSigningKeyKid}}",
            "credentialSigningKeyId": "{{credentialSigningKeyID}}"
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
curl --location --globoff '{{customerCredentialSigningApiUrl}}' \
--header 'Content-Type: application/json' \
--data '{
    "purpose": "Sign Credential payload",
    "payloads": [
        {
            "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
            "kid": "{{credentialSigningKeyKid}}",
            "credentialSigningKeyId": "{{credentialSigningKeyID}}"
        }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{customerCredentialSigningApiUrl}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"    ""purpose"": ""Sign Credential payload""," + "\n" +
@"    ""payloads"": [" + "\n" +
@"        {" + "\n" +
@"            ""payload"": ""{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}""," + "\n" +
@"            ""kid"": ""{{credentialSigningKeyKid}}""," + "\n" +
@"            ""credentialSigningKeyId"": ""{{credentialSigningKeyID}}""" + "\n" +
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

  url := "{{customerCredentialSigningApiUrl}}"
  method := "POST"

  payload := strings.NewReader(`{
    "purpose": "Sign Credential payload",
    "payloads": [
        {
            "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
            "kid": "{{credentialSigningKeyKid}}",
            "credentialSigningKeyId": "{{credentialSigningKeyID}}"
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
POST / HTTP/1.1
Host: {{customerCredentialSigningApiUrl}}
Content-Type: application/json

{
    "purpose": "Sign Credential payload",
    "payloads": [
        {
            "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
            "kid": "{{credentialSigningKeyKid}}",
            "credentialSigningKeyId": "{{credentialSigningKeyID}}"
        }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"purpose\": \"Sign Credential payload\",\n    \"payloads\": [\n        {\n            \"payload\": \"{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}\",\n            \"kid\": \"{{credentialSigningKeyKid}}\",\n            \"credentialSigningKeyId\": \"{{credentialSigningKeyID}}\"\n        }\n    ]\n}");
Request request = new Request.Builder()
  .url("{{customerCredentialSigningApiUrl}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{customerCredentialSigningApiUrl}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "purpose": "Sign Credential payload",
    "payloads": [
      {
        "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
        "kid": "{{credentialSigningKeyKid}}",
        "credentialSigningKeyId": "{{credentialSigningKeyID}}"
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
  'url': '{{customerCredentialSigningApiUrl}}',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "purpose": "Sign Credential payload",
    "payloads": [
      {
        "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
        "kid": "{{credentialSigningKeyKid}}",
        "credentialSigningKeyId": "{{credentialSigningKeyID}}"
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

url = "{{customerCredentialSigningApiUrl}}"

payload = json.dumps({
  "purpose": "Sign Credential payload",
  "payloads": [
    {
      "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
      "kid": "{{credentialSigningKeyKid}}",
      "credentialSigningKeyId": "{{credentialSigningKeyID}}"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{customerCredentialSigningApiUrl}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json'
));
$request->setBody('{\n    "purpose": "Sign Credential payload",\n    "payloads": [\n        {\n            "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",\n            "kid": "{{credentialSigningKeyKid}}",\n            "credentialSigningKeyId": "{{credentialSigningKeyID}}"\n        }\n    ]\n}');
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

url = URI("{{customerCredentialSigningApiUrl}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "purpose": "Sign Credential payload",
  "payloads": [
    {
      "payload": "{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}",
      "kid": "{{credentialSigningKeyKid}}",
      "credentialSigningKeyId": "{{credentialSigningKeyID}}"
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"purpose\": \"Sign Credential payload\",\n    \"payloads\": [\n        {\n            \"payload\": \"{{credentialSigningHeaderBase64}}.{{credentialSigningPayloadBase64}}\",\n            \"kid\": \"{{credentialSigningKeyKid}}\",\n            \"credentialSigningKeyId\": \"{{credentialSigningKeyID}}\"\n        }\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{customerCredentialSigningApiUrl}}")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")

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
    "signedData": [
        {
            "payload": "ewogICAgImFsZyI6ICJSUzI1NiIsCiAgICAidHlwZSI6ICJKV1QiCn0=./9j/4AAQSkZJRgABAQEAYABgAAD/4QBoRXhpZgAATU0AKgAAAAgABAEaAAUAAAABAAAAPgEbAAUAAAABAAAARgEoAAMAAAABAAIAAAExAAIAAAARAAAATgAAAAAAAABgAAAAAQAAAGAAAAABcGFpbnQubmV0IDQuMy4xMAAA/9sAQwABAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB/9sAQwEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEB/8AAEQgAIAAgAwEhAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8A/r+/4KW/t8eBv+CbX7KmuftNeN7Hwn4ha0+Inwf+HHhjwP4q+J2j/Cc+Nta+J/xM8M+EtYt9B8Savo3iM3eqeBfAF941+MGpaLp+gand3Xg/4beKby6fRdFsNW8SaN+EH/EWH8AP+iUfB7/xNPwX/wDOor5PiLiHM8mrYalgOG8fnkK1KdSpVwjxCjQlGfKqc/Y4DFrmkveXNKDt9l7n9BeDXg9wN4l5ZnOO4s8auFPC3EZZj6GEwmX8RQyiVbNaNXDutPGYf+0uK+HpqlRn+5l7KjiIc+9WL9w7v4W/8HS/7M/j34m/DnwL4k8MfAr4eeHfGnjvwh4T17x/rf7aPgBtF8DaL4j8Qafo+qeMNXW/+HeiWLaX4ZsbyfWtQF7rWkWhtLKUXGqWEO+7i/Wpv+Cs/wCyU37Tng/9mCw1Hxfr+q/EK4+F8PgT4veE7Lwl4x+BnjGL40+B/C/jv4Wap4a8ZeFfGesazrXh/wAbWPjTwvpujeJdP8KXHh973WLbU59Tg8JLP4mi4sLxnUjhKeKzvIcyyRV81wmVUIVYVKkpzxdOrUWJmsRh8DNYel7GSqOjCvUvbkpybsvp8/8Aoz4Wrn+LyHwu8WOCvE+plfAPEHH+a4rAV8Hg6OHwvD+NwGCqZNQnlGb8V4eWcY+WY0KmChmWJynBuEajr4ujCKqP5i/4OMtW0/8A4dcfEfwHf+ENb8aRfE/4yfs06Te2GmeH4fEWjaP4P+F/xz8EftIfFrxf8QbWaTbp/wAM/B3wW+B/xI8SeOtfls9Q0vw9oWm3OseJY9P8J2eva7pP+cboH/BLPwTp3ja01fXPidrHiPwJa6xPev4Lfw3HpWrajpKSTSadoupeMbHxF/16Qa1qWl+HdKudRtkvRpKeHLq6tbvTvP4w4yxXDmLlSw+ElXWKwlTD0qtWpKnSw2OowjWjXpw5KsMRGMMfQdei/YznyU4upGHLKX2H0cfo15H408PUMfnHENLKXkXEWEzjHYDA4KnjMfnXC+Z4ivltbK8ZiPrWAxWUVa2K4TzWGU5jD+0cNhlisbWhhK+I9tSo8Fp37Kf7McP7ZNj8MdE8aeJIpPC1na+P9X+GXiTRNE1Xw7q2oQ3KeJLT4f6Z4p13UoNQ1ezHh7UdD1XUPDk3g/xhPe+DLHxAL/xv/arX7aH/AKol5/wSl/Zt+KviTxn8U/2tdK/4aL+OfxC8UXWv+JvH1nfePfg14b0/SrWw03w54O8EeDPh94B+Iot9I8MeDfB+haHo1rd+J/EHjbxprd/DqWt6/wCLr99Qt7LTYyylieMnTo8TYal9Tw+VZLmcMJQq4mEMdiMfHM1h8w9tSnQeGjHD+1p1cJR9rGdZxc8Slh1h49PG+YZL9GqGMzLwOzrHviTOeP8AxM4HxPEOa4HJa+I4XyfhGtwNPOOEP7Px2FzannVWtnLwOLwPEGZ/UamHyyFeGFyWUs3ec1fzS/4J7f8ABLz9ou/8cftAw/8ABQ74ef298Hvij8GPjd8PdR8NeNvizYeNfEninxZ+1BB4e8J/Gnxn4c1n4feMdf1jwf4o8YfC/QNb8GfEP4kWfinwf8Q9WsPEmi2Wlanq8EeqXOg/hDdf8E4v+Chnwj8M/B3w38bP2cvHd78XPGfw7bW9T0H4enwh8X9au9T8F6f4IsPiXq91pfwL1jxva6RpekeJvG+gWU2oPBYaFLd65ZW+jyzxsEj+OzrhTPafCmVvEYCrXzLD5ljauLjSrQxeKjTx0sLhKCmqNWo8XVqvD4SMVQ+szpUY04t04xqRh/SHhn9IDwrxf0gOO6eUcWYHKuCM44K4Zy/h2tjsuxPD+RVcXwrRz7iHNJYepmOBwUOH8DgIZxxBXrPNFk2Fx2Y1sbVpwxlevg6+I1I/+CVXxW8CN8PP2jvi14L+H/7Mo/aG8bn4Dy/Ez46yax4E1bw/faHpuoar4Sk+KWjW3hzWfGHgnwx42uNG1vR9K8U33hsQi28D6brPxIufDXw6sPh34nvv60P2c/8Agrb8J/2qf2sE/Zx+DXwq+J/iDwe/hjxdq/8Awuu4sobPSra/8J3t5/xNNW8H+VNqnh34YeItLh0uHw9458SappHiWTxp4o8MeCtY+G2jXGqf2pB6XCGYYzhzHRwOcwr18xzueQYDCYNSk8RgMBQw01TrYqnKCWHo0KeMp0VQ0rKphsY6sIKkqlX4v6RXCHDvjPwtW4r8NcRlmVcGeF2G8XeK+IeJJ0qEMm4r4tzTO8NLGZZkWMoYmcs3zTNsXw3jMwlmyjLLamFzrhqGBxWKnjpYTL/1jr+a/wCL/wAPf+C2Fj+3J8TP2ivg34B/tDwfZ+KPEvgz4Z+GtZ+Jvwi1n4bX3wSt/EXg1YNNsfA/jz4sXOqeBf8AhbGl/C3wN4j+JF54RPgPxbfa8+o3VldeF7iWO0sfuuMaXElbD5d/q5S9rXoZhDF4he2w9GMoUKc/ZU6scTXo0q1GVWanKk1NqpSo1Y8k6cZH8o/RuzDwWy7OeNP+I04/6jlOacH4rIMpqf2Zm+YVaWJzXF4dY/GYCtkmVZlj8szOjgcPPDUMdCeGpywWOzHA11isPjKtB/rvpHwp8fftf/sXy/Cr9u7wBpfgDx98TtL1vT/iZ4P+GOux21p4Wu9D+IOoan8O9b8LazY+K/iFYnVNPsdC8FeMY4r3X/E+i3GtJLp/iDSLrSZdR8M10/7H37G/wc/Yx+GVn4F+GHh3S4fEWraX4Wb4o+P4rbVI9a+Jvi/w/wCH7XR7rxLqC63rvia+0TS7y+XVta0jwPp2tSeFvCV34g1saFaQzatqt3f+jhsohicblfEOZYeFPO6OUU8JXpwk5UsNXqRdSuqHLWqQXs54jGUObnr89KqlGraLlU+PzvxGxOS8McdeD/Beb4rGeGGZeIeN4gyzGYilTo5hneVYKtDCZVUzb2uW4LFS+uYXKOHM0dBYfK1hsdgqjq4BSrRpYT//2Q==",
            "signature": "ERCkCxDvULSODX3UXC3qbpyu6WvGkp_HsDbMUP3Yt_cdagLMQNrRkBqrjDJRh4CWmFxTKtuHvsY2v4p_7b0JJCD_MkJ6_UctwEymDNcRa1ms95_xtvSz8-XQmwqJ8ES7mD-_8qfDlgDl7upyYkUul3HxzRb3WzgaeSU_CIFQoCRHhaknMscpIpTKbZI1GE8Ghxe6EDmOPN34FoMbnjJbrEkigpymnBdhCRev3LbDLhw-7f45D1WBmeJ5kzOCqKtK6bl7yYHk03XPzjov3xdtoMCOHT9DfhpuTwaqR4SL3sc-Uc2GumoQNM5cpYP_1l1IgyZ2Ud2kpUdvQ1CEDbOaqw"
        }
    ]
}
```
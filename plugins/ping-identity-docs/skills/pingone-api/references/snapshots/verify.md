---
title: Complete Verification Documents
description: Complete processing of all documents submitted to a PingOne Verify verification transaction and prohibit further submissions
component: pingone-api
page_id: pingone-api:verify:verify-documents/complete-verification-documents
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-documents/complete-verification-documents.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Complete Verification Documents

##

Required permission:

* [idverifications:update:document](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-update-document "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents` request with a Content-Type of `application/vnd.pingidentity.documents.complete+json` to have the service complete processing all documents submitted to a verification transaction. This request requires no body.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This completes processing documents that have been collected and prohibits submitting more documents. This returns an error if not enough documents have been provided for the required verification types. |

For a list of permitted document types and the format of their values, refer to [Document types and values](index.html#verify-document-types-and-values).

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users/index.html), especially [User operations](../../platform/users/users-1/index.html).

* [Create a verify transaction](../verify-transactions/create-verify-transaction.html) to get a `transactionID` for the endpoint. Refer also to [Verify Transactions](../verify-transactions/index.html).

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.documents.complete+json

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
curl --location --globoff --request POST '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents' \
--header 'Content-Type: application/vnd.pingidentity.documents.complete+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.documents.complete+json");
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.documents.complete+json")
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
POST /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.documents.complete+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.documents.complete+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.documents.complete+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.documents.complete+json",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.documents.complete+json',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"

payload = {}
headers = {
  'Content-Type': 'application/vnd.pingidentity.documents.complete+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.documents.complete+json',
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.documents.complete+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.documents.complete+json", forHTTPHeaderField: "Content-Type")
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb/documents/a7753108-2db2-4e38-8360-ef530e3169b3"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049"
        },
        "verifyTransaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb"
        }
    },
    "id": "a7753108-2db2-4e38-8360-ef530e3169b3",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "49825b76-e1df-4cdc-b973-0c580f1cb049"
    },
    "verifyTransaction": {
        "id": "e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb"
    },
    "type": "Selfie",
    "value": "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",
    "status": "PROCESSED",
    "source": {
        "provider": "AUTHENTICATED_CLIENT"
    },
    "createdAt": "2022-08-26T12:27:28.886Z",
    "updatedAt": "2022-08-26T12:27:28.886Z"
}
```

---

---
title: Create Verification Document
description: Submit a document to a PingOne Verify verification transaction
component: pingone-api
page_id: pingone-api:verify:verify-documents/create-verification-documents
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-documents/create-verification-documents.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Verification Document

##

Required permission:

* [idverifications:create:document](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-create-document "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents` request to submit a document to a verification transaction.

> **Collapse: Request Model**
>
> | Property | Type   | Required |
> | -------- | ------ | -------- |
> | `type`   | String | Required |
> | `value`  | String | Required |

For a list of permitted document types and the format of their values, refer to [Document types and values](index.html#verify-document-types-and-values). Note that `Email` and `Phone Number` are not supported document types for this endpoint.

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users/index.html), especially [User operations](../../platform/users/users-1/index.html).

* [Create a verify transaction](../verify-transactions/create-verify-transaction.html) to get a `transactionID` for the endpoint. Refer also to [Verify Transactions](../verify-transactions/index.html).

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "type": "Selfie",
    "value": "{{base64EncodedData}}"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "type": "Selfie",
    "value": "{{base64EncodedData}}"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""type"": ""Selfie""," + "\n" +
@"    ""value"": ""{{base64EncodedData}}""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"
  method := "POST"

  payload := strings.NewReader(`{
    "type": "Selfie",
    "value": "{{base64EncodedData}}"
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
POST /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "type": "Selfie",
    "value": "{{base64EncodedData}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"type\": \"Selfie\",\n    \"value\": \"{{base64EncodedData}}\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "type": "Selfie",
    "value": "{{base64EncodedData}}"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "type": "Selfie",
    "value": "{{base64EncodedData}}"
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"

payload = json.dumps({
  "type": "Selfie",
  "value": "{{base64EncodedData}}"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "type": "Selfie",\n    "value": "{{base64EncodedData}}"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "type": "Selfie",
  "value": "{{base64EncodedData}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"type\": \"Selfie\",\n    \"value\": \"{{base64EncodedData}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb/documents/a7753108-2db2-4e38-8360-ef530e3169b3"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049"
        },
        "verifyTransaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb"
        }
    },
    "id": "a7753108-2db2-4e38-8360-ef530e3169b3",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "49825b76-e1df-4cdc-b973-0c580f1cb049"
    },
    "verifyTransaction": {
        "id": "e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb"
    },
    "type": "Selfie",
    "value": "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",
    "status": "COLLECTED",
    "source": {
        "provider": "AUTHENTICATED_CLIENT"
    },
    "createdAt": "2022-08-26T12:27:28.886Z",
    "updatedAt": "2022-08-26T12:27:28.886Z"
}
```

---

---
title: Create Verify Policy
description: Create a PingOne Verify policy in a specified environment to define identity verification requirements and parameters
component: pingone-api
page_id: pingone-api:verify:verify-policy/create-verify-policy
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-policy/create-verify-policy.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-06
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
  example-response-2: Example Response
  example-response-3: Example Response
  example-response-4: Example Response
---

# Create Verify Policy

##

Required permission:

* [idverifications:create:verifyPolicy](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-create-verifyPolicy "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/verifyPolicies
```

Create a new verify policy for the specified environment with the `POST {{apiPath}}/v1/environments/{{envID}}/verifyPolicies` request.

The first example response returns when `.provider.auto` is `Veriff`. The second example response returns when `.provider.auto` is not provided. The third example shows an Aadhaar-enabled policy.

### Prerequisites

* Refer to [Verify Policies](index.html) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Verify policy data model](index.html#verify-verify-policy-data-model) for full property descriptions.
>
> | Property                        | Type     | Required |
> | ------------------------------- | -------- | -------- |
> | `biometricEnrollment`           | Object   | Optional |
> | `dataBasedIdentityVerification` | Object   | Optional |
> | `default`                       | Boolean  | Optional |
> | `description`                   | String   | Optional |
> | `deviceOwnership`               | Object   | Optional |
> | `email`                         | Object   | Optional |
> | `environment.id`                | String   | Required |
> | `facialComparison`              | Object   | Optional |
> | `governmentId`                  | Object   | Optional |
> | `id`                            | String   | Required |
> | `identityRecordMatching`        | Object   | Optional |
> | `liveness`                      | Object   | Optional |
> | `name`                          | String   | Required |
> | `phone`                         | Object   | Optional |
> | `transaction`                   | Object   | Optional |
> | `updatedAt`                     | DateTime | N/A      |
> | `verifiableCredential`          | Object   | Optional |
> | `voice` (deprecated)            | Object   | Optional |
>
> `biometricEnrollment` - Biometric enrollment configuration object
>
> | Property       | Type    | Required |
> | -------------- | ------- | -------- |
> | `face.enabled` | Boolean | Optional |
>
> `dataBasedIdentityVerification` - Data-based identity verification configuration object
>
> | Property    | Type   | Required |
> | ----------- | ------ | -------- |
> | `threshold` | String | Optional |
>
> `deviceOwnership` - Device ownership configuration object
>
> | Property                           | Type   | Required |
> | ---------------------------------- | ------ | -------- |
> | `transunion`                       | Object | Required |
> | `transunion.emailToNameThreshold`  | String | Optional |
> | `transunion.emailToPhoneThreshold` | String | Optional |
> | `transunion.phoneRiskThreshold`    | String | Required |
> | `transunion.phoneToNameThreshold`  | String | Required |
> | `verify`                           | String | Required |
>
> `email` and `phone` - Email address and phone number configuration object
>
> | Property                                    | Type    | Required |
> | ------------------------------------------- | ------- | -------- |
> | `createMfaDevice`                           | Boolean | Optional |
> | `otp`                                       | Object  | Optional |
> | `otp.` `attempts`                           | Object  | Required |
> | `otp.` `attempts.` `count`                  | Integer | Required |
> | `otp.` `deliveries`                         | Object  | Required |
> | `otp.` `deliveries.` `coolDown`             | Object  | Required |
> | `otp.` `deliveries.` `coolDown.` `duration` | Integer | Required |
> | `otp.` `deliveries.` `coolDown.` `timeUnit` | String  | Required |
> | `otp.` `deliveries.` `count`                | Integer | Required |
> | `otp.` `lifeTime`                           | Object  | Required |
> | `otp.` `lifeTime.` `duration`               | Integer | Required |
> | `otp.` `lifeTime.` `timeUnit`               | String  | Required |
> | `otp.` `notification`                       | Object  | Required |
> | `otp.` `notification.` `templateName`       | String  | Required |
> | `otp.` `notification.` `variantName`        | String  | Optional |
> | `verify`                                    | String  | Required |
>
> `facialComparison` - Facial comparison configuration object
>
> | Property    | Type   | Required |
> | ----------- | ------ | -------- |
> | `threshold` | String | Required |
> | `verify`    | String | Required |
>
> `governmentId` - Government identification document configuration object
>
> | Property          | Type    | Required |
> | ----------------- | ------- | -------- |
> | `aadhaar`         | Object  | Optional |
> | `aadhaar.enabled` | Boolean | Optional |
> | `failExpiredId`   | Boolean | Optional |
> | `inspectionType`  | String  | Optional |
> | `provider.auto`   | String  | Optional |
> | `provider.manual` | String  | Optional |
> | `retry.attempts`  | Integer | Optional |
> | `verify`          | String  | Required |
> | `verifyAamva`     | Boolean | Optional |
>
> `identityRecordMatching` - Identity record matching configuration object
>
> | Property                    | Type    | Required |
> | --------------------------- | ------- | -------- |
> | `address`                   | String  | Optional |
> | `address.fieldRequired`     | Boolean | Required |
> | `address.threshold`         | String  | Required |
> | `birth_date`                | String  | Optional |
> | `birth_date.fieldRequired`  | Boolean | Required |
> | `birth_date.threshold`      | String  | Required |
> | `family_name`               | String  | Optional |
> | `family_name.fieldRequired` | Boolean | Required |
> | `family_name.threshold`     | String  | Required |
> | `given_name.fieldRequired`  | Boolean | Required |
> | `given_name`                | String  | Optional |
> | `given_name.threshold`      | String  | Required |
> | `name`                      | String  | Optional |
> | `name.fieldRequired`        | Boolean | Required |
> | `name.threshold`            | String  | Required |
>
> `liveness` - Liveness configuration object
>
> | Property         | Type    | Required |
> | ---------------- | ------- | -------- |
> | `retry.attempts` | Integer | Optional |
> | `threshold`      | String  | Required |
> | `verify`         | String  | Required |
>
> `transaction` - Transaction configuration object
>
> | Property                                | Type    | Required |
> | --------------------------------------- | ------- | -------- |
> | `dataCollection`                        | Object  | Optional |
> | `dataCollection.` `timeout`             | Object  | Required |
> | `dataCollection.` `timeout.` `duration` | Integer | Required |
> | `dataCollection.` `timeout.` `timeUnit` | String  | Required |
> | `dataCollectionOnly`                    | Boolean | Optional |
> | `ida.enabled`                           | Boolean | Optional |
> | `timeout`                               | Object  | Optional |
> | `timeout.` `duration`                   | Integer | Required |
> | `timeout.` `timeUnit`                   | String  | Required |
>
> `verifiableCredential` - Verifiable credential configuration object
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
> | `verify`                      | String    | Required |
>
> `voice` - Voice verification configuration object

Voice verification is deprecated and will be removed on November 25, 2026.

| Property                                    | Type    | Required |
| ------------------------------------------- | ------- | -------- |
| `comparison.` `threshold`                   | String  | Required |
| `enrollment`                                | Boolean | Required |
| `liveness.` `threshold`                     | String  | Required |
| `referenceData`                             | Object  | Optional |
| `referenceData.` `retainOriginalRecordings` | Boolean | Optional |
| `referenceData.` `updateOnReenrollment`     | Boolean | Optional |
| `referenceData.` `updateOnVerification`     | Boolean | Optional |
| `textDependent`                             | Object  | Optional |
| `textDependent.` `phrase.` `id`             | String  | Required |
| `textDependent.` `samples`                  | Integer | Required |
| `verify`                                    | String  | Required |

The `notification.variantName` in the `email` and `phone` configuration objects can define a variant for the `email_phone_verification` notification submitted in `notification.templateName`, if needed. After receipt of a [Create Verify Transaction](../verify-transactions/create-verify-transaction.html) request, the verification service uses an `email_phone_verification` notification template to send notice of the action taken to the user via email or SMS text.

A policy-specific `locale` cannot be specified for the `email_phone_verification` notification. The notification uses the user's preferred language or, if the user has no preferred language, the default language of the environment.

When setting timeouts in the transaction configuration object, `dataCollection.timeout.duration` must be less than or equal to `timeout.duration`. Use caution when reducing the timeouts below the defaults to avoid an unfavorable user experience.

The first example response includes AAMVA. The second example response includes data-based identity verification.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "failExpiredId": "true",
        "retry": {
            "attempts": 3
        },
        "provider": {
            "auto": "VERIFF",
            "manual": "MITEK"
        },
        "verifyAamva": true
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 3
        }
    },
    "identityRecordMatching": {
        "address": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "birth_date": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "family_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "given_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "name": {
            "fieldRequired": false,
            "threshold": "MEDIUM"
        }
    },
    "dataBasedIdentityVerification": {
        "threshold": "HIGH"
    },
    "email": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "dataCollectionOnly": false
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/verifyPolicies' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "failExpiredId": "true",
        "retry": {
            "attempts": 3
        },
        "provider": {
            "auto": "VERIFF",
            "manual": "MITEK"
        },
        "verifyAamva": true
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 3
        }
    },
    "identityRecordMatching": {
        "address": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "birth_date": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "family_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "given_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "name": {
            "fieldRequired": false,
            "threshold": "MEDIUM"
        }
    },
    "dataBasedIdentityVerification": {
        "threshold": "HIGH"
    },
    "email": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "dataCollectionOnly": false
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/verifyPolicies")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Verify everything""," + "\n" +
@"    ""description"": ""All types required""," + "\n" +
@"    ""default"": false," + "\n" +
@"    ""governmentId"": {" + "\n" +
@"        ""verify"": ""REQUIRED""," + "\n" +
@"        ""inspectionType"": ""AUTOMATIC""," + "\n" +
@"        ""failExpiredId"": ""true""," + "\n" +
@"        ""retry"": {" + "\n" +
@"            ""attempts"": 3" + "\n" +
@"        }," + "\n" +
@"        ""provider"": {" + "\n" +
@"            ""auto"": ""VERIFF""," + "\n" +
@"            ""manual"": ""MITEK""" + "\n" +
@"        }," + "\n" +
@"        ""verifyAamva"": true" + "\n" +
@"    }," + "\n" +
@"    ""facialComparison"": {" + "\n" +
@"        ""verify"": ""REQUIRED""," + "\n" +
@"        ""threshold"": ""HIGH""" + "\n" +
@"    }," + "\n" +
@"    ""liveness"": {" + "\n" +
@"        ""verify"": ""REQUIRED""," + "\n" +
@"        ""threshold"": ""HIGH""," + "\n" +
@"        ""retry"": {" + "\n" +
@"            ""attempts"": 3" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""identityRecordMatching"": {" + "\n" +
@"        ""address"": {" + "\n" +
@"            ""fieldRequired"": true," + "\n" +
@"            ""threshold"": ""MEDIUM""" + "\n" +
@"        }," + "\n" +
@"        ""birth_date"": {" + "\n" +
@"            ""fieldRequired"": true," + "\n" +
@"            ""threshold"": ""MEDIUM""" + "\n" +
@"        }," + "\n" +
@"        ""family_name"": {" + "\n" +
@"            ""fieldRequired"": true," + "\n" +
@"            ""threshold"": ""MEDIUM""" + "\n" +
@"        }," + "\n" +
@"        ""given_name"": {" + "\n" +
@"            ""fieldRequired"": true," + "\n" +
@"            ""threshold"": ""MEDIUM""" + "\n" +
@"        }," + "\n" +
@"        ""name"": {" + "\n" +
@"            ""fieldRequired"": false," + "\n" +
@"            ""threshold"": ""MEDIUM""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""dataBasedIdentityVerification"": {" + "\n" +
@"        ""threshold"": ""HIGH""" + "\n" +
@"    }," + "\n" +
@"    ""email"": {" + "\n" +
@"        ""verify"": ""REQUIRED""," + "\n" +
@"        ""createMfaDevice"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""attempts"": {" + "\n" +
@"                ""count"": 5" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 10," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""deliveries"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""cooldown"": {" + "\n" +
@"                    ""duration"": 30," + "\n" +
@"                    ""timeUnit"": ""SECONDS""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""notification"": {" + "\n" +
@"                ""templateName"": ""email_phone_verification""" + "\n" +
@"            }" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""phone"": {" + "\n" +
@"        ""verify"": ""REQUIRED""," + "\n" +
@"        ""createMfaDevice"": true," + "\n" +
@"        ""otp"": {" + "\n" +
@"            ""attempts"": {" + "\n" +
@"                ""count"": 5" + "\n" +
@"            }," + "\n" +
@"            ""lifeTime"": {" + "\n" +
@"                ""duration"": 10," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }," + "\n" +
@"            ""deliveries"": {" + "\n" +
@"                ""count"": 3," + "\n" +
@"                ""cooldown"": {" + "\n" +
@"                    ""duration"": 30," + "\n" +
@"                    ""timeUnit"": ""SECONDS""" + "\n" +
@"                }" + "\n" +
@"            }," + "\n" +
@"            ""notification"": {" + "\n" +
@"                ""templateName"": ""email_phone_verification""" + "\n" +
@"            }" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""transaction"": {" + "\n" +
@"        ""timeout"": {" + "\n" +
@"            ""duration"": 30," + "\n" +
@"            ""timeUnit"": ""MINUTES""" + "\n" +
@"        }," + "\n" +
@"        ""dataCollection"": {" + "\n" +
@"            ""timeout"": {" + "\n" +
@"                ""duration"": 15," + "\n" +
@"                ""timeUnit"": ""MINUTES""" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""dataCollectionOnly"": false" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "failExpiredId": "true",
        "retry": {
            "attempts": 3
        },
        "provider": {
            "auto": "VERIFF",
            "manual": "MITEK"
        },
        "verifyAamva": true
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 3
        }
    },
    "identityRecordMatching": {
        "address": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "birth_date": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "family_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "given_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "name": {
            "fieldRequired": false,
            "threshold": "MEDIUM"
        }
    },
    "dataBasedIdentityVerification": {
        "threshold": "HIGH"
    },
    "email": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "dataCollectionOnly": false
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
POST /v1/environments/{{envID}}/verifyPolicies HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "failExpiredId": "true",
        "retry": {
            "attempts": 3
        },
        "provider": {
            "auto": "VERIFF",
            "manual": "MITEK"
        },
        "verifyAamva": true
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 3
        }
    },
    "identityRecordMatching": {
        "address": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "birth_date": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "family_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "given_name": {
            "fieldRequired": true,
            "threshold": "MEDIUM"
        },
        "name": {
            "fieldRequired": false,
            "threshold": "MEDIUM"
        }
    },
    "dataBasedIdentityVerification": {
        "threshold": "HIGH"
    },
    "email": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "dataCollectionOnly": false
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Verify everything\",\n    \"description\": \"All types required\",\n    \"default\": false,\n    \"governmentId\": {\n        \"verify\": \"REQUIRED\",\n        \"inspectionType\": \"AUTOMATIC\",\n        \"failExpiredId\": \"true\",\n        \"retry\": {\n            \"attempts\": 3\n        },\n        \"provider\": {\n            \"auto\": \"VERIFF\",\n            \"manual\": \"MITEK\"\n        },\n        \"verifyAamva\": true\n    },\n    \"facialComparison\": {\n        \"verify\": \"REQUIRED\",\n        \"threshold\": \"HIGH\"\n    },\n    \"liveness\": {\n        \"verify\": \"REQUIRED\",\n        \"threshold\": \"HIGH\",\n        \"retry\": {\n            \"attempts\": 3\n        }\n    },\n    \"identityRecordMatching\": {\n        \"address\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"birth_date\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"family_name\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"given_name\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"name\": {\n            \"fieldRequired\": false,\n            \"threshold\": \"MEDIUM\"\n        }\n    },\n    \"dataBasedIdentityVerification\": {\n        \"threshold\": \"HIGH\"\n    },\n    \"email\": {\n        \"verify\": \"REQUIRED\",\n        \"createMfaDevice\": true,\n        \"otp\": {\n            \"attempts\": {\n                \"count\": 5\n            },\n            \"lifeTime\": {\n                \"duration\": 10,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"deliveries\": {\n                \"count\": 3,\n                \"cooldown\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            },\n            \"notification\": {\n                \"templateName\": \"email_phone_verification\"\n            }\n        }\n    },\n    \"phone\": {\n        \"verify\": \"REQUIRED\",\n        \"createMfaDevice\": true,\n        \"otp\": {\n            \"attempts\": {\n                \"count\": 5\n            },\n            \"lifeTime\": {\n                \"duration\": 10,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"deliveries\": {\n                \"count\": 3,\n                \"cooldown\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            },\n            \"notification\": {\n                \"templateName\": \"email_phone_verification\"\n            }\n        }\n    },\n    \"transaction\": {\n        \"timeout\": {\n            \"duration\": 30,\n            \"timeUnit\": \"MINUTES\"\n        },\n        \"dataCollection\": {\n            \"timeout\": {\n                \"duration\": 15,\n                \"timeUnit\": \"MINUTES\"\n            }\n        },\n        \"dataCollectionOnly\": false\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/verifyPolicies")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
      "verify": "REQUIRED",
      "inspectionType": "AUTOMATIC",
      "failExpiredId": "true",
      "retry": {
        "attempts": 3
      },
      "provider": {
        "auto": "VERIFF",
        "manual": "MITEK"
      },
      "verifyAamva": true
    },
    "facialComparison": {
      "verify": "REQUIRED",
      "threshold": "HIGH"
    },
    "liveness": {
      "verify": "REQUIRED",
      "threshold": "HIGH",
      "retry": {
        "attempts": 3
      }
    },
    "identityRecordMatching": {
      "address": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "birth_date": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "family_name": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "given_name": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "name": {
        "fieldRequired": false,
        "threshold": "MEDIUM"
      }
    },
    "dataBasedIdentityVerification": {
      "threshold": "HIGH"
    },
    "email": {
      "verify": "REQUIRED",
      "createMfaDevice": true,
      "otp": {
        "attempts": {
          "count": 5
        },
        "lifeTime": {
          "duration": 10,
          "timeUnit": "MINUTES"
        },
        "deliveries": {
          "count": 3,
          "cooldown": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        },
        "notification": {
          "templateName": "email_phone_verification"
        }
      }
    },
    "phone": {
      "verify": "REQUIRED",
      "createMfaDevice": true,
      "otp": {
        "attempts": {
          "count": 5
        },
        "lifeTime": {
          "duration": 10,
          "timeUnit": "MINUTES"
        },
        "deliveries": {
          "count": 3,
          "cooldown": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        },
        "notification": {
          "templateName": "email_phone_verification"
        }
      }
    },
    "transaction": {
      "timeout": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "dataCollection": {
        "timeout": {
          "duration": 15,
          "timeUnit": "MINUTES"
        }
      },
      "dataCollectionOnly": false
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/verifyPolicies',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
      "verify": "REQUIRED",
      "inspectionType": "AUTOMATIC",
      "failExpiredId": "true",
      "retry": {
        "attempts": 3
      },
      "provider": {
        "auto": "VERIFF",
        "manual": "MITEK"
      },
      "verifyAamva": true
    },
    "facialComparison": {
      "verify": "REQUIRED",
      "threshold": "HIGH"
    },
    "liveness": {
      "verify": "REQUIRED",
      "threshold": "HIGH",
      "retry": {
        "attempts": 3
      }
    },
    "identityRecordMatching": {
      "address": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "birth_date": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "family_name": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "given_name": {
        "fieldRequired": true,
        "threshold": "MEDIUM"
      },
      "name": {
        "fieldRequired": false,
        "threshold": "MEDIUM"
      }
    },
    "dataBasedIdentityVerification": {
      "threshold": "HIGH"
    },
    "email": {
      "verify": "REQUIRED",
      "createMfaDevice": true,
      "otp": {
        "attempts": {
          "count": 5
        },
        "lifeTime": {
          "duration": 10,
          "timeUnit": "MINUTES"
        },
        "deliveries": {
          "count": 3,
          "cooldown": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        },
        "notification": {
          "templateName": "email_phone_verification"
        }
      }
    },
    "phone": {
      "verify": "REQUIRED",
      "createMfaDevice": true,
      "otp": {
        "attempts": {
          "count": 5
        },
        "lifeTime": {
          "duration": 10,
          "timeUnit": "MINUTES"
        },
        "deliveries": {
          "count": 3,
          "cooldown": {
            "duration": 30,
            "timeUnit": "SECONDS"
          }
        },
        "notification": {
          "templateName": "email_phone_verification"
        }
      }
    },
    "transaction": {
      "timeout": {
        "duration": 30,
        "timeUnit": "MINUTES"
      },
      "dataCollection": {
        "timeout": {
          "duration": 15,
          "timeUnit": "MINUTES"
        }
      },
      "dataCollectionOnly": false
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

url = "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies"

payload = json.dumps({
  "name": "Verify everything",
  "description": "All types required",
  "default": False,
  "governmentId": {
    "verify": "REQUIRED",
    "inspectionType": "AUTOMATIC",
    "failExpiredId": "true",
    "retry": {
      "attempts": 3
    },
    "provider": {
      "auto": "VERIFF",
      "manual": "MITEK"
    },
    "verifyAamva": True
  },
  "facialComparison": {
    "verify": "REQUIRED",
    "threshold": "HIGH"
  },
  "liveness": {
    "verify": "REQUIRED",
    "threshold": "HIGH",
    "retry": {
      "attempts": 3
    }
  },
  "identityRecordMatching": {
    "address": {
      "fieldRequired": True,
      "threshold": "MEDIUM"
    },
    "birth_date": {
      "fieldRequired": True,
      "threshold": "MEDIUM"
    },
    "family_name": {
      "fieldRequired": True,
      "threshold": "MEDIUM"
    },
    "given_name": {
      "fieldRequired": True,
      "threshold": "MEDIUM"
    },
    "name": {
      "fieldRequired": False,
      "threshold": "MEDIUM"
    }
  },
  "dataBasedIdentityVerification": {
    "threshold": "HIGH"
  },
  "email": {
    "verify": "REQUIRED",
    "createMfaDevice": True,
    "otp": {
      "attempts": {
        "count": 5
      },
      "lifeTime": {
        "duration": 10,
        "timeUnit": "MINUTES"
      },
      "deliveries": {
        "count": 3,
        "cooldown": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      },
      "notification": {
        "templateName": "email_phone_verification"
      }
    }
  },
  "phone": {
    "verify": "REQUIRED",
    "createMfaDevice": True,
    "otp": {
      "attempts": {
        "count": 5
      },
      "lifeTime": {
        "duration": 10,
        "timeUnit": "MINUTES"
      },
      "deliveries": {
        "count": 3,
        "cooldown": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      },
      "notification": {
        "templateName": "email_phone_verification"
      }
    }
  },
  "transaction": {
    "timeout": {
      "duration": 30,
      "timeUnit": "MINUTES"
    },
    "dataCollection": {
      "timeout": {
        "duration": 15,
        "timeUnit": "MINUTES"
      }
    },
    "dataCollectionOnly": False
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/verifyPolicies');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Verify everything",\n    "description": "All types required",\n    "default": false,\n    "governmentId": {\n        "verify": "REQUIRED",\n        "inspectionType": "AUTOMATIC",\n        "failExpiredId": "true",\n        "retry": {\n            "attempts": 3\n        },\n        "provider": {\n            "auto": "VERIFF",\n            "manual": "MITEK"\n        },\n        "verifyAamva": true\n    },\n    "facialComparison": {\n        "verify": "REQUIRED",\n        "threshold": "HIGH"\n    },\n    "liveness": {\n        "verify": "REQUIRED",\n        "threshold": "HIGH",\n        "retry": {\n            "attempts": 3\n        }\n    },\n    "identityRecordMatching": {\n        "address": {\n            "fieldRequired": true,\n            "threshold": "MEDIUM"\n        },\n        "birth_date": {\n            "fieldRequired": true,\n            "threshold": "MEDIUM"\n        },\n        "family_name": {\n            "fieldRequired": true,\n            "threshold": "MEDIUM"\n        },\n        "given_name": {\n            "fieldRequired": true,\n            "threshold": "MEDIUM"\n        },\n        "name": {\n            "fieldRequired": false,\n            "threshold": "MEDIUM"\n        }\n    },\n    "dataBasedIdentityVerification": {\n        "threshold": "HIGH"\n    },\n    "email": {\n        "verify": "REQUIRED",\n        "createMfaDevice": true,\n        "otp": {\n            "attempts": {\n                "count": 5\n            },\n            "lifeTime": {\n                "duration": 10,\n                "timeUnit": "MINUTES"\n            },\n            "deliveries": {\n                "count": 3,\n                "cooldown": {\n                    "duration": 30,\n                    "timeUnit": "SECONDS"\n                }\n            },\n            "notification": {\n                "templateName": "email_phone_verification"\n            }\n        }\n    },\n    "phone": {\n        "verify": "REQUIRED",\n        "createMfaDevice": true,\n        "otp": {\n            "attempts": {\n                "count": 5\n            },\n            "lifeTime": {\n                "duration": 10,\n                "timeUnit": "MINUTES"\n            },\n            "deliveries": {\n                "count": 3,\n                "cooldown": {\n                    "duration": 30,\n                    "timeUnit": "SECONDS"\n                }\n            },\n            "notification": {\n                "templateName": "email_phone_verification"\n            }\n        }\n    },\n    "transaction": {\n        "timeout": {\n            "duration": 30,\n            "timeUnit": "MINUTES"\n        },\n        "dataCollection": {\n            "timeout": {\n                "duration": 15,\n                "timeUnit": "MINUTES"\n            }\n        },\n        "dataCollectionOnly": false\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/verifyPolicies")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Verify everything",
  "description": "All types required",
  "default": false,
  "governmentId": {
    "verify": "REQUIRED",
    "inspectionType": "AUTOMATIC",
    "failExpiredId": "true",
    "retry": {
      "attempts": 3
    },
    "provider": {
      "auto": "VERIFF",
      "manual": "MITEK"
    },
    "verifyAamva": true
  },
  "facialComparison": {
    "verify": "REQUIRED",
    "threshold": "HIGH"
  },
  "liveness": {
    "verify": "REQUIRED",
    "threshold": "HIGH",
    "retry": {
      "attempts": 3
    }
  },
  "identityRecordMatching": {
    "address": {
      "fieldRequired": true,
      "threshold": "MEDIUM"
    },
    "birth_date": {
      "fieldRequired": true,
      "threshold": "MEDIUM"
    },
    "family_name": {
      "fieldRequired": true,
      "threshold": "MEDIUM"
    },
    "given_name": {
      "fieldRequired": true,
      "threshold": "MEDIUM"
    },
    "name": {
      "fieldRequired": false,
      "threshold": "MEDIUM"
    }
  },
  "dataBasedIdentityVerification": {
    "threshold": "HIGH"
  },
  "email": {
    "verify": "REQUIRED",
    "createMfaDevice": true,
    "otp": {
      "attempts": {
        "count": 5
      },
      "lifeTime": {
        "duration": 10,
        "timeUnit": "MINUTES"
      },
      "deliveries": {
        "count": 3,
        "cooldown": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      },
      "notification": {
        "templateName": "email_phone_verification"
      }
    }
  },
  "phone": {
    "verify": "REQUIRED",
    "createMfaDevice": true,
    "otp": {
      "attempts": {
        "count": 5
      },
      "lifeTime": {
        "duration": 10,
        "timeUnit": "MINUTES"
      },
      "deliveries": {
        "count": 3,
        "cooldown": {
          "duration": 30,
          "timeUnit": "SECONDS"
        }
      },
      "notification": {
        "templateName": "email_phone_verification"
      }
    }
  },
  "transaction": {
    "timeout": {
      "duration": 30,
      "timeUnit": "MINUTES"
    },
    "dataCollection": {
      "timeout": {
        "duration": 15,
        "timeUnit": "MINUTES"
      }
    },
    "dataCollectionOnly": false
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Verify everything\",\n    \"description\": \"All types required\",\n    \"default\": false,\n    \"governmentId\": {\n        \"verify\": \"REQUIRED\",\n        \"inspectionType\": \"AUTOMATIC\",\n        \"failExpiredId\": \"true\",\n        \"retry\": {\n            \"attempts\": 3\n        },\n        \"provider\": {\n            \"auto\": \"VERIFF\",\n            \"manual\": \"MITEK\"\n        },\n        \"verifyAamva\": true\n    },\n    \"facialComparison\": {\n        \"verify\": \"REQUIRED\",\n        \"threshold\": \"HIGH\"\n    },\n    \"liveness\": {\n        \"verify\": \"REQUIRED\",\n        \"threshold\": \"HIGH\",\n        \"retry\": {\n            \"attempts\": 3\n        }\n    },\n    \"identityRecordMatching\": {\n        \"address\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"birth_date\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"family_name\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"given_name\": {\n            \"fieldRequired\": true,\n            \"threshold\": \"MEDIUM\"\n        },\n        \"name\": {\n            \"fieldRequired\": false,\n            \"threshold\": \"MEDIUM\"\n        }\n    },\n    \"dataBasedIdentityVerification\": {\n        \"threshold\": \"HIGH\"\n    },\n    \"email\": {\n        \"verify\": \"REQUIRED\",\n        \"createMfaDevice\": true,\n        \"otp\": {\n            \"attempts\": {\n                \"count\": 5\n            },\n            \"lifeTime\": {\n                \"duration\": 10,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"deliveries\": {\n                \"count\": 3,\n                \"cooldown\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            },\n            \"notification\": {\n                \"templateName\": \"email_phone_verification\"\n            }\n        }\n    },\n    \"phone\": {\n        \"verify\": \"REQUIRED\",\n        \"createMfaDevice\": true,\n        \"otp\": {\n            \"attempts\": {\n                \"count\": 5\n            },\n            \"lifeTime\": {\n                \"duration\": 10,\n                \"timeUnit\": \"MINUTES\"\n            },\n            \"deliveries\": {\n                \"count\": 3,\n                \"cooldown\": {\n                    \"duration\": 30,\n                    \"timeUnit\": \"SECONDS\"\n                }\n            },\n            \"notification\": {\n                \"templateName\": \"email_phone_verification\"\n            }\n        }\n    },\n    \"transaction\": {\n        \"timeout\": {\n            \"duration\": 30,\n            \"timeUnit\": \"MINUTES\"\n        },\n        \"dataCollection\": {\n            \"timeout\": {\n                \"duration\": 15,\n                \"timeUnit\": \"MINUTES\"\n            }\n        },\n        \"dataCollectionOnly\": false\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/verifyPolicies/80c3f3c3-1099-4ff3-967e-dc35e742aa63"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "notificationTemplates": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/templates/email_phone_verification"
        }
    },
    "id": "80c3f3c3-1099-4ff3-967e-dc35e742aa63",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "failExpiredId": true,
        "retry": {
            "attempts": 3
        },
        "provider": {
            "auto": "VERIFF",
            "manual": "MITEK"
        },
        "verifyAamva": true,
        "documentImages": {
            "enabled": true
        }
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 3
        }
    },
    "email": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "dataCollectionOnly": false,
        "authenticationMode": false
    },
    "verifiableCredential": {
        "verify": "DISABLED",
        "protocol": "NATIVE"
    },
    "identityRecordMatching": {
        "address": {
            "threshold": "MEDIUM",
            "fieldRequired": true
        },
        "birth_date": {
            "threshold": "MEDIUM",
            "fieldRequired": true
        },
        "family_name": {
            "threshold": "MEDIUM",
            "fieldRequired": true
        },
        "given_name": {
            "threshold": "MEDIUM",
            "fieldRequired": true
        },
        "name": {
            "threshold": "MEDIUM",
            "fieldRequired": false
        }
    },
    "dataBasedIdentityVerification": {
        "threshold": "HIGH"
    },
    "createdAt": "2025-08-12T20:23:14.930Z",
    "updatedAt": "2025-08-12T20:23:14.942Z",
    "systemProvided": false
}
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/verifyPolicies/60ee17a9-611e-4281-88b8-32acf451220b"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "notificationTemplates": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/templates/email_phone_verification"
        }
    },
    "id": "60ee17a9-611e-4281-88b8-32acf451220b",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "failExpiredId": true,
        "retry": {
            "attempts": 3
        },
        "provider": {
            "auto": "VERIFF",
            "manual": "MITEK"
        },
        "verifyAamva": true,
        "documentImages": {
           "enabled": true
        }
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 3
        }
    },
    "email": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "ida": {
            "enabled": true
        },
        "dataCollectionOnly": false
    },
    "verifiableCredential": {
        "verify": "DISABLED",
        "protocol": "NATIVE"
    },
    "createdAt": "2025-01-03T14:48:37.946Z",
    "updatedAt": "2025-01-03T14:48:37.963Z"
}
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/verifyPolicies/fec27b2c-a1be-4c96-9eed-f0de64ad6408"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "fec27b2c-a1be-4c96-9eed-f0de64ad6408",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Verify everything",
    "description": "All types required",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "retry": {
            "attempts": 3
        },
        "provider": {
            "auto": "MITEK",
            "manual": "MITEK"
        },
        "documentImages": {
            "enabled": true
        }
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 3
        }
    },
    "email": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "REQUIRED",
        "createMfaDevice": true,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "dataCollectionOnly": false
    },
    "verifiableCredential": {
        "verify": "DISABLED",
        "protocol": "NATIVE"
    },
    "createdAt": "2024-04-10T20:26:06.326Z",
    "updatedAt": "2024-04-10T20:26:06.330Z"
}
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/verifyPolicies/5c5989a3-c167-444e-9321-b73a28df9e1b"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "5c5989a3-c167-444e-9321-b73a28df9e1b",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Verify Policy Use GovId - Aadhaar",
    "description": "Require Aadhaar ID.",
    "default": false,
    "governmentId": {
        "verify": "REQUIRED",
        "inspectionType": "AUTOMATIC",
        "failExpiredId": false,
        "provider": {
            "auto": "MITEK",
            "manual": "MITEK"
        },
        "verifyAamva": true,
        "aadhaar": {
            "enabled": true
        },
        "documentImages": {
            "enabled": true
        }
    },
    "facialComparison": {
        "verify": "REQUIRED",
        "threshold": "HIGH"
    },
    "liveness": {
        "verify": "REQUIRED",
        "threshold": "HIGH",
        "retry": {
            "attempts": 1
        }
    },
    "email": {
        "verify": "DISABLED",
        "createMfaDevice": false,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "phone": {
        "verify": "DISABLED",
        "createMfaDevice": false,
        "otp": {
            "attempts": {
                "count": 5
            },
            "lifeTime": {
                "duration": 10,
                "timeUnit": "MINUTES"
            },
            "deliveries": {
                "count": 3,
                "cooldown": {
                    "duration": 30,
                    "timeUnit": "SECONDS"
                }
            },
            "notification": {
                "templateName": "email_phone_verification"
            }
        }
    },
    "transaction": {
        "timeout": {
            "duration": 30,
            "timeUnit": "MINUTES"
        },
        "dataCollection": {
            "timeout": {
                "duration": 15,
                "timeUnit": "MINUTES"
            }
        },
        "ida": {
            "enabled": true
        },
        "dataCollectionOnly": false
    },
    "verifiableCredential": {
        "verify": "DISABLED",
        "protocol": "NATIVE"
    },
    "createdAt": "2025-04-21T18:16:50.040Z",
    "updatedAt": "2025-04-21T18:16:50.044Z"
}
```

---

---
title: Create Verify Transaction
description: Create a new PingOne Verify verification transaction for a specified user
component: pingone-api
page_id: pingone-api:verify:verify-transactions/create-verify-transaction
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-transactions/create-verify-transaction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-30
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Verify Transaction

##

Required permission:

* [idverifications:create:verifyTransactions](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-create-verifyTransactions "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions
```

Create a new verify transaction for the specified user with the `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions` request.

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users/index.html), especially [User operations](../../platform/users/users-1/index.html).

* [Create a verify policy](../verify-policy/create-verify-policy.html) to get a `verifyPolicyID` for the body. Refer also to [Verify Policies](../verify-policy/index.html).

> **Collapse: Request Model**
>
> Refer to [Verify transaction data model](index.html#verify-transaction-data-model) for full property descriptions.
>
> | Property                 | Type   | Required |
> | ------------------------ | ------ | -------- |
> | `callback`               | Object | Optional |
> | `callback.headers`       | Object | Optional |
> | `callback.url`           | String | Required |
> | `redirect`               | Object | Optional |
> | `redirect.message`       | String | Optional |
> | `redirect.url`           | String | Required |
> | `requirements`           | Object | Optional |
> | `sendNotification.email` | String | Optional |
> | `sendNotification.phone` | String | Optional |
> | `verifyPolicy.id`        | String | Optional |
>
> `requirements` - Requirements object
>
> | Property                | Type      | Required          |
> | ----------------------- | --------- | ----------------- |
> | `address`               | Object    | Optional          |
> | `address.options`       | String\[] | Required/Optional |
> | `address.value`         | String    | Required/Optional |
> | `birth_date`            | Object    | Optional          |
> | `birth_date.options`    | String\[] | Required/Optional |
> | `birth_date.value`      | String    | Required/Optional |
> | `email`                 | String    | Optional          |
> | `email.options`         | String\[] | Required          |
> | `family_name`           | Object    | Optional          |
> | `family_name.options`   | String\[] | Required/Optional |
> | `family_name.value`     | String    | Required/Optional |
> | `given_name`            | Object    | Optional          |
> | `given_name.options`    | String\[] | Required/Optional |
> | `given_name.value`      | String    | Required/Optional |
> | `name`                  | Object    | Optional          |
> | `name.options`          | String\[] | Required/Optional |
> | `name.value`            | String    | Required/Optional |
> | `phone`                 | String    | Optional          |
> | `phone.value`           | String    | Required          |
> | `referenceSelfie`       | Object    | Required/Optional |
> | `referenceSelfie.value` | String    | Required          |
>
> A `referenceSelfie` is required when, in the verify policy referenced by `verifyPolicy.id` (or the default verify policy), `facialComparison.verify` is `REQUIRED` and `governmentID.verify` is `DISABLED`. Otherwise, `referenceSelfie` is ignored.

Biographic matching occurs when the [Verify Policy](../verify-policy/index.html) includes `governmentId` and this body includes the optional biographic matching data `requirements` (`given_name`, `family_name`, `name`, `address`, and `birth_date`). If the client does not provide biographic matching data, the service performs the verifications required by the verify policy. If the client does provide biographic matching data, the service performs the verifications required by the verify policy and then compares the data extracted from the government identity document to the data provided by the client.

For `webVerificationUrl` in the response body, the value is the URL for the `${app.open.url}` dynamic variable of the `id_verification` notification sent to the user. Furthermore, it has optional query parameters. Refer to [Verify transaction query parameters](index.html#verify-transaction-query-parameters)

There are three parties to creating a verify transaction, the user, the company requesting the transaction, and the service. When used, `requirements.email.options` can have 0, 1, or multiple email addresses.

* If the company sends 0 email addresses, the user can provide any email they want.

* If the company sends 1 email address from their records, that email address receives the OTP and the user cannot change it.

* If the company sends 2 or more email addresses from their records, the service returns the addresses to the user with part of the address masked. The user sends the email address they want to verify.

When a phone number is needed, a valid phone number string must be provided in international format (includes a leading + character), for example, +14155552671.

Always include the country code in the value you provide for the `phone` parameter. Phone formats across the globe are constantly expanding and changing. If the country code is not included, issues might occur with message delivery.

The following sample shows acceptable valid `phone` attribute formatting for the same number:

```none
+1.5125551234
+15125551234
+1.512.555.1234
15125551234
1-512-555-1234
+1 (512) 555-1234
```

The device (browser or smartphone) receives a single page application (SPA) - an HTML web page containing a code that establishes a link between the device and this transaction. With a link established, the device captures identity documents for verification. After completing verification, depending on the [verify policy](../verify-policy/index.html), the email or phone number submitted with the transaction can become a multifactor authentication device for PingOne.

If a phone number or an email address or both are supplied in the request body, after receipt of this request the verification service sends notifications using these notification templates:

* `email_phone_verification` - Sends a one-time password (OTP) to verify an SMS number or email address or both for a verify transaction. You can define a notification variant and locale for the `email_phone_verification` notification with [Create Verify Policy](../verify-policy/create-verify-policy.html) or [Update Verify Policy](../verify-policy/update-verify-policy.html). Associate a verify policy in `verifyPolicy` of this request or, if no `verifyPolicy` is provided, the default verify policy for the environment is used.

* `id_verification` - Sends an SMS or email or both to the end user with a link to Web Verify (Universal Capture) for the verify transaction. You cannot define a notification variant or locale for an `id_verification` notification.

The transaction is used by client applications when sending a web verification request, and for allowing requests to service providers.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "sendNotification": {
        "phone": "{{phone}}",
        "email": "{{email}}"
    },
    "verifyPolicy": {
        "id": "{{verifyPolicyID}}"
    },
    "requirements": {
        "referenceSelfie": {
            "value": "{{base64EncodedData}}"
        },
        "phone": {
            "value": "{{phone}}"
        },
        "email": {
            "options": [
                "{{email}}",
                "test@mailinator.com"
            ]
        },
        "given_name": {
            "options": [
                "Paddy",
                "Pat"
            ]
        },
        "family_name": {
            "value": "Thornton"
        },
        "name": {
            "value": "Paddy Thornton"
        },
        "address": {
            "options": [
                "4321 Main Street #407, Hollywood, CA 90027",
                "4321 Main Street Apt 407, Hollywood, CA 90027"
            ]
        },
        "birth_date": {
            "value": "1984-08-02"
        }
    },
    "callback": {
        "url": "{{callbackUrl}}",
        "headers": {
            "x-environment-id": "{{envID}}",
            "x-phone": "{{phone}}"
        }
    },
    "redirect": {
        "url": "{{redirectUrl}}",
        "message": "Document collection complete. Click Return."
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data-raw '{
    "sendNotification": {
        "phone": "{{phone}}",
        "email": "{{email}}"
    },
    "verifyPolicy": {
        "id": "{{verifyPolicyID}}"
    },
    "requirements": {
        "referenceSelfie": {
            "value": "{{base64EncodedData}}"
        },
        "phone": {
            "value": "{{phone}}"
        },
        "email": {
            "options": [
                "{{email}}",
                "test@mailinator.com"
            ]
        },
        "given_name": {
            "options": [
                "Paddy",
                "Pat"
            ]
        },
        "family_name": {
            "value": "Thornton"
        },
        "name": {
            "value": "Paddy Thornton"
        },
        "address": {
            "options": [
                "4321 Main Street #407, Hollywood, CA 90027",
                "4321 Main Street Apt 407, Hollywood, CA 90027"
            ]
        },
        "birth_date": {
            "value": "1984-08-02"
        }
    },
    "callback": {
        "url": "{{callbackUrl}}",
        "headers": {
            "x-environment-id": "{{envID}}",
            "x-phone": "{{phone}}"
        }
    },
    "redirect": {
        "url": "{{redirectUrl}}",
        "message": "Document collection complete. Click Return."
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""sendNotification"": {" + "\n" +
@"        ""phone"": ""{{phone}}""," + "\n" +
@"        ""email"": ""{{email}}""" + "\n" +
@"    }," + "\n" +
@"    ""verifyPolicy"": {" + "\n" +
@"        ""id"": ""{{verifyPolicyID}}""" + "\n" +
@"    }," + "\n" +
@"    ""requirements"": {" + "\n" +
@"        ""referenceSelfie"": {" + "\n" +
@"            ""value"": ""{{base64EncodedData}}""" + "\n" +
@"        }," + "\n" +
@"        ""phone"": {" + "\n" +
@"            ""value"": ""{{phone}}""" + "\n" +
@"        }," + "\n" +
@"        ""email"": {" + "\n" +
@"            ""options"": [" + "\n" +
@"                ""{{email}}""," + "\n" +
@"                ""test@mailinator.com""" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""given_name"": {" + "\n" +
@"            ""options"": [" + "\n" +
@"                ""Paddy""," + "\n" +
@"                ""Pat""" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""family_name"": {" + "\n" +
@"            ""value"": ""Thornton""" + "\n" +
@"        }," + "\n" +
@"        ""name"": {" + "\n" +
@"            ""value"": ""Paddy Thornton""" + "\n" +
@"        }," + "\n" +
@"        ""address"": {" + "\n" +
@"            ""options"": [" + "\n" +
@"                ""4321 Main Street #407, Hollywood, CA 90027""," + "\n" +
@"                ""4321 Main Street Apt 407, Hollywood, CA 90027""" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""birth_date"": {" + "\n" +
@"            ""value"": ""1984-08-02""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""callback"": {" + "\n" +
@"        ""url"": ""{{callbackUrl}}""," + "\n" +
@"        ""headers"": {" + "\n" +
@"            ""x-environment-id"": ""{{envID}}""," + "\n" +
@"            ""x-phone"": ""{{phone}}""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""redirect"": {" + "\n" +
@"        ""url"": ""{{redirectUrl}}""," + "\n" +
@"        ""message"": ""Document collection complete. Click Return.""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions"
  method := "POST"

  payload := strings.NewReader(`{
    "sendNotification": {
        "phone": "{{phone}}",
        "email": "{{email}}"
    },
    "verifyPolicy": {
        "id": "{{verifyPolicyID}}"
    },
    "requirements": {
        "referenceSelfie": {
            "value": "{{base64EncodedData}}"
        },
        "phone": {
            "value": "{{phone}}"
        },
        "email": {
            "options": [
                "{{email}}",
                "test@mailinator.com"
            ]
        },
        "given_name": {
            "options": [
                "Paddy",
                "Pat"
            ]
        },
        "family_name": {
            "value": "Thornton"
        },
        "name": {
            "value": "Paddy Thornton"
        },
        "address": {
            "options": [
                "4321 Main Street #407, Hollywood, CA 90027",
                "4321 Main Street Apt 407, Hollywood, CA 90027"
            ]
        },
        "birth_date": {
            "value": "1984-08-02"
        }
    },
    "callback": {
        "url": "{{callbackUrl}}",
        "headers": {
            "x-environment-id": "{{envID}}",
            "x-phone": "{{phone}}"
        }
    },
    "redirect": {
        "url": "{{redirectUrl}}",
        "message": "Document collection complete. Click Return."
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
POST /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "sendNotification": {
        "phone": "{{phone}}",
        "email": "{{email}}"
    },
    "verifyPolicy": {
        "id": "{{verifyPolicyID}}"
    },
    "requirements": {
        "referenceSelfie": {
            "value": "{{base64EncodedData}}"
        },
        "phone": {
            "value": "{{phone}}"
        },
        "email": {
            "options": [
                "{{email}}",
                "test@mailinator.com"
            ]
        },
        "given_name": {
            "options": [
                "Paddy",
                "Pat"
            ]
        },
        "family_name": {
            "value": "Thornton"
        },
        "name": {
            "value": "Paddy Thornton"
        },
        "address": {
            "options": [
                "4321 Main Street #407, Hollywood, CA 90027",
                "4321 Main Street Apt 407, Hollywood, CA 90027"
            ]
        },
        "birth_date": {
            "value": "1984-08-02"
        }
    },
    "callback": {
        "url": "{{callbackUrl}}",
        "headers": {
            "x-environment-id": "{{envID}}",
            "x-phone": "{{phone}}"
        }
    },
    "redirect": {
        "url": "{{redirectUrl}}",
        "message": "Document collection complete. Click Return."
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"sendNotification\": {\n        \"phone\": \"{{phone}}\",\n        \"email\": \"{{email}}\"\n    },\n    \"verifyPolicy\": {\n        \"id\": \"{{verifyPolicyID}}\"\n    },\n    \"requirements\": {\n        \"referenceSelfie\": {\n            \"value\": \"{{base64EncodedData}}\"\n        },\n        \"phone\": {\n            \"value\": \"{{phone}}\"\n        },\n        \"email\": {\n            \"options\": [\n                \"{{email}}\",\n                \"test@mailinator.com\"\n            ]\n        },\n        \"given_name\": {\n            \"options\": [\n                \"Paddy\",\n                \"Pat\"\n            ]\n        },\n        \"family_name\": {\n            \"value\": \"Thornton\"\n        },\n        \"name\": {\n            \"value\": \"Paddy Thornton\"\n        },\n        \"address\": {\n            \"options\": [\n                \"4321 Main Street #407, Hollywood, CA 90027\",\n                \"4321 Main Street Apt 407, Hollywood, CA 90027\"\n            ]\n        },\n        \"birth_date\": {\n            \"value\": \"1984-08-02\"\n        }\n    },\n    \"callback\": {\n        \"url\": \"{{callbackUrl}}\",\n        \"headers\": {\n            \"x-environment-id\": \"{{envID}}\",\n            \"x-phone\": \"{{phone}}\"\n        }\n    },\n    \"redirect\": {\n        \"url\": \"{{redirectUrl}}\",\n        \"message\": \"Document collection complete. Click Return.\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "sendNotification": {
      "phone": "{{phone}}",
      "email": "{{email}}"
    },
    "verifyPolicy": {
      "id": "{{verifyPolicyID}}"
    },
    "requirements": {
      "referenceSelfie": {
        "value": "{{base64EncodedData}}"
      },
      "phone": {
        "value": "{{phone}}"
      },
      "email": {
        "options": [
          "{{email}}",
          "test@mailinator.com"
        ]
      },
      "given_name": {
        "options": [
          "Paddy",
          "Pat"
        ]
      },
      "family_name": {
        "value": "Thornton"
      },
      "name": {
        "value": "Paddy Thornton"
      },
      "address": {
        "options": [
          "4321 Main Street #407, Hollywood, CA 90027",
          "4321 Main Street Apt 407, Hollywood, CA 90027"
        ]
      },
      "birth_date": {
        "value": "1984-08-02"
      }
    },
    "callback": {
      "url": "{{callbackUrl}}",
      "headers": {
        "x-environment-id": "{{envID}}",
        "x-phone": "{{phone}}"
      }
    },
    "redirect": {
      "url": "{{redirectUrl}}",
      "message": "Document collection complete. Click Return."
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "sendNotification": {
      "phone": "{{phone}}",
      "email": "{{email}}"
    },
    "verifyPolicy": {
      "id": "{{verifyPolicyID}}"
    },
    "requirements": {
      "referenceSelfie": {
        "value": "{{base64EncodedData}}"
      },
      "phone": {
        "value": "{{phone}}"
      },
      "email": {
        "options": [
          "{{email}}",
          "test@mailinator.com"
        ]
      },
      "given_name": {
        "options": [
          "Paddy",
          "Pat"
        ]
      },
      "family_name": {
        "value": "Thornton"
      },
      "name": {
        "value": "Paddy Thornton"
      },
      "address": {
        "options": [
          "4321 Main Street #407, Hollywood, CA 90027",
          "4321 Main Street Apt 407, Hollywood, CA 90027"
        ]
      },
      "birth_date": {
        "value": "1984-08-02"
      }
    },
    "callback": {
      "url": "{{callbackUrl}}",
      "headers": {
        "x-environment-id": "{{envID}}",
        "x-phone": "{{phone}}"
      }
    },
    "redirect": {
      "url": "{{redirectUrl}}",
      "message": "Document collection complete. Click Return."
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions"

payload = json.dumps({
  "sendNotification": {
    "phone": "{{phone}}",
    "email": "{{email}}"
  },
  "verifyPolicy": {
    "id": "{{verifyPolicyID}}"
  },
  "requirements": {
    "referenceSelfie": {
      "value": "{{base64EncodedData}}"
    },
    "phone": {
      "value": "{{phone}}"
    },
    "email": {
      "options": [
        "{{email}}",
        "test@mailinator.com"
      ]
    },
    "given_name": {
      "options": [
        "Paddy",
        "Pat"
      ]
    },
    "family_name": {
      "value": "Thornton"
    },
    "name": {
      "value": "Paddy Thornton"
    },
    "address": {
      "options": [
        "4321 Main Street #407, Hollywood, CA 90027",
        "4321 Main Street Apt 407, Hollywood, CA 90027"
      ]
    },
    "birth_date": {
      "value": "1984-08-02"
    }
  },
  "callback": {
    "url": "{{callbackUrl}}",
    "headers": {
      "x-environment-id": "{{envID}}",
      "x-phone": "{{phone}}"
    }
  },
  "redirect": {
    "url": "{{redirectUrl}}",
    "message": "Document collection complete. Click Return."
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "sendNotification": {\n        "phone": "{{phone}}",\n        "email": "{{email}}"\n    },\n    "verifyPolicy": {\n        "id": "{{verifyPolicyID}}"\n    },\n    "requirements": {\n        "referenceSelfie": {\n            "value": "{{base64EncodedData}}"\n        },\n        "phone": {\n            "value": "{{phone}}"\n        },\n        "email": {\n            "options": [\n                "{{email}}",\n                "test@mailinator.com"\n            ]\n        },\n        "given_name": {\n            "options": [\n                "Paddy",\n                "Pat"\n            ]\n        },\n        "family_name": {\n            "value": "Thornton"\n        },\n        "name": {\n            "value": "Paddy Thornton"\n        },\n        "address": {\n            "options": [\n                "4321 Main Street #407, Hollywood, CA 90027",\n                "4321 Main Street Apt 407, Hollywood, CA 90027"\n            ]\n        },\n        "birth_date": {\n            "value": "1984-08-02"\n        }\n    },\n    "callback": {\n        "url": "{{callbackUrl}}",\n        "headers": {\n            "x-environment-id": "{{envID}}",\n            "x-phone": "{{phone}}"\n        }\n    },\n    "redirect": {\n        "url": "{{redirectUrl}}",\n        "message": "Document collection complete. Click Return."\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "sendNotification": {
    "phone": "{{phone}}",
    "email": "{{email}}"
  },
  "verifyPolicy": {
    "id": "{{verifyPolicyID}}"
  },
  "requirements": {
    "referenceSelfie": {
      "value": "{{base64EncodedData}}"
    },
    "phone": {
      "value": "{{phone}}"
    },
    "email": {
      "options": [
        "{{email}}",
        "test@mailinator.com"
      ]
    },
    "given_name": {
      "options": [
        "Paddy",
        "Pat"
      ]
    },
    "family_name": {
      "value": "Thornton"
    },
    "name": {
      "value": "Paddy Thornton"
    },
    "address": {
      "options": [
        "4321 Main Street \#407, Hollywood, CA 90027",
        "4321 Main Street Apt 407, Hollywood, CA 90027"
      ]
    },
    "birth_date": {
      "value": "1984-08-02"
    }
  },
  "callback": {
    "url": "{{callbackUrl}}",
    "headers": {
      "x-environment-id": "{{envID}}",
      "x-phone": "{{phone}}"
    }
  },
  "redirect": {
    "url": "{{redirectUrl}}",
    "message": "Document collection complete. Click Return."
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"sendNotification\": {\n        \"phone\": \"{{phone}}\",\n        \"email\": \"{{email}}\"\n    },\n    \"verifyPolicy\": {\n        \"id\": \"{{verifyPolicyID}}\"\n    },\n    \"requirements\": {\n        \"referenceSelfie\": {\n            \"value\": \"{{base64EncodedData}}\"\n        },\n        \"phone\": {\n            \"value\": \"{{phone}}\"\n        },\n        \"email\": {\n            \"options\": [\n                \"{{email}}\",\n                \"test@mailinator.com\"\n            ]\n        },\n        \"given_name\": {\n            \"options\": [\n                \"Paddy\",\n                \"Pat\"\n            ]\n        },\n        \"family_name\": {\n            \"value\": \"Thornton\"\n        },\n        \"name\": {\n            \"value\": \"Paddy Thornton\"\n        },\n        \"address\": {\n            \"options\": [\n                \"4321 Main Street #407, Hollywood, CA 90027\",\n                \"4321 Main Street Apt 407, Hollywood, CA 90027\"\n            ]\n        },\n        \"birth_date\": {\n            \"value\": \"1984-08-02\"\n        }\n    },\n    \"callback\": {\n        \"url\": \"{{callbackUrl}}\",\n        \"headers\": {\n            \"x-environment-id\": \"{{envID}}\",\n            \"x-phone\": \"{{phone}}\"\n        }\n    },\n    \"redirect\": {\n        \"url\": \"{{redirectUrl}}\",\n        \"message\": \"Document collection complete. Click Return.\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/ad7b009a-6d88-4830-b3a6-99906049e372/verifyTransactions/293c1116-4050-47a1-ace0-be126b115d46"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/ad7b009a-6d88-4830-b3a6-99906049e372"
        }
    },
    "id": "293c1116-4050-47a1-ace0-be126b115d46",
    "verifyPolicy": {
        "id": "cf4fc8f1-9db1-45b1-a157-ab4035425e00"
    },
    "transactionStatus": {
        "status": "REQUESTED",
        "verificationStatus": {
            "FACIAL_COMPARISON_DOCUMENT": "REQUESTED",
            "FACIAL_COMPARISON_REFERENCE_SELFIE": "REQUESTED",
            "GOVERNMENT_ID": "REQUESTED",
            "LIVENESS": "REQUESTED"
        }
    },
    "qrUrl": "https://api.pingone.com/v1/idValidations/webVerifications/293c1116-4050-47a1-ace0-be126b115d46/qr",
    "webVerificationUrl": "https://apps.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/verify/verify-webapp/v2/index.html?txnid=293c1116-4050-47a1-ace0-be126b115d46&url=https%3A%2F%2Fapi.pingone.com%2Fv1%2FidValidations%2FwebVerifications&code=232660&envId=abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
    "webVerificationCode": "232660",
    "requirements": {
        "address": {
            "options": [
                "4321 Main Street #407, Hollywood, CA 90027",
                "4321 Main Street Apt 407, Hollywood, CA 90027"
            ]
        },
        "referenceSelfie": {
            "value": "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"
        },
        "phone": {
            "value": "+1 972-555-1234"
        },
        "birth_date": {
            "value": "1984-08-02"
        },
        "name": {
            "value": "Paddy Thornton"
        },
        "given_name": {
            "options": [
                "Paddy",
                "Pat"
            ]
        },
        "family_name": {
            "value": "Thornton"
        },
        "email": {
            "options": [
                "user@example.com",
                "test@mailinator.com"
            ]
        }
    },
    "callback": {
        "url": "https://example.com/testUrl2",
        "headers": {
            "x-environment-id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
            "x-phone": "+1 972-555-1234"
        }
    },
    "sendNotification": {
        "email": "user@example.com",
        "phone": "+1 972-555-1234",
        "results": [
            {
                "method": "SMS",
                "sent": true,
                "notification": {
                    "id": "00ce0d7d-7c8d-4898-befa-90d301195471"
                }
            },
            {
                "method": "EMAIL",
                "sent": true,
                "notification": {
                    "id": "0091eb4b-5180-4c93-b65c-3b8d181619b0"
                }
            }
        ]
    },
    "createdAt": "2024-02-06T15:00:28.250Z",
    "updatedAt": "2024-02-06T15:00:28.250Z",
    "expiresAt": "2024-02-06T15:30:28.250Z"
}
```

---

---
title: Delete All User Verified Data
description: Delete all verified data submitted by a specified user for a PingOne Verify verification transaction
component: pingone-api
page_id: pingone-api:verify:verified-data/delete-all-user-verified-data
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verified-data/delete-all-user-verified-data.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete All User Verified Data

##

Required permission:

* [idverifications:delete:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifiedUserData "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData
```

Delete all verified data submitted by the specified user with the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData` request.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")!,timeoutInterval: Double.infinity)
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
title: Delete All Verification MetaData
description: "Delete all identity verification metadata results for a specified user's verification transaction in PingOne Verify"
component: pingone-api
page_id: pingone-api:verify:verification-metadata/delete-all-verification-metadata
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verification-metadata/delete-all-verification-metadata.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete All Verification MetaData

##

Required permission:

* [idverifications:delete:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifiedUserData "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData
```

Delete all the results of identity data submitted by, and returned from verification for, a specified user with the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData` request.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")!,timeoutInterval: Double.infinity)
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
title: Delete All Verify Transaction Metrics
description: "Delete all application-event metrics for a specified user's PingOne Verify verification transaction"
component: pingone-api
page_id: pingone-api:verify:verification-metrics/delete-all-verify-transaction-metrics
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verification-metrics/delete-all-verify-transaction-metrics.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete All Verify Transaction Metrics

##

Required permission:

* [idverifications:delete:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifiedUserData "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents
```

Use the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents` request to delete the collection of all verify transaction metrics in the environment for the specified user for the specified transaction.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents")!,timeoutInterval: Double.infinity)
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
title: Delete One User Verified Data
description: Delete one type of verified data submitted by a specified user for a PingOne Verify verification transaction
component: pingone-api
page_id: pingone-api:verify:verified-data/delete-one-user-verified-data
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verified-data/delete-one-user-verified-data.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete One User Verified Data

##

Required permission:

* [idverifications:delete:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifiedUserData "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}
```

Delete one type of verified data submitted by the specified user with the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}` request. Use [Read All User Verified Data](read-all-user-verified-data.html) to get all verified data for the `{{transactionID}}` to find the `id` of the `type` sought.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData/{{verifiedDataID}}")!,timeoutInterval: Double.infinity)
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
title: Delete One Verification MetaData
description: "Delete one identity verification metadata result for a specified user's verification transaction in PingOne Verify"
component: pingone-api
page_id: pingone-api:verify:verification-metadata/delete-one-verification-metadata
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verification-metadata/delete-one-verification-metadata.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete One Verification MetaData

##

Required permission:

* [idverifications:delete:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifiedUserData "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}
```

Delete one result of identity data submitted by, and returned from verification for, a specified user with the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}` request.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")!,timeoutInterval: Double.infinity)
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
title: Delete One Verify Transaction Metric
description: "Delete one application-event metric for a specified user's PingOne Verify verification transaction"
component: pingone-api
page_id: pingone-api:verify:verification-metrics/delete-one-verify-transaction-metric
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verification-metrics/delete-one-verify-transaction-metric.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete One Verify Transaction Metric

##

Required permission:

* [idverifications:delete:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifiedUserData "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}
```

Use the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}` to delete the specified verify transaction metric in the environment for the specified user for the specified transaction.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents/{{appEventID}}")!,timeoutInterval: Double.infinity)
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
title: Delete Verification Document
description: Delete a document from a PingOne Verify verification transaction
component: pingone-api
page_id: pingone-api:verify:verify-documents/delete-verification-document
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-documents/delete-verification-document.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete Verification Document

##

Required permission:

* [idverifications:delete:document](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-document "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}
```

Use the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}` request to delete a document from a verification transaction.

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users/index.html), especially [User operations](../../platform/users/users-1/index.html).

* [Create a verify transaction](../verify-transactions/create-verify-transaction.html) to get a `transactionID` for the endpoint. Refer also to [Verify Transactions](../verify-transactions/index.html).

* [Create a verification document](create-verification-documents.html) to get a `documentID` for the endpoint. Refer also to [Verify Documents](index.html).

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents/{{documentID}}")!,timeoutInterval: Double.infinity)
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
title: Delete Verify Identity Assurance
description: Remove all identity assurance claims for a specified user in a PingOne environment
component: pingone-api
page_id: pingone-api:verify:verify-identity-assurance-ida/delete-verify-identity-assurance
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-identity-assurance-ida/delete-verify-identity-assurance.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete Verify Identity Assurance

##

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance
```

You remove all identity assurance claims for a specified user in a specified environment with the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance` operation.

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users/index.html), especially [User operations](../../platform/users/users-1/index.html).

* [Create a verify policy](../verify-policy/create-verify-policy.html) with `ida.enabled` set to `true` to save identity assurance claims for users as they are verified. Refer also to [Verify Policies](../verify-policy/index.html).

* [Create a verification transaction](../verify-transactions/create-verify-transaction.html) for a user to offer evidence of their identity, which generate identity assurance claims. Refer also to [Verify Transactions](../verify-transactions/index.html).

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/identityAssurance HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/identityAssurance")!,timeoutInterval: Double.infinity)
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
title: Delete Verify Policy
description: Delete a PingOne Verify policy from a specified environment
component: pingone-api
page_id: pingone-api:verify:verify-policy/delete-verify-policy
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-policy/delete-verify-policy.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete Verify Policy

##

Required permission:

* [idverifications:delete:verifyPolicy](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifyPolicy "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}
```

Delete a verify policy from the specified environment with the `DELETE {{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}` request.

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You cannot delete the default verify policy. If `{{verifyPolicyID}}` is the environment's default verify policy, you must make another verify policy the default with the [Update Verify Policy](update-verify-policy.html) request with `default` set to `true`. Then you can delete `{{verifyPolicyID}}`. |

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}"
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
DELETE /v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/verifyPolicies/{{verifyPolicyID}}")!,timeoutInterval: Double.infinity)
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
title: Delete Verify Transaction
description: Delete a specified PingOne Verify verification transaction for a user in an environment
component: pingone-api
page_id: pingone-api:verify:verify-transactions/delete-verify-transaction
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-transactions/delete-verify-transaction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete Verify Transaction

##

Required permission:

* [idverifications:delete:verifyTransactions](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-delete-verifyTransactions "Learn more about this permission")

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}
```

Use the `DELETE {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}` request to delete the specified verify transaction for the user in the environment.

The request returns `204 No Content` if successful.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}"
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
DELETE /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}")!,timeoutInterval: Double.infinity)
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
title: PingOne Verify
description: Explains PingOne Verify identity verification, transaction records, OpenID Connect for Identity Assurance, and US driver license validation
component: pingone-api
page_id: pingone-api:verify:index
canonical_url: https://developer.pingidentity.com/pingone-api/verify/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-07
page_aliases: ["introduction.adoc"]
section_ids:
  openid-connect-for-identity-assurance: OpenID Connect for Identity Assurance
  us-based-driver-licenses: US-based Driver Licenses
  request-groups: Request groups
---

# PingOne Verify

PingOne Verify provides identity verification so organizations can instantly ensure users are who they claim to be. Identity verification is the process of validating an end user to ensure their digital identity is tied to their real-life identity, such as a driver license, passport, or other government issued ID. Give your business the confidence that a user interacting with your brand is a real-life human and truly the person they claim to be, instead of someone else or a bot.

For a user to initiate an ID verification request, the client must obtain an ID verification transaction record from the ID verification service. The transaction record is created when a `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions` request is made.

The transaction record acts as permission for the user to engage in the verification process. The user can then submit the necessary user ID information (such as a driver license or passport) for verification by the ID Validation service. The user can also send a self-image that the ID Validation service compares to the submitted identity document, to ensure the submitter is the person on the document, and checks for liveness, to prevent fraud.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | These requests require `PING_ONE_VERIFY` in the Bill of Materials (BOM) for your environment. To check the BOM for the list of PingOne products associated with your environment, refer to [Read One Bill of Materials](../platform/bill-of-materials-bom/read-one-bill-of-materials.html). If `PING_ONE_VERIFY` is not in the BOM, contact your PingOne administrator to check whether your license supports adding this product to your environment. |

One of the challenges to identity proofing is getting high quality images from the user. Our Universal Capture frontends do the best quality verification they can, but it is still possible that the images will not pass the quality check of the identity proofing vendor. When images are taken during verification (such as submitting government documents, liveness checks, or selfies), retries can be permitted to obtain a satisfactory image for processing. The number of retries permitted, if any, are set on the [Verify Policy](verify-policy/index.html). The user's Universal Capture interface, such as a mobile phone with an app using the [PingOne Verify Native SDKs](../native-sdks/pingone-neo-native-sdks/pingone-verify-native-sdks/index.html), and the verification service negotiate directly for retries when an unacceptable image is submitted and a retry is permitted. Interaction at the API level is not required.

After verification, the transaction record also acts as a tracking mechanism to identify the user provisioned using ID Validation. This information is logged with the transaction record by the ID Validation service when the transaction ID is received by the client.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | All personally identifiable information (PII) is encrypted at rest and removed 30 minutes after a verification decision is made. |

## OpenID Connect for Identity Assurance

OpenID Connect for Identity Assurance, OIDC4IDA, is an extension of the OpenID Connect (OIDC) protocol specifically designed to provide higher levels of assurance in identity verification. It addresses scenarios where traditional OIDC might not provide sufficient assurances about the identity of users, especially in contexts requiring strong identity proofing and authentication measures.

Identity Assurance (IDA) is not a separate type of verification check, but rather aggregates data from other verification types performed. It is selected with `transaction.ida.enabled` when you [create a verify policy](verify-policy/create-verify-policy.html). It is a separate type of personally identifiable information (PII) that can be returned by [Verified Data](verified-data/index.html).

## US-based Driver Licenses

Document verification provides additional verification support with [American Association of Motor Vehicle Administrators](https://www.aamva.org/about) (AAMVA). AAMVA offers a service, [Driver's License Data Verification](https://www.aamva.org/technology/systems/verification-systems/dldv) (DLDV), for identity proofing and vetting driver license, identity cards, mobile driver license (mDL), and other secure credentials. Most states (43) and the District of Columbia participate in DLDV. No U.S. territories participate. The states that do *not* participate in DLDV are:

* Alaska (under review)

* California (SSA only)

* Louisiana (SSA only)

* Minnesota (SSA only)

* New York (SSA only)

* Pennsylvania (participates but requires written permission from the individual)

* Utah (SSA only)

`SSA only` indicates that only the Social Security Administration has access, not even other government agencies have access. SSA uses AAMVA for employment eligibility.

Submitting state-issued driver license or identity document to DLDV increases the accuracy of document authentication and also checks their validity by the state government. Accuracy and validity increase by comparing the biographic data, selfie, or both with the issuing government system of record, or another authoritative commercial system of record when the government system of record is unavailable. Results of DLDV checks are returned with the results of other checks in the [Verification Metadata](verification-metadata/index.html).

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | System of Record check (AAMVA DLDV) requires an additional license and is available only to environments in the North America region. |

## Request groups

The requests are grouped by endpoints for ease of use.

| Documentation                                                                                 | Endpoint                                                                                      |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [Verify policies](verify-policy/index.html)                                                   | /v1/environments/{{envID}}/verifyPolicies                                                     |
| [Verify transactions](verify-transactions/index.html)                                         | /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions                                |
| [Verify identity record matching](verify-identity-record-matching/index.html)                 | /v1/environments/{{envID}}/users/{{userID}}/identityRecordMatching                            |
| [Verify data-based identity verification](verify-data-based-identity-verification/index.html) | /v1/environments/{{envID}}/users/{{userID}}/dataBasedIdentityVerification                     |
| [Verify device ownership verification](verify-device-ownership-verification/index.html)       | /v1/environments/{{envID}}/users/{{userID}}/deviceOwnershipVerification                       |
| [Verify documents](verify-documents/index.html)                                               | /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents    |
| [Verified data](verified-data/index.html)                                                     | /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData |
| [Verification metadata](verification-metadata/index.html)                                     | /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData     |
| [Verify Identity Assurance (IDA)](verification-metadata/index.html)                           | /v1/environments/{{envID}}/users/{{userID}}/identityAssurance                                 |
| [Verification metrics](verification-metrics/index.html)                                       | /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/appEvents    |

---

---
title: Postman and the PingOne APIs
description: Explains how to download the PingOne Verify Postman collections and environment template for testing the PingOne Verify APIs
component: pingone-api
page_id: pingone-api:verify:working-with-pingone-apis/postman-and-pingone/index
canonical_url: https://developer.pingidentity.com/pingone-api/verify/working-with-pingone-apis/postman-and-pingone/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
---

# Postman and the PingOne APIs

We use Postman to create our PingOne Verify API docs, and have supplied our Postman collections for you to download. There's also an accompanying Postman Environment template already populated with the variables used in the collections.

If you aren't currently using Postman, you can install the free version. Refer to [Download Postman](https://www.postman.com/downloads/) to install Postman, either locally, or in your browser.

Refer to [The PingOne Verify API Postman collections](download-the-pingone-postman-collections.html#verify-collections) for the collections you can download or fork.

For more information about our Postman environment variables, refer to [The PingOne Postman environment template](use-the-pingone-postman-environment-template.html).

You'll also find all of the Postman collections for our documented PingOne use cases in our [Use Case Library](../../../workflow-library/index.html).

---

---
title: Process Verification Documents
description: Process all documents submitted to a PingOne Verify verification transaction while still permitting further submissions
component: pingone-api
page_id: pingone-api:verify:verify-documents/process-verification-documents
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-documents/process-verification-documents.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Process Verification Documents

##

Required permission:

* [idverifications:update:document](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-update-document "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents` request with a Content-Type of `application/vnd.pingidentity.documents.process+json` to have the service process all documents submitted to a verification transaction. This request requires no body.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | This processes documents that have been collected but still permits submitting more documents. |

For a list of permitted document types and the format of their values, refer to [Document types and values](index.html#verify-document-types-and-values).

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users/index.html), especially [User operations](../../platform/users/users-1/index.html).

* [Create a verify transaction](../verify-transactions/create-verify-transaction.html) to get a `transactionID` for the endpoint. Refer also to [Verify Transactions](../verify-transactions/index.html).

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.documents.process+json

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
curl --location --globoff --request POST '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents' \
--header 'Content-Type: application/vnd.pingidentity.documents.process+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.documents.process+json");
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.documents.process+json")
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
POST /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.documents.process+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.documents.process+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.documents.process+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.documents.process+json",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.documents.process+json',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"

payload = {}
headers = {
  'Content-Type': 'application/vnd.pingidentity.documents.process+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.documents.process+json',
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.documents.process+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.documents.process+json", forHTTPHeaderField: "Content-Type")
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb/documents/a7753108-2db2-4e38-8360-ef530e3169b3"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049"
        },
        "verifyTransaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb"
        }
    },
    "id": "a7753108-2db2-4e38-8360-ef530e3169b3",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "49825b76-e1df-4cdc-b973-0c580f1cb049"
    },
    "verifyTransaction": {
        "id": "e4e5eefc-41e9-42f1-b68f-77f92d5ec6bb"
    },
    "type": "Selfie",
    "value": "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",
    "status": "PROCESSED",
    "source": {
        "provider": "AUTHENTICATED_CLIENT"
    },
    "createdAt": "2022-08-26T12:27:28.886Z",
    "updatedAt": "2022-08-26T12:27:28.886Z"
}
```

---

---
title: Read All User Verified Data
description: Retrieve a list of verified data submitted by a specified user for a PingOne Verify verification transaction
component: pingone-api
page_id: pingone-api:verify:verified-data/read-all-user-verified-data
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verified-data/read-all-user-verified-data.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
  example-response-2: Example Response
---

# Read All User Verified Data

##

Required permission:

* [idverifications:get:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-get-verifiedUserData "Learn more about this permission")

```none
GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData
```

Get a list of verified data submitted by the specified user with the `GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData` request. Because the size of the data for some types can be quite large, the response to this request only includes the `id` and `type` of each. To retrieve the complete data for a type, use [Read One User Verified Data](read-one-user-verified-data.html) to get that specific type of verified data.

> **Collapse: Query parameters**
>
> | Parameter | Description                                                                                   |
> | --------- | --------------------------------------------------------------------------------------------- |
> | `type`    | Value is a case-insensitive, comma-delimited string (no spaces permitted) of types to return. |
> | `attempt` | Value defines which attempt or attempts to return.                                            |
>
> For `type`, available types are in the [Verified data data model](index.html#verify-verified-data-data-model). When `type` is used, the response includes the full [specific verified data data model](index.html#verify-specific-verified-data-data-model).
>
> For `attempt`, possible values and what each returns are:
>
> | Value    | Returns                                                                                                   |
> | -------- | --------------------------------------------------------------------------------------------------------- |
> | `ALL`    | Default value, latest attempt in `retry.attempt` and all other attempts in `retry.previousAttempts` array |
> | `LATEST` | Latest attempt only in `retry.attempt`                                                                    |
> | `1`      | First attempt only in `retry.attempt`                                                                     |
> | `2`      | Second attempt only in `retry.attempt`                                                                    |
> | `3`      | Third attempt only in `retry.attempt`                                                                     |
> | `4`      | Fourth attempt only in `retry.attempt`                                                                    |

The example responses show verified data from:

1. government identity document verification

2. Aadhaar document verification.

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData"
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
GET /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/verifiedData")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/"
        },
        "user": {
            "href": "https://api.pingone.com/v1/users/a27dec16-1e80-4f10-a261-2cac46a12b78"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "transaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b"
        }
    },
    "_embedded": {
        "verifiedData": [
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/84170421-62c6-49a5-b343-496bee93c206"
                    }
                },
                "id": "84170421-62c6-49a5-b343-496bee93c206",
                "type": "GOVERNMENT_ID",
                "createdAt": "2022-02-23T15:51:01.603Z",
                "retry": {
                    "attempt": 2
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/ef6cd8cd-d869-4695-af69-29c78b6f041a"
                    }
                },
                "id": "ef6cd8cd-d869-4695-af69-29c78b6f041a",
                "type": "SELFIE",
                "createdAt": "2022-02-25T16:22:35.649Z",
                "retry": {
                    "attempt": 2
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/bf6cd8cd-d869-4695-af69-29c78b6f041a"
                    }
                },
                "id": "bf6cd8cd-d869-4695-af69-29c78b6f041a",
                "type": "BACK_IMAGE",
                "createdAt": "2022-02-25T16:22:35.649Z",
                "retry": {
                    "attempt": 2
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/af6cd8cd-d869-4695-af69-29c78b6f041a"
                    }
                },
                "id": "af6cd8cd-d869-4695-af69-29c78b6f041a",
                "type": "FRONT_IMAGE",
                "createdAt": "2022-02-25T16:22:35.649Z",
                "retry": {
                    "attempt": 2
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/:id"
                    }
                },
                "id": "yf6cd8cd-d869-4695-af69-29c78b6f041a",
                "type": "DOCUMENT_PORTRAIT",
                "createdAt": "2022-02-25T16:22:35.649Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/:id"
                    }
                },
                "id": "vf6cd8cd-d869-4695-af69-29c78b6f041a",
                "type": "CROPPED_DOCUMENT",
                "createdAt": "2022-02-25T16:22:35.649Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/:id"
                    }
                },
                "id": "if6cd8cd-d869-4695-af69-29c78b6f041a",
                "type": "CROPPED_SIGNATURE",
                "createdAt": "2022-02-25T16:22:35.649Z"
            }
        ],
        "previousAttempts": [
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/320f341f-050b-4351-9585-5f16dba6667c"
                    }
                },
                "id": "320f341f-050b-4351-9585-5f16dba6667c",
                "type": "GOVERNMENT_ID",
                "createdAt": "2022-02-23T15:51:01.603Z",
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/ce0bb6d8-82d5-4ad0-b348-e7fb97edc64f"
                    }
                },
                "id": "ce0bb6d8-82d5-4ad0-b348-e7fb97edc64f",
                "type": "SELFIE",
                "createdAt": "2022-02-25T16:22:35.649Z",
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/639116d2-c1ff-44f3-bdba-af7e1e1d0bdd"
                    }
                },
                "id": "639116d2-c1ff-44f3-bdba-af7e1e1d0bdd",
                "type": "BACK_IMAGE",
                "createdAt": "2022-02-25T16:22:35.649Z",
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/verifiedData/92faff31-02c5-43af-b09a-c7eac93c59a4"
                    }
                },
                "id": "92faff31-02c5-43af-b09a-c7eac93c59a4",
                "type": "FRONT_IMAGE",
                "createdAt": "2022-02-25T16:22:35.649Z",
                "retry": {
                    "attempt": 1
                }
            }
        ]
    },
    "size": 7
}
```

### Example Response

200 OK

```json
{
    "_links": {
        "environment": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "verifyTransaction": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774"
        },
        "self": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData"
        },
        "user": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e"
        }
    },
    "_embedded": {
        "verifiedData": [
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData/84a9a538-4c78-3b96-ba62-33a8a43c4599"
                    }
                },
                "id": "84a9a538-4c78-3b96-ba62-33a8a43c4599",
                "type": "FRONT_IMAGE",
                "createdAt": "2025-04-10T17:31:50.545Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData/124efc59-7c37-33c7-8677-f725b7a4ef4c"
                    }
                },
                "id": "124efc59-7c37-33c7-8677-f725b7a4ef4c",
                "type": "BACK_IMAGE",
                "createdAt": "2025-04-10T17:31:50.552Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData/b9395684-bbda-378e-90bf-3d2da09cb9a2"
                    }
                },
                "id": "b9395684-bbda-378e-90bf-3d2da09cb9a2",
                "type": "DOCUMENT_PORTRAIT",
                "createdAt": "2025-04-10T17:32:53.001Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData/95085fe4-40f8-3938-92d2-fc05cbe4ea13"
                    }
                },
                "id": "95085fe4-40f8-3938-92d2-fc05cbe4ea13",
                "type": "SELFIE",
                "retry": {
                    "attempt": 1
                },
                "createdAt": "2025-04-10T17:31:50.536Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData/8b71dbd9-ca0f-4932-b0b9-96aed76671a2"
                    }
                },
                "id": "8b71dbd9-ca0f-4932-b0b9-96aed76671a2",
                "type": "END_USER_CLIENT",
                "createdAt": "2025-04-10T17:28:12.239Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData/456c88a8-75bb-4e1a-bae0-7f175d91cc9b"
                    }
                },
                "id": "456c88a8-75bb-4e1a-bae0-7f175d91cc9b",
                "type": "IDA",
                "createdAt": "2025-04-10T17:32:53.080Z"
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/verifiedData/6961411d-ac24-4b39-a6d0-c009b529ef62"
                    }
                },
                "id": "6961411d-ac24-4b39-a6d0-c009b529ef62",
                "type": "GOVERNMENT_ID",
                "createdAt": "2025-04-10T17:32:53.020Z"
            }
        ]
    },
    "size": 7
}
```

---

---
title: Read All Verification Documents
description: "Retrieve a list of documents submitted for a specified user's PingOne Verify verification transaction"
component: pingone-api
page_id: pingone-api:verify:verify-documents/read-all-verification-documents
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verify-documents/read-all-verification-documents.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read All Verification Documents

##

Required permission:

* [idverifications:get:document](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-get-document "Learn more about this permission")

```none
GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents
```

Get a list of documents submitted for a specified user for a specified verification transaction with the `GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents` request.

For a list of documents that can be submitted, refer to [Document types and values](index.html#verify-document-types-and-values).

### Prerequisites

* [Create a user](../../platform/users/users-1/create-user.html) to get a `userID` for the endpoint. Refer also to [Users](../../platform/users/index.html), especially [User operations](../../platform/users/users-1/index.html).

* [Create a verify transaction](../verify-transactions/create-verify-transaction.html) to get a `transactionID` for the endpoint. Refer also to [Verify Transactions](../verify-transactions/index.html).

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"
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
GET /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/documents")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c/documents"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "verifyTransaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c"
        }
    },
    "_embedded": {
        "documents": [
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c/documents/5c5163aa-e128-3af2-b118-d02a87899d0d"
                    }
                },
                "id": "5c5163aa-e128-3af2-b118-d02a87899d0d",
                "type": "Driver License Front",
                "status": "PROCESSED",
                "source": {
                    "provider": "END_USER"
                },
                "value": "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",
                "retry": {
                    "attempt": 2
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c/documents/412b0bdd-b3d7-3ac0-b083-b1851dcac758"
                    }
                },
                "id": "412b0bdd-b3d7-3ac0-b083-b1851dcac758",
                "type": "Selfie",
                "status": "PROCESSED",
                "source": {
                    "provider": "END_USER"
                },
                "value": "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",
                "retry": {
                    "attempt": 2
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c/documents/638762fd-12b7-3329-afc7-084e7cf624a6"
                    }
                },
                "id": "638762fd-12b7-3329-afc7-084e7cf624a6",
                "type": "Driver License Back",
                "status": "PROCESSED",
                "source": {
                    "provider": "END_USER"
                },
                "value": "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",
                "retry": {
                    "attempt": 2
                }
            }
        ],
        "previousAttempts": [
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c/documents/b5a695de-136d-4c6c-83cd-eb8a70e02fda"
                    }
                },
                "id": "b5a695de-136d-4c6c-83cd-eb8a70e02fda",
                "type": "Driver License Front",
                "status": "PROCESSED",
                "source": {
                    "provider": "END_USER"
                },
                "value": "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",
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c/documents/6b0b0f76-8cdd-4e6e-8b6f-49f4156b07da"
                    }
                },
                "id": "6b0b0f76-8cdd-4e6e-8b6f-49f4156b07da",
                "type": "Selfie",
                "status": "PROCESSED",
                "source": {
                    "provider": "END_USER"
                },
                "value": "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",
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/49825b76-e1df-4cdc-b973-0c580f1cb049/verifyTransactions/0839a8cb-1e82-4afc-baa1-c7719b7d038c/documents/d2de4a20-4853-4132-9421-30c8d2fd79ba"
                    }
                },
                "id": "d2de4a20-4853-4132-9421-30c8d2fd79ba",
                "type": "Driver License Back",
                "status": "PROCESSED",
                "source": {
                    "provider": "END_USER"
                },
                "value": "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",
                "retry": {
                    "attempt": 1
                }
            }
        ]
    },
    "size": 3
}
```

---

---
title: Read All Verification MetaData
description: "Retrieve all identity verification metadata results for a specified user's verification transaction in PingOne Verify"
component: pingone-api
page_id: pingone-api:verify:verification-metadata/read-all-verification-metadata
canonical_url: https://developer.pingidentity.com/pingone-api/verify/verification-metadata/read-all-verification-metadata.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-05
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
  example-response-2: Example Response
  example-response-3: Example Response
---

# Read All Verification MetaData

##

Required permission:

* [idverifications:get:verifiedUserData](../../platform/reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-idverifications-get-verifiedUserData "Learn more about this permission")

```none
GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData
```

Get all the results of identity data submitted by, and returned from verification for, a specified user with the `GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData` request.

The examples show metadata from:

1. government identity metadata

2. Aadhaar metadata

3. Government identity document verification with facial comparison to both the document portrait and a reference selfie

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData"
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
GET /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6/metaData"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "verifyTransaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6"
        }
    },
    "_embedded": {
        "metaData": [
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6/metaData/4ebb9165-4e5c-4270-94e4-d50d7b17ecb4"
                    }
                },
                "id": "4ebb9165-4e5c-4270-94e4-d50d7b17ecb4",
                "provider": "IDRND",
                "type": "LIVENESS",
                "status": "SUCCESS",
                "data": {
                    "score": 6.4909873,
                    "probability": 0.99848527,
                    "quality": 0.94462675
                },
                "retry": {
                    "attempt": 2
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6/metaData/ae186d6c-1a79-4912-bad8-79afa3626cca"
                    }
                },
                "id": "ae186d6c-1a79-4912-bad8-79afa3626cca",
                "provider": "IDRND",
                "type": "INJECTION_DETECTION",
                "status": "SUCCESS",
                "data": {
                    "probability": 1.0
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6/metaData/546d3a8e-f606-4078-92f1-96a5c2d003e9"
                    }
                },
                "id": "546d3a8e-f606-4078-92f1-96a5c2d003e9",
                "provider": "AMAZON",
                "type": "FACIAL_COMPARISON",
                "status": "SUCCESS",
                "data": {
                    "similarity": 99.37002,
                    "confidence": 99.99767,
                    "quality": {
                        "brightness": 36.77353,
                        "sharpness": 20.92731
                    }
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6/metaData/96315a69-fb46-4d28-9b0d-c79927e59df1"
                    }
                },
                "id": "96315a69-fb46-4d28-9b0d-c79927e59df1",
                "provider": "BIOGRAPHIC_MATCHER",
                "type": "BIOGRAPHIC_MATCH",
                "status": "SUCCESS",
                "data": {
                    "biographic_match_results": [
                        {
                            "identifier": "address",
                            "match": "NOT_APPLICABLE"
                        },
                        {
                            "identifier": "given_name",
                            "match": "NONE"
                        },
                        {
                            "identifier": "family_name",
                            "match": "HIGH"
                        },
                        {
                            "identifier": "birth_date",
                            "match": "HIGH"
                        }
                    ]
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6/metaData/fba13756-8c24-49ff-9b42-ff1a3661d0ae"
                    }
                },
                "id": "fba13756-8c24-49ff-9b42-ff1a3661d0ae",
                "provider": "MITEK",
                "type": "DOCUMENT_AUTHENTICATION",
                "status": "SUCCESS",
                "data": {
                    "mitekVerifications": [
                        {
                            "name": "Document Ensemble Authenticator",
                            "judgement": "Authentic",
                            "verificationType": 202,
                            "probability": 753,
                            "version": "3.47.0.7114",
                            "documentId": "048f28f1-a7fe-42a5-9722-f10977606719"
                        },
                        {
                            "name": "Black And White Copy",
                            "judgement": "Authentic",
                            "verificationType": 102,
                            "probability": 717,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "Image Classification",
                            "judgement": "Authentic",
                            "verificationType": 105,
                            "probability": 1000,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "Data Comparison",
                            "judgement": "Authentic",
                            "verificationType": 700,
                            "probability": 1000,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "Ensemble Authenticator",
                            "judgement": "Authentic",
                            "verificationType": 201,
                            "probability": 753,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "ID Document Blacklist",
                            "judgement": "Authentic",
                            "verificationType": 101,
                            "probability": 1000,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "Generic Font",
                            "judgement": "Authentic",
                            "verificationType": 104,
                            "probability": 926,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "MRZ Check Digit",
                            "judgement": "Authentic",
                            "verificationType": 601,
                            "probability": 1000,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "MRZ Font Type Authentication",
                            "judgement": "Authentic",
                            "verificationType": 600,
                            "probability": 1000,
                            "version": "3.47.0.7114",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "Image Processing",
                            "judgement": "Authentic",
                            "verificationType": 710,
                            "probability": 1000,
                            "version": "1.0",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        },
                        {
                            "name": "Document Liveness",
                            "judgement": "Authentic",
                            "verificationType": 108,
                            "probability": 999,
                            "version": "1.0",
                            "documentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856"
                        }
                    ],
                    "frontImageDocumentId": "e290d74d-bf9c-4116-9fe7-9b6fb909c856",
                    "documentEvidenceId": "048f28f1-a7fe-42a5-9722-f10977606719",
                    "retry": {
                        "attempt": 1
                    }
                }
            }
        ]
    },
    "previousAttempts": [
        {
            "_links": {
                "self": {
                    "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/03df72b1-b80b-4449-8eef-ee8f85f48d94/verifyTransactions/7668563d-0226-4ca5-8401-03f6dc5bcdc6/metaData/06aebfbd-0053-4860-8b59-4f3cb7371dcb"
                }
            },
            "id": "06aebfbd-0053-4860-8b59-4f3cb7371dcb",
            "provider": "IDRND",
            "type": "LIVENESS",
            "status": "FAIL",
            "data": {
                "score": 2.4509223,
                "probability": 0.40062885,
                "quality": 0.40874674
            },
            "retry": {
                "attempt": 1
            }
        }
    ],
    "size": 5
}
```

### Example Response

200 OK

```json
{
    "_links": {
        "environment": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "verifyTransaction": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774"
        },
        "self": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/metaData"
        },
        "user": {
            "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e"
        }
    },
    "_embedded": {
        "metaData": [
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/metaData/18258efd-c8ef-4365-b80e-730f4b730203"
                    }
                },
                "id": "18258efd-c8ef-4365-b80e-730f4b730203",
                "provider": "TRINSIC",
                "type": "AADHAAR",
                "status": "SUCCESS",
                "data": {
                    "success": true,
                    "done": true
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/metaData/9ae17c91-5d6a-491f-b541-8c92c804422a"
                    }
                },
                "id": "9ae17c91-5d6a-491f-b541-8c92c804422a",
                "provider": "IDRND",
                "type": "LIVENESS",
                "status": "SUCCESS",
                "data": {
                    "score": 0,
                    "probability": 0.99,
                    "quality": 0
                },
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/metaData/39b4d2b8-52a2-483e-8c3a-bce5102424ee"
                    }
                },
                "id": "39b4d2b8-52a2-483e-8c3a-bce5102424ee",
                "provider": "AMAZON",
                "type": "FACIAL_COMPARISON",
                "status": "SUCCESS",
                "data": {
                    "similarity": 99,
                    "quality": {
                        "brightness": 50,
                        "sharpness": 50
                    }
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "http://api.pingone.com/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/af1397ec-189b-4ae5-a99b-d6f8bc91664e/verifyTransactions/703f0eb4-f996-48df-812d-42ae69582774/metaData/89357261-baae-4c4f-9019-7d965613e784"
                    }
                },
                "id": "89357261-baae-4c4f-9019-7d965613e784",
                "provider": "IDRND",
                "type": "INJECTION_DETECTION",
                "status": "SUCCESS",
                "data": {
                    "probability": 1
                },
                "retry": {
                    "attempt": 1
                }
            }
        ]
    },
    "size": 4
}
```

### Example Response

200 OK

```json
{
    "_links": {
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "verifyTransaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d/verifyTransactions/20fa1e5e-12fb-4305-8feb-799af19620d9"
        },
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d/verifyTransactions/20fa1e5e-12fb-4305-8feb-799af19620d9/metaData"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d"
        }
    },
    "_embedded": {
        "metaData": [
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d/verifyTransactions/20fa1e5e-12fb-4305-8feb-799af19620d9/metaData/60a28117-8233-4d58-a99b-e08b061e9714"
                    }
                },
                "id": "60a28117-8233-4d58-a99b-e08b061e9714",
                "provider": "MITEK",
                "type": "AAMVA",
                "status": "SUCCESS",
                "data": {
                    "requestId": "680e5025-a682-4917-8367-0dced7c9af17",
                    "matchResults": {
                        "dateOfBirth": true,
                        "documentNumber": true
                    },
                    "status": "Successful"
                },
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d/verifyTransactions/20fa1e5e-12fb-4305-8feb-799af19620d9/metaData/61d8c027-1689-4720-9cda-f0698228bba5"
                    }
                },
                "id": "61d8c027-1689-4720-9cda-f0698228bba5",
                "provider": "AMAZON",
                "type": "FACIAL_COMPARISON_REFERENCE_SELFIE",
                "status": "SUCCESS",
                "data": {
                    "comparisons": [
                        {
                            "source": "SELFIE",
                            "target": "REQUIREMENTS",
                            "status": "SUCCESS",
                            "detailedResults": {
                                "similarity": 99.99906,
                                "confidence": 99.99642,
                                "quality": {
                                    "brightness": 87.33947,
                                    "sharpness": 99.549995
                                }
                            }
                        }
                    ]
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d/verifyTransactions/20fa1e5e-12fb-4305-8feb-799af19620d9/metaData/cc82876c-08f1-4a6d-a100-836f99303ace"
                    }
                },
                "id": "cc82876c-08f1-4a6d-a100-836f99303ace",
                "provider": "VERIFF",
                "type": "DOCUMENT_AUTHENTICATION",
                "status": "SUCCESS",
                "data": {
                    "veriffVerification": {
                        "vendorData": "20fa1e5e-12fb-4305-8feb-799af19620d9",
                        "status": "approved",
                        "id": "bd0bd1a1-7b59-4ba0-a19b-3f308c109821",
                        "code": 9001,
                        "decisionTime": "2025-05-28T18:47:47.425621Z",
                        "acceptanceTime": "2025-05-28T18:47:37.738651Z"
                    }
                },
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d/verifyTransactions/20fa1e5e-12fb-4305-8feb-799af19620d9/metaData/0a454f32-9ebc-4b0a-bee2-ecbb4a4e1cd2"
                    }
                },
                "id": "0a454f32-9ebc-4b0a-bee2-ecbb4a4e1cd2",
                "provider": "IDRND",
                "type": "LIVENESS",
                "status": "SUCCESS",
                "data": {
                    "score": 0.12734735,
                    "probability": 0.5317939,
                    "quality": 0.99473304
                },
                "retry": {
                    "attempt": 1
                }
            },
            {
                "_links": {
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/8d68b29b-f510-4ebf-8a99-b3c90d56ca4d/verifyTransactions/20fa1e5e-12fb-4305-8feb-799af19620d9/metaData/462790f2-d29d-4928-b8d7-7d902bd36719"
                    }
                },
                "id": "462790f2-d29d-4928-b8d7-7d902bd36719",
                "provider": "AMAZON",
                "type": "FACIAL_COMPARISON",
                "status": "SUCCESS",
                "data": {
                    "similarity": 99.88053,
                    "confidence": 99.99928,
                    "quality": {
                        "brightness": 79.84607,
                        "sharpness": 73.3221
                    }
                }
            }
        ]
    },
    "size": 5
}
```
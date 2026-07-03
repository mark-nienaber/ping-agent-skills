---
title: Approve Snapshot
description: The POST /version-control/snapshots/{{snapshotId}}/addApproval operation adds approval to the snapshot specified by the ID in the request URL.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/version-control/snapshot-management/approve-snapshot
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/version-control/snapshot-management/approve-snapshot.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Approve Snapshot

##

```none
POST {{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval
```

The `POST /version-control/snapshots/{{snapshotId}}/addApproval` operation adds approval to the snapshot specified by the ID in the request URL.

### Headers

x-user-id      {{userId}}

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
curl --location --globoff --request POST '{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval' \
--header 'x-user-id: {{userId}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
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

  url := "{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")

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
POST /version-control/snapshots/{{snapshotId}}/addApproval HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}"
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
  'url': '{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval',
  'headers': {
    'x-user-id': '{{userId}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval"

payload = {}
headers = {
  'x-user-id': '{{userId}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}'
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

url = URI("{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/version-control/snapshots/{{snapshotId}}/addApproval")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")

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
    "id": "5c400c4e-ac2b-4e08-8f28-d9a25c5f037e",
    "parentId": "bb23e640-86e0-4373-ab95-64aaf86b4e9a",
    "state": "COMMITTED",
    "commitDetails": {
        "userId": "admin",
        "dateTime": "2024-11-22T19:39:20.150490Z",
        "message": "first commit"
    },
    "approvals": [
        "selfgovernanceadmin"
    ],
    "branchId": "9df2835b-cbbb-4ef9-a20e-ab63c0b6da67"
}
```

---

---
title: Authentication
description: Clients authenticate to the SCIM APIs by using bearer token authentication, as defined by RFC 6750. Every request must include an Authorization request header, where the header value uses the form Bearer {access token}.
component: pingauthorize
page_id: pingauthorize:pingauthorize:scim/authentication
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/scim/authentication.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authentication

Clients authenticate to the SCIM APIs by using bearer token authentication, as defined by [RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750). Every request must include an Authorization request header, where the header value uses the form `Bearer {access token}`.

A bearer token must be obtained from an external authorization server, such as PingFederate.

---

---
title: Authorization
description: By default, the access token provided by the client in the request (refer to Authentication) is used to control access to requested resources. The PingAuthorize Server's access control policies are customizable, but in general, the scopes granted by the access token determine which resources and attributes are returned.
component: pingauthorize
page_id: pingauthorize:pingauthorize:scim/authorization
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/scim/authorization.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authorization

By default, the access token provided by the client in the request (refer to [Authentication](authentication.html)) is used to control access to requested resources. The PingAuthorize Server's access control policies are customizable, but in general, the scopes granted by the access token determine which resources and attributes are returned.

If access controls determine that the client cannot access the requested resource, then a response with a `403` status code is returned.

```json
{
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:Error"
    ],
    "scimType": "insufficient_scope",
    "status": 403,
    "detail": "Requested operation not allowed by the granted OAuth2 scopes."
}
```

A client may be allowed to access a resource but not all of its attributes. Clients should be prepared to receive incomplete resources, including resources stripped of attributes that are required by the schema.

For information about how to configure an application appropriately for SCIM API access, refer to configuring scopes in the PingAuthorize Server client developer guide.

---

---
title: Authorization
description: Before calculating a decision, the XACML-JSON PDP API attempts to authorize the client making the XACML-JSON PDP API request by invoking the Policy Decision Service.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-decision/xacml-json-pdp/authorization
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision/xacml-json-pdp/authorization.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authorization

Before calculating a decision, the XACML-JSON PDP API attempts to authorize the client making the XACML-JSON PDP API request by invoking the Policy Decision Service.

To target a PDP authorization request in-policy, it must apply to the `PDP` Service and the `authorize` Action. The default policies included with PingAuthorize Server perform this authorization by only permitting requests with active access tokens that contain the `urn:pingauthorize:pdp` scope.

For example, under the default policies, the following request would result in an authorized client when the PDP is configured with a mock access token validator:

```bash
curl --insecure -X POST \
  -H 'Authorization: Bearer {"active":true,"scope":"urn:pingauthorize:pdp", "sub":"<valid-subject>"}' \
  -H 'Content-Type: application/xacml+json' \
  -d '{"Request":{}}' "https://<your-pingauthorize-host>:<your-pingauthorize-port>/pdp"
```

The default policies are intended to provide a foundation. You can modify these policies if additional authorization logic is required.

---

---
title: Authorize Client with Batch Decision
description: The POST /governance-engine/batch operation authorizes the client using an individual request. On successful client authorization, the JSON PDP API invokes the Policy Decision Service.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-decision/json-pdp/batch-requests/authorize-client-with-batch-decision
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision/json-pdp/batch-requests/authorize-client-with-batch-decision.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Authorize Client with Batch Decision

##

```none
POST {{apiPath}}/governance-engine/batch
```

The `POST /governance-engine/batch` operation authorizes the client using an individual request. On successful client authorization, the JSON PDP API invokes the Policy Decision Service.

The `{{apiPath}}` variable in this request represents the client's PingAuthorize host and port. For example, `https://<your-pingauthorize-host>:<your-pingauthorize-port>`.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

Accept      application/json

### Body

raw ( application/json )

```json
{
  "requests": [
    {
      "domain": "Sales.Asia Pacific",
      "action": "Retrieve",
      "service": "Mobile.Landing page",
      "identityProvider": "Social Networks.Spacebook",
      "attributes": {
        "Prospect name": "B. Vo"
      }
    },
    {
      "domain": "Sales.EMEA",
      "action": "Search",
      "service": "Mobile.Users search",
      "identityProvider": "Social Networks.Chirper",
      "attributes": {
        "Prospect name": "A. Mann"
      }
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
curl --location --globoff '{{apiPath}}/governance-engine/batch' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "requests": [
    {
      "domain": "Sales.Asia Pacific",
      "action": "Retrieve",
      "service": "Mobile.Landing page",
      "identityProvider": "Social Networks.Spacebook",
      "attributes": {
        "Prospect name": "B. Vo"
      }
    },
    {
      "domain": "Sales.EMEA",
      "action": "Search",
      "service": "Mobile.Users search",
      "identityProvider": "Social Networks.Chirper",
      "attributes": {
        "Prospect name": "A. Mann"
      }
    }
  ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/governance-engine/batch")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Accept", "application/json");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""requests"": [" + "\n" +
@"    {" + "\n" +
@"      ""domain"": ""Sales.Asia Pacific""," + "\n" +
@"      ""action"": ""Retrieve""," + "\n" +
@"      ""service"": ""Mobile.Landing page""," + "\n" +
@"      ""identityProvider"": ""Social Networks.Spacebook""," + "\n" +
@"      ""attributes"": {" + "\n" +
@"        ""Prospect name"": ""B. Vo""" + "\n" +
@"      }" + "\n" +
@"    }," + "\n" +
@"    {" + "\n" +
@"      ""domain"": ""Sales.EMEA""," + "\n" +
@"      ""action"": ""Search""," + "\n" +
@"      ""service"": ""Mobile.Users search""," + "\n" +
@"      ""identityProvider"": ""Social Networks.Chirper""," + "\n" +
@"      ""attributes"": {" + "\n" +
@"        ""Prospect name"": ""A. Mann""" + "\n" +
@"      }" + "\n" +
@"    }" + "\n" +
@"  ]" + "\n" +
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

  url := "{{apiPath}}/governance-engine/batch"
  method := "POST"

  payload := strings.NewReader(`{
  "requests": [
    {
      "domain": "Sales.Asia Pacific",
      "action": "Retrieve",
      "service": "Mobile.Landing page",
      "identityProvider": "Social Networks.Spacebook",
      "attributes": {
        "Prospect name": "B. Vo"
      }
    },
    {
      "domain": "Sales.EMEA",
      "action": "Search",
      "service": "Mobile.Users search",
      "identityProvider": "Social Networks.Chirper",
      "attributes": {
        "Prospect name": "A. Mann"
      }
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
  req.Header.Add("Accept", "application/json")
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
POST /governance-engine/batch HTTP/1.1
Host: {{apiPath}}
Accept: application/json
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "requests": [
    {
      "domain": "Sales.Asia Pacific",
      "action": "Retrieve",
      "service": "Mobile.Landing page",
      "identityProvider": "Social Networks.Spacebook",
      "attributes": {
        "Prospect name": "B. Vo"
      }
    },
    {
      "domain": "Sales.EMEA",
      "action": "Search",
      "service": "Mobile.Users search",
      "identityProvider": "Social Networks.Chirper",
      "attributes": {
        "Prospect name": "A. Mann"
      }
    }
  ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"requests\": [\n    {\n      \"domain\": \"Sales.Asia Pacific\",\n      \"action\": \"Retrieve\",\n      \"service\": \"Mobile.Landing page\",\n      \"identityProvider\": \"Social Networks.Spacebook\",\n      \"attributes\": {\n        \"Prospect name\": \"B. Vo\"\n      }\n    },\n    {\n      \"domain\": \"Sales.EMEA\",\n      \"action\": \"Search\",\n      \"service\": \"Mobile.Users search\",\n      \"identityProvider\": \"Social Networks.Chirper\",\n      \"attributes\": {\n        \"Prospect name\": \"A. Mann\"\n      }\n    }\n  ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/governance-engine/batch")
  .method("POST", body)
  .addHeader("Accept", "application/json")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/governance-engine/batch",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "requests": [
      {
        "domain": "Sales.Asia Pacific",
        "action": "Retrieve",
        "service": "Mobile.Landing page",
        "identityProvider": "Social Networks.Spacebook",
        "attributes": {
          "Prospect name": "B. Vo"
        }
      },
      {
        "domain": "Sales.EMEA",
        "action": "Search",
        "service": "Mobile.Users search",
        "identityProvider": "Social Networks.Chirper",
        "attributes": {
          "Prospect name": "A. Mann"
        }
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
  'url': '{{apiPath}}/governance-engine/batch',
  'headers': {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "requests": [
      {
        "domain": "Sales.Asia Pacific",
        "action": "Retrieve",
        "service": "Mobile.Landing page",
        "identityProvider": "Social Networks.Spacebook",
        "attributes": {
          "Prospect name": "B. Vo"
        }
      },
      {
        "domain": "Sales.EMEA",
        "action": "Search",
        "service": "Mobile.Users search",
        "identityProvider": "Social Networks.Chirper",
        "attributes": {
          "Prospect name": "A. Mann"
        }
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

url = "{{apiPath}}/governance-engine/batch"

payload = json.dumps({
  "requests": [
    {
      "domain": "Sales.Asia Pacific",
      "action": "Retrieve",
      "service": "Mobile.Landing page",
      "identityProvider": "Social Networks.Spacebook",
      "attributes": {
        "Prospect name": "B. Vo"
      }
    },
    {
      "domain": "Sales.EMEA",
      "action": "Search",
      "service": "Mobile.Users search",
      "identityProvider": "Social Networks.Chirper",
      "attributes": {
        "Prospect name": "A. Mann"
      }
    }
  ]
})
headers = {
  'Accept': 'application/json',
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
$request->setUrl('{{apiPath}}/governance-engine/batch');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Accept' => 'application/json',
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "requests": [\n    {\n      "domain": "Sales.Asia Pacific",\n      "action": "Retrieve",\n      "service": "Mobile.Landing page",\n      "identityProvider": "Social Networks.Spacebook",\n      "attributes": {\n        "Prospect name": "B. Vo"\n      }\n    },\n    {\n      "domain": "Sales.EMEA",\n      "action": "Search",\n      "service": "Mobile.Users search",\n      "identityProvider": "Social Networks.Chirper",\n      "attributes": {\n        "Prospect name": "A. Mann"\n      }\n    }\n  ]\n}');
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

url = URI("{{apiPath}}/governance-engine/batch")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Accept"] = "application/json"
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "requests": [
    {
      "domain": "Sales.Asia Pacific",
      "action": "Retrieve",
      "service": "Mobile.Landing page",
      "identityProvider": "Social Networks.Spacebook",
      "attributes": {
        "Prospect name": "B. Vo"
      }
    },
    {
      "domain": "Sales.EMEA",
      "action": "Search",
      "service": "Mobile.Users search",
      "identityProvider": "Social Networks.Chirper",
      "attributes": {
        "Prospect name": "A. Mann"
      }
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"requests\": [\n    {\n      \"domain\": \"Sales.Asia Pacific\",\n      \"action\": \"Retrieve\",\n      \"service\": \"Mobile.Landing page\",\n      \"identityProvider\": \"Social Networks.Spacebook\",\n      \"attributes\": {\n        \"Prospect name\": \"B. Vo\"\n      }\n    },\n    {\n      \"domain\": \"Sales.EMEA\",\n      \"action\": \"Search\",\n      \"service\": \"Mobile.Users search\",\n      \"identityProvider\": \"Social Networks.Chirper\",\n      \"attributes\": {\n        \"Prospect name\": \"A. Mann\"\n      }\n    }\n  ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/governance-engine/batch")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Accept")
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

200 OK

```json
{
    "responses": [
        {
            "id": "12345678-90ab-cdef-1234-567890abcdef",
            "deploymentPackageId": "12345678-90ab-cdef-1234-567890abcdef",
            "timestamp": "2021-06-11T04:18:32.820482Z",
            "elapsedTime": 830492,
            "decision": "PERMIT",
            "authorized": true,
            "statements": [
                {
                    "id": "12345678-90ab-cdef-1234-567890abcdef",
                    "name": "Advice Name",
                    "code": "advice-code",
                    "payload": "{\"data\": \"some data\"}",
                    "obligatory": true,
                    "fulfilled": false,
                    "attributes": {}
                }
            ],
            "status": {
                "code": "OKAY",
                "messages": [],
                "errors": []
            }
        },
        {
            "id": "fedcba09-8765-4321-fedcba098765",
            "deploymentPackageId": "fedcba09-8765-4321-fedcba098765",
            "timestamp": "2021-06-11T04:18:33.650974Z",
            "elapsedTime": 492048,
            "decision": "PERMIT",
            "authorized": true,
            "statements": [
                {
                    "id": "fedcba09-8765-4321-fedcba098765",
                    "name": "Different Advice",
                    "code": "advice-code",
                    "payload": "{\"data\": \"other data\"}",
                    "obligatory": false,
                    "fulfilled": false,
                    "attributes": {}
                }
            ],
            "status": {
                "code": "OKAY",
                "messages": [],
                "errors": []
            }
        }
    ]
}
```

---

---
title: Authorize Client with Individual Decision
description: The POST /governance-engine operation authorizes the client using an individual request. On successful client authorization, the JSON PDP API invokes the Policy Decision Service.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-decision/json-pdp/individual-requests/authorize-client-with-individual-decision
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision/json-pdp/individual-requests/authorize-client-with-individual-decision.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Authorize Client with Individual Decision

##

```none
POST {{apiPath}}/governance-engine
```

The `POST /governance-engine` operation authorizes the client using an individual request. On successful client authorization, the JSON PDP API invokes the Policy Decision Service.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

Accept      application/json

### Body

raw ( application/json )

```json
{
  "domain": "Sales.Asia Pacific",
  "action": "Retrieve",
  "service": "Mobile.Landing page",
  "identityProvider": "Social Networks.Spacebook",
  "attributes": {
    "Prospect name": "B. Vo"
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
curl --location --globoff '{{apiPath}}/governance-engine' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "domain": "Sales.Asia Pacific",
  "action": "Retrieve",
  "service": "Mobile.Landing page",
  "identityProvider": "Social Networks.Spacebook",
  "attributes": {
    "Prospect name": "B. Vo"
  }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/governance-engine")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Accept", "application/json");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""domain"": ""Sales.Asia Pacific""," + "\n" +
@"  ""action"": ""Retrieve""," + "\n" +
@"  ""service"": ""Mobile.Landing page""," + "\n" +
@"  ""identityProvider"": ""Social Networks.Spacebook""," + "\n" +
@"  ""attributes"": {" + "\n" +
@"    ""Prospect name"": ""B. Vo""" + "\n" +
@"  }" + "\n" +
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

  url := "{{apiPath}}/governance-engine"
  method := "POST"

  payload := strings.NewReader(`{
  "domain": "Sales.Asia Pacific",
  "action": "Retrieve",
  "service": "Mobile.Landing page",
  "identityProvider": "Social Networks.Spacebook",
  "attributes": {
    "Prospect name": "B. Vo"
  }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Accept", "application/json")
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
POST /governance-engine HTTP/1.1
Host: {{apiPath}}
Accept: application/json
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "domain": "Sales.Asia Pacific",
  "action": "Retrieve",
  "service": "Mobile.Landing page",
  "identityProvider": "Social Networks.Spacebook",
  "attributes": {
    "Prospect name": "B. Vo"
  }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"domain\": \"Sales.Asia Pacific\",\n  \"action\": \"Retrieve\",\n  \"service\": \"Mobile.Landing page\",\n  \"identityProvider\": \"Social Networks.Spacebook\",\n  \"attributes\": {\n    \"Prospect name\": \"B. Vo\"\n  }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/governance-engine")
  .method("POST", body)
  .addHeader("Accept", "application/json")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/governance-engine",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "domain": "Sales.Asia Pacific",
    "action": "Retrieve",
    "service": "Mobile.Landing page",
    "identityProvider": "Social Networks.Spacebook",
    "attributes": {
      "Prospect name": "B. Vo"
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
  'url': '{{apiPath}}/governance-engine',
  'headers': {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "domain": "Sales.Asia Pacific",
    "action": "Retrieve",
    "service": "Mobile.Landing page",
    "identityProvider": "Social Networks.Spacebook",
    "attributes": {
      "Prospect name": "B. Vo"
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

url = "{{apiPath}}/governance-engine"

payload = json.dumps({
  "domain": "Sales.Asia Pacific",
  "action": "Retrieve",
  "service": "Mobile.Landing page",
  "identityProvider": "Social Networks.Spacebook",
  "attributes": {
    "Prospect name": "B. Vo"
  }
})
headers = {
  'Accept': 'application/json',
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
$request->setUrl('{{apiPath}}/governance-engine');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Accept' => 'application/json',
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "domain": "Sales.Asia Pacific",\n  "action": "Retrieve",\n  "service": "Mobile.Landing page",\n  "identityProvider": "Social Networks.Spacebook",\n  "attributes": {\n    "Prospect name": "B. Vo"\n  }\n}');
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

url = URI("{{apiPath}}/governance-engine")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Accept"] = "application/json"
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "domain": "Sales.Asia Pacific",
  "action": "Retrieve",
  "service": "Mobile.Landing page",
  "identityProvider": "Social Networks.Spacebook",
  "attributes": {
    "Prospect name": "B. Vo"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"domain\": \"Sales.Asia Pacific\",\n  \"action\": \"Retrieve\",\n  \"service\": \"Mobile.Landing page\",\n  \"identityProvider\": \"Social Networks.Spacebook\",\n  \"attributes\": {\n    \"Prospect name\": \"B. Vo\"\n  }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/governance-engine")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Accept")
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

200 OK

```json
{
    "id": "12345678-90ab-cdef-1234-567890abcdef",
    "deploymentPackageId": "12345678-90ab-cdef-1234-567890abcdef",
    "timestamp": "2021-06-11T03:12:19.720485Z",
    "elapsedTime": 184024,
    "decision": "PERMIT",
    "authorized": true,
    "statements": [
        {
            "id": "12345678-90ab-cdef-1234-567890abcdef",
            "name": "Statement Name",
            "code": "statement-code",
            "payload": "{\"data\": \"some data\"}",
            "obligatory": true,
            "fulfilled": false,
            "attributes": {}
        }
    ],
    "status": {
        "code": "OKAY",
        "messages": [],
        "errors": []
    }
}
```

---

---
title: Authorize Client With MultiRequests JSON Object
description: The POST /pdp operation authorizes the client using the MultiRequests JSON object. On successful client authorization, the XACML-JSON PDP API invokes the Policy Decision Service with batch decision requests converted from the XACML-JSON request.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-decision/xacml-json-pdp/requests-and-responses/authorize-client-with-multirequests-json-object
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision/xacml-json-pdp/requests-and-responses/authorize-client-with-multirequests-json-object.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Authorize Client With MultiRequests JSON Object

##

```none
POST {{apiPath}}/pdp
```

The `POST /pdp` operation authorizes the client using the MultiRequests JSON object. On successful client authorization, the XACML-JSON PDP API invokes the Policy Decision Service with batch decision requests converted from the XACML-JSON request.

The `{{apiPath}}` variable in this request represents the client's PingAuthorize host and port. For example, `https://<your-pingauthorize-host>:<your-pingauthorize-port>`.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/xacml+json

Accept      application/xacml+json

### Body

raw ( application/xacml+json )

```json
{
  "Request": {
    "MultiRequests": {
      "RequestReference": [{
        "ReferenceId": [
          "dom",
          "act",
          "srv",
          "idp",
          "att"
        ]
      }]
    },
    "AccessSubject": [{
      "Id": "dom",
      "Attribute": [{
        "AttributeId": "domain",
        "Value": "Sales.Asia Pacific"
      }]
    }],
    "Action": [{
      "Id": "act",
      "Attribute": [{
        "AttributeId": "action",
        "Value": "Retrieve"
      }]
    }],
    "Resource": [{
      "Id": "srv",
      "Attribute": [{
        "AttributeId": "service",
        "Value": "Mobile.Landing page"
      }]
    }],
    "Environment": [{
      "Id": "idp",
      "Attribute": [{
        "AttributeId": "symphonic-idp",
        "Value": "Social networks.Spacebook"
      }]
    }],
    "Category": [{
      "Id": "att",
      "Attribute": [{
        "AttributeId": "attribute:Prospect name",
        "Value": "B. Vo"
      }]
    }]
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
curl --location --globoff '{{apiPath}}/pdp' \
--header 'Accept: application/xacml+json' \
--header 'Content-Type: application/xacml+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "Request": {
    "MultiRequests": {
      "RequestReference": [{
        "ReferenceId": [
          "dom",
          "act",
          "srv",
          "idp",
          "att"
        ]
      }]
    },
    "AccessSubject": [{
      "Id": "dom",
      "Attribute": [{
        "AttributeId": "domain",
        "Value": "Sales.Asia Pacific"
      }]
    }],
    "Action": [{
      "Id": "act",
      "Attribute": [{
        "AttributeId": "action",
        "Value": "Retrieve"
      }]
    }],
    "Resource": [{
      "Id": "srv",
      "Attribute": [{
        "AttributeId": "service",
        "Value": "Mobile.Landing page"
      }]
    }],
    "Environment": [{
      "Id": "idp",
      "Attribute": [{
        "AttributeId": "symphonic-idp",
        "Value": "Social networks.Spacebook"
      }]
    }],
    "Category": [{
      "Id": "att",
      "Attribute": [{
        "AttributeId": "attribute:Prospect name",
        "Value": "B. Vo"
      }]
    }]
  }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/pdp")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Accept", "application/xacml+json");
request.AddHeader("Content-Type", "application/xacml+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""Request"": {" + "\n" +
@"    ""MultiRequests"": {" + "\n" +
@"      ""RequestReference"": [{" + "\n" +
@"        ""ReferenceId"": [" + "\n" +
@"          ""dom""," + "\n" +
@"          ""act""," + "\n" +
@"          ""srv""," + "\n" +
@"          ""idp""," + "\n" +
@"          ""att""" + "\n" +
@"        ]" + "\n" +
@"      }]" + "\n" +
@"    }," + "\n" +
@"    ""AccessSubject"": [{" + "\n" +
@"      ""Id"": ""dom""," + "\n" +
@"      ""Attribute"": [{" + "\n" +
@"        ""AttributeId"": ""domain""," + "\n" +
@"        ""Value"": ""Sales.Asia Pacific""" + "\n" +
@"      }]" + "\n" +
@"    }]," + "\n" +
@"    ""Action"": [{" + "\n" +
@"      ""Id"": ""act""," + "\n" +
@"      ""Attribute"": [{" + "\n" +
@"        ""AttributeId"": ""action""," + "\n" +
@"        ""Value"": ""Retrieve""" + "\n" +
@"      }]" + "\n" +
@"    }]," + "\n" +
@"    ""Resource"": [{" + "\n" +
@"      ""Id"": ""srv""," + "\n" +
@"      ""Attribute"": [{" + "\n" +
@"        ""AttributeId"": ""service""," + "\n" +
@"        ""Value"": ""Mobile.Landing page""" + "\n" +
@"      }]" + "\n" +
@"    }]," + "\n" +
@"    ""Environment"": [{" + "\n" +
@"      ""Id"": ""idp""," + "\n" +
@"      ""Attribute"": [{" + "\n" +
@"        ""AttributeId"": ""symphonic-idp""," + "\n" +
@"        ""Value"": ""Social networks.Spacebook""" + "\n" +
@"      }]" + "\n" +
@"    }]," + "\n" +
@"    ""Category"": [{" + "\n" +
@"      ""Id"": ""att""," + "\n" +
@"      ""Attribute"": [{" + "\n" +
@"        ""AttributeId"": ""attribute:Prospect name""," + "\n" +
@"        ""Value"": ""B. Vo""" + "\n" +
@"      }]" + "\n" +
@"    }]" + "\n" +
@"  }" + "\n" +
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

  url := "{{apiPath}}/pdp"
  method := "POST"

  payload := strings.NewReader(`{
  "Request": {
    "MultiRequests": {
      "RequestReference": [{
        "ReferenceId": [
          "dom",
          "act",
          "srv",
          "idp",
          "att"
        ]
      }]
    },
    "AccessSubject": [{
      "Id": "dom",
      "Attribute": [{
        "AttributeId": "domain",
        "Value": "Sales.Asia Pacific"
      }]
    }],
    "Action": [{
      "Id": "act",
      "Attribute": [{
        "AttributeId": "action",
        "Value": "Retrieve"
      }]
    }],
    "Resource": [{
      "Id": "srv",
      "Attribute": [{
        "AttributeId": "service",
        "Value": "Mobile.Landing page"
      }]
    }],
    "Environment": [{
      "Id": "idp",
      "Attribute": [{
        "AttributeId": "symphonic-idp",
        "Value": "Social networks.Spacebook"
      }]
    }],
    "Category": [{
      "Id": "att",
      "Attribute": [{
        "AttributeId": "attribute:Prospect name",
        "Value": "B. Vo"
      }]
    }]
  }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Accept", "application/xacml+json")
  req.Header.Add("Content-Type", "application/xacml+json")
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
POST /pdp HTTP/1.1
Host: {{apiPath}}
Accept: application/xacml+json
Content-Type: application/xacml+json
Authorization: Bearer {{accessToken}}

{
  "Request": {
    "MultiRequests": {
      "RequestReference": [{
        "ReferenceId": [
          "dom",
          "act",
          "srv",
          "idp",
          "att"
        ]
      }]
    },
    "AccessSubject": [{
      "Id": "dom",
      "Attribute": [{
        "AttributeId": "domain",
        "Value": "Sales.Asia Pacific"
      }]
    }],
    "Action": [{
      "Id": "act",
      "Attribute": [{
        "AttributeId": "action",
        "Value": "Retrieve"
      }]
    }],
    "Resource": [{
      "Id": "srv",
      "Attribute": [{
        "AttributeId": "service",
        "Value": "Mobile.Landing page"
      }]
    }],
    "Environment": [{
      "Id": "idp",
      "Attribute": [{
        "AttributeId": "symphonic-idp",
        "Value": "Social networks.Spacebook"
      }]
    }],
    "Category": [{
      "Id": "att",
      "Attribute": [{
        "AttributeId": "attribute:Prospect name",
        "Value": "B. Vo"
      }]
    }]
  }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/xacml+json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"Request\": {\n    \"MultiRequests\": {\n      \"RequestReference\": [{\n        \"ReferenceId\": [\n          \"dom\",\n          \"act\",\n          \"srv\",\n          \"idp\",\n          \"att\"\n        ]\n      }]\n    },\n    \"AccessSubject\": [{\n      \"Id\": \"dom\",\n      \"Attribute\": [{\n        \"AttributeId\": \"domain\",\n        \"Value\": \"Sales.Asia Pacific\"\n      }]\n    }],\n    \"Action\": [{\n      \"Id\": \"act\",\n      \"Attribute\": [{\n        \"AttributeId\": \"action\",\n        \"Value\": \"Retrieve\"\n      }]\n    }],\n    \"Resource\": [{\n      \"Id\": \"srv\",\n      \"Attribute\": [{\n        \"AttributeId\": \"service\",\n        \"Value\": \"Mobile.Landing page\"\n      }]\n    }],\n    \"Environment\": [{\n      \"Id\": \"idp\",\n      \"Attribute\": [{\n        \"AttributeId\": \"symphonic-idp\",\n        \"Value\": \"Social networks.Spacebook\"\n      }]\n    }],\n    \"Category\": [{\n      \"Id\": \"att\",\n      \"Attribute\": [{\n        \"AttributeId\": \"attribute:Prospect name\",\n        \"Value\": \"B. Vo\"\n      }]\n    }]\n  }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/pdp")
  .method("POST", body)
  .addHeader("Accept", "application/xacml+json")
  .addHeader("Content-Type", "application/xacml+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/pdp",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Accept": "application/xacml+json",
    "Content-Type": "application/xacml+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "Request": {
      "MultiRequests": {
        "RequestReference": [
          {
            "ReferenceId": [
              "dom",
              "act",
              "srv",
              "idp",
              "att"
            ]
          }
        ]
      },
      "AccessSubject": [
        {
          "Id": "dom",
          "Attribute": [
            {
              "AttributeId": "domain",
              "Value": "Sales.Asia Pacific"
            }
          ]
        }
      ],
      "Action": [
        {
          "Id": "act",
          "Attribute": [
            {
              "AttributeId": "action",
              "Value": "Retrieve"
            }
          ]
        }
      ],
      "Resource": [
        {
          "Id": "srv",
          "Attribute": [
            {
              "AttributeId": "service",
              "Value": "Mobile.Landing page"
            }
          ]
        }
      ],
      "Environment": [
        {
          "Id": "idp",
          "Attribute": [
            {
              "AttributeId": "symphonic-idp",
              "Value": "Social networks.Spacebook"
            }
          ]
        }
      ],
      "Category": [
        {
          "Id": "att",
          "Attribute": [
            {
              "AttributeId": "attribute:Prospect name",
              "Value": "B. Vo"
            }
          ]
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
  'url': '{{apiPath}}/pdp',
  'headers': {
    'Accept': 'application/xacml+json',
    'Content-Type': 'application/xacml+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "Request": {
      "MultiRequests": {
        "RequestReference": [
          {
            "ReferenceId": [
              "dom",
              "act",
              "srv",
              "idp",
              "att"
            ]
          }
        ]
      },
      "AccessSubject": [
        {
          "Id": "dom",
          "Attribute": [
            {
              "AttributeId": "domain",
              "Value": "Sales.Asia Pacific"
            }
          ]
        }
      ],
      "Action": [
        {
          "Id": "act",
          "Attribute": [
            {
              "AttributeId": "action",
              "Value": "Retrieve"
            }
          ]
        }
      ],
      "Resource": [
        {
          "Id": "srv",
          "Attribute": [
            {
              "AttributeId": "service",
              "Value": "Mobile.Landing page"
            }
          ]
        }
      ],
      "Environment": [
        {
          "Id": "idp",
          "Attribute": [
            {
              "AttributeId": "symphonic-idp",
              "Value": "Social networks.Spacebook"
            }
          ]
        }
      ],
      "Category": [
        {
          "Id": "att",
          "Attribute": [
            {
              "AttributeId": "attribute:Prospect name",
              "Value": "B. Vo"
            }
          ]
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

url = "{{apiPath}}/pdp"

payload = json.dumps({
  "Request": {
    "MultiRequests": {
      "RequestReference": [
        {
          "ReferenceId": [
            "dom",
            "act",
            "srv",
            "idp",
            "att"
          ]
        }
      ]
    },
    "AccessSubject": [
      {
        "Id": "dom",
        "Attribute": [
          {
            "AttributeId": "domain",
            "Value": "Sales.Asia Pacific"
          }
        ]
      }
    ],
    "Action": [
      {
        "Id": "act",
        "Attribute": [
          {
            "AttributeId": "action",
            "Value": "Retrieve"
          }
        ]
      }
    ],
    "Resource": [
      {
        "Id": "srv",
        "Attribute": [
          {
            "AttributeId": "service",
            "Value": "Mobile.Landing page"
          }
        ]
      }
    ],
    "Environment": [
      {
        "Id": "idp",
        "Attribute": [
          {
            "AttributeId": "symphonic-idp",
            "Value": "Social networks.Spacebook"
          }
        ]
      }
    ],
    "Category": [
      {
        "Id": "att",
        "Attribute": [
          {
            "AttributeId": "attribute:Prospect name",
            "Value": "B. Vo"
          }
        ]
      }
    ]
  }
})
headers = {
  'Accept': 'application/xacml+json',
  'Content-Type': 'application/xacml+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/pdp');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Accept' => 'application/xacml+json',
  'Content-Type' => 'application/xacml+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "Request": {\n    "MultiRequests": {\n      "RequestReference": [{\n        "ReferenceId": [\n          "dom",\n          "act",\n          "srv",\n          "idp",\n          "att"\n        ]\n      }]\n    },\n    "AccessSubject": [{\n      "Id": "dom",\n      "Attribute": [{\n        "AttributeId": "domain",\n        "Value": "Sales.Asia Pacific"\n      }]\n    }],\n    "Action": [{\n      "Id": "act",\n      "Attribute": [{\n        "AttributeId": "action",\n        "Value": "Retrieve"\n      }]\n    }],\n    "Resource": [{\n      "Id": "srv",\n      "Attribute": [{\n        "AttributeId": "service",\n        "Value": "Mobile.Landing page"\n      }]\n    }],\n    "Environment": [{\n      "Id": "idp",\n      "Attribute": [{\n        "AttributeId": "symphonic-idp",\n        "Value": "Social networks.Spacebook"\n      }]\n    }],\n    "Category": [{\n      "Id": "att",\n      "Attribute": [{\n        "AttributeId": "attribute:Prospect name",\n        "Value": "B. Vo"\n      }]\n    }]\n  }\n}');
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

url = URI("{{apiPath}}/pdp")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Accept"] = "application/xacml+json"
request["Content-Type"] = "application/xacml+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "Request": {
    "MultiRequests": {
      "RequestReference": [
        {
          "ReferenceId": [
            "dom",
            "act",
            "srv",
            "idp",
            "att"
          ]
        }
      ]
    },
    "AccessSubject": [
      {
        "Id": "dom",
        "Attribute": [
          {
            "AttributeId": "domain",
            "Value": "Sales.Asia Pacific"
          }
        ]
      }
    ],
    "Action": [
      {
        "Id": "act",
        "Attribute": [
          {
            "AttributeId": "action",
            "Value": "Retrieve"
          }
        ]
      }
    ],
    "Resource": [
      {
        "Id": "srv",
        "Attribute": [
          {
            "AttributeId": "service",
            "Value": "Mobile.Landing page"
          }
        ]
      }
    ],
    "Environment": [
      {
        "Id": "idp",
        "Attribute": [
          {
            "AttributeId": "symphonic-idp",
            "Value": "Social networks.Spacebook"
          }
        ]
      }
    ],
    "Category": [
      {
        "Id": "att",
        "Attribute": [
          {
            "AttributeId": "attribute:Prospect name",
            "Value": "B. Vo"
          }
        ]
      }
    ]
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"Request\": {\n    \"MultiRequests\": {\n      \"RequestReference\": [{\n        \"ReferenceId\": [\n          \"dom\",\n          \"act\",\n          \"srv\",\n          \"idp\",\n          \"att\"\n        ]\n      }]\n    },\n    \"AccessSubject\": [{\n      \"Id\": \"dom\",\n      \"Attribute\": [{\n        \"AttributeId\": \"domain\",\n        \"Value\": \"Sales.Asia Pacific\"\n      }]\n    }],\n    \"Action\": [{\n      \"Id\": \"act\",\n      \"Attribute\": [{\n        \"AttributeId\": \"action\",\n        \"Value\": \"Retrieve\"\n      }]\n    }],\n    \"Resource\": [{\n      \"Id\": \"srv\",\n      \"Attribute\": [{\n        \"AttributeId\": \"service\",\n        \"Value\": \"Mobile.Landing page\"\n      }]\n    }],\n    \"Environment\": [{\n      \"Id\": \"idp\",\n      \"Attribute\": [{\n        \"AttributeId\": \"symphonic-idp\",\n        \"Value\": \"Social networks.Spacebook\"\n      }]\n    }],\n    \"Category\": [{\n      \"Id\": \"att\",\n      \"Attribute\": [{\n        \"AttributeId\": \"attribute:Prospect name\",\n        \"Value\": \"B. Vo\"\n      }]\n    }]\n  }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/pdp")!,timeoutInterval: Double.infinity)
request.addValue("application/xacml+json", forHTTPHeaderField: "Accept")
request.addValue("application/xacml+json", forHTTPHeaderField: "Content-Type")
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
    "Response": [
        {
            "Decision": "Permit",
            "Obligations": [
                {
                    "Id": "obligation-id",
                    "AttributeAssignments": [
                        {
                            "AttributeId": "payload",
                            "Value": "payload-value"
                        }
                    ]
                }
            ],
            "AssociatedAdvice": [
                {
                    "Id": "advice-id",
                    "AttributeAssignments": [
                        {
                            "AttributeId": "payload",
                            "Value": "payload-value"
                        }
                    ]
                }
            ]
        }
    ]
}
```

---

---
title: Batch Requests
description: "Batch requests consist of an array named \"requests\" of JSON objects, each of which is a standard JSON PDP API single decision request."
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-decision/json-pdp/batch-requests
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision/json-pdp/batch-requests.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Batch Requests

Batch requests consist of an array named "`requests`" of JSON objects, each of which is a standard JSON PDP API single decision request.

After the Policy Decision Service determines a decision response, it hands the response back to the JSON PDP API to provide to the client. JSON PDP API responses include decisions, such as `Permit` or `Deny`, and any obligations or advice that matched during policy processing.

The batch decision responses are guaranteed to be returned in the same order as the received responses. For example, the first response in the batch responses corresponds to a decision on the first request in the batch requests.

---

---
title: Branch Manager
description: The branch manager provides operations to create snapshots, as well as read, update, and merge policy branches.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/version-control/branch-manager
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/version-control/branch-manager.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  branch-manager-data-model: Branch manager data model
  resolution-data-model: Resolution data model
  branch-entity-reference: Entity reference
  response-codes: Response codes
---

# Branch Manager

The branch manager provides operations to create snapshots, as well as read, update, and merge policy branches.

Policy branches enable you to manage different sets of Trust Framework definitions and policies by storing these sets in separate branches. This is helpful in development environments, where you might need to quickly reconfigure PingAuthorize between policy branches.

To easily switch between policy branches and test configurations, define [Policy External Servers](https://docs.pingidentity.com/pingauthorize/latest/pingauthorize_server_administration_guide/paz_config_external_pdp.html) for each branch and update the Policy Decision Service's `policy-server` property. Learn more in [Changing the active policy branch](https://docs.pingidentity.com/pingauthorize/latest/pingauthorize_server_administration_guide/paz_change_active_policy_branch.html).

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | Learn about creating a new child branch in [Snapshot Management](snapshot-management/create-child-branch-from-snapshot.html). |

## Branch manager data model

| Property       | Type                                    | Required | Mutable   | Description                                                                    |
| -------------- | --------------------------------------- | -------- | --------- | ------------------------------------------------------------------------------ |
| `name`         | String                                  | Required | Mutable   | Specifies the name of the policy branch.                                       |
| `message`      | String                                  | Required | Immutable | Provides the commit message for creation of a new snapshot.                    |
| `fromBranchId` | String                                  | Required | Immutable | Specifies the branch to merge changes from.                                    |
| `resolutions`  | [Resolution](#resolution-data-model)\[] | Optional | Mutable   | A collection that includes `resolution` objects for resolving merge conflicts. |

## Resolution data model

| Property          | Type                                            | Required | Mutable   | Description                                             |
| ----------------- | ----------------------------------------------- | -------- | --------- | ------------------------------------------------------- |
| `resolutionType`  | String                                          | Required | Immutable | Specifies the action to resolve the conflict.           |
| `entityReference` | [Entity reference](#branch-entity-reference)\[] | Required | Immutable | Provides a collection of entities causing the conflict. |

## Entity reference

| Property | Type   | Required | Mutable   | Description                     |
| -------- | ------ | -------- | --------- | ------------------------------- |
| `id`     | String | N/A      | Read-only | Specifies the ID of the entity. |
| `type`   | String | N/A      | Read-only | Specifies the entity type.      |

## Response codes

| Code | Message                                                                              |
| ---- | ------------------------------------------------------------------------------------ |
| 201  | Changes from the source branch were successfully merged into the destination branch. |
| 204  | Successful operation.                                                                |
| 404  | There is no branch in the system with the given ID.                                  |
| 409  | The merge failed due to conflicting changes in the source and destination branches.  |

---

---
title: Changelog
description: The following changes have been made to the PingAuthorize SCIM API.
component: pingauthorize
page_id: pingauthorize:pingauthorize:scim/changelog
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/scim/changelog.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Changelog

The following changes have been made to the PingAuthorize SCIM API.

| Release Date | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| 6/9/2022     | The PingAuthorize SCIM API Reference migrated from Postman. |

---

---
title: Create A User
description: "The POST /scim/v2/Users endpoint creates a new user resource, providing a complete representation of the resource in the request body. Read-only attributes such as meta can be omitted. If the request is successful, the PingAuthorize Server returns a response with a status code of 201, with the resource's canonical URI as the value of the Location header. For example, +Location: https://example.com:443/scim/v2/Users/5caa81af-ec05-41ff-a709-c7378007a99c."
component: pingauthorize
page_id: pingauthorize:pingauthorize:scim/user-profile/create-a-user
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/scim/user-profile/create-a-user.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create A User

##

```none
POST {{apiPath}}/scim/v2/Users
```

The `POST /scim/v2/Users` endpoint creates a new user resource, providing a complete representation of the resource in the request body. Read-only attributes such as `meta` can be omitted. If the request is successful, the PingAuthorize Server returns a response with a status code of `201`, with the resource's canonical URI as the value of the `Location` header. For example, `+Location: https://example.com:443/scim/v2/Users/5caa81af-ec05-41ff-a709-c7378007a99c`.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/scim+json

Content-Length      488

### Body

raw ( application/scim+json )

```json
{
    "emails": [
        {
            "primary": true,
            "type": "work",
            "value": "pat.conley@runciter.com"
        }
    ],
    "name": {
        "familyName": "Conley",
        "formatted": "Pat Conley",
        "givenName": "Pat"
    },
    "password": {{$randomPassword}},
    "schemas": [
        "urn:pingidentity:schemas:User:1.0",
        "urn:pingidentity:schemas:sample:profile:1.0"
    ],
    "urn:pingidentity:schemas:sample:profile:1.0": {
        "birthDate": "1948-07-13"
    },
    "userName": "pconley"
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
curl --location --globoff '{{apiPath}}/scim/v2/Users' \
--header 'Content-Type: application/scim+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data-raw '{
    "emails": [
        {
            "primary": true,
            "type": "work",
            "value": "pat.conley@runciter.com"
        }
    ],
    "name": {
        "familyName": "Conley",
        "formatted": "Pat Conley",
        "givenName": "Pat"
    },
    "password": {{$randomPassword}},
    "schemas": [
        "urn:pingidentity:schemas:User:1.0",
        "urn:pingidentity:schemas:sample:profile:1.0"
    ],
    "urn:pingidentity:schemas:sample:profile:1.0": {
        "birthDate": "1948-07-13"
    },
    "userName": "pconley"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/Users")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/scim+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""emails"": [" + "\n" +
@"        {" + "\n" +
@"            ""primary"": true," + "\n" +
@"            ""type"": ""work""," + "\n" +
@"            ""value"": ""pat.conley@runciter.com""" + "\n" +
@"        }" + "\n" +
@"    ]," + "\n" +
@"    ""name"": {" + "\n" +
@"        ""familyName"": ""Conley""," + "\n" +
@"        ""formatted"": ""Pat Conley""," + "\n" +
@"        ""givenName"": ""Pat""" + "\n" +
@"    }," + "\n" +
@"    ""password"": {{$randomPassword}}," + "\n" +
@"    ""schemas"": [" + "\n" +
@"        ""urn:pingidentity:schemas:User:1.0""," + "\n" +
@"        ""urn:pingidentity:schemas:sample:profile:1.0""" + "\n" +
@"    ]," + "\n" +
@"    ""urn:pingidentity:schemas:sample:profile:1.0"": {" + "\n" +
@"        ""birthDate"": ""1948-07-13""" + "\n" +
@"    }," + "\n" +
@"    ""userName"": ""pconley""" + "\n" +
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

  url := "{{apiPath}}/scim/v2/Users"
  method := "POST"

  payload := strings.NewReader(`{
    "emails": [
        {
            "primary": true,
            "type": "work",
            "value": "pat.conley@runciter.com"
        }
    ],
    "name": {
        "familyName": "Conley",
        "formatted": "Pat Conley",
        "givenName": "Pat"
    },
    "password": {{$randomPassword}},
    "schemas": [
        "urn:pingidentity:schemas:User:1.0",
        "urn:pingidentity:schemas:sample:profile:1.0"
    ],
    "urn:pingidentity:schemas:sample:profile:1.0": {
        "birthDate": "1948-07-13"
    },
    "userName": "pconley"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/scim+json")
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
POST /scim/v2/Users HTTP/1.1
Host: {{apiPath}}
Content-Type: application/scim+json
Authorization: Bearer {{accessToken}}

{
    "emails": [
        {
            "primary": true,
            "type": "work",
            "value": "pat.conley@runciter.com"
        }
    ],
    "name": {
        "familyName": "Conley",
        "formatted": "Pat Conley",
        "givenName": "Pat"
    },
    "password": {{$randomPassword}},
    "schemas": [
        "urn:pingidentity:schemas:User:1.0",
        "urn:pingidentity:schemas:sample:profile:1.0"
    ],
    "urn:pingidentity:schemas:sample:profile:1.0": {
        "birthDate": "1948-07-13"
    },
    "userName": "pconley"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/scim+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"emails\": [\n        {\n            \"primary\": true,\n            \"type\": \"work\",\n            \"value\": \"pat.conley@runciter.com\"\n        }\n    ],\n    \"name\": {\n        \"familyName\": \"Conley\",\n        \"formatted\": \"Pat Conley\",\n        \"givenName\": \"Pat\"\n    },\n    \"password\": {{$randomPassword}},\n    \"schemas\": [\n        \"urn:pingidentity:schemas:User:1.0\",\n        \"urn:pingidentity:schemas:sample:profile:1.0\"\n    ],\n    \"urn:pingidentity:schemas:sample:profile:1.0\": {\n        \"birthDate\": \"1948-07-13\"\n    },\n    \"userName\": \"pconley\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/Users")
  .method("POST", body)
  .addHeader("Content-Type", "application/scim+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/Users",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/scim+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": "{\n    \"emails\": [\n        {\n            \"primary\": true,\n            \"type\": \"work\",\n            \"value\": \"pat.conley@runciter.com\"\n        }\n    ],\n    \"name\": {\n        \"familyName\": \"Conley\",\n        \"formatted\": \"Pat Conley\",\n        \"givenName\": \"Pat\"\n    },\n    \"password\": {{$randomPassword}},\n    \"schemas\": [\n        \"urn:pingidentity:schemas:User:1.0\",\n        \"urn:pingidentity:schemas:sample:profile:1.0\"\n    ],\n    \"urn:pingidentity:schemas:sample:profile:1.0\": {\n        \"birthDate\": \"1948-07-13\"\n    },\n    \"userName\": \"pconley\"\n}",
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/scim/v2/Users',
  'headers': {
    'Content-Type': 'application/scim+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: '{\n    "emails": [\n        {\n            "primary": true,\n            "type": "work",\n            "value": "pat.conley@runciter.com"\n        }\n    ],\n    "name": {\n        "familyName": "Conley",\n        "formatted": "Pat Conley",\n        "givenName": "Pat"\n    },\n    "password": {{$randomPassword}},\n    "schemas": [\n        "urn:pingidentity:schemas:User:1.0",\n        "urn:pingidentity:schemas:sample:profile:1.0"\n    ],\n    "urn:pingidentity:schemas:sample:profile:1.0": {\n        "birthDate": "1948-07-13"\n    },\n    "userName": "pconley"\n}'

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/scim/v2/Users"

payload = "{\n    \"emails\": [\n        {\n            \"primary\": true,\n            \"type\": \"work\",\n            \"value\": \"pat.conley@runciter.com\"\n        }\n    ],\n    \"name\": {\n        \"familyName\": \"Conley\",\n        \"formatted\": \"Pat Conley\",\n        \"givenName\": \"Pat\"\n    },\n    \"password\": {{$randomPassword}},\n    \"schemas\": [\n        \"urn:pingidentity:schemas:User:1.0\",\n        \"urn:pingidentity:schemas:sample:profile:1.0\"\n    ],\n    \"urn:pingidentity:schemas:sample:profile:1.0\": {\n        \"birthDate\": \"1948-07-13\"\n    },\n    \"userName\": \"pconley\"\n}"
headers = {
  'Content-Type': 'application/scim+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/scim/v2/Users');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/scim+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "emails": [\n        {\n            "primary": true,\n            "type": "work",\n            "value": "pat.conley@runciter.com"\n        }\n    ],\n    "name": {\n        "familyName": "Conley",\n        "formatted": "Pat Conley",\n        "givenName": "Pat"\n    },\n    "password": {{$randomPassword}},\n    "schemas": [\n        "urn:pingidentity:schemas:User:1.0",\n        "urn:pingidentity:schemas:sample:profile:1.0"\n    ],\n    "urn:pingidentity:schemas:sample:profile:1.0": {\n        "birthDate": "1948-07-13"\n    },\n    "userName": "pconley"\n}');
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

url = URI("{{apiPath}}/scim/v2/Users")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/scim+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = "{\n    \"emails\": [\n        {\n            \"primary\": true,\n            \"type\": \"work\",\n            \"value\": \"pat.conley@runciter.com\"\n        }\n    ],\n    \"name\": {\n        \"familyName\": \"Conley\",\n        \"formatted\": \"Pat Conley\",\n        \"givenName\": \"Pat\"\n    },\n    \"password\": {{\\$randomPassword}},\n    \"schemas\": [\n        \"urn:pingidentity:schemas:User:1.0\",\n        \"urn:pingidentity:schemas:sample:profile:1.0\"\n    ],\n    \"urn:pingidentity:schemas:sample:profile:1.0\": {\n        \"birthDate\": \"1948-07-13\"\n    },\n    \"userName\": \"pconley\"\n}"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"emails\": [\n        {\n            \"primary\": true,\n            \"type\": \"work\",\n            \"value\": \"pat.conley@runciter.com\"\n        }\n    ],\n    \"name\": {\n        \"familyName\": \"Conley\",\n        \"formatted\": \"Pat Conley\",\n        \"givenName\": \"Pat\"\n    },\n    \"password\": {{$randomPassword}},\n    \"schemas\": [\n        \"urn:pingidentity:schemas:User:1.0\",\n        \"urn:pingidentity:schemas:sample:profile:1.0\"\n    ],\n    \"urn:pingidentity:schemas:sample:profile:1.0\": {\n        \"birthDate\": \"1948-07-13\"\n    },\n    \"userName\": \"pconley\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/Users")!,timeoutInterval: Double.infinity)
request.addValue("application/scim+json", forHTTPHeaderField: "Content-Type")
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
    "emails": [
        {
            "primary": true,
            "type": "work",
            "value": "pat.conley@runciter.com"
        }
    ],
    "id": "76b4c133-87a7-4b2f-8058-4716e78b0fd4",
    "meta": {
        "created": "2016-07-30T00:01:23.824Z",
        "lastModified": "2016-07-30T00:01:23.824Z",
        "location": "https://example.com:443/scim/v2/Users/76b4c133-87a7-4b2f-8058-4716e78b0fd4",
        "resourceType": "Users"
    },
    "name": {
        "familyName": "Conley",
        "formatted": "Pat Conley",
        "givenName": "Pat"
    },
    "schemas": [
        "urn:pingidentity:schemas:sample:profile:1.0",
        "urn:pingidentity:schemas:User:1.0"
    ],
    "urn:pingidentity:schemas:sample:profile:1.0": {
        "birthDate": "1948-07-13"
    },
    "userName": "pconley"
}
```

---

---
title: Create Child Branch From Snapshot
description: The POST /version-control/snapshots/{{snapshotId}}/branch operation creates a new child branch. The child branch is forked from the snapshot specified by the ID in the request URL.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/version-control/snapshot-management/create-child-branch-from-snapshot
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/version-control/snapshot-management/create-child-branch-from-snapshot.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Child Branch From Snapshot

##

```none
POST {{apiPath}}/version-control/snapshots/{{snapshotId}}/branch
```

The `POST /version-control/snapshots/{{snapshotId}}/branch` operation creates a new child branch. The child branch is forked from the snapshot specified by the ID in the request URL.

> **Collapse: Request Model**
>
> For property descriptions, refer to [Snapshot manager data model](../snapshot-management.html#snapshot-manager-data-model)
>
> | Property | Type   | Required |
> | -------- | ------ | -------- |
> | `name`   | String | Required |

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
{
    "name": "example-branch"
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
curl --location --globoff '{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
    "name": "example-branch"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"    ""name"": ""example-branch""" + "\n" +
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

  url := "{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "example-branch"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /version-control/snapshots/{{snapshotId}}/branch HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
    "name": "example-branch"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"example-branch\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "name": "example-branch"
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
  'url': '{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "name": "example-branch"
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

url = "{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch"

payload = json.dumps({
  "name": "example-branch"
})
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n    "name": "example-branch"\n}');
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

url = URI("{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "example-branch"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"example-branch\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/version-control/snapshots/{{snapshotId}}/branch")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "id": "bc61eedf-a9c1-4aae-b35f-7df637c403ed",
    "name": "example-branch",
    "head": "5c400c4e-ac2b-4e08-8f28-d9a25c5f037e",
    "tip": {
        "id": "1057e1ea-7da6-419e-b676-9a9ff2f45d5c",
        "parentId": "5c400c4e-ac2b-4e08-8f28-d9a25c5f037e",
        "state": "UNCOMMITTED",
        "commitDetails": {
            "userId": null,
            "dateTime": null,
            "message": null
        },
        "approvals": [],
        "branchId": "bc61eedf-a9c1-4aae-b35f-7df637c403ed"
    },
    "parentId": "9df2835b-cbbb-4ef9-a20e-ab63c0b6da67"
}
```

---

---
title: Create Child Test Suite Entity
description: The POST /test-suite/{{testSuiteEntryId}} operation creates a new child test suite entity. The allowable values for {{testSuiteType}} are TEST_SCENARIO, TEST_CASE, or ASSERTION. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the test suite entity should be created.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/test-suite/create-child-test-suite-entry
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/test-suite/create-child-test-suite-entry.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Child Test Suite Entity

##

```none
POST {{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}
```

The `POST /test-suite/{{testSuiteEntryId}}` operation creates a new child test suite entity. The allowable values for `{{testSuiteType}}` are `TEST_SCENARIO`, `TEST_CASE`, or `ASSERTION`. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the test suite entity should be created.

### Prerequisites

* [Create a branch](../version-control/snapshot-management/create-child-branch-from-snapshot.html) to get a branch ID.

* [Create a snapshot](../version-control/branch-manager/create-snapshot.html) to get a snapshot ID.

> **Collapse: Query parameters**
>
> | Query parameter | Description       |
> | --------------- | ----------------- |
> | `branch`        | Branch ID or name |
> | `snapshot`      | Snapshot ID       |

> **Collapse: Request Model**
>
> For property descriptions, refer to [Test suite data model](../test-suite.html#test-suite-data-model)
>
> \=== Test scenario request model
>
> | Property                                  | Type    | Required |
> | ----------------------------------------- | ------- | -------- |
> | `name`                                    | String  | Required |
> | `description`                             | String  | Optional |
> | `objectType`                              | String  | Required |
> | `parentId`                                | UUID    | Optional |
> | `permissions.rolePermissions`             | JSON\[] | Optional |
> | `permissions.inherit`                     | Boolean | Optional |
> | `testScenario.request.domainId`           | String  | Optional |
> | `testScenario.request.serviceId`          | String  | Optional |
> | `testScenario.request.identityProviderId` | String  | Optional |
> | `testScenario.request.actionId`           | String  | Optional |
> | `testScenario.attributeOverrides`         | JSON    | Optional |
> | `testScenario.serviceOverrides`           | JSON    | Optional |
>
> To create an test scenario group rather than an individual test scenario, set the `testScenario` property to `null`.
>
> \=== Test case request model
>
> | Property                                           | Type                                                                       | Required |
> | -------------------------------------------------- | -------------------------------------------------------------------------- | -------- |
> | `name`                                             | String                                                                     | Required |
> | `description`                                      | String                                                                     | Optional |
> | `objectType`                                       | String                                                                     | Required |
> | `parentId`                                         | UUID                                                                       | Optional |
> | `permissions.rolePermissions`                      | JSON\[]                                                                    | Optional |
> | `permissions.inherit`                              | Boolean                                                                    | Optional |
> | `testCase.testedEntities`                          | [Test entity](../policy-manager/test-cases.html#test-entity-data-model)\[] | Required |
> | `testCase.testedEntities.assertions`               | [Assertion](../policy-manager/test-cases.html#assertion-data-model)\[]     | Optional |
> | `testCase.testScenarioDefinitionId`                | String                                                                     | Optional |
> | `testCase.testScenario.request.domainId`           | String                                                                     | Optional |
> | `testCase.testScenario.request.serviceId`          | String                                                                     | Optional |
> | `testCase.testScenario.request.identityProviderId` | String                                                                     | Optional |
> | `testCase.testScenario.request.actionId`           | String                                                                     | Optional |
> | `testCase.testScenario.attributeOverrides`         | JSON                                                                       | Optional |
> | `testCase.testScenario.serviceOverrides`           | JSON                                                                       | Optional |
>
> To create an test case group rather than an individual test case, set the `testCase` property to `null`.
>
> \=== Assertion data model
>
> | Property                          | Type    | Required |
> | --------------------------------- | ------- | -------- |
> | `name`                            | String  | Required |
> | `description`                     | String  | Optional |
> | `parentId`                        | UUID    | Optional |
> | `objectType`                      | String  | Optional |
> | `permissions.rolePermissions`     | JSON\[] | Optional |
> | `permissions.inherit`             | Boolean | Optional |
> | `assertion.accessor`              | String  | Required |
> | `assertion.comparator`            | String  | Optional |
> | `assertion.expectation.valueType` | String  | Required |
> | `assertion.expectation.value`     | String  | Required |
>
> To create an assertion group rather than an individual assertion, set the `assertion` property to `null`.

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
{
    "name": "child-test-scenario",
    "description": "",
    "objectType": "TestScenarioDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "testScenario": {
        "request": {
            "actionId": {{actionId}},
            "serviceId": {{serviceId}}
        },
        "attributeOverrides": {},
        "serviceOverrides": {}
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
curl --location --globoff '{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
    "name": "child-test-scenario",
    "description": "",
    "objectType": "TestScenarioDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "testScenario": {
        "request": {
            "actionId": {{actionId}},
            "serviceId": {{serviceId}}
        },
        "attributeOverrides": {},
        "serviceOverrides": {}
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"    ""name"": ""child-test-scenario""," + "\n" +
@"    ""description"": """"," + "\n" +
@"    ""objectType"": ""TestScenarioDefinition""," + "\n" +
@"    ""permissions"": {" + "\n" +
@"        ""inherit"": true," + "\n" +
@"        ""rolePermissions"": []" + "\n" +
@"    }," + "\n" +
@"    ""testScenario"": {" + "\n" +
@"        ""request"": {" + "\n" +
@"            ""actionId"": {{actionId}}," + "\n" +
@"            ""serviceId"": {{serviceId}}" + "\n" +
@"        }," + "\n" +
@"        ""attributeOverrides"": {}," + "\n" +
@"        ""serviceOverrides"": {}" + "\n" +
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

  url := "{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "child-test-scenario",
    "description": "",
    "objectType": "TestScenarioDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "testScenario": {
        "request": {
            "actionId": {{actionId}},
            "serviceId": {{serviceId}}
        },
        "attributeOverrides": {},
        "serviceOverrides": {}
    }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /test-suite/{{testSuiteEntityId}}?branch={{branchId}} HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
    "name": "child-test-scenario",
    "description": "",
    "objectType": "TestScenarioDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "testScenario": {
        "request": {
            "actionId": {{actionId}},
            "serviceId": {{serviceId}}
        },
        "attributeOverrides": {},
        "serviceOverrides": {}
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"child-test-scenario\",\n    \"description\": \"\",\n    \"objectType\": \"TestScenarioDefinition\",\n    \"permissions\": {\n        \"inherit\": true,\n        \"rolePermissions\": []\n    },\n    \"testScenario\": {\n        \"request\": {\n            \"actionId\": {{actionId}},\n            \"serviceId\": {{serviceId}}\n        },\n        \"attributeOverrides\": {},\n        \"serviceOverrides\": {}\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": "{\n    \"name\": \"child-test-scenario\",\n    \"description\": \"\",\n    \"objectType\": \"TestScenarioDefinition\",\n    \"permissions\": {\n        \"inherit\": true,\n        \"rolePermissions\": []\n    },\n    \"testScenario\": {\n        \"request\": {\n            \"actionId\": {{actionId}},\n            \"serviceId\": {{serviceId}}\n        },\n        \"attributeOverrides\": {},\n        \"serviceOverrides\": {}\n    }\n}",
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: '{\n    "name": "child-test-scenario",\n    "description": "",\n    "objectType": "TestScenarioDefinition",\n    "permissions": {\n        "inherit": true,\n        "rolePermissions": []\n    },\n    "testScenario": {\n        "request": {\n            "actionId": {{actionId}},\n            "serviceId": {{serviceId}}\n        },\n        "attributeOverrides": {},\n        "serviceOverrides": {}\n    }\n}'

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}"

payload = "{\n    \"name\": \"child-test-scenario\",\n    \"description\": \"\",\n    \"objectType\": \"TestScenarioDefinition\",\n    \"permissions\": {\n        \"inherit\": true,\n        \"rolePermissions\": []\n    },\n    \"testScenario\": {\n        \"request\": {\n            \"actionId\": {{actionId}},\n            \"serviceId\": {{serviceId}}\n        },\n        \"attributeOverrides\": {},\n        \"serviceOverrides\": {}\n    }\n}"
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n    "name": "child-test-scenario",\n    "description": "",\n    "objectType": "TestScenarioDefinition",\n    "permissions": {\n        "inherit": true,\n        "rolePermissions": []\n    },\n    "testScenario": {\n        "request": {\n            "actionId": {{actionId}},\n            "serviceId": {{serviceId}}\n        },\n        "attributeOverrides": {},\n        "serviceOverrides": {}\n    }\n}');
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

url = URI("{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = "{\n    \"name\": \"child-test-scenario\",\n    \"description\": \"\",\n    \"objectType\": \"TestScenarioDefinition\",\n    \"permissions\": {\n        \"inherit\": true,\n        \"rolePermissions\": []\n    },\n    \"testScenario\": {\n        \"request\": {\n            \"actionId\": {{actionId}},\n            \"serviceId\": {{serviceId}}\n        },\n        \"attributeOverrides\": {},\n        \"serviceOverrides\": {}\n    }\n}"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"child-test-scenario\",\n    \"description\": \"\",\n    \"objectType\": \"TestScenarioDefinition\",\n    \"permissions\": {\n        \"inherit\": true,\n        \"rolePermissions\": []\n    },\n    \"testScenario\": {\n        \"request\": {\n            \"actionId\": {{actionId}},\n            \"serviceId\": {{serviceId}}\n        },\n        \"attributeOverrides\": {},\n        \"serviceOverrides\": {}\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/test-suite/{{testSuiteEntityId}}?branch={{branchId}}")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "objectType": "TestScenarioDefinition",
    "id": "71419680-6f72-4781-9595-8ee83c0e5835",
    "version": "932877d9-0000-48a1-a489-e7a6d32a967e",
    "type": "TEST_SCENARIO",
    "name": "child-test-scenario",
    "fullName": "new group.child-test-scenario",
    "description": "",
    "parentId": "3e0e2026-78bc-49ec-8537-ccf4bbedc935",
    "numberOfChildren": 0,
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "testScenario": {
        "request": {
            "domainId": null,
            "serviceId": "25769e5c-5b33-4daf-9780-3e09b6f32207",
            "identityProviderId": null,
            "actionId": "b072d76e-0085-4423-99c2-4e16b74e88fa",
            "attributes": {}
        },
        "attributeOverrides": {},
        "serviceOverrides": {}
    },
    "properties": []
}
```

---

---
title: Create Deployment Package
description: The POST /deployment-packages operation creates a new deployment package instance.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/deployment-package/create-deployment-package
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/deployment-package/create-deployment-package.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Deployment Package

##

```none
POST {{apiPath}}/deployment-packages
```

The `POST /deployment-packages` operation creates a new deployment package instance.

> **Collapse: Request Model**
>
> For property descriptions, refer to the [Authorization deployment package data model](../deployment-package.html#authorization-deployment-package-data-model).
>
> | Property         | Type   | Required |
> | ---------------- | ------ | -------- |
> | `name`           | String | Required |
> | `snapshotId`     | String | Required |
> | `decisionNodeId` | String | Required |

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
{
    "name": "new deployment package",
    "snapshotId": {{snapshotId}},
    "decisionNodeId": {{decisionNodeId}}
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
curl --location --globoff '{{apiPath}}/deployment-packages' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
    "name": "new deployment package",
    "snapshotId": {{snapshotId}},
    "decisionNodeId": {{decisionNodeId}}
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/deployment-packages")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"    ""name"": ""new deployment package""," + "\n" +
@"    ""snapshotId"": {{snapshotId}}," + "\n" +
@"    ""decisionNodeId"": {{decisionNodeId}}" + "\n" +
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

  url := "{{apiPath}}/deployment-packages"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "new deployment package",
    "snapshotId": {{snapshotId}},
    "decisionNodeId": {{decisionNodeId}}
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /deployment-packages HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
    "name": "new deployment package",
    "snapshotId": {{snapshotId}},
    "decisionNodeId": {{decisionNodeId}}
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"new deployment package\",\n    \"snapshotId\": {{snapshotId}},\n    \"decisionNodeId\": {{decisionNodeId}}\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/deployment-packages")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/deployment-packages",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": "{\n    \"name\": \"new deployment package\",\n    \"snapshotId\": {{snapshotId}},\n    \"decisionNodeId\": {{decisionNodeId}}\n}",
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{apiPath}}/deployment-packages',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: '{\n    "name": "new deployment package",\n    "snapshotId": {{snapshotId}},\n    "decisionNodeId": {{decisionNodeId}}\n}'

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{apiPath}}/deployment-packages"

payload = "{\n    \"name\": \"new deployment package\",\n    \"snapshotId\": {{snapshotId}},\n    \"decisionNodeId\": {{decisionNodeId}}\n}"
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/deployment-packages');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n    "name": "new deployment package",\n    "snapshotId": {{snapshotId}},\n    "decisionNodeId": {{decisionNodeId}}\n}');
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

url = URI("{{apiPath}}/deployment-packages")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = "{\n    \"name\": \"new deployment package\",\n    \"snapshotId\": {{snapshotId}},\n    \"decisionNodeId\": {{decisionNodeId}}\n}"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"new deployment package\",\n    \"snapshotId\": {{snapshotId}},\n    \"decisionNodeId\": {{decisionNodeId}}\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/deployment-packages")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "id": "2a8d0f02-d449-4190-853f-98c76500a5ef",
    "name": "deployment package",
    "dateCreated": "2025-01-30T22:01:10.457241Z",
    "createdBy": "admin",
    "snapshotId": "2faaa442-b7c0-4bd4-94d2-04ecd15d5aca",
    "snapshotMessage": "first commit",
    "snapshotDateCommitted": "2025-01-30T19:37:05.558192Z",
    "decisionNodeId": "e51688ff-1dc9-4b6c-bb36-8af64d02e9d1",
    "decisionNodeName": "Global Decision Point"
}
```

---

---
title: Create Deployment Package Approval
description: The POST /deployment-packages/{{deploymentPackageId}}/approval operation creates an application package approval.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/deployment-package/create-deployment-package-approval
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/deployment-package/create-deployment-package-approval.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Create Deployment Package Approval

##

```none
POST {{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval
```

The `POST /deployment-packages/{{deploymentPackageId}}/approval` operation creates an application package approval.

### Headers

x-user-id      {{userId}}

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
curl --location --globoff --request POST '{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval' \
--header 'x-user-id: {{userId}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
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

  url := "{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")

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
POST /deployment-packages/{{deploymentPackageId}}/approval HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}"
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
  'url': '{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval',
  'headers': {
    'x-user-id': '{{userId}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval"

payload = {}
headers = {
  'x-user-id': '{{userId}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}'
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

url = URI("{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/deployment-packages/{{deploymentPackageId}}/approval")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")

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

204 No Content

```json
```

---

---
title: Create Policy
description: The POST /v2/policy-manager/policies operation creates a new policy. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the policy should be added.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/policy-manager/policies/create-policy
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/policy-manager/policies/create-policy.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Policy

##

```none
POST {{apiPath}}/v2/policy-manager/policies?branch={{branchId}}
```

The `POST /v2/policy-manager/policies` operation creates a new policy. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the policy should be added.

### Prerequisites

* [Create a branch](../../version-control/snapshot-management/create-child-branch-from-snapshot.html) to get a branch ID.

* [Create a snapshot](../../version-control/branch-manager/create-snapshot.html) to get a snapshot ID.

> **Collapse: Query parameters**
>
> | Query parameter | Description       |
> | --------------- | ----------------- |
> | `branch`        | Branch ID or name |
> | `snapshot`      | Snapshot ID       |

> **Collapse: Request Model**
>
> For property descriptions, refer to [Authorization policy data model](../policies.html#authorization-policy-data-model).
>
> | Property             | Type                                      | Required |
> | -------------------- | ----------------------------------------- | -------- |
> | `version`            | String                                    | Optional |
> | `name`               | String                                    | Required |
> | `description`        | String                                    | Required |
> | `shared`             | Boolean                                   | Optional |
> | `disabled`           | Boolean                                   | Optional |
> | `combiningAlgorithm` | CombiningAlgorithm                        | Required |
> | `children`           | Collection of RuleNodeRepresentation      | Optional |
> | `repetitionSettings` | RepetitionSettings                        | Required |
> | `condition`          | Condition object                          | Required |
> | `statements`         | Collection of StatementNodeRepresentation | Optional |
> | `targets`            | Collection of TargetNodeRepresentation    | Optional |

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
{
  "type": "Policy",
  "name": "Test Token Authorization",
  "description": "Token authorization policy.",
  "shared": false,
  "disabled": false,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
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
curl --location --globoff '{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
  "type": "Policy",
  "name": "Test Token Authorization",
  "description": "Token authorization policy.",
  "shared": false,
  "disabled": false,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
  }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"  ""type"": ""Policy""," + "\n" +
@"  ""name"": ""Test Token Authorization""," + "\n" +
@"  ""description"": ""Token authorization policy.""," + "\n" +
@"  ""shared"": false," + "\n" +
@"  ""disabled"": false," + "\n" +
@"  ""combiningAlgorithm"": {" + "\n" +
@"    ""algorithm"": ""DenyOverrides""" + "\n" +
@"  }" + "\n" +
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

  url := "{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}"
  method := "POST"

  payload := strings.NewReader(`{
  "type": "Policy",
  "name": "Test Token Authorization",
  "description": "Token authorization policy.",
  "shared": false,
  "disabled": false,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
  }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /v2/policy-manager/policies?branch={{branchId}} HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
  "type": "Policy",
  "name": "Test Token Authorization",
  "description": "Token authorization policy.",
  "shared": false,
  "disabled": false,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
  }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"type\": \"Policy\",\n  \"name\": \"Test Token Authorization\",\n  \"description\": \"Token authorization policy.\",\n  \"shared\": false,\n  \"disabled\": false,\n  \"combiningAlgorithm\": {\n    \"algorithm\": \"DenyOverrides\"\n  }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "type": "Policy",
    "name": "Test Token Authorization",
    "description": "Token authorization policy.",
    "shared": false,
    "disabled": false,
    "combiningAlgorithm": {
      "algorithm": "DenyOverrides"
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
  'url': '{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "type": "Policy",
    "name": "Test Token Authorization",
    "description": "Token authorization policy.",
    "shared": false,
    "disabled": false,
    "combiningAlgorithm": {
      "algorithm": "DenyOverrides"
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

url = "{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}"

payload = json.dumps({
  "type": "Policy",
  "name": "Test Token Authorization",
  "description": "Token authorization policy.",
  "shared": False,
  "disabled": False,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
  }
})
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n  "type": "Policy",\n  "name": "Test Token Authorization",\n  "description": "Token authorization policy.",\n  "shared": false,\n  "disabled": false,\n  "combiningAlgorithm": {\n    "algorithm": "DenyOverrides"\n  }\n}');
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

url = URI("{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "type": "Policy",
  "name": "Test Token Authorization",
  "description": "Token authorization policy.",
  "shared": false,
  "disabled": false,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"type\": \"Policy\",\n  \"name\": \"Test Token Authorization\",\n  \"description\": \"Token authorization policy.\",\n  \"shared\": false,\n  \"disabled\": false,\n  \"combiningAlgorithm\": {\n    \"algorithm\": \"DenyOverrides\"\n  }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v2/policy-manager/policies?branch={{branchId}}")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "id": "ddd13d3f-7a52-4c6c-8d36-d4dad6c8616f",
    "version": "a704ed93-f121-4fc1-adec-149cf9ee1b53",
    "type": "Policy",
    "name": "Test Token Authorization",
    "description": "Token authorization policy.",
    "shared": false,
    "disabled": false,
    "combiningAlgorithm": {
        "algorithm": "DenyOverrides",
        "evaluateAll": false
    },
    "children": [],
    "repetitionSettings": null,
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "targets": [],
    "statements": [],
    "properties": [],
    "condition": null
}
```

---

---
title: Create PolicySet
description: The POST /v2/policy-manager/policysets operation creates a new policy set. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the policy set should be added.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/policy-manager/policysets/create-policyset
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/policy-manager/policysets/create-policyset.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create PolicySet

##

```none
POST {{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}
```

The `POST /v2/policy-manager/policysets` operation creates a new policy set. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the policy set should be added.

### Prerequisites

* [Create a branch](../../version-control/snapshot-management/create-child-branch-from-snapshot.html) to get a branch ID.

* [Create a snapshot](../../version-control/branch-manager/create-snapshot.html) to get a snapshot ID.

> **Collapse: Query parameters**
>
> | Query parameter | Description       |
> | --------------- | ----------------- |
> | `branch`        | Branch ID or name |
> | `snapshot`      | Snapshot ID       |

> **Collapse: Request Model**
>
> For property descriptions, refer to [Authorization policy set data model](../policysets.html#authorization-policy-set-data-model).
>
> | Property             | Type                                      | Required |
> | -------------------- | ----------------------------------------- | -------- |
> | `name`               | String                                    | Required |
> | `description`        | String                                    | Required |
> | `shared`             | Boolean                                   | Optional |
> | `disabled`           | Boolean                                   | Optional |
> | `combiningAlgorithm` | CombiningAlgorithm                        | Required |
> | `children`           | Collection of RuleNodeRepresentation      | Optional |
> | `repetitionSettings` | RepetitionSettings                        | Required |
> | `condition`          | Condition object                          | Required |
> | `statements`         | Collection of StatementNodeRepresentation | Optional |
> | `targets`            | Collection of TargetNodeRepresentation    | Optional |

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
{
            "type": "PolicySet",
            "name": "Test Token Authorization",
            "description": "Token authorization policyset.",
            "shared": false,
            "disabled": false,
            "combiningAlgorithm": {
                "algorithm": "DenyOverrides"
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
curl --location --globoff '{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
            "type": "PolicySet",
            "name": "Test Token Authorization",
            "description": "Token authorization policyset.",
            "shared": false,
            "disabled": false,
            "combiningAlgorithm": {
                "algorithm": "DenyOverrides"
         }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"            ""type"": ""PolicySet""," + "\n" +
@"            ""name"": ""Test Token Authorization""," + "\n" +
@"            ""description"": ""Token authorization policyset.""," + "\n" +
@"            ""shared"": false," + "\n" +
@"            ""disabled"": false," + "\n" +
@"            ""combiningAlgorithm"": {" + "\n" +
@"                ""algorithm"": ""DenyOverrides""" + "\n" +
@"         }" + "\n" +
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

  url := "{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}"
  method := "POST"

  payload := strings.NewReader(`{
            "type": "PolicySet",
            "name": "Test Token Authorization",
            "description": "Token authorization policyset.",
            "shared": false,
            "disabled": false,
            "combiningAlgorithm": {
                "algorithm": "DenyOverrides"
         }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /v2/policy-manager/policysets?branch={{branchId}} HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
            "type": "PolicySet",
            "name": "Test Token Authorization",
            "description": "Token authorization policyset.",
            "shared": false,
            "disabled": false,
            "combiningAlgorithm": {
                "algorithm": "DenyOverrides"
         }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n            \"type\": \"PolicySet\",\n            \"name\": \"Test Token Authorization\",\n            \"description\": \"Token authorization policyset.\",\n            \"shared\": false,\n            \"disabled\": false,\n            \"combiningAlgorithm\": {\n                \"algorithm\": \"DenyOverrides\"\n         }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "type": "PolicySet",
    "name": "Test Token Authorization",
    "description": "Token authorization policyset.",
    "shared": false,
    "disabled": false,
    "combiningAlgorithm": {
      "algorithm": "DenyOverrides"
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
  'url': '{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "type": "PolicySet",
    "name": "Test Token Authorization",
    "description": "Token authorization policyset.",
    "shared": false,
    "disabled": false,
    "combiningAlgorithm": {
      "algorithm": "DenyOverrides"
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

url = "{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}"

payload = json.dumps({
  "type": "PolicySet",
  "name": "Test Token Authorization",
  "description": "Token authorization policyset.",
  "shared": False,
  "disabled": False,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
  }
})
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n            "type": "PolicySet",\n            "name": "Test Token Authorization",\n            "description": "Token authorization policyset.",\n            "shared": false,\n            "disabled": false,\n            "combiningAlgorithm": {\n                "algorithm": "DenyOverrides"\n         }\n}');
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

url = URI("{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "type": "PolicySet",
  "name": "Test Token Authorization",
  "description": "Token authorization policyset.",
  "shared": false,
  "disabled": false,
  "combiningAlgorithm": {
    "algorithm": "DenyOverrides"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n            \"type\": \"PolicySet\",\n            \"name\": \"Test Token Authorization\",\n            \"description\": \"Token authorization policyset.\",\n            \"shared\": false,\n            \"disabled\": false,\n            \"combiningAlgorithm\": {\n                \"algorithm\": \"DenyOverrides\"\n         }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v2/policy-manager/policysets?branch={{branchId}}")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "id": "83505379-49df-4c36-8a08-a532f6fe98bd",
    "version": "58c1ec64-db12-40f2-9d01-0f99cc09a013",
    "type": "PolicySet",
    "name": "Test Token Authorization",
    "description": "Token authorization policyset.",
    "shared": false,
    "disabled": false,
    "combiningAlgorithm": {
        "algorithm": "DenyOverrides"
    },
    "children": [],
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "condition": null,
    "properties": [],
    "targets": [],
    "statements": []
}
```

---

---
title: Create Root Test Suite Entity
description: The POST /test-suite/roots/{{testSuiteType}} operation creates a new root test suite entity. The allowable values for {{testSuiteType}} are TEST_SCENARIO, TEST_CASE, or ASSERTION. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the test suite entity should be created.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/test-suite/create-root-test-suite-entry
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/test-suite/create-root-test-suite-entry.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  test-scenario-request-model: Test Scenario Request Model
  test-case-request-model: Test case request model
  assertion-data-model: Assertion data model
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Root Test Suite Entity

##

```none
POST {{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}
```

The `POST /test-suite/roots/{{testSuiteType}}` operation creates a new root test suite entity. The allowable values for `{{testSuiteType}}` are `TEST_SCENARIO`, `TEST_CASE`, or `ASSERTION`. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the test suite entity should be created.

### Prerequisites

* [Create a branch](../version-control/snapshot-management/create-child-branch-from-snapshot.html) to get a branch ID.

* [Create a snapshot](../version-control/branch-manager/create-snapshot.html) to get a snapshot ID.

> **Collapse: Query parameters**
>
> | Query parameter | Description       |
> | --------------- | ----------------- |
> | `branch`        | Branch ID or name |
> | `snapshot`      | Snapshot ID       |

> **Collapse: Request Model**
>
> For property descriptions, refer to [Test suite data model](../test-suite.html#test-suite-data-model).
>
> #### Test Scenario Request Model
>
> | Property                                  | Type    | Required |
> | ----------------------------------------- | ------- | -------- |
> | `name`                                    | String  | Required |
> | `description`                             | String  | Optional |
> | `permissions.rolePermissions`             | JSON\[] | Optional |
> | `permissions.inherit`                     | Boolean | Optional |
> | `testScenario.request.domainId`           | String  | Optional |
> | `testScenario.request.serviceId`          | String  | Optional |
> | `testScenario.request.identityProviderId` | String  | Optional |
> | `testScenario.request.actionId`           | String  | Optional |
> | `testScenario.attributeOverrides`         | JSON    | Optional |
> | `testScenario.serviceOverrides`           | JSON    | Optional |
>
> To create an test scenario group rather than an individual test scenario, set the `testScenario` property to `null`.
>
> #### Test case request model
>
> | Property                                           | Type                                                        | Required |
> | -------------------------------------------------- | ----------------------------------------------------------- | -------- |
> | `name`                                             | String                                                      | Required |
> | `description`                                      | String                                                      | Optional |
> | `permissions.rolePermissions`                      | JSON\[]                                                     | Optional |
> | `permissions.inherit`                              | Boolean                                                     | Optional |
> | `testCase.testedEntities`                          | [Test entity](../test-suite.html#test-entity-data-model)\[] | Required |
> | `testCase.testedEntities.assertions`               | [Assertion](../test-suite.html#assertion-data-model)\[]     | Optional |
> | `testCase.testScenarioDefinitionId`                | String                                                      | Optional |
> | `testCase.testScenario.request.domainId`           | String                                                      | Optional |
> | `testCase.testScenario.request.serviceId`          | String                                                      | Optional |
> | `testCase.testScenario.request.identityProviderId` | String                                                      | Optional |
> | `testCase.testScenario.request.actionId`           | String                                                      | Optional |
> | `testCase.testScenario.attributeOverrides`         | JSON                                                        | Optional |
> | `testCase.testScenario.serviceOverrides`           | JSON                                                        | Optional |
>
> To create an test case group rather than an individual test case, set the `testCase` property to `null`.
>
> #### Assertion data model
>
> | Property                          | Type    | Required |
> | --------------------------------- | ------- | -------- |
> | `name`                            | String  | Required |
> | `description`                     | String  | Optional |
> | `permissions.rolePermissions`     | JSON\[] | Optional |
> | `permissions.inherit`             | Boolean | Optional |
> | `assertion.accessor`              | String  | Required |
> | `assertion.comparator`            | String  | Optional |
> | `assertion.expectation.valueType` | String  | Required |
> | `assertion.expectation.value`     | String  | Required |
>
> To create an assertion group rather than an individual assertion, set the `assertion` property to `null`.

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
  {
    "name": "assertion-example-1",
    "description": "",
    "numberOfChildren": 0,
    "objectType": "AssertionDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "assertion": {
        "type": "json-path",
        "accessor": "$.value",
        "comparator": "Equals",
        "expectation": {
            "valueType": "STRING",
            "value": "123"
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
curl --location --globoff '{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
    "name": "assertion-example-1",
    "description": "",
    "numberOfChildren": 0,
    "objectType": "AssertionDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "assertion": {
        "type": "json-path",
        "accessor": "$.value",
        "comparator": "Equals",
        "expectation": {
            "valueType": "STRING",
            "value": "123"
        }
    }
  }'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"" + "\n" +
@"  {" + "\n" +
@"    ""name"": ""assertion-example-1""," + "\n" +
@"    ""description"": """"," + "\n" +
@"    ""numberOfChildren"": 0," + "\n" +
@"    ""objectType"": ""AssertionDefinition""," + "\n" +
@"    ""permissions"": {" + "\n" +
@"        ""inherit"": true," + "\n" +
@"        ""rolePermissions"": []" + "\n" +
@"    }," + "\n" +
@"    ""assertion"": {" + "\n" +
@"        ""type"": ""json-path""," + "\n" +
@"        ""accessor"": ""$.value""," + "\n" +
@"        ""comparator"": ""Equals""," + "\n" +
@"        ""expectation"": {" + "\n" +
@"            ""valueType"": ""STRING""," + "\n" +
@"            ""value"": ""123""" + "\n" +
@"        }" + "\n" +
@"    }" + "\n" +
@"  }";
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

  url := "{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "assertion-example-1",
    "description": "",
    "numberOfChildren": 0,
    "objectType": "AssertionDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "assertion": {
        "type": "json-path",
        "accessor": "$.value",
        "comparator": "Equals",
        "expectation": {
            "valueType": "STRING",
            "value": "123"
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
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /test-suite/roots/{{testSuiteType}}?branch={{branchId}} HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
    "name": "assertion-example-1",
    "description": "",
    "numberOfChildren": 0,
    "objectType": "AssertionDefinition",
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "assertion": {
        "type": "json-path",
        "accessor": "$.value",
        "comparator": "Equals",
        "expectation": {
            "valueType": "STRING",
            "value": "123"
        }
    }
  }
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "\n  {\n    \"name\": \"assertion-example-1\",\n    \"description\": \"\",\n    \"numberOfChildren\": 0,\n    \"objectType\": \"AssertionDefinition\",\n    \"permissions\": {\n        \"inherit\": true,\n        \"rolePermissions\": []\n    },\n    \"assertion\": {\n        \"type\": \"json-path\",\n        \"accessor\": \"$.value\",\n        \"comparator\": \"Equals\",\n        \"expectation\": {\n            \"valueType\": \"STRING\",\n            \"value\": \"123\"\n        }\n    }\n  }");
Request request = new Request.Builder()
  .url("{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "name": "assertion-example-1",
    "description": "",
    "numberOfChildren": 0,
    "objectType": "AssertionDefinition",
    "permissions": {
      "inherit": true,
      "rolePermissions": []
    },
    "assertion": {
      "type": "json-path",
      "accessor": "$.value",
      "comparator": "Equals",
      "expectation": {
        "valueType": "STRING",
        "value": "123"
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
  'url': '{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "name": "assertion-example-1",
    "description": "",
    "numberOfChildren": 0,
    "objectType": "AssertionDefinition",
    "permissions": {
      "inherit": true,
      "rolePermissions": []
    },
    "assertion": {
      "type": "json-path",
      "accessor": "$.value",
      "comparator": "Equals",
      "expectation": {
        "valueType": "STRING",
        "value": "123"
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

url = "{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}"

payload = json.dumps({
  "name": "assertion-example-1",
  "description": "",
  "numberOfChildren": 0,
  "objectType": "AssertionDefinition",
  "permissions": {
    "inherit": True,
    "rolePermissions": []
  },
  "assertion": {
    "type": "json-path",
    "accessor": "$.value",
    "comparator": "Equals",
    "expectation": {
      "valueType": "STRING",
      "value": "123"
    }
  }
})
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n    "name": "assertion-example-1",\n    "description": "",\n    "numberOfChildren": 0,\n    "objectType": "AssertionDefinition",\n    "permissions": {\n        "inherit": true,\n        "rolePermissions": []\n    },\n    "assertion": {\n        "type": "json-path",\n        "accessor": "$.value",\n        "comparator": "Equals",\n        "expectation": {\n            "valueType": "STRING",\n            "value": "123"\n        }\n    }\n  }');
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

url = URI("{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "name": "assertion-example-1",
  "description": "",
  "numberOfChildren": 0,
  "objectType": "AssertionDefinition",
  "permissions": {
    "inherit": true,
    "rolePermissions": []
  },
  "assertion": {
    "type": "json-path",
    "accessor": "\$.value",
    "comparator": "Equals",
    "expectation": {
      "valueType": "STRING",
      "value": "123"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"assertion-example-1\",\n    \"description\": \"\",\n    \"numberOfChildren\": 0,\n    \"objectType\": \"AssertionDefinition\",\n    \"permissions\": {\n        \"inherit\": true,\n        \"rolePermissions\": []\n    },\n    \"assertion\": {\n        \"type\": \"json-path\",\n        \"accessor\": \"$.value\",\n        \"comparator\": \"Equals\",\n        \"expectation\": {\n            \"valueType\": \"STRING\",\n            \"value\": \"123\"\n        }\n    }\n  }"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/test-suite/roots/{{testSuiteType}}?branch={{branchId}}")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "objectType": "AssertionDefinition",
    "id": "0c9bffec-a65d-486f-b071-07956cad0362",
    "version": "37988047-b75c-4be6-bbe8-40832cd90a03",
    "type": "ASSERTION",
    "name": "assertion-example-1",
    "fullName": "assertion-example-1",
    "description": "",
    "parentId": null,
    "numberOfChildren": 0,
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "assertion": {
        "type": "json-path",
        "name": null,
        "accessor": "$.value",
        "comparator": "Equals",
        "expectation": {
            "value": "123",
            "valueType": "STRING"
        }
    },
    "properties": []
}
```

---

---
title: Create Rule
description: The POST /v2/policy-manager/rules operation creates a new rule. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the rule should be added.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/policy-manager/rules/create-rule
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/policy-manager/rules/create-rule.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Rule

##

```none
POST {{apiPath}}/v2/policy-manager/rules?branch={{branchId}}
```

The `POST /v2/policy-manager/rules` operation creates a new rule. The request must provide either a branch ID or a snapshot ID in the request URL to specify where the rule should be added.

### Prerequisites

* [Create a branch](../../version-control/snapshot-management/create-child-branch-from-snapshot.html) to get a branch ID.

* [Create a snapshot](../../version-control/branch-manager/create-snapshot.html) to get a snapshot ID.

> **Collapse: Query parameters**
>
> | Query parameter | Description                      |
> | --------------- | -------------------------------- |
> | `branch`        | Branch ID or name                |
> | `snapshot`      | Snapshot ID                      |
> | `page`          | Page number of returned policies |
> | `page-size`     | Number of policies per page      |

> **Collapse: Request Model**
>
> For property descriptions, refer to [Authorization rules data model](../rules.html#authorization-rules-data-model).
>
> | Property         | Type                                            | Required |
> | ---------------- | ----------------------------------------------- | -------- |
> | `condition`      | Condition object                                | Required |
> | `description`    | String                                          | Required |
> | `disabled`       | Boolean                                         | Required |
> | `effectSettings` | [EffectSettings](../rules.html#effect-settings) | Required |
> | `name`           | String                                          | Required |
> | `shared`         | Boolean                                         | Required |
> | `statements`     | Collection of StatementNodeRepresentation       | Required |
> | `targets`        | Collection of TargetNodeRepresentation          | Required |

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
{
    "type": "Rule",
    "name": "Permitted OAuth client 2",
    "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
    "shared": true,
    "disabled": false,
    "effectSettings": {
        "type": "unconditionalPermit"
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
curl --location --globoff '{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
    "type": "Rule",
    "name": "Permitted OAuth client 2",
    "description": "Rule for matching an access token'\''s client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
    "shared": true,
    "disabled": false,
    "effectSettings": {
        "type": "unconditionalPermit"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"    ""type"": ""Rule""," + "\n" +
@"    ""name"": ""Permitted OAuth client 2""," + "\n" +
@"    ""description"": ""Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.""," + "\n" +
@"    ""shared"": true," + "\n" +
@"    ""disabled"": false," + "\n" +
@"    ""effectSettings"": {" + "\n" +
@"        ""type"": ""unconditionalPermit""" + "\n" +
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

  url := "{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}"
  method := "POST"

  payload := strings.NewReader(`{
    "type": "Rule",
    "name": "Permitted OAuth client 2",
    "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
    "shared": true,
    "disabled": false,
    "effectSettings": {
        "type": "unconditionalPermit"
    }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /v2/policy-manager/rules?branch={{branchId}} HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
    "type": "Rule",
    "name": "Permitted OAuth client 2",
    "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
    "shared": true,
    "disabled": false,
    "effectSettings": {
        "type": "unconditionalPermit"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"type\": \"Rule\",\n    \"name\": \"Permitted OAuth client 2\",\n    \"description\": \"Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.\",\n    \"shared\": true,\n    \"disabled\": false,\n    \"effectSettings\": {\n        \"type\": \"unconditionalPermit\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "type": "Rule",
    "name": "Permitted OAuth client 2",
    "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
    "shared": true,
    "disabled": false,
    "effectSettings": {
      "type": "unconditionalPermit"
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
  'url': '{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "type": "Rule",
    "name": "Permitted OAuth client 2",
    "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
    "shared": true,
    "disabled": false,
    "effectSettings": {
      "type": "unconditionalPermit"
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

url = "{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}"

payload = json.dumps({
  "type": "Rule",
  "name": "Permitted OAuth client 2",
  "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
  "shared": True,
  "disabled": False,
  "effectSettings": {
    "type": "unconditionalPermit"
  }
})
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n    "type": "Rule",\n    "name": "Permitted OAuth client 2",\n    "description": "Rule for matching an access token\'s client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",\n    "shared": true,\n    "disabled": false,\n    "effectSettings": {\n        "type": "unconditionalPermit"\n    }\n}');
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

url = URI("{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "type": "Rule",
  "name": "Permitted OAuth client 2",
  "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
  "shared": true,
  "disabled": false,
  "effectSettings": {
    "type": "unconditionalPermit"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"type\": \"Rule\",\n    \"name\": \"Permitted OAuth client 2\",\n    \"description\": \"Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.\",\n    \"shared\": true,\n    \"disabled\": false,\n    \"effectSettings\": {\n        \"type\": \"unconditionalPermit\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v2/policy-manager/rules?branch={{branchId}}")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "id": "f39b0dab-9500-4f91-906c-7235066add55",
    "version": "fb07c95d-ace1-4b3b-9033-789fb4dea5b2",
    "type": "Rule",
    "name": "Permitted OAuth client 2",
    "description": "Rule for matching an access token's client_id value with a permitted OAuth client. Clone this rule to a policy and then replace CHANGEME with a permitted client ID.",
    "shared": true,
    "disabled": false,
    "permissions": {
        "inherit": true,
        "rolePermissions": []
    },
    "condition": {
        "empty": {}
    },
    "properties": [],
    "targets": [],
    "effectSettings": {
        "type": "unconditionalPermit"
    },
    "statements": []
}
```

---

---
title: Create Snapshot
description: The POST /version-control/branches/{{branchId}}/commit operation commits all uncommitted changes into a new snapshot. The operation places the snapshot at the head of the branch identified by {{branchId}}.
component: pingauthorize
page_id: pingauthorize:pingauthorize:policy-editor/version-control/branch-manager/create-snapshot
canonical_url: https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-editor/version-control/branch-manager/create-snapshot.html
llms_txt: https://developer.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Snapshot

##

```none
POST {{apiPath}}/version-control/branches/{{branchId}}/commit
```

The `POST /version-control/branches/{{branchId}}/commit` operation commits all uncommitted changes into a new snapshot. The operation places the snapshot at the head of the branch identified by `{{branchId}}`.

After committing your changes, you can [create a deployment package](../../deployment-package/create-deployment-package.html) from the commit.

> **Collapse: Request Model**
>
> For property descriptions, refer to [Branch manager data model](../branch-manager.html#branch-manager-data-model)
>
> | Property  | Type   | Required |
> | --------- | ------ | -------- |
> | `message` | String | Required |

### Headers

Content-Type      application/json

x-user-id      {{userId}}

### Body

raw ( application/json )

```json
{
    "message": "example-commit-message"
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
curl --location --globoff '{{apiPath}}/version-control/branches/{{branchId}}/commit' \
--header 'x-user-id: {{userId}}' \
--header 'Content-Type: application/json' \
--data '{
    "message": "example-commit-message"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/version-control/branches/{{branchId}}/commit")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("x-user-id", "{{userId}}");
request.AddHeader("Content-Type", "application/json");
var body = @"{" + "\n" +
@"    ""message"": ""example-commit-message""" + "\n" +
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

  url := "{{apiPath}}/version-control/branches/{{branchId}}/commit"
  method := "POST"

  payload := strings.NewReader(`{
    "message": "example-commit-message"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("x-user-id", "{{userId}}")
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
POST /version-control/branches/{{branchId}}/commit HTTP/1.1
Host: {{apiPath}}
x-user-id: {{userId}}
Content-Type: application/json

{
    "message": "example-commit-message"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"message\": \"example-commit-message\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/version-control/branches/{{branchId}}/commit")
  .method("POST", body)
  .addHeader("x-user-id", "{{userId}}")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/version-control/branches/{{branchId}}/commit",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "x-user-id": "{{userId}}",
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "message": "example-commit-message"
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
  'url': '{{apiPath}}/version-control/branches/{{branchId}}/commit',
  'headers': {
    'x-user-id': '{{userId}}',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "message": "example-commit-message"
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

url = "{{apiPath}}/version-control/branches/{{branchId}}/commit"

payload = json.dumps({
  "message": "example-commit-message"
})
headers = {
  'x-user-id': '{{userId}}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/version-control/branches/{{branchId}}/commit');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'x-user-id' => '{{userId}}',
  'Content-Type' => 'application/json'
));
$request->setBody('{\n    "message": "example-commit-message"\n}');
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

url = URI("{{apiPath}}/version-control/branches/{{branchId}}/commit")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["x-user-id"] = "{{userId}}"
request["Content-Type"] = "application/json"
request.body = JSON.dump({
  "message": "example-commit-message"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"message\": \"example-commit-message\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/version-control/branches/{{branchId}}/commit")!,timeoutInterval: Double.infinity)
request.addValue("{{userId}}", forHTTPHeaderField: "x-user-id")
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

201 Created

```json
{
    "id": "8b5491c0-b49c-404c-8ca3-382744c976ad",
    "parentId": "98ef14f6-ac2f-4cd4-b927-9ff2e1f6b56d",
    "state": "COMMITTED",
    "commitDetails": {
        "userId": "admin",
        "dateTime": "2025-03-06T00:43:48.477821Z",
        "message": "example-commit-message"
    },
    "approvals": [],
    "branchId": "e94d66f9-ea57-4a92-b4a1-eb0c26af26fa"
}
```
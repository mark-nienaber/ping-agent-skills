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

---

---
title: Accept Device Authorization Grant Consent
description: The POST /{{envID}}/flows/{{flowID}} operation uses the application/vnd.pingidentity.deviceAuthGrant.consent+json custom media type in the request header to specify that a consent action is required.
component: pingone-api
page_id: pingone-api:auth:flows/device-authorization-grant-flows/accept-device-authorization-grant-consent
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/device-authorization-grant-flows/accept-device-authorization-grant-consent.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
---

# Accept Device Authorization Grant Consent

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

The `POST /{{envID}}/flows/{{flowID}}` operation uses the `application/vnd.pingidentity.deviceAuthGrant.consent+json` custom media type in the request header to specify that a consent action is required.

An authentication flow can prompt users to consent to (or reject) an agreement. The flow configuration determines whether consent is required. If the user does not have any recorded consents that satisfy any of the agreement languages, then the flow requires user consent.

### Prerequisites

* Send an authorize request to get a user code: [Device Authorization](../../openid-connect-oauth-2/device-authorization-grant.html).

* Refer also to the \`DAG\_CONSENT\_REQUIRED \` flow state in the [Flow status values table](../flows-1.html).

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After accepting consent, a record is stored in the user's [OAuth Scope Consents](../../../platform/users/user-oauth-scope-consents.html). If the user refuses to consent to the terms of service agreement, the flow fails. |

> **Collapse: Request Model**
>
> | Property | Type    | Required |
> | -------- | ------- | -------- |
> | `accept` | Boolean | Required |
>
> Refer to the [Flows](../flows-1.html) for full property descriptions.

### Headers

Content-Type      application/vnd.pingidentity.deviceAuthGrant.consent+json

### Body

raw ( application/vnd.pingidentity.deviceAuthGrant.consent+json )

```json
{
    "accept": true
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
--header 'Content-Type: application/vnd.pingidentity.deviceAuthGrant.consent+json' \
--data '{
    "accept": true
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/flows/{{flowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.deviceAuthGrant.consent+json");
var body = @"{" + "\n" +
@"    ""accept"": true" + "\n" +
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
    "accept": true
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.deviceAuthGrant.consent+json")

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
Content-Type: application/vnd.pingidentity.deviceAuthGrant.consent+json

{
    "accept": true
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.deviceAuthGrant.consent+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"accept\": true\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/flows/{{flowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.deviceAuthGrant.consent+json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/flows/{{flowID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.deviceAuthGrant.consent+json"
  },
  "data": JSON.stringify({
    "accept": true
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
    'Content-Type': 'application/vnd.pingidentity.deviceAuthGrant.consent+json'
  },
  body: JSON.stringify({
    "accept": true
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
  "accept": True
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.deviceAuthGrant.consent+json'
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
  'Content-Type' => 'application/vnd.pingidentity.deviceAuthGrant.consent+json'
));
$request->setBody('{\n    "accept": true\n}');
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
request["Content-Type"] = "application/vnd.pingidentity.deviceAuthGrant.consent+json"
request.body = JSON.dump({
  "accept": true
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"accept\": true\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/flows/{{flowID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.deviceAuthGrant.consent+json", forHTTPHeaderField: "Content-Type")

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
title: Admin Invitations
description: The flows endpoint supports operations to accept administrator invitations sent to users.
component: pingone-api
page_id: pingone-api:auth:flows/flows-1/admin-invitations
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/flows-1/admin-invitations.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  response-codes: Response codes
---

# Admin Invitations

The flows endpoint supports operations to accept administrator invitations sent to users.

## Response codes

| Code | Message                                  |
| ---- | ---------------------------------------- |
| 200  | Successful operation.                    |
| 204  | Successfully removed. No content.        |
| 400  | The request could not be completed.      |
| 401  | You do not have access to this resource. |
| 404  | The requested resource was not found.    |

---

---
title: Agreement Accept Consent
description: An authentication flow can prompt users to consent to (or reject) an agreement. The agreement to which users must consent is configured in the sign-on policy. The flow determines whether consent is required based on the agreement configuration and the user's consent history. If the user does not have any recorded consents that satisfy any of the agreement languages, then the flow requires user consent.
component: pingone-api
page_id: pingone-api:auth:flows/registration-and-verification/agreement-accept-consent
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/registration-and-verification/agreement-accept-consent.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Agreement Accept Consent

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

An authentication flow can prompt users to consent to (or reject) an agreement. The agreement to which users must consent is configured in the sign-on policy. The flow determines whether consent is required based on the agreement configuration and the user's consent history. If the user does not have any recorded consents that satisfy any of the agreement languages, then the flow requires user consent.

### Prerequisites

* Refer to [Flows](../flows-1.html) for important overview information.

* Send an authorize request to get a flow ID: [Authorize](../../openid-connect-oauth-2/authorize-intro.html). Refer also to [Login action authentication flow](../../../foundations/authentication-concepts/pingone-authentication-flow-states/login-action.html) and [Authorization and authentication](../../../foundations/authentication-concepts.html).

* Start the flow: [Read Flow](../flows-1/read-flow.html).

* Refer also to the `AGREEMENT_CONSENT_REQUIRED` flow state in the [Flow status values table](../flows-1.html).

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | If the user refuses to consent to the terms of service agreement, the flow fails. |

The `POST /{{envID}}/flows/{{flowID}}` operation uses the `application/vnd.pingidentity.user.consent+json` custom media type in the request header to specify that a consent action is required.

> **Collapse: Request Model**
>
> | Property | Type    | Required |
> | -------- | ------- | -------- |
> | `accept` | Boolean | Required |

### Headers

Content-Type      application/vnd.pingidentity.user.consent+json

### Body

raw ( application/vnd.pingidentity.user.consent+json )

```json
{
  "accept": true
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
--header 'Content-Type: application/vnd.pingidentity.user.consent+json' \
--data '{
  "accept": true
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/flows/{{flowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.user.consent+json");
var body = @"{" + "\n" +
@"  ""accept"": true" + "\n" +
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
  "accept": true
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.user.consent+json")

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
Content-Type: application/vnd.pingidentity.user.consent+json

{
  "accept": true
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.user.consent+json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"accept\": true\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/flows/{{flowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.user.consent+json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/flows/{{flowID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.user.consent+json"
  },
  "data": JSON.stringify({
    "accept": true
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
    'Content-Type': 'application/vnd.pingidentity.user.consent+json'
  },
  body: JSON.stringify({
    "accept": true
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
  "accept": True
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.user.consent+json'
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
  'Content-Type' => 'application/vnd.pingidentity.user.consent+json'
));
$request->setBody('{\n  "accept": true\n}');
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
request["Content-Type"] = "application/vnd.pingidentity.user.consent+json"
request.body = JSON.dump({
  "accept": true
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"accept\": true\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/flows/{{flowID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.user.consent+json", forHTTPHeaderField: "Content-Type")

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
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/00003344-4d27-4d08-8ebf-3153104acf80"
        }
    },
    "id": "00003344-4d27-4d08-8ebf-3153104acf80",
    "session": {
        "id": "44b31cb5-39b2-414a-8b20-9a9d178c591c"
    },
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=00003344-4d27-4d08-8ebf-3153104acf80",
    "status": "COMPLETED",
    "createdAt": "2021-10-07T18:24:57.154Z",
    "expiresAt": "2021-10-07T18:40:17.259Z",
    "_embedded": {
        "user": {
            "id": "c8c726b0-b38f-4c77-99e3-0e87365c537a",
            "username": "agreement_user_1633631083",
            "name": {
                "given": "Test",
                "family": "AgreementUser"
            }
        },
        "application": {
            "name": "WebAppWithAgreement_1633630997"
        }
    }
}
```

---

---
title: Authorization
description: The authorize endpoints support the following actions:
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-intro
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-intro.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authorization

The authorize endpoints support the following actions:

* The authorize endpoint `/{{envID}}/as/authorize` is used to interact with the end user and obtain an authorization grant. Note that PingOne supports both `GET` and `POST` operations for authorize requests. The supported parameters for an authorize request vary depending on the value of the `response_type` parameter (`code`, `token`, `id_token` or combinations of these three options).

* For non-redirect flows, such as with native mobile apps in which the app renders the end user interface, `response_mode` property value is set to `pi.flow`. This setting allows the app to authenticate using the PingOne flows API without needing to handle HTTP redirections. The `pi.flow` value is also used with transaction approval use cases in which strong authentication is required for elevated security for a high-value transaction, or high-risk resource or service.

* For offline access, on applications having a `refresh_token` grant type, when the authorize request includes `offline_access` in the `scope` parameter, and the request specifies the `authorization_code` or `device_code` grant type, a refresh token is always included in the token response. Otherwise, if the `offline_access` scope is omitted from the `scope` parameter of the authorize request, a refresh token is not included, even if the `refresh_token` grant type is defined in the application configuration. Refer to [Application Resource Grants](../../platform/applications/application-resource-grants.html) to add the `offline_access` scope to the application's resource grant.

  If the application does not have a resource grant that includes `offline_access` in the `scope` parameter, a refresh token is always included in the token response for grant types that allow it.

  |   |                                                                                                                                                                                                                                                                                                                                                                   |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If the client includes `prompt=consent` in a request with an `authorization_code` grant type, PingOne doesn't prompt for application consent. This limitation doesn't apply to requests with a `device_code` grant type, because the PingOne authentication policy service always prompts for application consent when requests use the `device_code` grant type. |

> **Collapse: Related topics**
>
> * [Authorization and authentication by application type](../../foundations/authentication-concepts/authorization-and-authentication-by-application-type.html)
>
> * [Authorization flow by grant type](../../foundations/authentication-concepts/authorization-flow-by-grant-type.html)
>
> * [Access services through scopes and roles](../../foundations/pingone-roles-scopes-and-permissions/access-services-through-scopes-and-roles.html)

---

---
title: Authorize (authorization_code GET)
description: The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the GET /{{envID}}/as/authorize operation. The request URL includes the response_type parameter with a value of code, which designates that this authorization request, if successful, returns an authorization code that is exchanged for an access token.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-authorization_code
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-authorization_code.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example-request: Example Request
  example-response: Example Response
---

# Authorize (authorization\_code GET)

##

```none
GET {{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}
```

The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the `GET /{{envID}}/as/authorize` operation. The request URL includes the `response_type` parameter with a value of `code`, which designates that this authorization request, if successful, returns an authorization code that is exchanged for an access token.

For a Proof Key for Code Exchange (PKCE) authorization request, the `/{{envID}}/as/authorize` request must include the `code_challenge` parameter. The `code_challenge_method` parameter is required if the application's `pkceEnforcement` property is set to `S256_REQUIRED`. Otherwise, it is optional.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The optional `request` property specifies a JWT that enables OIDC/OAuth2 request parameters to be passed as a single, self-contained parameter. For details on how to construct the JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

> **Collapse: Query parameters**
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1%3Aread%3Auser&redirect_uri={{redirect_uri}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
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

  url := "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1%3Aread%3Auser&redirect_uri={{redirect_uri}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
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
GET /{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}} HTTP/1.1
Host: {{authPath}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
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

url = URI("{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1:read:user&redirect_uri={{redirect_uri}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{appID}}&scope=openid%20profile%20p1%3Aread%3Auser&redirect_uri={{redirect_uri}}")!,timeoutInterval: Double.infinity)
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

302 Found

---

---
title: Authorize (authorization_code POST)
description: "The authorization endpoint is used in a POST request. The POST request accepts all the same parameters as the GET request. Both initiate an authorization request. Note that for the POST request, parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the Content-Type: application/x-www-form-urlencoded request header."
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-authorization_code-1
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-authorization_code-1.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Authorize (authorization\_code POST)

##

```none
POST {{authPath}}/{{envID}}/as/authorize
```

The authorization endpoint is used in a `POST` request. The `POST` request accepts all the same parameters as the `GET` request. Both initiate an authorization request. Note that for the `POST` request, parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the `Content-Type: application/x-www-form-urlencoded` request header.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The optional `request` property specifies a JWT that enables OIDC/OAuth2 request parameters to be passed as a single, self-contained parameter. For details on how to construct the JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

The sample shows the `POST /{{envID}}/as/authorize` operation.

### Prerequisites

* Refer to [OpenID Connect/OAuth 2](../openid-connect-oauth-2.html) for important overview information.

* Create an application to get an `appID`. Refer to \[Application Operations]/pingone/platform/v1/api/#application-operations). Run [Read All Applications](../../platform/applications/applications-1/read-all-applications.html) to find an existing application.

* Run [Read All Templates](../../platform/notifications/notifications-templates/read-all-templates.html) to find a `templateName`.

* Run [Read All Contents](../../platform/notifications/notifications-templates/read-all-contents.html) to find a `variantName`.

> **Collapse: Request Model**
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |
>
> Refer to the [OpenID Connect/OAuth2 data model](../openid-connect-oauth-2.html) for full property descriptions.

### Headers

Content-Type      application/x-www-form-urlencoded

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key            | Value                       |
| -------------- | --------------------------- |
| response\_type | code                        |
| client\_id     | {{appID}}                   |
| redirect\_uri  | {{redirect\_uri}}           |
| scope          | openid profile p1:read:user |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'response_type=code' \
--data-urlencode 'client_id={{appID}}' \
--data-urlencode 'redirect_uri={{redirect_uri}}' \
--data-urlencode 'scope=openid profile p1:read:user'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddParameter("response_type", "code");
request.AddParameter("client_id", "{{appID}}");
request.AddParameter("redirect_uri", "{{redirect_uri}}");
request.AddParameter("scope", "openid profile p1:read:user");
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

  url := "{{authPath}}/{{envID}}/as/authorize"
  method := "POST"

  payload := strings.NewReader("response_type=code&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")

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
POST /{{envID}}/as/authorize HTTP/1.1
Host: {{authPath}}
Content-Type: application/x-www-form-urlencoded

response_type=code&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "response_type=code&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid profile p1:read:user");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "response_type": "code",
    "client_id": "{{appID}}",
    "redirect_uri": "{{redirect_uri}}",
    "scope": "openid profile p1:read:user"
  }
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{authPath}}/{{envID}}/as/authorize',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  form: {
    'response_type': 'code',
    'client_id': '{{appID}}',
    'redirect_uri': '{{redirect_uri}}',
    'scope': 'openid profile p1:read:user'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize"

payload = 'response_type=code&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded'
));
$request->addPostParameter(array(
  'response_type' => 'code',
  'client_id' => '{{appID}}',
  'redirect_uri' => '{{redirect_uri}}',
  'scope' => 'openid profile p1:read:user'
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

url = URI("{{authPath}}/{{envID}}/as/authorize")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request.body = "response_type=code&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "response_type=code&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize")!,timeoutInterval: Double.infinity)
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

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

302 Found

---

---
title: Authorize (device)
description: "The POST /{{envID}}/as/device_authorization endpoint initiates a device authorization operation on applications that specify DEVICE_CODE as the grantTypes property value. The POST request's parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the Content-Type: application/x-www-form-urlencoded request header."
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/device-authorization-grant/authorize-device
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/device-authorization-grant/authorize-device.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Authorize (device)

##

```none
POST {{authPath}}/{{envID}}/as/device_authorization
```

The `POST /{{envID}}/as/device_authorization` endpoint initiates a device authorization operation on applications that specify `DEVICE_CODE` as the `grantTypes` property value. The `POST` request's parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the `Content-Type: application/x-www-form-urlencoded` request header.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `verification_uri` and `verification_uri_complete` properties in the response include the identifier `/go` in the URL. This ID is the value of the `devicePathId` set on the application. For more information about application configuration for device authorization grants, refer to [Create Application (OIDC Device Authorization Grant)](../../../platform/applications/applications-1/create-application-oidc-device-authorization-grant.html). |

> **Collapse: Request Model**
>
> | Property    | Type   | Required |
> | ----------- | ------ | -------- |
> | `client_id` | String | Required |
> | `scope`     | String | Optional |
>
> Refer to the [Device authentication grant data model](../device-authorization-grant.html#device-authorization-grant-data-model) for full property descriptions.

### Headers

Content-Type      application/x-www-form-urlencoded

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key        | Value           |
| ---------- | --------------- |
| client\_id | {{deviceAppID}} |
| scope      | openid          |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/device_authorization' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{deviceAppID}}' \
--data-urlencode 'scope=openid'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/device_authorization")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddParameter("client_id", "{{deviceAppID}}");
request.AddParameter("scope", "openid");
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

  url := "{{authPath}}/{{envID}}/as/device_authorization"
  method := "POST"

  payload := strings.NewReader("client_id=%7B%7BdeviceAppID%7D%7D&scope=openid")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")

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
POST /{{envID}}/as/device_authorization HTTP/1.1
Host: {{authPath}}
Content-Type: application/x-www-form-urlencoded

client_id=%7B%7BdeviceAppID%7D%7D&scope=openid
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "client_id={{deviceAppID}}&scope=openid");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/device_authorization")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/device_authorization",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "client_id": "{{deviceAppID}}",
    "scope": "openid"
  }
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{authPath}}/{{envID}}/as/device_authorization',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  form: {
    'client_id': '{{deviceAppID}}',
    'scope': 'openid'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/device_authorization"

payload = 'client_id=%7B%7BdeviceAppID%7D%7D&scope=openid'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/device_authorization');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded'
));
$request->addPostParameter(array(
  'client_id' => '{{deviceAppID}}',
  'scope' => 'openid'
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

url = URI("{{authPath}}/{{envID}}/as/device_authorization")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request.body = "client_id=%7B%7BdeviceAppID%7D%7D&scope=openid"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "client_id=%7B%7BdeviceAppID%7D%7D&scope=openid"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/device_authorization")!,timeoutInterval: Double.infinity)
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

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
    "device_code": "031887ee-2328-49a7-a2cc-83ff491e10f8",
    "user_code": "BVKV-2GZ2",
    "verification_uri": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/device/go",
    "verification_uri_complete": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/device/go?user_code=BVKV-2GZ2",
    "expires_in": 600,
    "interval": 5
}
```

---

---
title: Authorize (hybrid GET)
description: The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the GET /{{envID}}/as/authorize operation. The request URL includes the response_type parameter with a value of code id_token token, which designates that this authorization request is a hybrid flow.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-hybrid
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-hybrid.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example-request: Example Request
  example-response: Example Response
---

# Authorize (hybrid GET)

##

```none
GET {{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}
```

The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the `GET /{{envID}}/as/authorize` operation. The request URL includes the `response_type` parameter with a value of `code id_token token`, which designates that this authorization request is a hybrid flow.

In a hybrid flow, an authorization code is returned from the authorization endpoint, some tokens are returned from the authorization endpoint, and others are returned from the token endpoint. The authorization endpoint's `response_type` property specifies the `code` type and it also specifies `id_token`, or `token`, or both. An authorization code (specified by the `code` response type) is always returned in a hybrid flow. An ID token is returned when the `response_type` property is `code id_token` or `code id_token token`. An access token is returned when the `response_type` property is `code token` or `code id_token token`.

Note that for the `POST` request, parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the `Content-Type: application/x-www-form-urlencoded` request header.

For a Proof Key for Code Exchange (PKCE) authorization request, the `/{{envID}}/as/authorize` request must include the `code_challenge` parameter. The `code_challenge_method` parameter is required if the application's `pkceEnforcement` property is set to `S256_REQUIRED`. Otherwise, it is optional.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The optional `request` property specifies a JWT that enables OIDC/OAuth2 request parameters to be passed as a single, self-contained parameter. For details on how to construct the JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

The sample shows the `POST /{{envID}}/as/authorize` operation for a hybrid flow. For more information about hybrid flows, refer to [Authentication using the Hybrid Flow](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth).

> **Collapse: Query parameters**
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |

> **Collapse: Related topics**
>
> * [Authorization flow by grant type](../../foundations/authentication-concepts/authorization-flow-by-grant-type.html)

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1%3Aread%3Auser&nonce={{nonce}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
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

  url := "{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1%3Aread%3Auser&nonce={{nonce}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
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
GET /{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}} HTTP/1.1
Host: {{authPath}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
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

url = URI("{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize?response_type=code%20token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1%3Aread%3Auser&nonce={{nonce}}")!,timeoutInterval: Double.infinity)
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

302 Found

---

---
title: Authorize (hybrid POST)
description: The authorization endpoint can be used to initiate a hybrid flow authorization request, in which an authorization code is returned from the authorization endpoint, some tokens are returned from the authorization endpoint, and others are returned from the token endpoint. In a hybrid flow, the authorization endpoint's response_type property specifies the code type and it also specifies id_token, or token, or both. An authorization code (specified by the code response type) is always returned in a hybrid flow. An ID token is returned when the response_type property is code id_token or code id_token token. An access token is returned when the response_type property is code token or code id_token token.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-hybrid-1
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-hybrid-1.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Authorize (hybrid POST)

##

```none
POST {{authPath}}/{{envID}}/as/authorize
```

The authorization endpoint can be used to initiate a hybrid flow authorization request, in which an authorization code is returned from the authorization endpoint, some tokens are returned from the authorization endpoint, and others are returned from the token endpoint. In a hybrid flow, the authorization endpoint's `response_type` property specifies the `code` type and it also specifies `id_token`, or `token`, or both. An authorization code (specified by the `code` response type) is always returned in a hybrid flow. An ID token is returned when the `response_type` property is `code id_token` or `code id_token token`. An access token is returned when the `response_type` property is `code token` or `code id_token token`.

Note that for the `POST` request, parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the `Content-Type: application/x-www-form-urlencoded` request header.

For a Proof Key for Code Exchange (PKCE) authorization request, the `/{{envID}}/as/authorize` request must include the `code_challenge` parameter. The `code_challenge_method` parameter is required if the application's `pkceEnforcement` property is set to `S256_REQUIRED`. Otherwise, it is optional.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The optional `request` property specifies a JWT that enables OIDC/OAuth2 request parameters to be passed as a single, self-contained parameter. For details on how to construct the JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

The sample shows the `POST /{{envID}}/as/authorize` operation for a hybrid flow. For more information about hybrid flows, refer to [Authentication using the Hybrid Flow](https://openid.net/specs/openid-connect-core-1_0.html#HybridFlowAuth).

### Prerequisites

* Refer to [OpenID Connect/OAuth 2](../openid-connect-oauth-2.html) for important overview information.

* Create an application to get an `appID`. Refer to [Application Operations](../../platform/applications/applications-1.html). Run [Read All Applications](../../platform/applications/applications-1/read-all-applications.html) to find an existing application.

* Run [Read All Templates](../../platform/notifications/notifications-templates/read-all-templates.html) to find a `templateName`.

* Run [Read All Contents](../../platform/notifications/notifications-templates/read-all-contents.html) to find a `variantName`.

> **Collapse: Request Model**
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |
>
> Refer to the [OpenID Connect/OAuth2 data model](../openid-connect-oauth-2.html) for full property descriptions.

> **Collapse: Related topics**
>
> * [Authorization flow by grant type](../../foundations/authentication-concepts/authorization-flow-by-grant-type.html)

### Headers

Content-Type      application/x-www-form-urlencoded

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key            | Value                |
| -------------- | -------------------- |
| response\_type | code id\_token       |
| client\_id     | {{appID}}            |
| redirect\_uri  | {{redirect\_uri}}    |
| scope          | openid profile email |
| state          | {{state}}            |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'response_type=code id_token' \
--data-urlencode 'client_id={{appID}}' \
--data-urlencode 'redirect_uri={{redirect_uri}}' \
--data-urlencode 'scope=openid profile email' \
--data-urlencode 'state={{state}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddParameter("response_type", "code id_token");
request.AddParameter("client_id", "{{appID}}");
request.AddParameter("redirect_uri", "{{redirect_uri}}");
request.AddParameter("scope", "openid profile email");
request.AddParameter("state", "{{state}}");
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

  url := "{{authPath}}/{{envID}}/as/authorize"
  method := "POST"

  payload := strings.NewReader("response_type=code%20id_token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20email&state=%7B%7Bstate%7D%7D")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")

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
POST /{{envID}}/as/authorize HTTP/1.1
Host: {{authPath}}
Content-Type: application/x-www-form-urlencoded

response_type=code%20id_token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20email&state=%7B%7Bstate%7D%7D
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "response_type=code id_token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid profile email&state={{state}}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "response_type": "code id_token",
    "client_id": "{{appID}}",
    "redirect_uri": "{{redirect_uri}}",
    "scope": "openid profile email",
    "state": "{{state}}"
  }
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{authPath}}/{{envID}}/as/authorize',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  form: {
    'response_type': 'code id_token',
    'client_id': '{{appID}}',
    'redirect_uri': '{{redirect_uri}}',
    'scope': 'openid profile email',
    'state': '{{state}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize"

payload = 'response_type=code%20id_token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20email&state=%7B%7Bstate%7D%7D'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded'
));
$request->addPostParameter(array(
  'response_type' => 'code id_token',
  'client_id' => '{{appID}}',
  'redirect_uri' => '{{redirect_uri}}',
  'scope' => 'openid profile email',
  'state' => '{{state}}'
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

url = URI("{{authPath}}/{{envID}}/as/authorize")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request.body = "response_type=code%20id_token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20email&state=%7B%7Bstate%7D%7D"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "response_type=code%20id_token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20email&state=%7B%7Bstate%7D%7D"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize")!,timeoutInterval: Double.infinity)
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

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

302 Found

---

---
title: Authorize (implicit GET)
description: The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the GET /{{envID}}/as/authorize operation. The request URL includes the response_type parameter with a value of token.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-implicit
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-implicit.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example-request: Example Request
  example-response: Example Response
---

# Authorize (implicit GET)

##

```none
GET {{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}
```

The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the `GET /{{envID}}/as/authorize` operation. The request URL includes the `response_type` parameter with a value of `token`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The optional `request` property specifies a JWT that enables OIDC/OAuth2 request parameters to be passed as a single, self-contained parameter. For details on how to construct the JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

> **Collapse: Query parameters**
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1%3Aread%3Auser&nonce={{nonce}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
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

  url := "{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1%3Aread%3Auser&nonce={{nonce}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
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
GET /{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}} HTTP/1.1
Host: {{authPath}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
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

url = URI("{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1:read:user&nonce={{nonce}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize?response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid%20profile%20p1%3Aread%3Auser&nonce={{nonce}}")!,timeoutInterval: Double.infinity)
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

302 Found

---

---
title: Authorize (implicit POST)
description: "The authorization endpoint is used in a POST request. The POST request accepts all the same parameters as the GET request. Both initiate an authorization request. Note that for the POST request, parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the Content-Type: application/x-www-form-urlencoded request header."
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-implicit-1
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-implicit-1.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Authorize (implicit POST)

##

```none
POST {{authPath}}/{{envID}}/as/authorize
```

The authorization endpoint is used in a `POST` request. The `POST` request accepts all the same parameters as the `GET` request. Both initiate an authorization request. Note that for the `POST` request, parameters and their values are Form Serialized by adding the parameter names and values to the entity body of the HTTP request and specifying the `Content-Type: application/x-www-form-urlencoded` request header.

The sample shows the `POST /{{envID}}/as/authorize` operation. The request includes a `response_type` parameter with a value of `token`, which designates that this authorization request, if successful, returns an access token.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The optional `request` property specifies a JWT that enables OIDC/OAuth2 request parameters to be passed as a single, self-contained parameter. For details on how to construct the JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

### Prerequisites

* Refer to [OpenID Connect/OAuth 2](../openid-connect-oauth-2.html) for important overview information.

* Create an application to get an `appID`. Refer to [Application Operations](../../platform/applications/applications-1.html). Run [Read All Applications](../../platform/applications/applications-1/read-all-applications.html) to find an existing application.

* Run [Read All Templates](../../platform/notifications/notifications-templates/read-all-templates.html) to find a `templateName`.

* Run [Read All Contents](../../platform/notifications/notifications-templates/read-all-contents.html) to find a `variantName`.

> **Collapse: Request Model**
>
> Supported parameters for an authorization request with a `response_type` that returns a token:
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |
>
> Refer to the [OpenID Connect/OAuth2 data model](../openid-connect-oauth-2.html) for full property descriptions.

### Headers

Content-Type      application/x-www-form-urlencoded

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key            | Value                       |
| -------------- | --------------------------- |
| response\_type | token                       |
| client\_id     | {{appID}}                   |
| redirect\_uri  | {{redirect\_uri}}           |
| scope          | openid profile p1:read:user |
| nonce          | {{nonce}}                   |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'response_type=token' \
--data-urlencode 'client_id={{appID}}' \
--data-urlencode 'redirect_uri={{redirect_uri}}' \
--data-urlencode 'scope=openid profile p1:read:user' \
--data-urlencode 'nonce={{nonce}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddParameter("response_type", "token");
request.AddParameter("client_id", "{{appID}}");
request.AddParameter("redirect_uri", "{{redirect_uri}}");
request.AddParameter("scope", "openid profile p1:read:user");
request.AddParameter("nonce", "{{nonce}}");
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

  url := "{{authPath}}/{{envID}}/as/authorize"
  method := "POST"

  payload := strings.NewReader("response_type=token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser&nonce=%7B%7Bnonce%7D%7D")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")

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
POST /{{envID}}/as/authorize HTTP/1.1
Host: {{authPath}}
Content-Type: application/x-www-form-urlencoded

response_type=token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser&nonce=%7B%7Bnonce%7D%7D
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "response_type=token&client_id={{appID}}&redirect_uri={{redirect_uri}}&scope=openid profile p1:read:user&nonce={{nonce}}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "data": {
    "response_type": "token",
    "client_id": "{{appID}}",
    "redirect_uri": "{{redirect_uri}}",
    "scope": "openid profile p1:read:user",
    "nonce": "{{nonce}}"
  }
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{authPath}}/{{envID}}/as/authorize',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  form: {
    'response_type': 'token',
    'client_id': '{{appID}}',
    'redirect_uri': '{{redirect_uri}}',
    'scope': 'openid profile p1:read:user',
    'nonce': '{{nonce}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize"

payload = 'response_type=token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser&nonce=%7B%7Bnonce%7D%7D'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded'
));
$request->addPostParameter(array(
  'response_type' => 'token',
  'client_id' => '{{appID}}',
  'redirect_uri' => '{{redirect_uri}}',
  'scope' => 'openid profile p1:read:user',
  'nonce' => '{{nonce}}'
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

url = URI("{{authPath}}/{{envID}}/as/authorize")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request.body = "response_type=token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser&nonce=%7B%7Bnonce%7D%7D"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "response_type=token&client_id=%7B%7BappID%7D%7D&redirect_uri=%7B%7Bredirect_uri%7D%7D&scope=openid%20profile%20p1%3Aread%3Auser&nonce=%7B%7Bnonce%7D%7D"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize")!,timeoutInterval: Double.infinity)
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

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

302 Found

---

---
title: Authorize (implicit) (request_uri)
description: The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the GET /{{envID}}/as/authorize operation. The request URL includes the request_uri parameter which is returned from a pushed authorization request.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/par-authorize-implicit
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/par-authorize-implicit.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example-request: Example Request
  example-response: Example Response
---

# Authorize (implicit) (request\_uri)

##

```none
GET {{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}
```

The authorization endpoint is used to interact with the end user and obtain an authorization grant. The sample shows the `GET /{{envID}}/as/authorize` operation. The request URL includes the `request_uri` parameter which is returned from a pushed authorization request.

> **Collapse: Query parameters**
>
> | Parameter     | Description                                                                 |
> | ------------- | --------------------------------------------------------------------------- |
> | `client_id`   | The application's UUID.                                                     |
> | `request_uri` | A string that specifies the URI corresponding to the authorization request. |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
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

  url := "{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
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
GET /{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}} HTTP/1.1
Host: {{authPath}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
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

url = URI("{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize?client_id={{appID}}&request_uri={{requestURI}}")!,timeoutInterval: Double.infinity)
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

302 Moved Temporarily

---

---
title: Authorize (Non-redirect and MFA Only Flows)
description: For browerless use cases such as native mobile apps where the app wants to render the end user interface, setting the response_mode property to pi.flow allows the app to authenticate using the flows API without needing to handle HTTP redirections. When authentication is complete, the app receives the auth code, access token, or ID token in a JSON response instead of a redirect.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-browserless-and-mfa-only-flows
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-browserless-and-mfa-only-flows.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  preqrequisites: Preqrequisites
  non-redirect-mfa-flow-example: Non-redirect MFA flow example
  example-request: Example Request
  example-response: Example Response
---

# Authorize (Non-redirect and MFA Only Flows)

##

```none
GET {{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}
```

For browerless use cases such as native mobile apps where the app wants to render the end user interface, setting the `response_mode` property to `pi.flow` allows the app to authenticate using the flows API without needing to handle HTTP redirections. When authentication is complete, the app receives the auth code, access token, or ID token in a JSON response instead of a redirect.

The `response_mode` property is the mechanism for returning authorization response parameters from the authorization endpoint. Options are `query`, `fragment`, `form_post`, and `pi.flow`. The `pi.flow` option is a Ping Identity custom response mode to specify that the `redirect_uri` parameter is not required and authorization response parameters are encoded as a JSON object wrapped in a flow response and returned directly to the client with a `200` status. For more information about the `query`, `fragment`, and `form_post` options, refer to the [ResponseModes](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html#ResponseModes) section of the *OAuth 2.0 Multiple Response Type Encoding Practices* specification. For non-redirect use case information, refer to [Redirect and non-redirect authentication flows](../auth-config-options/browserless-authentication-flow-options.html).

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For additional non-redirect use case information, refer to [Redirect and non-redirect authentication flows](../auth-config-options/browserless-authentication-flow-options.html). |

The sample shows the `GET /{{envID}}/as/authorize` operation, which includes the `response_mode` parameter to designate one of the following special authentication flow options:

* A non-redirect flow for mobile clients that implements custom flow interfaces with PingOne platform flow APIs but with native application interface components.

* An integration of PingOne authentication APIs and PingFederate (backend only integration). PingFederate's authentication policy and HTML form adapter handles the initial authentication, and PingOne supplies the multi-factor authentication by providing a `login_hint_token` in the authorization request.

* An MFA only flow where PingFederate performs the initial authentication, and sends the authenticated user to PingOne to complete the MFA workflow. PingFederate returns the `login_hint_token` in a My Account application link to PingOne. The application uses this link to redirect to My Account in PingOne for multi-factor authentication.

  |   |                                                                                                                                                                                                                                                                                                                                                             |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In this case, from a PingOne perspective, PingFederate and the application accessing My Account in PingOne will use different user sessions. This means that any user session context (such as, last MFA time) will not be shared between PingFederate and PingOne. So, the application accessing My Account, and the end user may need to re-authenticate. |

### Preqrequisites

* To build the `login_hint_token` JWT, refer to [Create a login\_hint\_token JWT](../auth-config-options/create-a-login_hint_token-jwt.html).

* To build the `request` JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html).

> **Collapse: Query parameters**
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |

### Non-redirect MFA flow example

Using both the `login_hint_token` and `request` properties, you can set up a non-redirect MFA flow that can evaluate a user's IP address to determine whether an MFA action is required. In this use case, the authorize request looks like this:

```none
https://auth.pingone.com/{{envID}}/as/authorize?acr_values=MFA-Only&response_type=token id_token&client_id={{clientID}}&response_mode=pi.flow&scope=openid profile email&state={{state}}&login_hint_token={{loginHintTokenJWT}}&request={{requestJWT}}
```

The `acr_values` property identifies an MFA sign-on policy name that includes the appropriate IP-based rules.

The `login_hint_token` property value is a JWT that includes the following claims:

```none
{
"iss": "{{issuerApplicationID}}",
"aud": "https://auth.pingone.com/{{envID}}/as",
"sub": "{{authenticatedUserID}}"
}
```

The `request` property value is a JWT that includes the following claims:

```none
{
"iss": "{{issuerApplicationID}}",
"aud": "https://auth.pingone.com/{{envID}}/as",
"pi.remoteIp": "{{ipAddress}}"
}
```

The `request` token passes in the user's IP address securely.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For details on how to construct the `request` property JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
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

  url := "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
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
GET /{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}} HTTP/1.1
Host: {{authPath}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
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

url = URI("{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid%20profile%20email&login_hint_token={{loginHintJwt}}&client_id={{clientID}}")!,timeoutInterval: Double.infinity)
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
        "otp.check": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03101bf2-7eed-41ca-a326-1f47061eb434"
        },
        "device.select": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03101bf2-7eed-41ca-a326-1f47061eb434"
        },
        "self": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03101bf2-7eed-41ca-a326-1f47061eb434"
        },
        "signOnPage": {
            "href": "https://apps.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/signon/?flowId=03101bf2-7eed-41ca-a326-1f47061eb434"
        }
    },
    "_embedded": {
        "devices": [
            {
                "id": "3d9dd925-6aef-4267-a9f6-2e7824c18d33",
                "type": "SMS",
                "status": "ACTIVE",
                "userRetries": 0,
                "phone": "*******01"
            }
        ],
        "application": {
            "name": "WebAppWithMFA_1626821450"
        }
    },
    "id": "03101bf2-7eed-41ca-a326-1f47061eb434",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=03101bf2-7eed-41ca-a326-1f47061eb434",
    "status": "OTP_REQUIRED",
    "createdAt": "2021-07-20T22:51:31.743Z",
    "expiresAt": "2021-07-20T23:06:32.005Z",
    "bypassAllowed": false,
    "selectedDevice": {
        "id": "3d9dd925-6aef-4267-a9f6-2e7824c18d33"
    }
}
```

---

---
title: Authorize (Transaction Approval)
description: PingOne supports transaction approval when strong authentication is required for elevated security for a high-value transaction, or high-risk resource or service. The sample shows the GET /{{envID}}/as/authorize operation, which includes the response_mode and request parameters in the authorization request.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-transaction-approval-
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-transaction-approval-.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example-request: Example Request
  example-response: Example Response
---

# Authorize (Transaction Approval)

##

```none
GET {{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}
```

PingOne supports transaction approval when strong authentication is required for elevated security for a high-value transaction, or high-risk resource or service. The sample shows the `GET /{{envID}}/as/authorize` operation, which includes the `response_mode` and `request` parameters in the authorization request.

The `response_mode` property is the mechanism for returning authorization response parameters from the authorization endpoint. Options are `query`, `fragment`, `form_post`, and `pi.flow`. The `pi.flow` option is a Ping Identity custom response mode to specify that the `redirect_uri` parameter is not required and authorization response parameters are encoded as a JSON object wrapped in a flow response and returned directly to the client with a `200` status. For more information about the `query`, `fragment`, and `form_post` options, refer to the [ResponseModes](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html#ResponseModes) section of the *OAuth 2.0 Multiple Response Type Encoding Practices* specification. For non-redirect use case information, refer to [Redirect and non-redirect authentication flows](../auth-config-options/browserless-authentication-flow-options.html).

The `request` property contains request parameters from the application. If the application's `supportUnsignedRequestObject` property value is set to `false`, the JWT must be signed using the `HS256` algorithm and the app's client secret as the key. Using a JWT enables integrity protection of parameters that are required for risk based authentication or privacy and consent use cases.

The `request` property JWT should be constructed according to the following example:

```none
JWT: "header" :
{
  "alg": "HS256",
  "typ": "JWT"
},
"body" :
{
  "aud": "https://auth.pingone.com/{{envID}}/as",
  "iss": "{{appID}}",
  "pi.template": {
    "name": "{{templateName}}",
    "variant": "{{variantName}}",
    "variables": {
      "key1": "value1"
    }
  },
  "pi.clientContext": {
    "key2": "value2"
  }
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `request` property specifies a JWT that enables OIDC/OAuth2 request parameters to be passed as a single, self-contained parameter. Using a JWT enables integrity protection of parameters that are required for risk-based authentication or privacy and consent use cases. Specifically, (1) passing in the user agent's original IP address when the PingOne platform is used behind a server side application that is functioning as an authentication gateway or PingFederate, and (2) passing in a purpose or usage description string that could be displayed to the user on the authentication UI prompt, SMS or voice message, push notification, or email message. For details on how to construct the JWT, refer to [Create a request property JWT](../auth-config-options/create-a-request-property-jwt.html). For information on `pi.template` refer to [Notifications Templates](../../platform/notifications/notifications-templates.html). For information on `pi.clientContext` refer to [Device Authentication](../../mfa/mfa-authentication/mfa-device-authentications.html). |

> **Collapse: Query parameters**
>
> | Property                | Type   | Required |
> | ----------------------- | ------ | -------- |
> | `acr_values`            | String | Optional |
> | `client_id`             | String | Required |
> | `code_challenge_method` | String | Optional |
> | `login_hint`            | String | Optional |
> | `login_hint_token`      | String | Optional |
> | `mobilePayload`         | String | Optional |
> | `max_age`               | String | Optional |
> | `nonce`                 | String | Optional |
> | `prompt`                | String | Optional |
> | `redirect_uri`          | String | Required |
> | `request`               | String | Optional |
> | `response_mode`         | String | Optional |
> | `response_type`         | String | Required |
> | `scope`                 | String | Optional |
> | `state`                 | String | Optional |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
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

  url := "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
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
GET /{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}} HTTP/1.1
Host: {{authPath}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': '{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
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

url = URI("{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize?state={{state}}&response_type=token%20id_token&response_mode=pi.flow&scope=openid&request={{requestString}}&client_id={{clientID}}")!,timeoutInterval: Double.infinity)
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
        "otp.check": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/0392192e-8616-4d70-af9d-10631b3fd2ca"
        },
        "device.select": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/0392192e-8616-4d70-af9d-10631b3fd2ca"
        },
        "self": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/0392192e-8616-4d70-af9d-10631b3fd2ca"
        },
        "signOnPage": {
            "href": "https://apps.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/signon/?flowId=0392192e-8616-4d70-af9d-10631b3fd2ca"
        }
    },
    "_embedded": {
        "devices": [
            {
                "id": "1237625c-12f9-4ab1-8656-351142b6c100",
                "type": "SMS",
                "status": "ACTIVE",
                "phone": "*******01"
            }
        ],
        "application": {
            "name": "WebAppWithMFA_1628117875"
        }
    },
    "id": "0392192e-8616-4d70-af9d-10631b3fd2ca",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=0392192e-8616-4d70-af9d-10631b3fd2ca",
    "status": "OTP_REQUIRED",
    "createdAt": "2021-08-04T23:00:02.383Z",
    "expiresAt": "2021-08-04T23:15:02.666Z",
    "bypassAllowed": false,
    "selectedDevice": {
        "id": "1237625c-12f9-4ab1-8656-351142b6c100"
    }
}
```

---

---
title: Cancel Authentication Flow
description: This example shows how to cancel an authentication flow that has begun. You can use this in situations where the user wants to authenticate from a different device. Note that this feature requires version 2.0 or higher of the PingOne MFA SDK.
component: pingone-api
page_id: pingone-api:auth:flows/flows-1/cancel_authentication
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/flows-1/cancel_authentication.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
---

# Cancel Authentication Flow

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

This example shows how to cancel an authentication flow that has begun. You can use this in situations where the user wants to authenticate from a different device. Note that this feature requires version 2.0 or higher of the PingOne MFA SDK.

The ID of the flow is included in the URL: `{{authPath}}/{{envID}}/flows/{{flowID}}`

The value of the Content-Type header must be set to: `application/vnd.pingidentity.cancel.push.authentication+json`

The body consists of a single field, `reason`, which is set to CHANGE\_DEVICE.

> **Collapse: Request Model**
>
> | Property | Type   | Required |
> | -------- | ------ | -------- |
> | `reason` | String | Required |

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
curl --location --globoff '{{authPath}}/{{envID}}/flows/{{flowID}}' \
--header 'Content-Type: application/vnd.pingidentity.cancel.push.authentication+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "reason": "CHANGE_DEVICE"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/flows/{{flowID}}")
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

  url := "{{authPath}}/{{envID}}/flows/{{flowID}}"
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
POST /{{envID}}/flows/{{flowID}} HTTP/1.1
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
  .url("{{authPath}}/{{envID}}/flows/{{flowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.cancel.push.authentication+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/flows/{{flowID}}",
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
  'url': '{{authPath}}/{{envID}}/flows/{{flowID}}',
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

url = "{{authPath}}/{{envID}}/flows/{{flowID}}"

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
$request->setUrl('{{authPath}}/{{envID}}/flows/{{flowID}}');
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

url = URI("{{authPath}}/{{envID}}/flows/{{flowID}}")

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

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/flows/{{flowID}}")!,timeoutInterval: Double.infinity)
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

---

---
title: Check Assertion
description: The multi-factor authentication flow for a FIDO device checks the authenticator assertion response, which contains the signed challenge needed to complete the MFA flow. The MFA actions service validates the challenge.
component: pingone-api
page_id: pingone-api:auth:flows/flows-1/check-assertion
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/flows-1/check-assertion.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
---

# Check Assertion

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

The multi-factor authentication flow for a FIDO device checks the authenticator assertion response, which contains the signed challenge needed to complete the MFA flow. The MFA actions service validates the challenge.

### Prerequisites

* Refer to [Flows](../flows-1.html) for important overview information.

* Send an authorize request to get a flow ID: [Authorize](../../openid-connect-oauth-2/authorize-intro.html). Refer also to [Login action authentication flow](../../../foundations/authentication-concepts/pingone-authentication-flow-states/login-action.html) and [Authorization and authentication](../../../foundations/authentication-concepts.html).

* Start the flow: [Read Flow](read-flow.html).

* Refer also to the `ASSERTION_REQUIRED` flow state in the [Flow status values table](../flows-1.html).

* Refer also to [FIDO Policies](../../../mfa/fido-policies.html).

|   |                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `ASSERTION_REQUIRED` flow state includes the `publicKeyCredentialRequestOptions` response property that specifies the public key credential request options object generated for the selected device that is used to call the `navigator.credentials.get()` on the browser to generate the assertion. |

The following sample shows the `POST /{{envID}}/flows/{{flowID}}` operation to validate the assertion used in the multi-factor authentication flow. This operation uses the `application/vnd.pingidentity.assertion.check+json` custom media type as the content type in the request header.

If completed successfully, and if this action is the last action of the authentication flow, the `status` property shows a value of `COMPLETED`.

> **Collapse: Request Model**
>
> | Property        | Type   | Required |
> | --------------- | ------ | -------- |
> | `assertion`     | String | Required |
> | `compatibility` | String | Optional |
> | `origin`        | String | Required |

### Headers

Content-Type      application/vnd.pingidentity.assertion.check+json

### Body

raw ( application/vnd.pingidentity.assertion.check+json )

```json
{
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility": "FULL"
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
--header 'Content-Type: application/vnd.pingidentity.assertion.check+json' \
--data '{
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility": "FULL"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/flows/{{flowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.assertion.check+json");
var body = @"{" + "\n" +
@"    ""origin"": ""https://app.pingone.com""," + "\n" +
@"    ""assertion"": ""{{assertionFromBrowser}}""," + "\n" +
@"    ""compatibility"": ""FULL""" + "\n" +
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
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility": "FULL"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.assertion.check+json")

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
Content-Type: application/vnd.pingidentity.assertion.check+json

{
    "origin": "https://app.pingone.com",
    "assertion": "{{assertionFromBrowser}}",
    "compatibility": "FULL"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.assertion.check+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"origin\": \"https://app.pingone.com\",\n    \"assertion\": \"{{assertionFromBrowser}}\",\n    \"compatibility\": \"FULL\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/flows/{{flowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.assertion.check+json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/flows/{{flowID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.assertion.check+json"
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
  'url': '{{authPath}}/{{envID}}/flows/{{flowID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.assertion.check+json'
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

url = "{{authPath}}/{{envID}}/flows/{{flowID}}"

payload = json.dumps({
  "origin": "https://app.pingone.com",
  "assertion": "{{assertionFromBrowser}}",
  "compatibility": "FULL"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.assertion.check+json'
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
  'Content-Type' => 'application/vnd.pingidentity.assertion.check+json'
));
$request->setBody('{\n    "origin": "https://app.pingone.com",\n    "assertion": "{{assertionFromBrowser}}",\n    "compatibility": "FULL"\n}');
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
request["Content-Type"] = "application/vnd.pingidentity.assertion.check+json"
request.body = JSON.dump({
  "origin": "https://app.pingone.com",
  "assertion": "{{assertionFromBrowser}}",
  "compatibility": "FULL"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"origin\": \"https://app.pingone.com\",\n    \"assertion\": \"{{assertionFromBrowser}}\",\n    \"compatibility\": \"FULL\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/flows/{{flowID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.assertion.check+json", forHTTPHeaderField: "Content-Type")

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
title: Check One-Time Password (OTP)
description: The multi-factor authentication flow uses a one-time password (OTP) sent to the user's device to continue the login flow. The user receives the OTP and submits it as a step in the login process. The MFA actions service validates the OTP to complete the authentication flow.
component: pingone-api
page_id: pingone-api:auth:flows/flows-1/check-one-time-password-otp
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/flows-1/check-one-time-password-otp.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Check One-Time Password (OTP)

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

The multi-factor authentication flow uses a one-time password (OTP) sent to the user's device to continue the login flow. The user receives the OTP and submits it as a step in the login process. The MFA actions service validates the OTP to complete the authentication flow.

The following sample shows the `POST /{{envID}}/flows/{{flowID}}` operation to validate the OTP used in the multi-factor authentication flow. This operation uses the `application/vnd.pingidentity.otp.check+json` custom media type as the content type in the request header.

### Prerequisites

* Refer to [Flows](../flows-1.html) for important overview information.

* Send an authorize request to get a flow ID: [Authorize](../../openid-connect-oauth-2/authorize-intro.html). Refer also to [Login action authentication flow](../../../foundations/authentication-concepts/pingone-authentication-flow-states/login-action.html) and [Authorization and authentication](../../../foundations/authentication-concepts.html).

* Start the flow: [Read Flow](read-flow.html).

* Refer also to the `OTP_REQUIRED` flow state in the [Flow status values table](../flows-1.html).

If completed successfully, and if this action is the last action of the authentication flow, the `status` property shows a value of `COMPLETED`.

> **Collapse: Request Model**
>
> | Property | Type   | Required |
> | -------- | ------ | -------- |
> | `otp`    | String | Required |

### Headers

Content-Type      application/vnd.pingidentity.otp.check+json

### Body

raw ( application/vnd.pingidentity.otp.check+json )

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
curl --location --globoff '{{authPath}}/{{envID}}/flows/{{flowID}}' \
--header 'Content-Type: application/vnd.pingidentity.otp.check+json' \
--data '{
    "otp": "xxxxxx"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/flows/{{flowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.otp.check+json");
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

  url := "{{authPath}}/{{envID}}/flows/{{flowID}}"
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
  req.Header.Add("Content-Type", "application/vnd.pingidentity.otp.check+json")

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
Content-Type: application/vnd.pingidentity.otp.check+json

{
    "otp": "xxxxxx"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.otp.check+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"otp\": \"xxxxxx\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/flows/{{flowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.otp.check+json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/flows/{{flowID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.otp.check+json"
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
  'url': '{{authPath}}/{{envID}}/flows/{{flowID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.otp.check+json'
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

url = "{{authPath}}/{{envID}}/flows/{{flowID}}"

payload = json.dumps({
  "otp": "xxxxxx"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.otp.check+json'
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
  'Content-Type' => 'application/vnd.pingidentity.otp.check+json'
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

url = URI("{{authPath}}/{{envID}}/flows/{{flowID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.otp.check+json"
request.body = JSON.dump({
  "otp": "xxxxxx"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"otp\": \"xxxxxx\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/flows/{{flowID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.otp.check+json", forHTTPHeaderField: "Content-Type")

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
      "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/d8bbb008-dc4d-469e-819f-e12a350f51c2"
    },
    "id": "7b37d3e8-38b0-4469-b553-04b8bee08e6f",
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=d8bbb008-dc4d-469e-819f-e12a350f51c2",
    "status": "COMPLETED",
    "createdAt": "2018-09-20T13:40:56.977Z",
    "expiresAt": "2018-09-20T13:56:12.306Z",
    "_embedded": {
      "user": {
        "id": "482a626f-a894-485d-b9f3-ba8f4ed0c58d",
        "username": "johndoe",
        "name": {
          "given": "John",
          "family": "Doe"
        }
      }
    }
  }
}
```

---

---
title: Check Username/Password
description: The POST /{{envID}}/flows/{{flowID}} operation initiates an action to allow users to login with a username and password. The request body requires the username and password attributes. The values for these properties provided by the user are verified in this action. This operation uses the application/vnd.pingidentity.usernamePassword.check+json custom media type as the content type in the request header.
component: pingone-api
page_id: pingone-api:auth:flows/flows-1/check-username-password
canonical_url: https://developer.pingidentity.com/pingone-api/auth/flows/flows-1/check-username-password.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Check Username/Password

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

The `POST /{{envID}}/flows/{{flowID}}` operation initiates an action to allow users to login with a username and password. The request body requires the `username` and `password` attributes. The values for these properties provided by the user are verified in this action. This operation uses the `application/vnd.pingidentity.usernamePassword.check+json` custom media type as the content type in the request header.

### Prerequisites

* Refer to [Flows](../flows-1.html) for important overview information.

* Send an authorize request to get a flow ID: [Authorize](../../openid-connect-oauth-2/authorize-intro.html). Refer also to [Login action authentication flow](../../../foundations/authentication-concepts/pingone-authentication-flow-states/login-action.html) and [Authorization and authentication](../../../foundations/authentication-concepts.html).

* Start the flow: [Read Flow](read-flow.html).

* Refer also to the `USERNAME_PASSWORD_REQUIRED` and `ACCOUNT_LINKING_REQUIRED` flow states in the [Flow status values table](../flows-1.html).

If there is a user already associated with the current flow, and a `username` value is provided in the request body, then the value of `username` must identify the user associated with the session.

In the response data, the `status` property value indicates that the one-time password validation step used in a multi-factor authentication flow is a required action. The `validateOTP` link to initiate this required step is also included in the response.

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This action is also used with the `ACCOUNT_LINKING_REQUIRED` status. When linking to an existing user, the `usernamePassword.check` action is required. |

> **Collapse: Request Model**
>
> | Property   | Type   | Required |
> | ---------- | ------ | -------- |
> | `username` | String | Required |
> | `password` | String | Required |

### Headers

Content-Type      application/vnd.pingidentity.usernamePassword.check+json

### Body

raw ( application/vnd.pingidentity.usernamePassword.check+json )

```json
{
    "username": "{{email}}",
    "password": "{{userPassword}}"
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
--header 'Content-Type: application/vnd.pingidentity.usernamePassword.check+json' \
--data '{
    "username": "{{email}}",
    "password": "{{userPassword}}"
}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/flows/{{flowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.usernamePassword.check+json");
var body = @"{" + "\n" +
@"    ""username"": ""{{email}}""," + "\n" +
@"    ""password"": ""{{userPassword}}""" + "\n" +
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
    "username": "{{email}}",
    "password": "{{userPassword}}"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.usernamePassword.check+json")

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
Content-Type: application/vnd.pingidentity.usernamePassword.check+json

{
    "username": "{{email}}",
    "password": "{{userPassword}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.usernamePassword.check+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"username\": \"{{email}}\",\n    \"password\": \"{{userPassword}}\"\n}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/flows/{{flowID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.usernamePassword.check+json")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/flows/{{flowID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.usernamePassword.check+json"
  },
  "data": JSON.stringify({
    "username": "{{email}}",
    "password": "{{userPassword}}"
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
    'Content-Type': 'application/vnd.pingidentity.usernamePassword.check+json'
  },
  body: JSON.stringify({
    "username": "{{email}}",
    "password": "{{userPassword}}"
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
  "username": "{{email}}",
  "password": "{{userPassword}}"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.usernamePassword.check+json'
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
  'Content-Type' => 'application/vnd.pingidentity.usernamePassword.check+json'
));
$request->setBody('{\n    "username": "{{email}}",\n    "password": "{{userPassword}}"\n}');
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
request["Content-Type"] = "application/vnd.pingidentity.usernamePassword.check+json"
request.body = JSON.dump({
  "username": "{{email}}",
  "password": "{{userPassword}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"username\": \"{{email}}\",\n    \"password\": \"{{userPassword}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/flows/{{flowID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.usernamePassword.check+json", forHTTPHeaderField: "Content-Type")

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
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03e52d0a-c55a-4807-889b-cd14f74ec4c5"
        }
    },
    "id": "03e52d0a-c55a-4807-889b-cd14f74ec4c5",
    "session": {
        "id": "5655baab-c282-4f9d-8d01-b635fe66b528"
    },
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=03e52d0a-c55a-4807-889b-cd14f74ec4c5",
    "status": "COMPLETED",
    "createdAt": "2021-07-23T16:19:34.570Z",
    "expiresAt": "2021-07-23T16:34:53.196Z",
    "_embedded": {
        "user": {
            "id": "831441df-b71f-473c-8871-c0af518ad851",
            "username": "app_user_1627057164",
            "name": {
                "given": "Test",
                "family": "ApplicationUser"
            }
        },
        "application": {
            "name": "Single-Page-App_1627057132"
        }
    }
}
```

---

---
title: CIBA Authorize
description: The CIBA grant type uses its own authorize endpoint, POST /{{envID}}/as/cibaAuthorization, unlike other grant types. This endpoint returns an auth_req_id value that the relying party (RP) then passes to the token endpoint to obtain an access token and ID token.
component: pingone-api
page_id: pingone-api:auth:openid-connect-oauth-2/authorize-ciba
canonical_url: https://developer.pingidentity.com/pingone-api/auth/openid-connect-oauth-2/authorize-ciba.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# CIBA Authorize

##

```none
POST {{authPath}}/{{envID}}/as/cibaAuthorization
```

The CIBA grant type uses its own authorize endpoint, `POST /{{envID}}/as/cibaAuthorization`, unlike other grant types. This endpoint returns an `auth_req_id` value that the relying party (RP) then passes to the token endpoint to obtain an access token and ID token.

The request must include a value for either `login_hint`, `id_token_hint`, or `login_hint_token`. Providing more than one of these properties will result in an error. Learn more in [Create a login\_hint\_token JWT](../auth-config-options/create-a-login_hint_token-jwt.html).

The application's configured `tokenEndpointAuthMethod` value determines how you authenticate. This must be either `CLIENT_SECRET_BASIC`, `CLIENT_SECRET_JWT`, `PRIVATE_KEY_JWT`, or `CLIENT_SECRET_POST`.

In the sample request shown here, the application's `tokenEndpointAuthMethod` value is `CLIENT_SECRET_BASIC`, which requires the `Authorization: Basic` HTTP header and a Base64-encoded representation of "username:password" in the request, in which the username is the `client_id` and the password is the `client_secret`.

If the application's `tokenEndpointAuthMethod` value is `CLIENT_SECRET_JWT`, the endpoint accepts a JWT signed by the application's client secret to authenticate the request. Learn more about creating the JWT and the claims in the JWT in [Create a client secret JWT](../auth-config-options/create-a-client-secret-jwt.html). This request requires the `client_assertion` and `client_assertion_type` properties to specify the JWT:

```
curl --location --request POST '{{authPath}}/{{envID}}/as/cibaAuthorization' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_assertion={{clientSecretJWT}}' \
--data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
--data-urlencode 'login_hint={{cibaHint}}' \
--data-urlencode 'scope=openid'
```

If the application's `tokenEndpointAuthMethod` value is `PRIVATE_KEY_JWT`, the endpoint accepts a JWT signed by an external private key file to authenticate the request. Learn more about creating the JWT and the claims in the JWT in [Create a private key JWT](../auth-config-options/create-a-private-key-jwt.html). This request requires the `client_assertion` and `client_assertion_type` properties to specify the JWT:

```
curl --location --request POST '{{authPath}}/{{envID}}/as/cibaAuthorization' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_assertion={{privateKeyJWT}}' \
--data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
--data-urlencode 'login_hint={{cibaHint}}' \
--data-urlencode 'scope=openid'
```

If the application's `tokenEndpointAuthMethod` value is `CLIENT_SECRET_POST`, the request does not require an Authorization header, and the `client_id` and `client_secret` properties are sent in the request body:

```
curl --location --request POST '{{authPath}}/{{envID}}/as/cibaAuthorization' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{appID}}' \
--data-urlencode 'client_secret={{appSecret}}'\
--data-urlencode 'login_hint={{cibaHint}}' \
--data-urlencode 'scope=openid'
```

### Prerequisites

* Refer to [OpenID Connect/OAuth 2](../openid-connect-oauth-2.html), [Authorization](authorize-intro.html), and [CIBA grant type](../../foundations/authentication-concepts/authorization-flow-by-grant-type/ciba-grant-type.html) for overview information.

* Refer to [Create a login\_hint\_token JWT](../auth-config-options/create-a-login_hint_token-jwt.html) for information about creating a `login_hint_token`.

> **Collapse: Request Model**
>
> | Property           | Type   | Required |
> | ------------------ | ------ | -------- |
> | `login_hint`       | String | Optional |
> | `id_token_hint`    | String | Optional |
> | `login_hint_token` | String | Optional |
> | `scope`            | String | Required |
>
> Refer to the [OpenID Connect/OAuth2 data model](../openid-connect-oauth-2.html) for full property descriptions.

### Headers

Authorization

Content-Type      application/x-www-form-urlencoded

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key         | Value        |
| ----------- | ------------ |
| login\_hint | {{cibaHint}} |
| scope       | {{scopeID}}  |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/cibaAuthorization' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0=' \
--data-urlencode 'login_hint={{cibaHint}}' \
--data-urlencode 'scope={{scopeID}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/cibaAuthorization")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddHeader("Authorization", "Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0=");
request.AddParameter("login_hint", "{{cibaHint}}");
request.AddParameter("scope", "{{scopeID}}");
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

  url := "{{authPath}}/{{envID}}/as/cibaAuthorization"
  method := "POST"

  payload := strings.NewReader("login_hint=%7B%7BcibaHint%7D%7D&scope=%7B%7BscopeID%7D%7D")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
  req.Header.Add("Authorization", "Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0=")

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
POST /{{envID}}/as/cibaAuthorization HTTP/1.1
Host: {{authPath}}
Content-Type: application/x-www-form-urlencoded
Authorization: Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0=

login_hint=%7B%7BcibaHint%7D%7D&scope=%7B%7BscopeID%7D%7D
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "login_hint={{cibaHint}}&scope={{scopeID}}");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/cibaAuthorization")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .addHeader("Authorization", "Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0=")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/cibaAuthorization",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0="
  },
  "data": {
    "login_hint": "{{cibaHint}}",
    "scope": "{{scopeID}}"
  }
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{authPath}}/{{envID}}/as/cibaAuthorization',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0='
  },
  form: {
    'login_hint': '{{cibaHint}}',
    'scope': '{{scopeID}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/cibaAuthorization"

payload = 'login_hint=%7B%7BcibaHint%7D%7D&scope=%7B%7BscopeID%7D%7D'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/cibaAuthorization');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Authorization' => 'Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0='
));
$request->addPostParameter(array(
  'login_hint' => '{{cibaHint}}',
  'scope' => '{{scopeID}}'
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

url = URI("{{authPath}}/{{envID}}/as/cibaAuthorization")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request["Authorization"] = "Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0="
request.body = "login_hint=%7B%7BcibaHint%7D%7D&scope=%7B%7BscopeID%7D%7D"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "login_hint=%7B%7BcibaHint%7D%7D&scope=%7B%7BscopeID%7D%7D"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/cibaAuthorization")!,timeoutInterval: Double.infinity)
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3thcHBJRH19Ont7YXBwU2VjcmV0fX0=", forHTTPHeaderField: "Authorization")

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
  "auth_req_id": "1c266114-a1be-4700-8ad1-04986c5b9ac1",
  "expires_in": 120,
  "interval": 2
}
```
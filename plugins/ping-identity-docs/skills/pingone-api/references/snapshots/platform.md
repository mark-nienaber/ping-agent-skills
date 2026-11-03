---
title: Accept Agreement
description: Accept a terms of service agreement on behalf of a PingOne user for a specified language and revision
component: pingone-api
page_id: pingone-api:platform:users/user-agreement-consents/accept-agreement
canonical_url: https://developer.pingidentity.com/pingone-api/platform/users/user-agreement-consents/accept-agreement.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-05-29
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
---

# Accept Agreement

##

Required permission:

* [agreements:create:userConsent](../../reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-agreements-create-userConsent "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}
```

The `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/agreementConsents/{{agreementID}}` operation gives the actor the ability to accept an agreement for the specified user. This operation uses the `application/vnd.pingidentity.consent.accept+json` custom content type in the request header.

The request body specifies the language ID and the revision ID associated with the agreement ID specified in the request URL. The request also supports the `consentedAt` property to designate the timestamp to set for the time of consent. If this property is not provided, a value of `Date.now` is used by default.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For information about importing external consents into PingOne, refer to [Migrate Existing External Agreement Consents to PingOne](../../agreement-management/migrate-existing-external-agreement-consents-to-pingone.html). |

### Prerequisites

* Refer to [User Operations](../users-1/index.html) for important overview information.

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
> Refer to the [User agreement consents data model](index.html#user-agreement-consents-data-model) for full property descriptions.

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

---

---
title: Activate Trusted Email Address
description: Activate a new trusted email address for a trusted email domain using the verification code sent to that address
component: pingone-api
page_id: pingone-api:platform:notifications/trusted-email-addresses/activate-trusted-email-address
canonical_url: https://developer.pingidentity.com/pingone-api/platform/notifications/trusted-email-addresses/activate-trusted-email-address.html
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

# Activate Trusted Email Address

##

Required permission:

* [notifications:create:emailDomain](../../reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-notifications-create-emailDomain "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}
```

The `POST {{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}` operation is used to activate a new trusted email address resource of the trusted email domain in the specified environment. This operation uses the `application/vnd.pingidentity.trustedEmail.activate+json` custom media type as the content type in the request header.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | The email address can be activated in the 24-hour period after the verification code has been sent. |

### Prerequisites

* [Create a trusted email domain](../trusted-email-domains/create-trusted-email-domain.html) to get an `emailDomainID` for the endpoint. Refer also to [Notifications](../index.html), especially [Trusted Email Domains](../trusted-email-domains/index.html).

* [Create a trusted email address](create-trusted-email-address.html) to get a `trustedEmailID` for the endpoint. Refer also to [Notifications](../index.html), especially [Trusted Email Addresses](index.html).

> **Collapse: Request Model**
>
> | Property           | Type   | Required |
> | ------------------ | ------ | -------- |
> | `verificationCode` | String | Required |
>
> Refer to the [Trusted email domains data models](../trusted-email-domains/index.html) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.trustedEmail.activate+json

### Body

raw ( application/vnd.pingidentity.trustedEmail.activate+json )

```json
{
   "verificationCode":"avu0w4lt"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}' \
--header 'Content-Type: application/vnd.pingidentity.trustedEmail.activate+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
   "verificationCode":"avu0w4lt"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.trustedEmail.activate+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{  " + "\n" +
@"   ""verificationCode"":""avu0w4lt""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}"
  method := "POST"

  payload := strings.NewReader(`{
   "verificationCode":"avu0w4lt"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.trustedEmail.activate+json")
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
POST /v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.trustedEmail.activate+json
Authorization: Bearer {{accessToken}}

{
   "verificationCode":"avu0w4lt"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.trustedEmail.activate+json");
RequestBody body = RequestBody.create(mediaType, "{  \n   \"verificationCode\":\"avu0w4lt\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.trustedEmail.activate+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.trustedEmail.activate+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "verificationCode": "avu0w4lt"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.trustedEmail.activate+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "verificationCode": "avu0w4lt"
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

url = "{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}"

payload = json.dumps({
  "verificationCode": "avu0w4lt"
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.trustedEmail.activate+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.trustedEmail.activate+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{  \n   "verificationCode":"avu0w4lt"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.trustedEmail.activate+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "verificationCode": "avu0w4lt"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{  \n   \"verificationCode\":\"avu0w4lt\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/emailDomains/{{emailDomainID}}/trustedEmails/{{trustedEmailID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.trustedEmail.activate+json", forHTTPHeaderField: "Content-Type")
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/emailDomains/abe400ab-674d-42ac-9a70-7c911d7bcace/trustedEmails/17665a60-9fc5-40c2-90e3-91494bbe38be"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "emailDomain": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/emailDomains/abe400ab-674d-42ac-9a70-7c911d7bcace"
        }
    },
    "id": "17665a60-9fc5-40c2-90e3-91494bbe38be",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "domain": {
        "id": "abe400ab-674d-42ac-9a70-7c911d7bcace"
    },
    "emailAddress": "noreply1@auth.shopco.com",
    "status": "ACTIVE",
    "createdAt": "2020-06-21T14:33:47.511Z",
    "updatedAt": "2020-06-21T14:33:47.511Z",
    "domainId": "abe400ab-674d-42ac-9a70-7c911d7bcace"
}
```

---

---
title: Active Identity Counts
description: Explains PingOne active identity counts, which track identities that successfully authenticate or complete a password check in a given period
component: pingone-api
page_id: pingone-api:platform:active-identity-counts/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/active-identity-counts/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  active-identity-count-errors: Active identity count errors
---

# Active Identity Counts

Active identity counts gather information about identities that have completed one of the following actions successfully during a specified period of time:

* **Authentication**

  The identity has completed at least one authentication flow successfully.

* **Password check**

  The identity has completed at least one [Password Check](../users/user-passwords/password-check.html) successfully.

This service uses authentication and password-evaluation user events to determine whether an identity is active within a specified sampling period.

|   |                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Currently, the active identity count does not return product-specific counts (such as, for PingOne SSO, MFA, or Protect), nor does it count active users when DaVinci is used. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../group-role-assignments/index.html).

* [User Role Assignments](../users/user-role-assignments/index.html).

Refer to [Roles Management](../roles/index.html) for more information.

## Active identity count errors

In addition to the general [error codes](../reference/error-codes.html), active identity count operations can return the following errors:

| HTTP status | Top‑level code     | Detail code | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400         | `INVALID_REQUEST`  | None        | **Message:** `Parameter startDate can't be null or empty.` or `Invalid cursor request parameter`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts request omits the `startDate` filter or specifies an invalid cursor.
>
> **Details:** None.                                                                                                                                                                              |
| 400         | `INVALID_REQUEST`  | None        | **Message:** `Filter parameter startDate can't be in the future.`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts request specifies a `startDate` filter that is later than the current date.
>
> **Details:** None.                                                                                                                                                                                                      |
| 400         | `INVALID_REQUEST`  | None        | **Message:** `Filter parameter startDate can't be earlier than 2 years ago.`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts request specifies a `startDate` filter that is more than 2 years earlier than the current date.
>
> **Details:** None.                                                                                                                                                                       |
| 400         | `INVALID_REQUEST`  | None        | **Message:** `Wrong date time format in filter parameter - startDate. Correct date pattern is yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts request specifies a `startDate` filter value that is not a valid date and time in `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'` format.
>
> **Details:** None.                                                                                               |
| 400         | `INVALID_DATA`     | None        | **Message:** `<samplePeriod> is not a valid samplePeriod. Use one of [DAY, MONTH]`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts request specifies a `samplePeriod` value that is not `DAY` or `MONTH`.
>
> **Details:** None.                                                                                                                                                                                          |
| 400         | `INVALID_REQUEST`  | None        | **Message:** `Limit parameter should be in range (1 - 730) for DAY sample period parameter and (1 - 24) for MONTH`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts request specifies a `limit` value outside the range allowed for the sample period (1-730 for `DAY`, 1-24 for `MONTH`).
>
> **Details:** None.                                                                                                          |
| 400         | `INVALID_REQUEST`  | None        | **Message:** `aggregatedBy request parameter must be specified. Available values: licenseYear, calendarMonth` or `limit parameter must be in range from 1 to 1000`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts by license request omits the `aggregatedBy` parameter or specifies a value that is not `licenseYear` or `calendarMonth`, or specifies a `limit` value outside the range 1-1000.
>
> **Details:** None. |
| 400         | `INVALID_DATA`     | None        | **Message:** The message text varies with the filter evaluation error.> **Collapse: When and details**
>
> **When:** A `GET` active identity counts request specifies a filter value that the service cannot evaluate (for example, a malformed `startDate` filter expression).
>
> **Details:** None.                                                                                                                                                 |
| 403         | `ACCESS_FAILED`    | None        | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `orgmgt:read:environment` permission for the active identity counts by date range operation or lacks the `licensing:read:license` permission for the active identity counts by license operation (`GET` operations).
>
> **Details:** None.                                                            |
| 404         | `NOT_FOUND`        | None        | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `GET` active identity counts by license request specifies a `licenseId` that does not exist or is not associated with the `organizationId` in the request path.
>
> **Details:** None.                                                                                                                        |
| 500         | `UNEXPECTED_ERROR` | None        | **Message:** `Issue with fetching data from data server.`> **Collapse: When and details**
>
> **When:** The service fails to fetch data from the data server.
>
> **Details:** None.                                                                                                                                                                                                                                                                   |

---

---
title: Add User to Group
description: Directly add a PingOne user to a specified group
component: pingone-api
page_id: pingone-api:platform:users/group-membership/add-user-to-group
canonical_url: https://developer.pingidentity.com/pingone-api/platform/users/group-membership/add-user-to-group.html
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

# Add User to Group

##

Required permission:

* [dir:create:groupMembership](../../reference/roles-and-permissions-in-pingone/pingone-permissions-by-identifier.html#permission-dir-create-groupMembership "Learn more about this permission")

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups
```

The `POST {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups` operation directly adds one user to a specified group. The group ID is indicated in the body of the request. For more information on adding users to groups, refer to [Group Membership](index.html).

|   |                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If a user is a member of a group that is added to a population, changing the user's population will remove the user from that group. Additionally, if a user's population changes, they are also removed from any group in this population in which they are a member. |

For more information about groups, refer to [Groups](../../groups/index.html).

Admins cannot add or remove themselves from a a group with admin roles.

### Prerequisites

* Refer to [Users](../index.html) for important overview information.

* Create a user to get a `userID`. Refer to [Create User](../users-1/create-user.html). Run [Read User or Users](../users-1/read-all-users.html) to find an existing user.

* Create a user group to get a `groupID`. Refer to [Create Group](../../groups/create-group.html). Run [Read All Groups](../../groups/read-all-groups.html) to find an existing group.

> **Collapse: Request Model**
>
> | Property | Type   | Required |
> | -------- | ------ | -------- |
> | `id`     | String | Required |
>
> Refer to the [Groups data model](../../groups/index.html#groups-data-model) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "id": "{{groupID}}"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "id": "{{groupID}}"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""id"": ""{{groupID}}""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups"
  method := "POST"

  payload := strings.NewReader(`{
    "id": "{{groupID}}"
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
POST /v1/environments/{{envID}}/users/{{userID}}/memberOfGroups HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "id": "{{groupID}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"id\": \"{{groupID}}\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "id": "{{groupID}}"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "id": "{{groupID}}"
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups"

payload = json.dumps({
  "id": "{{groupID}}"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "id": "{{groupID}}"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "id": "{{groupID}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"id\": \"{{groupID}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/memberOfGroups")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/c98fd0cc-c34b-406a-9e0b-a892edb7a702/memberOfGroups/e947cec5-62c5-4d80-af16-497b29e8a685"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/c98fd0cc-c34b-406a-9e0b-a892edb7a702"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "group": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/groups/e947cec5-62c5-4d80-af16-497b29e8a685"
        }
    },
    "id": "e947cec5-62c5-4d80-af16-497b29e8a685",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Managers",
    "type": "DIRECT"
}
```

---

---
title: Administrator Security
description: Read and update PingOne administrator sign-on security settings, including MFA enforcement, external IdP configuration, and hybrid population-based MFA rules
component: pingone-api
page_id: pingone-api:platform:administrator-security/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/administrator-security/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  administrator-security-data-model: Administrator security data model
  response-codes: Response codes
  administrator-security-errors: Administrator security errors
---

# Administrator Security

Use the administrator security endpoints to read and update environment administrator sign-on settings. By default, MFA is enforced for administrators. You can use the PUT operation to:

* Use an external identity provider or a hybrid configuration by making a request to `PUT {{apiPath}}/v1/environments/{{envID}}/adminConfig` and setting the `authenticationMethod` property.

* Require MFA for all admin sign-ons. In this case, use PingOne as the value of `authenticationMethod`, set the `mfaStatus` value to `ENFORCE`, and the `allowedMethods` to the MFA methods you want to enable.

Refer to [Configuring Administrator Security](https://docs.pingidentity.com/pingone/settings/p1_configure_administrator_security.html) in the PingOne administrator documentation for more information.

|   |                                                         |
| - | ------------------------------------------------------- |
|   | Misconfiguring an external IdP can result in a lockout. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../group-role-assignments/index.html).

* [User Role Assignments](../users/user-role-assignments/index.html).

Refer to [Roles Management](../roles/index.html) for more information.

## Administrator security data model

| Property               | Type    | Required | Mutable   | Description                                                                                                                                                                          |
| ---------------------- | ------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `allowedMethods`       | Object  | Optional | Mutable   | Indicates the methods to enable or disable for admin sign-on. Required properties are `TOTP` (temporary one-time password), `FIDO2`, and `EMAIL`.                                    |
| `allowedMethods.EMAIL` | String  | Required | Mutable   | Indicates whether to enable email for sign-on. Must be set to either `{\"enabled\":true}` or `{\"enabled\":false}`.                                                                  |
| `allowedMethods.FIDO2` | String  | Required | Mutable   | Indicates whether to enable FIDO2 for sign-on. Must be set to either `{\"enabled\":true}` or `{\"enabled\":false}`.                                                                  |
| `allowedMethods.TOTP`  | String  | Required | Mutable   | Indicates whether to enable TOTP for sign-on. Must be set to either `{\"enabled\":true}` or `{\"enabled\":false}`.                                                                   |
| `authenticationMethod` | String  | Required | Mutable   | Indicates whether to use PingOne MFA, an external IdP, or a combination of both for admin sign-on. Possible values are `PINGONE`, `EXTERNAL`, or `HYBRID`. The default is `PINGONE`. |
| `createdAt`            | Date    | N/A      | Read-only | The timestamp the resource was created.                                                                                                                                              |
| `environment.id`       | UUID    | N/A      | Read-only | The ID of the environment.                                                                                                                                                           |
| `hasFido2Capabilities` | Boolean | N/A      | Read-only | Indicates whether the environment supports FIDO2 passkeys for MFA.                                                                                                                   |
| `isPingIDInBOM`        | Boolean | N/A      | Read-only | Indicates whether the environment supports PingID for MFA.                                                                                                                           |
| `mfaStatus`            | String  | Required | Immutable | This property must be set to `ENFORCE` as MFA is required for administrator sign-ons. This property applies only to the specified environment.                                       |
| `provider.id`          | UUID    | Optional | Mutable   | The UUID of the external IdP, if applicable.                                                                                                                                         |
| `recovery`             | Boolean | Required | Mutable   | Indicates whether to allow account recovery within the admin policy.                                                                                                                 |
| `updatedAt`            | Date    | N/A      | Read-only | The timestamp the resource was last updated.                                                                                                                                         |

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## Administrator security errors

In addition to the general [error codes](../reference/error-codes.html), administrator security operations can return the following errors:

| HTTP status | Top‑level code    | Detail code | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------- | ----------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_REQUEST` | None        | **Message:** Describes the rejected property, such as `Recovery must be provided when updating admin configuration.`, `Authentication method must be provided when updating admin configuration.`, `Provider must not be provided when using authentication method PINGONE.`, `Populations are only applicable if authentication method is HYBRID.`, `Discovery Rules are only applicable if authentication method is HYBRID.`, or `MFA Status must be provided when updating admin configuration.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /adminConfig` request omits or supplies an invalid value for a required property on update: `recovery`, `authenticationMethod`, `mfaStatus`, or a property that conflicts with the configured method, such as `provider` with `PINGONE` or `populations` and `discoveryRules` with a method other than `HYBRID`
>
> **Details:** None. |
| 400         | `INVALID_REQUEST` | None        | **Message:** `MFA status must be ENFORCE.`> **Collapse: When and details**
>
> **When:** A `PUT /adminConfig` request changes `mfaStatus` from `ENFORCE` to another value
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 400         | `INVALID_REQUEST` | None        | **Message:** Describes the rejected configuration, such as `Allowed methods must include EMAIL, TOTP, and FIDO2.`, `Enabled must be provided for method: <method>`, `Error processing allowed methods JSON for method: <method>`, `At least one method must be enabled.`, or `FIDO2 is not available for this environment.`> **Collapse: When and details**
>
> **When:** A `PUT /adminConfig` request supplies an `allowedMethods` configuration that is invalid: missing one of `EMAIL`, `TOTP`, or `FIDO2`, a method entry without an `enabled` value or with malformed JSON, no methods enabled, or `FIDO2` enabled in an environment that does not support it
>
> **Details:** None.                                                                                                                                                                                                                 |
| 400         | `INVALID_REQUEST` | None        | **Message:** `Discovery Rules exceeds the maximum limit of <maximum>`> **Collapse: When and details**
>
> **When:** A `PUT /adminConfig` request with a `HYBRID` method supplies more discovery rules than the environment allows
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 400         | `INVALID_REQUEST` | None        | **Message:** `Admin configuration is not enabled for the organization or environment.`> **Collapse: When and details**
>
> **When:** A `POST /adminConfig` request is made for an organization or environment that does not have the administrator MFA configuration enabled
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `INVALID_REQUEST` | None        | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /adminConfig` request body cannot be deserialized, for example an unrecognized `authenticationMethod` or `mfaStatus` value
>
> **Details:** For a JSON field conversion error, the target is the field path. Otherwise no detail is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 400         | `REQUEST_FAILED`  | None        | **Message:** `Admin configuration for environment ID <environmentId> already exists.` or `Provider must be provided when using the authentication method EXTERNAL.` (or `Provider must be provided when using an authentication method other than PINGONE.`)> **Collapse: When and details**
>
> **When:** A `POST /adminConfig` request creates a configuration for an environment that already has one, or supplies an external or hybrid method without a `provider`
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                            |
| 400         | `REQUEST_FAILED`  | None        | **Message:** Describes the failed operation, such as `Error creating admin configuration for environment ID <environmentId>.`, `Error updating admin configuration for environment ID <environmentId>.`, `Error reading admin configuration for environment ID <environmentId>.`, `Error retrieving environment with ID <environmentId>.`, `Error retrieving identity provider with ID <providerId>.`, `Error retrieving population with ID <populationId>.`, or `Error retrieving provider with ID <providerId>.`> **Collapse: When and details**
>
> **When:** The request cannot be completed because of a downstream service failure while validating or storing the configuration
>
> **Details:** None.                                                                                                                                                                                             |
| 403         | `ACCESS_FAILED`   | None        | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `admin:read:config` permission (`GET`), the `admin:create:config` permission (`POST`), or the `admin:update:config` permission (`PUT`)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 404         | `NOT_FOUND`       | None        | **Message:** `Environment with ID <environmentId> does not exist.` or `Admin configuration for environment ID = <environmentId> not found.`> **Collapse: When and details**
>
> **When:** A `PUT /adminConfig` request references an environment that does not exist, or updates a configuration that has not been created
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 404         | `NOT_FOUND`       | None        | **Message:** `Identity provider with ID <providerId> does not exist.`, `Population with ID <populationId> does not exist.`, `Provider with ID <providerId> does not exist.`, or `Identity provider with ID <providerId> is not enabled.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /adminConfig` request references an identity provider, population, or discovery‑rule provider that does not exist, or an identity provider that is disabled
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                |

---

---
title: Agreement Languages Resources
description: Describes the agreement languages resource, which defines the locale configuration and data model for managing PingOne agreement languages
component: pingone-api
page_id: pingone-api:platform:agreement-management/agreement-languages-resources/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/agreement-management/agreement-languages-resources/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  agreement-languages-data-model: Agreement languages data model
  response-codes: Response codes
  agreement-language-errors: Agreement language errors
---

# Agreement Languages Resources

Agreement languages define the configuration for the locale and for the configuration that applies to all revision resources associated with the language.

Agreement languages are defined by either the language code (for example, `en`) or the combination of language code and country code (for example, `en-gb`). For identifying languages, the API follows the tags for identifying languages described in [RFC_4646](https://tools.ietf.org/html/rfc4646). For selecting a language code to use in an agreement, the API follows the matching of language tags described in [RFC_4647](https://tools.ietf.org/html/rfc4647).

The end user's language selection for the consent agreement is determined by these attributes in the following priority: (1) the user's preferred locale, (2) the browser locale, or (3) the default language for the environment.

The agreement languages service implements functions to create, read, update, and delete agreement language resources.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | You need the Environment Admin role to perform operations on agreement languages resources. |

## Agreement languages data model

| Property                            | Type   | Required          | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------------------- | ------ | ----------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agreement`                         | String | Required          | Read-Only | A UUID that specifies the agreement resource associated with this language resource.                                                                                                                                                                                                                                                                           |
| `currentRevision`                   | String | Optional          | Read-Only | A UUID that specifies the current revision associated with this language resource. The current revision is the one shown to users for new consents in the language.                                                                                                                                                                                            |
| `displayName`                       | String | Required          | Mutable   | Used as the title of the agreement for the language presented to the user.                                                                                                                                                                                                                                                                                     |
| `enabled`                           | Date   | Required/Optional | Mutable   | Maps directly with a language being enabled or displayed for the environment within the platform. When running [Create Language](../../language-management/languages/create-language-1.html), `enabled` value will be `false` whether or not this property is included. If the language is disabled at the environment level, this property if always `false`. |
| `id`                                | String | Required          | Read-Only | UUID that specifies the language ID.                                                                                                                                                                                                                                                                                                                           |
| `locale`                            | String | Required          | Mutable   | The tag for identifying the language resource associated with this agreement consent (for example, `en-US`). For more information about language tags, refer to [Tags for Identifying Languages](https://tools.ietf.org/html/bcp47).                                                                                                                           |
| `userExperience.acceptCheckboxText` | String | Optional          | Mutable   | The text next to the "accept" checkbox in the end user interface. Accepted character are unicode letters, combining marks, numeric characters, whitespace, and punctuation characters (regex: `^[\p{L}\p{M}\p{N}\p{Zs}\p{P}]+$`).                                                                                                                              |
| `userExperience.continueButtonText` | String | Optional          | Mutable   | The text of the "continue" button in the end user interface. Accepted character are unicode letters, combining marks, numeric characters, whitespace, and punctuation characters (regex: `^[\p{L}\p{M}\p{N}\p{Zs}\p{P}]+$`).                                                                                                                                   |
| `userExperience.declineButtonText`  | String | Optional          | Mutable   | The text of the "decline" button in the end user interface. Accepted character are unicode letters, combining marks, numeric characters, whitespace, and punctuation characters (regex: `^[\p{L}\p{M}\p{N}\p{Zs}\p{P}]+$`).                                                                                                                                    |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## Agreement language errors

In addition to the general [error codes](../../reference/error-codes.html), agreement language operations can return the following errors:

| HTTP status | Top‑level code    | Detail code                                        | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------- | ----------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`    | `EMPTY_VALUE` or `OUT_OF_RANGE` or `INVALID_VALUE` | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /agreements/{agreementID}/languages` request omits the required `displayName` or `locale` property, or supplies a `displayName` that is empty, blank, over 256 characters, or does not match the display name character rules
>
> **Details:** `must not be null` for an omitted `displayName` or `locale`, `size must be between 1 and 256` for an empty or over-long `displayName`, `must not be empty or blank` for a blank `displayName`, or:
>
> ```
> must contain only Unicode letters, marks, numbers, spaces, forward slashes, dots, apostrophes, brackets, underscores, or hyphens
> ```
>
> for a `displayName` that does not match the display name character rules, for example `Validation Error : [displayName must not be null]`. |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`                                    | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /agreements/{agreementID}/languages` request supplies a `userExperience` object with no `acceptCheckboxText`, `continueButtonText`, or `declineButtonText` value
>
> **Details:** `must not be an empty object` with target `userExperience`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 400         | `INVALID_DATA`    | `UNIQUENESS_VIOLATION`                             | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /agreements/{agreementID}/languages` request creates a language with a `locale` that another language of the same agreement already uses (case‑insensitive)
>
> **Details:** `A resource with the specified name already exists.` with target `locale`                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `DELETE /agreements/{agreementID}/languages/{ID}` request deletes a language that has an effective revision
>
> **Details:** `Agreement language with effective revision can not be deleted.` with no target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`                                    | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `PUT /agreements/{agreementID}/languages/{ID}` request sets `enabled` to `true` when the language has no effective revision to show users
>
> **Details:** `The language must have a revision to show users in order to be enabled. Please create a revision for the language that is configured to take effect immediately.` with target `enabled`                                                                                                                                                                                                                                                                                                                                                                 |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT /agreements/{agreementID}/languages/{ID}` request sets `enabled` to `true` when the language is not enabled for the environment, or is not configured for the environment at all
>
> **Details:** `the language is not enabled for the environment` or `the language is not configured for the environment`, each with target `enabled`                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT /agreements/{agreementID}/languages/{ID}` request sets `enabled` to `false` for the language that supports the environment's default language while the agreement is enabled
>
> **Details:**
>
> ```
> The agreement language that supports default environment language can not be disabled. To disable agreement language 1) disable an agreement or 2) configure default environment language to another.
> ```
>
> with target `enabled`.                                                                                                                                                                                                                                                                         |
| 400         | `INVALID_REQUEST` | None                                               | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** A path identifier cannot be parsed as a UUID, or the request body cannot be deserialized
>
> **Details:** For a JSON field conversion error, the target is the field path. Otherwise no detail is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 403         | `ACCESS_FAILED`   | None                                               | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `agreements:read:agreement` permission (`GET` operations), the `agreements:update:agreement` permission (`POST` and `PUT`), or the `agreements:delete:agreement` permission (`DELETE`)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 404         | `NOT_FOUND`       | None                                               | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /agreements/{agreementID}/languages/{ID}` references an agreement language that does not exist, or an agreement that does not exist
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

---

---
title: Agreement Management
description: Explains PingOne agreement management, including agreements, language, and revision resources, and how agreement content is presented to end users for consent
component: pingone-api
page_id: pingone-api:platform:agreement-management/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/agreement-management/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  agreement-configuration: Agreement configuration
  how-agreement-content-is-presented-to-users: How agreement content is presented to users
  agreement-consent-history: Agreement consent history
  agreements-events-generated: Agreements events generated
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
---

# Agreement Management

Agreements define the details of an agreement to which end users provide consent. An agreement consists of these PingOne resources:

* **Agreements resources**

  Defines the top level configuration for all the languages resources associated with the agreement. For more information, refer to [Agreements Resources](agreements-resources/index.html).

* **Language resources**

  Defines the configuation for the locale and for the configuration that applies to all revision resources associated with the language. For more information, refer to [Agreement Languages Resources](agreement-languages-resources/index.html).

* **Revisions resources**

  Defines the specific version text (the agreement content) to manage the lifecycle of the agreement to which users provide consent. For more information, refer to [Agreement Revisions Resources](agreement-revisions-resources/index.html).

Learn more in [Agreements](https://docs.pingidentity.com/pingone/user_experience/p1_agreements.html) in the PingOne admin guide.

## Agreement configuration

An agreement cannot be enabled unless it supports the default environment language. The agreement resource can have its `enabled` property set to `true` only if there is "agreement content to show" for the default environment language. If the `enabled` property on the agreement resource is `false`, the agreement cannot be presented to end users.

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | For information about the environment's default language, refer to [Language Management](../language-management/index.html). |

The condition of having "agreement content to show" requires that at least the environment's default language is configured as an agreement language resource. The agreement language resource that supports the environment's default language must be enabled. The agreement language resource can have its `enabled` property set to `true` only if there is "localized content to show" configured on its associated agreement revisions resource. If the `enabled` property on the agreement language resource is `false`, the agreement language cannot be presented to end users. Remember, you must enable the agreement language resource that represents the environment's default language to enable the agreement. Additional agreement languages can also be configured and associated with the agreement.

The agreement revision resource associated with an agreement language resource must have text content (and it can have optional buttons and checkboxes) configured on the resource to meet the "localized content to show" condition to enable the language. For the agreement revision to be active, the agreement revision's `effectiveDate` property must not be set to a future date. However, the `effectiveDate` value can be set to a future date, but the revision is inactive until the specified date.

|   |                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information about the agreement resources described above and how these resources contribute to a user's agreement consent state, refer to [User Agreement Consents](../users/user-agreement-consents/index.html). |

## How agreement content is presented to users

Agreement languages are defined by either the language code (for example, `en`) or the combination of language code and country code (for example, `en-GB`). For identifying languages, the API follows the tags for identifying languages described in [RFC_4646](https://tools.ietf.org/html/rfc4646). For selecting a language code to use in an agreement, the API follows the matching of language tags described in [RFC_4647](https://tools.ietf.org/html/rfc4647).

When an agreement is active, languages are presented to the user in the following order:

1. *User preference*: The end user receives agreement content in the language that matches the user's `preferredLanguage` property value.

2. *Browser preference*: If the user's `preferredLanguage` is not configured (or enabled) as one of the supported agreement language resources for this agreement, the end user receives agreement content in the language associated with the browser's configured locale.

3. *Environment default language*: If the browser's configured language is not one of the enabled agreement language resources for this agreement, then the agreement content is presented to the end user in the environment's default language.

The following table shows an example of how the platform presents agreement languages to users, depending on the environment default language, the configured agreement languages, and the user's language preferences.

| Environment default language | Configured agreement languages | User preference languages (ordered) | Language presented to user |
| ---------------------------- | ------------------------------ | ----------------------------------- | -------------------------- |
| `es`                         | `en`, `es`                     | `en-US`, `es`                       | `en`                       |
| `es`                         | `en-GB`, `es`                  | `en-US`                             | `es`                       |
| `es`                         | `en`, `en-GB`, `es`            | `en-US`, `es`, `en-GB`              | `en`                       |

## Agreement consent history

A user's consents to agreements do not expire by default, but they can be configured to designate a re-consent action based on a specified length of time or the active date of an agreement revision. An environment supports up to 100 agreement resources.

Only the user's latest consent information is kept in the API. Agreement consent history is visible through audit reporting events. For more information about audit reporting, refer to [Audit Activities](../audit-activities/index.html).

For example, to search for the consent history for a specific user to an agreement using the audit activities API, the query filter looks like this:

```none
recordedat ge "2020-12-11T22:13:41.838Z" and recordedat le "2021-06-09T21:13:41.838Z" and resources.type eq "user" and resources.id eq "<user-id>" and (action.type eq "AGREEMENT_CONSENT.ACCEPTED")
```

To search for consent history for an agreement (showing consents for all users), the query filter looks like this:

```none
recordedat ge "2020-12-11T22:11:54.484Z" and recordedat le "2021-06-09T21:11:54.484Z" and resources.id eq "<agreement-id>" and (action.type eq "AGREEMENT_CONSENT.ACCEPTED")
```

## Agreements events generated

Refer to [Audit Reporting Events](../reference/audit-reporting-events.html) for the events generated.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `LOCALIZATION_STATUS.UPDATED` events are consumed by the language management service and are used to verify whether localization is complete for a language for a specific service, which, in this case, is the agreements management service. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../group-role-assignments/index.html).

* [User Role Assignments](../users/user-role-assignments/index.html).

Refer to [Roles Management](../roles/index.html) for more information.

---

---
title: Agreement Revisions Resources
description: Describes the agreement revisions resource, which manages the versioned content and data model for PingOne agreement revisions
component: pingone-api
page_id: pingone-api:platform:agreement-management/agreement-revisions-resources/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/agreement-management/agreement-revisions-resources/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  revision-data-model: Revision data model
  response-codes: Response codes
  agreement-revision-errors: Agreement revision errors
---

# Agreement Revisions Resources

Agreement revisions define the specific version text (the agreement content) to manage the lifecycle of the agreement to which users provide consent.

A revision resource allows you to update the content for an agreement language. (A language can have up to 100 associated revisions.) The revision must have a value specified for the `effectiveDate` property, and when showing content to a user for an agreement language, the content associated with a revision with an effective date closest to the current date is shown. The revision can be configured to force the user to consent again to the agreement.

The revisions service implements functions to create, read, and delete agreement revision resources. Agreement revision resources cannot be updated. If an agreement revision needs to be updated, a new agreement revision should be created. In addition, agreement revision resources that have become effective cannot be deleted, which ensures that consent data is preserved.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | You need the Environment Admin role to perform operations on agreement revisions resources. |

## Revision data model

| Property            | Type    | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | ------- | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agreement`         | String  | Required | Read-Only | The UUID for the agreement resource for this revision.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `contentType`       | String  | Required | Immutable | The content type of `text`. Options are `text/html` and `text/plain`, as defined by [rfc-6838](https://datatracker.ietf.org/doc/html/rfc6838#section-4.2.1) and [Media Types/text](https://www.iana.org/assignments/media-types/media-types.xhtml#text). This attribute is supported in `POST` requests only.                                                                                                                                                                                                          |
| `effectiveAt`       | Date    | Required | Mutable   | The start date that the revision is presented to users. This property value can be modified only if the current value is a date that has not already passed. The effective date must be unique for each language agreement, and the property value can be the present date or a future date only.                                                                                                                                                                                                                      |
| `id`                | String  | Required | Read-Only | The revision ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `language`          | String  | Required | Mutable   | A UUID that specifies the language resource associated with this revision.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `notValidAfter`     | Date    | Optional | Read-Only | Specifies whether the revision is still valid in the context of all revisions for a language. This property is calculated dynamically at read time, taking into consideration the agreement language, the language enabled property, and the agreement enabled property. When a new revision is added, the `notValidAfter` property values for all other previous revisions might be impacted. For example, if a new revision becomes effective and it forces reconsent, then all older revisions are no longer valid. |
| `requiresReconsent` | Boolean | Required | Mutable   | Whether the user is required to provide consent to the language revision after it becomes effective.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `text`              | String  | Required | Immutable | Text or HTML for the revision. HTML support includes:\* tags - italicize, bold, links, headers, paragraph, line breaks\* link (a) tags - allow href, style, target attributes\* block tags (p, b, h) - allow style and align attributesThis attribute is supported in `POST` requests only. For more information, refer to `contentType`.                                                                                                                                                                              |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## Agreement revision errors

In addition to the general [error codes](../../reference/error-codes.html), agreement revision operations can return the following errors:

| HTTP status | Top‑level code    | Detail code            | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------- | ----------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`    | `EMPTY_VALUE`          | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /agreements/{agreementID}/languages/{languageID}/revisions` request omits the required `effectiveAt` or `requireReconsent` property, or a `POST` request omits the required `text` property
>
> **Details:** Describes the failing property, such as `must not be null` for an omitted `effectiveAt`, `requireReconsent`, or `text` property, for example `Validation Error : [effectiveAt must not be null]`                         |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST /agreements/{agreementID}/languages/{languageID}/revisions` request supplies a `contentType` value other than `text/html` or `text/plain`
>
> **Details:** `must be one of [text/html, text/plain]`, for example `Validation Error : [contentType must be one of [text/html, text/plain]]`                                                                                                                                                     |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /agreements/{agreementID}/languages/{languageID}/revisions` request supplies revision text that is empty or exceeds 150 KB
>
> **Details:** `must not be empty` or `maximum size is 150KB`                                                                                                                                                                                                        |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /agreements/{agreementID}/languages/{languageID}/revisions` request with a `contentType` of `text/html` supplies HTML that the revision content rules reject, such as unsupported tags or attributes, or a link that does not use `https://` or `mailto://`
>
> **Details:** Describes the rejected HTML, such as `unsupported HTML` or `All HTML links must use https:// or mailto:// protocols` |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /agreements/{agreementID}/languages/{languageID}/revisions` request supplies an `effectiveAt` date more than 5 seconds in the past, or an `effectiveAt` date that another revision of the same language already uses
>
> **Details:** `The revision can not take effect in the past.` or `Another revision has the same effectiveAt date.`                                               |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST /agreements/{agreementID}/languages/{languageID}/revisions` request would exceed the maximum number of revisions for the language
>
> **Details:** `The maximum of <maximum> revisions per language has been reached.`                                                                                                                                                                                    |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT /agreements/{agreementID}/languages/{languageID}/revisions/{ID}` request changes the `effectiveAt` date of a revision that has already taken effect
>
> **Details:**
>
> ```
> The revision is already effective and can not be updated. If this is the current revision and you need to override it try creating a new revision and forcing reconsent.
> ```                                              |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `DELETE /agreements/{agreementID}/languages/{languageID}/revisions/{ID}` request deletes a revision that has taken effect
>
> **Details:** `A currently effective revision cannot be deleted.`                                                                                                                                                                                                                  |
| 400         | `INVALID_REQUEST` | None                   | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A path identifier cannot be parsed as a UUID
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                       |
| 400         | `INVALID_REQUEST` | `INVALID_VALUE`        | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** The request body cannot be deserialized as JSON
>
> **Details:** `Invalid value for attribute.`, with the target set to the field path for a field conversion error. Otherwise no detail is returned.                                                                                                                                                                                                                  |
| 403         | `ACCESS_FAILED`   | None                   | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `agreements:read:agreement` permission (`GET` operations), the `agreements:update:agreement` permission (`POST` and `PUT`), or the `agreements:delete:agreement` permission (`DELETE`)
>
> **Details:** None.                                                                                                                                                                                                 |
| 404         | `NOT_FOUND`       | None                   | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /agreements/{agreementID}/languages/{languageID}/revisions/{ID}` references a revision, language, or agreement that does not exist
>
> **Details:** None.                                                                                                                                                                                                                                     |

---

---
title: Agreements Resources
description: Describes the agreements resource, which defines the top level configuration and data model for PingOne agreements
component: pingone-api
page_id: pingone-api:platform:agreement-management/agreements-resources/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/agreement-management/agreements-resources/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  agreements-data-model: Agreements data model
  response-codes: Response codes
  agreement-errors: Agreement errors
---

# Agreements Resources

The agreements API defines the top level configuration for all the languages resources associated with the agreement. It implements functions to create, read, update, and delete agreement resources.

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | You need the Environment Admin role to perform operations on agreement resources. |

## Agreements data model

| Property                 | Type    | Required | Mutable   | Description                                                                                                                                                                                                                                                            |
| ------------------------ | ------- | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `consentCountsUpdatedAt` | Date    | N/A      | Read-Only | The time the consent count metric was last updated. This value is typically updated once every 24 hours.                                                                                                                                                               |
| `description`            | String  | Optional | Mutable   | The description of the agreement.                                                                                                                                                                                                                                      |
| `enabled`                | Boolean | Required | Mutable   | The current enabled state of the agreement. The agreement must support the default language to be enabled. It cannot be disabled if it is referenced by a sign-on action. When an agreement is disabled, it is not used anywhere that it is configured across PingOne. |
| `environment.id`         | String  | N/A      | Read-Only | A string that specifies the environment associated with the agreement.                                                                                                                                                                                                 |
| `expiredUserConsents`    | Integer | Required | Read-Only | The number of users who have consented to the agreement, but their consent has expired. This value is last calculated at the `consentCountsUpdatedAt` time.                                                                                                            |
| `id`                     | String  | N/A      | Read-Only | The agreement ID.                                                                                                                                                                                                                                                      |
| `name`                   | String  | Required | Mutable   | The name of the agreement resource.                                                                                                                                                                                                                                    |
| `reconsentPeriodDays`    | Float   | Optional | Mutable   | The number of days until a consent to this agreement expires.                                                                                                                                                                                                          |
| `totalUserConsents`      | Integer | Required | Read-Only | The total number of users who have consented to the agreement. This value is last calculated at the `consentCountsUpdatedAt` time.                                                                                                                                     |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## Agreement errors

In addition to the general [error codes](../../reference/error-codes.html), agreement operations can return the following errors:

| HTTP status | Top‑level code    | Detail code            | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ----------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`    | `EMPTY_VALUE`          | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /agreements` request omits the required `name` or `enabled` property
>
> **Details:** `must not be null` on `name` or `enabled` (detail `EMPTY_VALUE`), for example `Validation Error : [name must not be null]`                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /agreements` request supplies a `name` that does not match the object name rules, or a `description` that does not match the description character rules
>
> **Details:** `must contain only Unicode letters, marks, numbers, spaces, forward slashes, dots, apostrophes, underscores, or hyphens` for an invalid `name`, or ``must contain only Unicode letters, marks, numbers, spaces, or punctuation (except $, +, <, =, >, ^, `, \|, ~)`` for an invalid `description`, for example:
>
> ```
> Validation Error : [name must contain only Unicode letters, marks, numbers, spaces, forward slashes, dots, apostrophes, underscores, or hyphens]
> ``` |
| 400         | `INVALID_DATA`    | `OUT_OF_RANGE`         | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /agreements` request supplies a `name` or `description` that exceeds its maximum length, or a `reconsentPeriodDays` value of `0` or less
>
> **Details:** `size must be between 1 and 256` for a too-long `name`, `size must be between 1 and 1024` for a too-long `description`, or `must be greater than 0` for `reconsentPeriodDays` (detail `INVALID_VALUE` for the `reconsentPeriodDays` violation), for example `Validation Error : [reconsentPeriodDays must be greater than 0]`                                                                                                                                                                    |
| 400         | `INVALID_DATA`    | `UNIQUENESS_VIOLATION` | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST /agreements` request creates an agreement with a name that duplicates another agreement in the environment, or a `PUT /agreements/{ID}` request renames the agreement to one that does
>
> **Details:** `A resource with the specified name already exists.`                                                                                                                                                                                                                                                                                                                                                           |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST /agreements` request would exceed the maximum number of agreements for the environment (default 100)
>
> **Details:** `The maximum of <maximum> agreements has been reached.`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST /agreements` request sets `enabled` to `true`. An agreement is enabled only after it supports the environment's default language
>
> **Details:** `Must be false. The agreement can be enabled upon configuring support for the environment's default language.`                                                                                                                                                                                                                                                                                                                                                               |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `PUT /agreements/{ID}` request sets `enabled` to `true` when the agreement does not have an enabled language matching the environment's default language
>
> **Details:** `The agreement can not be enabled without supporting the default language configured for the environment.`                                                                                                                                                                                                                                                                                                                                                 |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `DELETE /agreements/{ID}` request deletes an agreement that is enabled
>
> **Details:** `Can not delete an enabled agreement.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `DELETE /agreements/{ID}` request deletes an agreement that end users have consented to, including expired consents
>
> **Details:** `Can not delete an agreement that has been consented to by end users.`                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 400         | `INVALID_REQUEST` | None                   | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A path identifier cannot be parsed as a UUID, or the request body cannot be deserialized
>
> **Details:** For a JSON field conversion error, the target is the field path. Otherwise no detail is returned.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 403         | `ACCESS_FAILED`   | None                   | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `agreements:read:agreement` permission (`GET` operations), the `agreements:create:agreement` permission (`POST`), the `agreements:update:agreement` permission (`PUT`), or the `agreements:delete:agreement` permission (`DELETE`)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                          |
| 404         | `NOT_FOUND`       | None                   | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /agreements/{ID}` references an agreement that does not exist in the environment
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

---
title: Alerting
description: Configure PingOne alert channels to notify administrators by email about resource-state changes that can cause service disruptions
component: pingone-api
page_id: pingone-api:platform:alerting/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/alerting/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  alert-channel-data-model: Alert channel data model
  alert-events-generated: Alert events generated
  response-codes: Response codes
  alert-errors: Alert errors
---

# Alerting

The Alerting service delivers warnings to administrators' email addresses regarding changes in resource states that can cause service disruptions. By default, each alert is sent only once. The Alerting service filters out any duplicate alerts.

For administrators to receive these alerts, you must configure the alert channel to use for each environment. Currently, email is the only supported type of alert channel. Use the Alerting service endpoints to configure the alert channel.

|   |                                                                                      |
| - | ------------------------------------------------------------------------------------ |
|   | Administrators can also configure Alerting preferences in the PingOne admin console. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../roles/predefined-roles/index.html#automatic-role-assignment).

* [Group Role Assignments](../group-role-assignments/index.html).

* [User Role Assignments](../users/user-role-assignments/index.html).

Refer to [Roles Management](../roles/index.html) for more information.

## Alert channel data model

| Property            | Type      | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------- | --------- | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `addresses`         | String\[] | Required | Mutable   | The administrator email addresses to send the alerts to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `channelType`       | String    | Required | Mutable   | Alert channel type. Currently, this must be `EMAIL`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `alertName`         | String    | Optional | Mutable   | The name to assign to the alert channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `environment.id`    | String    | Required | Immutable | Unique ID of the environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `id`                | String    | N/A      | Read-only | Unique ID of the alert channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `includeSeverities` | String\[] | Optional | Mutable   | Filters alerts by severity. If empty, all severities are included. Possible values are `INFO`, `WARNING`, and `ERROR`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `includeAlertTypes` | String\[] | Optional | Mutable   | Use the `includeAlertTypes` array to specify the alert types you want to create. If empty, all alert types are included. Possible values are: `CERTIFICATE_EXPIRED`, `CERTIFICATE_EXPIRING`, `GATEWAY_ERROR_ALERT`, `GATEWAY_INFO_ALERT`, `GATEWAY_WARNING_ALERT`, `GATEWAY_VERSION_DEPRECATED`, `GATEWAY_VERSION_DEPRECATING` , `KEY_PAIR_EXPIRED`, `KEY_PAIR_EXPIRING`, `LICENSE_90_PERCENT_USER_SOFT_LIMIT`, `LICENSE_ENTITLEMENT_80_PERCENT_EXCEEDED`, `LICENSE_ENTITLEMENT_90_PERCENT_EXCEEDED`, `LICENSE_ENTITLEMENT_EXCEEDED`, `LICENSE_EXPIRED`, `LICENSE_EXPIRING`, `LICENSE_ROTATED`, `LICENSE_USER_HARD_LIMIT_EXCEEDED`, `LICENSE_USER_SOFT_LIMIT_EXCEEDED`, `RATE_LIMIT_EXCEEDED`, `RATE_LIMIT_WARNING`, `RISK_CONFIGURATION`, `SUSPICIOUS_TRAFFIC`. |

## Alert events generated

Refer to [Audit Reporting Events](../reference/audit-reporting-events.html) for the events generated.

### Response codes

| Code | Message                                  |
| ---- | ---------------------------------------- |
| 200  | Successful operation.                    |
| 201  | Successfully created.                    |
| 204  | Successfully removed. No content.        |
| 400  | The request could not be completed.      |
| 401  | You do not have access to this resource. |
| 404  | The requested resource was not found.    |

## Alert errors

In addition to the general [error codes](../reference/error-codes.html), alert channel operations can return the following errors:

| HTTP status | Top‑level code    | Detail code                      | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------- | ----------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`                  | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /alertChannels` request includes an alert type that does not exist in `includeAlertTypes` or `excludeAlertTypes`
>
> **Details:** Describes the failing property: `Invalid alert type(s): <alertTypes>` with the comma‑separated list of unrecognized types, on the `includeAlertTypes` or `excludeAlertTypes` target                                                                                                                                                              |
| 400         | `INVALID_DATA`    | `EMPTY_VALUE` or `INVALID_VALUE` | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /alertChannels` request omits the required `addresses` property, supplies an empty `addresses` set, or includes an address that is not a valid email address
>
> **Details:** Describes the failing property: `addresses must not be null` for an omitted `addresses`, `must not be empty` for an empty `addresses` set, or `must be a well-formed email address` for an `addresses` entry that is not a valid email address, for example `Validation Error : [addresses must not be null]`.                                    |
| 400         | `INVALID_DATA`    | None                             | **Message:** `Alert type 'EVENT_DELIVERY_FAILED' is not enabled. Requires feature flag 'paxp-330_test_connection_for_webhooks'.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /alertChannels` request includes `EVENT_DELIVERY_FAILED` in `includeAlertTypes` or `excludeAlertTypes` when the event delivery failure alert feature flag is off for the environment
>
> **Details:** None. The response has no `details` array.                                                                                                                                                                                                        |
| 400         | `INVALID_REQUEST` | `INVALID_VALUE`                  | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** A path identifier cannot be parsed as a UUID, or the request body cannot be deserialized, for example an invalid `includeSeverities` value or a property with the wrong JSON type
>
> **Details:** For a JSON field conversion error, the target is the field path and the detail message is `Invalid value for attribute.`. Otherwise no detail is returned. The same handler also covers a `channelType` value that does not name a registered subtype, which returns the custom channel‑type message instead. |
| 400         | `INVALID_REQUEST` | None                             | **Message:** `Invalid channelType '<channelType>'. Must be one of: EMAIL`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /alertChannels` request supplies a `channelType` value that is not a known channel type, such as `SMS`
>
> **Details:** None. The invalid channel‑type rejection carries the `INVALID_REQUEST` top‑level code with no detail, while other JSON deserialization failures keep the `INVALID_VALUE` detail structure.                                                                                                                                                                                             |
| 403         | `ACCESS_FAILED`   | None                             | **Message:** `You do not have permissions or are not licensed to make this request.`> **Collapse: When and details**
>
> **When:** The actor lacks the `alerting:read:channel` permission (`GET` operations), the `alerting:create:channel` permission (`POST`), the `alerting:update:channel` permission (`PUT`), or the `alerting:delete:channel` permission (`DELETE`)
>
> **Details:** None.                                                                                                                                                                                                                                                        |
| 404         | `NOT_FOUND`       | None                             | **Message:** `AlertChannel not found. EnvironmentId: <environmentId>, AlertChannelId: <channelId>`> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /alertChannels/{channelId}` references an alert channel that does not exist in the environment
>
> **Details:** None. The service‑specific not‑found message replaces the standard `NOT_FOUND` default message.                                                                                                                                                                                                                                                               |

---

---
title: Application - Device Requirements (PingID mobile app only)
description: Use the deviceRequirements endpoint to set device requirements for using the PingID app, for example, the minimum Android or iOS version required.
component: pingone-api
page_id: pingone-api:platform:applications/device-requirements/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/applications/device-requirements/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["applications/device-requirements.adoc"]
section_ids:
  device-requirements-data-model: Device requirements data model
  device-requirements-errors: Device requirements errors
---

# Application - Device Requirements (PingID mobile app only)

Use the `deviceRequirements` endpoint to set device requirements for using the PingID app, for example, the minimum Android or iOS version required.

## Device requirements data model

| Property                                              | Type    | Required | Mutable   | Description                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------- | ------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `application.id`                                      | String  | N/A      | Read-only | The PingOne ID of the application.                                                                                                                                                                                                                                                         |
| `deviceLockEnableRequire.enabled`                     | Boolean | Optional | Mutable   | Set to `true` if you want to require a user's device to have a device lock enabled in order to use the PingID mobile app.                                                                                                                                                                  |
| `deviceNotAllowedRootedOrJailBroken.enabled`          | Boolean | Optional | Mutable   | Set to `true` if you want to prevent users from using the PingID mobile app on a rooted or jailbroken device.                                                                                                                                                                              |
| `deviceRequireBiometricsCapabilities.enabled`         | Boolean | Optional | Mutable   | Set to `true` if you want to require a user's device to have biometric capabilities such as fingerprint reading in order to pair or authenticate with the PingID mobile app.                                                                                                               |
| `environment.id`                                      | String  | N/A      | Read-only | The PingOne environment associated with the application.                                                                                                                                                                                                                                   |
| `minimumOSVersionRequire.enabled`                     | Boolean | Optional | Mutable   | Set to `true` if you want to specify a minimum operating system version on the device to allow pairing and authentication with the PingID mobile app. Use `minimumOSVersionRequire.android` and \` minimumOSVersionRequire.ios\` to specify the minimum versions for Android and iOS.      |
| `minimumOSVersionRequire.android`                     | String  | Optional | Mutable   | If `minimumOSVersionRequire.enabled` is set to `true`, use `android` to specify the minimum Android version that you want to require.                                                                                                                                                      |
| `minimumOSVersionRequire.ios`                         | String  | Optional | Mutable   | If `minimumOSVersionRequire.enabled` is set to `true`, use `ios` to specify the minimum iOS version that you want to require.                                                                                                                                                              |
| `minimumPingIDAppVersionRequire.enabled`              | Boolean | Optional | Mutable   | Set to `true` if you want to specify a minimum version of the PingID mobile app on the device to allow pairing and authentication with the app. Use `minimumPingIDAppVersionRequire.android` and `minimumPingIDAppVersionRequire.ios` to specify the minimum versions for Android and iOS. |
| `minimumPingIDAppVersionRequire.android`              | String  | Optional | Mutable   | If `minimumPingIDAppVersionRequire.enabled` is set to `true`, use `android` to specify the minimum PingID version that you want to require on Android.                                                                                                                                     |
| `minimumPingIDAppVersionRequire.ios`                  | String  | Optional | Mutable   | If `minimumPingIDAppVersionRequire.enabled` is set to `true`, use `ios` to specify the minimum PingID version that you want to require on iOS.                                                                                                                                             |
| `mobileDeviceManagementRequire.enabled`               | Boolean | Optional | Mutable   | If you require mobile device management for all devices using the PingID mobile app, set to `true` to generate a token.                                                                                                                                                                    |
| `mobileDeviceManagementRequire.effectiveDate`         | Date    | Optional | Mutable   | Use `effectiveDate` to specify the date by which you want the MDM requirement to be applied. Required when `mobileDeviceManagementRequire.enabled` is set to `true`.                                                                                                                       |
| `mobileDeviceManagementRequire.tokens`                | Array   | Optional | Mutable   | Contains the information for tokens generated for mobile device management. Required when `mobileDeviceManagementRequire.enabled` is set to `true`.                                                                                                                                        |
| `mobileDeviceManagementRequire.tokens[].creationTime` | String  | Optional | Mutable   | The date and time the token was generated. Required when `mobileDeviceManagementRequire.enabled` is set to `true`.                                                                                                                                                                         |
| `mobileDeviceManagementRequire.tokens[].token`        | String  | Optional | Mutable   | The token generated for mobile device management. Required when `mobileDeviceManagementRequire.enabled` is set to `true`.                                                                                                                                                                  |
| `restrictDevicesByBrand.enabled`                      | Boolean | Optional | Mutable   | Set to `true` if you want to limit use of the PingID mobile app to a group of device brands or device models. You can specify the brands/devices that can be used by defining an allow list or by defining a disallow list.                                                                |
| `restrictDevicesByBrand.deviceBrandsAllowed`          | Array   | Optional | Mutable   | Array of the device brand names that you are limiting use of the PingID app to.                                                                                                                                                                                                            |
| `restrictDevicesByBrand.deviceBrandsDisAllowed`       | Array   | Optional | Mutable   | Array of the device brand names for which you are not allowing use of the PingID mobile app.                                                                                                                                                                                               |
| `restrictDevicesByBrand.deviceModelsAllowed`          | Array   | Optional | Mutable   | Array of the device model names that you are limiting use of the PingID app to.                                                                                                                                                                                                            |
| `restrictDevicesByBrand.deviceModelsDisAllowed`       | Array   | Optional | Mutable   | Array of the device model names for which you are not allowing use of the PingID mobile app.                                                                                                                                                                                               |
| `updatedAt`                                           | Date    | N/A      | Read-only | The time the resource was last updated.                                                                                                                                                                                                                                                    |

## Device requirements errors

In addition to the general [error codes](../../reference/error-codes.html), device requirements operations can return the following errors:

| HTTP status | Top‑level code    | Detail code     | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | ----------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`    | `EMPTY_VALUE`   | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `PUT /deviceRequirements` request body omits a required property, such as an `enabled` setting
>
> **Details:** Describes the missing property. For a nested `mobileDeviceManagementRequire.tokens` entry, an omitted `token` or `creationTime` value yields `must not be null`, for example `Validation Error : [mobileDeviceManagementRequire.tokens[0].token must not be null]`.                                                                                                                                                                                                                                                                                                                                                             |
| 400         | `INVALID_DATA`    | `INVALID_VALUE` | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `PUT /deviceRequirements` request supplies an invalid value: an unrecognized Android or iOS version for `minimumOSVersionRequire` or `minimumPingIDAppVersionRequire`, an unknown brand or model in `restrictDevicesByBrand`, allowed and disallowed lists that share an entry, or lists supplied while `restrictDevicesByBrand.enabled` is `false`
>
> **Details:** Describes the rejected value, such as `invalid android version` or `invalid ios version` for `minimumOSVersionRequire` and `minimumPingIDAppVersionRequire`, `invalid brands - <brands>` for `restrictDevicesByBrand`, or `settings are disabled, brands/models must be empty`, for example `Validation Error : [restrictDevicesByBrand invalid brands - [invalidBrand1]]` |
| 400         | `INVALID_DATA`    | `INVALID_VALUE` | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `PUT /deviceRequirements` request enables `mobileDeviceManagementRequire` without an `effectiveDate` or without tokens, or supplies an `effectiveDate` or tokens while it is disabled
>
> **Details:** Describes the inconsistent MDM setting, such as `settings are enabled, effective date must be provided`, `settings are enabled, mobile device management tokens must be provided`, `settings are disabled, effectiveDate and tokens must be empty`, or `The mobile device management token must be in UUID format.`, for example `Validation Error : [mobileDeviceManagementRequire settings are enabled, effective date must be provided]`                                                                                              |
| 400         | `INVALID_REQUEST` | None            | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** A `PUT /deviceRequirements` request body cannot be deserialized
>
> **Details:** For a JSON field conversion error, the target is the field path. Otherwise no detail is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 404         | `NOT_FOUND`       | None            | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** The application ID in the request URL does not exist in the environment (applies to `GET`, `PUT`, and `DELETE /deviceRequirements`)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 404         | `NOT_FOUND`       | None            | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** `GET` or `DELETE /deviceRequirements` references device requirements that have not been set for the application
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

---
title: Application Attribute Mapping
description: Customize the content of ID tokens and SAML assertions by mapping custom attributes for PingOne OIDC and SAML applications
component: pingone-api
page_id: pingone-api:platform:applications/application-attribute-mapping/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/applications/application-attribute-mapping/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  id-token-and-saml-assertion-customization: ID token and SAML assertion customization
  openid-connect-application-attribute-mappings: OpenID Connect application attribute mappings
  saml-application-attribute-mappings: SAML application attribute mappings
  advanced-attribute-mapping: Advanced attribute mapping
  applications-attribute-mapping-data-model: Applications attribute mapping data model
  oidc-application-core-mapping-attributes: OIDC application core mapping attributes
  saml-application-core-mapping-attributes: SAML application core mapping attributes
  application-attribute-events-generated: Application Attribute events generated
  response-codes: Response codes
  application-attribute-mapping-errors: Application attribute mapping errors
---

# Application Attribute Mapping

## ID token and SAML assertion customization

The application attributes service lets you customize the content of an ID token or a SAML assertion by adding custom attributes and their values. Custom attributes have a cumulative length constraint of 16 Kb. Refer to [Custom attributes](../../schemas/index.html) in Schemas for more information.

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have multiple identity providers (IdPs) configured, you need to include an attribute mapping for `IDP ID` to distinguish between the IdPs. |

In the Authorization request header field of all samples, the `accessToken` value is your full base64url-encoded JSON web token generated by the authentication service.

## OpenID Connect application attribute mappings

For OpenID Connect (OIDC) applications, the user claim defined by the custom attribute mapping is returned in the ID token, regardless of the scopes specified in the authorization request. For example, suppose you want to include a user's `accountId` in ID tokens associated with the specified OIDC application, a custom application attribute resource can be created to map the user's account ID to the `accountId` PingOne user attribute. The request looks like this:

```sh
curl -X "POST" "https://api.pingone.com/v1/environments/{{envID}}/applications/{{appID}}/attributes" \
-H 'Content-type: application/json' \
-H 'Authorization: Bearer {{accessToken}}' \
-d '{
	"name": "userAccountID",
	"value": "${user.accountId}",
	"required": true
}
```

## SAML application attribute mappings

For SAML applications, the user claim defined by the custom attribute mapping is returned in the SAML assertion.

For example, suppose you want to include an `externalId` in assertions associated with the specified SAML application, a custom application attribute resource can be created to map the SAML `externalId` attribute to the user's external ID attribute. The request looks like this:

```sh
curl -X "POST" "https://api.pingone.com/v1/environments/{{envID}}/applications/{{appID}}/attributes" \
-H 'Content-type: application/json' \
-H 'Authorization: Bearer {{accessToken}}' \
-d '{
	"name": "externalId",
	"value": "${user.externalId}",
	"required": true
}
```

## Advanced attribute mapping

You can use PingOne's expression language for advanced attribute mapping. The supported expression language is an augmentation of SpEL. SpEL is a powerful expression language used for querying and manipulating an object graph at runtime.

For example, with advanced attribute mapping capabilities, you can write an expression that concatenates two or more user attributes in the `value` property:

```sh
curl -X "POST" "https://api.pingone.com/v1/environments/{{envID}}/applications/{{appID}}/attributes" \
-H 'Content-type: application/json' \
-H 'Authorization: Bearer {{accessToken}}' \
-d '{
	"name": "fullName",
	"value": "${user.name.given + ', ' + user.name.family}",
	"required": true
}
```

In this request, the `fullName` mapped attribute includes the user's first name and last name in the response.

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information about PingOne's expression language, refer to [PingOne's expression language](https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expression_language.html). |

## Applications attribute mapping data model

| Property         | Type    | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------- | ------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `application.id` | String  | Required | Read-only | The application associated with the application mapping resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `createdAt`      | Date    | N/A      | Read-only | The time the resource was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `environment.id` | String  | Required | Read-only | The environment associated with the application mapping resource.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `id`             | UUID    | Required | Read-only | The application mapping ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `mappingType`    | String  | Required | Read-only | The mapping type of the attribute. Options are `CORE`, `SCOPE`, and `CUSTOM`. The `CORE` and `SCOPE` mapping types are for reserved attributes managed by the API and cannot be removed. Attribute values for these mapping types can be updated. The `CUSTOM` mapping type is for user-defined attributes. Attributes of this type can be updated and deleted.                                                                                                                                                           |
| `name`           | String  | Required | Immutable | The name of attribute. Must be unique within an application. The property is set on create only and cannot be changed after creation. For SAML applications, the `samlAssertion.subject` name is a reserved case-insensitive name which indicates the mapping to be used for the subject in an assertion. For OpenID Connect applications, the following names are reserved and cannot be used:\* acr\* amr\* at_hash\* aud\* auth_time\* azp\* client_id\* exp\* iat\* iss\* jti\* nbf\* nonce\* org\* scope\* sid\* sub |
| `nameFormat`     | String  | Optional | Mutable   | A URI reference representing the classification of the attribute. Helps the service provider interpret the attribute format.                                                                                                                                                                                                                                                                                                                                                                                              |
| `required`       | Boolean | Required | Mutable   | Whether a mapping value is required for this attribute. If true, a value must be set and a non-empty value must be available in the SAML assertion or ID token.                                                                                                                                                                                                                                                                                                                                                           |
| `updatedAt`      | Date    | N/A      | Read-only | The time the resource was updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `value`          | String  | Required | Mutable   | The string constants or expression for mapping the attribute path against a specific source. The expression format is: `${<source>.<attribute_path>}`. The only supported source is `user` (for example, `${user.id}`).                                                                                                                                                                                                                                                                                                   |
| `idToken`        | Boolean | Optional | Mutable   | Whether the attribute mapping should be available in the ID Token. This property is applicable only when the application's `protocol` property is `OPENID_CONNECT`. If omitted, the default is `true`. Note that the `idToken` and `userInfo` properties cannot both be set to `false`. At least one of these properties must have a value of `true`.                                                                                                                                                                     |
| `userInfo`       | Boolean | Optional | Mutable   | Whether the attribute mapping should be available through the `/as/userinfo` endpoint. This property is applicable only when the application's `protocol` property is `OPENID_CONNECT`. If omitted, the default is `true`. Note that the `idToken` and `userInfo` properties cannot both be set to `false`. At least one of these properties must have a value of `true`.                                                                                                                                                 |
| `oidcScopes`     | List    | Optional | Mutable   | OIDC resource scope IDs that this attribute mapping is available for exclusively. This setting overrides any global OIDC resource scopes that contain an attribute mapping with the same name. The list can contain only scope IDs that have been granted for the application through the `/grants` endpoint. A null value is accepted for backwards compatibility. However, an empty set is invalid, and one scope ID is expected. If null, the response includes this mapping in the `openid` scope.                    |

## OIDC application core mapping attributes

| Property | Type   | Required | Mutable | Description                                                                                                                                                                    |
| -------- | ------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sub`    | String | Required | Mutable | A string that specifies the core OIDC application mapping attribute. The default user attribute value is `${user.id}` and the `required` property value must be set to `true`. |

## SAML application core mapping attributes

| Property       | Type   | Required | Mutable | Description                                                                                                                                                        |
| -------------- | ------ | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `saml_subject` | String | Required | Mutable | A string that specifies the core SAML mapping attribute. The default user attribute value is `${user.id}` and the `required` property value must be set to `true`. |

|   |                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------- |
|   | The core attribute mapping is created automatically when the OpenID Connect or SAML application is created. |

## Application Attribute events generated

Refer to [Audit Reporting Events](../../reference/audit-reporting-events.html) for the events generated.

### Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | An unexpected error occurred.                                         |

## Application attribute mapping errors

In addition to the general [error codes](../../reference/error-codes.html), application attribute mapping operations can return the following errors:

| HTTP status | Top‑level code    | Detail code            | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | ----------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_REQUEST` | `INVALID_VALUE`        | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** The application's protocol does not support application attributes
>
> **Details:**
>
> ```
> Attributes are only supported for applications with protocols [SAML, OPENID_CONNECT] and not applicable to the '<protocol>' application [<appID> - <appName>] in environment '<envID>
> ```                                                                                                                                                                |
| 400         | `INVALID_DATA`    | `UNIQUENESS_VIOLATION` | **Message:** Identifies the conflicting mapping name.> **Collapse: When and details**
>
> **When:** A custom mapping name duplicates an existing mapping or a reserved core mapping name
>
> **Details:** `name already exists`                                                                                                                                                                                                                                                                                                                                                                 |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request violates a constraint imposed by the service.`> **Collapse: When and details**
>
> **When:** Creating or updating a mapping would exceed the application's maximum number of mappings (100)
>
> **Details:** `Application has reached maximum amount of attributes: Application '<appID>' in Environment '<envID>'`                                                                                                                                                                                                                                                   |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** The mapping name is reserved or is invalid for the application's protocol
>
> **Details:** Describes the invalid name.                                                                                                                                                                                                                                                                                                                      |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** For an invalid expression, describes the rejected reference, such as `Unsupported property / object reference - [<expression>] are not allowed for this expression.`; for an invalid name format, `Validation Error : [nameFormat is not valid]`> **Collapse: When and details**
>
> **When:** A mapping expression or name format is invalid
>
> **Details:** For an expression, `expression not valid`; for a name format, `is not valid`                                                                                                                                        |
| 400         | `INVALID_DATA`    | `EMPTY_VALUE`          | **Message:** `Validation Error : [value must not be blank]`> **Collapse: When and details**
>
> **When:** A mapping value is empty or null where the protocol does not allow it — SAML and WS‑Federation mappings reject blank values regardless of `required`, and OIDC core mappings reject empty or null values
>
> **Details:** `must not be blank`. OIDC custom mappings allow empty values when `required` is false; with `required: true` a blank value uses the separate constraint‑violation response.                                                                                 |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** An OIDC mapping configuration is inconsistent: both `idToken` and `userInfo` are false, `oidcScopes` is empty or ungranted, or a required custom mapping has an empty value
>
> **Details:** `Attribute userInfo must be true if idToken is false.`, `oidcScopes must be null or contain at least one item`, `oidcScopes contains an invalid scope which has not been granted for the application`, or `value cannot be blank when required is set` |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`        | **Message:** Identifies the core mapping and the rejected property or value.> **Collapse: When and details**
>
> **When:** An update changes the immutable `name` or `required` property of a core mapping, or supplies a literal value for a core mapping
>
> **Details:** `property cannot be changed` or `Core attribute cannot have literal/static values`                                                                                                                                                                                                                                  |
| 400         | `REQUEST_FAILED`  | `CONSTRAINT_VIOLATION` | **Message:** Identifies the unsupported operation and mapping.> **Collapse: When and details**
>
> **When:** `DELETE /attributes/{attributeID}` targets a core mapping
>
> **Details:** `operation not supported`                                                                                                                                                                                                                                                                                                                                                                               |
| 403         | `ACCESS_FAILED`   | None                   | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `applications:read:application` permission (the `GET` operations), the `applications:update:application` permission (the `POST` and `PUT` operations), or the `applications:delete:application` permission (the `DELETE` operation)
>
> **Details:** None.                                                                                                                                                                                      |
| 404         | `NOT_FOUND`       | None                   | **Message:** Identifies the application and environment.> **Collapse: When and details**
>
> **When:** The application does not exist, or is a self‑service, admin console, or application portal application (applies to all application attribute mapping operations)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                  |
| 404         | `NOT_FOUND`       | None                   | **Message:** Identifies the attribute mapping, application, and environment.> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /attributes/{attributeID}` references an attribute mapping that does not exist
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                       |

---

---
title: Application Flow Policy Assignments
description: Manage which PingOne DaVinci flow policies are assigned to an application and how their priority controls the authentication flow
component: pingone-api
page_id: pingone-api:platform:applications/application-flow-policy-assignments/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/applications/application-flow-policy-assignments/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  no-flow-policy-assignments: No flow policy assignments
  one-flow-policy-assignment: One flow policy assignment
  two-or-more-flow-policy-assignments: Two or more flow policy assignments
  flow-policies-and-the-pingone-application-portal: Flow policies and the PingOne application portal
  application-flow-policy-assignments-data-model: Application flow policy assignments data model
  flow-policy-events-generated: Flow Policy events generated
  response-codes: Response codes
  application-flow-policy-assignment-errors: Application flow policy assignment errors
---

# Application Flow Policy Assignments

Flow policy assignment endpoints manage the flow policies associated with the specified application. An application can have zero or more flow policies assigned to it that determine how users are authenticated. The number of flow policies assigned to an application also controls how the authentication flow progresses.

## No flow policy assignments

Applications that have no flow policy assignments use the environment resource's default sign-on policy to authenticate users (or a designated sign-on policy assignment).

## One flow policy assignment

Applications that have one flow policy assignment always use that flow policy to authenticate users.

## Two or more flow policy assignments

If an application has two or more assigned flow policies, the authentication flow uses the flow policy with the highest priority (priority 1) first. If authentication is successful, the flow is complete. If authentication fails, the flow initiates the flow policy with the next highest priority. The flow continues until one of the assigned flow policies completes successfully or all policies have been tried and failed.

OIDC applications can request a lower-priority policy by using the `acr_values` OIDC parameter with the desired PingOne authentication name or DaVinci flow policy ID. Refer to [OpenID Connect/OAuth2 data model](../applications-1/index.html#applications-oidc-settings-data-model).

SAML applications can request a lower-priority policy by sending a SAML 2.0 authentication request with the `RequestedAuthnContext` parameter, where the value indicates the desired PingOne authentication name or DaVinci flow policy ID. Note that the `enableRequestAuthnContext` must be set to `true` for the SAML application. Refer to [SAML settings data model](../applications-1/index.html#applications-saml-settings-data-model).

## Flow policies and the PingOne application portal

If the PingOne application portal is not configured with any flow policies, it will use the default PingOne policy.

You can apply policies other than the default to the PingOne application portal by appending the `policy` query parameter to your Application Portal Home Page URL. For example, the Home Page URL `https://apps.pingone.com/<envID>/myapps/` would become `https://apps.pingone.com/<envID>/myapps/?policy=<value>`, where `<value>` is the name of a configured PingOne policy, or the ID of a configured DaVinci flow policy. If the policy name or ID doesn't match any configured policy, then PingOne returns an error.

## Application flow policy assignments data model

| Property         | Type    | Required | Mutable   | Description                                                                                                                                                                                     |
| ---------------- | ------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `application.id` | String  | Required | Read only | A string that specifies the application resource ID associated with the flow policy assignment.                                                                                                 |
| `environment.id` | String  | Required | Read only | A string that specifies the environment associated with the application.                                                                                                                        |
| `flowPolicy.id`  | String  | Required | Mutable   | A string that specifies the flow policy resource ID associated with the flow policy assignment.                                                                                                 |
| `id`             | String  | Required | Read only | A string that specifies the flow policy assignment resource's unique identifier.                                                                                                                |
| `priority`       | Integer | Required | Mutable   | The order in which the policy referenced by this assignment is evaluated during an authentication flow relative to other policies. An assignment with a lower priority will be evaluated first. |

## Flow Policy events generated

Refer to [Audit Reporting Events](../../reference/audit-reporting-events.html) for the events generated.

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | An unexpected error occurred.                                         |

## Application flow policy assignment errors

In addition to the general [error codes](../../reference/error-codes.html), application flow policy assignment operations can return the following errors:

| HTTP status | Top‑level code     | Detail code                      | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------- | ------------------ | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`     | `UNIQUENESS_VIOLATION`           | **Message:**```
Flow policy '<flowPolicyId>' cannot be assigned to the application '<applicationId>' in environment '<environmentId>' multiple times. Existing flow policy assignment id is '<existingAssignmentId>'
```> **Collapse: When and details**
>
> **When:** Creating or updating an assignment would assign the same flow policy to the application more than once
>
> **Details:** `flow policy already assigned to the application`, with target `flowPolicy.id` and `innerError.existingId` identifying the existing assignment |
| 400         | `INVALID_DATA`     | `EMPTY_VALUE` or `INVALID_VALUE` | **Message:** `Validation Error : <field errors>`> **Collapse: When and details**
>
> **When:** The request body omits `flowPolicy`, `flowPolicy.id`, or `priority`, or sets `priority` to less than `1`
>
> **Details:** Describes the failing property. A missing `priority` value returns `EMPTY_VALUE`, while a `priority` below `1` returns `INVALID_VALUE`.                                                                                                                                                                              |
| 400         | `INVALID_REQUEST`  | None                             | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A path identifier cannot be parsed as a UUID
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                       |
| 400         | `INVALID_REQUEST`  | None                             | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** The request body is missing or is not valid JSON syntax
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                         |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`                  | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A request body field cannot be converted to the expected type (for example, a non-UUID value where a UUID is expected)
>
> **Details:** `Invalid value for attribute.`, with target = the field path.                                                                                                                                                                                     |
| 400         | `REQUEST_FAILED`   | None                             | **Message:** Describes the downstream error.> **Collapse: When and details**
>
> **When:** DaVinci returns an HTTP error status other than 404 while resolving the flow policy during assignment create or update
>
> **Details:** None.                                                                                                                                                                                                                                                                                                      |
| 404         | `NOT_FOUND`        | None                             | **Message:** `Unable to find an active Flow Policy with ID: '<flowPolicyId>' in Environment '<environmentId>'`> **Collapse: When and details**
>
> **When:** Creating or updating an assignment references a flow policy that does not exist or is disabled
>
> **Details:** None.                                                                                                                                                                                                                                                            |
| 404         | `NOT_FOUND`        | None                             | **Message:**```
Unable to find Flow Policy Assignment with ID: '<assignmentId>' in Environment '<environmentId>' for Application '<applicationId>'
```> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /flowPolicyAssignments/{ID}` references an assignment that does not exist for the application
>
> **Details:** None.                                                                                                                                                                                            |
| 500         | `UNEXPECTED_ERROR` | None                             | **Message:** Describes the underlying failure.> **Collapse: When and details**
>
> **When:** Assignment mapping or storage processing fails after a request is accepted, or the DaVinci access token response is empty before resolving the flow policy
>
> **Details:** None.                                                                                                                                                                                                                                                                |

> **Collapse: Related topics**
>
> * [Flow Policies](../../flow-policies/index.html)

---

---
title: Application Management
description: Create and manage PingOne application connections, including application types, secrets, resource grants, sign-on policy assignments, role assignments, and attribute mapping
component: pingone-api
page_id: pingone-api:platform:application-management
canonical_url: https://developer.pingidentity.com/pingone-api/platform/application-management.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-06
page_aliases: ["platform:applications/application-management.adoc"]
section_ids:
  managing-applications: Managing applications
---

# Application Management

Application resources define the connection between PingOne and the actual application (also known as a client connection). The application type you choose to create includes default settings that you're free to change. For example, you can configure the settings for a Single-Page application to match the settings for a Web application. This is by design for maximum flexibility.

Learn more in [Applications](https://docs.pingidentity.com/pingone/applications/p1_application_types.html) in the PingOne admin guide.

When you make a request to create a new application, you must specify the `type` property that specifies one of the following application types:

* **Web application**

  A browser-based application with a server-side component, such as ASP, CGI, JSP/Java, Node.js, or Ruby on Rails applications.

* **Native application**

  An application that is installed and run directly on the local operating system, like Java, Objective-C, Swift, or React applications. Native applications are typically intended for mobile devices. These native applications are optionally configured using the `mobile` property.

* **Single-Page application**

  A browser-based application that runs on the front-end with no server-side component, such as Sencha Touch, AngularJS, and React applications. A single page application runs on the client side after it loads, so it cannot keep a client secret.

* **Non-interactive**

  A web application that does not require user interaction through the web browser, like a command line interface, a service, or a daemon.

* **Worker**

  An administrator application that can interact with platform APIs. Access to platform APIs is determined by the user's or application's role assignments. The role assignment for a Worker app is set by the `assignActorRoles` property.

* **Device authorization**

  Creating an application of this type initiates an action that returns an activation code to the end user. This enables you to obtain authorization from the end user through (what is typically) a mobile device.

* **Platform applications**

  PingOne creates platform applications (PingOne Admin Console, PingOne Application Portal, PingOne Self-Service - MyAccount, and PingFederate-SSO) when the environment is created. The PingFederate-SSO platform application is created only if the PingOne environment includes PingFederate, and unlike the other platform applications, PingFederate-SSO application information is not returned through a GET request.

These are the **default** `grantTypes`, `response_type`, and `tokenEndpointAuthMethod` attributes for the application types:

| Application type       | Grant type                   | Response type         | Token endpoint authentication method |
| ---------------------- | ---------------------------- | --------------------- | ------------------------------------ |
| Device Authorization   | DEVICE_CODE, REFRESH_TOKEN   | N/A                   | NONE                                 |
| Native                 | AUTHORIZATION_CODE, IMPLICIT | TOKEN, ID_TOKEN, CODE | NONE                                 |
| Single-page            | IMPLICIT                     | TOKEN, ID_TOKEN       | NONE                                 |
| Web                    | AUTHORIZATION_CODE           | CODE                  | CLIENT_SECRET_BASIC                  |
| Worker/Non-interactive | CLIENT_CREDENTIALS           | TOKEN                 | CLIENT_SECRET_BASIC                  |

|   |                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For any application type (except Worker/Non-interactive), you can specify either `NONE`, `CLIENT_SECRET_BASIC`, or `CLIENT_SECRET_POST` as the `tokenEndpointAuthMethod` attribute value. Non-interactive applications use the `CLIENT_CREDENTIALS` grant type, which does not support a `tokenEndpointAuthMethod` value of `NONE`. |

## Managing applications

The base endpoint, `/v1/environments/{{envID}}/applications`, provides endpoint operations to create, read, update, and delete OIDC and SAML application connections. There are `POST` request examples to show the required properties to create each type of application connection. For more information, refer to [Application Operations](applications/applications-1/index.html).

The secret endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/secret`, provides endpoint operations to read and update the application's secret, if the requesting actor has a superset of the application's role assignments. For more information, refer to [Application Secret](applications/application-secret/index.html).

Applications support the following additional configuration properties:

* **Application resource grants**

  The application resource grants endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/grants`, provides endpoint operations to create, read, update, and delete the resource grant associated with the application connection. For more information, refer to [Application Resource Grants](applications/application-resource-grants/index.html).

* **Application sign-on policy assignments**

  The application sign-on policy assignments endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/signOnPolicyAssignments`, provides endpoint operations to create, read, update, and delete the sign-on policies associated with the application connection. For more information, refer to [Application Sign-On Policy Assignments](applications/application-sign-on-policy-assignments/index.html).

* **Application role assignments**

  The application role assignments endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/roleAssignments`, provides endpoint operations to create, read, update, and delete the role assignments associated with the application connection. For more information, refer to [Application Role Assignments](applications/application-role-assignments/index.html).

* **Application attribute mapping**

  The application attribute mapping endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/roleAssignments`, lets you customize the content of an ID token or a SAML assertion by adding custom attributes and their values. For more information, refer to [Application Attribute Mapping](applications/application-attribute-mapping/index.html).

* **Application MFA push credentials**

  Push credentials are required for sending push notifications to a native application. The endpoint, `/v1/environments/{{envID}}/applications/{{appID}}/pushCredentials`, provides endpoint operations to create, read, update, and delete the push credentials associated with the application connection. This section provides examples for both `APNS` and `FCM` push credential types. For more information, refer to [Application MFA Push Credentials](applications/application-mfa-push-credentials/index.html).

> **Collapse: Related topics**
>
> * [Authorization and authentication by application type](../foundations/authentication-concepts/authorization-and-authentication-by-application-type/index.html)
>
> * [Applications](https://docs.pingidentity.com/pingone/applications/p1_application_types.html)

---

---
title: Application Metadata
description: Manage custom JSON metadata properties for a PingOne application, such as contact details or other administrative information
component: pingone-api
page_id: pingone-api:platform:applications/application-metadata/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/applications/application-metadata/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  applications-metadata-data-model: Applications metadata data model
  response-codes: Response codes
  application-metadata-errors: Application metadata errors
---

# Application Metadata

The application metadata endpoints allow administrators to manage custom JSON properties for their apps, providing a flexible way to store attributes that aren't natively modeled. This metadata can be used for administrative purposes, such as storing contact details or other relevant information about the application.

## Applications metadata data model

| Property        | Type      | Required | Mutable   | Description                                                                                                                                              |
| --------------- | --------- | -------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `metadata`      | JSON blob | Required | Mutable   | User-defined custom metadata. The metadata must be a JSON object, and can include any custom properties that you want to associate with the application. |
| `applicationId` | String    | Required | Read-only | A string that specifies the application resource ID.                                                                                                     |
| `environmentId` | String    | Required | Read-only | A string that specifies the environment associated with the application.                                                                                 |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | Unexpected server error.                                              |

## Application metadata errors

In addition to the general [error codes](../../reference/error-codes.html), application metadata operations can return the following errors:

| HTTP status | Top‑level code     | Detail code            | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | ------------------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_REQUEST`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** Application metadata is not enabled for the environment (applies to `GET`, `PUT`, and `POST` metadata operations)
>
> **Details:** `Application metadata is not yet available for your environment`                                                                                                                                                                                                                                                                                                               |
| 400         | `INVALID_REQUEST`  | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** The application type does not support metadata (applies to `GET`, `PUT`, and `POST` metadata operations) — PingID applications and platform‑managed application types such as self‑service, admin console, portal, template, portal‑link, and MCP server applications
>
> **Details:** Detail `CONSTRAINT_VIOLATION` with target `type`: `Metadata is not available for applications of type: <type>` for platform‑managed types, or `Metadata is not available for PingID applications` for PingID applications. |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`        | **Message:** The constraint‑violation text in the form `<propertyPath> <message>.` with a trailing space after the period (for example, `metadata must be smaller than 10 KB.` followed by a trailing space)> **Collapse: When and details**
>
> **When:** The serialized metadata object exceeds 10 KB
>
> **Details:** Detail `INVALID_VALUE` with target `metadata` and message `must be smaller than 10 KB`                                                                                                                                                                                                                                          |
| 400         | `INVALID_DATA`     | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** The `metadata` property cannot be deserialized as a JSON object (a request body that is malformed JSON or supplies a value of the wrong type)
>
> **Details:** The raw deserialization message with target = the JSON field path.                                                                                                                                                                                                                                                                    |
| 404         | `NOT_FOUND`        | None                   | **Message:** `Unable to find Application with ID: '<applicationId>' in Environment '<environmentId>'`> **Collapse: When and details**
>
> **When:** The application does not exist in the environment (applies to `GET`, `PUT`, and `POST` metadata operations)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                   |
| 415         | `INVALID_REQUEST`  | None                   | **Message:** The standard unsupported‑media‑type message.> **Collapse: When and details**
>
> **When:** A metadata `GET`, `PUT`, or `POST` request supplies an unsupported `Content-Type`, such as `text/html` (the metadata endpoints accept `application/json` and `application/hal+json`)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                      |
| 500         | `UNEXPECTED_ERROR` | None                   | **Message:** `There was an unexpected error with the service. Please try again later.`> **Collapse: When and details**
>
> **When:** Previously stored metadata cannot be parsed as JSON when read for a `GET` or `PUT` operation
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                 |

---

---
title: Application MFA Push Credentials
description: Create, read, update, and delete APNs, FCM, and HMS push credentials used to send push notifications to a PingOne native application
component: pingone-api
page_id: pingone-api:platform:applications/application-mfa-push-credentials/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/applications/application-mfa-push-credentials/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  mfa-push-credentials-data-model: MFA push credentials data model
  response-codes: Response codes
  application-mfa-push-credential-errors: Application MFA push credential errors
---

# Application MFA Push Credentials

Push credentials are required for the purpose of sending push notifications to a native application. Push credentials must be defined for the application.

The push credentials endpoint implements functions to create, read, update and delete the push credentials associated with native application resources.

There are three types of push credentials:

* `APNS` (Apple)

* `FCM_HTTP_V1` (Google)

* `HMS` (Huawei)

The `FCM` type, used previously for Google Play-based applications, is no longer supported. Use `FCM_HTTP_V1` instead.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | The request bodies, their mandatory properties, and responses vary according to the push credential type. |

## MFA push credentials data model

| Property                        | Type   | Required | Mutable   | Description                                                                                                                                                                        |
| ------------------------------- | ------ | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type                            | String | Required | Immutable | Specifies the push credential type. Valid values:\* `APNS` (for Apple)\* `FCM_HTTP_V1` (for Google)\* `HMS` (for Huawei)\* `FCM` (no longer supported, used previously for Google) |
| clientId                        | String | Required | Immutable | Used only if `type` is set to `HMS`. OAuth 2.0 Client ID from the Huawei Developers API console.                                                                                   |
| clientSecret                    | String | Required | Immutable | Used only if `type` is set to `HMS`. The client secret associated with the OAuth 2.0 Client ID.                                                                                    |
| googleServiceAccountCredentials | String | Required | Immutable | Used when `type` is set to `FCM_HTTP_V1`. The value should be the contents of the JSON file that represents your Service Account Credentials (the Firebase Admin SDK private key). |
| key                             | String | Required | Immutable | Used when `type` is set to `APNS`. The value should be the key ID. Before the deprecation of the `FCM` type, this was also used for the server key.                                |
| teamId                          | String | Required | Immutable | Used only if `type` is set to `APNS`. Used to identify teams.                                                                                                                      |
| token                           | String | Required | Immutable | Used only if `type` is set to `APNS`. Used as the authentication token signing key to securely connect to APNS. This is a p8 file with a private key format.                       |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | Unexpected server error.                                              |

## Application MFA push credential errors

In addition to the general [error codes](../../reference/error-codes.html), application MFA push credential operations can return the following errors:

| HTTP status | Top‑level code    | Detail code             | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------- | ----------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`    | `EMPTY_VALUE`           | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /pushCredentials` request omits a property required for the credential type: `key`, `token`, or `teamId` for `APNS`, `clientId` or `clientSecret` for `HMS`, or `googleServiceAccountCredentials` for `FCM_HTTP_V1`
>
> **Details:** `must not be blank`, for example `Validation Error : [token must not be blank]`                                                                                                 |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`         | **Message:** `Validation Error : [customProvider must have an id]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /pushCredentials` request supplies a `customProvider` relationship without an `id`
>
> **Details:** `must have an id`                                                                                                                                                                                                                                                                                      |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`         | **Message:** `Validation Error : [<property> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /pushCredentials` request supplies a credential value that fails format validation: an APNS `token` that is not a PKCS8 private key, or `googleServiceAccountCredentials` that is not a valid Google service account key file
>
> **Details:** `must be a valid PKCS8 private key` or `Google Service Account Credentials are not valid`, for example `Validation Error : [token must be a valid PKCS8 private key]` |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`         | **Message:** `Invalid value for attribute.`> **Collapse: When and details**
>
> **When:** A `POST /pushCredentials` request creates credentials of a type that the application already has (each application can have only one set of credentials per type)
>
> **Details:** `<type> credentials already exists in environment '<environmentId>' for application <applicationId>`, with target `type` and the existing credentials ID in `innerError.existingId`                                                                             |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`         | **Message:** `Invalid value for attribute.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /pushCredentials` request uses the `FCM` type, which is no longer supported
>
> **Details:** `Push Credentials of type FCM are not supported`, with target `type`                                                                                                                                                                                                                                                                 |
| 400         | `INVALID_DATA`    | `INVALID_VALUE`         | **Message:**```
Property 'type' is immutable and cannot be changed on push credentials '<pushCredentialsId>' in environment '<environmentId>', application '<applicationId>'
```> **Collapse: When and details**
>
> **When:** A `PUT /pushCredentials/{ID}` request changes the `type` of the existing credentials
>
> **Details:** `property cannot be changed`                                                                                                                                                                            |
| 400         | `INVALID_REQUEST` | None                    | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A path identifier cannot be parsed as a UUID. The top‑level code is `INVALID_REQUEST` even though the message text is the `INVALID_DATA` default message.
>
> **Details:** None.                                                                                                                                                                                                         |
| 400         | `INVALID_REQUEST` | `INVALID_VALUE` or None | **Message:** `The request could not be completed. The request was malformed or invalid.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /pushCredentials` request body cannot be deserialized as one of the supported credential types (`APNS`, `FCM_HTTP_V1`, `HMS`)
>
> **Details:** For a JSON field conversion error, the target is the field path. Otherwise no detail is returned.                                                                                                                                     |
| 403         | `ACCESS_FAILED`   | None                    | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `applications:read:pushCredentials` permission (`GET` operations), the `applications:create:pushCredentials` permission (`POST`), the `applications:update:pushCredentials` permission (`PUT`), or the `applications:delete:pushCredentials` permission (`DELETE`)
>
> **Details:** None.                                                                                                    |
| 404         | `NOT_FOUND`       | None                    | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** The application ID in the request URL does not exist (applies to all operations)
>
> **Details:** None.                                                                                                                                                                                                                                                                                               |
| 404         | `NOT_FOUND`       | None                    | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /pushCredentials/{ID}` references push credentials that do not exist for the application
>
> **Details:** None.                                                                                                                                                                                                                                                              |
| 404         | `NOT_FOUND`       | `INVALID_VALUE`         | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /pushCredentials` request references a custom provider through `customProvider.id` that does not exist
>
> **Details:** `PushDeliverySettings resource not found, id=<customProviderId>`                                                                                                                                                                                             |

---

---
title: Application Operations
description: Create, read, update, and delete PingOne application resources across OIDC, SAML, and WS-Federation protocols, including CORS configuration
component: pingone-api
page_id: pingone-api:platform:applications/applications-1/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/applications/applications-1/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  cors-support: Cross-origin resource sharing
  migrate-oidc-apps: Importing external OIDC applications to PingOne
  applications-data-models: Applications data models
  applications-base-data-model: Applications base data model
  applications-oidc-settings-data-model: Applications OIDC settings data model
  oidc-self-service: Applications OIDC settings data model for PING_ONE_SELF_SERVICE
  oidc-app-portal: Applications OIDC settings data model for PING_ONE_PORTAL
  applications-saml-settings-data-model: Applications SAML settings data model
  applications-saml-settings-metadata-model: Applications SAML metadata settings data model
  applications-ws-federation-settings-data-model: Applications WS-Federation settings data model
  applications-ws-federation-settings-hybrid-join: Applications WS-Federation settings data model for Microsoft Entra ID hybrid join
  pingid-mobile-app-configuration-data-model: PingID mobile app configuration data model
  application-events-generated: Application events generated
  response-codes: Response codes
  application-errors: Application errors
---

# Application Operations

The Applications service implements operations to create, read, update, and delete, applications resources.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | You need the Client Application Developer role to perform operations on application resources. |

Refer also to [Authorization and authentication by application type](../../../foundations/authentication-concepts/authorization-and-authentication-by-application-type/index.html)

## Cross-origin resource sharing

PingOne supports cross-origin resource sharing (CORS), which gives applications running at different domains permission to access resources on PingOne servers. For example, an application at https\://myapp.com that uses PingOne to authenticate users needs to request permission to access resources at https\://auth.pingone.com before authentication operations are executed. In this case, a request is made to the resource owner (auth.pingone.com) from the requestor (myapp.com) using CORS headers to ask for access privileges. The response from auth.pingone.com returns the CORS `Access-Control-Allow-Origin` header with a value that confirms the requestor's access rights.

PingOne servers are configured to trust all origins when using access tokens. However, when requesting sensitive resources that use PingOne session cookies for authentication, only specified origins will be trusted. The following endpoints require session cookies for authentication, and only the origins specified in the application's `corsSettings` property will be trusted when calling these endpoints:

```text
/{envId}/as/authorize
/{envId}/as/resume
/{envId}/as/signoff
/{envId}/rp/authenticate
/{envId}/rp/callback/{callbackId}
/{envId}/saml20/idp/sso
/{envId}/saml20/idp/startsso
/{envId}/saml20/resume
/{envId}/saml20/idp/slo
/{envId}/wsf/sts/{appId}
/{envId}/wsf/mex/{appId}
/{envId}/wsf/prp/{appId}
/{envId}/wsf/prp/resume
```

When using session cookies for authentication, no origins will be trusted when calling these endpoints:

```text
/{envId}/as/txs
/{envId}/saml20/sp/sso
/{envId}/saml20/sp/acs
/{envId}/saml20/sp/jwtacs
```

Consequently, when defining an application's connection to PingOne, you generally do not need to add your application's domain to a list of trusted origins. Cross-origin requests that use HTTP methods to modify the resource, such as `PUT`, `PATCH`, `POST`, and `DELETE`, trigger a preflight request to ensure that the initial request can be sent. The browser initiates a preflight HTTP `OPTIONS` request to verify that the HTTP method used in the actual request is allowed. In these cases, the response from auth.pingone.com to the preflight request returns a response with the CORS `Access-Control-Allow-Methods` header to specify the allowed methods.

When making CORS requests, only these headers can be used:

* `Accept`

* `Accept-Language`

* `Content-Language`

* `Content-Type`

* `Range`

* `Authorization`

* `Content-Length`

* `Cookie`

* `Correlation-Id`

* `Origin`

* `Origin-Cookies`

* `Referer` or `Referrer`

* `X-Amz-Date`

* `X-Amz-Security-Token`

* `X-Api-Key`

* `X-client-version`

* `X-Content-Type-Options`

When accessing CORS responses, you're restricted to reading only the `Correlation-Id` header (as well as the request body).

Attempting to submit or access headers that are not listed above may prevent you from making CORS requests or reading the responses.

## Importing external OIDC applications to PingOne

Environment Admins can import OIDC applications to PingOne, preserving the existing application client ID and client secret. This enables you to:

* Replicate OIDC application records that have been created in another platform.

* Recover from an accidental deletion of an OIDC application. You can create a new application record using the client ID and client secret of the deleted application.

Import of OIDC applications is supported only by [Import Application (OIDC Protocol)](import-application-oidc.html), and specifying `clientId` and `clientSecret` in the request body. You're also able to import external resources to PingOne. Refer to [Importing external resources to PingOne](../../resources/resources-1/index.html#migrate-resources) for more information.

## Applications data models

The following applications properties tables show the base data model for properties that apply to all application protocols, and the specific properties for the OpenID Connect (OIDC), SAML, and WS-Federation application protocols.

### Applications base data model

| Property                     | Type      | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `accessControl.role.type`    | String    | Optional | Mutable   | The user role required to access the application. Options are `ADMIN_USERS_ONLY`. A user is an admin user if the user has one or more of the following roles: Organization Admin, Environment Admin, Identity Data Admin, or Client Application Developer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `accessControl.group.type`   | String    | Optional | Mutable   | The group type required to access the application. Options are `ANY_GROUP` (the actor must belong to at least one group listed in the `accessControl.group.groups` property) and `ALL_GROUPS` (the actor must belong to all groups listed in the `accessControl.group.groups` property).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `accessControl.group.groups` | String\[] | Optional | Mutable   | The group IDs for the groups the actor must belong to for access to the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `createdAt`                  | Date      | N/A      | Read-only | The time the resource was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `description`                | String    | Optional | Mutable   | The description of the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `enabled`                    | Boolean   | Required | Mutable   | The current enabled state of the application. Options are `true` (enabled) or `false` (disabled).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `environment.id`             | String    | Required | Read-only | The PingOne environment associated with the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `externalId`                 | String    | Optional | Mutable   | For applications whose `type` is PORTAL_LINK_APP, you can use `externalId` to specify an external ID that should be used for the application in contexts such as targeted risk policies. Note that PORTAL_LINK_APP applications that do not have an external ID specified are not displayed in the list of applications when defining a targeted risk policy in the UI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `hiddenFromAppPortal`        | Boolean   | Optional | Mutable   | Whether the application is hidden in the application portal despite the configured group access policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `homePageUrl`                | String    | Optional | Mutable   | The custom home page URL for the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `icon`                       | Object    | Optional | Mutable   | The HREF and the ID for the application icon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `id`                         | String    | Required | Read-only | The application UUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `loginPageUrl`               | String    | Optional | Mutable   | The custom login page URL for the application. If you set the `loginPageUrl` property for applications in an environment that sets a custom domain, the URL should include the top-level domain and at least one additional domain level. **Warning:** To avoid issues with third-party cookies in some browsers, a custom domain must be used, giving your PingOne environment the same parent domain as your authentication application. For more information about custom domains, refer to [Custom domains](../../custom-domains/index.html). If a `loginPageUrl` value is not specified, the OIDC app resource includes a Ping-provided login page at `https://{{apps domain}}/{{envId}}/signon/` or `https://{{custom domain}}/signon/`. If a PingOne authentication session exists and the sign-on policy does not indicate that re-authentication is needed, a login page is not displayed (either Ping-provided or custom). |
| `name`                       | String    | Required | Mutable   | The name of the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `protocol`                   | String    | Required | Immutable | The protocol used by the application. Options are `OPENID_CONNECT`, `SAML`, `WS_FED`, and `EXTERNAL_LINK`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `type`                       | String    | Required | Immutable | The application type. Options are `WEB_APP`, `NATIVE_APP`, `SINGLE_PAGE_APP`, `SERVICE`, `AI_AGENT`, `CUSTOM_APP`, `WORKER`, `PING_ONE_SELF_SERVICE`, `PING_ONE_ADMIN_CONSOLE`, `PING_ONE_PORTAL`, `TEMPLATE_APP`, and `PORTAL_LINK_APP`. The `AI_AGENT` type is required when you have the Agent IAM Core license package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `updatedAt`                  | Date      | N/A      | Read-only | The time the resource was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Applications OIDC settings data model

| Property                                                         | Type      | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------- | --------- | -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additionalRefreshTokenReplayProtectionEnabled`                  | Boolean   | Optional | Mutable   | PingOne detects a replay attack when a refresh token is reused outside of its specified grace period (refer to below for information on `refreshTokenRollingGracePeriodDuration`). If the refresh token is revoked because of a replay attack, then PingOne also revokes any associated access tokens if, and only if, this setting is enabled. Setting this property to null equates to a false setting. For more information about refresh token rotation, refer to [Refresh token rotation](https://docs.pingidentity.com/pingone/applications/p1_refresh_token_rotation.html) in the PingOne admin guide.                                                                                                                                                                                                                                                     |
| `allowWildcardInRedirectUris`                                    | Boolean   | Optional | Mutable   | Whether wildcards are allowed in redirect URIs. For more information, refer to [Wildcards in Redirect URIs](https://docs.pingidentity.com/pingone/applications/p1_wildcard_redirect_uri.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `assignActorRoles`                                               | Boolean   | Optional | Mutable   | Indicates whether the permissions service should assign to the application the roles of the actor creating the application (defaults to true). This property is set only on the `POST` request. The property is ignored when included in a `PUT` request. **Best Practice**: When creating a Worker app, the best practice is to set this value to false. This is for security purposes, to ensure you assign only the minimal set of permissions necessary for the Worker app.                                                                                                                                                                                                                                                                                                                                                                                   |
| `clientId`                                                       | String    | Optional | Immutable | (Required when `clientSecret` is specified.) Supported only for POST operations. If a client ID exists for an external application that's being imported to PingOne, this identifier can be set here. This must be a minimum of 8 alpha-numeric characters (maximum 256), and must be unique to the PingOne environment in which the application is being imported. If a client ID for an external application doesn't exist when it's imported to PingOne, the `id` value automatically generated for the application is used as the identifier, and only for configuration endpoints. You can use only `clientId` to authenticate.                                                                                                                                                                                                                              |
| `clientSecret`                                                   | String    | Optional | Immutable | Supported only for POST operations. This is the client secret associated with `clientId` for an external application that is being migrated to PingOne. This must be a minimum of 8 alpha-numeric characters, and a maximum of 1024 characters. This value is encrypted by PingOne, and returned by the POST, GET, and PUT requests. When a client secret is not provided, PingOne generates a client secret as part of the application-creation process. In this case, you'll need to update the generated client secret with a new one using [Update Application Secret](../application-secret/update-application-secret.html).                                                                                                                                                                                                                                 |
| `corsSettings`                                                   | Object    | Optional | Mutable   | Enables you to customize how the Authorization and Authentication APIs interact with CORS requests that reference the application. If omitted, the application allows CORS requests from any origin except for operations that expose sensitive information (such as, operations from `/as/authorize` and `/as/token`). We recommend you use `corsSettings`, rather than omitting this property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `corsSettings.behavior`                                          | String    | Required | Mutable   | Options are "ALLOW_NO_ORIGINS" and "ALLOW_SPECIFIC_ORIGINS". ALLOWS_NO_ORIGINS rejects all CORS requests. ALLOW_SPECIFIC_ORIGINS rejects all CORS requests except those listed in `corsSettings.origins`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `corsSettings.origins`                                           | String\[] | Optional | Mutable   | This must be specified when `corsSettings.behavior` is ALLOW_SPECIFIC_ORIGINS, and must be omitted or empty when `corsSettings.behaviour` is ALLOW_NO_ORIGINS. Limited to 40 values. The values are the origins from which CORS requests to the Authorization and Authentication APIs are allowed. Each value is an HTTP or HTTPS URL without a path. The host may be a domain name (including localhost), or an IPv4 address. Subdomains can be specified using the wildcard (\*) to match any string.                                                                                                                                                                                                                                                                                                                                                           |
| `devicePathId`                                                   | String    | Optional | Mutable   | A string that specifies a unique identifier within an environment for a device authorization grant flow to provide a short identifier to the application. This property is ignored when the `deviceCustomVerificationUri` property is configured. The string can contain any letters, numbers, and some special characters (regex: `a-zA-Z0-9_-`). It can have a length of no more than 50 characters (`min/max=1/50`).                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `deviceCustomVerificationUri`                                    | String    | Optional | Mutable   | A string that specifies an optional custom verification URI that is returned for the `/device_authorization` endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `deviceTimeout`                                                  | Integer   | Required | Mutable   | An integer that specifies the length of time (in seconds) that the `userCode` and `deviceCode` returned by the `/device_authorization` endpoint are valid. This property is required only for applications in which the `grantTypes` property is set to `device_code`. The default value is 600 seconds. It can have a value of no more than 3600 seconds (`min/max=1/3600`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `devicePollingInterval`                                          | Integer   | Required | Mutable   | An integer that specifies the frequency (in seconds) for the client to poll the `/as/token` endpoint. This property is required only for applications in which the `grantTypes` property is set to `device_code`. The default value is 5 seconds. It can have a value of no more than 60 seconds (`min/max=1/60`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `grantTypes`                                                     | String\[] | Optional | Mutable   | The grant type for the authorization request. Options are `authorization_code`, `implicit`, `refresh_token`, `device_code`, and `client_credentials`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `idpSignoff`                                                     | Boolean   | Optional | Mutable   | Set this to true to allow an application to request to terminate a user session using only the ID token. The application is not required to have access to the session token cookie. Refer to [GET IdP Signoff](../../../auth/openid-connect-oauth-2/authorization/idp-signoff.html) for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `includeTyp`                                                     | Boolean   | Optional | Mutable   | Specifies whether tokens signed for this application include the `typ` header with a value of `at+jwt`, regardless of whether the intended audience is the UserInfo endpoint, PingOne APIs, or custom resources. This specifies the JWT as an OAuth 2.0 access token for increased security. On March 2, 2027, PingOne will always include the `typ` header with a value of `at+jwt` when minting access token for the UserInfo endpoint, PingOne APIs, or custom resources. Learn more in [Access token claims](../../../foundations/authentication-concepts/access-tokens-and-id-tokens/token-claims.html#access-token-claims), [RFC 7519 section 5.1](https://datatracker.ietf.org/doc/html/rfc7519#section-5.1), and [RFC 9068 section 2.1](https://datatracker.ietf.org/doc/html/rfc9068#section-2.1).                                                       |
| `includeX5t`                                                     | Boolean   | Optional | Mutable   | Specifies whether tokens signed for this application include the `x5t` signature header in the signed JWT. Refer to [JSON Web Signature (JWS), section "x5t" (X.509 Certificate SHA-1 Thumbprint) Header Parameter](https://www.rfc-editor.org/rfc/rfc7515.html#section-4.1.7).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `initiateLoginUri`                                               | String    | Optional | Mutable   | The URI to use for third-parties to begin the sign-on process for the application. If specified, PingOne redirects users to this URI to initiate SSO to PingOne. The application is responsible for implementing the relevant OIDC flow when the initiate login URI is requested. This property is required if you want the application to appear in the PingOne Application Portal. Refer to the OIDC specification section [Initiating Login from a Third Party](https://openid.net/specs/openid-connect-core-1_0.html#ThirdPartyInitiatedLogin) for more information.                                                                                                                                                                                                                                                                                          |
| `jwks`                                                           | String    | Optional | Mutable   | A JWKS string that validates the signature of signed JWTs for applications that use the `PRIVATE_KEY_JWT` option for the `tokenEndpointAuthMethod`. This property is required when `tokenEndpointAuthMethod` is `PRIVATE_KEY_JWT` and the `jwksUrl` property is empty. For more information, refer to [Create a private_key_jwt JWKS string](../../../auth/auth-config-options/create-a-private-key-jwt-property-jwt.html). This property is also required if the optional `request` property JWT on the authorize endpoint is signed using the RS256 (or RS384, RS512) signing algorithm and the `jwksUrl` property is empty. For more infornmation about signing the `request` property JWT, refer to [Create a request property JWT](../../../auth/auth-config-options/create-a-request-property-jwt.html).                                                    |
| `jwksUrl`                                                        | String    | Optional | Mutable   | A URL (supports `https://` only) that provides access to a JWKS string that validates the signature of signed JWTs for applications that use the `PRIVATE_KEY_JWT` option for the `tokenEndpointAuthMethod`. This property is required when `tokenEndpointAuthMethod` is `PRIVATE_KEY_JWT` and the `jwks` property is empty. For more information, refer to [Create a private_key_jwt JWKS string](../../../auth/auth-config-options/create-a-private-key-jwt-property-jwt.html). This property is also required if the optional `request` property JWT on the authorize endpoint is signed using the RS256 (or RS384, RS512) signing algorithm and the `jwks` property is empty. For more infornmation about signing the `request` property JWT, refer to [Create a request property JWT](../../../auth/auth-config-options/create-a-request-property-jwt.html). |
| `kerberos.key`                                                   | Object    | Optional | Mutable   | A Relationship object containing the certificate issuer (root CA).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `kerberos.key.id`                                                | String    | Optional | Immutable | The unique identifier for the Kerberos key. Required if `kerberos.key` is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `mobile.appleTeamId`                                             | String    | Optional | Mutable   | If you set `mobile.integrityDetection.appleAppAttestSettings.enabled` to `true` to use Apple App Attest for device integrity checking, you must also set `mobile.appleTeamId` to the Team ID from your Apple Developer account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `mobile.bundleId`                                                | String    | Optional | Immutable | The bundle associated with the application, for push notifications in native apps. The value of the `bundleId` property is unique per environment, and once defined, is immutable. Used only for applications for the Apple ecosystem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `mobile.huaweiAppId`                                             | String    | Optional | Immutable | The unique identifier for the app on the device and in the Huawei Mobile Service AppGallery. The value of the `mobile.huaweiAppId` property is unique per environment, and once defined, is immutable. Used only for applications for the Huawei ecosystem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `mobile.huaweiPackageName`                                       | String    | Optional | Immutable | The package name associated with the application, for push notifications in native apps. The value of the `mobile.huaweiPackageName` property is unique per environment, and once defined, is immutable. Used only for applications for the Huawei ecosystem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `mobile.integrityDetection.mode`                                 | String    | Optional | Mutable   | Indicates whether device integrity detection takes place on mobile devices, for the application's enrollment and authentication events. The possible values are `ENABLED` or `DISABLED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `mobile.integrityDetection.excludedPlatforms`                    | Array     | Optional | Mutable   | You can enable device integrity checking separately for Android and iOS by setting `mobile.integrityDetection.mode` to ENABLED and then using this property to specify an ecosystem where you do not want to use device integrity checking. The possible values are `GOOGLE` and `IOS`. Note that this is implemented as an array even though currently you can only include a single value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `mobile.integrityDetection.appleAppAttestSettings.enabled`       | Boolean   | Optional | Mutable   | Set the value of `appleAppAttestSettings.enabled` to `true` if you have enabled device integrity checking for your iOS app and you want to use Apple App Attest for the check. If the value is set to `true`, you must also include a value for `mobile.appleTeamId`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `mobile.integrityDetection.googlePlay`                           | Object    | Optional | Mutable   | Object that contains the credentials required for using Google's Play Integrity API for integrity detection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `mobile.integrityDetection.googlePlay.verificationType`          | String    | Optional | Mutable   | The type of verification that should be used. The possible values are GOOGLE and INTERNAL. Using internal verification will not count against your Google API call quota. The value you select for `verificationType` determines what other parameters you must provide. When set to GOOGLE, you must provide `serviceAccountCredentials`. When set to INTERNAL, you must provide `decryptionKey` and `verificationKey`.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `mobile.integrityDetection.googlePlay.serviceAccountCredentials` | String    | Optional | Mutable   | Contents of the JSON file that represents your Service Account Credentials. This parameter must be provided if you have set `mobile.integrityDetection.googlePlay.verificationType` to GOOGLE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `mobile.integrityDetection.googlePlay.decryptionKey`             | String    | Optional | Mutable   | Play Integrity verdict decryption key from your Google Play Services account. This parameter must be provided if you have set `mobile.integrityDetection.googlePlay.verificationType` to INTERNAL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `mobile.integrityDetection.googlePlay.verificationKey`           | String    | Optional | Mutable   | Play Integrity verdict signature verification key from your Google Play Services account. This parameter must be provided if you have set `mobile.integrityDetection.googlePlay.verificationType` to INTERNAL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `mobile.integrityDetection.cacheDuration.amount`                 | Integer   | Optional | Mutable   | The duration between successful integrity detection calls. Every attestation request entails a certain time tradeoff. You can choose to cache successful integrity detection calls for a predefined duration, between a minimum of 1 minute and a maximum of 48 hours. If `mobile.integrityDetection.mode` is ENABLED, the cache duration must be set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `mobile.integrityDetection.cacheDuration.units`                  | String    | Optional | Mutable   | The time units used for `mobile.integrityDetection.cacheDuration.amount`. The possible values are `MINUTES` or `HOURS`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `mobile.packageName`                                             | String    | Optional | Immutable | The package name associated with the application, for push notifications in native apps. The value of the `mobile.packageName` property is unique per environment, and once defined, is immutable. Used only for applications for the Google ecosystem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `mobile.passcodeGracePeriod`                                     | Integer   | Optional | Mutable   | To cover time synchronization issues, you can use `passcodeGracePeriod` to customize the grace period during which the passcode can still be used even after the passcode has been refreshed. The value of the parameter should be the number of windows to use (min 1, max 10). In this context, a window is equal to the passcode refresh period in either direction. For example, if you defined a passcode refresh duration of 30 seconds and a grace period of 2 windows, the passcode is valid for 150 seconds (from 60 seconds behind the time of issue until 60 seconds past the expiration time). When `passcodeGracePeriod` is not included, the default value used is 5 windows.                                                                                                                                                                       |
| `mobile.passcodeRefreshDuration.duration`                        | Integer   | Optional | Mutable   | The amount of time a passcode should be displayed before being replaced with a new passcode. Must be between 30 and 60 (seconds).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `mobile.passcodeRefreshDuration.timeUnit`                        | String    | Optional | Mutable   | The type of time unit for `mobile.passcodeRefreshDuration.duration`. Currently, this must be SECONDS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `mobile.push.numberMatching.type`                                | String    | Optional | Mutable   | This option is used to specify the type of number matching that should be used in MFA policies where number matching has been enabled for the application (refer to the `numberMatching.enabled` parameter in [Device Authentication Policies](../../../mfa/device-authentication-policy/index.html)). The possible values are: \<li>SELECT_NUMBER - Users must select the correct number from a group of three numbers\</li> \<li>ENTER_MANUALLY - Users must enter the number that was shown\</li>                                                                                                                                                                                                                                                                                                                                                              |
| `mobile.uriPrefix`                                               | String    | Optional | Mutable   | A URI prefix that enables direct triggering of the mobile application when scanning a QR code. The URI prefix can be set to a universal link with a valid value (which can be a URL address that starts with `HTTP://` or `HTTPS://`, such as `https://www.acme.com`), or an app schema, which is just a string and requires no special validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `opSessionCheckEnabled`                                          | Boolean   | Optional | Mutable   | When enabled, PingOne includes the `session_state` parameter in the authentication response, per spec with [OpenID Connect Session Management 1.0](https://openid.net/specs/openid-connect-session-1_0.html). Refer to [OIDC Session Management](../../../foundations/authentication-concepts/oidc-session-management.html) in the Developer's Foundations for more information. This property is disabled by default.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `parRequirement`                                                 | Enum      | Optional | Mutable   | Whether pushed authorization requests (PAR) are required. Options are `REQUIRED` and `OPTIONAL`. The default value is `OPTIONAL`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `parTimeout`                                                     | Integer   | Optional | Mutable   | PAR timeout in seconds. Must be between `1` and `600`. The default value is `60`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `pkceEnforcement`                                                | String    | Optional | Mutable   | Specifies how PKCE request parameters are handled on the authorize request. Options are: `OPTIONAL`: PKCE code_challenge is optional and any code challenge method is acceptable. `REQUIRED`: PKCE code_challenge is required and any code challenge method is acceptable. `S256_REQUIRED`: PKCE code_challenge is required and the code_challenge_method must be `S256`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `postLogoutRedirectUris`                                         | String\[] | Optional | Mutable   | The URLs that the browser can be redirected to after logout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `redirectUris`                                                   | String\[] | Optional | Mutable   | The callback URI for the authentication response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `refreshTokenDuration`                                           | Integer   | Optional | Mutable   | The lifetime in seconds of the refresh token. If a value is not provided, the default value is 2592000, or 30 days. Valid values are between `60` and `2147483647`. If the `refreshTokenRollingDuration` property is specified for the application, then this property must be less than or equal to the value of `refreshTokenRollingDuration`. After this property is set, the value cannot be nullified. This value is used to generate the value for the `exp` claim when minting a new refresh token.                                                                                                                                                                                                                                                                                                                                                        |
| `refreshTokenRollingDuration`                                    | Integer   | Optional | Mutable   | The number of seconds a refresh token can be exchanged before re-authentication is required. If a value is not provided, the refresh token is valid forever. Valid values are between `60` and `2147483647`. After this property is set, the value cannot be nullified. This value is used to generate the value for the `exp` claim when minting a new refresh token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `refreshTokenRollingGracePeriodDuration`                         | Integer   | Optional | Mutable   | The number of seconds that a refresh token may be reused after having been exchanged for a new set of tokens. This is useful in the case of network errors on the client. Valid values are between 0 and 86400 seconds. Null is treated the same as 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `refreshTokenType`                                               | String    | Optional | Mutable   | Specifies the format of the refresh token. Options are `JSON_WEB_TOKEN` or `OPAQUE_TOKEN` (default). As opaque tokens are more secure and the recommended format, Ping Identity is shifting towards deprecating JWT tokens. For more information, refer to [Refresh Tokens](../../../foundations/authentication-concepts/access-tokens-and-id-tokens/index.html#refresh-tokens).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `requestScopesForMultipleResourcesEnabled`                       | Boolean   | Optional | Mutable   | Specifies whether the application can request scopes from multiple custom resources. The default value is `false`. For more information about scopes and access tokens, refer to [Resource Scopes](../../resources/resource-scopes/index.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `requireSignedRequestObject`                                     | Boolean   | Optional | Mutable   | Indicates that the JSON Web Token (JWT) for the [request query](https://openid.net/specs/openid-connect-core-1_0.html#RequestObject) parameter is required to be signed. If false or null (default), a signed request object is not required. Both `supportUnsignedRequestObject` and this property cannot be set to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `responseTypes`                                                  | String\[] | Optional | Mutable   | The code or token type returned by an authorization request. Options are `TOKEN`, `ID_TOKEN`, and `CODE`. For hybrid flows that specify `CODE` with `TOKEN` or `ID_TOKEN`, refer to [Hybrid grant type](../../../foundations/authentication-concepts/authorization-flow-by-grant-type/hybrid-grant-type.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `signing`                                                        | Object    | Optional | Mutable   | Configuration for the signing key. If absent, application tokens will be signed and verified by the PingOne default key at runtime. This property applies to OIDC applications of type `WORKER`, `WEB_APP`, `NATIVE_APP`, `SINGLE_PAGE_APP`, and `CUSTOM_APP`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `signing.keyRotationPolicy`                                      | Object    | Required | Mutable   | Contains the Key Rotation Policy (KRP) ID. This property is required if `signing` is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `signing.keyRotationPolicy.id`                                   | String    | Required | Mutable   | Reference to a KRP ID from certificate management. This property is required if `signing` is set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `skipTokenSessionValidation`                                     | Boolean   | Optional | Mutable   | Indicates whether the session associated with an access token or a refresh token should be taken into consideration when PingOne needs to determine the validity of the token. When set to `true`, PingOne ignores the session status, allowing the use of a valid token even if the user session has expired. By default, this property's value is set to `false`, which invalidates the token (regardless of the token's validity) if the user session is invalid. To learn more, refer to [Token validation](../../../foundations/authentication-concepts/access-tokens-and-id-tokens/token-validation.html).                                                                                                                                                                                                                                                  |
| `supportUnsignedRequestObject`                                   | Boolean   | Optional | Mutable   | Indicates whether the JSON Web Token (JWT) for the [request query](https://openid.net/specs/openid-connect-core-1_0.html#RequestObject) parameter is allowed to be unsigned. If false or null (default), an unsigned request object is not allowed. Both `requireSignedRequestObject` and this property cannot be set to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `tags`                                                           | String\[] | Optional | Mutable   | An array that specifies the list of labels associated with the application. Options are `PING_FED_CONNECTION_INTEGRATION`. Only applicable for [Create Application (OIDC Protocol - PingFederate Worker App)](create-application-oidc-protocol---pingfederate-worker-app.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `targetLinkUri`                                                  | String    | Optional | Mutable   | The URI for the application. If specified, PingOne will redirect application users to this URI after a user is authenticated. In the PingOne admin console, this becomes the value of the `target_link_uri` parameter used for the Initiate Single Sign-On URL field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `template`                                                       | Object    | Optional | Mutable   | Valid only when the application `type` is `TEMPLATE_APP`. This identifies the application as integration in [Integration Catalog](../../integration-catalog/index.html). (by integration.id and version.id) and provides key-value map of parameters needed by the integration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `template.configuration`                                         | Object    | Required | Mutable   | Contains a key/value map of the parameters required by the integration in Integration Catalog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `template.integration.id`                                        | String    | Required | Mutable   | The UUID of the integration in Integration Catalog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `template.version.id`                                            | String    | Required | Mutable   | The UUID of the integration version in Integration Catalog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `tokenEndpointAuthMethod`                                        | String    | Optional | Mutable   | The client authentication methods supported by the token endpoint. Options are `NONE`, `CLIENT_SECRET_BASIC`, `CLIENT_SECRET_POST`, `PRIVATE_KEY_JWT`, and `CLIENT_SECRET_JWT`. If this property is not set, the default values for supported app types are: `CLIENT_SECRET_BASIC` for `WEB_APP` and `WORKER` types, `NONE` for `NATIVE_APP`, `SINGLE_PAGE_APP`, and `CUSTOM_APP` types (when `CUSTOM_APP` specifies a `DEVICE_CODE` grant type for device authorization). For PKCE authentication flows, the `tokenEndpointAuthMethod` must be set to `NONE`.                                                                                                                                                                                                                                                                                                    |

#### Applications OIDC settings data model for PING_ONE_SELF_SERVICE

For applications of `type` PING_ONE_SELF_SERVICE only. Ignored for all other application types.

| Property                           | Type    | Required | Mutable | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------- | ------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `applyDefaultTheme`                | Boolean | Required | Mutable | If `true`, applies the default theme to the self service application.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `enableDefaultThemeFooter`         | Boolean | Required | Mutable | If `true`, shows the default theme footer on the self service application. Applies only if `applyDefaultTheme` is also `true`.                                                                                                                                                                                                                                                                                                                                                               |
| `logoutType`                       | String  | Optional | Mutable | The logout type for the self service application. This can be either `OIDC_RP_INITIATED` (the default) or `SAML2_SLO`.                                                                                                                                                                                                                                                                                                                                                                       |
| `manageDevicesViaMyAccountEnabled` | Boolean | Optional | Mutable | When set to `true`, PingID users can manage their devices using the MyAccount app. This will also add the MyAccount app to all PingID policies that already include Device Management. To limit the scope of PingID users, ensure an MFA policy or MFA DaVinci flow policy limiting their scope is added to the MyAccount app. For more information, refer to [Self service](https://docs.pingidentity.com/pingone/user_experience/p1_self_service.html) in the PingOne admin documentation. |

#### Applications OIDC settings data model for PING_ONE_PORTAL

For applications of `type` PING_ONE_PORTAL only. Ignored for all other application types.

| Property            | Type    | Required | Mutable | Description                                                                                                          |
| ------------------- | ------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------- |
| `applyDefaultTheme` | Boolean | Required | Mutable | If `true`, applies the default theme to the app portal application.                                                  |
| `logoutType`        | String  | Optional | Mutable | The logout type for the app portal application. This can be either `OIDC_RP_INITIATED` (the default) or `SAML2_SLO`. |

### Applications SAML settings data model

| Property                                           | Type      | Required   | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------- | --------- | ---------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `acsUrls`                                          | String\[] | Required   | Mutable   | The Assertion Consumer Service URLs. The first URL in the list is used as default (there must be at least one URL).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `assertionDuration`                                | Integer   | Required   | Mutable   | The assertion validity duration in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `assertionSigned`                                  | Boolean   | Optional   | Mutable   | Indicates whether the SAML assertion itself should be signed. The default value is `true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `corsSettings`                                     | Object    | Optional   | Mutable   | Enables you to customize how the Authorization and Authentication APIs interact with CORS requests that reference the application. If omitted, the application allows CORS requests from any origin except for operations that expose sensitive information (such as, operations from `/as/authorize` and `/as/token`). We recommend you use `corsSettings`, rather than omitting this property.                                                                                                                                                                                                                                                                                                                                                  |
| `corsSettings.behavior`                            | String    | Required   | Mutable   | Options are "ALLOW_NO_ORIGINS" and "ALLOW_SPECIFIC_ORIGINS". ALLOWS_NO_ORIGINS rejects all CORS requests. ALLOW_SPECIFIC_ORIGINS rejects all CORS requests except those listed in `corsSettings.origins`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `corsSettings.origins`                             | String\[] | Optional   | Mutable   | This must be specified when `corsSettings.behavior` is ALLOW_SPECIFIC_ORIGINS, and must be omitted or empty when `corsSettings.behavior` is ALLOW_NO_ORIGINS. Limited to 20 values. The values are the origins from which CORS requests to the Authorization and Authentication APIs are allowed. Each value is an HTTP or HTTPS URL without a path. The host may be a domain name (including localhost), or an IPv4 address. Subdomains can be specified using the wildcard (\*) to match any string.                                                                                                                                                                                                                                            |
| `defaultTargetUrl`                                 | String    | Optional   | Mutable   | This is used as the RelayState parameter by the IdP to deep link into the application after authentication. This value can be overridden by the `applicationUrl` query parameter for [GET Identity Provider Initiated SSO](../../../auth/saml-2.0/identity-provider-initiated-sso.html). Although both of these parameters are generally URLs, because they are used as deep links, this is not enforced. If neither `defaultTargetUrl` nor `applicationUrl` is specified during a SAML authentication flow, no RelayState value is supplied to the application. The `defaultTargetUrl` (or the `applicationUrl`) value is passed to the SAML application's ACS URL as a separate RelayState key value (not within the SAMLResponse key value).   |
| `enableRequestedAuthnContext`                      | Boolean   | Optional   | Mutable   | Indicates whether `requestedAuthnContext` is taken into account in policy decision-making.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `enableAlwaysAcceptAcsUrlInSignedAuthnRequest`     | Boolean   | Optional   | Mutable   | If enabled (`true`), this indicates that when a service provider (SP) specifies an ACS URL in its AuthnRequest, and signs the AuthnRequest, then assuming the identity provider (IdP) can validate the signature, the IdP can accept the ACS URL as valid. This is so, regardless of whether the ACS URL is specified in `acsUrls` as an allowable ACS URL (refer to [Applications SAML metadata settings data model](#applications-saml-settings-metadata-model)). Enabling this setting is useful when an SP generates ACS URLs dynamically.                                                                                                                                                                                                    |
| `idpSigning.algorithm`                             | String    | Optional   | Mutable   | The algorithm used by the IdP signing key. Algorithms supported: SHA256withRSA, SHA384withRSA, SHA512withRSA, SHA256withECDSA, SHA384withECDSA, and SHA512withECDSA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `idpSigning.key.id`                                | String    | Optional   | Mutable   | The certificate to be used by the identity provider to sign assertions and responses. If this property is omitted, the default signing certificate for the environment is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `nameIdFormat`                                     | String    | Optional   | Mutable   | The format of the Subject `NameID` attribute in the SAML assertion. Options are:- `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`: The Subject's `NameID` format is not specified. Use this format if you are not sure which format to use.

- `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`: The Subject's `NameID` format is in the form of an email address.

- `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`: The Subject's `NameID` format is an opaque unique identifier for a user that retains the same value over time.

- `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`: The Subject's `NameID` format is a randomly generated identifier. A different value is used for each SSO for a given user. |
| `responseSigned`                                   | Boolean   | Optional   | Mutable   | Indicates whether the SAML assertion response itself should be signed. The default value is `False`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sessionNotOnOrAfterDuration`                      | Integer   | Optional   | Mutable   | Update this value if the SAML application requires a different `SessionNotOnOrAfter` attribute value within the `AuthnStatement` element than the `NotOnOrAfter` value set by the `assertionDuration` property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `sloBinding`                                       | String    | Optional   | Mutable   | The binding protocol to be used for the logout response. Options are `HTTP_REDIRECT` or `HTTP_POST`. The default is `HTTP_POST`; existing configurations with no data default to `HTTP_POST`. This is an optional property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sloEndpoint`                                      | String    | Optional   | Mutable   | The logout endpoint URL. This is an optional property. However, if a `sloEndpoint` logout endpoint URL is not defined, logout actions result in an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `sloResponseEndpoint`                              | String    | Optional   | Mutable   | The endpoint URL to submit the logout response. If a value is not provided, the `sloEndpoint` property value is used to submit SLO response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `sloWindow`                                        | Integer   | Optional   | Mutable   | Defines how long PingOne can exchange logout messages with the application, specifically a `LogoutRequest` from the application, since the initial request. PingOne can also send a `LogoutRequest` to the application when a single logout is initiated by the user from other session participants, such as an application or identity provider. This setting is per application. The SLO logout is separate from the user session logout that revokes all tokens.                                                                                                                                                                                                                                                                              |
| `spEncryption`                                     | Object    | Optional   | Mutable   | Enables PingOne to encrypt SAML assertions to be sent to the application. Assertions are not encrypted by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `spEncryption.algorithm`                           | String    | Required   | Mutable   | The algorithm for encrypting the assertions (AES_128, AES_256, or TRIPLEDES).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `spEncryption.certificate`                         | Object    | Required   | Mutable   | Contains the ID of the encryption public certificate that has been uploaded to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `spEncryption.certificate.id`                      | String    | Required   | Mutable   | The unique identifier of the encryption public certificate that has been uploaded to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `spEntityId`                                       | String    | Required   | Immutable | The service provider entity ID used to lookup the application. This must be unique within the environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `spVerification.authnRequestSigned`                | Boolean   | Optional   | Mutable   | Whether the Authn Request signing should be enforced. Default is `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `spVerification.certificates[].id`                 | String\[] | Optional   | Mutable   | An array that specifies the certificate IDs used to verify the service provider signature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `template`                                         | Object    | Optional   | Mutable   | Valid only when the application `type` is `TEMPLATE_APP`. This identifies the application as integration in [Integration Catalog](../../integration-catalog/index.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `template.configuration`                           | Object    | Required   | Mutable   | Contains a key/value map of the parameters required by the integration in Integration Catalog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `template.integration.id`                          | String    | Required   | Mutable   | The UUID of the integration in Integration Catalog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `template.version.id`                              | String    | Required   | Mutable   | The UUID of the integration version in Integration Catalog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `virtualServerIdSettings`                          | Object    | Optional   | Mutable   | Contains the virtual server ID or IDs to be used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `virtualServerIdSettings.enabled`                  | Boolean   | Optional   | Mutable   | Indicates whether the virtual server ID or IDs specified are to be used. Defaults to `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `virtualServerIdSettings.virtualServerIds`         | Object\[] | Optional\* | Mutable   | \*Required if `enabled` is `true`. Contains the list of virtual ID or IDs to be used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `virtualServerIdSettings.virtualServerIds.vsId`    | String    | Optional\* | Mutable   | \*Required if `enabled` is `true`. This must be a valid SAML entity ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `virtualServerIdSettings.virtualServerIds.default` | Boolean   | Optional   | Mutable   | Indicates whether the virtual server identified by the associated `vsId` is to be used as the default virtual server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

#### Applications SAML metadata settings data model

| Property                         | Type      | Required | Mutable | Description                                                                                                    |
| -------------------------------- | --------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------- |
| `acsBindings`                    | String    | Optional | Mutable | The assertion consumer service binding protocol. Options are: `HTTP_REDIRECT` or `HTTP_POST`                   |
| `acsUrls`                        | String\[] | Optional | Mutable | The assertion consumer service URLs.                                                                           |
| `authnRequestsSigned`            | Boolean   | Optional | Mutable | Indicates whether the SAML authentication request is signed.                                                   |
| `encryptionCertificate.pkcs7Der` | Byte\[]   | Optional | Mutable | The PKCS7 encryption certificate in DER format.                                                                |
| `sloBinding`                     | String    | Optional | Mutable | The SAML single logout binding protocol used for logout response. Options are: `HTTP_REDIRECT` or `HTTP_POST`. |
| `sloEndpoint`                    | String    | Required | Mutable | The SAML single logout endpoint URL.                                                                           |
| `signingCertificates[].pkcs7Der` | Byte\[]   | Optional | Mutable | The PKCS7 signing certificates in DER format.                                                                  |

### Applications WS-Federation settings data model

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | These settings are for applications of type `WEB_APP` only, and are ignored for all other application types. |

| Property                        | Type      | Required | Mutable | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------- | --------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assertionDuration`             | Integer   | Optional | Mutable | The assertion validity duration in seconds. The default value is 300 seconds (5 minutes). Valid values are between `300` and `3932100`.                                                                                                                                                                                                                                                                                                                                                                 |
| `audienceRestriction`           | String    | Optional | Mutable | The service provider ID. Defaults to `urn:federation:MicrosoftOnline`.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `corsSettings`                  | Object    | Optional | Mutable | Enables you to customize how the Authorization and Authentication APIs interact with CORS requests that reference the application. If omitted, the application allows CORS requests from any origin except for operations that expose sensitive information (such as, operations from `/as/authorize` and `/as/token`). We recommend you use `corsSettings`, rather than omitting this property.                                                                                                        |
| `corsSettings.behavior`         | String    | Required | Mutable | Options are "ALLOW_NO_ORIGINS" and "ALLOW_SPECIFIC_ORIGINS". ALLOWS_NO_ORIGINS rejects all CORS requests. ALLOW_SPECIFIC_ORIGINS rejects all CORS requests except those listed in `corsSettings.origins`.                                                                                                                                                                                                                                                                                               |
| `corsSettings.origins`          | String\[] | Optional | Mutable | This must be specified when `corsSettings.behavior` is ALLOW_SPECIFIC_ORIGINS, and must be omitted or empty when `corsSettings.behaviour` is ALLOW_NO_ORIGINS. Limited to 20 values. The values are the origins from which CORS requests to the Authorization and Authentication APIs are allowed. Each value is an HTTP or HTTPS URL without a path. The host may be a domain name (including localhost), or an IPv4 address. Subdomains can be specified using the wildcard (\*) to match any string. |
| `domainName`                    | String    | Required | Mutable | The federated domain name (for example, the Azure custom domain).                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `idpSigning`                    | Object    | Required | Mutable | Contains the information about the signing of requests by the identity provider (IdP).                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `idpSigning.algorithm`          | String    | Required | Mutable | The signature algorithm to be used for signing. Algorithms supported: SHA256withRSA, SHA384withRSA, SHA512withRSA, SHA256withECDSA, SHA384withECDSA, and SHA512withECDSA.                                                                                                                                                                                                                                                                                                                               |
| `idpSigning.key`                | String    | Required | Mutable | The key pair to be used by the IdP to sign requests. If this isn't specified, the default signing certificate for the environment is used.                                                                                                                                                                                                                                                                                                                                                              |
| `idpSigning.key.id`             | String    | Required | Mutable | The ID of the key specified for `idpSigning.key`.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `kerberos`                      | Object    | Optional | Mutable | Contains the Kerberos authentication settings. Set this to null to disable Kerberos authentication.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `kerberos.gateways`             | Object\[] | Optional | Mutable | Contains the gateway properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `kerberos.gateways.id`          | String    | Required | Mutable | The UUID of the LDAP gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `kerberos.gateways.type`        | String    | Required | Mutable | The gateway type. This must be "LDAP".                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `kerberos.gateways.userType.id` | String    | Required | Mutable | The UUID of a user type in the list of `userTypes` for the LDAP gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `replyUrl`                      | String    | Required | Mutable | The URL that the replying party (such as, Office365) uses to accept submissions of RequestSecurityTokenResponse messages that are a result of SSO requests.                                                                                                                                                                                                                                                                                                                                             |
| `sloEndpoint`                   | String    | Optional | Mutable | The single logout endpoint URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `subjectNameIdentifierFormat`   | String    | Optional | Mutable | The format to use for the SubjectNameIdentifier element. This value must be one of the following:- `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`

- `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`                                                                                                                                                                                                                                                                                  |
| `wsTrustVersion`                | String    | Optional | Mutable | The WS-Trust (Web Services Trust) version to use. Valid values are `1.2` and `1.3`.                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Applications WS-Federation settings data model for Microsoft Entra ID hybrid join

Hybrid join simplifies device management and allows organizations to join devices to on-premises Active Directory and the cloud with Entra ID.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Device authentication using hybrid join is available as a limited access release for customers who are licensed with PingOne for Workforce Plus or Premium in the North America geography only and isn't covered under standard Support service level agreements (SLAs). You can open support cases for feedback, bug reports, configuration questions, or other inquiries related, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so response times might exceed the usual SLAs for your Support package.Topics for this feature are draft documentation for limited access purposes only and aren't complete or final. |

| Property                     | Type      | Required | Mutable | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------- | --------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hybridJoinDeviceAttribute`  | String    | Optional | Mutable | Required for Entra ID hybrid join. The value must be the name of a custom user attribute that an administrator has created. See [Creating attributes and a population for hybrid joined devices](https://docs.pingidentity.com/pingone/use_cases/p1_microsoft_entra_hybrid_join.html#p1-create-attributes) for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `stsTokenType`               | String    | Optional | Mutable | The type of token to use. Valid values:- `http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLV1.1`: Corresponds to SAML 1.1 in the admin console. Not suitable for Entra ID hybrid join.

- `urn:oasis:names:tc:SAML:1.0:assertion`: Corresponds to SAML 1.1 for Office 365 in the admin console. Required for Entra ID hybrid join.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `useMex13`                   | Boolean   | Optional | Mutable | Must be `true` to enable Entra ID hybrid join. After it's set to `true`, update Entra ID to use the new metadata exchange endpoint. See [Updating the federated IdP setting](https://docs.pingidentity.com/pingone/use_cases/p1_microsoft_entra_hybrid_join.html#p1-update-federated-idp) for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `userAttributeUsernameMatch` | String    | Optional | Mutable | Specifies the PingOne user attribute used to match the username from a Security Token Service (STS) request to an existing user profile.By default, PingOne matches the username against the user's email address. Configure this setting if:- The username in the token is the user's user principal name (`userPrincipalName` attribute in Active Directory), but it differs from their email address (`mail` attribute in Active Directory).

- The username is something other than the user's user principal name or email address.The selected attribute must match the username format in the token to ensure successful identification.When specifying a PingOne custom user attribute as the `userAttributeUsernameMatch` property value, the admin must ensure the attribute is configured with the following properties:```json
"schemaType": "CUSTOM"
"type": "STRING"
"unique": true
"enabled": true
"multiValued": false
"required": false or true
``` |
| `userAttributeX509Match`     | String    | Optional | Mutable | The user attribute to match against the user information in the X.509 certificate.Supports Microsoft Windows primary refresh token (PRT) operations when users log on to their Windows devices, or unlock their locked Windows devices, using PingID. See [Integrating PingID with Windows Login](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integrating_with_windows_login_passwordless.html). If these setting isn't specified, Windows PRT operations are still supported, but only when users log on to (or unlock) their Windows devices using their username and password.                                                                                                                                                                                                                                                                                                                                                                   |
| `validIssuanceCertificates`  | Object\[] | Optional | Mutable | Contains the list of valid issuance certificate IDs for the application. A maximum of 10 certificate IDs can be specified.Supports Microsoft Windows primary refresh token (PRT) operations when users log on to their Windows devices, or unlock their locked Windows devices, using PingID. See [Integrating PingID with Windows Login](https://docs.pingidentity.com/pingid/pingid_integrations/pid_integrating_with_windows_login_passwordless.html). If these setting isn't specified, Windows PRT operations are still supported, but only when users log on to (or unlock) their Windows devices using their username and password.                                                                                                                                                                                                                                                                                                                           |

### PingID mobile app configuration data model

| Property                                                             | Type    | Required | Mutable   | Description                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------- | ------- | -------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `description`                                                        | String  | Optional | Mutable   | The description used in PingOne for the PingID mobile app.                                                                                                                                                                                                                                                                                                                                                                  |
| `enabled`                                                            | Boolean | Required | Immutable | Used to enable/disable the application. For the PingID mobile app, must be set to `true`.                                                                                                                                                                                                                                                                                                                                   |
| `mobile.allowAuthenticationDeviceLocked.enabled`                     | Boolean | Optional | Mutable   | Set to `true` if you want to allow users to authenticate from the lock screen if they using Android 10.0 or earlier.                                                                                                                                                                                                                                                                                                        |
| `mobile.allowUnPairAndChangeDeviceFromApp.enabled`                   | Boolean | Optional | Mutable   | Set to `true` if you want to allow users to unpair or change device from the PingID mobile app.                                                                                                                                                                                                                                                                                                                             |
| `mobile.bundleId`                                                    | String  | Required | Immutable | Must be set to `com.pingidentity.pingid.prod`.                                                                                                                                                                                                                                                                                                                                                                              |
| `mobile.mobileAppSecurityPinRequire.enabled`                         | Boolean | Optional | Mutable   | Set to `true` if you want to require the user to enter a security PIN to access the PingID mobile app.                                                                                                                                                                                                                                                                                                                      |
| `mobile.mobileAppSecurityPinRequire.requireForAllDevices`            | Boolean | Optional | Mutable   | If `mobile.mobileAppSecurityPinRequire.enabled` is set to `true`, then by default, the PIN is required only if a device PIN or biometrics have not been defined for the device. Set `requireForAllDevices` to `true` if you want to require PIN use for all devices.                                                                                                                                                        |
| `mobile.mobileAppSecurityPinRequire.securityPinDigit`                | String  | Optional | Mutable   | If `mobile.mobileAppSecurityPinRequire.enabled` is set to `true`, then by default, a six-digit security PIN is required. To specify that a four-digit PIN is sufficient, set `securityPinDigit` to `FOUR_DIGIT`. Use `SIX_DIGIT` to specify that a six-digit PIN is required.                                                                                                                                               |
| `mobile.mobileDeviceBiometricsSetting.devicePasscodeFallbackEnabled` | Boolean | Optional | Mutable   | Set `devicePasscodeFallbackEnabled` to `true` if you want to allow iOS users to authenticate using the device passcode if biometric authentication fails.                                                                                                                                                                                                                                                                   |
| `mobile.mobileDeviceBiometricsSetting.faceIdConsentEnabled`          | Boolean | Optional | Mutable   | For iOS devices, set `faceIdConsentEnabled` to `true` if you want to prevent users with FaceID defined from authenticating by mistake. When set to `true`, the user is prompted to consent explicitly before each face scan is taken.                                                                                                                                                                                       |
| `mobile.mobileDeviceBiometricsSetting.notificationActionsEnabled`    | Boolean | Optional | Mutable   | Set `notificationActionsEnabled` to `true` if you want to allow users to approve notification requests from their device's lock screen.                                                                                                                                                                                                                                                                                     |
| `mobile.mobileDeviceBiometricsSetting.required`                      | Boolean | Optional | Mutable   | If you have allowed biometric authentication methods in the MFA policy, then by default, the user is required to use a biometric method with PingID if one is available on their device. If you want to specify that users can authenticate with the PingID mobile app only if they have a biometric method configured, set `mobile.mobileDeviceBiometricsSetting.required` to `true`.                                      |
| `mobile.notifyOptionalMobileVersionUpdates.enabled`                  | Boolean | Optional | Mutable   | Set `notifyOptionalMobileVersionUpdates.enabled` to `true` if you want to notify your users that there is a newer version of the PingID app available if they want to update. The notification is displayed as soon as the user opens the app. When set to `true`, you must provide a value for `notifyOptionalMobileVersionUpdates.android`, `notifyOptionalMobileVersionUpdates.ios`, or both.                            |
| `mobile.notifyOptionalMobileVersionUpdates.android`                  | String  | Optional | Mutable   | If you set `notifyOptionalMobileVersionUpdates.enabled` to `true`, use `android` to specify the version of the app that you want to notify Android device users about. Set the value to `latest` if you want to always notify users about the latest version of the PingID app that is available.                                                                                                                           |
| `mobile.notifyOptionalMobileVersionUpdates.ios`                      | String  | Optional | Mutable   | If you set `notifyOptionalMobileVersionUpdates.enabled` to `true`, use `ios` to specify the version of the app that you want to notify iOS device users about. Set the value to `latest` if you want to always notify users about the latest version of the PingID app that is available.                                                                                                                                   |
| `mobile.notifyRequireMobileVersionUpdates.enabled`                   | Boolean | Optional | Mutable   | Set `notifyRequireMobileVersionUpdates.enabled` to `true` if you want to require a minimum version of the PingID app and notify the user that they must update the app if they are using an older version. The notification is displayed as soon as the user opens the app. When set to `true`, you must provide a value for `notifyRequireMobileVersionUpdates.android`, `notifyRequireMobileVersionUpdates.ios`, or both. |
| `mobile.notifyRequireMobileVersionUpdates.android`                   | String  | Optional | Mutable   | If you set `notifyRequireMobileVersionUpdates.enabled` to `true`, use `android` to specify the minimum version of the app that you want to require on Android devices. Set the value to `latest` if you want to require your users to always be running the latest version of the PingID app.                                                                                                                               |
| `mobile.notifyRequireMobileVersionUpdates.ios`                       | String  | Optional | Mutable   | If you set `notifyRequireMobileVersionUpdates.enabled` to `true`, use `ios` to specify the minimum version of the app that you want to require on iOS devices. Set the value to `latest` if you want to require your users to always be running the latest version of the PingID app.                                                                                                                                       |
| `mobile.otpPushNotificationEnabled.enabled`                          | Boolean | Optional | Mutable   | Set to `true` if you want users to receive a push notification during authentication that they can tap to open the PingID app.                                                                                                                                                                                                                                                                                              |
| `mobile.packageName`                                                 | String  | Required | Immutable | Must be set to `prod.com.pingidentity.pingid`.                                                                                                                                                                                                                                                                                                                                                                              |
| `mobile.pingIDSettings`                                              | Boolean | Required | Immutable | Must be set to `true`.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `mobile.push.numberMatching.type`                                    | String  | Optional | Mutable   | If you enabled number-matching authentication in the MFA policy, use `mobile.push.numberMatching.type` to specify whether users should select the displayed number from a group of three numbers, or whether you want to require users to actually enter the number that was shown. Use one of the following values: `SELECT_NUMBER` (default) or `ENTER_MANUALLY`.                                                         |
| `mobile.showAuthenticationInformation.enabled`                       | Boolean | Optional | Mutable   | Set to `true` if you want push notifications to include a map that displays the location of the user requesting access.                                                                                                                                                                                                                                                                                                     |
| `name`                                                               | String  | Required | Mutable   | The name used in PingOne for the PingID mobile app.                                                                                                                                                                                                                                                                                                                                                                         |
| `protocol`                                                           | String  | Required | Immutable | The protocol used by the application. For the PingID mobile app, must be set to `OPENID_CONNECT`.                                                                                                                                                                                                                                                                                                                           |
| `type`                                                               | String  | Required | Immutable | The application type. For the PingID mobile app, must be set to `NATIVE_APP`.                                                                                                                                                                                                                                                                                                                                               |

## Application events generated

Refer to [Audit Reporting Events](../../reference/audit-reporting-events.html) for the events generated.

## Response codes

| Code | Message                                                                                            |
| ---- | -------------------------------------------------------------------------------------------------- |
| 200  | Successful operation.                                                                              |
| 201  | Successfully created.                                                                              |
| 204  | Successfully removed. No content.                                                                  |
| 400  | The request could not be completed.                                                                |
| 401  | You do not have access to this resource.                                                           |
| 403  | You do not have permissions or are not licensed to make this request, or your license is exceeded. |
| 404  | The requested resource was not found.                                                              |
| 500  | An unexpected error occurred.                                                                      |

## Application errors

In addition to the general [error codes](../../reference/error-codes.html), application operations can return the following errors:

| HTTP status | Top‑level code   | Detail code                                                                                                  | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ---------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`   | `UNIQUENESS_VIOLATION`                                                                                       | **Message:**```
Application name '<name>' already exists in environment '<environmentId>' for application '<applicationId>'
```> **Collapse: When and details**
>
> **When:** The application `name` is already in use (application create and update)
>
> **Details:** `name already exists` for target `name`, with `innerError.existingId` set to the existing application ID                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `INVALID_DATA`   | `UNIQUENESS_VIOLATION`                                                                                       | **Message:** Identifies the conflicting value and existing application. For mobile identifiers, the existing application is identified only in the detail's `innerError.existingId`> **Collapse: When and details**
>
> **When:** A supplied OIDC `clientId`, SAML `spEntityId`, OIDC `devicePathId`, or supported mobile identifier is already in use on application create or update. An update ignores a changed `clientId` rather than rejecting it
>
> **Details:** `<property> already exists`, or for `clientId`, `client id already exists`                                                                                                                                                                                                                                                                                    |
| 400         | `INVALID_DATA`   | `INVALID_VALUE`                                                                                              | **Message:**```
Property '<property>' is immutable and cannot be changed on application '<applicationId>' in environment '<environmentId>'
```> **Collapse: When and details**
>
> **When:** An update attempts to change an immutable application property, such as `protocol`, `type`, or a protected mobile identifier
>
> **Details:** `property cannot be changed` for each immutable property, with the property name as the target and repeated in `innerError.name`. When several properties change at once, the message reads `Properties [<property>, …​] are immutable and cannot be changed on application '<applicationId>' in environment '<environmentId>'` and one detail is returned per property.                                                                                                                    |
| 400         | `INVALID_DATA`   | None                                                                                                         | **Message:** `Invalid application ID: <id>`> **Collapse: When and details**
>
> **When:** The `id` in the body of the request differs from the application ID in `PUT /applications/{applicationId}`
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 400         | `INVALID_DATA`   | None                                                                                                         | **Message:** `Cannot create more than <maximum> applications for environment <environmentId>`> **Collapse: When and details**
>
> **When:** Creating an application would exceed the environment's application limit
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 400         | `REQUEST_FAILED` | `CONSTRAINT_VIOLATION`                                                                                       | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** The request creates, updates, or deletes a platform‑managed application in a way that violates its management constraints
>
> **Details:** Identifies the restricted application type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 400         | `INVALID_DATA`   | `INVALID_VALUE` or `EMPTY_VALUE` or `REQUIRED_VALUE` or `CONSTRAINT_VIOLATION` or `INSUFFICIENT_PERMISSIONS` | **Message:** Describes the rejected property, such as a missing certificate or invalid application configuration.> **Collapse: When and details**
>
> **When:** Application validation rejects a protocol‑specific property, a reserved client ID, or a referenced certificate or key
>
> **Details:** Field‑specific validation message. Target depends on the rejected property. Most rejections return `INVALID_VALUE`. A few return `EMPTY_VALUE` for missing SAML verification certificates, `REQUIRED_VALUE` for missing paired mobile settings or missing PingID Desktop Gen2 sub-application settings, `CONSTRAINT_VIOLATION` for mutually exclusive `jwks` and `jwksUrl` settings or a missing environment signing key, or `INSUFFICIENT_PERMISSIONS` for a WS‑Federation X.509 setting that the environment does not enable. |
| 400         | `INVALID_DATA`   | `INVALID_PARAMETER`                                                                                          | **Message:** `Cannot create application due to invalid or missing template parameters: <detail>`> **Collapse: When and details**
>
> **When:** A `TEMPLATE_APP` request includes template configuration parameters that cannot be resolved, such as a missing or misspelled parameter
>
> **Details:** Message is repeated in the detail, for target `template.configuration`.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 400         | `INVALID_DATA`   | None                                                                                                         | **Message:**```
Invalid template '<integrationId>' version '<versionId>' is used, the latest version '<latestVersionId>' of the template '<integrationId>' should be used when creating the application.
```> **Collapse: When and details**
>
> **When:** A `TEMPLATE_APP` request uses a template version that is not the current version (application create)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 400         | `REQUEST_FAILED` | `INVALID_PARAMETER`                                                                                          | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** `GET /applications` uses a `limit` value outside the supported range
>
> **Details:** `Must be between 1 and <maximum>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 400         | `REQUEST_FAILED` | `INVALID_FILTER` or `INVALID_PARAMETER`                                                                      | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** `GET /applications` uses an unsupported or malformed `filter` or `order` query parameter
>
> **Details:** The detail message target is one of `operator` (unsupported operator), `attribute` (unknown or unfilterable attribute), `value` (malformed filter value), or `filter` (application‑level filter rule). For an order value, the target is `order`. The detail explains the unsupported attribute, value, or syntax.                                                                                                                                                                                                                                                       |
| 400         | `INVALID_DATA`   | None                                                                                                         | **Message:** `Error retrieving or parsing SAML metadata`> **Collapse: When and details**
>
> **When:** SAML metadata supplied to `POST /applications` with `application/samlmetadata+xml` or `application/samlmetadata+url` cannot be retrieved or parsed
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 403         | `ACCESS_FAILED`  | `LICENSE_EXCEEDED`                                                                                           | **Message:** `The request could not be completed. You do not have access to this resource.`> **Collapse: When and details**
>
> **When:** A WS‑Federation application create or update uses an advanced STS feature that the environment is not licensed or enabled for, such as a restricted `stsTokenType`, hybrid join setting, issuance certificate, or X.509 username matching attribute
>
> **Details:** The detail message names the environment and the restricted feature, for example `Environment is not licensed [or enabled] for advanced STS: <environmentId>`. The feature wording is `adding valid issuance certificates` or `selecting a user attribute for X.509 token username matching` for those settings, and the detail target is the changed property for those two features.                                  |
| 404         | `NOT_FOUND`      | None                                                                                                         | **Message:** `Unable to find Application with ID: '<applicationId>' in Environment '<environmentId>'`> **Collapse: When and details**
>
> **When:** The application ID in the request URL does not exist in the environment (applies to `GET`, `PUT`, and `DELETE /applications/{applicationId}`)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 404         | `NOT_FOUND`      | None                                                                                                         | **Message:** `Unable to find Template with ID: '<integrationId>' in Environment '<environmentId>'` for a create, or `Unable to find Template with ID: '<integrationId>' and Version ID: '<versionId>' in Environment '<environmentId>'` for an update> **Collapse: When and details**
>
> **When:** A `TEMPLATE_APP` request references an integration template that does not exist (check the `template.integration.id` value in the request body), or an update references a template version that does not exist
>
> **Details:** None.                                                                                                                                                                                                                                                                                             |

---

---
title: Application Resource Grants
description: Manage resource access grants that let a PingOne application request OAuth 2 scopes for protected resources
component: pingone-api
page_id: pingone-api:platform:applications/application-resource-grants/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/applications/application-resource-grants/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  applications-resource-grant-data-model: Applications resource grant data model
  response-codes: Response codes
  application-resource-grant-errors: Application resource grant errors
---

# Application Resource Grants

Resources are the protected endpoints that applications request access to using OAuth 2 authorization services. A resource access grant specifies the identifier of the resource associated with the specified application.

## Applications resource grant data model

| Property         | Type      | Required | Mutable   | Description                                                     |
| ---------------- | --------- | -------- | --------- | --------------------------------------------------------------- |
| `application.id` | String    | N/A      | Read-only | The application resource ID associated with the resource grant. |
| `createdAt`      | Date      | N/A      | Read-only | The time the resource was created.                              |
| `id`             | String    | N/A      | Read-only | The application resource grant ID.                              |
| `resource.id`    | String    | N/A      | Read-only | The ID of the protected resource associated with this grant.    |
| `scopes.id`      | String\[] | Required | Mutable   | The IDs of the scopes associated with this grant.               |
| `updatedAt`      | Date      | N/A      | Read only | The time the resource was last updated.                         |

Refer also to [Authorization flow by grant type](../../../foundations/authentication-concepts/authorization-flow-by-grant-type/index.html).

## Response codes

|   |                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `/v1/environments/{{envID}}/applications/{{appID}}/grants` endpoint returns a `404 NOT FOUND` on `GET`, `POST`, `PUT`, and `DELETE` operations if the application's `type` property is set to `PING_ONE_ADMIN_CONSOLE` or the MCP server application type. |

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |
| 500  | An unexpected error occurred.                                         |

## Application resource grant errors

In addition to the general [error codes](../../reference/error-codes.html), application resource grant operations can return the following errors:

| HTTP status | Top‑level code   | Detail code            | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                           |
| ----------- | ---------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 400         | `INVALID_DATA`   | `INVALID_VALUE`        | **Message:** `The data provided was invalid.`> **Collapse: When and details**
>
> **When:** A `POST /grants` request creates a grant for an application and resource pair that already has a grant
>
> **Details:** `grant to given resource already exists` (target: `resource`), with `existingId`, `appId`, and `resId` inner errors                                                                                  |
| 400         | `INVALID_DATA`   | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /grants/{ID}` request references scopes that do not exist for the resource
>
> **Details:** `Unable to find scopes with the following IDs: <scopeIds>` (target: `scopes`)                                                                           |
| 400         | `INVALID_DATA`   | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT /grants/{ID}` request adds a scope whose name is already granted to the application through a different resource
>
> **Details:** `Multiple scopes with the same name cannot be added to the same grant` (target: `scopes`)                         |
| 400         | `REQUEST_FAILED` | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST /grants` request creates a grant for a resource other than the `openid` resource for an application of type WORKER
>
> **Details:** `Resource access grants for applications of type 'WORKER' can only be created for the 'openid' resource` (target: `resource.id`) |
| 400         | `INVALID_DATA`   | `INVALID_VALUE`        | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `PUT /grants/{ID}` request changes the grant's environment, application, or resource
>
> **Details:** `The attribute is immutable and can not be updated.`                                                                                                         |
| 404         | `NOT_FOUND`      | None                   | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** The application does not exist in the environment, or is an admin console or MCP server application. Applies to all application resource grant operations
>
> **Details:** None.                                                                                                  |
| 404         | `NOT_FOUND`      | None                   | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** `GET`, `PUT`, or `DELETE /grants/{ID}` references a grant that does not exist, or a `POST` or `PUT` request references a resource that does not exist in the environment
>
> **Details:** None.                                                                                   |

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | You need the Client Application Developer role to perform operations on application resources. |

---

---
title: Application Resources
description: Explains the PingOne Authorize applicationResources endpoint for creating, reading, updating, and deleting application resources
component: pingone-api
page_id: pingone-api:platform:resources/application-resources/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/resources/application-resources/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  application-resources-data-model: API application resources data model
  response-codes: Response codes
  application-resource-errors: Application resource errors
---

# Application Resources

The PingOne Authorize `{{apiPath}}/v1/environments/{{envID}}/resources/{{resourceID}}/applicationResources` endpoint provides operations to create, read, update, and delete application resources in PingOne.

## API application resources data model

| Property      | Type   | Required | Mutable   | Description                                                              |
| ------------- | ------ | -------- | --------- | ------------------------------------------------------------------------ |
| `description` | String | Optional | Mutable   | The application resource's description.                                  |
| `id`          | String | N/A      | Read only | The resource's unique identifier.                                        |
| `name`        | String | Required | Mutable   | The application resource name. The `name` value must be unique.          |
| `parent`      | Object | N/A      | Read only | The application resource's parent.                                       |
| `parent.type` | String | N/A      | Read only | The application resource's parent type. Options are `PING_ONE_RESOURCE`. |
| `parent.id`   | String | N/A      | Read only | The application resource's parent ID.                                    |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 201  | Successfully created.                                                 |
| 204  | Successfully removed. No content.                                     |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## Application resource errors

In addition to the general [error codes](../../reference/error-codes.html), application resource operations can return the following errors:

| HTTP status | Top‑level code     | Detail code                                        | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------- | ------------------ | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `INVALID_DATA`     | `EMPTY_VALUE` or `OUT_OF_RANGE` or `INVALID_VALUE` | **Message:** `Validation Error : [<field> <message>]`> **Collapse: When and details**
>
> **When:** A `POST` or `PUT` request body omits `name` or supplies a blank `name`, or supplies a `name` value longer than 20 characters or containing characters other than Unicode letters, marks, numbers, spaces, forward slashes, dots, apostrophes, underscores, and hyphens, or supplies a `description` value that fails validation
>
> **Details:** Describes the failing property, such as `must not be blank` for an omitted or blank `name` (detail `EMPTY_VALUE`), `must contain only Unicode letters, marks, numbers, spaces, forward slashes, dots, apostrophes, underscores, or hyphens` for a `name` with disallowed characters (detail `INVALID_VALUE`), or `size must be between 1 and 20` for a `name` longer than 20 characters (detail `OUT_OF_RANGE` with `rangeMinimumValue` 1 and `rangeMaximumValue` 20 inner errors), for example `Validation Error : [name must not be blank]`. A `description` that exceeds 1024 characters returns `size must be between 1 and 1024` (detail `OUT_OF_RANGE`), and a `description` with disallowed characters returns ``must contain only Unicode letters, marks, numbers, spaces, or punctuation (except $, +, <, =, >, ^, `, \|, ~)`` (detail `INVALID_VALUE`). |
| 400         | `INVALID_DATA`     | `UNIQUENESS_VIOLATION`                             | **Message:** `The request could not be completed. One or more validation errors were in the request.`> **Collapse: When and details**
>
> **When:** A `POST` request specifies an application resource name already used by another application resource on the same parent resource server, or a `PUT` request changes the `name` to one that already exists on the same parent resource server
>
> **Details:** `A resource with this name already exists.` with target `name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST`, `PUT`, `GET`, or `DELETE` request references a `resourceID` that exists but is not a custom PingOne SSO resource (application resources are supported only on custom resources)
>
> **Details:** `You can only perform this operation on custom PingOne SSO resources.` with no target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 400         | `REQUEST_FAILED`   | `CONSTRAINT_VIOLATION`                             | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** A `POST` request exceeds the environment's application resource limit (128 per environment)
>
> **Details:** `Maximum limit of application resources per environment reached` with no target                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 403         | `ACCESS_FAILED`    | None                                               | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `applicationRoles:create:applicationResource` permission (`POST`), the `applicationRoles:read:applicationResource` permission (`GET`), the `applicationRoles:update:applicationResource` permission (`PUT`), or the `applicationRoles:delete:applicationResource` permission (`DELETE`)
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 404         | `NOT_FOUND`        | None                                               | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** A `GET`, `PUT`, or `DELETE` request references a resource server ID or application resource ID that does not exist, or a `POST` request references a resource server ID that does not exist
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 500         | `UNEXPECTED_ERROR` | None                                               | **Message:** `There was an unexpected error with the service. Please try again later.`> **Collapse: When and details**
>
> **When:** Application resource creation fails after repeated attempts (5) to generate a unique identifier
>
> **Details:** None.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

---
title: Application Resources Permissions
description: Explains the PingOne Authorize applicationPermissions endpoint for reading application resource permissions on a specified PingOne resource
component: pingone-api
page_id: pingone-api:platform:resources/application-resources-permissions/index
canonical_url: https://developer.pingidentity.com/pingone-api/platform/resources/application-resources-permissions/index.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  application-resources-permissions-data-model: Application resources permissions data model
  response-codes: Response codes
  application-resource-permission-errors: Application resource permission errors
---

# Application Resources Permissions

The PingOne Authorize `{{apiPath}}/v1/environments/{{envID}}/resources/{{resourceID}}/applicationPermissions` endpoint provides operations to read application resource permissions on the specified PingOne resource identified by its ID in the request URL.

## Application resources permissions data model

| Property                        | Type   | Required | Mutable   | Description                                                                 |
| ------------------------------- | ------ | -------- | --------- | --------------------------------------------------------------------------- |
| `action`                        | String | Required | Mutable   | The action associated with this permission.                                 |
| `description`                   | String | Optional | Mutable   | The resource's description.                                                 |
| `id`                            | String | N/A      | Read only | The resource's unique identifier.                                           |
| `key`                           | String | N/A      | Read only | The `resource.name:action` pair of the permission.                          |
| `resource`                      | Object | N/A      | Read only | An object that identifies the associated application resource.              |
| `resource.id`                   | String | N/A      | Read only | The ID for the associated application resource.                             |
| `resource.name`                 | String | N/A      | Read only | The name of the associated application resource.                            |
| `resourceServer.id`             | String | N/A      | Read only | The ID for the associated application resource server.                      |
| `resourceServer.environment.id` | String | N/A      | Read only | The ID for the environment associated with the application resource server. |

## Response codes

| Code | Message                                                               |
| ---- | --------------------------------------------------------------------- |
| 200  | Successful operation.                                                 |
| 400  | The request could not be completed.                                   |
| 401  | You do not have access to this resource.                              |
| 403  | You do not have permissions or are not licensed to make this request. |
| 404  | The requested resource was not found.                                 |

## Application resource permission errors

In addition to the general [error codes](../../reference/error-codes.html), application resource permission operations can return the following errors:

| HTTP status | Top‑level code   | Detail code            | When it happens and what the response contains                                                                                                                                                                                                                                                                                                                                                                 |
| ----------- | ---------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | `REQUEST_FAILED` | `CONSTRAINT_VIOLATION` | **Message:** `The request could not be completed. There was an issue processing the request.`> **Collapse: When and details**
>
> **When:** The `GET /resources/{resourceServerId}/applicationPermissions` request references a `resourceID` (resource server ID) that exists but is not a custom PingOne SSO resource
>
> **Details:** `You can only perform this operation on custom PingOne SSO resources.` |
| 403         | `ACCESS_FAILED`  | None                   | **Message:** `The actor attempting to perform the request is not authorized.`> **Collapse: When and details**
>
> **When:** The actor lacks the `applicationRoles:read:applicationPermission` permission (`GET` operations)
>
> **Details:** None.                                                                                                                                                             |
| 404         | `NOT_FOUND`      | None                   | **Message:** `The request could not be completed. The requested resource was not found.`> **Collapse: When and details**
>
> **When:** The `GET /resources/{resourceServerId}/applicationPermissions` request references a resource server ID that does not exist
>
> **Details:** None.                                                                                                                       |
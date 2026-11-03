---
title: Applications
description: Manage PingCentral application resources, including creating, updating, deleting, and promoting applications between environments
component: pingcentral
page_id: pingcentral:pingcentral:applications/index
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/applications/index.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  applications-data-model: Applications data model
  client-secret-data-model: Client secret data model
  application-promotion-history-data-model: Application promotion history data model
  response-codes: Response codes
---

# Applications

The application management API endpoints support operations to manage application resources, including designating an application owner and promoting the application from a development environment to production.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can revert applications to previously promoted versions. The reverted versions of the application will not exist outside of PingCentral until you promote them again. |

## Applications data model

| Property                              | Description                                                                                                                                                       |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `applicationOwners`                   | An array of strings that specifies the list of application owners. This is a required property.                                                                   |
| `applicationOwnerGroups`              | A string array of PingCentral groups that are application owners. This property is only applicable if PingCentral is configured in SSO mode.                      |
| `created`                             | A string that specifies the creation date for the application resource.                                                                                           |
| `description`                         | A string that provides a description of the resource.                                                                                                             |
| `enabled`                             | A boolean that specifies whether the PingCentral application is enabled.                                                                                          |
| `environmentId`                       | A string that specifies the environment associated with the resource.                                                                                             |
| `id`                                  | A string that specifies the resource identifier.                                                                                                                  |
| `modified`                            | A string that specifies the date the resource was last modified.                                                                                                  |
| `name`                                | A string that specifies the name of the resource. This is a required property.                                                                                    |
| `pingcentralVersion`                  | A string that specifies the PingCentral software version.                                                                                                         |
| `shouldUpdateToLatestTemplateVersion` | A boolean that returns `true` if the application should update to the latest template version.                                                                    |
| `templateId`                          | A string that specifies the template associated with a PingCentral application, when applicable. If a `templateId` is provided, the `environmentId` must be null. |
| `templateVersion`                     | A read-only integer that stores the version of the template currently being used.                                                                                 |
| `type`                                | A string that specifies the application type. Options are `OAuth`, `OIDC`, `SAML_20_SP`, and `PINGACCESS`. This is a required property.                           |
| `unmanaged`                           | A boolean that specifies whether this application is not managed by PingCentral.                                                                                  |
| `usingOutdatedTemplate`               | A boolean that returns `true` if the application is not using the latest template version.                                                                        |

## Client secret data model

| Property       | Description                                          |
| -------------- | ---------------------------------------------------- |
| `clientSecret` | A string that specifies the encrypted client secret. |

## Application promotion history data model

| Property                      | Description                                                                                                                                                     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `applicationId`               | A string that specifies the ID of a promoted PingCentral application. This is a required property, specified in the request URL.                                |
| `environmentId`               | A string that specifies the environment ID associated with the promotion of an application. This is a required property, specified in the request URL.          |
| `environmentName`             | A string that specifies the name of the environment associated with the promotion of an application.                                                            |
| `environmentShortCode`        | A string that specifies the short code of the environment associated with the promotion of an application.                                                      |
| `id`                          | A string that specifies the ID associated with the promotion of a PingCentral application.                                                                      |
| `name`                        | A string that specifies the name of an application at the time it was promoted. This is a required property.                                                    |
| `notPromotedInCurrentVersion` | A boolean that returns `true` if the promotion history was created in the previous version of PingCentral.                                                      |
| `outdatedVersion`             | A boolean that specifies whether a promoted application was created using an outdated version of PingCentral.                                                   |
| `promoted`                    | The time and date when a PingCentral application was promoted.                                                                                                  |
| `type`                        | A string that specifies the type of promoted PingCentral application. Options are `OAuth`, `OIDC`, `SAML_20_SP`, and `PINGACCESS`. This is a required property. |

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
| 422  | The requested could not be completed because of validation error(s).                               |

---

---
title: Certificate Utilities
description: Use PingCentral certificate utility endpoints to convert, encode, read, and validate certificates and key pairs
component: pingcentral
page_id: pingcentral:pingcentral:certificate-utilities/index
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/certificate-utilities/index.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  data-model: Data model
  response-codes: Response codes
---

# Certificate Utilities

The certificate management API endpoints support operations to manage certificate resources.

## Data model

| Property             | Description                                                                    |
| -------------------- | ------------------------------------------------------------------------------ |
| `expires`            | A string that specifies the date at which the certificate expires.             |
| `fileData`           | A string that specifies the certificate data.                                  |
| `issuerDN`           | A string that specifies the certificate's issuer distinguished name value.     |
| `serialNumber`       | A string that specifies the certificate's serial number.                       |
| `signatureAlgorithm` | A string that specifies the certificate's signature algorithm.                 |
| `subjectDN`          | A string that specifies the certificate's subject distinguished name value.    |
| `validFrom`          | A string that specifies the time and date from which the certificate is valid. |
| `version`            | An integer that specifies the certificate's version number.                    |

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
| 422  | The requested could not be completed because of validation error(s).                               |

---

---
title: Certificates
description: Create, read, update, and delete PingCentral certificate resources through the Certificates API
component: pingcentral
page_id: pingcentral:pingcentral:certificates/index
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/certificates/index.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  data-model: Data model
  response-codes: Response codes
---

# Certificates

Use the Certificates API endpoints to manage PingCentral certificates.

## Data model

`CertImportView` - A representation of certificate data with an alias.

| Property   | Type   | Description            |
| ---------- | ------ | ---------------------- |
| `alias`    | String | The certificate alias. |
| `fileData` | String | The certificate data.  |

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
| 422  | The requested could not be completed because of validation error(s).                               |

---

---
title: Convert Certificate
description: Convert a certificate to X.509 format for downloading
component: pingcentral
page_id: pingcentral:pingcentral:certificate-utilities/convert-certificate
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/certificate-utilities/convert-certificate.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Convert Certificate

##

```none
POST {{baseUrl}}/api/v1/certificateUtils/convert
```

The `POST /api/v1/certificateUtils/convert` endpoint converts a certificate to X.509 format for downloading.

### Headers

Authorization

Content-Type      application/json

Cookie      \<string>

X-XSRF-Header      PASS

### Body

raw ( application/json )

```json
"string"
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
curl --location --globoff '{{baseUrl}}/api/v1/certificateUtils/convert' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==' \
--data '"string"'
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/certificateUtils/convert")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
var body = @"""string""";
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

  url := "{{baseUrl}}/api/v1/certificateUtils/convert"
  method := "POST"

  payload := strings.NewReader(`"string"`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/certificateUtils/convert HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Content-Type: application/json
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==

"string"
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "\"string\"");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/certificateUtils/convert")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/certificateUtils/convert",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Content-Type": "application/json",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
  },
  "data": JSON.stringify("string"),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': '{{baseUrl}}/api/v1/certificateUtils/convert',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Content-Type': 'application/json',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  },
  body: JSON.stringify("string")

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests
import json

url = "{{baseUrl}}/api/v1/certificateUtils/convert"

payload = json.dumps("string")
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Content-Type': 'application/json',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/certificateUtils/convert');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Content-Type' => 'application/json',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
));
$request->setBody('"string"');
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

url = URI("{{baseUrl}}/api/v1/certificateUtils/convert")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Content-Type"] = "application/json"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
request.body = JSON.dump("string")

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "\"string\""
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/certificateUtils/convert")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
```

---

---
title: CREATE Application
description: Create a new PingCentral application resource
component: pingcentral
page_id: pingcentral:pingcentral:applications/create-application
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/applications/create-application.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# CREATE Application

##

```none
POST {{baseUrl}}/api/v1/applications
```

The `POST /api/v1/applications` endpoint creates a new application resource.

### Headers

Authorization

Content-Type      application/json

Cookie      \<string>

X-XSRF-Header      PASS

### Body

raw ( application/json )

```json
{
    "applicationOwnerGroups": [
        "<string>",
        "<string>"
    ],
    "applicationOwners": [
        "<string>",
        "<string>"
    ],
    "created": "<dateTime>",
    "description": "<string>",
    "environmentId": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "name": "<string>",
    "pingcentralVersion": "<string>",
    "shouldUpdateToLatestTemplateVersion": "<boolean>",
    "templateId": "<string>",
    "templateVersion": "<int>",
    "type": "<string>",
    "unmanaged": "<boolean>",
    "usingOutdatedTemplate": "<boolean>"
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
curl --location --globoff '{{baseUrl}}/api/v1/applications' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==' \
--data '{
    "applicationOwnerGroups": [
        "<string>",
        "<string>"
    ],
    "applicationOwners": [
        "<string>",
        "<string>"
    ],
    "created": "<dateTime>",
    "description": "<string>",
    "environmentId": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "name": "<string>",
    "pingcentralVersion": "<string>",
    "shouldUpdateToLatestTemplateVersion": "<boolean>",
    "templateId": "<string>",
    "templateVersion": "<int>",
    "type": "<string>",
    "unmanaged": "<boolean>",
    "usingOutdatedTemplate": "<boolean>"
}'
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/applications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
var body = @"{" + "\n" +
@"    ""applicationOwnerGroups"": [" + "\n" +
@"        ""<string>""," + "\n" +
@"        ""<string>""" + "\n" +
@"    ]," + "\n" +
@"    ""applicationOwners"": [" + "\n" +
@"        ""<string>""," + "\n" +
@"        ""<string>""" + "\n" +
@"    ]," + "\n" +
@"    ""created"": ""<dateTime>""," + "\n" +
@"    ""description"": ""<string>""," + "\n" +
@"    ""environmentId"": ""<string>""," + "\n" +
@"    ""id"": ""<string>""," + "\n" +
@"    ""modified"": ""<dateTime>""," + "\n" +
@"    ""name"": ""<string>""," + "\n" +
@"    ""pingcentralVersion"": ""<string>""," + "\n" +
@"    ""shouldUpdateToLatestTemplateVersion"": ""<boolean>""," + "\n" +
@"    ""templateId"": ""<string>""," + "\n" +
@"    ""templateVersion"": ""<int>""," + "\n" +
@"    ""type"": ""<string>""," + "\n" +
@"    ""unmanaged"": ""<boolean>""," + "\n" +
@"    ""usingOutdatedTemplate"": ""<boolean>""" + "\n" +
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

  url := "{{baseUrl}}/api/v1/applications"
  method := "POST"

  payload := strings.NewReader(`{
    "applicationOwnerGroups": [
        "<string>",
        "<string>"
    ],
    "applicationOwners": [
        "<string>",
        "<string>"
    ],
    "created": "<dateTime>",
    "description": "<string>",
    "environmentId": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "name": "<string>",
    "pingcentralVersion": "<string>",
    "shouldUpdateToLatestTemplateVersion": "<boolean>",
    "templateId": "<string>",
    "templateVersion": "<int>",
    "type": "<string>",
    "unmanaged": "<boolean>",
    "usingOutdatedTemplate": "<boolean>"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/applications HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Content-Type: application/json
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==

{
    "applicationOwnerGroups": [
        "<string>",
        "<string>"
    ],
    "applicationOwners": [
        "<string>",
        "<string>"
    ],
    "created": "<dateTime>",
    "description": "<string>",
    "environmentId": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "name": "<string>",
    "pingcentralVersion": "<string>",
    "shouldUpdateToLatestTemplateVersion": "<boolean>",
    "templateId": "<string>",
    "templateVersion": "<int>",
    "type": "<string>",
    "unmanaged": "<boolean>",
    "usingOutdatedTemplate": "<boolean>"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"applicationOwnerGroups\": [\n        \"<string>\",\n        \"<string>\"\n    ],\n    \"applicationOwners\": [\n        \"<string>\",\n        \"<string>\"\n    ],\n    \"created\": \"<dateTime>\",\n    \"description\": \"<string>\",\n    \"environmentId\": \"<string>\",\n    \"id\": \"<string>\",\n    \"modified\": \"<dateTime>\",\n    \"name\": \"<string>\",\n    \"pingcentralVersion\": \"<string>\",\n    \"shouldUpdateToLatestTemplateVersion\": \"<boolean>\",\n    \"templateId\": \"<string>\",\n    \"templateVersion\": \"<int>\",\n    \"type\": \"<string>\",\n    \"unmanaged\": \"<boolean>\",\n    \"usingOutdatedTemplate\": \"<boolean>\"\n}");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/applications")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/applications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Content-Type": "application/json",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
  },
  "data": JSON.stringify({
    "applicationOwnerGroups": [
      "<string>",
      "<string>"
    ],
    "applicationOwners": [
      "<string>",
      "<string>"
    ],
    "created": "<dateTime>",
    "description": "<string>",
    "environmentId": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "name": "<string>",
    "pingcentralVersion": "<string>",
    "shouldUpdateToLatestTemplateVersion": "<boolean>",
    "templateId": "<string>",
    "templateVersion": "<int>",
    "type": "<string>",
    "unmanaged": "<boolean>",
    "usingOutdatedTemplate": "<boolean>"
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
  'url': '{{baseUrl}}/api/v1/applications',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Content-Type': 'application/json',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  },
  body: JSON.stringify({
    "applicationOwnerGroups": [
      "<string>",
      "<string>"
    ],
    "applicationOwners": [
      "<string>",
      "<string>"
    ],
    "created": "<dateTime>",
    "description": "<string>",
    "environmentId": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "name": "<string>",
    "pingcentralVersion": "<string>",
    "shouldUpdateToLatestTemplateVersion": "<boolean>",
    "templateId": "<string>",
    "templateVersion": "<int>",
    "type": "<string>",
    "unmanaged": "<boolean>",
    "usingOutdatedTemplate": "<boolean>"
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

url = "{{baseUrl}}/api/v1/applications"

payload = json.dumps({
  "applicationOwnerGroups": [
    "<string>",
    "<string>"
  ],
  "applicationOwners": [
    "<string>",
    "<string>"
  ],
  "created": "<dateTime>",
  "description": "<string>",
  "environmentId": "<string>",
  "id": "<string>",
  "modified": "<dateTime>",
  "name": "<string>",
  "pingcentralVersion": "<string>",
  "shouldUpdateToLatestTemplateVersion": "<boolean>",
  "templateId": "<string>",
  "templateVersion": "<int>",
  "type": "<string>",
  "unmanaged": "<boolean>",
  "usingOutdatedTemplate": "<boolean>"
})
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Content-Type': 'application/json',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/applications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Content-Type' => 'application/json',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
));
$request->setBody('{\n    "applicationOwnerGroups": [\n        "<string>",\n        "<string>"\n    ],\n    "applicationOwners": [\n        "<string>",\n        "<string>"\n    ],\n    "created": "<dateTime>",\n    "description": "<string>",\n    "environmentId": "<string>",\n    "id": "<string>",\n    "modified": "<dateTime>",\n    "name": "<string>",\n    "pingcentralVersion": "<string>",\n    "shouldUpdateToLatestTemplateVersion": "<boolean>",\n    "templateId": "<string>",\n    "templateVersion": "<int>",\n    "type": "<string>",\n    "unmanaged": "<boolean>",\n    "usingOutdatedTemplate": "<boolean>"\n}');
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

url = URI("{{baseUrl}}/api/v1/applications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Content-Type"] = "application/json"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
request.body = JSON.dump({
  "applicationOwnerGroups": [
    "<string>",
    "<string>"
  ],
  "applicationOwners": [
    "<string>",
    "<string>"
  ],
  "created": "<dateTime>",
  "description": "<string>",
  "environmentId": "<string>",
  "id": "<string>",
  "modified": "<dateTime>",
  "name": "<string>",
  "pingcentralVersion": "<string>",
  "shouldUpdateToLatestTemplateVersion": "<boolean>",
  "templateId": "<string>",
  "templateVersion": "<int>",
  "type": "<string>",
  "unmanaged": "<boolean>",
  "usingOutdatedTemplate": "<boolean>"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"applicationOwnerGroups\": [\n        \"<string>\",\n        \"<string>\"\n    ],\n    \"applicationOwners\": [\n        \"<string>\",\n        \"<string>\"\n    ],\n    \"created\": \"<dateTime>\",\n    \"description\": \"<string>\",\n    \"environmentId\": \"<string>\",\n    \"id\": \"<string>\",\n    \"modified\": \"<dateTime>\",\n    \"name\": \"<string>\",\n    \"pingcentralVersion\": \"<string>\",\n    \"shouldUpdateToLatestTemplateVersion\": \"<boolean>\",\n    \"templateId\": \"<string>\",\n    \"templateVersion\": \"<int>\",\n    \"type\": \"<string>\",\n    \"unmanaged\": \"<boolean>\",\n    \"usingOutdatedTemplate\": \"<boolean>\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/applications")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
  "applicationOwnerGroups": [
    "5b081eed-3100-4ccf-a643-16410c141ad4",
    "52d49ff7-e31d-409a-9085-cb9ce89be9a0"
  ],
  "applicationOwners": [
    "7df2cedf-97fb-4033-9906-8ece5508d8a1",
    "4eef13af-66ef-427f-8c38-0c5100d0e932"
  ],
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the application.",
  "enabled": true,
  "environmentId": "8c5af57e-f665-4c3e-948f-d30f75cfb69c",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Application Name",
  "pingcentralVersion": "1.6.0",
  "shouldUpdateToLatestTemplateVersion": false,
  "templateId": "412ab035-2ae1-4c78-be0b-6a7b401615f1",
  "templateVersion": 2,
  "type": "OAuth",
  "unmanaged": false,
  "usingOutdatedTemplate": false
}
```

---

---
title: CREATE Certificate
description: Add a new trusted certificate to PingCentral
component: pingcentral
page_id: pingcentral:pingcentral:certificates/create-certificate
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/certificates/create-certificate.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# CREATE Certificate

##

```none
POST {{baseUrl}}/api/v1/certificates
```

The `POST /api/v1/certificates` endpoint adds a new trusted certificate to PingCentral defined by the JSON in the request body.

### Headers

Authorization

Content-Type      application/json

Cookie      \<string>

X-XSRF-Header      PASS

### Body

raw ( application/json )

```json
{
    "alias": "<string>",
    "fileData": "<string>"
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
curl --location --globoff '{{baseUrl}}/api/v1/certificates' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==' \
--data '{
    "alias": "<string>",
    "fileData": "<string>"
}'
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/certificates")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
var body = @"{" + "\n" +
@"    ""alias"": ""<string>""," + "\n" +
@"    ""fileData"": ""<string>""" + "\n" +
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

  url := "{{baseUrl}}/api/v1/certificates"
  method := "POST"

  payload := strings.NewReader(`{
    "alias": "<string>",
    "fileData": "<string>"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/certificates HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Content-Type: application/json
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==

{
    "alias": "<string>",
    "fileData": "<string>"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"alias\": \"<string>\",\n    \"fileData\": \"<string>\"\n}");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/certificates")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/certificates",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Content-Type": "application/json",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
  },
  "data": JSON.stringify({
    "alias": "<string>",
    "fileData": "<string>"
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
  'url': '{{baseUrl}}/api/v1/certificates',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Content-Type': 'application/json',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  },
  body: JSON.stringify({
    "alias": "<string>",
    "fileData": "<string>"
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

url = "{{baseUrl}}/api/v1/certificates"

payload = json.dumps({
  "alias": "<string>",
  "fileData": "<string>"
})
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Content-Type': 'application/json',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/certificates');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Content-Type' => 'application/json',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
));
$request->setBody('{\n    "alias": "<string>",\n    "fileData": "<string>"\n}');
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

url = URI("{{baseUrl}}/api/v1/certificates")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Content-Type"] = "application/json"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
request.body = JSON.dump({
  "alias": "<string>",
  "fileData": "<string>"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"alias\": \"<string>\",\n    \"fileData\": \"<string>\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/certificates")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
  "alias": "Cert Name",
  "expires": "2020-12-13T20:30:00Z",
  "fileData": "-----BEGIN CERTIFICATE-----\n \n-----END CERTIFICATE-----",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "issuerDN": "CN=PingCentralCertificate, OU=PingCentral, O=Ping, L=DEN, ST=CO, C=US",
  "serialNumber": 1576269000547,
  "signatureAlgorithm": "SHA256withRSA",
  "status": "Valid\" | \"ExpiredOrNotYetValid",
  "subjectAlternativeNames": [
    "altName1",
    "altName2"
  ],
  "subjectDN": "CN=PingCentralCertificate, OU=PingCentral, O=Ping, L=DEN, ST=CO, C=US",
  "type": "TRUSTED_CERTIFICATE",
  "validFrom": "2019-12-13T20:30:00Z",
  "version": 1
}
```

---

---
title: CREATE Client Secret
description: Generate a client secret for a PingCentral application
component: pingcentral
page_id: pingcentral:pingcentral:applications/create-client-secret
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/applications/create-client-secret.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# CREATE Client Secret

##

```none
GET {{baseUrl}}/api/v1/applications/clientSecretGenerator
```

The `GET /api/v1/applications/clientSecretGenerator` endpoint generates the application's client secret.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff '{{baseUrl}}/api/v1/applications/clientSecretGenerator' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/applications/clientSecretGenerator")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/applications/clientSecretGenerator"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
GET /api/v1/applications/clientSecretGenerator HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/applications/clientSecretGenerator")
  .method("GET", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/applications/clientSecretGenerator",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/applications/clientSecretGenerator',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/applications/clientSecretGenerator"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/applications/clientSecretGenerator');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/applications/clientSecretGenerator")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/applications/clientSecretGenerator")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
  "clientSecret": "NutVaKFpgvV9YNdga581xvhgQ7chBJ+Wvle8FQHXm1Y="
}
```

---

---
title: Create Environments
description: Create a new PingCentral environment resource
component: pingcentral
page_id: pingcentral:pingcentral:environments/create-environments
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/environments/create-environments.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Environments

##

```none
POST {{baseUrl}}/api/v1/environments
```

The `POST /api/v1/environments` endpoint adds a new environment resource.

### Headers

Authorization

Content-Type      application/json

Cookie      \<string>

X-XSRF-Header      PASS

### Body

raw ( application/json )

```json
{
    "description": "<string>",
    "id": "<string>",
    "idpSigningCertificate": "<string>",
    "idpSigningCertificateName": "<string>",
    "idpSigningCertificatePassword": "<string>",
    "name": "<string>",
    "paAuthenticationType": "<string>",
    "paClientId": "<string>",
    "paClientSecret": "<string>",
    "paEnabled": "<boolean>",
    "paHost": "<string>",
    "paPassword": "<string>",
    "paPort": "<integer>",
    "paScopes": "<string>",
    "paSkipVerification": "<boolean>",
    "paTokenEndpoint": "<string>",
    "paUsername": "<string>",
    "paVersion": "<string>",
    "pfAuthenticationType": "<string>",
    "pfClientId": "<string>",
    "pfClientSecret": "<string>",
    "pfHost": "<string>",
    "pfPassword": "<string>",
    "pfPort": "<integer>",
    "pfScopes": "<string>",
    "pfSkipVerification": "<boolean>",
    "pfTokenEndpoint": "<string>",
    "pfUsername": "<string>",
    "pfVersion": "<string>",
    "shielded": "<boolean>",
    "shortCode": "<string>"
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
curl --location --globoff '{{baseUrl}}/api/v1/environments' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==' \
--data '{
    "description": "<string>",
    "id": "<string>",
    "idpSigningCertificate": "<string>",
    "idpSigningCertificateName": "<string>",
    "idpSigningCertificatePassword": "<string>",
    "name": "<string>",
    "paAuthenticationType": "<string>",
    "paClientId": "<string>",
    "paClientSecret": "<string>",
    "paEnabled": "<boolean>",
    "paHost": "<string>",
    "paPassword": "<string>",
    "paPort": "<integer>",
    "paScopes": "<string>",
    "paSkipVerification": "<boolean>",
    "paTokenEndpoint": "<string>",
    "paUsername": "<string>",
    "paVersion": "<string>",
    "pfAuthenticationType": "<string>",
    "pfClientId": "<string>",
    "pfClientSecret": "<string>",
    "pfHost": "<string>",
    "pfPassword": "<string>",
    "pfPort": "<integer>",
    "pfScopes": "<string>",
    "pfSkipVerification": "<boolean>",
    "pfTokenEndpoint": "<string>",
    "pfUsername": "<string>",
    "pfVersion": "<string>",
    "shielded": "<boolean>",
    "shortCode": "<string>"
}'
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/environments")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
var body = @"{" + "\n" +
@"    ""description"": ""<string>""," + "\n" +
@"    ""id"": ""<string>""," + "\n" +
@"    ""idpSigningCertificate"": ""<string>""," + "\n" +
@"    ""idpSigningCertificateName"": ""<string>""," + "\n" +
@"    ""idpSigningCertificatePassword"": ""<string>""," + "\n" +
@"    ""name"": ""<string>""," + "\n" +
@"    ""paAuthenticationType"": ""<string>""," + "\n" +
@"    ""paClientId"": ""<string>""," + "\n" +
@"    ""paClientSecret"": ""<string>""," + "\n" +
@"    ""paEnabled"": ""<boolean>""," + "\n" +
@"    ""paHost"": ""<string>""," + "\n" +
@"    ""paPassword"": ""<string>""," + "\n" +
@"    ""paPort"": ""<integer>""," + "\n" +
@"    ""paScopes"": ""<string>""," + "\n" +
@"    ""paSkipVerification"": ""<boolean>""," + "\n" +
@"    ""paTokenEndpoint"": ""<string>""," + "\n" +
@"    ""paUsername"": ""<string>""," + "\n" +
@"    ""paVersion"": ""<string>""," + "\n" +
@"    ""pfAuthenticationType"": ""<string>""," + "\n" +
@"    ""pfClientId"": ""<string>""," + "\n" +
@"    ""pfClientSecret"": ""<string>""," + "\n" +
@"    ""pfHost"": ""<string>""," + "\n" +
@"    ""pfPassword"": ""<string>""," + "\n" +
@"    ""pfPort"": ""<integer>""," + "\n" +
@"    ""pfScopes"": ""<string>""," + "\n" +
@"    ""pfSkipVerification"": ""<boolean>""," + "\n" +
@"    ""pfTokenEndpoint"": ""<string>""," + "\n" +
@"    ""pfUsername"": ""<string>""," + "\n" +
@"    ""pfVersion"": ""<string>""," + "\n" +
@"    ""shielded"": ""<boolean>""," + "\n" +
@"    ""shortCode"": ""<string>""" + "\n" +
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

  url := "{{baseUrl}}/api/v1/environments"
  method := "POST"

  payload := strings.NewReader(`{
    "description": "<string>",
    "id": "<string>",
    "idpSigningCertificate": "<string>",
    "idpSigningCertificateName": "<string>",
    "idpSigningCertificatePassword": "<string>",
    "name": "<string>",
    "paAuthenticationType": "<string>",
    "paClientId": "<string>",
    "paClientSecret": "<string>",
    "paEnabled": "<boolean>",
    "paHost": "<string>",
    "paPassword": "<string>",
    "paPort": "<integer>",
    "paScopes": "<string>",
    "paSkipVerification": "<boolean>",
    "paTokenEndpoint": "<string>",
    "paUsername": "<string>",
    "paVersion": "<string>",
    "pfAuthenticationType": "<string>",
    "pfClientId": "<string>",
    "pfClientSecret": "<string>",
    "pfHost": "<string>",
    "pfPassword": "<string>",
    "pfPort": "<integer>",
    "pfScopes": "<string>",
    "pfSkipVerification": "<boolean>",
    "pfTokenEndpoint": "<string>",
    "pfUsername": "<string>",
    "pfVersion": "<string>",
    "shielded": "<boolean>",
    "shortCode": "<string>"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/environments HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Content-Type: application/json
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==

{
    "description": "<string>",
    "id": "<string>",
    "idpSigningCertificate": "<string>",
    "idpSigningCertificateName": "<string>",
    "idpSigningCertificatePassword": "<string>",
    "name": "<string>",
    "paAuthenticationType": "<string>",
    "paClientId": "<string>",
    "paClientSecret": "<string>",
    "paEnabled": "<boolean>",
    "paHost": "<string>",
    "paPassword": "<string>",
    "paPort": "<integer>",
    "paScopes": "<string>",
    "paSkipVerification": "<boolean>",
    "paTokenEndpoint": "<string>",
    "paUsername": "<string>",
    "paVersion": "<string>",
    "pfAuthenticationType": "<string>",
    "pfClientId": "<string>",
    "pfClientSecret": "<string>",
    "pfHost": "<string>",
    "pfPassword": "<string>",
    "pfPort": "<integer>",
    "pfScopes": "<string>",
    "pfSkipVerification": "<boolean>",
    "pfTokenEndpoint": "<string>",
    "pfUsername": "<string>",
    "pfVersion": "<string>",
    "shielded": "<boolean>",
    "shortCode": "<string>"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"description\": \"<string>\",\n    \"id\": \"<string>\",\n    \"idpSigningCertificate\": \"<string>\",\n    \"idpSigningCertificateName\": \"<string>\",\n    \"idpSigningCertificatePassword\": \"<string>\",\n    \"name\": \"<string>\",\n    \"paAuthenticationType\": \"<string>\",\n    \"paClientId\": \"<string>\",\n    \"paClientSecret\": \"<string>\",\n    \"paEnabled\": \"<boolean>\",\n    \"paHost\": \"<string>\",\n    \"paPassword\": \"<string>\",\n    \"paPort\": \"<integer>\",\n    \"paScopes\": \"<string>\",\n    \"paSkipVerification\": \"<boolean>\",\n    \"paTokenEndpoint\": \"<string>\",\n    \"paUsername\": \"<string>\",\n    \"paVersion\": \"<string>\",\n    \"pfAuthenticationType\": \"<string>\",\n    \"pfClientId\": \"<string>\",\n    \"pfClientSecret\": \"<string>\",\n    \"pfHost\": \"<string>\",\n    \"pfPassword\": \"<string>\",\n    \"pfPort\": \"<integer>\",\n    \"pfScopes\": \"<string>\",\n    \"pfSkipVerification\": \"<boolean>\",\n    \"pfTokenEndpoint\": \"<string>\",\n    \"pfUsername\": \"<string>\",\n    \"pfVersion\": \"<string>\",\n    \"shielded\": \"<boolean>\",\n    \"shortCode\": \"<string>\"\n}");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/environments")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/environments",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Content-Type": "application/json",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
  },
  "data": JSON.stringify({
    "description": "<string>",
    "id": "<string>",
    "idpSigningCertificate": "<string>",
    "idpSigningCertificateName": "<string>",
    "idpSigningCertificatePassword": "<string>",
    "name": "<string>",
    "paAuthenticationType": "<string>",
    "paClientId": "<string>",
    "paClientSecret": "<string>",
    "paEnabled": "<boolean>",
    "paHost": "<string>",
    "paPassword": "<string>",
    "paPort": "<integer>",
    "paScopes": "<string>",
    "paSkipVerification": "<boolean>",
    "paTokenEndpoint": "<string>",
    "paUsername": "<string>",
    "paVersion": "<string>",
    "pfAuthenticationType": "<string>",
    "pfClientId": "<string>",
    "pfClientSecret": "<string>",
    "pfHost": "<string>",
    "pfPassword": "<string>",
    "pfPort": "<integer>",
    "pfScopes": "<string>",
    "pfSkipVerification": "<boolean>",
    "pfTokenEndpoint": "<string>",
    "pfUsername": "<string>",
    "pfVersion": "<string>",
    "shielded": "<boolean>",
    "shortCode": "<string>"
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
  'url': '{{baseUrl}}/api/v1/environments',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Content-Type': 'application/json',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  },
  body: JSON.stringify({
    "description": "<string>",
    "id": "<string>",
    "idpSigningCertificate": "<string>",
    "idpSigningCertificateName": "<string>",
    "idpSigningCertificatePassword": "<string>",
    "name": "<string>",
    "paAuthenticationType": "<string>",
    "paClientId": "<string>",
    "paClientSecret": "<string>",
    "paEnabled": "<boolean>",
    "paHost": "<string>",
    "paPassword": "<string>",
    "paPort": "<integer>",
    "paScopes": "<string>",
    "paSkipVerification": "<boolean>",
    "paTokenEndpoint": "<string>",
    "paUsername": "<string>",
    "paVersion": "<string>",
    "pfAuthenticationType": "<string>",
    "pfClientId": "<string>",
    "pfClientSecret": "<string>",
    "pfHost": "<string>",
    "pfPassword": "<string>",
    "pfPort": "<integer>",
    "pfScopes": "<string>",
    "pfSkipVerification": "<boolean>",
    "pfTokenEndpoint": "<string>",
    "pfUsername": "<string>",
    "pfVersion": "<string>",
    "shielded": "<boolean>",
    "shortCode": "<string>"
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

url = "{{baseUrl}}/api/v1/environments"

payload = json.dumps({
  "description": "<string>",
  "id": "<string>",
  "idpSigningCertificate": "<string>",
  "idpSigningCertificateName": "<string>",
  "idpSigningCertificatePassword": "<string>",
  "name": "<string>",
  "paAuthenticationType": "<string>",
  "paClientId": "<string>",
  "paClientSecret": "<string>",
  "paEnabled": "<boolean>",
  "paHost": "<string>",
  "paPassword": "<string>",
  "paPort": "<integer>",
  "paScopes": "<string>",
  "paSkipVerification": "<boolean>",
  "paTokenEndpoint": "<string>",
  "paUsername": "<string>",
  "paVersion": "<string>",
  "pfAuthenticationType": "<string>",
  "pfClientId": "<string>",
  "pfClientSecret": "<string>",
  "pfHost": "<string>",
  "pfPassword": "<string>",
  "pfPort": "<integer>",
  "pfScopes": "<string>",
  "pfSkipVerification": "<boolean>",
  "pfTokenEndpoint": "<string>",
  "pfUsername": "<string>",
  "pfVersion": "<string>",
  "shielded": "<boolean>",
  "shortCode": "<string>"
})
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Content-Type': 'application/json',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/environments');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Content-Type' => 'application/json',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
));
$request->setBody('{\n    "description": "<string>",\n    "id": "<string>",\n    "idpSigningCertificate": "<string>",\n    "idpSigningCertificateName": "<string>",\n    "idpSigningCertificatePassword": "<string>",\n    "name": "<string>",\n    "paAuthenticationType": "<string>",\n    "paClientId": "<string>",\n    "paClientSecret": "<string>",\n    "paEnabled": "<boolean>",\n    "paHost": "<string>",\n    "paPassword": "<string>",\n    "paPort": "<integer>",\n    "paScopes": "<string>",\n    "paSkipVerification": "<boolean>",\n    "paTokenEndpoint": "<string>",\n    "paUsername": "<string>",\n    "paVersion": "<string>",\n    "pfAuthenticationType": "<string>",\n    "pfClientId": "<string>",\n    "pfClientSecret": "<string>",\n    "pfHost": "<string>",\n    "pfPassword": "<string>",\n    "pfPort": "<integer>",\n    "pfScopes": "<string>",\n    "pfSkipVerification": "<boolean>",\n    "pfTokenEndpoint": "<string>",\n    "pfUsername": "<string>",\n    "pfVersion": "<string>",\n    "shielded": "<boolean>",\n    "shortCode": "<string>"\n}');
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

url = URI("{{baseUrl}}/api/v1/environments")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Content-Type"] = "application/json"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
request.body = JSON.dump({
  "description": "<string>",
  "id": "<string>",
  "idpSigningCertificate": "<string>",
  "idpSigningCertificateName": "<string>",
  "idpSigningCertificatePassword": "<string>",
  "name": "<string>",
  "paAuthenticationType": "<string>",
  "paClientId": "<string>",
  "paClientSecret": "<string>",
  "paEnabled": "<boolean>",
  "paHost": "<string>",
  "paPassword": "<string>",
  "paPort": "<integer>",
  "paScopes": "<string>",
  "paSkipVerification": "<boolean>",
  "paTokenEndpoint": "<string>",
  "paUsername": "<string>",
  "paVersion": "<string>",
  "pfAuthenticationType": "<string>",
  "pfClientId": "<string>",
  "pfClientSecret": "<string>",
  "pfHost": "<string>",
  "pfPassword": "<string>",
  "pfPort": "<integer>",
  "pfScopes": "<string>",
  "pfSkipVerification": "<boolean>",
  "pfTokenEndpoint": "<string>",
  "pfUsername": "<string>",
  "pfVersion": "<string>",
  "shielded": "<boolean>",
  "shortCode": "<string>"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"description\": \"<string>\",\n    \"id\": \"<string>\",\n    \"idpSigningCertificate\": \"<string>\",\n    \"idpSigningCertificateName\": \"<string>\",\n    \"idpSigningCertificatePassword\": \"<string>\",\n    \"name\": \"<string>\",\n    \"paAuthenticationType\": \"<string>\",\n    \"paClientId\": \"<string>\",\n    \"paClientSecret\": \"<string>\",\n    \"paEnabled\": \"<boolean>\",\n    \"paHost\": \"<string>\",\n    \"paPassword\": \"<string>\",\n    \"paPort\": \"<integer>\",\n    \"paScopes\": \"<string>\",\n    \"paSkipVerification\": \"<boolean>\",\n    \"paTokenEndpoint\": \"<string>\",\n    \"paUsername\": \"<string>\",\n    \"paVersion\": \"<string>\",\n    \"pfAuthenticationType\": \"<string>\",\n    \"pfClientId\": \"<string>\",\n    \"pfClientSecret\": \"<string>\",\n    \"pfHost\": \"<string>\",\n    \"pfPassword\": \"<string>\",\n    \"pfPort\": \"<integer>\",\n    \"pfScopes\": \"<string>\",\n    \"pfSkipVerification\": \"<boolean>\",\n    \"pfTokenEndpoint\": \"<string>\",\n    \"pfUsername\": \"<string>\",\n    \"pfVersion\": \"<string>\",\n    \"shielded\": \"<boolean>\",\n    \"shortCode\": \"<string>\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/environments")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
    "id": "b1376132-9873-4e16-a6ea-6bb7bc772c5c",
    "name": "My PingFed Instance",
    "shortCode": "PF",
    "description": "My PingFed environment",
    "pfHost": "10.101.50.64",
    "pfPort": 9999,
    "pfUsername": "administrator",
    "pfPassword": null,
    "pfSkipVerification": false,
    "pfVersion": "9.2.3.0",
    "pfAuthenticationType": "OAuth2",
    "pfClientId": "oidc_client",
    "pfClientSecret": "clientSecret",
    "pfTokenEndpoint": "https://tokenendpoint.com",
    "pfScopes": "openid admin",
    "paEnabled": false,
    "paHost": null,
    "paPort": 0,
    "paUsername": null,
    "paPassword": null,
    "paSkipVerification": false,
    "paVersion": null,
    "paAuthenticationType": null,
    "paClientId": null,
    "paClientSecret": null,
    "paScopes": null,
    "paTokenEndpoint": null,
    "shielded": false,
    "idpSigningCertificate": null,
    "idpSigningCertificateName": null,
    "idpSigningCertificatePassword": null
}
```

---

---
title: CREATE Group
description: Create a PingCentral group
component: pingcentral
page_id: pingcentral:pingcentral:groups/create-group
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/groups/create-group.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# CREATE Group

##

```none
POST {{baseUrl}}/api/v1/groups
```

Use the `POST {{baseUrl}}/api/v1/groups` request to create a PingCentral group.

### Headers

Authorization

Content-Type      application/json

Cookie      \<string>

X-XSRF-Header      PASS

### Body

raw ( application/json )

```json
{
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the group.",
  "displayName": "All Employees",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "members": [
    {
      "firstName": "Default",
      "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
      "lastName": "User",
      "source": "PASS-ISS",
      "username": "administrator"
    }
  ],
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Company-Employees",
  "source": "PASS-ISS"
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
curl --location --globoff '{{baseUrl}}/api/v1/groups' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==' \
--data '{
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the group.",
  "displayName": "All Employees",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "members": [
    {
      "firstName": "Default",
      "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
      "lastName": "User",
      "source": "PASS-ISS",
      "username": "administrator"
    }
  ],
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Company-Employees",
  "source": "PASS-ISS"
}'
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/groups")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
var body = @"{" + "\n" +
@"  ""created"": ""2020-12-03T12:52:25.973290Z""," + "\n" +
@"  ""description"": ""Description of the group.""," + "\n" +
@"  ""displayName"": ""All Employees""," + "\n" +
@"  ""id"": ""cd00f834-0c26-45ec-9410-cc38156cb4d4""," + "\n" +
@"  ""members"": [" + "\n" +
@"    {" + "\n" +
@"      ""firstName"": ""Default""," + "\n" +
@"      ""id"": ""cd00f834-0c26-45ec-9410-cc38156cb4d4""," + "\n" +
@"      ""lastName"": ""User""," + "\n" +
@"      ""source"": ""PASS-ISS""," + "\n" +
@"      ""username"": ""administrator""" + "\n" +
@"    }" + "\n" +
@"  ]," + "\n" +
@"  ""modified"": ""2020-12-03T12:52:25.973290Z""," + "\n" +
@"  ""name"": ""Company-Employees""," + "\n" +
@"  ""source"": ""PASS-ISS""" + "\n" +
@"}" + "\n" +
@"";
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

  url := "{{baseUrl}}/api/v1/groups"
  method := "POST"

  payload := strings.NewReader(`{
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the group.",
  "displayName": "All Employees",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "members": [
    {
      "firstName": "Default",
      "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
      "lastName": "User",
      "source": "PASS-ISS",
      "username": "administrator"
    }
  ],
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Company-Employees",
  "source": "PASS-ISS"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/groups HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Content-Type: application/json
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==

{
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the group.",
  "displayName": "All Employees",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "members": [
    {
      "firstName": "Default",
      "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
      "lastName": "User",
      "source": "PASS-ISS",
      "username": "administrator"
    }
  ],
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Company-Employees",
  "source": "PASS-ISS"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"created\": \"2020-12-03T12:52:25.973290Z\",\n  \"description\": \"Description of the group.\",\n  \"displayName\": \"All Employees\",\n  \"id\": \"cd00f834-0c26-45ec-9410-cc38156cb4d4\",\n  \"members\": [\n    {\n      \"firstName\": \"Default\",\n      \"id\": \"cd00f834-0c26-45ec-9410-cc38156cb4d4\",\n      \"lastName\": \"User\",\n      \"source\": \"PASS-ISS\",\n      \"username\": \"administrator\"\n    }\n  ],\n  \"modified\": \"2020-12-03T12:52:25.973290Z\",\n  \"name\": \"Company-Employees\",\n  \"source\": \"PASS-ISS\"\n}\n");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/groups")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/groups",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Content-Type": "application/json",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
  },
  "data": JSON.stringify({
    "created": "2020-12-03T12:52:25.973290Z",
    "description": "Description of the group.",
    "displayName": "All Employees",
    "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
    "members": [
      {
        "firstName": "Default",
        "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
        "lastName": "User",
        "source": "PASS-ISS",
        "username": "administrator"
      }
    ],
    "modified": "2020-12-03T12:52:25.973290Z",
    "name": "Company-Employees",
    "source": "PASS-ISS"
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
  'url': '{{baseUrl}}/api/v1/groups',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Content-Type': 'application/json',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  },
  body: JSON.stringify({
    "created": "2020-12-03T12:52:25.973290Z",
    "description": "Description of the group.",
    "displayName": "All Employees",
    "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
    "members": [
      {
        "firstName": "Default",
        "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
        "lastName": "User",
        "source": "PASS-ISS",
        "username": "administrator"
      }
    ],
    "modified": "2020-12-03T12:52:25.973290Z",
    "name": "Company-Employees",
    "source": "PASS-ISS"
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

url = "{{baseUrl}}/api/v1/groups"

payload = json.dumps({
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the group.",
  "displayName": "All Employees",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "members": [
    {
      "firstName": "Default",
      "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
      "lastName": "User",
      "source": "PASS-ISS",
      "username": "administrator"
    }
  ],
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Company-Employees",
  "source": "PASS-ISS"
})
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Content-Type': 'application/json',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/groups');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Content-Type' => 'application/json',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
));
$request->setBody('{\n  "created": "2020-12-03T12:52:25.973290Z",\n  "description": "Description of the group.",\n  "displayName": "All Employees",\n  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",\n  "members": [\n    {\n      "firstName": "Default",\n      "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",\n      "lastName": "User",\n      "source": "PASS-ISS",\n      "username": "administrator"\n    }\n  ],\n  "modified": "2020-12-03T12:52:25.973290Z",\n  "name": "Company-Employees",\n  "source": "PASS-ISS"\n}');
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

url = URI("{{baseUrl}}/api/v1/groups")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Content-Type"] = "application/json"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
request.body = JSON.dump({
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the group.",
  "displayName": "All Employees",
  "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
  "members": [
    {
      "firstName": "Default",
      "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
      "lastName": "User",
      "source": "PASS-ISS",
      "username": "administrator"
    }
  ],
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Company-Employees",
  "source": "PASS-ISS"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"created\": \"2020-12-03T12:52:25.973290Z\",\n  \"description\": \"Description of the group.\",\n  \"displayName\": \"All Employees\",\n  \"id\": \"cd00f834-0c26-45ec-9410-cc38156cb4d4\",\n  \"members\": [\n    {\n      \"firstName\": \"Default\",\n      \"id\": \"cd00f834-0c26-45ec-9410-cc38156cb4d4\",\n      \"lastName\": \"User\",\n      \"source\": \"PASS-ISS\",\n      \"username\": \"administrator\"\n    }\n  ],\n  \"modified\": \"2020-12-03T12:52:25.973290Z\",\n  \"name\": \"Company-Employees\",\n  \"source\": \"PASS-ISS\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/groups")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
    "created": "2020-12-03T12:52:25.973290Z",
    "description": "Description of the group.",
    "displayName": "All Employees",
    "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
    "members": [
        {
            "firstName": "Default",
            "id": "cd00f834-0c26-45ec-9410-cc38156cb4d4",
            "lastName": "User",
            "source": "PASS-ISS",
            "username": "administrator"
        }
    ],
    "modified": "2020-12-03T12:52:25.973290Z",
    "name": "Company-Employees",
    "source": "PASS-ISS"
}
```

---

---
title: CREATE Session (Login)
description: Create a new PingCentral user session by authenticating login credentials
component: pingcentral
page_id: pingcentral:pingcentral:session-login-management/create-session-login
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/session-login-management/create-session-login.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# CREATE Session (Login)

##

```none
POST {{baseUrl}}/api/v1/session/login
```

The `POST /api/v1/session/login` endpoint creates a new user session.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request POST '{{baseUrl}}/api/v1/session/login' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/session/login")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/session/login"
  method := "POST"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/session/login HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/session/login")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/session/login",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/session/login',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/session/login"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/session/login');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/session/login")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/session/login")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
  "aty": [
    "ROLE_AO"
  ],
  "aud": "PASS-AUD",
  "exp": 1607349623,
  "iat": 1607348723,
  "iss": "PASS-ISS",
  "jti": "HiFHMDJED4pc7BeOIue-GZ",
  "oiat": 1607347950,
  "sub": "admin"
}
```

---

---
title: CREATE Template
description: Create a PingCentral template based on an existing PingFederate or PingAccess application
component: pingcentral
page_id: pingcentral:pingcentral:templates/create-template
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/templates/create-template.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# CREATE Template

##

```none
POST {{baseUrl}}/api/v1/templates
```

The `POST /api/v1/templates` endpoint adds a new OAuth, OIDC, SAML, or PingAccess template.

### Headers

Authorization

Content-Type      application/json

Cookie      \<string>

X-XSRF-Header      PASS

### Body

raw ( application/json )

```json
{
    "environmentId": "<string>",
    "name": "<string>",
    "type": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "icon": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "pingcentralVersionAtCreation": "<string>",
    "revisionSummaryViews": [
    {
      "modified": "<dateTime>",
      "modifiedBy": "<string>",
      "revisionNumber": "<int>",
      "updateTemplateComment": "<string>"
    }
  ],
  "updateTemplateComment": "<string>"
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
curl --location --globoff '{{baseUrl}}/api/v1/templates' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==' \
--data '{
    "environmentId": "<string>",
    "name": "<string>",
    "type": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "icon": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "pingcentralVersionAtCreation": "<string>",
    "revisionSummaryViews": [
    {
      "modified": "<dateTime>",
      "modifiedBy": "<string>",
      "revisionNumber": "<int>",
      "updateTemplateComment": "<string>"
    }
  ],
  "updateTemplateComment": "<string>"
}'
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/templates")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
var body = @"{" + "\n" +
@"    ""environmentId"": ""<string>""," + "\n" +
@"    ""name"": ""<string>""," + "\n" +
@"    ""type"": ""<string>""," + "\n" +
@"    ""created"": ""<dateTime>""," + "\n" +
@"    ""description"": ""<string>""," + "\n" +
@"    ""icon"": ""<string>""," + "\n" +
@"    ""id"": ""<string>""," + "\n" +
@"    ""modified"": ""<dateTime>""," + "\n" +
@"    ""pingcentralVersionAtCreation"": ""<string>""," + "\n" +
@"    ""revisionSummaryViews"": [" + "\n" +
@"    {" + "\n" +
@"      ""modified"": ""<dateTime>""," + "\n" +
@"      ""modifiedBy"": ""<string>""," + "\n" +
@"      ""revisionNumber"": ""<int>""," + "\n" +
@"      ""updateTemplateComment"": ""<string>""" + "\n" +
@"    }" + "\n" +
@"  ]," + "\n" +
@"  ""updateTemplateComment"": ""<string>""" + "\n" +
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

  url := "{{baseUrl}}/api/v1/templates"
  method := "POST"

  payload := strings.NewReader(`{
    "environmentId": "<string>",
    "name": "<string>",
    "type": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "icon": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "pingcentralVersionAtCreation": "<string>",
    "revisionSummaryViews": [
    {
      "modified": "<dateTime>",
      "modifiedBy": "<string>",
      "revisionNumber": "<int>",
      "updateTemplateComment": "<string>"
    }
  ],
  "updateTemplateComment": "<string>"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/templates HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Content-Type: application/json
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==

{
    "environmentId": "<string>",
    "name": "<string>",
    "type": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "icon": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "pingcentralVersionAtCreation": "<string>",
    "revisionSummaryViews": [
    {
      "modified": "<dateTime>",
      "modifiedBy": "<string>",
      "revisionNumber": "<int>",
      "updateTemplateComment": "<string>"
    }
  ],
  "updateTemplateComment": "<string>"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"environmentId\": \"<string>\",\n    \"name\": \"<string>\",\n    \"type\": \"<string>\",\n    \"created\": \"<dateTime>\",\n    \"description\": \"<string>\",\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"modified\": \"<dateTime>\",\n    \"pingcentralVersionAtCreation\": \"<string>\",\n    \"revisionSummaryViews\": [\n    {\n      \"modified\": \"<dateTime>\",\n      \"modifiedBy\": \"<string>\",\n      \"revisionNumber\": \"<int>\",\n      \"updateTemplateComment\": \"<string>\"\n    }\n  ],\n  \"updateTemplateComment\": \"<string>\"\n}");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/templates")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/templates",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Content-Type": "application/json",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
  },
  "data": JSON.stringify({
    "environmentId": "<string>",
    "name": "<string>",
    "type": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "icon": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "pingcentralVersionAtCreation": "<string>",
    "revisionSummaryViews": [
      {
        "modified": "<dateTime>",
        "modifiedBy": "<string>",
        "revisionNumber": "<int>",
        "updateTemplateComment": "<string>"
      }
    ],
    "updateTemplateComment": "<string>"
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
  'url': '{{baseUrl}}/api/v1/templates',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Content-Type': 'application/json',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  },
  body: JSON.stringify({
    "environmentId": "<string>",
    "name": "<string>",
    "type": "<string>",
    "created": "<dateTime>",
    "description": "<string>",
    "icon": "<string>",
    "id": "<string>",
    "modified": "<dateTime>",
    "pingcentralVersionAtCreation": "<string>",
    "revisionSummaryViews": [
      {
        "modified": "<dateTime>",
        "modifiedBy": "<string>",
        "revisionNumber": "<int>",
        "updateTemplateComment": "<string>"
      }
    ],
    "updateTemplateComment": "<string>"
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

url = "{{baseUrl}}/api/v1/templates"

payload = json.dumps({
  "environmentId": "<string>",
  "name": "<string>",
  "type": "<string>",
  "created": "<dateTime>",
  "description": "<string>",
  "icon": "<string>",
  "id": "<string>",
  "modified": "<dateTime>",
  "pingcentralVersionAtCreation": "<string>",
  "revisionSummaryViews": [
    {
      "modified": "<dateTime>",
      "modifiedBy": "<string>",
      "revisionNumber": "<int>",
      "updateTemplateComment": "<string>"
    }
  ],
  "updateTemplateComment": "<string>"
})
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Content-Type': 'application/json',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/templates');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Content-Type' => 'application/json',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
));
$request->setBody('{\n    "environmentId": "<string>",\n    "name": "<string>",\n    "type": "<string>",\n    "created": "<dateTime>",\n    "description": "<string>",\n    "icon": "<string>",\n    "id": "<string>",\n    "modified": "<dateTime>",\n    "pingcentralVersionAtCreation": "<string>",\n    "revisionSummaryViews": [\n    {\n      "modified": "<dateTime>",\n      "modifiedBy": "<string>",\n      "revisionNumber": "<int>",\n      "updateTemplateComment": "<string>"\n    }\n  ],\n  "updateTemplateComment": "<string>"\n}');
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

url = URI("{{baseUrl}}/api/v1/templates")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Content-Type"] = "application/json"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
request.body = JSON.dump({
  "environmentId": "<string>",
  "name": "<string>",
  "type": "<string>",
  "created": "<dateTime>",
  "description": "<string>",
  "icon": "<string>",
  "id": "<string>",
  "modified": "<dateTime>",
  "pingcentralVersionAtCreation": "<string>",
  "revisionSummaryViews": [
    {
      "modified": "<dateTime>",
      "modifiedBy": "<string>",
      "revisionNumber": "<int>",
      "updateTemplateComment": "<string>"
    }
  ],
  "updateTemplateComment": "<string>"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"environmentId\": \"<string>\",\n    \"name\": \"<string>\",\n    \"type\": \"<string>\",\n    \"created\": \"<dateTime>\",\n    \"description\": \"<string>\",\n    \"icon\": \"<string>\",\n    \"id\": \"<string>\",\n    \"modified\": \"<dateTime>\",\n    \"pingcentralVersionAtCreation\": \"<string>\",\n    \"revisionSummaryViews\": [\n    {\n      \"modified\": \"<dateTime>\",\n      \"modifiedBy\": \"<string>\",\n      \"revisionNumber\": \"<int>\",\n      \"updateTemplateComment\": \"<string>\"\n    }\n  ],\n  \"updateTemplateComment\": \"<string>\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/templates")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
  "created": "2020-12-03T12:52:25.973290Z",
  "description": "Description of the template.",
  "environmentId": "8c5af57e-f665-4c3e-948f-d30f75cfb69c",
  "icon": "cog",
  "id": "3c0c3547-b2c5-4536-8566-dad1da81cbf6",
  "modified": "2020-12-03T12:52:25.973290Z",
  "name": "Template Name",
  "pingcentralVersionAtCreation": "1.6.0",
  "type": "OAuth",
  "revisionSummaryViews": [
    {
      "modified": "2020-12-03T12:52:25.973290Z",
      "modifiedBy": "administrator",
      "revisionNumber": 1,
      "updateTemplateComment": "Updated to include a new grant type."
    }
  ],
  "updateTemplateComment": "Updated to include a new grant type."
}
```

---

---
title: CREATE User
description: Create a new PingCentral user with a name, user name, and assigned role
component: pingcentral
page_id: pingcentral:pingcentral:users/create-user
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/users/create-user.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# CREATE User

##

```none
POST {{baseUrl}}/api/v1/users
```

The `POST /api/v1/users` endpoint creates a new PingCentral user.

### Headers

Authorization

Content-Type      application/json

Cookie      \<string>

X-XSRF-Header      PASS

### Body

raw ( application/json )

```json
{
  "confirmpassword": "password",
  "firstName": "Tom",
  "lastName": "Jones",
  "password": "password",
  "role": "AO",
  "source": "PASS-ISS",
  "username": "tomjones"
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
curl --location --globoff '{{baseUrl}}/api/v1/users' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==' \
--data '{
  "confirmpassword": "password",
  "firstName": "Tom",
  "lastName": "Jones",
  "password": "password",
  "role": "AO",
  "source": "PASS-ISS",
  "username": "tomjones"
}'
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/users")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
var body = @"{" + "\n" +
@"  ""confirmpassword"": ""password""," + "\n" +
@"  ""firstName"": ""Tom""," + "\n" +
@"  ""lastName"": ""Jones""," + "\n" +
@"  ""password"": ""password""," + "\n" +
@"  ""role"": ""AO""," + "\n" +
@"  ""source"": ""PASS-ISS""," + "\n" +
@"  ""username"": ""tomjones""" + "\n" +
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

  url := "{{baseUrl}}/api/v1/users"
  method := "POST"

  payload := strings.NewReader(`{
  "confirmpassword": "password",
  "firstName": "Tom",
  "lastName": "Jones",
  "password": "password",
  "role": "AO",
  "source": "PASS-ISS",
  "username": "tomjones"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
POST /api/v1/users HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Content-Type: application/json
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==

{
  "confirmpassword": "password",
  "firstName": "Tom",
  "lastName": "Jones",
  "password": "password",
  "role": "AO",
  "source": "PASS-ISS",
  "username": "tomjones"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"confirmpassword\": \"password\",\n  \"firstName\": \"Tom\",\n  \"lastName\": \"Jones\",\n  \"password\": \"password\",\n  \"role\": \"AO\",\n  \"source\": \"PASS-ISS\",\n  \"username\": \"tomjones\"\n}");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/users")
  .method("POST", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/users",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Content-Type": "application/json",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
  },
  "data": JSON.stringify({
    "confirmpassword": "password",
    "firstName": "Tom",
    "lastName": "Jones",
    "password": "password",
    "role": "AO",
    "source": "PASS-ISS",
    "username": "tomjones"
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
  'url': '{{baseUrl}}/api/v1/users',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Content-Type': 'application/json',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  },
  body: JSON.stringify({
    "confirmpassword": "password",
    "firstName": "Tom",
    "lastName": "Jones",
    "password": "password",
    "role": "AO",
    "source": "PASS-ISS",
    "username": "tomjones"
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

url = "{{baseUrl}}/api/v1/users"

payload = json.dumps({
  "confirmpassword": "password",
  "firstName": "Tom",
  "lastName": "Jones",
  "password": "password",
  "role": "AO",
  "source": "PASS-ISS",
  "username": "tomjones"
})
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Content-Type': 'application/json',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/users');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Content-Type' => 'application/json',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
));
$request->setBody('{\n  "confirmpassword": "password",\n  "firstName": "Tom",\n  "lastName": "Jones",\n  "password": "password",\n  "role": "AO",\n  "source": "PASS-ISS",\n  "username": "tomjones"\n}');
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

url = URI("{{baseUrl}}/api/v1/users")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Content-Type"] = "application/json"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
request.body = JSON.dump({
  "confirmpassword": "password",
  "firstName": "Tom",
  "lastName": "Jones",
  "password": "password",
  "role": "AO",
  "source": "PASS-ISS",
  "username": "tomjones"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"confirmpassword\": \"password\",\n  \"firstName\": \"Tom\",\n  \"lastName\": \"Jones\",\n  \"password\": \"password\",\n  \"role\": \"AO\",\n  \"source\": \"PASS-ISS\",\n  \"username\": \"tomjones\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/users")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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
  "id": "32981766-cc07-43a3-875a-41cc39339ba8",
  "source": "PASS-ISS",
  "username": "tomjones",
  "firstName": "Tom",
  "lastName": "Jones",
  "password": null,
  "confirmpassword": null,
  "role": "AO"}
```

---

---
title: CSRF Protection
description: Manage Cross Site Request Forgery protection settings that guard PingCentral against unauthorized HTTP requests from trusted users
component: pingcentral
page_id: pingcentral:pingcentral:csrf-protection/index
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/csrf-protection/index.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-11
section_ids:
  data-model: Data model
  response-codes: Response codes
---

# CSRF Protection

The Cross Site Request Forgery (CSRF) API endpoint supports operations to manage CSRF protection against unauthorized HTTP requests submitted from a trusted users.

## Data model

| Property        | Description                                          |
| --------------- | ---------------------------------------------------- |
| `headerName`    | A string that specifies the name of the HTTP header. |
| `parameterName` | A string that specifies the parameter name.          |
| `token`         | A string that specifies the CSRF token.              |

## Response codes

| Code | Message                                                                                            |
| ---- | -------------------------------------------------------------------------------------------------- |
| 200  | Successful operation.                                                                              |
| 400  | The request could not be completed.                                                                |
| 401  | You do not have access to this resource.                                                           |
| 403  | You do not have permissions or are not licensed to make this request, or your license is exceeded. |
| 404  | The requested resource was not found.                                                              |
| 500  | An unexpected error occurred.                                                                      |

---

---
title: DELETE Application
description: Delete a PingCentral application resource by ID
component: pingcentral
page_id: pingcentral:pingcentral:applications/delete-application
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/applications/delete-application.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# DELETE Application

##

```none
DELETE {{baseUrl}}/api/v1/applications/{{appID}}
```

The `DELETE /api/v1/applications/{{appID}}` endpoint deletes the application resource specified by its ID in the request URL.

When successful, the `DELETE` request returns a code `204 No Content` message.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request DELETE '{{baseUrl}}/api/v1/applications/{{appID}}' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/applications/{{appID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/applications/{{appID}}"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
DELETE /api/v1/applications/{{appID}} HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/applications/{{appID}}")
  .method("DELETE", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/applications/{{appID}}",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/applications/{{appID}}',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/applications/{{appID}}"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/applications/{{appID}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/applications/{{appID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/applications/{{appID}}")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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

```json
```

---

---
title: DELETE Certificate
description: Remove a PingCentral certificate by ID
component: pingcentral
page_id: pingcentral:pingcentral:certificates/delete-certificate
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/certificates/delete-certificate.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# DELETE Certificate

##

```none
DELETE {{baseUrl}}/api/v1/certificates/{{certificateId}}
```

The `DELETE /api/v1/certificates/{{certificateId}}` endpoint removes the certificate with the specified ID in the request URL.

A successful delete operation returns a `204 No Content` response.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request DELETE '{{baseUrl}}/api/v1/certificates/{{certificateId}}' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/certificates/{{certificateId}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/certificates/{{certificateId}}"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
DELETE /api/v1/certificates/{{certificateId}} HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/certificates/{{certificateId}}")
  .method("DELETE", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/certificates/{{certificateId}}",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/certificates/{{certificateId}}',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/certificates/{{certificateId}}"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/certificates/{{certificateId}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/certificates/{{certificateId}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/certificates/{{certificateId}}")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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

```json
```

---

---
title: DELETE Environments
description: Delete the PingCentral environment specified by its ID
component: pingcentral
page_id: pingcentral:pingcentral:environments/delete-environments
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/environments/delete-environments.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
---

# DELETE Environments

##

```none
DELETE {{baseUrl}}/api/v1/environments/{{envID}}
```

The `DELETE /api/v1/environments/{{envID}}` endpoint deletes the environment specified by its ID in the request URL.

When successful, the `DELETE` request returns a code `204 No Content` message.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request DELETE '{{baseUrl}}/api/v1/environments/{{envID}}' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/environments/{{envID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/environments/{{envID}}"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
DELETE /api/v1/environments/{{envID}} HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/environments/{{envID}}")
  .method("DELETE", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/environments/{{envID}}",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/environments/{{envID}}',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/environments/{{envID}}"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/environments/{{envID}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/environments/{{envID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/environments/{{envID}}")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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

---

---
title: DELETE Group
description: Remove the PingCentral group identified by its group ID
component: pingcentral
page_id: pingcentral:pingcentral:groups/delete-group
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/groups/delete-group.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# DELETE Group

##

```none
DELETE {{baseUrl}}/api/v1/groups/{{groupID}}
```

Use the `DELETE {{baseUrl}}/api/v1/groups/{{groupID}}` request to remove the PingCentral group identified by groupID.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request DELETE '{{baseUrl}}/api/v1/groups/{{groupID}}' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/groups/{{groupID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/groups/{{groupID}}"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
DELETE /api/v1/groups/{{groupID}} HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/groups/{{groupID}}")
  .method("DELETE", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/groups/{{groupID}}",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/groups/{{groupID}}',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/groups/{{groupID}}"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/groups/{{groupID}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/groups/{{groupID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/groups/{{groupID}}")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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

```json
```

---

---
title: DELETE Session (Logout)
description: Terminate the current PingCentral user session by logging the user out
component: pingcentral
page_id: pingcentral:pingcentral:session-login-management/delete-session-logout
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/session-login-management/delete-session-logout.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# DELETE Session (Logout)

##

```none
DELETE {{baseUrl}}/api/v1/session/logout
```

The `DELETE /api/v1/session/logout` endpoint terminates the current user session.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request DELETE '{{baseUrl}}/api/v1/session/logout' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/session/logout")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/session/logout"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
DELETE /api/v1/session/logout HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/session/logout")
  .method("DELETE", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/session/logout",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/session/logout',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/session/logout"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/session/logout');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/session/logout")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/session/logout")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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

```json
```

---

---
title: DELETE Template
description: Delete a PingCentral template by ID
component: pingcentral
page_id: pingcentral:pingcentral:templates/delete-template
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/templates/delete-template.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# DELETE Template

##

```none
DELETE {{baseUrl}}/api/v1/templates/{{templateID}}
```

The `DELETE /api/v1/templates/{{templateID}}` endpoint deletes the template with the specified ID.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request DELETE '{{baseUrl}}/api/v1/templates/{{templateID}}' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/templates/{{templateID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/templates/{{templateID}}"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
DELETE /api/v1/templates/{{templateID}} HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/templates/{{templateID}}")
  .method("DELETE", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/templates/{{templateID}}",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/templates/{{templateID}}',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/templates/{{templateID}}"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/templates/{{templateID}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/templates/{{templateID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/templates/{{templateID}}")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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

```json
```

---

---
title: DELETE User
description: Delete a PingCentral user by ID
component: pingcentral
page_id: pingcentral:pingcentral:users/delete-user
canonical_url: https://developer.pingidentity.com/pingcentral/pingcentral/users/delete-user.html
llms_txt: https://developer.pingidentity.com/pingcentral/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# DELETE User

##

```none
DELETE {{baseUrl}}/api/v1/users/{{userID}}
```

The `DELETE /api/v1/users/{{userID}}` endpoint delete the user from a specified ID.

When successful, the `DELETE` request returns a code `204 No Content` message.

### Headers

Authorization

Cookie      \<string>

X-XSRF-Header      PASS

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
curl --location --globoff --request DELETE '{{baseUrl}}/api/v1/users/{{userID}}' \
--header 'Cookie: <string>' \
--header 'X-XSRF-Header: PASS' \
--header 'Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
```

```csharp
var options = new RestClientOptions("{{baseUrl}}/api/v1/users/{{userID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Cookie", "<string>");
request.AddHeader("X-XSRF-Header", "PASS");
request.AddHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==");
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

  url := "{{baseUrl}}/api/v1/users/{{userID}}"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "<string>")
  req.Header.Add("X-XSRF-Header", "PASS")
  req.Header.Add("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")

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
DELETE /api/v1/users/{{userID}} HTTP/1.1
Host: {{baseUrl}}
Cookie: <string>
X-XSRF-Header: PASS
Authorization: Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{baseUrl}}/api/v1/users/{{userID}}")
  .method("DELETE", body)
  .addHeader("Cookie", "<string>")
  .addHeader("X-XSRF-Header", "PASS")
  .addHeader("Authorization", "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{baseUrl}}/api/v1/users/{{userID}}",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Cookie": "<string>",
    "X-XSRF-Header": "PASS",
    "Authorization": "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="
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
  'url': '{{baseUrl}}/api/v1/users/{{userID}}',
  'headers': {
    'Cookie': '<string>',
    'X-XSRF-Header': 'PASS',
    'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{baseUrl}}/api/v1/users/{{userID}}"

payload = {}
headers = {
  'Cookie': '<string>',
  'X-XSRF-Header': 'PASS',
  'Authorization': 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{baseUrl}}/api/v1/users/{{userID}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => '<string>',
  'X-XSRF-Header' => 'PASS',
  'Authorization' => 'Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=='
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

url = URI("{{baseUrl}}/api/v1/users/{{userID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Cookie"] = "<string>"
request["X-XSRF-Header"] = "PASS"
request["Authorization"] = "Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ=="

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{baseUrl}}/api/v1/users/{{userID}}")!,timeoutInterval: Double.infinity)
request.addValue("<string>", forHTTPHeaderField: "Cookie")
request.addValue("PASS", forHTTPHeaderField: "X-XSRF-Header")
request.addValue("Basic e3t1c2VybmFtZX19Ont7cGFzc3dvcmR9fQ==", forHTTPHeaderField: "Authorization")

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

```json
```
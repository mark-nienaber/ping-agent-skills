---
title: Authentication
description: Authenticate PingDirectory and PingDirectoryProxy SCIM 2.0 API requests with an OAuth 2.0 access (bearer) token, as defined by RFC 6750. Obtain the bearer token through an OAuth 2 authorization server, such as PingFederate. Add the bearer token to the Authorization header of your requests.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:authentication
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/authentication.html
---

# Authentication

Authenticate PingDirectory and PingDirectoryProxy SCIM 2.0 API requests with an OAuth 2.0 access (bearer) token, as defined by [RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750). Obtain the bearer token through an OAuth 2 authorization server, such as PingFederate. Add the bearer token to the Authorization header of your requests.

```none
curl --location --request GET '{{apiPath}}/scim/v2/Users/5caa81af-ec05-41ff-a709-c7378007a99c?attributes=userName' \
--header 'Authorization: Bearer eyJraWQiOiJBY2Nlc3MgVG9rZW4gU2lnbmluZ...' \
--header 'Accept: application/scim+json' \
--header 'Accept-Encoding: gzip, deflate'
```

If the access token is missing, expired, or invalid, the server responds with a status code of `401 Unauthorized`.

```json
{
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:Error"
    ],
    "scimType": "invalid_token",
    "status": 401,
    "detail": "Access token is expired or otherwise invalid."
}
```

---

---
title: Authorization
description: For Authentication, you provide an OAuth 2.0 access (bearer) token. That bearer token controls access to which resources and attributes are returned. It does this through a scope that an administrator configures on the server that contains the data. What this means is that regardless of whether you use PingDirectory or PingDirectoryProxy as the endpoint server, you always configure access controls on the PingDirectory server. For more information on configuring SCIM 2.0 on PingDirectory, refer to Configuring SCIM 2.0 on Your Server.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:authorization
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/authorization.html
---

# Authorization

For [Authentication](authentication.html), you provide an OAuth 2.0 access (bearer) token. That bearer token controls access to which resources and attributes are returned. It does this through a scope that an administrator configures on the server that contains the data. What this means is that regardless of whether you use PingDirectory or PingDirectoryProxy as the endpoint server, you always configure access controls on the PingDirectory server. For more information on configuring SCIM 2.0 on PingDirectory, refer to [Configuring SCIM 2.0 on Your Server](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_config_scim_2_server.html).

If access controls determine that you cannot perform the requested operation, the response depends on the request. Refer to the following examples.

* If you send a search request, but you do not have search and read permissions, you get a `200 OK` status code without any results.

* If you send a retrieve, replace, or modify request, but you do not have search and read permissions, you get a `404 Not Found` status code.

  ```json
    {
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:Error"
    ],
    "status": 404,
    "detail": "Request failed:
    correlationID='473ac6b1-50e5-4c48-9d65-8b1fc633280d'"
    }
  ```

* If you send a create, replace, or modify request and you have search and read permissions, but you do not have write permissions, you get a `403 Forbidden status` code.

  ```json
    {
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:Error"
    ],
    "status": "403",
    "detail": "Request failed:
    correlationID='aa74e893-2ae6-4395-b3c4-351f38becb8a'"
    }
  ```

Based on access control configuration, you may be allowed to access a resource but not all of its attributes. See your administrator if you receive incomplete resources, including resources stripped of attributes that are required by the schema.

---

---
title: Create a User
description: The POST /scim/v2/Users endpoint creates a new user resource, providing a complete representation of the resource in the request body. Read-only attributes such as meta can be omitted.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:user-profile-endpoints/create-a-user
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/user-profile-endpoints/create-a-user.html
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create a User

##

```none
POST {{apiPath}}/scim/v2/Users
```

The `POST /scim/v2/Users` endpoint creates a new user resource, providing a complete representation of the resource in the request body. Read-only attributes such as `meta` can be omitted.

If the request is successful, the server returns a response with a status code of `201`, with the resource's canonical URI as the value of the `Location` header (for example, `Location: \https://example.com:443/scim/v2/Users/5caa81af-ec05-41ff-a709-c7378007a99c`.)

The User resource and its attributes are defined in [RFC 7643, Section 4.1](https://tools.ietf.org/html/rfc7643#section-4.1).

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
    "password": "valis",
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
    "password": "valis",
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
@"    ""password"": ""valis""," + "\n" +
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
    "password": "valis",
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
    "password": "valis",
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
RequestBody body = RequestBody.create(mediaType, "{\n    \"emails\": [\n        {\n            \"primary\": true,\n            \"type\": \"work\",\n            \"value\": \"pat.conley@runciter.com\"\n        }\n    ],\n    \"name\": {\n        \"familyName\": \"Conley\",\n        \"formatted\": \"Pat Conley\",\n        \"givenName\": \"Pat\"\n    },\n    \"password\": \"valis\",\n    \"schemas\": [\n        \"urn:pingidentity:schemas:User:1.0\",\n        \"urn:pingidentity:schemas:sample:profile:1.0\"\n    ],\n    \"urn:pingidentity:schemas:sample:profile:1.0\": {\n        \"birthDate\": \"1948-07-13\"\n    },\n    \"userName\": \"pconley\"\n}");
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
  "data": JSON.stringify({
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
    "password": "valis",
    "schemas": [
      "urn:pingidentity:schemas:User:1.0",
      "urn:pingidentity:schemas:sample:profile:1.0"
    ],
    "urn:pingidentity:schemas:sample:profile:1.0": {
      "birthDate": "1948-07-13"
    },
    "userName": "pconley"
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
  'url': '{{apiPath}}/scim/v2/Users',
  'headers': {
    'Content-Type': 'application/scim+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
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
    "password": "valis",
    "schemas": [
      "urn:pingidentity:schemas:User:1.0",
      "urn:pingidentity:schemas:sample:profile:1.0"
    ],
    "urn:pingidentity:schemas:sample:profile:1.0": {
      "birthDate": "1948-07-13"
    },
    "userName": "pconley"
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

url = "{{apiPath}}/scim/v2/Users"

payload = json.dumps({
  "emails": [
    {
      "primary": True,
      "type": "work",
      "value": "pat.conley@runciter.com"
    }
  ],
  "name": {
    "familyName": "Conley",
    "formatted": "Pat Conley",
    "givenName": "Pat"
  },
  "password": "valis",
  "schemas": [
    "urn:pingidentity:schemas:User:1.0",
    "urn:pingidentity:schemas:sample:profile:1.0"
  ],
  "urn:pingidentity:schemas:sample:profile:1.0": {
    "birthDate": "1948-07-13"
  },
  "userName": "pconley"
})
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
$request->setBody('{\n    "emails": [\n        {\n            "primary": true,\n            "type": "work",\n            "value": "pat.conley@runciter.com"\n        }\n    ],\n    "name": {\n        "familyName": "Conley",\n        "formatted": "Pat Conley",\n        "givenName": "Pat"\n    },\n    "password": "valis",\n    "schemas": [\n        "urn:pingidentity:schemas:User:1.0",\n        "urn:pingidentity:schemas:sample:profile:1.0"\n    ],\n    "urn:pingidentity:schemas:sample:profile:1.0": {\n        "birthDate": "1948-07-13"\n    },\n    "userName": "pconley"\n}');
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
request.body = JSON.dump({
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
  "password": "valis",
  "schemas": [
    "urn:pingidentity:schemas:User:1.0",
    "urn:pingidentity:schemas:sample:profile:1.0"
  ],
  "urn:pingidentity:schemas:sample:profile:1.0": {
    "birthDate": "1948-07-13"
  },
  "userName": "pconley"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"emails\": [\n        {\n            \"primary\": true,\n            \"type\": \"work\",\n            \"value\": \"pat.conley@runciter.com\"\n        }\n    ],\n    \"name\": {\n        \"familyName\": \"Conley\",\n        \"formatted\": \"Pat Conley\",\n        \"givenName\": \"Pat\"\n    },\n    \"password\": \"valis\",\n    \"schemas\": [\n        \"urn:pingidentity:schemas:User:1.0\",\n        \"urn:pingidentity:schemas:sample:profile:1.0\"\n    ],\n    \"urn:pingidentity:schemas:sample:profile:1.0\": {\n        \"birthDate\": \"1948-07-13\"\n    },\n    \"userName\": \"pconley\"\n}"
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
title: Data Types and Resources
description: The PingDirectory and PingDirectoryProxy SCIM 2.0 APIs use the data types and resource format specified by the SCIM 2.0 schema standard, RFC 7643.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:data-types-and-resources
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/data-types-and-resources.html
section_ids:
  scim-data-types: SCIM data types
  scim-resource-format: SCIM resource format
  common-attributes: Common attributes
  list-responses: List responses
---

# Data Types and Resources

The PingDirectory and PingDirectoryProxy SCIM 2.0 APIs use the data types and resource format specified by the SCIM 2.0 schema standard, [RFC 7643](https://datatracker.ietf.org/doc/html/rfc7643).

## SCIM data types

SCIM attributes are typed. The following data types are used:

| Data type | Description                                                                                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| string    | A JSON string.                                                                                                                                                                                       |
| boolean   | A JSON boolean value, `true` or `false`.                                                                                                                                                             |
| decimal   | A JSON floating-point number.                                                                                                                                                                        |
| integer   | A JSON integer number.                                                                                                                                                                               |
| dateTime  | A JSON string representing a timestamp. SCIM DateTime values are always encoded as an xsd:dateTime value, as specified by XML Schema, section 3.3.7.                                                 |
| binary    | A JSON string representing a binary value. SCIM binary values are always base64-encoded.                                                                                                             |
| reference | A JSON string representing a reference to another resource. A SCIM reference is always a URI: This can be a URN, the URL of another SCIM resource, or another URL. URLs can be absolute or relative. |
| Object    | A JSON object. A SCIM complex attribute is a composition of sub-attributes. These sub-attributes can have any data type except "complex".                                                            |

A SCIM attribute can also be multi-valued. All members of a multi-valued attribute must be of the same data type.

## SCIM resource format

A SCIM resource is always represented as a JSON object.

SCIM schemas define a resource's attributes. A resource type has at least one core schema and can have zero or more extension schemas. An extension schema can be configured to be either required or optional for a resource to be valid.

SCIM schemas provide the means of namespacing JSON attributes. Every schema is identified by a unique schema URN prefix. When specifying attributes, the schema URN prefix is implied for attributes belonging to the core schema but must be provided for attributes belonging to extension schemas. Consider this example resource:

```none
{
  "schemas": [
    "urn:pingidentity:schemas:User:1.0",
    "urn:pingidentity:schemas:sample:profile:1.0"
  ],
  "id": "5caa81af-ec05-41ff-a709-c7378007a99c",
  "meta": {
    "created": "2016-06-07T13:13:30.873Z",
    "lastModified": "2016-06-07T13:13:30.873Z",
    "resourceType": "Users",
    "location": "\https://example.com/scim/v2/Users/5caa81af-ec05-41ff-a709-c7378007a99c"
  },
  "userName": "joe.chip",
  "name": {
    "familyName": "Chip",
    "formatted": "Joe Chip",
    "givenName": "Joe"
  },
  "accountVerified": true,
  "urn:pingidentity:schemas:sample:profile:1.0": {
    "termsOfService": [
      {
        "id": "urn:X-pingidentity:ToS:StandardUser:1.0",
        "timeStamp": "2014-11-23T16:36:59Z",
        "collector": "urn:X-pingidentity:App:Mobile:1.0"
      }
    ]
  }
}
```

This resource has two schemas:

* A core schema: `urn:pingidentity:schemas:User:1.0`

* An extension schema: `urn:pingidentity:schemas:sample:profile:1.0`

The core schema attribute `userName` can be specified as `userName` or as `+urn:pingidentity:schemas:User:1.0: {"userName": …​}`.

The extension schema attribute `termsOfService` can only be specified as `+urn:pingidentity:schemas:sample:profile:1.0: {"termsOfService": […​]}`.

### Common attributes

In addition to core schema and extension schema attributes, all SCIM resources can have common attributes. These attributes never need to be namespaced with a URN.

| Common attribute | Description                                                                                                          |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| id               | An immutable unique identifier for the resource. This attribute is always present.                                   |
| externalId       | An optional identifier assigned to the resource by the client that provisioned it.                                   |
| meta             | A complex read-only attribute containing resource metadata. Its sub-attributes are described in the following table. |

| Meta sub-attribute | Description                                                    |
| ------------------ | -------------------------------------------------------------- |
| resourceType       | The resource type.                                             |
| created            | A timestamp indicating the resource's creation date.           |
| lastModified       | A timestamp indicating the time of the resource's last update. |
| location           | The canonical URI of the resource.                             |

### List responses

Some SCIM responses, such as search responses, contain multiple resources. These responses are called list responses and include the following fields:

| Field        | Type   | Provided? | Description                                                                                                                           |
| ------------ | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| schemas      | array  | always    | The SCIM schema of the list response. Always contains the value urn:ietf:params:scim:api:messages:2.0:ListResponse.                   |
| totalResults | number | always    | The number of matching resources.                                                                                                     |
| startIndex   | number |           | The index of the first result in the current set of list results. Index starts at 1. Always present if pagination is used.            |
| itemsPerPage | number |           | The number of resources returned per page. Always present if pagination is used.                                                      |
| Resources    | array  | always    | An array consisting of one or more resource objects. For example, this may contain all of the User resources matching a search query. |

---

---
title: Delete a User
description: The DELETE /scim/v2/Users/{{id}} endpoint removes the user specified by the ID in the request URL.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:user-profile-endpoints/delete-a-user
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/user-profile-endpoints/delete-a-user.html
section_ids:
  headers: Headers
  example-request: Example Request
---

# Delete a User

##

```none
DELETE {{apiPath}}/scim/v2/Users/{{id}}
```

The `DELETE /scim/v2/Users/{{id}}` endpoint removes the user specified by the ID in the request URL.

When successful, the response returns a `204 No Content` status code.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/scim+json

Accept      application/scim+json

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
curl --location --globoff --request DELETE '{{apiPath}}/scim/v2/Users/{{id}}' \
--header 'Content-Type: application/scim+json' \
--header 'Accept: application/scim+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/Users/{{id}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Delete);
request.AddHeader("Content-Type", "application/scim+json");
request.AddHeader("Accept", "application/scim+json");
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

  url := "{{apiPath}}/scim/v2/Users/{{id}}"
  method := "DELETE"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/scim+json")
  req.Header.Add("Accept", "application/scim+json")
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
DELETE /scim/v2/Users/{{id}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/scim+json
Accept: application/scim+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/scim+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/Users/{{id}}")
  .method("DELETE", body)
  .addHeader("Content-Type", "application/scim+json")
  .addHeader("Accept", "application/scim+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/Users/{{id}}",
  "method": "DELETE",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/scim+json",
    "Accept": "application/scim+json",
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
  'url': '{{apiPath}}/scim/v2/Users/{{id}}',
  'headers': {
    'Content-Type': 'application/scim+json',
    'Accept': 'application/scim+json',
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

url = "{{apiPath}}/scim/v2/Users/{{id}}"

payload = {}
headers = {
  'Content-Type': 'application/scim+json',
  'Accept': 'application/scim+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/scim/v2/Users/{{id}}');
$request->setMethod(HTTP_Request2::METHOD_DELETE);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/scim+json',
  'Accept' => 'application/scim+json',
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

url = URI("{{apiPath}}/scim/v2/Users/{{id}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Content-Type"] = "application/scim+json"
request["Accept"] = "application/scim+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/Users/{{id}}")!,timeoutInterval: Double.infinity)
request.addValue("application/scim+json", forHTTPHeaderField: "Content-Type")
request.addValue("application/scim+json", forHTTPHeaderField: "Accept")
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

---

---
title: Errors
description: Like all other responses, errors are returned as SCIM responses with a media type of application/scim+json.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:errors
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/errors.html
section_ids:
  password-update-errors: Password update errors
---

# Errors

Like all other responses, errors are returned as SCIM responses with a media type of `application/scim+json`.

Some errors contain correlation IDs that can be used to troubleshoot. For more information, refer to [Troubleshoot the SCIM 2.0 Servlet Extension](https://docs.pingidentity.com/pingdirectory/latest/managing_scim_11_and_20_servlet_extensions/pd_proxy_troubleshoot_scim_2_servelet_ext.html).

| Field    | Type   | Provided? | Description                                                                                                                                                                                                                                                   |
| -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| schemas  | array  | always    | SCIM schemas used in the error message. The schemas array always includes the value `urn:ietf:params:scim:api:messages:2.0:Error` to identify the message as an error. Other schema values can be present if Ping Identity-proprietary error fields are used. |
| status   | number | always    | The HTTP status code of the error. This is always in the `400` or `500` range.                                                                                                                                                                                |
| scimType | string |           | An error code defined by [RFC 7644](https://tools.ietf.org/html/rfc7644), section 3.12.                                                                                                                                                                       |
| detail   | string |           | A human-readable error description. In some cases, this field contains a correlation ID corresponding to log messages on the endpoint server.                                                                                                                 |

```json
{
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:Error"
    ],
    "status": "400",
    "detail": "Request failed: correlationID='269bb1a8-8c51-48b3-83a0-380e1d4b4ab9'"
}
```

## Password update errors

If an error response is returned because of a password update failure, an additional field is provided under the `urn:unboundid:scim:api:messages:2.0:PasswordUpdateError` schema URN.

| Field                | Type  | Provided? | Description                                                                                                                   |
| -------------------- | ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| passwordRequirements | array |           | An array of password quality requirements. These are rules that must be satisfied in order to successfully change a password. |

```json
{
     "detail": "The provided new password cannot be the same as the current password or any password in the user's password history",
     "schemas": [
         "urn:pingidentity:scim:api:messages:2.0:PasswordUpdateError"
     ],
     "scimType": "invalidValue",
     "status": 400,
     "urn:pingidentity:scim:api:messages:2.0:PasswordUpdateError": {
         "passwordRequirements": [
             {
                 "additionalInfo": "The provided new password cannot be the same as the current password or any password in the user's password history.",
                 "description": "The new password must not be the same as the current password.",
                 "requirementSatisfied": false,
                 "type": "notCurrentPassword"
             }
         ]
     }
 }
```

---

---
title: Group search configuration
description: Follow the steps below to configure the directory/proxy to use the SCIM2 API to search for groups or determine the members of a particular group.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:group-search-configuration
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/group-search-configuration.html
---

# Group search configuration

Follow the steps below to configure the directory/proxy to use the SCIM2 API to search for groups or determine the members of a particular group.

1. Create a SCIM Schema

```text
dsconfig create-scim-schema --schema-name urn:pingidentity:schemas:Group:1.0 --set display-name:Group
```

1. Create the SCIM Attributes

```text
dsconfig create-scim-attribute --schema-name urn:pingidentity:schemas:Group:1.0 --attribute-name members --set type:complex

dsconfig create-scim-attribute --schema-name urn:pingidentity:schemas:Group:1.0 --attribute-name displayName
```

1. Create the SCIM Subattribute

```text
dsconfig create-scim-subattribute --schema-name urn:pingidentity:schemas:Group:1.0 --attribute-name members --subattribute-name value --set multi-valued:true
```

1. Create the SCIM Resource Type

```text
dsconfig create-scim-resource-type --type-name Groups --type ldap-mapping --set enabled:true --set endpoint:Groups --set structural-ldap-objectclass:groupOfNames --set include-base-dn:ou=Groups,dc=example,dc=com --set core-schema:urn:pingidentity:schemas:Group:1.0
```

1. Create the SCIM Attribute Mappings

```text
dsconfig create-scim-attribute-mapping --type-name Groups --mapping-name members --set scim-resource-type-attribute:members.value --set ldap-attribute:member --set searchable:true

dsconfig create-scim-attribute-mapping --type-name Groups --mapping-name displayName --set scim-resource-type-attribute:displayName --set ldap-attribute:cn
```

1. Verify the configuration

Verify the configuration by querying the `ResourceTypes` endpoint using a `GET` request.

```bash
curl -k -X GET '{{apiPath}}/ResourceTypes' \
--header 'Authorization: {{accessToken}}' \
--header 'Accept: application/scim+json' \
--header 'Accept-Encoding: gzip, deflate' | jq
```

Sample response:

```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "totalResults": 1,
  "Resources": [
    {
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:ResourceType"
      ],
      "id": "Groups",
      "name": "Groups",
      "endpoint": "Groups",
      "schema": "urn:pingidentity:schemas:Group:1.0",
      "meta": {
        "resourceType": "ResourceType",
        "location": "\https://example.com/scim/v2/ResourceTypes/Groups"
      }
    }
  ]
}
```

---

---
title: Overview
description: The PingDirectory and PingDirectoryProxy SCIM 2.0 APIs are a set of REST interfaces based on the SCIM (System for Cross-domain Identity Management) 2.0 standard. With these APIs, you can:
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:overview
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/overview.html
---

# Overview

The PingDirectory and PingDirectoryProxy SCIM 2.0 APIs are a set of REST interfaces based on the [SCIM (System for Cross-domain Identity Management) 2.0](http://www.simplecloud.info/) standard. With these APIs, you can:

* Create users.

* Search for users.

* Retrieve and update a user's profile.

* Change a user's password.

* Manage a user's login sessions.

* Retrieve a user's history of consent to data access.

* Manage second factor authentication settings.

With SCIM 2.0, any type of data is called a resource type. One or more schemas specify the attributes available for any given resource type. Resources are formatted as JSON and are requested using standard HTTP methods such as `GET`, `POST`, or `PATCH`. For more information about SCIM 2.0, refer to [RFC 7642](https://tools.ietf.org/html/rfc7642), [RFC 7643](https://datatracker.ietf.org/doc/html/rfc7643), and [RFC 7644](https://datatracker.ietf.org/doc/html/rfc7644).

To use these APIs, you must configure PingDirectory or PingDirectoryProxy for SCIM 2.0. You can set up PingDirectory as a stand-alone server. Whereas, you must set up PingDirectoryProxy with an external PingDirectory server.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To configure either server for SCIM 2.0, you must enable encryption. If you configure PingDirectoryProxy as the SCIM 2.0 server, then it and its backend servers need to be using the same encryption settings definition. For more information on importing and exporting encryption settings definitions, refer to [Encrypting Sensitive Data](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_encrypt_sensitive_data.html). |

For more information on configuring PingDirectory for SCIM 2.0, refer to [Configuring SCIM 2.0 on Your Server](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_config_scim_2_server.html). For more information on configuring PingDirectoryProxy for SCIM 2.0, refer to the [PingDirectoryProxy Server Administration Guide](https://docs.pingidentity.com/pingdirectory/latest/pingdirectoryproxy_server_administration_guide/pd_proxy_intro_pdproxy_server.html).

These topics provide the following information about the PingDirectory and PingDirectoryProxy SCIM 2.0 APIs:

* [Data types and resources](data-types-and-resources.html): Data types and resource format specified by the SCIM 2.0 schema standard.

* [Authorization](authorization.html): Authorization to access SCIM API resources.

* [Authentication](authentication.html): Authentication requirement to access SCIM APIs.

* [Requests and responses](requests-and-responses.html): SCIM API requests and responses.

* [Errors](errors.html): SCIM 2.0 errors.

* [Service metadata endpoints](service-metadata-endpoints.html): SCIM 2.0 service metadata endpoints.

* [User profile endpoints](user-profile-endpoints.html): SCIM 2.0 user profile endpoints.

---

---
title: PingDirectory and PingDirectoryProxy SCIM 2.0 API Reference
description: Before you read the PingDirectory and PingDirectoryProxy SCIM 2.0 API topics or use the API, review the following:
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:introduction
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/introduction.html
---

# PingDirectory and PingDirectoryProxy SCIM 2.0 API Reference

Before you read the PingDirectory and PingDirectoryProxy SCIM 2.0 API topics or use the API, review the following:

* [PingDirectory Server Administration Guide](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_intro_pindirectory_server.html)

* [PingDirectoryProxy Server Administration Guide](https://docs.pingidentity.com/pingdirectory/latest/pingdirectoryproxy_server_administration_guide/pd_proxy_intro_pdproxy_server.html)

* [SCIM Overview](http://www.simplecloud.info/)

* [RFC 7643, System for Cross-domain Identity Management: Core Schema](https://datatracker.ietf.org/doc/html/rfc7643)

* [RFC 7644, System for Cross-domain Identity Management: Protocol](https://datatracker.ietf.org/doc/html/rfc7644)

In addition, ensure you are familiar with HTTP headers, methods, and response codes. For more information, refer to the following articles:

* [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

* [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

* [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

---
title: Read a SCIM Service Provider Configuration
description: The GET /scim/v2/ServiceProviderConfig endpoint returns read-only metadata indicating the server's OAuth 2.0 authentication scheme and its support for optional or configurable SCIM features.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:service-metadata-endpoints/read-a-scim-service-provider-configuration
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/service-metadata-endpoints/read-a-scim-service-provider-configuration.html
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read a SCIM Service Provider Configuration

##

```none
GET {{apiPath}}/scim/v2/ServiceProviderConfig
```

The `GET /scim/v2/ServiceProviderConfig` endpoint returns read-only metadata indicating the server's OAuth 2.0 authentication scheme and its support for optional or configurable SCIM features.

`ServiceProviderConfig` objects and their attributes are defined in [RFC 7643, section 5](https://tools.ietf.org/html/rfc7643#section-5).

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
curl --location --globoff '{{apiPath}}/scim/v2/ServiceProviderConfig' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/ServiceProviderConfig")
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

  url := "{{apiPath}}/scim/v2/ServiceProviderConfig"
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
GET /scim/v2/ServiceProviderConfig HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/ServiceProviderConfig")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/ServiceProviderConfig",
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
  'url': '{{apiPath}}/scim/v2/ServiceProviderConfig',
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

url = "{{apiPath}}/scim/v2/ServiceProviderConfig"

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
$request->setUrl('{{apiPath}}/scim/v2/ServiceProviderConfig');
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

url = URI("{{apiPath}}/scim/v2/ServiceProviderConfig")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/ServiceProviderConfig")!,timeoutInterval: Double.infinity)
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
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig"
    ],
    "patch": {
        "supported": true
    },
    "bulk": {
        "supported": false,
        "maxOperations": 0,
        "maxPayloadSize": 0
    },
    "filter": {
        "supported": true,
        "maxResults": 500
    },
    "changePassword": {
        "supported": true
    },
    "sort": {
        "supported": false
    },
    "etag": {
        "supported": false
    },
    "authenticationSchemes": [
        {
            "name": "OAuth 2.0 Bearer Token",
            "description": "The OAuth 2.0 Bearer Token Authentication scheme. OAuth enables clients to access protected resources by obtaining an access token, which is defined in RFC 6750 as \"a string representing an access authorization issued to the client\", rather than using the resource owner's credentials directly.",
            "specUri": "http://tools.ietf.org/html/rfc6750",
            "type": "oauthbearertoken",
            "primary": true
        }
    ],
    "meta": {
        "resourceType": "ServiceProviderConfig",
        "location": "https://example.com/scim/v2/ServiceProviderConfig"
    }
}
```

---

---
title: Read One SCIM Resource Type
description: The GET /scim/v2/ResourceTypes/{{id}} endpoint retrieves a specific SCIM resource type, specified by its ID.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:service-metadata-endpoints/read-a-scim-resource-type
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/service-metadata-endpoints/read-a-scim-resource-type.html
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read One SCIM Resource Type

##

```none
GET {{apiPath}}/scim/v2/ResourceTypes/{{id}}
```

The `GET /scim/v2/ResourceTypes/{{id}}` endpoint retrieves a specific SCIM resource type, specified by its ID.

Resource type objects and their attributes are defined in [RFC 7643, section 6](https://datatracker.ietf.org/doc/html/rfc7643#section-6).

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
curl --location --globoff '{{apiPath}}/scim/v2/ResourceTypes/{{id}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/ResourceTypes/{{id}}")
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

  url := "{{apiPath}}/scim/v2/ResourceTypes/{{id}}"
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
GET /scim/v2/ResourceTypes/{{id}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/ResourceTypes/{{id}}")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/ResourceTypes/{{id}}",
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
  'url': '{{apiPath}}/scim/v2/ResourceTypes/{{id}}',
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

url = "{{apiPath}}/scim/v2/ResourceTypes/{{id}}"

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
$request->setUrl('{{apiPath}}/scim/v2/ResourceTypes/{{id}}');
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

url = URI("{{apiPath}}/scim/v2/ResourceTypes/{{id}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/ResourceTypes/{{id}}")!,timeoutInterval: Double.infinity)
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
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:ResourceType"
    ],
    "id": "Users",
    "name": "Users",
    "endpoint": "Users",
    "schema": "urn:pingidentity:schemas:User:1.0",
    "schemaExtensions": [
        {
            "schema": "urn:pingidentity:schemas:sample:profile:1.0",
            "required": false
        }
    ],
    "meta": {
        "resourceType": "ResourceType",
        "location": "https://example.com/scim/v2/ResourceTypes/Users"
    }
}
```

---

---
title: Read One SCIM Schema
description: The GET /scim/v2/Schemas/{{id}} endpoint retrieves a specific SCIM schema, specified by its ID, which is always a URN.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:service-metadata-endpoints/read-a-scim-schema
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/service-metadata-endpoints/read-a-scim-schema.html
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read One SCIM Schema

##

```none
GET {{apiPath}}/scim/v2/Schemas/{{id}}
```

The `GET /scim/v2/Schemas/{{id}}` endpoint retrieves a specific SCIM schema, specified by its ID, which is always a URN.

Schema objects and their attributes are defined by [RFC 7643, section 7](https://datatracker.ietf.org/doc/html/rfc7643#section-7).

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
curl --location --globoff '{{apiPath}}/scim/v2/Schemas/{{id}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/Schemas/{{id}}")
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

  url := "{{apiPath}}/scim/v2/Schemas/{{id}}"
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
GET /scim/v2/Schemas/{{id}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/Schemas/{{id}}")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/Schemas/{{id}}",
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
  'url': '{{apiPath}}/scim/v2/Schemas/{{id}}',
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

url = "{{apiPath}}/scim/v2/Schemas/{{id}}"

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
$request->setUrl('{{apiPath}}/scim/v2/Schemas/{{id}}');
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

url = URI("{{apiPath}}/scim/v2/Schemas/{{id}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/Schemas/{{id}}")!,timeoutInterval: Double.infinity)
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
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Schema"
    ],
    "id": "urn:pingidentity:schemas:User:1.0",
    "name": "User",
    "attributes": [
        {
            "name": "accountVerified",
            "type": "boolean",
            "multiValued": false,
            "required": false,
            "caseExact": false,
            "mutability": "readWrite",
            "returned": "default",
            "uniqueness": "none"
        },
        {
            "name": "addresses",
            "type": "complex",
            "subAttributes": [
                {
                    "name": "country",
                    "type": "string",
                    "multiValued": false,
                    "required": false,
                    "caseExact": false,
                    "mutability": "readWrite",
                    "returned": "default",
                    "uniqueness": "none"
                }...
```

---

---
title: Read One User
description: The GET /scim/v2/Users/{{id}} endpoint retrieves information for the user specified by the ID in the request URL.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:user-profile-endpoints/read-a-user
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/user-profile-endpoints/read-a-user.html
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read One User

##

```none
GET {{apiPath}}/scim/v2/Users/{{id}}
```

The `GET /scim/v2/Users/{{id}}` endpoint retrieves information for the user specified by the ID in the request URL.

The User resource and its attributes are defined in [RFC 7643, Section 4.1](https://tools.ietf.org/html/rfc7643#section-4.1).

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/scim+json

Accept      application/scim+json

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
curl --location --globoff '{{apiPath}}/scim/v2/Users/{{id}}' \
--header 'Content-Type: application/scim+json' \
--header 'Accept: application/scim+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/Users/{{id}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Content-Type", "application/scim+json");
request.AddHeader("Accept", "application/scim+json");
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

  url := "{{apiPath}}/scim/v2/Users/{{id}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/scim+json")
  req.Header.Add("Accept", "application/scim+json")
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
GET /scim/v2/Users/{{id}} HTTP/1.1
Host: {{apiPath}}
Content-Type: application/scim+json
Accept: application/scim+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/scim+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/Users/{{id}}")
  .method("GET", body)
  .addHeader("Content-Type", "application/scim+json")
  .addHeader("Accept", "application/scim+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/Users/{{id}}",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/scim+json",
    "Accept": "application/scim+json",
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
  'url': '{{apiPath}}/scim/v2/Users/{{id}}',
  'headers': {
    'Content-Type': 'application/scim+json',
    'Accept': 'application/scim+json',
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

url = "{{apiPath}}/scim/v2/Users/{{id}}"

payload = {}
headers = {
  'Content-Type': 'application/scim+json',
  'Accept': 'application/scim+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/scim/v2/Users/{{id}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/scim+json',
  'Accept' => 'application/scim+json',
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

url = URI("{{apiPath}}/scim/v2/Users/{{id}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Content-Type"] = "application/scim+json"
request["Accept"] = "application/scim+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/Users/{{id}}")!,timeoutInterval: Double.infinity)
request.addValue("application/scim+json", forHTTPHeaderField: "Content-Type")
request.addValue("application/scim+json", forHTTPHeaderField: "Accept")
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
title: Read SCIM Resource Types
description: The GET /scim/v2/ResourceTypes endpoint returns all of the SCIM resource types configured for use on this server. Use this information to determine the endpoint, core schema, and extension schemas of any resource types supported by the server.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:service-metadata-endpoints/read-scim-resource-types
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/service-metadata-endpoints/read-scim-resource-types.html
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read SCIM Resource Types

##

```none
GET {{apiPath}}/scim/v2/ResourceTypes
```

The `GET /scim/v2/ResourceTypes` endpoint returns all of the SCIM resource types configured for use on this server. Use this information to determine the endpoint, core schema, and extension schemas of any resource types supported by the server.

The response is formatted as a list response, with one or more resource type objects in the `Resources` field.

Resource type objects and their attributes are defined in [RFC 7643, section 6](https://tools.ietf.org/html/rfc7643#section-6).

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
curl --location --globoff '{{apiPath}}/scim/v2/ResourceTypes' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/ResourceTypes")
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

  url := "{{apiPath}}/scim/v2/ResourceTypes"
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
GET /scim/v2/ResourceTypes HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/ResourceTypes")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/ResourceTypes",
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
  'url': '{{apiPath}}/scim/v2/ResourceTypes',
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

url = "{{apiPath}}/scim/v2/ResourceTypes"

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
$request->setUrl('{{apiPath}}/scim/v2/ResourceTypes');
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

url = URI("{{apiPath}}/scim/v2/ResourceTypes")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/ResourceTypes")!,timeoutInterval: Double.infinity)
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
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "totalResults": 1,
    "Resources": [
        {
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:ResourceType"
            ],
            "id": "Users",
            "name": "Users",
            "endpoint": "Users",
            "schema": "urn:pingidentity:schemas:User:1.0",
            "schemaExtensions": [
                {
                    "schema": "urn:pingidentity:schemas:sample:profile:1.0",
                    "required": false
                }
            ],
            "meta": {
                "resourceType": "ResourceType",
                "location": "https://example.com/scim/v2/ResourceTypes/Users"
            }
        }
    ]
}
```

---

---
title: Read SCIM Schemas
description: The GET /scim/v2/Schemas endpoint lists the SCIM schemas configured for use on this server. These schemas define the various attributes available to resource types.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:service-metadata-endpoints/read-scim-schemas
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/service-metadata-endpoints/read-scim-schemas.html
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read SCIM Schemas

##

```none
GET {{apiPath}}/scim/v2/Schemas
```

The `GET /scim/v2/Schemas` endpoint lists the SCIM schemas configured for use on this server. These schemas define the various attributes available to resource types.

The response is formatted as a list response, with one or more schema objects in the Resources field.

Schema objects and their attributes are defined by [RFC 7643, section 7](https://datatracker.ietf.org/doc/html/rfc7643#section-7).

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
curl --location --globoff '{{apiPath}}/scim/v2/Schemas' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/Schemas")
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

  url := "{{apiPath}}/scim/v2/Schemas"
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
GET /scim/v2/Schemas HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/Schemas")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/Schemas",
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
  'url': '{{apiPath}}/scim/v2/Schemas',
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

url = "{{apiPath}}/scim/v2/Schemas"

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
$request->setUrl('{{apiPath}}/scim/v2/Schemas');
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

url = URI("{{apiPath}}/scim/v2/Schemas")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/Schemas")!,timeoutInterval: Double.infinity)
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
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "totalResults": 2,
    "Resources": [
      {
          "schemas": [
              "urn:ietf:params:scim:schemas:core:2.0:Schema"
          ],
          "id": "urn:pingidentity:schemas:User:1.0",
          "name": "User",
          "attributes": [
              {
                  "name": "accountVerified",
                  "type": "boolean",
                  "multiValued": false,
                  "required": false,
                  "caseExact": false,
                  "mutability": "readWrite",
                  "returned": "default",
                  "uniqueness": "none"
              },
              {
                  "name": "addresses",
                  "type": "complex",
                  "subAttributes": [
                      {
                          "name": "country",
                          "type": "string",
                          "multiValued": false,
                          "required": false,
                          "caseExact": false,
                          "mutability": "readWrite",
                          "returned": "default",
                          "uniqueness": "none"
                      } ...
```

---

---
title: READ search group members by group display name
description: Use the GET /Groups endpoint to filter for matching group member resources.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:user-profile-endpoints/get-read-search-group-members-display-name
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/user-profile-endpoints/get-read-search-group-members-display-name.html
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# READ search group members by group display name

##

```none
GET {{apiPath}}/Groups/?filter=displayName eq "group-9"
```

Use the `GET /Groups` endpoint to filter for matching group member resources.

This example shows `/Groups/?filter=displayName eq "group-9"` using the group's `displayName` query parameter and `eq` operator.

### Prerequisites

* Complete the configuration steps outlined in [Group search configuration](../group-search-configuration.html).

If the request is valid, the response returns a `200` status code.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/scim+json

Accept      application/scim+json

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
curl --location --globoff '{{apiPath}}/Groups/?filter=displayName%20eq%20%22group-9%22' \
--header 'Accept: application/scim+json' \
--header 'Content-Type: application/scim+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/Groups/?filter=displayName eq \"group-9\"")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Accept", "application/scim+json");
request.AddHeader("Content-Type", "application/scim+json");
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

  url := "{{apiPath}}/Groups/?filter=displayName%20eq%20%22group-9%22"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Accept", "application/scim+json")
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
GET /Groups/?filter=displayName eq "group-9" HTTP/1.1
Host: {{apiPath}}
Accept: application/scim+json
Content-Type: application/scim+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/scim+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/Groups/?filter=displayName eq \"group-9\"")
  .method("GET", body)
  .addHeader("Accept", "application/scim+json")
  .addHeader("Content-Type", "application/scim+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/Groups/?filter=displayName eq \"group-9\"",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/scim+json",
    "Content-Type": "application/scim+json",
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
  'url': '{{apiPath}}/Groups/?filter=displayName eq "group-9"',
  'headers': {
    'Accept': 'application/scim+json',
    'Content-Type': 'application/scim+json',
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

url = "{{apiPath}}/Groups/?filter=displayName eq \"group-9\""

payload = {}
headers = {
  'Accept': 'application/scim+json',
  'Content-Type': 'application/scim+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/Groups/?filter=displayName eq "group-9"');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Accept' => 'application/scim+json',
  'Content-Type' => 'application/scim+json',
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

url = URI("{{apiPath}}/Groups/?filter=displayName eq \"group-9\"")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Accept"] = "application/scim+json"
request["Content-Type"] = "application/scim+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/Groups/?filter=displayName%20eq%20%22group-9%22")!,timeoutInterval: Double.infinity)
request.addValue("application/scim+json", forHTTPHeaderField: "Accept")
request.addValue("application/scim+json", forHTTPHeaderField: "Content-Type")
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

```json
{
    "displayName": "test-group",
    "members": {
        "value": [
            "uid=user.0,ou=People,dc=example,dc=com",
            "uid=user.1,ou=People,dc=example,dc=com",
            "uid=user.2,ou=People,dc=example,dc=com",
            "uid=user.3,ou=People,dc=example,dc=com",
            "uid=user.4,ou=People,dc=example,dc=com",
            "uid=user.5,ou=People,dc=example,dc=com",
            "uid=user.6,ou=People,dc=example,dc=com",
            "uid=user.7,ou=People,dc=example,dc=com",
            "uid=user.8,ou=People,dc=example,dc=com",
            "uid=user.9,ou=People,dc=example,dc=com"
        ]
    },
    "id": "1a8e021b-c7b0-4bd9-8e2d-af5691c035ce",
    "meta": {
        "resourceType": "Groups",
        "location": "https://example.com:443/scim/v2/Groups/1a8e021b-c7b0-4bd9-8e2d-af5691c035ce"
    },
    "schemas": [
        "urn:pingidentity:schemas:Group:1.0"
    ]
}
```

---

---
title: READ search group members by group entry ID
description: The GET /Groups/{{groupEntryID}} endpoint returns a group's members by performing a GET request with a specified group entry ID.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:user-profile-endpoints/get-read-search-group-members-entry-id
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/user-profile-endpoints/get-read-search-group-members-entry-id.html
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# READ search group members by group entry ID

##

```none
GET {{apiPath}}/Groups/{{groupEntryID}}
```

The `GET /Groups/{{groupEntryID}}` endpoint returns a group's members by performing a `GET` request with a specified group entry ID.

### Prerequisites

* Complete the configuration steps outlined in [Group search configuration](../group-search-configuration.html).

If the request is valid, the response returns a `200` status code.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/scim+json

Accept      application/scim+json

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
curl --location --globoff '{{apiPath}}/Groups/{{groupEntryID}}' \
--header 'Accept: application/scim+json' \
--header 'Content-Type: application/scim+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/Groups/{{groupEntryID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Accept", "application/scim+json");
request.AddHeader("Content-Type", "application/scim+json");
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

  url := "{{apiPath}}/Groups/{{groupEntryID}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Accept", "application/scim+json")
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
GET /Groups/{{groupEntryID}} HTTP/1.1
Host: {{apiPath}}
Accept: application/scim+json
Content-Type: application/scim+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/scim+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/Groups/{{groupEntryID}}")
  .method("GET", body)
  .addHeader("Accept", "application/scim+json")
  .addHeader("Content-Type", "application/scim+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/Groups/{{groupEntryID}}",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/scim+json",
    "Content-Type": "application/scim+json",
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
  'url': '{{apiPath}}/Groups/{{groupEntryID}}',
  'headers': {
    'Accept': 'application/scim+json',
    'Content-Type': 'application/scim+json',
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

url = "{{apiPath}}/Groups/{{groupEntryID}}"

payload = {}
headers = {
  'Accept': 'application/scim+json',
  'Content-Type': 'application/scim+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/Groups/{{groupEntryID}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Accept' => 'application/scim+json',
  'Content-Type' => 'application/scim+json',
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

url = URI("{{apiPath}}/Groups/{{groupEntryID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Accept"] = "application/scim+json"
request["Content-Type"] = "application/scim+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/Groups/{{groupEntryID}}")!,timeoutInterval: Double.infinity)
request.addValue("application/scim+json", forHTTPHeaderField: "Accept")
request.addValue("application/scim+json", forHTTPHeaderField: "Content-Type")
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
  "displayName": "test-group",
  "members": {
    "value": [
      "uid=user.0,ou=People,dc=example,dc=com",
      "uid=user.1,ou=People,dc=example,dc=com",
      "uid=user.2,ou=People,dc=example,dc=com",
      "uid=user.3,ou=People,dc=example,dc=com",
      "uid=user.4,ou=People,dc=example,dc=com",
      "uid=user.5,ou=People,dc=example,dc=com",
      "uid=user.6,ou=People,dc=example,dc=com",
      "uid=user.7,ou=People,dc=example,dc=com",
      "uid=user.8,ou=People,dc=example,dc=com",
      "uid=user.9,ou=People,dc=example,dc=com"
    ]
  },
  "id": "1a8e021b-c7b0-4bd9-8e2d-af5691c035ce",
  "meta": {
    "resourceType": "Groups",
    "location": "https://example.com:443/scim/v2/Groups/1a8e021b-c7b0-4bd9-8e2d-af5691c035ce"
  },
  "schemas": [
    "urn:pingidentity:schemas:Group:1.0"
  ]
}
```

---

---
title: Requests and Responses
description: Each resource has an identifier. The resource type name (Users) is combined with the identifier (5caa81af-ec05-41ff-a709-c7378007a99c) to uniquely identify the resource to the PingDirectory or PingDirectoryProxy Server. For example:
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:requests-and-responses
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/requests-and-responses.html
section_ids:
  http-request-headers: HTTP request headers
  updating-resources: Updating resources
  specifying-attributes-to-return: Specifying attributes to return
  filtering-searches: Filtering searches
  pagination: Pagination
---

# Requests and Responses

Each resource has an identifier. The resource type name (`Users`) is combined with the identifier (`5caa81af-ec05-41ff-a709-c7378007a99c`) to uniquely identify the resource to the PingDirectory or PingDirectoryProxy Server. For example:

```none
/scim/v2/Users/5caa81af-ec05-41ff-a709-c7378007a99c
```

All requests and responses use UTF-8 character encoding and are formatted as JSON.

## HTTP request headers

* `Accept`

  Provide this header with a value of `application/scim+json` or `application/json`.

* `Content-Type`

  If you provide a request body (as with `POST`, `PUT`, and `PATCH` requests), also include this header with the value `application/scim+json` or `application/json`.

## Updating resources

SCIM resources are modified using the `PUT` and `PATCH` methods, described in sections 3.5.1 and 3.5.2 of [RFC 7644](https://datatracker.ietf.org/doc/html/rfc7644). For examples, refer to [User profile endpoints](user-profile-endpoints.html).

| HTTP method | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `PUT`       | Updates a resource by completely replacing it.               |
| `PATCH`     | Updates a resource by modifying only the changes to be made. |

Because access controls enforced by the PingDirectory server policies and scopes can limit your view of a resource, the server must assume that you may not have access to all attributes of a resource. This is important for `PUT` requests, because the server needs to distinguish between a case in which you explicitly wish to remove an attribute and a case in which you do not know about an attribute. The general rule is that the server ignores an attribute that is omitted from a `PUT` request, rather than deleting it. If you explicitly wish to delete an attribute, then you should set its value to `null`.

When you request a modification, the server computes the difference between the current state of the resource and the state specified by the modification request, applying a minimal set of changes when passing the modification request to the user store. In effect, this means that a `PUT` request is ultimately treated as if it were a `PATCH` request. This prevents unnecessary modifications from being sent to the user store and, more importantly, also prevents you from inadvertently removing attributes that you did not specify because you did not have access to them.

The server performs this diffing logic at the attribute and sub-attribute level, comparing each attribute in a modification request against the corresponding attribute in the current resource. For multivalued, complex attributes, the server iterates through the values in the modification request and tries to find the corresponding value in the current resource to determine a match. If it is found, it then diffs at the sub-attribute level.

This behavior is summarized by the following table.

| Operation                                                                                                                | Result                                  |
| ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| `PUT` request omitting a simple single-valued attribute (such as userName).                                              | No change.                              |
| `PUT` or `PATCH` request setting a simple single-valued attribute to null.                                               | The attribute is deleted.               |
| `PUT` or `PATCH` request replacing the value of a multi-valued attribute, omitting an existing member of the array.      | The omitted member is deleted.          |
| `PUT` or `PATCH` request replacing the value of a complex attribute, omitting an existing sub-attribute from the object. | No change to the omitted sub-attribute. |

For example, if the current value of a resource's `phoneNumbers` attribute is:

```json
"phoneNumbers": [
   {
      "value": "054-757-2291",
      "type": "work",
      "primary":"true"
   }
]
```

And a modification request includes:

```json
"phoneNumbers": [
   {
      "value": "054-757-2291",
      "primary": "false"
   }
]
```

Then the final result is:

```json
"phoneNumbers": [
   {
      "value": "054-757-2291",
      "type": "work",
      "primary": "false"
   }
]
```

When finding a matching value in a complex attribute, matches of the `value`, `$ref`, `type`, and `display` sub-attribute values are given more weight when compared to values of other sub-attributes. This is done because the above sub-attribute values are typically unique for any given complex attribute.

## Specifying attributes to return

By default, all attributes that you are authorized to read are returned when a resource is requested. Your application can provide special query parameters to override this behavior.

| Parameter          | Description                                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| attributes         | Indicates the set of attributes to include in the response. Takes a comma-separated list of attribute names. Extension schema attribute names must be prefixed with the extension schema URN. |
| excludedAttributes | Indicates a set of attributes to exclude from the response. Takes a comma-separated list of attribute names. Extension schema attribute names must be prefixed with the extension schema URN. |

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | The `attributes` and `excludedAttributes` parameters are mutually exclusive and should not be specified in the same request. |

## Filtering searches

Some endpoints support an optional `filter` parameter for filtering responses containing multiple resources. In general, if a SCIM path returns a single resource, it does not support filtering. If it returns multiple resources, then it generally supports filtering. For example, `/scim/v2/Users` supports filtering, but `+/scim/v2/Users/{userid}` does not.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | SCIM filters do not filter for attributes. They filter for resources. |

SCIM filtering is described in detail by [RFC 7644](https://tools.ietf.org/html/rfc7644), section 3.4.2.2. The following discussion should not be considered exhaustive.

The value of the filter parameter is a search filter, which typically takes the form `<attribute> <operator> <value>`. For example:

```none
filter=userName eq "pkd"
```

Search responses are always list responses, except in the case of an error.

The following attribute operators are supported:

| Operator | Description              |
| -------- | ------------------------ |
| eq       | equal                    |
| ne       | not equal                |
| co       | contains                 |
| sw       | starts with              |
| ew       | ends with                |
| pr       | present                  |
| gt       | greater than             |
| ge       | greater than or equal to |
| lt       | less than                |
| le       | less than or equal to    |

The following logical operators are supported:

| Operator |
| -------- |
| and      |
| or       |
| not      |

The following grouping operators are supported:

| Operator | Description                                                                                |
| -------- | ------------------------------------------------------------------------------------------ |
| ()       | Groups expressions to alter precedence.                                                    |
| \[]      | Contains a filter expression to be applied to a complex attribute. Refer to example below. |

The following is a sample of filtering by a core attribute:

```none
filter=userName eq "pkd"
```

The following is a sample of filtering by an extended attribute using the 'starts with' operator:

```none
filter=urn:pingidentity:schemas:sample:profile:1.0:birthDate sw "1939"
```

The following is a sample of a complex filter:

```none
filter=emails[value eq "glen@runciter.com"]
```

The following is a sample of a complex filter with two expressions:

```none
filter=emails[value eq "glen@runciter.com" and type eq "work"]
```

## Pagination

The client can provide pagination parameters to page through search result sets.

| Parameter  | Description                                                                                                                                                                                                                            |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| startIndex | The index of the first query result. Indexing starts at 1.                                                                                                                                                                             |
| count      | A non-negative integer specifying the maximum number of matching resources to return per page. If 0 is specified, then no resources will be returned, but the totalResults field will still indicate the number of matching resources. |

---

---
title: Search User Profile (GET)
description: The GET /scim/v2/Users endpoint filters for matching user resources by performing a GET and providing a filter query parameter. Pagination parameters can also be provided.A client can filter for matching resources by performing a GET and providing a filter query parameter, as described above. Pagination parameters can also be provided.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:user-profile-endpoints/get-read-search-users
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/user-profile-endpoints/get-read-search-users.html
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Search User Profile (GET)

##

```none
GET {{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22
```

The `GET /scim/v2/Users` endpoint filters for matching user resources by performing a `GET` and providing a filter query parameter. Pagination parameters can also be provided.A client can filter for matching resources by performing a `GET` and providing a filter query parameter, as described above. Pagination parameters can also be provided.

The response is formatted as a list response containing zero or more matching resources in the `Resources` field. If the request is valid, the response returns a `200` status code, even if no matching resources are found.

|   |                                                                       |
| - | --------------------------------------------------------------------- |
|   | The server does not support searching across multiple resource types. |

The sample performs a search for resources under the `/Users` endpoint using specific values for `name.givenName` and `name.familyName`.

The User resource and its attributes are defined in [RFC 7643, Section 4.1](https://tools.ietf.org/html/rfc7643#section-4.1).

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/scim+json

Accept      application/scim+json

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
curl --location --globoff '{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22' \
--header 'Accept: application/scim+json' \
--header 'Content-Type: application/scim+json' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Accept", "application/scim+json");
request.AddHeader("Content-Type", "application/scim+json");
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

  url := "{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Accept", "application/scim+json")
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
GET /scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22 HTTP/1.1
Host: {{apiPath}}
Accept: application/scim+json
Content-Type: application/scim+json
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/scim+json");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22")
  .method("GET", body)
  .addHeader("Accept", "application/scim+json")
  .addHeader("Content-Type", "application/scim+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Accept": "application/scim+json",
    "Content-Type": "application/scim+json",
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
  'url': '{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22',
  'headers': {
    'Accept': 'application/scim+json',
    'Content-Type': 'application/scim+json',
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

url = "{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22"

payload = {}
headers = {
  'Accept': 'application/scim+json',
  'Content-Type': 'application/scim+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Accept' => 'application/scim+json',
  'Content-Type' => 'application/scim+json',
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

url = URI("{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Accept"] = "application/scim+json"
request["Content-Type"] = "application/scim+json"
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/Users?filter=name.givenName%20eq%20%22Pat%22%20and%20name.familyName%20eq%20%22Conley%22")!,timeoutInterval: Double.infinity)
request.addValue("application/scim+json", forHTTPHeaderField: "Accept")
request.addValue("application/scim+json", forHTTPHeaderField: "Content-Type")
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
    "Resources": [
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
                "created": "2016-07-30T00:28:07.507Z",
                "lastModified": "2016-07-30T00:28:07.507Z",
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
    ],
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "totalResults": 1
}
```

---

---
title: Search User Profile (POST)
description: The POST /scim/v2/Users/.search endpoint filters for matching user resources by performing a POST against the special .search endpoint and providing a filter value. Pagination directives can also be provided.
component: pingdirectory
page_id: pingdirectory:directory-proxy-scim:user-profile-endpoints/post-read-search-users
canonical_url: https://developer.pingidentity.com/pingdirectory/directory-proxy-scim/user-profile-endpoints/post-read-search-users.html
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Search User Profile (POST)

##

```none
POST {{apiPath}}/scim/v2/Users/.search
```

The `POST /scim/v2/Users/.search` endpoint filters for matching user resources by performing a `POST` against the special `.search` endpoint and providing a filter value. Pagination directives can also be provided.

The response is formatted as a list response containing zero or more matching user resources in the `Resources` field. If the request is valid, the response returns a `200` status code, even if no matching resources are found.

The User resource and its attributes are defined in [RFC 7643, Section 4.1](https://tools.ietf.org/html/rfc7643#section-4.1).

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/scim+json

Accept      application/scim+json

### Body

raw ( application/scim+json )

```json
{
    "filter": "userName sw \"pc\""
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
curl --location --globoff '{{apiPath}}/scim/v2/Users/.search' \
--header 'Accept: application/scim+json' \
--header 'Content-Type: application/scim+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "filter": "userName sw \"pc\""
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/scim/v2/Users/.search")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Accept", "application/scim+json");
request.AddHeader("Content-Type", "application/scim+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""filter"": ""userName sw \""pc\""""" + "\n" +
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

  url := "{{apiPath}}/scim/v2/Users/.search"
  method := "POST"

  payload := strings.NewReader(`{
    "filter": "userName sw \"pc\""
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Accept", "application/scim+json")
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
POST /scim/v2/Users/.search HTTP/1.1
Host: {{apiPath}}
Accept: application/scim+json
Content-Type: application/scim+json
Authorization: Bearer {{accessToken}}

{
    "filter": "userName sw \"pc\""
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/scim+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"filter\": \"userName sw \\\"pc\\\"\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/scim/v2/Users/.search")
  .method("POST", body)
  .addHeader("Accept", "application/scim+json")
  .addHeader("Content-Type", "application/scim+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/scim/v2/Users/.search",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Accept": "application/scim+json",
    "Content-Type": "application/scim+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "filter": "userName sw \"pc\""
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
  'url': '{{apiPath}}/scim/v2/Users/.search',
  'headers': {
    'Accept': 'application/scim+json',
    'Content-Type': 'application/scim+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "filter": "userName sw \"pc\""
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

url = "{{apiPath}}/scim/v2/Users/.search"

payload = json.dumps({
  "filter": "userName sw \"pc\""
})
headers = {
  'Accept': 'application/scim+json',
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
$request->setUrl('{{apiPath}}/scim/v2/Users/.search');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Accept' => 'application/scim+json',
  'Content-Type' => 'application/scim+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "filter": "userName sw \\"pc\\""\n}');
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

url = URI("{{apiPath}}/scim/v2/Users/.search")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Accept"] = "application/scim+json"
request["Content-Type"] = "application/scim+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "filter": "userName sw \"pc\""
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"filter\": \"userName sw \\\"pc\\\"\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/scim/v2/Users/.search")!,timeoutInterval: Double.infinity)
request.addValue("application/scim+json", forHTTPHeaderField: "Accept")
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

200 OK

```json
{
    "Resources": [
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
    ],
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "totalResults": 1
}
```
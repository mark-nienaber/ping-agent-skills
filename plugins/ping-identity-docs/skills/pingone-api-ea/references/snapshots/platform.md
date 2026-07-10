---
title: Configuration Management
description: The Configuration Management service gives you a secure and flexible approach to automating (promoting) configurations across multiple environments, enabling the seamless creation, updating, and deletion of resources while supporting dynamic configurations through variable management. Resource dependencies are maintained, ensuring smooth cross-environment transitions and promotions. Auditing and reporting enhance oversight and compliance.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  special-handling: Resources requiring special handling
  secrets-and-passwords: Secrets and passwords
  certificates: Certificates
  user-attributes: User attributes
  ldap-gateway: LDAP Gateway
  notification-settings: Notification settings
  davinci-resources: DaVinci resources
  davinci-flows: DaVinci flows
  davinci-flow-policies: DaVinci flow policies
  davinci-applications: DaVinci applications
  deleted-configuration-resources: Deleted configuration resources
  if-you-want-to-use-postman: If you want to use Postman
---

# Configuration Management

The Configuration Management service gives you a secure and flexible approach to automating (promoting) configurations across multiple environments, enabling the seamless creation, updating, and deletion of resources while supporting dynamic configurations through variable management. Resource dependencies are maintained, ensuring smooth cross-environment transitions and promotions. Auditing and reporting enhance oversight and compliance.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | Currently, you can promote configurations only to environments within the same PingOne tenant. |

To use the Configuration Management service you need to have the Environment Admin role for at least two environments. The general workflow is:

* Select configurations that you want to promote from one environment to another (generally, through development, testing, and production stages).

* If desired, use promotion variables to dynamically substitute different property values for a configuration resource included in a promotion operation.

* Use the promotion plan returned by the [Read One Promotion](configuration-management/promotions/get-one-promotion.html) or [Read All Promotions](configuration-management/promotions/get-all-promotions.html) to move the configuration from the source environment to the target environment.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only resources used for PingOne configurations are contained in a snapshot (such as applications, policies, and flows). Other PingOne resources not used for configuration purposes, are not tracked by the Configuration Management service. Such resources are excluded from promotions, and include:* Users and user profiles

* Admin role assignments

* Environment properties

* Externally provisioned groups

* Audit logs |

The Configuration Management service is comprised of these sub-services:

* [Snapshots](configuration-management/snapshots.html)

* [Promotions](configuration-management/promotions.html)

* [Promotion Variables](configuration-management/promotion-variables.html)

* [Promotion Configuration](configuration-management/promotion-configuration.html)

## Resources requiring special handling

Some resources can't be promoted. Excluded resources generally fall into the following categories:

* User and operational data: Resources that contain user-specific or operational data, such as audit logs, user profiles, or device and session data, are excluded from promotion to prevent data integrity issues.

* Environment-specific secrets and keys: These resources are inherently tied to a specific environment for security reasons and can't be promoted or used by another environment.

* Roles and permissions: While you can promote resources that require permissions or roles, the administrative access to them isn't promoted. This includes administrator role assignment and application role assignments. After the resource is promoted, you must manually assign the appropriate roles and permissions to the resource in the target environment.

You'll find a complete list of excluded resources in [Excluded Resources](configuration-management/promotions/excluded-resources.html).

### Secrets and passwords

Many configuration resources in PingOne use secrets or passwords to connect third-party services such as an external identity provider or a PingOne DaVinci connector. When you select to promote a resource that includes attributes for secrets or passwords, PingOne requires you to create sensitive variables for promotion, which are stored securely and encrypted anywhere they appear.

### Certificates

Certificates can't be promoted directly, and certificate references in other resources require special handling:

* Default certificates: If a resource in the source environment references a default certificate, the promotion service automatically maps that reference to the default certificate in the target environment during the promotion.

* Certificates as variables: For non-default certificates, you must create promotion variables to store the certificate IDs for both the source and target environments. During the promotion, the service substitutes the variable value for the certificate ID in the target environment.

The following example illustrates this process:

1. Create verification certificates in both the source and target environments.

2. Create a SAML application in the source environment that uses the verification certificate for that environment.

3. Create a promotion variable for the certificate ID attribute of the SAML application, setting the source environment value to the certificate ID in the source environment and the target environment value to the certificate ID in the target environment.

4. Promote the SAML application from the source environment to the target environment.

The SAML application in the source environment uses the certificate ID defined in the variable for that environment. The SAML application promoted to the target environment uses the certificate ID defined in the variable for the target environment.

### User attributes

Individual user attributes are supported for promotion. However, when you promote an application or FIDO policy that references custom user attributes, all schema attributes are added to the promotion plan. You can manually exclude them before you run the promotion.

### LDAP Gateway

Gateway credentials can't be promoted or managed using promotion variables. These credentials must be created in each environment after the gateway is promoted.

### Notification settings

Email notification settings can be promoted, but if you're using the allow list capability, you must configure the allow list in each environment. The allow list itself can't be promoted directly.

### DaVinci resources

The promotion service fully supports the promotion of PingOne DaVinci resources, including flows, subflows, flow policies, connectors, and DaVinci applications. However, there are several differences in how certain types of DaVinci resources are processed during promotion.

As with other types of configuration resources, you can map DaVinci dependencies to existing resources if they exist in the target environment, or create them as new resources if they don't, but dependency behavior varies depending on the resource you select for direct promotion.

#### DaVinci flows

When you promote a DaVinci flow, the promotion service identifies all of the dependent configurations used in the flow if they're referenced correctly. Only the most recent deployed version of the flow is promoted to the target environment. For example, if your flow has four versions, and version 3 is the most recent deployed version, only version 3 is promoted. Similarly, if the flow includes subflows, only the subflow versions referenced by the flow are promoted.

#### DaVinci flow policies

When you promote a DaVinci flow policy, the promotion service identifies the flows referenced by the policy and the specific versions of the flows referenced. All flow versions used in the policy are promoted as dependencies of the policy.

For example, if you are promoting a flow policy that references two flows, and the policy uses version 2 of flow A and versions 1 and 3 of flow B, version 2 of flow A and versions 1 and 3 of flow B are promoted as dependencies of the flow policy.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | DaVinci flow policies are always linked to a DaVinci application. If you promote a flow policy directly, the associated DaVinci application is promoted as a dependency of the flow policy. This application won't be listed in the PingOne admin console **Auto-Selected Dependencies** page when you configure the promotion, but it will be listed when you confirm the promotion configuration.If the application has additional flow policies associated with it, those policies aren't promoted as dependencies of the application.To promote all flow policies associated with a DaVinci application, promote the application directly instead of promoting the flow policies individually. |

#### DaVinci applications

When you promote a DaVinci application, the promotion service identifies all associated flow policies and promotes them as dependencies of the application. The specific versions of the flow policies referenced by the application are promoted.

### Deleted configuration resources

When you delete a configuration resource from the source environment after it has been promoted to the target environment, that resource remains in the target environment until you explicitly delete it there. You can use the promotion service to handle the deletion. A deletion promotion works similarly to a standard promotion, but instead of creating or updating the resource in the target environment, the promotion service deletes it.

## If you want to use Postman

You can download or fork the Postman collection for the early access Configuration Management APIs, and test them in your Postman environment. If you don't already have a Postman installation, you can install the free version. Refer to [Download Postman](https://www.postman.com/downloads/).

Import or fork the Postman collection `PingOne Configuration Management APIs - Early Access` into your Postman installation by clicking the **Run in Postman** button below:

[Run in Postman](https://god.gw.postman.com/run-collection/5375867-3dcb7dec-86a1-4ba9-a429-f33fe07b6583?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D5375867-3dcb7dec-86a1-4ba9-a429-f33fe07b6583%26entityType%3Dcollection%26workspaceId%3D936f1637-06aa-461a-b23d-0964e90621c6)

Refer to [Postman and the PingOne APIs](https://developer.pingidentity.com/pingone-api/platform/working-with-pingone-apis/postman-and-pingone.html) for more information.

---

---
title: Create Custom Push Provider
description: This example uses the pushDeliverySettings endpoint to create a custom sender for push notifications.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/push-delivery-settings/create_custom_push_provider
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/push-delivery-settings/create_custom_push_provider.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Custom Push Provider

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings
```

This example uses the `pushDeliverySettings` endpoint to create a custom sender for push notifications.

This allows you to use a gateway of your own to send the push data to push notification services such as APNs and FCM, rather than having PingOne communicate directly with the push notification services.

If you define such a gateway, you just have to provide PingOne with the authentication credentials for your gateway rather than having to provide your credentials for the push notification service.

As can be seen in the `authentication` object, OAuth2 is used for authentication with the gateway.

The variable `${push-data}` represents the relevant data provided by PingOne so that you can make the appropriate API calls to the push notification service to send the push notifications to your users.

> **Collapse: Request Model**
>
> | Property                      | Type   | Required? |
> | ----------------------------- | ------ | --------- |
> | `authentication.authUrl`      | String | Required  |
> | `authentication.clientId`     | String | Required  |
> | `authentication.clientSecret` | String | Required  |
> | `authentication.method`       | String | Required  |
> | `authentication.scopes`       | Array  | Optional  |
> | `name`                        | String | Required  |
> | `provider`                    | String | Required  |
> | `requests.body`               | String | Required  |
> | `requests.deliveryMethod`     | String | Required  |
> | `requests.headers`            | Array  | Optional  |
> | `requests.method`             | String | Required  |
> | `requests.url`                | String | Required  |
>
> Refer to the [Push delivery data model](../push-delivery-settings.html#push-delivery-data-model) for full property descriptions.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
	"name":"Custom push provider - created with API",
	"authentication": {
        "authUrl": "https://login.example.com/oauth/token",
        "clientId": "idForAccount",
        "clientSecret": "{{customProviderClientSecret}}",
        "scopes":["push:send"],
        "method": "OAUTH2"
    },
	"requests":[
	    {
            "body":"data=${push-data}",
		    "method":"POST",
		    "deliveryMethod":"PUSH",
		    "url":"https://www.example.com",
		    "headers": {
                "content-type":"application/json"
            }
		}
	],
	"provider":"CUSTOM_PROVIDER"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
	"name":"Custom push provider - created with API",
	"authentication": {
        "authUrl": "https://login.example.com/oauth/token",
        "clientId": "idForAccount",
        "clientSecret": "{{customProviderClientSecret}}",
        "scopes":["push:send"],
        "method": "OAUTH2"
    },
	"requests":[
	    {
            "body":"data=${push-data}",
		    "method":"POST",
		    "deliveryMethod":"PUSH",
		    "url":"https://www.example.com",
		    "headers": {
                "content-type":"application/json"
            }
		}
	],
	"provider":"CUSTOM_PROVIDER"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"	""name"":""Custom push provider - created with API""," + "\n" +
@"	""authentication"": {" + "\n" +
@"        ""authUrl"": ""https://login.example.com/oauth/token""," + "\n" +
@"        ""clientId"": ""idForAccount""," + "\n" +
@"        ""clientSecret"": ""{{customProviderClientSecret}}""," + "\n" +
@"        ""scopes"":[""push:send""]," + "\n" +
@"        ""method"": ""OAUTH2""" + "\n" +
@"    }," + "\n" +
@"	""requests"":[" + "\n" +
@"	    {" + "\n" +
@"            ""body"":""data=${push-data}""," + "\n" +
@"		    ""method"":""POST""," + "\n" +
@"		    ""deliveryMethod"":""PUSH""," + "\n" +
@"		    ""url"":""https://www.example.com""," + "\n" +
@"		    ""headers"": {" + "\n" +
@"                ""content-type"":""application/json""" + "\n" +
@"            }" + "\n" +
@"		}" + "\n" +
@"	]," + "\n" +
@"	""provider"":""CUSTOM_PROVIDER""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings"
  method := "POST"

  payload := strings.NewReader(`{
	"name":"Custom push provider - created with API",
	"authentication": {
        "authUrl": "https://login.example.com/oauth/token",
        "clientId": "idForAccount",
        "clientSecret": "{{customProviderClientSecret}}",
        "scopes":["push:send"],
        "method": "OAUTH2"
    },
	"requests":[
	    {
            "body":"data=${push-data}",
		    "method":"POST",
		    "deliveryMethod":"PUSH",
		    "url":"https://www.example.com",
		    "headers": {
                "content-type":"application/json"
            }
		}
	],
	"provider":"CUSTOM_PROVIDER"
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
POST /v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
	"name":"Custom push provider - created with API",
	"authentication": {
        "authUrl": "https://login.example.com/oauth/token",
        "clientId": "idForAccount",
        "clientSecret": "{{customProviderClientSecret}}",
        "scopes":["push:send"],
        "method": "OAUTH2"
    },
	"requests":[
	    {
            "body":"data=${push-data}",
		    "method":"POST",
		    "deliveryMethod":"PUSH",
		    "url":"https://www.example.com",
		    "headers": {
                "content-type":"application/json"
            }
		}
	],
	"provider":"CUSTOM_PROVIDER"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n\t\"name\":\"Custom push provider - created with API\",\n\t\"authentication\": {\n        \"authUrl\": \"https://login.example.com/oauth/token\",\n        \"clientId\": \"idForAccount\",\n        \"clientSecret\": \"{{customProviderClientSecret}}\",\n        \"scopes\":[\"push:send\"],\n        \"method\": \"OAUTH2\"\n    },\n\t\"requests\":[\n\t    {\n            \"body\":\"data=${push-data}\",\n\t\t    \"method\":\"POST\",\n\t\t    \"deliveryMethod\":\"PUSH\",\n\t\t    \"url\":\"https://www.example.com\",\n\t\t    \"headers\": {\n                \"content-type\":\"application/json\"\n            }\n\t\t}\n\t],\n\t\"provider\":\"CUSTOM_PROVIDER\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Custom push provider - created with API",
    "authentication": {
      "authUrl": "https://login.example.com/oauth/token",
      "clientId": "idForAccount",
      "clientSecret": "{{customProviderClientSecret}}",
      "scopes": [
        "push:send"
      ],
      "method": "OAUTH2"
    },
    "requests": [
      {
        "body": "data=${push-data}",
        "method": "POST",
        "deliveryMethod": "PUSH",
        "url": "https://www.example.com",
        "headers": {
          "content-type": "application/json"
        }
      }
    ],
    "provider": "CUSTOM_PROVIDER"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Custom push provider - created with API",
    "authentication": {
      "authUrl": "https://login.example.com/oauth/token",
      "clientId": "idForAccount",
      "clientSecret": "{{customProviderClientSecret}}",
      "scopes": [
        "push:send"
      ],
      "method": "OAUTH2"
    },
    "requests": [
      {
        "body": "data=${push-data}",
        "method": "POST",
        "deliveryMethod": "PUSH",
        "url": "https://www.example.com",
        "headers": {
          "content-type": "application/json"
        }
      }
    ],
    "provider": "CUSTOM_PROVIDER"
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

url = "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings"

payload = json.dumps({
  "name": "Custom push provider - created with API",
  "authentication": {
    "authUrl": "https://login.example.com/oauth/token",
    "clientId": "idForAccount",
    "clientSecret": "{{customProviderClientSecret}}",
    "scopes": [
      "push:send"
    ],
    "method": "OAUTH2"
  },
  "requests": [
    {
      "body": "data=${push-data}",
      "method": "POST",
      "deliveryMethod": "PUSH",
      "url": "https://www.example.com",
      "headers": {
        "content-type": "application/json"
      }
    }
  ],
  "provider": "CUSTOM_PROVIDER"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n	"name":"Custom push provider - created with API",\n	"authentication": {\n        "authUrl": "https://login.example.com/oauth/token",\n        "clientId": "idForAccount",\n        "clientSecret": "{{customProviderClientSecret}}",\n        "scopes":["push:send"],\n        "method": "OAUTH2"\n    },\n	"requests":[\n	    {\n            "body":"data=${push-data}",\n		    "method":"POST",\n		    "deliveryMethod":"PUSH",\n		    "url":"https://www.example.com",\n		    "headers": {\n                "content-type":"application/json"\n            }\n		}\n	],\n	"provider":"CUSTOM_PROVIDER"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Custom push provider - created with API",
  "authentication": {
    "authUrl": "https://login.example.com/oauth/token",
    "clientId": "idForAccount",
    "clientSecret": "{{customProviderClientSecret}}",
    "scopes": [
      "push:send"
    ],
    "method": "OAUTH2"
  },
  "requests": [
    {
      "body": "data=\${push-data}",
      "method": "POST",
      "deliveryMethod": "PUSH",
      "url": "https://www.example.com",
      "headers": {
        "content-type": "application/json"
      }
    }
  ],
  "provider": "CUSTOM_PROVIDER"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n\t\"name\":\"Custom push provider - created with API\",\n\t\"authentication\": {\n        \"authUrl\": \"https://login.example.com/oauth/token\",\n        \"clientId\": \"idForAccount\",\n        \"clientSecret\": \"{{customProviderClientSecret}}\",\n        \"scopes\":[\"push:send\"],\n        \"method\": \"OAUTH2\"\n    },\n\t\"requests\":[\n\t    {\n            \"body\":\"data=${push-data}\",\n\t\t    \"method\":\"POST\",\n\t\t    \"deliveryMethod\":\"PUSH\",\n\t\t    \"url\":\"https://www.example.com\",\n\t\t    \"headers\": {\n                \"content-type\":\"application/json\"\n            }\n\t\t}\n\t],\n\t\"provider\":\"CUSTOM_PROVIDER\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/notificationsSettings/pushDeliverySettings/4d64a2b8-80cf-4295-97ae-ad33ab08db6b"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "4d64a2b8-80cf-4295-97ae-ad33ab08db6b",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Custom push provider - created with API",
    "provider": "CUSTOM_PROVIDER",
    "authentication": {
        "grantType": "CLIENT_CREDENTIALS",
        "authUrl": "https://login.example.com/oauth/token",
        "clientId": "idForAccount",
        "scopes": [
            "push:send"
        ],
        "method": "OAUTH2"
    },
    "requests": [
        {
            "deliveryMethod": "PUSH",
            "url": "https://www.example.com",
            "method": "POST",
            "body": "${push-data}",
            "headers": {
                "content-type": "application/json"
            }
        }
    ],
    "createdAt": "2026-06-23T15:42:12.555Z",
    "updatedAt": "2026-06-23T15:42:12.555Z"
}
```

---

---
title: Create Promotion
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotions/create-promotion
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotions/create-promotion.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Promotion

##

 

```none
POST {{apiPath}}/v1/environments/{{envID}}/promotions
```

Use POST `{{apiPath}}/v1/environments/{{envID}}/promotions` to create a promotion for the specified configuration resource or resources in the source and target environments. You need to have the Environment Admin role for both the source and target environments.

When you create a promotion, you've the option to specify a snapshot of the configuration resource or resources for the source or target environments, or allow the Configuration Management service to automatically generate snapshots for both. You've also the option to specify a mapping between the source and target configuration resource or resources. If you don't specify a mapping, the source and target environment snapshots are compared, and a mapping between the source and target configuration resources is automatically calculated. After the comparison, the promotion is stored with the mapping, and a promotion plan is automatically generated. Use the [Read One Promotion](get-one-promotion.html) or [Read All Promotions](get-all-promotions.html) to view the promotion plan.

> **Collapse: Request Model**
>
> For complete property descriptions, refer to [Promotions](../promotions.html).
>
> | Property            | Type        | Required |
> | ------------------- | ----------- | -------- |
> | `description`       | String      | Optional |
> | `excludedResources` | Object\[]\* | Optional |
> | `resourceMapping`   | Map         | Optional |
> | `selectedResources` | Object\[]\* | Optional |
> | `targetEnvironment` | Object      | Required |
> | `sourceSnapshot`    | Object      | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "targetEnvironment": {
        "id": "{{targetEnvID}}"
    },
    "sourceSnapshot": {
        "id": "{{sourceSnapshotId}}"
    },
    "selectedResources": [
        "09facb42-b428-4590-aaba-1f4278f4ed63"
    ],
    "excludedResources": [
        "363ef235-f6fe-4bc7-ae3d-63217482f57f"

    ],
    "resourceMapping": {"{{sourcePopulationsResource}}":"{{targetPopulationsResource}}"},
    "description": "Test promotion"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/promotions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "targetEnvironment": {
        "id": "{{targetEnvID}}"
    },
    "sourceSnapshot": {
        "id": "{{sourceSnapshotId}}"
    },
    "selectedResources": [
        "09facb42-b428-4590-aaba-1f4278f4ed63"
    ],
    "excludedResources": [
        "363ef235-f6fe-4bc7-ae3d-63217482f57f"

    ],
    "resourceMapping": {"{{sourcePopulationsResource}}":"{{targetPopulationsResource}}"},
    "description": "Test promotion"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/promotions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""targetEnvironment"": {" + "\n" +
@"        ""id"": ""{{targetEnvID}}""" + "\n" +
@"    }," + "\n" +
@"    ""sourceSnapshot"": {" + "\n" +
@"        ""id"": ""{{sourceSnapshotId}}""" + "\n" +
@"    }," + "\n" +
@"    ""selectedResources"": [" + "\n" +
@"        ""09facb42-b428-4590-aaba-1f4278f4ed63""" + "\n" +
@"    ]," + "\n" +
@"    ""excludedResources"": [" + "\n" +
@"        ""363ef235-f6fe-4bc7-ae3d-63217482f57f""" + "\n" +
@"" + "\n" +
@"    ]," + "\n" +
@"    ""resourceMapping"": {""{{sourcePopulationsResource}}"":""{{targetPopulationsResource}}""}," + "\n" +
@"    ""description"": ""Test promotion""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/promotions"
  method := "POST"

  payload := strings.NewReader(`{
    "targetEnvironment": {
        "id": "{{targetEnvID}}"
    },
    "sourceSnapshot": {
        "id": "{{sourceSnapshotId}}"
    },
    "selectedResources": [
        "09facb42-b428-4590-aaba-1f4278f4ed63"
    ],
    "excludedResources": [
        "363ef235-f6fe-4bc7-ae3d-63217482f57f"

    ],
    "resourceMapping": {"{{sourcePopulationsResource}}":"{{targetPopulationsResource}}"},
    "description": "Test promotion"
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
POST /v1/environments/{{envID}}/promotions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "targetEnvironment": {
        "id": "{{targetEnvID}}"
    },
    "sourceSnapshot": {
        "id": "{{sourceSnapshotId}}"
    },
    "selectedResources": [
        "09facb42-b428-4590-aaba-1f4278f4ed63"
    ],
    "excludedResources": [
        "363ef235-f6fe-4bc7-ae3d-63217482f57f"

    ],
    "resourceMapping": {"{{sourcePopulationsResource}}":"{{targetPopulationsResource}}"},
    "description": "Test promotion"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"targetEnvironment\": {\n        \"id\": \"{{targetEnvID}}\"\n    },\n    \"sourceSnapshot\": {\n        \"id\": \"{{sourceSnapshotId}}\"\n    },\n    \"selectedResources\": [\n        \"09facb42-b428-4590-aaba-1f4278f4ed63\"\n    ],\n    \"excludedResources\": [\n        \"363ef235-f6fe-4bc7-ae3d-63217482f57f\"\n\n    ],\n    \"resourceMapping\": {\"{{sourcePopulationsResource}}\":\"{{targetPopulationsResource}}\"},\n    \"description\": \"Test promotion\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/promotions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/promotions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "targetEnvironment": {
      "id": "{{targetEnvID}}"
    },
    "sourceSnapshot": {
      "id": "{{sourceSnapshotId}}"
    },
    "selectedResources": [
      "09facb42-b428-4590-aaba-1f4278f4ed63"
    ],
    "excludedResources": [
      "363ef235-f6fe-4bc7-ae3d-63217482f57f"
    ],
    "resourceMapping": {
      "{{sourcePopulationsResource}}": "{{targetPopulationsResource}}"
    },
    "description": "Test promotion"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/promotions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "targetEnvironment": {
      "id": "{{targetEnvID}}"
    },
    "sourceSnapshot": {
      "id": "{{sourceSnapshotId}}"
    },
    "selectedResources": [
      "09facb42-b428-4590-aaba-1f4278f4ed63"
    ],
    "excludedResources": [
      "363ef235-f6fe-4bc7-ae3d-63217482f57f"
    ],
    "resourceMapping": {
      "{{sourcePopulationsResource}}": "{{targetPopulationsResource}}"
    },
    "description": "Test promotion"
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

url = "{{apiPath}}/v1/environments/{{envID}}/promotions"

payload = json.dumps({
  "targetEnvironment": {
    "id": "{{targetEnvID}}"
  },
  "sourceSnapshot": {
    "id": "{{sourceSnapshotId}}"
  },
  "selectedResources": [
    "09facb42-b428-4590-aaba-1f4278f4ed63"
  ],
  "excludedResources": [
    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
  ],
  "resourceMapping": {
    "{{sourcePopulationsResource}}": "{{targetPopulationsResource}}"
  },
  "description": "Test promotion"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/promotions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "targetEnvironment": {\n        "id": "{{targetEnvID}}"\n    },\n    "sourceSnapshot": {\n        "id": "{{sourceSnapshotId}}"\n    },\n    "selectedResources": [\n        "09facb42-b428-4590-aaba-1f4278f4ed63"\n    ],\n    "excludedResources": [\n        "363ef235-f6fe-4bc7-ae3d-63217482f57f"\n\n    ],\n    "resourceMapping": {"{{sourcePopulationsResource}}":"{{targetPopulationsResource}}"},\n    "description": "Test promotion"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/promotions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "targetEnvironment": {
    "id": "{{targetEnvID}}"
  },
  "sourceSnapshot": {
    "id": "{{sourceSnapshotId}}"
  },
  "selectedResources": [
    "09facb42-b428-4590-aaba-1f4278f4ed63"
  ],
  "excludedResources": [
    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
  ],
  "resourceMapping": {
    "{{sourcePopulationsResource}}": "{{targetPopulationsResource}}"
  },
  "description": "Test promotion"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"targetEnvironment\": {\n        \"id\": \"{{targetEnvID}}\"\n    },\n    \"sourceSnapshot\": {\n        \"id\": \"{{sourceSnapshotId}}\"\n    },\n    \"selectedResources\": [\n        \"09facb42-b428-4590-aaba-1f4278f4ed63\"\n    ],\n    \"excludedResources\": [\n        \"363ef235-f6fe-4bc7-ae3d-63217482f57f\"\n\n    ],\n    \"resourceMapping\": {\"{{sourcePopulationsResource}}\":\"{{targetPopulationsResource}}\"},\n    \"description\": \"Test promotion\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/promotions")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/a8fa2955-63ce-441e-87ed-57e9e92404e4"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "targetEnvironment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "sourceSnapshot": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/versions/17044f5a-8dc3-42d9-9db1-683df0965ff2"
        },
        "targetSnapshot": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/versions/657fe011-b198-4efa-bd15-14d6425509fb"
        },
        "promotionSteps": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/a8fa2955-63ce-441e-87ed-57e9e92404e4/promotionSteps"
        }
    },
    "id": "a8fa2955-63ce-441e-87ed-57e9e92404e4",
    "createdAt": "2026-05-25T17:55:39.850Z",
    "updatedAt": "2026-05-25T17:55:39.850Z",
    "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
    "sourceEnvironment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
    "targetEnvironment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "sourceSnapshotId": "17044f5a-8dc3-42d9-9db1-683df0965ff2",
    "sourceSnapshot": {
        "id": "17044f5a-8dc3-42d9-9db1-683df0965ff2"
    },
    "targetSnapshotId": "657fe011-b198-4efa-bd15-14d6425509fb",
    "targetSnapshot": {
        "id": "657fe011-b198-4efa-bd15-14d6425509fb"
    },
    "status": "NEW",
    "selectedResources": [
        "26a126c2-054f-4f18-b077-8226c0c4bf3e"
    ],
    "excludedResources": [
        "363ef235-f6fe-4bc7-ae3d-63217482f57f"
    ],
    "resourceMapping": {
        "2c3b1245-2c38-4174-97fa-069d88a543b1": "c7c92d16-e07b-4ddb-8d17-073fea3a219c"
    },
    "description": "Test promotion of population"
}
```

---

---
title: Create Snapshot
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/snapshots/create-snapshot
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/snapshots/create-snapshot.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
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
POST {{apiPath}}/v1/environments/{{envID}}/snapshots
```

Use POST `{{apiPath}}/v1/environments/{{envID}}/snapshots` to generate a snapshot of a configuration resource. The resource is identified by the `baseResourceURL` property in the request body.

The configuration resource, and optionally all of its dependencies (using the `expand=all` query parameter), are then stored by the Configuration Management service. Subsequent calls to the request POST `{{apiPath}}/v1/environments/{{envID}}/snapshots` for the same configuration resource generates a new version of the configuration resource each time the request is called, identified by a new snapshot ID.

> **Collapse: Query parameters**
>
> | Parameter | Description                                                                           |
> | --------- | ------------------------------------------------------------------------------------- |
> | `expand`  | When equal to `all`, shows all dependencies for the specified configuration resource. |
>
> Example: POST `{{apiPath}}/v1/environments/{{envID}}/snapshots?expand=all`

> **Collapse: Request Model**
>
> For property descriptions, refer to [Snapshot](../snapshots.html).
>
> | Property          | Type   | Required |
> | ----------------- | ------ | -------- |
> | `baseResourceURL` | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "baseResourceURL" : "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/snapshots' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "baseResourceURL" : "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/snapshots")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""baseResourceURL"" : ""https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/snapshots"
  method := "POST"

  payload := strings.NewReader(`{
    "baseResourceURL" : "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
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
POST /v1/environments/{{envID}}/snapshots HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "baseResourceURL" : "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"baseResourceURL\" : \"https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/snapshots")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/snapshots",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "baseResourceURL": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/snapshots',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "baseResourceURL": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
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

url = "{{apiPath}}/v1/environments/{{envID}}/snapshots"

payload = json.dumps({
  "baseResourceURL": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/snapshots');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "baseResourceURL" : "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/snapshots")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "baseResourceURL": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"baseResourceURL\" : \"https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/b6fcccdf-0bb2-42bc-b0aa-2431d158521a\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/snapshots")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/0b7795ac-c589-4311-82bd-b1a9caff7a6a/versions/ab00b05b-26d3-4de1-9c17-74a08adc238e"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "c47e8abf-e830-4bb4-9fe0-260895ce326e",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "snapshotId": "ab00b05b-26d3-4de1-9c17-74a08adc238e",
    "resource": {
        "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a"
    },
    "createdAt": "2024-09-09T14:43:55.346Z",
    "status": "WAITING",
    "resourceUrl": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a"
}
```

---

---
title: Create Variable Declaration
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotion-variables/create-variable-declaration
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-variables/create-variable-declaration.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Variable Declaration

##

 

```none
POST {{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations
```

Use the POST `{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations` request to declare (assign a value to) a promotion variable for use in the specified environment. You must first have defined the promotion variable using the [Create Variable Definition](create-variable-definition.html) request.

|   |                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When creating or updating promotion variable declarations, if the bound resource attribute is classified as sensitive (such as for client secrets or passwords), the associated variable definition in the target environment must also be marked as sensitive (the `isSensitive` attribute set to `true`). If it is not, the request fails with a validation error. |

> **Collapse: Request Model**
>
> | Property     | Type   | Required |
> | ------------ | ------ | -------- |
> | `resourceId` | String | Required |
> | `variables`  | Map    | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "resource": {"id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"},
    "variables": {"sloEndpoint": "${promotionVariable: sloEndpointVar}"}
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "resource": {"id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"},
    "variables": {"sloEndpoint": "${promotionVariable: sloEndpointVar}"}
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""resource"": {""id"": ""d8e643d9-105b-4f59-82f0-e549a34ee0c0""}," + "\n" +
@"    ""variables"": {""sloEndpoint"": ""${promotionVariable: sloEndpointVar}""}" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations"
  method := "POST"

  payload := strings.NewReader(`{
    "resource": {"id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"},
    "variables": {"sloEndpoint": "${promotionVariable: sloEndpointVar}"}
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
POST /v1/environments/{{envID}}/promotionVariableDeclarations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "resource": {"id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"},
    "variables": {"sloEndpoint": "${promotionVariable: sloEndpointVar}"}
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"resource\": {\"id\": \"d8e643d9-105b-4f59-82f0-e549a34ee0c0\"},\n    \"variables\": {\"sloEndpoint\": \"${promotionVariable: sloEndpointVar}\"}\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "resource": {
      "id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"
    },
    "variables": {
      "sloEndpoint": "${promotionVariable: sloEndpointVar}"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "resource": {
      "id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"
    },
    "variables": {
      "sloEndpoint": "${promotionVariable: sloEndpointVar}"
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

url = "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations"

payload = json.dumps({
  "resource": {
    "id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"
  },
  "variables": {
    "sloEndpoint": "${promotionVariable: sloEndpointVar}"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "resource": {"id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"},\n    "variables": {"sloEndpoint": "${promotionVariable: sloEndpointVar}"}\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "resource": {
    "id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"
  },
  "variables": {
    "sloEndpoint": "\${promotionVariable: sloEndpointVar}"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"resource\": {\"id\": \"d8e643d9-105b-4f59-82f0-e549a34ee0c0\"},\n    \"variables\": {\"sloEndpoint\": \"${promotionVariable: sloEndpointVar}\"}\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotionVariableDeclarations/d8e643d9-105b-4f59-82f0-e549a34ee0c0"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "resource": {
        "id": "d8e643d9-105b-4f59-82f0-e549a34ee0c0"
    },
    "variables": {
        "sloEndpoint": "${promotionVariable: sloEndpointVar}"
    },
    "createdAt": "2024-09-09T17:37:23.136Z",
    "updatedAt": "2024-09-09T17:37:23.136Z"
}
```

---

---
title: Create Variable Definition
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotion-variables/create-variable-definition
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-variables/create-variable-definition.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
  example-response-2: Example Response
---

# Create Variable Definition

##

 

```none
POST {{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions
```

Use the POST `{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions` request to define a promotion variable to be used in the specified environment. At this point, the promotion variable isn't associated with a configuration resource property. The next step is to use the [Create Variable Declaration](create-variable-declaration.html) request to associate the promotion variable you've defined with a configuration resource property.

> **Collapse: Request Model**
>
> Refer to [Promotion Variables](variable-definitions.html) for complete property descriptions.
>
> | Property      | Type    | Required |
> | ------------- | ------- | -------- |
> | `name`        | String  | Required |
> | `isSensitive` | Boolean | Optional |
> | `value`       | Object  | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "appSecret",
    "value": "mySecretSecret",
    "isSensitive": true
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "appSecret",
    "value": "mySecretSecret",
    "isSensitive": true
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""appSecret""," + "\n" +
@"    ""value"": ""mySecretSecret""," + "\n" +
@"    ""isSensitive"": true" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "appSecret",
    "value": "mySecretSecret",
    "isSensitive": true
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
POST /v1/environments/{{envID}}/promotionVariableDefinitions HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "appSecret",
    "value": "mySecretSecret",
    "isSensitive": true
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"appSecret\",\n    \"value\": \"mySecretSecret\",\n    \"isSensitive\": true\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "appSecret",
    "value": "mySecretSecret",
    "isSensitive": true
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "appSecret",
    "value": "mySecretSecret",
    "isSensitive": true
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

url = "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions"

payload = json.dumps({
  "name": "appSecret",
  "value": "mySecretSecret",
  "isSensitive": True
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "appSecret",\n    "value": "mySecretSecret",\n    "isSensitive": true\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "appSecret",
  "value": "mySecretSecret",
  "isSensitive": true
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"appSecret\",\n    \"value\": \"mySecretSecret\",\n    \"isSensitive\": true\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotionVariableDefinitions/sloEndpointVar"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "sloEndpointVar",
    "value": "http://example.com/slo",
    "createdAt": "2024-08-16T18:32:01.703Z",
    "updatedAt": "2024-08-16T18:32:01.703Z"
}
```

### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotionVariableDefinitions/appSecret"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "appSecret",
    "value": "******",
    "createdAt": "2026-04-10T13:56:41.147Z",
    "updatedAt": "2026-04-10T13:56:41.147Z",
    "variableType": "ENCRYPTED_STRING",
    "isSensitive": true
}
```

---

---
title: Delete Promotion
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotions/delete-promotion
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotions/delete-promotion.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
---

# Delete Promotion

##

 

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}
```

Use the DELETE `{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}` request to delete the specified promotion. A 204 response indicates a successful deletion.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}"
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
DELETE /v1/environments/{{envID}}/promotions/{{promotionID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/promotions/{{promotionID}}")!,timeoutInterval: Double.infinity)
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
title: Delete Variable Declaration
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotion-variables/delete-variable-declaration
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-variables/delete-variable-declaration.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
---

# Delete Variable Declaration

##

 

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa
```

Use the DELETE `{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/{{configResourceID}}` request to delete all promotion variables in the environment for the specified configuration resource. A 204 response indicates a successful deletion.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa"
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
DELETE /v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa',
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

url = "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDeclarations/e2450d85-1233-45fc-87eb-cd6903f624fa")!,timeoutInterval: Double.infinity)
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
title: Delete Variable Definition
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotion-variables/delete-variable-definition
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-variables/delete-variable-definition.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
---

# Delete Variable Definition

##

 

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}
```

Use the DELETE `{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}` request to delete the specified promotion variable definition. A 204 response indicates a successful deletion.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}"
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
DELETE /v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/promotionVariableDefinitions/{{definitionName}}")!,timeoutInterval: Double.infinity)
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
title: Early Access
description: These early access features are available for preview purposes only, and are not covered under standard Support SLAs. You can open support cases for feedback, bug reports, configuration questions, or other inquiries related to early access features, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so timelines might exceed the usual SLAs for your Support package.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Early Access

These early access features are available for preview purposes only, and are not covered under standard Support SLAs. You can open support cases for feedback, bug reports, configuration questions, or other inquiries related to early access features, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so timelines might exceed the usual SLAs for your Support package.

We encourage you to use any of the early access features you find applicable. You'll need to enable each feature you'd like to use.

---

---
title: Excluded Resources
description: Currently, not all resources, services, or products can be used in a promotion operation.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotions/excluded-resources
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotions/excluded-resources.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  excluded-products-or-services: Excluded products or services
  excluded-resources: Excluded resources
  permanently-excluded-resources: Permanently excluded resources
  currently-excluded-resources: Currently excluded resources
---

# Excluded Resources

Currently, not all resources, services, or products can be used in a promotion operation.

## Excluded products or services

* PingOne Neo (includes PingOne Verify and PingOne Credentials)

* PingOne Authorize

## Excluded resources

Some resources can never be promoted, while others will be supported for promotion, but currently are not.

### Permanently excluded resources

These resources are expected to never be supported for promotion:

* Active Identity Counts

* Activities

* Admin Config

* Applications Role Assignments

* Applications Secret

* Application Signons

* Application Signons Statistics

* Certificates (Refer to [Resources requiring special handling](../../configuration-management.html#special-handling).)

* Connectors (Refer to [Resources requiring special handling](../../configuration-management.html#special-handling).)

* Dashboards

* Data Exploration Batches

* Data Explorations

* Data Exploration Templates

* Migrate

* PingOne for Enterprise

* Promotions

* Promotion Variable Declarations

* Risk Evaluations

* Sessions

* Snapshots

* Software Licenses

* Total Identities

* Users

* Variables

### Currently excluded resources

These resources will be supported for promotion, but are not currently:

* API Servers

* Application Entitlements

* Application Permissions

* Application Resources

* Application Roles

* Authorization Attributes

* Authorization Changes

* Authorization Conditions

* Authorization Connector Templates

* Authorization Policies

* Authorization Processors

* Authorization Rules

* Authorization Services

* Authorization Statements

* Credential Counts

* Credential Issuer Profile

* Credential Types

* Custom Domains

* Decision Endpoints

* Digital Wallet Applications

* Fido Devices Metadata

* Identity Cloud

* Identity Cloud Orchestrations

* Images

* Integrations

* Metrics

* Notification Callback

* Notification Callback AWS email

* Notification Callback Syniverse

* Notification Callback Twilio

* Notification Callback Whatsapp

* Notifications

* Notifications Quota

* OAuth Jobs

* OAuth Tokens

* Organization Quota

* Password Storage Scheme Config

* Pingid

* Pingid Mobile App Versions

* Pingid Mobile Display Names

* Pingid Mobile Os Versions

* Portal

* Presentation Sessions

* Propagation

* Propagation Mappings

* Propagation Plans

* Propagation Provisioning Syncs

* Propagation Revisions ID

* Propagation Revisions ID Latest

* Propagation Rules

* Propagation Store Metadata

* Propagation Stores

* QS Dashboards

* Rate Limit IP Configs

* Resources Secret

* Risk Feedback

* Roles

* Seen Devices

* Solutions

* Subscriptions

* Tiles

* Translations

* Voice Phrases

---

---
title: Platform SSO APIs - Early Access
description: The PingOne early access APIs are available to you when you enable the early access features. When enabled, the features apply only to a specified environment. You select the features to enable, and can remove the feature from the specified environment at any time during the early access period.
component: pingone-api-ea
page_id: pingone-api-ea:platform:introduction
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/introduction.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Platform SSO APIs - Early Access

The PingOne early access APIs are available to you when you enable the early access features. When enabled, the features apply only to a specified environment. You select the features to enable, and can remove the feature from the specified environment at any time during the early access period.

---

---
title: Promotion Configuration
description: The promotionConfiguration endpoint sets and reads default target environment to be used for promotions. When you know that you'll be working with a specific target environment, you can set this environment as the default for the promotions you're doing.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotion-configuration
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-configuration.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  promotionConfig-model: Promotion Configuration data model
---

# Promotion Configuration

The `promotionConfiguration` endpoint sets and reads default target environment to be used for promotions. When you know that you'll be working with a specific target environment, you can set this environment as the default for the promotions you're doing.

## Promotion Configuration data model

| Property              | Type   | Required | Mutable | Description                               |
| --------------------- | ------ | -------- | ------- | ----------------------------------------- |
| `environmentId`       | String | Optional | Mutable | The identifier of the source environment. |
| `targetEnvironmentId` | String | Optional | Mutable | The identifier of the target environment. |

---

---
title: Promotion Mappings
description: The Promotion Mappings operations enable you to track the mappings used by the Promotions service from the source environment to one or more target environment. This is particularly important if you've allowed the Promotions service to automatically generate the mappings when you created the promotion. Refer to Create Promotion for more information.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotion-mappings
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-mappings.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  promotion-mappings-model: Promotion Mappings data model
---

# Promotion Mappings

The Promotion Mappings operations enable you to track the mappings used by the Promotions service from the source environment to one or more target environment. This is particularly important if you've allowed the Promotions service to automatically generate the mappings when you created the promotion. Refer to [Create Promotion](promotions/create-promotion.html) for more information.

## Promotion Mappings data model

| Property               | Type   | Required | Mutable   | Description                                                                                            |
| ---------------------- | ------ | -------- | --------- | ------------------------------------------------------------------------------------------------------ |
| `sourceEnvironment.id` | String | N/A      | Read-only | The identifier of the source environment.                                                              |
| `targetEnvironment.id` | String | N/A      | Read-only | The identifier of the target environment.                                                              |
| `resourceMappings`     | String | N/A      | Read-only | The mappings of source environment resource to target environment resource based on their identifiers. |

---

---
title: Promotion Variables
description: Use promotion variables to account for environment-specific differences, such as third-party integrations or URLs. You can specify configuration resource property values for either the source or target environment. The source environment property values will be substituted for the target environment property values by the promotion.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotion-variables
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotion-variables.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Promotion Variables

Use promotion variables to account for environment-specific differences, such as third-party integrations or URLs. You can specify configuration resource property values for either the source or target environment. The source environment property values will be substituted for the target environment property values by the promotion.

A promotion changes only the corresponding target environment property values with the promotion variables you set for the source environment. If you do not set any promotion variables, the configuration resource or resources that you specify for the source or target environment will be used as is, and cannot be changed during the promotion operation.

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Not all properties for configuration resources can be used as promotion variables. Refer to [Variable Resources](promotion-variables/variable-resources.html) for the listing of supported configuration resources and properties. |

To use promotion variables, you need to:

1. Specify the configuration resource to be promoted in a snapshot.

2. Define the variable or variables to be used for a source or target environment configuration resource property. Refer to [Variable Definitions](promotion-variables/variable-definitions.html).

3. Declare the variables to be used by the promotion operation. Refer to [Variable Declarations](promotion-variables/variable-declarations.html).

A few things to be aware of:

* The variables are scoped only to the specified configuration resources, and are not applied to any dependent resources.

* Variables are not versioned with a snapshot, so for each promotion operation, you need to ensure the variable settings for a configuration resource are correct.

* Any configuration resources that you change directly without updating the variables will be overwritten by a subsequent promotion operation. This is because the promotion operation will use the existing variable set.

---

---
title: Promotions
description: A promotion includes, at a minimum, source and target environment references, automatically generated source and target snapshots, the resource or resources to promote to the target environment, and a promotion plan for the promotion operation. You need to have the Environment Admin role for both the source and target environments. You can optionally include a specific source environment snapshot to use, as well as a mapping of the source environment configuration resource or resources to the target environment configuration resource or resources.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotions
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotions.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  promotions-model: Promotions data model
  rolling-back-a-promotion: Rolling back a promotion
  limitations-and-considerations: Limitations and considerations
---

# Promotions

A promotion includes, at a minimum, source and target environment references, automatically generated source and target snapshots, the resource or resources to promote to the target environment, and a promotion plan for the promotion operation. You need to have the Environment Admin role for both the source and target environments. You can optionally include a specific source environment snapshot to use, as well as a mapping of the source environment configuration resource or resources to the target environment configuration resource or resources.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | Currently, you can promote configurations only to environments within the same PingOne tenant. |

A PingOne admin having Environment Admin permissions can review the promotion plan, and update the promotion mapping and variable definitions or declarations as needed. The promotion plan is then regenerated based on the updates. Use the [Read One Promotion](promotions/get-one-promotion.html) or [Read All Promotions](promotions/get-all-promotions.html) to view the promotion plan.

If you do not set any promotion variables, the configuration resource or resources that you specify for the source or target environment will be used as is, and cannot be changed during the promotion operation. Refer to [Promotion Variables](promotion-variables.html) for more information.

When you choose to start the promotion operation, the promotion plan supplies the promotion operation instructions to the Promotions service. The Promotions service then:

* Filters out any configuration resources that haven't changed, and calls the required target environment API using the new or altered resources.

* Sets the promotion's `startedAt` and `status` values.

* Collects any errors into a JSON array, and returns the errors.

* Updates the promotion's `completedAt` and `status` values when the promotion operation is complete.

## Promotions data model

| Property                      | Type        | Required          | Mutable   | Description                                                                                                                                                                                                                                                                        |
| ----------------------------- | ----------- | ----------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `createdAt`                   | Date        | N/A               | Read-only | The date and time the promotion was created.                                                                                                                                                                                                                                       |
| `completedAt`                 | Date        | N/A               | Read-only | The date and time the promotion operation completed.                                                                                                                                                                                                                               |
| `description`                 | String      | Optional          | Mutable   | A description of the promotion to be performed.                                                                                                                                                                                                                                    |
| `errors`                      | Object\[]   | N/A               | Read-only | An array of JSON objects correlating the configuration resource identifier in the source environment to the error messages from the target environment.                                                                                                                            |
| `excludedResources`           | Object\[]\* | Optional          | Mutable   | An array of JSON objects. \*Optionally, this can be an array of strings. Contains the resource identifiers, and resource URLs for the configuration resources to be excluded from promotion.                                                                                       |
| `resourceMapping`             | Map         | Optional          | Mutable   | A mapping of the configuration resource identifiers in the source environment to the configuration resource identifiers in the target environment.                                                                                                                                 |
| `promotionPlan`               | Object\[]   | N/A               | Read-only | An array of JSON objects containing the promotion plan generated. The promotion plan is generated by the POST operation, but is returned only by either of the Read Promotion operations. For a DELETE operation, the `payload` property in the response will be empty.            |
| `promotionPlan.steps`         | Object\[]   | N/A               | Read-only | An array of JSON objects identifying the resource or resources, the configuration of the resource or resources, and the target environment or environments.                                                                                                                        |
| `promotionPlan.totalDistance` | Integer     | N/A               | Read-only | (Internal use only.) A comparison metric the Configuration Management service uses to determine whether there is a comparable resource in the target environment to replace.                                                                                                       |
| `selectedResources`           | Object\[]\* | Optional          | Mutable   | An array of JSON objects. \*Optionally, this can be an array of strings. Contains the resource identifiers, and resource URLs for the configuration resources selected for promotion. If this is omitted, the entire current environment is used (the environment ID is injected.) |
| `sourceEnvironment`           | Object      | Optional          | Mutable   | Contains the identifier of the source environment.                                                                                                                                                                                                                                 |
| `sourceEnvironment.id`        | String      | Required/Optional | Mutable   | The identifier of the source environment.                                                                                                                                                                                                                                          |
| `sourceSnapshot`              | Object      | Optional          | Mutable   | Contains the identifier of the snapshot to use as the promotion source.                                                                                                                                                                                                            |
| `sourceSnapshot.id`           | String      | Required/Optional | Mutable   | The identifier of the snapshot to use as the promotion source. If not specified, the Configuration Management service automatically generates a snapshot of the source environment at the time of the POST request, and uses that snapshot as the promotion source.                |
| `startedAt`                   | Date        | N/A               | Read-only | The date and time the promotion operation started.                                                                                                                                                                                                                                 |
| `status`                      | String      | N/A               | Read-only | An enumeration indicating the status of the promotion. This can be: `NEW`, `PREPARING`, `ADDITIONAL_SNAPSHOTS_REQUESTED`, `READY`, `IN_PROGRESS`, `VALIDATION_FAILED`, `COMPLETED`, `ERROR`, `ROLLED_BACK`, `ROLLBACK_NEW`, `ROLLBACK_PREPARING`.                                  |
| `targetEnvironment`           | Object      | Required          | Immutable | A JSON object containing the identifier of the target environment.                                                                                                                                                                                                                 |
| `targetEnvironment.id`        | String      | Required          | Immutable | The identifier of the target environment.                                                                                                                                                                                                                                          |
| `targetSnapshot`              | Object      | N/A               | Read-only | A JSON object containing the identifier of the target snapshot.                                                                                                                                                                                                                    |
| `targetSnapshot.id`           | String      | Required          | Immutable | The identifier of the target snapshot.                                                                                                                                                                                                                                             |

## Rolling back a promotion

You can roll back promotions as needed (whether they failed or were successful), restoring the environment to its prior state.

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | A rollback cannot be undone, so be sure to review the limitations and considerations before you use it. |

### Limitations and considerations

* You can roll back only the most recent promotion to the target environment. You can't select a subset of resources to roll back, nor can you roll back a completed rollback.

* A promotion can sometimes affect resources that weren't part of the promotion plan. For example, if you promote the deletion of a policy that was assigned to an application, the promotion also deletes the association between the application and the policy in the target environment. To restore the target environment to its previous state, a rollback must not only restore the deleted policy, but also restore the association between the policy and the application. In this case, the application is considered an indirectly affected resource, and is included in the rollback.

* If you update promoted resources in the target environment after the initial promotion and before the rollback, those changes can be overwritten by the rollback.

---

---
title: Push Delivery Settings
description: This information is provided as part of the early-access program. API details described here might change before the official release of the feature.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/push-delivery-settings
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/push-delivery-settings.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  push-delivery-data-model: Push delivery data model
---

# Push Delivery Settings

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This information is provided as part of the early-access program. API details described here might change before the official release of the feature. |

You can use the `pushDeliverySettings` endpoint to create a custom sender for push notifications.

This allows you to use a gateway of your own to send the push data to push notification services such as APNs and FCM, rather than having PingOne communicate directly with the push notification services.

If you define such a gateway, you just have to provide PingOne with the authentication credentials for your gateway rather than having to provide your credentials for the push notification service.

You can define up to three custom push senders.

## Push delivery data model

| Property                                    | Type   | Required? | Mutable?  | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------- | ------ | --------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authentication`                            | Object | Required  | Mutable   | Contains the information for authenticating with the provider.                                                                                                                                                                                                                                                                                                                                                    |
| `authentication.assertion`                  | String | Required  | Mutable   | The assertion to use if `authentication.grantType` is set to `JWT_BEARER`. Must be a valid JWT.                                                                                                                                                                                                                                                                                                                   |
| `authentication.authToken`                  | String | Required  | Mutable   | The authentication token for the custom provider account. Required when `authentication.method`=`BEARER`                                                                                                                                                                                                                                                                                                          |
| `authentication.authUrl`                    | String | Required  | Mutable   | The URL of the authorization server that provides the access token. Required when `authentication.method`=`OAUTH2`                                                                                                                                                                                                                                                                                                |
| `authentication.clientAuthenticationMethod` | String | N/A       | Read-only | The method used for sending credentials for OAuth2. Returned in responses for custom providers that require OAuth 2 authentication. For client ID/secret-based authentication, the value returned is `BASIC_AUTH_HEADER`. For JWT-based authentication, the value returned is `BODY`.                                                                                                                             |
| `authentication.clientId`                   | String | Required  | Mutable   | The client's public identifier. Required when `authentication.grantType` is set to `CLIENT_CREDENTIALS`.                                                                                                                                                                                                                                                                                                          |
| `authentication.clientSecret`               | String | Required  | Mutable   | The client's secret. Required when `authentication.grantType` is set to `CLIENT_CREDENTIALS`.                                                                                                                                                                                                                                                                                                                     |
| `authentication.grantType`                  | String | Optional  | Mutable   | The grant type used. Relevant for custom providers that require OAuth 2 authentication. Set to `JWT_BEARER` for JWT-based authentication, and to `CLIENT_CREDENTIALS` for authentication based on client ID and secret. If not specified in the request, the default value is `CLIENT_CREDENTIALS`.                                                                                                               |
| `authentication.headerName`                 | String | Required  | Mutable   | The name of the custom header used for authentication. Required when `authentication.method`=`CUSTOM_HEADER`                                                                                                                                                                                                                                                                                                      |
| `authentication.headerValue`                | String | Required  | Mutable   | The value to use for the custom header used for authentication. Required when `authentication.method`=`CUSTOM_HEADER`                                                                                                                                                                                                                                                                                             |
| `authentication.method`                     | String | Required  | Mutable   | The custom provider account's authentication method. Possible values:\* BASIC - username/password\* BEARER - bearer token\* OAUTH2 - OAuth 2\* CUSTOM\_HEADER - authentication using a custom header                                                                                                                                                                                                              |
| `authentication.password`                   | String | Required  | Mutable   | The password for the custom provider account. Required when `authentication.method`=`BASIC`                                                                                                                                                                                                                                                                                                                       |
| `authentication.scopes`                     | Array  | Optional  | Mutable   | When `authentication.method` is set to OAUTH2, use `scopes` to specify the capabilities that the issued token should have, for example, `["push:send"]`.                                                                                                                                                                                                                                                          |
| `authentication.username`                   | String | Required  | Mutable   | The username for the custom provider account. Required when `authentication.method`=`BASIC`                                                                                                                                                                                                                                                                                                                       |
| `name`                                      | String | Required  | Mutable   | The name you want to use for the provider.                                                                                                                                                                                                                                                                                                                                                                        |
| `provider`                                  | String | Required  | Immutable | Must be set to `CUSTOM_PROVIDER`.                                                                                                                                                                                                                                                                                                                                                                                 |
| `requests.body`                             | String | Required  | Mutable   | The body for the request sent to the push gateway. Must include the mandatory ${push-data} variable, which represents the data provided by PingOne so that you can make the appropriate API calls to the push notification service to send the push notifications to your users. You can also include the optional ${push-provider} variable to specify the push notification service, such as APNS, FCM, or HMS. |
| `requests.deliveryMethod`                   | String | Required  | Mutable   | The notification's delivery method. Must be set to `PUSH`.                                                                                                                                                                                                                                                                                                                                                        |
| `requests.headers`                          | Array  | Optional  | Mutable   | The headers to include for the request, for example, `{ "content-type":"application/json" }`.                                                                                                                                                                                                                                                                                                                     |
| `requests.method`                           | String | Required  | Mutable   | The type of HTTP request method. For push senders, must be set to `POST`.                                                                                                                                                                                                                                                                                                                                         |
| `requests.url`                              | String | Required  | Mutable   | The URL of the gateway for the provider, for example, https\://pushgateway.example.com                                                                                                                                                                                                                                                                                                                            |

[Run in Postman](https://god.gw.postman.com/run-collection/19814817-00f505f8-96d7-4957-9efd-2c9f7e345bc1?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D19814817-00f505f8-96d7-4957-9efd-2c9f7e345bc1%26entityType%3Dcollection%26workspaceId%3D936f1637-06aa-461a-b23d-0964e90621c6)

---

---
title: Read All Custom Push Providers
description: This example uses the pushDeliverySettings endpoint to return the information for all the custom push providers defined for the PingOne environment.
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/push-delivery-settings/get_custom_push_providers
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/push-delivery-settings/get_custom_push_providers.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read All Custom Push Providers

##

```none
GET {{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings
```

This example uses the `pushDeliverySettings` endpoint to return the information for all the custom push providers defined for the PingOne environment.

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings"
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
GET /v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings',
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

url = "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/notificationsSettings/pushDeliverySettings")!,timeoutInterval: Double.infinity)
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
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "self": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/notificationsSettings/pushDeliverySettings"
        }
    },
    "_embedded": {
        "pushDeliverySettings": [
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/notificationsSettings/pushDeliverySettings/be724435-b51c-4c86-88ec-adf84bf27b69"
                    }
                },
                "id": "be724435-b51c-4c86-88ec-adf84bf27b69",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "name": "custom push provider",
                "provider": "CUSTOM_PROVIDER",
                "authentication": {
                    "username": "one",
                    "method": "BASIC"
                },
                "requests": [
                    {
                        "deliveryMethod": "PUSH",
                        "url": "https://www.example.com",
                        "method": "POST",
                        "body": "data=${push-data}",
                        "headers": {
                            "content-type": "application/x-www-form-urlencoded"
                        }
                    }
                ],
                "createdAt": "2026-03-19T10:33:25.665Z",
                "updatedAt": "2026-03-19T10:33:25.665Z"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/notificationsSettings/pushDeliverySettings/4d64a2b8-80cf-4295-97ae-ad33ab08db6b"
                    }
                },
                "id": "4d64a2b8-80cf-4295-97ae-ad33ab08db6b",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "name": "Custom push provider - created with API",
                "provider": "CUSTOM_PROVIDER",
                "authentication": {
                    "grantType": "CLIENT_CREDENTIALS",
                    "clientAuthenticationMethod": "BASIC_AUTH_HEADER",
                    "authUrl": "https://login.example.com/oauth/token",
                    "clientId": "idForAccount",
                    "scopes": [
                        "push:send"
                    ],
                    "method": "OAUTH2"
                },
                "requests": [
                    {
                        "deliveryMethod": "PUSH",
                        "url": "https://www.example.com",
                        "method": "POST",
                        "body": "data=${push-data}",
                        "headers": {
                            "content-type": "application/json"
                        }
                    }
                ],
                "createdAt": "2026-06-23T15:42:12.555Z",
                "updatedAt": "2026-06-23T15:42:12.555Z"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/notificationsSettings/pushDeliverySettings/61debe8b-fc8a-4d69-9c99-082cd1d982ea"
                    }
                },
                "id": "61debe8b-fc8a-4d69-9c99-082cd1d982ea",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "name": "Custom push provider - created with API 2",
                "provider": "CUSTOM_PROVIDER",
                "authentication": {
                    "grantType": "CLIENT_CREDENTIALS",
                    "clientAuthenticationMethod": "BASIC_AUTH_HEADER",
                    "authUrl": "https://login.example.com/oauth/token",
                    "clientId": "idForAccount",
                    "scopes": [
                        "push:send"
                    ],
                    "method": "OAUTH2"
                },
                "requests": [
                    {
                        "deliveryMethod": "PUSH",
                        "url": "https://www.example.com",
                        "method": "POST",
                        "body": "data=${push-data}",
                        "headers": {
                            "content-type": "application/json"
                        }
                    }
                ],
                "createdAt": "2026-06-23T15:52:55.506Z",
                "updatedAt": "2026-06-23T15:52:55.506Z"
            }
        ]
    },
    "size": 3
}
```

---

---
title: Read All Promotions
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/promotions/get-all-promotions
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/promotions/get-all-promotions.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read All Promotions

##

   

```none
GET {{apiPath}}/v1/environments/{{envID}}/promotions
```

Use the GET `{{apiPath}}/v1/environments/{{envID}}/promotions` request to return the details for all promotions.

> **Collapse: Query parameters**
>
> | Query parameter | Attributes (or allowed limits) |
> | --------------- | ------------------------------ |
> | `filter`        | status (eq)                    |

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/promotions' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/promotions")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/promotions"
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
GET /v1/environments/{{envID}}/promotions HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/promotions")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/promotions",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/promotions',
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

url = "{{apiPath}}/v1/environments/{{envID}}/promotions"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/promotions');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/promotions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/promotions")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions?limit=25"
        }
    },
    "_embedded": {
        "promotions": [
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/5d2105ef-2657-4920-93ff-1328f86d51ab"
                    }
                },
                "_embedded": null,
                "id": "5d2105ef-2657-4920-93ff-1328f86d51ab",
                "createdAt": "2026-05-21T17:47:15.975Z",
                "updatedAt": "2026-05-21T17:47:15.975Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "a9009a41-80f0-497b-a194-338deded5d1c",
                "sourceSnapshot": {
                    "id": "a9009a41-80f0-497b-a194-338deded5d1c"
                },
                "targetSnapshotId": "d98c98d9-50f1-4774-9c92-c47f7522d657",
                "targetSnapshot": {
                    "id": "d98c98d9-50f1-4774-9c92-c47f7522d657"
                },
                "previousPromotion": {
                    "id": "461a33b0-f041-44b0-92ff-e59402c1c2ac"
                },
                "status": "ERROR",
                "promotionErrors": [
                    "Selected resources list is empty"
                ],
                "resourceMapping": {},
                "description": "Rolling back promotion."
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/f2a2c7ac-3cc8-4d6a-b506-74fe3d416b2e"
                    }
                },
                "_embedded": null,
                "id": "f2a2c7ac-3cc8-4d6a-b506-74fe3d416b2e",
                "createdAt": "2026-05-21T11:53:41.990Z",
                "updatedAt": "2026-05-21T11:53:41.990Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "b958d5ec-07d9-4cf4-aef8-47060a55bc28",
                "sourceSnapshot": {
                    "id": "b958d5ec-07d9-4cf4-aef8-47060a55bc28"
                },
                "targetSnapshotId": "ef487a49-b27f-4845-b411-67c95b65eedb",
                "targetSnapshot": {
                    "id": "ef487a49-b27f-4845-b411-67c95b65eedb"
                },
                "status": "NEW",
                "selectedResources": [
                    "26a126c2-054f-4f18-b077-8226c0c4bf3e"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f5"
                ],
                "resourceMapping": {
                    "2c3b1245-2c38-4174-97fa-069d88a543b1": "c7c92d16-e07b-4ddb-8d17-073fea3a219c"
                },
                "description": "Test promotion of population"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/4012c2b0-4700-41b7-befa-64972e9ad975"
                    }
                },
                "_embedded": null,
                "id": "4012c2b0-4700-41b7-befa-64972e9ad975",
                "createdAt": "2026-05-20T15:01:11.465Z",
                "updatedAt": "2026-05-20T15:01:11.465Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "2bd7f053-eb90-416e-87b9-b7031816e7e2",
                "sourceSnapshot": {
                    "id": "2bd7f053-eb90-416e-87b9-b7031816e7e2"
                },
                "targetSnapshotId": "10d01baf-563c-42db-899e-e08cd9345e55",
                "targetSnapshot": {
                    "id": "10d01baf-563c-42db-899e-e08cd9345e55"
                },
                "status": "NEW",
                "selectedResources": [
                    "26a126c2-054f-4f18-b077-8226c0c4bf3e"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                ],
                "resourceMapping": {
                    "2c3b1245-2c38-4174-97fa-069d88a543b1": "c7c92d16-e07b-4ddb-8d17-073fea3a219c"
                },
                "description": "Test promotion of population"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/461a33b0-f041-44b0-92ff-e59402c1c2ac"
                    }
                },
                "_embedded": null,
                "id": "461a33b0-f041-44b0-92ff-e59402c1c2ac",
                "createdAt": "2025-07-04T15:51:36.883Z",
                "updatedAt": "2026-05-21T16:36:40.906Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "04776ecf-9f38-40e5-a833-514f0c86fb23",
                "sourceSnapshot": {
                    "id": "04776ecf-9f38-40e5-a833-514f0c86fb23"
                },
                "targetSnapshotId": "a9009a41-80f0-497b-a194-338deded5d1c",
                "targetSnapshot": {
                    "id": "a9009a41-80f0-497b-a194-338deded5d1c"
                },
                "status": "ERROR",
                "promotionErrors": [
                    "400 Bad Request on PUT request for \"https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/27091971-0a42-4f67-95d1-d617fc2a16e5\": \"{<EOL>  \"id\" : \"419562f1-8bce-4fac-80c3-bf41aa840fa2\",<EOL>  \"code\" : \"INVALID_DATA\",<EOL>  \"message\" : \"The request could not be completed. One or more validation errors were in the request.\",<EOL>  \"details\" : [ {<EOL>    \"code\" : \"INVALID_VALUE\",<EOL>    \"target\" : \"passwordPolicy\",<EOL>    \"message\" : \"invalid passwordPolicy value was provided\"<EOL>  } ]<EOL>}\""
                ],
                "selectedResources": [
                    "26a126c2-054f-4f18-b077-8226c0c4bf3e"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                ],
                "resourceMapping": {
                    "5ab94557-59c3-4afc-bbf6-046444bd04b8": "f0c75a0b-859e-433d-9edc-07a7c847e185",
                    "26a126c2-054f-4f18-b077-8226c0c4bf3e": "27091971-0a42-4f67-95d1-d617fc2a16e5",
                    "2c3b1245-2c38-4174-97fa-069d88a543b1": "c7c92d16-e07b-4ddb-8d17-073fea3a219c"
                },
                "startedAt": "2026-05-21T16:36:40.906Z",
                "completedAt": "2026-05-21T16:36:42.718Z",
                "description": "Test promotion of population"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/e2cf9a22-5aeb-4046-ad3d-c6dc97c90ef9"
                    }
                },
                "_embedded": null,
                "id": "e2cf9a22-5aeb-4046-ad3d-c6dc97c90ef9",
                "createdAt": "2025-07-04T15:29:43.199Z",
                "updatedAt": "2025-07-04T15:29:43.199Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "0c31da80-8588-4ec1-8837-ad7f7aa94884",
                "sourceSnapshot": {
                    "id": "0c31da80-8588-4ec1-8837-ad7f7aa94884"
                },
                "targetSnapshotId": "9f6f1184-6d61-4a42-8115-136c34574d8d",
                "targetSnapshot": {
                    "id": "9f6f1184-6d61-4a42-8115-136c34574d8d"
                },
                "status": "VALIDATION_FAILED",
                "promotionErrors": [
                    "Mapped target resources were not found in the target snapshot list: [c7c92d16-e07b-4ddb-8d17-073fea3a219c]"
                ],
                "selectedResources": [
                    "26a126c2-054f-4f18-b077-8226c0c4bf3e"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                ],
                "resourceMapping": {
                    "26a126c2-054f-4f18-b077-8226c0c4bf3e": "c7c92d16-e07b-4ddb-8d17-073fea3a219c"
                },
                "description": "Test promotion of agreements and themes"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/a7575b6f-f91f-4279-b88d-96498bc6fb13"
                    }
                },
                "_embedded": null,
                "id": "a7575b6f-f91f-4279-b88d-96498bc6fb13",
                "createdAt": "2025-07-03T16:50:26.621Z",
                "updatedAt": "2025-07-03T16:50:26.621Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "d2bbfc49-ec83-446f-a533-5e78a1a20323",
                "sourceSnapshot": {
                    "id": "d2bbfc49-ec83-446f-a533-5e78a1a20323"
                },
                "targetSnapshotId": "59c99f40-cbc1-4f99-93f8-36960a0d3f23",
                "targetSnapshot": {
                    "id": "59c99f40-cbc1-4f99-93f8-36960a0d3f23"
                },
                "status": "VALIDATION_FAILED",
                "promotionErrors": [
                    "Mapped target resources were not found in the target snapshot list: [c7c92d16-e07b-4ddb-8d17-073fea3a219c]"
                ],
                "selectedResources": [
                    "26a126c2-054f-4f18-b077-8226c0c4bf3e"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                ],
                "resourceMapping": {
                    "2c3b1245-2c38-4174-97fa-069d88a543b1": "c7c92d16-e07b-4ddb-8d17-073fea3a219c"
                },
                "description": "Test promotion of another population"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/630c1dfe-8a17-41f8-9765-a4996501f84a"
                    }
                },
                "_embedded": null,
                "id": "630c1dfe-8a17-41f8-9765-a4996501f84a",
                "createdAt": "2025-07-03T16:40:13.301Z",
                "updatedAt": "2025-07-03T16:40:13.301Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "1185c5ea-9451-4491-9987-658335cfa667",
                "sourceSnapshot": {
                    "id": "1185c5ea-9451-4491-9987-658335cfa667"
                },
                "targetSnapshotId": "7da7458d-e85f-45b6-84b4-07c094012c44",
                "targetSnapshot": {
                    "id": "7da7458d-e85f-45b6-84b4-07c094012c44"
                },
                "status": "VALIDATION_FAILED",
                "promotionErrors": [
                    "Mapped source resources were not found in the source snapshot list: [1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e]",
                    "Mapped target resources were not found in the target snapshot list: [363ef235-f6fe-4bc7-ae3d-63217482f57f]"
                ],
                "selectedResources": [
                    "1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e",
                    "8ae17de9-8e2a-41db-916e-3e46adaf16d9"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                ],
                "resourceMapping": {
                    "1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e": "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                },
                "description": "Test promotion of agreements and themes"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/f2467696-1d16-483c-8f9c-00a7c62fddfe"
                    }
                },
                "_embedded": null,
                "id": "f2467696-1d16-483c-8f9c-00a7c62fddfe",
                "createdAt": "2025-04-22T16:31:46.717Z",
                "updatedAt": "2025-04-22T16:31:46.717Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "a502a852-509a-41ac-852a-6a1d4a9b8ea5",
                "sourceSnapshot": {
                    "id": "a502a852-509a-41ac-852a-6a1d4a9b8ea5"
                },
                "targetSnapshotId": "87eff785-97b6-4bbb-8016-7acd320612b4",
                "targetSnapshot": {
                    "id": "87eff785-97b6-4bbb-8016-7acd320612b4"
                },
                "status": "VALIDATION_FAILED",
                "promotionErrors": [
                    "Mapped source resources were not found in the source snapshot list: [1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e]",
                    "Mapped target resources were not found in the target snapshot list: [363ef235-f6fe-4bc7-ae3d-63217482f57f]"
                ],
                "selectedResources": [
                    "1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e",
                    "8ae17de9-8e2a-41db-916e-3e46adaf16d9"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                ],
                "resourceMapping": {
                    "1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e": "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                },
                "description": "Test promotion of agreements and themes"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/166f212b-5615-461c-a13d-9330439ecb19"
                    }
                },
                "_embedded": null,
                "id": "166f212b-5615-461c-a13d-9330439ecb19",
                "createdAt": "2024-11-01T14:13:02.018Z",
                "updatedAt": "2024-11-01T14:13:02.018Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "23ef7815-cfde-4227-8121-369887e9b21e",
                "sourceSnapshot": {
                    "id": "23ef7815-cfde-4227-8121-369887e9b21e"
                },
                "targetSnapshotId": "ae20eee9-193e-4c87-bbec-94beaa4eba5f",
                "targetSnapshot": {
                    "id": "ae20eee9-193e-4c87-bbec-94beaa4eba5f"
                },
                "status": "VALIDATION_FAILED",
                "promotionErrors": [
                    "Mapped source resources were not found in the source snapshot list: [1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e]",
                    "Mapped target resources were not found in the target snapshot list: [363ef235-f6fe-4bc7-ae3d-63217482f57f]"
                ],
                "selectedResources": [
                    "1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e",
                    "8ae17de9-8e2a-41db-916e-3e46adaf16d9"
                ],
                "excludedResources": [
                    "363ef235-f6fe-4bc7-ae3d-63217482f57f"
                ],
                "resourceMapping": {},
                "description": "Test promotion of agreements and themes"
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/promotions/84fc497e-4b8e-45af-b8a7-a67b754363b1"
                    }
                },
                "_embedded": null,
                "id": "84fc497e-4b8e-45af-b8a7-a67b754363b1",
                "createdAt": "2024-09-11T14:27:32.959Z",
                "updatedAt": "2024-09-11T14:27:32.959Z",
                "sourceEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "sourceEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "targetEnvironmentId": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
                "targetEnvironment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "sourceSnapshotId": "d0265755-14a2-43e7-b915-4328f637575b",
                "sourceSnapshot": {
                    "id": "d0265755-14a2-43e7-b915-4328f637575b"
                },
                "targetSnapshotId": "4a10525c-3f54-4ddc-9c8d-083a38619b9d",
                "targetSnapshot": {
                    "id": "4a10525c-3f54-4ddc-9c8d-083a38619b9d"
                },
                "status": "VALIDATION_FAILED",
                "selectedResources": [
                    "1d0ff9f4-0fae-4859-9dfa-0aa6cac9150e",
                    "8ae17de9-8e2a-41db-916e-3e46adaf16d9"
                ],
                "resourceMapping": {},
                "description": "Test promotion of agreements and themes"
            }
        ]
    },
    "size": 10
}
```

---

---
title: Read All Snapshot Versions
component: pingone-api-ea
page_id: pingone-api-ea:platform:early-access/configuration-management/snapshots/get-all-snapshot-versions
canonical_url: https://developer.pingidentity.com/pingone-api-ea/platform/early-access/configuration-management/snapshots/get-all-snapshot-versions.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read All Snapshot Versions

##

   

```none
GET {{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions
```

Use GET `{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions` to return the version information for all versions of the snapshot of the specified configuration resource.

Any `configuration` attributes specified that contain sensitive information in plain text (such as, display names, client secrets, passwords) are masked in the response, and aren't available to any caller, even administrators. Refer to [Snapshots data model](../snapshots.html#snaphots-model).

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions"
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
GET /v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions',
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

url = "{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/snapshots/{{configResourceID}}/versions")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/0b7795ac-c589-4311-82bd-b1a9caff7a6a/versions"
        }
    },
    "_embedded": {
        "snapshots": [
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/0b7795ac-c589-4311-82bd-b1a9caff7a6a/versions/ab00b05b-26d3-4de1-9c17-74a08adc238e"
                    }
                },
                "id": "c47e8abf-e830-4bb4-9fe0-260895ce326e",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "snapshotId": "ab00b05b-26d3-4de1-9c17-74a08adc238e",
                "resource": {
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                },
                "createdAt": "2024-09-09T14:43:55.346Z",
                "startedAt": "2024-09-09T14:43:55.482Z",
                "completedAt": "2024-09-09T14:43:55.538Z",
                "versionedAt": "2021-10-08T18:00:20.458Z",
                "status": "COMPLETE",
                "resourceUrl": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                "configuration": {
                    "_links": {
                        "self": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                        },
                        "environment": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                        }
                    },
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                    "environment": {
                        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "name": "ApplicationPopulation_1633716020",
                    "description": "Population for application users",
                    "userCount": 1,
                    "createdAt": "2021-10-08T18:00:20.458Z",
                    "updatedAt": "2021-10-08T18:00:20.458Z",
                    "default": false
                }
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/0b7795ac-c589-4311-82bd-b1a9caff7a6a/versions/79451a5d-8a8f-49be-800a-67f396eb81ed"
                    }
                },
                "id": "51edcd76-6b3e-4ddf-9bf3-44f81f415129",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "snapshotId": "79451a5d-8a8f-49be-800a-67f396eb81ed",
                "resource": {
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                },
                "createdAt": "2024-09-09T13:58:17.675Z",
                "startedAt": "2024-09-09T13:58:17.881Z",
                "completedAt": "2024-09-09T13:58:28.827Z",
                "versionedAt": "2021-10-08T18:00:20.458Z",
                "status": "COMPLETE",
                "resourceUrl": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                "configuration": {
                    "_links": {
                        "self": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                        },
                        "environment": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                        }
                    },
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                    "environment": {
                        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "name": "ApplicationPopulation_1633716020",
                    "description": "Population for application users",
                    "userCount": 1,
                    "createdAt": "2021-10-08T18:00:20.458Z",
                    "updatedAt": "2021-10-08T18:00:20.458Z",
                    "default": false
                }
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/0b7795ac-c589-4311-82bd-b1a9caff7a6a/versions/73a64c05-d67d-49fb-8430-9dc86634e528"
                    }
                },
                "id": "1377ce69-9d42-4e1a-952a-9d00031b4b71",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "snapshotId": "73a64c05-d67d-49fb-8430-9dc86634e528",
                "resource": {
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                },
                "createdAt": "2024-09-06T14:42:36.795Z",
                "startedAt": "2024-09-06T14:42:36.839Z",
                "completedAt": "2024-09-06T14:42:45.470Z",
                "versionedAt": "2021-10-08T18:00:20.458Z",
                "status": "COMPLETE",
                "resourceUrl": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                "configuration": {
                    "_links": {
                        "self": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                        },
                        "environment": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                        }
                    },
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                    "environment": {
                        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "name": "ApplicationPopulation_1633716020",
                    "description": "Population for application users",
                    "userCount": 1,
                    "createdAt": "2021-10-08T18:00:20.458Z",
                    "updatedAt": "2021-10-08T18:00:20.458Z",
                    "default": false
                }
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/0b7795ac-c589-4311-82bd-b1a9caff7a6a/versions/c719a926-dee7-4026-b2f6-70f569c9d60d"
                    }
                },
                "id": "7606c962-8b7a-4fb0-aa90-7e97b4953b7c",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "snapshotId": "c719a926-dee7-4026-b2f6-70f569c9d60d",
                "resource": {
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                },
                "createdAt": "2024-09-06T14:37:30.903Z",
                "startedAt": "2024-09-06T14:37:30.962Z",
                "completedAt": "2024-09-06T14:37:44.004Z",
                "versionedAt": "2021-10-08T18:00:20.458Z",
                "status": "COMPLETE",
                "resourceUrl": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                "configuration": {
                    "_links": {
                        "self": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                        },
                        "environment": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                        }
                    },
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                    "environment": {
                        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "name": "ApplicationPopulation_1633716020",
                    "description": "Population for application users",
                    "userCount": 1,
                    "createdAt": "2021-10-08T18:00:20.458Z",
                    "updatedAt": "2021-10-08T18:00:20.458Z",
                    "default": false
                }
            },
            {
                "_links": {
                    "environment": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/snapshots/0b7795ac-c589-4311-82bd-b1a9caff7a6a/versions/cc64ea07-1da0-4bf8-b487-5c178667d8c8"
                    }
                },
                "id": "d443b74c-542c-4ec4-b0b7-20a5e68a2882",
                "environment": {
                    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                },
                "snapshotId": "cc64ea07-1da0-4bf8-b487-5c178667d8c8",
                "resource": {
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                },
                "createdAt": "2024-09-06T14:24:54.035Z",
                "startedAt": "2024-09-06T14:24:54.080Z",
                "completedAt": "2024-09-06T14:25:08.706Z",
                "versionedAt": "2021-10-08T18:00:20.458Z",
                "status": "COMPLETE",
                "resourceUrl": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                "configuration": {
                    "_links": {
                        "self": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/0b7795ac-c589-4311-82bd-b1a9caff7a6a"
                        },
                        "environment": {
                            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                        }
                    },
                    "id": "0b7795ac-c589-4311-82bd-b1a9caff7a6a",
                    "environment": {
                        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
                    },
                    "name": "ApplicationPopulation_1633716020",
                    "description": "Population for application users",
                    "userCount": 1,
                    "createdAt": "2021-10-08T18:00:20.458Z",
                    "updatedAt": "2021-10-08T18:00:20.458Z",
                    "default": false
                }
            }
        ]
    },
    "size": 5
}
```
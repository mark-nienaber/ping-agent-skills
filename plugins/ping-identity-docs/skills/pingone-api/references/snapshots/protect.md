---
title: Create Risk Evaluation
description: The sample shows the POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations operation to create a new risk evaluation resource associated with the environment specified in the request URL. The request body defines the event that is processed for risk evaluation.
component: pingone-api
page_id: pingone-api:protect:risk-evaluations/create-risk-evaluation
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create-risk-evaluation.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Evaluation

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations
```

The sample shows the `POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations` operation to create a new risk evaluation resource associated with the environment specified in the request URL. The request body defines the event that is processed for risk evaluation.

This request uses the `sdk.signals.data` field to provide the additional risk input provided by the Signals (Protect) SDK. For more information, refer to the [Signals (Protect) SDK documentation](../../native-sdks/pingone-risk-sdks/risk_evaluation_sdk.html).

### Prerequisites

* Refer to [Risk Evaluations](../risk-evaluations.html) for important overview information.

* [Create Risk Policy Set](../risk-policies/create_risk_policy_set_scores.html).

> **Collapse: Request Model**
>
> For complete property descriptions, refer to [Risk Evaluations](../risk-evaluations.html).
>
> | Property                  | Type      | Required |
> | ------------------------- | --------- | -------- |
> | `browser`                 | Object    | Optional |
> | `evaluatedFactors.status` | String    | Optional |
> | `evaluatedFactors.type`   | String    | Optional |
> | `event`                   | Object    | Required |
> | `ip`                      | String    | Required |
> | `flow.type`               | String    | Optional |
> | `origin`                  | String    | Optional |
> | `riskPolicySet.id`        | String    | Optional |
> | `riskPolicySet.name`      | String    | Optional |
> | `sdk.signals.data`        | String    | Optional |
> | `session.id`              | String    | Optional |
> | `targetResource.id`       | String    | Optional |
> | `targetResource.name`     | String    | Optional |
> | `user.id`                 | String    | Required |
> | `user.name`               | String    | Optional |
> | `user.type`               | String    | Required |
> | `user.groups`             | String\[] | Optional |
> | `user.groups.name`        | String    | Optional |
> | `sharingType`             | String    | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""event"": {" + "\n" +
@"        ""targetResource"": {" + "\n" +
@"            ""id"": ""{{targetResourceID}}""," + "\n" +
@"            ""name"": ""Jira""" + "\n" +
@"        }," + "\n" +
@"        ""ip"": ""156.35.85.124""," + "\n" +
@"        ""sdk"": {" + "\n" +
@"            ""signals"": {" + "\n" +
@"                ""data"": ""{{signalsSdkPayload}}""" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""flow"": {" + "\n" +
@"            ""type"": ""AUTHENTICATION""," + "\n" +
@"            ""subtype"": ""ACTIVE_SESSION""" + "\n" +
@"        }," + "\n" +
@"        ""session"": {" + "\n" +
@"            ""id"": ""{{sessionID}}""" + "\n" +
@"        }," + "\n" +
@"        ""user"": {" + "\n" +
@"            ""id"": ""john""," + "\n" +
@"            ""name"": ""John DeMock""," + "\n" +
@"            ""type"": ""EXTERNAL""," + "\n" +
@"            ""groups"": [" + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""dev""" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""sre""" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""sharingType"": ""SHARED""," + "\n" +
@"        ""browser"": {" + "\n" +
@"            ""userAgent"": ""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicySet"": {" + "\n" +
@"        ""id"": ""{{riskPolicySetID}}""," + "\n" +
@"        ""name"": ""ExamplePolicy""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"
  method := "POST"

  payload := strings.NewReader(`{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
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
POST /v1/environments/{{envID}}/riskEvaluations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"{{signalsSdkPayload}}\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\",\n            \"subtype\": \"ACTIVE_SESSION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"id\": \"{{riskPolicySetID}}\",\n        \"name\": \"ExamplePolicy\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "sdk": {
        "signals": {
          "data": "{{signalsSdkPayload}}"
        }
      },
      "flow": {
        "type": "AUTHENTICATION",
        "subtype": "ACTIVE_SESSION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "id": "{{riskPolicySetID}}",
      "name": "ExamplePolicy"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "sdk": {
        "signals": {
          "data": "{{signalsSdkPayload}}"
        }
      },
      "flow": {
        "type": "AUTHENTICATION",
        "subtype": "ACTIVE_SESSION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "id": "{{riskPolicySetID}}",
      "name": "ExamplePolicy"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"

payload = json.dumps({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "sdk": {
      "signals": {
        "data": "{{signalsSdkPayload}}"
      }
    },
    "flow": {
      "type": "AUTHENTICATION",
      "subtype": "ACTIVE_SESSION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "id": "{{riskPolicySetID}}",
    "name": "ExamplePolicy"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskEvaluations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "event": {\n        "targetResource": {\n            "id": "{{targetResourceID}}",\n            "name": "Jira"\n        },\n        "ip": "156.35.85.124",\n        "sdk": {\n            "signals": {\n                "data": "{{signalsSdkPayload}}"\n            }\n        },\n        "flow": {\n            "type": "AUTHENTICATION",\n            "subtype": "ACTIVE_SESSION"\n        },\n        "session": {\n            "id": "{{sessionID}}"\n        },\n        "user": {\n            "id": "john",\n            "name": "John DeMock",\n            "type": "EXTERNAL",\n            "groups": [\n                {\n                    "name": "dev"\n                },\n                {\n                    "name": "sre"\n                }\n            ]\n        },\n        "sharingType": "SHARED",\n        "browser": {\n            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"\n        }\n    },\n    "riskPolicySet": {\n        "id": "{{riskPolicySetID}}",\n        "name": "ExamplePolicy"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "sdk": {
      "signals": {
        "data": "{{signalsSdkPayload}}"
      }
    },
    "flow": {
      "type": "AUTHENTICATION",
      "subtype": "ACTIVE_SESSION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "id": "{{riskPolicySetID}}",
    "name": "ExamplePolicy"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"{{signalsSdkPayload}}\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\",\n            \"subtype\": \"ACTIVE_SESSION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"id\": \"{{riskPolicySetID}}\",\n        \"name\": \"ExamplePolicy\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/a35a68e2-8066-4dbc-933b-585e29b64ec8"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "event": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/a35a68e2-8066-4dbc-933b-585e29b64ec8/event"
        }
    },
    "id": "a35a68e2-8066-4dbc-933b-585e29b64ec8",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2024-08-14T14:41:38.075Z",
    "updatedAt": "2024-08-14T14:41:38.075Z",
    "event": {
        "completionStatus": "IN_PROGRESS",
        "targetResource": {
            "id": "ce601c0a-5d55-46cd-9524-387e22a2ce5a",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "01ddc236-0698-467a-919e-40ef0d47cb34"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "8893902f-e7b7-40fe-85ef-82e06f85266f",
        "name": "Example - Weight Policy"
    },
    "result": {
        "level": "LOW",
        "score": 1.5625,
        "source": "AGGREGATED_WEIGHTS",
        "type": "VALUE"
    },
    "details": {
        "ipAddressReputation": {
            "score": 0,
            "domain": {
                "asn": 766,
                "sld": "uniovi",
                "tld": "es",
                "organization": "universidad de oviedo",
                "isp": "entidad publica empresarial red.es"
            },
            "level": "LOW"
        },
        "anonymousNetworkDetected": false,
        "country": "spain",
        "device": {
            "id": "Id-4c0013c4-5739-440f-91f4-147f460dd2ec",
            "estimatedDistance": 0,
            "os": {
                "name": "Mac OS X"
            },
            "browser": {
                "name": "Chrome"
            }
        },
        "state": "asturias",
        "city": "oviedo",
        "impossibleTravel": false,
        "suspiciousDevice": {
            "level": "LOW",
            "type": "DEVICE"
        },
        "ipVelocityByUser": {
            "level": "LOW",
            "threshold": {
                "source": "MIN_NOT_REACHED"
            },
            "velocity": {
                "distinctCount": 1,
                "during": 3600
            },
            "type": "VELOCITY"
        },
        "userLocationAnomaly": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "USER_LOCATION_ANOMALY"
        },
        "trafficAnomalyCreatedFromAPI": {
            "level": "LOW",
            "type": "TRAFFIC_ANOMALY"
        },
        "geoVelocity": {
            "level": "LOW",
            "type": "GEO_VELOCITY"
        },
        "botDetection": {
            "level": "HIGH",
            "reason": "Browser loading anomaly",
            "detected": {
                "rule": {
                    "id": 628
                }
            },
            "type": "BOT"
        },
        "newDevice": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "DEVICE"
        },
        "ipRisk": {
            "level": "LOW",
            "type": "IP_REPUTATION"
        },
        "userBasedRiskBehavior": {
            "level": "MEDIUM",
            "reason": "The default fallback level is used",
            "status": "IN_TRAINING_PERIOD",
            "type": "USER_RISK_BEHAVIOR"
        },
        "adversaryInTheMiddle": {
            "level": "HIGH",
            "reason": "Unusual domain ping-devops.com. If this is a known domain it should be added to the predictor's allow List.",
            "status": "UNKNOWN_DOMAIN",
            "type": "ADVERSARY_IN_THE_MIDDLE"
        }
    }
}
```

---

---
title: Create Risk Evaluation (includes device trust predictor)
description: This example uses POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations to create a risk evaluation where the risk policy used includes the PingID Device Trust predictor.
component: pingone-api
page_id: pingone-api:protect:risk-evaluations/create_risk_eval_with_trust_agent
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create_risk_eval_with_trust_agent.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Evaluation (includes device trust predictor)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations
```

This example uses `POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations` to create a risk evaluation where the risk policy used includes the PingID Device Trust predictor.

The body of the request does not contain any special parameters beyond those used ordinarily for risk evaluations.

The response includes the risk level calculated for the device trust predictor as well as the reason for the risk level for the predictor.

If the risk level for the predictor is not HIGH, the response will also include data for the user's computer, under `details.device.agent`.

> **Collapse: Request Model**
>
> For complete property descriptions, refer to [Risk Evaluations](#risk-evaluations).
>
> | Property                  | Type      | Required |
> | ------------------------- | --------- | -------- |
> | `browser`                 | Object    | Optional |
> | `evaluatedFactors.status` | String    | Optional |
> | `evaluatedFactors.type`   | String    | Optional |
> | `event`                   | Object    | Required |
> | `flow.type`               | String    | Optional |
> | `flow.subtype`            | String    | Optional |
> | `ip`                      | String    | Required |
> | `origin`                  | String    | Optional |
> | `riskPolicySet.id`        | String    | Optional |
> | `riskPolicySet.name`      | String    | Optional |
> | `sdk.signals.data`        | String    | Optional |
> | `session.id`              | String    | Optional |
> | `targetResource.id`       | String    | Optional |
> | `targetResource.name`     | String    | Optional |
> | `user.id`                 | String    | Required |
> | `user.name`               | String    | Optional |
> | `user.type`               | String    | Required |
> | `user.groups`             | String\[] | Optional |
> | `user.groups.name`        | String    | Optional |
> | `sharingType`             | String    | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkOutput}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkOutput}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""event"": {" + "\n" +
@"        ""targetResource"": {" + "\n" +
@"            ""id"": ""{{targetResourceID}}""," + "\n" +
@"            ""name"": ""Jira""" + "\n" +
@"        }," + "\n" +
@"        ""ip"": ""156.35.85.124""," + "\n" +
@"        ""sdk"": {" + "\n" +
@"            ""signals"": {" + "\n" +
@"                ""data"": ""{{signalsSdkOutput}}""" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""flow"": {" + "\n" +
@"            ""type"": ""AUTHENTICATION""," + "\n" +
@"            ""subtype"": ""ACTIVE_SESSION""" + "\n" +
@"        }," + "\n" +
@"        ""session"": {" + "\n" +
@"            ""id"": ""{{sessionID}}""" + "\n" +
@"        }," + "\n" +
@"        ""user"": {" + "\n" +
@"            ""id"": ""john""," + "\n" +
@"            ""name"": ""John DeMock""," + "\n" +
@"            ""type"": ""EXTERNAL""," + "\n" +
@"            ""groups"": [" + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""dev""" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""sre""" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""sharingType"": ""SHARED""," + "\n" +
@"        ""browser"": {" + "\n" +
@"            ""userAgent"": ""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicySet"": {" + "\n" +
@"        ""id"": ""{{riskPolicySetID}}""," + "\n" +
@"        ""name"": ""ExamplePolicy""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"
  method := "POST"

  payload := strings.NewReader(`{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkOutput}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
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
POST /v1/environments/{{envID}}/riskEvaluations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkOutput}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"{{signalsSdkOutput}}\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\",\n            \"subtype\": \"ACTIVE_SESSION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"id\": \"{{riskPolicySetID}}\",\n        \"name\": \"ExamplePolicy\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "sdk": {
        "signals": {
          "data": "{{signalsSdkOutput}}"
        }
      },
      "flow": {
        "type": "AUTHENTICATION",
        "subtype": "ACTIVE_SESSION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "id": "{{riskPolicySetID}}",
      "name": "ExamplePolicy"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "sdk": {
        "signals": {
          "data": "{{signalsSdkOutput}}"
        }
      },
      "flow": {
        "type": "AUTHENTICATION",
        "subtype": "ACTIVE_SESSION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "id": "{{riskPolicySetID}}",
      "name": "ExamplePolicy"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"

payload = json.dumps({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "sdk": {
      "signals": {
        "data": "{{signalsSdkOutput}}"
      }
    },
    "flow": {
      "type": "AUTHENTICATION",
      "subtype": "ACTIVE_SESSION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "id": "{{riskPolicySetID}}",
    "name": "ExamplePolicy"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskEvaluations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "event": {\n        "targetResource": {\n            "id": "{{targetResourceID}}",\n            "name": "Jira"\n        },\n        "ip": "156.35.85.124",\n        "sdk": {\n            "signals": {\n                "data": "{{signalsSdkOutput}}"\n            }\n        },\n        "flow": {\n            "type": "AUTHENTICATION",\n            "subtype": "ACTIVE_SESSION"\n        },\n        "session": {\n            "id": "{{sessionID}}"\n        },\n        "user": {\n            "id": "john",\n            "name": "John DeMock",\n            "type": "EXTERNAL",\n            "groups": [\n                {\n                    "name": "dev"\n                },\n                {\n                    "name": "sre"\n                }\n            ]\n        },\n        "sharingType": "SHARED",\n        "browser": {\n            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"\n        }\n    },\n    "riskPolicySet": {\n        "id": "{{riskPolicySetID}}",\n        "name": "ExamplePolicy"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "sdk": {
      "signals": {
        "data": "{{signalsSdkOutput}}"
      }
    },
    "flow": {
      "type": "AUTHENTICATION",
      "subtype": "ACTIVE_SESSION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "id": "{{riskPolicySetID}}",
    "name": "ExamplePolicy"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"{{signalsSdkOutput}}\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\",\n            \"subtype\": \"ACTIVE_SESSION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"id\": \"{{riskPolicySetID}}\",\n        \"name\": \"ExamplePolicy\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/312330d7-1514-40e4-ad4b-941acb2e2847"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "event": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/312330d7-1514-40e4-ad4b-941acb2e2847/event"
        }
    },
    "id": "312330d7-1514-40e4-ad4b-941acb2e2847",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2025-02-04T12:05:54.572Z",
    "updatedAt": "2025-02-04T12:05:54.572Z",
    "event": {
        "completionStatus": "IN_PROGRESS",
        "targetResource": {
            "id": "abd14e",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "e7992c24-0df6-4c71-ad38-6950f4829290"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "410e041d-4e40-072b-29db-f6499c81e9a0",
        "name": "Default Risk Policy"
    },
    "result": {
        "level": "LOW",
        "score": 0,
        "source": "AGGREGATED_SCORES",
        "type": "VALUE"
    },
    "details": {
        "ipAddressReputation": {
            "score": 0,
            "domain": {
                "asn": 766,
                "sld": "uniovi",
                "tld": "es",
                "organization": "universidad de oviedo",
                "isp": "entidad publica empresarial red.es"
            },
            "level": "LOW"
        },
        "anonymousNetworkDetected": false,
        "country": "spain",
        "device": {
            "id": "Id-4fc35854-7612-402f-a2ae-b3071e00898a",
            "os": {
                "name": "Mac OS X"
            },
            "browser": {
                "name": "Chrome"
            },
            "agent": {
                "id": "C23BF4F0-A3F4-7B18-93C3-844B0C02360E",
                "os": {
                    "name": "macOS",
                    "version": "14.7.3"
                },
                "loggedInUser": {
                    "name": "stevesmith"
                },
                "version": "0.1.0",
                "name": "mac-2D90R1MD",
                "macAddress": [
                    "14-7d-da-0f-71-5e",
                    "5e-59-41-5c-ec-e7",
                    "ac-de-48-00-11-22"
                ]
            }
        },
        "state": "asturias",
        "city": "oviedo",
        "impossibleTravel": false,
        "ipVelocityByUser": {
            "level": "LOW",
            "threshold": {
                "source": "MIN_NOT_REACHED"
            },
            "velocity": {
                "distinctCount": 1,
                "during": 3600
            },
            "type": "VELOCITY"
        },
        "userVelocityByIp": {
            "level": "LOW",
            "threshold": {
                "source": "MIN_NOT_REACHED"
            },
            "velocity": {
                "distinctCount": 1,
                "during": 3600
            },
            "type": "VELOCITY"
        },
        "newDevice": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "DEVICE"
        },
        "ipRisk": {
            "level": "LOW",
            "type": "IP_REPUTATION"
        },
        "adversaryInTheMiddle": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "ADVERSARY_IN_THE_MIDDLE"
        },
        "trafficAnomaly": {
            "level": "LOW",
            "type": "TRAFFIC_ANOMALY"
        },
        "suspiciousDevice": {
            "level": "LOW",
            "type": "DEVICE"
        },
        "userLocationAnomaly": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "USER_LOCATION_ANOMALY"
        },
        "geoVelocity": {
            "level": "LOW",
            "type": "GEO_VELOCITY"
        },
        "botDetection": {
            "level": "LOW",
            "type": "BOT"
        },
        "userBasedRiskBehavior": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "USER_RISK_BEHAVIOR"
        },
        "anonymousNetwork": {
            "level": "LOW",
            "type": "ANONYMOUS_NETWORK"
        },
        "trustedDevice": {
            "level": "LOW",
            "reason": "PingID Device trust verified successfully",
            "status": "TRUST_VERIFIED",
            "type": "DEVICE"
        }
    }
}
```

---

---
title: Create Risk Evaluation (using targeted risk policies)
description: This example uses POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations to create a risk evaluation that processes the defined targeted risk policies before carrying out the risk evaluation.
component: pingone-api
page_id: pingone-api:protect:risk-evaluations/create_risk_eval_with_targeted_policies
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create_risk_eval_with_targeted_policies.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Evaluation (using targeted risk policies)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations
```

This example uses `POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations` to create a risk evaluation that processes the defined targeted risk policies before carrying out the risk evaluation.

The body of the request specifies that the targeted risk policies should be used by setting `riskPolicySet.targeted` to `true`, rather than providing a risk policy ID in the `riskPolicySet` object.

The selection of the risk policy to use for the evaluation is based on the flow type, user, and target application, which are provided as part of the `event` object (`flow`, `user`, `targetResource`).

### Prerequisites

* Refer to [Risk Evaluations](#risk-evaluations) for important overview information.

:::requestmodel

For complete property descriptions, refer to [Risk Evaluations](#risk-evaluations).

| Property                    | Type    | Required |
| --------------------------- | ------- | -------- |
| `event`                     | Object  | Required |
| `event.browser.userAgent`   | String  | Optional |
| `event.flow.type`           | String  | Optional |
| `event.flow.subtype`        | String  | Optional |
| `event.ip`                  | String  | Required |
| `event.session.id`          | String  | Optional |
| `event.sharingType`         | String  | Optional |
| `event.sdk.signals.data`    | String  | Optional |
| `event.targetResource.id`   | String  | Optional |
| `event.targetResource.name` | String  | Optional |
| `event.user.groups`         | Array   | Optional |
| `event.user.groups[].name`  | String  | Optional |
| `event.user.id`             | String  | Required |
| `event.user.name`           | String  | Optional |
| `event.user.type`           | String  | Required |
| `riskPolicySet.targeted`    | Boolean | Optional |

* :

  :leveloffset: -1

#### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

#### Body

raw ( application/json )

```json
{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "targeted": true
    }
}
```

###

#### Example Request

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "targeted": true
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""event"": {" + "\n" +
@"        ""targetResource"": {" + "\n" +
@"            ""id"": ""{{targetResourceID}}""," + "\n" +
@"            ""name"": ""Jira""" + "\n" +
@"        }," + "\n" +
@"        ""ip"": ""156.35.85.124""," + "\n" +
@"        ""sdk"": {" + "\n" +
@"            ""signals"": {" + "\n" +
@"                ""data"": ""{{signalsSdkPayload}}""" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""flow"": {" + "\n" +
@"            ""type"": ""AUTHENTICATION""," + "\n" +
@"            ""subtype"": ""ACTIVE_SESSION""" + "\n" +
@"        }," + "\n" +
@"        ""session"": {" + "\n" +
@"            ""id"": ""{{sessionID}}""" + "\n" +
@"        }," + "\n" +
@"        ""user"": {" + "\n" +
@"            ""id"": ""john""," + "\n" +
@"            ""name"": ""John DeMock""," + "\n" +
@"            ""type"": ""EXTERNAL""," + "\n" +
@"            ""groups"": [" + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""dev""" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""sre""" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""sharingType"": ""SHARED""," + "\n" +
@"        ""browser"": {" + "\n" +
@"            ""userAgent"": ""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicySet"": {" + "\n" +
@"        ""targeted"": true" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"
  method := "POST"

  payload := strings.NewReader(`{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "targeted": true
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
POST /v1/environments/{{envID}}/riskEvaluations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "sdk": {
            "signals": {
                "data": "{{signalsSdkPayload}}"
            }
        },
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "targeted": true
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"{{signalsSdkPayload}}\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\",\n            \"subtype\": \"ACTIVE_SESSION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"targeted\": true\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "sdk": {
        "signals": {
          "data": "{{signalsSdkPayload}}"
        }
      },
      "flow": {
        "type": "AUTHENTICATION",
        "subtype": "ACTIVE_SESSION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "targeted": true
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "sdk": {
        "signals": {
          "data": "{{signalsSdkPayload}}"
        }
      },
      "flow": {
        "type": "AUTHENTICATION",
        "subtype": "ACTIVE_SESSION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "targeted": true
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"

payload = json.dumps({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "sdk": {
      "signals": {
        "data": "{{signalsSdkPayload}}"
      }
    },
    "flow": {
      "type": "AUTHENTICATION",
      "subtype": "ACTIVE_SESSION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "targeted": True
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskEvaluations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "event": {\n        "targetResource": {\n            "id": "{{targetResourceID}}",\n            "name": "Jira"\n        },\n        "ip": "156.35.85.124",\n        "sdk": {\n            "signals": {\n                "data": "{{signalsSdkPayload}}"\n            }\n        },\n        "flow": {\n            "type": "AUTHENTICATION",\n            "subtype": "ACTIVE_SESSION"\n        },\n        "session": {\n            "id": "{{sessionID}}"\n        },\n        "user": {\n            "id": "john",\n            "name": "John DeMock",\n            "type": "EXTERNAL",\n            "groups": [\n                {\n                    "name": "dev"\n                },\n                {\n                    "name": "sre"\n                }\n            ]\n        },\n        "sharingType": "SHARED",\n        "browser": {\n            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"\n        }\n    },\n    "riskPolicySet": {\n        "targeted": true\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "sdk": {
      "signals": {
        "data": "{{signalsSdkPayload}}"
      }
    },
    "flow": {
      "type": "AUTHENTICATION",
      "subtype": "ACTIVE_SESSION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "targeted": true
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"{{signalsSdkPayload}}\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\",\n            \"subtype\": \"ACTIVE_SESSION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"targeted\": true\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")!,timeoutInterval: Double.infinity)
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

#### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/f46ef994-e5e8-4881-a8e1-17b727cf249b"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "event": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/f46ef994-e5e8-4881-a8e1-17b727cf249b/event"
        }
    },
    "id": "f46ef994-e5e8-4881-a8e1-17b727cf249b",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2025-04-10T11:42:19.263Z",
    "updatedAt": "2025-04-10T11:42:19.263Z",
    "event": {
        "completionStatus": "IN_PROGRESS",
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "flow": {
            "type": "AUTHENTICATION",
            "subtype": "ACTIVE_SESSION"
        },
        "session": {
            "id": "01ddc236-0698-467a-919e-40ef0d47cb34"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2",
        "name": "Score-based policy",
        "targeted": true
    },
    "result": {
        "level": "HIGH",
        "score": 0,
        "source": "INVALID_SDK_PAYLOAD",
        "recommendedAction": "DENY",
        "type": "VALUE"
    },
    "details": {
        "ipAddressReputation": {
            "score": 0,
            "domain": {
                "asn": 766,
                "sld": "uniovi",
                "tld": "es",
                "organization": "universidad de oviedo",
                "isp": "entidad publica empresarial red.es"
            },
            "level": "LOW"
        },
        "anonymousNetworkDetected": false,
        "country": "spain",
        "device": {
            "id": "Id-4c0013c4-5739-440f-91f4-147f460dd2ec",
            "estimatedDistance": 0,
            "os": {
                "name": "Windows"
            },
            "browser": {
                "name": "Chrome"
            }
        },
        "state": "asturias",
        "city": "oviedo",
        "impossibleTravel": false,
        "ipvel4": {
            "level": "LOW",
            "threshold": {
                "source": "MIN_NOT_REACHED"
            },
            "velocity": {
                "distinctCount": 1,
                "during": 3600
            },
            "type": "VELOCITY"
        },
        "ipvel3": {
            "level": "LOW",
            "threshold": {
                "source": "MIN_NOT_REACHED"
            },
            "velocity": {
                "distinctCount": 1,
                "during": 3600
            },
            "type": "VELOCITY"
        },
        "userLocationAnomaly": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "USER_LOCATION_ANOMALY"
        },
        "newDevice": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "DEVICE"
        },
        "deviceManagementPredictor": {
            "reason": "Not enough information to assess risk score",
            "status": "NOT_AVAILABLE",
            "attribute": "${event.isManaged}",
            "type": "MAP"
        }
    }
}
```

---

---
title: Create Risk Evaluation (with custom input)
description: This example uses POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations to create a risk evaluation, and includes a custom attribute as part of the input for the evaluation.
component: pingone-api
page_id: pingone-api:protect:risk-evaluations/create_risk_eval_with_custom_attribute
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-evaluations/create_risk_eval_with_custom_attribute.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Evaluation (with custom input)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations
```

This example uses `POST {{apiPath}}/v1/environments/{{envID}}/riskEvaluations` to create a risk evaluation, and includes a custom attribute as part of the input for the evaluation.

Custom input is provided directly under the `event` object. In this case, `event.isManaged` indicates whether or not the device used is a managed device.

The risk policy used for the evaluation includes a custom risk predictor (`deviceManagementPredictor`) that assigns Low risk for managed devices and Medium risk for unmanaged devices. Refer to the `deviceManagementPredictor` object in the body of the response.

The example also uses the `sdk.signals.data` field to provide the additional risk input provided by the Signals (Protect) SDK. For more information, refer to the [Signals (Protect) SDK documentation](/pingone/native-sdks/v1/api/#pingone-protect-native-sdks).

### Prerequisites

* Refer to [Risk Evaluations](#risk-evaluations) for important overview information.

* [Create a Risk Policy Set](../risk-policies.html)

> **Collapse: Request Model**
>
> For complete property descriptions, refer to [Risk Evaluations](#risk-evaluations).
>
> | Property                  | Type      | Required |
> | ------------------------- | --------- | -------- |
> | `browser`                 | Object    | Optional |
> | `evaluatedFactors.status` | String    | Optional |
> | `evaluatedFactors.type`   | String    | Optional |
> | `event`                   | Object    | Required |
> | `ip`                      | String    | Required |
> | `flow.type`               | String    | Optional |
> | `origin`                  | String    | Optional |
> | `riskPolicySet.id`        | String    | Optional |
> | `riskPolicySet.name`      | String    | Optional |
> | `sdk.signals.data`        | String    | Optional |
> | `session.id`              | String    | Optional |
> | `targetResource.id`       | String    | Optional |
> | `targetResource.name`     | String    | Optional |
> | `user.id`                 | String    | Required |
> | `user.name`               | String    | Optional |
> | `user.type`               | String    | Required |
> | `user.groups`             | String\[] | Optional |
> | `user.groups.name`        | String    | Optional |
> | `sharingType`             | String    | Optional |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "isManaged": "no",
        "sdk": {
            "signals": {
                "data": "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.eDE="
            }
        },
        "flow": {
            "type": "AUTHENTICATION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "isManaged": "no",
        "sdk": {
            "signals": {
                "data": "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.eDE="
            }
        },
        "flow": {
            "type": "AUTHENTICATION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""event"": {" + "\n" +
@"        ""targetResource"": {" + "\n" +
@"            ""id"": ""{{targetResourceID}}""," + "\n" +
@"            ""name"": ""Jira""" + "\n" +
@"        }," + "\n" +
@"        ""ip"": ""156.35.85.124""," + "\n" +
@"        ""isManaged"": ""no""," + "\n" +
@"        ""sdk"": {" + "\n" +
@"            ""signals"": {" + "\n" +
@"                ""data"": ""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.eDE=""" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        ""flow"": {" + "\n" +
@"            ""type"": ""AUTHENTICATION""" + "\n" +
@"        }," + "\n" +
@"        ""session"": {" + "\n" +
@"            ""id"": ""{{sessionID}}""" + "\n" +
@"        }," + "\n" +
@"        ""user"": {" + "\n" +
@"            ""id"": ""john""," + "\n" +
@"            ""name"": ""John DeMock""," + "\n" +
@"            ""type"": ""EXTERNAL""," + "\n" +
@"            ""groups"": [" + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""dev""" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""name"": ""sre""" + "\n" +
@"                }" + "\n" +
@"            ]" + "\n" +
@"        }," + "\n" +
@"        ""sharingType"": ""SHARED""," + "\n" +
@"        ""browser"": {" + "\n" +
@"            ""userAgent"": ""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicySet"": {" + "\n" +
@"        ""id"": ""{{riskPolicySetID}}""," + "\n" +
@"        ""name"": ""ExamplePolicy""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"
  method := "POST"

  payload := strings.NewReader(`{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "isManaged": "no",
        "sdk": {
            "signals": {
                "data": "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.eDE="
            }
        },
        "flow": {
            "type": "AUTHENTICATION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
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
POST /v1/environments/{{envID}}/riskEvaluations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "event": {
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "isManaged": "no",
        "sdk": {
            "signals": {
                "data": "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.eDE="
            }
        },
        "flow": {
            "type": "AUTHENTICATION"
        },
        "session": {
            "id": "{{sessionID}}"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
    },
    "riskPolicySet": {
        "id": "{{riskPolicySetID}}",
        "name": "ExamplePolicy"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"isManaged\": \"no\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"R/o/dFNiakI1MtoQAymdsuqZaAWiS8MYR8VJwZVT9LSAUYdkM9H54HOrpvx5SDx85yPcy8x8I8KltFJWDD2oDxYjotS9/Dv9ky4Ebpbp8b37lqcOTyX0/7z4jZuVlXuimcTYwV0ELsVQCPZ8cRNmQB5lbuOCWj0mDWBGKPGf71MWnGxCmxgzUy3nryqJyIu2KZMOD12BzjG7pEgITgT3t/EGGioSeZK4lIlwNVq93VBl7sXUrOAWljsq2Ck1BZ1lpAPvbZ2I4OxZG7BonZV8E9lPk0XE1pf5C754RIVqDvMs/HOao6eTzUWxFudK9DVlwvK0o1nslwH57oLtxY2Yz4OBfDkiSz5VtnsBEcmWCzktNEqI0JAEgM3lDS1NisCdMxW+R9YYxhXaDP5OUUAri3aWJoMvmSBTq6rGGq9i/Q4oSq12OTZbInhjcEVTYW8BtaQu//Z6/zyuk4R3zTDM61HSkFa+rvyY7cr89tPD1qZbhdTqafGK0Nxy7cfTY4fyjZpop6EzizfgnGyANY7J29rQHGdpPdJhl82Dhnu9sXboMcGNZbHDJ7inzbIipYYYGs7jvXHXfUByvaYqVrRGrYd5H8MX7UFgBN6614SywJIyVJl7FX0Nvuvyt8dG7R2d01QiyZkahvJ5u7eRKQNIgfcS0ZylN9Vyhc+p9F66IkqDF6B6b2kPlpw+besA/PLxtRJi4jDWd44oLxPR0EAtB6urwGS7bSIDdnhwD6Fm9FGXMfzHQOc2ZY3anehMXgEe5uqFOUGjyavyNpy+zWnGNncwj3hAIBVaFv5WpboKuIi3lj28MoTXo2hNoZvlkNHdWG+iVXJorR9IfgRhyRpm/4yF/S0wnKA/P12o/S2Rm+09Gx5dG2No8gMXwp930HGpebtYu8+YyfVQYI0/5vopDuYG1ZRknj/7eXSAXydUw7B0KLDtqOcAU7Xs6xyROpM1MdHdJaGU9wYeIe0GbXzpSI2hy2UgxgESTMTHHlW+7D5Ys3HamjaDZfTnypw6fIVTJxi8wLuDM0rSO0Pewinm2JX9gpNVeZeB7r04FuFegFvzwgvaHPruqWg6s5Nw9pkhsBAO5H7deST6PVRymCWBt2HewxzGX5mcfnAM2fyaKKjvlcBRw1I8K5Pft3vPJwEW63aFbhX0GUGNmN8eCV8epqpRMkQLDzW2+BsFt69DIWTf3tWwxXjwMiVnF2JayKQ4nkyfUQ5ss04hM93hM5Am9c8Pw7VS4vP/q0aT2qunAzec1jtqc1xwzuG31jhMhXpZfTmFjzurk4wZ1Wl1SLx1lDM2xTc/Hfjrd0oXGFVaar29CNItEM/1/aUAzzOlTiwBufmSf3WuKPLCwh3VSieVxRCjKtK6FTvdJBTQrSpe/MTlTLHHz9RhTSsDp6sU8HQD7Jul+G8z2uk98gg2FK1U8LODTfJ2rCf6Oka7bcbWZ+bH3AbvfA1U1Tb9BMfPlIdu2HkCxD5v0gOQZSyhcE6CRiCA1s96eUe7fp4MzsDge+Uo4XRbcwd+AFJ+eN4NmQaaa5tJEwukcTrXoLrEkBLw3hpCMZJUhzqOlglcSrqOl7dJbKpLcG0b/ULcT7Xj+y501yXS9OIzyzgHt2uFXwI7+8x/vnpU8RNggVhErziq1KgghIO5cpZTd1zbcokRGdQ9t+QpXixDkv0AfnqXCr2IofBsb0nlzvx5q6SKA0MJAZkVQfhBkYzVnFkpzS4JOEhOSunxJXRxoJHnTVvgOf2AW+i8IG93GbBD30AoNaDHZmVCl6CKFkvds/M3GN8PMzAz1hGTLh65zzu2W+Q1EF1KztZv+aJ1orchgdvzwYbDoLFkPesKd+zR5as5JV6IuwR4vFBlEamVsrCPtyeMayGTJnnNdncsFKKwjaSnmx7UTQowEYpSfVkMjsEPk2hiPx/8BnZcbKbEMers9VNMgb3NL/B5Z9IqHzPszz/5zmyjBuHIH0qc2jL5bwXKeNJPaZxC7Fr5ufq+k1lQrVN6fSgx7xkzD4xTVA4kVgf4QCitOWveT4UVltDVeBGgyIhg+IGExd8G+6U6LmCYnWvISonYogrVmKR/nuG/dGK2semuslfcv8GFjG9M3cuMppzkkyfwXwoYzwrA3un1cwV3sdD3X+Tk+t46v5ha0t8LwGEVFvQh8GRDfCaJKyXHdgXEoltA225iPMHZEVI83mqkPbHrukQokJvfpJrvi8ql3mhyd/4bKzkQuV66FJhwksC9IqPr+tmoJqN331df4WZEo3NSAc2OXrOO2ZETzNCKHl30cax+wPlJB0l4ED3MoieIyC4NRg2Mc1R3cB3B6ugCa9g/WoFg30x8hekWzMQI+yr9TPwPUbl7fd7riA1ZGJ7e8A3PmWd07/F6Q+IdCzSg24tERWPDrCgGXDqsQw//nAjiW7i3BrmeCFsC/SpWtb0G6ABbjkjLnhBHH+tGir9PYdJx5pfdC9T6tgtskHY0PRxDo2giXvNxE2NTZuM85rmoRevczX184NvjWNE3gpfFxopvSAP8H0M5KZkAxEkUfrp8TujteUtmTZ6YjLFhzgzCENQvbKPp4cR9WJKPnE7vu55J1vXIrICJhUmiPDDmQ796Rg7RVHJ0lrBzS7tVqz0/c/prbVN2viuiajAd0ZNxXIQxGZ2hBU0yOnlwAtnmZjGsdKnnV/Y7Wc/j7sjO0Fi3WPX+a8LVDOH5kKfok3Oab+bWPMEwWkYOPLCznLmgwTMjqZ1/nujOUsAVcPvVbrcW38WAolT3DXdW6jctwK+0yCFi3kNB07wPNyLYnV0PN2Hy16dlqYtb/utCUqHfF3TbRCsIxMgNbvrxtHHlb9dX5t37hNa6Lc3Sh07etMuedqtPpfLUNAcPie6gW7QFfoNuGrcV2AAXS6W6UKMF8bWqyxXrsOKdCRmhvy+d26kSeJNRsSoGWYeCe8IL+6KrmBz/Nlvvzh4wjyzGcqBfpyQ2q51ktHnUqucdicZCOLKjSaR24OsqIH6/eecQQHhTKnMidPBLyPxEfMp15GLhYWXReX2TEOZUdtgrpy1BUDmq+fJIR3AzLcaUow4myvrLxsi+qoK5Ths0zJrpF4sJYJGlHNjCDennCc9vYY0ABEm7+cHNWtqXVuHNnm9BV1KyuYmDdjuqbObb557t5AIAvWVxKTY/1B0z8/1f/V6KPNaLlCimwPWYpycqp/ENy/I6GHSjJhaoqGtyuT1EZtMJjqAG111oGNlNJza49+W3V7fX3sbHHOmcXooAGUtrjmDKg34urirscesn44NSMqr1cABiLVCZhitHbRz+wWqFj3Fu/U6ajc3NcebCPGWHP5R5+auQyrHaz3hfG+fNIHrq3llS3JagIQFpFYWG5GbNTapUVOecBVkuuaIV0BiZjQlLtT/G+w5H/N0UjB+fpJUYf5J+8An24n5iLcUMgL9dYCFynBDcQCRWAXpTjwvncAlThwmTUgft9sBLRD9Oa/Sb6c25u96YC3fIGSvnPqfH8yFpJObuZB+MNxEm/b0/EYFXy+XxJ1J9VEAX886DC3ejZJ+kKrFGhoLstIstlfaVwxwfKnpEvxvj/Y4avhH1u+WKPX4FSdgw+ErybvyKTjjoCzqPvGL+KUQKW39kVKSV5bogVxIY9BBXvPqwNwbopap2f2+eRDq5bfb0aAloSYFDfyPfhhIdfSmLnhAsrgZmEan4eSYRc4DJKl9L2AXFFC3SaHIQ1rxiv5OIl9KisyGwoDT0uW5KjJF+gp0P9hSQ5LnJn8utJj/XkDWYx9TFsqS7GmMIbaSYRSf6jkY497hBTSw0ELRx91aJay4FtwLEmz3PV4+1lSFYipRxQmmy4aRZgz7axKAq2c5tu/nR7Jr+u0rcYAesalHPdHQBNGv8q3goLh5I6axIw5ic2yk6eud8BFlzCi2t/79mZgcBF92dDIIFni2wvtKNKyKzMO80OaEUqekatDF8iQWoaWzDaWcpc6656CnqHcGdGwjdiqxsITkSkhPW5/IM+s7lE3nGXPMzPMDhgBCv8HPOT0NKm6Lqv3LLkCbYDpeZQmM5OVh/uSW8iPw+YtbUiry7eGs/dvAwKMmquAN5iABWA4etYOT7U/SoO8q+pHB5FVObyqG6nKnRSbhkgcHuPWxyupOA4/IwL5E4+inBukgk9ZsDXszQf0Vi0hIH/80aXCvrjOHRDtgmijimF6Vvxi3ToThJTMn3hZT6xc8f5VObOif/6As9Q8NMjIhFTRUUWokHA33zFaEechgPHo/j05ppXifMhVJMpr/cN0wRDj3sNESmg63/PLM9Phl9aE8Ga77tzvBIAUXYXKuGTynXtsqIgOoGOyzC+NE6TVDCJ5TFj4Qunr+5/eLXKqV2BRklpX/pgGHjKDQy8KKL+JYRSNhRDbnkmHe6M7bgDgk4j3uZaejG0LPd0ztRmtQfLgGO8BiZAqrQ+8Udrv3jftXblH+1JLvg5PYolV9JAHRapADcor5V5ujMCV7+h3e5gUuDTifc5a/EJjL2qeLIuu4K0kpwg/da8Vt6/Nv1mtEKTUFcQLYX7Ot+92XpMQyDtAEw7NRTekHFjxRwxP14gVjfz2BP4s2A4soM6PqA+B+2O3Nz49RMxcsb1vJUNsZuukNScamH5URj5oQf+KadzwkeTnciWuMfmPNdKjIUxr1wfLQHEuEpYJyMfqou2BsjI9UeLGW2jj6kZvljzCxVPP5ZV3UUM2+WC1Jxs0hJWMIbeUXEyt79JWcZD5r/OegbwhJMzHEfv6frXw2MLjF5ugK+WLYToQLWz4R1COS/N6C3Tlg9qqjaX+FlN2apV2ZGMNGYky0p52CyckWHKmww2y55kgXYU2Ea0vgxeE4Mze4R9wqFaZvT/vST9iWpKwbllu1WJPOUsSr3idKVgUOtWVy/nWhptNRG07ErhN1HzVLCXlD2rHx8mMpzaQ9AK3CtdKYY1flzZM80Rdc1GPHCiM/SkAkHkqtmT/kNPK5jWVlWe6iT7J4o9HzEyWEdyaA6srrL1yMF6hoHQPwwTFCJs1XlRJkw/hGddb58yHwBHS0gnR6zuaJX0PGowz7As+3tu8FWH+dd2zOrQ2TH1RvsMNZJP0AIhg4rwa/rw817iirc/+ymIx8EtsGqYMPjcWC5oHgiNP8f5TjKiwzsFekJ30LUPYN84Qm7KcJdoFjo7GQw80y3ry9yeNQozDMlFNxaMwtfNOPJraEqlqk672sjV1H+Fl+HdXql/LS2TMSOI19hatl7AairodQkEVjLorBfTC2ylL3CbqlmQNPELnT7qOC0Lts4gwDa6OdWj8/h2vyQyPhlY4fuFMebwAKJ36qBEpTnVPTUZP+8IXtIOwUqwxcWZw/tJMSnJnwL03q09BfID6TivfJ9u3rdphoNRZUI5/Ubg8P+56ffnYEJ+VEVsN66DQOzmhWeCK4Hc3Tm13g20bWl7jEoQWD0d3k0se5MP/RRF1J4P61aXn8jABiq99YbhEG1OYloJQJm+eru8n3GtcuaHVAaBshdlDhUu+8dOAP8UIHLSRxdqF05U8b8ujBry3SCvJhoBMjuMbzIkH1uz2Ld50WxzwJblOP7WUE7IsfZVJyTVP01AIsHAK7HBBSu5zhQuiPxz28FWxKsGX9GyZ+dYJ+txYzq0nIJiZ0+bsxXgjfZnp7CvonPn/VrVYTE6FCi73OMXdCSPZLUyWMKWyRQkU/yGWFtkf3NZhI6PP1a8LiVc8kjxHsMD9z+fWdyTTXsXJD45uzXaNo69QYSfJmmAoyJyxkolXxvTZQeiW9JGfgTKa4EaNnqMVRxyYgN92RZNaAqEIijPy9OefdVGHATuPSzn+R6XkxzRDkMoK7uHIv6fWOocdGTXLv9A+Vxa5S2ny9dJ/SJ9VxkD4NfdJNqkZImu1kUyOJQzolITdj5ZNC5NEVqIb/JALfLOgpHjYCk3oDHqI3ovV8ZgsVcZK+VUgdlkJ/I5QRTTxGTmhb32WSJ3ZzZCcMfBNl/PpxxAgavj5oIR5hwjDEiHOhJhyB/Tb8MjdKrbhD8HVmme27XmoyrYMuKGxun5vB0vHzk6wbIP9QIR0XLaRL3LbmAZWEoFdr9j8iP/0ScUTjIFMsvNkiDpWz/TI4Yw549lJ6YFJfYKsmpPSnrLQQZn5uYSLFiWSIy9fW4GmIcI0qDfWiKEogr1EYVHr7TZ3mFU26AdZh2uaP/xsU5lTOpX7kORqF8MBmBx5ZKCVquP7OkV59JIZz4VhirL4oiW5SZJ6pVi1RLpnQ9rnze3ABB0yQFzmbeWgokHJVHzUpyLwX8AWVvqDpJhXA8KWvdhPIZi9rqAMX+RnLlwClKegrICT4HKYtuVN2M1mvEPc7lw8lgyGOIdUsgwak1rx/PO/Iph/7AJ0Xp3HlH7MUDqzqS9gOYBVDUB/mjlVo8UHcdy/k4Bsu/gUy70198agLe7/8ZgyEiGaXnaAPPdhztuHYut708rYdwqjKYl1Sl+ULBjY0ZLbsxg/Y4p1asRI4xdTqZifrgoQWa8B4VWjJLV19xNPJ8CdwMm3IanOHPCBUrpjuULyTXvvAJ2ZwZe/fJYeADzho3aUZSaLewX59Pb1VvJ5JtKjcrxN+hROFtIkQqlflG3tUX8miAoaASHtp6c09TsFT7DGWIYMSjLAS8gBZnP9KJQK14UQ+9KaDR/dQMLxaE3V6FjcgYUtyRC/2+0+xJQFTRGwy+9/pcBkvLDnivRoKSGZLrCdr6C9TMv8x44RQQ8oQFM/1ExSndaGsdDzW5e8UcQdG4xsvYuFPqI1TLAJKgklr/+KRFdNR0imGpTJ98mtWLBK3UxoMoMh+qUsqUFP9E1bdc1+mB6taJuSQHtp4w/MCz22isvM7xSpMYjpfp0Q+jPksMpOh23fHYH29FPbbD+57UES/9AYmD0/5TUIcIjr3QFn2aZWj+qnKVnJfGGhmbdY2nF0gkZ18Ps94mFHYEF4U60zwrQslBmOKpqen2RuTYWDoZGpD9uD0yFrh+n1yV/t9Ao/hIqLON87X3nMnghcO0xDgfRtcR0PqRfayaLXc20YygS/1Yy8QjHHs2jSC7qLAgPdWGHtQOaqLVoMkmsT5K78LeSR5jp0StlgO0aqTDjcJBjfQJHtFUvUNGbOrWDIzw9SUkU0gkRpc2MWZD4rYcD7396v9Ou4VmjCFzfym0SM4W7SJZyQY+Hxa3Xm0UQQndjAouKOBwUb/FKPq9N+zgkjXApzuvmzEYyC8PxkqUB8ZywSMOivHvBp5qOwF4KkxmHOkm0+sWGN9f266ia9XRNkpWM5AoJxeoDinUqBAbBnhsqhaq6Tn2mMbKVdAQ6T1XgdP0s2QI8Dl1jwmA3E2DWHD65n5sLgWBzP2MsmIGvUIqz/iOYI9VKcOpWVxzL8ID0yi5nxj9PMR4cPVzfr2pBSiCRDU2XhRrxZ4EXgPgjCJzOul0KfGIgvyx+uUre8vetZ2I3bhoJhQeRsO+2Ud5n16FwU/8tQ4fk3zTaXijU+JyOlDEIre+PWisNyFPoARD1fBlq8KPYvmQPxBZ5eBuTJooc8dSipJl05yl3OzBpslHJ7lTx3l8CokELESeV89Dt8KCNx4XemxN60h/siT9IK/Zv0k6VinNWOb+4u+2/CncwM2gmJvCjJSaiMqiJrZ/tgVZuhuaow8Xl/Q/84jELxpX1Y67xw/kn2U5itXLugT5o8jo3ZG2UJlTlrRaBURdk6rEh81iV/wfLRW2DtRiRa3Av6z3yPiFeUtgNPYBDahgonBJosjLLlLnU0cB92oS89UJE1utcwqMp0pUXAId28qg2j5Q4EqqElpc+HRmXR3GhponT/5L56Q9CYrYTqgbUxvheXmV8UVKipssvQlejGgFHl1sqgyVcJBMGNpHfRvlSN7uTW2Z1SmHCgZkeWW5M1p1WFTUe1ikxmx2MUBJ0aZcMojqti0/1855OkVxXv71T2SpYlYkWIpH1eLV8f+zv5OJZPkIrPANWzAG456JwTXpkJsHIRZiyKGijKqGOi+DcT/jdvFkIOu9Fv3Rlf1CtITgjv5aAIU/RqxUEoqnXt6Gj4tDzFT3GLhJHi6PqeLTNCGDY/hP2abC708wvFL9qEHtSf2ebPgUTS4kc/AzociVa8YVncjgPQfYuKeUHwK//F6g0+DgL4tj6/s+8JdqPvJZg5CBZjD98Vp2RdoU7AsFnccsu/LQ4Knx1aKTL3su//9DK01ebc0w5DS1X0kZPIqTMaFFWSE6Lk75gcCob8OvqJlFa2aP2vERh2jjOonrs7H/a03RfSt8QhKXKLZaFKCu8EmVTITVL0a4Hkwn7XH9DYMUCD4SeBX+QCyE9IfL22monjoYOZwSVwMzTZNld/WMEWYeIkoBOUqvysPd4QZfkZGw9lbwf45PRJ3QG0AIoCwJqB//UL4g8MIBZlrWEZasr4OR9ksSfhxsOpLGQHH6JHH0Ko6JeiGVN9XDfEQ1Kk4Efcvvymp9Rc/K3rwYamhy6AtYOF5aSSVtMMwN6IuLjIYCJxMdG8lhJ6B8dCPoBOHhlrsGgvio6CKKwznGEYaGJAFIEifqwCGTVNDlAsSn57PRoPD4aDSox0z14MFwzMj3CqNVwApqoJAIPlluiV/sg4V0GEGTM/X1g7x+ys5pscxizdup/rlVACwP1AP15laXiQruAS2BuOXjPKdScm3L2LB7NYeKfEkiiZ6hLWJKDBMwPmH1BnQX7JMZ3BMuE8LJnHt08dFe7L7DircXp7oaMCgdVuc1Zouk4e2PvJKWdGeP+b74TU+SLOWEFJxKIhvFT+HVXW7z5VEDxl4hpBoZpf7OkOznVXBkIBgvtVAD9E0aRwA0d59R2oqDbtQ7bXSFAsuLKKd+V9k6/blkblZMH211oMVpE04ZC8Lg59n24UQj8pzJkgDNjeYBiHMrPmthgNEDnXewYh34gTiQgONpWotfdOm2T1qce/3/okXtR72cmLtbWFQynX1IuOuMDzMDWzI0dTsAMCmrpJBbqVjpeNCoMY2Zrg6WXUwYPJSEiGXdTvk/ifIuxGZZ8hbruI3p9O4p9M0+H0jqDaTbpIWgbjeJHJgncMQc6DfAasfy7oI4/CsFkjQCJTWOF1HfuSKVb1FlsLMkYY6umg1ilP6/o1d+3N2/Xv9LIxzQPGVk9d4//4H5x+w7ON8Nda7XNcXhFbnMXRM6CDQbRE0DtYvsJKXMM50zXCvFIEoUQt6XxKPcOKDWrtxKZBMieYkk4FoDp1YUfyQJUvQfxekTRLXIEZqbzQciLMLzhWmh2TL70oq+N03AGVJoib32+J2LoekCbUxnOKtSUA23WBkzGaHGq3i1GOEuljEU61jNKX6YtbpMCPHTol4totNbZhPpTWVBXPY1J1Nv0RxS2R4Ieb0fjKI5QziOBEibBIMao1FmxKX0YvydsX1NastNMave/CWKkZkfvyu+/awnVOTwfKskRvUWxH8PMoBpFJFoo3NNn9d81UV+RE8q/fVUUAuNFdbc/mb6WwW4x2YXvBQwY8Ov1RX11D6XBWIE7ih36vESGc2PHEB9qZNpF7aZoPC2GcmTdp9ZlQHrbl8QDujlw3KZdFceIbO3uTq9hNQmUbal86htMlGGpk+YQdz/ltsTUQx+9ay8haLfkcs0WyJM9fs3A+W4u3PdGdR8prx0ck/oc8CRgq4CZzoENj90L7UFqiHclncnwXW5TamxbZbV6ouGo8F4gFyuopVIwER+Fmq5NgAElBf/lGAwqSX7UWsZJWTG2ExMdIjlIioI5nhxzuqEMJeKhaTd9qyK4oANsq91XrLGR3FVSl0CS0JEW8UknWZH9ZB2zZ2EImxykUvLM1gxpeaQtHG19qu8Jj40JhpwJNj4R8aGa8EiKY5/kKmxBTIVLEstBf6a3W+QiBVWDYhw5RihHheE/rDHpKG7yV9W24cCKEQC99fIl7Qa68RGi8nnfSWgQ2gGLUnfG1ILKMvZ4eOOHkota4Kvdzrt11AHgMr78TL3iUZOPdcQgc1YRRZdtHLXz+8pSmqPUnAaHuHd5sFhC43v34NRAAVcGCzoVavvf6qgHTCV2MtRANrkWGAv8d9Dacx+pyv7kLdSQ4z3Jxy4v8kRm5lalBHRTdU/QAa4HonRb4CbFf7qN1+CRg20GDsM9fqU0UVgteFr4tj+LaIbhmW4X1sNKtr4KwTCZUfFFMDgq1dKjbLVdbnruVtwGCcuogI7NfoFt8vzsvmb860rm724rKqd/UpsCCo4mqi5P0DC0mCDtb7HjVqvaPKHpo2p6NbJ9MbpLJh+UVgrX5yLzousX3gs3x4X1HaYm5sld0eGFb8sKWJq.eDE=\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"id\": \"{{riskPolicySetID}}\",\n        \"name\": \"ExamplePolicy\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "isManaged": "no",
      "sdk": {
        "signals": {
          "data": "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.eDE="
        }
      },
      "flow": {
        "type": "AUTHENTICATION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "id": "{{riskPolicySetID}}",
      "name": "ExamplePolicy"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskEvaluations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "event": {
      "targetResource": {
        "id": "{{targetResourceID}}",
        "name": "Jira"
      },
      "ip": "156.35.85.124",
      "isManaged": "no",
      "sdk": {
        "signals": {
          "data": "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.eDE="
        }
      },
      "flow": {
        "type": "AUTHENTICATION"
      },
      "session": {
        "id": "{{sessionID}}"
      },
      "user": {
        "id": "john",
        "name": "John DeMock",
        "type": "EXTERNAL",
        "groups": [
          {
            "name": "dev"
          },
          {
            "name": "sre"
          }
        ]
      },
      "sharingType": "SHARED",
      "browser": {
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
      }
    },
    "riskPolicySet": {
      "id": "{{riskPolicySetID}}",
      "name": "ExamplePolicy"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations"

payload = json.dumps({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "isManaged": "no",
    "sdk": {
      "signals": {
        "data": "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.eDE="
      }
    },
    "flow": {
      "type": "AUTHENTICATION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "id": "{{riskPolicySetID}}",
    "name": "ExamplePolicy"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskEvaluations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "event": {\n        "targetResource": {\n            "id": "{{targetResourceID}}",\n            "name": "Jira"\n        },\n        "ip": "156.35.85.124",\n        "isManaged": "no",\n        "sdk": {\n            "signals": {\n                "data": "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.eDE="\n            }\n        },\n        "flow": {\n            "type": "AUTHENTICATION"\n        },\n        "session": {\n            "id": "{{sessionID}}"\n        },\n        "user": {\n            "id": "john",\n            "name": "John DeMock",\n            "type": "EXTERNAL",\n            "groups": [\n                {\n                    "name": "dev"\n                },\n                {\n                    "name": "sre"\n                }\n            ]\n        },\n        "sharingType": "SHARED",\n        "browser": {\n            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"\n        }\n    },\n    "riskPolicySet": {\n        "id": "{{riskPolicySetID}}",\n        "name": "ExamplePolicy"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "event": {
    "targetResource": {
      "id": "{{targetResourceID}}",
      "name": "Jira"
    },
    "ip": "156.35.85.124",
    "isManaged": "no",
    "sdk": {
      "signals": {
        "data": "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.eDE="
      }
    },
    "flow": {
      "type": "AUTHENTICATION"
    },
    "session": {
      "id": "{{sessionID}}"
    },
    "user": {
      "id": "john",
      "name": "John DeMock",
      "type": "EXTERNAL",
      "groups": [
        {
          "name": "dev"
        },
        {
          "name": "sre"
        }
      ]
    },
    "sharingType": "SHARED",
    "browser": {
      "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
  },
  "riskPolicySet": {
    "id": "{{riskPolicySetID}}",
    "name": "ExamplePolicy"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"event\": {\n        \"targetResource\": {\n            \"id\": \"{{targetResourceID}}\",\n            \"name\": \"Jira\"\n        },\n        \"ip\": \"156.35.85.124\",\n        \"isManaged\": \"no\",\n        \"sdk\": {\n            \"signals\": {\n                \"data\": \"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.eDE=\"\n            }\n        },\n        \"flow\": {\n            \"type\": \"AUTHENTICATION\"\n        },\n        \"session\": {\n            \"id\": \"{{sessionID}}\"\n        },\n        \"user\": {\n            \"id\": \"john\",\n            \"name\": \"John DeMock\",\n            \"type\": \"EXTERNAL\",\n            \"groups\": [\n                {\n                    \"name\": \"dev\"\n                },\n                {\n                    \"name\": \"sre\"\n                }\n            ]\n        },\n        \"sharingType\": \"SHARED\",\n        \"browser\": {\n            \"userAgent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36\"\n        }\n    },\n    \"riskPolicySet\": {\n        \"id\": \"{{riskPolicySetID}}\",\n        \"name\": \"ExamplePolicy\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskEvaluations")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/1dfedcd3-dc5b-4c7d-a18f-c2f751acec6b"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "event": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskEvaluations/1dfedcd3-dc5b-4c7d-a18f-c2f751acec6b/event"
        }
    },
    "id": "1dfedcd3-dc5b-4c7d-a18f-c2f751acec6b",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2024-04-15T10:15:24.141Z",
    "updatedAt": "2024-04-15T10:15:24.141Z",
    "event": {
        "completionStatus": "IN_PROGRESS",
        "targetResource": {
            "id": "{{targetResourceID}}",
            "name": "Jira"
        },
        "ip": "156.35.85.124",
        "flow": {
            "type": "AUTHENTICATION"
        },
        "session": {
            "id": "01ddc236-0698-467a-919e-40ef0d47cb34"
        },
        "user": {
            "id": "john",
            "name": "John DeMock",
            "type": "EXTERNAL",
            "groups": [
                {
                    "name": "dev"
                },
                {
                    "name": "sre"
                }
            ]
        },
        "sharingType": "SHARED",
        "browser": {
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        },
        "isManaged": "no"
    },
    "riskPolicySet": {
        "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2",
        "name": "Score-based policy"
    },
    "result": {
        "level": "HIGH",
        "score": 105,
        "source": "AGGREGATED_SCORES",
        "recommendedAction": "BOT_MITIGATION",
        "type": "VALUE"
    },
    "details": {
        "ipAddressReputation": {
            "score": 0,
            "domain": {
                "asn": 766,
                "sld": "uniovi",
                "tld": "es",
                "organization": "universidad de oviedo",
                "isp": "entidad publica empresarial red.es"
            },
            "level": "LOW"
        },
        "anonymousNetworkDetected": false,
        "country": "spain",
        "device": {
            "id": "Id-4c0013c4-5739-440f-91f4-147f460dd2ec",
            "estimatedDistance": 0,
            "os": {
                "name": "Mac OS X"
            },
            "browser": {
                "name": "Chrome"
            }
        },
        "state": "asturias",
        "city": "oviedo",
        "impossibleTravel": false,
        "ipvel4": {
            "level": "LOW",
            "threshold": {
                "source": "MIN_NOT_REACHED"
            },
            "velocity": {
                "distinctCount": 1,
                "during": 3600
            },
            "type": "VELOCITY"
        },
        "userLocationAnomaly": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "USER_LOCATION_ANOMALY"
        },
        "ipvel3": {
            "level": "LOW",
            "threshold": {
                "source": "MIN_NOT_REACHED"
            },
            "velocity": {
                "distinctCount": 1,
                "during": 3600
            },
            "type": "VELOCITY"
        },
        "botDetection": {
            "level": "HIGH",
            "reason": "Browser loading anomaly",
            "detected": {
                "rule": {
                    "id": 628
                }
            },
            "type": "BOT"
        },
        "newDevice": {
            "reason": "Not enough information to assess risk score",
            "status": "IN_TRAINING_PERIOD",
            "type": "DEVICE"
        },
        "deviceManagementPredictor": {
            "level": "MEDIUM",
            "reason": "Attribute ${event.isManaged} is \"no\".",
            "attribute": "${event.isManaged}",
            "value": "no",
            "type": "MAP"
        }
    }
}
```

---

---
title: Create Risk Policy Set
description: The POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets operation adds a new risk policy set to the specified environment.
component: pingone-api
page_id: pingone-api:protect:risk-policies/create_risk_policy_set_scores
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-policies/create_risk_policy_set_scores.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Policy Set

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets
```

The `POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets` operation adds a new risk policy set to the specified environment.

This example uses the Scores approach for combining the individual predictors.

Note that `condition.type` is set to AGGREGATED\_SCORES, and that the request contains the array `condition.aggregatedScores` rather than `condition.aggregatedWeights`.

### Prerequisites

* Refer to [Risk Policies](#risk-policies) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for more information, including the data models.
>
> **Base data model**
>
> | Property                | Type      | Required |
> | ----------------------- | --------- | -------- |
> | `createdAt`             | Date      | Required |
> | `default`               | Boolean   | Optional |
> | `defaultResult`         | Object    | Optional |
> | `description`           | String    | Optional |
> | `environment.id`        | String    | Required |
> | `evaluatedPredictors`   | String\[] | Optional |
> | `id`                    | String    | Required |
> | `name`                  | String    | Required |
> | `riskPolicies`          | String\[] | Required |
> | `triggers`              | Object\[] | Optional |
> | `triggers.type`         | String    | Required |
> | `triggers.policySet`    | Object    | Required |
> | `triggers.policySet.id` | String    | Required |
> | `triggers.expiresAt`    | String    | Required |
> | `updatedAt`             | Date      | Required |
>
> **Risk policies data model**
>
> This table lists the fields and objects that can be included in each of the elements in the `riskPolicies` array.
>
> | Property                           | Type    | Required          |
> | ---------------------------------- | ------- | ----------------- |
> | `condition`                        | Object  | Required          |
> | `condition.aggregatedScores`       | Array   | Required/Optional |
> | `condition.aggregatedScores.value` | String  | Required          |
> | `condition.aggregatedScores.score` | Integer | Required          |
> | `condition.type`                   | String  | Required          |
> | `condition.between.minScore`       | Integer | Required/Optional |
> | `condition.between.maxScore`       | Integer | Required/Optional |
> | `createdAt`                        | Date    | Required          |
> | `description`                      | String  | Optional          |
> | `id`                               | String  | Required          |
> | `name`                             | String  | Required          |
> | `priority`                         | Integer | Required          |
> | `result.level`                     | String  | Required          |
> | `updatedAt`                        | Date    | Required          |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Score-based policy",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        },
        {
            "name": "GEOVELOCITY_ANOMALY",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "value": "${details.impossibleTravel}",
                "equals": true
            }
        },
        {
            "name": "Medium scored policy",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 700,
                    "maxScore": 900
                }
            }
        },
        {
            "name": "High scored policy",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 900,
                    "maxScore": 1000
                }
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Score-based policy",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        },
        {
            "name": "GEOVELOCITY_ANOMALY",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "value": "${details.impossibleTravel}",
                "equals": true
            }
        },
        {
            "name": "Medium scored policy",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 700,
                    "maxScore": 900
                }
            }
        },
        {
            "name": "High scored policy",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 900,
                    "maxScore": 1000
                }
            }
        }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Score-based policy""," + "\n" +
@"    ""default"": false," + "\n" +
@"    ""defaultResult"": {" + "\n" +
@"        ""level"": ""Low""" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicies"": [" + "\n" +
@"        {" + "\n" +
@"            ""name"": ""ANONYMOUS_NETWORK_DETECTION""," + "\n" +
@"            ""result"": {" + "\n" +
@"                ""level"": ""HIGH""" + "\n" +
@"            }," + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""value"": ""${details.anonymousNetworkDetected}""," + "\n" +
@"                ""equals"": true" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"            ""name"": ""GEOVELOCITY_ANOMALY""," + "\n" +
@"            ""result"": {" + "\n" +
@"                ""level"": ""MEDIUM""" + "\n" +
@"            }," + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""value"": ""${details.impossibleTravel}""," + "\n" +
@"                ""equals"": true" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"            ""name"": ""Medium scored policy""," + "\n" +
@"            ""result"": {" + "\n" +
@"                ""level"": ""MEDIUM""" + "\n" +
@"            }," + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""type"": ""AGGREGATED_SCORES""," + "\n" +
@"                ""aggregatedScores"": [" + "\n" +
@"                    {" + "\n" +
@"                        ""value"": ""${details.userLocationAnomaly.level}""," + "\n" +
@"                        ""score"": 40" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""value"": ""${details.anonymousNetwork.level}""," + "\n" +
@"                        ""score"": 60" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""value"": ""${details.ipRisk.level}""," + "\n" +
@"                        ""score"": 40" + "\n" +
@"                    }" + "\n" +
@"                ]," + "\n" +
@"                ""between"": {" + "\n" +
@"                    ""minScore"": 700," + "\n" +
@"                    ""maxScore"": 900" + "\n" +
@"                }" + "\n" +
@"            }" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"            ""name"": ""High scored policy""," + "\n" +
@"            ""result"": {" + "\n" +
@"                ""level"": ""HIGH""" + "\n" +
@"            }," + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""type"": ""AGGREGATED_SCORES""," + "\n" +
@"                ""aggregatedScores"": [" + "\n" +
@"                    {" + "\n" +
@"                        ""value"": ""${details.userLocationAnomaly.level}""," + "\n" +
@"                        ""score"": 40" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""value"": ""${details.anonymousNetwork.level}""," + "\n" +
@"                        ""score"": 60" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""value"": ""${details.ipRisk.level}""," + "\n" +
@"                        ""score"": 40" + "\n" +
@"                    }" + "\n" +
@"                ]," + "\n" +
@"                ""between"": {" + "\n" +
@"                    ""minScore"": 900," + "\n" +
@"                    ""maxScore"": 1000" + "\n" +
@"                }" + "\n" +
@"            }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Score-based policy",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        },
        {
            "name": "GEOVELOCITY_ANOMALY",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "value": "${details.impossibleTravel}",
                "equals": true
            }
        },
        {
            "name": "Medium scored policy",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 700,
                    "maxScore": 900
                }
            }
        },
        {
            "name": "High scored policy",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 900,
                    "maxScore": 1000
                }
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
POST /v1/environments/{{envID}}/riskPolicySets HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Score-based policy",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "riskPolicies": [
        {
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "value": "${details.anonymousNetworkDetected}",
                "equals": true
            }
        },
        {
            "name": "GEOVELOCITY_ANOMALY",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "value": "${details.impossibleTravel}",
                "equals": true
            }
        },
        {
            "name": "Medium scored policy",
            "result": {
                "level": "MEDIUM"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 700,
                    "maxScore": 900
                }
            }
        },
        {
            "name": "High scored policy",
            "result": {
                "level": "HIGH"
            },
            "condition": {
                "type": "AGGREGATED_SCORES",
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "between": {
                    "minScore": 900,
                    "maxScore": 1000
                }
            }
        }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Score-based policy\",\n    \"default\": false,\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"riskPolicies\": [\n        {\n            \"name\": \"ANONYMOUS_NETWORK_DETECTION\",\n            \"result\": {\n                \"level\": \"HIGH\"\n            },\n            \"condition\": {\n                \"value\": \"${details.anonymousNetworkDetected}\",\n                \"equals\": true\n            }\n        },\n        {\n            \"name\": \"GEOVELOCITY_ANOMALY\",\n            \"result\": {\n                \"level\": \"MEDIUM\"\n            },\n            \"condition\": {\n                \"value\": \"${details.impossibleTravel}\",\n                \"equals\": true\n            }\n        },\n        {\n            \"name\": \"Medium scored policy\",\n            \"result\": {\n                \"level\": \"MEDIUM\"\n            },\n            \"condition\": {\n                \"type\": \"AGGREGATED_SCORES\",\n                \"aggregatedScores\": [\n                    {\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"score\": 40\n                    },\n                    {\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"score\": 60\n                    },\n                    {\n                        \"value\": \"${details.ipRisk.level}\",\n                        \"score\": 40\n                    }\n                ],\n                \"between\": {\n                    \"minScore\": 700,\n                    \"maxScore\": 900\n                }\n            }\n        },\n        {\n            \"name\": \"High scored policy\",\n            \"result\": {\n                \"level\": \"HIGH\"\n            },\n            \"condition\": {\n                \"type\": \"AGGREGATED_SCORES\",\n                \"aggregatedScores\": [\n                    {\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"score\": 40\n                    },\n                    {\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"score\": 60\n                    },\n                    {\n                        \"value\": \"${details.ipRisk.level}\",\n                        \"score\": 40\n                    }\n                ],\n                \"between\": {\n                    \"minScore\": 900,\n                    \"maxScore\": 1000\n                }\n            }\n        }\n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Score-based policy",
    "default": false,
    "defaultResult": {
      "level": "Low"
    },
    "riskPolicies": [
      {
        "name": "ANONYMOUS_NETWORK_DETECTION",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "value": "${details.anonymousNetworkDetected}",
          "equals": true
        }
      },
      {
        "name": "GEOVELOCITY_ANOMALY",
        "result": {
          "level": "MEDIUM"
        },
        "condition": {
          "value": "${details.impossibleTravel}",
          "equals": true
        }
      },
      {
        "name": "Medium scored policy",
        "result": {
          "level": "MEDIUM"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 700,
            "maxScore": 900
          }
        }
      },
      {
        "name": "High scored policy",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 900,
            "maxScore": 1000
          }
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Score-based policy",
    "default": false,
    "defaultResult": {
      "level": "Low"
    },
    "riskPolicies": [
      {
        "name": "ANONYMOUS_NETWORK_DETECTION",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "value": "${details.anonymousNetworkDetected}",
          "equals": true
        }
      },
      {
        "name": "GEOVELOCITY_ANOMALY",
        "result": {
          "level": "MEDIUM"
        },
        "condition": {
          "value": "${details.impossibleTravel}",
          "equals": true
        }
      },
      {
        "name": "Medium scored policy",
        "result": {
          "level": "MEDIUM"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 700,
            "maxScore": 900
          }
        }
      },
      {
        "name": "High scored policy",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 900,
            "maxScore": 1000
          }
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"

payload = json.dumps({
  "name": "Score-based policy",
  "default": False,
  "defaultResult": {
    "level": "Low"
  },
  "riskPolicies": [
    {
      "name": "ANONYMOUS_NETWORK_DETECTION",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "value": "${details.anonymousNetworkDetected}",
        "equals": True
      }
    },
    {
      "name": "GEOVELOCITY_ANOMALY",
      "result": {
        "level": "MEDIUM"
      },
      "condition": {
        "value": "${details.impossibleTravel}",
        "equals": True
      }
    },
    {
      "name": "Medium scored policy",
      "result": {
        "level": "MEDIUM"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 700,
          "maxScore": 900
        }
      }
    },
    {
      "name": "High scored policy",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 900,
          "maxScore": 1000
        }
      }
    }
  ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPolicySets');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Score-based policy",\n    "default": false,\n    "defaultResult": {\n        "level": "Low"\n    },\n    "riskPolicies": [\n        {\n            "name": "ANONYMOUS_NETWORK_DETECTION",\n            "result": {\n                "level": "HIGH"\n            },\n            "condition": {\n                "value": "${details.anonymousNetworkDetected}",\n                "equals": true\n            }\n        },\n        {\n            "name": "GEOVELOCITY_ANOMALY",\n            "result": {\n                "level": "MEDIUM"\n            },\n            "condition": {\n                "value": "${details.impossibleTravel}",\n                "equals": true\n            }\n        },\n        {\n            "name": "Medium scored policy",\n            "result": {\n                "level": "MEDIUM"\n            },\n            "condition": {\n                "type": "AGGREGATED_SCORES",\n                "aggregatedScores": [\n                    {\n                        "value": "${details.userLocationAnomaly.level}",\n                        "score": 40\n                    },\n                    {\n                        "value": "${details.anonymousNetwork.level}",\n                        "score": 60\n                    },\n                    {\n                        "value": "${details.ipRisk.level}",\n                        "score": 40\n                    }\n                ],\n                "between": {\n                    "minScore": 700,\n                    "maxScore": 900\n                }\n            }\n        },\n        {\n            "name": "High scored policy",\n            "result": {\n                "level": "HIGH"\n            },\n            "condition": {\n                "type": "AGGREGATED_SCORES",\n                "aggregatedScores": [\n                    {\n                        "value": "${details.userLocationAnomaly.level}",\n                        "score": 40\n                    },\n                    {\n                        "value": "${details.anonymousNetwork.level}",\n                        "score": 60\n                    },\n                    {\n                        "value": "${details.ipRisk.level}",\n                        "score": 40\n                    }\n                ],\n                "between": {\n                    "minScore": 900,\n                    "maxScore": 1000\n                }\n            }\n        }\n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Score-based policy",
  "default": false,
  "defaultResult": {
    "level": "Low"
  },
  "riskPolicies": [
    {
      "name": "ANONYMOUS_NETWORK_DETECTION",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "value": "\${details.anonymousNetworkDetected}",
        "equals": true
      }
    },
    {
      "name": "GEOVELOCITY_ANOMALY",
      "result": {
        "level": "MEDIUM"
      },
      "condition": {
        "value": "\${details.impossibleTravel}",
        "equals": true
      }
    },
    {
      "name": "Medium scored policy",
      "result": {
        "level": "MEDIUM"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "\${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "\${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "\${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 700,
          "maxScore": 900
        }
      }
    },
    {
      "name": "High scored policy",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "\${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "\${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "\${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 900,
          "maxScore": 1000
        }
      }
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Score-based policy\",\n    \"default\": false,\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"riskPolicies\": [\n        {\n            \"name\": \"ANONYMOUS_NETWORK_DETECTION\",\n            \"result\": {\n                \"level\": \"HIGH\"\n            },\n            \"condition\": {\n                \"value\": \"${details.anonymousNetworkDetected}\",\n                \"equals\": true\n            }\n        },\n        {\n            \"name\": \"GEOVELOCITY_ANOMALY\",\n            \"result\": {\n                \"level\": \"MEDIUM\"\n            },\n            \"condition\": {\n                \"value\": \"${details.impossibleTravel}\",\n                \"equals\": true\n            }\n        },\n        {\n            \"name\": \"Medium scored policy\",\n            \"result\": {\n                \"level\": \"MEDIUM\"\n            },\n            \"condition\": {\n                \"type\": \"AGGREGATED_SCORES\",\n                \"aggregatedScores\": [\n                    {\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"score\": 40\n                    },\n                    {\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"score\": 60\n                    },\n                    {\n                        \"value\": \"${details.ipRisk.level}\",\n                        \"score\": 40\n                    }\n                ],\n                \"between\": {\n                    \"minScore\": 700,\n                    \"maxScore\": 900\n                }\n            }\n        },\n        {\n            \"name\": \"High scored policy\",\n            \"result\": {\n                \"level\": \"HIGH\"\n            },\n            \"condition\": {\n                \"type\": \"AGGREGATED_SCORES\",\n                \"aggregatedScores\": [\n                    {\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"score\": 40\n                    },\n                    {\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"score\": 60\n                    },\n                    {\n                        \"value\": \"${details.ipRisk.level}\",\n                        \"score\": 40\n                    }\n                ],\n                \"between\": {\n                    \"minScore\": 900,\n                    \"maxScore\": 1000\n                }\n            }\n        }\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPolicySets/f394426f-9b71-4e01-ac78-2956a2e92ac2"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Score-based policy",
    "createdAt": "2022-07-21T06:54:42.494Z",
    "updatedAt": "2022-07-21T06:54:42.494Z",
    "defaultResult": {
        "level": "LOW",
        "type": "VALUE"
    },
    "riskPolicies": [
        {
            "id": "e58475bc-ae86-44fa-aabe-37fcc59390f3",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2"
            },
            "name": "ANONYMOUS_NETWORK_DETECTION",
            "priority": 1,
            "result": {
                "level": "HIGH",
                "type": "VALUE"
            },
            "condition": {
                "equals": true,
                "value": "${details.anonymousNetworkDetected}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2022-07-21T06:54:42.494Z",
            "updatedAt": "2022-07-21T06:54:42.494Z"
        },
        {
            "id": "bcb992d2-133b-438c-9d04-1f720a4e4011",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2"
            },
            "name": "GEOVELOCITY_ANOMALY",
            "priority": 2,
            "result": {
                "level": "MEDIUM",
                "type": "VALUE"
            },
            "condition": {
                "equals": true,
                "value": "${details.impossibleTravel}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2022-07-21T06:54:42.494Z",
            "updatedAt": "2022-07-21T06:54:42.494Z"
        },
        {
            "id": "70ab14c2-bfbd-4c75-8d14-e6b85fbee064",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2"
            },
            "name": "Medium scored policy",
            "priority": 3,
            "result": {
                "level": "MEDIUM",
                "type": "VALUE"
            },
            "condition": {
                "between": {
                    "minScore": 700,
                    "maxScore": 900
                },
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "type": "AGGREGATED_SCORES"
            },
            "createdAt": "2022-07-21T06:54:42.494Z",
            "updatedAt": "2022-07-21T06:54:42.494Z"
        },
        {
            "id": "3fabcf6f-1eb0-426b-9b1d-e448b9159866",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2"
            },
            "name": "High scored policy",
            "priority": 4,
            "result": {
                "level": "HIGH",
                "type": "VALUE"
            },
            "condition": {
                "between": {
                    "minScore": 900,
                    "maxScore": 1000
                },
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "type": "AGGREGATED_SCORES"
            },
            "createdAt": "2022-07-21T06:54:42.494Z",
            "updatedAt": "2022-07-21T06:54:42.494Z"
        }
    ],
    "default": false
}
```

---

---
title: Create Risk Policy Set - Targeted Policy no Scores (PingID users)
description: This example uses POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets to create a new targeted risk policy in an environment that has the PingID service but not the Protect service. The policy contains mitigations but because the Protect service is absent, the policy does not contain a list of specific predictors and scores to use to calculate overall risk level.
component: pingone-api
page_id: pingone-api:protect:risk-policies/create_risk_policy_set_targeted_no_scores
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-policies/create_risk_policy_set_targeted_no_scores.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Policy Set - Targeted Policy no Scores (PingID users)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets
```

This example uses `POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets` to create a new targeted risk policy in an environment that has the PingID service but not the Protect service. The policy contains mitigations but because the Protect service is absent, the policy does not contain a list of specific predictors and scores to use to calculate overall risk level.

The flow type, user group, and application conditions are defined in the `targets` object.

The `mitigations` array is used to specify the recommended course of action that should be taken. Currently this array can only contain a single object.

### Prerequisites

* Refer to [Risk Policies](#risk-policies) for important overview information.

:::requestmodel

For complete property descriptions, refer to [Risk Policies](#risk-policies).

| Property                                           | Type    | Required |
| -------------------------------------------------- | ------- | -------- |
| `default`                                          | Boolean | Optional |
| `defaultResult.level`                              | Object  | Optional |
| `name`                                             | String  | Required |
| `riskPolicies`                                     | String  | Required |
| `riskPolicies[].condition`                         | Object  | Required |
| `riskPolicies[].condition.equals`                  | String  | Optional |
| `riskPolicies[].condition.type`                    | String  | Required |
| `riskPolicies[].condition.value`                   | String  | Optional |
| `riskPolicies[].name`                              | String  | Required |
| `riskPolicies[].result`                            | Object  | Required |
| `riskPolicies[].result.mitigations`                | Array   | Optional |
| `riskPolicies[].result.mitigations[].action`       | String  | Optional |
| `riskPolicies[].result.mitigations[].customAction` | String  | Optional |
| `riskPolicies[].result.mitigations[].policyId`     | String  | Optional |
| `riskPolicies[].result.type`                       | String  | Optional |
| `targets`                                          | Object  | Optional |
| `targets.condition`                                | Object  | Optional |
| `targets.condition.and`                            | Array   | Optional |
| `targets.condition.and[].contains`                 | String  | Optional |
| `targets.condition.and[].list`                     | Array   | Optional |

* :

  :leveloffset: -1

#### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

#### Body

raw ( application/json )

```json
{
    "name": "Targeted policy without scores - for PingID users",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
        }
      }
    ]
}
```

###

#### Example Request

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Targeted policy without scores - for PingID users",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
        }
      }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Targeted policy without scores - for PingID users""," + "\n" +
@"    ""default"": false," + "\n" +
@"    ""defaultResult"": {" + "\n" +
@"        ""level"": ""Low""" + "\n" +
@"    }," + "\n" +
@"    ""targets"":{" + "\n" +
@"        ""condition"": { ""and"": [{" + "\n" +
@"            ""list"": [""AUTHENTICATION"", ""AUTHORIZATION""]," + "\n" +
@"            ""contains"": ""${event.flow.type}""" + "\n" +
@"          }," + "\n" +
@"          { " + "\n" +
@"            ""list"": [""Sales""]," + "\n" +
@"            ""contains"": ""${event.user.groups}""" + "\n" +
@"          }," + "\n" +
@"          { " + "\n" +
@"            ""list"": [""6b6f867b-d768-4c2c-a9b6-6816da00d824"", ""845c9918-94d7-430c-b3d8-eafafc215fd9""]," + "\n" +
@"            ""contains"": ""${event.targetResource.id}""" + "\n" +
@"          }]" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicies"": [{" + "\n" +
@"        ""name"" : ""USER_LOCATION_ANOMALY""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""CUSTOM""," + "\n" +
@"            ""customAction"" : ""CustomActionForUserLocationAnomaly""" + "\n" +
@"          }]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.userLocationAnomaly.level}""," + "\n" +
@"          ""equals"" : ""High""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      }," + "\n" +
@"      {" + "\n" +
@"        ""name"" : ""VELOCITY""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""DENY_AND_SUSPEND""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.ipVelocityByUser.level}""," + "\n" +
@"          ""equals"" : ""High""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      },{" + "\n" +
@"        ""name"" : ""USER_RISK_BEHAVIOR""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""VERIFY""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.userBasedRiskBehavior.level}""," + "\n" +
@"          ""equals"" : ""Medium""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      }," + "\n" +
@"      {" + "\n" +
@"        ""name"" : ""EMAIL_REPUTATION""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""MFA""," + "\n" +
@"            ""mfaAuthenticationPolicyId"" : ""{{deviceAuthenticationPolicyID}}""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.emailReputation.level}""," + "\n" +
@"          ""equals"" : ""High""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      }," + "\n" +
@"      {" + "\n" +
@"        ""name"" : ""IP_REPUTATION""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""APPROVE""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.ipRisk.level}""," + "\n" +
@"          ""equals"" : ""Low""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"        {" + "\n" +
@"        ""name"" : ""FALLBACK""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""DENY""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION_FALLBACK""" + "\n" +
@"        }" + "\n" +
@"      } " + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Targeted policy without scores - for PingID users",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
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
POST /v1/environments/{{envID}}/riskPolicySets HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Targeted policy without scores - for PingID users",
    "default": false,
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
        }
      }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Targeted policy without scores - for PingID users\",\n    \"default\": false,\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"targets\":{\n        \"condition\": { \"and\": [{\n            \"list\": [\"AUTHENTICATION\", \"AUTHORIZATION\"],\n            \"contains\": \"${event.flow.type}\"\n          },\n          { \n            \"list\": [\"Sales\"],\n            \"contains\": \"${event.user.groups}\"\n          },\n          { \n            \"list\": [\"6b6f867b-d768-4c2c-a9b6-6816da00d824\", \"845c9918-94d7-430c-b3d8-eafafc215fd9\"],\n            \"contains\": \"${event.targetResource.id}\"\n          }]\n        }\n    },\n    \"riskPolicies\": [{\n        \"name\" : \"USER_LOCATION_ANOMALY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"CUSTOM\",\n            \"customAction\" : \"CustomActionForUserLocationAnomaly\"\n          }],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userLocationAnomaly.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"VELOCITY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY_AND_SUSPEND\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipVelocityByUser.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },{\n        \"name\" : \"USER_RISK_BEHAVIOR\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"VERIFY\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userBasedRiskBehavior.level}\",\n          \"equals\" : \"Medium\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"EMAIL_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"MFA\",\n            \"mfaAuthenticationPolicyId\" : \"{{deviceAuthenticationPolicyID}}\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.emailReputation.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"IP_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"APPROVE\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipRisk.level}\",\n          \"equals\" : \"Low\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n    },\n        {\n        \"name\" : \"FALLBACK\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY\"\n          } ],\n          \"type\" : \"MITIGATION_FALLBACK\"\n        }\n      } \n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Targeted policy without scores - for PingID users",
    "default": false,
    "defaultResult": {
      "level": "Low"
    },
    "targets": {
      "condition": {
        "and": [
          {
            "list": [
              "AUTHENTICATION",
              "AUTHORIZATION"
            ],
            "contains": "${event.flow.type}"
          },
          {
            "list": [
              "Sales"
            ],
            "contains": "${event.user.groups}"
          },
          {
            "list": [
              "6b6f867b-d768-4c2c-a9b6-6816da00d824",
              "845c9918-94d7-430c-b3d8-eafafc215fd9"
            ],
            "contains": "${event.targetResource.id}"
          }
        ]
      }
    },
    "riskPolicies": [
      {
        "name": "USER_LOCATION_ANOMALY",
        "result": {
          "mitigations": [
            {
              "action": "CUSTOM",
              "customAction": "CustomActionForUserLocationAnomaly"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userLocationAnomaly.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "VELOCITY",
        "result": {
          "mitigations": [
            {
              "action": "DENY_AND_SUSPEND"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipVelocityByUser.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "USER_RISK_BEHAVIOR",
        "result": {
          "mitigations": [
            {
              "action": "VERIFY"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userBasedRiskBehavior.level}",
          "equals": "Medium",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "EMAIL_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "MFA",
              "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.emailReputation.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "IP_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "APPROVE"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipRisk.level}",
          "equals": "Low",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "FALLBACK",
        "result": {
          "mitigations": [
            {
              "action": "DENY"
            }
          ],
          "type": "MITIGATION_FALLBACK"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Targeted policy without scores - for PingID users",
    "default": false,
    "defaultResult": {
      "level": "Low"
    },
    "targets": {
      "condition": {
        "and": [
          {
            "list": [
              "AUTHENTICATION",
              "AUTHORIZATION"
            ],
            "contains": "${event.flow.type}"
          },
          {
            "list": [
              "Sales"
            ],
            "contains": "${event.user.groups}"
          },
          {
            "list": [
              "6b6f867b-d768-4c2c-a9b6-6816da00d824",
              "845c9918-94d7-430c-b3d8-eafafc215fd9"
            ],
            "contains": "${event.targetResource.id}"
          }
        ]
      }
    },
    "riskPolicies": [
      {
        "name": "USER_LOCATION_ANOMALY",
        "result": {
          "mitigations": [
            {
              "action": "CUSTOM",
              "customAction": "CustomActionForUserLocationAnomaly"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userLocationAnomaly.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "VELOCITY",
        "result": {
          "mitigations": [
            {
              "action": "DENY_AND_SUSPEND"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipVelocityByUser.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "USER_RISK_BEHAVIOR",
        "result": {
          "mitigations": [
            {
              "action": "VERIFY"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userBasedRiskBehavior.level}",
          "equals": "Medium",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "EMAIL_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "MFA",
              "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.emailReputation.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "IP_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "APPROVE"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipRisk.level}",
          "equals": "Low",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "FALLBACK",
        "result": {
          "mitigations": [
            {
              "action": "DENY"
            }
          ],
          "type": "MITIGATION_FALLBACK"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"

payload = json.dumps({
  "name": "Targeted policy without scores - for PingID users",
  "default": False,
  "defaultResult": {
    "level": "Low"
  },
  "targets": {
    "condition": {
      "and": [
        {
          "list": [
            "AUTHENTICATION",
            "AUTHORIZATION"
          ],
          "contains": "${event.flow.type}"
        },
        {
          "list": [
            "Sales"
          ],
          "contains": "${event.user.groups}"
        },
        {
          "list": [
            "6b6f867b-d768-4c2c-a9b6-6816da00d824",
            "845c9918-94d7-430c-b3d8-eafafc215fd9"
          ],
          "contains": "${event.targetResource.id}"
        }
      ]
    }
  },
  "riskPolicies": [
    {
      "name": "USER_LOCATION_ANOMALY",
      "result": {
        "mitigations": [
          {
            "action": "CUSTOM",
            "customAction": "CustomActionForUserLocationAnomaly"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.userLocationAnomaly.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "VELOCITY",
      "result": {
        "mitigations": [
          {
            "action": "DENY_AND_SUSPEND"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.ipVelocityByUser.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "USER_RISK_BEHAVIOR",
      "result": {
        "mitigations": [
          {
            "action": "VERIFY"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.userBasedRiskBehavior.level}",
        "equals": "Medium",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "EMAIL_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "MFA",
            "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.emailReputation.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "IP_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "APPROVE"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.ipRisk.level}",
        "equals": "Low",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "FALLBACK",
      "result": {
        "mitigations": [
          {
            "action": "DENY"
          }
        ],
        "type": "MITIGATION_FALLBACK"
      }
    }
  ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPolicySets');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Targeted policy without scores - for PingID users",\n    "default": false,\n    "defaultResult": {\n        "level": "Low"\n    },\n    "targets":{\n        "condition": { "and": [{\n            "list": ["AUTHENTICATION", "AUTHORIZATION"],\n            "contains": "${event.flow.type}"\n          },\n          { \n            "list": ["Sales"],\n            "contains": "${event.user.groups}"\n          },\n          { \n            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],\n            "contains": "${event.targetResource.id}"\n          }]\n        }\n    },\n    "riskPolicies": [{\n        "name" : "USER_LOCATION_ANOMALY",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "CUSTOM",\n            "customAction" : "CustomActionForUserLocationAnomaly"\n          }],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.userLocationAnomaly.level}",\n          "equals" : "High",\n          "type" : "VALUE_COMPARISON"\n        }\n      },\n      {\n        "name" : "VELOCITY",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "DENY_AND_SUSPEND"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.ipVelocityByUser.level}",\n          "equals" : "High",\n          "type" : "VALUE_COMPARISON"\n        }\n      },{\n        "name" : "USER_RISK_BEHAVIOR",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "VERIFY"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.userBasedRiskBehavior.level}",\n          "equals" : "Medium",\n          "type" : "VALUE_COMPARISON"\n        }\n      },\n      {\n        "name" : "EMAIL_REPUTATION",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "MFA",\n            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.emailReputation.level}",\n          "equals" : "High",\n          "type" : "VALUE_COMPARISON"\n        }\n      },\n      {\n        "name" : "IP_REPUTATION",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "APPROVE"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.ipRisk.level}",\n          "equals" : "Low",\n          "type" : "VALUE_COMPARISON"\n        }\n    },\n        {\n        "name" : "FALLBACK",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "DENY"\n          } ],\n          "type" : "MITIGATION_FALLBACK"\n        }\n      } \n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Targeted policy without scores - for PingID users",
  "default": false,
  "defaultResult": {
    "level": "Low"
  },
  "targets": {
    "condition": {
      "and": [
        {
          "list": [
            "AUTHENTICATION",
            "AUTHORIZATION"
          ],
          "contains": "\${event.flow.type}"
        },
        {
          "list": [
            "Sales"
          ],
          "contains": "\${event.user.groups}"
        },
        {
          "list": [
            "6b6f867b-d768-4c2c-a9b6-6816da00d824",
            "845c9918-94d7-430c-b3d8-eafafc215fd9"
          ],
          "contains": "\${event.targetResource.id}"
        }
      ]
    }
  },
  "riskPolicies": [
    {
      "name": "USER_LOCATION_ANOMALY",
      "result": {
        "mitigations": [
          {
            "action": "CUSTOM",
            "customAction": "CustomActionForUserLocationAnomaly"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.userLocationAnomaly.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "VELOCITY",
      "result": {
        "mitigations": [
          {
            "action": "DENY_AND_SUSPEND"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.ipVelocityByUser.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "USER_RISK_BEHAVIOR",
      "result": {
        "mitigations": [
          {
            "action": "VERIFY"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.userBasedRiskBehavior.level}",
        "equals": "Medium",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "EMAIL_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "MFA",
            "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.emailReputation.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "IP_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "APPROVE"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.ipRisk.level}",
        "equals": "Low",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "FALLBACK",
      "result": {
        "mitigations": [
          {
            "action": "DENY"
          }
        ],
        "type": "MITIGATION_FALLBACK"
      }
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Targeted policy without scores - for PingID users\",\n    \"default\": false,\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"targets\":{\n        \"condition\": { \"and\": [{\n            \"list\": [\"AUTHENTICATION\", \"AUTHORIZATION\"],\n            \"contains\": \"${event.flow.type}\"\n          },\n          { \n            \"list\": [\"Sales\"],\n            \"contains\": \"${event.user.groups}\"\n          },\n          { \n            \"list\": [\"6b6f867b-d768-4c2c-a9b6-6816da00d824\", \"845c9918-94d7-430c-b3d8-eafafc215fd9\"],\n            \"contains\": \"${event.targetResource.id}\"\n          }]\n        }\n    },\n    \"riskPolicies\": [{\n        \"name\" : \"USER_LOCATION_ANOMALY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"CUSTOM\",\n            \"customAction\" : \"CustomActionForUserLocationAnomaly\"\n          }],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userLocationAnomaly.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"VELOCITY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY_AND_SUSPEND\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipVelocityByUser.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },{\n        \"name\" : \"USER_RISK_BEHAVIOR\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"VERIFY\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userBasedRiskBehavior.level}\",\n          \"equals\" : \"Medium\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"EMAIL_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"MFA\",\n            \"mfaAuthenticationPolicyId\" : \"{{deviceAuthenticationPolicyID}}\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.emailReputation.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"IP_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"APPROVE\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipRisk.level}\",\n          \"equals\" : \"Low\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n    },\n        {\n        \"name\" : \"FALLBACK\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY\"\n          } ],\n          \"type\" : \"MITIGATION_FALLBACK\"\n        }\n      } \n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")!,timeoutInterval: Double.infinity)
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

#### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPolicySets/eb2769ed-bb27-473b-8134-95f9385a326f"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "eb2769ed-bb27-473b-8134-95f9385a326f",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Targeted policy without scores - for PingID users",
    "createdAt": "2025-06-08T10:17:05.812Z",
    "updatedAt": "2025-06-08T10:17:05.812Z",
    "defaultResult": {
        "level": "LOW",
        "type": "VALUE"
    },
    "targets": {
        "condition": {
            "and": [
                {
                    "list": [
                        "AUTHENTICATION",
                        "AUTHORIZATION"
                    ],
                    "contains": "${event.flow.type}",
                    "type": "STRING_LIST"
                },
                {
                    "list": [
                        "Sales"
                    ],
                    "contains": "${event.user.groups}",
                    "type": "GROUPS_INTERSECTION"
                },
                {
                    "list": [
                        "6b6f867b-d768-4c2c-a9b6-6816da00d824",
                        "845c9918-94d7-430c-b3d8-eafafc215fd9"
                    ],
                    "contains": "${event.targetResource.id}",
                    "type": "STRING_LIST"
                }
            ],
            "type": "AND"
        }
    },
    "riskPolicies": [
        {
            "id": "f1bebb84-61dd-4b2b-97e3-f82f6187791b",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "eb2769ed-bb27-473b-8134-95f9385a326f"
            },
            "name": "USER_LOCATION_ANOMALY",
            "priority": 1,
            "result": {
                "mitigations": [
                    {
                        "action": "CUSTOM",
                        "customAction": "CustomActionForUserLocationAnomaly"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "High",
                "value": "${details.userLocationAnomaly.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:17:05.812Z",
            "updatedAt": "2025-06-08T10:17:05.812Z"
        },
        {
            "id": "009caa89-a2b7-4b5c-bfea-e96c19200b93",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "eb2769ed-bb27-473b-8134-95f9385a326f"
            },
            "name": "VELOCITY",
            "priority": 2,
            "result": {
                "mitigations": [
                    {
                        "action": "DENY_AND_SUSPEND"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "High",
                "value": "${details.ipVelocityByUser.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:17:05.812Z",
            "updatedAt": "2025-06-08T10:17:05.812Z"
        },
        {
            "id": "2d1a8403-6e99-4f3a-9ce2-4063125dc7bd",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "eb2769ed-bb27-473b-8134-95f9385a326f"
            },
            "name": "USER_RISK_BEHAVIOR",
            "priority": 3,
            "result": {
                "mitigations": [
                    {
                        "action": "VERIFY"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "Medium",
                "value": "${details.userBasedRiskBehavior.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:17:05.812Z",
            "updatedAt": "2025-06-08T10:17:05.812Z"
        },
        {
            "id": "65e43c3b-67a5-41dd-85fe-91ce0372c9c8",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "eb2769ed-bb27-473b-8134-95f9385a326f"
            },
            "name": "EMAIL_REPUTATION",
            "priority": 4,
            "result": {
                "mitigations": [
                    {
                        "action": "MFA",
                        "mfaAuthenticationPolicyId": "a3e7a1d1-90ea-4e63-aa81-23383ba1c004"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "High",
                "value": "${details.emailReputation.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:17:05.812Z",
            "updatedAt": "2025-06-08T10:17:05.812Z"
        },
        {
            "id": "a5880c20-fa83-4477-af6f-01af5829dfd0",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "eb2769ed-bb27-473b-8134-95f9385a326f"
            },
            "name": "IP_REPUTATION",
            "priority": 5,
            "result": {
                "mitigations": [
                    {
                        "action": "APPROVE"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "Low",
                "value": "${details.ipRisk.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:17:05.812Z",
            "updatedAt": "2025-06-08T10:17:05.812Z"
        },
        {
            "id": "3d2c2dec-5f3e-4761-8b36-dde4c7ad49e9",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "eb2769ed-bb27-473b-8134-95f9385a326f"
            },
            "name": "FALLBACK",
            "result": {
                "mitigations": [
                    {
                        "action": "DENY"
                    }
                ],
                "type": "MITIGATION_FALLBACK"
            },
            "createdAt": "2025-06-08T10:17:05.812Z",
            "updatedAt": "2025-06-08T10:17:05.812Z"
        }
    ],
    "default": false
}
```

---

---
title: Create Risk Policy Set - Targeted Policy with Mitigations
description: This example uses POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets to create a new targeted risk policy that includes a number of mitigations.
component: pingone-api
page_id: pingone-api:protect:risk-policies/create_risk_policy_set_targeted_w_mitigations
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-policies/create_risk_policy_set_targeted_w_mitigations.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Policy Set - Targeted Policy with Mitigations

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets
```

This example uses `POST {{apiPath}}/v1/environments/{{envID}}/riskPolicySets` to create a new targeted risk policy that includes a number of mitigations.

The flow type, user group, and application conditions are defined in the `targets` object.

The `mitigations` array is used to specify the recommended course of action that should be taken. Currently this array can only contain a single object.

### Prerequisites

* Refer to [Risk Policies](#risk-policies) for important overview information.

:::requestmodel

For complete property descriptions, refer to [Risk Policies](#risk-policies).

| Property                                           | Type    | Required |
| -------------------------------------------------- | ------- | -------- |
| `defaultResult.level`                              | Object  | Optional |
| `name`                                             | String  | Required |
| `riskPolicies`                                     | String  | Required |
| `riskPolicies[].condition`                         | Object  | Required |
| `riskPolicies[].condition.equals`                  | String  | Optional |
| `riskPolicies[].condition.type`                    | String  | Required |
| `riskPolicies[].condition.value`                   | String  | Optional |
| `riskPolicies[].condition.aggregatedScores`        | Array   | Required |
| `riskPolicies[].condition.aggregatedScores.score`  | Integer | Required |
| `riskPolicies[].condition.aggregatedScores.value`  | String  | Required |
| `riskPolicies[].condition.between.maxScore`        | Integer | Required |
| `riskPolicies[].condition.between.minScore`        | Integer | Required |
| `riskPolicies[].name`                              | String  | Required |
| `riskPolicies[].result`                            | Object  | Required |
| `riskPolicies[].result.level`                      | String  | Required |
| `riskPolicies[].result.mitigations`                | Array   | Optional |
| `riskPolicies[].result.mitigations[].action`       | String  | Optional |
| `riskPolicies[].result.mitigations[].customAction` | String  | Optional |
| `riskPolicies[].result.mitigations[].policyId`     | String  | Optional |
| `riskPolicies[].result.type`                       | String  | Optional |
| `targets`                                          | Object  | Optional |
| `targets.condition`                                | Object  | Optional |
| `targets.condition.and`                            | Array   | Optional |
| `targets.condition.and[].contains`                 | String  | Optional |
| `targets.condition.and[].list`                     | Array   | Optional |

* :

  :leveloffset: -1

#### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

#### Body

raw ( application/json )

```json
{
    "name": "Targeted policy with mitigations",
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
    {
        "name": "Medium scored policy",
        "result": {
            "level": "MEDIUM"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 700,
                "maxScore": 900
            }
        }
    },
    {
        "name": "High scored policy",
        "result": {
            "level": "HIGH"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 900,
                "maxScore": 1000
            }
        }
        },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
        }
      }
    ]
}
```

###

#### Example Request

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Targeted policy with mitigations",
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
    {
        "name": "Medium scored policy",
        "result": {
            "level": "MEDIUM"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 700,
                "maxScore": 900
            }
        }
    },
    {
        "name": "High scored policy",
        "result": {
            "level": "HIGH"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 900,
                "maxScore": 1000
            }
        }
        },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
        }
      }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Targeted policy with mitigations""," + "\n" +
@"    ""defaultResult"": {" + "\n" +
@"        ""level"": ""Low""" + "\n" +
@"    }," + "\n" +
@"    ""targets"":{" + "\n" +
@"        ""condition"": { ""and"": [{" + "\n" +
@"            ""list"": [""AUTHENTICATION"", ""AUTHORIZATION""]," + "\n" +
@"            ""contains"": ""${event.flow.type}""" + "\n" +
@"          }," + "\n" +
@"          { " + "\n" +
@"            ""list"": [""Sales""]," + "\n" +
@"            ""contains"": ""${event.user.groups}""" + "\n" +
@"          }," + "\n" +
@"          { " + "\n" +
@"            ""list"": [""6b6f867b-d768-4c2c-a9b6-6816da00d824"", ""845c9918-94d7-430c-b3d8-eafafc215fd9""]," + "\n" +
@"            ""contains"": ""${event.targetResource.id}""" + "\n" +
@"          }]" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""riskPolicies"": [{" + "\n" +
@"        ""name"" : ""USER_LOCATION_ANOMALY""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""CUSTOM""," + "\n" +
@"            ""customAction"" : ""CustomActionForUserLocationAnomaly""" + "\n" +
@"          }]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.userLocationAnomaly.level}""," + "\n" +
@"          ""equals"" : ""High""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      }," + "\n" +
@"      {" + "\n" +
@"        ""name"" : ""VELOCITY""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""DENY_AND_SUSPEND""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.ipVelocityByUser.level}""," + "\n" +
@"          ""equals"" : ""High""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      },{" + "\n" +
@"        ""name"" : ""USER_RISK_BEHAVIOR""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""VERIFY""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.userBasedRiskBehavior.level}""," + "\n" +
@"          ""equals"" : ""Medium""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      }," + "\n" +
@"      {" + "\n" +
@"        ""name"" : ""EMAIL_REPUTATION""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""MFA""," + "\n" +
@"            ""mfaAuthenticationPolicyId"" : ""{{deviceAuthenticationPolicyID}}""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.emailReputation.level}""," + "\n" +
@"          ""equals"" : ""High""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"      }," + "\n" +
@"      {" + "\n" +
@"        ""name"" : ""IP_REPUTATION""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""APPROVE""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION""" + "\n" +
@"        }," + "\n" +
@"        ""condition"" : {" + "\n" +
@"          ""value"" : ""${details.ipRisk.level}""," + "\n" +
@"          ""equals"" : ""Low""," + "\n" +
@"          ""type"" : ""VALUE_COMPARISON""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    {" + "\n" +
@"        ""name"": ""Medium scored policy""," + "\n" +
@"        ""result"": {" + "\n" +
@"            ""level"": ""MEDIUM""" + "\n" +
@"        }," + "\n" +
@"        ""condition"": {" + "\n" +
@"            ""type"": ""AGGREGATED_SCORES""," + "\n" +
@"            ""aggregatedScores"": [" + "\n" +
@"                {" + "\n" +
@"                    ""value"": ""${details.userLocationAnomaly.level}""," + "\n" +
@"                    ""score"": 40" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""value"": ""${details.anonymousNetwork.level}""," + "\n" +
@"                    ""score"": 60" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""value"": ""${details.ipRisk.level}""," + "\n" +
@"                    ""score"": 40" + "\n" +
@"                }" + "\n" +
@"            ]," + "\n" +
@"            ""between"": {" + "\n" +
@"                ""minScore"": 700," + "\n" +
@"                ""maxScore"": 900" + "\n" +
@"            }" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    {" + "\n" +
@"        ""name"": ""High scored policy""," + "\n" +
@"        ""result"": {" + "\n" +
@"            ""level"": ""HIGH""" + "\n" +
@"        }," + "\n" +
@"        ""condition"": {" + "\n" +
@"            ""type"": ""AGGREGATED_SCORES""," + "\n" +
@"            ""aggregatedScores"": [" + "\n" +
@"                {" + "\n" +
@"                    ""value"": ""${details.userLocationAnomaly.level}""," + "\n" +
@"                    ""score"": 40" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""value"": ""${details.anonymousNetwork.level}""," + "\n" +
@"                    ""score"": 60" + "\n" +
@"                }," + "\n" +
@"                {" + "\n" +
@"                    ""value"": ""${details.ipRisk.level}""," + "\n" +
@"                    ""score"": 40" + "\n" +
@"                }" + "\n" +
@"            ]," + "\n" +
@"            ""between"": {" + "\n" +
@"                ""minScore"": 900," + "\n" +
@"                ""maxScore"": 1000" + "\n" +
@"            }" + "\n" +
@"        }" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"        ""name"" : ""FALLBACK""," + "\n" +
@"        ""result"" : {" + "\n" +
@"          ""mitigations"" : [ {" + "\n" +
@"            ""action"" : ""DENY""" + "\n" +
@"          } ]," + "\n" +
@"          ""type"" : ""MITIGATION_FALLBACK""" + "\n" +
@"        }" + "\n" +
@"      } " + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Targeted policy with mitigations",
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
    {
        "name": "Medium scored policy",
        "result": {
            "level": "MEDIUM"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 700,
                "maxScore": 900
            }
        }
    },
    {
        "name": "High scored policy",
        "result": {
            "level": "HIGH"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 900,
                "maxScore": 1000
            }
        }
        },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
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
POST /v1/environments/{{envID}}/riskPolicySets HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Targeted policy with mitigations",
    "defaultResult": {
        "level": "Low"
    },
    "targets":{
        "condition": { "and": [{
            "list": ["AUTHENTICATION", "AUTHORIZATION"],
            "contains": "${event.flow.type}"
          },
          {
            "list": ["Sales"],
            "contains": "${event.user.groups}"
          },
          {
            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],
            "contains": "${event.targetResource.id}"
          }]
        }
    },
    "riskPolicies": [{
        "name" : "USER_LOCATION_ANOMALY",
        "result" : {
          "mitigations" : [ {
            "action" : "CUSTOM",
            "customAction" : "CustomActionForUserLocationAnomaly"
          }],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userLocationAnomaly.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "VELOCITY",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY_AND_SUSPEND"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipVelocityByUser.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },{
        "name" : "USER_RISK_BEHAVIOR",
        "result" : {
          "mitigations" : [ {
            "action" : "VERIFY"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.userBasedRiskBehavior.level}",
          "equals" : "Medium",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "EMAIL_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "MFA",
            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.emailReputation.level}",
          "equals" : "High",
          "type" : "VALUE_COMPARISON"
        }
      },
      {
        "name" : "IP_REPUTATION",
        "result" : {
          "mitigations" : [ {
            "action" : "APPROVE"
          } ],
          "type" : "MITIGATION"
        },
        "condition" : {
          "value" : "${details.ipRisk.level}",
          "equals" : "Low",
          "type" : "VALUE_COMPARISON"
        }
    },
    {
        "name": "Medium scored policy",
        "result": {
            "level": "MEDIUM"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 700,
                "maxScore": 900
            }
        }
    },
    {
        "name": "High scored policy",
        "result": {
            "level": "HIGH"
        },
        "condition": {
            "type": "AGGREGATED_SCORES",
            "aggregatedScores": [
                {
                    "value": "${details.userLocationAnomaly.level}",
                    "score": 40
                },
                {
                    "value": "${details.anonymousNetwork.level}",
                    "score": 60
                },
                {
                    "value": "${details.ipRisk.level}",
                    "score": 40
                }
            ],
            "between": {
                "minScore": 900,
                "maxScore": 1000
            }
        }
        },
        {
        "name" : "FALLBACK",
        "result" : {
          "mitigations" : [ {
            "action" : "DENY"
          } ],
          "type" : "MITIGATION_FALLBACK"
        }
      }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Targeted policy with mitigations\",\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"targets\":{\n        \"condition\": { \"and\": [{\n            \"list\": [\"AUTHENTICATION\", \"AUTHORIZATION\"],\n            \"contains\": \"${event.flow.type}\"\n          },\n          { \n            \"list\": [\"Sales\"],\n            \"contains\": \"${event.user.groups}\"\n          },\n          { \n            \"list\": [\"6b6f867b-d768-4c2c-a9b6-6816da00d824\", \"845c9918-94d7-430c-b3d8-eafafc215fd9\"],\n            \"contains\": \"${event.targetResource.id}\"\n          }]\n        }\n    },\n    \"riskPolicies\": [{\n        \"name\" : \"USER_LOCATION_ANOMALY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"CUSTOM\",\n            \"customAction\" : \"CustomActionForUserLocationAnomaly\"\n          }],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userLocationAnomaly.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"VELOCITY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY_AND_SUSPEND\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipVelocityByUser.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },{\n        \"name\" : \"USER_RISK_BEHAVIOR\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"VERIFY\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userBasedRiskBehavior.level}\",\n          \"equals\" : \"Medium\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"EMAIL_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"MFA\",\n            \"mfaAuthenticationPolicyId\" : \"{{deviceAuthenticationPolicyID}}\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.emailReputation.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"IP_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"APPROVE\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipRisk.level}\",\n          \"equals\" : \"Low\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n    },\n    {\n        \"name\": \"Medium scored policy\",\n        \"result\": {\n            \"level\": \"MEDIUM\"\n        },\n        \"condition\": {\n            \"type\": \"AGGREGATED_SCORES\",\n            \"aggregatedScores\": [\n                {\n                    \"value\": \"${details.userLocationAnomaly.level}\",\n                    \"score\": 40\n                },\n                {\n                    \"value\": \"${details.anonymousNetwork.level}\",\n                    \"score\": 60\n                },\n                {\n                    \"value\": \"${details.ipRisk.level}\",\n                    \"score\": 40\n                }\n            ],\n            \"between\": {\n                \"minScore\": 700,\n                \"maxScore\": 900\n            }\n        }\n    },\n    {\n        \"name\": \"High scored policy\",\n        \"result\": {\n            \"level\": \"HIGH\"\n        },\n        \"condition\": {\n            \"type\": \"AGGREGATED_SCORES\",\n            \"aggregatedScores\": [\n                {\n                    \"value\": \"${details.userLocationAnomaly.level}\",\n                    \"score\": 40\n                },\n                {\n                    \"value\": \"${details.anonymousNetwork.level}\",\n                    \"score\": 60\n                },\n                {\n                    \"value\": \"${details.ipRisk.level}\",\n                    \"score\": 40\n                }\n            ],\n            \"between\": {\n                \"minScore\": 900,\n                \"maxScore\": 1000\n            }\n        }\n        },\n        {\n        \"name\" : \"FALLBACK\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY\"\n          } ],\n          \"type\" : \"MITIGATION_FALLBACK\"\n        }\n      } \n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Targeted policy with mitigations",
    "defaultResult": {
      "level": "Low"
    },
    "targets": {
      "condition": {
        "and": [
          {
            "list": [
              "AUTHENTICATION",
              "AUTHORIZATION"
            ],
            "contains": "${event.flow.type}"
          },
          {
            "list": [
              "Sales"
            ],
            "contains": "${event.user.groups}"
          },
          {
            "list": [
              "6b6f867b-d768-4c2c-a9b6-6816da00d824",
              "845c9918-94d7-430c-b3d8-eafafc215fd9"
            ],
            "contains": "${event.targetResource.id}"
          }
        ]
      }
    },
    "riskPolicies": [
      {
        "name": "USER_LOCATION_ANOMALY",
        "result": {
          "mitigations": [
            {
              "action": "CUSTOM",
              "customAction": "CustomActionForUserLocationAnomaly"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userLocationAnomaly.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "VELOCITY",
        "result": {
          "mitigations": [
            {
              "action": "DENY_AND_SUSPEND"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipVelocityByUser.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "USER_RISK_BEHAVIOR",
        "result": {
          "mitigations": [
            {
              "action": "VERIFY"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userBasedRiskBehavior.level}",
          "equals": "Medium",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "EMAIL_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "MFA",
              "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.emailReputation.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "IP_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "APPROVE"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipRisk.level}",
          "equals": "Low",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "Medium scored policy",
        "result": {
          "level": "MEDIUM"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 700,
            "maxScore": 900
          }
        }
      },
      {
        "name": "High scored policy",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 900,
            "maxScore": 1000
          }
        }
      },
      {
        "name": "FALLBACK",
        "result": {
          "mitigations": [
            {
              "action": "DENY"
            }
          ],
          "type": "MITIGATION_FALLBACK"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Targeted policy with mitigations",
    "defaultResult": {
      "level": "Low"
    },
    "targets": {
      "condition": {
        "and": [
          {
            "list": [
              "AUTHENTICATION",
              "AUTHORIZATION"
            ],
            "contains": "${event.flow.type}"
          },
          {
            "list": [
              "Sales"
            ],
            "contains": "${event.user.groups}"
          },
          {
            "list": [
              "6b6f867b-d768-4c2c-a9b6-6816da00d824",
              "845c9918-94d7-430c-b3d8-eafafc215fd9"
            ],
            "contains": "${event.targetResource.id}"
          }
        ]
      }
    },
    "riskPolicies": [
      {
        "name": "USER_LOCATION_ANOMALY",
        "result": {
          "mitigations": [
            {
              "action": "CUSTOM",
              "customAction": "CustomActionForUserLocationAnomaly"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userLocationAnomaly.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "VELOCITY",
        "result": {
          "mitigations": [
            {
              "action": "DENY_AND_SUSPEND"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipVelocityByUser.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "USER_RISK_BEHAVIOR",
        "result": {
          "mitigations": [
            {
              "action": "VERIFY"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.userBasedRiskBehavior.level}",
          "equals": "Medium",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "EMAIL_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "MFA",
              "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.emailReputation.level}",
          "equals": "High",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "IP_REPUTATION",
        "result": {
          "mitigations": [
            {
              "action": "APPROVE"
            }
          ],
          "type": "MITIGATION"
        },
        "condition": {
          "value": "${details.ipRisk.level}",
          "equals": "Low",
          "type": "VALUE_COMPARISON"
        }
      },
      {
        "name": "Medium scored policy",
        "result": {
          "level": "MEDIUM"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 700,
            "maxScore": 900
          }
        }
      },
      {
        "name": "High scored policy",
        "result": {
          "level": "HIGH"
        },
        "condition": {
          "type": "AGGREGATED_SCORES",
          "aggregatedScores": [
            {
              "value": "${details.userLocationAnomaly.level}",
              "score": 40
            },
            {
              "value": "${details.anonymousNetwork.level}",
              "score": 60
            },
            {
              "value": "${details.ipRisk.level}",
              "score": 40
            }
          ],
          "between": {
            "minScore": 900,
            "maxScore": 1000
          }
        }
      },
      {
        "name": "FALLBACK",
        "result": {
          "mitigations": [
            {
              "action": "DENY"
            }
          ],
          "type": "MITIGATION_FALLBACK"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets"

payload = json.dumps({
  "name": "Targeted policy with mitigations",
  "defaultResult": {
    "level": "Low"
  },
  "targets": {
    "condition": {
      "and": [
        {
          "list": [
            "AUTHENTICATION",
            "AUTHORIZATION"
          ],
          "contains": "${event.flow.type}"
        },
        {
          "list": [
            "Sales"
          ],
          "contains": "${event.user.groups}"
        },
        {
          "list": [
            "6b6f867b-d768-4c2c-a9b6-6816da00d824",
            "845c9918-94d7-430c-b3d8-eafafc215fd9"
          ],
          "contains": "${event.targetResource.id}"
        }
      ]
    }
  },
  "riskPolicies": [
    {
      "name": "USER_LOCATION_ANOMALY",
      "result": {
        "mitigations": [
          {
            "action": "CUSTOM",
            "customAction": "CustomActionForUserLocationAnomaly"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.userLocationAnomaly.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "VELOCITY",
      "result": {
        "mitigations": [
          {
            "action": "DENY_AND_SUSPEND"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.ipVelocityByUser.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "USER_RISK_BEHAVIOR",
      "result": {
        "mitigations": [
          {
            "action": "VERIFY"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.userBasedRiskBehavior.level}",
        "equals": "Medium",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "EMAIL_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "MFA",
            "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.emailReputation.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "IP_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "APPROVE"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "${details.ipRisk.level}",
        "equals": "Low",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "Medium scored policy",
      "result": {
        "level": "MEDIUM"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 700,
          "maxScore": 900
        }
      }
    },
    {
      "name": "High scored policy",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 900,
          "maxScore": 1000
        }
      }
    },
    {
      "name": "FALLBACK",
      "result": {
        "mitigations": [
          {
            "action": "DENY"
          }
        ],
        "type": "MITIGATION_FALLBACK"
      }
    }
  ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPolicySets');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Targeted policy with mitigations",\n    "defaultResult": {\n        "level": "Low"\n    },\n    "targets":{\n        "condition": { "and": [{\n            "list": ["AUTHENTICATION", "AUTHORIZATION"],\n            "contains": "${event.flow.type}"\n          },\n          { \n            "list": ["Sales"],\n            "contains": "${event.user.groups}"\n          },\n          { \n            "list": ["6b6f867b-d768-4c2c-a9b6-6816da00d824", "845c9918-94d7-430c-b3d8-eafafc215fd9"],\n            "contains": "${event.targetResource.id}"\n          }]\n        }\n    },\n    "riskPolicies": [{\n        "name" : "USER_LOCATION_ANOMALY",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "CUSTOM",\n            "customAction" : "CustomActionForUserLocationAnomaly"\n          }],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.userLocationAnomaly.level}",\n          "equals" : "High",\n          "type" : "VALUE_COMPARISON"\n        }\n      },\n      {\n        "name" : "VELOCITY",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "DENY_AND_SUSPEND"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.ipVelocityByUser.level}",\n          "equals" : "High",\n          "type" : "VALUE_COMPARISON"\n        }\n      },{\n        "name" : "USER_RISK_BEHAVIOR",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "VERIFY"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.userBasedRiskBehavior.level}",\n          "equals" : "Medium",\n          "type" : "VALUE_COMPARISON"\n        }\n      },\n      {\n        "name" : "EMAIL_REPUTATION",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "MFA",\n            "mfaAuthenticationPolicyId" : "{{deviceAuthenticationPolicyID}}"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.emailReputation.level}",\n          "equals" : "High",\n          "type" : "VALUE_COMPARISON"\n        }\n      },\n      {\n        "name" : "IP_REPUTATION",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "APPROVE"\n          } ],\n          "type" : "MITIGATION"\n        },\n        "condition" : {\n          "value" : "${details.ipRisk.level}",\n          "equals" : "Low",\n          "type" : "VALUE_COMPARISON"\n        }\n    },\n    {\n        "name": "Medium scored policy",\n        "result": {\n            "level": "MEDIUM"\n        },\n        "condition": {\n            "type": "AGGREGATED_SCORES",\n            "aggregatedScores": [\n                {\n                    "value": "${details.userLocationAnomaly.level}",\n                    "score": 40\n                },\n                {\n                    "value": "${details.anonymousNetwork.level}",\n                    "score": 60\n                },\n                {\n                    "value": "${details.ipRisk.level}",\n                    "score": 40\n                }\n            ],\n            "between": {\n                "minScore": 700,\n                "maxScore": 900\n            }\n        }\n    },\n    {\n        "name": "High scored policy",\n        "result": {\n            "level": "HIGH"\n        },\n        "condition": {\n            "type": "AGGREGATED_SCORES",\n            "aggregatedScores": [\n                {\n                    "value": "${details.userLocationAnomaly.level}",\n                    "score": 40\n                },\n                {\n                    "value": "${details.anonymousNetwork.level}",\n                    "score": 60\n                },\n                {\n                    "value": "${details.ipRisk.level}",\n                    "score": 40\n                }\n            ],\n            "between": {\n                "minScore": 900,\n                "maxScore": 1000\n            }\n        }\n        },\n        {\n        "name" : "FALLBACK",\n        "result" : {\n          "mitigations" : [ {\n            "action" : "DENY"\n          } ],\n          "type" : "MITIGATION_FALLBACK"\n        }\n      } \n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Targeted policy with mitigations",
  "defaultResult": {
    "level": "Low"
  },
  "targets": {
    "condition": {
      "and": [
        {
          "list": [
            "AUTHENTICATION",
            "AUTHORIZATION"
          ],
          "contains": "\${event.flow.type}"
        },
        {
          "list": [
            "Sales"
          ],
          "contains": "\${event.user.groups}"
        },
        {
          "list": [
            "6b6f867b-d768-4c2c-a9b6-6816da00d824",
            "845c9918-94d7-430c-b3d8-eafafc215fd9"
          ],
          "contains": "\${event.targetResource.id}"
        }
      ]
    }
  },
  "riskPolicies": [
    {
      "name": "USER_LOCATION_ANOMALY",
      "result": {
        "mitigations": [
          {
            "action": "CUSTOM",
            "customAction": "CustomActionForUserLocationAnomaly"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.userLocationAnomaly.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "VELOCITY",
      "result": {
        "mitigations": [
          {
            "action": "DENY_AND_SUSPEND"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.ipVelocityByUser.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "USER_RISK_BEHAVIOR",
      "result": {
        "mitigations": [
          {
            "action": "VERIFY"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.userBasedRiskBehavior.level}",
        "equals": "Medium",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "EMAIL_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "MFA",
            "mfaAuthenticationPolicyId": "{{deviceAuthenticationPolicyID}}"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.emailReputation.level}",
        "equals": "High",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "IP_REPUTATION",
      "result": {
        "mitigations": [
          {
            "action": "APPROVE"
          }
        ],
        "type": "MITIGATION"
      },
      "condition": {
        "value": "\${details.ipRisk.level}",
        "equals": "Low",
        "type": "VALUE_COMPARISON"
      }
    },
    {
      "name": "Medium scored policy",
      "result": {
        "level": "MEDIUM"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "\${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "\${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "\${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 700,
          "maxScore": 900
        }
      }
    },
    {
      "name": "High scored policy",
      "result": {
        "level": "HIGH"
      },
      "condition": {
        "type": "AGGREGATED_SCORES",
        "aggregatedScores": [
          {
            "value": "\${details.userLocationAnomaly.level}",
            "score": 40
          },
          {
            "value": "\${details.anonymousNetwork.level}",
            "score": 60
          },
          {
            "value": "\${details.ipRisk.level}",
            "score": 40
          }
        ],
        "between": {
          "minScore": 900,
          "maxScore": 1000
        }
      }
    },
    {
      "name": "FALLBACK",
      "result": {
        "mitigations": [
          {
            "action": "DENY"
          }
        ],
        "type": "MITIGATION_FALLBACK"
      }
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Targeted policy with mitigations\",\n    \"defaultResult\": {\n        \"level\": \"Low\"\n    },\n    \"targets\":{\n        \"condition\": { \"and\": [{\n            \"list\": [\"AUTHENTICATION\", \"AUTHORIZATION\"],\n            \"contains\": \"${event.flow.type}\"\n          },\n          { \n            \"list\": [\"Sales\"],\n            \"contains\": \"${event.user.groups}\"\n          },\n          { \n            \"list\": [\"6b6f867b-d768-4c2c-a9b6-6816da00d824\", \"845c9918-94d7-430c-b3d8-eafafc215fd9\"],\n            \"contains\": \"${event.targetResource.id}\"\n          }]\n        }\n    },\n    \"riskPolicies\": [{\n        \"name\" : \"USER_LOCATION_ANOMALY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"CUSTOM\",\n            \"customAction\" : \"CustomActionForUserLocationAnomaly\"\n          }],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userLocationAnomaly.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"VELOCITY\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY_AND_SUSPEND\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipVelocityByUser.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },{\n        \"name\" : \"USER_RISK_BEHAVIOR\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"VERIFY\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.userBasedRiskBehavior.level}\",\n          \"equals\" : \"Medium\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"EMAIL_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"MFA\",\n            \"mfaAuthenticationPolicyId\" : \"{{deviceAuthenticationPolicyID}}\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.emailReputation.level}\",\n          \"equals\" : \"High\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n      },\n      {\n        \"name\" : \"IP_REPUTATION\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"APPROVE\"\n          } ],\n          \"type\" : \"MITIGATION\"\n        },\n        \"condition\" : {\n          \"value\" : \"${details.ipRisk.level}\",\n          \"equals\" : \"Low\",\n          \"type\" : \"VALUE_COMPARISON\"\n        }\n    },\n    {\n        \"name\": \"Medium scored policy\",\n        \"result\": {\n            \"level\": \"MEDIUM\"\n        },\n        \"condition\": {\n            \"type\": \"AGGREGATED_SCORES\",\n            \"aggregatedScores\": [\n                {\n                    \"value\": \"${details.userLocationAnomaly.level}\",\n                    \"score\": 40\n                },\n                {\n                    \"value\": \"${details.anonymousNetwork.level}\",\n                    \"score\": 60\n                },\n                {\n                    \"value\": \"${details.ipRisk.level}\",\n                    \"score\": 40\n                }\n            ],\n            \"between\": {\n                \"minScore\": 700,\n                \"maxScore\": 900\n            }\n        }\n    },\n    {\n        \"name\": \"High scored policy\",\n        \"result\": {\n            \"level\": \"HIGH\"\n        },\n        \"condition\": {\n            \"type\": \"AGGREGATED_SCORES\",\n            \"aggregatedScores\": [\n                {\n                    \"value\": \"${details.userLocationAnomaly.level}\",\n                    \"score\": 40\n                },\n                {\n                    \"value\": \"${details.anonymousNetwork.level}\",\n                    \"score\": 60\n                },\n                {\n                    \"value\": \"${details.ipRisk.level}\",\n                    \"score\": 40\n                }\n            ],\n            \"between\": {\n                \"minScore\": 900,\n                \"maxScore\": 1000\n            }\n        }\n        },\n        {\n        \"name\" : \"FALLBACK\",\n        \"result\" : {\n          \"mitigations\" : [ {\n            \"action\" : \"DENY\"\n          } ],\n          \"type\" : \"MITIGATION_FALLBACK\"\n        }\n      } \n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets")!,timeoutInterval: Double.infinity)
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

#### Example Response

201 Created

```json
{
    "_links": {
        "self": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPolicySets/a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Targeted policy with mitigations",
    "createdAt": "2025-06-08T10:15:46.467Z",
    "updatedAt": "2025-06-08T10:15:46.467Z",
    "defaultResult": {
        "level": "LOW",
        "type": "VALUE"
    },
    "targets": {
        "condition": {
            "and": [
                {
                    "list": [
                        "AUTHENTICATION",
                        "AUTHORIZATION"
                    ],
                    "contains": "${event.flow.type}",
                    "type": "STRING_LIST"
                },
                {
                    "list": [
                        "Sales"
                    ],
                    "contains": "${event.user.groups}",
                    "type": "GROUPS_INTERSECTION"
                },
                {
                    "list": [
                        "6b6f867b-d768-4c2c-a9b6-6816da00d824",
                        "845c9918-94d7-430c-b3d8-eafafc215fd9"
                    ],
                    "contains": "${event.targetResource.id}",
                    "type": "STRING_LIST"
                }
            ],
            "type": "AND"
        }
    },
    "riskPolicies": [
        {
            "id": "c4f4a620-c795-4b98-8674-a8b112120c2e",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "USER_LOCATION_ANOMALY",
            "priority": 1,
            "result": {
                "mitigations": [
                    {
                        "action": "CUSTOM",
                        "customAction": "CustomActionForUserLocationAnomaly"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "High",
                "value": "${details.userLocationAnomaly.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        },
        {
            "id": "a8e30812-64c4-45af-a64f-95d7e421c0fe",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "VELOCITY",
            "priority": 2,
            "result": {
                "mitigations": [
                    {
                        "action": "DENY_AND_SUSPEND"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "High",
                "value": "${details.ipVelocityByUser.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        },
        {
            "id": "900278ed-f80b-4fdf-b429-6fd250732f0d",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "USER_RISK_BEHAVIOR",
            "priority": 3,
            "result": {
                "mitigations": [
                    {
                        "action": "VERIFY"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "Medium",
                "value": "${details.userBasedRiskBehavior.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        },
        {
            "id": "388b2703-a0f0-46f1-be6f-d20ef0e654ca",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "EMAIL_REPUTATION",
            "priority": 4,
            "result": {
                "mitigations": [
                    {
                        "action": "MFA",
                        "mfaAuthenticationPolicyId": "a3e7a1d1-90ea-4e63-aa81-23383ba1c004"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "High",
                "value": "${details.emailReputation.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        },
        {
            "id": "65260390-81df-4e44-94f3-4ea39a1234b1",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "IP_REPUTATION",
            "priority": 5,
            "result": {
                "mitigations": [
                    {
                        "action": "APPROVE"
                    }
                ],
                "type": "MITIGATION"
            },
            "condition": {
                "equals": "Low",
                "value": "${details.ipRisk.level}",
                "type": "VALUE_COMPARISON"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        },
        {
            "id": "0d4bb94c-55d9-4b3f-864f-23f8a8707b95",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "Medium scored policy",
            "priority": 7,
            "result": {
                "level": "MEDIUM",
                "type": "VALUE"
            },
            "condition": {
                "between": {
                    "minScore": 700,
                    "maxScore": 900
                },
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "type": "AGGREGATED_SCORES"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        },
        {
            "id": "83bdc5fd-92f4-4174-9a2b-644fcfc44ce3",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "High scored policy",
            "priority": 6,
            "result": {
                "level": "HIGH",
                "type": "VALUE"
            },
            "condition": {
                "between": {
                    "minScore": 900,
                    "maxScore": 1000
                },
                "aggregatedScores": [
                    {
                        "value": "${details.userLocationAnomaly.level}",
                        "score": 40
                    },
                    {
                        "value": "${details.anonymousNetwork.level}",
                        "score": 60
                    },
                    {
                        "value": "${details.ipRisk.level}",
                        "score": 40
                    }
                ],
                "type": "AGGREGATED_SCORES"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        },
        {
            "id": "33e76625-22fc-4bd8-9c16-9f9e4060d65d",
            "environment": {
                "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
            },
            "policySet": {
                "id": "a5a076d4-4182-4aa5-8fbd-d2ce5502af3d"
            },
            "name": "FALLBACK",
            "result": {
                "mitigations": [
                    {
                        "action": "DENY"
                    }
                ],
                "type": "MITIGATION_FALLBACK"
            },
            "createdAt": "2025-06-08T10:15:46.467Z",
            "updatedAt": "2025-06-08T10:15:46.467Z"
        }
    ],
    "default": false
}
```

---

---
title: Create Risk Predictor (Composite with country and user group)
description: This request creates a composite predictor that includes a condition that takes into account what user groups the user belongs to.
component: pingone-api
page_id: pingone-api:protect:risk-predictors/create_risk_predictor_composite_with_user_group
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/create_risk_predictor_composite_with_user_group.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Predictor (Composite with country and user group)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPredictors
```

This request creates a composite predictor that includes a condition that takes into account what user groups the user belongs to.

The `compositions` array contains a number of condition sets.

The first set of conditions specify that the composite predictor should be assigned a risk level of High if any of the following conditions are met:

* The `anonymousNetwork` predictor is determined to be high risk.

* Any three predictors in the policy being evaluated are found to be high risk.

* The user is requesting access from a country other than Italy or Germany.

If none of the above conditions are met, the second object in the `compositions` array specifies that if the `userLocationAnomaly` predictor is determined to be high risk, and the user is not a member of the `networkAdmins` group, then the composite predictor should be assigned a risk level of Medium.

If the second set of conditions is also not met, the composite predictor should be assigned a risk level of Low (`default.result.level`).

### Prerequisites

* Refer to [Risk Predictors](#risk-predictors) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for the complete data models.
>
> **Base data model**
>
> | Property               | Type    | Required |
> | ---------------------- | ------- | -------- |
> | `compactName`          | String  | Required |
> | `default`              | Object  | Required |
> | `default.weight`       | Integer | Required |
> | `default.result`       | Object  | Required |
> | `default.result.level` | String  | Required |
> | `description`          | String  | Optional |
> | `licensed`             | Boolean | Required |
> | `name`                 | String  | Required |
> | `reason`               | String  | Required |
> | `type`                 | String  | Required |
> | `whiteList`            | List\[] | Optional |
>
> **Composite data model**
>
> | Property                   | Type   | Required |
> | -------------------------- | ------ | -------- |
> | `compositions`             | Array  | Required |
> | `compositions[].condition` | Object | Required |
> | `compositions[].level`     | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Composite - including country and user groups",
    "compactName": "compositeWithCountryAndUserGroups",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "list":["networkAdmins"],
                        "notContains":"${event.user.groups}",
                        "type":"GROUPS_INTERSECTION"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPredictors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Composite - including country and user groups",
    "compactName": "compositeWithCountryAndUserGroups",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "list":["networkAdmins"],
                        "notContains":"${event.user.groups}",
                        "type":"GROUPS_INTERSECTION"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
        }
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Composite - including country and user groups""," + "\n" +
@"    ""compactName"": ""compositeWithCountryAndUserGroups""," + "\n" +
@"    ""licensed"": true," + "\n" +
@"    ""compositions"": [" + "\n" +
@"        {" + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""or"": [" + "\n" +
@"                    {" + "\n" +
@"                        ""equals"": 3," + "\n" +
@"                        ""value"": ""${details.counters.predictorLevels.high}""," + "\n" +
@"                        ""type"": ""VALUE_COMPARISON""" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""equals"": ""HIGH""," + "\n" +
@"                        ""value"": ""${details.anonymousNetwork.level}""," + "\n" +
@"                        ""type"": ""VALUE_COMPARISON""" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""type"": ""STRING_LIST""," + "\n" +
@"                        ""list"": [" + "\n" +
@"                            ""Italy""," + "\n" +
@"                            ""Germany""" + "\n" +
@"                        ]," + "\n" +
@"                        ""notContains"": ""${details.country}""" + "\n" +
@"                    }" + "\n" +
@"                ]" + "\n" +
@"            }," + "\n" +
@"            ""level"": ""HIGH""" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""and"": [" + "\n" +
@"                    {" + "\n" +
@"                        ""equals"": ""HIGH""," + "\n" +
@"                        ""value"": ""${details.userLocationAnomaly.level}""," + "\n" +
@"                        ""type"": ""VALUE_COMPARISON""" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""list"":[""networkAdmins""]," + "\n" +
@"                        ""notContains"":""${event.user.groups}""," + "\n" +
@"                        ""type"":""GROUPS_INTERSECTION""" + "\n" +
@"                    }" + "\n" +
@"                ]" + "\n" +
@"            }," + "\n" +
@"            ""level"": ""MEDIUM""" + "\n" +
@"        }    " + "\n" +
@"    ]," + "\n" +
@"    ""type"": ""COMPOSITE""," + "\n" +
@"    ""default"": {" + "\n" +
@"        ""weight"": 5," + "\n" +
@"        ""score"": 50," + "\n" +
@"        ""result"": {" + "\n" +
@"            ""level"": ""LOW""," + "\n" +
@"            ""type"": ""VALUE""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Composite - including country and user groups",
    "compactName": "compositeWithCountryAndUserGroups",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "list":["networkAdmins"],
                        "notContains":"${event.user.groups}",
                        "type":"GROUPS_INTERSECTION"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
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
POST /v1/environments/{{envID}}/riskPredictors HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Composite - including country and user groups",
    "compactName": "compositeWithCountryAndUserGroups",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "list":["networkAdmins"],
                        "notContains":"${event.user.groups}",
                        "type":"GROUPS_INTERSECTION"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
        }
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Composite - including country and user groups\",\n    \"compactName\": \"compositeWithCountryAndUserGroups\",\n    \"licensed\": true,\n    \"compositions\": [\n        {\n            \"condition\": {\n                \"or\": [\n                    {\n                        \"equals\": 3,\n                        \"value\": \"${details.counters.predictorLevels.high}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"type\": \"STRING_LIST\",\n                        \"list\": [\n                            \"Italy\",\n                            \"Germany\"\n                        ],\n                        \"notContains\": \"${details.country}\"\n                    }\n                ]\n            },\n            \"level\": \"HIGH\"\n        },\n        {\n            \"condition\": {\n                \"and\": [\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"list\":[\"networkAdmins\"],\n                        \"notContains\":\"${event.user.groups}\",\n                        \"type\":\"GROUPS_INTERSECTION\"\n                    }\n                ]\n            },\n            \"level\": \"MEDIUM\"\n        }    \n    ],\n    \"type\": \"COMPOSITE\",\n    \"default\": {\n        \"weight\": 5,\n        \"score\": 50,\n        \"result\": {\n            \"level\": \"LOW\",\n            \"type\": \"VALUE\"\n        }\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Composite - including country and user groups",
    "compactName": "compositeWithCountryAndUserGroups",
    "licensed": true,
    "compositions": [
      {
        "condition": {
          "or": [
            {
              "equals": 3,
              "value": "${details.counters.predictorLevels.high}",
              "type": "VALUE_COMPARISON"
            },
            {
              "equals": "HIGH",
              "value": "${details.anonymousNetwork.level}",
              "type": "VALUE_COMPARISON"
            },
            {
              "type": "STRING_LIST",
              "list": [
                "Italy",
                "Germany"
              ],
              "notContains": "${details.country}"
            }
          ]
        },
        "level": "HIGH"
      },
      {
        "condition": {
          "and": [
            {
              "equals": "HIGH",
              "value": "${details.userLocationAnomaly.level}",
              "type": "VALUE_COMPARISON"
            },
            {
              "list": [
                "networkAdmins"
              ],
              "notContains": "${event.user.groups}",
              "type": "GROUPS_INTERSECTION"
            }
          ]
        },
        "level": "MEDIUM"
      }
    ],
    "type": "COMPOSITE",
    "default": {
      "weight": 5,
      "score": 50,
      "result": {
        "level": "LOW",
        "type": "VALUE"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Composite - including country and user groups",
    "compactName": "compositeWithCountryAndUserGroups",
    "licensed": true,
    "compositions": [
      {
        "condition": {
          "or": [
            {
              "equals": 3,
              "value": "${details.counters.predictorLevels.high}",
              "type": "VALUE_COMPARISON"
            },
            {
              "equals": "HIGH",
              "value": "${details.anonymousNetwork.level}",
              "type": "VALUE_COMPARISON"
            },
            {
              "type": "STRING_LIST",
              "list": [
                "Italy",
                "Germany"
              ],
              "notContains": "${details.country}"
            }
          ]
        },
        "level": "HIGH"
      },
      {
        "condition": {
          "and": [
            {
              "equals": "HIGH",
              "value": "${details.userLocationAnomaly.level}",
              "type": "VALUE_COMPARISON"
            },
            {
              "list": [
                "networkAdmins"
              ],
              "notContains": "${event.user.groups}",
              "type": "GROUPS_INTERSECTION"
            }
          ]
        },
        "level": "MEDIUM"
      }
    ],
    "type": "COMPOSITE",
    "default": {
      "weight": 5,
      "score": 50,
      "result": {
        "level": "LOW",
        "type": "VALUE"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"

payload = json.dumps({
  "name": "Composite - including country and user groups",
  "compactName": "compositeWithCountryAndUserGroups",
  "licensed": True,
  "compositions": [
    {
      "condition": {
        "or": [
          {
            "equals": 3,
            "value": "${details.counters.predictorLevels.high}",
            "type": "VALUE_COMPARISON"
          },
          {
            "equals": "HIGH",
            "value": "${details.anonymousNetwork.level}",
            "type": "VALUE_COMPARISON"
          },
          {
            "type": "STRING_LIST",
            "list": [
              "Italy",
              "Germany"
            ],
            "notContains": "${details.country}"
          }
        ]
      },
      "level": "HIGH"
    },
    {
      "condition": {
        "and": [
          {
            "equals": "HIGH",
            "value": "${details.userLocationAnomaly.level}",
            "type": "VALUE_COMPARISON"
          },
          {
            "list": [
              "networkAdmins"
            ],
            "notContains": "${event.user.groups}",
            "type": "GROUPS_INTERSECTION"
          }
        ]
      },
      "level": "MEDIUM"
    }
  ],
  "type": "COMPOSITE",
  "default": {
    "weight": 5,
    "score": 50,
    "result": {
      "level": "LOW",
      "type": "VALUE"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Composite - including country and user groups",\n    "compactName": "compositeWithCountryAndUserGroups",\n    "licensed": true,\n    "compositions": [\n        {\n            "condition": {\n                "or": [\n                    {\n                        "equals": 3,\n                        "value": "${details.counters.predictorLevels.high}",\n                        "type": "VALUE_COMPARISON"\n                    },\n                    {\n                        "equals": "HIGH",\n                        "value": "${details.anonymousNetwork.level}",\n                        "type": "VALUE_COMPARISON"\n                    },\n                    {\n                        "type": "STRING_LIST",\n                        "list": [\n                            "Italy",\n                            "Germany"\n                        ],\n                        "notContains": "${details.country}"\n                    }\n                ]\n            },\n            "level": "HIGH"\n        },\n        {\n            "condition": {\n                "and": [\n                    {\n                        "equals": "HIGH",\n                        "value": "${details.userLocationAnomaly.level}",\n                        "type": "VALUE_COMPARISON"\n                    },\n                    {\n                        "list":["networkAdmins"],\n                        "notContains":"${event.user.groups}",\n                        "type":"GROUPS_INTERSECTION"\n                    }\n                ]\n            },\n            "level": "MEDIUM"\n        }    \n    ],\n    "type": "COMPOSITE",\n    "default": {\n        "weight": 5,\n        "score": 50,\n        "result": {\n            "level": "LOW",\n            "type": "VALUE"\n        }\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Composite - including country and user groups",
  "compactName": "compositeWithCountryAndUserGroups",
  "licensed": true,
  "compositions": [
    {
      "condition": {
        "or": [
          {
            "equals": 3,
            "value": "\${details.counters.predictorLevels.high}",
            "type": "VALUE_COMPARISON"
          },
          {
            "equals": "HIGH",
            "value": "\${details.anonymousNetwork.level}",
            "type": "VALUE_COMPARISON"
          },
          {
            "type": "STRING_LIST",
            "list": [
              "Italy",
              "Germany"
            ],
            "notContains": "\${details.country}"
          }
        ]
      },
      "level": "HIGH"
    },
    {
      "condition": {
        "and": [
          {
            "equals": "HIGH",
            "value": "\${details.userLocationAnomaly.level}",
            "type": "VALUE_COMPARISON"
          },
          {
            "list": [
              "networkAdmins"
            ],
            "notContains": "\${event.user.groups}",
            "type": "GROUPS_INTERSECTION"
          }
        ]
      },
      "level": "MEDIUM"
    }
  ],
  "type": "COMPOSITE",
  "default": {
    "weight": 5,
    "score": 50,
    "result": {
      "level": "LOW",
      "type": "VALUE"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Composite - including country and user groups\",\n    \"compactName\": \"compositeWithCountryAndUserGroups\",\n    \"licensed\": true,\n    \"compositions\": [\n        {\n            \"condition\": {\n                \"or\": [\n                    {\n                        \"equals\": 3,\n                        \"value\": \"${details.counters.predictorLevels.high}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"type\": \"STRING_LIST\",\n                        \"list\": [\n                            \"Italy\",\n                            \"Germany\"\n                        ],\n                        \"notContains\": \"${details.country}\"\n                    }\n                ]\n            },\n            \"level\": \"HIGH\"\n        },\n        {\n            \"condition\": {\n                \"and\": [\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"list\":[\"networkAdmins\"],\n                        \"notContains\":\"${event.user.groups}\",\n                        \"type\":\"GROUPS_INTERSECTION\"\n                    }\n                ]\n            },\n            \"level\": \"MEDIUM\"\n        }    \n    ],\n    \"type\": \"COMPOSITE\",\n    \"default\": {\n        \"weight\": 5,\n        \"score\": 50,\n        \"result\": {\n            \"level\": \"LOW\",\n            \"type\": \"VALUE\"\n        }\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPredictors/abfbd59d-c390-4acf-bd74-305973ed9b7c"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "abfbd59d-c390-4acf-bd74-305973ed9b7c",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2024-07-21T15:27:58.924Z",
    "createdBy": "USER_DEFINED",
    "updatedAt": "2024-07-21T15:27:58.924Z",
    "name": "Composite - including country and user groups",
    "compactName": "compositeWithCountryAndUserGroups",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}",
                        "type": "STRING_LIST"
                    }
                ],
                "type": "OR"
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "list": [
                            "networkAdmins"
                        ],
                        "notContains": "${event.user.groups}",
                        "type": "GROUPS_INTERSECTION"
                    }
                ],
                "type": "AND"
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "composition": {
        "condition": {
            "or": [
                {
                    "equals": 3,
                    "value": "${details.counters.predictorLevels.high}",
                    "type": "VALUE_COMPARISON"
                },
                {
                    "equals": "HIGH",
                    "value": "${details.anonymousNetwork.level}",
                    "type": "VALUE_COMPARISON"
                },
                {
                    "list": [
                        "Italy",
                        "Germany"
                    ],
                    "notContains": "${details.country}",
                    "type": "STRING_LIST"
                }
            ],
            "type": "OR"
        },
        "level": "HIGH"
    },
    "condition": {
        "scores": [
            {
                "name": "HIGH",
                "value": "HIGH"
            },
            {
                "name": "MEDIUM",
                "value": "MEDIUM"
            },
            {
                "name": "LOW",
                "value": "LOW"
            }
        ]
    },
    "tooltip": "predictor.tooltip.composite",
    "deletable": true,
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
        },
        "evaluated": false
    }
}
```

---

---
title: Create Risk Predictor (Composite with country)
description: This request creates a composite predictor.
component: pingone-api
page_id: pingone-api:protect:risk-predictors/create_risk_predictor_composite
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/create_risk_predictor_composite.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Predictor (Composite with country)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPredictors
```

This request creates a composite predictor.

The `compositions` array contains a number of condition sets.

The first set of conditions specify that the composite predictor should be assigned a risk level of High if any of the following conditions are met:

* The `anonymousNetwork` predictor is determined to be high risk.

* Any three predictors in the policy being evaluated are found to be high risk.

* The user is requesting access from a country other than Italy or Germany.

If none of the above conditions are met, the second object in the `compositions` array specifies that if the `userLocationAnomaly` predictor is determined to be high risk, then the composite predictor should be assigned a risk level of Medium.

If the condition for the `userLocationAnomaly` predictor is also not met, the composite predictor should be assigned a risk level of Low (`default.result.level`).

### Prerequisites

* Refer to [Risk Predictors](#risk-predictors) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for the complete data models.
>
> **Base data model**
>
> | Property               | Type    | Required |
> | ---------------------- | ------- | -------- |
> | `compactName`          | String  | Required |
> | `default`              | Object  | Required |
> | `default.weight`       | Integer | Required |
> | `default.result`       | Object  | Required |
> | `default.result.level` | String  | Required |
> | `description`          | String  | Optional |
> | `licensed`             | Boolean | Required |
> | `name`                 | String  | Required |
> | `reason`               | String  | Required |
> | `type`                 | String  | Required |
> | `whiteList`            | List\[] | Optional |
>
> **Composite data model**
>
> | Property                   | Type   | Required |
> | -------------------------- | ------ | -------- |
> | `compositions`             | Array  | Required |
> | `compositions[].condition` | Object | Required |
> | `compositions[].level`     | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Composite - anonymous network and country",
    "compactName": "compositeAnonymousAndCountry",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPredictors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Composite - anonymous network and country",
    "compactName": "compositeAnonymousAndCountry",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
        }
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Composite - anonymous network and country""," + "\n" +
@"    ""compactName"": ""compositeAnonymousAndCountry""," + "\n" +
@"    ""licensed"": true," + "\n" +
@"    ""compositions"": [" + "\n" +
@"        {" + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""or"": [" + "\n" +
@"                    {" + "\n" +
@"                        ""equals"": 3," + "\n" +
@"                        ""value"": ""${details.counters.predictorLevels.high}""," + "\n" +
@"                        ""type"": ""VALUE_COMPARISON""" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""equals"": ""HIGH""," + "\n" +
@"                        ""value"": ""${details.anonymousNetwork.level}""," + "\n" +
@"                        ""type"": ""VALUE_COMPARISON""" + "\n" +
@"                    }," + "\n" +
@"                    {" + "\n" +
@"                        ""type"": ""STRING_LIST""," + "\n" +
@"                        ""list"": [" + "\n" +
@"                            ""Italy""," + "\n" +
@"                            ""Germany""" + "\n" +
@"                        ]," + "\n" +
@"                        ""notContains"": ""${details.country}""" + "\n" +
@"                    }" + "\n" +
@"                ]" + "\n" +
@"            }," + "\n" +
@"            ""level"": ""HIGH""" + "\n" +
@"        }," + "\n" +
@"        {" + "\n" +
@"            ""condition"": {" + "\n" +
@"                ""and"": [" + "\n" +
@"                    {" + "\n" +
@"                        ""equals"": ""HIGH""," + "\n" +
@"                        ""value"": ""${details.userLocationAnomaly.level}""," + "\n" +
@"                        ""type"": ""VALUE_COMPARISON""" + "\n" +
@"                    }" + "\n" +
@"                ]" + "\n" +
@"            }," + "\n" +
@"            ""level"": ""MEDIUM""" + "\n" +
@"        }    " + "\n" +
@"    ]," + "\n" +
@"    ""type"": ""COMPOSITE""," + "\n" +
@"    ""default"": {" + "\n" +
@"        ""weight"": 5," + "\n" +
@"        ""score"": 50," + "\n" +
@"        ""result"": {" + "\n" +
@"            ""level"": ""LOW""," + "\n" +
@"            ""type"": ""VALUE""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Composite - anonymous network and country",
    "compactName": "compositeAnonymousAndCountry",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
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
POST /v1/environments/{{envID}}/riskPredictors HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Composite - anonymous network and country",
    "compactName": "compositeAnonymousAndCountry",
    "licensed": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "type": "STRING_LIST",
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}"
                    }
                ]
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    }
                ]
            },
            "level": "MEDIUM"
        }
    ],
    "type": "COMPOSITE",
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
        }
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Composite - anonymous network and country\",\n    \"compactName\": \"compositeAnonymousAndCountry\",\n    \"licensed\": true,\n    \"compositions\": [\n        {\n            \"condition\": {\n                \"or\": [\n                    {\n                        \"equals\": 3,\n                        \"value\": \"${details.counters.predictorLevels.high}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"type\": \"STRING_LIST\",\n                        \"list\": [\n                            \"Italy\",\n                            \"Germany\"\n                        ],\n                        \"notContains\": \"${details.country}\"\n                    }\n                ]\n            },\n            \"level\": \"HIGH\"\n        },\n        {\n            \"condition\": {\n                \"and\": [\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    }\n                ]\n            },\n            \"level\": \"MEDIUM\"\n        }    \n    ],\n    \"type\": \"COMPOSITE\",\n    \"default\": {\n        \"weight\": 5,\n        \"score\": 50,\n        \"result\": {\n            \"level\": \"LOW\",\n            \"type\": \"VALUE\"\n        }\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Composite - anonymous network and country",
    "compactName": "compositeAnonymousAndCountry",
    "licensed": true,
    "compositions": [
      {
        "condition": {
          "or": [
            {
              "equals": 3,
              "value": "${details.counters.predictorLevels.high}",
              "type": "VALUE_COMPARISON"
            },
            {
              "equals": "HIGH",
              "value": "${details.anonymousNetwork.level}",
              "type": "VALUE_COMPARISON"
            },
            {
              "type": "STRING_LIST",
              "list": [
                "Italy",
                "Germany"
              ],
              "notContains": "${details.country}"
            }
          ]
        },
        "level": "HIGH"
      },
      {
        "condition": {
          "and": [
            {
              "equals": "HIGH",
              "value": "${details.userLocationAnomaly.level}",
              "type": "VALUE_COMPARISON"
            }
          ]
        },
        "level": "MEDIUM"
      }
    ],
    "type": "COMPOSITE",
    "default": {
      "weight": 5,
      "score": 50,
      "result": {
        "level": "LOW",
        "type": "VALUE"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Composite - anonymous network and country",
    "compactName": "compositeAnonymousAndCountry",
    "licensed": true,
    "compositions": [
      {
        "condition": {
          "or": [
            {
              "equals": 3,
              "value": "${details.counters.predictorLevels.high}",
              "type": "VALUE_COMPARISON"
            },
            {
              "equals": "HIGH",
              "value": "${details.anonymousNetwork.level}",
              "type": "VALUE_COMPARISON"
            },
            {
              "type": "STRING_LIST",
              "list": [
                "Italy",
                "Germany"
              ],
              "notContains": "${details.country}"
            }
          ]
        },
        "level": "HIGH"
      },
      {
        "condition": {
          "and": [
            {
              "equals": "HIGH",
              "value": "${details.userLocationAnomaly.level}",
              "type": "VALUE_COMPARISON"
            }
          ]
        },
        "level": "MEDIUM"
      }
    ],
    "type": "COMPOSITE",
    "default": {
      "weight": 5,
      "score": 50,
      "result": {
        "level": "LOW",
        "type": "VALUE"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"

payload = json.dumps({
  "name": "Composite - anonymous network and country",
  "compactName": "compositeAnonymousAndCountry",
  "licensed": True,
  "compositions": [
    {
      "condition": {
        "or": [
          {
            "equals": 3,
            "value": "${details.counters.predictorLevels.high}",
            "type": "VALUE_COMPARISON"
          },
          {
            "equals": "HIGH",
            "value": "${details.anonymousNetwork.level}",
            "type": "VALUE_COMPARISON"
          },
          {
            "type": "STRING_LIST",
            "list": [
              "Italy",
              "Germany"
            ],
            "notContains": "${details.country}"
          }
        ]
      },
      "level": "HIGH"
    },
    {
      "condition": {
        "and": [
          {
            "equals": "HIGH",
            "value": "${details.userLocationAnomaly.level}",
            "type": "VALUE_COMPARISON"
          }
        ]
      },
      "level": "MEDIUM"
    }
  ],
  "type": "COMPOSITE",
  "default": {
    "weight": 5,
    "score": 50,
    "result": {
      "level": "LOW",
      "type": "VALUE"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Composite - anonymous network and country",\n    "compactName": "compositeAnonymousAndCountry",\n    "licensed": true,\n    "compositions": [\n        {\n            "condition": {\n                "or": [\n                    {\n                        "equals": 3,\n                        "value": "${details.counters.predictorLevels.high}",\n                        "type": "VALUE_COMPARISON"\n                    },\n                    {\n                        "equals": "HIGH",\n                        "value": "${details.anonymousNetwork.level}",\n                        "type": "VALUE_COMPARISON"\n                    },\n                    {\n                        "type": "STRING_LIST",\n                        "list": [\n                            "Italy",\n                            "Germany"\n                        ],\n                        "notContains": "${details.country}"\n                    }\n                ]\n            },\n            "level": "HIGH"\n        },\n        {\n            "condition": {\n                "and": [\n                    {\n                        "equals": "HIGH",\n                        "value": "${details.userLocationAnomaly.level}",\n                        "type": "VALUE_COMPARISON"\n                    }\n                ]\n            },\n            "level": "MEDIUM"\n        }    \n    ],\n    "type": "COMPOSITE",\n    "default": {\n        "weight": 5,\n        "score": 50,\n        "result": {\n            "level": "LOW",\n            "type": "VALUE"\n        }\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Composite - anonymous network and country",
  "compactName": "compositeAnonymousAndCountry",
  "licensed": true,
  "compositions": [
    {
      "condition": {
        "or": [
          {
            "equals": 3,
            "value": "\${details.counters.predictorLevels.high}",
            "type": "VALUE_COMPARISON"
          },
          {
            "equals": "HIGH",
            "value": "\${details.anonymousNetwork.level}",
            "type": "VALUE_COMPARISON"
          },
          {
            "type": "STRING_LIST",
            "list": [
              "Italy",
              "Germany"
            ],
            "notContains": "\${details.country}"
          }
        ]
      },
      "level": "HIGH"
    },
    {
      "condition": {
        "and": [
          {
            "equals": "HIGH",
            "value": "\${details.userLocationAnomaly.level}",
            "type": "VALUE_COMPARISON"
          }
        ]
      },
      "level": "MEDIUM"
    }
  ],
  "type": "COMPOSITE",
  "default": {
    "weight": 5,
    "score": 50,
    "result": {
      "level": "LOW",
      "type": "VALUE"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Composite - anonymous network and country\",\n    \"compactName\": \"compositeAnonymousAndCountry\",\n    \"licensed\": true,\n    \"compositions\": [\n        {\n            \"condition\": {\n                \"or\": [\n                    {\n                        \"equals\": 3,\n                        \"value\": \"${details.counters.predictorLevels.high}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.anonymousNetwork.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    },\n                    {\n                        \"type\": \"STRING_LIST\",\n                        \"list\": [\n                            \"Italy\",\n                            \"Germany\"\n                        ],\n                        \"notContains\": \"${details.country}\"\n                    }\n                ]\n            },\n            \"level\": \"HIGH\"\n        },\n        {\n            \"condition\": {\n                \"and\": [\n                    {\n                        \"equals\": \"HIGH\",\n                        \"value\": \"${details.userLocationAnomaly.level}\",\n                        \"type\": \"VALUE_COMPARISON\"\n                    }\n                ]\n            },\n            \"level\": \"MEDIUM\"\n        }    \n    ],\n    \"type\": \"COMPOSITE\",\n    \"default\": {\n        \"weight\": 5,\n        \"score\": 50,\n        \"result\": {\n            \"level\": \"LOW\",\n            \"type\": \"VALUE\"\n        }\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPredictors/ce192e3c-37bc-4c75-aaa9-03e51d8ece53"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "ce192e3c-37bc-4c75-aaa9-03e51d8ece53",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2023-08-29T12:07:12.978Z",
    "updatedAt": "2023-08-29T12:07:12.978Z",
    "name": "Composite - anonymous network and country",
    "compactName": "compositeAnonymousAndCountry",
    "licensed": true,
    "deletable": true,
    "compositions": [
        {
            "condition": {
                "or": [
                    {
                        "equals": 3,
                        "value": "${details.counters.predictorLevels.high}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "equals": "HIGH",
                        "value": "${details.anonymousNetwork.level}",
                        "type": "VALUE_COMPARISON"
                    },
                    {
                        "list": [
                            "Italy",
                            "Germany"
                        ],
                        "notContains": "${details.country}",
                        "type": "STRING_LIST"
                    }
                ],
                "type": "OR"
            },
            "level": "HIGH"
        },
        {
            "condition": {
                "and": [
                    {
                        "equals": "HIGH",
                        "value": "${details.userLocationAnomaly.level}",
                        "type": "VALUE_COMPARISON"
                    }
                ],
                "type": "AND"
            },
            "level": "MEDIUM"
        }
    ],
    "composition": {
        "condition": {
            "or": [
                {
                    "equals": 3,
                    "value": "${details.counters.predictorLevels.high}",
                    "type": "VALUE_COMPARISON"
                },
                {
                    "equals": "HIGH",
                    "value": "${details.anonymousNetwork.level}",
                    "type": "VALUE_COMPARISON"
                },
                {
                    "list": [
                        "Italy",
                        "Germany"
                    ],
                    "notContains": "${details.country}",
                    "type": "STRING_LIST"
                }
            ],
            "type": "OR"
        },
        "level": "HIGH"
    },
    "type": "COMPOSITE",
    "condition": {
        "scores": [
            {
                "name": "HIGH",
                "value": "HIGH"
            },
            {
                "name": "MEDIUM",
                "value": "MEDIUM"
            },
            {
                "name": "LOW",
                "value": "LOW"
            }
        ]
    },
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
        },
        "evaluated": false
    }
}
```

---

---
title: Create Risk Predictor (Custom - IP range)
description: This example uses the riskPredictors endpoint to create a custom predictor that assigns a risk level on the basis of defined IP ranges.
component: pingone-api
page_id: pingone-api:protect:risk-predictors/create_risk_predictor_custom_ip_range
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/create_risk_predictor_custom_ip_range.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Predictor (Custom - IP range)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPredictors
```

This example uses the `riskPredictors` endpoint to create a custom predictor that assigns a risk level on the basis of defined IP ranges.

The `ipRange` array is used to specify the relevant IP ranges, and the `contains` property is used to reference the IP associated with the event.

`type` is set to MAP to indicate that it is a custom predictor.

### Prerequisites

* Refer to [Risk Predictors](#risk-predictors) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for the complete data models.
>
> | Property                    | Type   | Required |
> | --------------------------- | ------ | -------- |
> | `compactName`               | String | Required |
> | `default`                   | Object | Optional |
> | `default.result.level`      | String | Optional |
> | `map.<risk level>.ipRange`  | Array  | Required |
> | `map.<risk level>.contains` | String | Required |
> | `name`                      | String | Required |
> | `type`                      | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
  "name": "Device IP - custom",
  "compactName": "deviceIpCustom",
  "map": {
    "high": {
        "ipRange": [
            "1.1.1.1/5",
            "2.2.2.2/8"
        ],
        "contains": "${event.ip}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPredictors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "name": "Device IP - custom",
  "compactName": "deviceIpCustom",
  "map": {
    "high": {
        "ipRange": [
            "1.1.1.1/5",
            "2.2.2.2/8"
        ],
        "contains": "${event.ip}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
    }
  }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""name"": ""Device IP - custom""," + "\n" +
@"  ""compactName"": ""deviceIpCustom""," + "\n" +
@"  ""map"": {" + "\n" +
@"    ""high"": {" + "\n" +
@"        ""ipRange"": [" + "\n" +
@"            ""1.1.1.1/5""," + "\n" +
@"            ""2.2.2.2/8""" + "\n" +
@"        ]," + "\n" +
@"        ""contains"": ""${event.ip}""" + "\n" +
@"    }" + "\n" +
@"  }," + "\n" +
@"  ""type"": ""MAP""," + "\n" +
@"  ""default"": {" + "\n" +
@"    ""result"": {" + "\n" +
@"      ""level"": ""MEDIUM""" + "\n" +
@"    }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"
  method := "POST"

  payload := strings.NewReader(`{
  "name": "Device IP - custom",
  "compactName": "deviceIpCustom",
  "map": {
    "high": {
        "ipRange": [
            "1.1.1.1/5",
            "2.2.2.2/8"
        ],
        "contains": "${event.ip}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
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
POST /v1/environments/{{envID}}/riskPredictors HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Device IP - custom",
  "compactName": "deviceIpCustom",
  "map": {
    "high": {
        "ipRange": [
            "1.1.1.1/5",
            "2.2.2.2/8"
        ],
        "contains": "${event.ip}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
    }
  }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Device IP - custom\",\n  \"compactName\": \"deviceIpCustom\",\n  \"map\": {\n    \"high\": {\n        \"ipRange\": [\n            \"1.1.1.1/5\",\n            \"2.2.2.2/8\"\n        ],\n        \"contains\": \"${event.ip}\"\n    }\n  },\n  \"type\": \"MAP\",\n  \"default\": {\n    \"result\": {\n      \"level\": \"MEDIUM\"\n    }\n  }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Device IP - custom",
    "compactName": "deviceIpCustom",
    "map": {
      "high": {
        "ipRange": [
          "1.1.1.1/5",
          "2.2.2.2/8"
        ],
        "contains": "${event.ip}"
      }
    },
    "type": "MAP",
    "default": {
      "result": {
        "level": "MEDIUM"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Device IP - custom",
    "compactName": "deviceIpCustom",
    "map": {
      "high": {
        "ipRange": [
          "1.1.1.1/5",
          "2.2.2.2/8"
        ],
        "contains": "${event.ip}"
      }
    },
    "type": "MAP",
    "default": {
      "result": {
        "level": "MEDIUM"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"

payload = json.dumps({
  "name": "Device IP - custom",
  "compactName": "deviceIpCustom",
  "map": {
    "high": {
      "ipRange": [
        "1.1.1.1/5",
        "2.2.2.2/8"
      ],
      "contains": "${event.ip}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "name": "Device IP - custom",\n  "compactName": "deviceIpCustom",\n  "map": {\n    "high": {\n        "ipRange": [\n            "1.1.1.1/5",\n            "2.2.2.2/8"\n        ],\n        "contains": "${event.ip}"\n    }\n  },\n  "type": "MAP",\n  "default": {\n    "result": {\n      "level": "MEDIUM"\n    }\n  }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Device IP - custom",
  "compactName": "deviceIpCustom",
  "map": {
    "high": {
      "ipRange": [
        "1.1.1.1/5",
        "2.2.2.2/8"
      ],
      "contains": "\${event.ip}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"name\": \"Device IP - custom\",\n  \"compactName\": \"deviceIpCustom\",\n  \"map\": {\n    \"high\": {\n        \"ipRange\": [\n            \"1.1.1.1/5\",\n            \"2.2.2.2/8\"\n        ],\n        \"contains\": \"${event.ip}\"\n    }\n  },\n  \"type\": \"MAP\",\n  \"default\": {\n    \"result\": {\n      \"level\": \"MEDIUM\"\n    }\n  }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPredictors/f48c5f9a-5723-4fe6-ac67-b1c21755f52c"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "f48c5f9a-5723-4fe6-ac67-b1c21755f52c",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2023-07-18T13:27:02.980Z",
    "updatedAt": "2023-07-18T13:27:02.980Z",
    "name": "Device IP - custom",
    "compactName": "deviceIpCustom",
    "licensed": true,
    "deletable": true,
    "map": {
        "high": {
            "ipRange": [
                "1.1.1.1/5",
                "2.2.2.2/8"
            ],
            "contains": "${event.ip}",
            "type": "IP_RANGE"
        }
    },
    "type": "MAP",
    "condition": {
        "scores": [
            {
                "name": "HIGH",
                "value": "HIGH"
            },
            {
                "name": "MEDIUM",
                "value": "MEDIUM"
            },
            {
                "name": "LOW",
                "value": "LOW"
            }
        ]
    },
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "MEDIUM",
            "type": "VALUE"
        },
        "evaluated": false
    }
}
```

---

---
title: Create Risk Predictor (Custom - numeric range)
description: This example uses the riskPredictors endpoint to create a custom predictor that assigns high, medium, or low risk based on the distance between the current location of the device and the location of the device when the last risk evaluation was carried out (distance is given in meters).
component: pingone-api
page_id: pingone-api:protect:risk-predictors/create_risk_predictor_custom_numeric_range
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/create_risk_predictor_custom_numeric_range.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Predictor (Custom - numeric range)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPredictors
```

This example uses the `riskPredictors` endpoint to create a custom predictor that assigns high, medium, or low risk based on the distance between the current location of the device and the location of the device when the last risk evaluation was carried out (distance is given in meters).

The `minScore` and `maxScore` properties are used to specify the ranges that should be considered high, medium, and low risk.

Note that the `maxScore` value for each of the risk categories is used as the `minScore` for the next risk level. If the distance equals the overlap value, the higher level of risk is assigned. So in this example, a distance of 804672 meters would be considered high risk.

`type` is set to MAP to indicate that it is a custom predictor.

### Prerequisites

* Refer to [Risk Predictors](#risk-predictors) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for the complete data models.
>
> | Property                            | Type   | Required |
> | ----------------------------------- | ------ | -------- |
> | `compactName`                       | String | Required |
> | `default`                           | Object | Optional |
> | `default.result.level`              | String | Optional |
> | `map.<risk level>.between.minScore` | Double | Required |
> | `map.<risk level>.between.maxScore` | Double | Required |
> | `map.<risk level>.contains`         | Double | Required |
> | `name`                              | String | Required |
> | `type`                              | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
  "name": "Device Network Location",
  "compactName": "deviceNetworkLocation",
  "map": {
    "high": {
      "between": {
        "minScore": 804672,
        "maxScore": 12742000
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "medium": {
      "between": {
        "minScore": 321869,
        "maxScore": 804672
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "low": {
      "between": {
        "minScore": 0,
        "maxScore": 321869
      },
      "contains": "${details.device.estimatedDistance}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "LOW"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPredictors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "name": "Device Network Location",
  "compactName": "deviceNetworkLocation",
  "map": {
    "high": {
      "between": {
        "minScore": 804672,
        "maxScore": 12742000
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "medium": {
      "between": {
        "minScore": 321869,
        "maxScore": 804672
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "low": {
      "between": {
        "minScore": 0,
        "maxScore": 321869
      },
      "contains": "${details.device.estimatedDistance}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "LOW"
    }
  }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""name"": ""Device Network Location""," + "\n" +
@"  ""compactName"": ""deviceNetworkLocation""," + "\n" +
@"  ""map"": {" + "\n" +
@"    ""high"": {" + "\n" +
@"      ""between"": {" + "\n" +
@"        ""minScore"": 804672," + "\n" +
@"        ""maxScore"": 12742000" + "\n" +
@"      }," + "\n" +
@"      ""contains"": ""${details.device.estimatedDistance}""" + "\n" +
@"    }," + "\n" +
@"    ""medium"": {" + "\n" +
@"      ""between"": {" + "\n" +
@"        ""minScore"": 321869," + "\n" +
@"        ""maxScore"": 804672" + "\n" +
@"      }," + "\n" +
@"      ""contains"": ""${details.device.estimatedDistance}""" + "\n" +
@"    }," + "\n" +
@"    ""low"": {" + "\n" +
@"      ""between"": {" + "\n" +
@"        ""minScore"": 0," + "\n" +
@"        ""maxScore"": 321869" + "\n" +
@"      }," + "\n" +
@"      ""contains"": ""${details.device.estimatedDistance}""" + "\n" +
@"    }" + "\n" +
@"  }," + "\n" +
@"  ""type"": ""MAP""," + "\n" +
@"  ""default"": {" + "\n" +
@"    ""result"": {" + "\n" +
@"      ""level"": ""LOW""" + "\n" +
@"    }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"
  method := "POST"

  payload := strings.NewReader(`{
  "name": "Device Network Location",
  "compactName": "deviceNetworkLocation",
  "map": {
    "high": {
      "between": {
        "minScore": 804672,
        "maxScore": 12742000
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "medium": {
      "between": {
        "minScore": 321869,
        "maxScore": 804672
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "low": {
      "between": {
        "minScore": 0,
        "maxScore": 321869
      },
      "contains": "${details.device.estimatedDistance}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "LOW"
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
POST /v1/environments/{{envID}}/riskPredictors HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Device Network Location",
  "compactName": "deviceNetworkLocation",
  "map": {
    "high": {
      "between": {
        "minScore": 804672,
        "maxScore": 12742000
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "medium": {
      "between": {
        "minScore": 321869,
        "maxScore": 804672
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "low": {
      "between": {
        "minScore": 0,
        "maxScore": 321869
      },
      "contains": "${details.device.estimatedDistance}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "LOW"
    }
  }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Device Network Location\",\n  \"compactName\": \"deviceNetworkLocation\",\n  \"map\": {\n    \"high\": {\n      \"between\": {\n        \"minScore\": 804672,\n        \"maxScore\": 12742000\n      },\n      \"contains\": \"${details.device.estimatedDistance}\"\n    },\n    \"medium\": {\n      \"between\": {\n        \"minScore\": 321869,\n        \"maxScore\": 804672\n      },\n      \"contains\": \"${details.device.estimatedDistance}\"\n    },\n    \"low\": {\n      \"between\": {\n        \"minScore\": 0,\n        \"maxScore\": 321869\n      },\n      \"contains\": \"${details.device.estimatedDistance}\"\n    }\n  },\n  \"type\": \"MAP\",\n  \"default\": {\n    \"result\": {\n      \"level\": \"LOW\"\n    }\n  }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Device Network Location",
    "compactName": "deviceNetworkLocation",
    "map": {
      "high": {
        "between": {
          "minScore": 804672,
          "maxScore": 12742000
        },
        "contains": "${details.device.estimatedDistance}"
      },
      "medium": {
        "between": {
          "minScore": 321869,
          "maxScore": 804672
        },
        "contains": "${details.device.estimatedDistance}"
      },
      "low": {
        "between": {
          "minScore": 0,
          "maxScore": 321869
        },
        "contains": "${details.device.estimatedDistance}"
      }
    },
    "type": "MAP",
    "default": {
      "result": {
        "level": "LOW"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Device Network Location",
    "compactName": "deviceNetworkLocation",
    "map": {
      "high": {
        "between": {
          "minScore": 804672,
          "maxScore": 12742000
        },
        "contains": "${details.device.estimatedDistance}"
      },
      "medium": {
        "between": {
          "minScore": 321869,
          "maxScore": 804672
        },
        "contains": "${details.device.estimatedDistance}"
      },
      "low": {
        "between": {
          "minScore": 0,
          "maxScore": 321869
        },
        "contains": "${details.device.estimatedDistance}"
      }
    },
    "type": "MAP",
    "default": {
      "result": {
        "level": "LOW"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"

payload = json.dumps({
  "name": "Device Network Location",
  "compactName": "deviceNetworkLocation",
  "map": {
    "high": {
      "between": {
        "minScore": 804672,
        "maxScore": 12742000
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "medium": {
      "between": {
        "minScore": 321869,
        "maxScore": 804672
      },
      "contains": "${details.device.estimatedDistance}"
    },
    "low": {
      "between": {
        "minScore": 0,
        "maxScore": 321869
      },
      "contains": "${details.device.estimatedDistance}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "LOW"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "name": "Device Network Location",\n  "compactName": "deviceNetworkLocation",\n  "map": {\n    "high": {\n      "between": {\n        "minScore": 804672,\n        "maxScore": 12742000\n      },\n      "contains": "${details.device.estimatedDistance}"\n    },\n    "medium": {\n      "between": {\n        "minScore": 321869,\n        "maxScore": 804672\n      },\n      "contains": "${details.device.estimatedDistance}"\n    },\n    "low": {\n      "between": {\n        "minScore": 0,\n        "maxScore": 321869\n      },\n      "contains": "${details.device.estimatedDistance}"\n    }\n  },\n  "type": "MAP",\n  "default": {\n    "result": {\n      "level": "LOW"\n    }\n  }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Device Network Location",
  "compactName": "deviceNetworkLocation",
  "map": {
    "high": {
      "between": {
        "minScore": 804672,
        "maxScore": 12742000
      },
      "contains": "\${details.device.estimatedDistance}"
    },
    "medium": {
      "between": {
        "minScore": 321869,
        "maxScore": 804672
      },
      "contains": "\${details.device.estimatedDistance}"
    },
    "low": {
      "between": {
        "minScore": 0,
        "maxScore": 321869
      },
      "contains": "\${details.device.estimatedDistance}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "LOW"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"name\": \"Device Network Location\",\n  \"compactName\": \"deviceNetworkLocation\",\n  \"map\": {\n    \"high\": {\n      \"between\": {\n        \"minScore\": 804672,\n        \"maxScore\": 12742000\n      },\n      \"contains\": \"${details.device.estimatedDistance}\"\n    },\n    \"medium\": {\n      \"between\": {\n        \"minScore\": 321869,\n        \"maxScore\": 804672\n      },\n      \"contains\": \"${details.device.estimatedDistance}\"\n    },\n    \"low\": {\n      \"between\": {\n        \"minScore\": 0,\n        \"maxScore\": 321869\n      },\n      \"contains\": \"${details.device.estimatedDistance}\"\n    }\n  },\n  \"type\": \"MAP\",\n  \"default\": {\n    \"result\": {\n      \"level\": \"LOW\"\n    }\n  }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPredictors/30674bdd-9304-4574-a0e7-d4865bb72b42"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "30674bdd-9304-4574-a0e7-d4865bb72b42",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2023-07-18T13:28:14.971Z",
    "updatedAt": "2023-07-18T13:28:14.971Z",
    "name": "Device Network Location",
    "compactName": "deviceNetworkLocation",
    "licensed": true,
    "deletable": true,
    "map": {
        "high": {
            "between": {
                "minScore": 804672,
                "maxScore": 12742000
            },
            "contains": "${details.device.estimatedDistance}",
            "type": "RANGE"
        },
        "medium": {
            "between": {
                "minScore": 321869,
                "maxScore": 804672
            },
            "contains": "${details.device.estimatedDistance}",
            "type": "RANGE"
        },
        "low": {
            "between": {
                "minScore": 0,
                "maxScore": 321869
            },
            "contains": "${details.device.estimatedDistance}",
            "type": "RANGE"
        }
    },
    "type": "MAP",
    "condition": {
        "scores": [
            {
                "name": "HIGH",
                "value": "HIGH"
            },
            {
                "name": "MEDIUM",
                "value": "MEDIUM"
            },
            {
                "name": "LOW",
                "value": "LOW"
            }
        ]
    },
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "LOW",
            "type": "VALUE"
        },
        "evaluated": false
    }
}
```

---

---
title: Create Risk Predictor (Custom - string matching)
description: This example uses the riskPredictors endpoint to create a custom predictor that assigns high or medium risk based on the country where the device is located.
component: pingone-api
page_id: pingone-api:protect:risk-predictors/create_risk_predictor_custom_string_matching
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/create_risk_predictor_custom_string_matching.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Predictor (Custom - string matching)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPredictors
```

This example uses the `riskPredictors` endpoint to create a custom predictor that assigns high or medium risk based on the country where the device is located.

The `list` array is used to specify countries that should be considered high risk and countries that should be considered medium risk, and the `contains` property is used to reference the country where the device is located.

`type` is set to MAP to indicate that it is a custom predictor.

### Prerequisites

* Refer to [Risk Predictors](#risk-predictors) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for the complete data models.
>
> | Property                    | Type   | Required |
> | --------------------------- | ------ | -------- |
> | `compactName`               | String | Required |
> | `default`                   | Object | Optional |
> | `default.result.level`      | String | Optional |
> | `map.<risk level>.list`     | Array  | Required |
> | `map.<risk level>.contains` | String | Required |
> | `name`                      | String | Required |
> | `type`                      | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
  "name": "Device country - custom",
  "compactName": "deviceCountryCustom",
  "map": {
    "high": {
        "list": [
            "Iran",
            "Syria"
        ],
        "contains": "${details.country}"
    },
    "medium": {
        "list": [
            "Ethiopia",
            "Russia"
        ],
        "contains": "${details.country}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPredictors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "name": "Device country - custom",
  "compactName": "deviceCountryCustom",
  "map": {
    "high": {
        "list": [
            "Iran",
            "Syria"
        ],
        "contains": "${details.country}"
    },
    "medium": {
        "list": [
            "Ethiopia",
            "Russia"
        ],
        "contains": "${details.country}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
    }
  }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""name"": ""Device country - custom""," + "\n" +
@"  ""compactName"": ""deviceCountryCustom""," + "\n" +
@"  ""map"": {" + "\n" +
@"    ""high"": {" + "\n" +
@"        ""list"": [" + "\n" +
@"            ""Iran""," + "\n" +
@"            ""Syria""" + "\n" +
@"        ]," + "\n" +
@"        ""contains"": ""${details.country}""" + "\n" +
@"    }," + "\n" +
@"    ""medium"": {" + "\n" +
@"        ""list"": [" + "\n" +
@"            ""Ethiopia""," + "\n" +
@"            ""Russia""" + "\n" +
@"        ]," + "\n" +
@"        ""contains"": ""${details.country}""" + "\n" +
@"    }" + "\n" +
@"  }," + "\n" +
@"  ""type"": ""MAP""," + "\n" +
@"  ""default"": {" + "\n" +
@"    ""result"": {" + "\n" +
@"      ""level"": ""MEDIUM""" + "\n" +
@"    }" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"
  method := "POST"

  payload := strings.NewReader(`{
  "name": "Device country - custom",
  "compactName": "deviceCountryCustom",
  "map": {
    "high": {
        "list": [
            "Iran",
            "Syria"
        ],
        "contains": "${details.country}"
    },
    "medium": {
        "list": [
            "Ethiopia",
            "Russia"
        ],
        "contains": "${details.country}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
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
POST /v1/environments/{{envID}}/riskPredictors HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "Device country - custom",
  "compactName": "deviceCountryCustom",
  "map": {
    "high": {
        "list": [
            "Iran",
            "Syria"
        ],
        "contains": "${details.country}"
    },
    "medium": {
        "list": [
            "Ethiopia",
            "Russia"
        ],
        "contains": "${details.country}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
    }
  }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Device country - custom\",\n  \"compactName\": \"deviceCountryCustom\",\n  \"map\": {\n    \"high\": {\n        \"list\": [\n            \"Iran\",\n            \"Syria\"\n        ],\n        \"contains\": \"${details.country}\"\n    },\n    \"medium\": {\n        \"list\": [\n            \"Ethiopia\",\n            \"Russia\"\n        ],\n        \"contains\": \"${details.country}\"\n    }\n  },\n  \"type\": \"MAP\",\n  \"default\": {\n    \"result\": {\n      \"level\": \"MEDIUM\"\n    }\n  }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Device country - custom",
    "compactName": "deviceCountryCustom",
    "map": {
      "high": {
        "list": [
          "Iran",
          "Syria"
        ],
        "contains": "${details.country}"
      },
      "medium": {
        "list": [
          "Ethiopia",
          "Russia"
        ],
        "contains": "${details.country}"
      }
    },
    "type": "MAP",
    "default": {
      "result": {
        "level": "MEDIUM"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Device country - custom",
    "compactName": "deviceCountryCustom",
    "map": {
      "high": {
        "list": [
          "Iran",
          "Syria"
        ],
        "contains": "${details.country}"
      },
      "medium": {
        "list": [
          "Ethiopia",
          "Russia"
        ],
        "contains": "${details.country}"
      }
    },
    "type": "MAP",
    "default": {
      "result": {
        "level": "MEDIUM"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"

payload = json.dumps({
  "name": "Device country - custom",
  "compactName": "deviceCountryCustom",
  "map": {
    "high": {
      "list": [
        "Iran",
        "Syria"
      ],
      "contains": "${details.country}"
    },
    "medium": {
      "list": [
        "Ethiopia",
        "Russia"
      ],
      "contains": "${details.country}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "name": "Device country - custom",\n  "compactName": "deviceCountryCustom",\n  "map": {\n    "high": {\n        "list": [\n            "Iran",\n            "Syria"\n        ],\n        "contains": "${details.country}"\n    },\n    "medium": {\n        "list": [\n            "Ethiopia",\n            "Russia"\n        ],\n        "contains": "${details.country}"\n    }\n  },\n  "type": "MAP",\n  "default": {\n    "result": {\n      "level": "MEDIUM"\n    }\n  }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Device country - custom",
  "compactName": "deviceCountryCustom",
  "map": {
    "high": {
      "list": [
        "Iran",
        "Syria"
      ],
      "contains": "\${details.country}"
    },
    "medium": {
      "list": [
        "Ethiopia",
        "Russia"
      ],
      "contains": "\${details.country}"
    }
  },
  "type": "MAP",
  "default": {
    "result": {
      "level": "MEDIUM"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"name\": \"Device country - custom\",\n  \"compactName\": \"deviceCountryCustom\",\n  \"map\": {\n    \"high\": {\n        \"list\": [\n            \"Iran\",\n            \"Syria\"\n        ],\n        \"contains\": \"${details.country}\"\n    },\n    \"medium\": {\n        \"list\": [\n            \"Ethiopia\",\n            \"Russia\"\n        ],\n        \"contains\": \"${details.country}\"\n    }\n  },\n  \"type\": \"MAP\",\n  \"default\": {\n    \"result\": {\n      \"level\": \"MEDIUM\"\n    }\n  }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPredictors/2b63c1bb-b384-4e28-912d-75386aece572"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "2b63c1bb-b384-4e28-912d-75386aece572",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2023-07-18T13:27:41.485Z",
    "updatedAt": "2023-07-18T13:27:41.485Z",
    "name": "Device country - custom",
    "compactName": "deviceCountryCustom",
    "licensed": true,
    "deletable": true,
    "map": {
        "high": {
            "list": [
                "Iran",
                "Syria"
            ],
            "contains": "${details.country}",
            "type": "STRING_LIST"
        },
        "medium": {
            "list": [
                "Ethiopia",
                "Russia"
            ],
            "contains": "${details.country}",
            "type": "STRING_LIST"
        }
    },
    "type": "MAP",
    "condition": {
        "scores": [
            {
                "name": "HIGH",
                "value": "HIGH"
            },
            {
                "name": "MEDIUM",
                "value": "MEDIUM"
            },
            {
                "name": "LOW",
                "value": "LOW"
            }
        ]
    },
    "default": {
        "weight": 5,
        "score": 50,
        "result": {
            "level": "MEDIUM",
            "type": "VALUE"
        },
        "evaluated": false
    }
}
```

---

---
title: Create Risk Predictor (Suspicious device)
description: This request creates a suspicious device predictor.
component: pingone-api
page_id: pingone-api:protect:risk-predictors/create_risk_predictor_suspicious_device
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/create_risk_predictor_suspicious_device.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Predictor (Suspicious device)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPredictors
```

This request creates a suspicious device predictor.

By setting the value of `shouldValidatePayloadSignature` to `true`, it specifies that any risk policies that include this predictor will require that the Signals SDK payload be provided as a signed JWT whose signature will be verified before proceeding with risk evaluation.

### Prerequisites

* Refer to [Risk Predictors](#risk-predictors) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for the complete data models.
>
> **Base data model**
>
> | Property                         | Type    | Required |
> | -------------------------------- | ------- | -------- |
> | `compactName`                    | String  | Required |
> | `default`                        | Object  | Required |
> | `default.result`                 | Object  | Required |
> | `default.result.level`           | String  | Required |
> | `detect`                         | String  | Required |
> | `licensed`                       | Boolean | Required |
> | `name`                           | String  | Required |
> | `shouldValidatePayloadSignature` | Boolean | Optional |
> | `type`                           | String  | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Susp Device with signed SDK payload",
    "compactName": "susDeviceSignedPayload",
    "licensed": true,
    "type": "DEVICE",
    "detect":"SUSPICIOUS_DEVICE",
    "shouldValidatePayloadSignature": true,
    "default": {
        "result": {
            "level": "MEDIUM"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPredictors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Susp Device with signed SDK payload",
    "compactName": "susDeviceSignedPayload",
    "licensed": true,
    "type": "DEVICE",
    "detect":"SUSPICIOUS_DEVICE",
    "shouldValidatePayloadSignature": true,
    "default": {
        "result": {
            "level": "MEDIUM"
        }
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Susp Device with signed SDK payload""," + "\n" +
@"    ""compactName"": ""susDeviceSignedPayload""," + "\n" +
@"    ""licensed"": true," + "\n" +
@"    ""type"": ""DEVICE""," + "\n" +
@"    ""detect"":""SUSPICIOUS_DEVICE""," + "\n" +
@"    ""shouldValidatePayloadSignature"": true," + "\n" +
@"    ""default"": {" + "\n" +
@"        ""result"": {" + "\n" +
@"            ""level"": ""MEDIUM""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Susp Device with signed SDK payload",
    "compactName": "susDeviceSignedPayload",
    "licensed": true,
    "type": "DEVICE",
    "detect":"SUSPICIOUS_DEVICE",
    "shouldValidatePayloadSignature": true,
    "default": {
        "result": {
            "level": "MEDIUM"
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
POST /v1/environments/{{envID}}/riskPredictors HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Susp Device with signed SDK payload",
    "compactName": "susDeviceSignedPayload",
    "licensed": true,
    "type": "DEVICE",
    "detect":"SUSPICIOUS_DEVICE",
    "shouldValidatePayloadSignature": true,
    "default": {
        "result": {
            "level": "MEDIUM"
        }
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Susp Device with signed SDK payload\",\n    \"compactName\": \"susDeviceSignedPayload\",\n    \"licensed\": true,\n    \"type\": \"DEVICE\",\n    \"detect\":\"SUSPICIOUS_DEVICE\",\n    \"shouldValidatePayloadSignature\": true,\n    \"default\": {\n        \"result\": {\n            \"level\": \"MEDIUM\"\n        }\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Susp Device with signed SDK payload",
    "compactName": "susDeviceSignedPayload",
    "licensed": true,
    "type": "DEVICE",
    "detect": "SUSPICIOUS_DEVICE",
    "shouldValidatePayloadSignature": true,
    "default": {
      "result": {
        "level": "MEDIUM"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Susp Device with signed SDK payload",
    "compactName": "susDeviceSignedPayload",
    "licensed": true,
    "type": "DEVICE",
    "detect": "SUSPICIOUS_DEVICE",
    "shouldValidatePayloadSignature": true,
    "default": {
      "result": {
        "level": "MEDIUM"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"

payload = json.dumps({
  "name": "Susp Device with signed SDK payload",
  "compactName": "susDeviceSignedPayload",
  "licensed": True,
  "type": "DEVICE",
  "detect": "SUSPICIOUS_DEVICE",
  "shouldValidatePayloadSignature": True,
  "default": {
    "result": {
      "level": "MEDIUM"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Susp Device with signed SDK payload",\n    "compactName": "susDeviceSignedPayload",\n    "licensed": true,\n    "type": "DEVICE",\n    "detect":"SUSPICIOUS_DEVICE",\n    "shouldValidatePayloadSignature": true,\n    "default": {\n        "result": {\n            "level": "MEDIUM"\n        }\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Susp Device with signed SDK payload",
  "compactName": "susDeviceSignedPayload",
  "licensed": true,
  "type": "DEVICE",
  "detect": "SUSPICIOUS_DEVICE",
  "shouldValidatePayloadSignature": true,
  "default": {
    "result": {
      "level": "MEDIUM"
    }
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Susp Device with signed SDK payload\",\n    \"compactName\": \"susDeviceSignedPayload\",\n    \"licensed\": true,\n    \"type\": \"DEVICE\",\n    \"detect\":\"SUSPICIOUS_DEVICE\",\n    \"shouldValidatePayloadSignature\": true,\n    \"default\": {\n        \"result\": {\n            \"level\": \"MEDIUM\"\n        }\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPredictors/b57a6b99-58cc-4eb9-a3bb-e647c84da2db"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "b57a6b99-58cc-4eb9-a3bb-e647c84da2db",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2024-06-18T13:21:21.829Z",
    "createdBy": "USER_DEFINED",
    "updatedAt": "2024-06-18T13:21:21.829Z",
    "name": "Susp Device with signed SDK payload",
    "compactName": "susDeviceSignedPayload",
    "licensed": true,
    "detect": "SUSPICIOUS_DEVICE",
    "shouldValidatePayloadSignature": true,
    "type": "DEVICE",
    "condition": {
        "scores": [
            {
                "name": "HIGH",
                "value": "HIGH"
            },
            {
                "name": "MEDIUM",
                "value": "MEDIUM"
            },
            {
                "name": "LOW",
                "value": "LOW"
            }
        ]
    },
    "deletable": true,
    "tooltip": "predictor.tooltip.device.suspicious.device",
    "default": {
        "weight": 5,
        "score": 80,
        "result": {
            "level": "MEDIUM",
            "type": "VALUE"
        },
        "evaluated": false
    }
}
```

---

---
title: Create Risk Predictor (Traffic anomaly)
description: This request creates a traffic anomaly predictor.
component: pingone-api
page_id: pingone-api:protect:risk-predictors/create_risk_predictor_traffic_anomaly
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/create_risk_predictor_traffic_anomaly.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Create Risk Predictor (Traffic anomaly)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskPredictors
```

This request creates a traffic anomaly predictor.

The `rules` array contains a single rule - tracking of unique users on a single device, the only rule that can currently be included in traffic anomaly predictors.

The `threshold` object is used to specify the number of users that will be considered Medium risk and the number of users that will be considered High risk.

The `interval` object is used to define the timeframe for tracking unique users on a device.

### Prerequisites

* Refer to [Risk Predictors](#risk-predictors) for important overview information.

> **Collapse: Request Model**
>
> Refer to [Risk Predictors](#risk-predictors) for the complete data models.
>
> **Base data model**
>
> | Property                        | Type    | Required |
> | ------------------------------- | ------- | -------- |
> | `compactName`                   | String  | Required |
> | `default`                       | Object  | Required |
> | `default.result.level`          | String  | Required |
> | `default.result.type`           | String  | Required |
> | `name`                          | String  | Required |
> | `rules`                         | Array   | Optional |
> | `rules[].enabled`               | Boolean | Required |
> | `rules[].interval`              | Object  | Required |
> | `rules[].interval.unit`         | String  | Required |
> | \`rules\[].interval.quantity \` | Integer | Required |
> | `rules[].threshold`             | Object  | Required |
> | `rules[].threshold.medium`      | Integer | Required |
> | `rules[].threshold.high`        | Integer | Required |
> | `rules[].type`                  | String  | Required |
> | `type`                          | String  | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Traffic anomaly predictor created with API",
    "compactName": "trafficAnomalyCreatedFromAPI",
    "type": "TRAFFIC_ANOMALY",
    "default": {
        "result": {
            "level": "medium",
            "type": "VALUE"
        }
    },
    "rules": [
        {
            "type": "UNIQUES_USERS_PER_DEVICE",
            "threshold": {
                "medium": 3,
                "high": 6
            },
            "interval": {
                "unit": "DAY",
                "quantity": 7
            },
            "enabled": true
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskPredictors' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Traffic anomaly predictor created with API",
    "compactName": "trafficAnomalyCreatedFromAPI",
    "type": "TRAFFIC_ANOMALY",
    "default": {
        "result": {
            "level": "medium",
            "type": "VALUE"
        }
    },
    "rules": [
        {
            "type": "UNIQUES_USERS_PER_DEVICE",
            "threshold": {
                "medium": 3,
                "high": 6
            },
            "interval": {
                "unit": "DAY",
                "quantity": 7
            },
            "enabled": true
        }
    ]
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Traffic anomaly predictor created with API""," + "\n" +
@"    ""compactName"": ""trafficAnomalyCreatedFromAPI""," + "\n" +
@"    ""type"": ""TRAFFIC_ANOMALY""," + "\n" +
@"    ""default"": {" + "\n" +
@"        ""result"": {" + "\n" +
@"            ""level"": ""medium""," + "\n" +
@"            ""type"": ""VALUE""" + "\n" +
@"        }" + "\n" +
@"    }," + "\n" +
@"    ""rules"": [" + "\n" +
@"        {" + "\n" +
@"            ""type"": ""UNIQUES_USERS_PER_DEVICE""," + "\n" +
@"            ""threshold"": {" + "\n" +
@"                ""medium"": 3," + "\n" +
@"                ""high"": 6" + "\n" +
@"            }," + "\n" +
@"            ""interval"": {" + "\n" +
@"                ""unit"": ""DAY""," + "\n" +
@"                ""quantity"": 7" + "\n" +
@"            }," + "\n" +
@"            ""enabled"": true" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Traffic anomaly predictor created with API",
    "compactName": "trafficAnomalyCreatedFromAPI",
    "type": "TRAFFIC_ANOMALY",
    "default": {
        "result": {
            "level": "medium",
            "type": "VALUE"
        }
    },
    "rules": [
        {
            "type": "UNIQUES_USERS_PER_DEVICE",
            "threshold": {
                "medium": 3,
                "high": 6
            },
            "interval": {
                "unit": "DAY",
                "quantity": 7
            },
            "enabled": true
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
POST /v1/environments/{{envID}}/riskPredictors HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Traffic anomaly predictor created with API",
    "compactName": "trafficAnomalyCreatedFromAPI",
    "type": "TRAFFIC_ANOMALY",
    "default": {
        "result": {
            "level": "medium",
            "type": "VALUE"
        }
    },
    "rules": [
        {
            "type": "UNIQUES_USERS_PER_DEVICE",
            "threshold": {
                "medium": 3,
                "high": 6
            },
            "interval": {
                "unit": "DAY",
                "quantity": 7
            },
            "enabled": true
        }
    ]
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Traffic anomaly predictor created with API\",\n    \"compactName\": \"trafficAnomalyCreatedFromAPI\",\n    \"type\": \"TRAFFIC_ANOMALY\",\n    \"default\": {\n        \"result\": {\n            \"level\": \"medium\",\n            \"type\": \"VALUE\"\n        }\n    },\n    \"rules\": [\n        {\n            \"type\": \"UNIQUES_USERS_PER_DEVICE\",\n            \"threshold\": {\n                \"medium\": 3,\n                \"high\": 6\n            },\n            \"interval\": {\n                \"unit\": \"DAY\",\n                \"quantity\": 7\n            },\n            \"enabled\": true\n        }\n    ]\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Traffic anomaly predictor created with API",
    "compactName": "trafficAnomalyCreatedFromAPI",
    "type": "TRAFFIC_ANOMALY",
    "default": {
      "result": {
        "level": "medium",
        "type": "VALUE"
      }
    },
    "rules": [
      {
        "type": "UNIQUES_USERS_PER_DEVICE",
        "threshold": {
          "medium": 3,
          "high": 6
        },
        "interval": {
          "unit": "DAY",
          "quantity": 7
        },
        "enabled": true
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Traffic anomaly predictor created with API",
    "compactName": "trafficAnomalyCreatedFromAPI",
    "type": "TRAFFIC_ANOMALY",
    "default": {
      "result": {
        "level": "medium",
        "type": "VALUE"
      }
    },
    "rules": [
      {
        "type": "UNIQUES_USERS_PER_DEVICE",
        "threshold": {
          "medium": 3,
          "high": 6
        },
        "interval": {
          "unit": "DAY",
          "quantity": 7
        },
        "enabled": true
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors"

payload = json.dumps({
  "name": "Traffic anomaly predictor created with API",
  "compactName": "trafficAnomalyCreatedFromAPI",
  "type": "TRAFFIC_ANOMALY",
  "default": {
    "result": {
      "level": "medium",
      "type": "VALUE"
    }
  },
  "rules": [
    {
      "type": "UNIQUES_USERS_PER_DEVICE",
      "threshold": {
        "medium": 3,
        "high": 6
      },
      "interval": {
        "unit": "DAY",
        "quantity": 7
      },
      "enabled": True
    }
  ]
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Traffic anomaly predictor created with API",\n    "compactName": "trafficAnomalyCreatedFromAPI",\n    "type": "TRAFFIC_ANOMALY",\n    "default": {\n        "result": {\n            "level": "medium",\n            "type": "VALUE"\n        }\n    },\n    "rules": [\n        {\n            "type": "UNIQUES_USERS_PER_DEVICE",\n            "threshold": {\n                "medium": 3,\n                "high": 6\n            },\n            "interval": {\n                "unit": "DAY",\n                "quantity": 7\n            },\n            "enabled": true\n        }\n    ]\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Traffic anomaly predictor created with API",
  "compactName": "trafficAnomalyCreatedFromAPI",
  "type": "TRAFFIC_ANOMALY",
  "default": {
    "result": {
      "level": "medium",
      "type": "VALUE"
    }
  },
  "rules": [
    {
      "type": "UNIQUES_USERS_PER_DEVICE",
      "threshold": {
        "medium": 3,
        "high": 6
      },
      "interval": {
        "unit": "DAY",
        "quantity": 7
      },
      "enabled": true
    }
  ]
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Traffic anomaly predictor created with API\",\n    \"compactName\": \"trafficAnomalyCreatedFromAPI\",\n    \"type\": \"TRAFFIC_ANOMALY\",\n    \"default\": {\n        \"result\": {\n            \"level\": \"medium\",\n            \"type\": \"VALUE\"\n        }\n    },\n    \"rules\": [\n        {\n            \"type\": \"UNIQUES_USERS_PER_DEVICE\",\n            \"threshold\": {\n                \"medium\": 3,\n                \"high\": 6\n            },\n            \"interval\": {\n                \"unit\": \"DAY\",\n                \"quantity\": 7\n            },\n            \"enabled\": true\n        }\n    ]\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/riskPredictors/fe36c631-6520-431b-a586-e680277a9f85"
        },
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "id": "fe36c631-6520-431b-a586-e680277a9f85",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "createdAt": "2024-08-06T15:22:09.536Z",
    "createdBy": "USER_DEFINED",
    "updatedAt": "2024-08-06T15:22:09.536Z",
    "name": "Traffic anomaly predictor created with API",
    "compactName": "trafficAnomalyCreatedFromAPI",
    "licensed": true,
    "rules": [
        {
            "type": "UNIQUES_USERS_PER_DEVICE",
            "threshold": {
                "medium": 3,
                "high": 6
            },
            "interval": {
                "unit": "DAY",
                "quantity": 7
            },
            "enabled": true
        }
    ],
    "type": "TRAFFIC_ANOMALY",
    "condition": {
        "scores": [
            {
                "name": "HIGH",
                "value": "HIGH"
            },
            {
                "name": "MEDIUM",
                "value": "MEDIUM"
            },
            {
                "name": "LOW",
                "value": "LOW"
            }
        ]
    },
    "deletable": true,
    "tooltip": "predictor.tooltip.traffic.anomaly",
    "default": {
        "weight": 5,
        "score": 80,
        "result": {
            "level": "MEDIUM",
            "type": "VALUE"
        },
        "evaluated": false
    }
}
```

---

---
title: Delete Risk Policy Set
description: The GET {{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}} operation deletes the risk policy set identified by its ID in the request URL.
component: pingone-api
page_id: pingone-api:protect:risk-policies/delete-risk-policy-set-
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-policies/delete-risk-policy-set-.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete Risk Policy Set

##

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}
```

The `GET {{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}` operation deletes the risk policy set identified by its ID in the request URL.

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The environment's default policy set can be deleted only after another policy set has been designated as the environment's default policy set. |

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}"
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
DELETE /v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPolicySets/{{riskPolicySetID}}")!,timeoutInterval: Double.infinity)
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

200 OK

---

---
title: Delete Risk Predictor
description: The PUT {{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}} operation deletes the custom risk predictor specified by its ID in the request URL. Only risk predictors with a type property value set to MAP can be deleted.
component: pingone-api
page_id: pingone-api:protect:risk-predictors/delete-risk-predictor
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-predictors/delete-risk-predictor.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Delete Risk Predictor

##

```none
DELETE {{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}
```

The `PUT {{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}` operation deletes the custom risk predictor specified by its ID in the request URL. Only risk predictors with a `type` property value set to `MAP` can be deleted.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If a risk predictor is in use by an existing risk policy, it cannot be deleted. To delete the risk predictor, you must delete the associated risk policy before attempting the delete operation. Alternatively, you can remove the usage of the predictor in the risk policy by setting the predictor's weight to 0 and removing it from the `overrides` section. For information about risk policies and risk policy sets, refer to [Risk Policies](#risk-policies). Similarly, you cannot delete a predictor that is currently used in a composite predictor. |

When successful, the `DELETE` request returns a code `204 No Content` message.

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
curl --location --globoff --request DELETE '{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}"
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
DELETE /v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}")
  .method("DELETE", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Delete.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskPredictors/{{riskPredictorID}}")!,timeoutInterval: Double.infinity)
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
title: Erase Risk Data for User
description: This example uses POST {{apiPath}}/v1/environments/{{envID}}/riskUserProfile to erase all of the risk-related data that was collected for the specified user.
component: pingone-api
page_id: pingone-api:protect:risk-data/erase_risk_data_for_user
canonical_url: https://developer.pingidentity.com/pingone-api/protect/risk-data/erase_risk_data_for_user.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Erase Risk Data for User

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/riskUserProfile
```

This example uses `POST {{apiPath}}/v1/environments/{{envID}}/riskUserProfile` to erase all of the risk-related data that was collected for the specified user.

Note that the request uses a special value for the Content-Type header: `application/vnd.pingidentity.risk.userProfile.reset+json`.

> **Collapse: Request Model**
>
> Refer to [Risk Data](../risk-data.html) for the complete data model.
>
> | Property    | Type   | Required |
> | ----------- | ------ | -------- |
> | `user`      | Object | Required |
> | `user.id`   | String | Required |
> | `user.type` | String | Required |

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.risk.userProfile.reset+json

### Body

raw ( application/vnd.pingidentity.risk.userProfile.reset+json )

```json
{
    "user": {
        "id":"{{userID}}",
        "type": "EXTERNAL"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/riskUserProfile' \
--header 'Content-Type: application/vnd.pingidentity.risk.userProfile.reset+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "user": {
        "id":"{{userID}}",
        "type": "EXTERNAL"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/riskUserProfile")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/vnd.pingidentity.risk.userProfile.reset+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""user"": {" + "\n" +
@"        ""id"":""{{userID}}""," + "\n" +
@"        ""type"": ""EXTERNAL""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/riskUserProfile"
  method := "POST"

  payload := strings.NewReader(`{
    "user": {
        "id":"{{userID}}",
        "type": "EXTERNAL"
    }
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.risk.userProfile.reset+json")
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
POST /v1/environments/{{envID}}/riskUserProfile HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.risk.userProfile.reset+json
Authorization: Bearer {{accessToken}}

{
    "user": {
        "id":"{{userID}}",
        "type": "EXTERNAL"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.risk.userProfile.reset+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"user\": {\n        \"id\":\"{{userID}}\",\n        \"type\": \"EXTERNAL\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/riskUserProfile")
  .method("POST", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.risk.userProfile.reset+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/riskUserProfile",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.risk.userProfile.reset+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "user": {
      "id": "{{userID}}",
      "type": "EXTERNAL"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/riskUserProfile',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.risk.userProfile.reset+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "user": {
      "id": "{{userID}}",
      "type": "EXTERNAL"
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

url = "{{apiPath}}/v1/environments/{{envID}}/riskUserProfile"

payload = json.dumps({
  "user": {
    "id": "{{userID}}",
    "type": "EXTERNAL"
  }
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.risk.userProfile.reset+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/riskUserProfile');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.risk.userProfile.reset+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "user": {\n        "id":"{{userID}}",\n        "type": "EXTERNAL"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/riskUserProfile")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/vnd.pingidentity.risk.userProfile.reset+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "user": {
    "id": "{{userID}}",
    "type": "EXTERNAL"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"user\": {\n        \"id\":\"{{userID}}\",\n        \"type\": \"EXTERNAL\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/riskUserProfile")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.risk.userProfile.reset+json", forHTTPHeaderField: "Content-Type")
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
    "_links": {
        "environment": {
            "href": "https://api.pingone.eu/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "b30ac647-e33e-464f-a6ea-0275082d4c26",
        "type": "EXTERNAL"
    }
}
```

---

---
title: PingOne Protect
description: The PingOne Protect service provides capabilities to configure and retrieve risk evaluations from internal and external risk providers based on a specified risk policy.
component: pingone-api
page_id: pingone-api:protect:introduction
canonical_url: https://developer.pingidentity.com/pingone-api/protect/introduction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
section_ids:
  risk-policies: Risk Policies
  risk-evaluations: Risk Evaluations
  risk-predictors: Risk Predictors
  use-cases: Use Cases
---

# PingOne Protect

The PingOne Protect service provides capabilities to configure and retrieve risk evaluations from internal and external risk providers based on a specified risk policy.

Refer also to [PingOne Protect's integration with Ping Gateway](https://docs.pingidentity.com/pinggateway/2025.3/pingone/risk.html) for on-premise use of PingOne Protect with web applications protected by PingGateway.

## Risk Policies

A risk policy is determined by your specific configuration settings. The risk policy enables you to customize a risk evaluation to fit your use case. The policy is used during a risk evaluation to calculate the risk scores for received events. For more information about risk policies, refer to [Risk Policies](#risk-policies).

## Risk Evaluations

Use risk evaluations to calculate the risk level and other risk-related details associated with a received event based on the environment's settings and data provided in the event. For more information about risk evaluation, refer to [Risk Evaluations](#risk-evaluations).

## Risk Predictors

Risk predictors are employed by risk policies, and define thresholds for certain criteria (such as, IP Velocity, User Velocity, or User Location Anomaly) to determine whether there's the potential for fraudulent user behavior. For more information refer to [Risk Predictors](#risk-predictors).

## Use Cases

* [Create a risk policy set](/pingone/tutorial/v1/api/#create-a-risk-policy-set)

* [Create a risk evaluation](/pingone/tutorial/v1/api/#create-a-risk-evaluation)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These requests require `PING_ONE_RISK` in the Bill of Materials (BOM) for your environment. To check the BOM for the list of PingOne products associated with your environment, refer to [Read One Bill of Materials](/pingone/platform/v1/api/#get-read-one-bill-of-materials). If `PING_ONE_RISK` is not in the BOM, contact your PingOne administrator to check whether your license supports adding this product to your environment. |

---

---
title: Postman and the PingOne APIs
description: We use Postman to create our PingOne DaVinci Admin API docs, and have supplied our Postman collections for you to download. There's also an accompanying Postman Environment template already populated with the variables used in the collections.
component: pingone-api
page_id: pingone-api:protect:working-with-pingone-apis/postman-and-pingone
canonical_url: https://developer.pingidentity.com/pingone-api/protect/working-with-pingone-apis/postman-and-pingone.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Postman and the PingOne APIs

We use Postman to create our PingOne DaVinci Admin API docs, and have supplied our Postman collections for you to download. There's also an accompanying Postman Environment template already populated with the variables used in the collections.

If you aren't currently using Postman, you can install the free version. Refer to [Download Postman](https://www.postman.com/downloads/) to install Postman, either locally, or in your browser.

Refer to [The PingOne Protect API Postman collections](#protect-collections) for the collections you can download or fork.

For more information about our Postman environment variables, refer to [The PingOne Postman environment template](postman-and-pingone/use-the-pingone-postman-environment-template.html).

You'll also find all of the Postman collections for our documented PingOne use cases in our [Use Case Library](/pingone/workflow-library/v1/api/).

---

---
title: Protect Settings
description: Use the riskSettings endpoint to specify maximum data retention periods for the risk data that is used by specific predictors.
component: pingone-api
page_id: pingone-api:protect:protect-settings
canonical_url: https://developer.pingidentity.com/pingone-api/protect/protect-settings.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
  protect-settings-data-model: Protect settings data model
---

# Protect Settings

Use the `riskSettings` endpoint to specify maximum data retention periods for the risk data that is used by specific predictors.

You can define different data retention periods for each of the following risk predictors:

* New Device

* User Location Anomaly

* User Base Risk Behavior

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you modify the maximum data retention period, the new period applies only to the new data that is collected after you changed the setting. |

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.

## Protect settings data model

| Property                                    | Type    | Required | Mutable   | Description                                                                                                                                |
| ------------------------------------------- | ------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `dataRetention`                             | Object  | Required | Mutable   | The object that contains the fields for setting the data retention period for specific risk predictors.                                    |
| `dataRetention.newDeviceInDays`             | Integer | Optional | Mutable   | The number of days that data for the New Device predictor should be retained. Minimum is 1, maximum is 180. Default is 180.                |
| `dataRetention.userBasedRiskBehaviorInDays` | Integer | Optional | Mutable   | The number of days that data for the User Based Risk Behavior predictor should be retained. Minimum is 30, maximum is 180. Default is 180. |
| `dataRetention.userLocationAnomalyInDays`   | Integer | Optional | Mutable   | The number of days that data for the User Location Anomaly predictor should be retained. Minimum is 30, maximum is 90. Default is 90.      |
| `environment.id`                            | String  | N/A      | Read-only | The ID of the PingOne environment for which the Protect settings are being modified.                                                       |
| `updatedAt`                                 | Date    | N/A      | Read-only | The date and time the Protect settings were last updated.                                                                                  |
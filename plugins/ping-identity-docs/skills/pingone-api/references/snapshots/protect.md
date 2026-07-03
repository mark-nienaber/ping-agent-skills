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

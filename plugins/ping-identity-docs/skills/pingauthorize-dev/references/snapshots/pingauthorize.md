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

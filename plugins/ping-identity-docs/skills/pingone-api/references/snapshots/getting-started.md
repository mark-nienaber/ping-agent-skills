---
title: Getting Started
description: This guide uses fundamental workflows to walk you through the steps to get an access token, and begin using the PingOne APIs.
component: pingone-api
page_id: pingone-api:getting-started:introduction
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/introduction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
section_ids:
  what-youll-do: What you'll do
  how-the-workflows-interact: How the workflows interact
  the-postman-choice: The Postman choice
---

# Getting Started

This guide uses fundamental workflows to walk you through the steps to get an access token, and begin using the PingOne APIs.

## What you'll do

There are three inter-related workflows you'll use to:

1. **Task 1:** Sign on to the admin console for your PingOne environment, create an admin-level Worker app, and assign roles to the Worker app. This is the only workflow for which you'll use the admin console. The remaining workflows use the PingOne APIs.

2. **Task 2:** Create and initially configure a new test environment and test user.

   As part of the workflow to create a new environment, you'll get an admin access token (a JSON Web Token) with permissions to call any of the PingOne APIs.

3. **Task 3:** Create a web application and sign-on (SSO) to that application using the test user you created in Task 2.

## How the workflows interact

![Workflows](../_images/p1_tutorial-flow.svg)

## The Postman choice

We use Postman to create our PingOne API docs, and have done so in this Getting Started guide as well. We highly recommend you use Postman to complete the workflows using the PingOne APIs ([Task 2: Create a test environment](create-a-test-environment.html) and [Task 3: Create an SSO workflow](simple-sso-workflow.html)). We've configured a Postman collection for you to download in each of these workflows, so you can call these requests in your own Postman installation. There's also an accompanying Postman Environment template already populated with the necessary variables.

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | Postman offers a free version. Refer to [Download Postman](https://www.postman.com/downloads/). |

If you'd rather not install Postman, this guide doesn't limit or constrain you in that respect. Each Postman request in this guide is well-documented, and has a dropdown list to show the coding language to use for the request. (This is also true for our [Platform Reference API](../platform/introduction.html) docs.)

![RequestLanguage](../_images/p1_requestLanguageList.png)

You can use cURL (the default) and call the request from your command line, or select one of the other coding languages in the dropdown list, copy the request into your IDE, and call it from there.

---

---
title: "Step 1: Get a new PingOne access token"
description: Because the access token you used for the workflow to create a test environment may have expired (a 1 hour expiry), you'll again call the POST {{authPath}}/{{adminEnvID}}/as/token request to obtain a new access token. This request uses Basic authorization to get an access token having an authorization code grant type.
component: pingone-api
page_id: pingone-api:getting-started:simple-sso-workflow/step-1-get-new-access-token
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/simple-sso-workflow/step-1-get-new-access-token.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 1: Get a new PingOne access token

##

```none
POST {{authPath}}/{{adminEnvID}}/as/token
```

Because the access token you used for the workflow to create a test environment may have expired (a 1 hour expiry), you'll again call the `POST {{authPath}}/{{adminEnvID}}/as/token` request to obtain a new access token. This request uses Basic authorization to get an access token having an `authorization code` grant type.

In this request:

* `{{authPath}}` is the geographic domain to use for authentication and authorization for your PingOne environment. The PingOne top-level domain is `https://auth.pingone.com/` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html#pingone-api-domains) for the top-level domains for other regions.

* `{{adminEnvID}}` is the environment that contains the admin Worker application you created using the PingOne admin console in the prior workflow to [Create an admin Worker app connection](../create-an-admin-worker-app/step-3-assign-roles.html).

If you're using Postman, set these variables in the Authorization tab. If you're not using Postman, these are header variables:

* `{{adminAppID}}` is your Worker application's **Client ID** that you obtained from the PingOne admin console when you created the Worker app.

* `{{adminAppSecret}}` is your Worker application's **Client Secret** that you obtained from the PingOne admin console when you created the Worker app.

![Dev Guide Postman Environment](../../_images/p1_PostmanDevEnv1.png)

When successful, the response returns a `Status: 200 OK` message, and an access token is returned.

### Troubleshooting

* Verify that `{{adminEnvID}}` is the ID for your initial PingOne environment (automatically created for your account), used when you created the admin Worker app connection.

* Verify that `{{authPath}}` is correct for your geographic domain .

* If you're using Postman, verify the URL against the `{{adminAppID}}` and `{{adminAppSecret}}` values shown in Postman's Auth tab to ensure the correct values have been added to your Postman environment. In Postman, unassigned variables are shown in red, and assigned variables in blue.

### Headers

Authorization

Content-Type      application/x-www-form-urlencoded

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key         | Value               |
| ----------- | ------------------- |
| grant\_type | client\_credentials |

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
curl --location --globoff '{{authPath}}/{{adminEnvID}}/as/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19' \
--data-urlencode 'grant_type=client_credentials'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{adminEnvID}}/as/token")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddHeader("Authorization", "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19");
request.AddParameter("grant_type", "client_credentials");
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

  url := "{{authPath}}/{{adminEnvID}}/as/token"
  method := "POST"

  payload := strings.NewReader("grant_type=client_credentials")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
  req.Header.Add("Authorization", "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19")

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
POST /{{adminEnvID}}/as/token HTTP/1.1
Host: {{authPath}}
Content-Type: application/x-www-form-urlencoded
Authorization: Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19

grant_type=client_credentials
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "grant_type=client_credentials");
Request request = new Request.Builder()
  .url("{{authPath}}/{{adminEnvID}}/as/token")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .addHeader("Authorization", "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{adminEnvID}}/as/token",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19"
  },
  "data": {
    "grant_type": "client_credentials"
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
  'url': '{{authPath}}/{{adminEnvID}}/as/token',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19'
  },
  form: {
    'grant_type': 'client_credentials'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{adminEnvID}}/as/token"

payload = 'grant_type=client_credentials'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{adminEnvID}}/as/token');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Authorization' => 'Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19'
));
$request->addPostParameter(array(
  'grant_type' => 'client_credentials'
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

url = URI("{{authPath}}/{{adminEnvID}}/as/token")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request["Authorization"] = "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19"
request.body = "grant_type=client_credentials"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "grant_type=client_credentials"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{adminEnvID}}/as/token")!,timeoutInterval: Double.infinity)
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19", forHTTPHeaderField: "Authorization")

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
    "access_token": "eyJhbGciOi....",
    "token_type": "Bearer",
    "expires_in": 3600
}
```

---

---
title: "Step 1: Get a PingOne access token"
description: Use the POST {{authPath}}/{{adminEnvID}}/as/token request to obtain an access token. The access token is needed to call any of the PingOne APIs. This request uses Basic authorization to get an access token having a client_credentials grant type.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-1-get-access-token
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-1-get-access-token.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 1: Get a PingOne access token

##

```none
POST {{authPath}}/{{adminEnvID}}/as/token
```

Use the `POST {{authPath}}/{{adminEnvID}}/as/token` request to obtain an access token. The access token is needed to call any of the PingOne APIs. This request uses Basic authorization to get an access token having a `client_credentials` grant type.

In this request:

* `{{authPath}}` is the geographic domain to use for authentication and authorization for your PingOne environment. The PingOne top-level domain is `https://auth.pingone.com/` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

* `{{adminEnvID}}` is the environment that contains the admin Worker application you created using the PingOne admin console in the prior workflow to [Create an admin Worker app connection](../create-an-admin-worker-app.html).

If you're using Postman, set these variables in the Authorization tab. If you're not using Postman, these are header variables:

* `{{adminAppID}}` is your Worker application's **Client ID** that you obtained from the PingOne admin console when you created the Worker app.

* `{{adminAppSecret}}` is your Worker application's **Client Secret** that you obtained from the PingOne admin console when you created the Worker app.

![Dev Guide Postman Environment](../../_images/p1_PostmanDevEnv1.png)

When successful, the response returns a `Status: 200 OK` message, and an access token is returned.

### Troubleshooting

* Verify that `{{adminEnvID}}` is the ID for your initial PingOne environment (automatically created for your account), used when you created the admin Worker app connection.

* Verify that `{{authPath}}` is correct for your geographic domain .

* If you're using Postman, verify the URL against the `{{adminAppID}}` and `{{adminAppSecret}}` values shown in Postman's Auth tab to ensure the correct values have been added to your Postman environment. In Postman, unassigned variables are shown in red, and assigned variables in blue.

### Headers

Authorization

Content-Type      application/x-www-form-urlencoded

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key         | Value               |
| ----------- | ------------------- |
| grant\_type | client\_credentials |

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
curl --location --globoff '{{authPath}}/{{adminEnvID}}/as/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19' \
--data-urlencode 'grant_type=client_credentials'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{adminEnvID}}/as/token")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddHeader("Authorization", "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19");
request.AddParameter("grant_type", "client_credentials");
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

  url := "{{authPath}}/{{adminEnvID}}/as/token"
  method := "POST"

  payload := strings.NewReader("grant_type=client_credentials")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
  req.Header.Add("Authorization", "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19")

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
POST /{{adminEnvID}}/as/token HTTP/1.1
Host: {{authPath}}
Content-Type: application/x-www-form-urlencoded
Authorization: Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19

grant_type=client_credentials
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "grant_type=client_credentials");
Request request = new Request.Builder()
  .url("{{authPath}}/{{adminEnvID}}/as/token")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .addHeader("Authorization", "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{adminEnvID}}/as/token",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19"
  },
  "data": {
    "grant_type": "client_credentials"
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
  'url': '{{authPath}}/{{adminEnvID}}/as/token',
  'headers': {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19'
  },
  form: {
    'grant_type': 'client_credentials'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{adminEnvID}}/as/token"

payload = 'grant_type=client_credentials'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{adminEnvID}}/as/token');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Authorization' => 'Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19'
));
$request->addPostParameter(array(
  'grant_type' => 'client_credentials'
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

url = URI("{{authPath}}/{{adminEnvID}}/as/token")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/x-www-form-urlencoded"
request["Authorization"] = "Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19"
request.body = "grant_type=client_credentials"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "grant_type=client_credentials"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{adminEnvID}}/as/token")!,timeoutInterval: Double.infinity)
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3thZG1pbkFwcElEfX06e3thZG1pbkFwcFNlY3JldH19", forHTTPHeaderField: "Authorization")

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
    "access_token": "eyJhbGciOi....",
    "token_type": "Bearer",
    "expires_in": 3600
}
```

---

---
title: "Step 1: Sign on to admin console"
description: Sign on to the PingOne admin console. For more information about the PingOne admin console, refer to Accessing the admin console home page.
component: pingone-api
page_id: pingone-api:getting-started:create-an-admin-worker-app/step-1-login
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-an-admin-worker-app/step-1-login.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Step 1: Sign on to admin console

Sign on to the PingOne admin console. For more information about the PingOne admin console, refer to [Accessing the admin console home page](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_access_admin_console.html).

---

---
title: "Step 2: Add a Worker app"
description: In the admin console, add a Worker app connection to PingOne:
component: pingone-api
page_id: pingone-api:getting-started:create-an-admin-worker-app/step-2-add-worker-app
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-an-admin-worker-app/step-2-add-worker-app.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Step 2: Add a Worker app

In the admin console, add a Worker app connection to PingOne:

1. Select **Applications** -→ **Applications**.

   ![Admin-Console-App-Main](../../_images/p1_AdminConsoleAppMain.png)

2. Click the **+** icon next to **Applications** to add a new app.

3. In the **Application Name** field, enter an application name, and select **Worker** as the Application Type.

   ![Admin-Console-Add-App](../../_images/ui-addWorkerApp.png)

4. Click **Save**. The Roles tab is then displayed on the application information page.

---

---
title: "Step 2: Create a Web application"
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/applications operation to create a new PingOne OpenID Connect (OIDC) Web app. This app configuration represents (to PingOne) your custom application for user sign-on.
component: pingone-api
page_id: pingone-api:getting-started:simple-sso-workflow/step-2-create-a-web-application
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/simple-sso-workflow/step-2-create-a-web-application.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 2: Create a Web application

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/applications
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/applications` operation to create a new PingOne OpenID Connect (OIDC) Web app. This app configuration represents (to PingOne) your custom application for user sign-on.

In this request:

* ``{{apiPath}}`is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1`` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html#pingone-api-domains) for the top-level domains for other regions.

* `{{envID}}` is the ID of the environment you created when you created your test environment. Refer to [Create a Test Environment](../create-a-test-environment.html).

In the request body:

* `enabled` is a Boolean (true/false) value indicating the current state of the application. You want to enable the Web application for use.

* `name` is a String containing the name of the application.

* `type` is a String containing the application type. In this workflow, the `type` is `WEB_APP`.

* `protocol` is a String containing the protocol used by the application. In this workflow, the `protocol` is `OPENID_CONNECT`.

* `grantTypes` is a String array containing the grant type or types for the authorization request. In this workflow, the `grantTypes` value needs to use the `authorization_code` grant type.

* `redirectUris` is a String array containing the callback URIs to use for the authentication response.

* `responseTypes` is a String array containing the code or token type or types returned by the authorization request. In this workflow, the `responseTypes` value needs to be `CODE` to return an authorization code. This corresponds to the `grantTypes` value set.

* `tokenEndpointAuthMethod` is a String containing the client authentication method supported by the token endpoint. In this workflow, the `tokenEndpointAuthMethod` value needs to be `CLIENT_SECRET_BASIC`.

When successful, the response returns a `Status: 201 created` message and shows the new application's configuration data.

The configuration data includes the application's `id` property. This is needed to get the application's `secret` value in the next step.

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've assigned either the Environment Admin or Client Application Developer role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests), and you have a valid access token. For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red).

* Verify that you've set the variables used in the request body correctly.

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain .

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "enabled": true,
    "name": "Shared-Web-App",
    "description": "This is an OIDC Web application for workflow testing.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applications' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "enabled": true,
    "name": "Shared-Web-App",
    "description": "This is an OIDC Web application for workflow testing.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applications")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""enabled"": true," + "\n" +
@"    ""name"": ""Shared-Web-App""," + "\n" +
@"    ""description"": ""This is an OIDC Web application for workflow testing.""," + "\n" +
@"    ""type"": ""WEB_APP""," + "\n" +
@"    ""protocol"": ""OPENID_CONNECT""," + "\n" +
@"    ""grantTypes"": [" + "\n" +
@"        ""AUTHORIZATION_CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""redirectUris"": [" + "\n" +
@"        ""http://localhost:3000/callback""" + "\n" +
@"    ]," + "\n" +
@"    ""responseTypes"": [" + "\n" +
@"        ""CODE""" + "\n" +
@"    ]," + "\n" +
@"    ""tokenEndpointAuthMethod"": ""CLIENT_SECRET_BASIC""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/applications"
  method := "POST"

  payload := strings.NewReader(`{
    "enabled": true,
    "name": "Shared-Web-App",
    "description": "This is an OIDC Web application for workflow testing.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
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
POST /v1/environments/{{envID}}/applications HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "enabled": true,
    "name": "Shared-Web-App",
    "description": "This is an OIDC Web application for workflow testing.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "responseTypes": [
        "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"enabled\": true,\n    \"name\": \"Shared-Web-App\",\n    \"description\": \"This is an OIDC Web application for workflow testing.\",\n    \"type\": \"WEB_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"http://localhost:3000/callback\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"CLIENT_SECRET_BASIC\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applications")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applications",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "enabled": true,
    "name": "Shared-Web-App",
    "description": "This is an OIDC Web application for workflow testing.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "http://localhost:3000/callback"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/applications',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "enabled": true,
    "name": "Shared-Web-App",
    "description": "This is an OIDC Web application for workflow testing.",
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "grantTypes": [
      "AUTHORIZATION_CODE"
    ],
    "redirectUris": [
      "http://localhost:3000/callback"
    ],
    "responseTypes": [
      "CODE"
    ],
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
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

url = "{{apiPath}}/v1/environments/{{envID}}/applications"

payload = json.dumps({
  "enabled": True,
  "name": "Shared-Web-App",
  "description": "This is an OIDC Web application for workflow testing.",
  "type": "WEB_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "http://localhost:3000/callback"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applications');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "enabled": true,\n    "name": "Shared-Web-App",\n    "description": "This is an OIDC Web application for workflow testing.",\n    "type": "WEB_APP",\n    "protocol": "OPENID_CONNECT",\n    "grantTypes": [\n        "AUTHORIZATION_CODE"\n    ],\n    "redirectUris": [\n        "http://localhost:3000/callback"\n    ],\n    "responseTypes": [\n        "CODE"\n    ],\n    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/applications")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "enabled": true,
  "name": "Shared-Web-App",
  "description": "This is an OIDC Web application for workflow testing.",
  "type": "WEB_APP",
  "protocol": "OPENID_CONNECT",
  "grantTypes": [
    "AUTHORIZATION_CODE"
  ],
  "redirectUris": [
    "http://localhost:3000/callback"
  ],
  "responseTypes": [
    "CODE"
  ],
  "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"enabled\": true,\n    \"name\": \"Shared-Web-App\",\n    \"description\": \"This is an OIDC Web application for workflow testing.\",\n    \"type\": \"WEB_APP\",\n    \"protocol\": \"OPENID_CONNECT\",\n    \"grantTypes\": [\n        \"AUTHORIZATION_CODE\"\n    ],\n    \"redirectUris\": [\n        \"http://localhost:3000/callback\"\n    ],\n    \"responseTypes\": [\n        \"CODE\"\n    ],\n    \"tokenEndpointAuthMethod\": \"CLIENT_SECRET_BASIC\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applications")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7bc39672-6770-4d78-b7f5-09728ca64f41"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "attributes": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7bc39672-6770-4d78-b7f5-09728ca64f41/attributes"
        },
        "secret": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7bc39672-6770-4d78-b7f5-09728ca64f41/secret"
        },
        "grants": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/7bc39672-6770-4d78-b7f5-09728ca64f41/grants"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "id": "7bc39672-6770-4d78-b7f5-09728ca64f41",
    "name": "Shared-Web-App",
    "description": "This is an OIDC Web application for workflow testing.",
    "enabled": true,
    "hiddenFromAppPortal": false,
    "type": "WEB_APP",
    "protocol": "OPENID_CONNECT",
    "createdAt": "2025-03-28T11:43:10.462Z",
    "updatedAt": "2025-03-28T11:43:10.462Z",
    "assignActorRoles": false,
    "responseTypes": [
        "CODE"
    ],
    "grantTypes": [
        "AUTHORIZATION_CODE"
    ],
    "idpSignoff": false,
    "additionalRefreshTokenReplayProtectionEnabled": true,
    "tokenEndpointAuthMethod": "CLIENT_SECRET_BASIC",
    "pkceEnforcement": "OPTIONAL",
    "parRequirement": "OPTIONAL",
    "devicePollingInterval": 5,
    "redirectUris": [
        "http://localhost:3000/callback"
    ],
    "parTimeout": 60,
    "deviceTimeout": 600
}
```

---

---
title: "Step 2: Read All Licenses"
description: Use GET {{apiPath}}/v1/organizations/{{orgID}}/licenses to return the list of licenses associated with your organization. You'll want to do this because an organization can have several licenses, including multiple active licenses (an environment can have one license only). If your organization has more than one license, you can use a filter as a query parameter to limit the licenses returned.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-2-read-all-licenses
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-2-read-all-licenses.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Step 2: Read All Licenses

##

```none
GET {{apiPath}}/v1/organizations/{{orgID}}/licenses
```

Use `GET {{apiPath}}/v1/organizations/{{orgID}}/licenses` to return the list of licenses associated with your organization. You'll want to do this because an organization can have several licenses, including multiple active licenses (an environment can have one license only). If your organization has more than one license, you can use a filter as a query parameter to limit the licenses returned.

You can use the filtering expression `filter=status eq "active"` to return licenses that have a `status` value of `ACTIVE`.

In this request:

* `{{apiPath}}` is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

* `{{orgID}}` is the ID of the organization in which you created your test environment. To find your `orgID`, log in to the PingOne admin console, ensure the environment selected is the one you're currently using, and go to Settings > Environment Properties. The Organization ID is displayed.

When successful, the response returns a `Status: 200 success` message and shows the application's secret.

> **Collapse: Query parameters**
>
> | Query parameter | Attributes (or allowed limits) |
> | --------------- | ------------------------------ |
> | `filter`        | `beginsAt` (lt), `status` (eq) |
> | `order`         | `beginsAt`                     |

### Troubleshooting

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests), and you have a valid access token.

  For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red). The Postman script (in the Scripts tab) in the previous set to get an access token should have set the access token. Note that if Bearer Token and the access token is set correctly here, our Postman scripts will carry these settings forward to the remaining steps in this workflow.

* Verify that you've assigned the Organization Admin role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain.

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
curl --location --globoff '{{apiPath}}/v1/organizations/{{orgID}}/licenses' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/organizations/{{orgID}}/licenses")
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

  url := "{{apiPath}}/v1/organizations/{{orgID}}/licenses"
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
GET /v1/organizations/{{orgID}}/licenses HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/organizations/{{orgID}}/licenses")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/organizations/{{orgID}}/licenses",
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
  'url': '{{apiPath}}/v1/organizations/{{orgID}}/licenses',
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

url = "{{apiPath}}/v1/organizations/{{orgID}}/licenses"

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
$request->setUrl('{{apiPath}}/v1/organizations/{{orgID}}/licenses');
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

url = URI("{{apiPath}}/v1/organizations/{{orgID}}/licenses")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/organizations/{{orgID}}/licenses")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda/licenses"
        }
    },
    "_embedded": {
        "licenses": [
            {
                "_links": {
                    "organization": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda/licenses/38adfae2-f87d-429b-842d-d36a0fa1c66f"
                    }
                },
                "advancedServices": {
                    "pingId": {
                        "included": false,
                        "type": "NONE"
                    }
                },
                "assignedEnvironmentsCount": 0,
                "authorize": {
                    "allowApiAccessManagement": false,
                    "allowDynamicAuthorization": false,
                    "allowApplicationPermissions": false
                },
                "beginsAt": "2020-12-16T00:00:00.000Z",
                "credentials": {
                    "allowCredentials": false,
                    "allowPushNotifications": false
                },
                "environments": {
                    "allowAddResources": false,
                    "allowConnections": true,
                    "allowCustomDomain": false,
                    "allowCustomSchema": false,
                    "allowProduction": false,
                    "max": 5,
                    "regions": [
                        "NORTH_AMERICA"
                    ]
                },
                "expiresAt": "2021-01-15T00:00:00.000Z",
                "fraud": {
                    "allowBotMaliciousDeviceDetection": false,
                    "allowAccountProtection": false,
                    "allowAccountTakeoverDetection": false,
                    "allowNewAccountFraudDetection": false,
                    "allowCredentialSharingDetection": false,
                    "allowDataEnrichment": false
                },
                "gateways": {
                    "allowLdapGateway": false,
                    "allowKerberosGateway": false,
                    "allowRadiusGateway": false
                },
                "id": "38adfae2-f87d-429b-842d-d36a0fa1c66f",
                "intelligence": {
                    "allowReputation": true,
                    "allowGeoVelocity": true,
                    "allowAnonymousNetworkDetection": true,
                    "allowDataConsent": false,
                    "allowRisk": true,
                    "allowAdvancedPredictors": true,
                    "allowIntelligenceProtect": false,
                    "allowIntelligenceNewDevicePredictor": false,
                    "numberOfProtectTransactions": 0
                },
                "mfa": {
                    "allowPushNotification": false,
                    "allowNotificationOutsideWhitelist": false,
                    "allowFido2Devices": false,
                    "allowVoiceOtp": false,
                    "allowEmailOtp": false,
                    "allowSmsOtp": false,
                    "allowTotp": false,
                    "allowPingIDApp": false,
                    "allowOATHToken": false,
                    "allowYubikey": false,
                    "allowWinLogin": false,
                    "allowEditNotificationTemplate": false,
                    "allowPingSmsAccount": true,
                    "allowWhatsAppOtp": false,
                    "allowIntelligenceTrustDevicePredictor": false,
                    "allowPingIdDesktop": false,
                    "allowPingIdDesktopGen2": false
                },
                "name": "RISKTRIAL",
                "orchestrate": {
                    "allowOrchestration": false,
                    "allowAdminAccess": false,
                    "flowsPerEnvironmentMax": 0
                },
                "organization": {
                    "id": "bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                },
                "package": "RISKTRIAL",
                "status": "TERMINATED",
                "terminatesAt": "2021-01-15T00:00:00.000Z",
                "users": {
                    "max": 12000,
                    "hardLimitMax": 13201,
                    "annualActiveIncluded": 1000,
                    "allowPasswordPolicy": false,
                    "allowPasswordManagementNotifications": false,
                    "allowVerificationFlow": false,
                    "allowIdentityProviders": false,
                    "allowMyAccount": false,
                    "allowProvisioning": false,
                    "allowInboundProvisioning": false,
                    "allowRoleAssignment": false,
                    "allowPasswordOnlyAuthentication": false,
                    "allowUpdateSelf": false,
                    "allowUniversalDeviceId": false,
                    "entitledToSupport": false
                },
                "verify": {
                    "allowPushNotifications": false,
                    "allowDocumentMatch": false,
                    "allowFaceMatch": false,
                    "allowManualIdInspection": false,
                    "allowAamva": false,
                    "allowVoice": false,
                    "allowDigitalVerifications": false,
                    "allowManualIDStepUpInspection": false,
                    "allowUniversalCapture": false,
                    "allowAccountOwnership": false,
                    "allowAadhaar": false,
                    "numberOfManualIDStepUpInspection": 0,
                    "numberOfDigitalVerifications": 0,
                    "numberOfUniversalCapture": 0,
                    "numberOfAAMVA": 0,
                    "numberOfVoiceBiometrics": 0,
                    "numberOfFaceVerifications": 0,
                    "numberOfManualIdInspections": 0,
                    "numberOfDocumentMatches": 0,
                    "numberOfAccountOwnership": 0,
                    "numberOfAadhaar": 0,
                    "numberOfDataVerifications": 0,
                    "numberOfLiveAgent": 0,
                    "numberOfDeviceReputationScoring": 0,
                    "numberOfGlobalWatchlist": 0,
                    "numberOfDataVerificationGroup1": 0,
                    "numberOfDataVerificationGroup2": 0,
                    "numberOfDataVerificationGroup3": 0,
                    "numberOfDataVerificationGroup4": 0,
                    "numberOfDataVerificationGroup5": 0
                }
            },
            {
                "_links": {
                    "organization": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda/licenses/3f06970a-3235-46cb-b46f-cf6dfee2bb84"
                    }
                },
                "advancedServices": {
                    "pingId": {
                        "included": true,
                        "type": "FULL"
                    }
                },
                "assignedEnvironmentsCount": 7,
                "authorize": {
                    "allowApiAccessManagement": true,
                    "allowDynamicAuthorization": true,
                    "allowApplicationPermissions": true
                },
                "beginsAt": "2020-07-08T19:15:57.324Z",
                "credentials": {
                    "allowCredentials": true,
                    "allowPushNotifications": true
                },
                "environments": {
                    "allowAddResources": true,
                    "allowConnections": true,
                    "allowCustomDomain": true,
                    "allowCustomSchema": true,
                    "allowProduction": true,
                    "max": 50,
                    "regions": [
                        "AP",
                        "NORTH_AMERICA",
                        "EU"
                    ]
                },
                "expiresAt": "2100-01-31T00:00:00.324Z",
                "fraud": {
                    "allowBotMaliciousDeviceDetection": true,
                    "allowAccountProtection": true,
                    "allowAccountTakeoverDetection": true,
                    "allowNewAccountFraudDetection": true,
                    "allowCredentialSharingDetection": true,
                    "allowDataEnrichment": true
                },
                "gateways": {
                    "allowLdapGateway": true,
                    "allowKerberosGateway": true,
                    "allowRadiusGateway": true
                },
                "id": "3f06970a-3235-46cb-b46f-cf6dfee2bb84",
                "intelligence": {
                    "allowReputation": true,
                    "allowGeoVelocity": true,
                    "allowAnonymousNetworkDetection": true,
                    "allowDataConsent": true,
                    "allowRisk": true,
                    "allowAdvancedPredictors": true,
                    "allowIntelligenceProtect": true,
                    "allowIntelligenceNewDevicePredictor": true,
                    "numberOfProtectTransactions": 0
                },
                "mfa": {
                    "allowPushNotification": true,
                    "allowNotificationOutsideWhitelist": true,
                    "allowFido2Devices": true,
                    "allowVoiceOtp": true,
                    "allowEmailOtp": true,
                    "allowSmsOtp": true,
                    "allowTotp": true,
                    "allowPingIDApp": true,
                    "allowOATHToken": true,
                    "allowYubikey": true,
                    "allowWinLogin": true,
                    "allowEditNotificationTemplate": true,
                    "allowPingSmsAccount": true,
                    "allowWhatsAppOtp": true,
                    "allowIntelligenceTrustDevicePredictor": true,
                    "allowPingIdDesktop": true,
                    "allowPingIdDesktopGen2": true
                },
                "name": "INTERNAL",
                "orchestrate": {
                    "allowOrchestration": true,
                    "allowAdminAccess": true,
                    "flowsPerEnvironmentMax": 100
                },
                "organization": {
                    "id": "bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                },
                "package": "INTERNAL",
                "status": "ACTIVE",
                "users": {
                    "max": 50000000,
                    "hardLimitMax": 50000000,
                    "annualActiveIncluded": 10000000,
                    "allowPasswordPolicy": true,
                    "allowPasswordManagementNotifications": true,
                    "allowVerificationFlow": true,
                    "allowIdentityProviders": true,
                    "allowMyAccount": true,
                    "allowProvisioning": true,
                    "allowInboundProvisioning": true,
                    "allowRoleAssignment": true,
                    "allowPasswordOnlyAuthentication": true,
                    "allowUpdateSelf": true,
                    "allowUniversalDeviceId": true,
                    "entitledToSupport": true
                },
                "verify": {
                    "allowPushNotifications": true,
                    "allowDocumentMatch": true,
                    "allowFaceMatch": true,
                    "allowManualIdInspection": false,
                    "allowAamva": true,
                    "allowVoice": true,
                    "allowDigitalVerifications": true,
                    "allowManualIDStepUpInspection": false,
                    "allowUniversalCapture": true,
                    "allowAccountOwnership": true,
                    "allowAadhaar": true,
                    "numberOfManualIDStepUpInspection": 0,
                    "numberOfDigitalVerifications": 0,
                    "numberOfUniversalCapture": 0,
                    "numberOfAAMVA": 0,
                    "numberOfVoiceBiometrics": 0,
                    "numberOfFaceVerifications": 0,
                    "numberOfManualIdInspections": 0,
                    "numberOfDocumentMatches": 0,
                    "numberOfAccountOwnership": 0,
                    "numberOfAadhaar": 0,
                    "numberOfDataVerifications": 500,
                    "numberOfLiveAgent": 500,
                    "numberOfDeviceReputationScoring": 500,
                    "numberOfGlobalWatchlist": 500,
                    "numberOfDataVerificationGroup1": 500,
                    "numberOfDataVerificationGroup2": 500,
                    "numberOfDataVerificationGroup3": 500,
                    "numberOfDataVerificationGroup4": 500,
                    "numberOfDataVerificationGroup5": 500
                }
            },
            {
                "_links": {
                    "organization": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda/licenses/4bfa577b-2ece-49d6-ab8b-8f105d11aa49"
                    }
                },
                "advancedServices": {
                    "pingId": {
                        "included": false,
                        "type": "NONE"
                    }
                },
                "assignedEnvironmentsCount": 1,
                "authorize": {
                    "allowApiAccessManagement": false,
                    "allowDynamicAuthorization": false,
                    "allowApplicationPermissions": false
                },
                "beginsAt": "2025-11-19T18:23:29.281Z",
                "credentials": {
                    "allowCredentials": false,
                    "allowPushNotifications": false
                },
                "environments": {
                    "allowAddResources": false,
                    "allowConnections": false,
                    "allowCustomDomain": false,
                    "allowCustomSchema": false,
                    "allowProduction": false,
                    "max": 100,
                    "regions": [
                        "NORTH_AMERICA"
                    ]
                },
                "expiresAt": "2025-11-19T18:24:29.281Z",
                "fraud": {
                    "allowBotMaliciousDeviceDetection": false,
                    "allowAccountProtection": false,
                    "allowAccountTakeoverDetection": false,
                    "allowNewAccountFraudDetection": false,
                    "allowCredentialSharingDetection": false,
                    "allowDataEnrichment": false
                },
                "gateways": {
                    "allowLdapGateway": false,
                    "allowKerberosGateway": false,
                    "allowRadiusGateway": false
                },
                "id": "4bfa577b-2ece-49d6-ab8b-8f105d11aa49",
                "intelligence": {
                    "allowReputation": false,
                    "allowGeoVelocity": false,
                    "allowAnonymousNetworkDetection": false,
                    "allowDataConsent": false,
                    "allowRisk": false,
                    "allowAdvancedPredictors": false,
                    "allowIntelligenceProtect": false,
                    "allowIntelligenceNewDevicePredictor": false,
                    "numberOfProtectTransactions": 0
                },
                "mfa": {
                    "allowPushNotification": false,
                    "allowNotificationOutsideWhitelist": false,
                    "allowFido2Devices": false,
                    "allowVoiceOtp": false,
                    "allowEmailOtp": false,
                    "allowSmsOtp": false,
                    "allowTotp": false,
                    "allowPingIDApp": false,
                    "allowOATHToken": false,
                    "allowYubikey": false,
                    "allowWinLogin": false,
                    "allowEditNotificationTemplate": false,
                    "allowPingSmsAccount": false,
                    "allowPingIdDesktop": false,
                    "allowPingIdDesktopGen2": false
                },
                "name": "Unlicensed",
                "orchestrate": {
                    "allowOrchestration": false,
                    "allowAdminAccess": false,
                    "flowsPerEnvironmentMax": 0
                },
                "organization": {
                    "id": "bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                },
                "package": "NO LICENSE",
                "status": "TERMINATED",
                "terminatesAt": "2025-11-19T18:24:30.281Z",
                "users": {
                    "max": 0,
                    "hardLimitMax": 0,
                    "annualActiveIncluded": 0,
                    "allowPasswordPolicy": false,
                    "allowPasswordManagementNotifications": false,
                    "allowVerificationFlow": false,
                    "allowIdentityProviders": false,
                    "allowMyAccount": false,
                    "allowProvisioning": false,
                    "allowInboundProvisioning": false,
                    "allowRoleAssignment": false,
                    "allowPasswordOnlyAuthentication": false,
                    "allowUpdateSelf": false,
                    "allowUniversalDeviceId": false,
                    "entitledToSupport": false
                },
                "verify": {
                    "allowPushNotifications": false,
                    "allowDocumentMatch": false,
                    "allowFaceMatch": false,
                    "allowManualIdInspection": false,
                    "allowAamva": false,
                    "allowVoice": false,
                    "allowDigitalVerifications": false,
                    "allowManualIDStepUpInspection": false,
                    "allowUniversalCapture": false,
                    "allowAccountOwnership": false,
                    "allowAadhaar": false,
                    "numberOfManualIDStepUpInspection": 0,
                    "numberOfDigitalVerifications": 0,
                    "numberOfUniversalCapture": 0,
                    "numberOfAAMVA": 0,
                    "numberOfVoiceBiometrics": 0,
                    "numberOfFaceVerifications": 0,
                    "numberOfManualIdInspections": 0,
                    "numberOfDocumentMatches": 0,
                    "numberOfAccountOwnership": 0,
                    "numberOfAadhaar": 0,
                    "numberOfDataVerifications": 0,
                    "numberOfLiveAgent": 0,
                    "numberOfDeviceReputationScoring": 0,
                    "numberOfGlobalWatchlist": 0,
                    "numberOfDataVerificationGroup1": 0,
                    "numberOfDataVerificationGroup2": 0,
                    "numberOfDataVerificationGroup3": 0,
                    "numberOfDataVerificationGroup4": 0,
                    "numberOfDataVerificationGroup5": 0
                }
            },
            {
                "_links": {
                    "organization": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda/licenses/748bea25-0178-4a62-a6d0-8046b7a2d907"
                    }
                },
                "advancedServices": {
                    "pingId": {
                        "included": false,
                        "type": "NONE"
                    }
                },
                "assignedEnvironmentsCount": 0,
                "authorize": {
                    "allowApiAccessManagement": false,
                    "allowDynamicAuthorization": false,
                    "allowApplicationPermissions": false
                },
                "beginsAt": "2020-09-30T00:00:00.000Z",
                "credentials": {
                    "allowCredentials": false,
                    "allowPushNotifications": false
                },
                "environments": {
                    "allowAddResources": false,
                    "allowConnections": true,
                    "allowCustomDomain": false,
                    "allowCustomSchema": false,
                    "allowProduction": false,
                    "max": 5,
                    "regions": [
                        "NORTH_AMERICA"
                    ]
                },
                "expiresAt": "2020-10-30T00:00:00.000Z",
                "fraud": {
                    "allowBotMaliciousDeviceDetection": false,
                    "allowAccountProtection": false,
                    "allowAccountTakeoverDetection": false,
                    "allowNewAccountFraudDetection": false,
                    "allowCredentialSharingDetection": false,
                    "allowDataEnrichment": false
                },
                "gateways": {
                    "allowLdapGateway": false,
                    "allowKerberosGateway": false,
                    "allowRadiusGateway": true
                },
                "id": "748bea25-0178-4a62-a6d0-8046b7a2d907",
                "intelligence": {
                    "allowReputation": false,
                    "allowGeoVelocity": false,
                    "allowAnonymousNetworkDetection": false,
                    "allowDataConsent": false,
                    "allowRisk": false,
                    "allowAdvancedPredictors": false,
                    "allowIntelligenceProtect": false,
                    "allowIntelligenceNewDevicePredictor": false,
                    "numberOfProtectTransactions": 0
                },
                "mfa": {
                    "allowPushNotification": true,
                    "allowNotificationOutsideWhitelist": false,
                    "allowFido2Devices": true,
                    "allowVoiceOtp": true,
                    "allowEmailOtp": true,
                    "allowSmsOtp": true,
                    "allowTotp": true,
                    "allowPingIDApp": false,
                    "allowOATHToken": false,
                    "allowYubikey": false,
                    "allowWinLogin": false,
                    "allowEditNotificationTemplate": false,
                    "allowPingSmsAccount": true,
                    "allowWhatsAppOtp": true,
                    "allowIntelligenceTrustDevicePredictor": false,
                    "allowPingIdDesktop": false,
                    "allowPingIdDesktopGen2": false
                },
                "name": "MFA TRIAL",
                "orchestrate": {
                    "allowOrchestration": false,
                    "allowAdminAccess": false,
                    "flowsPerEnvironmentMax": 0
                },
                "organization": {
                    "id": "bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                },
                "package": "MFA TRIAL",
                "status": "TERMINATED",
                "terminatesAt": "2020-10-30T00:00:00.000Z",
                "users": {
                    "max": 1000000,
                    "hardLimitMax": 1100000,
                    "annualActiveIncluded": 1000,
                    "allowPasswordPolicy": false,
                    "allowPasswordManagementNotifications": false,
                    "allowVerificationFlow": false,
                    "allowIdentityProviders": false,
                    "allowMyAccount": true,
                    "allowProvisioning": false,
                    "allowInboundProvisioning": false,
                    "allowRoleAssignment": false,
                    "allowPasswordOnlyAuthentication": false,
                    "allowUpdateSelf": false,
                    "allowUniversalDeviceId": false,
                    "entitledToSupport": false
                },
                "verify": {
                    "allowPushNotifications": false,
                    "allowDocumentMatch": false,
                    "allowFaceMatch": false,
                    "allowManualIdInspection": false,
                    "allowAamva": false,
                    "allowVoice": false,
                    "allowDigitalVerifications": false,
                    "allowManualIDStepUpInspection": false,
                    "allowUniversalCapture": false,
                    "allowAccountOwnership": false,
                    "allowAadhaar": false,
                    "numberOfManualIDStepUpInspection": 0,
                    "numberOfDigitalVerifications": 0,
                    "numberOfUniversalCapture": 0,
                    "numberOfAAMVA": 0,
                    "numberOfVoiceBiometrics": 0,
                    "numberOfFaceVerifications": 0,
                    "numberOfManualIdInspections": 0,
                    "numberOfDocumentMatches": 0,
                    "numberOfAccountOwnership": 0,
                    "numberOfAadhaar": 0,
                    "numberOfDataVerifications": 0,
                    "numberOfLiveAgent": 0,
                    "numberOfDeviceReputationScoring": 0,
                    "numberOfGlobalWatchlist": 0,
                    "numberOfDataVerificationGroup1": 0,
                    "numberOfDataVerificationGroup2": 0,
                    "numberOfDataVerificationGroup3": 0,
                    "numberOfDataVerificationGroup4": 0,
                    "numberOfDataVerificationGroup5": 0
                }
            },
            {
                "_links": {
                    "organization": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                    },
                    "self": {
                        "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda/licenses/8ec37673-2528-49ff-a9cc-e8cab67d2a7f"
                    }
                },
                "advancedServices": {
                    "pingId": {
                        "included": false,
                        "type": "NONE"
                    }
                },
                "assignedEnvironmentsCount": 0,
                "authorize": {
                    "allowApiAccessManagement": false,
                    "allowDynamicAuthorization": false,
                    "allowApplicationPermissions": false
                },
                "beginsAt": "2024-09-24T16:47:31.918Z",
                "credentials": {
                    "allowCredentials": false,
                    "allowPushNotifications": false
                },
                "environments": {
                    "allowAddResources": true,
                    "allowConnections": false,
                    "allowCustomDomain": false,
                    "allowCustomSchema": false,
                    "allowProduction": true,
                    "max": 1,
                    "regions": [
                        "NORTH_AMERICA"
                    ]
                },
                "expiresAt": "2100-01-31T00:00:00.324Z",
                "fraud": {
                    "allowBotMaliciousDeviceDetection": false,
                    "allowAccountProtection": false,
                    "allowAccountTakeoverDetection": false,
                    "allowNewAccountFraudDetection": false,
                    "allowCredentialSharingDetection": false,
                    "allowDataEnrichment": false
                },
                "gateways": {
                    "allowLdapGateway": false,
                    "allowKerberosGateway": false,
                    "allowRadiusGateway": false
                },
                "id": "8ec37673-2528-49ff-a9cc-e8cab67d2a7f",
                "intelligence": {
                    "allowReputation": true,
                    "allowGeoVelocity": true,
                    "allowAnonymousNetworkDetection": true,
                    "allowDataConsent": false,
                    "allowRisk": false,
                    "allowAdvancedPredictors": false,
                    "allowIntelligenceProtect": false,
                    "allowIntelligenceNewDevicePredictor": false,
                    "numberOfProtectTransactions": 0
                },
                "mfa": {
                    "allowPushNotification": true,
                    "allowNotificationOutsideWhitelist": false,
                    "allowFido2Devices": true,
                    "allowVoiceOtp": false,
                    "allowEmailOtp": true,
                    "allowSmsOtp": false,
                    "allowTotp": true,
                    "allowPingIDApp": false,
                    "allowOATHToken": false,
                    "allowYubikey": false,
                    "allowWinLogin": false,
                    "allowEditNotificationTemplate": false,
                    "allowPingSmsAccount": true,
                    "allowWhatsAppOtp": true,
                    "allowIntelligenceTrustDevicePredictor": false,
                    "allowPingIdDesktop": false,
                    "allowPingIdDesktopGen2": false
                },
                "name": "ADMIN",
                "orchestrate": {
                    "allowOrchestration": false,
                    "allowAdminAccess": false,
                    "flowsPerEnvironmentMax": 0
                },
                "organization": {
                    "id": "bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
                },
                "package": "ADMIN",
                "status": "ACTIVE",
                "users": {
                    "max": 600,
                    "hardLimitMax": 660,
                    "annualActiveIncluded": 50,
                    "allowPasswordPolicy": true,
                    "allowPasswordManagementNotifications": true,
                    "allowVerificationFlow": true,
                    "allowIdentityProviders": true,
                    "allowMyAccount": true,
                    "allowProvisioning": false,
                    "allowInboundProvisioning": false,
                    "allowRoleAssignment": true,
                    "allowPasswordOnlyAuthentication": true,
                    "allowUpdateSelf": true,
                    "allowUniversalDeviceId": true,
                    "entitledToSupport": false
                },
                "verify": {
                    "allowPushNotifications": false,
                    "allowDocumentMatch": false,
                    "allowFaceMatch": false,
                    "allowManualIdInspection": false,
                    "allowAamva": false,
                    "allowVoice": false,
                    "allowDigitalVerifications": false,
                    "allowManualIDStepUpInspection": false,
                    "allowUniversalCapture": false,
                    "allowAccountOwnership": false,
                    "allowAadhaar": false,
                    "numberOfManualIDStepUpInspection": 0,
                    "numberOfDigitalVerifications": 0,
                    "numberOfUniversalCapture": 0,
                    "numberOfAAMVA": 0,
                    "numberOfVoiceBiometrics": 0,
                    "numberOfFaceVerifications": 0,
                    "numberOfManualIdInspections": 0,
                    "numberOfDocumentMatches": 0,
                    "numberOfAccountOwnership": 0,
                    "numberOfAadhaar": 0,
                    "numberOfDataVerifications": 0,
                    "numberOfLiveAgent": 0,
                    "numberOfDeviceReputationScoring": 0,
                    "numberOfGlobalWatchlist": 0,
                    "numberOfDataVerificationGroup1": 0,
                    "numberOfDataVerificationGroup2": 0,
                    "numberOfDataVerificationGroup3": 0,
                    "numberOfDataVerificationGroup4": 0,
                    "numberOfDataVerificationGroup5": 0
                }
            }
        ]
    },
    "count": 5,
    "size": 5
}
```

---

---
title: "Step 3: Assign roles to the Worker app"
description: In the application information page for your new Worker app, you'll assign the roles that grant admin-level permissions to the Worker app.
component: pingone-api
page_id: pingone-api:getting-started:create-an-admin-worker-app/step-3-assign-roles
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-an-admin-worker-app/step-3-assign-roles.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Step 3: Assign roles to the Worker app

In the application information page for your new Worker app, you'll assign the roles that grant admin-level permissions to the Worker app.

1. In the Roles tab, click Grant Roles. The best practice is to ensure the roles assigned to the Worker app are limited to only those necessary. For this workflow, grant the roles and permissions as shown.

   1a. Assign the Organization Admin role as shown. This role is needed to create a new environment:

   ![Admin-Console-Worker-App-Org-Admin-Role](../../_images/p1_ui-orgAdmin.png)

   1b. Expand the Environment Admin role:

   ![Admin-Console-Worker-App-Env-Admin-Role](../../_images/p1_ui-envAdmin1.png)

   1c. Click the Organization checkbox for the Environment Admin role, and note the information displayed:

   ![Admin-Console-Worker-App-Env-Admin-Role](../../_images/p1_ui-envAdmin2.png)

2. Click **Save**.

3. The roles and permissions you've granted are then displayed. They should look like this:

   ![Admin-Console-Worker-App-Env-Admin-Role](../../_images/p1_ui-assignedRoles.png)

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The roles and permissions apply only to the Worker app, and not to any PingOne admin user. We'll show you how to assign these permissions to an admin user when you get to the create a test environment workflow. |

When you subsequently call Management API requests, as you will in steps 2-5 of the next workflow to create a test environment, you'll see one or more of these PingOne role icons beneath the request title:

| Role                          | Can Assign                                                          |
| ----------------------------- | ------------------------------------------------------------------- |
| Organization Admin            | Environment Admin                                                   |
| Environment Admin             | All roles except Organization Admin                                 |
| Identity Data Admin           | Identity Data Admin, Identity Data Read-Only Admin, Help Desk Admin |
| DaVinci Admin                 | DaVinci Admin, DaVinci Read-Only Admin                              |
| Custom Role Admin             | None                                                                |
| Application Owner             | None                                                                |
| Identity Data Read-Only Admin | None                                                                |
| Configuration Read-Only Admin | None                                                                |
| DaVinci Read-Only Admin       | None                                                                |
| Client Application Developer  | None                                                                |
| Help Desk Admin               | None                                                                |
| Privilege Admin               | None                                                                |

For example, in the request documentation to GET all applications for an environment, either the Client Application Developer or Environment Admin role is required to call the request:

![Admin-Console-Worker-App-Env-Admin-Role](../../_images/p1_get-all-apps.png)

For some requests, multiple roles have permissions necessary to call the request. As long as your Worker app has at least one of the roles shown for the request, the Worker app can make the call.

---

---
title: "Step 3: Create an environment"
description: Use the POST {{apiPath}}/v1/environments request to create a new environment. You need to have the Organization Admin role to create an environment. You're automatically assigned the Organization Admin role when you create a PingOne account.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-3-create-an-environment
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-3-create-an-environment.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 3: Create an environment

##

```none
POST {{apiPath}}/v1/environments
```

Use the `POST {{apiPath}}/v1/environments` request to create a new environment. You need to have the Organization Admin role to create an environment. You're automatically assigned the Organization Admin role when you create a PingOne account.

When your organization includes more than one PingOne license, you must include the following JSON with a valid license ID in the request body.

```json
 "license": {
    "id": "{{licenseID}}"
  }
```

The new environment will include several PingOne resources automatically created for a new environment (such as, a default sign-on policy, password policy, a default population, and defined notifications templates). This workflow uses the environment's default sign-on policy and password policy to simplify the workflow.

In this request:

* ``{{apiPath}}`is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1`` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

In the request body:

* `name` is required, and is a String containing the name to assign to the environment.

* `description` is optional, and describes the purpose of the environment.

* `type` can be either `SANDBOX` or `PRODUCTION`. In this case, use `SANDBOX`.

When successful, the response returns a `Status: 201 created` message, and shows the new environment's configuration data.

The response includes an `id` property value (a UUID) for your new environment. If you're using Postman, the script in the Script tab sets `{{envID}}` to this value. Every request in this workflow uses `{{envID}}` in the request URL to specify the PingOne resources associated with your environment.

It's useful to sign on to the PingOne admin console, and see your new environment shown. Note that there is no associated population, which you'll create in the next step.

### Troubleshooting

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests), and you have a valid access token.

  For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red). The Postman script (in the Scripts tab) in the previous set to get an access token should have set the access token. Note that if Bearer Token and the access token is set correctly here, our Postman scripts will carry these settings forward to the remaining steps in this workflow.

* Verify that you've assigned the Organization Admin role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain.

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
  "name": "New-Solution-Env_{{$timestamp}}",
  "description": "New environment description",
  "type": "SANDBOX",
  "region": "NA",
    "license": {
        "id": "{{licenseID}}"
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
curl --location --globoff '{{apiPath}}/v1/environments' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
  "name": "New-Solution-Env_{{$timestamp}}",
  "description": "New environment description",
  "type": "SANDBOX",
  "region": "NA",
    "license": {
        "id": "{{licenseID}}"
    }
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"  ""name"": ""New-Solution-Env_{{$timestamp}}""," + "\n" +
@"  ""description"": ""New environment description""," + "\n" +
@"  ""type"": ""SANDBOX""," + "\n" +
@"  ""region"": ""NA""," + "\n" +
@"    ""license"": {" + "\n" +
@"        ""id"": ""{{licenseID}}""" + "\n" +
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

  url := "{{apiPath}}/v1/environments"
  method := "POST"

  payload := strings.NewReader(`{
  "name": "New-Solution-Env_{{$timestamp}}",
  "description": "New environment description",
  "type": "SANDBOX",
  "region": "NA",
    "license": {
        "id": "{{licenseID}}"
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
POST /v1/environments HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
  "name": "New-Solution-Env_{{$timestamp}}",
  "description": "New environment description",
  "type": "SANDBOX",
  "region": "NA",
    "license": {
        "id": "{{licenseID}}"
    }
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"New-Solution-Env_{{$timestamp}}\",\n  \"description\": \"New environment description\",\n  \"type\": \"SANDBOX\",\n  \"region\": \"NA\",\n    \"license\": {\n        \"id\": \"{{licenseID}}\"\n    }\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "New-Solution-Env_{{$timestamp}}",
    "description": "New environment description",
    "type": "SANDBOX",
    "region": "NA",
    "license": {
      "id": "{{licenseID}}"
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
  'url': '{{apiPath}}/v1/environments',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "New-Solution-Env_{{$timestamp}}",
    "description": "New environment description",
    "type": "SANDBOX",
    "region": "NA",
    "license": {
      "id": "{{licenseID}}"
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

url = "{{apiPath}}/v1/environments"

payload = json.dumps({
  "name": "New-Solution-Env_{{$timestamp}}",
  "description": "New environment description",
  "type": "SANDBOX",
  "region": "NA",
  "license": {
    "id": "{{licenseID}}"
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
$request->setUrl('{{apiPath}}/v1/environments');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n  "name": "New-Solution-Env_{{$timestamp}}",\n  "description": "New environment description",\n  "type": "SANDBOX",\n  "region": "NA",\n    "license": {\n        "id": "{{licenseID}}"\n    }\n}');
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

url = URI("{{apiPath}}/v1/environments")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "New-Solution-Env_{{\$timestamp}}",
  "description": "New environment description",
  "type": "SANDBOX",
  "region": "NA",
  "license": {
    "id": "{{licenseID}}"
  }
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n  \"name\": \"New-Solution-Env_{{$timestamp}}\",\n  \"description\": \"New environment description\",\n  \"type\": \"SANDBOX\",\n  \"region\": \"NA\",\n    \"license\": {\n        \"id\": \"{{licenseID}}\"\n    }\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "organization": {
            "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
        },
        "license": {
            "href": "https://api.pingone.com/v1/organizations/bed432e6-676a-4ebe-b5a5-6b3b54e46bda/licenses/57f0efac-37d9-4a17-8a35-196bb3362983"
        },
        "populations": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations"
        },
        "users": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users"
        },
        "applications": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications"
        },
        "activities": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/activities"
        },
        "branding": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/branding"
        },
        "resources": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/resources"
        },
        "passwordPolicies": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/passwordPolicies"
        },
        "userActivities": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/userActivities"
        },
        "signOnPolicies": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/signOnPolicies"
        },
        "keys": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/keys"
        },
        "templates": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/templates"
        },
        "notificationsSettings": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/notificationsSettings"
        },
        "schemas": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/schemas"
        },
        "gateways": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/gateways"
        },
        "capabilities": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/capabilities"
        },
        "activeIdentityCounts": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/activeIdentityCounts"
        },
        "propagation/plans": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/propagation/plans"
        },
        "propagation/stores": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/propagation/stores"
        },
        "propagation/revisions/id:latest": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/propagation/revisions/id:latest"
        },
        "billOfMaterials": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/billOfMaterials"
        }
    },
    "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6",
    "name": "New-Solution-Env_1680720342",
    "description": "New environment description",
    "organization": {
        "id": "bed432e6-676a-4ebe-b5a5-6b3b54e46bda"
    },
    "type": "SANDBOX",
    "region": "NA",
    "createdAt": "2023-04-05T18:45:41.822Z",
    "updatedAt": "2023-04-05T18:45:41.822Z",
    "license": {
        "id": "57f0efac-37d9-4a17-8a35-196bb3362983"
    },
    "billOfMaterials": {
        "products": [
            {
                "id": "f27354d1-3604-45b6-a9ca-117b04465db5",
                "type": "PING_ONE_BASE",
                "description": "PingOne Base"
            },
            {
                "id": "2d367bc0-1bbb-436a-994d-3079d106a481",
                "type": "PING_ONE_MFA",
                "description": "PingOne MFA"
            },
            {
                "id": "b6d91834-94a2-44f8-924a-5757cf9f70b3",
                "type": "PING_ONE_RISK",
                "description": "PingOne Risk"
            },
            {
                "id": "f1e950d2-babf-4599-b0f4-0e11d0cefa30",
                "type": "PING_ONE_PROVISIONING",
                "description": "PingOne Provisioning"
            },
            {
                "id": "8af7b167-e802-41de-b940-20740d0e7202",
                "type": "PING_ONE_VERIFY",
                "description": "PingOne Verify"
            },
            {
                "id": "b332968c-6f93-4432-81b0-be36d954934a",
                "type": "PING_ONE_AUTHORIZE",
                "description": "PingOne Authorize"
            },
            {
                "id": "86b9e37a-eaa9-4d4e-be03-321489636c01",
                "type": "PING_ONE_DAVINCI",
                "description": "PingOne DaVinci"
            }
        ],
        "createdAt": "2023-04-05T18:45:41.845Z",
        "updatedAt": "2023-04-05T18:45:41.845Z"
    }
}
```

---

---
title: "Step 3: Get the application secret"
description: Use the GET {{apiPath}}/v1/environments/{{envID}}/applications/{{solutionAppID}}/secret operation to get the application's secret. The application secret serves as the application's password. This will be needed to authenticate the token request in a subsequent step.
component: pingone-api
page_id: pingone-api:getting-started:simple-sso-workflow/step-3-get-the-application-secret
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/simple-sso-workflow/step-3-get-the-application-secret.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Step 3: Get the application secret

##

```none
GET {{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret
```

Use the `GET {{apiPath}}/v1/environments/{{envID}}/applications/{{solutionAppID}}/secret` operation to get the application's secret. The application secret serves as the application's password. This will be needed to authenticate the token request in a subsequent step.

In this request:

* ``{{apiPath}}`is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1`` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html#pingone-api-domains) for the top-level domains for other regions.

* `{{envID}}` is the ID of the environment you created when you created your test environment. Refer to [Create Your Test Environment](../create-a-test-environment.html).

* `{{solutionAppID}}` is the Web application ID returned by your previous request to create the Web application.

* When successful, the response returns a `Status: 200 success` message and shows the application's secret.

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've assigned either the Environment Admin or Client Application Developer role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests), and you have a valid access token. For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red).

* Verify that the `{{solutionAppID}}` value is the Web application ID value returned by the previous step to create a Web application. For Postman users, unassigned variables are shown in red, and assigned variables in blue.

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain .

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret"
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
GET /v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret',
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

url = "{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/applications/{{sharedWebAppID}}/secret")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/106d8426-5b47-43e9-b0ed-ae32a708c3c1/secret"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "application": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/applications/106d8426-5b47-43e9-b0ed-ae32a708c3c1"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "secret": "mKxZl...."
}
```

---

---
title: "Step 4: Copy Worker app credentials"
description: While still in the application information page for your new Worker app, you'll get the Worker app credentials, and enable the Worker app.
component: pingone-api
page_id: pingone-api:getting-started:create-an-admin-worker-app/step-4-app-credentials
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-an-admin-worker-app/step-4-app-credentials.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Step 4: Copy Worker app credentials

While still in the application information page for your new Worker app, you'll get the Worker app credentials, and enable the Worker app.

1. Select the Overview tab. The general information for your Worker app is displayed. In particular, you'll see the Environment ID, and the credentials for your Worker app: the Client ID, and Client Secret.

   ![Admin-Console-ClientId-and-Secret](../../_images/p1_ui-overviewInfo.png)

(The Connection Details information isn't shown here for brevity.)

1. Copy the **Client ID** and **Client Secret** values for your Worker app. You'll need these credentials when obtaining an admin access token in the subsequent workflow to create your test environment.

2. Also copy the **Environment ID**. You'll need this because this is the environment in which you created the Worker app. When you need to get an access token for your Worker app, as you will in the next workflows, this is the environment you'll specify for the request.

3. Click the toggle at the upper right to enable the application. The Worker app is saved, and you can now close the application information page.

|   |                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These credentials apply only to the Worker app, and at this point, not to any PingOne admin user. An admin user will need the same roles and permissions for the credentials to be available. We'll show you how to assign the roles and permissions necessary to an admin user when you get to the create a test environment workflow. |

You're now all set to use the PingOne APIs in the next workflows.

---

---
title: "Step 4: Create a population"
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/populations operation to create a new population. All users in PingOne must be associated with a population. Although your new environment automatically includes a default population, creating a new population gives you the ability to associate this user with a more specific population grouping.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-4-create-a-population
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-4-create-a-population.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 4: Create a population

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/populations
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/populations` operation to create a new population. All users in PingOne must be associated with a population. Although your new environment automatically includes a default population, creating a new population gives you the ability to associate this user with a more specific population grouping.

In this request:

* ``{{apiPath}}`is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1`` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

* `{{envID}}` is the ID of the environment you created in the previous step. If you're using Postman, this value is automatically set by the script in the Script tab used for the previous step.

In the request body:

* `name` is a String containing the name to assign to the new population. This is already specified for you in the request body, although you can choose to change it.

* `description` is an optional property describing the new population. This is already specified for you in the request body, although you can choose to change it.

When successful, the request returns a `Status: 201 created` message and shows the new population's configuration data.

The response data includes the population's `id` property. If you're using Postman, the script in the Script tab automatically sets `{{sharedPopID}}` to this value. The `{{sharedPopID}}` property is needed to create the new user in the next step.

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've assigned the Environment Admin role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests), and you have a valid access token. For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red).

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain .

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "name": "Shared-Test-User-Population",
    "description": "Population for PingOne test users"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/populations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "name": "Shared-Test-User-Population",
    "description": "Population for PingOne test users"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/populations")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""name"": ""Shared-Test-User-Population""," + "\n" +
@"    ""description"": ""Population for PingOne test users""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/populations"
  method := "POST"

  payload := strings.NewReader(`{
    "name": "Shared-Test-User-Population",
    "description": "Population for PingOne test users"
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
POST /v1/environments/{{envID}}/populations HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "name": "Shared-Test-User-Population",
    "description": "Population for PingOne test users"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"name\": \"Shared-Test-User-Population\",\n    \"description\": \"Population for PingOne test users\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/populations")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/populations",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "name": "Shared-Test-User-Population",
    "description": "Population for PingOne test users"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/populations',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "name": "Shared-Test-User-Population",
    "description": "Population for PingOne test users"
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

url = "{{apiPath}}/v1/environments/{{envID}}/populations"

payload = json.dumps({
  "name": "Shared-Test-User-Population",
  "description": "Population for PingOne test users"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/populations');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "name": "Shared-Test-User-Population",\n    "description": "Population for PingOne test users"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/populations")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "name": "Shared-Test-User-Population",
  "description": "Population for PingOne test users"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"name\": \"Shared-Test-User-Population\",\n    \"description\": \"Population for PingOne test users\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/populations")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/fe09831e-bbf7-46f1-92e4-aafe10df56fd"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "theme": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/themes/5ab94557-59c3-4afc-bbf6-046444bd04b8"
        }
    },
    "id": "fe09831e-bbf7-46f1-92e4-aafe10df56fd",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "name": "Shared-Test-User-Population",
    "description": "Population for PingOne test users",
    "userCount": 0,
    "createdAt": "2026-03-23T16:34:44.760Z",
    "updatedAt": "2026-03-23T16:34:44.760Z",
    "preferredLanguage": "en",
    "theme": {
        "id": "5ab94557-59c3-4afc-bbf6-046444bd04b8"
    },
    "default": false
}
```

---

---
title: "Step 4: Send an authorization request"
description: Use the GET {{authPath}}/{{envID}}/as/authorize operation to send an authorization request to the PingOne authorization server. This step queries the authorization server, and returns the flow ID as the id property in the response. You'll use this flow ID in Step 5 to start the sign-on flow and submit your test user's credentials.
component: pingone-api
page_id: pingone-api:getting-started:simple-sso-workflow/step-4-send-an-authorization-request
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/simple-sso-workflow/step-4-send-an-authorization-request.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  example-request: Example Request
  example-response: Example Response
---

# Step 4: Send an authorization request

##

```none
GET {{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow
```

Use the `GET {{authPath}}/{{envID}}/as/authorize` operation to send an authorization request to the PingOne authorization server. This step queries the authorization server, and returns the flow ID as the `id` property in the response. You'll use this flow ID in Step 5 to start the sign-on flow and submit your test user's credentials.

In this request:

* `{{authPath}}` is the geographic domain to use for authentication and authorization for your PingOne environment. The PingOne top-level domain is `https://auth.pingone.com/` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html#pingone-api-domains) for the top-level domains for other regions.

* `{{envID}}` is the environment ID for the environment you created in the prior workflow to create your test environment.

These request query parameters are required:

* `response_type` needs a value of `code` to correspond to the `responseTypes` value you set when creating the Web application in a prior step.

* `client_id` is the application ID returned when you created the Web application in a prior step. This is represented by the value of the `{{solutionAppID}}` Postman variable written automatically to your Postman environment.

* `redirect_uri` is one of the redirect URIs that you set when you created the Web application in a prior step.

* `response_mode` when set to `pi.flow`, it directs the authorization server to return a JSON response instead of a redirect.

* `scope` needs to be the OpenID Connect (OIDC) `openid` user claim that will be included in the token.

When successful, the request returns JSON that includes a flow ID and a `status` property to specify the next action in the sign-on flow. In this case, the flow status returns `USERNAME_PASSWORD_REQUIRED`.

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've set the variables used in the request body correctly.

* Verify that `{{authPath}}` is correct for your geographic domain .

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
curl --location --globoff '{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid&response_mode=pi.flow'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow")
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

  url := "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid&response_mode=pi.flow"
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
GET /{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow HTTP/1.1
Host: {{authPath}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow")
  .method("GET", body)
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow",
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
  'url': '{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow',
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

url = "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow');
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

url = URI("{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http://localhost:3000/callback&scope=openid&response_mode=pi.flow")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/authorize?response_type=code&client_id={{sharedWebAppID}}&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid&response_mode=pi.flow")!,timeoutInterval: Double.infinity)
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
        "usernamePassword.check": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03c69293-8ec6-4f4a-a60f-535eae4b7520"
        },
        "password.forgot": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03c69293-8ec6-4f4a-a60f-535eae4b7520"
        },
        "self": {
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03c69293-8ec6-4f4a-a60f-535eae4b7520"
        },
        "signOnPage": {
            "href": "https://apps.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/signon/?flowId=03c69293-8ec6-4f4a-a60f-535eae4b7520"
        }
    },
    "_embedded": {
        "application": {
            "name": "SolutionApp_1768234372"
        }
    },
    "id": "03c69293-8ec6-4f4a-a60f-535eae4b7520",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=03c69293-8ec6-4f4a-a60f-535eae4b7520",
    "status": "USERNAME_PASSWORD_REQUIRED",
    "createdAt": "2026-01-16T17:38:05.995Z",
    "expiresAt": "2026-01-16T17:53:05.996Z"
}
```

---

---
title: "Step 5: Create a user"
description: Use the POST {{apiPath}}/v1/environments/{{envID}}/users request to create a new user.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-5-create-a-user
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-5-create-a-user.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 5: Create a user

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users
```

Use the `POST {{apiPath}}/v1/environments/{{envID}}/users` request to create a new user.

In this request:

* ``{{apiPath}}`is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1`` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

* `{{envID}}` is the ID of the environment you created in the previous step. If you're using Postman, this value is automatically set by the script in the Script tab used for the previous step.

In the request body:

* `email` is a String containing the unique email address for the new user.

* `{{sharedPopID}}` is a String containing the ID for the population you created in the previous step. If you're using Postman, you'll find that the `{{sharedPopID}}` variable has already been set by the Script in the prior call (to create a population).

* `username` is a String containing the name for the new user. This must be a unique name within your environment.

A successful response returns a `Status: 201 created` message, and shows the new user's coniguration data.

The configuration data includes the user's `id` property. If you're using Postman, the script in the Script tab automatically sets `{{sharedUserID}}` to this value. The `{{sharedUserID}}` property is needed to set user password in the next step.

In the next step, you'll find the admin roles needed to make your new user an admin with the same permissions as the Worker app you created.

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've assigned either the Environment Admin or Identity Admin role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* Verify that the `{{sharedPopID}}` value is the population ID value returned by the previous step to create a population. For Postman users, unassigned variables are shown in red, and assigned variables in blue.

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests). For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red).

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain .

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "email": "{{email}}",
    "population": {
        "id": "{{sharedPopID}}"
    },
    "username": "sharedTestUser"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "email": "{{email}}",
    "population": {
        "id": "{{sharedPopID}}"
    },
    "username": "sharedTestUser"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""email"": ""{{email}}""," + "\n" +
@"    ""population"": {" + "\n" +
@"        ""id"": ""{{sharedPopID}}""" + "\n" +
@"    }," + "\n" +
@"    ""username"": ""sharedTestUser""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users"
  method := "POST"

  payload := strings.NewReader(`{
    "email": "{{email}}",
    "population": {
        "id": "{{sharedPopID}}"
    },
    "username": "sharedTestUser"
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
POST /v1/environments/{{envID}}/users HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "email": "{{email}}",
    "population": {
        "id": "{{sharedPopID}}"
    },
    "username": "sharedTestUser"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"email\": \"{{email}}\",\n    \"population\": {\n        \"id\": \"{{sharedPopID}}\"\n    },\n    \"username\": \"sharedTestUser\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "email": "{{email}}",
    "population": {
      "id": "{{sharedPopID}}"
    },
    "username": "sharedTestUser"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "email": "{{email}}",
    "population": {
      "id": "{{sharedPopID}}"
    },
    "username": "sharedTestUser"
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

url = "{{apiPath}}/v1/environments/{{envID}}/users"

payload = json.dumps({
  "email": "{{email}}",
  "population": {
    "id": "{{sharedPopID}}"
  },
  "username": "sharedTestUser"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "email": "{{email}}",\n    "population": {\n        "id": "{{sharedPopID}}"\n    },\n    "username": "sharedTestUser"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "email": "{{email}}",
  "population": {
    "id": "{{sharedPopID}}"
  },
  "username": "sharedTestUser"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"email\": \"{{email}}\",\n    \"population\": {\n        \"id\": \"{{sharedPopID}}\"\n    },\n    \"username\": \"sharedTestUser\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "population": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/populations/fe09831e-bbf7-46f1-92e4-aafe10df56fd"
        },
        "devices": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/devices"
        },
        "roleAssignments": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/roleAssignments"
        },
        "password": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "password.reset": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "password.set": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "password.check": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "password.recover": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "linkedAccounts": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/linkedAccounts"
        },
        "account.sendVerificationCode": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c"
        },
        "memberOfGroups": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/memberOfGroups"
        }
    },
    "id": "b7119e13-9612-42d0-a57c-039e74a0f27c",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "account": {
        "canAuthenticate": true,
        "status": "OK"
    },
    "createdAt": "2026-03-23T16:37:59.659Z",
    "email": "sharedTestUser@example.com",
    "enabled": true,
    "identityProvider": {
        "type": "PING_ONE"
    },
    "lifecycle": {
        "status": "ACCOUNT_OK"
    },
    "mfaEnabled": false,
    "population": {
        "id": "fe09831e-bbf7-46f1-92e4-aafe10df56fd"
    },
    "updatedAt": "2026-03-23T16:37:59.659Z",
    "username": "sharedTestUser",
    "verifyStatus": "NOT_INITIATED"
}
```

---

---
title: "Step 5: Submit login credentials"
description: Use POST {{authPath}}/{{envID}}/flows/{{flowID}} to respond to the USERNAME_PASSWORD_REQUIRED flow state set by the previous call to get the flow. This requires that the user initiates the usernamePassword.check action.
component: pingone-api
page_id: pingone-api:getting-started:simple-sso-workflow/step-5-submit-login-credentials
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/simple-sso-workflow/step-5-submit-login-credentials.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 5: Submit login credentials

##

```none
POST {{authPath}}/{{envID}}/flows/{{flowID}}
```

Use `POST {{authPath}}/{{envID}}/flows/{{flowID}}` to respond to the `USERNAME_PASSWORD_REQUIRED` flow state set by the previous call to get the flow. This requires that the user initiates the `usernamePassword.check` action.

You need to set the `application/vnd.pingidentity.usernamePassword.check+json` custom media type in the `Content-type` HTTP request header to identify the action.

In this request:

* `{{authPath}}` is the geographic domain to use for authentication and authorization for your PingOne environment. The PingOne top-level domain is `https://auth.pingone.com/` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html#pingone-api-domains) for the top-level domains for other regions.

* `{{envID}}` is the environment ID for the environment you created in the prior workflow to create your test environment.

* `{{flowID}}` is the flow ID value returned by the authorization request as the `id` property in the response JSON.

In the request body:

* `username` is a String containing the `username` value you assigned when you created the user in Task 2 [Step 5: Create a user](../create-a-test-environment/step-5-create-a-user.html).

* `password` is a String containing the user's password you set in Task 2 [Step 6: Set the user password](../create-a-test-environment/step-6-set-user-password.html).

If the `usernamePassword.check` action completes successfully, the authentication flow completes, and the flow returns to the authorization server in the next step.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This endpoint generates a session token cookie that is returned as a header in the response. You will need this ST ID to run the `/resume` and `/token` endpoints in Steps 6 and 7. The session token header looks like this:`set-cookie: ST=3e0967f4-aba0-479c-86cf-fb5fe5b804d6; Path=/082dba86-d36e-413e-85b4-ee499a5cea55; Max-Age=2592000; Expires=Thu, 19 Feb 2026 19:29:00 GMT; Secure; HttpOnly; SameSite=None` |

### Troubleshooting

* Verify that the `application/vnd.pingidentity.usernamePassword.check+json` custom media type in the `Content-type` HTTP request header is correct.

* Verify that you're submitting the correct username and password for your test user. If you're using the Postman collection, these values are set for you automatically in this request.

* Verify that `{{authPath}}` is correct for your geographic domain .

### Headers

Content-Type      application/vnd.pingidentity.usernamePassword.check+json

### Body

raw ( application/vnd.pingidentity.usernamePassword.check+json )

```json
{
    "username": "{{sharedUsername}}",
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
    "username": "{{sharedUsername}}",
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
@"    ""username"": ""{{sharedUsername}}""," + "\n" +
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
    "username": "{{sharedUsername}}",
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
    "username": "{{sharedUsername}}",
    "password": "{{userPassword}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.usernamePassword.check+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"username\": \"{{sharedUsername}}\",\n    \"password\": \"{{userPassword}}\"\n}");
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
    "username": "{{sharedUsername}}",
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
    "username": "{{sharedUsername}}",
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
  "username": "{{sharedUsername}}",
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
$request->setBody('{\n    "username": "{{sharedUsername}}",\n    "password": "{{userPassword}}"\n}');
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
  "username": "{{sharedUsername}}",
  "password": "{{userPassword}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"username\": \"{{sharedUsername}}\",\n    \"password\": \"{{userPassword}}\"\n}"
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
            "href": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03ae576a-2832-477f-8a72-856afd5df7d7"
        }
    },
    "id": "03ae576a-2832-477f-8a72-856afd5df7d7",
    "session": {
        "id": "f351ad5e-9fb1-4574-908d-335d933c48f3"
    },
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=03ae576a-2832-477f-8a72-856afd5df7d7",
    "status": "COMPLETED",
    "createdAt": "2026-03-16T19:14:03.375Z",
    "expiresAt": "2026-03-16T19:32:53.935Z",
    "_embedded": {
        "user": {
            "id": "af7bb93b-fc2c-4346-afc1-9d31873ac47e",
            "username": "sharedTestUser"
        },
        "application": {
            "name": "Shared-Web-App"
        }
    }
}
```

---

---
title: "Step 6: Call the resume endpoint"
description: Use the GET {{authPath}}/{{envID}}/as/resume?flowId={{flowID}} request to obtain the authorization code required to exchange for an access token.
component: pingone-api
page_id: pingone-api:getting-started:simple-sso-workflow/step-6-call-the-resume-endpoint
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/simple-sso-workflow/step-6-call-the-resume-endpoint.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Step 6: Call the resume endpoint

##

```none
GET {{authPath}}/{{envID}}/as/resume?flowId={{flowID}}
```

Use the `GET {{authPath}}/{{envID}}/as/resume?flowId={{flowID}}` request to obtain the authorization code required to exchange for an access token.

In this request:

* `{{authPath}}` is the geographic domain to use for authentication and authorization for your PingOne environment. The PingOne top-level domain is `https://auth.pingone.com/` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html#pingone-api-domains) for the top-level domains for other regions.

* `{{envID}}` is the environment ID for the environment you created in the prior workflow to create your test environment.

* `{{flowID}}` is a String containing the flow ID value returned by the authorization request.

In the request headers:

* `Cookie` header must be set to the ST ID value returned in Step 5 (for example, `ST=3e0967f4-aba0-479c-86cf-fb5fe5b804d6`).

The response returns JSON that includes the authorization code.

### Troubleshooting

* Verify that the `flowID` value is correct.

* Verify that `{{authPath}}` is correct for your geographic domain .

* Make sure you set the value for the ST cookie. This is the session token that links the authenticated user to this sign-on session. The ST value is returned in the response as a header after successfully providing the username and password in Step 5.

### Headers

Cookie      ST={{set-cookieID}}

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
curl --location --globoff '{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}' \
--header 'Cookie: ST={{set-cookieID}}'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Get);
request.AddHeader("Cookie", "ST={{set-cookieID}}");
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

  url := "{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "ST={{set-cookieID}}")

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
GET /{{envID}}/as/resume?flowId={{flowID}} HTTP/1.1
Host: {{authPath}}
Cookie: ST={{set-cookieID}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}")
  .method("GET", body)
  .addHeader("Cookie", "ST={{set-cookieID}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Cookie": "ST={{set-cookieID}}"
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
  'url': '{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}',
  'headers': {
    'Cookie': 'ST={{set-cookieID}}'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

```python
import requests

url = "{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}"

payload = {}
headers = {
  'Cookie': 'ST={{set-cookieID}}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}');
$request->setMethod(HTTP_Request2::METHOD_GET);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => 'ST={{set-cookieID}}'
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

url = URI("{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Cookie"] = "ST={{set-cookieID}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/resume?flowId={{flowID}}")!,timeoutInterval: Double.infinity)
request.addValue("ST={{set-cookieID}}", forHTTPHeaderField: "Cookie")

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
            "href": "http://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/flows/03ae576a-2832-477f-8a72-856afd5df7d7"
        },
        "signOnPage": {
            "href": "https://apps.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/signon/?flowId=03ae576a-2832-477f-8a72-856afd5df7d7"
        }
    },
    "_embedded": {
        "user": {
            "id": "af7bb93b-fc2c-4346-afc1-9d31873ac47e",
            "username": "sharedTestUser"
        },
        "application": {
            "name": "Shared-Web-App"
        }
    },
    "id": "03ae576a-2832-477f-8a72-856afd5df7d7",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "session": {
        "id": "f351ad5e-9fb1-4574-908d-335d933c48f3"
    },
    "resumeUrl": "https://auth.pingone.com/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/as/resume?flowId=03ae576a-2832-477f-8a72-856afd5df7d7",
    "status": "COMPLETED",
    "createdAt": "2026-03-16T19:14:03.375Z",
    "expiresAt": "2026-03-16T19:33:26.348Z",
    "authorizeResponse": {
        "code": "031f9202-6ac3-4864-b219-803c3c1694ca"
    }
}
```

---

---
title: "Step 6: Set the user password"
description: Use the PUT {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password request to assign an initial password for the new user. The request requires the application/vnd.pingidentity.password.set+json custom content type in the Content-Type HTTP header to initate the set password action. If you're using Postman, we use a pre-request script to set the user password.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-6-set-user-password
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-6-set-user-password.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 6: Set the user password

##

```none
PUT {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password
```

Use the `PUT {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password` request to assign an initial password for the new user. The request requires the `application/vnd.pingidentity.password.set+json` custom content type in the `Content-Type` HTTP header to initate the set password action. If you're using Postman, we use a pre-request script to set the user password.

This request is an admin-level assignment of a user's initial password.

In this request:

* `{{apiPath}}` is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

* `{{envID}}` is the ID of the environment you created in the previous step. If you're using Postman, this value is automatically set by the script in the Script tab used for the previous step.

* `{{sharedUserID}}` is the ID for the user you created in the previous step. If you're using Postman, this has been automatically set for you by the script in the Script tab when you created the new user.

In the request body:

* `{{userPassword}}` is a String containing the new user password to assign. If you're using Postman, this has been automatically set for you by our pre-request script.

* `forceChange` indicates whether a user-level password change is required after a user's initial sign on. Because this is an admin-level password assignment, the `forceChange` property in the request body is set to `false`. If you like, you can set this to `true` to see the result when you first sign on as this user.

A successful response returns a `Status: 200 successful` message, and shows the user's password `status` of `OK`.

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've assigned either the Environment Admin or Identity Admin role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* Verify that the `{{sharedUserID}}` value is the user ID value returned by the previous step to create a user. For Postman users, unassigned variables are shown in red, and assigned variables in blue.

* Verify that the `{{userPassword}}` value in the request body is set to a valid password. For Postman users, unassigned variables are shown in red, and assigned variables in blue.

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests). For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red).

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain .

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/vnd.pingidentity.password.set+json

### Body

raw ( application/vnd.pingidentity.password.set+json )

```json
{
    "value": "{{userPassword}}",
    "forceChange": false
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
curl --location --globoff --request PUT '{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password' \
--header 'Content-Type: application/vnd.pingidentity.password.set+json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "value": "{{userPassword}}",
    "forceChange": false
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Put);
request.AddHeader("Content-Type", "application/vnd.pingidentity.password.set+json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""value"": ""{{userPassword}}""," + "\n" +
@"    ""forceChange"": false" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password"
  method := "PUT"

  payload := strings.NewReader(`{
    "value": "{{userPassword}}",
    "forceChange": false
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/vnd.pingidentity.password.set+json")
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
PUT /v1/environments/{{envID}}/users/{{sharedUserID}}/password HTTP/1.1
Host: {{apiPath}}
Content-Type: application/vnd.pingidentity.password.set+json
Authorization: Bearer {{accessToken}}

{
    "value": "{{userPassword}}",
    "forceChange": false
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/vnd.pingidentity.password.set+json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"value\": \"{{userPassword}}\",\n    \"forceChange\": false\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password")
  .method("PUT", body)
  .addHeader("Content-Type", "application/vnd.pingidentity.password.set+json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password",
  "method": "PUT",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/vnd.pingidentity.password.set+json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "value": "{{userPassword}}",
    "forceChange": false
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password',
  'headers': {
    'Content-Type': 'application/vnd.pingidentity.password.set+json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "value": "{{userPassword}}",
    "forceChange": false
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password"

payload = json.dumps({
  "value": "{{userPassword}}",
  "forceChange": False
})
headers = {
  'Content-Type': 'application/vnd.pingidentity.password.set+json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password');
$request->setMethod(HTTP_Request2::METHOD_PUT);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/vnd.pingidentity.password.set+json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "value": "{{userPassword}}",\n    "forceChange": false\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Put.new(url)
request["Content-Type"] = "application/vnd.pingidentity.password.set+json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "value": "{{userPassword}}",
  "forceChange": false
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"value\": \"{{userPassword}}\",\n    \"forceChange\": false\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/password")!,timeoutInterval: Double.infinity)
request.addValue("application/vnd.pingidentity.password.set+json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "PUT"
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c"
        },
        "passwordPolicy": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/passwordPolicies/a6f57fd8-0597-448c-8993-8bec226c38ef"
        },
        "password.check": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "password.reset": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "password.set": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        },
        "password.recover": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/password"
        }
    },
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "b7119e13-9612-42d0-a57c-039e74a0f27c"
    },
    "passwordPolicy": {
        "id": "a6f57fd8-0597-448c-8993-8bec226c38ef"
    },
    "status": "OK",
    "lastChangedAt": "2026-03-23T16:40:01.366Z"
}
```

---

---
title: "Step 7: Enable user MFA"
description: The POST {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled operation enables MFA for the specified user.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-7-enable-user-mfa
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-7-enable-user-mfa.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 7: Enable user MFA

##

```none
PUT {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled
```

The `POST {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled` operation enables MFA for the specified user.

In this request:

* `{{apiPath}}` is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

* `{{envID}}` is the ID of the environment you created in the previous step. If you're using Postman, this value is automatically set by the script in the Script tab used for the previous step.

* `{{sharedUserID}}` is the ID for the user you created in the step to create a user. If you're using Postman, this has been automatically set for you by the script in the Script tab when you created the new user.

In the request body:

* `mfaEnabled` indicates whether to enable MFA for the user. This must be set to `true` to allow the user to authenticate using MFA. The default value is `false`.

A successful response returns a `Status: 200 successful` message, and shows the user's password `status` of `OK`.

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've assigned either the Environment Admin or Identity Admin role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* Verify that the `{{sharedUserID}}` value is the user ID value returned by the step to create a user. For Postman users, unassigned variables are shown in red, and assigned variables in blue.

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests). For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red).

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain .

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "mfaEnabled": true
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
curl --location --globoff --request PUT '{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "mfaEnabled": true
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Put);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""mfaEnabled"": true" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled"
  method := "PUT"

  payload := strings.NewReader(`{
    "mfaEnabled": true
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
PUT /v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "mfaEnabled": true
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"mfaEnabled\": true\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled",
  "method": "PUT",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "mfaEnabled": true
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "mfaEnabled": true
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled"

payload = json.dumps({
  "mfaEnabled": True
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {{accessToken}}'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled');
$request->setMethod(HTTP_Request2::METHOD_PUT);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "mfaEnabled": true\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Put.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "mfaEnabled": true
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"mfaEnabled\": true\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/mfaEnabled")!,timeoutInterval: Double.infinity)
request.addValue("application/json", forHTTPHeaderField: "Content-Type")
request.addValue("Bearer {{accessToken}}", forHTTPHeaderField: "Authorization")

request.httpMethod = "PUT"
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/mfaEnabled"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c"
        }
    },
    "mfaEnabled": true
}
```

---

---
title: "Step 7: Get the access token"
description: Use the POST {{authPath}}/{{envID}}/as/token request to acquire the access token by presenting the client's (the Web application's) authorization grant.
component: pingone-api
page_id: pingone-api:getting-started:simple-sso-workflow/step-7-get-the-access-token
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/simple-sso-workflow/step-7-get-the-access-token.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 7: Get the access token

##

```none
POST {{authPath}}/{{envID}}/as/token
```

Use the `POST {{authPath}}/{{envID}}/as/token` request to acquire the access token by presenting the client's (the Web application's) authorization grant.

|   |                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This request requires Basic authentication, in which the application ID from Step 2 and the application secret from Step 3 are used to authenticate this request. If you're using Postman, these values are already set for you. In a curl command, you can use the `--user` parameter to satisfy the Basic authentication requirement like this: `--user "{{appID}}:{{appSecret}}"`. |

In this request:

* `{{authPath}}` is the geographic domain to use for authentication and authorization for your PingOne environment. The PingOne top-level domain is `https://auth.pingone.com/` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html#pingone-api-domains) for the top-level domains for other regions.

* `{{envID}}` is the environment ID for the environment you created in the prior workflow to create your test environment.

In the request body:

* `grant_type` is a String containing the grant type of the token request. In this example, the value is `authorization_code`.

* `code` is a String containing the authorization code value returned by the `/as/resume` request in Step 6.

* `redirect_uri` is a String containing the URL for the return entry point of the Web application.

In the request headers:

* `Cookie` header must be set to the ST ID value returned in Step 5 (for example, `ST=3e0967f4-aba0-479c-86cf-fb5fe5b804d6`).

A successful response contains the access token and the ID token. In receiving these tokens from PingOne, the user you created has completed the sign-on flow to access their account on the Web application you configured in Step 2.

### Troubleshooting

* Verify that the authorization code returned by the resume endpoint is set as the value for the `code` property in the request body.

* Verify that the value of `redirect_uri` here matches the `redirect_uri` value that you set when you created the Web application in [Step 2: Create a Web application](step-2-create-a-web-application.html).

* Verify that `{{authPath}}` is correct for your geographic domain .

* Make sure you set the value for the ST cookie. This is the session token that links the authenticated user to this sign-on session. The ST value is returned in the response as a header after successfully providing the username and password in Step 5.

### Headers

Authorization

Content-Type      application/x-www-form-urlencoded

Cookie      ST={{set-cookieID}}

### Body

urlencoded ( application/x-www-form-urlencoded )

| Key           | Value                            |
| ------------- | -------------------------------- |
| grant\_type   | authorization\_code              |
| code          | {{authCode}}                     |
| redirect\_uri | <http://localhost:3000/callback> |
| scope         | openid                           |

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
curl --location --globoff '{{authPath}}/{{envID}}/as/token' \
--header 'Cookie: ST={{set-cookieID}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Authorization: Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0=' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code={{authCode}}' \
--data-urlencode 'redirect_uri=http://localhost:3000/callback' \
--data-urlencode 'scope=openid'
```

```csharp
var options = new RestClientOptions("{{authPath}}/{{envID}}/as/token")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Cookie", "ST={{set-cookieID}}");
request.AddHeader("Content-Type", "application/x-www-form-urlencoded");
request.AddHeader("Authorization", "Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0=");
request.AddParameter("grant_type", "authorization_code");
request.AddParameter("code", "{{authCode}}");
request.AddParameter("redirect_uri", "http://localhost:3000/callback");
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

  url := "{{authPath}}/{{envID}}/as/token"
  method := "POST"

  payload := strings.NewReader("grant_type=authorization_code&code=%7B%7BauthCode%7D%7D&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid")

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Cookie", "ST={{set-cookieID}}")
  req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
  req.Header.Add("Authorization", "Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0=")

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
POST /{{envID}}/as/token HTTP/1.1
Host: {{authPath}}
Cookie: ST={{set-cookieID}}
Content-Type: application/x-www-form-urlencoded
Authorization: Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0=

grant_type=authorization_code&code=%7B%7BauthCode%7D%7D&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "grant_type=authorization_code&code={{authCode}}&redirect_uri=http://localhost:3000/callback&scope=openid");
Request request = new Request.Builder()
  .url("{{authPath}}/{{envID}}/as/token")
  .method("POST", body)
  .addHeader("Cookie", "ST={{set-cookieID}}")
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .addHeader("Authorization", "Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0=")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{authPath}}/{{envID}}/as/token",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Cookie": "ST={{set-cookieID}}",
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": "Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0="
  },
  "data": {
    "grant_type": "authorization_code",
    "code": "{{authCode}}",
    "redirect_uri": "http://localhost:3000/callback",
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
  'url': '{{authPath}}/{{envID}}/as/token',
  'headers': {
    'Cookie': 'ST={{set-cookieID}}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0='
  },
  form: {
    'grant_type': 'authorization_code',
    'code': '{{authCode}}',
    'redirect_uri': 'http://localhost:3000/callback',
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

url = "{{authPath}}/{{envID}}/as/token"

payload = 'grant_type=authorization_code&code=%7B%7BauthCode%7D%7D&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid'
headers = {
  'Cookie': 'ST={{set-cookieID}}',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

```php
<?php
require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('{{authPath}}/{{envID}}/as/token');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Cookie' => 'ST={{set-cookieID}}',
  'Content-Type' => 'application/x-www-form-urlencoded',
  'Authorization' => 'Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0='
));
$request->addPostParameter(array(
  'grant_type' => 'authorization_code',
  'code' => '{{authCode}}',
  'redirect_uri' => 'http://localhost:3000/callback',
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

url = URI("{{authPath}}/{{envID}}/as/token")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Cookie"] = "ST={{set-cookieID}}"
request["Content-Type"] = "application/x-www-form-urlencoded"
request["Authorization"] = "Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0="
request.body = "grant_type=authorization_code&code=%7B%7BauthCode%7D%7D&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid"

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "grant_type=authorization_code&code=%7B%7BauthCode%7D%7D&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2Fcallback&scope=openid"
let postData =  parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{authPath}}/{{envID}}/as/token")!,timeoutInterval: Double.infinity)
request.addValue("ST={{set-cookieID}}", forHTTPHeaderField: "Cookie")
request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
request.addValue("Basic e3tzaGFyZWRXZWJBcHBJRH19Ont7c2hhcmVkV2ViQXBwU2VjcmV0fX0=", forHTTPHeaderField: "Authorization")

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
    "access_token": "eyJhbGciOiJSUz...",
    "token_type": "Bearer",
    "expires_in": 3600,
    "scope": "openid",
    "id_token": "eyJhbGciOiJSUz..."
}
```

---

---
title: "Step 8: Set user device (Email)"
description: The POST {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices operation creates an MFA device (method) for an email address and associates this with the specified user. The user can then receive an email notification for MFA authentication.
component: pingone-api
page_id: pingone-api:getting-started:create-a-test-environment/step-8-set-user-device-email
canonical_url: https://developer.pingidentity.com/pingone-api/getting-started/create-a-test-environment/step-8-set-user-device-email.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  troubleshooting: Troubleshooting
  headers: Headers
  body: Body
  example-request: Example Request
  example-response: Example Response
---

# Step 8: Set user device (Email)

##

```none
POST {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices
```

The `POST {{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices` operation creates an MFA device (method) for an email address and associates this with the specified user. The user can then receive an email notification for MFA authentication.

In this request:

* `{{apiPath}}` is the geographic domain for the PingOne API endpoints for your PingOne environment. The PingOne top-level domain is `https://api.pingone.com/v1` for the U.S. Refer to [PingOne API domains](../../before-you-begin/introduction.html) for the top-level domains for other regions.

* `{{envID}}` is the ID of the environment you created in the previous step. If you're using Postman, this value is automatically set by the script in the Script tab used for the previous step.

* `{{sharedUserID}}` is the ID for the user you created in the step to create a user. If you're using Postman, this has been automatically set for you by the script in the Script tab when you created the new user.

In the request body:

* `type` is the type of device communication to use. In this case, the value must be "EMAIL".

* `email` is a valid email address for the user.

A successful response returns a `Status: 200 successful` message, and shows the user's password `status` of `OK`.

You're now ready to create an SSO workflow for this test environment using the PingOne APIs. Refer to [Create an SSO Workflow](../simple-sso-workflow.html).

### Troubleshooting

* Verify that `{{envID}}` is the ID for the new test environment you created.

* Verify that you've assigned either the Environment Admin or Identity Admin role to your Worker app. Refer to [Assign roles to the Worker app](../create-an-admin-worker-app/step-3-assign-roles.html).

* Verify that the `{{sharedUserID}}` value is the user ID value returned by the step to create a user. For Postman users, unassigned variables are shown in red, and assigned variables in blue.

* Verify that you're using Bearer authorization for this request (and all `{{apiPath}}` requests). For Postman users, check that the Authorization tab in Postman is set to Bearer Token, and the access token variable is assigned (shown in blue, not red).

* If you get a 401 Unauthorized message, this is likely due to the access token expiring (a 1 hour expiry time). Refer to the step to get an access token, and call this request again.

* Verify that `{{apiPath}}` is correct for your geographic domain .

### Headers

Authorization      Bearer {{accessToken}}

Content-Type      application/json

### Body

raw ( application/json )

```json
{
    "type": "EMAIL",
    "email": "{{email}}"
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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "type": "EMAIL",
    "email": "{{email}}"
}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("", Method.Post);
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Authorization", "Bearer {{accessToken}}");
var body = @"{" + "\n" +
@"    ""type"": ""EMAIL""," + "\n" +
@"    ""email"": ""{{email}}""" + "\n" +
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices"
  method := "POST"

  payload := strings.NewReader(`{
    "type": "EMAIL",
    "email": "{{email}}"
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
POST /v1/environments/{{envID}}/users/{{sharedUserID}}/devices HTTP/1.1
Host: {{apiPath}}
Content-Type: application/json
Authorization: Bearer {{accessToken}}

{
    "type": "EMAIL",
    "email": "{{email}}"
}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n    \"type\": \"EMAIL\",\n    \"email\": \"{{email}}\"\n}");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer {{accessToken}}"
  },
  "data": JSON.stringify({
    "type": "EMAIL",
    "email": "{{email}}"
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices',
  'headers': {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {{accessToken}}'
  },
  body: JSON.stringify({
    "type": "EMAIL",
    "email": "{{email}}"
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices"

payload = json.dumps({
  "type": "EMAIL",
  "email": "{{email}}"
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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setHeader(array(
  'Content-Type' => 'application/json',
  'Authorization' => 'Bearer {{accessToken}}'
));
$request->setBody('{\n    "type": "EMAIL",\n    "email": "{{email}}"\n}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Post.new(url)
request["Content-Type"] = "application/json"
request["Authorization"] = "Bearer {{accessToken}}"
request.body = JSON.dump({
  "type": "EMAIL",
  "email": "{{email}}"
})

response = http.request(request)
puts response.read_body
```

```swift
let parameters = "{\n    \"type\": \"EMAIL\",\n    \"email\": \"{{email}}\"\n}"
let postData = parameters.data(using: .utf8)

var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{sharedUserID}}/devices")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c/devices/3e3139bb-5eed-41b3-acff-c544dae4c57e"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/b7119e13-9612-42d0-a57c-039e74a0f27c"
        }
    },
    "id": "3e3139bb-5eed-41b3-acff-c544dae4c57e",
    "environment": {
        "id": "abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
    },
    "user": {
        "id": "b7119e13-9612-42d0-a57c-039e74a0f27c"
    },
    "type": "EMAIL",
    "status": "ACTIVE",
    "createdAt": "2026-03-30T18:29:31.559Z",
    "updatedAt": "2026-03-30T18:29:31.559Z",
    "email": "mobetta@example.com"
}
```
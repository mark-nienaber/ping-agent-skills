---
title: Document Authentication Using NFC Chip Verification
description: Describes the early access NFC-based document authentication for mobile PingOne Verify and how to enable it for preview in an environment
component: pingone-api-ea
page_id: pingone-api-ea:verify:early-access/document-authentication-using-nfc-chip-verification/index
canonical_url: https://developer.pingidentity.com/pingone-api-ea/verify/early-access/document-authentication-using-nfc-chip-verification/index.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16
---

# Document Authentication Using NFC Chip Verification

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This information is provided as part of the early-access program. API details described here might change before the official release of the feature. |

This feature adds NFC chip verification to native mobile PingOne Verify journeys to provide customers, especially those in highly-regulated industries, customer identity access management and workforce identity proofing with the higher-assurance document authentication anchored on embedded, cryptographically-signed chip data read by NFC.

This section provides Verify services where the extensions for NFC-based document authentication are described. For full details on standard document verification, refer to [PingOne Verify](https://developer.pingidentity.com/pingone-api/verify/index.html).

[Run in Postman](https://god.gw.postman.com/run-collection/18568624-51e4189e-4985-446b-9e3d-68381c5a5129?action=collection%2Ffork\&source=rip_markdown\&collection-url=entityId%3D18568624-51e4189e-4985-446b-9e3d-68381c5a5129%26entityType%3Dcollection%26workspaceId%3D936f1637-06aa-461a-b23d-0964e90621c6)

---

---
title: Early Access
description: Explains support terms for PingOne early access features and how to enable them for preview in a specified environment
component: pingone-api-ea
page_id: pingone-api-ea:verify:early-access/index
canonical_url: https://developer.pingidentity.com/pingone-api-ea/verify/early-access/index.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16
---

# Early Access

These early access features are available for preview purposes only, and are not covered under standard Support SLAs. You can open support cases for feedback, bug reports, configuration questions, or other inquiries related to early access features, but resolution times for these cases will vary. These cases often require collaboration with our Engineering and Product teams, so timelines might exceed the usual SLAs for your Support package.

We encourage you to use any of the early access features you find applicable. You'll need to enable each feature you'd like to use. Refer to [Early Access Features](https://developer.pingidentity.com/pingone-api/platform/environments/early-access-features/index.html) for instructions.

---

---
title: PingOne Verify - Early Access
description: Introduces the PingOne Verify early access APIs, which you enable per environment to preview upcoming authentication features before general availability
component: pingone-api-ea
page_id: pingone-api-ea:verify:index
canonical_url: https://developer.pingidentity.com/pingone-api-ea/verify/index.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16
page_aliases: ["introduction.adoc"]
---

# PingOne Verify - Early Access

The PingOne early access APIs are available to you when you enable the early access features. When enabled, the features apply only to a specified environment. You select the features to enable, and can remove the feature from the specified environment at any time during the early access period.

---

---
title: Read One Verification MetaData
description: "Retrieve one identity verification metadata result for a specified user's verification transaction in PingOne Verify"
component: pingone-api-ea
page_id: pingone-api-ea:verify:early-access/document-authentication-using-nfc-chip-verification/verification-metadata/read-one-verification-metadata
canonical_url: https://developer.pingidentity.com/pingone-api-ea/verify/early-access/document-authentication-using-nfc-chip-verification/verification-metadata/read-one-verification-metadata.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16
section_ids:
  headers: Headers
  example-request: Example Request
  example-response: Example Response
---

# Read One Verification MetaData

##

```none
GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}
```

Get one result of identity data submitted by, and returned from verification for, a specified user with the `GET {{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}` request. The response differs by the `type` and `provider` that returned the result. Refer to [Specific verification metaData data model](index.html#verify-verification-metadata-data-model) for the data model of each response.

The example responses include:

1. Signicat (document authentication) \[EA]

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
curl --location --globoff '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

```csharp
var options = new RestClientOptions("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")
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

  url := "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}"
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
GET /v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}} HTTP/1.1
Host: {{apiPath}}
Authorization: Bearer {{accessToken}}
```

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")
  .method("GET", body)
  .addHeader("Authorization", "Bearer {{accessToken}}")
  .build();
Response response = client.newCall(request).execute();
```

```javascript
var settings = {
  "url": "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}",
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
  'url': '{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}',
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

url = "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}"

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
$request->setUrl('{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}');
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

url = URI("{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")

http = Net::HTTP.new(url.host, url.port);
request = Net::HTTP::Get.new(url)
request["Authorization"] = "Bearer {{accessToken}}"

response = http.request(request)
puts response.read_body
```

```swift
var request = URLRequest(url: URL(string: "{{apiPath}}/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData/{{metaDataID}}")!,timeoutInterval: Double.infinity)
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
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b/metaData/3270bba3-2e3b-41cd-99e3-20ba73418245"
        },
        "environment": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
        },
        "user": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78"
        },
        "verifyTransaction": {
            "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/a27dec16-1e80-4f10-a261-2cac46a12b78/verifyTransactions/0e2ed48f-6c3a-46c4-bcb5-3a6bd791348b"
        }
    },
    "id": "3270bba3-2e3b-41cd-99e3-20ba73418245",
    "provider": "SIGNICAT",
    "type": "DOCUMENT_AUTHENTICATION",
    "status": "SUCCESS",
    "data": {
        "sessionId": "66c4c592-ee41-8064-957c-428f8aa89ba7",
        "success": true,
        "finishingState": "DONE",
        "activeAuthentication": "PRESENT_SUCCEEDED",
        "activeAuthenticationReason": "SIGNATURE_CHECKED",
        "countrySigner": "PRESENT_SUCCEEDED",
        "countrySignerReason": "FOUND_A_CHAIN_SUCCEEDED",
        "documentSigner": "PRESENT_SUCCEEDED",
        "documentSignerReason": "SIGNATURE_CHECKED",
        "extendedChipAuthentication": "PRESENT_SUCCEEDED",
        "extendedChipAuthenticationReason": "SUCCEEDED",
        "hashTable": "PRESENT_SUCCEEDED",
        "hashTableReason": "ALL_HASHES_MATCH"
    }
}
```

---

---
title: Verification MetaData
description: Explains the PingOne Verify verification metaData data model and endpoint for retrieving scores from a verification transaction
component: pingone-api-ea
page_id: pingone-api-ea:verify:early-access/document-authentication-using-nfc-chip-verification/verification-metadata/index
canonical_url: https://developer.pingidentity.com/pingone-api-ea/verify/early-access/document-authentication-using-nfc-chip-verification/verification-metadata/index.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16
section_ids:
  verify-all-verification-metadata-data-model: All verification metaData data model
  verify-specific-verification-metadata-data-model: Specific verification metaData data model
  verify-verification-metadata-data-model: Verification metaData data model
  verify-data-object-data-model: data object data model
  verify-data-object-for-type-document_authentication-and-provider-signicat: data object for DOCUMENT_AUTHENTICATION + SIGNICAT [EA]
  verify-signicat-verification-status-verdict: Verification Status Verdict
  verify-signicat-verification-status-reason-code: Verification Status Reason Code
---

# Verification MetaData

For each verification attempt, you can retrieve all scores in the transaction returned from verification services. The `metaData` endpoint, `/v1/environments/{{envID}}/users/{{userID}}/verifyTransactions/{{transactionID}}/metaData`, receives all requests for scores associated with the verification attempt and returned from verification services.

## All verification metaData data model

When [all metaData](https://developer.pingidentity.com/pingone-api/verify/verification-metadata/read-all-verification-metadata.html) for a verification transaction are requested, the [verification metaData](#verify-verification-metadata-data-model) for each verification type of the most recent retry appears in a `metaData` array in the response. The verification metaData data model for each verification type of earlier retries appear in a `previousAttempts` array in the response.

| Property           | Type      | Required | Mutable   | Description                                                                                                                                             |
| ------------------ | --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_embedded`        | Object    | N/A      | Read-only | Container for returned data.                                                                                                                            |
| `metaData`         | Object\[] | N/A      | Read-only | Array of [verification metaData objects](#verify-verification-metadata-data-model) for each verification type for the most recent verification attempt. |
| `previousAttempts` | Object\[] | N/A      | Read-only | Array of [verification metaData objects](#verify-verification-metadata-data-model) for each verification type for unacceptable verification attempts.   |
| `size`             | Integer   | N/A      | Read-only | The number of objects returned in `metaData`.                                                                                                           |

## Specific verification metaData data model

When [specific metaData](read-one-verification-metadata.html) for a verification type within a verification transaction are requested, the [verification metaData data model](#verify-verification-metadata-data-model) appears as the response, regardless of which retry attempt it is.

### Verification metaData data model

| Property        | Type    | Required | Mutable   | Description                                                                                                                          |
| --------------- | ------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `data`          | Object  | N/A      | Read-only | Data model by provider and type as seen in the *Data model* column of [data object data model](#verify-data-object-data-model).      |
| `id`            | String  | N/A      | Read-only | Identifier (UUID) of the transaction metaData.                                                                                       |
| `provider`      | String  | N/A      | Read-only | The provider of metaData in the object as seen in the *Provider* column of [data object data model](#verify-data-object-data-model). |
| `retry.attempt` | Integer | N/A      | Read-only | Number of the retry attempt when submitting images.                                                                                  |
| `status`        | String  | N/A      | Read-only | Status of the check. Can be `SUCCESS` or `FAIL`.                                                                                     |
| `type`          | String  | N/A      | Read-only | The type of metaData in the object as seen in the *Type* column of [data object data model](#verify-data-object-data-model).         |

### data object data model

The `data` object in verification metaData varies depending on the values of `type` and `provider` as seen in the table.

| Type                    | Provider | Data model                                                                               |
| ----------------------- | -------- | ---------------------------------------------------------------------------------------- |
| DOCUMENT_AUTHENTICATION | SIGNICAT | [data model](#verify-data-object-for-type-document_authentication-and-provider-signicat) |

#### data object for DOCUMENT_AUTHENTICATION + SIGNICAT \[EA]

Signicat provides document authentication using Near Field Communication (NFC), which securely reads the embedded chip in "smart" documents.

| Property                           | Type    | Required | Mutable   | Description                                                                                                                                                     |
| ---------------------------------- | ------- | -------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sessionId`                        | String  | N/A      | Read-only | Provider's session identifier (UUID) for the verification.                                                                                                      |
| `success`                          | Boolean | N/A      | Read-only | Whether or not the verification was successful.                                                                                                                 |
| `finishingState`                   | String  | N/A      | Read-only | Final state of the verification. Can be `NOT_STARTED`, `BUSY`, or `DONE`.                                                                                       |
| `activeAuthentication`             | String  | N/A      | Read-only | Active authentication verdict. Refer to [Verification Status Verdict](#verify-signicat-verification-status-verdict)                                             |
| `activeAuthenticationReason`       | String  | N/A      | Read-only | Reason for the active authentication verdict. Can be null. Refer to [Verification Status Reason Code](#verify-signicat-verification-status-reason-code).        |
| `countrySigner`                    | String  | N/A      | Read-only | Country signer verification verdict. Refer to [Verification Status Verdict](#verify-signicat-verification-status-verdict).                                      |
| `countrySignerReason`              | String  | N/A      | Read-only | Reason for the country signer verification verdict. Can be null. Refer to [Verification Status Reason Code](#verify-signicat-verification-status-reason-code).  |
| `documentSigner`                   | String  | N/A      | Read-only | Document signer verification verdict. Refer to [Verification Status Verdict](#verify-signicat-verification-status-verdict).                                     |
| `documentSignerReason`             | String  | N/A      | Read-only | Reason for the document signer verification verdict. Can be null. Refer to [Verification Status Reason Code](#verify-signicat-verification-status-reason-code). |
| `extendedChipAuthentication`       | String  | N/A      | Read-only | Extended chip authentication verdict. Refer to [Verification Status Verdict](#verify-signicat-verification-status-verdict).                                     |
| `extendedChipAuthenticationReason` | String  | N/A      | Read-only | Reason for the extended chip authentication verdict. Can be null. Refer to [Verification Status Reason Code](#verify-signicat-verification-status-reason-code). |
| `hashTable`                        | String  | N/A      | Read-only | Hash table verification verdict. Refer to [Verification Status Verdict](#verify-signicat-verification-status-verdict).                                          |
| `hashTableReason`                  | String  | N/A      | Read-only | Reason for the hash table verification verdict. Can be null. Refer to [Verification Status Reason Code](#verify-signicat-verification-status-reason-code).      |

##### Verification Status Verdict

| Verdict             | Description                                                                          |
| ------------------- | ------------------------------------------------------------------------------------ |
| NOT_PRESENT         | Item is not present                                                                  |
| PRESENT_FAILED      | Item is present but failed verification, check the corresponding Reason for details. |
| PRESENT_NOT_CHECKED | Item is present but was not checked for verification.                                |
| PRESENT_SUCCEEDED   | Item is present and successfully verified.                                           |
| UNKNOWN             | Item's verification status is unknown.                                               |

##### Verification Status Reason Code

| Reason Code                          | Description                                                                                                                                                              |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ALL_HASHES_MATCH                     | All hashes (that were computed of data-groups read) match (with hashes stored in the security object document). This is the successful case for hash table verification. |
| CERTIFICATE_EXPIRED                  | Certificate expired.                                                                                                                                                     |
| COULD_NOT_BUILD_CHAIN_FAILURE        | Could not build certificate chain. This is the abnormal failure case for country signer verification.                                                                    |
| FOUND_A_CHAIN_SUCCEEDED              | Found a certificate chain to a trust anchor. This is the successful case for country signer verification.                                                                |
| HASH_MISMATCH_FAILURE                | Hash mismatch failure. This is a failure case for hash table verification.                                                                                               |
| NO_CSCA_TRUST_ANCHORS_FOUND_FAILURE  | No Country Signer Certificate Authority root certificates (trust anchors) were found. This is a failure case for country signer verification.                            |
| NO_VERIFIER                          | The verifier was not configured.                                                                                                                                         |
| NON_MATCH_ALERT                      | Non-matched verification.                                                                                                                                                |
| NOT_SUPPORTED                        | The specific mechanism is not supported by the chip.                                                                                                                     |
| PRESENCE_DETECTED                    | The specific mechanism is present (supported by the chip).                                                                                                               |
| READ_ERROR_CONFIGURATION_FAILURE     | The reader or the verifier could not be configured correctly.                                                                                                            |
| READ_ERROR_SOD_FAILURE               | The verifier could not acquire or parse the chip's security object document.                                                                                             |
| SIGNATURE_CHECKED                    | The signature checked. This is the successful case for active authentication and document signer verification.                                                           |
| SIGNATURE_FAILURE                    | The signature failed. This is a failure case for active authentication and document signer verification.                                                                 |
| STORED_HASH_NOT_FOUND                | The stored hash could not be found. This is a failure case for hash table verification.                                                                                  |
| SUCCEEDED                            | The verification succeeded. This is the general successful case for verification.                                                                                        |
| UNEXPECTED_EXCEPTION_FAILURE         | Reader or verifier encountered an unexpected exception. This is a general failure case for verification.                                                                 |
| UNKNOWN                              | Item's verification status is unknown. No further information could be determined. Default value.                                                                        |
| UNSUPPORTED_DIGEST_ALGORITHM_FAILURE | The verification requires a digest algorithm not supported by the verifier. This is a failure case for hash table verification.                                          |
| UNSUPPORTED_KEY_TYPE_FAILURE         | Unsupported key type failure during verification.                                                                                                                        |
| UNSUPPORTED_DIGEST_SIGNATURE_FAILURE | The verification requires a signature algorithm not supported by the verifier. This is a failure case for active authentication and document signer verification.        |

---

---
title: Verify Policies
description: Explains PingOne Verify policies for configuring identity verification requirements, parameters, and checks in an environment
component: pingone-api-ea
page_id: pingone-api-ea:verify:early-access/document-authentication-using-nfc-chip-verification/verify-policy
canonical_url: https://developer.pingidentity.com/pingone-api-ea/verify/early-access/document-authentication-using-nfc-chip-verification/verify-policy.html
llms_txt: https://developer.pingidentity.com/pingone-api-ea/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-16
section_ids:
  verify-policy-checks: Verify policy checks
  verify-verify-policy-data-model: Verify policy data model
  verify-governmentid-configuration-object: governmentID configuration object
---

# Verify Policies

With verify policies, you can:

* Configure what is required to verify a user.

* Configure parameters for verification, such as the number of one-time password (OTP) attempts and OTP expiration.

You can create as many verify policies as needed to satisfy every verification scenario.

## Verify policy checks

A verify policy defines which identity verification checks are performed for a verification transaction and configures the parameters of each check.

Checks can be either required or optional. All checks are performed for every document type received regardless of whether any check fails. If a type is optional, then the transaction can be processed with or without the documents for that type. If the documents are provided for that type and the optional type verification fails, it will not cause the entire transaction to fail.

## Verify policy data model

| Property                        | Type    | Required | Mutable   | Description                                                                                                                                                                                    |
| ------------------------------- | ------- | -------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `createdAt`                     | String  | N/A      | Read-only | Date and time the verify policy was created                                                                                                                                                    |
| `dataBasedIdentityVerification` | Object  | Optional | Mutable   | [dataBasedIdentityVerification configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-databasedidentityverification-configuration-object) |
| `default`                       | Boolean | Optional | Mutable   | Required as `true` to set this verify policy as the default policy for the environment, otherwise optional and defaults to `false`                                                             |
| `description`                   | String  | Optional | Mutable   | Description displayed in PingOne Admin UI, 1-1024 characters                                                                                                                                   |
| `deviceOwnership`               | Object  | Optional | Mutable   | [deviceOwnership configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-deviceownership-configuration-object)                             |
| `email`                         | Object  | Optional | Mutable   | [email and phone configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-email-and-phone-configuration-object)                             |
| `environment.id`                | String  | Required | Immutable | Ping environment identifier (UUID) for user                                                                                                                                                    |
| `facialComparison`              | Object  | Optional | Mutable   | [facialComparison configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-facialcomparison-configuration-object)                           |
| `geolocation`                   | Object  | Optional | Mutable   | [geolocation configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-geolocation-configuration-object)                                     |
| `governmentId`                  | Object  | Optional | Mutable   | [governmentID configuration object](#verify-governmentid-configuration-object)                                                                                                                 |
| `id`                            | String  | N/A      | Read-only | Policy identifier (UUID)                                                                                                                                                                       |
| `identityRecordMatching`        | Object  | Optional | Mutable   | [identityRecordMatching configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-identityrecordmatching-configuration-object)               |
| `liveness`                      | Object  | Optional | Mutable   | [liveness configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-liveness-configuration-object)                                           |
| `name`                          | String  | Required | Mutable   | Name displayed in PingOne Admin UI                                                                                                                                                             |
| `phone`                         | Object  | Optional | Mutable   | [email and phone configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-email-and-phone-configuration-object)                             |
| `transaction`                   | Object  | Optional | Mutable   | [transaction configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-transaction-configuration-object)                                     |
| `updatedAt`                     | String  | N/A      | Read-only | Date and time the verify policy was updated. Can be null.                                                                                                                                      |
| `verifiableCredential`          | Object  | Optional | Mutable   | [verifiableCredential configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-verifiableCredential-configuration-object)                   |
| `voice` (deprecated)            | Object  | Optional | Mutable   | [voice configuration object](https://developer.pingidentity.com/pingone-api/verify/verify-policy/index.html#verify-voice-configuration-object)                                                 |

### governmentID configuration object

The `GOVERNMENT_ID` configuration object includes `BIOGRAPHIC_MATCHING` in the policy (if biographic data is provided when the client [creates a verify transaction](https://developer.pingidentity.com/pingone-api/verify/verify-transactions/create-verify-transaction.html)), but results are returned separately in [Verification MetaData](https://developer.pingidentity.com/pingone-api/verify/verification-metadata/index.html).

| Property                 | Type    | Required | Mutable | Description                                                                                                                                                           |
| ------------------------ | ------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aadhaar.enabled`        | Boolean | Optional | Mutable | Whether Aadhaar verification is enabled or not                                                                                                                        |
| `documentImages.enabled` | Boolean | Optional | Mutable | Whether document images verification is enabled or not. Defaults to `true`. Refer to comments following this table for more information.                              |
| `failExpiredId`          | Boolean | Optional | Mutable | Whether the Government ID verification fails when the document is expired                                                                                             |
| `inspectionType`         | String  | Optional | Mutable | Determine whether document authentication is automated, manual, or possibly both. Can be `AUTOMATIC`, `MANUAL`, or `STEP_UP`. Refer to notes following this table.    |
| `nfc.enabled` \[EA]      | Boolean | Optional | Mutable | Whether NFC verification is enabled or not                                                                                                                            |
| `provider.auto`          | String  | Optional | Mutable | Provider to use for the automatic verification service. Can be `MITEK` (the default) or `VERIFF`.                                                                     |
| `provider.manual`        | String  | Optional | Mutable | Provider to use for the manual verification service. Can be `MITEK`.                                                                                                  |
| `retry.attempts`         | Integer | Optional | Mutable | Number of retries permitted when submitting images. Must be 0 (no retries permitted) to 3.                                                                            |
| `verify`                 | String  | Required | Mutable | Controls if Government ID verification is `REQUIRED` or `DISABLED`                                                                                                    |
| `verifyAamva`            | Boolean | Optional | Mutable | Whether [AAMVA DLDV](https://developer.pingidentity.com/pingone-api/verify/index.html#us-based-driver-licenses) verification is enabled for supported driver licenses |

When `documentImages.enabled` is set to `false`, document capture is disabled and the user is not prompted to submit images of any document. This is especially useful when you want to verify identification using just Aadhaar information, where document authentication is unnecessary. Defaults to `true` to preserve backwards compatibility with existing verify policies.

Options for `inspectionType` are:

* `AUTOMATIC` invokes automated identification inspection only

* `MANUAL` invokes manual identification inspection only (additional license required)

* `STEP_UP` invokes automated identification inspection and, if that fails, invokes manual identification inspection (additional license required)

If `verify` is set to `DISABLED`, `inspectionType` is optional and ignored if used.

If `inspectionType` is not used, it defaults to the highest option available to the license capabilities in your environment. Similarly, availability of the options depend on the license capabilities of your environment. For example, if your environment is only licensed for automated identification inspection, then `MANUAL` and `STEP_UP` will not be available.

When `nfc.enabled` is set to `true`, the service attempts to perform NFC-based document authentication using the embedded chip data. If `nfc.enabled` is set to `false` (or absent), NFC verification is skipped, and only the other enabled verification methods are used. Enabling NFC verification may require additional permissions or capabilities on the user's device, such as NFC hardware and appropriate operating system support. Ensure that your mobile app gracefully handles cases where NFC is unavailable or disabled on the device.
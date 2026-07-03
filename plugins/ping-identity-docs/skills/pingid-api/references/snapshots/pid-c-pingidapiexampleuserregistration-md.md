---
title: "Example: PingID User Registration"
description: The following example will register a new user at the PingID service and pair their phone to their profile using the online pairing process. At the end of this example a new PingID user will be configured and ready to authenticate using the PingID mobile application.
component: pingid-api
page_id: pingid-api::pid_c_PingIDapiExampleUserRegistration
canonical_url: https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiExampleUserRegistration.html
section_ids:
  overview: Overview
  step-1-create-the-adduser-request: "Step 1 : Create the AddUser Request"
  create-the-api-token-header: Create the API token header
  create-the-api-token-payload: Create the API token payload
  build-and-sign-the-api-request-token: Build and sign the API request token
  step-2-perform-the-adduser-api-call: "Step 2 : Perform the AddUser API call"
  step-3-parse-the-adduser-response: "Step 3 : Parse the AddUser response"
  step-4-initiate-online-pairing: "Step 4 : Initiate Online Pairing"
  poll-the-getpairingstatus-operation: Poll the GetPairingStatus operation
  display-activation-code: Display activation code
---

# Example: PingID User Registration

## Overview

The following example will register a new user at the PingID service and pair their phone to their profile using the online pairing process. At the end of this example a new PingID user will be configured and ready to authenticate using the PingID mobile application.

For this example, we have already created a developer PingOne account, enabled "third-party clients" and downloaded out PingID properties file. The properties file we will use for this example is below:

```properties
#Auto-Generated from PingOne
use_base64_key=JWC41crr322aUfdckVfJKHvGKNIPyAPGL7rMsTbzHlA=
use_signature=true
token=1a2b3c4d5e6f
idp_url=https://idpxnyl3m.pingidentity.com/pingid
org_alias=aaaaaaaa-a1b2-123a-b456-1234abcd5678
admin_url=https://idpxnyl3m.pingidentity.com/pingid
```

|   |                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you do not have a PingOne account, you can register for a developer PingOne account on the [Ping Identity website](https://www.pingidentity.com/en/try-ping.html). For more details on the steps to configure your PingOne account to use the PingID API, refer to [PingID API Overview](pid_c_PingIDapiOverview.html). |

For this example, our registration process already knows who the user is and will initiate the online pairing process for all users. The steps our application will need to perform are:

1. Call the AddUser operation with the end-user's details and set the activateUser parameter to "true" (so we get an activation code back in the response)

2. Display the activation code to the end-user to allow them to pair their PingID application

3. Poll the GetPairingStatus operation to wait for the user to complete the PingID application pairing

## Step 1 : Create the AddUser Request

Our application is going to register a new user, Meredith Archer, into the PingID service. We already know that we want to perform online pairing so we will set the activateUser parameter to "true" when we call the AddUser operation.

The API request consists of building the JWT header and payload, signing the values and forming the token. Once we have the token we will send it to the AddUser API endpoint and inspect the results.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For this example, on the values we use in the API operation are defined. For more information on what the parameters mean and their descriptions, refer to [PingID API Overview](pid_c_PingIDapiOverview.html). |

### Create the API token header

The token header consists of three parameters, the signature algorithm which is always "HS256" and the org\_alias and token values retrieved from the PingID properties file:

| Parameter  | Value                                |
| ---------- | ------------------------------------ |
| alg        | HS256                                |
| org\_alias | aaaaaaaa-a1b2-123a-b456-1234abcd5678 |
| token      | 1a2b3c4d5e6f                         |

These values are formatted in a JSON object:

```json
{
 "alg": "HS256",
 "org_alias": "aaaaaaaa-a1b2-123a-b456-1234abcd5678",
 "token": "1a2b3c4d5e6f"
}
```

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | The token header is the same for all API calls described in this example and can be re-used across API calls. |

### Create the API token payload

The request payload is a JSON object containing two child objects: a request header (reqHeader) and a request body (reqBody). The request header is constructed with the following parameters:

| Parameter | Value                                |
| --------- | ------------------------------------ |
| locale    | en                                   |
| orgAlias  | aaaaaaaa-a1b2-123a-b456-1234abcd5678 |
| secretKey | 1a2b3c4d5e6f                         |
| timestamp | 2015-09-03 11:57:25.229              |
| version   | 4.9                                  |

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The token header is the same for all API calls described in this example and can be re-used across API calls (this timestamp should be updated for each call). |

The request body (reqBody object) in the API payload varies per API operation. In this step we are using the AddUser operation to create a PingID account for "Meredith Archer". The parameters we need for this API operation are defined below:

| Parameter    | Value                         |
| ------------ | ----------------------------- |
| activateUser | true                          |
| email        | <meredith@pingdevelopers.com> |
| fName        | Meredith                      |
| lname        | Archer                        |
| username     | meredith                      |
| role         | REGULAR                       |
| clientData   | null                          |

Putting both the reqHeader and reqBody objects into JSON and joining them together, the following JSON will provide the request token payload for the AddUser operation:

```json
{
 "reqHeader": {
  "locale":"en",
  "orgAlias":"aaaaaaaa-a1b2-123a-b456-1234abcd5678",
  "secretKey":"1a2b3c4d5e6f",
  "timestamp":"2015-09-03 11:57:25.229",
  "version":"4.9"
 },
 "reqBody": {
  "activateUser":false,
  "email":"marcher@pingdevelopers.com",
  "fName":"Meredith",
  "lname":"Archer",
  "username":"meredith",
  "role":"REGULAR",
  "clientData":null
 }
}
```

### Build and sign the API request token

To create the JWS signature, apply Base64URL encoding to the header and payload JSON. After encoding both JSON objects, join these with a period then create a signature of this string using the HMAC with SHA-256 hash algorithm. The key used for the HMAC process is the "use\_base64\_key" value found in your PingID properties file.

The steps to create the API token are described below:

```
[Signed Data] = base64UrlEncode([JSON Header]) + "." + base64UrlEncode([JSON Payload])

[Signature] = base64UrlEncode( HMACSHA256( [Signed Data] , [use_base64_key] ) )

API request token = [Signed Data] + "." + [Signature]
```

The following items are used to construct the API request token:

* Signature key (use\_base64\_key from the PingID properties file):

  ```
    JWC41crr322aUfdckVfJKHvGKNIPyAPGL7rMsTbzHlA=
  ```

* JOSE Header:

  ```
    eyJhbGciOiJIUzI1NiIsIm9yZ19hbGlhcyI6ImFhYWFhYWFhLWExYjItMTIzYS1iNDU2LTEyMzRhYmNkNTY3OCIsInRva2VuIjoiMWEyYjNjNGQ1ZTZmIn0
  ```

* JSON Payload:

  ```
    eyByZXFIZWFkZXIiOiB7ICAibG9jYWxlIjoiZW4iLCAgIm9yZ0FsaWFzIjoiYWFhYWFhYWEtYTFiMi0xMjNhLWI0NTYtMTIzNGFiY2Q1Njc4IiwgICJzZWNyZXRLZXkiOiIxYTJiM2M0ZDVlNmYiLCAgInRpbWVzdGFtcCI6IjIwMTUtMDktMDMgMTE6NTc6MjUuMjI5IiwgICJ2ZXJzaW9uIjoiNC42IiB9LCAicmVxQm9keSI6IHsgICJhY3RpdmF0ZVVzZXIiOnRydWUsICAiZW1haWwiOiJtYXJjaGVyQHBpbmdkZXZlbG9wZXJzLmNvbSIsICAiZk5hbWUiOiJNZXJlZGl0aCIsICAibG5hbWUiOiJBcmNoZXIiLCAgInVzZXJuYW1lIjoibWVyZWRpdGgiLCAgInJvbGUiOiJSRUdVTEFSIiwgICJjbGllbnREYXRhIjpudWxsIH0gfQ
  ```

* Digital Signature:

  ```
    4o60VnZOFP-C3g17WTVGxqIGc-XLrpGZphRhhoo4rWo
  ```

The resulting API request token is as follows:

```
eyJhbGciOiJIUzI1NiIsIm9yZ19hbGlhcyI6ImFhYWFhYWFhLWExYjItMTIzYS1iNDU2LTEyMzRhYmNkNTY3OCIsInRva2VuIjoiMWEyYjNjNGQ1ZTZmIn0.eyByZXFIZWFkZXIiOiB7ICAibG9jYWxlIjoiZW4iLCAgIm9yZ0FsaWFzIjoiYWFhYWFhYWEtYTFiMi0xMjNhLWI0NTYtMTIzNGFiY2Q1Njc4IiwgICJzZWNyZXRLZXkiOiIxYTJiM2M0ZDVlNmYiLCAgInRpbWVzdGFtcCI6IjIwMTUtMDktMDMgMTE6NTc6MjUuMjI5IiwgICJ2ZXJzaW9uIjoiNC42IiB9LCAicmVxQm9keSI6IHsgICJhY3RpdmF0ZVVzZXIiOnRydWUsICAiZW1haWwiOiJtYXJjaGVyQHBpbmdkZXZlbG9wZXJzLmNvbSIsICAiZk5hbWUiOiJNZXJlZGl0aCIsICAibG5hbWUiOiJBcmNoZXIiLCAgInVzZXJuYW1lIjoibWVyZWRpdGgiLCAgInJvbGUiOiJSRUdVTEFSIiwgICJjbGllbnREYXRhIjpudWxsIH0gfQ.4o60VnZOFP-C3g17WTVGxqIGc-XLrpGZphRhhoo4rWo
```

## Step 2 : Perform the AddUser API call

The next step is to make the API call to the AddUser API endpoint. This is done by sending a HTTP POST to the AddUser endpoint with the encoded API request token included as the HTTP request body. From the documentation of the [AddUser](pid_c_PingIDapiUserManagement.html#adduser) operation, the endpoint we need to POST this token to is:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/adduser/do
```

The resulting HTTPS call will look similar to the following:

```
POST https://idpxnyl3m.pingidentity.com/pingid/rest/4/adduser/do HTTP/1.1
Content-Type: application/json

eyJhbGciOiJIUzI1NiIsIm9yZ19hbGlhcyI6ImFhYWFhYWFhLWExYjItMTIzYS1iNDU2LTEyMzRhYmNkNTY3OCIsInRva2VuIjoiMWEyYjNjNGQ1ZTZmIn0.eyByZXFIZWFkZXIiOiB7ICAibG9jYWxlIjoiZW4iLCAgIm9yZ0FsaWFzIjoiYWFhYWFhYWEtYTFiMi0xMjNhLWI0NTYtMTIzNGFiY2Q1Njc4IiwgICJzZWNyZXRLZXkiOiIxYTJiM2M0ZDVlNmYiLCAgInRpbWVzdGFtcCI6IjIwMTUtMDktMDMgMTE6NTc6MjUuMjI5IiwgICJ2ZXJzaW9uIjoiNC42IiB9LCAicmVxQm9keSI6IHsgICJhY3RpdmF0ZVVzZXIiOnRydWUsICAiZW1haWwiOiJtYXJjaGVyQHBpbmdkZXZlbG9wZXJzLmNvbSIsICAiZk5hbWUiOiJNZXJlZGl0aCIsICAibG5hbWUiOiJBcmNoZXIiLCAgInVzZXJuYW1lIjoibWVyZWRpdGgiLCAgInJvbGUiOiJSRUdVTEFSIiwgICJjbGllbnREYXRhIjpudWxsIH0gfQ.4o60VnZOFP-C3g17WTVGxqIGc-XLrpGZphRhhoo4rWo
```

A successful response to this request will be:

```
HTTP/1.1 200 OK

eyJhbGciOiJIUzI1NiIsIm9yZ19hbGlhcyI6ImFhYWFhYWFhLWExYjItMTIzYS1iNDU2LTEyMzRhYmNkNTY3OCIsInRva2VuIjoiMWEyYjNjNGQ1ZTZmIn0.eyAgImFjdGl2YXRpb25Db2RlIjogIjI5MjA3MDUyMjcwMSIsICAgICJ1c2VyRGV0YWlscyI6IHsgICAgICAiZW1haWwiOiAibWVyZWRpdGhAcGluZ2RldmVsb3BlcnMuY29tIiwgICAgICAidXNlcklkIjogMTc0NTcsICAgICAgImxuYW1lIjogIkFyY2hlciIsICAgICAgInVzZXJFbmFibGVkIjogZmFsc2UsICAgICAgImZuYW1lIjogIk1lcmVkaXRoIiwgICAgICAicGljVVJMIjogIkIyVU1PVUlGRUwzQ1FIVlY0S08zWjVSMk8yRlRKWUFWVDMzTlVINk1NSTRCNUdPU1BJWkFSTkE9IiwgICAgICAic3BMaXN0IjogW10sICAgICAgImxhc3RMb2dpbiI6IG51bGwsICAgICAgImJ5cGFzc0V4cGlyYXRpb24iOiBudWxsLCAgICAgICJkZXZpY2VEZXRhaWxzIjogbnVsbCwgICAgICAibGFzdFRyYW5zYWN0aW9ucyI6IFtdLCAgICAgICJ1c2VySW5CeXBhc3MiOiBmYWxzZSwgICAgICAidXNlck5hbWUiOiAibWVyZWRpdGgiLCAgICAgICJzdGF0dXMiOiAiUEVORElOR19BQ1RJVkFUSU9OIiwgICAgICAicm9sZSI6ICJSRUdVTEFSIiAgICB9LCAgICAiZXJyb3JJZCI6IDIwMCwgICAgInVuaXF1ZU1zZ0lkIjogIndlYnNfT3pHVGVXemxGeENyejVhZXRuOUlnUlFIWGxXLVlqaGgxcU9BeGtLdmJkSSIsICAgICJlcnJvck1zZyI6ICJvayIsICAgICJjbGllbnREYXRhIjogbnVsbCAgfQ.6XMoyLUdrw7Y124-X4gNnIpj-s1qMNx-5TMXCvog5eg
```

The HTTP status code indicates that this is a success, so we can move to the next step of parsing the results of the AddUser operation.

## Step 3 : Parse the AddUser response

We received a successful response so we know the the request was successful. We can now parse the response token payload to check for the following items:

* the errorCode value in the response payload (should be 200 for a successful AddUser operation)

* the activationCode value in the UserDetails object that we need to display to the end-user to complete the device pairing process

The API response is a signed JWT, as we received the response directly from our HTTP POST operation to the HTTPS API endpoint, we are satisfied that the response is valid. So we are just going to extract the response payload from the JSON by splitting the payload at the periods and taking the second Base64URL encoded section of the token. When we Base64URL decode this section we end up with the JSON response object that we can parse with our favourite JSON parser:

```json
{
 "activationCode": "292070522701",
 "userDetails": {
  "email": "meredith@pingdevelopers.com",
  "userId": 17457,
  "lname": "Archer",
  "userEnabled": false,
  "fname": "Meredith",
  "picURL": "B2UMOUIFEL3CQHVV4KO3Z5R2O2FTJYAVT33NUH6MMI4B5GOSPIZARNA=",
  "spList": [],
  "lastLogin": null,
  "bypassExpiration": null,
  "deviceDetails": null,
  "lastTransactions": [],
  "userInBypass": false,
  "userName": "meredith",
  "status": "PENDING_ACTIVATION",
  "role": "REGULAR"
 },
 "errorId": 200,
 "uniqueMsgId": "webs_OzGTeWzlFxCrz5aetn9IgRQHXlW-Yjhh1qOAxkKvbdI",
 "errorMsg": "ok",
 "clientData": null
}
```

We can now check the two items we are interested in:

* errorId is equal to 200 which indicates that the call was successful

* activationCode is 292070522701 which we need to display to the end-user to have them pair their device

## Step 4 : Initiate Online Pairing

We have successfully created Meredith's user in the PingID service and have received an activationCode that we need Meredith to enter into her PingID mobile app. While the activationCode is being displayed and entered into Merediths phone, the application will poll the GetPairingStatus operation to check whether the mobile app pairing process is complete.

Therefore in this stage, we need to perform two tasks:

* Create a loop that polls the GetPairingStatus operation at regular intervals to evaluate the pairingStatus value (this value will be "NOT\_CLAIMED" until Meredith has successfully paired her device when it will return "SUCCESS")

* Provide the activationCode (292070522701) to Meredith so that she can enter it into her PingID mobile app

### Poll the GetPairingStatus operation

Using the steps above to create an API request token, we will create an API call to the GetPairingStatus operation with the following reqBody object. The rest of the API token (token header and reqHeader object) remains the same for all API calls so we only need to create a new reqBody object and sign the resulting token.

The [GetPairingStatus](pid_c_PingIDapiUserManagement.html#getpairingstatus) operation only requires a single parameter of activationCode that will be the activationCode we received from the AddUser call and that we are also presenting to Meredith (the clientData parameter is optional).

We will create a loop every two seconds that makes the call to the GetPairingStatus operation and evaluates the pairingStatus value in the response. When the pairingStatus value return SUCCESS we can exit the loop and return a message to Meredith that her device was successfully paired.

### Display activation code

While we are polling the GetPairingStatus operation, the application needs to provide the activationCode value to the end-user so they can enter it into their PingID mobile app (or scan a QR code representation).

The simplest process is just to display the activationCode on screen and instruct the end-user to download the PingID mobile app, and enter the activationCode when they create the service.

The application can also render a QR code to the user to simplify this process for them. To create the QR code, do the following:

1. Using the activationCode received from the AddUser operation, create a query parameter "act\_code" with the value being the activationCode (i.e. act\_code=292070522701)

2. Base64 encode this value and append to the QR redirection URL (see [Activation code redirect link for Online Pairing](pid_c_PingIDapiUserManagement.html#activation-code-redirect-link-for-online-pairing)).

   ```
    https://idpxnyl3m.pingidentity.com/pingid/QRRedirection?YWN0X2NvZGU9MjkyMDcwNTIyNzAx
   ```

3. Present this QR code to the end-user. They can either scan it with the PingID mobile app or a QR code reader to be redirected to the PingID mobile app (or the appropriate App Store for the device to download the PingID mobile app).

---
title: About the Ping Autonomous Identity API
description: Ping Autonomous Identity provides a RESTful application programming interface (API) that lets you use HTTP request methods (GET, PUT, and POST) to interact with the system and its components. The API lets a developer make requests to send or receive data to an Ping Autonomous Identity endpoint, a point where the API communicates with the system. The data that is sent or returned is in JavaScript Object Notation (JSON) format.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-api-intro
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-api-intro.html
section_ids:
  using_postman: Using Postman
---

# About the Ping Autonomous Identity API

Ping Autonomous Identity provides a RESTful application programming interface (API) that lets you use HTTP request methods (GET, PUT, and POST) to interact with the system and its components. The API lets a developer make requests to send or receive data to an Ping Autonomous Identity endpoint, a point where the API communicates with the system. The data that is sent or returned is in JavaScript Object Notation (JSON) format.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | With the release of version 2021.8.4, Ping Autonomous Identity no longer provides a Swagger client that you can access on the console. The Swagger UI was removed to tighten security within Ping Autonomous Identity. However, you can download the Ping Autonomous Identity API and import it into Postman. |

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | You cannot import the Ping Autonomous Identity API into Swagger as there is an existing CORS issue that breaks functionality. |

## Using Postman

**Download the Ping Autonomous Identity API**

1. On an upgraded Ping Autonomous Identity instance, open a browser, and log in using your account at `https://autoid-ui.forgerock.com/.`

2. Point your browser to `https://autoid-ui.forgerock.com/api/swagger.` An Opening Swagger dialog appears.

3. Save the file as `api.yml` or `conf.yml` to your local server or laptop.

4. Open Postman, and click Import. The file is imported into Postman.

5. Click Zoran-API-Service.

> **Collapse: Click an example**
>
> ![postman api](_images/postman-api.gif)

You now can access the Ping Autonomous Identity API in Postman.

---

---
title: Access Control
description: The following are Ping Autonomous Identity access control endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-access-control-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-access-control-api.html
section_ids:
  get_apiuserdetailsdecisions: GET /api/userDetails/decisions
  post_apiuserdetailsdecisions: POST /api/userDetails/decisions
  post_apirulesdecision: POST /api/rules/decision
---

# Access Control

The following are Ping Autonomous Identity access control endpoints:

## GET /api/userDetails/decisions

* GET /api/userDetails/decisions

  Get the current entitlement decisions for the user. \[Supervisor, Ent Owner, App Owner, Admin]

  Endpoint

  ```
  /api/userDetails/decisions
  ```

  Authorization

  ```
  <Bearer Token JWT-value> OR <API-KEY>
  ```

  Param

  ```
  user=john.doe
  ```

  **Query Parameters**

  | Parameter | Type   | Description                                 |
  | --------- | ------ | ------------------------------------------- |
  | user      | string | User ID (required)                          |
  | filter    | object | Filter to add (single property shown below) |

  **Filter Query Object Properties**

  | Parameter           | Type   | Description                              |
  | ------------------- | ------ | ---------------------------------------- |
  | datasinkStatus      | string | Datasink status filter ('ack' or 'nack') |
  | timestampThresholds |        | Timestamp threshold object               |

  **timestampThresholds Object Properties**

  | Parameter | Type   | Description                                                                                        |
  | --------- | ------ | -------------------------------------------------------------------------------------------------- |
  | gt        | string | Greater than timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **gte**.         |
  | gte       | string | Greater than or equal timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **gt**. |
  | lt        | string | Less than timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **lte**.            |
  | lte       | string | Less than or equal timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **le**.    |

  Example Request (DatasinkStatus Filter)

  ```
  curl -k -X GET \
  'datasinkStatus=nack' \
  -H 'Authorization: Bearer <token value>' \  <or>   -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json'
  ```

  Example Response (DatasinkStatus Filter)

  ```
  {
    "decisions": [
      {
        "user": "john.doe",
        "entitlement": "ent_1",
        "is_certified": false,
        "is_revoked": false,
        "is_processed": false,
        "is_archived": false,
        "author": "jane.smith",
        "author_name": "Jane Smith",
        "author_type": "Zoran Admin",
        "reason": null,
        "last_updated": "2022-01-11T19:48:17.195Z",
        "datasink_status": "nack",
        "usr_name": "John Doe",
        "ent_name": "Entitlement 1",
        "app_id": "Gateway",
        "app_name": "Gateway",
        "usr_manager_id": "john.smith",
        "conf": 0.75,
        "freq": 4,
        "freqUnion": 3
      }
    ]
  }
  ```

## POST /api/userDetails/decisions

* POST /api/userDetails/decisions

  Update entitlement decisions for users. \[Supervisor, Ent Owner, App Owner, Admin]

  Endpoint

  ```
  /api/userDetails/decisions
  ```

  Authorization

  ```
  <Bearer Token JWT-value> OR &ltAPI-KEY>
  ```

  **Request Body Parameters**

  | Parameter        | Type                        | Description                                                                                |
  | ---------------- | --------------------------- | ------------------------------------------------------------------------------------------ |
  | assignments      | array of assignment objects | List of assignments affected by the decision (available properties listed below)(required) |
  | is\_certified    | boolean                     | Certification decision                                                                     |
  | is\_revoked      | boolean                     | Revoke decision                                                                            |
  | is\_requested    | boolean                     | Decision is processed                                                                      |
  | reason           | string                      | Reason for decision                                                                        |
  | datasink\_status | string                      | Datasink status ('ack' or 'nack')                                                          |

  **Assignments Object Properties**

  | Parameter    | Type         | Description                         |
  | ------------ | ------------ | ----------------------------------- |
  | user         | string       | User ID (required)                  |
  | entitlements | string array | List of entitlement ID's (required) |

  Body

  ```
  {
    "assignments": [
      {
        "user": "string",
        "entitlements": [
          "string"
        ]
      }
    ],
    "is_certified": true,
    "is_revoked": true,
    "is_requested": true,
    "is_processed": true,
    "reason": "string",
    "datasink_status": "nack"
  }
  ```

  Example Request

  ```
  curl --request POST "https://autoid-api.forgerock.com/api/userDetails/decisions" \
  -H  "accept: /" -H  "Content-Type: application/json" \
  --data-raw '{
      "assignments": [
         {
            "user": "string",
            "entitlements": [
               "string"
            ]
         }
      ],
      "is_certified": true,
      "is_revoked": true,
      "is_requested": true,
      "is_processed": true,
      "reason": "string",
      "datasink_status": "nack"
  }'
  ```

  Example Response

  ```
  {
    "status": 200
  }
  ```

## POST /api/rules/decision

* POST /api/rules/decision

  Update rule decisions. \[Supervisor, Ent Owner, App Owner, Admin]

  Endpoint

  ```
  /api/rules/decision
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  **Request Body Parameters**

  | Parameter           | Type                   | Description                                                                          |
  | ------------------- | ---------------------- | ------------------------------------------------------------------------------------ |
  | rules               | array of rules objects | List of rules affected by the decision (available properties listed below)(required) |
  | is\_autocertify     | boolean                | Auto-Certification decision (required)                                               |
  | is\_autorequest     | boolean                | Auto-Request decision (required)                                                     |
  | autocertify\_reason | boolean                | Auto-Certification reason (required)                                                 |
  | autorequest\_reason | boolean                | Auto-Request reason (required)                                                       |
  | datasink\_status    | string                 | Datasink status ('ack' or 'nack')                                                    |

  **Rule Object Properties**

  | Parameter     | Type         | Description                           |
  | ------------- | ------------ | ------------------------------------- |
  | entitlement   | string       | Entitlement ID (required)             |
  | justification | string array | List of raw justifications (required) |

  Body

  ```
  {
    "rules": [
      {
        "entitlement": "string",
        "justification": [
          "string"
        ]
      }
    ],
    "is_autocertify": true,
    "is_autorequest": true,
    "autocertify_reason": "string",
    "autorequest_reason": "string"
  }
  ```

  Example Request

  ```
  curl -k -X POST \
  "https://autoid-api.forgerock.com/api/rules/decision" \
  -H 'Authorization: Bearer <token-value>' \
  -H  "accept: /" -H  "Content-Type: application/json" \
  --data-raw '{
  "rules": [
      {
        "entitlement": "Ent_1",
        "justification": [
          "0C_CHIEF_YES_NO_Yes",
          "0C_JOBCODE_NAME_Service Representitive II",
          "0C_MANAGER_NAME_John_Doe",
          "0C_USR_EMP_TYPE_Non-Employee"
        ]
      }
    ],
    "is_autocertify": true,
    "is_autorequest": false,
    "autocertify_reason": "Goodbye, world.",
    "autorequest_reason": "Hello, world."
  }'
  ```

  Example Response

  ```
  Status 204: No Content
  ```

---

---
title: API service
description: The following are Ping Autonomous Identity API Service endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-api-service
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-api-service.html
section_ids:
  get_health_check: GET /health-check
  get_version: GET /version
---

# API service

The following are Ping Autonomous Identity API Service endpoints:

## GET /health-check

* GET /health-check

  Check that the Ping Autonomous Identity API service is running. Get uptime statistics. \[All]

  Endpoint

  ```
  /health-check
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Body

  Example Request

  ```
  curl --request GET "<instance-IP>/health-check" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "status": "zoran-api: OK",
    "uptime": 5412.465875997,
    "uptimeFormatted": "1:30:12"
  }
  ```

## GET /version

* GET /version

  Get the version number of this service. \[All]

  Endpoint

  ```
  /version
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Body

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/version" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "version": "1.0",
  }
  ```

---

---
title: Applications
description: The following are Ping Autonomous Identity applications view endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-applications-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-applications-api.html
section_ids:
  get_apiapplications: GET /api/applications
  post_apiapplicationsappid: POST /api/applications/{appId}
  post_apiapplicationsappidassignments: POST /api/applications/{appId}/assignments
  get_apiapplicationssearch: GET /api/applications/search
---

# Applications

The following are Ping Autonomous Identity applications view endpoints:

## GET /api/applications

* GET /api/applications

  Get a list of applications and stats for an Application Owner. \[App Owner, Admin]

  Endpoint

  ```
  /api/applications
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  ownerId (optional)  derick.hui
  cursor (optional)   string (Indicator on where to start a 2+ page list)
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/applications?ownerId=derick.hui" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "cursor": "string",
    "total_applications": 0,
    "total_entitlements": 0,
    "total_assignments": 0,
    "applications": [
      {
        "app_id": "string",
        "app_name": "string",
        "high": 0,
        "medium": 0,
        "low": 0,
        "avg": 0
      }
    ]
  }
  ```

## POST /api/applications/{appId}

* POST /api/applications/{appId}

  Get a list of entitlements and stats for a selected application. \[App Owner, Admin]

  Endpoint

  ```
  /api/applications/{appId}
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  appId  (required)   app_1
  cursor (optional)   string (Indicator on where to start a 2+ page list)
  ```

  Body

  ```
  {
    "filters": [
      {
        "type": "user",
        "attribute": "city",
        "value": ["Seattle", "Denver"]
      },
      {
        "type": "user",
        "attribute": "line_of_business",
        "value": ["Distribution Operations"]
      }
    ]
  }
  ```

  Example Request

  ```
  curl --request POST "https://autoid-api.forgerock.com/api/applications/app_1" \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer <token>" \
  --data-raw '{
    "filters": [
      {
        "type": "user",
        "attribute": "city",
        "value": ["Seattle", "Denver"]
      },
      {
        "type": "user",
        "attribute": "line_of_business",
        "value": ["Distribution Operations"]
      }
    ]
  }'
  ```

  Example Response

  ```
  {
    "cursor": "string",
    "total_entitlements": 0,
    "total_users": 0,
    "total_rules": 0,
    "entitlements": [
      {
        "ent": "string",
        "ent_name": "string",
        "high": 0,
        "medium": 0,
        "low": 0,
        "avg": 0
      }
    ]
  }
  ```

## POST /api/applications/{appId}/assignments

* POST /api/applications/{appId}/assignments

  Get filterable user-entitlement assignment and decision data for a specific application. \[App Owner, Admin]

  Endpoint

  ```
  api/applications/{appId}/assignments
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  appId  (required)   app_1
  user                string
  cursor (optional)   string (Indicator on where to start a 2+ page list)
  sortBy              string
  sortDir             string
  ```

  Body

  ```
  {
    "filters": [
      {
        "type": "user",
        "attribute": "city",
        "value": [
          "Seattle",
          "Denver"
        ]
      },
      {
        "type": "user",
        "attribute": "line_of_business",
        "value": [
          "Distribution Operations"
        ]
      }
    ]
  }
  ```

  Example Request

  ```
  curl --request POST "https://autoid-api.forgerock.com/api/applications/app_1/assignments" \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer <token>" \
  --data-raw '{
     "filters": [
         {
           "type": "user",
           "attribute": "city",
           "value": [
             "Seattle",
             "Denver"
           ]
         },
         {
           "type": "user",
           "attribute": "line_of_business",
           "value": [
             "Distribution Operations"
           ]
         }
       ]
  }'
  ```

  Example Response

  ```
  {
    "cursor": "string",
    "total_users": 0,
    "total_entitlements": 0,
    "total_assignments": 0,
    "assignments": [
      {
        "ent": "string",
        "ent_name": "string",
        "confidence": 0,
        "user_id": "string",
        "user_name": "string",
        "isCertified": true,
        "dateCertified": "2021-04-14T19:10:39.178Z",
        "isRevoked": true,
        "dateRevoked": "2021-04-14T19:10:39.178Z",
        "isRequested": true,
        "dateRequested": "2021-04-14T19:10:39.178Z",
        "isProcessed": true,
        "approvalAuthor": {
          "id": "string",
          "name": "string"
        }
      }
    ]
  }
  ```

## GET /api/applications/search

* GET /api/applications/search

  Search all applications. \[App Owner, Admin]

  Endpoint

  ```
  /api/applications/search
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  by	     appOwner or enttOwner
  user     user ID
  q        Search query string
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/applications/search" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "values": [
      {
        "app_id": "string",
        "app_name": "string"
      }
    ]
  }
  ```

---

---
title: Assignments
description: The following endpoint has been added to support the extraction of assignments. New APIs introduced in this release are marked with .
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-assignments-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-assignments-api.html
section_ids:
  post_apiassignments: POST /api/assignments
---

# Assignments

The following endpoint has been added to support the extraction of assignments. New APIs introduced in this release are marked with [icon: star, set=fa].

## POST /api/assignments

* [icon: star, set=fa]

  POST /api/assignments

  Get a list of all assignments or filtered assignments when the following optional filtering is sent as a JSON request body.

  The endpoint requires a valid API key passed in a `X-API-KEY` header for authorization (refer to [Generate an API key](chap-obtain-api-key.html)) or an authorized admin-level bearer token.

  Endpoint

  \+

  ```
  /api/assignments
  ```

  Headers

  \+

  ```
  Content-Type      application/json
  ```

  Body Parameters

  | Parameter | Type    | Description                                                                                            |
  | --------- | ------- | ------------------------------------------------------------------------------------------------------ |
  | cursor    | string  | Cursor to send for the next page of assignments (the response returns null if there are no more pages) |
  | pageSize  | integer | Number of assignments to return per page                                                               |
  | ent\_id   | string  | Entitlement ID to filter by                                                                            |
  | usr\_id   | string  | User ID to filter by                                                                                   |
  | app\_id   | string  | Application ID to filter by                                                                            |

  Example Request

  \+

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/assignments \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "pageSize": 20,
    "cursor": "WyJhYXJvbi5maXNjaGVyIiwiV0VCX3VzZXJfU2hhcmVkX0VkaXRfQURNSU5fSUkiXQ=="
  }'
  ```

  Example Response

  \+

  ```
  {
    "cursor": "WyJhYXJvbi5mb2x0eiIsIldlYl9TZXJ2aWNlQW5hbHl0aWNzIDogS1BJIEFnZW50IGFuZCBQb3dlciBBY2Nlc3NfSUkiXQ==",
    "assignments": [
     {
        "ent_id": "WEB_user_Web_Local Access 32 All_II_Europe",
        "usr_id": "aaron.fischer",
        "score": null,
        "justification": []
      },
     {
        "ent_id": "WEB_user_Web_Shared_Edit_ADMIN_Europe",
        "usr_id": "aaron.fischer",
        "score": null,
        "justification": []
     },
     {
        "ent_id": "WEB_user_Web_WEB RCQ Flare NonIT Distribution_Europe",
        "usr_id": "aaron.fischer",
        "score": 0.98,
        "justification": [
         {
            "id": "CHIEF_YES_NO",
            "title": "chief_yes_no",
            "value": "Yes"
         },
         {
            "id": "USR_DEPARTMENT_NAME",
            "title": "USR_DEPARTMENT_NAME",
            "value": "Information Systems 1"
         }
        ]
     },
     {
        "ent_id": "Web_Flare NonIT Distribution",
        "usr_id": "aaron.fischer",
        "score": 0.6,
        "justification": [
         {
           "id": "CITY",
           "title": "city",
           "value": "Jacksonville"
         },
         {
           "id": "USR_EMP_TYPE",
           "title": "usr_emp_type",
           "value": "Employee"
         },
         {
           "id": "LINE_OF_BUSINESS",
           "title": "line_of_business",
           "value": "Strategy and Policy"
         }
        ]
      }
    ]
  }
  ```

---

---
title: Authentication
description: The following are Ping Autonomous Identity authentication endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-authentication-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-authentication-api.html
section_ids:
  post_apiauthenticationlogin: POST /api/authentication/login
  api-authentication-verify: GET /api/authentication/verify
  post_apiauthenticationrenewtoken: POST /api/authentication/renewToken
  get_apiauthenticationactions: GET /api/authentication/actions
---

# Authentication

The following are Ping Autonomous Identity authentication endpoints:

## POST /api/authentication/login

* POST /api/authentication/login

  Log in to the system. The endpoint accepts the `username` and `password` in the body of the request. The token provided has an expiry date that can be obtained by decoding the returned JWT and using the `exp` data inside the token. \[All]

  Endpoint

  ```
  /api/authentication/login
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Body

  ```
  {
  	"username": "admin@test.com",
  	"password": "test"
  }
  ```

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/authentication/login' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  	"username": "admin@test.com",
  	"password": "test"
  }'
  ```

  Example Response

  ```
  {
    "user": {
      "dn": "cn=test.user@test.com,dc=example,dc=org",
      "controls": [],
      "gidNumber": "7777",
      "uid": "test.user",
      "displayName": "Test User",
      "_groups": [
        "Admin"
      ]
    },
    "token": "123456"
  }
  ```

## GET /api/authentication/verify

* GET /api/authentication/verify

  Verify the authenticity of a bearer token.

  Endpoint

  ```
  /api/authentication/verify
  ```

  Authorization

  ```
  Token             <token>
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Body

  ```
  ''
  ```

  Example Request

  ```
  curl --location --request GET 'https://autoid-api.forgerock.com/api/authentication/verify' \
  --header 'Content-Type: application/json'
  ```

  Example Response

  ```
  {
    "user": {
      "controls": [],
      "displayName": "Bob Rodgers",
      "email": "bob.rodgers@forgerock.com",
      "dn": "cn=bob.rodgers@forgerock.com,ou=People,dc=zoran,dc=com",
      "gidNumber": "999",
      "uid": "bob.rodgers",
      "_groups": [
        "Zoran Admin"
      ],
      "iat": 1628893019,
      "exp": 1628936219,
      "aud": "http://my.service",
      "sub": "6711197"
    }
  }
  ```

## POST /api/authentication/renewToken

* POST /api/authentication/renewToken

  Renew a token for the system. The endpoint accepts the JWT in the header `Authorization: Bearer JWT`. The expiry time of the token is reset and return in the new token. \[All]

  Endpoint

  ```
  /api/authentication/renewToken
  ```

  Authorization

  ```
  Token             <token>
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Body

  ```
  ''
  ```

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/authentication/renewToken' \
  --header 'Content-Type: application/json' \
  --data-raw ''
  ```

  Example Response

  ```
  {
    "user": {
      "dn": "cn=test.user@test.com,dc=example,dc=org",
      "controls": [],
      "gidNumber": "7777",
      "uid": "test.user",
      "displayName": "Test User",
      "_groups": [
        "Admin"
      ]
    },
    "token": "123456"
  }
  ```

## GET /api/authentication/actions

* GET /api/authentication/actions

  Retrieve the permitted actions of the currently authenticated user. \[All]

  Endpoint

  ```
  /api/authentication/action
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Example Request

  ```
  curl --location --request GET 'https://autoid-api.forgerock.com/api/authentication/actions' \
  --header 'Content-Type: application/json'
  ```

  Example Response

  ```
  {
    "userActions": [
      "*"
    ],
    "roleTitle": "Unknown",
    "homepage": "company"
  }
  ```

---

---
title: Autonomous Identity API
description: This chapter is targeted to developers who want to access Ping Autonomous Identity using the REST Application Programming Interface (API).
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:preface
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/preface.html
---

# Autonomous Identity API

This chapter is targeted to developers who want to access Ping Autonomous Identity using the REST Application Programming Interface (API).

Ping® Autonomous Identity is an entitlements and roles analytics system that lets you fully manage your company's access to your data.

An entitlement refers to the rights or privileges assigned to a user or thing for access to specific resources. A company can have millions of entitlements without a clear picture of what they are, what they do, and who they are assigned to. Ping Autonomous Identity solves this problem by using advanced artificial intelligence (AI) and automation technology to determine the full entitlements landscape for your company. The system also detects potential risks arising from incorrect or over-provisioned entitlements that lead to policy violations. Ping Autonomous Identity eliminates the manual re-certification of entitlements and provides a centralized, transparent, and contextual view of all access points within your company.

[icon: question, set=fas, size=3x]

#### [About the API](chap-api-intro.html)

Learn about the Ping Autonomous Identity API.

[icon: key, set=fas, size=3x]

#### [Obtain the API key](chap-obtain-api-key.html)

Learn how to get an API key.

[icon: code, set=fas, size=3x]

#### [API service](chap-api-service.html)

Access the API Service endpoints.

[icon: handshake, set=fas, size=3x]

#### [Authentication](chap-authentication-api.html)

Access the Authentication endpoints.

[icon: user-shield, set=fas, size=3x]

#### [SSO](chap-sso-api.html)

Access the SSO endpoints.

[icon: cogs, set=fas, size=3x]

#### [Config](chap-config-api.html)

Access the Config endpoints.

[icon: book, set=fas, size=3x]

#### [Report](chap-report-api.html)

Access the Report API.

[icon: building, set=fas, size=3x]

#### [Company view](chap-companyview-api.html)

Access the Company View API.

[icon: user, set=fas, size=3x]

#### [User details](chap-userdetails-api.html)

Access the user details endpoints.

[icon: compress-arrows-alt, set=fas, size=3x]

#### [Access control](chap-access-control-api.html)

Access the Access Control endpoints.

[icon: calendar-check, set=fas, size=3x]

#### [Applications](chap-applications-api.html)

Access the applications endpoints.

[icon: user-plus, set=fas, size=3x]

#### [Entitlements](chap-entitlements-api.html)

Access the entitlements endpoints.

[icon: equals, set=fas, size=3x]

#### [Assignments](chap-assignments-api.html)

Access the assignments endpoint.

[icon: gavel, set=fas, size=3x]

#### [Rules](chap-rules-api.html)

Access the rules endpoints.

[icon: filter, set=fas, size=3x]

#### [Filters](chap-filters-api.html)

Access the filters endpoints.

[icon: user-cog, set=fas, size=3x]

#### [Roles](chap-roles-api.html)

Access the roles endpoints.

[icon: file-import, set=fas, size=3x]

#### [Ingest](chap-ingest-api.html)

Access the ingest endpoints.

[icon: briefcase, set=fas, size=3x]

#### [Jobs](chap-jobs-api.html)

Access the jobs endpoints.

---

---
title: Company View
description: The following are Ping Autonomous Identity company view endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-companyview-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-companyview-api.html
section_ids:
  get_apicompanyview: GET /api/companyview
  get_apicompanyviewallentitlementsavggroups: GET /api/companyview/allEntitlementsAvgGroups
  get_apicompanyviewmostcriticalentitlements: GET /api/companyview/mostCriticalEntitlements
  get_apicompanyviewassignmentstats: GET /api/companyview/assignmentStats
  get_apicompanyviewassignmenthistconfsummaryyearmonth: GET /api/companyview/assignmentHistConfSummary/{year}/{month}
---

# Company View

The following are Ping Autonomous Identity company view endpoints:

## GET /api/companyview

* GET /api/companyview

  Get the data for company overview dashboard data. \[Executive, Admin]

  Endpoint

  ```
  /api/companyview
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/companyview" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "companyView": {
      "employeeTypes": [
        {
          "type": "Employee",
          "high": 723,
          "low": 27,
          "medium": 1796,
          "null_conf": 0,
          "total": 2546
        },
        {
          "type": "Non-Employee",
          "high": 867,
          "low": 14,
          "medium": 1768,
          "null_conf": 0,
          "total": 2649
        }
      ],
      "employees_wo_manager": 0,
      "employees_w_manager": 5200,
      "entitlements_without_roleowners": 0,
      "entitlements_with_roleowners": 2456,
      "total_employees": 5200,
      "coverage": {
        "total": 2456,
        "covered": 2456,
        "not_covered": 0
      },
      "entitlementsDistribution": {
        "no_users": 0,
        "one_user": 0,
        "zero_to_five_users": 1,
        "five_to_ten_users": 1064,
        "ten_to_hundred_users": 1549,
        "hundred_to_onek_user": 35,
        "onek_to_tenk_users": 0,
        "tenk_users": 0,
        "hundredk_users": 0
      }
    }
  }
  ```

## GET /api/companyview/allEntitlementsAvgGroups

* GET /api/companyview/allEntitlementsAvgGroups

  Get the average confidence score list for the company view chart. \[Executive, Admin]

  Endpoint

  ```
  /api/companyview/allEntitlementAvgGroups
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/companyview/allEntitlementAvgGroups" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "entitlementList": [
      {
        "start": 0,
        "end": 0.05,
        "entitlementCount": 2
      },
      {
        "start": 0.06,
        "end": 0.1,
        "entitlementCount": 14
      }
    ]
  }
  ```

## GET /api/companyview/mostCriticalEntitlements

* GET /api/companyview/mostCriticalEntitlements

  Get the most critical entitlements list. \[Executive, Admin]

  Endpoint

  ```
  /api/companyview/mostCriticalEntitlements
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/companyview/mostCriticalEntitlements" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  [
    {
      "org": "organization",
      "entt_id": "ent1",
      "avg_conf_score": 0.04,
      "entt_name": "Ent 1",
      "high": 0,
      "low": 1,
      "medium": 0,
      "seq": 0,
      "total_employees": 6
    },
    {
      "org": "organization",
      "entt_id": "ent2",
      "avg_conf_score": 0.04571,
      "entt_name": "Ent 2",
      "high": 0,
      "low": 1,
      "medium": 0,
      "seq": 1,
      "total_employees": 7
    }
  ]
  ```

## GET /api/companyview/assignmentStats

* GET /api/companyview/assignmentStats

  Get the total assignments, low/high confidence, high volume and low/high confidence, most assigned \[Executive, Admin]

  Endpoint

  ```
  /api/companyview/assignmentsStats
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  assignmentLimit  1
  highVolumeHighMinScore  0.9
  highVolumentHighMinUsersCount 100
  highVolumenLowMaxScore  0.2
  highVolumeLowMinUsersCount 100
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/companyview/assignmentsStats?assignmentsLimit=5" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "total": 47670,
    "high": 13145,
    "low": 4992,
    "unscored": 4986,
    "mostAssigned": [
      {
        "count": 344,
        "entitlement": "ent1"
      }
    ],
    "mostAssignedCount": 35,
    "highVolume": {
      "high": 23,
      "low": 17
    }
  }
  ```

## GET /api/companyview/assignmentHistConfSummary/{year}/{month}

* GET /api/companyview/assignmentHistConfSummary/{year}/{month}

  Get the number of high, medium, and low confidence assignments for the past 12-month period ending in a given year and month. \[Executive, admin]

  Endpoint

  ```
  /api/companyview/assignmentsHistConfSummary/2020/01
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/companyview/assignmentsHistConfSummary/2020/1" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  [
    {
      "year": 0,
      "month": 0,
      "highConf": 0,
      "medConf": 0,
      "lowConf": 0,
      "total": 0
    }
  ]
  ```

---

---
title: Config
description: The following are Ping Autonomous Identity config endpoint:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-config-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-config-api.html
section_ids:
  get_apiconfig: GET /api/config
  get_apiadminreloaduiconfig: GET /api/admin/reloadUIConfig
  api-admin-updateuser: POST /api/admin/updateUser
  api-admin-updateself: POST /api/admin/updateSelf
  api-admin-disableuser: POST /api/admin/disableUser
  api-admin-enableuser: POST /api/admin/enableUser
  api-admin-createuser: POST /api/admin/createUser
  api-admin-createapitoken: POST /api/admin/createApiToken
  api-admin-revokeapitoken: POST /api/admin/revokeApiToken
  api-admin-verifyapitoken: GET /api/admin/verifyApiToken/{token}
  api-admin-gettokens: GET /api/admin/getTokens
  api-admin-getusers: GET /api/admin/getUsers
---

# Config

The following are Ping Autonomous Identity config endpoint:

## GET /api/config

* GET /api/config

  Get the configuration. This endpoint is mainly used by the Ping Autonomous Identity UI microservice to get values stored in Consul. \[All]

  Endpoint

  ```
  /api/config
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/config" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "thresholds": {
      "top": 1.01,
      "high": 0.75,
      "medium": 0.35,
      "low": 0,
      "autoAccess": 0.5
    },
    "volumeThresholds": {
      "high": 90,
      "low": 20
    },
    "mostAssignedStats": {
      "count": 100
    },
    "highVolumeStats": {
      "high": {
        "minScore": 0.9,
        "minUsersCount": 100
      },
      "low": {
        "maxScore": 0.2,
        "minUsersCount": 100
      }
    },
    "authorizers": {
      "ldap": true,
      "oidc": false
    }
  }
  ```

## GET /api/admin/reloadUIConfig

* GET /api/admin/reloadUIConfig

  Reload justification and filterable attributes configuration from JAS. \[User, Supervisor, Ent Owner, App Owner, Admin]

  Endpoint

  ```
  /api/admin/reloadUIConfig
  ```

  Headers

  ```
  Content-Type      / 
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/admin/reloadUIConfig" \
  -H  "accept: /"
  ```

## POST /api/admin/updateUser

* POST /api/admin/updateUser

  Update credentials for a user.

  Endpoint

  ```
  /api/admin/updateUser
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	email: "john.doe@forgerock.com",
  	password: "password",
  	groups: ["Zoran Supervisor", "Zoran Role Engineer"]
  }
  ```

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/admin/updateUser' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <token>' \
  --data-raw '{
      "email": "john.doe@forgerock.com",
      "password": "password",
  	"groups": ["Zoran Supervisor", "Zoran Role Engineer"]
  }'
  ```

  Example Response

  ```
  { message: 'success' }
  ```

## POST /api/admin/updateSelf

* POST /api/admin/updateSelf

  Update credentials for a user.

  Endpoint

  ```
  /api/admin/updateSelf
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	email: "john.doe@forgerock.com",
  	password: "password",
  	groups: ["Zoran Supervisor", "Zoran Role Engineer"]
  }
  ```

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/admin/updateSelf' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <token>' \
  --data-raw '{
      "email": "john.doe@forgerock.com",
  	"password": "password",
  	"groups": ["Zoran Supervisor", "Zoran Role Engineer"]
  }'
  ```

  Example Response

  ```
  { message: 'success' }
  ```

## POST /api/admin/disableUser

* POST /api/admin/disableUser

  Disable user account.

  Endpoint

  ```
  /api/admin/disableuser
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	email: "john.doe@forgerock.com"
  }
  ```

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/admin/disableUser' \
  --header 'Content-type: application/json' \
  --header 'Authorization: Bearer <token>' \
  --data-raw '{
  	"email": "john.doe@forgerock.com"
  }'
  ```

  Example Response

  ```
  { message: 'success' }
  ```

## POST /api/admin/enableUser

* POST /api/admin/enableUser

  Enable a user account.

  Endpoint

  ```
  /api/admin/enableUser
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	email: "john.doe@forgerock.com"
  }
  ```

  Example Request

  ```
  curl --location --request POST "https://autoid-api.forgerock.com/api/admin/enableUser" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>" \
  --data-raw '{
      "email": "john.doe@forgerock.com"
  }'
  ```

  Example Response

  ```
  { message: 'success' }
  ```

## POST /api/admin/createUser

* POST /api/admin/createUser

  Create credentials for a user

  Endpoint

  ```
  /api/admin/createUser
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	dn: "cn=john.doe@forgerock.com,ou=People,dc=zoran,dc=com",gidNumber: "321",
  	email: "john.doe@forgerock.com",
  	password: "password",
  	controls: [],
  	displayName: "John Doe",
  	uid: "john.doe",
  	groups: ["Zoran Admin"]
  }
  ```

  Example Request

  ```
  curl --request POST "https://autoid-api.forgerock.com/api/admin/createUser" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>" \
  --data-raw '{
  	dn: "cn=john.doe@forgerock.com,ou=People,dc=zoran,dc=com",gidNumber: "321",
  	email: "john.doe@forgerock.com",
  	password: "password",
  	controls: [],
  	displayName: "John Doe",
  	uid: "john.doe",
  	groups: ["Zoran Admin"]
  }'
  ```

  Example Response

  ```
  { message: 'success' }
  ```

## POST /api/admin/createApiToken

* POST /api/admin/createApiToken

  Create API credentials (token) for a user.

  Endpoint

  ```
  /api/admin/createApiToken
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	name: "John Doe",
  	description: "description",
  	expiration: "2021-08-12T12:00:00.000Z"
  }
  ```

  Example Request

  ```
  curl --request POST "https://autoid-api.forgerock.com/api/admin/createApiToken" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>" \
  --data-raw '{
  	name: "John Doe",
  	description: "description",
  	expiration: "2021-08-12T12:00:00.000Z"
  }'
  ```

  Example Response

  ```
  { token: uuid }
  ```

## POST /api/admin/revokeApiToken

* POST /api/admin/revokeApiToken

  Revoke API credentials for a user.

  Endpoint

  ```
  /api/admin/revokeApiToken
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	token: "11b57769-d436-4357-bc1c-0e0b9c6a49b6"
  }
  ```

  Example Request

  ```
  curl --location --request POST "https://autoid-api.forgerock.com/api/admin/revokeApiToken" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>" \
  --data-raw '{
  	token: "11b57769-d436-4357-bc1c-0e0b9c6a49b6"
  }'
  ```

  Example Response

  ```
  { message: 'User token disabled' }
  ```

## GET /api/admin/verifyApiToken/{token}

* GET /api/admin/verifyApiToken/{token}

  Verify that an API token is valid

  Endpoint

  ```
  /api/admin/verifyApiToke
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/admin/verifyApiToken/da0b5228-1e11-4278-ad1c-f0938fccdf82" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>"
  ```

  Example Response

  ```
  {
    "name": "John Doe",
    "description": "description",
    "expiration": "2021-08-17T12:00:00.000Z",
    "is_valid": true,
    "creator": "bob.rodgers@forgerock.com",
    "modifier": "bob.rodgers@forgerock.com"
  }
  ```

## GET /api/admin/getTokens

* GET /api/admin/getTokens

  Get a list of tokens.

  Endpoint

  ```
  /api/admin/getTokens
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  		maxResults: 6,
  		offset: 5
  }
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/admin/getTokens" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>" \
  --data-raw '{
  	maxResults: 6,
  	offset: 5
  }'
  ```

  Example Response

  ```
  [{
    "token": "da0b5228-1e11-4278-ad1c-f0938fccdf82",
    "name": "John Doe",
    "description": "description",
    "expiration": "2021-08-17T12:00:00.000Z",
    "is_valid": true,
    "creator": "bob.rodgers@forgerock.com",
    "modifier": "bob.rodgers@forgerock.com"
  }]
  ```

## GET /api/admin/getUsers

* GET /api/admin/getUsers

  Get a list of users.

  Endpoint

  ```
  /api/admin/getUsers
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
  	maxResults: 6,
  	offset: 5,
  	sortBy: uid | displayName | gidNumber
  }
  ```

  Example Request

  ```
  curl --location --request GET "https://autoid-api.forgerock.com/api/admin/getUsers" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>" \
  --data-raw '{
  	maxResults: 6,
      offset: 5,
      sortBy: uid
  }'
  ```

  Example Response

  ```
  [{
      "controls": [],
      "displayName": "David Elliott",
      "email": "david.elliott@forgerock.com",
      "dn": "cn=david.elliott@forgerock.com,ou=People,dc=zoran,dc=com",
      "gidNumber": "809",
      "uid": "david.elliott",
      "_groups": [
        "Zoran Entitlement Owner"
      ],
      "enabled": true
  }]
  ```

---

---
title: Config
description: The following are Ping Autonomous Identity configuration endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-configurations-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-configurations-api.html
---

# Config

The following are Ping Autonomous Identity configuration endpoints:

* PUT RevokeCertifyAccessConf

  Sets the schema definition for the matching database table (`revoke_certify_access_request`), which is stored in Consul. This endpoint allows the configuration to be changed on the fly.

Endpoint

```
/config/RevokeCertifyAccessConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "RevokeCertifyAccess",
  "modelDefinition": {
    "fields": {
      "is_processed": "boolean",
      "entitlement": "text",
      "user": "text",
      "manager": "text",
      "manager_decision": "int",
      "manager_date_created": "timestamp",
      "role_owner": "text",
      "role_owner_decision": "int",
      "role_owner_date_created": "timestamp",
      "date_created": "timestamp"
   },
   "key": [
      "is_processed"
   ],
   "table_name": "revoke_certify_access_request"
  }
}
```

Example Request

```
curl --location --request PUT '/config/RevokeCertifyAccessConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name"	: "RevokeCertifyAccess",
  "modelDefinition": {
    "fields": {
      "is_processed": "boolean",
      "entitlement": "text",
      "user": "text",
      "manager": "text",
      "manager_decision": "int",
      "manager_date_created": "timestamp",
      "role_owner": "text",
      "role_owner_decision": "int",
      "role_owner_date_created": "timestamp",
      "date_created": "timestamp"
   },
   "key": [
      "is_processed"
   ],
   "table_name": "revoke_certify_access_request"
  }
}'
```

* PUT CompanyViewOverviewConf

  Sets the schema definition for the related database table {{company\_view\_overview}}.

Endpoint

```
/config/CompanyViewOverviewConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "CompanyViewOverview",
  "modelDefinition": {
    "fields": {
      "key": "text",
      "total_employees": "int",
      "employees_wo_manager": "int",
      "employees_w_manager": "int",
      "entitlements_without_roleowners": "int",
      "entitlements_with_roleowners": "int",
      "total_entitlements": "int",
      "entitlements_covered_by_model": "int",
      "entitlements_not_covered": "int",
      "entitlements_w_no_users": "int",
      "entitlements_w_one_user": "int",
      "entitlements_w_zero_to_five_users": "int",
      "entitlements_w_five_to_ten_users": "int",
      "entitlements_w_ten_to_hundred_users": "int",
      "entitlements_w_hundred_to_onek_user": "int",
      "entitlements_w_onek_to_tenk_users": "int",
      "entitlements_w_tenk_users": "int",
      "entitlements_w_hundredk_users": "int"
    },
    "key": [
      "key"
    ],
    "table_name": "company_view_overview"
  }
}
```

Example Request

```
curl --location --request PUT '/config/CompanyViewOverviewConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "CompanyViewOverview",
  "modelDefinition": {
    "fields": {
      "key": "text",
      "total_employees": "int",
      "employees_wo_manager": "int",
      "employees_w_manager": "int",
      "entitlements_without_roleowners": "int",
      "entitlements_with_roleowners": "int",
      "total_entitlements": "int",
      "entitlements_covered_by_model": "int",
      "entitlements_not_covered": "int",
      "entitlements_w_no_users": "int",
      "entitlements_w_one_user": "int",
      "entitlements_w_zero_to_five_users": "int",
      "entitlements_w_five_to_ten_users": "int",
      "entitlements_w_ten_to_hundred_users": "int",
      "entitlements_w_hundred_to_onek_user": "int",
      "entitlements_w_onek_to_tenk_users": "int",
      "entitlements_w_tenk_users": "int",
      "entitlements_w_hundredk_users": "int"
    },
    "key": [
      "key"
    ],
    "table_name": "company_view_overview"
  }
}'
```

* PUT CompanyViewEmployeeTypeConf

  \>Sets the schema definition for the related database table {{company\_view\_employeetype}}.

Endpoint

```
/config/CompanyViewEmployeeTypeConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "CompanyViewEmployeeType",
  "modelDefinition": {
    "fields": {
      "type": "text",
      "high": "int",
      "medium": "int",
      "low": "int",
      "null_conf": "int",
      "total": "int"
    },
    "key": [
      "type"
    ],
    "table_name": "company_view_employee_type"
  }
}
```

Example Request

```
curl --location --request PUT '/config/CompanyViewEmployeeTypeConf' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "CompanyViewEmployeeType",
  "modelDefinition": {
    "fields": {
      "type": "text",
      "high": "int",
      "medium": "int",
      "low": "int",
      "null_conf": "int",
      "total": "int"
    },
    "key": [
      "type"
    ],
    "table_name": "company_view_employee_type"
  }
}'
```

* PUT EntitlementAverageConfScoreConf

  Sets the schema definition for the related database table {{entitlement\_average\_conf\_score}}.

Endpoint

```
/config/EntitlementAverageConfScoreConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "EntitlementAverageConfScore",
	"modelDefinition": {
	   "fields": {
	      "org": "text",
	      "avg_score": "float",
	      "entitlement": "text"
	   },
	   "key": [
	      "org"
	   ],
	   "table_name": "entitlement_average_conf_score"
	}
}
```

Example Request

```
curl --location --request PUT '/config/EntitlementAverageConfScoreConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "EntitlementAverageConfScore",
	"modelDefinition": {
	   "fields": {
	      "org": "text",
	      "avg_score": "float",
	      "entitlement": "text"
	   },
	   "key": [
	      "org"
	   ],
	   "table_name": "entitlement_average_conf_score"
	}
}'
```

* PUT EntitlementUserScoresConf

  Sets the schema definition for the related database table {{entitlement\_user\_scores}}.

Endpoint

```
/config/EntitlementUserScoresConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
    "name": "EntitlementUserScores",
    "modelDefinition": {
      "fields": {
        "entitlement": "text",
        "entitlement_name": "text",
        "user": "text",
        "user_name": "text",
        "score": "float",
        "justification": {
          "type": "list",
          "typeDef": "<text>"
        },
        "app_id": "text",
        "app_name": "text"
      },
      "key": ["entitlement"],
      "table_name": "entitlement_user_scores"
    }
}
```

Example Request

```
curl --location --request PUT '/config/EntitlementUserScoresConf' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "EntitlementUserScores",
    "modelDefinition": {
      "fields": {
        "entitlement": "text",
        "entitlement_name": "text",
        "user": "text",
        "user_name": "text",
        "score": "float",
        "justification": {
          "type": "list",
          "typeDef": "<text>"
        },
        "app_id": "text",
        "app_name": "text"
      },
      "key": ["entitlement"],
      "table_name": "entitlement_user_scores"
    }
  }'
```

* PUT GraphByRoleConf

  Sets the schema definition for the related database table {{graph\_by\_role}}.

Endpoint

```
/config/GraphByRoleConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
    "name": "GraphByRole",
    "modelDefinition": {
      "fields": {
        "role": "text",
        "entitlement": "text",
        "entitlement_name": "text",
        "app_id": "text",
        "app_name": "text",
        "high_risk": "text"
      },
      "key": ["role"],
      "table_name": "graph_by_role"
    }
}
```

Example Request

```
curl --location --request PUT '/config/GraphByRoleConf' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "GraphByRole",
    "modelDefinition": {
      "fields": {
        "role": "text",
        "entitlement": "text",
        "entitlement_name": "text",
        "app_id": "text",
        "app_name": "text",
        "high_risk": "text"
      },
      "key": ["role"],
      "table_name": "graph_by_role"
    }
  }'
```

* PUT GraphConf

  Sets the schema definition for the related database table {{graph}}.

Endpoint

```
/config/GraphConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
    "name": "Graph",
    "modelDefinition": {
      "fields": {
        "manager": "text",
        "user": "text",
        "manager_name": "text",
        "user_name": "text"
      },
      "key": ["manager"],
      "table_name": "graph_by_manager"
    }
  }
```

Example Request

```
curl --location --request PUT '/config/GraphConf' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Graph",
    "modelDefinition": {
      "fields": {
        "manager": "text",
        "user": "text",
        "manager_name": "text",
        "user_name": "text"
      },
      "key": ["manager"],
      "table_name": "graph_by_manager"
    }
  }'
```

* PUT ManagerConf

  Set manager data.

Endpoint

```
/config/ManagerConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "Manager",
  "modelDefinition": {
    "fields": {
      "org": "text",
      "manager": "int"
    },
    "key": [
      "manager"
   ],
    "table_name": "managers_by_org"
  }
}
```

Example Request

```
curl --location --request PUT '/config/ManagerConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "Manager",
  "modelDefinition": {
    "fields": {
      "org": "text",
      "manager": "int"
    },
    "key": [
      "manager"
    ],
    "table_name": "managers_by_org"
  }
}'
```

* PUT RoleOwnerConf

  Sets the schema definition for the related database table {{role\_owner}}.

Endpoint

```
/config/RoleOwnerConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
    "name": "RoleOwner",
    "modelDefinition": {
      "fields": {
        "role": "text",
        "role_name": "text",
        "entitlement": "text",
        "entitlement_name": "text",
        "user": "text",
        "user_name": "text",
        "score": "float",
        "justification": {
          "type": "list",
          "typeDef": "<text>"
        },
        "app_id": "text",
        "app_name": "text",
        "high_risk": "text"
      },
      "key": ["role"],
      "table_name": "usr_scores_by_role"
    }
}
```

Example Request

```
curl --location --request PUT '/config/RoleOwnerConf' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "RoleOwner",
    "modelDefinition": {
      "fields": {
        "role": "text",
        "role_name": "text",
        "entitlement": "text",
        "entitlement_name": "text",
        "user": "text",
        "user_name": "text",
        "score": "float",
        "justification": {
          "type": "list",
          "typeDef": "<text>"
        },
        "app_id": "text",
        "app_name": "text",
        "high_risk": "text"
      },
      "key": ["role"],
      "table_name": "usr_scores_by_role"
    }
  }'
```

* PUT RoleOwnerWithAppConf

  Set role owner with application.

Endpoint

```
/config/RoleOwnerWithAppConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "RoleOwnerWithApp",
  "modelDefinition": {
    "fields": {
      "role": "text",
      "role_name": "text",
      "entitlement": "text",
      "entitlement_name": "text",
      "user": "text",
      "user_name": "text",
      "score": "float",
      "justification": {
         "type": "list",
         "typeDef": "<text>"
      },
      "app_id": "text",
      "app_name": "text"
    },
    "key": [
      "role"
    ],
    "table_name": "usr_scores_by_role_with_app"
  }
}
```

Example Request

```
curl --location --request PUT '/config/RoleOwnerWithAppConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "RoleOwnerWithApp",
  "modelDefinition": {
    "fields": {
      "role": "text",
      "role_name": "text",
      "entitlement": "text",
      "entitlement_name": "text",
      "user": "text",
      "user_name": "text",
      "score": "float",
      "justification": {
         "type": "list",
         "typeDef": "<text>"
      },
      "app_id": "text",
      "app_name": "text"
    },
    "key": [
      "role"
    ],
    "table_name": "usr_scores_by_role_with_app"
  }
}'
```

* PUT UserConf

  Sets the schema definition for the related database table {{user}}.

Endpoint

```
/config/UserConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
    "name": "User",
    "modelDefinition": {
      "fields": {
        "user": "text",
        "manager": "text",
        "department": "text",
        "empType": "text",
        "udfChief": "text",
        "udfCostCenter": "text",
        "jobCode": "text",
        "buildingCode": "text",
        "lob": "text",
        "lobSubgroup": "text",
        "userName": "text",
        "managerName": "text",
        "departmentDescription": "text",
        "jobDescription": "text"
      },
      "key": ["user"],
      "table_name": "user"
    }
}
```

Example Request

```
curl --location --request PUT '/config/UserConf' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "User",
    "modelDefinition": {
      "fields": {
        "user": "text",
        "manager": "text",
        "department": "text",
        "empType": "text",
        "udfChief": "text",
        "udfCostCenter": "text",
        "jobCode": "text",
        "buildingCode": "text",
        "lob": "text",
        "lobSubgroup": "text",
        "userName": "text",
        "managerName": "text",
        "departmentDescription": "text",
        "jobDescription": "text"
      },
      "key": ["user"],
      "table_name": "user"
    }
}'
```

* PUT UserScoreConf

  Sets the schema definition for the related database table {{user\_score}}.

Endpoint

```
/config/UserScoreConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
    "name": "UserScore",
    "modelDefinition": {
      "fields": {
        "manager": "text",
        "user": "text",
        "manager_name": "text",
        "user_name": "text",
        "score": "float",
        "entitlement": "text",
        "entitlement_name": "text",
        "justification": {
          "type": "list",
          "typeDef": "<text>"
        },
        "app_id": "text",
        "app_name": "text",
        "high_risk": "text"
      },
      "key": ["manager"],
      "table_name": "usr_scores_by_manager"
    }
}
```

Example Request

```
curl --location --request PUT '/config/UserScoreConf' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "UserScore",
    "modelDefinition": {
      "fields": {
        "manager": "text",
        "user": "text",
        "manager_name": "text",
        "user_name": "text",
        "score": "float",
        "entitlement": "text",
        "entitlement_name": "text",
        "justification": {
          "type": "list",
          "typeDef": "<text>"
        },
        "app_id": "text",
        "app_name": "text",
        "high_risk": "text"
      },
      "key": ["manager"],
      "table_name": "usr_scores_by_manager"
    }
  }'
```

* PUT FilteringOptionsModelConf

  Sets the schema definition for the related database table {{filtering\_options\_model}}.

Endpoint

```
/config/FilteringOptionsModelConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "FilteringOptions",
	"modelDefinition": {
	    "fields":{
	        "type": "int",
	        "owner_id"    : "text",
	        "group" : "text",
	        "id" : "text",
	        "name"     : "text",
	        "user_ids": {
		         "type": "list",
		         "typeDef": "<text>"
		      }
	      },
	      "key": ["type"],
	      "table_name": "filtering_options"
	}
}
```

Example Request

```
curl --location --request PUT '/config/FilteringOptionsModelConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "FilteringOptions",
	"modelDefinition": {
	    "fields":{
	        "type": "int",
	        "owner_id"    : "text",
	        "group" : "text",
	        "id" : "text",
	        "name"     : "text",
	        "user_ids": {
		         "type": "list",
		         "typeDef": "<text>"
		      }
	      },
	      "key": ["type"],
	      "table_name": "filtering_options"
	}
}'
```

* PUT CompanyViewMostCriticalEnttConf

  Sets the schema definition for the related database table {{company\_view\_most\_critical\_entt}}.

Endpoint

```
/config/CompanyViewMostCriticalEnttConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"name": "CompanyViewMostCriticalEntt",
	"modelDefinition": {
	  "fields":{
	      "org": "text",
        "entt_id"    : "text",
        "entt_name" : "text",
	      "high" : "int",
	      "medium" : "int",
	      "seq" : "int",
        "low": "int",
        "total_employees" : "int",
	      "avg_conf_score": "float"
	  },
	  "key": ["org"],
	  "table_name": "company_view_most_critical_entt"
	}
}
```

Example Request

```
curl --location --request PUT '/config/CompanyViewMostCriticalEnttConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "CompanyViewMostCriticalEntt",
	"modelDefinition": {
	   "fields":{
	      "org": "text",
	      "entt_id"    : "text",
	      "entt_name" : "text",
	      "high" : "int",
        "medium" : "int",
        "seq" : "int",
	      "low": "int",
	      "total_employees" : "int",
	      "avg_conf_score": "float"
     },
	   "key": ["org"],
	   "table_name": "company_view_most_critical_entt"
	}
}'
```

* PUT FilteringOptionsConf

  Set the filtering options.

Endpoint

```
/config/FilteringOptionsConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
      "filteringOptions": [
        {
            "type": "user",
            "groupName": "STATE",
            "title": "State"
        },
        {
            "type": "user",
            "groupName": "DEPARTMENT",
            "title": "Department"
        }
      ]
}
```

Example Request

```
curl --location --request PUT '/config/FilteringOptionsConf' \
--header 'Content-Type: application/json' \
--data-raw '{
      "filteringOptions": [
        {
            "type": "user",
            "groupName": "STATE",
            "title": "State"
        },
        {
            "type": "user",
            "groupName": "DEPARTMENT",
            "title": "Department"
        }
      ]
  }'
```

* PUT OrgNameConf

  Set the organization name.

Endpoint

```
/config/OrgNameConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"orgName": "abc"
}
```

Example Request

```
curl --location --request PUT '/config/OrgNameConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"orgName": "abc"
}'
```

* PUT ConfidenceScorethresholdsConf

  Set the confidence score thresholds.

Endpoint

```
/config/ConfidenceScorethresholdsConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
	"thresholds": {
	  "top": 1.01,
	  "high": 0.75,
	  "medium": 0.35,
	  "low": 0
	}
}
```

Example Request

```
curl --location --request PUT '/config/ConfidenceScoreThresholdsConf' \
--header 'Content-Type: application/json' \
--data-raw '{
	"thresholds": {
	  "top": 1.01,
	  "high": 0.75,
	  "medium": 0.35,
	  "low": 0
	}
}'
```

* PUT UIHRData

  Set the UI HR data.

Endpoint

```
/config/UIHRData
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
  "user": "User",
  "manager": "Manager",
  "emptype": " Employee Type",
  "buildingcode": "Building Code",
  "department": "Department Code",
  "departmentdescription": "Department Description",
  "jobcode": "Job code",
  "jobdescription": "Job Code Description",
  "lob": "Line Of Business",
  "lobsubgroup": "Line Of Business SubGroup",
  "managername": "Manager Name",
  "udfchief": "UDF Chief",
  "udfcostcenter": "UDF Cost Center",
  "username": "User Name"
}
```

Example Request

```
curl --location --request PUT '/config/UIHRData' \
--header 'Content-Type: application/json' \
--data-raw '{
  "user": "User",
  "manager": "Manager",
  "emptype": " Employee Type",
  "buildingcode": "Building Code",
  "department": "Department Code",
  "departmentdescription": "Department Description",
  "jobcode": "Job code",
  "jobdescription": "Job Code Description",
  "lob": "Line Of Business",
  "lobsubgroup": "Line Of Business SubGroup",
  "managername": "Manager Name",
  "udfchief": "UDF Chief",
  "udfcostcenter": "UDF Cost Center",
  "username": "User Name"
}'
```

* PUT UIJustifications

  Set the UI justifications.

Endpoint

```
/config/UIJustifications
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
  "USR_MANAGER_KEY": "Supervisor",
  "USR_DEPT_NO": "Department No",
  "USR_EMP_TYPE": "Employee Type",
  "USR_UDF_CHIEF": " UDF Chief",
  "USR_UDF_COST_CENTER": "UDF Cost Center",
  "USR_UDF_JOBCODE": "Job Code",
  "USR_UDF_BUILDINGCODE": "Building Code",
  "USR_UDF_LOB": "Line Of Business",
  "USR_UDF_LOBSUBGROUP": "Line of Business Subgroup"
}
```

Example Request

```
curl --location --request PUT '/config/UIJustifications' \
--header 'Content-Type: application/json' \
--data-raw '{
  "USR_MANAGER_KEY": "Supervisor",
  "USR_DEPT_NO": "Department No",
  "USR_EMP_TYPE": "Employee Type",
  "USR_UDF_CHIEF": " UDF Chief",
  "USR_UDF_COST_CENTER": "UDF Cost Center",
  "USR_UDF_JOBCODE": "Job Code",
  "USR_UDF_BUILDINGCODE": "Building Code",
  "USR_UDF_LOB": "Line Of Business",
  "USR_UDF_LOBSUBGROUP": "Line of Business Subgroup"
}'
```

* PUT HighRiskConf

  Set the high risk filter value.

Endpoint

```
/config/HighRiskConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
  "filterValue": "1"
}
```

Example Request

```
curl --location --request PUT '/config/HighRiskConf' \
--header 'Content-Type: application/json' \
--data-raw '{
  "filterValue": "1"
}'
```

* PUT JustificationDelimiter

  Set the justification delimiter to separate the different justifications in the string saved in Cassandra. For .csv files, the delimiter is a comma ( , ).

Endpoint

```
/config/JustificationDelimiter
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
    "justificationDelimeter": "_"
}
```

Example Request

```
curl --location --request PUT '/config/JustificationDelimeter' \
--header 'Content-Type: application/json' \
--data-raw '{
    "justificationDelimeter": "_"
  }'
```

* PUT PermissionsConf

  Set the permissions.

Endpoint

```
/config/PermissionsConf
```

Authorization

```
<Bearer Token JWT-value>
```

Headers

```
Content-Type      application/json
```

Body

```
{
  "actions": [
    "CERTIFYENTITLEMENTS_TO_USERS",
    "CERTIFYUSERS_TO_ENTITLEMENTS",
    "FILTERENTITLEMENTS",
    "REVOKECERTIFY_ACCESS",
    "SEARCHUSER",
    "SEARCHUSER_ENTITLEMENTS",
    "SEARCHSUPERVISOR_USER_ENTITLEMENTS",
    "SHOWASSIGNMENTS_STATS",
    "SHOWCOMPANY_PAGE",
    "SHOWCOMPANY_COVERAGE_DATA",
    "SHOWCOMPANY_ENTITLEMENTS_DATA",
    "SHOWCOMPANY_EMPLOYEE_PAGE",
    "SHOWCRITICAL_ENTITLEMENTS",
    "SHOWEMPLOYEE",
    "SHOWENTITLEMENT",
    "SHOWENTITLEMENT_AVG_GROUPS",
    "SHOWENTITLEMENT_AVG_GROUP_DETAILS",
    "SHOWENTITLEMENT_USERS",
    "SHOWFILTER_OPTIONS",
    "SHOWROLE_OWNER_PAGE",
    "SHOWROLE_OWNER_USER_DATA",
    "SHOWROLE_OWNER_ENT_DATA",
    "SHOWROLE_OWNER_AUTO_DATA",
    "SHOWSUPERVISOR_PAGE",
    "SHOWSUPERVISOR_DETAILS_PAGE",
    "SHOWSUPERVISOR_ENT_DATA",
    "SHOWSUPERVISOR_USER_DATA",
    "SHOWSUPERVISOR_ENTITLEMENT_USERS",
    "SHOWSUPERVISOR_USER_ENTITLEMENTS",
    "SHOWROLEOWNER_UNSCORED_ENTITLEMENTS",
    "SHOWSUPERVISOR_UNSCORED_ENTITLEMENTS",
    "SHOWUNSCORED_ENTITLEMENTS",
    "SHOWUSER",
    "SHOWALL_ROLE_OWNER_DATA"
  ],
  "permissions": {
    "Zoran Admin": {
      "can": "*"
    },
    "Zoran Entitlement Owner": {
      "can": [
        "FILTERENTITLEMENTS",
        "SEARCHUSER_ENTITLEMENTS",
        "SHOWENTITLEMENT",
        "SHOWENTITLEMENT_USERS",
        "SHOWFILTER_OPTIONS",
        "SHOWROLEOWNER_UNSCORED_ENTITLEMENTS",
        "SHOWROLE_OWNER_PAGE",
        "SHOWROLE_OWNER_ENT_DATA",
        "SHOWROLE_OWNER_AUTO_DATA",
        "SHOWROLE_OWNER_USER_PAGE",
        "SHOWROLE_OWNER_ENT_PAGE",
        "SHOWUSER_ENTITLEMENTS",
        "SHOWUNSCORED_ENTITLEMENTS",
        "CERTIFYENTITLEMENTS_TO_USERS",
        "CERTIFYUSERS_TO_ENTITLEMENTS",
        "REVOKECERTIFY_ACCESS"
      ]
    },
    "Zoran Executive": {
      "can": [
        "SHOWASSIGNMENTS_STATS",
        "SHOWCOMPANY_PAGE",
        "SHOWCOMPANY_COVERAGE_PAGE",
        "SHOWCOMPANY_ENTITLEMENTS_PAGE",
        "SHOWCOMPANY_EMPLOYEE_PAGE",
        "SHOWCRITICAL_ENTITLEMENTS",
        "SHOWENTITLEMENT_AVG_GROUPS",
        "SHOWENTITLEMENT_AVG_GROUP_DETAILS",
        "SHOWUSER_ENTITLEMENTS"
      ]
    },
    "Zoran Supervisor": {
      "can": [
        "FILTERENTITLEMENTS",
        "SHOWEMPLOYEE",
        "SHOWFILTER_OPTIONS",
        "SHOWSUPERVISOR_PAGE",
        "SHOWSUPERVISOR_DETAILS_PAGE",
        "SHOWSUPERVISOR_ENT_DATA",
        "SHOWSUPERVISOR_USER_DATA",
        "SHOWSUPERVISOR_ENTITLEMENT_USERS",
        "SHOWSUPERVISOR_USER_ENTITLEMENTS",
        "SEARCHSUPERVISOR_USER_ENTITLEMENTS",
        "SHOWSUPERVISOR_UNSCORED_ENTITLEMENTS",
        "CERTIFYENTITLEMENTS_TO_USERS",
        "CERTIFYUSERS_TO_ENTITLEMENTS",
        "REVOKECERTIFY_ACCESS"
      ]
    },
    "Zoran User": {
      "can": [
        "SHOWCERTIFICATIONS",
        "SEARCHUSER",
        "SHOWENTITLEMENT",
        "SHOW__USER"
      ]
    }
  }
}
```

Example Request

```
curl --location --request PUT '/config/PermissionsConf' \
--header 'Content-Type: application/json' \
--data-raw '{"actions":["CERTIFYENTITLEMENTS_TO_USERS"
  ,"CERTIFYUSERS_TO_ENTITLEMENTS","FILTERENTITLEMENTS"
  ,"REVOKECERTIFY_ACCESS","SEARCHUSER","SEARCHUSER_ENTITLEMENTS"
  ,"SEARCHSUPERVISOR_USER_ENTITLEMENTS","SHOWASSIGNMENTS_STATS"
  ,"SHOW_COMPANY_PAGE","SHOWCOMPANY_COVERAGE_DATA"
  ,"SHOW_COMPANY_ENTITLEMENTS_DATA","SHOWCOMPANY_EMPLOYEE_PAGE"
  ,"SHOW_CRITICAL_ENTITLEMENTS","SHOWEMPLOYEE","SHOWENTITLEMENT"
  ,"SHOW_ENTITLEMENT_AVG_GROUPS","SHOWENTITLEMENT_AVG_GROUP_DETAILS"
  ,"SHOW_ENTITLEMENT_USERS","SHOWFILTER_OPTIONS","SHOWROLE_OWNER_PAGE"
  ,"SHOW_ROLE_OWNER_USER_DATA","SHOWROLE_OWNER_ENT_DATA"
  ,"SHOW_ROLE_OWNER_AUTO_DATA","SHOWSUPERVISOR_PAGE"
  ,"SHOW_SUPERVISOR_DETAILS_PAGE","SHOWSUPERVISOR_ENT_DATA"
  ,"SHOW_SUPERVISOR_USER_DATA","SHOWSUPERVISOR_ENTITLEMENT_USERS"
  ,"SHOW_SUPERVISOR_USER_ENTITLEMENTS","SHOW_ROLEOWNER_UNSCORED_ENTITLEMENTS"
  ,"SHOW_SUPERVISOR_UNSCORED_ENTITLEMENTS","SHOW_UNSCORED_ENTITLEMENTS"
  ,"SHOWUSER","SHOWALL_ROLE_OWNER_DATA"]
  ,"permissions"
  :{"Zoran Admin":{"can":"*"},"Zoran Entitlement Owner"
  :{"can":["FILTERENTITLEMENTS","SEARCHUSER_ENTITLEMENTS"
  ,"SHOWENTITLEMENT","SHOWENTITLEMENT_USERS","SHOWFILTER_OPTIONS"
  ,"SHOWROLEOWNER_UNSCORED_ENTITLEMENTS","SHOWROLE_OWNER_PAGE"
  ,"SHOWROLE_OWNER_ENT_DATA","SHOWROLE_OWNER_AUTO_DATA"
  ,"SHOWROLE_OWNER_USER_PAGE","SHOWROLE_OWNER_ENT_PAGE"
  ,"SHOWUSER_ENTITLEMENTS","SHOWUNSCORED_ENTITLEMENTS"
  ,"CERTIFYENTITLEMENTS_TO_USERS","CERTIFYUSERS_TO_ENTITLEMENTS"
  ,"REVOKECERTIFY_ACCESS"]},"Zoran Executive"
  :{"can":["SHOWASSIGNMENTS_STATS","SHOWCOMPANY_PAGE"
  ,"SHOWCOMPANY_COVERAGE_PAGE","SHOWCOMPANY_ENTITLEMENTS_PAGE"
  ,"SHOWCOMPANY_EMPLOYEE_PAGE","SHOWCRITICAL_ENTITLEMENTS"
  ,"SHOWENTITLEMENT_AVG_GROUPS","SHOWENTITLEMENT_AVG_GROUP_DETAILS"
  ,"SHOWUSER_ENTITLEMENTS"]},"Zoran Supervisor"
  :{"can":["FILTERENTITLEMENTS","SHOWEMPLOYEE","SHOWFILTER_OPTIONS"
  ,"SHOWSUPERVISOR_PAGE","SHOWSUPERVISOR_DETAILS_PAGE"
  ,"SHOWSUPERVISOR_ENT_DATA","SHOWSUPERVISOR_USER_DATA"
  ,"SHOWSUPERVISOR_ENTITLEMENT_USERS","SHOWSUPERVISOR_USER_ENTITLEMENTS"
  ,"SEARCHSUPERVISOR_USER_ENTITLEMENTS","SHOWSUPERVISOR_UNSCORED_ENTITLEMENTS"
  ,"CERTIFYENTITLEMENTS_TO_USERS","CERTIFYUSERS_TO_ENTITLEMENTS"
  ,"REVOKECERTIFY_ACCESS"]},"Zoran User"
  :{"can":["SHOWCERTIFICATIONS","SEARCHUSER","SHOWENTITLEMENT"
  ,"SHOWUSER"]}
  }
}'
```

---

---
title: Data Sink
description: Data sink is the downstream consumer of data within Ping Autonomous Identity for service connectors and is accessible through API endpoints.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-datasink-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-datasink-api.html
section_ids:
  datasink-create: POST /api/datasink/create
  datasink-update: POST /api/datasink/update
  datasink-delete: POST /api/datasink/delete
  datasink-update-status-assignments: POST /api/datasink/update/status/assignments
  datasink-update-status-rules: POST /api/datasink/update/status/rules
  datasink-update-status-roles: POST /api/datasink/update/status/roles
  datasink-query: POST /api/datasink/query
  datasink-update-timestamp: POST /api/datasink/update/timestamp
  datasink-query-logs: POST /api/datasink/query/logs
  datasink-update-logs: POST /api/datasink/update/logs
---

# Data Sink

Data sink is the downstream consumer of data within Ping Autonomous Identity for service connectors and is accessible through API endpoints.

> **Collapse: See a conceptual image of Data Sink**
>
> ![Data Sink](_images/datasink.png)

The following are Ping Autonomous Identity datasink endpoints:

## POST /api/datasink/create

* POST /api/datasink/create

  Create a new /common/datasink entity.

  Endpoint

  ```
  /api/datasink/create
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  **JSON Body Parameters**

  | Parameter            | Type   | Description                                                                    |
  | -------------------- | ------ | ------------------------------------------------------------------------------ |
  | id                   | string | Data sink ID (format: UUID) (required)                                         |
  | name                 | string | Data sink name (required)                                                      |
  | config               | object | Free form client-defined connection object                                     |
  | autoCertifyTimestamp | string | Last auto-certification operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ) |
  | autoRequestTimestamp | string | Last auto-request operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)       |
  | certifyTimestamp     | string | Last certification operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)      |
  | revokeTimestamp      | string | Last revoke operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)             |
  | rolePublishTimestamp | string | Last role publish timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)                 |
  | logs                 | object | Free form client-defined log object                                            |

  Example Request

  ```
  curl -k -X POST https://autoid-ui.forgerock.com/api/datasink/create' \
  -H 'Authorization: Bearer <token value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "eaa19702-3806-4ee7-9466-91f0968699d9",
    "name": "Test",
    "config": { "something": 1234 }
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": "ok"
  }
  ```

## POST /api/datasink/update

* POST /api/datasink/update

  Update a /common/datasink entity.

  Endpoint

  ```
  /api/datasink/update
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  **JSON Body Parameters**

  | Parameter            | Type   | Description                                                                    |
  | -------------------- | ------ | ------------------------------------------------------------------------------ |
  | id                   | string | Data sink ID (format: UUID) (required)                                         |
  | name                 | string | Data sink name (required)                                                      |
  | config               | object | Free form client-defined connection object                                     |
  | autoCertifyTimestamp | string | Last auto-certification operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ) |
  | autoRequestTimestamp | string | Last auto-request operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)       |
  | certifyTimestamp     | string | Last certification operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)      |
  | revokeTimestamp      | string | Last revoke operation timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)             |
  | rolePublishTimestamp | string | Last role publish timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ)                 |
  | logs                 | object | Free form client-defined log object                                            |

  Example Request

  ```
  curl -k -X POST https://autoid-ui.forgerock.com/api/datasink/update' \
  -H 'Authorization: Bearer <token value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "eaa19702-3806-4ee7-9466-91f0968699d9",
    "name": "Test3",
    "config": { "something": 5678 }
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": ok
  }
  ```

## POST /api/datasink/delete

* POST /api/datasink/delete

  Remove a /common/datasink entity.

  Endpoint

  ```
  /api/datasink/delete
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  **JSON Body Parameters**

  | Parameter | Type   | Description                            |
  | --------- | ------ | -------------------------------------- |
  | id        | string | Data sink ID (format: UUID) (required) |

  Example Request

  ```
  curl -k -X POST https://autoid-ui.forgerock.com/api/datasink/delete' \
  -H 'Authorization: Bearer <token value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "eaa19702-3806-4ee7-9466-91f0968699d9"
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": ok
  }
  ```

## POST /api/datasink/update/status/assignments

* POST /api/datasink/update/status/assignments

  Update data sink status for assignment decisions. Decisions are stored in the /autoid/api/user\_access\_decisions JAS entity and *entitlement-assignment* Elasticsearch index.

  Endpoint

  ```
  /api/datasink/update/status/assignments
  ```

  Authorization

  ```
  <API Key>
  ```

  **JSON Body Parameters**

  | Parameter   | Type  | Description                                               |
  | ----------- | ----- | --------------------------------------------------------- |
  | assignments | array | Array of assignment objects (properties below) (required) |

  **Base Assignment Object Properties**

  | Parameter        | Type         | Description                         |
  | ---------------- | ------------ | ----------------------------------- |
  | user             | string       | User ID (required)                  |
  | entitlements     | string array | Array of entitlement IDs (required) |
  | datasink\_status | string       | Updated data sink status (required) |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/datasink/update/status/assignments \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "assignments": [
      {
        "user": "john.doe",
        "entitlements": [
          "entitlement_1"
        ],
        "datasink_status": "ack"
      },
      {
        "user": "jane.smith",
        "entitlements": [
          "entitlement_1",
          "entitlement_2",
        ],
        "datasink_status": "nack"
      }
    ]
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": ok
  }
  ```

## POST /api/datasink/update/status/rules

* POST /api/datasink/update/status/rules

  Update data sink status for rule decisions. Decisions are stored in the /autoid/api/rule\_access\_decisions JAS entity and *entitlement-assignment* Elasticsearch index.

  Endpoint

  ```
  /api/datasink/update/status/rules
  ```

  Authorization

  ```
  <API Key>
  ```

  **JSON Body Parameters**

  | Parameter | Type  | Description                                         |
  | --------- | ----- | --------------------------------------------------- |
  | rules     | array | Array of rule objects (properties below) (required) |

  **Base Rules Object Properties**

  | Parameter        | Type         | Description                         |
  | ---------------- | ------------ | ----------------------------------- |
  | entitlement      | string       | Entitlement ID (required)           |
  | justification    | string array | Array of justifications (required)  |
  | datasink\_status | string       | Updated data sink status (required) |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/datasink/update/status/rules \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "rules": [
      {
        "entitlement": "entitlement_1",
        "justification": [
          "0B_COST_CENTER_OP_TS5",
          "0C_USR_EMP_TYPE_Non-Employee",
          "10_LINE_OF_BUSINESS_Health and Safety",
          "13_USR_DEPARTMENT_NAME_Testing"
        ],
        "datasink_status": "nack"
      }
    ]
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": ok
  }
  ```

## POST /api/datasink/update/status/roles

* POST /api/datasink/update/status/roles

  Update data sink status for exported roles.

  Endpoint

  ```
  /api/datasink/update/status/roles
  ```

  Authorization

  ```
  <API Key>
  ```

  **JSON Body Parameters**

  | Parameter | Type  | Description                                         |
  | --------- | ----- | --------------------------------------------------- |
  | roles     | array | Array of role objects (properties below) (required) |

  **Base Roles Object Properties**

  | Parameter        | Type   | Description                                       |
  | ---------------- | ------ | ------------------------------------------------- |
  | role\_id         | string | Role ID (required)                                |
  | status           | string | Role status (draft, candidate, active) (required) |
  | datasink\_status | string | Updated data sink status (required)               |

  Example Request

  ```
  curl -k -X POST \
  /https://autoid-ui.forgerock.com/api/datasink/update/status/roles \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "roles": [
      {
        "role_id": "027d9a1d-9a2f-488a-8ab2-adf404e0aecb",
        "status": "draft",
        "datasink_status": "nack"
      }
    ]
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": ok
  }
  ```

## POST /api/datasink/query

* POST /api/datasink/query

  Query data sink entities. Optional filtering can be applied as a JSON request body outlined below.

  Endpoint

  ```
  /api/datasink/query
  ```

  Authorization

  ```
  <API Key>
  ```

  **JSON Body Parameters**

  | Parameter            | Type   | Description                                                                      |
  | -------------------- | ------ | -------------------------------------------------------------------------------- |
  | id                   | string | Data sink ID (format: UUID)                                                      |
  | name                 | string | Data sink name                                                                   |
  | autoCertifyTimestamp | object | Last auto-certify operation timestamp filter object (available properties below) |
  | autoRequestTimestamp | object | Last auto-request operation timestamp filter object (available properties below) |
  | certifyTimestamp     | object | Last certify operation timestamp filter object (available properties below)      |
  | revokeTimestamp      | object | Last revoke operation timestamp filter object (available properties below)       |
  | rolePublishTimestamp | object | Last role publish timestamp filter object (available properties below)           |

  **timestampThresholds Object Properties**

  | Parameter | Type   | Description                                                                                        |
  | --------- | ------ | -------------------------------------------------------------------------------------------------- |
  | gt        | string | Greater than timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **gte**.         |
  | gte       | string | Greater than or equal timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **gt**. |
  | lt        | string | Less than timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **lte**.            |
  | lte       | string | Less than or equal timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **le**.    |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/datasink/query \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "IIQ",
    "certifyTimestamp": {
      "gt": "2021-11-19T10:01:19.937Z",
      "lte": "2021-11-20T10:01:19.937Z"
    }
  }'
  ```

  Example Response (Success)

  ```
  [
    {
      "id": "b72c15b7-7dcb-44ac-b1d3-162565e360b4",
      "name": "IIQ",
      "certifyTimestamp": "2021-11-19T11:01:19.937Z",
      "auto_request_timestamp": "2021-10-01T10:01:19.937Z"
    },
    {
      "id": "9501810e-1480-4f41-80d4-bc97154fddeb",
      "name": "IIQ",
      "certifyTimestamp": "2021-11-20T09:01:19.937Z",
      "auto_request_timestamp": "2021-10-01T10:01:19.937Z"
    }
  ]
  ```

## POST /api/datasink/update/timestamp

* POST /api/datasink/update/timestamp

  Update timestamps for a data sink entity.

  Endpoint

  ```
  /api/datasink/update/timestamp
  ```

  Authorization

  ```
  <API Key>
  ```

  **JSON Body Parameters**

  | Parameter            | Type   | Description                                                                            |
  | -------------------- | ------ | -------------------------------------------------------------------------------------- |
  | id                   | string | Data sink ID (format: UUID)                                                            |
  | autoCertifyTimestamp | object | Last auto-certify operation timestamp filter object (format: yyyy-mm-ddThh:mm:ss.SSSZ) |
  | autoRequestTimestamp | object | Last auto-request operation timestamp filter object (format: yyyy-mm-ddThh:mm:ss.SSSZ) |
  | certifyTimestamp     | object | Last certify operation timestamp filter object (format: yyyy-mm-ddThh:mm:ss.SSSZ)      |
  | revokeTimestamp      | object | Last revoke operation timestamp filter object (format: yyyy-mm-ddThh:mm:ss.SSSZ)       |
  | rolePublishTimestamp | object | Last role publish timestamp filter object (format: yyyy-mm-ddThh:mm:ss.SSSZ)           |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/datasink/update/timestamp \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d ' {
    "id": "87e341c0-c1aa-4b0e-9ae5-1384bb6de8fc",
    "certifyTimestamp": "2021-11-19T10:01:19.937Z",
    "revokeTimestamp": "2021-11-19T10:01:19.937Z"
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": "ok"
  }
  ```

## POST /api/datasink/query/logs

* POST /api/datasink/query/logs

  Query data sink logs. Optional filtering can be applied as a JSON request body outlined below.

  Endpoint

  ```
  /api/datasink/query/logs
  ```

  Authorization

  ```
  <API Key>
  ```

  **JSON Body Parameters**

  | Parameter | Type   | Description                 |
  | --------- | ------ | --------------------------- |
  | id        | string | Data sink ID (format: UUID) |
  | name      | string | Data sink name              |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/datasink/query/logs \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "IIQ"
  }'
  ```

  Example Response (Success)

  ```
  [
    {
      "id": "5f8c48c5-8f70-43a0-a9a6-61d1b017dac7",
      "name": "IIQ",
      "certify_timestamp": "2021-10-01T10:01:19.937Z",
      "revokeTimestamp": "2021-10-23T10:01:19.937Z",
      "logs": [
        {
          "message": "log 1"
        },
        {
          "message": "log 2"
        }
      ]
    },
    {
      "id": "9c68c658-2d7d-487c-a0ce-6d9cdcc7eaf7",
      "name": "IIQ",
      "certify_timestamp": "2021-10-01T10:01:19.937Z",
      "revokeTimestamp": "2021-10-01T10:01:19.937Z",
      "logs": [
        {
          "message": "log 1"
        },
        {
          "message": "log 2"
        }
      ]
    }
  ]
  ```

## POST /api/datasink/update/logs

* POST /api/datasink/update/logs

  Update data sink logs.

  Endpoint

  ```
  /api/datasink/update/logs
  ```

  Authorization

  ```
  <API Key>
  ```

  **JSON Body Parameters**

  | Parameter | Type   | Description                            |
  | --------- | ------ | -------------------------------------- |
  | id        | string | Data sink ID (format: UUID) (required) |
  | logs      | object | JSON logs object (required)            |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/datasink/update/logs \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "id": "87e341c0-c1aa-4b0e-9ae5-1384bb6de8fc",
    "logs": {
      "logs": [
        {
          "created": "2021-11-19T09:01:19.937Z",
          "type": "INFO",
          "message": "transaction started"
        },
        {
          "created": "2021-11-19T10:01:19.937Z",
          "type": "INFO",
          "message": "transaction successful"
        }
      ]
    }
  }'
  ```

  Example Response (Success)

  ```
  {
    "message": "ok"
  }
  ```

---

---
title: Entitlements
description: The following are Ping Autonomous Identity filtering by entitlements endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-entitlements-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-entitlements-api.html
section_ids:
  get_apientitlementssearch: GET /api/entitlements/search
  post_apientitlementsstats: POST /api/entitlements/stats
  get_apientitlementsidid: GET /api/entitlements/id/{id}
  get_apientitlementsunscored: GET /api/entitlements/unscored
  api-entitlements-distinct: GET /api/entitlements/distinct
  api-entitlements-recommendations: GET /api/entitlements/recommendations
---

# Entitlements

The following are Ping Autonomous Identity filtering by entitlements endpoints:

## GET /api/entitlements/search

* GET /api/entitlements/search

  Search for entitlements by name and with applied filters. \[Ent Owner, App Owner, Admin]

  Endpoint

  ```
  /api/entitlements/search?q=QueryString
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  by      appOwner or enttOwner
  user    user ID
  q       Search query string (required)
  appId   Application ID to use as a filter
  ```

  Example Request

  ```
  curl --location --request GET 'https://autoid-api.forgerock.com/api/entitlements/search?by=enttOwner&user=john.doe&q=WEB&appId=Salesforce' \
  --header 'Content-Type: application/json'
  ```

  Example Response

  ```
  {
    "values": [
      {
        "id": "string",
        "app_id": "string",
        "app_name": "string",
        "entt_name": "string"
      }
    ]
  }
  ```

## POST /api/entitlements/stats

* POST /api/entitlements/stats

  Get data for entitlements view. \[Supervisor, Ent Owner, Admin]

  Endpoint

  ```
  /api/entitlements/stats?by=supervisor/entitlementOwner/admin
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  by      supervisor, roleOwner
  ```

  Body

  ```
  {
  	"ownerId": "timothy.slack",
  	"isHighRiskOnly": true,
  	"isMediumLowRiskOnly": false,
  	"isUserEntitlementsIncluded": true,
  	"filters": [{
  		"type": "app_id",
  		"group": "criticality",
  		"value": "Essential"
  	}]
  }
  ```

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/entitlements/stats?by=supervisor' \
  --header 'content-type: application/json' \
  --data-raw '{
  	"ownerId": "timothy.slack",
  	"isHighRiskOnly": true,
  	"isMediumLowRiskOnly": false,
  	"isUserEntitlementsIncluded": true,
  	"filters": [{
  		"type": "app_id",
  		"group": "criticality",
  		"value": "Essential"
  	}]
  }'
  ```

  Example Response

  ```
  {
    "total_entitlements": 0,
    "total_subordinates": 0,
    "unscoredEntitlements": 0,
    "scoredEntitlements": 0,
    "usersWithNoEntitlement": 0,
    "usersWithNoScoredEntitlement": 0,
    "distinct_apps": [
      {
        "app_id": "string",
        "app_name": "string",
        "low": 0,
        "medium": 0,
        "high": 0
      }
    ],
    "users": [
      {
        "user": "string",
        "user_name": "string",
        "high": 0,
        "medium": 0,
        "low": 0,
        "avg": "string"
      }
    ],
    "entitlements": [
      {
        "entitlement": "string",
        "entitlement_name": "string",
        "app_id": "string",
        "high_risk": "string",
        "high": 0,
        "medium": 0,
        "low": 0,
        "avg": "string"
      }
    ]
  }
  ```

## GET /api/entitlements/id/{id}

* GET /api/entitlements/id/{id}

  Get entitlement details. \[User, Supervisor, Ent Owner, App Owner, Admin]

  Endpoint

  ```
  /api/entitlements/id/{id+}
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  by      entitlement ID
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/entitlements/id/1234" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "entitlement_name": "string",
    "scores": {
      "avg": 0,
      "high": 0,
      "medium": 0,
      "low": 0
    },
    "drivingFactors": [
      {
        "attribute": {
          "id": "string",
          "title": "string",
          "value": "string"
        },
        "count": 0
      }
    ],
    "userScores": [
      {
        "score": 0,
        "count": 0
      }
    ],
    "users": [
      {
        "user": "string",
        "user_name": "string",
        "app_id": "string",
        "freq": 0,
        "frequnion": 0,
        "justification": [
          {
            "title": "string",
            "value": "string"
          }
        ],
        "rawJustification": [
          "string"
        ],
        "score": 0
      }
    ]
  }
  ```

## GET /api/entitlements/unscored

* GET /api/entitlements/unscored

  Get unscored entitlements and users for a given Supervisor or Entitlement Owner ID. \[Supervisor, Ent Owner, Admin]

  Endpoint

  ```
  /api/entitlements/unscored
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Params

  ```
  by      supervisor, entitlement owner
  user    supervisor or entitlement owner user ID
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/entitlements/unscored?by=supervisor&user=1234" \
  --header "Content-Type: application/json"
  ```

## GET /api/entitlements/distinct

* GET /api/entitlements/distinct

  Get a list of all entitlements.

  Endpoint

  ```
  /api/entitlements/distinct
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Example Request

  ```
  curl --location --request GET 'https://autoid-api.forgerock.com/api/entitlements/distinct' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <token>'
  ```

  Example Response

  ```
  [
    {
      "ent_id": "AccessType : XMLP_ADMIN",
      "ent_name": "AccessType : XMLP_ADMIN",
      "ent_owner_id": "julie.yee",
      "app_id": "Salesforce",
      "ent_criticality": "Non-Essential",
      "ent_risk_level": "Medium"
    }
  ]
  ```

## GET /api/entitlements/recommendations

* GET /api/entitlements/recommendations

  Get a list of entitlement recommendations for a given set of user attributes.

  Endpoint

  ```
  /api/entitlements/recommendations
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
        "confidenceThreshold": 0.1,
        "maxResults": 1000,
        "offset": 200,
        "userAttributes": [
                    "0E_USR_MANAGER_ID_gregory.suhr",
                    "13_USR_DEPARTMENT_NAME_Facilities Area A",
                    "0C_CHIEF_YES_NO_No",
                    "0C_MANAGER_NAME_Gregory Suhr",
                    "0C_USR_EMP_TYPE_Employee",
                    "13_USR_DEPARTMENT_NAME_Wireless Operations"
                      ]
  }
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/entitlements/recommendations" \
  --header  "Content-Type: application/json" \
  --header  "Authorization: Bearer <token>" \
  --data-raw '{
      "confidenceThreshold": 0.1,
      "maxResults": 1000,
      "offset": 200,
      "userAttributes": [
         "0E_USR_MANAGER_ID_gregory.suhr",
         "13_USR_DEPARTMENT_NAME_Facilities Area A",
         "0C_CHIEF_YES_NO_No",
         "0C_MANAGER_NAME_Gregory Suhr",
         "0C_USR_EMP_TYPE_Employee",
         "13_USR_DEPARTMENT_NAME_Wireless Operations"
         ]
       }'
  ```

  Example Response

  ```
  [
    {
      "attributes": [
        "0C_CHIEF_YES_NO_No",
        "0E_USR_MANAGER_ID_gregory.suhr"
      ],
      "entitlement": "06_ENT_ID_WEB_user_WEB RCQ Flare NonIT Distribution_II",
      "confidence": 0.14,
      "frequency": 22
    },
    {
      "attributes": [
        "0C_MANAGER_NAME_Gregory Suhr",
        "13_USR_DEPARTMENT_NAME_Facilities Area A"
      ],
      "entitlement": "06_ENT_ID_Web_tildeNon-security plus",
      "confidence": 0.14,
      "frequency": 28
    },
  ]
  ```

---

---
title: Filters
description: The following are Ping Autonomous Identity Filters endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-filters-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-filters-api.html
section_ids:
  get_apifiltersowner: GET /api/filters/owner
  get_apifiltersapp: GET /api/filters/app
---

# Filters

The following are Ping Autonomous Identity Filters endpoints:

## GET /api/filters/owner

* GET /api/filters/owner

  Get filterable attributes and values. \[Supervisor, Ent Owner, Admin]

  Endpoint

  ```
  /api/filters/owner?by=supervisor&user=albert.pardini
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Query Parameters

  ```
  by      supervisor, enttOwner
  user    albert.pardini
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/filters/owner?by=supervisor&user=albert.pardini" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "items": [
      {
        "title": "string",
        "field": "string",
        "filters": {
          "field": "string",
          "title": "string",
          "options": [
            {
              "text": "string",
              "value": "string",
              "count": 0
            }
          ]
        }
      }
    ]
  }
  ```

## GET /api/filters/app

* GET /api/filters/app

  Get filterable attributes and values. \[App Owner, Admin]

  Endpoint

  ```
  /api/filters/app
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Query Parameters

  ```
  id:   application ID
  ```

  Example Request

  ```
  curl --request GET "https://autoid-api.forgerock.com/api/filters/app?id=app_1" \
  --header "Content-Type: application/json"
  ```

  Example Response

  ```
  {
    "items": [
      {
        "title": "string",
        "field": "string",
        "filters": {
          "field": "string",
          "title": "string",
          "options": [
            {
              "text": "string",
              "value": "string",
              "count": 0
            }
          ]
        }
      }
    ]
  }
  ```

---

---
title: Generate an API key
description: Ping Autonomous Identity gives an administrator the ability to generate API keys for those who want to access certain endpoints using REST. Administrators can create an API from the Self-Service page of the Ping Autonomous Identity UI.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-obtain-api-key
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-obtain-api-key.html
section_ids:
  obtain-tenant-id: Obtain the tenant ID
  create-api-keys: Create an API key using the UI
  deactivate_api_keys_using_the_ui: Deactivate API keys using the UI
  create-api-key-curl: Create an API key using curl
  get-datasource-id: API key examples
---

# Generate an API key

Ping Autonomous Identity gives an administrator the ability to generate API keys for those who want to access certain endpoints using REST. Administrators can create an API from the Self-Service page of the Ping Autonomous Identity UI.

|   |                                                                |
| - | -------------------------------------------------------------- |
|   | As of this release, only the Ingest endpoints use the API key. |

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | To use an API token, you need both the tenant ID that the API key belongs to, and the API token itself. |

## Obtain the tenant ID

In Ping Autonomous Identity 2021.8.0 and later, the tenant ID is set as an environment variable that you can easily access.

* On the target node, get the tenant ID.

```
$ env | grep TENANT_ID
TENANT_ID=8700f5cb-eaca-461e-8c2e-245a25f2399d
```

## Create an API key using the UI

Administrators can create API keys on the Self-Service page of the Ping Autonomous Identity UI.

1. On the Ping Autonomous Identity UI, click the admin drop-down on the top-left of the page.

2. Click Self Service.

3. Click the API Keys tab.

4. Click Generate API Key.

5. Set the name, description, and expiration date for API key, and then click Create.

6. Make sure to make a copy of the key in the box as it cannot be retrieved once the dialog box is closed. The new API key appears in the list of keys on the API Keys page.

   > **Collapse: Click an example**
   >
   > ![self service api key](_images/self-service-api-key.gif)

## Deactivate API keys using the UI

Administrators can revoke or delete API keys. Use the following procedure to revoke an API key.

1. On the Ping Autonomous Identity UI, click the admin drop-down on the top-left of the page.

2. Click Self Service.

3. Click the API Keys tab.

4. In the Search field, enter the API key.

5. In the list of API keys, click the three dots, and select Revoke. This action deletes the API key for use.

   > **Collapse: Click an example**
   >
   > ![self service api key revoke](_images/self-service-api-key-revoke.gif)

## Create an API key using curl

Administrators can create API keys on the command line using curl commands.

1. Open a terminal, and create an authentication bearer token for an admin user:

   ```
   curl -k -X POST \
   https://autoid-ui.forgerock.com/api/authentication/login \
   -H 'Content-Type: application/json' \
   -d '{
   "username": "bob.rodgers@forgerock.com",
   "password": "Welcome123"
   }'
   ```

   The response is:

   ```
   {
     "user": {
       "dn": "cn=bob.rodgers@forgerock.com,ou=People,dc=zoran,dc=com",
       "controls": [],
       "displayName": "Bob Rodgers",
       "gidNumber": "999",
       "uid": "bob.rodgers",
       "_groups": [
         "Zoran User",
         "Zoran Admin"
       ]
     },
     "token": "token_value"
   }
   ```

2. Set the `TOKEN` environment variable:

   ```
   export TOKEN=token_value
   ```

3. Generate a new API key:

   ```
   curl -k -X POST \
   https://autoid-ui.forgerock.com/api/admin/createApiToken \
   -H "Authorization: Bearer $TOKEN" \
   -H 'Content-Type: application/json' \
   -d ' {
       "name": "Ingest Key",
       "description": "API key for ingestion endpoints",
       "expiration": "2022-01-02"
   }'
   ```

   The response is:

   ```
   {
     "token": "19412ace-1d99-44b2-88e0-16136fc5c77a"
   }
   ```

## API key examples

The following curl example illustrates how to use the API key to get a datasource ID for an ingestion job:

1. Obtain an API key from an administrator. See [Create API Keys](../admin-guide/chap-self-service.html#create-api-keys).

2. Obtain the tenant ID using the environment variable.

   ```
   $ env | grep TENANT_ID
   TENANT_ID=8700f5cb-eaca-461e-8c2e-245a25f2399d
   ```

3. Query Ping Autonomous Identity's Java API Service (JAS) to obtain a data source ID using the API Key (for example, '1b7789f0-6c2f-4afa-a84b-a65a28f5c1a1'):

   ```
   curl 'https://autoid-ui.forgerock.com/jas/datasource/search' \
     -H 'authority: autoid-ui.forgerock.com' \
     -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
     -H 'accept: application/json, text/plain, /' \
     -H 'x-tenant-id: 8700f5cb-eaca-461e-8c2e-245a25f2399d' \
     -H 'authorization: 1b7789f0-6c2f-4afa-a84b-a65a28f5c1a1' \
     -H 'sec-ch-ua-mobile: ?0' \
     -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
     -H 'content-type: application/json' \
     -H 'origin: https://autoid-ui.forgerock.com' \
     -H 'sec-fetch-site: same-origin' \
     -H 'sec-fetch-mode: cors' \
     -H 'sec-fetch-dest: empty' \
     -H 'referer: https://autoid-ui.forgerock.com/data-sources' \
     -H 'accept-language: en-US,en;q=0.9' \
     --data-raw '{
                   "query": {
                     "sort": [
                       {
                         "datasource_id.keyword": {
                           "order": "desc"
                         }
                       }
                     ],
                     "size": 10,
                     "track_total_hits": true,
                     "query": {
                       "match_all": {}
                     }
                   }
                 }' \
     --compressed \
     --insecure
   ```

   The response includes the datasource ID:

   ```
   {
     "took": 8,
     "timed_out": false,
     "_shards": {
       "total": 3,
       "successful": 3,
       "skipped": 0,
       "failed": 0
     },
     "hits": {
       "total": {
         "value": 1,
         "relation": "eq"
       },
       "max_score": null,
       "hits": [
         {
           "_index": "autonomous-iam_common_datasources_latest",
           "_type": "_doc",
           "_id": "259b80c7693e92c4c29bd64deac4cd99826d427027645c9413afdb3f083b891d8d34cefaebd5fcf098c066dc1a4da2879d8732d59bfd2e239a285184f8e7a35b",
           "_score": null,
           "_source": {
             "datasource_id": "2d7a6a76-469c-4035-b312-fb1daf104e98",
             "name": "Showcase-CSV-DS",
             "sync_type": "full",
             "icon": "apps",
             "isActive": true,
             "entityTypes": {
               "/autoid/system/datasources/2d7a6a76-469c-4035-b312-fb1daf104e98/applications": {
                 "uri": {
                   "file": "file:/data/input/applications.csv"
                 }
               },
               "/autoid/system/datasources/2d7a6a76-469c-4035-b312-fb1daf104e98/assignments": {
                 "uri": {
                   "file": "file:/data/input/assignments.csv"
                 }
               },
               "/autoid/system/datasources/2d7a6a76-469c-4035-b312-fb1daf104e98/entitlements": {
                 "uri": {
                   "file": "file:/data/input/entitlements.csv"
                 }
               },
               "/autoid/system/datasources/2d7a6a76-469c-4035-b312-fb1daf104e98/identities": {
                 "uri": {
                   "file": "file:/data/input/identities.csv"
                 }
               }
             },
             "connectionSettings": {
               "csv": {}
             },
             "metadata": {
               "contextId": "scripts",
               "entityType": "/common/datasources",
               "primaryKey": "2d7a6a76-469c-4035-b312-fb1daf104e98",
               "entityPath": "/common/datasources/2d7a6a76-469c-4035-b312-fb1daf104e98",
               "entityDefinition": "datasources",
               "namespace": "/common",
               "branch": "actual",
               "created": "2021-08-25T03:53:33.634Z",
               "tenantId": "autonomous-iam"
             }
           },
           "sort": [
             "2d7a6a76-469c-4035-b312-fb1daf104e98"
           ]
         }
       ]
     }
   }
   ```

4. Make sure your client that accesses the JAS configuration has something similar to the following:

   ```
   public static final String CONFIG_JAS_API_TOKEN = "JAS_API_KEY";
   public static final String CONFIG_JAS_TENANT_ID = "TENANT_ID";
   ```

---

---
title: Ingest
description: The following endpoints support the ingestion of base entities, such as applications, entitlements, identities, assignments, data sources, and mappings. New APIs introduced in this release are marked with .
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-ingest-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-ingest-api.html
section_ids:
  ingest-applications: POST /api/ingest/applications
  ingest-entitlements: POST /api/ingest/entitlements
  ingest-identities: POST /api/ingest/identities
  ingest-assignments: POST /api/ingest/assignments
  ingest-datasources: POST /api/ingest/datasources
  ingest-mappings: POST /api/ingest/mappings
---

# Ingest

The following endpoints support the ingestion of base entities, such as applications, entitlements, identities, assignments, data sources, and mappings. New APIs introduced in this release are marked with [icon: star, set=fa].

To access these endpoints, you need a valid API key in the *X-API-KEY* header for authorization. To obtain an API key, see [Generate an API key](chap-obtain-api-key.html).

## POST /api/ingest/applications

* POST /api/ingest/applications

  Create, update, upsert, or delete application entities.

  Endpoint

  ```
  /api/ingest/applications
  ```

  Authorization

  ```
  <API Key-value>
  ```

  **Body Parameters**

  | Parameter | Type   | Description                                                  |
  | --------- | ------ | ------------------------------------------------------------ |
  | action    | string | Action to perform: create, update, upsert, delete (required) |
  | apps      | array  | Array of application objects (properties below) (required)   |

  **Base Application Object Properties:**

  | Parameter      | Type   | Description               |
  | -------------- | ------ | ------------------------- |
  | app\_id        | string | Application ID (required) |
  | app\_name      | string | Application Name          |
  | app\_owner\_id | string | Application owner user ID |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/ingest/applications \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "action": "create",
    "apps": [
      {
        "app_id": "app1",
        "app_name": "Test App",
        "app_owner_id": "bob.rodgers"
      }
    ]
  }'
  ```

  Example Response

  ```
  {
    "message": "ok"
  }
  ```

## POST /api/ingest/entitlements

* POST /api/ingest/entitlements

  Create, update, upsert, or delete entitlement entities.

  Endpoint

  ```
  /api/ingest/entitlements
  ```

  Authorization

  ```
  <API Key-value>
  ```

  Body

  ```
  ```

  **Body Parameters**

  | Parameter    | Type   | Description                                                  |
  | ------------ | ------ | ------------------------------------------------------------ |
  | action       | string | Action to perform: create, update, upsert, delete (required) |
  | entitlements | array  | Array of entitlements objects (properties below) (required)  |

  **Base Entitlements Object Properties**

  | Parameter      | Type   | Description               |
  | -------------- | ------ | ------------------------- |
  | ent\_id        | string | Entitlement ID (required) |
  | ent\_name      | string | Entitlement Name          |
  | ent\_owner\_id | string | Entitlement owner user ID |
  | app\_id        | string | Application ID            |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/ingest/entitlements \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "action": "upsert",
    "entitlements": [
      {
        "ent_id": "ent1",
        "ent_name": "Test Ent",
        "ent_owner_id": "bob.rodgers",
        "app_id": "app1"
      }
    ]
  }'
  ```

  Example Response

  ```
  {
    "message": "ok"
  }
  ```

## POST /api/ingest/identities

* POST /api/ingest/identities

  Create, update, upsert, or delete identity entities.

  Endpoint

  ```
  /api/ingest/identities
  ```

  Authorization

  ```
  <API Key-value>
  ```

  **Body Parameters**

  | Parameter    | Type   | Description                                                  |
  | ------------ | ------ | ------------------------------------------------------------ |
  | action       | string | Action to perform: create, update, upsert, delete (required) |
  | entitlements | array  | Array of identities objects (properties below) (required)    |

  **Base Entitlements Object Properties**

  | Parameter        | Type   | Description        |
  | ---------------- | ------ | ------------------ |
  | usr\_id          | string | User ID (required) |
  | usr\_name        | string | User name          |
  | usr\_manager\_id | string | User's manager ID  |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/ingest/identities \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "action": "upsert",
    "identities": [
      {
        "usr_id": "john.doe",
        "usr_name": "John Doe",
        "usr_manager_id": "bob.rodgers"
      },
      {
        "usr_id": "jane.smith",
        "usr_name": "Jane Smith",
        "usr_manager_id": "bob.rodgers"
      }
    ]
  }'
  ```

  Example Response

  ```
  {
    "message": "ok"
  }
  ```

## POST /api/ingest/assignments

* POST /api/ingest/assignments

  Create, update, upsert, or delete assignment entities.

  Endpoint

  ```
  /api/ingest/assignments
  ```

  Authorization

  ```
  <API Key-value>
  ```

  **Body Parameters**

  | Parameter    | Type   | Description                                                  |
  | ------------ | ------ | ------------------------------------------------------------ |
  | action       | string | Action to perform: create, update, upsert, delete (required) |
  | entitlements | array  | Array of assignment objects (properties below) (required)    |

  **Base Entitlements Object Properties**

  | Parameter | Type   | Description                |
  | --------- | ------ | -------------------------- |
  | ent\_id   | string | Entitlementd ID (required) |
  | usr\_id   | string | User ID (required)         |

  Example Request

  ```
  curl -k -X POST \
  https://autoid-ui.forgerock.com/api/ingest/assignments \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "action": "upsert",
    "assignments": [
      {
        "usr_id": "john.doe",
        "ent_id": "ent1"
      },
      {
        "usr_id": "jane.smith",
        "ent_id": "ent1"
      }
    ]
  }'
  ```

  Example Response

  ```
  {
    "message": "ok"
  }
  ```

## POST /api/ingest/datasources

* POST /api/ingest/datasources

  Get data sources. Optional filtering can be applied as a JSON request body outlined below:

  Endpoint

  ```
  /api/ingest/datasources
  ```

  Authorization

  ```
  <API Key-value>
  ```

  **Body Parameters**

  | Parameter       | Type         | Description                                            |
  | --------------- | ------------ | ------------------------------------------------------ |
  | datasourceId    | string       | Data source ID                                         |
  | name            | string       | Data source name                                       |
  | isActive        | boolean      | Data source activated                                  |
  | connectionTypes | string array | List of connection types to filter: jdbc, csv, generic |
  | entityTypes     | string array | List of entity types                                   |

  Example Request

  ```
  curl -k -X GET \
  https://autoid-ui.forgerock.com/api/ingest/datasources \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "connectionTypes": ["csv"],
    "isActive": true
  }'
  ```

  Example Response

  ```
  [
    {
      "datasource_id": "fdbfb998-7b3e-4ddc-9e4a-a4c46cace49e",
      "name": "Test data",
      "sync_type": "full",
      "icon": "apps",
      "isActive": true,
      "entityTypes": {
        "/autoid/system/datasources/fdbfb998-7b3e-4ddc-9e4a-a4c46cace49e/applications": {
          "uri": {
            "file": "file:/data/input/applications.csv"
          }
        },
        "/autoid/system/datasources/fdbfb998-7b3e-4ddc-9e4a-a4c46cace49e/assignments": {
          "uri": {
            "file": "file:/data/input/assignments.csv"
          }
        },
        "/autoid/system/datasources/fdbfb998-7b3e-4ddc-9e4a-a4c46cace49e/entitlements": {
          "uri": {
            "file": "file:/data/input/entitlements.csv"
          }
        },
        "/autoid/system/datasources/fdbfb998-7b3e-4ddc-9e4a-a4c46cace49e/identities": {
          "uri": {
            "file": "file:/data/input/identities.csv"
          }
        }
      },
      "connectionSettings": {
        "csv": {}
      }
    }
  ]
  ```

## POST /api/ingest/mappings

* POST /api/ingest/mappings

  Get mappings. Optional filtering can be applied as a JSON request body outlined below:

  Endpoint

  ```
  /api/ingest/mappings
  ```

  Authorization

  ```
  <API Key-value>
  ```

  **Body Parameters**

  | Parameter        | Type         | Description                            |
  | ---------------- | ------------ | -------------------------------------- |
  | mappingId        | string       | Mapping ID                             |
  | sourceEntity     | string       | Mapping source entity                  |
  | targetEntity     | string       | Mapping target entity                  |
  | sourceProperties | string array | List of source properties to filter on |
  | targetProperties | string array | List of target properties to filter on |

  Example Request

  ```
  curl -k -X GET \
  https://autoid-ui.forgerock.com/api/ingest/mappings \
  -H 'X-API-KEY: <api key value>' \
  -H 'Content-Type: application/json' \
  -d '{
    "targetProperties": ["app_id", "app_name"]
  }'
  ```

  Example Response

  ```
  [
    {
      "mapping_id": "fb6896e5-8d0a-4bd7-b10d-5608c9a953a1",
      "source_entity": "/autoid/system/datasources/0474f92c-d530-43cc-a012-29fb6c8b3b8b/applications",
      "target_entity": "/autoid/base/applications",
      "properties": [
        {
          "source": "APP_ID",
          "target": "app_id",
          "apply": true
        },
        {
          "source": "APP_NAME",
          "target": "app_name",
          "apply": true
        },
        {
          "source": "APP_OWNER_ID",
          "target": "app_owner_id",
          "apply": true
        }
      ]
    }
  ]
  ```

---

---
title: Jobs
description: You can define, run, and get the status of each job using REST API endpoints. When using REST calls, the available job types are the following:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-jobs-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-jobs-api.html
section_ids:
  job-definition: POST /api/job_definition
  jas-job-run: POST /jas/job/run
  jas-job-status: GET /jas/job/status
  jas-job-search: GET /jas/job/search
---

# Jobs

You can define, run, and get the status of each job using REST API endpoints. When using REST calls, the available job types are the following:

* ingest

* train

* mine

* predict-as-is

* recommend

* load

* create-assignment-index

* create-assignment-index-report

* anomaly

* insight

* audit

The following are Ping Autonomous Identity jobs endpoints:

## POST /api/job\_definition

* POST /api/job\_definition

  Set up a job definition.

  Endpoint

  ```
  /api/job_definition
  ```

  Authorization

  ```
  Bearer <Token JWT-value> or
  <API Key-value>
  ```

  Body

  ```
  {
    "branch": "actual",
    "contextId": "40c20f01-a9d8-4284-b290-c8b6ccdb8b77",
    "entityData": [
      {
        "job_name": "ShowCaseCSVAnomaly",
        "job_type": "anomaly",
        "job_parameters": {
          "driverMemory": "2g",
          "driverCores": 3,
          "executorMemory": "3G",
          "executorCores": 6
        }
      }
    ],
    "indexingRequired": true,
    "tags": {},
    "indexInSync": true
  }
  ```

  |   |                                                                           |
  | - | ------------------------------------------------------------------------- |
  |   | `contextId` is a unique identifier string. It can be anything you define. |

  Example Request

  ```
  curl 'https://autoid-ui.forgerock.com/jas/entity/persist/autoid/api/job_definition' \
    -H 'authority: autoid-ui.forgerock.com' \
    -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
    -H 'accept: application/json, text/plain, /' \
    -H 'x-tenant-id: 8700f5cb-eaca-461e-8c2e-245a25f2399d' \
    -H 'authorization: 1b7789f0-6c2f-4afa-a84b-a65a28f5c1a1' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
    -H 'content-type: application/json' \
    -H 'origin: https://autoid-ui.forgerock.com' \
    -H 'sec-fetch-site: same-origin' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-dest: empty' \
    -H 'referer: https://autoid-ui.forgerock.com/jobs' \
    -H 'accept-language: en-US,en;q=0.9' \
    --data-raw '{
                  "branch": "actual",
                  "contextId": "40c20f01-a9d8-4284-b290-c8b6ccdb8b77",
                  "entityData": [
                    {
                      "job_name": "ShowCaseCSVAnomaly",
                      "job_type": "anomaly",
                      "job_parameters": {
                        "driverMemory": "2g",
                        "driverCores": 3,
                        "executorMemory": "3G",
                        "executorCores": 6
                      }
                    }
                  ],
                  "indexingRequired": true,
                  "tags": {},
                  "indexInSync": true
                }' \
    --compressed \
    --insecure
    }
  }'
  ```

  The Job definition for data ingestion requires a `datasourceId,` which you can query. Refer to [\[get-datasource-id\]](#get-datasource-id).

  Example Request (ingest)

  ```
  curl 'https://autoid-ui.forgerock.com/jas/entity/persist/autoid/api/job_definition' \
    -H 'authority: autoid-ui.forgerock.com' \
    -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
    -H 'accept: application/json, text/plain, /' \
    -H 'x-tenant-id: 8700f5cb-eaca-461e-8c2e-245a25f2399d' \
    -H 'authorization: 1b7789f0-6c2f-4afa-a84b-a65a28f5c1a1' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
    -H 'content-type: application/json' \
    -H 'origin: https://autoid-ui.forgerock.com' \
    -H 'sec-fetch-site: same-origin' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-dest: empty' \
    -H 'referer: https://autoid-ui.forgerock.com/jobs' \
    -H 'accept-language: en-US,en;q=0.9' \
    --data-raw '{
                  "branch": "actual",
                  "contextId": "ba9cefff-1e06-4cc3-b7d6-d15e2126351c",
                  "entityData": [
                    {
                      "job_name": "ShowCaseCSVIngest",
                      "job_type": "ingest",
                      "job_parameters": {
                        "driverMemory": "2g",
                        "driverCores": 3,
                        "executorMemory": "3G",
                        "executorCores": 6,
                        "datasourceId": "2d7a6a76-469c-4035-b312-fb1daf104e98"
                      }
                    }
                  ],
                  "indexingRequired": true,
                  "tags": {},
                  "indexInSync": true
                }' \
    --compressed \
    --insecure
  ```

## POST /jas/job/run

* POST /jas/job/run

  Run the job definition.

  Endpoint

  ```
  /jas/job/run
  ```

  Authorization

  ```
  Bearer <Token JWT-value> or
  <API Key-value>
  ```

  Body

  ```
  {
      "jobType":"ingest",
      "jobDefinitionName":"ShowCaseCSVIngest"
  }
  ```

  Example Request

  ```
  curl 'https://autoid-ui.forgerock.com/jas/job/run' \
    -H 'authority: autoid-ui.forgerock.com' \
    -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
    -H 'accept: application/json, text/plain, /' \
    -H 'x-tenant-id: 8700f5cb-eaca-461e-8c2e-245a25f2399d' \
    -H 'authorization: 1b7789f0-6c2f-4afa-a84b-a65a28f5c1a1' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
    -H 'content-type: application/json' \
    -H 'origin: https://autoid-ui.forgerock.com' \
    -H 'sec-fetch-site: same-origin' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-dest: empty' \
    -H 'referer: https://autoid-ui.forgerock.com/jobs' \
    -H 'accept-language: en-US,en;q=0.9' \
    --data-raw '{
      "jobType":"ingest",
      "jobDefinitionName":"ShowCaseCSVIngest"
    }' \
    --compressed \
    --insecure
  ```

## GET /jas/job/status

* GET /jas/job/status

  Obtain the job's status.

  Endpoint

  ```
  /jas/job/status
  ```

  Authorization

  ```
  Bearer <Token JWT-value> or
  <API Key-value>
  ```

  Body

  ```
  {
      "jobType":"anomaly",
      "jobDefinitionName":"ShowCaseCSVAnomaly"
  }
  ```

  Example Request

  ```
  curl 'https://autoid-ui.forgerock.com/jas/job/status' \
    -H 'authority: autoid-ui.forgerock.com' \
    -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
    -H 'accept: application/json, text/plain, /' \
    -H 'x-tenant-id: 8700f5cb-eaca-461e-8c2e-245a25f2399d' \
    -H 'authorization: 1b7789f0-6c2f-4afa-a84b-a65a28f5c1a1' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
    -H 'content-type: application/json' \
    -H 'origin: https://autoid-ui.forgerock.com' \
    -H 'sec-fetch-site: same-origin' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-dest: empty' \
    -H 'referer: https://autoid-ui.forgerock.com/jobs' \
    -H 'accept-language: en-US,en;q=0.9' \
    --data-raw '{
      "jobType":"anomaly",
      "jobDefinitionName":"ShowCaseCSVAnomaly"
    }' \
    --compressed \
    --insecure
  ```

## GET /jas/job/search

* GET /jas/job/search

  Search for a job definition.

  Endpoint

  ```
  /jas/job/search
  ```

  Authorization

  ```
  Bearer <Token JWT-value> or
  <API Key-value>
  ```

  Body

  ```
  {
    "query": {
      "sort": [
        {
          "job_name.keyword": {
            "order": "asc"
          }
        },
        {
          "metadata.primaryKey.keyword": {
            "order": "desc"
          }
        }
      ],
      "size": 10,
      "track_total_hits": true,
      "query": {
        "match_all": {}
      }
    }
  }
  ```

  Example Request

  ```
  curl 'https://autoid-ui.forgerock.com/jas/entity/search/autoid/api/job_definition' \
    -H 'authority: autoid-ui.forgerock.com' \
    -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
    -H 'accept: application/json, text/plain, /' \
    -H 'x-tenant-id: 8700f5cb-eaca-461e-8c2e-245a25f2399d' \
    -H 'authorization: 1b7789f0-6c2f-4afa-a84b-a65a28f5c1a1' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' \
    -H 'content-type: application/json' \
    -H 'origin: https://autoid-ui.forgerock.com' \
    -H 'sec-fetch-site: same-origin' \
    -H 'sec-fetch-mode: cors' \
    -H 'sec-fetch-dest: empty' \
    -H 'referer: https://autoid-ui.forgerock.com/jobs' \
    -H 'accept-language: en-US,en;q=0.9' \
    --data-raw '{
                  "query": {
                    "sort": [
                      {
                        "job_name.keyword": {
                          "order": "asc"
                        }
                      },
                      {
                        "metadata.primaryKey.keyword": {
                          "order": "desc"
                        }
                      }
                    ],
                    "size": 10,
                    "track_total_hits": true,
                    "query": {
                      "match_all": {}
                    }
                  }
                }' \
    --compressed \
    --insecure
  ```

---

---
title: Manager with Application Oriented
description: The following are Ping Autonomous Identity manager with application oriented endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-manager-with-app-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-manager-with-app-api.html
---

# Manager with Application Oriented

The following are Ping Autonomous Identity manager with application oriented endpoints:

* POST supervisor

  NOTE: This endpoint has been deprecated in this release by the `/entitlements/stats` endpoint.

Endpoint

```
/api/managersWithAppOriented/supervisor
```

Authorization

```
<Bearer Token JWT-value>
```

Body

```
{
	"managerId": "Christy.Cronin"
}
```

Example Request

```
curl --location --request POST '/api/managersWithAppOriented/supervisor' \
--header 'Content-Type: application/json' \
--data-raw '{
	"managerId": "Christy.Cronin"
}'
```

* POST supervisorEntitlements

  NOTE: This endpoint has been deprecated in this release by the `/entitlements/stats` endpoint.

Endpoint

```
/api/managersWithAppOriented/supervisorEntitlements
```

Authorization

```
<Bearer Token JWT-value>
```

Body

```
{
	"managerId": "Christy.Cronin"
}
```

Example Request

```
curl --location --request POST '/api/managersWithAppOriented/supervisorEntitlements' \
--header 'Content-Type: application/json' \
--data-raw '{
	"managerId": "Christy.Cronin"
}'
```

* POST supervisorUser

  NOTE: This endpoint has been deprecated in this release by the `/entitlements/stats` endpoint.

Endpoint

```
/api/managersWithAppOriented/supervisorUser
```

Authorization

```
<Bearer Token JWT-value>
```

Body

```
{
	"managerId": "Christy.Cronin"
}
```

Example Request

```
curl --location --request POST '/api/managersWithAppOriented/supervisorUser' \
--header 'Content-Type: application/json' \
--data-raw '{
	"managerId": "Christy.Cronin"
}'
```

---

---
title: Report
description: Ping Autonomous Identity captures information in its log files that are useful when troubleshooting problems. You can access the reports using REST calls to the Report API endpoint.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-report-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-report-api.html
section_ids:
  post_apireport: POST /api/report
---

# Report

Ping Autonomous Identity captures information in its log files that are useful when troubleshooting problems. You can access the reports using REST calls to the Report API endpoint.

## POST /api/report

* POST /api/report

  Get reporting data. \[All]

  Endpoint

  ```
  /api/report
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Headers

  ```
  Content-Type      application/json
  ```

  Params

  ```
  fields
  ```

  Body

  ```
  {
  	"fields": [
  		"id",
  		"type",
  		"batch_id",
  		"original",
  		"update"
  	],
  	"reportType": "EventBasedCertification"
  }
  ```

  Example Request

  ```
  curl --request POST "https://autoid-api.forgerock.com/api/report" \
  --header "Content-Type: application/json" \
  --header 'Authorization: Bearer <token>' \
  --data-raw '{
  	"fields": [
  		"id",
  		"type",
  		"batch_id",
  		"original",
  		"update"
  	],
  	"reportType": "EventBasedCertification"
  }'
  ```

---

---
title: Role Owner with Application Oriented
description: The following are Ping Autonomous Identity role owner with applications endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-roleowner-with-app-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-roleowner-with-app-api.html
---

# Role Owner with Application Oriented

The following are Ping Autonomous Identity role owner with applications endpoints:

* POST unscoredEntitlements

  NOTE: This endpoint has been deprecated in this release by the `/entitlements/unscored` endpoint.

Endpoint

```
/api/roleOwnerWithAppOriented/unscoredEntitlements
```

Authorization

```
<Bearer Token JWT-value>
```

Body

```
{
	"roleOwnerId": "supervisor"
}
```

Example Request

```
curl --location --request POST '/api/roleOwnerWithAppOriented/unscoredEntitlements' \
--header 'Content-Type: application/json' \
--data-raw '{
	"roleOwnerId": "supervisor"
}'
```

* POST entownuserdata

  NOTE: This endpoint has been deprecated in this release by the `/entitlements/stats` endpoint.

Endpoint

```
/api/roleOwnerWithAppOriented/entownuserdata
```

Authorization

```
<Bearer Token JWT-value>
```

Body

```
{
	"roleOwnerId": "elizabeth.saiz"
}
```

Example Request

```
curl --location --request POST '/api/roleOwnerWithAppOriented/entownuserdata' \
--header 'Content-Type: application/json' \
--data-raw '{
	"roleOwnerId": "26713",
	"onlyLM": "1"
}'
```

Example Response

```
{
  "roleOwner": {
    "roleOwnerId": "26713",
    "total_entitlements": 1,
    "total_subordinates": 1,
    "unscoredEntitlements": 0,
    "scoredEntitlements": 1,
    "entitlementsWithNoUser": 0,
    "entitlements": [
      {
        "app_id": "1",
        "app_name": "1",
        "entitlement": "1",
        "entitlement_name": "1",
        "high_risk": "1",
        "high": 0,
        "medium": 0,
        "low": 1,
        "avg": "0.20"
      }
    ],
    "distinctApps": [
      {
        "app_id": "1",
        "app_name": "1"
      }
    ]
  }
}
```

* POST entownentdata

  NOTE: This endpoint has been deprecated in this release by the `/entitlements/stats` endpoint.

Endpoint

```
/api/roleOwnerWithAppOriented/entownentdata
```

Authorization

```
<Bearer Token JWT-value>
```

Body

```
{
	"roleOwnerId": "elizabeth.saiz"
}
```

Example Request

```
curl --location --request POST '/api/roleOwnerWithAppOriented/entownuserdata' \
--header 'Content-Type: application/json' \
--data-raw '{
	"roleOwnerId": "26713",
	"onlyLM": "1"
}'
```

Example Response

```
{
  "roleOwner": {
    "roleOwnerId": "26713",
    "total_entitlements": 1,
    "total_subordinates": 1,
    "unscoredEntitlements": 0,
    "scoredEntitlements": 1,
    "entitlementsWithNoUser": 0,
    "entitlements": [
      {
        "app_id": "1",
        "app_name": "1",
        "entitlement": "1",
        "entitlement_name": "1",
        "high_risk": "1",
        "high": 0,
        "medium": 0,
        "low": 1,
        "avg": "0.20"
      }
    ],
    "distinctApps": [
      {
        "app_id": "1",
        "app_name": "1"
      }
    ]
  }
}
```

---

---
title: Roles
description: The following are Ping Autonomous Identity filtering by roles endpoints:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:api-guide:chap-roles-api
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/api-guide/chap-roles-api.html
section_ids:
  api-roles: POST /api/roles
  api-roles-delete: POST /api/roles/delete
  api-roles-export: POST /api/roles/export
---

# Roles

The following are Ping Autonomous Identity filtering by roles endpoints:

## POST /api/roles

* POST /api/roles

  Create draft roles and make updates to roles.

  Endpoint

  ```
  /api/roles
  ```

  Authorization

  ```
  <Bearer Token JWT-value> OR <API-KEY>
  ```

  **Request Body Parameters**

  | Parameter         | Type        | Description                                                             |
  | ----------------- | ----------- | ----------------------------------------------------------------------- |
  | action            | string      | Action to perform ('create', 'save', 'publish', 'unpublish') (required) |
  | updateAllMetadata | boolean     | Update metadata for all related roles regardless of statuus             |
  | role              | role object | Role object (properties below) (required)                               |

  **Role Object Properties**

  | Parameter              | Type                                  | Description                                                                 |
  | ---------------------- | ------------------------------------- | --------------------------------------------------------------------------- |
  | role\_id               | string                                | Role ID in uuid format (required)                                           |
  | status                 | string                                | Status of role ('draft', 'candidate', or 'active') (required)               |
  | custom\_role           | boolean                               | Role is a custom role                                                       |
  | member\_count          | number                                | Number of users the roles applies to                                        |
  | assignment\_count      | number                                | Number of assignments the role applies to                                   |
  | entitlements           | string array                          | List of entitlement IDs that are part of the role                           |
  | justifications         | string array                          | List of raw justifications                                                  |
  | datasink\_status       | string                                | Datasink status ('ack' or 'nack')                                           |
  | role\_metadata         | role metadata object                  | Role metadata (properties below)                                            |
  | entitlements\_metadata | array of entitlement metadata objects | List of entitlement metadata for each entitlement (object properties below) |

  **Role Metadata Object Properties**

  | Parameter                  | Type   | Description             |
  | -------------------------- | ------ | ----------------------- |
  | role\_name                 | string | Display name of role    |
  | description                | string | Role description        |
  | role\_owner\_id            | string | Role owner ID           |
  | role\_owner\_display\_name | string | Role owner display name |

  **Entitlement Metadata Object Properties**

  | Parameter          | Type               | Description                                      |
  | ------------------ | ------------------ | ------------------------------------------------ |
  | ent\_id            | string             | Entitlement ID (required)                        |
  | ent\_name          | string             | Entitlement name (required)                      |
  | application        | application object | Application metadata (object properties below)   |
  | entitlement\_owner | owner object       | Entitlement owner data (object properties below) |

  **Application Object Properties**

  | Parameter          | Type         | Description                                      |
  | ------------------ | ------------ | ------------------------------------------------ |
  | app\_id            | string       | Application ID                                   |
  | app\_name          | string       | Application name                                 |
  | application\_owner | owner object | Application owner data (object properties below) |

  **Owner Object Properties**

  | Parameter        | Type   | Description                |
  | ---------------- | ------ | -------------------------- |
  | usr\_id          | string | User ID (required)         |
  | usr\_name        | string | User name (required)       |
  | usr\_manager\_id | string | User manager ID (required) |

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/roles' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <token>' \
  --data-raw '{
    "action": "save",
    "updateAllMetadata": false,
    "role": {
      "role_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "status": "draft",
      "custom_role": false,
      "member_count": 0,
      "assignment_count": 0,
      "entitlements": [
        "string"
      ],
      "entitlements_metadata": [
        {
          "ent_id": "string",
          "ent_name": "string",
          "application": {
            "app_id": "string",
            "app_name": "string",
            "application_owner": {
              "usr_id": "string",
              "usr_name": "string",
              "usr_manager_id": "string"
            }
          },
          "entitlement_owner": {
            "usr_id": "string",
            "usr_name": "string",
            "usr_manager_id": "string"
          }
        }
      ],
      "justifications": [
        "string"
      ],
      "role_metadata": {
        "role_name": "string",
        "description": "string",
        "role_owner_display_name": "string",
        "role_owner_id": "string"
      }
    }
  }'
  ```

  Example Response

  ```
  204 (No Content)
  ```

## POST /api/roles/delete

* POST /api/roles/delete

  Delete roles.

  Endpoint

  ```
  /api/roles/delete
  ```

  Authorization

  ```
  <Bearer Token JWT-value>
  ```

  Body

  ```
  {
      "role_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "status": "draft" | "active"
  }
  ```

  Example Request

  ```
  curl --location --request POST 'https://autoid-api.forgerock.com/api/admin/updateSelf' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer <token>' \
  --data-raw '{
      "role_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "status": "draft" | "active"
  }'
  ```

  Example Response

  ```
  204 (No content)
  ```

## POST /api/roles/export

* POST /api/roles/export

  Export role data to json.

  Endpoint

  ```
  /api/roles/export
  ```

  Authorization

  ```
  <Bearer Token JWT-value> OR <API-KEY>
  ```

  **Query Parameters**

  | Parameter                  | Type   | Description                                             |
  | -------------------------- | ------ | ------------------------------------------------------- |
  | usrId                      | string | Roles that apply for a particular user ID               |
  | entId                      | string | Roles that apply for a particular entitlement ID        |
  | status                     | string | Status of role ('draft', 'candidate', or 'active')      |
  | role\_name                 | string | Role name                                               |
  | description                | string | Role description                                        |
  | role\_owner\_id            | string | Role owner ID                                           |
  | role\_owner\_display\_name | string | Role owner name                                         |
  | datasinkStatus             | string | Datasink status filter ('ack', 'nack')                  |
  | timestampThresholds        | object | Timestamp threshold object (available properties below) |

  **timestampThresholds Object Properties**

  | Parameter | Type   | Description                                                                                        |
  | --------- | ------ | -------------------------------------------------------------------------------------------------- |
  | gt        | string | Greater than timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **gte**.         |
  | gte       | string | Greater than or equal timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **gt**. |
  | lt        | string | Less than timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **lte**.            |
  | lte       | string | Less than or equal timestamp (format: yyyy-mm-ddThh:mm:ss.SSSZ). Cannot be present with **le**.    |

  Body

  ```
  {
    "usrId": "john.doe",
    "datasinkStatus": "nack"
  }
  ```

  Example Request (Datasink Filter)

  ```
  curl -k -X POST \
  'https://autoid-ui.forgerock.com/api/roles/export' \
  --header 'Content-type: application/json' \
  --header 'Authorization: Bearer <token>' <OR> -H 'X-API-KEY: <api-key-value>' \
  --data-raw '{
  	"usrId": "john.doe",
  	"datasinkStatus": "nack"
  }'
  ```

  Example Response (Datasink Filter)

  ```
  {
    "roles": [
      	{
  	  "temp_role_name": "Role J0-R21",
  	  "normalized_role_name": "role j0-r21",
  	  "member_count": 1,
  	  "assignment_count": 1,
  	  "entitlement_count": 1,
  	  "role_id": "4aaf81db-2f8c-42b4-b954-1018a71743de",
  	  "status": "candidate",
  	  "entitlements": [
  		"Ent_1"
  	  ],
  	  "entitlements_metadata": [
  		{
  		  "ent_criticality": "Essential",
  		  "ent_id": " Ent_1",
  		  "ent_name": " Ent_1",
  		  "ent_risk_level": "Low",
  		  "application":
  		  {
  			"app_criticality": "Essential",
  			"app_id": "Active Directory",
  			"app_name": "Active Directory",
  			"app_risk_level": "High",
  			"application_owner":
  			{
  			  "chief_yes_no": "Yes",
  			  "city": "Kansas City",
  			  "cost_center": "CON_SD9",
  			  "department": "Facilities Area A",
  			  "is_active": "Y",
  			  "job_description": "Facilities Area A",
  			  "jobcode_name": "Operating Clerk",
  			  "line_of_business": "Transmission Operations",
  			  "line_of_business_subgroup": "Real Estate",
  			  "manager_name": "Thomas Shawyer",
  			  "usr_department_name": "Facilities Area A",
  			  "usr_display_name": "Derick Hui",
  			  "usr_emp_type": "Non-Employee",
  			  "usr_id": "derick.hui",
  			  "usr_manager_id": "thomas.shawyer",
  			  "usr_name": "Derick Hui"
  			}
  		  },
  		  "entitlement_owner":
  		  {
  			"chief_yes_no": "No",
  			"city": "Saint Paul",
  			"cost_center": "OP_TT4",
  			"department": "InfoSYS Power Gen",
  			"is_active": "Y",
  			"job_description": "InfoSYS Power Gen",
  			"jobcode_name": "Lineman",
  			"line_of_business": "Ethics and Compliance",
  			"line_of_business_subgroup": "System Operations",
  			"manager_name": "James Bosch",
  			"usr_department_name": "InfoSYS Power Gen",
  			"usr_display_name": "Carolyn Latanafrancia",
  			"usr_emp_type": "Non-Employee",
  			"usr_id": "carolyn.latanafrancia",
  			"usr_manager_id": "james.bosch",
  			"usr_name": "Carolyn Latanafrancia"
  		  }
  		}
  	  ],
  	  "justifications": [
  		"0B_COST_CENTER_SOL_ER2 19_LINE_OF_BUSINESS_SUBGROUP_Energy%20Solutions"
  	  ],
  	  "users": [
  		{
  		  "usr_id": "aaron.lozada",
  		  "usr_display_name": "Aaron Lozada",
  		  "attributes": [
  			"13_USR_DEPARTMENT_NAME_Operations%20SUP",
  			"0F_JOB_DESCRIPTION_Operations_%20SUP",
  			"0C_JOBCODE_NAME_Apprentice",
  			"0C_MANAGER_NAME_Gary%20Amelio",
  			"09_IS_ACTIVE_Y",
  			"10_LINE_OF_BUSINESS_Distribution%20Operations",
  			"10_USR_DISPLAY_NAME_Aaron%20Lozada",
  			"0B_COST_CENTER_SOL_ER2",
  			"08_USR_NAME_Aaron%20Lozada",
  			"0C_CHIEF_YES_NO_No",
  			"0C_USR_EMP_TYPE_Employee",
  			"19_LINE_OF_BUSINESS_SUBGROUP_Energy%20Solutions",
  			"04_CITY_Kansas%20City"
  		  ]
  		}
  	  ]
       }
    ]
  }
  ```
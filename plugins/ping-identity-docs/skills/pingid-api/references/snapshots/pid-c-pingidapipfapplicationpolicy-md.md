---
title: PingID Application Policy Management API for PingFederate
description: PingID allows organizations to create web authentication policies, and apply them to one or more applications, or one or more user groups, or both. See Manage app and group lists in the PingID admin guide.
component: pingid-api
page_id: pingid-api::pid_c_PingIDapiPFapplicationPolicy
canonical_url: https://developer.pingidentity.com/pingid-api/pid_c_PingIDapiPFapplicationPolicy.html
section_ids:
  pingfederate-application-policy-api: PingFederate Application Policy API
  addapplication: AddApplication
  getapplications: GetApplications
  updateapplications: UpdateApplications
  deleteapplications: DeleteApplications
---

# PingID Application Policy Management API for PingFederate

## PingFederate Application Policy API

PingID allows organizations to create web authentication policies, and apply them to one or more applications, or one or more user groups, or both. See [Manage app and group lists](https://docs.pingidentity.com/pingid/pingid_service_management/pid_managing_app_group_lists.html) in the PingID admin guide.

The PingID API provides operations for you to programmatically create, retrieve, update and delete entries in the PingFederate applications list. These operations provide the flexibility for batch or mass application updates, as an alternative to manual updates of individual applications via the admin UI. After the API operations are successfully completed and committed, the updated PingFederate application list is visible by refreshing the admin UI.

## AddApplication

The AddApplication operation creates a new application entry in the PingFederate applications list.

This is the AddApplication URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/addapplication/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
reqBody: {
    "application": {
        "id": "<application ID>",
        "name": "<application name>"
    }
}
```

The parameters included in the reqBody object are:

| Parameter   | DataType    | Description                                                                                                                                                  |
| ----------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| application | Application | See details in the table below.                                                                                                                              |
| clientData  | String      | Optional.This value is returned unchanged in the API response.It can be used to save state and/or client context data for the application between API calls. |

The application parameters:

| Parameter | DataType | Description                                                                                                                                                                                                |
| --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id        | String   | The application's unique ID, up to 255 characters in length.Mandatory.It can contain alphanumeric characters and spaces.                                                                                   |
| name      | String   | The application's name, up to 20 characters in length.Mandatory.The application name is displayed in the PingFederate application list in the admin UI. It can contain alphanumeric characters and spaces. |

**Response Body Parameters**

Example response body:

```json
{
  "responseBody": {
    "clientData": null,
    "errorId": 200,
    "errorMsg": null,
    "application": {
        "id": "<application ID>",
        "name": "<application name>"
    },
    "uniqueMsgId": "webs_DqQkivHN1hEzZfJjbcaOQdGcel7fBtZUVj7l1yNbuNI"
  }
}
```

The parameters included in the responseBody object are:

| Parameter   | DataType    | Description                                                                                                                   |
| ----------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------- |
| clientData  | String      | The value sent in the request's clientData field.                                                                             |
| errorId     | Int         | A numeric error code.                                                                                                         |
| errorMsg    | String      | A textual description of the error, if there is one.                                                                          |
| application | Application | See details in the table below.                                                                                               |
| uniqueMsgId | String      | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes. |

The application parameters:

| Parameter | DataType | Description                                                                                                                                                        |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id        | String   | The application's unique ID. It can contain alphanumeric characters and spaces.                                                                                    |
| name      | String   | The application's name. The application name is displayed in the PingFederate application list in the admin UI. It can contain alphanumeric characters and spaces. |

## GetApplications

The GetApplications operation retrieves application details from the PingFederate applications list.

This is the GetApplications URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/getapplications/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
"reqBody":{}
```

The optional parameter in the reqBody object:

| Parameter  | DataType | Description                                                                                                                                                  |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| clientData | String   | Optional.This value is returned unchanged in the API response.It can be used to save state and/or client context data for the application between API calls. |

**Response Body Parameters**

Example response body:

```json
{
  "responseBody": {
    "clientData": null,
    "errorId": 200,
    "errorMsg": null,
    "applications": [
      {
        "id": "<application ID>",
        "name": "<application name>"
      }
    ],
    "uniqueMsgId": "webs_M5MrhPDA8TPjW7n-eaprHD3Bn3lbTmArviGdKhJ8r3U"
  }
}
```

The parameters included in the responseBody object are:

| Parameter    | DataType            | Description                                                                                                                   |
| ------------ | ------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| clientData   | String              | The value sent in the request's clientData field.                                                                             |
| errorId      | Int                 | A numeric error code.                                                                                                         |
| errorMsg     | String              | A textual description of the error, if there is one.                                                                          |
| applications | List \<Application> | See details in the application table below.                                                                                   |
| uniqueMsgId  | String              | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes. |

The application parameters:

| Parameter | DataType | Description                                                                                                                                                      |
| --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id        | String   | The application's unique ID.The application ID can contain any characters, including spaces and special characters.                                              |
| name      | String   | The application's name.The application name is displayed in the PingFederate application list in the admin UI.It can contain alphanumeric characters and spaces. |

## UpdateApplications

The UpdateApplications operation updates specified existing application entries in the PingFederate applications list.

This is the UpdateApplications URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/updateapplications/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
reqBody: {
    "appsData": {
        "<application current ID>": {
	        "id": "<application new ID>",
	        "name": "<application new name>"
        }
    }
}
```

The parameters included in the reqBody object are:

| Parameter  | DataType                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| appsData   | Map\<String, Application> | The application to be updated, and its new details.- key: The application's current ID.

- id: The application's new unique ID, up to 255 characters in length.

  It can contain alphanumeric characters and spaces.

- name: The application's new name, up to 20 characters in length.

  The application name is displayed in the PingFederate application list in the admin UI.

  It can contain alphanumeric characters and spaces. |
| clientData | String                    | Optional.This value is returned unchanged in the API response.It can be used to save state and/or client context data for the application between API calls.                                                                                                                                                                                                                                                                               |

**Response Body Parameters**

Example response body:

```json
{
  "responseBody": {
    "clientData": null,
    "errorId": 200,
    "errorMsg": null,
    "uniqueMsgId": "webs_mVZV1fssdOe8Tf1-ubh01oQTnZfDO8FOIK-RVUWs0ng"
  }
}
```

The parameters included in the responseBody object are:

| Parameter   | DataType | Description                                                                                                                   |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| clientData  | String   | The value sent in the request's clientData field.                                                                             |
| errorId     | Int      | A numeric error code.                                                                                                         |
| errorMsg    | String   | A textual description of the error, if there is one.                                                                          |
| uniqueMsgId | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes. |

## DeleteApplications

The DeleteApplications operation removes specified existing application entries in the PingFederate applications list.

This is the DeleteApplications URL:

```
https://idpxnyl3m.pingidentity.com/pingid/rest/4/deleteapplications/do
```

**Request Body Parameters**

Example reqBody object in the API payload:

```json
reqBody : {
    "applicationsIds": ["<application ID>"]
}
```

The parameters included in the reqBody object are:

| Parameter       | DataType      | Description                                                                                                                                                  |
| --------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| applicationsIds | List\<String> | The applications to be deleted, specified by their IDs.                                                                                                      |
| clientData      | String        | Optional.This value is returned unchanged in the API response.It can be used to save state and/or client context data for the application between API calls. |

**Response Body Parameters**

Example response body:

```json
{
  "responseBody": {
    "clientData": null,
    "errorId": 200,
    "errorMsg": null,
    "uniqueMsgId": "webs_9QxTikxO-MLHcFOTF9cX7kUQ4AzYwvM0q_Mt65QXwSI"
  }
}
```

The parameters included in the responseBody object are:

| Parameter   | DataType | Description                                                                                                                   |
| ----------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| clientData  | String   | The value sent in the request's clientData field.                                                                             |
| errorId     | Int      | A numeric error code.                                                                                                         |
| errorMsg    | String   | A textual description of the error, if there is one.                                                                          |
| uniqueMsgId | String   | A unique ID for the response message. This is logged and used to track the specific transaction for troubleshooting purposes. |

---
title: Creating a Resource
description: An action to create a user is performed by a POST operation. The JSON representation of the user (according to the SCIM schema) is POSTed to the User endpoint.
component: p14e-directory-api
page_id: p14e-directory-api::create-resource
canonical_url: https://developer.pingidentity.com/p14e-directory-api/create-resource.html
revdate: November 3, 2025
section_ids:
  creating-a-user: Creating a User
  creating-a-group: Creating a Group
---

# Creating a Resource

## Creating a User

An action to create a user is performed by a POST operation. The JSON representation of the user (according to the SCIM schema) is POSTed to the User endpoint.

```json
curl -v -X POST --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{
"schemas":["urn:scim:schemas:core:1.0"],
"userName":"marcher",
"password":"2Federate",
"active":true,
"name":{ "familyName":"Archer", "givenName":"Meredith" },
"emails": [ { "type": "work", "value": "meredith.archer@pingdevelopers.com" }]
}' \
https://directory-api.pingone.com/api/directory/user?option=DEFAULT_USER_GROUP
```

If an `externalId` value is specified in the request and a user with that external ID already exists, the request is treated as an update.

If you specify the `DEFAULT_USER_GROUP` option, the user is added to the directory Users group (the default group for new users). You can also replace `DEFAULT_USER_GROUP` with the UUID of a specific group to add the user to that group instead of the Users group.

To force the user to change their password during their next logon, set `urn:scim:schemas:com_pingone:1.0` to `{"passwordExpired": true}`.

A successful request will result in an HTTP `200 OK` response and the JSON representation of the user that was just created:

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id":"a7d67610-ceb5-4350-ba5a-746472c4f1f7",
  "schemas":[
    "urn:scim:schemas:core:1.0",
    "urn:scim:schemas:com_pingone:1.0"
  ],
  "urn:scim:schemas:com_pingone:1.0": {
    "createTimeStamp":1429123454227,
    "accountId":"a6538050-412a-4bca-a44d-07deb4b073a8",
    "lastModifiedTimeStamp":1429123454227,
    "directoryId":"90b3dfe3-f8d0-45ad-8c04-047c88b03137",
    "state":"ACTIVE"
  },
  "name":{
    "familyName":"Archer",
    "givenName":"Meredith"
  },
  "userName":"marcher",
  "active":true,
    "urn:scim:schemas:com_pingone:1.0":{
    "passwordExpired": true},
    "emails":[
    {
      "value":"meredith.archer@pingdevelopers.com",
      "type":"work"
    }
  ],
  "meta":{
   "lastModified":"2015-04-15T12:44:14.227-06:00",
   "location":"https://directory-api.pingone.com/api/directory/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7",
   "created":"2015-04-15T12:44:14.227-06:00"
  },
  "groups":[
    {
     "display":"Users",
     "value":"0b854f8d-a291-4e95-ad4b-68474a666e55"
    }
  ]
}
```

In the response, the `id` attribute contains the unique identifier for this user in the PingOne for Enterprise directory. To modify this user (such as adding them to other groups), you reference them using the `id` attribute value. The `location` attribute contains the full resource URL that you use to manipulate the resource in the next sections.

## Creating a Group

Creating a group is a similar process as creating a user, performing a POST operation against the Group endpoint:

```shell
curl -v -X POST --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d ' {
"schemas":["urn:scim:schemas:core:1.0"],
"displayName":"Software Developers" }' \
https://directory-api.pingone.com/api/directory/group
```

A successful request will result in an HTTP `200 OK` response and the JSON representation of the group that was just created:

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id":"7c513a7e-55d4-441c-858c-7329e6268084",
  "displayName":"Software Developers",
  "schemas":[
    "urn:scim:schemas:core:1.0",
    "urn:scim:schemas:com_pingone:1.0"
  ],
  "meta":{
    "lastModified":"2015-04-16T10:08:22.324-06:00",
    "created":"2015-04-16T10:08:22.324-06:00",
    "location":"https://directory-api.pingone.com/api/directory/group/7c513a7e-55d4-441c-
    858c-7329e6268084"
  },
  "urn:scim:schemas:com_pingone:1.0": {
    "createTimeStamp":1429200502324,
    "lastModifiedTimeStamp":1429200502324,
    "accountId":"a6538050-412a-4bca-a44d-07deb4b073a8",
    "directoryId":"90b3dfe3-f8d0-45ad-8c04-047c88b03137"
  }
}
```
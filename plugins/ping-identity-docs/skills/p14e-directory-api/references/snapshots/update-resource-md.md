---
title: Updating a Resource
description: Resources can be updated using either the PUT or PATCH operation.
component: p14e-directory-api
page_id: p14e-directory-api::update-resource
canonical_url: https://developer.pingidentity.com/p14e-directory-api/update-resource.html
revdate: November 3, 2025
section_ids:
  put-operation: PUT operation
  patch-operation: Patch operation
---

# Updating a Resource

Resources can be updated using either the PUT or PATCH operation.

## PUT operation

Resource modifications are performed using a PUT operation, which returns the entire user profile with the changes applied. For example, to add a title to Meredith's record, take the contents of a GET request, add in the `title` attribute, and PUT it back to Meredith's User resource location.

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some attributes are not enabled by default in PingOne for Enterprise Directory. You might need to enable the attribute in the PingOne for Enterprise administration console before modifying the record. |

```shell
curl -v "X PUT --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{
"id":"a7d67610-ceb5-4350-ba5a-746472c4f1f7",
"schemas":[ "urn:scim:schemas:core:1.0", "urn:scim:schemas:com_pingone:1.0" ],
"urn:scim:schemas:com_pingone:1.0":{
"createTimeStamp":1429123454227,
"accountId":"a6538050-412a-4bca-a44d-07deb4b073a8",
"lastModifiedTimeStamp":1429123454227,
"directoryId":"90b3dfe3-f8d0-45ad-8c04-047c88b03137",
"state":"ACTIVE" },
"name":{ "familyName":"Archer", "givenName":"Meredith" },
"userName":"marcher",
"title":"Software Developer",
"active":true,
"emails":[{"value":"meredith.archer@pingdevelopers.com","type":"work" }],
"meta":{
"lastModified":"2015-04-15T12:44:14.227-06:00",
"location":"https://directory-api.pingone.com/api/directory/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7",
"created":"2015-04-15T12:44:14.227-06:00" },
"groups":[{ "display":"Users", "value":"0b854f8d-a291-4e95-ad4b-68474a666e55" }]
}' \
https://directory-api.pingone.com/api/directory/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7
```

A successful response from a modify operation is the user profile returned in full:

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id":"a7d67610-ceb5-4350-ba5a-746472c4f1f7",
  "schemas":[
    "urn:scim:schemas:core:1.0",
    "urn:scim:schemas:com_pingone:1.0"
  ],
  "urn:scim:schemas:com_pingone:1.0":{
    "createTimeStamp":1429123454227,
    "accountId":"a6538050-412a-4bca-a44d-07deb4b073a8",
    "lastModifiedTimeStamp":1429123456527,
    "directoryId":"90b3dfe3-f8d0-45ad-8c04-047c88b03137",
    "state":"ACTIVE"
  },
  "name":{
    "familyName":"Archer",
    "givenName":"Meredith"
  },
  "userName":"marcher",
  "title":"Software Developer",
  "active":true,
  "emails":[
    {
      "value":"meredith.archer@pingdevelopers.com",
      "type":"work"
    }
  ],
  "meta":{
    "lastModified":"2015-04-15T12:46:18.224-06:00",
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

## Patch operation

The PATCH operation can be used to simplify changes to large multivalued attributes, such as the membership of a group resource. To add a new member to a group resource, you need to know the `id` value and resource type (User or Group) of the resource that you want to add. The request to add a user (Meredith) to the Software Developers group using the PATCH operation is as follows:

```shell
curl -v -X PATCH --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{ "members" : [{ "value" : "a7d67610-ceb5-4350-ba5a-746472c4f1f7", "type" : "User" }] }' \
https://directory-api.pingone.com/api/directory/group/7c513a7e-55d4-441c-858c-7329e6268084
```

To remove a member from the group, include an `operation` attribute with the value of "delete", for example to remove Meredith from the Software Developers group:

```shell
curl -v -X PATCH --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{ "members" : [{ "value" : "a7d67610-ceb5-4350-ba5a-746472c4f1f7", , "type" : "User", "operation" : "delete"
}] }' \
https://directory-api.pingone.com/api/directory/group/7c513a7e-55d4-441c-858c-7329e6268084
```
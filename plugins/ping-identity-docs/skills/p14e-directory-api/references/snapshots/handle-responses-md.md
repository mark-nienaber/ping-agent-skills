---
title: Handling Responses
description: In most scenarios, the API response will be the complete SCIM representation of the resource. This means that a DELETE action will not return a SCIM object. Here's an example of a successful API response to create a request:
component: p14e-directory-api
page_id: p14e-directory-api::handle-responses
canonical_url: https://developer.pingidentity.com/p14e-directory-api/handle-responses.html
revdate: October 30, 2025
---

# Handling Responses

In most scenarios, the API response will be the complete SCIM representation of the resource. This means that a DELETE action will not return a SCIM object. Here's an example of a successful API response to create a request:

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

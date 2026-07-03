---
title: Reading a Resource
description: You can retrieve a specific user's directory profile by:
component: p14e-directory-api
page_id: p14e-directory-api::read-resource
canonical_url: https://developer.pingidentity.com/p14e-directory-api/read-resource.html
revdate: November 3, 2025
---

# Reading a Resource

You can retrieve a specific user's directory profile by:

* Querying for the user by performing a GET operation against the User endpoint

* Retrieving the user by performing a GET operation against the User resource directly

To query for a user, use the SCIM query language to form your query. Learn more in the [SCIM specification](https://scim.cloud/). To retrieve the recently created user, use the filter `username eq "marcher"`, which will be URL-encoded and appended to the User endpoint as the `filter` parameter:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-X GET https://directory-api.pingone.com/api/directory/user?filter=userName%20eq%20%22marcher%22
```

Alternatively, you can perform a GET directly on the user resource, which is defined in the `location` attribute in the `meta` section of the user record. Both the previous example and this one will return the same result. So, to retrieve Meredith's profile directly, you can also perform the following command:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-X GET https://directory-api.pingone.com/api/directory/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7
```

A successful request will result in an HTTP `200 OK` response and the JSON representation of the user:

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

Additionally, you can retrieve the details for all users in the directory. In this case, don't specify a user filter and set the `startIndex` and `count` parameters to determine the number of users to return:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-X GET https://directory-api.pingone.com/api/directory/user?sortBy=userName&sortOrder=ascending&startIndex=1&count=100
```

The `startIndex` value is the position at which user retrieval will begin, and `count` is the number of users to return per page. The maximum count value is 1000. If you need to retrieve more than 1000 users, you must use multiple calls, increasing the `startIndex` value by 1000 each time until all users are returned.
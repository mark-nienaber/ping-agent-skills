---
title: Group Membership Count
description: Here's an example of querying for the number of direct user membership of a group:
component: p14e-directory-api
page_id: p14e-directory-api::group-membership-count
canonical_url: https://developer.pingidentity.com/p14e-directory-api/group-membership-count.html
revdate: October 30, 2025
---

# Group Membership Count

Here's an example of querying for the number of direct user membership of a group:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
https://directory-api.pingone.com/api/directory/group/7c513a7e-55d4-441c-858c-7329e6268084/users/count
```

This returns the number of users in a JSON object:

```json
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "users" : 1
}
```

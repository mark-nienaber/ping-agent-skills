---
title: Deleting a Resource
description: To delete a resource (user or group), use the DELETE operation against the resource endpoint. The following command deletes Meredith from the directory and returns an HTTP 200 OK message if successful.
component: p14e-directory-api
page_id: p14e-directory-api::delete-resource
canonical_url: https://developer.pingidentity.com/p14e-directory-api/delete-resource.html
revdate: October 30, 2025
---

# Deleting a Resource

To delete a resource (user or group), use the DELETE operation against the resource endpoint. The following command deletes Meredith from the directory and returns an HTTP `200 OK` message if successful.

```shell
curl -v "X DELETE --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh
-H "Content-Type: application/json" \
-H "Accept: application/json" \
https://directory-api.pingone.com/api/directory/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7
```

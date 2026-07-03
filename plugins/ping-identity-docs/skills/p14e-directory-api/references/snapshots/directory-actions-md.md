---
title: Directory Actions
description: The SCIM protocol uses the REST concept to define the actions a SCIM consumer can perform on a resource managed by PingOne for Enterprise Directory (a SCIM service provider). The following actions can be performed against user resources and group resources in the directory:
component: p14e-directory-api
page_id: p14e-directory-api::directory-actions
canonical_url: https://developer.pingidentity.com/p14e-directory-api/directory-actions.html
revdate: October 30, 2025
---

# Directory Actions

The SCIM protocol uses the REST concept to define the actions a SCIM consumer can perform on a resource managed by PingOne for Enterprise Directory (a SCIM service provider). The following actions can be performed against user resources and group resources in the directory:

| HTML Verb | Action                                                                                                                                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GET       | [Reads](read-resource.html) / queries for a resource or resources from the service provider.                                                                       |
| POST      | [Creates](create-resource.html) a new resource at the service provider.                                                                                            |
| PUT       | [Updates](update-resource.html) an existing resource. This action requires the entire resource provided in the body, making it more like a replace than an update. |
| PATCH     | [Updates](update-resource.html) an existing resource with changes to multi-value attributes (such as group membership).                                            |
| DELETE    | [Deletes](delete-resource.html) a resource at the service provider.                                                                                                |

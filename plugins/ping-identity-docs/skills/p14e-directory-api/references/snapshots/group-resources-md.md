---
title: Group Resources
description: Groups are represented by the SCIM group object. Groups can contain either group or user resources as members, allowing for nested group support. The group object also supports the PATCH operation for group membership changes.
component: p14e-directory-api
page_id: p14e-directory-api::group-resources
canonical_url: https://developer.pingidentity.com/p14e-directory-api/group-resources.html
revdate: October 30, 2025
---

# Group Resources

Groups are represented by the SCIM group object. Groups can contain either group or user resources as members, allowing for nested group support. The group object also supports the PATCH operation for group membership changes.

A group resource can be queried by the following API endpoint:

`https://directory-api.pingone.com/api/directory/group`

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For directories located in the European region, the API host is `https://directory-api.pingone.eu`, and for those in the APAC region, it's `https://directory-api.pingone.com.au`. |

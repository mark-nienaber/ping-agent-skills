---
title: User Resources
description: The user resource represents a user or identity profile in the directory. PingOne for Enterprise Directory supports the following SCIM schemas:
component: p14e-directory-api
page_id: p14e-directory-api::user-resources
canonical_url: https://developer.pingidentity.com/p14e-directory-api/user-resources.html
revdate: November 3, 2025
---

# User Resources

The user resource represents a user or identity profile in the directory. PingOne for Enterprise Directory supports the following SCIM schemas:

* SCIM Core Schema: `urn:scim:schemas:core:1.0`

* SCIM Enterprise User Schema: `urn:scim:schemas:extension:enterprise:1.0`

* PingOne Schema: `urn:scim:schemas:com_pingone:1.0`

A user resource can be queried by the following API endpoint:

`https://directory-api.pingone.com/api/directory/user`

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For directories located in the European region, the API host is `https://directory-api.pingone.eu`, and for those in the APAC region, it's `https://directory-api.pingone.com.au`. |

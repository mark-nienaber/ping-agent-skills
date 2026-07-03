---
title: SCIM 1.1 Developer Guide
description: SCIM or System for Cross-Domain Identity Management is a federated provisioning protocol. Providing a consistent API for user and group CRUD (Create, Read, Update and Delete) actions.
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:index
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/index.html
revdate: May 3, 2021
page_aliases: ["dev_scim11_overview.adoc"]
---

# SCIM 1.1 Developer Guide

SCIM or System for Cross-Domain Identity Management is a federated provisioning protocol. Providing a consistent API for user and group CRUD (Create, Read, Update and Delete) actions.

SCIM can be used by developers to standardize the way user profile information is retrieved from a data source (i.e. instead of having to manage connections to SQL tables, LDAP datastores and other data stores SCIM can provide a single interface to this data).

SCIM can also be used to provision user and group information from an enterprise to a partner (i.e. SaaS application) either as an out-of-band process or as part of an authentication action.

This developers guide provides a reference for developers to build against a SCIM data store interface to help standardize the method used to access identity data in a federated manner. It uses information from the SCIM v1.1 specifications (specifically the core schema and the SCIM API).

This developer guide references the SCIM v1.1 specifications:

* [SCIM Core Schema 1.1](http://www.simplecloud.info/specs/draft-scim-core-schema-01.html)

* [SCIM Protocol API 1.1](http://www.simplecloud.info/specs/draft-scim-api-01.html)

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although this guide provides raw protocol calls, it is highly recommended a developer utilize existing libraries to avoid implementation specific errors. |

---

---
title: "SCIM Action: Create a Resource"
description: SCIM resources are created using HTTP POST verb. The body of the call contains a JSON formatted SCIM schema resource.
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:create-resource
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/create-resource.html
revdate: September 30, 2020
page_aliases: ["dev_scim11_create_resource.adoc"]
section_ids:
  creating-a-user: Creating a User
  creating-a-group: Creating a Group
---

# SCIM Action: Create a Resource

SCIM resources are created using HTTP POST verb. The body of the call contains a JSON formatted SCIM schema resource.

## Creating a User

A user create is performed by a POST operation. The JSON representation of the user (according to the SCIM schema) is POSTed to the User endpoint.

```shell
curl -v -X POST --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{
"schemas":["urn:scim:schemas:core:1.0"],
"userName":"marcher",
"password":"2Federate",
"active":true,
"name":{ "familyName":"Archer", "givenName":"Meredith" },
"emails": [ { "type": "work", "value": "meredith.archer@pingdevelopers.com }]
}' \
https://directory-api.pingone.com:443/api/directory/user
```

A successful request will result in a HTTP 200 OK response and the JSON representation of the user that was just created:

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id":"a7d67610-ceb5-4350-ba5a-746472c4f1f7",
  "schemas": [
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
  "name": {
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
  "meta": {
    "lastModified":"2015-04-15T12:44:14.227-06:00",
    "location":"https://directory-api.pingone.com/v1/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7",
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

In the response, the id attribute contains the unique identifier for this user in the PingOne Directory. To modify this user, add them to groups etc you will reference them via this attribute value. The location attribute contains the full resource URL that you will use to manipulate the resource in the next sections.

## Creating a Group

Creating a group is a similar process, performing a POST operation against the Group endpoint:

```shell
curl -v -X POST --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d ' {
"schemas":["urn:scim:schemas:core:1.0"],
"displayName":"Software Developers" }' \
https://directory-api.pingone.com:443/api/directory/group
```

A successful request will result in a HTTP 200 OK response and the JSON representation of the group that was just created:

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "id":"7c513a7e-55d4-441c-858c-7329e6268084",
  "displayName":"Software Developers",
  "schemas": [
    "urn:scim:schemas:core:1.0",
    "urn:scim:schemas:com_pingone:1.0"
  ],
  "meta": {
    "lastModified":"2015-04-16T10:08:22.324-06:00",
    "created":"2015-04-16T10:08:22.324-06:00",
    "location":"https://directory-api.pingone.com/v1/group/7c513a7e-55d4-441c-858c-7329e6268084"
  },
  "urn:scim:schemas:com_pingone:1.0": {
    "createTimeStamp":1429200502324,
    "lastModifiedTimeStamp":1429200502324,
    "accountId":"a6538050-412a-4bca-a44d-07deb4b073a8",
    "directoryId":"90b3dfe3-f8d0-45ad-8c04-047c88b03137"
  }
}
```

---

---
title: "SCIM Action: Delete a Resource"
description: To delete a resource (user or group) you will use the DELETE operation against the resource's endpoint. The following command will delete Meredith from the directory and return a 200 OK message if successful.
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:delete-resource
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/delete-resource.html
revdate: September 30, 2020
page_aliases: ["dev_scim11_delete_resource.adoc"]
---

# SCIM Action: Delete a Resource

To delete a resource (user or group) you will use the DELETE operation against the resource's endpoint. The following command will delete Meredith from the directory and return a 200 OK message if successful.

```shell
curl -v -X DELETE --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
https://directory-api.pingone.com/v1/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7
```

---

---
title: "SCIM Action: Read a Resource"
description: To retrieve or read a resource from the SCIM Service Provider, the HTTP GET verb is used. There are two mechanisms that can be used to retrieve a user - via a filter or directly. These are both described below.
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:read-resource
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/read-resource.html
revdate: September 30, 2020
page_aliases: ["dev_scim11_read_resource.adoc"]
section_ids:
  retrieving-users-via-filter: Retrieving Users via Filter
  retrieving-users-directly: Retrieving Users Directly
---

# SCIM Action: Read a Resource

To retrieve or read a resource from the SCIM Service Provider, the HTTP GET verb is used. There are two mechanisms that can be used to retrieve a user - via a filter or directly. These are both described below.

The SCIM query defines filters that can be used to constrain the returned list of users as well as sorting and pagination mechanisms.NOTE: SCIM query, sort and pagination functionality is optional in the SCIM specifications so varying degrees of support may be found in SCIM Service Providers.

## Retrieving Users via Filter

To query for a user you will use the SCIM filter language to form your query. The filter language is fairly straightforward and the operators are defined below:

|    |                       |                                                                                                                                                                                                                                                                               |
| -- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eq | equal                 | The attribute and operator values must be identical for a match.                                                                                                                                                                                                              |
| co | contains              | The entire operator value must be a substring of the attribute value for a match.                                                                                                                                                                                             |
| sw | starts with           | The entire operator value must be a substring of the attribute value, starting at the beginning of the attribute value. This criterion is satisfied if the two strings are identical.                                                                                         |
| pr | present (has value)   | If the attribute has a non-empty value, or if it contains a non-empty node for complex attributes there is a match.                                                                                                                                                           |
| gt | greater than          | If the attribute value is greater than operator value, there is a match. The actual comparison is dependent on the attribute type. For string attribute types, this is a lexicographical comparison and for DateTime types, it is a chronological comparison.                 |
| ge | greater than or equal | If the attribute value is greater than or equal to the operator value, there is a match. The actual comparison is dependent on the attribute type. For string attribute types, this is a lexicographical comparison and for DateTime types, it is a chronological comparison. |
| lt | less than             | If the attribute value is less than operator value, there is a match. The actual comparison is dependent on the attribute type. For string attribute types, this is a lexicographical comparison and for DateTime types, it is a chronological comparison.                    |
| le | less than or equal    | If the attribute value is less than or equal to the operator value, there is a match. The actual comparison is dependent on the attribute type. For string attribute types, this is a lexicographical comparison and for DateTime types, it is a chronological comparison.    |

A simple example of a SCIM filter is to find a specific record by username:

```
username eq "marcher"
```

The filter expressions can be joined using the "and" and "or" logical operators and grouped via parentheses, for example to find all users who have a familyName that starts with "A" and have been modified since the 1st January 2015 we can use the filter:

```
(name.familyName sw "A") and (urn:scim:schemas:com_pingone:1.0:createTimeStamp gt 1420084800000)
```

|   |                                                                                       |
| - | ------------------------------------------------------------------------------------- |
|   | When submitting the GET request with a filter, be sure to urlencode the filter value. |

To retrieve our recently created user we will use the filter: username eq marcher which will be urlencoded and appended to the User endpoint as the filter parameter. Both requests below will result in the same response:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
https://directory-api.pingone.com/api/directory/user?filter=userName%20eq%20%22marcher%22
```

## Retrieving Users Directly

If we know the resources location value, we can perform a GET directly on the user resource (which is defined in the "location" attribute in the "meta" section of the user record). So to retrieve Meredith's profile directly I can also perform the following command:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
https://directory-api.pingone.com/v1/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7
```

A successful request will result in a HTTP 200 OK response and the JSON representation of the user:

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
{
  "id":"a7d67610-ceb5-4350-ba5a-746472c4f1f7",
  "schemas": [
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
  "name": {
    "familyName":"Archer",
    "givenName":"Meredith"
  },
  "userName":"marcher",
  "active":true,
  "emails": [
    {
      "value":"meredith.archer@pingdevelopers.com",
      "type":"work"
    }
  ],
  "meta": {
    "lastModified":"2015-04-15T12:44:14.227-06:00",
    "location":"https://directory-api.pingone.com/v1/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7",
    "created":"2015-04-15T12:44:14.227-06:00"
  },
  "groups": [
    {
      "display":"Users",
      "value":"0b854f8d-a291-4e95-ad4b-68474a666e55"
    }
  ]
}
```

---

---
title: "SCIM Action: Update a Resource"
description: "SCIM resource modifications are performed using a PUT operation returning the entire profile with the changes applied. For example, to add a \"title\" to Meredith's record I will take the contents of a GET request, add in the title attribute and PUT it back to Meredith's User resource location."
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:update-resource
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/update-resource.html
revdate: September 30, 2020
page_aliases: ["dev_scim11_update_resource.adoc"]
---

# SCIM Action: Update a Resource

SCIM resource modifications are performed using a PUT operation returning the entire profile with the changes applied. For example, to add a "title" to Meredith's record I will take the contents of a GET request, add in the title attribute and PUT it back to Meredith's User resource location.

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
  "location":"https://directory-api.pingone.com/v1/user/a7d67610-ceb5-4350-ba5a-
746472c4f1f7",
  "created":"2015-04-15T12:44:14.227-06:00" },
"groups":[{ "display":"Users", "value":"0b854f8d-a291-4e95-ad4b-68474a666e55" }]
}' \
https://directory-api.pingone.com/v1/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7
```

A successful response from a modify operation is the user profile returned in full:

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8

{
  "id":"a7d67610-ceb5-4350-ba5a-746472c4f1f7",
  "schemas": [
    "urn:scim:schemas:core:1.0",
    "urn:scim:schemas:com_pingone:1.0"
  ],
  "urn:scim:schemas:com_pingone:1.0": {
    "createTimeStamp":1429123454227,
    "accountId":"a6538050-412a-4bca-a44d-07deb4b073a8",
    "lastModifiedTimeStamp":1429123456527,
    "directoryId":"90b3dfe3-f8d0-45ad-8c04-047c88b03137",
    "state":"ACTIVE"
  },
  "name": {
    "familyName":"Archer",
    "givenName":"Meredith"
  },
  "userName":"marcher",
  "title":"Software Developer",
  "active":true,
  "emails": [
    {
      "value":"meredith.archer@pingdevelopers.com",
      "type":"work"
    }
  ],
  "meta": {
    "lastModified":"2015-04-15T12:46:18.224-06:00",
    "location":"https://directory-api.pingone.com/v1/user/a7d67610-ceb5-4350-ba5a-746472c4f1f7",
    "created":"2015-04-15T12:44:14.227-06:00"
  },
  "groups": [
    {
      "display":"Users",
      "value":"0b854f8d-a291-4e95-ad4b-68474a666e55"
    }
  ]
}
```

---

---
title: SCIM Actions
description: The SCIM protocol uses the REST concept to define the actions a SCIM Consumer can perform on a resource managed by a SCIM Service Provider. These actions are:
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:scim-actions
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/scim-actions.html
revdate: September 30, 2020
page_aliases: ["dev_scim11_overview_actions.adoc"]
---

# SCIM Actions

The SCIM protocol uses the REST concept to define the actions a SCIM Consumer can perform on a resource managed by a SCIM Service Provider. These actions are:

|        |                                                                                                                                          |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| GET    | Reads a resource (or resources) from the Service Provider                                                                                |
| POST   | Creates a new resource at the Service Provider                                                                                           |
| PUT    | Updates an existing resource, as this action requires the entire resource provided in the body, it is more like a replace than an update |
| PATCH  | Updates an existing resource with changes (where supported).	The PATCH action is optional and not supported in some implementations      |
| DELETE | Deletes a resource at the Service Provider                                                                                               |

---

---
title: SCIM Components and Roles
description: SCIM contains three main components, as with a number of the federation protocols, the terminology can be slightly confusing so we describe the components below:
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:scim-components-roles
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/scim-components-roles.html
revdate: September 30, 2020
page_aliases: ["dev_scim11_overview_components_roles.adoc"]
---

# SCIM Components and Roles

SCIM contains three main components, as with a number of the federation protocols, the terminology can be slightly confusing so we describe the components below:

* **Service Provider** The provider of the identity information (in a traditional enterprise scenario, the SCIM Service Provider is most likely the same as the SAML Identity Provider). For a majority of this guide we will use the PingOne Directory as an example of a SCIM Service Provider.

* **SCIM Consumer** The application or service that will consume the SCIM data. For example in a federated provisioning scenario, the SCIM Consumer will be the 3rd party receiving the identity information.

* **Resource** The object (i.e. a User or a Group) that the SCIM request is being performed on.

---

---
title: SCIM Schema
description: SCIM provides a standard schema that can be used to represent a user or a group. This schema is extensible so additional schema objects can be added to provide custom schema support.
component: developer-resources
page_id: developer-resources:scim_11_developer_guide:scim-schema
canonical_url: https://docs.pingidentity.com/developer-resources/scim_11_developer_guide/scim-schema.html
revdate: September 30, 2020
page_aliases: ["dev_scim11_schema.adoc"]
section_ids:
  scim-data-types: SCIM Data Types
  scim-attribute-types: SCIM Attribute Types
  common-schema-attributes: Common Schema Attributes
  scim-user-attributes: SCIM User Attributes
  group-schema-attributes: Group Schema Attributes
---

# SCIM Schema

SCIM provides a standard schema that can be used to represent a user or a group. This schema is extensible so additional schema objects can be added to provide custom schema support.

Along with the SCIM schema, specific data types are defined to simplify interoperability between partners.

## SCIM Data Types

The SCIM core schema has a support for common data types to provide maximum interoperability between SCIM Service Providers and SCIM Consumers. The following data types are available in the SCIM specification and examples are provided in JSON representation:

|                                 |                                    |
| ------------------------------- | ---------------------------------- |
| String                          | "familyName" : "Archer"            |
| Boolean                         | "active" : true                    |
| Decimal                         | "weight" : 173.2                   |
| Integer                         | "age" : 36                         |
| DateTime (xml date/time format) | "created" : "2015-05-18T15:00:00Z" |
| Binary (base64 encoded string)  | "photo" : "U2F5IENoZWVzZSE="       |

## SCIM Attribute Types

Attributes in SCIM can be either single-valued or multi-valued and SCIM can support complex attributes where an attribute can be comprised of multiple single or multi-valued sub attributes, for example:

|                                  |                                                                                                                                                               |                                                                                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simple Attribute (single-valued) | An attribute that contains a single value                                                                                                                     | ```json
{
  "displayName": "Archer, Meredith A"
}
```                                                                                                                                                      |
| Simple Attribute (multi-valued)  | An attribute that contains multiple values. Multiple values can include a "type" attribute to define the type of value specified (i.e. work vs home address). | ```json
{
  "emails": [
    {
      "type" : "other",
      "value" : "marcher@pingdevelopers.com"
    },
    {
      "type": "work",
      "value" : "meredith.archer@pingdevelopers.com"
    }
  ]
}
``` |
| Complex Attribute                | An attribute that contains one or more simple attributes                                                                                                      | ```json
{
  "name":
    {
      "familyName": "Archer",
      "givenName": "Meredith",
      "displayName" : "Archer, Meredith A"
    }
}
```                                                              |
| Sub-Attribute                    | An attribute that is a member of a complex attribute.                                                                                                         | using the previous example, "familyName" is a sub-attribute of "name"                                                                                                                                      |

## Common Schema Attributes

Common schema elements must be included on all resources and are used to provide a reference identifier for the resource as well as information about the resource:

|              |      |                       |                                                                                                                                                  |
| ------------ | ---- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| id           |      | String                | Unique identifier for the resource as defined by the Service Provider \[REQUIRED]                                                                |
| externalId   |      | String                | Identifier for the resource as defined by the SCIM Consumer (i.e. a local identifier or customerId in an application) \[REQUIRED]                |
| meta         |      | Complex Attribute     | The resources metadata, the "meta" complex attribute may consist of the following attributes: \[REQUIRED]                                        |
| created      | meta | DateTime              | When the resource was created                                                                                                                    |
| lastModified | meta | DateTime              | When the resource was last modified (if the resource has not been modified since creation, this value will be the same as the created attribute) |
| location     | meta | String                | The direct URI of the resource. You can use this URI to directly manage a resource rather than searching for it and then modifying.              |
| version      | meta | String                | (if supported). The version of the resource being returned.                                                                                      |
| attributes   | meta | String (multi-valued) | (if supported). Contains the list of attributes to remove during a PATCH operation.                                                              |

## SCIM User Attributes

A SCIM User consists of one required attribute (userName) and additional descriptive attributes:

|                   |           |                                |                                                                                                                                                 |
| ----------------- | --------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| userName          |           | String                         | Unique identifier for the User as described by the SCIM Consumer (typically the user name used to login) \[REQUIRED]                            |
| name              |           | Complex Attribute              | Components of the user's real name:                                                                                                             |
| formatted         | name      | String                         | The formatted representation of the user (i.e. "Ms Meredith Anne Archer, II")                                                                   |
| familyName        | name      | String                         | Family or last name of the user (i.e. Archer)                                                                                                   |
| givenName         | name      | String                         | Given or first name of the user (i.e. Meredith)                                                                                                 |
| middleName        | name      | String                         | The middle name(s) or initial(s) of the user (i.e. Anne)                                                                                        |
| honorificPrefix   | name      | String                         | Honorific or personal title of the user (i.e. Mr, Ms)                                                                                           |
| honorificSuffix   | name      | String                         | Honorific or generational suffix of the user (i.e. Jr, II)                                                                                      |
| displayName       |           | String                         | How the user name should be presented in an application, this is not necessarily tied to the formatted name attribute (i.e. Archer, Meredith A) |
| nickName          |           | String                         | Casual or preferred representation of the user's name (i.e. Bob rather than Robert)                                                             |
| profileUrl        |           | String                         | A fully qualified URL of the users profile (i.e. https\://profiles.pingdevelopers.com/marcher)                                                  |
| title             |           | String                         | Work title of the user (i.e. "Software Developer")                                                                                              |
| userType          |           | String                         | Defines the relationship of the user to the SCIM Service Provider organization (i.e. Employee)                                                  |
| preferredLanguage |           | String                         | User's preferred language and dialect (i.e. en\_US)                                                                                             |
| locale            |           | String                         | User's locale for localization purposes (currency, date time format etc) (i.e. en\_US)                                                          |
| timezone          |           | String                         | User's timezone in the "Olson" timezone database format (i.e. America/Denver)                                                                   |
| active            |           | Boolean                        | Whether the user is active at the Service Provider                                                                                              |
| password          |           | String                         | WRITE-ONLY. The user's clear-text password. Can only be provided in a POST operation (for a create) or a PUT operation for a password change.   |
| emails            |           | String Multi-valued            | Email address(es) for the user. Common "type" values are work, home, other.                                                                     |
| phoneNumbers      |           | String Multi-valued            | Telephone number(s) for the user. Common "type" values are work, home, fax, pager, mobile, other.                                               |
| ims               |           | String Multi-valued            | Instant messaging address(es) for the user. Common "type" values are gtalk, icq, aim, skype                                                     |
| photos            |           | String Multi-valued            | URL of a profile photo for the user. Common "type" values are thumbnail, photo                                                                  |
| addresses         |           | Complex Attribute Multi-Valued | Physical mailing address for the user. Common "type" values are home, work, other                                                               |
| formatted         | addresses | String                         | Full mailing address formatted for display (i.e. 1001 17th Street\nSuite 100\nDenver CO 80202)                                                  |
| streetAddress     | addresses | String                         | Full street address component (i.e. 1001 17th Street\nSuite 100)                                                                                |
| locality          | addresses | String                         | The city or locality (i.e. Denver)                                                                                                              |
| region            | addresses | String                         | The region / state / province of the address (i.e. CO)                                                                                          |
| postalCode        | addresses | String                         | The postal code or zipcode of the address (i.e. 80202)                                                                                          |
| country           | addresses | String                         | ISO3166-1 alpha 2 "short" format of the country (i.e. US)                                                                                       |
| groups            |           | String Multi-Valued            | List of groups the user belongs to                                                                                                              |
| entitlements      |           | Undefined Multi-Valued         | List of entitlements for the user (SCIM doesn't specify a format for these entitlements)                                                        |
| roles             |           | String Multi-Valued            | List of roles the user has (although SCIM doesn't specify a format for roles, its expected that they are a list of String values)               |
| x509Certificates  |           | Binary                         | List of x509 certificates for the user. Value is a binary (base64 encoded) DER encoded x509 certificate.                                        |

## Group Schema Attributes

A group resource can be used to define roles or groups a user is a member of.NOTE: Groups can be nested inside other groups to provide users with indirect membership of a group.

|             |   |                     |                                                                                                                                                             |
| ----------- | - | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| displayName |   | String              | Human readable name for the group \[REQUIRED]                                                                                                               |
| members     |   | String Multi-Valued | List of members of the group, the value will be the "id" value of the resource (user or group) and the multi-valued attribute type may be "user" or "group" |
---
title: Advanced Identity Cloud identity schema
description: Overview of the default and customizable identity schema for managing identity entities
component: pingoneaic
page_id: pingoneaic:identities:identity-cloud-identity-schema
canonical_url: https://docs.pingidentity.com/pingoneaic/identities/identity-cloud-identity-schema.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Data Object Model", "Schema", "Custom Properties"]
section_ids:
  summary-of-the-identity-schema: Summary of the identity schema
  use-cases-for-customizing-the-identity-schema: Use cases for customizing the identity schema
---

# Advanced Identity Cloud identity schema

PingOne Advanced Identity Cloud uses a default identity schema to organize users, roles, assignments, groups, organizations, and applications. The following diagram shows the identity schema relationships:

![idcloud identity schema](_images/idcloud-identity-schema.png)

Learn more about the Advanced Identity Cloud identity schema in [Summary of the identity schema](#summary-of-the-identity-schema).

You can customize the default identity schema to your business needs in the following ways:

* Create custom properties to store identity information specific to your business.

* Create indexable custom properties that let you search your identities and create customized segments.

* Create [organizations](organizations.html) to structure your identities in a flexible and performant way.

For examples of customizing the Advanced Identity Cloud identity schema, learn more in [Use cases for customizing the identity schema](#use-cases-for-customizing-the-identity-schema).

## Summary of the identity schema

* Users, roles, assignments, groups, organizations, and applications form the default identity schema. Their relationships are also part of the default schema.

* Users are *hybrid* object types:

  * Their default properties are explicitly defined in the schema with indexes also explicitly defined for these properties. These default properties include:

    * `givenName`

    * `mail`

    * `passwordLastChangedTime`

    * `passwordExpirationTime`

    * `sn`

    * `userName`

  * You can add custom properties to them. However, the properties are stored in an unindexed JSON data structure.

  * If you need a custom property for a user to be searchable, use an [indexed extension property](customize-object-types.html#use-general-purpose-extension-attributes) instead of a custom property.

* Roles, assignments, groups, and organizations are *generic* object types:

  * None of their properties are explicitly defined in the schema, and instead they are entirely stored in an indexed JSON data structure.

  * You can add custom properties to them, and they'll also be indexed.

* You can create custom object types. These custom object types are also generic. This means that they are entirely stored in an indexed JSON data structure.

* Applications are also generic object types. However, you shouldn't alter these in any way as they're reserved for modification by Ping Identity to support workforce use cases. You shouldn't add custom properties to them, repurpose their default properties, or reconcile data into them.

|   |                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - Advanced Identity Cloud doesn't support the modification of application object types.

- Ping Identity recommends that you add no more than 12 custom properties each to roles, assignments, groups, and organizations, as this can impact the performance of your tenant environments. |

The following table summarizes the identity schema:

| Object type                            | Type    | Indexes on default properties?           | Indexes on custom properties?              |
| -------------------------------------- | ------- | ---------------------------------------- | ------------------------------------------ |
| Users                                  | Hybrid  | [icon: check, set=fa]Yes (where defined) | [icon: times, set=fa]No                    |
| Roles Assignments Groups Organizations | Generic | [icon: check, set=fa]Yes (all)           | [icon: check, set=fa]Yes (all)             |
| Applications                           | Generic | [icon: check, set=fa]Yes (all)           | n/a (customer modifications not supported) |
| Custom                                 | Generic | n/a                                      | [icon: check, set=fa]Yes (all)             |

## Use cases for customizing the identity schema

The following are examples of how you might customize the default schema to support a media service:

* Add a custom property for membership level to user identities to support subscription-level access or rate limiting. For example, the membership levels might be "gold", "silver", and "bronze".

* Add a custom property for registration level to user identities to support access to premium content or to support progressive profiling in journeys. For example, the registration levels might be "guest", "pending", and "registered".

* Adapt a general purpose extension property to be a searchable user property for date of birth to support age-restricted access. Use the property to support delegated administration for different age segments, allowing separate users to administrate adults and children.

* Create organizations to structure user relationships between family members to support parental control.

The following are examples of how you might customize the default schema to support workforce:

* Add custom properties for job code, department number, or cost center to user identities to support the automatic provisioning of birthright roles.

* Add custom properties for external ID and metadata to user identities to support synchronization using System for Cross-domain Identity Management (SCIM).

Learn more about customizing the identity schema in [Customize managed object types](customize-object-types.html).

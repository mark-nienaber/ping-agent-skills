---
title: About groups and populations
description: Groups and populations are both used to organize users in PingOne, but they differ in several ways.
component: pingone
page_id: pingone:directory:p1_groups_vs_populations
canonical_url: https://docs.pingidentity.com/pingone/directory/p1_groups_vs_populations.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
section_ids:
  related-links: Related links
  p1-internal-external-groups: Internal and external groups
  p1-static-dynamic-groups: Static and dynamic groups
  p1-dynamic-group-ex: Dynamic group examples
  example-1: Example 1
  example-2: Example 2
  example-3: Example 3
  example-4: Example 4
  example-5: Example 5
  p1-nested-groups: Nested groups
  circular-references: Circular references
  p1-group-roles: Group roles
---

# About groups and populations

Groups and populations are both used to organize users in PingOne, but they differ in several ways.

A user can belong to multiple groups, but only one population. A population is a fundamental organizational unit, while groups offer more fine-grained control. For example, you could use a population to contain all your employees and use a group to define subsets, such as Marketing, HR, Contractors, or US Employees.

A population-level group can contain users from that population only, but an environment-level group can contain users from different populations in the same environment.

## Related links

* [Populations](p1_populations.html)

* [Viewing group membership](p1_view_group_membership.html)

* [Managing group membership](p1_add_members_to_group.html)

* [Searching for users using SCIM queries](p1_searchforusers.html#scim-query-users)

## Internal and external groups

In PingOne, you can have internal groups, which are created and managed in PingOne, or external groups, which are created through a connection to an external identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* or Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* gateway.

Internal groups are indicated on the **Groups** page with the **Internal Group** icon (![p1 internal group icon](_images/p1-internal-group-icon.png)) and are fully managed in PingOne. You can add, remove, and edit users directly.

You can create internal groups at the population level or the environment level. Administrators who are assigned roles scoped only to the population level can create groups for those populations only and cannot create groups at the environment level.

External groups are indicated on the **Groups** page with the **External Group** icon (![p1 external group icon](_images/p1-external-group-icon.png)). To view information about how the external groups are provisioned (for example, **Just-in-time**) and from where they are sourced (for example, **External IdP** or **LDAP Gateway**), click **Columns** and select **Sync Type** and **Group Source**. You can view the group membership for external groups in PingOne, but you can't add group members. Group membership is managed by the corresponding IdP or gateway from which the group originates. You can remove users, but the user might be added back to the group automatically the next time the group is synced with the source.

![A screenshot showing the Groups page with several internal groups and one external group. The details pane for the external group is open on the right.](_images/p1-external-groups-view.png)

## Static and dynamic groups

In PingOne, you can create static groups, dynamic groups, or a combination of both.

With static groups, you add or remove group members manually.

With dynamic groups, members are added based on rules. You'll set up an expression or filter to determine which users should be included in the group. If you change the filter criteria for a dynamic group, users will be added or removed automatically based on the current criteria in the filter. Likewise, as user attributes change to match or not match the filter, a user will be implicitly added or removed from the group.

Dynamic groups also allow you to add users directly. You can manually add users that do not match the SCIM filter.

For more information, see [Creating a group](p1_create_group.html) and [Managing group membership](p1_add_members_to_group.html).

### Dynamic group examples

You can use a custom filter to define dynamic internal groups, as in the following examples.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This topic is not applicable to external group membership. External group membership is managed through the source from which the group originates. |

#### Example 1

Filter with a simple **Any**. Include users from the following country codes:

* Country Code Equals `US`

* Country Code Equals `CA`

![Screen capture of the Create Dynamic Group page showing a filter Any with the Attribute of Country Code.](_images/vaj1669048225571.png)

#### Example 2

Filter with a simple **Any** using UUIDs. Include users from the following populations:

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

![Screen capture of the Create Dynamic Group page showing a filter Any with the Attribute Population ID.](_images/phf1669048669417.png)

#### Example 3

Filter with an **Any** and **All**. Include enabled users from the following populations:

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

* Enabled Equals `True`

![Screen capture of the Create Dynamic Group page showing a filter of Any and All with the Attributes Population ID and Enabled.](_images/vll1669049108863.png)

#### Example 4

Filter with an **All** and several **Any**. Include users from either of two populations in Canada, as well as a user with a particular email address.

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Country Code Equals `CA`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

* Country Code Equals `CA`

* Email Address Equals `admin@example.com`

![Screen Capture of the Create a Dynamic Group page showing a filter of Any and All with the Attributes Population ID, Country Code and Email Address.](_images/fsw1669049382070.png)

#### Example 5

Filter with an **All** and several **Any**. All users from either of two populations that are in the US and also in the Sales department, as well as a user with a particular email address. Note that the Department attribute is a custom attribute.

* Population ID Equals `10000000-0000-0000-0000-000000000001`

* Country Code Equals `US`

* Department Equals `Sales`

* Population ID Equals `20000000-0000-0000-0000-000000000001`

* Country Code Equals `US`

* Department Equals `Sales`

* Email Address Equals `admin@example.com`

![A Screen Capture of the Create Dynamic Group page showing a filter of All and Any with the Attributes Population ID, Country Code, Department and Email Address.](_images/fyd1669049885664.png)

Learn more in [Managing group membership](p1_add_members_to_group.html).

## Nested groups

A nested group is a group that is a member of another group.

Use nested groups to allow inheritance of membership and application access from one group to its subgroups. Learn more in [Application access control](../applications/p1_application_access_control.html).

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | You cannot nest an environment-level group inside a population-level group. |

For example, assume an environment has three groups: Group A, Group B, and Group C. Each group has access to a single application: Group A has access to App1, Group B has access to App2, and Group C has access to App3.

If you nest Group B inside of Group A, and Group C inside of Group B, then application access will be as follows:

* Group A has access to App1.

* Group B has access to App1 and App2.

* Group C has access to App1, App2, and App3.

The following diagram illustrates this example.

![Nested groups diagram](_images/xxv1636400449025.png)

### Circular references

You can also nest groups inside their subgroups. Continuing the previous example, if you add Group A as a subgroup of Group C, creating a circular reference, then all three groups will have access to all three applications.

For more information, see [Creating a nested group](p1_create_nested_group.html), [Removing a nested group](p1_remove_nested_group.html), and [Managing group membership](p1_add_members_to_group.html).

## Group roles

To make permissions management easier, you can assign roles to groups and individual users.

Using group roles, you can:

* Manage roles for multiple users at once.

* Apply role changes in bulk.

* See users that have a certain role by viewing group members.

  You can use roles to manage permissions for groups of administrators. Learn more in [Managing administrators](../getting_started_with_pingone/p1_manage_administrators.html).

For security reasons, you can assign roles to static groups but not to dynamic groups. Dynamic groups include members based on a filter or rule. Users could be added to a dynamic group unintentionally and could inherit role assignments you don't want to give them. Learn more in [Static and dynamic groups](#p1-static-dynamic-groups).

When adding users to static groups that are assigned roles, be careful not to inadvertently assign a role to a user unintentionally when you add them to a group. If a user is assigned a role because they are in a group and you don't want them to have the role, remove the user from the group.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * You can assign a role to a group you're a member of only if that role is assigned to you directly as an individual user, and is not assigned to you as part of a group that you belong to.

* If a built-in role you're assigned allows you to assign a different role, you can also assign that role to a group you are a member of. For example, the Identity Data Admin role has permissions that allow it to assign the Identity Data Admin Read Only role. If you're assigned the Identity Data Admin role, you can assign that role or the Identity Data Admin Read Only role to a group.

* An administrator might not have permissions to assign roles but can add or remove users from a group that has role assignments. For example, one administrator can assign roles to a group, and a different administrator can add or remove users from that group, depending on their role assignments.

* You can't add or remove yourself from a group that has roles assigned to it.

* Roles assigned to a group won't affect roles that are assigned to a user individually. If the role isn't assigned to the user directly, the role is removed when they're removed from the group.

* You can assign roles in up to 500 groups. |

Learn more in [Creating a group](p1_create_group.html) and [Managing group membership](p1_add_members_to_group.html).

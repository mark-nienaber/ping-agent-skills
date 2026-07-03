---
title: Access authorization
description: Configure access authorization using scopes to delegate user and entitlement management
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/governance-lcm-authorization
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-lcm-authorization.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["LCM", "user management", "authorization", "scopes", "permissions", "internal roles"]
section_ids:
  configure-authorization-using-scopes: Configure authorization using scopes
  add_scopes_and_assign_to_users: Add scopes and assign to users
  create_an_internal_role: Create an internal role
---

# Access authorization

Before you can delegate user and entitlement management to designated end users, you must configure access authorization using scopes. Access authorization defines what actions a delegated administrator can perform and on which set of users.

## Configure authorization using scopes

Scope permissions grant a specific subset of permissions for user management.

Permissions for user management are as follows:

| Permission  | Description                                                                                                                                                                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create User | Allows the end user to create new users in the system.This global permission overrides a scope's target conditions. For example, even if a scope is set to target only contractor users, a person with this permission can create any type of user, not just contractors. |
| Modify User | Allows the end user to modify the users matching the filter.                                                                                                                                                                                                              |
| Delete User | Allows the end user to delete the users matching the filter.                                                                                                                                                                                                              |
| View Grants | Allows the user to view the access of the matching users, for example, applications, entitlements, and roles.                                                                                                                                                             |

## Add scopes and assign to users

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. Go to Governance > Scopes.

3. Click [icon: add, set=material, size=inline] New Scopes.

4. On the New Scope page, enter the following in the Details section:

   1. Name: Enter the name for the scope.

   2. Description: Enter a description for the scope.

   3. Click Next.

      ![Scope details page displaying name and description](../_images/governance-user-lcm-scope-details.png)

5. On the Applies to page, define which users should be subject to this scope.

   1. Select if the All or Any condition must be met.

   2. Select a property for this scoping rule. For example, select userName.

   3. Select an operator for the scoping rule. For example, select contains.

   4. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

   5. Click Next.

      ![Scope \`applies to\` page defining the user to which the scope applies.](../_images/governance-user-lcm-scope-applies-to.png)

6. If you're granting user permissions, configure the following on the Access page:

   1. Select the Users checkbox.

   2. Select if All or Any condition must be met.

   3. Select a property for this scoping rule. For example, select accountStatus.

   4. Select an operator for the scoping rule. For example, select is.

   5. Enter a condition. For example, enter active.

   6. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

   7. Select the permissions available to the scope:

      * Create Users: Permission to create a new user.

      * Modify User: Permission to modify a user.

      * Delete User: Permission to delete a user.

      * View Grants: Permission to view the access for the users matching the scope filter.

   8. Click Save.

      ![Scope access matching the conditions.](../_images/governance-user-lcm-scope-access.png)

## Create an internal role

Administrators must create an internal role so that authorized end users can view the Users identity object.

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. Go to Identities > Manage.

3. Click Internal Roles > [icon: add, set=material, size=inline] New Internal Role.

   1. In the New Internal Role modal, enter the following and click Next.

      * Name: Enter a name for the internal role, such as UserLCMTest.

      * Description: Enter a description for the internal role.

        ![Creating a new internal role](../_images/governance-user-lcm-new-internal-role.png)

   2. In the Internal role Permissions modal, select Alpha realm - Users managed/alpha\_user, and click [icon: add, set=material, size=inline] Add.

      1. Click the internal role permissions you want available with the role:

         * View

         * Create

         * Update

         * Delete

      2. Click Show advanced. Select Read/Write for the attribute permissions and click Next:

         * userName

         * givenName

         * cn

         * sn

         * mail

           ![Internal role permissions](../_images/governance-user-lcm-internal-role-permissions-expanded.png)

      3. In the Dynamic Internal role Assignment modal, click Next.

      4. In the Time Constraint modal, click Save.

4. In the UserLCMTest page, click [icon: add, set=material, size=inline] Add Members.

   1. In the Add Members modal, select the users to which the internal role applies, and then click Save.

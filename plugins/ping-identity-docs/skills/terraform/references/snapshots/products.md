---
title: Admin Role Management Considerations
description: When creating and managing environments using Terraform, admin role management must be considered to avoid unexpected errors or unexpected inability to manage platform resources. The following describes admin role management considerations that administrators must take when using the PingOne Terraform provider.
component: terraform
page_id: terraform::products/pingone/develop_with_terraform/admin_roles
canonical_url: https://developer.pingidentity.com/terraform/products/pingone/develop_with_terraform/admin_roles.html
revdate: March 19, 2025
section_ids:
  pingone-admin-role-model: PingOne admin role model
  considerations-when-creating-environments: Considerations when using Terraform to create environments
  assigning-admin-roles: Assigning admin roles
  role-assignment-scope-conflicts: Role assignment scope conflicts
  importing-role-assignments-to-terraform-state: Importing role assignments to Terraform state
  import-by-terraform-cli: Import by Terraform CLI
  import-by-terraform-configuration-language: Import by Terraform configuration language
  cannot-manage-worker-application-secret: When admins cannot view or manage a worker application secret
---

# Admin Role Management Considerations

When creating and managing environments using Terraform, admin role management must be considered to avoid unexpected errors or unexpected inability to manage platform resources. The following describes admin role management considerations that administrators must take when using the PingOne Terraform provider.

## PingOne admin role model

An administrative role is a collection of permissions that you can assign to a user, group of users, application, or connection. Administrative roles give PingOne admins access to resources in the PingOne admin console, API, Terraform resources, and determine the actions they can take in PingOne.

You can find the list of available admin roles in [PingOne roles](https://docs.pingidentity.com/r/en-us/pingone/p1_c_roles) in the PingOne documentation.

Each role is a collection of permissions. You can find the list of permissions that each role contains in [PingOne role permissions](https://apidocs.pingidentity.com/pingone/platform/v1/api/#pingone-role-permissions) in the PingOne developer documentation.

## Considerations when using Terraform to create environments

When creating environments with Terraform using the [`pingone_environment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/environment), the worker application used to connect Terraform to the PingOne tenant should have the **Organization Admin** role assigned, as that role contains the permission **Create, promote, read, update, and delete environment**.

After the worker application has created the new environment, the worker application automatically inherits the following roles *scoped to the new environment*:

* **Environment Admin**.

* **Identity Data Admin**.

* **Client Application Developer**.

Any existing user, group of users, application, or connection that has an admin role assignment *scoped to the organization* also inherits the ability to manage the new environment with the permissions assigned to that role.

For example, if admin user Barbara Jensen has **Environment Admin** *scoped to the organization* and **Identity Data Admin** *scoped to individual environments*, either assigned directly or by being member of a group that has those admin roles assigned, Barbara will inherit the role permissions to be able to manage that new environment (inherited **Environment Admin** role permissions), but will *not* be able to manage user and group data of the environment (the **Identity Data Admin** role permissions have not been inherited). In this example, if Barbara needs to manage user identities and groups, she would need the **Identity Data Admin** role assigned *scoped to the new environment*, either directly or by being made a member of a group that has that role assigned. Learn more in [Assigning admin roles](#assigning-admin-roles).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To prevent privilege escalation, admin users, worker applications, or connections that previously could view and manage the worker application's secret might no longer be able to do so after an environment has been created with Terraform. This change can lead to an error ***Actor does not have permissions to access worker application client secrets***. You can find more information in [When admins cannot view a worker application secret](#cannot-manage-worker-application-secret). |

Other than the birthright roles assigned to the worker application on environment creation and the inherited permissions on actors with roles scoped to the organization, no other role assignments are given implicitly.

It's now up to the customer tenant administrators to consider:

* Are the Terraform worker application's birthright roles sufficient to perform further configuration with Terraform?

  If not, further roles might need to be explicitly assigned to the worker application. Adding additional roles can be done in the PingOne admin console by an administrator, by API, or by Terraform. Learn more in [Assigning admin roles](#assigning-admin-roles).

* Are the worker application's birthright role permissions beyond what's required for the worker application to perform its configuration management purpose and contravene least privilege principles?

  In this case, roles might need to be revoked from the worker application. Role revoking can be done in the PingOne admin console by an administrator or by API. You cannot revoke birthright roles from a worker application used to create an environment using Terraform unless the birthright role assignments are first imported into Terraform state. Learn more in [Importing role assignments to Terraform state](#importing-role-assignments-to-terraform-state).\_

* Should other users, worker applications, or connections be granted administrative roles that can manage the new environment or continue to manage the secret of the Terraform worker application? (Refer to [When admins cannot view or manage a worker application secret](#cannot-manage-worker-application-secret)).

  Roles can be explicitly assigned to any user, group of users, worker application, or connection in the PingOne admin console, by API, or by Terraform. Learn more in [Assigning admin roles](#assigning-admin-roles).

* Do existing users, worker applications, or connections that have roles *scoped to the organization* (and therefore implicitly gain permissions to manage the new environment) have the appropriate role permissions, or do those users (through direct assignment or through group membership), worker applications, or connections need to have their role scope reduced such that their roles should instead be *scoped to individual environments*.

  Reducing the scope of admin role assignments can be achieved in the PingOne admin console by an administrator, by API, or by Terraform (if those role assignments are managed using Terraform).

## Assigning admin roles

When assigning admin roles to users, worker applications, or connections, the role assignments can be assigned with a scope to individual environments, populations, or to the entire organization (depending on the role). Users can be assigned roles directly or by being members of a group that's been assigned admin roles.

Admin role assignments can be managed in the PingOne admin console, by API, or by Terraform. When using Terraform, the following resources apply:

* Assigning admin roles directly to users: [`pingone_user_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/user_role_assignment). *Role conflicts might occur. Learn more in [Role assignment scope conflicts](#role-assignment-scope-conflicts).*

* Assigning admin roles to groups: [`pingone_group_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/group_role_assignment). *Role conflicts might occur on the group role assignment, but role conflicts on group user members are resolved automatically. Learn more in [Role assignment scope conflicts](#role-assignment-scope-conflicts).*

* Assigning admin roles to worker applications: [`pingone_application_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/application_role_assignment). *Role conflicts might occur. Learn more in [Role assignment scope conflicts](#role-assignment-scope-conflicts).*

* Assigning admin roles to connections: [`pingone_gateway_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/gateway_role_assignment). *Role conflicts might occur. Learn more in [Role assignment scope conflicts](#role-assignment-scope-conflicts).*

Learn how Terraform can be used to assign roles to administrative actors in the [Role assignment with Terraform](../tutorials/role_assignment.html) tutorial.

Ping Identity recommends that customers follow documented [general best practices](../../../best_practices.html) and [PingOne-specific best practices](../best_practices.html) for developing with Terraform, paying close attention to best practices around [administrative role assignment](../best_practices.html#user-administrator-role-assignment).

### Role assignment scope conflicts

When assigning roles to users, groups of users, applications, or connections using Terraform, there are situations where role assignment uniqueness conflicts can occur. Errors could look similar to the following:

```
PingOne Error Details:
ID: f21b****-****-****-****-********a7d0
Code: INVALID_DATA
Message: The request could not be completed. One or more validation errors were in the request.
Details:
  - Code:       UNIQUENESS_VIOLATION
    Message:    May not assign duplicate Role
    Target:     role
```

This error occurs when a user, group, worker application, or connection already has the role assignment at a scope that is greater than or equal to the scope being configured.

For example, Janet Smith has the **Environment Admin** role assigned *scoped to the organization*. The `terraform apply` run attempts to assign the **Environment Admin** to Janet using the [`pingone_user_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/user_role_assignment), *scoped to an individual environment*. Because Janet already has **Environment Admin** with organization-level permissions (and so can manage all environments), Terraform is attempting to add duplicate role permissions.

In this example, the user-level conflict can be resolved by instead managing user's role assignments using groups, using the [`pingone_group_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/group_role_assignment) where needed. When using Terraform to manage role assignments, using groups to manage user's role assignments is a [documented best practice](../best_practices.html#use-group-role-assignments).

In the case of worker applications and connections, the Terraform HCL must be adjusted to resolve the role assignment scope conflict. You can change the following:

* Change how role assignments are managed as an out-of-band control to avoid the possibility of conflict. In this way, admin-level controls outside of Terraform ensure that conflicts are unlikely to happen when Terraform needs to manage role conflicts.

* Manage roles with privileged access management tools to reduce the need for Terraform to manage role assignments.

* Use Terraform to calculate the possibility of conflicting role assignments.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There are disadvantages to using Terraform to calculate the possibility of conflicting role assignments, as role assignments for a user, group, application, or connection must be fully known in order to calculate the potential conflicts. Because in Terraform, IDs are not known until the first `terraform apply`, this can lead to a situation where the Terraform HCL must be applied twice:1) Applying the initial role assignments

2) Applying again to perform an accurate calculation to ensure any future role assignments are not in conflictYou can find an example HCL in [GitHub issue 478](https://github.com/pingidentity/terraform-provider-pingone/issues/478#issue-1805321896) |

## Importing role assignments to Terraform state

Role assignments to users, groups, worker applications, and connections might have been defined outside of Terraform's management control. This includes role assignments that:

* Have been defined by administrators in the PingOne admin console

* Have been defined by administrators or scripts using the PingOne platform management API

* Have been defined implicitly by the platform when creating new environments though the PingOne admin console, by API, or by Terraform (using the `pingone_environment` resource)

These role assignments can be brought under Terraform's management control by using the **Terraform import** functionality. Import is supported on the following resources:

* Admin role assignment to a user directly: [`pingone_user_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/user_role_assignment)

* Admin role assignment to a group: [`pingone_group_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/group_role_assignment)

* Admin role assignment to a worker application: [`pingone_application_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/application_role_assignment)

* Admin role assignment to a connection: [`pingone_gateway_role_assignment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/gateway_role_assignment)

### Import by Terraform CLI

Hashicorp Terraform provides a standard CLI command, `terraform import`, that can be used to import any supported resource into Terraform state. Learn more in [Importing to Terraform state](../../../develop_with_terraform/importing_to_state.html).

Each resource listed previously contains an example for importing the resource to Terraform state using the Terraform CLI.

### Import by Terraform configuration language

Hashicorp Terraform provides a standard configuration language import declaration block, `import {}`, that you can use to import any supported resource into Terraform state and generate its resulting HCL. Learn more in [Importing to Terraform state](../../../develop_with_terraform/importing_to_state.html).

The following is an example of a role assignment import for `pingone_group_role_assignment`, where the ID is a composite ID of `<environment_id>/<group_id>/<role_assignment_id>`, as shown in the Terraform CLI import example in the [registry documentation](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/group_role_assignment):

```terraform
import {
  to = pingone_group_role_assignment.example
  id = "e16f****-****-****-****-********15be/80f9****-****-****-****-********e828/f936****-****-****-****-********65c1"
}
```

## When admins cannot view or manage a worker application secret

Admin actors (users, worker applications, and connections) might not be able to view or rotate a worker application's secret when they were able to previously as an unexpected change of behavior.

The issue can be observed in the PingOne admin console (manifesting as a lack of control over a worker application's secret), a `403` error response from the [Read Application Secret](https://apidocs.pingidentity.com/pingone/platform/v1/api/#get-read-application-secret) API, or the following error within Terraform when attempting to use the `pingone_application_secret` [resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/application_secret) or [data source](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/data-sources/application_secret):

```
PingOne Error Details:
ID: f21b****-****-****-****-********a7d0
Code: ACCESS_FAILED
Message: The request could not be completed. You do not have access to this resource.
Details:
  - Code:       INSUFFICIENT_PERMISSIONS
    Message:    Actor does not have permissions to access worker application client secrets
```

The change in ability to manage a worker application's client secret typically occurs when the worker application is granted additional role permissions that the user, admin worker application, or connection doesn't have. The worker application whose secret cannot be managed has a higher level of privilege to manage configuration and data within the tenant. The ability to view and change the secret is therefore restricted to mitigate privilege escalation issues where admin actors could potentially use the higher privileged worker application to make changes they aren't authorized to make in the platform.

For example, the worker application Terraform Admin is used to create a new environment using the `pingone_environment` resource. The Terraform Admin worker application is implicitly granted birthright roles to be able to manage that environment (refer to [Considerations when using Terraform to create environments](#considerations-when-creating-environments)), but other admin users, worker applications, and connections aren't provided the same birthright role permission assignments.

The Terraform Admin worker application that created the environment now has higher privileges than other administrators, so privilege escalation controls are applied to other platform administrators. Other platform administrators have now lost the ability to view and manage the Terraform Admin worker application secret.

The resolution is to apply the missing roles permissions by assigning roles to the users, worker applications, or connections that need to be able to manage the worker application's secret.

In the previous example, you would add a combination of **Environment Admin**, **Identity Data Admin**, and **Client Application Developer** roles *scoped to the newly created environment* to the users, worker applications, or connections that need to be able to manage the "Terraform Admin" worker application's secret.

Roles can be explicitly assigned to any user, group of users, worker application, or connection in the PingOne admin console, by API or by Terraform. Learn more in [Assigning admin roles](#assigning-admin-roles).

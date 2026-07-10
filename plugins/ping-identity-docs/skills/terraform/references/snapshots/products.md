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

---

---
title: Best practices
description: The following sections provide a set of best practices to apply when writing Terraform with the PingOne Terraform provider and associated modules.
component: terraform
page_id: terraform::products/pingone/best_practices
canonical_url: https://developer.pingidentity.com/terraform/products/pingone/best_practices.html
revdate: March 19, 2025
section_ids:
  develop-console-promote-as-code: Develop in the admin console, promote using Configuration as Code
  example-configuration-dependencies: Example or bootstrapped configuration dependencies
  deploy-to-clean-environments: "Deploy to \"clean\" environments, without example or bootstrapped configuration"
  platform: Platform
  davinci-service: DaVinci service
  mfa-service: MFA service
  verify-service: Verify service
  define-config-dependencies: Define all configuration dependencies in Terraform or elsewhere in the pipeline
  not-best-practice: Not best practice
  best-practice: Best practice
  protect-service-configuration-and-data: Protect service configuration and data
  rotate-worker-application-secrets: Regularly rotate worker application secrets
  review-force-delete-overrides: Review use of API force-delete provider overrides
  review-force-delete-environment-type-override: global_options.environment.production_type_force_delete
  review-force-delete-population-override: global_options.population.contains_users_force_delete
  use-lifecycle-prevent_destroy: Protect configuration and data with the lifecycle.prevent_destroy meta argument
  multi-team-development: Multi-team development
  use-on-demand-sandbox-environments: Use on-demand sandbox environments
  user-administrator-role-assignment: User administrator role assignment
  use-group-role-assignments: Use group role assignments over Terraform-managed user role assignments
  use-custom-roles: Use custom roles to follow principles of least privilege
---

# Best practices

The following sections provide a set of best practices to apply when writing Terraform with the PingOne Terraform provider and associated modules.

These guidelines are not intended to educate on the use of Terraform and are not a getting started guide. You can find more information about Terraform in [Hashicorp's Online Documentation](https://developer.hashicorp.com/terraform/docs). Learn how to get started with the PingOne Terraform provider in the [Getting started](getting_started.html) guide.

## Develop in the admin console, promote using Configuration as Code

Ping Identity recommends performing use-case development activities in the PingOne admin console whenever possible. This recommendation is due to the complex nature of Workforce IAM and Customer IAM deployments that includes policy definition, user experience design, and associated testing and validation of designed use cases.

After you've developed a configuration in the PingOne admin console, you can extract it as Configuration as Code to be stored in source control (such as a Git code repository) and linked with CI/CD tooling to automate the delivery of use cases into test and production environments.

For professionals experienced in DevOps development, configuration can be created and altered outside of the PingOne admin console, but care must be taken when modifying complex configuration, such PingOne Authorize, PingOne MFA, PingOne Protect, or PingOne SSO sign-on policies.

## Example or bootstrapped configuration dependencies

### Deploy to "clean" environments, without example or bootstrapped configuration

Example or bootstrapped configuration is deployed automatically by the PingOne service when an environment is created or new services are provisioned to an existing environment. This is the default behavior of the PingOne admin console and the API.

Example or bootstrapped configuration can be a useful starting point when initially creating use cases with the service (in the development phase), but creates conflicts when migrating the configuration through to test and production environments.

The definition of the example or bootstrapped configuration for new environment can also change over time, as new features are released and use case configuration best practices are defined. An environment created today might not be the same as an environment created a year from now.

It's best practice to create a new environment as a "clean" (without example or bootstrapped configuration) environment for those environments outside of the initial development one. If environments cannot be recreated or are intended to be long-lasting (such as staging or production), it might be enough to remove bootstrapped configuration manually when an environment is created.

Notable examples of demo configuration include:

#### Platform

* The default branding theme

* Optional directory schema attributes (which can be disabled if not used)

  * `accountId`

  * `address`

  * `email`

  * `externalId`

  * `locale`

  * `mobilePhone`

  * `name`

  * `nickname`

  * `photo`

  * `preferredLanguage`

  * `primaryPhone`

  * `timezone`

  * `title`

  * `type`

* The default Keys and Certificates

* The default notification policies

* The default `Single_Factor` sign-on policy

* The example password policies

* The `PingOne Application Portal` (which can be disabled if not used)

#### DaVinci service

* Example Forms

#### MFA service

* The default MFA Device Policy

* The default FIDO2 policies

* The `Multi_Factor` sign-on policy

#### Verify service

* The default verify policy

### Define all configuration dependencies in Terraform or elsewhere in the pipeline

Example or bootstrapped configuration is deployed automatically by the PingOne service when an environment is created or new services are provisioned to an existing environment. This is the default behavior of the PingOne admin console and the API.

Example or bootstrapped configuration can be a useful starting point when initially creating use cases with the service (in the development phase), but creates conflicts when migrating the configuration through to test and production environments.

The definition of the example or bootstrapped configuration for new environment can also change over time as new features are released and use case configuration best practices are defined. An environment created today might not be the same as an environment created a year from now.

It's best practice to explicitly define all configuration dependencies in Terraform (or as a prior step in the CI/CD pipeline) after developing flows for use cases. Most notably, this practice includes defining the policies (for example, sign-on, MFA Device, FIDO2, or Protect policies) that applications will use in HCL, rather than using the example or bootstrapped environment examples.

#### Not best practice

The following [`pingone_population`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/population) definition doesn't follow best practice, as it depends on the "Passphrase" password policy that was deployed by default when the environment was created. This definition assumes that this password policy will always exist and have a consistent definition on every environment creation. However, the password policy could change over time, invalidating the configuration.

```terraform
data "pingone_password_policy" "ootb_passphrase" {
  environment_id = pingone_environment.my_environment.id

  name = "Passphrase"
}

resource "pingone_population" "my_population" {
  environment_id = pingone_environment.my_environment.id

  name        = "My awesome population"
  description = "My new population for awesome people"

  password_policy_id = data.pingone_password_policy.ootb_passphrase.id

  lifecycle {
    # change the `prevent_destroy` parameter value to `true` to prevent this data carrying resource from being destroyed
    prevent_destroy = false
  }
}
```

#### Best practice

The following [`pingone_population`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/population) definition follows best practice, as the password policy that it depends on is explicitly defined using the [`pingone_password_policy`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/password_policy) resource. This explicit definition ensures that environments are built and configured consistently between development, test, and production.

```terraform
resource "pingone_password_policy" "my_password_policy" {
  environment_id = pingone_environment.my_environment.id

  name        = "My awesome password policy"

  excludes_commonly_used_passwords = true
  excludes_profile_data            = true
  not_similar_to_current           = true

  history = {
    count          = 6
    retention_days = 365
  }

  # ... other configuration parameters
}

resource "pingone_population" "my_population" {
  environment_id = pingone_environment.my_environment.id

  name        = "My awesome population"
  description = "My new population for awesome people"

  password_policy_id = pingone_password_policy.my_password_policy.id

  lifecycle {
    # change the `prevent_destroy` parameter value to `true` to prevent this data carrying resource from being destroyed
    prevent_destroy = false
  }
}
```

## Protect service configuration and data

The following sections detail best practices to apply to ensure protection of production data beyond what is covered in [Secrets management](../../best_practices.html#secrets-management) when using the PingOne Terraform provider.

### Regularly rotate worker application secrets

In PingOne, administration management functions against the API can be performed by worker applications with admin roles assigned, as described in [Configuring roles for a worker application](https://docs.pingidentity.com/pingone/applications/p1_configurerolesforworkerapplication.html) in the PingOne documentation. To use these worker applications, you might need to generate an application secret and use that secret in downstream applications and services. You should rotate these secrets on a regular basis to help mitigate against unauthorized platform changes.

Rotation can be controlled by a secrets engine that can update with the relevant API, as described in the [Update Application Secret](https://apidocs.pingidentity.com/pingone/platform/v1/api/#post-update-application-secret) in the PingOne developer documentation, but can also be rotated through the Terraform process.

For example, the following Terraform code will rotate an application secret for the application "My Awesome App" every 30 days:

```terraform
resource "pingone_application" "my_application" {
  name = "My Awesome App"
  enabled        = true

  oidc_options = {
    type                        = "WORKER"
    grant_types                 = ["CLIENT_CREDENTIALS"]
    token_endpoint_auth_method  = "CLIENT_SECRET_BASIC"
  }

  # ... other configuration parameters
}

resource "time_rotating" "application_secret_rotation" {
  rotation_days = 30
}

resource "pingone_application_secret" "foo" {
  environment_id = pingone_environment.my_environment.id
  application_id = pingone_application.my_application.id

  regenerate_trigger_values = {
    "rotation_rfc3339" : time_rotating.application_secret_rotation.rotation_rfc3339,
  }
}
```

## Review use of API force-delete provider overrides

The PingOne Terraform provider has a provider-level parameter named [`global_options`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs#nestedblock—​global_options) that allows administrators to override API behaviors for development, test, and demo purposes. You can find details in the [registry documentation](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs#global-options) of this parameter.

There are two parameters that allow force-deletion of configuration, which could result in loss of data if not used correctly.

### `global_options.environment.production_type_force_delete`

WARNING:

The `global_options.environment.production_type_force_delete` global option was removed in the PingOne Terraform provider version v1.0. This section applies to prior provider versions (v0.29 or earlier).

Misuse of the parameter could cause unintended data loss, so it must be used with caution.

The purpose of the parameter is to override the API level restriction of not being able to destroy environments of type "PRODUCTION". The default value of this parameter is `false`, meaning that environments will not be force-deleted if a [`pingone_environment`](https://registry.terraform.io/providers/pingidentity/pingone/0.29.2/docs/resources/environment) resource that has a `type` value of `PRODUCTION` has a destroy plan when run in the `terraform apply` phase. Use of this parameter is designed to help facilitate development, testing, or demonstration purposes and should be set to `false` or left undefined for environments that carry production data.

The implementation of this option is that the environment type will be changed from `PRODUCTION` to `SANDBOX` before a delete API request is issued. Instead of using this parameter, consider changing the type to `SANDBOX` manually before running a plan that destroys an environment.

### `global_options.population.contains_users_force_delete`

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | Misuse of the parameter could cause unintended data loss, so it must be used with caution. |

The purpose of the parameter is to override the API level restriction of not being able to destroy populations that contain user data. The default value of this parameter is `false`, meaning that populations that contain user data will not be force-deleted if a [`pingone_population`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/population) resource has a destroy plan when run in the `terraform apply` phase. Use of this parameter is designed to help facilitate development, testing, or demonstration purposes where non-production user data is created and can be safely discarded. The parameter should strictly be set to `false` or left undefined for environments that carry production data.

The implementation of this option is that the provider will find and delete all users assigned to the population being destroyed before a delete API request is issued to the population. Instead of using this parameter, consider removing non-production data manually before running a plan that destroys a population.

### Protect configuration and data with the `lifecycle.prevent_destroy` meta argument

While some resources are safe to remove and replace, there are some resources that, if removed, can result in data loss.

You should use the `lifecycle.prevent_destroy` meta argument to protect against accidental destroy plans that could cause data loss. You might also want to use the meta argument to prevent accidental removal of access policies and applications if dependent applications cannot be updated with Terraform in case of replacement.

For example:

```terraform
resource "pingone_schema_attribute" "my_attribute" {
  environment_id = pingone_environment.my_environment.id

  name = "myAttribute"

  # ... other configuration parameters

  lifecycle {
    prevent_destroy = true
  }
}
```

The following resources, if destroyed, put data at risk within a PingOne environment:

* [`pingone_schema_attribute`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/schema_attribute)

  * If a custom schema attribute is created, a destroy of the schema attribute will erase that attribute's data for users.

* [`pingone_population`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/population)

  * Users must belong to a population. If a population is removed, the users within that population could be at risk. There are platform controls to prevent accidental deletion of a population that contains users.

* [`pingone_environment`](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/environment)

  * Users might belong to the environment's default population. If the environment is removed, the users within that population could be at risk. There are platform API-level controls to prevent accidental deletion of an environment where the environment's type is set to `PRODUCTION`. `SANDBOX` environments do not have such API restrictions.

## Multi-team development

### Use on-demand sandbox environments

PingOne customer tenants have a "tenant-in-tenant" architecture, whereby a PingOne tenant organisation can contain many individual environments. These individual environments can be purposed for development, test, pre-production, and production purposes. These separate environments allow for easy maintenance of multiple development and test instances.

The recommended approach for multi-team development, when using a GitOps CI/CD promotion process, is to spin up on-demand development and test environments, specific to new features or to individual teams, to allow for development and integration testing that doesn't conflict with other team's development and test activities. The Terraform provider allows administrators to use CI/CD automation to provision new environments as required and remove them after the project activity no longer needs them.

In a GitOps CI/CD promotion pipeline, configuration can be translated to Terraform Configuration as Code and then merged (with pull requests) with common test environments, where automated tests can be run. This flow allows the activities in the on-demand environments to be merged into a common promotion pipeline to production environments.

## User administrator role assignment

### Use group role assignments over Terraform-managed user role assignments

PingOne supports assigning [administrator roles to groups](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_manage_admin_roles.html), such that members of the group get the administrator roles assigned.

Ping Identity recommends that groups with admin role assignments are controlled by the Joiner/Mover/Leaver Identity Governance processes, separate from the Terraform CI/CD process that configures applications, policies, domain verification, and so on. It could be that the groups with their role assignments are initially seeded by Terraform. In this case, it should still be a separate Terraform process from the process that controls platform configuration, and the user group assignments should still happen in the Joiner/Mover/Leaver Identity Governance process.

You can use Terraform to assign administrator roles to individuals directly, but this is not recommended best practice except in development or non-production environments. Ping Identity recommends that role assignment processes in non-production environments align as closely as possible to role assignment processes in production environments.

### Use custom roles to follow principles of least privilege

PingOne supports the creation of [custom administrator roles](https://docs.pingidentity.com/pingone/directory/p1_roles.html), which allow an administrator to define their own admin role based on a collection of permissions that represent a specific purpose.

Ping Identity recommends that customers create custom administrator roles to follow least privilege principles. To mitigate accidental or malicious changes to environments, assign the minimum required permissions for users to be able to perform their roles.

You can use Terraform to manage custom administrator roles and also manage the assignment of custom roles to groups and users.

---

---
title: Configuring the PingOne Self Service application
description: The following shows an example of how to configure the PingOne Self Service system application.
component: terraform
page_id: terraform::products/pingone/tutorials/configuring_the_self_service_application
canonical_url: https://developer.pingidentity.com/terraform/products/pingone/tutorials/configuring_the_self_service_application.html
revdate: March 19, 2025
---

# Configuring the PingOne Self Service application

The following shows an example of how to configure the PingOne Self Service system application.

You can [configure the PingOne Self Service application](https://docs.pingidentity.com/pingone/user_experience/p1_self_service.html) in the PingOne admin console. It's a web application, and its capabilities are configured by assigning resource scopes to the application, rather than through a dedicated API or Terraform resource.

First, you'll need to ensure that the Self Service application itself is configured using the [`pingone_system_application` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/system_application).

```terraform
resource "pingone_system_application" "pingone_self_service" {
  environment_id = pingone_environment.my_environment.id

  type    = "PING_ONE_SELF_SERVICE"
  enabled = true

  apply_default_theme         = true
  enable_default_theme_footer = true
}
```

You'll then select which self-service capabilities (the scopes) you want to apply to the Self Service application. The simplest way is to create a list and select the appropriate scope data using the [`pingone_resource_scope` data source](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/data-sources/resource_scope).

```terraform
locals {
  pingone_api_scopes = [
    # Manage Profile
    "p1:read:user",
    "p1:update:user",

    # Manage Authentication
    "p1:create:device",
    "p1:create:pairingKey",
    "p1:delete:device",
    "p1:read:device",
    "p1:read:pairingKey",
    "p1:update:device",

    # Enable or Disable MFA
    "p1:update:userMfaEnabled",

    # Change Password
    "p1:read:userPassword",
    "p1:reset:userPassword",
    "p1:validate:userPassword",

    # Manage Linked Accounts
    "p1:delete:userLinkedAccounts",
    "p1:read:userLinkedAccounts",

    # Manage Sessions
    "p1:delete:sessions",
    "p1:read:sessions",

    # View Agreements
    "p1:read:userConsent",

    # Manage OAuth Consents
    "p1:read:oauthConsent",
    "p1:update:oauthConsent",
  ]
}

data "pingone_resource_scope" "pingone_api" {
  for_each = toset(local.pingone_api_scopes)

  environment_id = pingone_environment.my_environment.id
  resource_type  = "PINGONE_API"

  name = each.key
}
```

Next, you'll map the appropriate scopes to enable the specific self-service features you want using the [`pingone_application_resource_grant` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/application_resource_grant).

```terraform
resource "pingone_application_resource_grant" "my_awesome_spa_pingone_api_resource_grants" {
  environment_id = pingone_environment.my_environment.id
  application_id = pingone_system_application.pingone_self_service.id

  resource_type = "PINGONE_API"

  scopes = [
    for scope in data.pingone_resource_scope.pingone_api : scope.id
  ]
}
```

The Self Service application is now configured with the required capabilities.

You can find the [full runable example](https://github.com/pingidentity/terraform-docs/tree/main/examples/pingone-configuring-the-self-service-application) on GitHub.

---

---
title: Develop with Terraform
description: Learn about administrator role considerations when using Terraform to manage PingOne environments.
component: terraform
page_id: terraform::products/pingone/develop_with_terraform
canonical_url: https://developer.pingidentity.com/terraform/products/pingone/develop_with_terraform.html
revdate: March 19, 2025
section_ids:
  administrator-role-considerations: Administrator role considerations
  importing-a-pingone-environment-to-terraform-state: Importing a PingOne environment to Terraform state
  exporting-or-generating-pingone-terraform-hcl: Exporting or generating PingOne Terraform HCL
---

# Develop with Terraform

## Administrator role considerations

Learn about administrator role considerations when using Terraform to manage PingOne environments.

[Admin Role Management Considerations](develop_with_terraform/admin_roles.html)

## Importing a PingOne environment to Terraform state

Take a preconfigured PingOne environment and import to Terraform state. Importing to Terraform state allows Terraform to manage a product environment without needing to recreate any configuration for that environment. This is useful when bringing a production environment under Terraform control retrospectively.

[Importing to Terraform state](../../develop_with_terraform/importing_to_state.html)

## Exporting or generating PingOne Terraform HCL

Generate Terraform HCL configuration for a preconfigured environment. This is useful when exporting configuration from a development environment to store in source control or promote to test or production.

[Exporting Terraform configuration](../../develop_with_terraform/exporting_configuration.html)

---

---
title: Frequently Asked Questions
description: You can find the list of supported PingDirectory versions by provider version the latest provider documentation.
component: terraform
page_id: terraform::products/pingdirectory/faq
canonical_url: https://developer.pingidentity.com/terraform/products/pingdirectory/faq.html
revdate: March 19, 2025
section_ids:
  what-versions-are-supported: What versions of PingDirectory are supported?
  configuring-tls-trust: How do I configure trust for connecting over HTTPS?
---

# Frequently Asked Questions

## What versions of PingDirectory are supported?

You can find the list of supported PingDirectory versions by provider version the [latest provider documentation](https://registry.terraform.io/providers/pingidentity/pingdirectory/latest/docs#pingdirectory-version-support).

## How do I configure trust for connecting over HTTPS?

You can find details on configuring TLS trust in the [Getting started](getting_started.html) guide.

---

---
title: Frequently Asked Questions
description: You can find the list of supported PingFederate versions by provider version the latest provider documentation.
component: terraform
page_id: terraform::products/pingfederate/faq
canonical_url: https://developer.pingidentity.com/terraform/products/pingfederate/faq.html
revdate: March 19, 2025
section_ids:
  what-versions-are-supported: What versions of PingFederate are supported?
  configuring-tls-trust: How do I configure trust for connecting over HTTPS?
---

# Frequently Asked Questions

## What versions of PingFederate are supported?

You can find the list of supported PingFederate versions by provider version the [latest provider documentation](https://registry.terraform.io/providers/pingidentity/pingfederate/latest/docs/guides/server-support).

## How do I configure trust for connecting over HTTPS?

You can find details on configuring TLS trust in the [Getting started](getting_started.html) guide.

---

---
title: Frequently Asked Questions
description: You can export configuration from a PingOne environment using a combination of Ping CLI and Terraform CLI tools.
component: terraform
page_id: terraform::products/pingone/faq
canonical_url: https://developer.pingidentity.com/terraform/products/pingone/faq.html
revdate: April 13, 2026
section_ids:
  export-from-configured-environment: How do I export configuration from a previously configured environment?
  import-previously-configured-environment-state: How do I bring a previously configured environment under Terraform management?
  cannot-create-workforce-environments: I cannot create a workforce-enabled environment or where can I Terraform creation of a PingID-enabled environment?
  admins-cannot-see-new-environment: I've created a new environment with Terraform, but my admins can't see it
  admins-cannot-see-new-environment-users: I've created a new environment or population with Terraform, but my admins can't view users, or manage group or population based configuration
  cannot-manage-worker-application-secret: "I get an error \"Actor does not have permissions to access worker application client secrets\""
  davinci-terraform-schema: Why doesn't the PingOne DaVinci Flow resource use a JSON export?
  sensitive-api-values: Why do I see a planned change after import even when the defined configuration matches live infrastructure?
---

# Frequently Asked Questions

## How do I export configuration from a previously configured environment?

You can export configuration from a PingOne environment using a combination of Ping CLI and Terraform CLI tools.

Learn more in [Exporting Terraform configuration](../../develop_with_terraform/exporting_configuration.html).

## How do I bring a previously configured environment under Terraform management?

You can bring any environment that has been configured without using Terraform under Terraform management using a combination of Ping CLI and Terraform CLI tools.

Learn more in [Importing to Terraform state](../../develop_with_terraform/importing_to_state.html).

## I cannot create a workforce-enabled environment or where can I Terraform creation of a PingID-enabled environment?

The PingOne provider does not yet support creation of a PingID-enabled workforce environment. You can track the list of known issues and provider limitations on [the project's GitHub](https://github.com/pingidentity/terraform-provider-pingone/issues/451).

## I've created a new environment with Terraform, but my admins can't see it

Check the admin user's role permissions. The admin user must have any of the following roles to see the new environment in the list of environments:

* **Organization Admin**

* **Environment Admin**

* **Identity Data Admin**

* **Client Application Developer**

* **Identity Data Read Only**

* **Configuration Read Only**

Refer to the [Admin Role Management Considerations](develop_with_terraform/admin_roles.html) guide for details on role assignment and considerations for admin role management when using Terraform.

## I've created a new environment or population with Terraform, but my admins can't view users, or manage group or population based configuration

Check the admin user's role permissions. The admin user must have any of the following roles to be able to view and manage identity data and configuration:

* **Identity Data Admin**

* **Identity Data Read Only**

Refer to the [Admin Role Management Considerations](develop_with_terraform/admin_roles.html) guide for details on role assignment and considerations for admin role management when using Terraform.

## I get an error "Actor does not have permissions to access worker application client secrets"

Admin actors (users, worker applications, connections) might not be able to view or rotate a worker application's secret when they could previously as an unexpected change of behavior.

The change in ability to manage a worker application's client secret typically occurs when the worker application is granted additional role permissions that the user, admin worker application, or connection doesn't have. The worker application whose secret cannot be managed has a higher level of privilege to manage configuration and data within the tenant. The ability to view and change the secret is therefore restricted to mitigate privilege escalation issues where admin actors could potentially use the higher privileged worker application to make changes they aren't authorized to make in the platform.

You can find more information and guidance on how to resolve this error in [Admin Role Management Considerations](develop_with_terraform/admin_roles.html).

## Why doesn't the PingOne DaVinci Flow resource use a JSON export?

The PingOne Terraform provider supports DaVinci Flow resources as complete HCL representations instead of referencing a JSON export for a number of reasons:

* **Difference reviewing**: The schema of attributes under `graph_data` is a map. This alleviates situations where the platform returns an export in which the ordering of nodes changes and makes a file comparison difficult. This format simplifies review of identified changes within a `terraform plan` rather than file comparisons for flow configuration changes. These differences should be more precise and easier to follow.

* **Dependency mapping**: With the flow represented in HCL, the process for adding references to other resources can use native Terraform dependencies (for example, a Flow node's connection\_id can point directly to a managed connection).

* **Direct configuration changes**: Changing a DaVinci flow in JSON is complex and error-prone. HCL provides an easier to read format and more access to Terraform's native functions.

* **Sensitive attributes**: This format allows for specific attributes (for example, node properties) to be marked sensitive, rather than the entire flow.

* **API alignment**: In general, all provider resource schemas intend to match the documented APIs for more direct reliance on API contracts and prevention of breaking changes.

PingOne DaVinci Flows can grow to be very large in both the UI and JSON representation. Converting a Flow's JSON export to HCL can be challenging, and you should use the [Ping CLI Terraformer plugin](https://github.com/pingidentity/pingcli-plugin-terraformer) for this conversion. The [Manage an Existing PingOne DaVinci Environment^](tutorials/manage-existing-davinci-environment.html) guide shows how to use this tool with a configured environment.

## Why do I see a planned change after import even when the defined configuration matches live infrastructure?

The PingOne API doesn't allow reading attributes that are considered secrets. For these fields, the Terraform provider only looks for mismatches between what's stored in state and what's defined in configuration, rather than refreshing state against live infrastructure. The `terraform import` command stores obfuscated values for these fields in Terraform state, and the identified change directs the Terraform provider to run an API `PUT` to bring the resource into alignment.

---

---
title: Getting started
description: The following provides guidance on preparing a PingOne tenant for Terraform access.
component: terraform
page_id: terraform::products/pingone/getting_started
canonical_url: https://developer.pingidentity.com/terraform/products/pingone/getting_started.html
revdate: March 19, 2025
section_ids:
  requirements: Requirements
  pingone-subscription-or-trial: PingOne subscription or trial
  configure-pingone-for-terraform-access: Configure PingOne for Terraform access
  finding-required-ids: Finding required IDs
  license-id-organization-id-and-organization-name: License ID, organization ID, and organization name
---

# Getting started

The following provides guidance on preparing a PingOne tenant for Terraform access.

## Requirements

* Terraform CLI 1.4+

* A licensed or trial PingOne cloud subscription. [Try Ping here.](https://www.pingidentity.com/en/try-ping.html)

* Administrator access to the [PingOne admin console](https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_signin.html).

## PingOne subscription or trial

To get started using the PingOne Terraform provider, you must first have an active PingOne cloud subscription. Get instant access with a [PingOne trial account](https://www.pingidentity.com/en/try-ping.html) or read more about Ping Identity at [pingidentity.com](https://www.pingidentity.com)

## Configure PingOne for Terraform access

The PingOne Terraform provider requires the ability to connect to the PingOne Management APIs through the use of a worker application that has administrative roles assigned.

The following steps describe how to connect Terraform to your PingOne instance using a worker application:

1. Sign on to your PingOne admin console. When you register for a trial, a link will be sent to your provided email address.

2. Open the **Administrators** environment. Note that any environment can be used.

3. Go to **Applications**.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne Administration Console](../../_images/products/pingone/getting_started/pingone-console-environment-home-applications.png)

4. Click the **+** icon to add a new application.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](../../_images/products/pingone/getting_started/pingone-console-applications-home.png)

5. Enter a name and an optional description, and ensure that **Worker** is selected as the application type.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](../../_images/products/pingone/getting_started/pingone-console-add-application.png)

6. Click the toggle to enable the application.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](../../_images/products/pingone/getting_started/pingone-console-application-settings.png)

7. On the **Roles** tab, set the administrative roles accordingly.

   The following image shows example roles to be able to create and manage environments and their configurations. You can find more information about role permissions in [Administrator Roles](https://docs.pingidentity.com/pingone/directory/p1_roles.html) in the PingOne documentation.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](../../_images/products/pingone/getting_started/pingone-console-application-roles.png)

8. On the **Configuration** tab, expand the **General** section and copy the **Client ID**, **Client Secret**, and **Environment ID** values. These IDs are used to authenticate the provider to your PingOne tenant.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](../../_images/products/pingone/getting_started/pingone-console-application-details.png)

9. You can find the steps to configure the PingOne Terraform provider using these values in the [Terraform Registry provider documentation](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs).

## Finding required IDs

There are tenant specific, unique IDs and name values that are required for the provider to operate. The following sections show how to retrieve the relevant IDs.

### License ID, organization ID, and organization name

The license ID is required when creating an environment using the [`pingone_environment` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/environment).

The organization ID and organization name can be used with the [`pingone_organization` data source](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/data-sources/organization). These values can be found with the following steps:

1. Sign on to the PingOne admin console using your unique console link.

2. Go to **Licenses**.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](../../_images/products/pingone/getting_started/pingone-console-admins-licenses.png)

3. Look for the relevant license (that's not an Admin license) and click the **Copy link** icon to copy the ID. The organization name and organization ID are also shown and can be copied.

   > **Collapse: Expand Screenshot**
   >
   > ![PingOne admin console](../../_images/products/pingone/getting_started/pingone-console-admins-licenses-detail.png)

---

---
title: Manage an existing PingOne DaVinci environment
description: The following guide walks you through the process of using the Ping CLI Terraformer plugin to:
component: terraform
page_id: terraform::products/pingone/tutorials/manage-existing-davinci-environment
canonical_url: https://developer.pingidentity.com/terraform/products/pingone/tutorials/manage-existing-davinci-environment.html
revdate: April 13, 2026
section_ids:
  prerequisites: Prerequisites
  set-up-authentication: Set up authentication
  export-terraform-configuration: Export Terraform configuration
  command-flags: Command flags
  review-and-apply-generated-configuration: Review and apply generated configuration
  configure-provider: Configure provider
  update-secret-values: Update secret values
  generate-a-plan: Generate a plan
  what-to-expect-in-the-plan: What to expect in the plan
  resources-to-be-imported: Resources to be imported
  configuration-updates: Configuration updates
  apply-the-configuration: Apply the configuration
  establish-continuous-development: Establish continuous development
  development-lifecycle: Development lifecycle
  initialize-version-control: Initialize version control
  commit-your-configuration: Commit your configuration
  next-steps: Next steps
  troubleshooting: Troubleshooting
  import-failures: Import failures
  secret-value-errors: Secret value errors
  plan-shows-unexpected-changes: Plan shows unexpected changes
  additional-resources: Additional resources
---

# Manage an existing PingOne DaVinci environment

The following guide walks you through the process of using the Ping CLI Terraformer plugin to:

* Export and generate Terraform HCL configuration from an existing PingOne DaVinci environment.

* Review and apply generated configuration.

* Begin establishing a continuous configuration management workflow using version control.

## Prerequisites

Before you begin, ensure you have:

* An existing PingOne environment with the DaVinci service enabled and configuration applied.

* A worker application with **at least** the **DaVinci Admin Read Only** role to read the live configuration.

* The `pingcli-terraformer` command-line tool installed. Refer to the [Ping CLI Terraformer plugin repository](https://github.com/pingidentity/pingcli-plugin-terraformer) for installation instructions.

* Terraform 1.5 or later installed.

* Git for version control (optional, but recommended).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You will need a higher role, such as **DaVinci Admin** or a custom role with write access to the [flow export endpoint](https://developer.pingidentity.com/pingone-api/davinci/davinci-admin-apis/admin-flow-versions/export-flow-version.html), on the worker application to generate DaVinci Variable dependencies within DaVinci Flows. If the `pingcli-terraformer` tool can't access the endpoint, a warning will be returned and generation of the dependency will be skipped. |

## Set up authentication

Configure your worker application credentials for use by the `pingcli-terraformer` tool:

```bash
export PINGCLI_PINGONE_ENVIRONMENT_ID="<your-environment-id>"
export PINGCLI_PINGONE_CLIENT_CREDENTIALS_CLIENT_ID="<your-client-id>"
export PINGCLI_PINGONE_CLIENT_CREDENTIALS_CLIENT_SECRET="<your-client-secret>"
export PINGCLI_PINGONE_REGION_CODE="NA"  # or EU, AP, CA, AU
```

## Export Terraform configuration

Use the `export` command to generate Terraform HCL from your live environment. The export:

* Reads all Terraform-supported resources in the live environment.

* Converts API responses to a reusable Terraform module.

* Abstracts environment-specific values to variables.

* Maps dependencies between resources for deployment ordering.

For managing an existing environment, run the export with the `--include-imports` and `--include-values` flags:

```bash
pingcli-terraformer export \
  --include-imports \
  --include-values
```

### Command flags

| Flag                                                                                                                           | Description        | `--include-imports`                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------ | ----------------------------------------------------------------------------------------- |
| Generates import blocks for each identified resource, enabling you to bring existing infrastructure under Terraform management | `--include-values` | Produces a `terraform.tfvars` file populated with actual values from the live environment |

The export creates a version-control-ready module that can be used standalone or composed into a larger root module.

## Review and apply generated configuration

Next, you will review the generated configuration to prepare for what will occur in a subsequent apply.

### Configure provider

The export generates a `versions.tf` file that specifies the expected PingOne Terraform provider version. You can add provider authentication directly to this file or supply credentials through environment variables. You can find details in the [Provider Authentication documentation](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs#provider-authentication).

Run `terraform init` to initialize the provider and download dependencies:

```bash
terraform init
```

### Update secret values

PingOne DaVinci has secret attributes (such as client application secrets) that are **not readable using APIs**. You must update these manually before importing:

1. Open the generated `ping-export-terraform.auto.tfvars` file.

2. Locate and update all fields marked as `# Secret value - provide manually`.

|   |                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All of the variable values in the `ping-export-terraform.auto.tfvars` could be considered sensitive or environment specific. This file should not be committed to version control. For automated Terraform deployments, the values to these secrets should be managed through the deployment tool or secrets manager. |

### Generate a plan

Output the plan to a file for review:

```bash
terraform plan -no-color > tfplan-1.txt 2>&1
```

### What to expect in the plan

The size of your Terraform plan will correspond to the size of your live infrastructure. The initial `terraform plan` and `terraform apply` process can produce the described actions.

#### Resources to be imported

The majority of the resources will show as items that will be brought under Terraform management without any interaction with the live infrastructure. This indicates that the defined HCL for the resource matches what would be stored in state exactly. For example, `module.ping-export.pingone_davinci_variable.pingcli__myVar_flowInstance will be imported`.

The generated `ping-export-imports.tf` file includes an import block and a commented-out `terraform import` command for each discovered resource. The import commands can be run in a terminal prior to `terraform apply` to minimize the size of the Terraform plan and focus on items that can indicate live infrastructure interactions. For an environment with around 100 resources, this sequential import process takes approximately 5 minutes.

#### Configuration updates

Resources that show `will be updated in-place` typically indicate that there will be an API call made to the live infrastructure. Some updates might be considered non-functional changes, even though there's an API call made to the live infrastructure. There could be cases where functional and non-functional changes are identified on the same resource, so you should carefully review all planned changes before moving forward.

Common planned changes include:

* **Default values**: The Terraform provider includes default values for certain attributes to maintain consistency in continuous management. For example, the DaVinci Flow resource schema expects a `default_log_level` of `4`, so this value is injected in the generated HCL, even if it's not found on the API read. This change will run an API `PUT` to update the flow to bring the live infrastructure into alignment with the defined configuration.

* **Deploy triggers**: If there is an update to a flow, the current version and published version will be out of sync, so the generated configuration will also look to `deploy` the flow for realignment.

* **Computed values**: Changes marked with `~` and ending in `(known after apply)` represent computed attributes updating to their refreshed state. These are non-functional. A resource whose plan shows only computed updates will not appear as an item to change.

* **Resources with secret values**: The PingOne API doesn't allow reading values of attributes that are considered secrets. For these values, the Terraform provider only looks for mismatches between what is stored in state and what is defined in configuration, rather than refreshing state against live infrastructure. If a `terraform import` command was run prior to this step, an obfuscated value will show in Terraform state. The identified change directs the Terraform provider to run an API `PUT` to bring the resource into alignment. This is a common case for Connector Instances that include client secrets as values. The `properties` attribute of a Connector Instance is considered sensitive, and child values are grouped together. You must be careful to ensure that your defined configuration on such resources is exact before running `terraform apply`.

The following is an example of a `terraform plan` output after running `terraform import` commands:

```text
# module.davinci.pingone_davinci_flow.my_flow will be updated in-place
  ~ resource "pingone_davinci_flow" "pingcli__OOTB-0020---0020-Account-0020-Recovery-0020-by-0020-Email" {
    ...
      ~ current_version   = 1 -> (known after apply)
      ~ settings          = {
          + log_level = 4
        }
        # (4 unchanged attributes hidden)
    }

  # module.ping-export.pingone_davinci_flow_enable.pingcli__OOTB-0020---0020-Account-0020-Recovery-0020-by-0020-Email will be updated in-place
  ~ resource "pingone_davinci_flow_enable" "pingcli__OOTB-0020---0020-Account-0020-Recovery-0020-by-0020-Email" {
      ~ enabled        = true -> (known after apply)
        id             = "01af583c6b951086992eb3c37aed7af5"
        # (2 unchanged attributes hidden)
    }
```

### Apply the configuration

After you're satisfied with the plan:

```bash
terraform apply
```

After approving the plan, your PingOne DaVinci environment is fully managed by Terraform.

## Establish continuous development

With your existing environment under Terraform management, you can adopt a continuous configuration management workflow.

### Development lifecycle

The typical development lifecycle:

1. Build features or changes in the PingOne UI.

2. Export those changes using `pingcli-terraformer export`.

3. View changes with your IDE or using `git diff --unified=0`.

4. Validate in Terraform. `terraform plan` should refresh state against the live environment and result in no changes required.

5. Commit to version control so changes can be picked up by automated pipelines.

6. Promote to higher environments through your CI/CD pipeline.

### Initialize version control

If you haven't already, initialize a Git repository:

```bash
git init
```

Create a `.gitignore` to exclude sensitive and generated files:

```none
# Terraform
.terraform/
.terraform.lock.hcl
*.tfstate
*.tfstate.*
tfplan*

# Sensitive or environment-specific
.env
.env.*
*.tfvars
*imports.tf
```

### Commit your configuration

```bash
git add .
git commit -m "Initial Terraform configuration for DaVinci environment"
```

### Next steps

* Set up a CI/CD pipeline to automate `terraform apply` for higher environments

* Establish branching strategies for development, staging, and production

* Document your team's workflow and approval processes

* Consider using Terraform workspaces or separate state files per environment

## Troubleshooting

### Import failures

* Verify that your Terraform provider worker application has the correct **DaVinci Admin** role

* Check that the resource IDs in the generated imports file are correct

* Ensure Terraform 1.5 or later is installed

### Secret value errors

* Confirm that all fields marked `# Secret value - provide manually` in the generated `terraform.tfvars` file have been updated

* Verify that secret values are correctly formatted (no extra spaces or newlines)

### Plan shows unexpected changes

* Review the diff carefully: some resources might receive default values on first apply

* Check whether API responses have changed since the export was generated

* Re-run the export if the environment was modified during the import process

## Additional resources

* [Ping CLI Terraformer repository](https://github.com/pingidentity/pingcli-plugin-terraformer)

* [Terraform import documentation](https://www.terraform.io/docs/cli/import/index.html)

* [PingOne DaVinci documentation](https://docs.pingidentity.com/davinci)
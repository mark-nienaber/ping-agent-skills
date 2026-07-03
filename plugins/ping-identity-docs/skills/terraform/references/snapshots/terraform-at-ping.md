---
title: Benefits of Terraform with Ping Identity deployments
description: The following sections describe the benefits of using Terraform with Ping Identity deployments.
component: terraform
page_id: terraform::terraform_at_ping/benefits_of_using_terraform_with_ping
canonical_url: https://developer.pingidentity.com/terraform/terraform_at_ping/benefits_of_using_terraform_with_ping.html
revdate: March 19, 2025
section_ids:
  accelerating-configuration-promotion: Accelerating configuration promotion
  accelerating-development-cycles: Accelerating development cycles
  protecting-against-accidental-or-malicious-configuration-changes: Protecting against accidental or malicious configuration changes
  consistent-and-homogenous-configuration-as-code-syntax: Consistent and homogenous Configuration as Code syntax
  auditability-and-readability-of-changes: Auditability and readability of changes
---

# Benefits of Terraform with Ping Identity deployments

The following sections describe the benefits of using Terraform with Ping Identity deployments.

## Accelerating configuration promotion

Terraform enables developers to define configuration once during development, create a Configuration as Code package, and then deploy that configuration consistently across different environments (development to test, test to production, and so on). By using Terraform's variables and modules, developers can easily parameterize configuration (use cases, solutions, and applications) and adapt them to each environment's specific requirements. This approach has the following benefits:

* Reduces the risk of errors and inconsistencies during deployment promotion and accelerates time to value for new features and end user experiences.

* Reduces the time needed to align configuration between environments.

* Enables quick rollback of configuration.

To get best value from accelerating configuration promotion, consider:

* Using GitOps methodology to store Terraform configuration as code in source control.

* Version controlling logical releases to accurately report the version of a solution that has been applied to any environment.

* Define a strong code review and change audit process to allow configuration owners to review and comment on potential changes before they enter (or during) the deployment pipeline.

* Apply testing automation to quickly alert to potential regression issues and gain confidence that configuration changes will be successful when deployed to production.

## Accelerating development cycles

Terraform accelerates multi-team development cycles by providing a standardized, code-driven approach to infrastructure and configuration management. Using Configuration as Code, teams can use industry standard GitOps tools, such as a common source control repository or central deployment and testing pipeline, to rapidly merge changes with full audit and approval control. This approach can allow:

* Ephemeral, on-demand environments to prevent multiple teams from conflicting in the same development environment.

* Rapid refreshes of development environments to avoid conflict with experimental or sandbox configurations.

* Clear definitions of ownership and change review, where different teams can be responsible for their own configuration and be notified for review and approval if a team's configuration is altered by a different team.

* Use cases, applications, and solutions can be modularized to help prevent configuration sprawl.

## Protecting against accidental or malicious configuration changes

As an out-of-the-box feature, Terraform compares the configuration that it's stored in Terraform state (from the last successful Terraform operation), the configuration the developer defines in the Configuration as Code HCL, and the configuration at the point in time that is active on the live service. When comparing these three sources, Terraform can determine whether configuration has been modified in the HCL by the developer (the live service should be updated to align with the developer's intention), or whether configuration has been modified in the live service (and not in Terraform HCL or state, meaning the live service has changed unexpectedly) and the live service should be corrected.

If the live service configuration has changed unexpectedly, this change might indicate an accidental or malicious configuration change. In Ping Identity systems, such a change might lead to an issue in the user experience, a weakened IAM security policy, or an untested or unapproved use case.

Consider running Terraform on a regular schedule to alert administrators to potential drift in configuration so that the cause can be investigated. Optionally, as part of the scheduled run, Terraform can be configured to be run to automatically remediate changed configuration to return the environment back to the originally tested state.

## Consistent and homogenous Configuration as Code syntax

Terraform provides two styles of Configuration as Code: Hashicorp Configuration Language (HCL) and JSON. For the Terraform community, both HCL and JSON are well understood, and the syntax can be applied to Ping Identity or any other supported third-party system. Both styles of code provide a consistent look and feel and have rich support for well-known code editors.

While both HCL and JSON are human and machine readable, the HCL style can be better organised by the developer to improve readability by:

* Adding lines of comments to add additional context to readers.

* Separating large code files into smaller, discrete files where file names provide clear direction as to the purpose of the contained HCL.

* Separating groups of files or repeated HCL code into clearly defined, well documented modules.

* Use of new line separators to create natural spacing between resources and data sources.

JSON can be used where machine readability (programatic manipulation) might be required over human readability.

## Auditability and readability of changes

When using Terraform to perform changes to a live service, Terraform provides a full list of proposed changes during the plan generation phase using the `terraform plan` command.

The full list of changes allows the developer to track:

* What new configuration resources are to be created in the live service (new resources have been added to the code by the developer).

* What existing configuration resources need to be modified (the developer has requested changes in the code, or the live service configuration needs correcting).

* What existing configuration resources should be deleted (resources have been removed from the code by the developer).

This `plan` output provides Ping Identity configuration administrators with an ability to review all the changes to an environment before they are made, allowing teams to understand the impact of proposed changes and potentially stop any accidental changes from being applied to an environment.

The `plan` output also provides a way to record, in audit, what configuration changes have been requested to be made to an environment. When reviewed alongside the `apply` output, auditors can trace configuration changes that have been made to an environment over time.

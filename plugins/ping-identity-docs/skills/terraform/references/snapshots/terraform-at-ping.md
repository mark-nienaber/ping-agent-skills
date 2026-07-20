---
title: Benefits of Terraform with Ping Identity deployments
description: Describes the benefits of using Terraform with Ping Identity deployments, including configuration promotion, auditability, and drift protection
component: terraform
page_id: terraform::terraform_at_ping/benefits_of_using_terraform_with_ping
canonical_url: https://developer.pingidentity.com/terraform/terraform_at_ping/benefits_of_using_terraform_with_ping.html
llms_txt: https://developer.pingidentity.com/terraform/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

---

---
title: What is Terraform
description: "Introduces Terraform, Terraform providers, state, resources, and data sources, and how they're used with Ping Identity products"
component: terraform
page_id: terraform::terraform_at_ping/what_is_terraform
canonical_url: https://developer.pingidentity.com/terraform/terraform_at_ping/what_is_terraform.html
llms_txt: https://developer.pingidentity.com/terraform/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  key-use-cases: Key use cases
  terraform-providers: Terraform providers
  terraform-state: Terraform state
  terraform-resources: Terraform resources
  terraform-data-sources: Terraform data sources
  meet-use-cases: Using providers, resources, and data sources to meet key use cases
---

# What is Terraform

[HashiCorp Terraform](https://www.terraform.io/) is an open-source Infrastructure as Code (IaC) and Configuration as Code (CaC) tool that allows developers to define and provision infrastructure using a declarative configuration language named [Hashcorp Configuration Langugage (HCL)](https://developer.hashicorp.com/terraform/language/syntax/configuration). It enables developers to manage infrastructure and configuration as code, which can be managed similarly to code a developer writes for an application. This includes using industry standard GitOps methodologies for version control, multi-team collaboration, and automation benefits.

## Key use cases

* **Multi-product configuration management**: Provision and manage interdependent configuration across multiple Ping Identity products and third-party service providers.

* **Multi-cloud infrastructure management**: Provision and manage infrastructure across multiple cloud providers, on-premises data centers, and SaaS platforms.

* **Configuration as Code**: Define and manage Ping Identity product configurations in a human-readable and machine-executable format.

* **Use Case Deployment**: Provision the necessary configuration for use case deployment, ensuring consistency and repeatability between environments.

* **Templated Configuration**: Create reusable and sharable configuration templates for product configuration, including policies, application integrations, and use cases.

* **Platform Orchestration:** Manage complex infrastructure and configuration dependencies between Ping Identity products and customer applications and services.

## Terraform providers

Providers are plugins that allow Terraform to interact with Ping Identity's products and services. They define the API interactions necessary to create, read, update, and delete resources on those platforms according to the HCL source code that the user defines. For example, the [PingOne Terraform provider](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs) allows Terraform to manage PingOne configuration resources such as applications, schema attributes, policy configuration, branding, localised translations, and more.

Learn more in [Hashicorp Terraform providers](https://developer.hashicorp.com/terraform/language/providers).

## Terraform state

A key feature of Terraform is the Terraform state. The Terraform state represents a stored record of the configuration successfully applied at the last run of Terraform, where configuration changes were made by Terraform. During execution, Terraform compares the configuration stored in Terraform state with the actual configuration of the live service to determine whether configuration has unexpectedly changed.

If the configuration of the live service has changed relative to the stored state, Terraform can issue configuration changes to realign the live service back to the stored state, effectively correcting any unauthorized or unexpected configuration changes that could lead to service outages or vulnerabilities.

Terraform state can be managed in different ways and should always be kept secure.

Learn more in [Hashicorp Terraform state](https://developer.hashicorp.com/terraform/language/state).

## Terraform resources

Resources represent the individual components of Ping Identity product configurations. They are the building blocks of a fully configured environment and manage the lifecycle of configuration resources through create, update, and delete actions. Resources typically align with a single API endpoint, and each resource is defined with a schema of fields that reflects that API's request and response payload and is used to specify the desired state. For configuration that a resource manages, the resource will retrieve the current configuration in the live service so that the configuration can be compared against the Terraform state and the developer's HCL. If changes are detected, Terraform will create a plan of action to reconcile and complete the changes.

For example, in the [PingOne Terraform provider](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs), the Terraform developer can define a single instance of an application using the [`pingone_application` resource](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/resources/application). Terraform can then manage the ongoing lifecycle of the application's configuration, including taking corrective actions if the configuration unexpectedly changes.

Learn more in [Hashicorp Terraform resources](https://developer.hashicorp.com/terraform/language/resources).

## Terraform data sources

Data sources allow Terraform to retrieve information about existing, unmanaged configuration or data from external systems. This enables developers to dynamically configure resources based on existing state or external inputs from data sources. Data sources typically align with a single API endpoint, and each data source is typically defined with a schema of fields that reflects that API's response payload and is used to retrieve some configuration state.

Terraform doesn't manage configuration using a data source, as data sources are read only.

For example, in the [PingOne Terraform provider](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs), the Terraform developer can read a single instance of an application using the [`pingone_application` data source](https://registry.terraform.io/providers/pingidentity/pingone/latest/docs/data-sources/application).

Learn more in [Hashicorp Terraform data sources](https://developer.hashicorp.com/terraform/language/data-sources).

## Using providers, resources, and data sources to meet key use cases

* The Terraform developer selects the appropriate provider for their target platform (for example, PingOne provider for PingOne).

* The Terraform developer then defines resources within their Terraform configuration files, specifying the desired state of each configuration item. A resource's Terraform code can be defined either:

  * Manually using the [Terraform Registry documentation](https://registry.terraform.io/namespaces/pingidentity) as a guide.

  * Export/Generation using Ping Identity's developer tools. Learn more in [Exporting configuration](../develop_with_terraform/exporting_configuration.html).

* Data sources are used to retrieve dynamic information, enabling flexible and adaptable configurations based on outside conditions.

* Terraform uses the selected provider to interact with the target platform's API to create, modify, or delete the defined resources.
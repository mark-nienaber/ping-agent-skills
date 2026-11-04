---
title: Exporting Terraform configuration
description: Use Ping CLI or Ping CLI Terraformer to export live configuration and generate Terraform HCL for promotion to test and production environments
component: terraform
page_id: terraform::develop_with_terraform/exporting_configuration
canonical_url: https://developer.pingidentity.com/terraform/develop_with_terraform/exporting_configuration.html
llms_txt: https://developer.pingidentity.com/terraform/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 13, 2026
section_ids:
  using-ping-cli-to-generate-terraform-configuration: Using Ping CLI to generate Terraform configuration
  using-ping-cli-terraformer-to-generate-terraform-configuration: Using Ping CLI Terraformer to generate Terraform configuration
---

# Exporting Terraform configuration

When working with Terraform, you should configure use cases in the Ping Identity administration console (typically in the development environment) and then export that configuration to Terraform HCL to promote it to your test and production environments.

Terraform includes experimental out-of-the-box functionality to export or generate configuration from a configured environment. You can find more details in the [Terraform documentation](https://developer.hashicorp.com/terraform/docs).

## Using Ping CLI to generate Terraform configuration

Terraform's out-of-the-box capability depends on the `import {}` block capability described in [Importing to Terraform state](importing_to_state.html).

Ping CLI has features to simplify generating Terraform HCL code for an environment. The `platform export` command is designed to connect to a supported Ping Identity product, read the live configuration of the service, and generate the required Terraform HCL files with clearly labelled `import {}` blocks, complete with all necessary IDs. The developer can then use the [Generate Terraform Configuration](https://developer.hashicorp.com/terraform/language/import/generating-configuration) feature to generate the full HCL for an environment. The developer can then choose which configuration items to include their Terraform HCL project.

## Using Ping CLI Terraformer to generate Terraform configuration

The [Ping CLI Terraformer plugin](https://github.com/pingidentity/pingcli-plugin-terraformer) provides an `export` command to generate an opinionated Terraform configuration. Similar to the `pingcli platform export` command, `pingcli-terraformer export` is designed to connect to a supported Ping Identity product and read the live configuration of the service. After reading the live configuration, the tool generates complete HCL and can optionally include automated post-processing used for safely storing Terraform configuration in version control and for promotion between environments. This post-processing includes updates such as converting environment-specific fields to variables and mapping identified dependencies using native Terraform references.

---

---
title: Getting support
description: Find support options for Ping Identity Terraform providers, including the community forum, GitHub issues, and Ping Identity Support tickets
component: terraform
page_id: terraform::develop_with_terraform/getting_support
canonical_url: https://developer.pingidentity.com/terraform/develop_with_terraform/getting_support.html
llms_txt: https://developer.pingidentity.com/terraform/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
---

# Getting support

Ping Identity's Terraform providers are delivered as open-source projects and can be found on [Ping Identity's GitHub account](https://github.com/pingidentity) according to Hashicorp's Terraform provider publishing guidelines. There are multiple ways to get support when using Ping Identity's Terraform providers:

* Community Forum: The DevOps developer forum provides a quick and simple way to interact with an active community of subject matter experts, including Ping Identity technical staff, customer, and partner specialists. The community forum is ideal for specific questions on how best to configure Ping Identity products using Terraform HCL to meet use cases.

* GitHub project issues: Each Terraform provider has a GitHub repository where open source provider code is published, and each repository has the GitHub issues feature enabled. With a GitHub account, anyone can create issues on the relevant project by filling in the provided template. Using GitHub project issues is ideal when requesting new features, enhancements, or reporting unexpected errors or provider bugs. The GitHub issues are closely monitored and are a quick and easy way to interact directly with the project team.

* Ping Identity Support: For customers with an active product license, support tickets can be raised according to the normal Ping Identity Support process. Raising a support ticket is ideal when there is a potential issue with the underlying product, or the issue should be tracked with the account team.

---

---
title: Importing to Terraform state
description: Bring existing product configuration under Terraform management by importing it to Terraform state using import blocks or Ping CLI
component: terraform
page_id: terraform::develop_with_terraform/importing_to_state
canonical_url: https://developer.pingidentity.com/terraform/develop_with_terraform/importing_to_state.html
llms_txt: https://developer.pingidentity.com/terraform/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  using-ping-cli-to-generate-import-blocks: Using Ping CLI to generate import blocks
---

# Importing to Terraform state

Terraform maintains a storage of the last known configuration of a product environment. This is to allow Terraform to compare the **intended** configuration of an environment (declared using the Terraform code language, HCL), with the actual configuration of the environment (which the provider will do when reading the current configuration of an environment using the service API), with what Terraform believes is the last known configuration of an environment. Terraform compares these three sources to reconcile configuration and produce an action plan to fix configuration drift in an environment, while simultaneously handling configuration additions and deletions.

Terraform state is a required component of Terraform management of an environment and must be handled securely. The storage mechanism of the Terraform state is left to the customer to decide. You can find more information and HashiCorp's own best practices when handling Terraform state in [State](https://developer.hashicorp.com/terraform/language/state) in the HashiCorp documentation.

You should not manage Terraform state configuration manually using a text editor. Terraform manages the state file itself in two ways:

1. By declaring end-state configuration in Terraform HCL and running the `terraform plan` and `terraform apply` commands. This method is most common when adding net-new configuration to a product, meaning that Terraform manages the full lifecycle of a configuration item including its initial creation.

2. By importing predefined configuration in an environment, using `import {}` block HCL code or using the `terraform import` command. This method is most common when bringing existing product configuration under Terraform control, where Terraform cannot manage the initial creation of that configuration.

Importing configuration is most suited to production environments that have been previously built and managed without using Terraform. Importing configuration to Terraform state is non-destructive (meaning that configuration is not expected to be removed or re-added). After configuration for an environment is imported to Terraform state, Terraform can manage the lifecycle of the imported configuration in the normal way.

## Using Ping CLI to generate import blocks

Terraform's out-of-the-box import capability requires the developer to import each configuration item individually by its unique ID. When working with Ping Identity products and Ping Identity Terraform providers, the required ID used for importing a specific configuration item could be a single ID or a compound ID (where two or more IDs are concatenated together with a `/` forward slash separator). Depending on the Ping Identity product, the ID could be customer developer defined or could be a platform generated UUID. In both cases, the customer developer might have difficulty in retrieving the required IDs for all configuration for a product environment.

The Ping CLI command-line tool has features to simplify importing configuration to Terraform state. The `platform export` command is designed to connect to a supported Ping Identity product, read the live configuration of the service, and generate the required Terraform HCL files with clearly labelled `import {}` blocks, complete with all necessary IDs. The developer can then import all configuration for an environment or choose which configuration items to include in import.

---

---
title: Interface stability
description: "Explains how Ping Identity's semantic versioning and release practices provide stability and predictability for Terraform provider development"
component: terraform
page_id: terraform::develop_with_terraform/interface_stability
canonical_url: https://developer.pingidentity.com/terraform/develop_with_terraform/interface_stability.html
llms_txt: https://developer.pingidentity.com/terraform/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  breaking-changes: Breaking changes
---

# Interface stability

To provide predictability and stability when developing Terraform HCL, Ping Identity's development practices align with development guidelines set out by Hashicorp and follow the expectations of the Hashicorp community.

When developing Terraform providers, Ping Identity follows the SemVer (Semantic Versioning) methodology set out at [Semver.org](https://semver.org).

This includes a regular cadence of major, minor and patch versions of each Terraform provider. Releases are issued on the respective GitHub code repositories using GitHub's Releases feature. Changelogs are compiled on each release that provide a list of issues resolved, enhancements, new features, general updates, and any breaking changes that might cause HCL developers to alter the Terraform code in order to use the update.

High-level descriptions of the release types are:

* Major releases: Typically once every year or couple of years. Major releases are issued when significant changes are made to the Terraform provider and typically require customers to change their HCL code, otherwise known as breaking changes.

* Minor releases: Typically on a planned schedule, such as every few weeks or aligned with product releases. Minor releases are issued when the providers are enhanced with additional, optional functionality and can also include planned bug fixes.

* Patch releases: Typically ad-hoc, patch releases are issued between minor releases where bug fixes or documentation updates must be released before the next minor release.

Learn more about major, minor, and patch releases at [Semver.org](https://semver.org)

## Breaking changes

Breaking changes to a Terraform provider typically require the customer Terraform developer to make changes to the written HCL before they can use the update.

Breaking changes are required periodically to ensure Ping Identity's Terraform providers remain aligned with the product API. Significant breaking changes are typically planned in advance to be released in-bulk in the major release cycle.

As part of Ping Identity's development practices, breaking changes are kept to a minimum and are planned as technical debt in the major release cycle. It's uncommon for breaking changes to occur in minor and patch releases.

Occasionally, breaking changes cannot be included in the major release cycle and must be included in a minor release to ensure that the provider functions correctly. These breaking changes are marked clearly in the release notes.

Some examples of breaking changes are: \* Scheduled removal of previously deprecated functionality. \* Renaming resources, data sources, or functions without following a deprecation path. \* Renaming or removing schema fields without following a deprecation path. \* Changing an Optional field to be Required in a resource or data source schema.

When breaking changes are made to a provider, these are highlighted in the release notes. If the change requires significant rework of HCL code, or the corrective action cannot be included in the release note, or if there are many breaking changes to be handled, then a specific guide might be created and published on the Terraform registry to assist with the conversion process. Upgrade and migration guides are typically created when major releases are issued.
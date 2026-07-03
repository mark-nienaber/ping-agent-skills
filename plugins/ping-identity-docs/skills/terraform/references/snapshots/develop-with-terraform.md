---
title: Exporting Terraform configuration
description: When working with Terraform, you should configure use cases in the Ping Identity administration console (typically in the development environment) and then export that configuration to Terraform HCL to promote it to your test and production environments.
component: terraform
page_id: terraform::develop_with_terraform/exporting_configuration
canonical_url: https://developer.pingidentity.com/terraform/develop_with_terraform/exporting_configuration.html
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

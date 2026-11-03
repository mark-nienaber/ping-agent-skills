---
title: Develop with Terraform
description: Overview of guides for importing, exporting, and understanding interface stability and support when developing with Ping Identity Terraform providers
component: terraform
page_id: terraform::develop_with_terraform
canonical_url: https://developer.pingidentity.com/terraform/develop_with_terraform.html
llms_txt: https://developer.pingidentity.com/terraform/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 19, 2025
section_ids:
  importing-to-terraform-state: Importing to Terraform state
  exporting-and-generating-terraform-hcl: Exporting and generating Terraform HCL
  interface-stability: Interface stability
  getting-support: Getting support
---

# Develop with Terraform

## Importing to Terraform state

Learn how to take a preconfigured product environment and import to Terraform state. Importing to Terraform state allows Terraform to manage a product environment without needing to recreate any configuration for that environment. This is useful when bringing a production environment under Terraform control retrospectively.

[Importing to Terraform state](develop_with_terraform/importing_to_state.html)

## Exporting and generating Terraform HCL

Learn how to generate Terraform HCL configuration for a preconfigured environment. This is useful when exporting configuration from a development environment to store in source control, or promote to test or production.

[Exporting Terraform configuration](develop_with_terraform/exporting_configuration.html)

## Interface stability

Learn how Ping Identity's development practices provide stability and predictability when using Ping Identity's Terraform providers.

[Interface stability](develop_with_terraform/interface_stability.html)

## Getting support

Learn where and how to get support on Ping Identity's Terraform providers.

[Getting support](develop_with_terraform/getting_support.html)
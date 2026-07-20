---
title: Configuration Promotion at Ping Identity
description: Learn how to automate configuration promotion for Ping Identity solutions using GitOps, Terraform, and the Ping CLI command-line tool
component: config-automation-promotion
page_id: config-automation-promotion::configuration_promotion_landing_page
canonical_url: https://developer.pingidentity.com/config-automation-promotion/configuration_promotion_landing_page.html
llms_txt: https://developer.pingidentity.com/config-automation-promotion/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 24, 2025
section_ids:
  learn-about-configuration-promotion-automation: Learn about configuration promotion automation
  gitops-cicd-pipeline-examples: GitOps CI/CD Pipeline Examples
  ping-identity-developer-tools-terraform: "Ping Identity developer tools: Terraform"
  ping-identity-developer-tools-ping-cli: "Ping Identity developer tools: Ping CLI"
---

# Configuration Promotion at Ping Identity

Effective configuration promotion is paramount to the success and stability of modern Ping Identity solutions within an overall multi-vendor solution. By adopting a systematic and well-planned approach to configuration management and configuration promotion automation, organizations can mitigate deployment risks, ensure consistency, and streamline the configuration promotion process.

Configuration promotion is not just a technical process. It is a strategic endeavor that demands collaboration, communication, and adherence to best practices. Through version control, automated testing, thorough code reviews, and staged environment deployments, teams can confidently and reliably push configurations from development to test, then test to production.

## Learn about configuration promotion automation

Learn about configuration promotion automation concepts and how Ping Identity deployments align with industry-standard GitOps methodology.

* [Overview](concepts/overview.html)

* [Configuration as Code (CaC)](concepts/configuration_as_code.html)

* [Testing Automation](concepts/automated_testing.html)

* [Auditing and Reviewing Changes](concepts/auditing_and_reviewing_changes.html)

* [Promoting and Deploying Configuration](concepts/promoting_and_deploying_configuration.html)

* [Verifying Deployed Configuration](concepts/verifying_deployed_configuration.html)

## GitOps CI/CD Pipeline Examples

Use the provided examples and templates to start your own Ping Identity Configuration Promotion Automation project.

* [GitOps Pipeline Examples](configuration_promotion_pipeline_examples.html)

## Ping Identity developer tools: Terraform

Use Terraform to create configuration as code packages for Ping Identity product configuration. Declare end-state configuration and use Terraform to manage deployment of configuration to development, testing, staging and production environments. Use Terraform's drift detection and auto-healing capabilities to ensure configuration remains accurate and consistent.

* [Get Started using Ping Identity's Terraform providers](https://terraform.pingidentity.com)

## Ping Identity developer tools: Ping CLI

Use Ping CLI to export configuration from fully configured Ping Identity deployments, generate Terraform import logic to import fully configured environments to Terraform state and script configuration management API calls.

* [Get Started using Ping CLI](https://developer.pingidentity.com/pingcli)
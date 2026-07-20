---
title: Terraform for Ping Identity Configuration
description: Declarative infrastructure-level Ping Identity configuration as code for managing Ping Identity environments in sandbox and production contexts.
component: build-with-ai
page_id: build-with-ai:terraform:overview
canonical_url: https://developer.pingidentity.com/build-with-ai/terraform/overview.html
llms_txt: https://developer.pingidentity.com/build-with-ai/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 18, 2026
keywords: ["Terraform", "infrastructure as code", "IaC", "Ping Identity", "configuration", "CI/CD", "GitOps", "agent"]
section_ids:
  what-terraform-manages: What Terraform manages
  role-in-agentic-workflows: Role in agentic workflows
  working-alongside-ping-cli: Working alongside Ping CLI
  providers-and-resources: Providers and resources
  full-documentation: Full documentation
---

# Terraform for Ping Identity Configuration

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]DaVinci [icon: circle-check, set=far]Authorize [icon: circle-check, set=far]Credentials [icon: circle-check, set=far]MFA [icon: circle-check, set=far]Protect [icon: circle-check, set=far]Verify [icon: circle-check, set=far]PingFederate

Terraform allows Ping Identity platform configuration to be expressed as declarative `.tf` files in version control. Rather than applying changes imperatively through a console or CLI, you define the desired state and Terraform reconciles the current state to match it.

In agentic workflows, Terraform plays different roles depending on the environment. In development and sandbox, agents can work with `.tf` files directly. In production, agents propose changes that the pipeline validates and applies after a review gate.

## What Terraform manages

Terraform providers for Ping Identity platforms expose identity infrastructure resources as Terraform-managed objects. These typically include:

* Environments and populations

* OAuth 2.0 / OIDC application registrations

* Identity provider connections

* Sign-on policies and authentication policies

* Resource definitions and scopes

* Organizational structure and role assignments

Where Ping CLI excels at imperative, ad-hoc operations; exporting configuration, querying current state, and running a one-off promotion, Terraform excels at maintaining the authoritative declared state of an environment over time.

|                   | Ping CLI                                                     | Terraform                                                                                                                    |
| ----------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Style             | Imperative (do this)                                         | Declarative (be this)                                                                                                        |
| Typical use       | Export, introspect, promote, run pipelines                   | Define and maintain environment configuration state                                                                          |
| State management  | Stateless operations                                         | Tracks state file; reconciles drift                                                                                          |
| Agent interaction | Agent invokes CLI commands as tools                          | Sandbox: agent edits `.tf` files and runs plan/apply directly; production: agent edits `.tf` files, pipeline runs plan/apply |
| Best for          | Sandbox prototyping, pipeline operations, one-off automation | Long-lived environments, repeatable infrastructure                                                                           |

## Role in agentic workflows

![terraform-iac-workflow](https://kroki.io/plantuml/svg/eNp1U8Fu2zAMvesriOyyHpqeukMHDPCctuilMNJhp14UiXaEyqIgKUmDYf8-SrYzd8kUIJbFp8fHRzq-GedlkD0o6j05dOklHS1CQJWk6yyKeIJobOXOph_4niprOtczGhT_YZihqhDoUJOlAJ9uy5oF6ynLd6neukA7p0foQ1kXoRQ0hhFWlTWDNUwkOzznu82_C8A5W13WDPRMCS9Jq--__Iua86x4sSohVeLXRfUEVcfKFyAjyLwTwg_pYfETQzTkuD6XAtkF_BLw131YLFMLrbEYX93nR5O4E56iYd7jVeFLbYmK3zPO-ummXkFjPFrj8IySGxRkS6EHb6UbWfL2I2yNe4MHeJQJOfd210sHXI4na9SYPBTI_9il9_Y40pf9B5GNcR00VqaMPdN47_YmUJkprrzi20bJxEbxW5MVGIyF2jNN5i2-wvX1t8kRuAMfiM1CUFue3eIgarbwZOmVmLDDvewBX-sxsMAbaNaQguk6nucxlmFDzQyLWzqANm0rxqOBpFTKYX4G2qMW01EOZ7Uc48-JnOLMkOjVaVRWBtQQE3sthON5gg2lRD1QO04MwIt0ekPvd8MB5FJ4nJwuPrMdrCV_pva4ZHATSO9UNmzCj2bEryxiGIzp4lIgs-SsZ7lPDV5xnWAi7E00G9a9QW7bwFDyrcnaDbeWARK6Mqd7DGlG_QcZH4Qu)

In development and sandbox environments, agents can read, modify, and apply `.tf` files directly. This supports rapid prototyping and is appropriate where strict governance is not required.

In production, agents propose changes to `.tf` files; the pipeline runs `terraform plan`, presents a diff for review, and then applies. The plan diff is the primary mechanism for catching errors before they reach a live environment.

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In production pipelines, the apply step belongs to the pipeline after a diff review gate, not to the agent directly. Always run `terraform plan` and review the output before `terraform apply` in production. |

## Working alongside Ping CLI

Terraform and Ping CLI address different parts of the configuration lifecycle and work well together in the same pipeline:

* **Ping CLI** introspects environments, exports configuration, and runs promotions between environments. It is well-suited for one-off operations and pipeline orchestration.

* **Terraform** manages the authoritative declared state of an environment's infrastructure configuration. It is well-suited for long-lived environments where drift detection and state reconciliation matter.

A typical pipeline might use Ping CLI to export a configuration baseline, then use Terraform to apply a target-state definition that incorporates it. Both tools feed into the same CI/CD review gate before reaching production.

Refer to [Managing Production Environments](../agentic-cicd-production.html) for the broader pipeline pattern and how these tools fit together.

## Providers and resources

Ping Identity Terraform providers are available on the [Terraform Registry](https://registry.terraform.io/namespaces/pingidentity).

Provider documentation covers available resources, data sources, authentication configuration, and example usage for each Ping Identity platform.

## Full documentation

Best practices, provider references, examples, and FAQ are in the Terraform docs for Ping Identity.

[icon: book, set=fas, size=3x]

#### [Terraform for Ping Identity documentation](https://developer.pingidentity.com/terraform)

Provider references, resource examples, authentication configuration, best practices, and FAQ.
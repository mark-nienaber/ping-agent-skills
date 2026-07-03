---
title: Licensing basics
description: Overview of Ping Identity licensing concepts, including subscription terms and environment types for production and non-production deployments.
component: licensing-guide
page_id: licensing-guide::licensing-basics
canonical_url: https://docs.pingidentity.com/licensing-guide/licensing-basics.html
llms_txt: https://docs.pingidentity.com/licensing-guide/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  overview: Overview
  environment-types: Environment types
  production: Production
  non-production-environments: Non-production environments
---

# Licensing basics

## Overview

A license is your contract-backed right to use specific Ping Identity products and features, in specific environments, up to an agreed amount of usage for a set period of time.

Licenses are typically sold as **subscriptions**. During the term, you are entitled to use the licensed products up to the contracted limits and receive the associated support and maintenance.

## Environment types

Licensing behaves differently across **production** and **non-production** environments. This section defines the common environment types and how they relate to usage.

### Production

* A **live** environment that serves real end users and real traffic.

* Production environments are where service level agreements (SLAs) and uptime commitments apply.

### Non-production environments

Non-production environments are used for **development, testing, and experimentation**. They are not intended for sustained production traffic and typically operate at **lower scale**.

* **Development**: An environment used by developers and quality assurance (QA) to experiment and prototype, build and test configurations and integrations, and run automated and integration tests.

* **Sandbox**: A more stable, long-lived non-production environment used to try out new features, validate configuration changes, test integrations before moving to user acceptance testing (UAT) or production, and provide a safe playground for admins.

* **Staging or UAT**: A testing environment intended to mirror production as closely as practical for UAT, performance testing within agreed limits, and cut-over rehearsals.

Your contract and Product Terms specify **how many non-production environments** are included and any **usage expectations**, such as fair-use guidelines for test traffic.

---
title: Add-on capabilities
description: Optional add-on capabilities for Advanced Identity Cloud, including access management, governance, reporting, and network security features
component: pingoneaic
page_id: pingoneaic:product-information:add-on-capabilities
canonical_url: https://docs.pingidentity.com/pingoneaic/product-information/add-on-capabilities.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Deployment", "Planning", "Governance", "Autonomous Access", "Tenants"]
section_ids:
  access-management-add-ons: Access management
  environment-management-add-ons: Environment management
  governance-and-reporting-add-ons: Governance and reporting
  network-security-add-ons: Network security
---

# Add-on capabilities

Add-on capabilities are features or integrated products that enhance PingOne Advanced Identity Cloud, but are not part of the standard offering. They can each be added to your tenant environments for an additional subscription; contact your Ping Identity representative to arrange this.

The following wording identifies add-on capabilities in the Advanced Identity Cloud documentation:

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add this feature to your Advanced Identity Cloud subscription. |

## Access management

| Capability             | Summary                                                                                                                                                                                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| WS-Federation/WS-Trust | Lets you integrate Advanced Identity Cloud with Microsoft 365 and other service providers (SPs) to provide SSO using the WS-Federation identity protocol. Microsoft 365 also supports using the WS-Trust protocol.Learn more in [Register an SSO application](../app-management/register-a-custom-application.html#register-SSO-application). |

## Environment management

| Capability                     | Summary                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multi-region high availability | Lets you deploy your Advanced Identity Cloud tenant environments across multiple geographic regions to enhance availability and disaster recovery capabilities.Learn more in [Architecture, availability, and disaster recovery](../tenants/environments-architecture-availability-disaster-recovery.html).	This capability is dependent on Outbound static IP addresses.                                               |
| Sandbox tenant environment     | Standalone environment that lets you experiment with new configuration or test new use cases without affecting other environments.Learn more in [Sandbox tenant environment](../tenants/environments-sandbox.html).                                                                                                                                                                                                     |
| UAT tenant environment         | Additional environment that you can add to your standard promotion group of [development, staging, and production tenant environments](../tenants/environments-development-staging-production.html). It has the same capabilities as your staging environment, allowing you to test your development changes in a production-like environment.Learn more in [UAT tenant environment](../tenants/environments-uat.html). |

## Governance and reporting

| Capability                  | Summary                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Advanced Reporting          | Lets you create custom reports on activity in your Advanced Identity Cloud tenant environment. You can query a number of metrics to create useful reports for your company.Learn more in [Advanced Reporting](../reports/administration/advanced-reports.html).                                                                                         |
| Agent Governance            | Lets you discover, onboard, and govern agents you've created in external AI agent platforms, such as AWS Bedrock and Azure AI Foundry. You can view and manage agent profiles, certify entitlements, and request access to tools on behalf of agents.Learn more in [Agent Governance](../identity-governance/administration/iga-agent-governance.html). |
| PingOne Identity Governance | Lets you centrally administer and manage user access to applications and data across your organization to support regulatory compliance.Learn more in [What is PingOne Identity Governance?](../identity-governance/administration/getting-started-what-is-iga.html).                                                                                   |

## Network security

| Capability     | Summary                                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Secure Connect | Lets you connect to Advanced Identity Cloud directly from your private network without using the public internet.Learn more in [Create private network connections with Secure Connect](../tenants/secure-connect.html). |

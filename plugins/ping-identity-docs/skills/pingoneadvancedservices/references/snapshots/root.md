---
title: How PingOne Advanced Services works
description: A high-level description and diagram that explains how PingOne Advanced Services works.
component: pingoneadvancedservices
version: 2.2
page_id: pingoneadvancedservices::p1as_how_works
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/2.2/p1as_how_works.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
---

# How PingOne Advanced Services works

PingOne Advanced Services is a hosted service on Amazon Web Services (AWS) that makes it possible for you to manage your service yourself without having to also manage cloud resources, containers, networking, scaling, healing, and backup and restoration.

The following diagram shows how PingOne Advanced Services works. The Ping Identity Professional Services team works with you to set up the platform, and when it's available, you can perform tasks yourself through the platform or submit support tickets for tasks you can't complete yourself.

![The following diagram illustrates how users and administrators use PingOne Advanced Services.](_images/ric1626213352047.png)

1. The Professional Services team works with you to initially set up PingOne Advanced Services.

   The team connects to your on-premise infrastructure and configures your data sources, environments, authentication and password policies, and ensures the platform is working correctly. Ping Identity follows industry best practices and deploys its products using Kubernetes and Docker.

2. The Support team and the site reliability engineers proactively monitor your infrastructure and deployments and attempt to address issues before they become problems. They don't monitor your product configurations. Learn more in the [Monitoring and logging](monitoring_and_logging/p1as_monitoring_logging.html) section of this guide.

3. When the IAM service is available:

   * You can perform a variety of tasks on a self-service basis in the platform, or in PingFederate or PingDirectory, which you can access from the platform. Learn more about the tasks you can perform yourself in the **[Self-service tasks](task_summary_table/p1as_platform_selfservice.html)** section of this guide.

   * There are also a variety of different tasks you cannot complete yourself, so we ask that you submit a service request. These requests are sent to our Support and Professional Services teams, who continually monitor the request queues and will work closely with you to complete the request. Learn more about submitting service requests in the **[Service requests](task_summary_table/p1as_service_requests.html)** section of this guide.

   All self-service tasks and service requests are also listed and grouped by product in the [Task summary table](task_summary_table/p1as_task_summary_table.html). The table contains links to instructions for completing each task.

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Remember that a service request is just a way to initiate a conversation about your needs. The more detail you provide in the request, the better equipped we'll be to help you and appropriately respond. |

---

---
title: Penetration and load testing
description: Information about our penetration and load-testing policies.
component: pingoneadvancedservices
version: 2.2
page_id: pingoneadvancedservices::p1as_load_testing
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/2.2/p1as_load_testing.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 15, 2025
section_ids:
  _penetration_load_testing: Penetration and load-testing policy
  _load_testing_requests: Load-testing requests
---

# Penetration and load testing

Penetration testing is a simulated attack designed to find and exploit vulnerabilities in a system's defenses that attackers could take advantage of, while load testing determines if the system will perform as intended under normal conditions.

Our policies regarding these tests were created to:

* **Preserve platform stability**: Unplanned testing can interfere with our ability to effectively support all of our customers. Since some tests are initially indistinguishable from denial-of-service (DoS) attacks or other serious issues, they can:

  * Set off alarms

  * Cause service shutdowns

  * Add services and IPs to deny lists

  * Prevent our Support teams from taking the appropriate remedial actions.

    This type of disruption can also disproportionately occupy our Support teams, which will delay our response to other customers.

* **Regulate testing**: When you request a load test, we ask that you provide us with your load testing plan, origin of testing information, and the name and contact information for members of your testing team. That way, we can schedule the tests and help ensure that your testing approach is realistic, manageable, and provides meaningful results.

* **Avoid unnecessary testing**: At Ping Identity, we test all of our infrastructure and applications for you using code scans and automated load tests, which ensures that testing methods are consistent and can be compared over time. A third party performs penetration testing.

## Penetration and load-testing policy

With PingOne Advanced Services, penetration testing is performed by a third party, which is an industry best practice. We can share the results of these tests with you at any time. Our engineers review the test results, eliminate false positives, and perform in-depth analysis regarding the security of your infrastructure and applications.

Regarding load testing, you can:

* Indirectly test Ping Identity infrastructure and applications, as part of a wider test of your own infrastructure and applications, in your staging environment. Load testing is not permitted in your development, test, and production environments.

* Specify the number of identities you intend to create and the throughput levels you intend to simulate, which should not exceed the number of licenses you have.

You cannot:

* Directly test Ping Identity-hosted infrastructure and applications. This specifically applies to DoS or DDoS attacks. Ping Identity already does this testing on your behalf.

* Authorize a third party to perform load testing without Ping Identity's prior written consent. To perform load testing, we must receive your request in writing at least 2 weeks prior to the proposed test date.

## Load-testing requests

When requesting a load test, we ask that you provide us with your:

* **Load-testing plan**: Describe the strategy you intend to follow when testing your own infrastructure and applications.

  Indicate the number of identities you intend to create, and the throughput levels you intend to simulate. This number should align with the number of identities and throughput level you agreed upon with Ping Identity when you purchased the service, and should not exceed the following thresholds:

  * Agreed number of identities +25%

  * Agreed throughput +50%

    This plan should also avoid unrealistic patterns, such as the setup and tear down of many identities for each load test, and instantaneous user actions, such as changing the password and simultaneously attempting to use the new password.

* **Origin of testing documentation**: Specify whether the testing will originate from an external source over the internet or from an internal source within your organization. If it's originating from an external source, you must also supply IP addresses.

* **Contact name**: Provide the name of a member of your testing team and their contact information in case we have questions or need to stop the testing for any reason.

In the unlikely event that a vulnerability is discovered in the Ping infrastructure or applications, we also need you to attest, in writing, that you will not test the vulnerability further than the point of discovery, and that you will immediately report the issue to us.

---

---
title: PingOne Advanced Services
description: The home page for the PingOne Advanced Services guide.
component: pingoneadvancedservices
version: 2.2
page_id: pingoneadvancedservices::index
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/2.2/index.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 1, 2024
page_aliases: ["p1as_home", "_@pingoneadvancedservices::index.adoc"]
section_ids:
  release-notes: Release Notes
  get-started-with-pingone-advanced-services: Get Started with PingOne Advanced Services
  use-pingone-advanced-services: Use PingOne Advanced Services
  learn-more: Learn More
---

# PingOne Advanced Services

PingOne Advanced Services is a powerful solution that simplifies identity management for enterprise organizations by providing them with full cloud services, without compromising security or system performance.

## Release Notes

* [Release Notes](release_notes/p1as_rel_notes.html)

## Get Started with PingOne Advanced Services

* [Introduction to PingOne Advanced Services](introduction_to_pingone_advanced_services/p1_p1advancedservices_start.html)

* [How PingOne Advanced Services works](p1as_how_works.html)

* [Comparison: PingOne Advanced Services and PingOne](comparison_pingone_advanced_services_and_pingone_cloud_platform/p1as_cloud_comparison.html)

* [Platform and product upgrades](p1as_platform_product_upgrades.html)

* [Support policy](p1as_support_policy.html)

* [Environments](environments/p1as_environments.html)

* [Network guide](network_guide/p1as_network_guide.html)

* [Limitations guide](limitations_guide/p1as_limitations.html)

* [Monitoring and logging](monitoring_and_logging/p1as_monitoring_logging.html)

* [Penetration and load testing](p1as_load_testing.html)

## Use PingOne Advanced Services

* [How PingOne Advanced Services works](p1as_how_works.html)

* [Renewing Let's Encrypt certificates](renew_certs/p1as_renew_cert.html)

* [Task summary table](task_summary_table/p1as_task_summary_table.html)

* [Platform self-service](task_summary_table/p1as_platform_selfservice.html)

* [Service requests](task_summary_table/p1as_service_requests.html)

## Learn More

* [PingOne Platform](https://docs.pingidentity.com/pingone/latest/p1_cloud__platform_main_landing_page.html)

* [PingOne Advanced Services Community](https://support.pingidentity.com/s/topic/0TO1W000000IEPIWA4/pingone-advanced-services)

---

---
title: Platform and product upgrades
description: Information about the PingOne Advanced Services platform and product upgrades.
component: pingoneadvancedservices
version: 2.2
page_id: pingoneadvancedservices::p1as_platform_product_upgrades
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/2.2/p1as_platform_product_upgrades.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why-upgrade: Why upgrade
  _if_you_dont: What happens if you don't upgrade
  _release_notes: Release notes
  _whats_included: What's included in an upgrade
  _how_scheduled: How upgrades are scheduled
  _downtime: Expected downtime
  _duration: Upgrade duration and planning
  _before_during_after: Before, during, and after an upgrade
  before-an-upgrade: Before an upgrade
  during-an-upgrade: During an upgrade
  after-an-upgrade: After an upgrade
  _emergency: Out-of-cycle or emergency upgrades
  _rollback: Rollback policy and criteria
---

# Platform and product upgrades

## Why upgrade

PingOne Advanced Services platform and product upgrades are required on a regular basis to ensure that the platform is secure, resilient, and remains reliable. These upgrades often include security fixes, updated TLS and cipher configurations, and dependency updates that help you meet internal and regulatory requirements. They also contain new features, bug fixes, and disaster recovery, observability, and operational tooling improvements.

## What happens if you don't upgrade

We prefer that you take the time to perform small, low-risk upgrades on a regular basis, rather than doing large, high-risk upgrades that could be more disruptive.

If you defer upgrades for an extended period of time:

* Older platform and product versions eventually fall outside our standard support posture and receive fewer fixes and performance improvements. Learn more about how platform and product versions are deprecated in our [Support policy](p1as_support_policy.html) and the [Ping Identity End-of-Life (EOL) Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker).

* You might miss out on resilience, disaster recovery, and observability improvements. Issues we fix in newer versions will continue to affect you.

* Your environments might be running on unsupported infrastructure, such as older Amazon Elastic Kubernetes Service (EKS) versions, which increases your operational and security risk.

  |   |                                                                                                                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | AWS manages Amazon EKS support timelines independently of Ping Identity. AWS might force those running Amazon EKS versions beyond their supported window to upgrade. When this happens, the upgrade does not follow our controlled rolling process, and your environments could experience significant unplanned downtime. |

In cases where a critical security vulnerability is identified, we might need to schedule an out-of-cycle security upgrade outside the normal cadence. In those situations, scheduling flexibility can be limited by urgency. Learn more in [Out-of-cycle or emergency upgrades](#_emergency).

## Release notes

The [PingOne Advanced Services release notes](release_notes/p1as_rel_notes.html) use Semantic Versioning (SemVer), in which version numbers are structured as Major.Minor.Patch to communicate the scope of changes:

* The Major.Minor format identifies the platform version, a tested bundle of the PingOne Advanced Services infrastructure, EKS, cluster tooling, and minimum required product versions, such as PingFederate, PingAccess, and PingDirectory.

* The patch identifies add-on or targeted updates built on top of a specific Major.Minor platform, such as a PingFederate security patch applied to 2.1 customers, or a targeted fix that does not require a full platform release.

Items to keep in mind include:

* Patch releases aren't always sequential across all products. A PingDirectory patch does not automatically mean PingFederate is also updated to the same patch number.

* Upgrading to a specific platform version could require catch-up product upgrades. If your current product versions are below the minimums required for the target platform, those catch-up upgrades will be included in the same campaign.

* If upgrades introduce changes that are not backward compatible with existing integrations, operational patterns, or with an underlying Ping Identity product, such as PingFederate or PingDirectory, we'll explain the change in the release notes and in your upgrade communications and provide recommended mitigation or validation steps.

* As we complete the migration to microservices, we plan to release frequent product-level updates, such as a new PingFederate version, without requiring a new platform campaign for every change.

Learn more about our version support policies and deprecation timelines in the PingOne Advanced Services [Support policy](p1as_support_policy.html).

## What's included in an upgrade

You'll be informed of which environments, versions, and components are in scope for a given upgrade. Upgrades can include:

* **Platform and orchestration layer updates**, which can include updates to Kubernetes, Amazon EKS, cluster tools, such as Argo CD and monitoring agents, or the orchestration logic that manages your environments.

* **Ping Identity product updates**, such as PingFederate, PingAccess, PingDirectory, PingDataSync, PingCentral, Delegated Admin, and components related to current, supported versions.

  |   |                                                                                                                                                                                                                                                                                 |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | PingDirectory is deployed in all PingOne Advanced Services environments, even if it is not a visible part of your identity solution design. PingDirectory serves as the datastore for PingFederate and other platform components, so it must be included in your upgrade plans. |

* **Security and compliance updates**, which can include security patches at the product, platform, and infrastructure layers, including updates driven by AWS, Kubernetes, and Ping Identity security bulletins.

Some upgrades also change security controls, such as TLS versions, cipher configurations, certificate handling, or logging hardening, to keep you aligned with current security standards. When that happens, it will be described in the PingOne Advanced Services release notes and in your upgrade communications so that you can determine whether changes to your configurations are needed.

The items included in a release, and the timing of the release, depend on the severity of the issues the release addresses, and the number of customers affected.

* **Patch or targeted releases**: Include fixes as a patch on top of the current platform version. This approach is typically used to address security issues or high-impact defects.

* **Next platform release**: Includes enhancements and improvements, and addresses lower-severity issues.

Issues and defects are initially identified by:

* Our support and engineering teams, who discover the issues when monitoring platforms, performing routine platform maintenance, or upgrading clients to new versions.

* Our professional services teams when working on partner implementations.

* Users like you. If you discover an issue, open a service request through the Support Portal.

After an issue is confirmed as a platform or product defect, our engineering team creates an internal tracking ticket (a TRIAGE ticket) to investigate the root cause of the issue, determine how we will fix it, and establish its priority.

From there, the engineering teams determine which updates, fixes, and enhancements will be included in each release and when the release will be available.

## How upgrades are scheduled

To continually improve the platform and keep it secure, we work to release new versions every quarter. However, your upgrades are scheduled around your availability, and the upgrade campaign sequence.

Upgrades are coordinated between you, your account team, and the PingOne Advanced Services support and operations teams. Your account team might consist of a support account manager or a technical support manager who will serve as the coordinator between you and the support and operations teams. They will help you establish dates and times for the upgrade and communicate with you throughout the process.

To initiate an upgrade:

* You can contact your account team or open a service request through the Support Portal requesting the upgrade.

* Your account team can initiate the upgrade and reach out to you to begin planning.

* The operations team can also initiate the upgrade and ask your account team to reach out to you to begin planning.

  |   |                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If we attempt to contact you regarding your upgrade, and you do not respond, we will proceed on our proposed dates. Ping Identity has a responsibility to maintain the security and integrity of the platform, and indefinite deferral carries real risk. We will always make at least three contact attempts and communicate with you before proceeding without a response. |

When you begin working with the account team, it's helpful to provide them with the following:

* Your preferred timeframe and any freeze periods or blackout dates.

* Your time zone and preferred maintenance windows.

* Any key business events to plan around, such as significant load events, large migrations, seasonal peaks, and regulatory reporting windows.

It's also helpful if you ensure that internal approvals and CAB processes are satisfied before scheduled upgrade windows.

All of this information and all upgrade-related communication will be tracked in the service request that you or your account team will open. It will include date confirmations, schedule changes, post-upgrade validation status, and provide an audit trail for internal and external reviews.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You cannot reschedule upgrades for your development and testing environments once the dates and times are established. These environments are used to validate the upgrade campaign and must be upgraded and stable before we can upgrade your staging and production environments. Staging and production environments can be rescheduled with at least 48 hours' notice. Changing the upgrade dates and times with less than 48 hours' notice is often not possible due to staffing and scheduling constraints. |

As we complete the transition to a microservice architecture, the upgrade cadence will change. Product-level upgrades, for example, a new PingFederate version, will be available independently of the broader platform, which means upgrades will become smaller, more targeted, and more frequent, with less scheduling overhead and disruption required for each one.

In the meantime, the best way to avoid a large catch-up campaign is to stay engaged with your account team and schedule upgrades when recommended.

## Expected downtime

PingOne Advanced Services environment configurations and customizations are preserved across upgrades, and most users should not notice the upgrade.

Specifically, the following will not be affected:

* PingFederate service provider (SP) connections

* Authentication flows and policies

  PingOne Advanced Services performs rolling upgrades of the application engines (PingFederate, PingAccess, PingDirectory), so at no point should the platform be unable to process authentication requests as a direct result of the upgrade.

  However, with some major version updates, PingFederate might not recognize tokens issued by earlier versions. As traffic moves from old to new instances, some users might need to reauthenticate.

* PingDirectory schemas

* PingAccess application rules and similar settings

If exceptions apply, you will be informed of them before the upgrade, and they will be documented in your upgrade runbook.

Downtime is expected, however, to occur with:

* Admin consoles and single-node resources

  Resources with a single node, such as the PingFederate admin console, will not be available while they are being upgraded. During that window, you will not be able to make configuration changes through those admin UIs or certain administrative APIs. Authentication engines continue to serve traffic while admin consoles are offline.

* Observability and tools

  Logging and metrics might show short gaps or brief anomalies when components are restarted. We monitor the platform before, during, and after the upgrade to ensure it returns to normal.

* Multi-region deployments

  For multi-region deployments, each region has a defined upgrade sequence established in the runbook for your account. In most cases, at least one region continues serving traffic while the other is being upgraded, but the specifics depend on your DNS and load-balancing configuration. We'll temporarily stop sending users to your primary region and send them to the secondary regions during the upgrade.

* Full rollback scenarios

  In the rare case of a full rollback, PingOne Advanced Services might need to reinitialize from backup in the affected environment. During the reinitialization and restoration process, the environment will be unavailable until fully restored and validated.

  Rollbacks are treated as incidents, and you will receive appropriate incident communication and updates throughout the process. If a full outage is expected for any reason during an upgrade, we will state that explicitly in your upgrade communication prior to the upgrade.

## Upgrade duration and planning

Upgrades are performed on each environment and the Customer Hub (CHUB), which is a shared infrastructure that underpins all of your PingOne Advanced Services environments, but it does not directly serve end-user authentication traffic. The CHUB hosts shared services all of your environments depend on, including networking, DNS, certificate management, and platform tooling, which is why the CHUB must be upgraded first in any platform upgrade campaign.

The following table provides information about each type of upgrade, the expected duration of the upgrade, and additional information regarding scheduling:

| Type of upgrade   | Duration                                               | Additional information                                                                                            |
| ----------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| CHUB              | A few hours, depending on the amount of data involved. | Must be explicitly scheduled and upgraded first. No impact to the customer experience.                            |
| DEV environment   | A few hours, depending on the size of the environment. | Upgraded to the target platform version and validated. Cannot be rescheduled once an upgrade date is set.         |
| TEST environment  | A few hours, depending on the size of the environment. | Upgraded, allowing broader integration and regression testing. Cannot be rescheduled once an upgrade date is set. |
| STAGE environment | Scheduled in 8 - 12 hour windows.                      | Upgraded after the DEV and TEST environment validation is complete.                                               |
| PROD environment  | Scheduled in 8 - 12 hour windows.                      | Upgraded after the STAGE environment validation is complete and internal change approvals are satisfied.          |

Multi-region environments take about 2 additional hours per region.

|   |                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't plan on completing an upgrade in less time than your account team plans for. We perform safe, rolling restarts and run health checks between each step to ensure mistakes aren't made. The time it takes to complete will also depend on blackout and freeze periods, internal approval processes, and any operational constraints. |

Also note that weekend upgrades are available as a paid add-on for PROD environments. If you have purchased this add-on, your account team can discuss how to schedule within that program. Targeted security patches do not qualify for the weekend upgrade slot.

## Before, during, and after an upgrade

There are a variety of tasks that must be completed before, during, and after an upgrade by you, your account team, and the support and operations teams. The support and operations teams, and your account team will create and maintain their own tickets to monitor and record progress throughout the upgrade.

### Before an upgrade

The support and operations teams will:

* Prepare for the upgrade and run the following standard backups:

  * PingFederate and PingAccess every hour.

  * PingDirectory every 6 hours, except if you have large PingDirectory upgrades that take longer than 6 hours to create backups. If you do not have large PingDirectory upgrades, backups are taken during the upgrade window after post-check testing is complete. These are the backups that the team will restore in the event of a rollback.

* Run an additional backup immediately before the upgrade. We note the date and time of this backup and will use it to compare the data and configurations after the upgrade is complete.

* Sign on to all products so that we can test the experiences and ensure they're working as expected after the upgrade.

Your account team will:

* Plan and schedule the upgrade, and ensure that you understand when upgrade windows will begin and end.

* Confirm the upgrade schedule with you through your upgrade service request, which will include the environments in scope, the target versions, and the planned start time for each environment. The service request will also contain links to the relevant release notes.

You should:

* Ensure internal approvals and CAB processes are satisfied before scheduled upgrade windows. Notify us in advance of any freeze periods or blackout windows.

* Let us know about significant load events, large migrations, or seasonal peaks so upgrades can be planned around them.

* Review the release notes before your upgrade window. Pay particular attention to any Java version updates or changes to security controls, as these are the areas most likely to require your attention.

* Ensure that you understand what time the upgrade is scheduled to start and end.

  Platform upgrades for STAGE and PROD environments are size-dependent and scheduled in 8 - 12 hour windows.

  * Single region: 8 hours

  * Double region: 10 hours

  * Triple region: 12 hours

    For example, if your upgrade is scheduled to start at 9:00 PM, plan for the window to run until approximately 7:00 AM. Ensure that your internal teams also understand when the upgrade windows begin and end.

  |   |                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Customers with large PingDirectory upgrades might be bumped to the next region size class due to the amount of time that PingDirectory requires to upgrade itself. |

### During an upgrade

The support and operations teams will:

* Complete a series of steps performed in most upgrades:

  1. Verify the current versions.

     Check to see which underlying product versions are currently being used.

  2. Divert traffic.

     For multi-region environments, we'll temporarily stop sending users to your primary region and send them to the secondary regions during the upgrade.

     |   |                                                                                               |
     | - | --------------------------------------------------------------------------------------------- |
     |   | Inform us if you don't want us to use a failover, or if you're not using our global endpoint. |

  3. Update the environment variables configuration in Git.

  4. Upgrade the PingFederate, PingAccess, and PingDirectory services.

     We'll use the upgrade utility to upgrade products to new versions and ensure that previous configurations are migrated to the new versions.

  5. Check on the status of the pods.

     We monitor the pods and only upgrade a few pods at a time using your pre-upgrade backup data and configuration information, so the environment comes back with the same settings and data it had before. Then, we verify that the correct product versions are being used and perform validation checks for the region.

  6. Return traffic.

     When we're done, we restore the primary region links within Global DNS reporting. These links enable traffic to be directed back to the upgraded primary region, diverting it from secondary regions, so that any remaining region upgrades can be performed.

  7. Inspect AWS monitors.

     We check and monitor the canary objects in AWS and ensure that they haven't had interruptions of service after the update was performed.

  8. Perform validation checks.

     We then complete post-upgrade validation checks, which include signing on to all products to validate rendering, and screen capture configuration review.

* Keep you and the account team informed of progress by updating the service request.

Your account team will:

* Serve as the central point of contact and keep you informed of progress by updating the ticket.

* Notify you when an environment upgrade is complete and ask you to ensure that your environment is functioning as it should before we start working on the next environment.

  Catching issues in the DEV and TEST environments is far less disruptive than discovering issues in your PROD environment.

* Answer any questions you have along the way.

You should:

* Stay up-to-date on upgrade communications and answer questions in the service request in a timely manner.

  If you have questions or observe unexpected behavior, immediately contact the support team in the service request. You should not need to communicate with an engineer directly.

* When notified, test your environments to ensure they are functioning as they should.

  You don't need to test every possible flow, but you should have a defined set of critical flows that you run after each upgrade as part of your business continuity practices. If you do not have this type of testing plan in place, we recommend developing one with your account team before the next upgrade campaign.

* Ensure that your integration kits and custom adapters work as expected.

  We verify that your integration kits initialize without errors after the upgrade and confirm that first-party integrations function with default endpoints. However, we cannot verify how an integration kit is operating on the external system, or whether a third-party application that relies on the kit continues to behave as expected after a product version change.

  You are responsible for validating end-to-end behavior through your critical flows in the STAGE environment. Pay particular attention when release notes call out Java version changes, which can affect your integration kits and custom adapter compatibility.

### After an upgrade

We test the platform and product stability throughout the upgrade process, but we cannot replicate all of your integrations and flows, which only you can test.

Specifically, we recommend that you test:

* **Primary authentication flows**: Verify that your main SSO flows, federation connections, and sign-on journeys work as expected for your administrators and end users.

* **SP connections and application integrations**: Confirm that applications that connect to PingFederate are authenticating successfully and receiving correct assertions or tokens.

* **Custom adapters and integration kits**: Verify that these initialize correctly and that the systems they integrate with are responding as expected. A kit loading without errors does not guarantee the downstream system is behaving correctly.

* **PingDirectory behavior**: If your use case relies on PingDirectory for identity data, password validation, or related functions, confirm that those flows are working.

* **Logging and observability**: Verify that your log streams are reaching your security information and event management (SIEM) or observability platform and that log formats match your parsing rules. If the release notes for your upgrade mention log format changes, be sure to test your log integrations.

* **Admin UI access**: Confirm that admin consoles are accessible and that your admin credentials work after the upgrade.

## Out-of-cycle or emergency upgrades

If a critical security vulnerability is identified that affects the platform or one of the underlying Ping Identity products, we might need to apply a security patch immediately, or outside the normal upgrade cadence, and without advance communication.

What to expect in most situations:

* We will reach out to you to explain the vulnerability and what the patch does to address it.

* We'll also explain the scope of the change, which environments will be patched, and in what order.

  The DEV and TEST environments will be patched first. Like other upgrades, once it's scheduled, it cannot be rescheduled. The STAGE and PROD environments also have the 48-hour rescheduling policy.

* Like other upgrades, you will be asked to validate your environments after each environment is patched before we proceed to the next.

Depending on the severity and exposure of the vulnerability, our scheduling flexibility might be limited. We will always communicate the urgency and the reason for it, and we will work with you to find a workable window while being transparent about the risk of delay.

Security patches are scheduled for weekdays and do not qualify for the weekend upgrade program.

If you are aware of upcoming blackout dates or constraints that could limit your ability to upgrade for a security patch on short notice, notify your account team.

## Rollback policy and criteria

If we detect an issue during or immediately after an upgrade, our operations team will pause or rollback changes in the affected environment or region, according to our runbooks. Our support team will open another ticket associated with your upgrade service request to communicate status, impact, next steps, and to coordinate the rollback, if necessary.

First, we will work to restore stability. Then, we'll analyze the root cause of the issues and work to address them.

Rollback decisions are made by our operations team and depend on whether specific conditions exist. If our operations team confirms that one or more of the following situations exist in your STAGE and PROD environments during the upgrade window, they might perform a rollback according to our runbooks.

* Authentication flows are failing, not just degraded, and cannot be stabilized within the upgrade window.

* A core service, (for example, PingFederate or PingDirectory) cannot reach a healthy running state.

* Pre-agreed health checks defined in the upgrade runbook cannot be satisfied.

A full rollback might require reinitializing the environment from backup, during which the environment will be unavailable until fully restored and validated.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We will not complete a rollback for your DEV and TEST environments unless our operations team deems it necessary. These environments exist to discover issues before they reach the STAGE and PROD environments. We resolve issues by creating a targeted fix, configuration correction, or component upgrade, during which the validation path remains intact. Rolling back a DEV or TEST environment would discard the information gained from the upgrade and delay the overall campaign. |

---

---
title: Support policy
description: Information about our support policy.
component: pingoneadvancedservices
version: 2.2
page_id: pingoneadvancedservices::p1as_support_policy
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/2.2/p1as_support_policy.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 3, 2026
section_ids:
  version-support: Version support
  example-n-2-version-support-timeline: "Example: N-2 version support timeline"
  deprecation-timeline: Deprecation timeline
  upgrade-management: Upgrade management
---

# Support policy

## Version support

PingOne Advanced Services uses Semantic Versioning (SemVer), in which version numbers are structured as Major.Minor.Patch to communicate the scope of changes.

\+ Starting with platform version 2.2, we will provide ongoing N-2 support for the two most recent major or minor versions of the platform available. N-2 support means that we provide active support, security updates, and fixes for the current version (N) and the two immediate previous versions (-2).

### Example: N-2 version support timeline

Beginning with platform version 2.2 (released March 2026), the N-2 support policy means that versions 2.2 (N), 2.1 (N-1), and 2.0 (N-2) are in Active Support. Versions 1.19 and earlier enter a six‑month Extended Support phase and will reach End of Life (EOL) six months after the end of the 2.2 release month, (for example, version 1.19 reaches EOL on September 30, 2026). When version 2.3 is released, version 2.0 will move into Extended Support and will reach EOL six months after the end of the 2.3 release month.

## Deprecation timeline

When a new platform version is released that places an older version outside the N-2 window, the older version enters a 6-month extended support phase.

When this 6-month window ends, the version reaches End of Life (EOL) status.

## Upgrade management

The PingOne Advanced Services operations team will coordinate mandatory upgrade windows for those approaching EOL. We encourage you to maintain N-1 status to ensure you have access to the latest security hardening and performance enhancements.
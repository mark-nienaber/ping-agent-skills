---
title: How PingOne Advanced Services works
description: A high-level description and diagram that explains how PingOne Advanced Services works.
component: pingoneadvancedservices
page_id: pingoneadvancedservices::p1as_how_works
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/p1as_how_works.html
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

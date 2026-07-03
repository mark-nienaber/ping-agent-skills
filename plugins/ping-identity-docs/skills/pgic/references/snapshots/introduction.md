---
title: Introduction to Ping Government Identity Cloud
description: Ping Government Identity Cloud is a managed, software as a service (SaaS) solution that resides in a scalable, secure, cloud environment. Its single-tenancy architecture provides you with your own dedicated, customizable environments where all of your resources are isolated and available only to you.
component: pgic
page_id: pgic:introduction:fedrampsolutions_intro
canonical_url: http://docs.pingidentity.com/pgic/introduction/fedrampsolutions_intro.html
revdate: November 1, 2023
section_ids:
  simplifying: Simplifying identity and access management
  how_works: How Ping Government Identity Cloud works
---

# Introduction to Ping Government Identity Cloud

Ping Government Identity Cloud is a managed, software as a service (SaaS) solution that resides in a scalable, secure, cloud environment. Its single-tenancy architecture provides you with your own dedicated, customizable environments where all of your resources are isolated and available only to you.

With Ping Government Identity Cloud, you have:

* Enhanced Security

  Single-tenant solutions are best for those of you who need to follow strict standards and regulations because you have your own isolated environments, which helps ensure that your data remains secure and unauthorized access risks are minimized.

* Ability to customize for compliance needs

  Single-tenant solutions are also highly customizable, which makes it possible for you to design the infrastructure to meet your unique compliance needs.

* Centralized management

  With Ping Government Identity Cloud, we handle the maintenance, updates, and support, which frees valuable time for your administrators and lets them focus on other business needs.

* Flexibility and scalability

  Ping Government Identity Cloud also provides the flexibility and scalability you need without affecting system performance or stability. And because your environments don't share API endpoints with others, rate limits, which are used to restrict the number of requests a client can make to an endpoint within a specified period of time, aren't needed.

* Expert support

  Our Professional Services and Support teams have extensive experience working with government organizations, and understand regulations and compliance requirements that you need to adhere to.

This solution has received:

* A FedRAMP (Federal Risk and Authorization Management Program) High authorization to operate (ATO), which signifies that this Cloud Service Offering (CSO) meets stringent security controls and is suitable to handle sensitive data.

* The Department of Defense (DoD) Provisional Authorization (PA), which is issued by the DISA Authorizing Official (AO) for a CSO based on FedRAMP and additional DoD security requirements Impact Level 5 (IL5).

## Simplifying identity and access management

Ping Government Identity Cloud is built on secure containers, which provide the tools to build, deploy, and securely run the containerized applications shown here. Deployment flexibility is also indicated in this diagram.

![Solutions](_images/Solutions.jpg)

## How Ping Government Identity Cloud works

This network is hosted by AWS GovCloud, which makes it possible for you to manage your service yourself without having to also manage cloud resources, containers, networking, scaling, healing, and backup and restoration.

1. Our Professional Services team works with you to set up Ping Government Identity Cloud.

   The team connects to your on-premise infrastructure and configures your data sources, environments, authentication, and password policies, and ensures the platform is working correctly. We follow industry best practices and deploy our products using Kubernetes and Docker.

2. Our Support team and the Site Reliability Engineers proactively monitor your infrastructure and deployments and attempt to address issues before they become problems. Note that they don't monitor your product configurations as that's your responsibility.

3. When the IAM service is available:

   * You can perform a variety of tasks on a self-service basis in the platform, or in a product, which you can access from the platform. Learn more about the tasks you can perform yourself in the [Self-service tasks](../products_and_self-service_tasks/p14g_products_selfservice.html) section of this guide.

   * There are also a variety of different tasks you cannot complete yourself, so we ask that you submit a service request. These requests are sent to our Support and Professional Services teams, who monitor the request queues and will work closely with you to complete the request. Learn more about submitting service requests in the [Service requests](../service_requests/p14g_service_requests.html) section of this guide.

Ping Government Identity Cloud is deployed in Kubernetes and application configurations are stored in GitLab, which makes it possible for us to redeploy your applications fully configured in case a failure or disaster occurred. In accordance with the FedRAMP initiative, any pieces that are deployed as a stateful set and backed with an Amazon Elastic Block Store (EBS) volume will have snapshots created daily. These daily snapshots are kept for 14 days, and weekly backups are kept for 6 weeks, but adjustments can be made, if necessary.

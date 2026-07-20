---
title: Data storage considerations
description: Data is measured in entries. An entry could be a user account, the grants associated with that user, or any data associated with that user. The total number of entries is also known as the total number of objects.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:environments:p1as_data_storage
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/environments/p1as_data_storage.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 23, 2024
---

# Data storage considerations

Data is measured in entries. An entry could be a user account, the grants associated with that user, or any data associated with that user. The total number of entries is also known as the total number of objects.

The amount of data that can be loaded to an environment depends on the size of each entry, the amount of memory required to store it, and the amount of storage available. As the schema for an entry is customized for each customer, there is no single calculation that can be made to determine how much memory and storage a customer will require.

In these examples, we illustrate how data storage is calculated using two different entry sizes.

* If the average size of each entry is 1 KB, and 1 GB can store 1 million KB:

  1 KB per entry \* 1 million entries = 1 GB of storage needed.

* If the average size of each entry is larger, the number of entries that can be stored in each GB will be smaller. For example, if the average size of each entry is 10 KB, you can only store about 100,000 entries:

  10 KB per entry \* 100,000 entries = 1 GB of storage needed.

![This image illustrates the storage capacity when the average size of each entry is 1 KB and when the average size of each entry is 10 KB.](_images/msk1678908440884.png)

Remember that Development and Testing environments are provisioned with 8 GB of RAM and 40 GB of disk space and are not intended for load testing. You can load a portion of your data into those environments to quality-check your applications and perform user acceptance testing, and then move all of your data to the Staging environment for performance and load testing.

---

---
title: Environments
description: Information about our production and non-production environments, and data storage considerations.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:environments:p1as_environments
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/environments/p1as_environments.html
llms_txt: https://docs.pingidentity.com/pingoneadvancedservices/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 24, 2024
section_ids:
  _production_environment: Production environment
  _non_production_environments: Non-production environments
  data-storage-considerations: Data storage considerations
---

# Environments

With PingOne Advanced Services, you have one production environment and a variety of non-production environments that you can use to develop and test your code and configurations.

Items of note include:

* Automation is used to build and deploy PingOne Advanced Services into AWS so that all environments follow the same generic footprint.

* Each environment has data storage limits, which are important to consider when configuring your platform. See [Data storage considerations](p1as_data_storage.html) for details.

* PingOne Advanced Services comes with a number of URLs to access different services, such as PingFederate and PingAccess runtime endpoints. Do not use these URLs for users accessing your production environment. Instead, provide a TLS certificate and key so that it can be branded to your domain.

## Production environment

The production environment (Prod) is where the latest versions of software, products, or updates are pushed live to their intended users.

With PingOne Advanced Services, the production environment is:

* Built to support the predicted load for each customer, based on their licensed identity count.

* The only environments that are subject to Ping Identity's uptime and Severity 1 and 2 service level agreements.

With multi-region deployments, production environments use active-active clustering configurations to achieve load balancing.

## Non-production environments

Non-production environments provide you with a way to develop and test your code and configurations using smaller sets of representative data, and then perform final testing and load testing in accordance with Ping Identity's load testing policies. Development and testing environments cannot be revised once they are created and remain static throughout their existence.

* **Development environments (Dev)**

  Each PingOne Advanced Services deployment includes one development environment by default. Development environments are used to create and test code without interfering with the content on live sites.

  Keep the following in mind:

  * These environments should not be used for performance or load testing.

  * They do not scale and are always deployed in a single-region model.

  * With multi-region deployments, development environments only exist in the primary region.

  * The Dev environment is provisioned with 8GB of RAM and 40 GB of disk space.

  * These environments are not subject to Ping Identity's uptime and Severity 1 and 2 service level agreements.

* **Testing (Test)**

  Testing environments are replicas of the Dev environments and are optional add-ons with PingOne Advanced Services. Testing environments are used to quality-check applications and perform user acceptance testing.

  Keep the following in mind:

  * These environments should not be used for performance or load testing.

  * With multi-region deployments, testing environments only exist in the primary region.

  * The Test environment is provisioned with 8GB of RAM and 40 GB of disk space.

  * These environments are not subject to Ping Identity's uptime and Severity 1 and 2 service level agreements.

* **Staging (Stage)**

  Staging environments are replicas of the production environment and are optional add-ons with PingOne Advanced Services. They can be used for performance and load testing, and for final testing before changes are released to the live site.

  Keep the following in mind:

  * With multi-region deployments, the staging environment clustering configuration matches the production environment configuration.

  * The Staging environment is provisioned with the same RAM and disk space as your production environment.

  * These environments are not subject to Ping Identity's uptime and Severity 1 and 2 service level agreements.

    |   |                                                                                                                                                                                                                                   |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | A staging environment is required for multi-region clustered deployments, even if one is not purchased. The environment will be present, but turned off, so be sure to account for the /22 RFC1918 IP space required to house it. |

* **Customer hub**: This environment is deployed in every region that your solution is deployed in, and serves as a central data store for cluster configuration code and product integration kits. PingCentral also runs here, which allows you to delegate common application configuration and deployment tasks to application owners. See [Introduction to PingCentral](https://docs.pingidentity.com/pingcentral/latest/pingcentral_for_iam_administrators/pingcentral_intro/pingcentral_intro.html) for details.

## Data storage considerations

Data is measured in entries. An entry could be a user account, the grants associated with that user, or any data associated with that user. The total number of entries is also known as the total number of objects.

The amount of data that can be loaded to an environment depends on the size of each entry, the amount of memory required to store it, and the amount of storage available. As the schema for an entry is customized for each customer, there is no single calculation that can be made to determine how much memory and storage a customer will require.

In these examples, we illustrate how data storage is calculated using two different entry sizes.

* If the average size of each entry is 1 KB, and 1 GB can store 1 million KB:

  1 KB per entry \* 1 million entries = 1 GB of storage needed.

* If the average size of each entry is larger, the number of entries that can be stored in each GB will be smaller. For example, if the average size of each entry is 10 KB, you can only store about 100,000 entries:

  10 KB per entry \* 100,000 entries = 1 GB of storage needed.

![This image illustrates the storage capacity when the average size of each entry is 1 KB and when the average size of each entry is 10 KB.](_images/msk1678908440884.png)

Remember that Development and Testing environments are provisioned with 8 GB of RAM and 40 GB of disk space and are not intended for load testing. You can load a portion of your data into those environments to quality-check your applications and perform user acceptance testing, and then move all of your data to the Staging environment for performance and load testing.
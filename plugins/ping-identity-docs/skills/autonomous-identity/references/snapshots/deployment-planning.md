---
title: Architecture in brief
description: "Ping Autonomous Identity has a powerful and flexible architecture that lets you deploy Ping Autonomous Identity in any number of ways: single-node or multi-node configurations across on-prem, cloud, hybrid, or multi-cloud environments. The Ping Autonomous Identity architecture has a simple three-layer conceptual model as follows:"
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:deployment-planning:chap-architecture-in-brief
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/chap-architecture-in-brief.html
---

# Architecture in brief

Ping Autonomous Identity has a powerful and flexible architecture that lets you deploy Ping Autonomous Identity in any number of ways: single-node or multi-node configurations across on-prem, cloud, hybrid, or multi-cloud environments. The Ping Autonomous Identity architecture has a simple three-layer conceptual model as follows:

* **Application Layer**. Ping Autonomous Identity implements a flexible Docker Swarm microservices architecture, where multiple applications run together in containers. The microservices component provides flexible configuration and end-user interaction to the deployment. The microservices components are the following:

  * **Ping Autonomous Identity UI**. Ping Autonomous Identity supports a dynamic UI that displays the entitlements, confidence scores, and recommendations.

  * **Ping Autonomous Identity API**. Ping Autonomous Identity provides an API that can access endpoints using REST. This allows easy scripting and programming for your system.

  * **Backend Repository**. The backend repository stores Ping Autonomous Identity user information.

  * **Nginx**. Nginx is a popular HTTP server and reverse proxy for routing HTTPS traffic.

  * **Apache Livy**. Ping Autonomous Identity supports Apache Livy to provide a RESTful interface to Apache Spark.

  * **Java API Service**. Ping Autonomous Identity supports a private Java API Service (JAS) for a RESTful interface to the Cassandra or MongoDB database.

* **Data Layer**. Ping Autonomous Identity supports Apache Cassandra NoSQL and MongoDB databases to serve predictions, confidence scores, and prediction data to the end user. Apache Cassandra is a distributed and linearly scalable database with no single point of failure. MongoDB is a schema-free, distributed database that uses JSON-like documents as data objects. Java API Service (JAS) provides a RESTful interface to the databases.

  Ping Autonomous Identity also implements Opensearch and Opensearch Dashboards to improve search performance for its entitlement data. Opensearch supports scalable writes and reads. Opensearch Dashboards provides a useful visualization tool for your Opensearch backend.

* **Analytics and Administration Layer**. Ping Autonomous Identity uses a multi-source Apache Spark analytics engine to generate the predictions and confidence scores. Apache Spark is a distributed, cluster-computing framework for AI machine learning for large datasets. Ping Autonomous Identity runs the analytics jobs directly from the Spark main over Apache Livy REST interface.

  ![Ping Autonomous Identity architecture](_images/autoid-architecture-conceptual.png)Figure 1. A Simple Conceptual Image of the Ping Autonomous Identity Architecture

---

---
title: Deployment checklist
description: Use the following checklist to ensure key considerations are covered for your 2022.11.12 deployment:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:deployment-planning:chap-checklist
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/chap-checklist.html
---

# Deployment checklist

Use the following checklist to ensure key considerations are covered for your 2022.11.12 deployment:

**Deployment Checklist**

|                     |                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Check               | Requirement                          | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Access              |                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \[ ]                | Remote Access                        | The Ping Autonomous Identity Team is a global team. To support the needs of client teams, remote access to all servers is required for deployment and support of product.                                                                                                                                                                                                                                                                                                                                                            |
| \[ ]                | Service Account                      | The service account must have the ability to run passwordless sudo commands. The deployer will not without this ability.                                                                                                                                                                                                                                                                                                                                                                                                             |
| \[ ]                | File Transfer Process                | The Ping Autonomous Identity Team require access to a file transfer process, which lets specified packages be transferred from the vendor to the client infrastructure.                                                                                                                                                                                                                                                                                                                                                              |
| Service Account     |                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \[ ]                | Service Account Group                | The service account group must be the same as the service account name. For example, if the service account name is `srv-autoid`, that user must be in the group `srv-autoid`.                                                                                                                                                                                                                                                                                                                                                       |
| \[ ]                | Ping Autonomous Identity Team Access | Ping Autonomous Identity team members must be able to switch to this user after logging in to the servers.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \[ ]                | SSH Ability                          | The service account must be able to passwordless SSH between all Ping Autonomous Identity servers; preferred method is RSA SSH key authentication.                                                                                                                                                                                                                                                                                                                                                                                   |
| \[ ]                | Default Shell                        | The default shell of the service account must be Bash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \[ ]                | Directory Ownership                  | Ownership of the following directories must be given to the Service Account.- /data or applicable name of the shared mount (Docker and Spark servers)

- /opt/autoid (all servers)

- /tmp (R, W, E required + NOEXEC flag must not be present)                                                                                                                                                                                                                                                                                      |
| \[ ]                | Docker Commands                      | The service account must have permissions to run Docker commands. Note that Docker should NOT need to be installed as a prerequisite; this will be installed by deployment team.                                                                                                                                                                                                                                                                                                                                                     |
| Networking/Internet |                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \[ ]                | Access to the Internet               | If available, the front-end servers downloads the required Docker images from the official Ping Autonomous Identity image repository.                                                                                                                                                                                                                                                                                                                                                                                                |
| \[ ]                | SSL Certificates                     | If SSL is being implemented, SSL certificates are required for the UI, Cassandra or MongoDB nodes, and Spark nodes. These certificates can be generated using one of the following four options:- Self-signed certificates for all 3 components

- Valid certificate for the UI and self-signed certificates for Cassandra, MongoDB, and Spark nodes (self-signed certs only used in server-server traffic)

- Valid and separate certificates for the UI, Cassandra, MongoDB, and Spark

- \*.domainname.com certificate (wildcard) |
| \[ ]                | Ports Open (Internal)                | All internal ports specified in the Networking section of the Environment Specifications need to be opened for the specified servers.                                                                                                                                                                                                                                                                                                                                                                                                |
| \[ ]                | Ports Open (external browser)        | The following ports must be accessible from a web browser within the client network:- 443 (Front-end)For a list of Ping Autonomous Identity ports, refer to [Autonomous Identity Ports](../release-notes/chap-before-you-install.html#sec-ports).                                                                                                                                                                                                                                                                                    |
| Required Packages   |                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \[ ]                | Dependencies                         | The following packages must be installed on specified servers as prerequisites:- Analytics Servers:

  * OpenJDK version "11.0.16"

  * Python 3.10.9 with symlinks to Python 3 (sudo ln -s /usr/bin/python3.10 /usr/bin/python3)                                                                                                                                                                                                                                                                                                    |
| Other               |                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \[ ]                | Infrastructure Support POC           | A point-of-contact (POC) with sufficient access to the infrastructure is required. The POC can support in case of infrastructure blockers arise (e.g., proxy, account access, or port issues).                                                                                                                                                                                                                                                                                                                                       |
| \[ ]                | SELinux                              | SELinux must be disabled on the Docker boxes. The package "container-selinux" must be present (this can be done as part of the root scripts described in the "Root Access" category).                                                                                                                                                                                                                                                                                                                                                |

---

---
title: Deployment planning
description: Use this chapter to plan your Ping Autonomous Identity deployment.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:deployment-planning:preface
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/preface.html
---

# Deployment planning

Use this chapter to plan your Ping Autonomous Identity deployment.

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This chapter is for deployers, technical consultants, and administrators who are familiar with Ping Autonomous Identity and are responsible for architecting a production deployment. |

[icon: building, set=fas, size=3x]

#### [Architecture in brief](chap-architecture-in-brief.html)

Learn about the Ping Autonomous Identity architecture.

[icon: lock, set=fas, size=3x]

#### [Security controls](chap-security-controls.html)

Learn about the Ping Autonomous Identity security controls.

[icon: list, set=fas, size=3x]

#### [Topology planning](chap-topology-planning.html)

Review topology sizing considerations.

[icon: check-square, set=fas, size=3x]

#### [Deployment checklist](chap-checklist.html)

Use the checklist.

For installation instructions, refer to the [Ping Autonomous Identity installation guide](../install-guide/preface.html).

For component versions, refer to the [Ping Autonomous Identity Release notes](../release-notes/preface.html).

---

---
title: Features
description: Ping Autonomous Identity provides the following features:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:deployment-planning:chap-autoid-features
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/chap-autoid-features.html
---

# Features

Ping Autonomous Identity provides the following features:

* **Broad Support for Major Identity Governance and Administration (IGA) Providers**. Ping Autonomous Identity supports a wide variety of Identity as a Service (IDaaS) and Identity Management (IDM) data including but not limited to comma-separated values (CSV), Lightweight Directory Access Protocol (LDAP), human resources (HR), database, and IGA solutions.

* **Highly-Scalable Architecture**. Ping Autonomous Identity deploys using a microservices architecture, either on-prem, cloud, or hybrid-cloud environments. Ping Autonomous Identity's architecture supports scalable reads and writes for efficient processing.

* **Powerful UI dashboard**. Ping Autonomous Identity displays your company's entitlements graphically on its UI console. You can immediately investigate those entitlement outliers as possible security risks. The UI also lets you quickly identify those entitlements that are good candidates for automated low-risk approvals or re-certifications. Users can also view a trend-line indicating how well they are managing their entitlements. The UI also provides an application-centric view and a single-page rules view for a different look at your entitlements.

* **Powerful Analytics Engine**. Ping Autonomous Identity's analytics engine is capable of processing millions of access points. Ping Autonomous Identity lets you configure the machine learning process and prune less productive rules. Customers can run analyses, predictions, and recommendations frequently to improve the machine learning process.

* **UI-Driven Schema Extension**. Ping Autonomous Identity lets administrators discover and extend the schema.

* **UI-Driven Data Ingestion and Mappings**. Ping Autonomous Identity provides improved data ingestion tools to define multiple csv input files needed for analysis and their attribute mappings to the schema using the UI.

* **Broad Database Support**. Ping Autonomous Identity supports both Apache Cassandra and MongoDB databases. Both are highly distributed databases with wide usage throughout the industry.

* **Improved Search Support**. Ping Autonomous Identity now incorporates Open Distro for Elasticsearch, a distributed, open-source search engine based on Lucene, to improve database search results and performance.

---

---
title: Glossary
description: A report that identifies potential anomalous assignments.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:deployment-planning:chap-glossary
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/chap-glossary.html
---

# Glossary

* anomaly report

  A report that identifies potential anomalous assignments.

* as-is predictions

  A process where confidence scores are assigned to the entitlements that users have.

* auto-certify

  An action that an entitlement owner can do to approve a justification. Auto-certify indicates that anyone who has the justification is automatically approved for the entitlement.

* auto-request

  An action that an entitlement owner can do to approve a justification. Auto-request indicates that anyone who matches these justification attributes but may not already have access should automatically get provisioned for this entitlement.

* confidence score

  A score from a scale from 0 to 100% that indicates the strength of correlation between an assigned entitlement and a user's data profile.

* data audit

  A pre-analytics process that audits the four data files to ensure data validity with the client.

* data ingestion

  A pre-analytics process that pushes the four data files into the Cassandra database. This allows the entire training process to be performed from the database.

* data sparsity

  A reference to data that has null values. Ping Autonomous Identity requires dense, high quality data with very few null values in the user attributes to get accurate analysis scores.

* data validation

  A pre-analytics process that tests the data to ensure that the content is correct and complete prior to the training process.

* driving factor

  An association rule that is a key factor in a high entitlement confidence score. Any rule that exceeds a confidence threshold level (e.g., 75%) is considered a driving factor.

* entitlement

  An entitlement is a specialized type of `assignment`. A user or device with an entitlement gets access rights to specified resources.

* insight report

  A report that provides metrics on the rules and predictions generated in the analytics run.

* recommendation

  A process run after the as-is predictions that assigns confidence scores to all entitlements and recommends entitlements that users do not currently have. If the confidence score meets a threshold, set by the `conf_thresh` property in the configuration file, the entitlement will be recommended to the user in the UI console.

* resource

  An external system, database, directory server, or other source of identity data to be managed and audited by an identity management system.

* REST

  Representational State Transfer. A software architecture style for exposing resources, using the technologies and protocols of the World Wide Web. REST describes how distributed data objects, or resources, can be defined and addressed.

* stemming

  A process that occurs after training that removes similar association rules that exist in a parent-child relationship. If the child meets three criteria, then it will be removed by the system. The criteria are: 1) the child must match the parent; 2) the child (e.g., \[San Jose, Finance]) is a superset of the parent rule. (e.g., \[Finance]); 3) the child and parent's confidence scores are within a +/- range of each other. The range is set in the configuration file.

* training

  A multi-step process that generates the association rules with confidence scores for each entitlement. First, Ping Autonomous Identity models the frequent itemsets that appear in the user attributes for each user. Next, Ping Autonomous Identity merges the user attributes with the entitlements that were assigned to the user. It then applies association rules to model the sets of user attributes that result in an entitlement access and calculates confidence scores, based on their frequency of appearances in the dataset.

---

---
title: Security controls overview
description: Ping Autonomous Identity uses a number of security protocols as summarized below.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:deployment-planning:chap-security-controls
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/chap-security-controls.html
---

# Security controls overview

Ping Autonomous Identity uses a number of security protocols as summarized below.

**Security Controls Summary**

|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Security                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Encryption Protocol**                  | TLSv1.2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Encryption: External Data in Transit** | All data in transit from Ping Autonomous Identity to the outside world is encrypted. SSL certificates must be configured with the load balancer. By default, Ping Autonomous Identity configures self-signed certificates used by Nginx. Customers can also use their own certificates during deployment.                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Encryption: Internal Data in Transit** | Within the Ping Autonomous Identity secure server network, most data in transit between the Ping Autonomous Identity services is encrypted, but not all. The exception is any non-encrypted communication between Ping Autonomous Identity servers. You can protect this communication via network firewalls.​It is also recommended to disable access on network and firewall ports for services like Spark and Livy that are meant for internal access only. The rest of the services are SSL/TLS-protected including all Nginx-protected services, MongoDB, Cassandra, and Opensearch nodes.                                                                                                              |
| **Encryption: Data at Rest**             | MongoDB is not encrypted natively in Ping Autonomous Identity, but can be encrypted via third-party disk encryption or using the MongoDB enterprise version. If encryption at rest is required, please confirm with the MongoDB vendors how this is handled in existing MongoDB clusters.​Likewise, Cassandra is not natively encrypted, but can be supported through its enterprise versions.                                                                                                                                                                                                                                                                                                               |
| **Authentication**                       | Ping Autonomous Identity uses various authentication methods within its systems, such as the following:- **Local Authentication**. User credentials (user/groups) are stored in Opensearch. Users can log in with a username and password. This is mostly used for development or QA scenarios.

- **OpenID Connect**. Ping Autonomous Identity can use Single Sign-On (SSO) by integrating SSO providers like Azure AD and ForgeRock® Access Management (AM).The API service and Java API Service (JAS) are protected by authentication handlers that support token-based access. JAS also supports certificate-based authentication, which is only used by internal services that require elevated access. |

---

---
title: Topology planning
description: Based on existing production deployments, we have determined a suggested number of servers and settings based on the numbers of identities, entitlements, assignments, and applications. These suggested number of servers and settings are general guidelines for your particular deployment requirements. Each deployment is unique, and requires review prior to implementation.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:deployment-planning:chap-topology-planning
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/deployment-planning/chap-topology-planning.html
section_ids:
  data-sizing: Data sizing
  suggested-number-of-servers: Suggested number of servers
  suggested-analytics-settings: Suggested analytics settings
  production-tech-specs: Production technical recommendations
---

# Topology planning

Based on existing production deployments, we have determined a suggested number of servers and settings based on the numbers of identities, entitlements, assignments, and applications. These suggested number of servers and settings are general guidelines for your particular deployment requirements. Each deployment is unique, and requires review prior to implementation.

For a description of possible production deployments, refer to [Deployment Architecture](../install-guide/chap-deployment-architectures.html) in the [Ping Autonomous Identity Installation Guide](../install-guide/preface.html).

## Data sizing

Ping Identity has determined general categories of dataset sizes based on a company's total number of identities, entitlements, assignments, and applications.

A key determining factor for sizing is the number of applications. If a company has identities, entitlements, and assignments in the Medium range, but if applications are close to 150, then the deployment could be sized for large datasets.

**Data Set Ranges**

|                    |       |         |          |             |
| ------------------ | ----- | ------- | -------- | ----------- |
|                    | Small | Medium  | Large    | Extra Large |
| Total Identities   | <10K  | 10K-50K | 50K-100K | 100K-1M     |
| Total Entitlements | <10K  | 10K-50K | 50K-100K | 100K+       |
| Total Assignments  | <1M   | 1M-6M   | 6M-15M   | 15M+        |
| Total Applications | <50   | 50-100  | 100-150  | 150+        |

## Suggested number of servers

Based on dataset sizing, the following chart shows the number of servers for each deployment. These numbers were derived from existing customer deployments and internal testing setups.

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These numbers are not hard-and-fast rules, but are only presented as starting points for deployment planning purposes. Each deployment is unique and requires proper review prior to implementation. |

**Suggested Number of Servers**

|                       |              |                       |                       |                   |
| --------------------- | ------------ | --------------------- | --------------------- | ----------------- |
|                       | Small        | Medium                | Large                 | Extra Large       |
| Deployer              | 1[\[1\]](#1) | 1                     | 1                     | 1                 |
| Docker                | 1            | 2 (manager; worker)   | 2 (manager; worker)   | Custom[\[2\]](#2) |
| Database              | 1            | 2 (2 seeds)           | 3 (3 seeds)           | Custom[\[2\]](#2) |
| Analytics             | 1            | 3 (master; 2 workers) | 5 (master; 4 workers) | Custom[\[2\]](#2) |
| Opensearch            | 1            | 2 (master; worker)    | 3 (master; 2 workers) | Custom[\[2\]](#2) |
| Opensearch Dashboards | 1            | 1                     | 1                     | 1                 |

\[1] This figure assumes that you have a separate deployer machine from the target machine for single-node deployments. You can also run the deployer on the target machine for a single-node deployment. For multi-node deployments, we recommend running the deployer on a dedicated low-spec box.\
\[2] For extra-large deployments, server requirements will need to be specifically determined.

## Suggested analytics settings

Analytics settings require proper sizing for optimal machine-learning performance.

The following chart shows the analytics settings that are for each deployment size. The numbers were derived from customer deployments and internal testing setups.

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These numbers are not hard-and-fast rules, but are only presented as starting points for deployment planning purposes. Each deployment is unique and requires proper review prior to implementation. |

**Suggested Analytics Settings**

|                              |       |        |       |                   |
| ---------------------------- | ----- | ------ | ----- | ----------------- |
|                              | Small | Medium | Large | Extra Large       |
| Driver Memory (GB)           | 2     | 10     | 50    | Custom[\[1\]](#1) |
| Driver Cores                 | 3     | 3      | 12    | Custom[\[1\]](#1) |
| Executor Memory (GB)         | 3     | 3-6    | 12    | Custom[\[1\]](#1) |
| Executor Cores               | 6     | 6      | 6     | Custom[\[1\]](#1) |
| Elastic Heap Size[\[2\]](#2) | 2     | 4-8    | 8     | Custom[\[1\]](#1) |

\[1] For extra-large deployments, server requirements will need to be specifically customized.\
\[2] Set in the `vars.yml` file.

## Production technical recommendations

Ping Autonomous Identity 2022.11.12 has the following technical specifications for production deployments:

**Production Technical Specifications**

|                                   |                                                                                           |                                                                      |                                                                      |                                                                                                                                                                                         |                                                                      |
| --------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
|                                   | **Deployer**                                                                              | **Database**                                                         | **Database**                                                         | **Analytics**                                                                                                                                                                           | **Opensearch**                                                       |
| Installed Components              | Docker                                                                                    | Cassandra                                                            | MongoDB                                                              | Spark (Spark Master)/Apache Livy                                                                                                                                                        | Opensearch                                                           |
| OS                                | CentOS                                                                                    | CentOS                                                               | CentOS                                                               | CentOS                                                                                                                                                                                  | CentOS                                                               |
| Number of Servers                 | Refer to [Suggested number of servers](#suggested-number-of-servers)                      | Refer to [Suggested number of servers](#suggested-number-of-servers) | Refer to [Suggested number of servers](#suggested-number-of-servers) | Refer to [Suggested number of servers](#suggested-number-of-servers)                                                                                                                    | Refer to [Suggested number of servers](#suggested-number-of-servers) |
| RAM (GB)                          | 4-32                                                                                      | 32                                                                   | 32                                                                   | 64-128                                                                                                                                                                                  | 64                                                                   |
| CPUs                              | 2-4                                                                                       | 8                                                                    | 8                                                                    | 16                                                                                                                                                                                      | 16                                                                   |
| Non-OS Disk Space (GB)[\[1\]](#1) | 32                                                                                        | 1000                                                                 | 1000                                                                 | 1000                                                                                                                                                                                    | 1000                                                                 |
| NFS Shared Mount                  | N/A                                                                                       | N/A                                                                  | N/A                                                                  | 1 TB NFS mount shared across all Docker Swarm nodes (if more than 1 node is provisioned) at location separate from the non-OS disk space requirement. For example, `/data` or `shared`. | N/A                                                                  |
| Networking                        | nginx: 443​Docker Manager: 2377 (TCP)​Docker Swarm: ​ 7946, 4789 (UDP) ​ 7946, 2049 (TCP) | Client Protocol Port: 9042Cassandra Nodes: 7000                      | Client Protocol Port: 27017MongoDB Nodes: 30994                      | Spark Master: 7077Spark Workers: Randomly assigned ports                                                                                                                                | Opensearch: 9300Opensearch (REST): 9200Opensearch Dashboards: 5601   |
| Licensing                         | N/A using Docker CE free version                                                          | N/A                                                                  | N/A                                                                  | N/A                                                                                                                                                                                     | N/A                                                                  |
| Software Version                  | Docker: 20.10.17                                                                          | Cassandra: 4.0.6                                                     | MongoDB: 4.4                                                         | Spark: 3.3.2Apache Livy: 0.8.0-incubating                                                                                                                                               | Opensearch/Opensearch Dashboards 1.3.14                              |
| Component Reference               | Refer to below.[\[2\]](#2)                                                                | Refer to below.[\[3\]](#3)                                           | Refer to below.[\[4\]](#4)                                           | Refer to below.[\[5\]](#5)                                                                                                                                                              | Refer to below.[\[6\]](#6)                                           |

\[1] At root directory "/"\
\[2] <https://docs.docker.com/ee/ucp/admin/install/system-requirements/>\
\[3] <https://docs.datastax.com/en/dse-planning/doc/planning/planningHardware.html>\
\[4] <http://cassandra.apache.org/doc/latest/operating/hardware.html>\
\[4] <http://www.mongodb.com>\
\[5] <https://spark.apache.org/docs/latest/security.html#configuring-ports-for-network-security>\
\[6] <https://Opensearch.org/>
---
title: Architecture in Brief
description: "Ping Autonomous Identity's flexible architecture can deploy in any number of ways: single-node or multi-node configurations across on-prem, cloud, hybrid, or multi-cloud environments. The Ping Autonomous Identity architecture has a simple three-layer conceptual model:"
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity::chap-architecture-in-brief
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/chap-architecture-in-brief.html
---

# Architecture in Brief

Ping Autonomous Identity's flexible architecture can deploy in any number of ways: single-node or multi-node configurations across on-prem, cloud, hybrid, or multi-cloud environments. The Ping Autonomous Identity architecture has a simple three-layer conceptual model:

* **Application Layer**. Ping Autonomous Identity implements a flexible Docker Swarm microservices architecture, where multiple applications run together in containers. The microservices component provides flexible configuration and end-user interaction to the deployment. The microservices components are the following:

  * **Ping Autonomous Identity UI**. Ping Autonomous Identity supports a dynamic UI that displays the entitlements, confidence scores, and recommendations.

  * **Ping Autonomous Identity API**. Ping Autonomous Identity provides an API that can access endpoints using REST. This allows easy scripting and programming for your system.

  * **Self-Service Tool**. The self-service tool lets users reset their Ping Autonomous Identity passwords.

  * **Backend Repository**. The backend repository stores Ping Autonomous Identity user information. To interface with the backend repository, you can use the `phpldapadmin` tool to enter and manage users.

  * **Configuration Service**. Ping Autonomous Identity supports a configuration service that allows you to set parameters for your system and processes.

  * **Nginx**. Nginx is a popular HTTP server and reverse proxy for routing HTTPS traffic.

  * **Hashicorp Consul**. Consul is a third-party system for service discovery and configuration.

  * **Apache Livy**. Ping Autonomous Identity supports Apache Livy to provide a RESTful interface to Apache Spark.

  * **Java API Service**. Ping Autonomous Identity supports the Java API Service for RESTful interface to the Cassandra or MongoDB database.

* **Data Layer**. Ping Autonomous Identity supports Apache Cassandra NoSQL and MongoDB databases to serve predictions, confidence scores, and prediction data to the end user. Apache Cassandra is a distributed and linearly scalable database with no single point of failure. MongoDB is a schema-free, distributed database that uses JSON-like documents as data objects. Java API Service (JAS) provides a REST interface to the databases.

  Ping Autonomous Identity also implements Open Distro for Elasticsearch and Kibana to improve search performance for its entitlement data. Elastic Persistent Search supports scalable writes and reads.

* **Analytics and Administration Layer**. Ping Autonomous Identity uses a multi-source Apache Spark analytics engine to generate the predictions and confidence scores. Apache Spark is a distributed, cluster-computing framework for AI machine learning for large datasets. Ping Autonomous Identity runs the analytics jobs directly from the Spark master over Apache Livy REST interface.

  Figure 1: A Simple Conceptual Image of the Ping Autonomous Identity Architecture

![Ping Autonomous Identity architecture](_images/autoid-architecture-conceptual.png)

---

---
title: Features
description: Ping Autonomous Identity provides the following features:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity::chap-autoid-features
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/chap-autoid-features.html
---

# Features

Ping Autonomous Identity provides the following features:

* **Broad Support for Major Identity Governance and Administration (IGA) Providers**. Ping Autonomous Identity supports a wide variety of Identity as a Service (IDaaS) and Identity Management (IDM) data including but not limited to comma-separated values (CSV), Lightweight Directory Access Protocol (LDAP), human resources (HR), database, and IGA solutions.

* **Highly-Scalable Architecture**. Ping Autonomous Identity deploys using a microservices architecture, either on-prem, cloud, or hybrid-cloud environments. Ping Autonomous Identity's architecture supports scalable reads and writes for efficient processing.

* **Powerful UI dashboard**. Ping Autonomous Identity displays your company's entitlements graphically on its UI console. You can immediately investigate those entitlement outliers as possible security risks. The UI also lets you quickly identify those entitlements that are good candidates for automated low-risk approvals or re-certifications. Users can also view a trend-line indicating how well they are managing their entitlements. The UI also provides an application-centric view and a single-page rules view for a different look at your entitlements.

* **Powerful Analytics Engine**. Ping Autonomous Identity's analytics engine is capable of processing millions of access points within a short period of time. Ping Autonomous Identity lets you configure the machine learning process and prune less productive rules. Customers can run analyses, predictions, and recommendations frequently to improve the machine learning process.

* **UI-Driven Schema Extension**. Ping Autonomous Identity lets administrators discover and extend the schema, and set up attribute mappings using the UI.

* **UI-Driven Data Ingestion and Mappings**. Ping Autonomous Identity provides improved data ingestion tools to define multiple csv input files needed for analysis and their attribute mappings to the schema using the UI.

* **UI-Driven Data Ingestion and Mappings**. Ping Autonomous Identity provides improved data ingestion tools to define multiple csv input files needed for analysis and their attribute mappings to the schema using the UI.

* **Broad Database Support**. Ping Autonomous Identity supports both Apache Cassandra and MongoDB databases. Both are highly distributed databases with wide usage throughout the industry.

* **Improved Search Support**. Ping Autonomous Identity now incorporates Open Distro for Elasticsearch, a distributed, open-source search engine based on Lucene, to improve database search results and performance.

---

---
title: Glossary
description: A report that identifies potential anomalous assignments.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity::chap-glossary
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/chap-glossary.html
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

  A pre-analytics process that audits the seven data files to ensure data validity with the client.

* data ingestion

  A pre-analytics process that pushes the seven .csv files into the Cassandra database. This allows the entire training process to be performed from the database.

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
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

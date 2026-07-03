---
title: "Appendix A: Ping Autonomous Identity ports"
description: The Ping Autonomous Identity deployment uses the following ports. The Docker deployer machine opens the ports in the firewall on the target node. If you are using cloud virtual machines, you need to open these ports on the virtual cloud network.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:appendix-deployment-ports
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/appendix-deployment-ports.html
---

# Appendix A: Ping Autonomous Identity ports

The Ping Autonomous Identity deployment uses the following ports. The Docker deployer machine opens the ports in the firewall on the target node. If you are using cloud virtual machines, you need to open these ports on the virtual cloud network.

Ping Autonomous Identity uses the following ports:

**Ping Autonomous Identity ports**

| Port        | Protocol | Machine                       | Source                                     | Description                                               |
| ----------- | -------- | ----------------------------- | ------------------------------------------ | --------------------------------------------------------- |
| 2377        | TCP      | Docker managers               | Docker managers and nodes                  | Communication between the nodes of a Docker swarm cluster |
| 7946        | TCP/UDP  | Docker managers and workers   | Docker managers and workers                | Communication among nodes for container network discovery |
| 4789        | UDP      | Docker managers and workers   | Docker managers and workers                | Overlay network traffic                                   |
| 7001        | TCP      | Cassandra                     | Cassandra nodes                            | Internode communication                                   |
| 9042        | TCP      | Cassandra                     | Cassandra nodes, Docker managers and nodes | CQL native transport                                      |
| 27017       | TCP      | MongoDB                       | MongoDB nodes, Docker managers and nodes   | Default ports for mongod and mongos instances             |
| 9200        | TCP      | Open Distro for Elasticsearch | Docker managers and nodes                  | Elasticsearch REST API endpoint                           |
| 7077        | TCP      | Spark master                  | Spark workers                              | Spark master internode communication port                 |
| 40040-40045 | TCP      | Spark Master                  | Spark Workers                              | Spark driver ports for Spark workers to callback          |
| 443         | TCP      | Docker managers               | User's browsers/API clients                | Port to access the dashboard and API                      |
| 10081       | TCP      | Docker managers               | User's browsers/API clients                | Port for the JAS service.                                 |

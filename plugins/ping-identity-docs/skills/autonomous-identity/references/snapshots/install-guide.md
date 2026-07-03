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

---

---
title: "Appendix B: vars.yml"
description: Ping Autonomous Identity has a configuration file where you can set the analytics data and configuration directories, private IP address mapping, LDAP/SSO options, and session duration during installation. The file is created when running the create-template command during the installation and is located in the /autoid-config directory.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:appendix-vars-yml
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/appendix-vars-yml.html
---

# Appendix B: vars.yml

Ping Autonomous Identity has a configuration file where you can set the analytics data and configuration directories, private IP address mapping, LDAP/SSO options, and session duration during installation. The file is created when running the `create-template` command during the installation and is located in the `/autoid-config` directory.

The file is as follows:

```
ai_product: auto-id                       # Product name
domain_name: forgerock.com                # Default domain name
target_environment: autoid                # Default namespace
analytics_data_dir: /data                 # Default data directory
analytics_conf_dir: /data/conf            # Default config directory for analytics

# set to true for air-gap installation
offline_mode: false

# choose the DB Type : cassandra| mongo
db_driver_type: cassandra

# Needed only if private and public IP address of
# target nodes are different. If cloud VMs the private
# is different than the IP address (public ip) used for
# SSH. Private IP addresses are used by various services
# to reach other services in the cluster
# Example:
# private_ip_address_mapping:
#   35.223.33.21: "10.128.0.5"
#   108.59.83.132: "10.128.0.37"
#   ...
private_ip_address_mapping:                        # private and external IP mapping
#private_ip_address_mapping-ip-addesses#

api:
 authentication_option: "Local"                   # Values: "Local", "SSO", "LocalAndSSO"
 access_log_enabled: true                         # Enable access logs
 jwt_expiry: "30 minutes"                         # Default session duration
 jwt_secret_file: "{{ install_path }}/jwt/secret.txt"   # Location of JWT secret file
 jwt_audience: "http://my.service"
 oidc_jwks_url: "na"
 local_auth_mode_password: Welcome123
 session_secret: "q0civ3L33W"

# set the following API parameters when           # SSO and LdapAndSSO properties
# authentication_option is SSO or LdapAndSSO
#  oidc_issuer:
#  oidc_auth_url
#  oidc_token_url:
#  oidc_user_info_url:
#  oidc_callback_url:
#  oidc_jwks_url:
#  oidc_client_scope:
#  oidc_groups_attribute:
#  oidc_uid_attribute:
#  oidc_client_id:
#  oidc_client_secret:
#  admin_object_id:
#  entitlement_owner_object_id:
#  executive_object_id:
#  supervisor_object_id:
#  user_object_id:
#  application_owner_object_id:
#  role_owner_object_id:
#  role_engineer_object_id:
#  oidc_end_session_endpoint:
#  oidc_logout_redirect_url:

# mongo config starts
# uncomment below for mongo with replication enabled. Not needed for
#   single node deployments
# mongodb_replication_replset: mongors

# custom key
# password for inter-process authentication
#
# please regenerate this file on production environment with command 'openssl rand -base64 741'
#mongodb_keyfile_content: |
#  8pYcxvCqoe89kcp33KuTtKVf5MoHGEFjTnudrq5BosvWRoIxLowmdjrmUpVfAivh
#  CHjqM6w0zVBytAxH1lW+7teMYe6eDn2S/O/1YlRRiW57bWU3zjliW3VdguJar5i9
#  Z+1a8lI+0S9pWynbv9+Ao0aXFjSJYVxAm/w7DJbVRGcPhsPmExiSBDw8szfQ8PAU
#  2hwRl7nqPZZMMR+uQThg/zV9rOzHJmkqZtsO4UJSilG9euLCYrzW2hdoPuCrEDhu
#  Vsi5+nwAgYR9dP2oWkmGN1dwRe0ixSIM2UzFgpaXZaMOG6VztmFrlVXh8oFDRGM0
#  cGrFHcnGF7oUGfWnI2Cekngk64dHA2qD7WxXPbQ/svn9EfTY5aPw5lXzKA87Ds8p
#  KHVFUYvmA6wVsxb/riGLwc+XZlb6M9gqHn1XSpsnYRjF6UzfRcRR2WyCxLZELaqu
#  iKxLKB5FYqMBH7Sqg3qBCtE53vZ7T1nefq5RFzmykviYP63Uhu/A2EQatrMnaFPl
#  TTG5CaPjob45CBSyMrheYRWKqxdWN93BTgiTW7p0U6RB0/OCUbsVX6IG3I9N8Uqt
#  l8Kc+7aOmtUqFkwo8w30prIOjStMrokxNsuK9KTUiPu2cj7gwYQ574vV3hQvQPAr
#  hhb9ohKr0zoPQt31iTj0FDkJzPepeuzqeq8F51HB56RZKpXdRTfY8G6OaOT68cV5
#  vP1O6T/okFKrl41FQ3CyYN5eRHyRTK99zTytrjoP2EbtIZ18z+bg/angRHYNzbgk
#  lc3jpiGzs1ZWHD0nxOmHCMhU4usEcFbV6FlOxzlwrsEhHkeiununlCsNHatiDgzp
#  ZWLnP/mXKV992/Jhu0Z577DHlh+3JIYx0PceB9yzACJ8MNARHF7QpBkhtuGMGZpF
#  T+c73exupZFxItXs1Bnhe3djgE3MKKyYvxNUIbcTJoe7nhVMrwO/7lBSpVLvC4p3
#  wR700U0LDaGGQpslGtiE56SemgoP

# mongo config ends

elastic_heap_size: 1g   # sets the heap size (1g|2g|3g) for the Elastic Servers

jas:
 auth_enabled: true
 auth_type: 'jwt'
 signiture_key_id: 'service1-hmac'
 signiture_algorithm: 'hmac-sha256'
 max_memory: 4096M
 mapping_entity_type: /common/mappings
 datasource_entity_type: /common/datasources

mongo_port: 27017   # Port where Mongo is running
mongo_ldap: false   # Specify if Mongo is authenticated against an LDAP

elastic_host: 10.128.0.28     # IP Address of master node where Opensearch is running
elastic_port: 9200            # Port of master node where Opensearch is running
elastic_user: elasticadmin    # Opensearch username

kibana_host: 10.128.0.28      # IP Address of node where Opensearch Dashboard is running

apache_livy:
 dest_dir: /home/ansible/livy # Folder where livy is installed. AutoID copies analytics files to this directory.

cassandra:                                                               # Cassandra Nodes details.
 enable_ssl: "true"                                                      # Set if SSL is enabled.
 contact_points:                                                         # Comma seperated list of ip addresses - first ip is master#
 port: 9042                                                              # Port where cassandra node is running
 username: zoranuser                                                     # User created for AutoID to seed Schema
 cassandra_keystore_password: "Acc#1234"                                 # Keystore Password
 cassandra_truststore_password: "Acc#1234"                               # Truststore Password
 ssl_client_key_file: "zoran-cassandra-client-key.pem"                   # Cassandra Client Key File
 ssl_client_cert_file: "zoran-cassandra-client-cer.pem"                  # Cassandra Client Cert File
 ssl_ca_file: "zoran-cassandra-server-cer.pem"                           # Cassandra Server Root CA File
 server_truststore_jks: "zoran-cassandra-server-truststore.jks"          # Server Truststore file for services to connect
 client_truststore_jks: "zoran-cassandra-client-truststore.jks"          # Client Truststore file for services to connect
 client_keystore_jks: "zoran-cassandra-client-keystore.jks"              # Client Keystore file for services to use
```

---

---
title: Architecture in Brief
description: "Ping Autonomous Identity's flexible architecture can deploy in any number of ways: single-node or multi-node configurations across on-prem, cloud, hybrid, or multi-cloud environments. The Ping Autonomous Identity architecture has a simple three-layer conceptual model:"
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-architecture-in-brief
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-architecture-in-brief.html
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

![Ping Autonomous Identity has a three-layer, scalable, and flexible architecture.](_images/autoid-architecture-conceptual.png)

---

---
title: Deployment architectures
description: To simplify your deployments, Ping Identity provides a deployer script to install Ping Autonomous Identity on a target node. The deployer pulls in images from the Ping Identity Google Cloud Repository and uses it to deploy the microservices and analytics for Ping Autonomous Identity on a target machine. The target machine only requires the base operating system.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-deployment-architectures
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-deployment-architectures.html
---

# Deployment architectures

To simplify your deployments, Ping Identity provides a deployer script to install Ping Autonomous Identity on a target node. The deployer pulls in images from the Ping Identity Google Cloud Repository and uses it to deploy the microservices and analytics for Ping Autonomous Identity on a target machine. The target machine only requires the base operating system.

|   |                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you are upgrading Ping Autonomous Identity on a RHEL 7/CentOS 7, the upgrade to 2022.11 uses RHEL 7/CentOS 7 only. For new and clean installations, Ping Autonomous Identity requires RHEL 8 or CentOS Stream 8 only. |

Autonomous Identity 2022.11.0 introduced a new deployer, Deployer Pro, that pulls in the base code from the Ping Identity Google Cloud repository. Customers must now pre-install the third-party software dependencies prior to running deployer pro. For more information, refer to [Install a single node deployment](chap-install-singlenode-target.html).

There are four basic deployments, all of them similar, but in slightly different configurations:

* **Single-Node Target Deployment**. Deploy Ping Autonomous Identity on a single Internet-connected target machine. The deployer script lets you deploy the system from a local laptop or machine or from the target machine itself. The target machine can be on on-prem or on a cloud service, such as Google Cloud Platform (GCP), Amazon Web Services (AWS), Microsoft Azure or others. For installation instructions, refer to [Install a Single-Node Deployment](chap-install-singlenode-target.html).

  ![Ping Autonomous Identity deployed in a single-node target deployment](_images/auto-id-singlenode.png)Figure 1. A single-node target deployment.

* **Single-Node Air-Gapped Target Deployment**. Deploy Ping Autonomous Identity on a single-node target machine that resides in an air-gapped deployment. In an air-gapped deployment, the target machine is placed in an enhanced security environment where external Internet access is not available. You transfer the deployer and image to the target machine using media, such as a portable drive. Then, run the deployment within the air-gapped environment. For installation instruction, refer to [Install a Single-Node Air-Gapped](chap-install-singlenode-airgap.html).

  ![Ping Autonomous Identity deployed in an environment that has no Internet connection](_images/auto-id-singlenode-airgap.png)Figure 2. An air-gapped deployment.

* **Multi-Node Deployment**. Deploy Ping Autonomous Identity on multi-node deployment to distribute the process load on the servers. For installation instruction, refer to [Install a Multi-Node Deployment](chap-install-multinode.html).

  ![Ping Autonomous Identity deployed in an environment that multiple nodes](_images/auto-id-multinode.png)Figure 3. A multi-node target deployment.

* **Multi-Node Air-Gapped Deployment**. Deploy Ping Autonomous Identity a multi-node configuration in an air-gapped network. The multinode network has no external Internet connection. For installation instruction, refer to [Install a Multi-Node Air-Gapped Deployment](chap-install-multinode-airgap.html).

  ![Ping Autonomous Identity deployed in an environment with multiple nodes in an air-gapped environment](_images/auto-id-multinode-airgap.png)Figure 4. A multi-node air-gapped target deployment.

---

---
title: Features
description: Ping Autonomous Identity provides the following features:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-autoid-features
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-autoid-features.html
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
title: Getting Started
description: This section presents the steps to prepare your target and deployer machines.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-getting-started
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-getting-started.html
section_ids:
  sec-auto-id-prerequisites: Prerequisites
  sec-setup-deployer-node: Set Up the Deployer Machine
  check_the_deployer_machine: Check the Deployer Machine
  install_docker_on_the_deployer_machine: Install Docker on the Deployer Machine
  set_up_ssh: Set Up SSH
---

# Getting Started

This section presents the steps to prepare your target and deployer machines.

Begin the deployment with the following pre-deployment steps:

## Prerequisites

To get you started on deploying Ping Autonomous Identity in your environment, make sure the following prerequisites are followed:

* **Operating System**. The target machine requires CentOS 8, Docker, and Python 3.6 or later. The deployer machine can use any operating system as long as Docker is installed. For this chapter, we use CentOS 8 as its base operating system.

* **Memory Requirements**. Make sure you have enough free disk space on the deployer machine before running the `deployer.sh` commands. We recommend at least 500GB.

Ping Autonomous Identity provides a Docker image that creates a `deployer.sh` script to download all of the images necessary for the installation. The following images are downloaded:

* Release 2020.6 microservices

* Apache Spark 2.4.4

* Cassandra 3.11.2

* Analytics service v19

* Various RPM and PIP packages that Ping Autonomous Identity requires.

## Set Up the Deployer Machine

Let's set up the deployer machine from which we will run Docker commands to install Ping Autonomous Identity onto the target node.

For prerequisites, make sure you have CentOS 8 installed on your server.

### Check the Deployer Machine

1. The install assumes that you have CentOS 8 as your operating system. Check your CentOS 8 version.

   ```
   $ [../../resources/install.bash:#check-centos-version]
   ```

2. As root, configure the user for passwordless sudo. Replace "username" with your username.

   ```
   # [../../resources/install.bash:#add-passwordless-sudo]
   ```

3. Install yum-utils package on the deployer machine. yum-utils is a utilities manager for the Yum RPM package repository. The repository compresses software packages for Linux distributions.

   ```
   $ sudo yum -y install yum-utils
   ```

4. Check your python version.

   ```
   $ python3 --version
   ```

5. If you do not have Python 3.6 or higher. Install it on your system.

   ```
   $ sudo yum -y install  python3
   ```

### Install Docker on the Deployer Machine

1. Create the installation directory. Note that you can use any install directory for your system as long as your run the `deployer.sh` script from there. Also, the disk volume where you have the install directory must have at least 8GB free space for the installation.

   ```
   $ mkdir ~/autoid-config
   ```

2. Set up the Docker-CE repository.

   ```
   $ sudo yum-config-manager \
        --add-repo https://download.docker.com/linux/centos/docker-ce.repo
   ```

3. Install the latest version of the Docker CE, the command-line interface, and containerd.io, a containerized website.

   ```
   $ sudo yum -y install  docker-ce docker-ce-cli containerd.io
   ```

4. Enable Docker to start at boot.

   ```
   $ sudo systemctl enable docker
   ```

5. Start Docker.

   ```
   $ sudo systemctl start docker
   ```

6. Add the user to the Docker group.

   ```
   $ sudo usermod -aG docker $USER
   ```

### Set Up SSH

The deployer machine requires SSH for communication with its managed nodes. The deployer machine's public SSH key should be copied to the `autoid-config` installation directory on the managed node in addition to the `~/.ssh/authorized_keys` directory. The `autoid-config` directory allows the `autoid` user on the deployer machine to log in to the account on the target.

Note that in single node deployments, SSH is still required for the deployer to communicate with itself.

1. On the deployer machine, run `ssh-keygen` to generate an RSA keypair, and then click Enter. You can use the default filename. Enter a password for protecting your private key.

   ```
   $ ssh-keygen -t rsa
   ```

   The public and private rsa key pair is stored in `home-directory/.ssh/id_rsa` and `home-directory/.ssh/id_rsa.pub` .

2. On the deployer machine, copy the SSH key to the `autoid-config` directory.

   ```
   $ cp ~/.ssh/id_rsa ~/autoid-config
   ```

3. Change the privileges to the file.

   ```
   $ chmod 400 ~/autoid-config/id_rsa
   ```

4. Copy the public key file to your `authorized_keys` directory on the target node.

   ```
   $ [../../resources/install.bash:#copy-ssh-key-to-target-authorized-keys]
   ```

5. Copy the public key file to the installation directory on the target node.

   ```
   $ [../../resources/install.bash:#copy-ssh-key-to-target-autoid-config]
   ```

6. Test your setup.

   ```
   $ ping remote_username@server_ip_address
   ```

---

---
title: Glossary
description: A report that identifies potential anomalous assignments.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-glossary
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-glossary.html
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

---

---
title: Install a multi-node air-gapped deployment
description: This chapter presents instructions on deploying Ping Autonomous Identity in a multi-node air-gapped or offline target machine with no external Internet connectivity. Ping Identity provides a deployer script that pulls a Docker image from Ping Identity's Google Cloud Registry repository. The image contains the microservices, analytics, and backend databases needed for the system.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-install-multinode-airgap
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-install-multinode-airgap.html
section_ids:
  summary_of_the_installation_steps: Summary of the installation steps
  prerequisites-multinode-airgap: Prerequisites
  setup-nodes-multinode-airgap: Set up the nodes
  install-third-party-multinode-airgap: Install third-party components
  setup-ssh-multinode-deployer-airgap: Set up SSH on the deployer
  prepare-tar-multinode-airgap: Prepare the tar file
  install-autoid-multinode-airgap: Install Ping Autonomous Identity air-gapped
  set-replication-factor-airgap: Set the replication factor
  resolve_hostname: Resolve Hostname
  access_the_dashboard: Access the Dashboard
  start_the_analytics: Start the Analytics
---

# Install a multi-node air-gapped deployment

This chapter presents instructions on deploying Ping Autonomous Identity in a multi-node air-gapped or offline target machine with no external Internet connectivity. Ping Identity provides a deployer script that pulls a Docker image from Ping Identity's Google Cloud Registry repository. The image contains the microservices, analytics, and backend databases needed for the system.

The air-gap installation is similar to that of the multi-node deployment, except that the image and deployer script must be stored on a portable drive and copied to the air-gapped target environment.

The deployment depends on how the network is configured. You could have a Docker cluster with multiple Spark nodes and Cassandra or MongoDB nodes. The key is to determine the IP addresses of each node.

## Summary of the installation steps

To set up the 2022.11.12 deployment, run the following steps:

* [Prerequisites](#prerequisites-multinode-airgap)

* [Set up the nodes](#setup-nodes-multinode-airgap)

* [Set up SSH on the deployer](#setup-ssh-multinode-deployer-airgap)

* [Prepare the tar file](#prepare-tar-multinode-airgap)

* [Install third-party components](#install-third-party-multinode-airgap)

* [Install Ping Autonomous Identity air-gapped](#install-autoid-multinode-airgap)

* [Set the replication factor](#set-replication-factor-airgap)

## Prerequisites

Deploy Ping Autonomous Identity on a multi-node air-gapped target on Redhat Linux Enterprise 8 or CentOS Stream 8. The following are prerequisites:

* **Operating System**. The target machine requires Redhat Linux Enterprise 8 or CentOS Stream 8. The deployer machine can use any operating system as long as Docker is installed. For this chapter, we use Redhat Linux Enterprise 8 as its base operating system.

  |   |                                                                                                                                                                                                                          |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you are upgrading Ping Autonomous Identity on a RHEL 7/CentOS 7, the upgrade to 2022.11 uses RHEL 7/CentOS 7 only. For new and clean installations, Ping Autonomous Identity requires RHEL 8 or CentOS Stream 8 only. |

* **Default Shell**. The default shell for the `autoid` user must be `bash`.

* **Subnet Requirements**. We recommend deploying your multi-node machines within the same subnet. Ports must be open for the installation to succeed. Each instance should be able to communicate to the other instances.

  |   |                                                                                                                                                                                                                                                                                  |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If any hosts used for the Docker cluster (docker-managers, docker-workers) have an IP address in the range of 10.0.x.x, they will conflict with the Swarm network. As a result, the services in the cluster will not connect to the Cassandra database or Elasticsearch backend. |

  The Docker cluster hosts must be in a subnet that provides IP addresses 10.10.1.x or higher.

* **Deployment Requirements**. Ping Autonomous Identity provides a `deployer.sh` script that downloads and installs the necessary Docker images. To download the deployment images, you must first obtain a registry key to sign on to the Ping Google Cloud Registry. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

* **Filesystem Requirements**. Ping Autonomous Identity requires a shared filesystem accessible from the Spark main, Spark worker, analytics hosts, and application layer. The shared filesystem should be mounted at the same mount directory on all of those hosts. If the mount directory for the shared filesystem is different from the default, `/data` , update the `/autoid-config/vars.yml` file to point to the correct directories:

  ```
  analytics_data_dir: /data
  analytics_conf_dif: /data/conf
  ```

* **Architecture Requirements**. Make sure that the Spark main is on a separate node from the Spark workers.

* **Database Requirements**. Decide which database you are using: Apache Cassandra or MongoDB. The configuration procedure is slightly different for each database.

* **Deployment Best-Practice**. The example combines the Opensearch data and Opensearch Dashboards nodes. For best performance in production, dedicate a separate node to Opensearch, data nodes, and Opensearch Dashboards.

* **IPv4 Forwarding**. Many high-security environments run their CentOS-based systems with IPv4 forwarding disabled. However, Docker Swarm doesn't work with a disabled IPv4 forward setting. In such environments, make sure to enable IPv4 forwarding in the file `/etc/sysctl.conf`:

  ```
  net.ipv4.ip_forward=1
  ```

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We recommend that your deployer team have someone with Cassandra expertise. This guide is not sufficient to troubleshoot any issues that may arise. |

## Set up the nodes

Set up each node as presented in [Set Up the Nodes](chap-install-multinode.html#setup-nodes-multinode).

Make sure you have sufficient storage for your particular deployment. For more information on sizing considerations, refer to [Deployment Planning Guide](../deployment-planning/chap-topology-planning.html).

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For multinode deployments, there is a known issue with RHEL 8/CentOS Stream 8 and overlay network configurations. Refer to [Known Issues in 2022.11.0](../release-notes/changelog.html#known-issues-2022-11-0). |

## Install third-party components

Set up a machine with the required third-party software dependencies. Refer to: [Install third-party components](chap-install-singlenode-target.html#install-third-party).

## Set up SSH on the deployer

1. On the deployer machine, run `ssh-keygen` to generate an RSA keypair, and then click Enter. You can use the default filename. Enter a password for protecting your private key.

   ```
   ssh-keygen -t rsa -C "autoid"
   ```

   The public and private rsa key pair is stored in `home-directory/.ssh/id_rsa` and `home-directory/.ssh/id_rsa.pub`.

2. Copy the SSH key to the `autoid-config` directory.

   ```
   cp ~/.ssh/id_rsa ~/autoid-config
   ```

3. Change the privileges to the file.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

## Prepare the tar file

Run the following steps on an Internet-connected host machine:

1. On the deployer machine, change to the installation directory.

   ```
   cd ~/autoid-config/
   ```

2. Sign on to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

   ```
   docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
   ```

   The following output is displayed:

   ```
   Login Succeeded
   ```

3. Run the `create-template` command to generate the `deployer.sh` script wrapper. Note that the command sets the configuration directory on the target node to `/config`. Note that the `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

   ```
   docker run --user=$(id -u) -v ~/autoid-config:/config -it gcr.io/forgerock-autoid/deployer-pro:2022.11.12 create-template
   ```

4. Open the `~/autoid-config/vars.yml` file, set the `offline_mode` property to `true`, and then save the file.

   ```
   offline_mode: true
   ```

5. Download the Docker images. This step downloads software dependencies needed for the deployment and places them in the `autoid-packages` directory.

   ```
   sudo ./deployer.sh download-images
   ```

6. Create a tar file containing all of the Ping Autonomous Identity binaries.

   ```
   tar czf autoid-packages.tgz deployer.sh autoid-packages/*
   ```

7. Copy the `autoid-packages.tgz` to a portable hard drive.

## Install Ping Autonomous Identity air-gapped

Make sure you have the following prerequisites:

* IP address of machines running Opensearch, MongoDB, or Cassandra.

* The Ping Autonomous Identity user should have permission to write to `/opt/autoid` on all machines

* To download the deployment images for the install, you still need your registry key to log into the Ping Google Cloud Registry to download the artifacts.

* Make sure you have the proper Opensearch certificates with the exact names for both pem and JKS files copied to `~/autoid-config/certs/elastic`:

  * esnode.pem

  * esnode-key.pem

  * root-ca.pem

  * elastic-client-keystore.jks

  * elastic-server-truststore.jks

* Make sure you have the proper MongoDB certificates with exact names for both pem and JKS files copied to `~/autoid-config/certs/mongo`:

  * mongo-client-keystore.jks

  * mongo-server-truststore.jks

  * mongodb.pem

  * rootCA.pem

* Make sure you have the proper Cassandra certificates with exact names for both pem and JKS files copied to \~/autoid-config/certs/cassandra:

  * Zoran-cassandra-client-cer.pem

  * Zoran-cassandra-client-keystore.jks

  * Zoran-cassandra-server-cer.pem

  * zoran-cassandra-server-keystore.jks

  * Zoran-cassandra-client-key.pem

  * Zoran-cassandra-client-truststore.jks

  * Zoran-cassandra-server-key.pem

  * Zoran-cassandra-server-truststore.jks

Install Ping Autonomous Identity:

1. Change to the directory.

   ```
   cd autoid-config
   ```

2. Run the create-template command to generate the `deployer.sh` script wrapper and configuration files. Note that the command sets the configuration directory on the target node to `/config`. The `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

   ```
   docker run --user=$(id -u) -v ~/autoid-config:/config -it gcr.io/forgerock-autoid/deployer-pro:2022.11.3 create-template
   ```

3. Create a certificate directory for elastic.

   ```
   mkdir -p autoid-config/certs/elastic
   ```

4. Copy the Opensearch certificates and JKS files to `autoid-config/certs/elastic`.

5. Create a certificate directory for MongoDB.

   ```
   mkdir -p autoid-config/certs/mongo
   ```

6. Copy the MongoDB certificates and JKS files to `autoid-config/certs/mongo`.

7. Create a certificate directory for Cassandra.

   ```
   mkdir -p autoid-config/certs/cassandra
   ```

8. Copy the Cassandra certificates and JKS files to `autoid-config/certs/cassandra`.

9. Update the `hosts` file with the IP addresses of the machines. The `hosts` file must include the IP addresses for Docker nodes, Spark main/livy, and the MongoDB master. While the deployer pro doesn't install or configure the MongoDB main server, the entry is required to run the MongoDB CLI to seed the Ping Autonomous Identity schema.

   ```
   [docker-managers]

   [docker-workers]

   [docker:children]
   docker-managers
   docker-workers

   [spark-master-livy]

   [cassandra-seeds]
   #For replica sets, add the IPs of all Cassandra nodes

   [mongo_master]
   # Add the MongoDB main node in the cluster deployment
   # For example: 10.142.15.248 mongodb_master=True

   [odfe-master-node]
   # Add only the main node in the cluster deployment
   ```

10. Update the `vars.yml` file:

    1. Set `offline_mode` to `true`.

    2. Set `db_driver_type` to `mongo` or `cassandra`.

    3. Set `elastic_host`, `elastic_port`, and `elastic_user` properties.

    4. Set `kibana_host`.

    5. Set the Apache livy install directory.

    6. Ensure the `elastic_user`, `elastic_port`, and `mongo_part` are correctly configured.

    7. Update the `vault.yml` passwords for elastic and mongo to refect your installation.

    8. Set the `mongo_ldap` variable to `true` if you want Ping Autonomous Identity to authenticate with Mongo DB, configured as LDAP.

       |   |                                                                                                                                                                                                                       |
       | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | The `mongo_ldap` variable only appears in fresh installs of 2022.11.0 and its upgrades (2022.11.1+). If you upgraded from a 2021.8.7 deployment, the variable is not available in your upgraded 2022.11.x deployment. |

    9. If you are using Cassandra, set the Cassandra-related parameters in the `vars.yml` file. Default values are:

       ```
       cassandra:
         enable_ssl: "true"
         contact_points: 10.142.15.248 # comma separated values in case of replication set
         port: 9042
         username: zoran_dba
         cassandra_keystore_password: "Acc#1234"
         cassandra_truststore_password: "Acc#1234"
         ssl_client_key_file: "zoran-cassandra-client-key.pem"
         ssl_client_cert_file: "zoran-cassandra-client-cer.pem"
         ssl_ca_file: "zoran-cassandra-server-cer.pem"
         server_truststore_jks: "zoran-cassandra-server-truststore.jks"
         client_truststore_jks: "zoran-cassandra-client-truststore.jks"
         client_keystore_jks: "zoran-cassandra-client-keystore.jks"
       ```

11. Install Apache Livy.

    * The official release of Apache Livy doesn't support Apache Spark 3.3.1 or 3.3.2. Ping Identity has re-compiled and packaged Apache Livy to work with Apache Spark 3.3.1 hadoop 3 and Apache Spark 3.3.2 hadoop 3. Use the zip file located at `autoid-config/apache-livy/apache-livy-0.8.0-incubating-SNAPSHOT-bin.zip` to install Apache Livy on the Spark-Livy machine.

    * For Livy configuration, refer to <https://livy.apache.org/get-started/>.

12. On the Spark-Livy machine, run the following commands to install the python package dependencies:

    1. Change to the `/opt/autoid` directory:

       ```
       cd /opt/autoid
       ```

    2. Create a `requirements.txt` file with the following content:

       ```
       six==1.11
       certifi==2019.11.28
       python-dateutil==2.8.1
       jsonschema==3.2.0
       cassandra-driver
       numpy==1.19.5
       pyarrow==0.16.0
       wrapt==1.11.0
       PyYAML==5.4
       requests==2.31.0
       urllib3==1.26.18
       pymongo
       pandas==1.0.5
       tabulate
       openpyxl
       ```

    3. Install the requirements file:

       ```
       pip3 install -r requirements.txt
       ```

13. Make sure that the `/opt/autoid` directory exists and that it is both readable and writable.

14. Run the deployer script:

    ```
    ./deployer.sh run
    ```

15. On the Spark-Livy machine, run the following commands to install the Python egg file:

    1. Install the egg file:

       ```
       cd /opt/autoid/eggs
       pip3.10 install autoid_analytics-2021.3-py3-none-any.whl
       ```

    2. Source the `.bashrc` file:

       ```
       source ~/.bashrc
       ```

    3. Restart Spark and Livy.

       ```
       ./spark/sbin/stop-all.sh
       ./livy/bin/livy-server stop

       ./spark/sbin/start-all.sh
       ./livy/bin/livy-server start
       ```

## Set the replication factor

Once Cassandra has been deployed, you need to set the replication factor to match the number of nodes on your system. This ensures that each record is stored in each of the nodes. In the event one node is lost, the remaining node can continue to serve content even if the cluster itself is running with reduced redundancy.

Refer to [Set the Replication Factor for Non-Airgap](chap-install-multinode.html#set-replication-factor).

## Resolve Hostname

After installing Ping Autonomous Identity, set up the hostname resolution for your deployment.

1. Configure your DNS servers to access Ping Autonomous Identity dashboard on the target node. The following domain names must resolve to the IP address of the target node:

   ```
   <target-environment>-ui.<domain-name>
   ```

2. If DNS cannot resolve target node hostname, edit it locally on the machine that you want to access Ping Autonomous Identity using a browser.

   Open a text editor and add an entry in the `/etc/hosts` (Linux/Unix) file or `C:\Windows\System32\drivers\etc\hosts` (Windows) for the target node.

   For multi-node, use the Docker Manager node as your target.

   ```
   <Docker Mgr Node Public IP Address>  <target-environment>-ui.<domain-name>
   ```

   For example:

   ```
   <IP Address>  autoid-ui.forgerock.com
   ```

3. If you set up a custom domain name and target environment, add the entries in `/etc/hosts`. For example:

   ```
   <IP Address>  myid-ui.abc.com
   ```

   For more information on customizing your domain name, see [Customize Domains](../admin-guide/chap-customize-domain.html).

## Access the Dashboard

Access the Ping Autonomous Identity console UI:

1. Open a browser. If you set up your own url, use it for your login.

   ```
   https://autoid-ui.forgerock.com/
   ```

2. Log in as a test user.

   ```
   test user: bob.rodgers@forgerock.com
   password: <password>
   ```

## Start the Analytics

If the previous installation steps all succeeded, you must now prepare your data's entity definitions, data sources, and attribute mappings prior to running your analytics jobs. These step are required and are critical for a successful analytics process.

For more information, refer to [Set Entity Definitions](../admin-guide/set-entity-definitions.html).

---

---
title: Install a multi-node deployment
description: This section presents instructions on deploying Ping Autonomous Identity in a multi-node deployment. Multi-node deployments are configured in production environments, providing performant throughput by distributing the processing load across servers and supporting failover redundancy.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-install-multinode
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-install-multinode.html
section_ids:
  summary_of_the_installation_steps: Summary of the installation steps
  prerequisites-multinode: Prerequisites
  setup-nodes-multinode: Set up the nodes
  install-third-party-multinode: Install third-party components
  setup-ssh-deployer-multinode: Set up SSH on the deployer
  set-up-shared-directory: Set up a shared data folder
  install-autoid-multinode: Install Ping Autonomous Identity
  set-replication-factor: Set the Cassandra replication factor
  resolve_hostname: Resolve Hostname
  access_the_dashboard: Access the Dashboard
  check_apache_cassandra: Check Apache Cassandra
  check_mongodb: Check MongoDB
  check_apache_spark: Check Apache Spark
  start_the_analytics: Start the Analytics
---

# Install a multi-node deployment

This section presents instructions on deploying Ping Autonomous Identity in a multi-node deployment. Multi-node deployments are configured in production environments, providing performant throughput by distributing the processing load across servers and supporting failover redundancy.

Like single-node deployment, Ping Identity provides a Deployer Pro script to pull a Docker image from Ping Identity's Google Cloud Registry repository with the microservices and analytics needed for the system. The deployer also uses the node IP addresses specified in your `hosts` file to set up an overlay network and your nodes.

|   |                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The procedures are similar to multinode deployments using older Ping Autonomous Identity release, except that you must install and configure the dependent software packages (for example, Apache Cassandra/MongoDB, Apache Spark and Livy, Opensearch and Opensearch Dashboards, and Docker) prior to running Ping Autonomous Identity. |

## Summary of the installation steps

To set up the 2022.11.12 deployment, run the following steps:

* [Prerequisites](#prerequisites-multinode)

* [Set up the nodes](#setup-nodes-multinode)

* [Install third-party components](#install-third-party-multinode)

* [Set up SSH on the deployer](#setup-ssh-deployer-multinode)

* [Set up a shared data folder](#set-up-shared-directory)

* [Install Ping Autonomous Identity](#install-autoid-multinode)

* [Set the Cassandra replication factor](#set-replication-factor)

## Prerequisites

Deploy Ping Autonomous Identity on a multi-node target on Redhat Linux Enterprise 8 or CentOS Stream 8. The following are prerequisites:

* **Operating System**. The target machine requires Redhat Linux Enterprise 8 or CentOS Stream 8. The deployer machine can use any operating system as long as Docker is installed. For this chapter, we use Redhat Linux Enterprise 8 as its base operating system.

  |   |                                                                                                                                                                                                                          |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you are upgrading Ping Autonomous Identity on a RHEL 7/CentOS 7, the upgrade to 2022.11 uses RHEL 7/CentOS 7 only. For new and clean installations, Ping Autonomous Identity requires RHEL 8 or CentOS Stream 8 only. |

* **Default Shell**. The default shell for the `autoid` user must be `bash`.

* **Subnet Requirements**. We recommend deploying your multi-node machines within the same subnet. Ports must be open for the installation to succeed. Each instance should be able to communicate to the other instances.

  |   |                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If any hosts used for the Docker cluster (docker-managers, docker-workers) have an IP address in the range of 10.0.x.x, they will conflict with the Swarm network. As a result, the services in the cluster will not connect to the Cassandra database or Elasticsearch backend.The Docker cluster hosts must be in a subnet that provides IP addresses 10.10.1.x or higher. |

* **Deployment Requirements**. Ping Autonomous Identity provides a `deployer.sh` script that downloads and installs the necessary Docker images. To download the deployment images, you must first obtain a registry key to sign on to the Ping Google Cloud Registry. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

* **Filesystem Requirements**. Ping Autonomous Identity requires a shared filesystem accessible from the Spark main, Spark worker, analytics hosts, and application layer. The shared filesystem should be mounted at the same mount directory on all of those hosts. If the mount directory for the shared filesystem is different from the default, `/data` , update the `/autoid-config/vars.yml` file to point to the correct directories:

  ```
  analytics_data_dir: /data
  analytics_conf_dif: /data/conf
  ```

* **Architecture Requirements**. Make sure that the Spark main is on a separate node from the Spark workers.

* **Database Requirements**. Decide which database you are using: Apache Cassandra or MongoDB. The configuration procedure is slightly different for each database.

* **Deployment Best-Practice**. The example combines the Opensearch data and Opensearch Dashboards nodes. For best performance in production, dedicate a separate node to Opensearch, data nodes, and Opensearch Dashboards.

* **IPv4 Forwarding**. Many high-security environments run their CentOS-based systems with IPv4 forwarding disabled. However, Docker Swarm doesn't work with a disabled IPv4 forward setting. In such environments, make sure to enable IPv4 forwarding in the file `/etc/sysctl.conf`:

  ```
  net.ipv4.ip_forward=1
  ```

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We recommend that your deployer team have someone with Cassandra expertise. This guide is not sufficient to troubleshoot any issues that may arise. |

## Set up the nodes

Set up three virtual machines.

1. Create a Redhat Linux Enterprise 8 or CentOS Stream 8 virtual machine: N2 4 core and 16 GB. Verify your operating system.

   ```
   sudo cat /etc/centos-release
   ```

   |   |                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For multinode deployments, there is a known issue with RHEL 8/CentOS Stream 8 and overlay network configurations. Refer to [Known Issues in 2022.11.0](../release-notes/changelog.html#known-issues-2022-11-0). |

2. Set the user for the target node to `autoid`. In this example, create user `autoid`:

   ```
   sudo adduser autoid
   sudo passwd autoid
   echo "autoid  ALL=(ALL)  NOPASSWD:ALL" | sudo tee /etc/sudoers.d/autoid
   sudo usermod -aG wheel autoid
   su - autoid
   ```

3. Optional. Install yum-utils package on the deployer machine. yum-utils is a utilities manager for the Yum RPM package repository. The repository compresses software packages for Linux distributions.

   ```
   sudo yum install -y yum-utils
   ```

4. Install the following packages needed in the Ping Autonomous Identity deployment:

   * **Java 11**. For example, `sudo dnf install java-11-openjdk-devel`.

   * **wget**. For example, `sudo dnf install wget`.

   * **unzip**. For example, `sudo dnf install unzip`.

   * **elinks**. For example, `sudo yum install -y elinks`.

   * **Python 3.10.9**. Refer to <https://docs.python.org/release/3.10.9/>.

5. Repeat this procedure for the other nodes.

## Install third-party components

Set up a machine with the required third-party software dependencies. Refer to: [Install third-party components](chap-install-singlenode-target.html#install-third-party).

## Set up SSH on the deployer

1. On the deployer machine, change to the `~/.ssh` directory.

   ```
   cd ~/.ssh
   ```

2. Run `ssh-keygen` to generate an RSA keypair, and then click Enter. You can use the default filename.

   |   |                                                             |
   | - | ----------------------------------------------------------- |
   |   | Do not add a key passphrase as it results in a build error. |

   ```
   ssh-keygen -t rsa -C "autoid"
   ```

   The public and private rsa key pair is stored in `home-directory/.ssh/id_rsa` and `home-directory/.ssh/id_rsa.pub`.

3. Copy the SSH key to the `autoid-config` directory.

   ```
   cp id_rsa ~/autoid-config
   ```

4. Change the privileges to the file.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

5. Copy your public SSH key, `id_rsa.pub`, to each of your nodes.

   |   |                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your target system doesn't have an `~/.ssh/authorized_keys`, create it using `sudo mkdir -p ~/.ssh`, then `sudo touch ~/.ssh/authorized_keys`. |

   For this example, copy the SSH key to each node:

   ```
   ssh-copy-id -i id_rsa.pub autoid@<Node IP Address>
   ```

6. On the deployer machine, test your SSH connection to each target machine. This is a critical step. Make sure the connection works before proceeding with the installation.

   For example, SSH to first node:

   ```
   ssh -i id_rsa autoid@<Node 1 IP Address>

   Last login: Sat Oct 3 03:02:40 2020
   ```

7. If you can successfully SSH to each machine, set the privileges on your `~/.ssh` and `~/.ssh/authorized_keys`.

   ```
   chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
   ```

8. Enter Exit to end your SSH session.

9. Repeat steps 5–8 again for each node.

## Set up a shared data folder

The Docker main and worker nodes plus the analytics main and worker nodes require a shared data directory, typically, `/data`. There are numerous ways to set up a shared directory, the following procedure is just one example and sets up an NFS server on the analytics master.

1. On the Analytics Spark Main node, install `nfs-utils`. This step may require that you run the install with root privileges, such as `sudo` or equivalent.

   ```
   sudo yum install -y nfs-utils
   ```

2. Create the `/data` directory.

   ```
   mkdir -p /data
   ```

3. Change the permissions on the `/data` directory.

   ```
   chmod -R 755 /data
   chown nfsnobody:nfsnobody /data
   ```

4. Start the services and enable them to start at boot.

   ```
   systemctl enable rpcbind
   systemctl enable nfs-server
   systemctl enable nfs-lock
   systemctl enable nfs-idmap

   systemctl start rpcbind
   systemctl start nfs-server
   systemctl start nfs-lock
   systemctl start nfs-idmap
   ```

5. Define the sharing points in the `/etc/exports` file.

   ```
   vi /etc/exports

   /data  <Remote IP Address 1>(rw,sync,no_root_squash,no_all_squash)
   /data  <Remote IP Address 2>(rw,sync,no_root_squash,no_all_squash)
   ```

   If you change the domain name and target environment, you need to also change the certificates to reflect the new changes. For more information, refer to [Customize Domains](../admin-guide/chap-customize-domain.html).

6. Start the NFS service.

   ```
   systemctl restart nfs-server
   ```

7. Add the NFS service to the `firewall-cmd` public zone service:

   ```
   firewall-cmd --permanent --zone=public --add-service=nfs
   firewall-cmd --permanent --zone=public --add-service=mountd
   firewall-cmd --permanent --zone=public --add-service=rpc-bind
   firewall-cmd --reload
   ```

8. On each spark worker node, run the following:

   1. Install `nfs-utils`:

      ```
      yum install -y nfs-utils
      ```

   2. Create the NFS directory mount points:

      ```
      mkdir -p /data
      ```

   3. Mount the NFS shared directory:

      ```
      mount -t nfs <NFS Server IP>:/data /data
      ```

   4. Test the new shared directory by creating a small text file. On an analytics worker node, run the following, and then check for the presence of the test file on the other servers:

      ```
      cd /data
      touch test
      ```

## Install Ping Autonomous Identity

Make sure you have the following prerequisites:

* IP address of machines running Opensearch, MongoDB, or Cassandra.

* The Ping Autonomous Identity user should have permission to write to `/opt/autoid` on all machines

* To download the deployment images for the install, you still need your registry key to log into the Ping Google Cloud Registry to download the artifacts.

* Make sure you have the proper Opensearch certificates with the exact names for both pem and JKS files copied to `~/autoid-config/certs/elastic`:

  * esnode.pem

  * esnode-key.pem

  * root-ca.pem

  * elastic-client-keystore.jks

  * elastic-server-truststore.jks

* Make sure you have the proper MongoDB certificates with exact names for both pem and JKS files copied to `~/autoid-config/certs/mongo`:

  * mongo-client-keystore.jks

  * mongo-server-truststore.jks

  * mongodb.pem

  * rootCA.pem

* Make sure you have the proper Cassandra certificates with exact names for both pem and JKS files copied to \~/autoid-config/certs/cassandra:

  * Zoran-cassandra-client-cer.pem

  * Zoran-cassandra-client-keystore.jks

  * Zoran-cassandra-server-cer.pem

  * zoran-cassandra-server-keystore.jks

  * Zoran-cassandra-client-key.pem

  * Zoran-cassandra-client-truststore.jks

  * Zoran-cassandra-server-key.pem

  * Zoran-cassandra-server-truststore.jks

Install Ping Autonomous Identity:

1. Create the `autoid-config` directory.

   ```
   mkdir autoid-config
   ```

2. Change to the directory.

   ```
   cd autoid-config
   ```

3. Sign on to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

   ```
   docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
   ```

   The following output is displayed:

   ```
   Login Succeeded
   ```

4. Run the create-template command to generate the `deployer.sh` script wrapper and configuration files. Note that the command sets the configuration directory on the target node to `/config`. The `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

   ```
   docker run --user=$(id -u) -v ~/autoid-config:/config -it gcr.io/forgerock-autoid/deployer-pro:2022.11.12 create-template
   ```

5. Create a certificate directory for elastic.

   ```
   mkdir -p autoid-config/certs/elastic
   ```

6. Copy the Opensearch certificates and JKS files to `autoid-config/certs/elastic`.

7. Create a certificate directory for MongoDB.

   ```
   mkdir -p autoid-config/certs/mongo
   ```

8. Copy the MongoDB certificates and JKS files to `autoid-config/certs/mongo`.

9. Create a certificate directory for Cassandra.

   ```
   mkdir -p autoid-config/certs/cassandra
   ```

10. Copy the Cassandra certificates and JKS files to `autoid-config/certs/cassandra`.

11. Update the `hosts` file with the IP addresses of the machines. The `hosts` file must include the IP addresses for Docker nodes, Spark main/livy, and the MongoDB master. While the deployer pro doesn't install or configure the MongoDB main server, the entry is required to run the MongoDB CLI to seed the Ping Autonomous Identity schema.

    ```
    [docker-managers]

    [docker-workers]

    [docker:children]
    docker-managers
    docker-workers

    [spark-master-livy]

    [cassandra-seeds]
    #For replica sets, add the IPs of all Cassandra nodes

    [mongo_master]
    # Add the MongoDB main node in the cluster deployment
    # For example: 10.142.15.248 mongodb_master=True

    [odfe-master-node]
    # Add only the main node in the cluster deployment
    ```

12. Update the `vars.yml` file:

    1. Set `db_driver_type` to `mongo` or `cassandra`.

    2. Set `elastic_host`, `elastic_port`, and `elastic_user` properties.

    3. Set `kibana_host`.

    4. Set the Apache livy install directory.

    5. Ensure the `elastic_user`, `elastic_port`, and `mongo_part` are correctly configured.

    6. Update the `vault.yml` passwords for elastic and mongo to refect your installation.

    7. Set the `mongo_ldap` variable to `true` if you want Ping Autonomous Identity to authenticate with Mongo DB, configured as LDAP.

       |   |                                                                                                                                                                                                                       |
       | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | The `mongo_ldap` variable only appears in fresh installs of 2022.11.0 and its upgrades (2022.11.1+). If you upgraded from a 2021.8.7 deployment, the variable is not available in your upgraded 2022.11.x deployment. |

    8. If you are using Cassandra, set the Cassandra-related parameters in the `vars.yml` file. Default values are:

       ```
       cassandra:
         enable_ssl: "true"
         contact_points: 10.142.15.248 # comma separated values in case of replication set
         port: 9042
         username: zoran_dba
         cassandra_keystore_password: "Acc#1234"
         cassandra_truststore_password: "Acc#1234"
         ssl_client_key_file: "zoran-cassandra-client-key.pem"
         ssl_client_cert_file: "zoran-cassandra-client-cer.pem"
         ssl_ca_file: "zoran-cassandra-server-cer.pem"
         server_truststore_jks: "zoran-cassandra-server-truststore.jks"
         client_truststore_jks: "zoran-cassandra-client-truststore.jks"
         client_keystore_jks: "zoran-cassandra-client-keystore.jks"
       ```

13. Download images:

    ```
    ./deployer.sh download-images
    ```

14. Install Apache Livy.

    * The official release of Apache Livy doesn't support Apache Spark 3.3.1 or 3.3.2. Ping Identity has re-compiled and packaged Apache Livy to work with Apache Spark 3.3.1 hadoop 3 and Apache Spark 3.3.2 hadoop 3. Use the zip file located at `autoid-config/apache-livy/apache-livy-0.8.0-incubating-SNAPSHOT-bin.zip` to install Apache Livy on the Spark-Livy machine.

    * For Livy configuration, refer to <https://livy.apache.org/get-started/>.

15. On the Spark-Livy machine, run the following commands to install the python package dependencies:

    1. Change to the `/opt/autoid` directory:

       ```
       cd /opt/autoid
       ```

    2. Create a `requirements.txt` file with the following content:

       ```
       six==1.11
       certifi==2019.11.28
       python-dateutil==2.8.1
       jsonschema==3.2.0
       cassandra-driver
       numpy==1.22.0
       pyarrow==6.0.1
       wrapt==1.11.0
       PyYAML==6.0
       requests==2.31.0
       urllib3==1.26.18
       pymongo
       pandas==1.3.5
       tabulate
       openpyxl
       wheel
       cython
       ```

    3. Install the requirements file:

       ```
       pip3 install -r requirements.txt
       ```

16. Make sure that the `/opt/autoid` directory exists and that it is both readable and writable.

17. Run the deployer script:

    ```
    ./deployer.sh run
    ```

18. On the Spark-Livy machine, run the following commands to install the Python egg file:

    1. Install the egg file:

       ```
       cd /opt/autoid/eggs
       pip3.10 install autoid_analytics-2021.3-py3-none-any.whl
       ```

    2. Source the `.bashrc` file:

       ```
       source ~/.bashrc
       ```

    3. Restart Spark and Livy.

       ```
       ./spark/sbin/stop-all.sh
       ./livy/bin/livy-server stop

       ./spark/sbin/start-all.sh
       ./livy/bin/livy-server start
       ```

## Set the Cassandra replication factor

Once Cassandra has been deployed, you need to set the replication factor to match the number of nodes on your system. This ensures that each record is stored in each of the nodes. In the event one node is lost, the remaining node can continue to serve content even if the cluster itself is running with reduced redundancy.

You can define replication on a per keyspace-basis as follows:

1. Start the Cassandra shell, `cqlsh`, and define the `autoid` keyspace. Change the replication factor to match the number of seed nodes. The default admin user for Cassandra is `zoran_dba`.

   ```
   bin/cqlsh -u zoran_dba

   zoran_dba@cqlsh> desc keyspace autoid;
   CREATE KEYSPACE autoid WITH replication = {'class':'SimpleStrategy','replication_factor':'2'} AND durable_writes=true;

   CREATE TABLE autoid.user_access_decisions_history(
     user text,
     entitlement text,
     date_created timestamp,
     …​
   ```

2. Restart Cassandra on this node.

3. Repeat these steps on the other Cassandra seed node(s).

## Resolve Hostname

After installing Ping Autonomous Identity, set up the hostname resolution for your deployment.

1. Configure your DNS servers to access Ping Autonomous Identity dashboard on the target node. The following domain names must resolve to the IP address of the target node:

   ```
   <target-environment>-ui.<domain-name>
   ```

2. If DNS cannot resolve target node hostname, edit it locally on the machine that you want to access Ping Autonomous Identity using a browser.

   Open a text editor and add an entry in the `/etc/hosts` (Linux/Unix) file or `C:\Windows\System32\drivers\etc\hosts` (Windows) for the target node.

   For multi-node, use the Docker Manager node as your target.

   ```
   <Docker Mgr Node Public IP Address>  <target-environment>-ui.<domain-name>
   ```

   For example:

   ```
   <IP Address>  autoid-ui.forgerock.com
   ```

3. If you set up a custom domain name and target environment, add the entries in `/etc/hosts`. For example:

   ```
   <IP Address>  myid-ui.abc.com
   ```

   For more information on customizing your domain name, see [Customize Domains](../admin-guide/chap-customize-domain.html).

## Access the Dashboard

Access the Ping Autonomous Identity console UI:

1. Open a browser. If you set up your own url, use it for your login.

   ```
   https://autoid-ui.forgerock.com/
   ```

2. Log in as a test user.

   ```
   test user: bob.rodgers@forgerock.com
   password: <password>
   ```

## Check Apache Cassandra

Check Cassandra:

1. Make sure Cassandra is running in cluster mode. For example

   ```
   /opt/autoid/apache-cassandra-3.11.2/bin/nodetool status
   ```

## Check MongoDB

Check MongoDB:

1. Make sure MongoDB is running. For example:

   ```
   mongo --tls \
   --host <Host IP> \
   --tlsCAFile /opt/autoid/mongo/certs/rootCA.pem  \
   --tlsAllowInvalidCertificates  \
   --tlsCertificateKeyFile /opt/autoid/mongo/certs/mongodb.pem
   ```

## Check Apache Spark

Check Spark:

1. SSH to the target node and open Spark dashboard using the bundled text-mode web browser

   ```
   elinks http://localhost:8080
   ```

   Spark Master status should display as ALIVE and worker(s) with State ALIVE.

   > **Collapse: Click to display an example of the Spark dashboard**
   >
   > ![Spark Dashboard](_images/spark-dashboard.png)

## Start the Analytics

If the previous installation steps all succeeded, you must now prepare your data's entity definitions, data sources, and attribute mappings prior to running your analytics jobs. These step are required and are critical for a successful analytics process.

For more information, refer to [Set Entity Definitions](../admin-guide/set-entity-definitions.html).

---

---
title: Install a single node air-gapped deployment
description: This section presents instructions on deploying Ping Autonomous Identity in a single-node target machine that has no Internet connectivity. This type of configuration, called an air-gap or offline deployment, provides enhanced security by isolating itself from outside Internet or network access.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-install-singlenode-airgap
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-install-singlenode-airgap.html
section_ids:
  installation_steps_for_an_airgap_deployment: Installation steps for an airgap deployment
  setup-nodes-singlenode-airgap: Set up the nodes
  setup-third-party-airgap: Set up the third-party software dependencies
  setup-ssh-deployer-airgap: Set up SSH on the deployer
  prepare-tar-airgap: Prepare the tar file
  install-from-air-gap-target: Install on the air-gap target
  install-autoid-singlenode-airgap: Install Ping Autonomous Identity
  resolve_hostname: Resolve Hostname
  access_the_dashboard: Access the Dashboard
  check_apache_cassandra: Check Apache Cassandra
  check_mongodb: Check MongoDB
  check_apache_spark: Check Apache Spark
  start_the_analytics: Start the Analytics
---

# Install a single node air-gapped deployment

This section presents instructions on deploying Ping Autonomous Identity in a single-node target machine that has no Internet connectivity. This type of configuration, called an *air-gap* or *offline* deployment, provides enhanced security by isolating itself from outside Internet or network access.

The air-gap installation is similar to that of the single-node target deployment with Internet connectivity, except that the image and deployer script must be saved on a portable drive and copied to the air-gapped target machine.

![Ping Autonomous Identity deployed in a single-node air-gapped target deployment](_images/auto-id-singlenode-airgap.png)Figure 1. A single-node air-gapped target deployment.

## Installation steps for an airgap deployment

The general procedure for an air-gap deployment is practically identical to that of a single node non-airgapped, except that you must prepare a tar file and copy the files to an air-gap machine.

* [Set up the nodes](#setup-nodes-singlenode-airgap)

* [Set up the third-party software dependencies](#setup-third-party-airgap)

* [Set up SSH on the deployer](#setup-ssh-deployer-airgap)

* [Prepare the tar file](#prepare-tar-airgap)

* [Install Ping Autonomous Identity](#install-autoid-singlenode-airgap)

## Set up the nodes

Set up each node as presented in [Install a single node deployment](chap-install-singlenode-target.html).

Make sure you have sufficient storage for your particular deployment. For more information on sizing considerations, refer to [Deployment Planning Guide](../deployment-planning/chap-topology-planning.html).

## Set up the third-party software dependencies

Download and unpack the third-party software dependencies in [Install third-party components](chap-install-singlenode-target.html#install-third-party).

## Set up SSH on the deployer

While SSH is not necessary to connect the deployer to the target node as the machines are isolated from one another. You still need SSH on the deployer so that it can communicate with itself.

1. On the deployer machine, run `ssh-keygen` to generate an RSA keypair, and then click Enter. You can use the default filename. Enter a password for protecting your private key.

   ```
   ssh-keygen -t rsa -C "autoid"
   ```

   The public and private rsa key pair is stored in `home-directory/.ssh/id_rsa` and `home-directory/.ssh/id_rsa.pub`.

2. Copy the SSH key to the `~/autoid-config` directory.

   ```
   cp ~/.ssh/id_rsa ~/autoid-config
   ```

3. Change the privileges to the file.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

## Prepare the tar file

Run the following steps on an Internet-connected host machine:

1. On the deployer machine, change to the installation directory.

   ```
   cd ~/autoid-config/
   ```

2. Sign on to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

   ```
   docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
   ```

   The following output is displayed:

   ```
   Login Succeeded
   ```

3. Run the `create-template` command to generate the `deployer.sh` script wrapper. The command sets the configuration directory on the target node to `/config`. Note that the `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

   ```
   docker run --user=$(id -u) -v ~/autoid-config:/config -it gcr.io/forgerock-autoid/deployer-pro:2022.11.12 create-template
   ```

4. Open the `~/autoid-config/vars.yml` file, set the `offline_mode` property to `true`, and then save the file.

   ```
   offline_mode: true
   ```

5. Download the Docker images. This step downloads software dependencies needed for the deployment and places them in the `autoid-packages` directory.

   ```
   ./deployer.sh download-images
   ```

6. Create a tar file containing all of the Ping Autonomous Identity binaries.

   ```
   tar czf autoid-packages.tgz deployer.sh autoid-packages/*
   ```

7. Copy the `autoid-packages.tgz` , `deployer.sh` , and SSH key (`id_rsa` ) to a portable hard drive.

## Install on the air-gap target

Before you begin, make sure you have CentOS Stream 8 and Docker installed on your air-gapped target machine.

1. Create the `~/autoid-config` directory if you haven't already.

   ```
   mkdir ~/autoid-config
   ```

2. Copy the `autoid-package.tgz` tar file from the portable storage device.

3. Unpack the tar file.

   ```
   tar xf autoid-packages.tgz -C ~/autoid-config
   ```

4. On the air-gap host node, copy the SSH key to the `~/autoid-config` directory.

5. Change the privileges to the file.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

6. Change to the configuration directory.

   ```
   cd ~/autoid-config
   ```

7. Import the deployer image.

   ```
   ./deployer.sh import-deployer
   ```

   The following output is displayed:

   ```
   …​
   db631c8b06ee: Loading layer [=============================================⇒]   2.56kB/2.56kB
   2d62082e3327: Loading layer [=============================================⇒]  753.2kB/753.2kB
   Loaded image: gcr.io/forgerock-autoid/deployer:2022.11.12
   ```

8. Create the configuration template using the `create-template` command. This command creates the configuration files: `ansible.cfg` , `vars.yml` , `vault.yml` and `hosts`.

   ```
   ./deployer.sh create-template
   ```

   The following output is displayed:

   ```
   Config template is copied to host machine directory mapped to /config
   ```

## Install Ping Autonomous Identity

Make sure you have the following prerequisites:

* IP address of machines running Opensearch, MongoDB, or Cassandra.

* The Ping Autonomous Identity user should have permission to write to `/opt/autoid` on all machines

* To download the deployment images for the install, you still need your registry key to log into the Ping Google Cloud Registry to download the artifacts.

* Make sure you have the proper Opensearch certificates with the exact names for both pem and JKS files copied to `~/autoid-config/certs/elastic`:

  * esnode.pem

  * esnode-key.pem

  * root-ca.pem

  * elastic-client-keystore.jks

  * elastic-server-truststore.jks

* Make sure you have the proper MongoDB certificates with exact names for both pem and JKS files copied to `~/autoid-config/certs/mongo`:

  * mongo-client-keystore.jks

  * mongo-server-truststore.jks

  * mongodb.pem

  * rootCA.pem

* Make sure you have the proper Cassandra certificates with exact names for both pem and JKS files copied to \~/autoid-config/certs/cassandra:

  * Zoran-cassandra-client-cer.pem

  * Zoran-cassandra-client-keystore.jks

  * Zoran-cassandra-server-cer.pem

  * zoran-cassandra-server-keystore.jks

  * Zoran-cassandra-client-key.pem

  * Zoran-cassandra-client-truststore.jks

  * Zoran-cassandra-server-key.pem

  * Zoran-cassandra-server-truststore.jks

Install Ping Autonomous Identity:

1. Create a certificate directory for elastic.

   ```
   mkdir -p autoid-config/certs/elastic
   ```

2. Copy the Opensearch certificates and JKS files to `autoid-config/certs/elastic`.

3. Create a certificate directory for MongoDB.

   ```
   mkdir -p autoid-config/certs/mongo
   ```

4. Copy the MongoDB certificates and JKS files to `autoid-config/certs/mongo`.

5. Create a certificate directory for Cassandra.

   ```
   mkdir -p autoid-config/certs/cassandra
   ```

6. Copy the Cassandra certificates and JKS files to `autoid-config/certs/cassandra`.

7. Update the `hosts` file with the IP addresses of the machines. The `hosts` file must include the IP addresses for Docker nodes, Spark main/livy, and the MongoDB master. While the deployer pro doesn't install or configure the MongoDB main server, the entry is required to run the MongoDB CLI to seed the Ping Autonomous Identity schema.

   ```
   [docker-managers]

   [docker-workers]

   [docker:children]
   docker-managers
   docker-workers

   [spark-master-livy]

   [cassandra-seeds]
   #For replica sets, add the IPs of all Cassandra nodes

   [mongo_master]
   # Add the MongoDB main node in the cluster deployment
   # For example: 10.142.15.248 mongodb_master=True

   [odfe-master-node]
   # Add only the main node in the cluster deployment
   ```

8. Update the `vars.yml` file:

   1. Set `offline_mode` to `true`.

   2. Set `db_driver_type` to `mongo` or `cassandra`.

   3. Set `elastic_host`, `elastic_port`, and `elastic_user` properties.

   4. Set `kibana_host`.

   5. Set the Apache livy install directory.

   6. Ensure the `elastic_user`, `elastic_port`, and `mongo_part` are correctly configured.

   7. Update the `vault.yml` passwords for elastic and mongo to refect your installation.

   8. Set the `mongo_ldap` variable to `true` if you want Ping Autonomous Identity to authenticate with Mongo DB, configured as LDAP.

      |   |                                                                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The `mongo_ldap` variable only appears in fresh installs of 2022.11.0 and its upgrades (2022.11.1+). If you upgraded from a 2021.8.7 deployment, the variable is not available in your upgraded 2022.11.x deployment. |

   9. If you are using Cassandra, set the Cassandra-related parameters in the `vars.yml` file. Default values are:

      ```
      cassandra:
        enable_ssl: "true"
        contact_points: 10.142.15.248 # comma separated values in case of replication set
        port: 9042
        username: zoran_dba
        cassandra_keystore_password: "Acc#1234"
        cassandra_truststore_password: "Acc#1234"
        ssl_client_key_file: "zoran-cassandra-client-key.pem"
        ssl_client_cert_file: "zoran-cassandra-client-cer.pem"
        ssl_ca_file: "zoran-cassandra-server-cer.pem"
        server_truststore_jks: "zoran-cassandra-server-truststore.jks"
        client_truststore_jks: "zoran-cassandra-client-truststore.jks"
        client_keystore_jks: "zoran-cassandra-client-keystore.jks"
      ```

9. Install Apache Livy.

   * The official release of Apache Livy doesn't support Apache Spark 3.3.1 or 3.3.2. Ping Identity has re-compiled and packaged Apache Livy to work with Apache Spark 3.3.1 hadoop 3 and Apache Spark 3.3.2 hadoop 3. Use the zip file located at `autoid-config/apache-livy/apache-livy-0.8.0-incubating-SNAPSHOT-bin.zip` to install Apache Livy on the Spark-Livy machine.

   * For Livy configuration, refer to <https://livy.apache.org/get-started/>.

10. On the Spark-Livy machine, run the following commands to install the python package dependencies:

    1. Change to the `/opt/autoid` directory:

       ```
       cd /opt/autoid
       ```

    2. Create a `requirements.txt` file with the following content:

       ```
       six==1.11
       certifi==2019.11.28
       python-dateutil==2.8.1
       jsonschema==3.2.0
       cassandra-driver
       numpy==1.22.0
       pyarrow==6.0.1
       wrapt==1.11.0
       PyYAML==6.0
       requests==2.31.0
       urllib3==1.26.18
       pymongo
       pandas==1.3.5
       tabulate
       openpyxl
       wheel
       cython
       ```

    3. Install the requirements file:

       ```
       pip3 install -r requirements.txt
       ```

11. Make sure that the `/opt/autoid` directory exists and that it is both readable and writable.

12. Run the deployer script:

    ```
    ./deployer.sh run
    ```

13. On the Spark-Livy machine, run the following commands to install the Python egg file:

    1. Install the egg file:

       ```
       cd /opt/autoid/eggs
       pip3.10 install autoid_analytics-2021.3-py3-none-any.whl
       ```

    2. Source the `.bashrc` file:

       ```
       source ~/.bashrc
       ```

    3. Restart Spark and Livy.

       ```
       ./spark/sbin/stop-all.sh
       ./livy/bin/livy-server stop

       ./spark/sbin/start-all.sh
       ./livy/bin/livy-server start
       ```

## Resolve Hostname

After installing Ping Autonomous Identity, set up the hostname resolution for your deployment.

Resolve the hostname:

1. Configure your DNS servers to access Ping Autonomous Identity dashboard on the target node. The following domain names must resolve to the IP address of the target node: `<target-environment>-ui.<domain-name>`.

2. If DNS cannot resolve target node hostname, edit it locally on the machine that you want to access Ping Autonomous Identity using a browser. Open a text editor and add an entry in the `/etc/hosts` (Linux/Unix) file or `C:\Windows\System32\drivers\etc\hosts` (Windows) for the self-service and UI services for each managed target node.

   ```
   <Target IP Address>  <target-environment>-ui.<domain-name>
   ```

   For example:

   ```
   34.70.190.144  autoid-ui.forgerock.com
   ```

3. If you set up a custom domain name and target environment, add the entries in `/etc/hosts`. For example:

   ```
   34.70.190.144  myid-ui.abc.com
   ```

   For more information on customizing your domain name, refer to [Customize Domains](../admin-guide/chap-customize-domain.html).

## Access the Dashboard

Access the Ping Autonomous Identity console UI:

1. Open a browser. If you set up your own url, use it for your login.

   ```
   https://autoid-ui.forgerock.com/
   ```

2. Log in as a test user.

   ```
   test user: bob.rodgers@forgerock.com
   password: <password>
   ```

## Check Apache Cassandra

Check Cassandra:

1. Make sure Cassandra is running in cluster mode. For example

   ```
   /opt/autoid/apache-cassandra-3.11.2/bin/nodetool status
   ```

## Check MongoDB

Check MongoDB:

1. Make sure MongoDB is running. For example:

   ```
   mongo --tls \
   --host <Host IP> \
   --tlsCAFile /opt/autoid/mongo/certs/rootCA.pem  \
   --tlsAllowInvalidCertificates  \
   --tlsCertificateKeyFile /opt/autoid/mongo/certs/mongodb.pem
   ```

## Check Apache Spark

Check Spark:

1. SSH to the target node and open Spark dashboard using the bundled text-mode web browser

   ```
   elinks http://localhost:8080
   ```

   Spark Master status should display as ALIVE and worker(s) with State ALIVE.

   > **Collapse: Click to display an example of the Spark dashboard**
   >
   > ![Spark Dashboard](_images/spark-dashboard.png)

## Start the Analytics

If the previous installation steps all succeeded, you must now prepare your data's entity definitions, data sources, and attribute mappings prior to running your analytics jobs. These step are required and are critical for a successful analytics process.

For more information, refer to [Set Entity Definitions](../admin-guide/set-entity-definitions.html).

---

---
title: Install a single node deployment
description: This section presents instructions on deploying Ping Autonomous Identity in a single-target machine with Internet connectivity.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-install-singlenode-target
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-install-singlenode-target.html
section_ids:
  summary_of_the_installation_steps: Summary of the installation steps
  prerequisites-singlenode: Prerequisites
  install-third-party: Install third-party components
  setup-ssh-deployer: Set up SSH on the deployer
  install-autoid: Install Ping Autonomous Identity
  resolve_hostname: Resolve Hostname
  access_the_dashboard: Access the Dashboard
  check_apache_cassandra: Check Apache Cassandra
  check_mongodb: Check MongoDB
  check_apache_spark: Check Apache Spark
  start_the_analytics: Start the Analytics
---

# Install a single node deployment

This section presents instructions on deploying Ping Autonomous Identity in a single-target machine with Internet connectivity.

![Ping Autonomous Identity deployed in a single-node target deployment](_images/auto-id-singlenode.png)Figure 1. A single-node target deployment.

Autonomous Identity 2022.11.0 introduced a new installation script, *deployer pro* (**Deployer** for **Pro**duction), letting customers manage their third-party software dependencies in their particular Ping Autonomous Identity environments. Ping Autonomous Identity 2022.11.12 continues to use this deployer script. For background information about the deployer, refer to [About the new deployer pro script](https://backstage.forgerock.com/docs/autonomous-identity/2022.11.0/install-guide/chap-install-singlenode-target.html#about_the_new_deployer_pro_script).

|   |                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The procedures presented in this section are generalized examples to help you get acquainted with Ping Autonomous Identity. Consult with your Ping Identity Professional Services or technical partner for specific assistance to install Ping Autonomous Identity within your particular environment. |

## Summary of the installation steps

To set up the 2022.11.12 deployment, run the following steps:

* [Prerequisites](#prerequisites-singlenode)

* [Install third-party components](#install-third-party)

* [Set up SSH on the deployer](#setup-ssh-deployer)

* [Install Ping Autonomous Identity](#install-autoid)

## Prerequisites

For new and clean deployments, the following are prerequisites:

* **Operating System**. The target machine requires Red Hat Linux 8/CentOS Stream 8. The deployer machine can use any operating system as long as Docker is installed. For this chapter, we use CentOS Stream 8 as its base operating system.

  |   |                                                                                                                                                                                                                          |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you are upgrading Ping Autonomous Identity on a RHEL 7/CentOS 7, the upgrade to 2022.11 uses RHEL 7/CentOS 7 only. For new and clean installations, Ping Autonomous Identity requires RHEL 8 or CentOS Stream 8 only. |

* **Memory Requirements**. Make sure you have enough free disk space on the deployer machine before running the `deployer.sh` commands. We recommend at least 500GB.

* **Default Shell**. The default shell for the `autoid` user must be bash.

* **Deployment Requirements**. Ping Autonomous Identity provides a Docker image that creates a `deployer.sh` script. The script downloads additional images necessary for the installation. To download the deployment images, you must first obtain a registry key to sign on to the Ping Google Cloud Registry. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

* **Database Requirements**. Decide which database you are using: Apache Cassandra or MongoDB.

* **IPv4 Forwarding**. Many high security environments run their CentOS-based systems with IPv4 forwarding disabled. However, Docker Swarm doesn't work with a disabled IPv4 forward setting. In such environments, make sure to enable IPv4 forwarding in the file `/etc/sysctl.conf`:

  ```
  net.ipv4.ip_forward=1
  ```

## Install third-party components

First, set up your GCP virtual machine and install the third-party package dependencies required for the Ping Autonomous Identity deployment:

Install third-party packages:

1. Create a GCP Red Hat Enterprise Linux (RHEL) 8 or CentOS Stream 8 virtual machine: n2-standard-4 (4 vCPU and 16GB memory). Refer to <https://www.centos.org/centos-stream/>.

2. Create an `autoid` user with the proper privileges to run the installation. For example:

   ```
   sudo adduser autoid
   sudo passwd autoid
   echo "autoid ALL=(ALL)  NOPASSWD:ALL" | sudo tee /etc/sudoers.d/autoid
   sudo usermod -aG wheel autoid
   su - autoid
   ```

3. Install the following packages needed in the Ping Autonomous Identity deployment:

   * **Java 11**. For example, `sudo dnf install java-11-openjdk-devel`.

   * **wget**. For example, `sudo dnf install wget`.

   * **unzip**. For example, `sudo dnf install unzip`.

   * **elinks**. For example, `sudo yum install -y elinks`.

4. Install Python 3.10.9.

   1. Refer to <https://docs.python.org/release/3.10.9/>.

   2. Make sure no other Python versions are installed on the machine. Remove those versions. For example:

      ```
      sudo rm -rf /usr/bin/python3
      sudo rm -rf /usr/bin/python3.6
      sudo rm -rf /usr/bin/python3m
      sudo rm -rf /usr/bin/pip3
      sudo rm -rf /usr/bin/easy_install-3
      sudo rm -rf /usr/bin/easy_install-3.6
      ```

   3. Create symlinks for python3:

      ```
      sudo ln -s /usr/bin/python 3.10 /usr/bin/python3
      sudo ln -s /usr/bin/eash_install-3.10 /usr/bin/easy_install-3
      sudo ln -s /usr/bin/pip3.10 /usr/bin/pip3
      ```

5. Install Cassandra 4.0.6. Refer to <https://cassandra.apache.org/doc/latest/cassandra/getting_started/index.html>. (For MongoDB installations, follow the instructions in [Download MongoDB](#download-mongodb).)

   1. Sign on to the Cassandra shell. For example:

      ```
      cassandra/bin/cqlsh <$ipaddress> -u cassandra -p cassandra
      ```

   2. Create the Cassandra roles for Ping Autonomous Identity. Refer to <https://cassandra.apache.org/doc/latest/cassandra/cql/security.html>. For example:

      ```
      cassandra/bin/cqlsh <$ipaddress> -u cassandra -p cassandra -e "CREATE ROLE zoran_dba WITH PASSWORD = 'password' AND SUPERUSER = true AND LOGIN = true;"
      cassandra/bin/cqlsh <$ipaddress> -u cassandra -p cassandra -e "CREATE ROLE zoranuser WITH PASSWORD = ''password' AND LOGIN = true;"
      cassandra/bin/cqlsh <$ipaddress> -u zoran_dba -p 'password -e "ALTER ROLE cassandra WITH PASSWORD='randompassword123' AND SUPERUSER=false AND LOGIN = false;"
      cassandra/bin/cqlsh <$ipaddress> -u zoran_dba -p 'password -e "ALTER KEYSPACE "system_auth" WITH REPLICATION = {'class' :'NetworkTopologyStrategy','datacenter1' : 1};"
      ```

   3. Configure security for Cassandra. Refer to <https://cassandra.apache.org/doc/latest/cassandra/operating/security.html>.

6) Install MongoDB 4.4. Follow the instructions in <https://www.mongodb.com/docs/v4.4/tutorial/install-mongodb-on-red-hat/>.

   1. Create a MongoDB user with username `mongoadmin` with admin privileges. Follow the instructions in <https://www.mongodb.com/docs/v4.4/core/security-users/>.

      For example:

      ```
      db.createUser({ user: "mongoadmin",pwd: "~@C~O>@%^()-_+=|<Y*$$rH&&/m#g{?-o!z/1}2??3=!*&", roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]})
      ```

   2. Set up SSL, refer to <https://www.mongodb.com/docs/v4.4/tutorial/configure-ssl/#procedures—​using-net.ssl-settings>. For example, the MongoDB configuration file (`/etc/mongod.conf`) would include a section similar to the following:

      ```
      net:
         tls:
            mode: requireTLS
            certificateKeyFile: /etc/ssl/mongodb.pem
            CAFile: /etc/ssl/rootCA.pem
      ```

      * IMPORTANT

        Make sure that the CN entry in the `mongodb.pem` certificate is the IP address/hostname of the `mongodb` instance. You need to add this same CN value to the `hosts` file during the Ping Autonomous Identity deployment.

   3. Restart the daemon and MongoDB.

      ```
      sudo systemctl daemon-reload
      sudo systemctl restart mongod
      ```

7) Install Apache Spark 3.3.2. Refer to <https://spark.apache.org/downloads.html>.

   |   |                                                                                                                                                                                                                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The official release of Apache Livy doesn't support Apache Spark 3.3.1 or 3.3.2. Ping Identity has re-compiled and packaged Apache Livy to work with Apache Spark 3.3.1 hadoop 3 and Apache Spark 3.3.2 hadoop 3. Use the zip file located at `autoid-config/apache-livy/apache-livy-0.8.0-incubating-SNAPSHOT-bin.zip` to install Apache Livy on the Spark-Livy machine. |

   1. Configure the `SPARK_HOME` in your `bashrc` file. For example:

      ```
      SPARK_HOME=/opt/spark/spark-3.3.2-bin-hadoop3
      export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
      ```

   2. Configure authentication on Spark, refer to <https://spark.apache.org/docs/latest/security.html#authentication>. For example:

      ```
      spark.authenticate          true
      spark.authenticate.secret   <your-secret>
      ```

   3. Enable and start the Spark main and secondary servers:

      ```
      sudo chown -R $USER:USER $SPARK_HOME
      ```

   4. Spark 3.3.1 and 3.3.2 no longer uses log4j1 and has upgraded to log4j2. Copy or move the log4j template file to the `log4j2.properties` file. For example:

      ```
      mv /opt/spark/spark-3.3.2-bin-hadoop3/conf/log4j.properties.template /opt/spark/spark-3.3.2-bin-hadoop3/conf/log4j2.properties
      ```

      |   |                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------- |
      |   | You will install Apache Livy in a later step. Refer to [Install Apache Livy](#install-apache-livy). |

8) Install Opensearch 1.3.14 and Opensearch Dashboards 1.3.14. For more information, refer to [Opensearch 1.3.14](https://opensearch.org/versions/opensearch-1-3-14.html).

   1. Configure Opensearch Dashboards using the `/Opensearch-dashboards/config/Opensearch_dashboards.yml` file. Refer to <https://Opensearch.org/docs/1.3/dashboards/install/index/>.

   2. Configure TLS/SSL security:

      * Follow the instructions in <https://Opensearch.org/docs/latest/security-plugin/configuration/tls/>.

      * Follow the instructions in <https://Opensearch.org/docs/2.0/security-plugin/configuration/generate-certificates/>.

        * IMPORTANT

          Make sure that the CN entry in the `esnode.pem` certificate is the IP address/hostname of the Opensearch instance. You need to add this same CN value to the `hosts` file during the Ping Autonomous Identity deployment.

9) Set up Docker using the procedures in <https://docs.docker.com/engine/install/centos/>.

   * For post-installation Docker steps, follow the instructions in <https://docs.docker.com/engine/install/linux-postinstall/>.

     |   |                                                                                                                                                                |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Do not use `/opt/autoid` as Docker root as the directory is overwritten during the Ping Autonomous Identity installation and will result in a recursive error. |

## Set up SSH on the deployer

This section shows how to set up SSH keys for the `autoid` user to the target machine. This is a critical step and necessary for a successful deployment.

1. On the deployer machine, change to the SSH directory.

   ```
   cd ~/.ssh
   ```

2. Run `ssh-keygen` to generate a 2048-bit RSA keypair for the `autoid` user, and then click Enter. Use the default settings, and do not enter a passphrase for your private key.

   ```
   ssh-keygen -t rsa -C "autoid"
   ```

   The public and private rsa key pair is stored in `home-directory/.ssh/id_rsa` and `home-directory/.ssh/id_rsa.pub`.

3. Copy the SSH key to the `autoid-config` directory.

   ```
   cp id_rsa ~/autoid-config
   ```

4. Change the privileges and owner to the file.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

5. Copy your public SSH key, `id_rsa.pub` , to the target machine's `~/.ssh/authorized_keys` folder. If your target system doesn't have an `~/.ssh/authorized_keys`, create it using `sudo mkdir -p ~/.ssh`, then `sudo touch ~/.ssh/authorized_keys`.

   This example uses `ssh-copy-id` to copy the public key to the target machine, which may or may not be available on your operating system. You can also manually copy-n-paste the public key to your `~/.ssh/authorized_keys` on the target machine.

   ```
   ssh-copy-id -i id_rsa.pub autoid@<Target IP Address>
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The `ssh-copy-id` command requires that you have public key authentication enabled on the target server. You can enable it by editing the `/etc/ssh/sshd_config` file on the target machine. For example: **sudo vi /etc/ssh/sshd\_config**, set **PubkeyAuthentication yes**, and save the file. Next, restart sshd: **sudo systemctl restart sshd**. |

6. On the deployer machine, test your SSH connection to the target machine. This is a critical step. Make sure the connection works before proceeding with the installation.

   ```
   ssh -i ~/.ssh/id_rsa autoid@<Target IP Address>

   Last login: Tue Dec 14 14:06:06 2020
   ```

7. While SSH'ing into the target node, set the privileges on your `~/.ssh` and `~/.ssh/authorized_keys`.

   ```
   chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys
   ```

8. If you successfully accessed the remote server and changed the privileges on the `~/.ssh` , enter `exit` to end your SSH session.

## Install Ping Autonomous Identity

Make sure you have the following prerequisites:

* IP address of machines running Opensearch, MongoDB, or Cassandra.

* The Ping Autonomous Identity user should have permission to write to `/opt/autoid` on all machines

* To download the deployment images for the install, you still need your registry key to log into the Ping Google Cloud Registry to download the artifacts.

* Make sure you have the proper Opensearch certificates with the exact names for both pem and JKS files copied to `~/autoid-config/certs/elastic`:

  * esnode.pem

  * esnode-key.pem

  * root-ca.pem

  * elastic-client-keystore.jks

  * elastic-server-truststore.jks

* Make sure you have the proper MongoDB certificates with exact names for both pem and JKS files copied to `~/autoid-config/certs/mongo`:

  * mongo-client-keystore.jks

  * mongo-server-truststore.jks

  * mongodb.pem

  * rootCA.pem

* Make sure you have the proper Cassandra certificates with exact names for both pem and JKS files copied to \~/autoid-config/certs/cassandra:

  * Zoran-cassandra-client-cer.pem

  * Zoran-cassandra-client-keystore.jks

  * Zoran-cassandra-server-cer.pem

  * zoran-cassandra-server-keystore.jks

  * Zoran-cassandra-client-key.pem

  * Zoran-cassandra-client-truststore.jks

  * Zoran-cassandra-server-key.pem

  * Zoran-cassandra-server-truststore.jks

Install Ping Autonomous Identity:

1. Create the `autoid-config` directory.

   ```
   mkdir autoid-config
   ```

2. Change to the directory.

   ```
   cd autoid-config
   ```

3. Sign on to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, refer to [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

   ```
   docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
   ```

   The following output is displayed:

   ```
   Login Succeeded
   ```

4. Run the create-template command to generate the `deployer.sh` script wrapper and configuration files. Note that the command sets the configuration directory on the target node to `/config`. The `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

   ```
   docker run --user=$(id -u) -v ~/autoid-config:/config -it gcr.io/forgerock-autoid/deployer-pro:2022.11.12 create-template
   ```

5. Create a certificate directory for elastic.

   ```
   mkdir -p autoid-config/certs/elastic
   ```

6. Copy the Opensearch certificates and JKS files to `autoid-config/certs/elastic`.

7. Create a certificate directory for MongoDB.

   ```
   mkdir -p autoid-config/certs/mongo
   ```

8. Copy the MongoDB certificates and JKS files to `autoid-config/certs/mongo`.

9. Create a certificate directory for Cassandra.

   ```
   mkdir -p autoid-config/certs/cassandra
   ```

10. Copy the Cassandra certificates and JKS files to `autoid-config/certs/cassandra`.

11. Update the `hosts` file with the IP addresses of the machines. The `hosts` file must include the IP addresses for Docker nodes, Spark main/livy, and the MongoDB master. While the deployer pro doesn't install or configure the MongoDB main server, the entry is required to run the MongoDB CLI to seed the Ping Autonomous Identity schema.

    ```
    [docker-managers]

    [docker-workers]

    [docker:children]
    docker-managers
    docker-workers

    [spark-master-livy]

    [cassandra-seeds]
    #For replica sets, add the IPs of all Cassandra nodes

    [mongo_master]
    # Add the MongoDB main node in the cluster deployment
    # For example: 10.142.15.248 mongodb_master=True

    [odfe-master-node]
    # Add only the main node in the cluster deployment

    [kibana-node]
    # Please add only the master node in cluster deployment
    ```

12. Update the `vars.yml` file:

    1. Set `db_driver_type` to `mongo` or `cassandra`.

    2. Set `elastic_host`, `elastic_port`, and `elastic_user` properties.

    3. Set `kibana_host`.

    4. Set the Apache livy install directory.

    5. Ensure the `elastic_user`, `elastic_port`, and `mongo_part` are correctly configured.

    6. Update the `vault.yml` passwords for elastic and mongo to refect your installation.

    7. Set the `mongo_ldap` variable to `true` if you want Ping Autonomous Identity to authenticate with Mongo DB, configured as LDAP.

       |   |                                                                                                                                                                                                                       |
       | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
       |   | The `mongo_ldap` variable only appears in fresh installs of 2022.11.0 and its upgrades (2022.11.1+). If you upgraded from a 2021.8.7 deployment, the variable is not available in your upgraded 2022.11.x deployment. |

    8. If you are using Cassandra, set the Cassandra-related parameters in the `vars.yml` file. Default values are:

       ```
       cassandra:
         enable_ssl: "true"
         contact_points: 10.142.15.248 # comma separated values in case of replication set
         port: 9042
         username: zoran_dba
         cassandra_keystore_password: "Acc#1234"
         cassandra_truststore_password: "Acc#1234"
         ssl_client_key_file: "zoran-cassandra-client-key.pem"
         ssl_client_cert_file: "zoran-cassandra-client-cer.pem"
         ssl_ca_file: "zoran-cassandra-server-cer.pem"
         server_truststore_jks: "zoran-cassandra-server-truststore.jks"
         client_truststore_jks: "zoran-cassandra-client-truststore.jks"
         client_keystore_jks: "zoran-cassandra-client-keystore.jks"
       ```

13. Download images:

    ```
    ./deployer.sh download-images
    ```

14) Install Apache Livy.

    * The official release of Apache Livy doesn't support Apache Spark 3.3.1 or 3.3.2. Ping Identity has re-compiled and packaged Apache Livy to work with Apache Spark 3.3.1 hadoop 3 and Apache Spark 3.3.2 hadoop 3. Use the zip file located at `autoid-config/apache-livy/apache-livy-0.8.0-incubating-SNAPSHOT-bin.zip` to install Apache Livy on the Spark-Livy machine.

    * For Livy configuration, refer to <https://livy.apache.org/get-started/>.

15) On the Spark-Livy machine, run the following commands to install the python package dependencies:

    1. Change to the `/opt/autoid` directory:

       ```
       cd /opt/autoid
       ```

    2. Create a `requirements.txt` file with the following content:

       ```
       six==1.11
       certifi==2019.11.28
       python-dateutil==2.8.1
       jsonschema==3.2.0
       cassandra-driver
       numpy==1.22.0
       pyarrow==6.0.1
       wrapt==1.11.0
       PyYAML==6.0
       requests==2.31.0
       urllib3==1.26.18
       pymongo
       pandas==1.3.5
       tabulate
       openpyxl
       wheel
       cython
       ```

    3. Install the requirements file:

       ```
       pip3 install -r requirements.txt
       ```

16) Make sure that the `/opt/autoid` directory exists and that it is both readable and writable.

17) Run the deployer script:

    ```
    ./deployer.sh run
    ```

18) On the Spark-Livy machine, run the following commands to install the Python egg file:

    1. Install the egg file:

       ```
       cd /opt/autoid/eggs
       pip3.10 install autoid_analytics-2021.3-py3-none-any.whl
       ```

    2. Source the `.bashrc` file:

       ```
       source ~/.bashrc
       ```

    3. Restart Spark and Livy.

       ```
       ./spark/sbin/stop-all.sh
       ./livy/bin/livy-server stop

       ./spark/sbin/start-all.sh
       ./livy/bin/livy-server start
       ```

## Resolve Hostname

After installing Ping Autonomous Identity, set up the hostname resolution for your deployment.

Resolve the hostname:

1. Configure your DNS servers to access Ping Autonomous Identity dashboard on the target node. The following domain names must resolve to the IP address of the target node: `<target-environment>-ui.<domain-name>`.

2. If DNS cannot resolve target node hostname, edit it locally on the machine that you want to access Ping Autonomous Identity using a browser. Open a text editor and add an entry in the `/etc/hosts` (Linux/Unix) file or `C:\Windows\System32\drivers\etc\hosts` (Windows) for the self-service and UI services for each managed target node.

   ```
   <Target IP Address>  <target-environment>-ui.<domain-name>
   ```

   For example:

   ```
   34.70.190.144  autoid-ui.forgerock.com
   ```

3. If you set up a custom domain name and target environment, add the entries in `/etc/hosts`. For example:

   ```
   34.70.190.144  myid-ui.abc.com
   ```

   For more information on customizing your domain name, refer to [Customize Domains](../admin-guide/chap-customize-domain.html).

## Access the Dashboard

Access the Ping Autonomous Identity console UI:

1. Open a browser. If you set up your own url, use it for your login.

   ```
   https://autoid-ui.forgerock.com/
   ```

2. Log in as a test user.

   ```
   test user: bob.rodgers@forgerock.com
   password: <password>
   ```

## Check Apache Cassandra

Check Cassandra:

1. Make sure Cassandra is running in cluster mode. For example

   ```
   /opt/autoid/apache-cassandra-3.11.2/bin/nodetool status
   ```

## Check MongoDB

Check MongoDB:

1. Make sure MongoDB is running. For example:

   ```
   mongo --tls \
   --host <Host IP> \
   --tlsCAFile /opt/autoid/mongo/certs/rootCA.pem  \
   --tlsAllowInvalidCertificates  \
   --tlsCertificateKeyFile /opt/autoid/mongo/certs/mongodb.pem
   ```

## Check Apache Spark

Check Spark:

1. SSH to the target node and open Spark dashboard using the bundled text-mode web browser

   ```
   elinks http://localhost:8080
   ```

   Spark Master status should display as ALIVE and worker(s) with State ALIVE.

   > **Collapse: Click to display an example of the Spark dashboard**
   >
   > ![Spark Dashboard](_images/spark-dashboard.png)

## Start the Analytics

If the previous installation steps all succeeded, you must now prepare your data's entity definitions, data sources, and attribute mappings prior to running your analytics jobs. These step are required and are critical for a successful analytics process.

For more information, refer to [Set Entity Definitions](../admin-guide/set-entity-definitions.html).

---

---
title: Installation
description: This chapter shows you how to install and deploy Ping Autonomous Identity for intelligent entitlements management in production environments. For hardware and software requirements, refer to the Release notes.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:preface
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/preface.html
---

# Installation

This chapter shows you how to install and deploy Ping Autonomous Identity for intelligent entitlements management in production environments. For hardware and software requirements, refer to the [Release notes](../release-notes/preface.html).

[icon: cubes, set=fas, size=3x]

#### [Deployment architectures](chap-deployment-architectures.html)

Learn about the different deployment architectures.

[icon: plus, set=fas, size=3x]

#### [Install single node](chap-install-singlenode-target.html)

Install a single-node Ping Autonomous Identity installation.

[icon: plus-square, set=fas, size=3x]

#### [Install single node air-gap](chap-install-singlenode-airgap.html)

Install a single-node air-gapped Ping Autonomous Identity installation.

[icon: project-diagram, set=fas, size=3x]

#### [Install multi-node deployment](chap-install-multinode.html)

Install a multi-node Ping Autonomous Identity installation for evaluation.

[icon: share-alt-square, set=fas, size=3x]

#### [Install multi-node air-gapped](chap-install-multinode-airgap.html)

Install a multi-node Ping Autonomous Identity air-gapped installation.

[icon: chevron-circle-up, set=fas, size=3x]

#### [Upgrade](chap-upgrade.html)

Upgrade to the latest version.

[icon: hdd, set=fas, size=3x]

#### [Appendix: Ports](appendix-deployment-ports.html)

Learn about the Ping Autonomous Identity ports.

[icon: cogs, set=fas, size=3x]

#### [Appendix: vars.yml](appendix-vars-yml.html)

Learn about the main deployment configuration file.

For a description of the Ping Autonomous Identity UI console, refer to the [Ping Autonomous Identity Users Guide](../users-guide/preface.html).

---

---
title: Load Data to Cassandra
description: By this point, you should populte the data into Cassandra using the zload script. The script populates the Ping Autonomous Identity keyspace with the tables required for the UI.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-data-load-to-cassandra
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-data-load-to-cassandra.html
---

# Load Data to Cassandra

By this point, you should populte the data into Cassandra using the `zload` script. The script populates the Ping Autonomous Identity keyspace with the tables required for the UI.

* Run the `zload.py` script.

  ```
  $ [../resources/examples.bash:#data-load]
  ```

---

---
title: Upgrade Ping Autonomous Identity
description: Ping Autonomous Identity provides an upgrade command to update your core software to the latest version while migrating your data.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:install-guide:chap-upgrade
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/install-guide/chap-upgrade.html
section_ids:
  upgrade_considerations: Upgrade Considerations
  upgrade_paths: Upgrade Paths
  sec-upgrade-2022.11.x-to-2022.11.12-deployer-pro: Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 using deployer pro
  sec-upgrade-2022.11.x-to-2022.11.12-airgap-deployer-pro: Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 Air-Gapped using deployer pro
  sec-upgrade-2022.11.x-to-2022.11.12-deployer: Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 using the deployer
  sec-upgrade-2022.11.x-to-2022.11.12-airgap-deployer: Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 Air-Gapped using the deployer
---

# Upgrade Ping Autonomous Identity

Ping Autonomous Identity provides an upgrade command to update your core software to the latest version while migrating your data.

## Upgrade Considerations

* **Database Systems are the Same**. If your current database is Apache Cassandra, you cannot upgrade to a MongoDB-based system. You will need to run a clean installation with the new version.

* **Host IPs should be the Same**. Host IP addresses must be the same for existing components. You must update the `~/autoid-config/hosts` file by adding the IP addresses for the Elasticsearch entries. Refer to the instructions below.

* **Registry Key Required**. To download the deployment images for the upgrade, you still need your registry key to sign on to the Ping Google Cloud Registry. Copy your registry key from your previous build to your new upgrade.

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | Make sure to test the upgrade on a staging or QA server before running it in production. |

## Upgrade Paths

The upgrade assumes the following upgrade paths depends on your current deployment version. The preferred upgrade path is to the latest patch release.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Clean installations of Ping Autonomous Identity 2022.11.x (2022.11.0–2022.11.11) to 2022.11.12 use the new `deployer pro` script. Upgrades from version 2021.8.7 to 2022.11.x to 2022.11.12 use the older `deployer` script. The upgrade procedures differ slightly between the deployer pro and deployer versions, primarily in certificates directory creation (deployer versions) and using the proper image name during the `create-template` command (deployer pro and deployer versions). |

The following chart summarizes these upgrade paths:

**Table 1: Upgrade Paths**

| Version                             | Upgrade To                           | Refer to                                                                                                                                                  |
| ----------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2022.11.x (deployer-pro)            | 2022.11.12 (deployer-pro)            | * [Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 using deployer pro](#sec-upgrade-2022.11.x-to-2022.11.12-deployer-pro)                   |
| 2022.11.x Air-Gapped (deployer-pro) | 2022.11.12 Air-Gapped (deployer-pro) | - [Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 Air-Gapped using deployer pro](#sec-upgrade-2022.11.x-to-2022.11.12-airgap-deployer-pro) |
| 2022.11.0 (deployer)                | 2022.11.12 (deployer)                | * [Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 using the deployer](#sec-upgrade-2022.11.x-to-2022.11.12-deployer)                       |
| 2022.11.0 Air-Gapped (deployer)     | 2022.11.12 Air Gapped (deployer)     | - [Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 Air-Gapped using the deployer](#sec-upgrade-2022.11.x-to-2022.11.12-airgap-deployer)     |

## Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 using deployer pro

The following instructions are for upgrading from Ping Autonomous Identity version 2022.11.0–2022.11.11 to the latest version **2022.11.12** in non air-gapped deployments using the **deployer pro**.

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following steps assume you ran a fresh install of Ping Autonomous Identity 2022.11.x, which uses deployer pro. Make sure you have upgraded your [third-party software](../release-notes/chap-before-you-install.html#sec-third-party-sw-requirements) packages to the supported versions prior to upgrade. |

Upgrade from 2022.11.x to 2022.11.12 (Non Air-Gap) using deployer pro:

1. Start on the target server, and back up your `/data/conf` configuration file. The upgrade overwrites this file when updating, so you must restore this file after running the upgrade.

   ```
   sudo mv /data/conf ~/backup-data-conf-2022.11.x
   ```

2. Next, if you changed any analytic settings on your deployment, make note of your configuration, so that you can replicate those settings on the upgraded server. Log in to Ping Autonomous Identity, navigate to Administration > Analytic Settings, and record your settings.

3. On the deployer machine, back up the 2022.11.x `~/autoid-config` directory or move it to another location.

   ```
   mv ~/autoid-config ~/backup-2022.11.x
   ```

4. Create a new `~/autoid-config` directory.

   ```
   mkdir ~/autoid-config
   ```

5. Copy your `autoid_registry_key.json`, `ansible.cfg`, and `vault.yml` files from your backup directory to `~/autoid-config`. If your `vault.yml` file is encrypted, copy the `.autoid_vault_password` file to `~/autoid-config`.

6. Set up your certificate directories for Opensearch, MongoDB, or Cassandra for the deployer:

   1. Create a certificate directory Opensearch:

      ```
      mkdir -p autoid-config/certs/elastic
      ```

   2. Copy the Opensearch certificates and JKS files to `autoid-config/certs/elastic`.

   3. Create a certificate directory for MongoDB (if you use MongoDB):

      ```
      mkdir -p autoid-config/certs/mongo
      ```

   4. Copy the MongoDB certificates and JKS files to `autoid-config/certs/mongo`.

   5. Create a certificate directory for Cassandra (if you use Cassandra):

      ```
      mkdir -p autoid-config/certs/cassandra
      ```

   6. Copy the Cassandra certificates and JKS files to `autoid-config/certs/cassandra`.

7. Copy your original SSH key into the new directory.

   ```
   cp ~/.ssh/id_rsa ~/autoid-config
   ```

8. Change the permission on the SSH key.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

9. Check if you can successfully SSH to the target server.

   ```
   ssh autoid@<Target-IP-Address>

   Last login: Mon Mar 19 12:20:18 2024
   ```

10. On the deployer node, change to the `~/autoid-config` directory.

    ```
    cd ~/autoid-config
    ```

11. Log in to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, see [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

    ```
    docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
    ```

    You should see:

    ```
    Login Succeeded
    ```

12. Run the `create-template` command to generate the `deployer.sh` script wrapper and configuration files. Note that the command sets the configuration directory on the target node to `/config`. The `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

    ```
    docker run --user=$(id -u) -v ~/autoid-config:/config \
    -it gcr.io/forgerock-autoid/deployer-pro:2022.11.12 create-template
    ```

13. Configure your upgraded system by editing the `~/autoid-config/vars.yml` , `~/autoid-config/hosts` , and `~/autoid-config/vault.yml` files on the deployer machine.

    |   |                                                                                  |
    | - | -------------------------------------------------------------------------------- |
    |   | You must keep your configuration settings consistent from one system to another. |

14. Stop the stack.

    |   |                                                                                            |
    | - | ------------------------------------------------------------------------------------------ |
    |   | If you are upgrading a multi-node deployment, run this command on the Docker Manager node. |

    ```
    docker stack rm configuration-service consul-server consul-client nginx jas swagger-ui ui api notebook
    ```

    You should see:

    ```
    Removing service configuration-service_configuration-service
    Removing service consul-server_consul-server
    Removing service consul-client_consul-client
    Removing service nginx_nginx
    Removing service jas_jasnode
    Removing service swagger-ui_swagger-ui
    Removing service ui_zoran-ui
    Removing service api_zoran-api
    Nothing found in stack: notebook
    ```

15. Prune old Docker images before running the upgrade command:

    1. Get all of the Docker images:

       ```
       docker images
       ```

    2. Identify the images that are Ping Autonomous Identity-related. They start with the URL of the Ping Google Cloud Registry (Ping Identity GCR). For example:

       ```
       REPOSITORY                                    TAG         IMAGE ID       CREATED       SIZE
       <ForgeRock GCR>/ci/develop/deployer           650879186   075481cea4c2   2 hours ago   823MB
       <ForgeRock GCR>/ci/develop/offline-packages   650879186   e1a90f389ccc   2 hours ago   3.03GB
       <ForgeRock GCR>/ci/develop/zoran-ui           650879186   bd303a28b5df   2 hours ago   35.3MB
       <ForgeRock GCR>/ci/develop/zoran-api          650879186   114d1aca5b0a   2 hours ago   421MB
       <ForgeRock GCR>/ci/develop/nginx              650879186   43b410661269   2 hours ago   16.7MB
       <ForgeRock GCR>/ci/develop/jas                650879186   2821e5c365d8   2 hours ago   491MB
       ```

    3. Remove the old images using the `docker rmi` command. For example:

       ```
       docker rmi -f <image ID>

       Example:
       docker rmi -f 075481cea4c2
       ```

    4. Repeat the previous command to remove all of the Ping Autonomous Identity-related Docker images.

16. For multinode deployments, run the following on the Docker Worker node:

    ```
    docker swarm leave
    ```

17. Enter `exit` to end your SSH session.

18. From the deployer, restart Docker command:

    ```
    sudo systemctl restart docker
    ```

19. Download the images. This step downloads software dependencies needed for the deployment and places them in the `autoid-packages` directory. Make sure you are in the `~/autoid-config` directory.

    ```
    ./deployer.sh download-images
    ```

20. On the Spark-Livy machine, run the following commands to install the python package dependencies:

    1. Change to the `/opt/autoid` directory:

       ```
       cd /opt/autoid
       ```

    2. Create a `requirements.txt` file with the following content:

       ```
       six==1.11
       certifi==2019.11.28
       python-dateutil==2.8.1
       jsonschema==3.2.0
       cassandra-driver
       numpy==1.22.0
       pyarrow==6.0.1
       wrapt==1.11.0
       PyYAML==6.0
       requests==2.31.0
       urllib3==1.26.18
       pymongo
       pandas==1.3.5
       tabulate
       openpyxl
       wheel
       cython
       ```

    3. Install the requirements file:

       ```
       pip3 install -r requirements.txt
       ```

21. Run the upgrade:

    ```
    ./deployer.sh upgrade
    ```

22. On the Spark-Livy machine, run the following commands to install the Python wheel distribution:

    1. Install the wheel file:

       ```
       cd /opt/autoid/eggs
       pip3.10 install autoid_analytics-2021.3-py3-none-any.whl
       ```

    2. Source the `.bashrc` file:

       ```
       source ~/.bashrc
       ```

    3. Restart Spark and Livy.

       ```
       ./spark/sbin/stop-all.sh
       ./livy/bin/livy-server stop

       ./spark/sbin/start-all.sh
       ./livy/bin/livy-server start
       ```

23. SSH to the target server.

24. On the target server, restore your `/data/conf` configuration data file from your previous installation.

    ```
    sudo mv ~/backup-data-conf-2022.11.x /data/conf
    ```

25. Re-apply your analytics settings to your upgraded server if you made changes on your previous Ping Autonomous Identity machine. Log in to Ping Autonomous Identity, navigate to Administration > Analytics Settings, and edit your changes.

26. Log out, and then log back in to Ping Autonomous Identity.

You have successfully upgraded your Ping Autonomous Identity server to 2022.11.12.

## Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 Air-Gapped using deployer pro

The following instructions are for upgrading from Ping Autonomous Identity version 2022.11.0–2022.11.11 on air-gapped deployments using the **deployer pro**.

|   |                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following steps assume you ran a fresh install of Ping Autonomous Identity 2022.11.x, which uses deployer pro. Make sure you have upgraded your [third-party software](../release-notes/chap-before-you-install.html#sec-third-party-sw-requirements) packages to the supported versions prior to upgrade. |

Upgrade from 2022.11.x to 2022.11.12 Air-Gapped using deployer pro:

1. Start on the target server, and back up your `/data/conf` configuration file. The upgrade overwrites this file when updating, so you must restore this file after running the upgrade.

   ```
   sudo mv /data/conf ~/backup-data-conf-2022.11.x
   ```

2. Next, if you changed any analytic settings on your deployment, make note of your configuration, so that you can replicate those settings on the upgraded server. Log in to Ping Autonomous Identity, navigate to Administration > Analytic Settings, and record your settings.

3. On the deployer machine, back up the 2022.11.x `~/autoid-config` directory or move it to another location.

   ```
   mv ~/autoid-config ~/backup-2022.11.x
   ```

4. Create a new `~/autoid-config` directory.

   ```
   mkdir ~/autoid-config
   ```

5. Copy your `autoid_registry_key.json`, `ansible.cfg`, and `vault.yml` files from your backup directory to `~/autoid-config`. If your `vault.yml` file is encrypted, copy the `.autoid_vault_password` file to `~/autoid-config`.

6. Set up your certificate directories for Opensearch, MongoDB, or Cassandra for the deployer:

   1. Create a certificate directory Opensearch:

      ```
      mkdir -p autoid-config/certs/elastic
      ```

   2. Copy the Opensearch certificates and JKS files to `autoid-config/certs/elastic`.

   3. Create a certificate directory for MongoDB (if you use MongoDB):

      ```
      mkdir -p autoid-config/certs/mongo
      ```

   4. Copy the MongoDB certificates and JKS files to `autoid-config/certs/mongo`.

   5. Create a certificate directory for Cassandra (if you use Cassandra):

      ```
      mkdir -p autoid-config/certs/cassandra
      ```

   6. Copy the Cassandra certificates and JKS files to `autoid-config/certs/cassandra`.

7. Copy your original SSH key into the new directory.

   ```
   cp ~/.ssh/id_rsa ~/autoid-config
   ```

8. Change the permission on the SSH key.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

9. On the deployer node, change to the `~/autoid-config` directory.

   ```
   cd ~/autoid-config
   ```

10. Log in to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, see [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

    ```
    docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
    ```

    You should see:

    ```
    Login Succeeded
    ```

11. Run the `create-template` command to generate the `deployer.sh` script wrapper and configuration files. Note that the command sets the configuration directory on the target node to `/config`. The `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

    ```
    docker run --user=$(id -u) -v ~/autoid-config:/config \
    -it gcr.io/forgerock-autoid/deployer-pro:2022.11.12 create-template
    ```

12. Configure your upgraded system by editing the `~/autoid-config/vars.yml` , `~/autoid-config/hosts` , and `~/autoid-config/vault.yml` files on the deployer machine.

    |   |                                                                                  |
    | - | -------------------------------------------------------------------------------- |
    |   | You must keep your configuration settings consistent from one system to another. |

13. Download the images. This step downloads software dependencies needed for the deployment and places them in the `autoid-packages` directory. Make sure you are in the `~/autoid-config` directory.

    ```
    ./deployer.sh download-images
    ```

14. On the Spark-Livy machine, run the following commands to install the python package dependencies:

    1. Change to the `/opt/autoid` directory:

       ```
       cd /opt/autoid
       ```

    2. Create a `requirements.txt` file with the following content:

       ```
       six==1.11
       certifi==2019.11.28
       python-dateutil==2.8.1
       jsonschema==3.2.0
       cassandra-driver
       numpy==1.22.0
       pyarrow==6.0.1
       wrapt==1.11.0
       PyYAML==6.0
       requests==2.31.0
       urllib3==1.26.18
       pymongo
       pandas==1.3.5
       tabulate
       openpyxl
       wheel
       cython
       ```

    3. Install the requirements file:

       ```
       pip3 install -r requirements.txt
       ```

15. Stop the stack.

    |   |                                                                                            |
    | - | ------------------------------------------------------------------------------------------ |
    |   | If you are upgrading a multi-node deployment, run this command on the Docker Manager node. |

    ```
    docker stack rm configuration-service consul-server consul-client nginx jas swagger-ui ui api notebook
    ```

    You should see:

    ```
    Removing service configuration-service_configuration-service
    Removing service consul-server_consul-server
    Removing service consul-client_consul-client
    Removing service nginx_nginx
    Removing service jas_jasnode
    Removing service swagger-ui_swagger-ui
    Removing service ui_zoran-ui
    Removing service api_zoran-api
    Nothing found in stack: notebook
    ```

16. Prune old Docker images before running the upgrade command:

    1. Get all of the Docker images:

       ```
       docker images
       ```

    2. Identify the images that are Ping Autonomous Identity-related. They start with the URL of the Ping Google Cloud Registry (Ping Identity GCR). For example:

       ```
       REPOSITORY                                    TAG         IMAGE ID       CREATED       SIZE
       <ForgeRock GCR>/ci/develop/deployer           650879186   075481cea4c2   2 hours ago   823MB
       <ForgeRock GCR>/ci/develop/offline-packages   650879186   e1a90f389ccc   2 hours ago   3.03GB
       <ForgeRock GCR>/ci/develop/zoran-ui           650879186   bd303a28b5df   2 hours ago   35.3MB
       <ForgeRock GCR>/ci/develop/zoran-api          650879186   114d1aca5b0a   2 hours ago   421MB
       <ForgeRock GCR>/ci/develop/nginx              650879186   43b410661269   2 hours ago   16.7MB
       <ForgeRock GCR>/ci/develop/jas                650879186   2821e5c365d8   2 hours ago   491MB
       ```

    3. Remove the old images using the `docker rmi` command. For example:

       ```
       docker rmi -f <image ID>

       Example:
       docker rmi -f 075481cea4c2
       ```

17. For multinode deployments, run the following on the Docker Worker node:

    ```
    docker swarm leave
    ```

18. From the deployer, restart Docker:

    ```
    sudo systemctl restart docker
    ```

19. Create a tar file containing all of the Autonomous Identity binaries.

    ```
    tar czf autoid-packages.tgz deployer.sh autoid-packages/*
    ```

20. Copy the `autoid-packages.tgz`, `deployer.sh`, and SSH key (id\_rsa ) to a portable hard drive.

21. On the air-gapped target machine, backup your previous `~/autoid-config` directory, and then create a new `~/autoid-config` directory.

    ```
    mkdir ~/autoid-config
    ```

22. Copy the `autoid-package.tgz` tar file, `deployer.sh`, and SSH key from the portable storage device to the `/autoid-config` folder.

23. Unpack the tar file.

    ```
    tar xf autoid-packages.tgz -C ~/autoid-config
    ```

24. Set up your certificate directories for Opensearch, MongoDB, or Cassandra for the deployer:

    1. Create a certificate directory Opensearch:

       ```
       mkdir -p autoid-config/certs/elastic
       ```

    2. Copy the Opensearch certificates and JKS files to `autoid-config/certs/elastic`.

    3. Create a certificate directory for MongoDB (if you use MongoDB):

       ```
       mkdir -p autoid-config/certs/mongo
       ```

    4. Copy the MongoDB certificates and JKS files to `autoid-config/certs/mongo`.

    5. Create a certificate directory for Cassandra (if you use Cassandra):

       ```
       mkdir -p autoid-config/certs/cassandra
       ```

    6. Copy the Cassandra certificates and JKS files to `autoid-config/certs/cassandra`.

25. Copy the SSH key to the `~/autoid-config` directory.

26. Change the privileges to the file.

    ```
    chmod 400 ~/autoid-config/id_rsa
    ```

27. Change to the configuration directory.

    ```
    cd ~/autoid-config
    ```

28. Import the deployer image.

    ```
    ./deployer.sh import-deployer
    ```

    You should see:

    ```
    …​
    db631c8b06ee: Loading layer [=============================================⇒]   2.56kB/2.56kB
    2d62082e3327: Loading layer [=============================================⇒]  753.2kB/753.2kB
    Loaded image: <ForgeRock Google cloud registry URl>/deployer:2022.11.12
    ```

29. Create the configuration template using the `create-template` command. This command creates the configuration files: `ansible.cfg` , `vars.yml` , `vault.yml` and `hosts`.

    ```
    ./deployer.sh create-template
    ```

    You should see:

    ```
    Config template is copied to host machine directory mapped to /config
    ```

30. Configure your upgraded system by editing the `~/autoid-config/vars.yml` , `~/autoid-config/hosts` , and `~/autoid-config/vault.yml` files on the deployer machine.

    |   |                                                                                  |
    | - | -------------------------------------------------------------------------------- |
    |   | You must keep your configuration settings consistent from one system to another. |

31. Run the upgrade:

    ```
    ./deployer.sh upgrade
    ```

32. On the Spark-Livy machine, run the following commands to install the Python wheel distribution:

    1. Install the wheel file:

       ```
       cd /opt/autoid/eggs
       pip3.10 install autoid_analytics-2021.3-py3-none-any.whl
       ```

    2. Source the `.bashrc` file:

       ```
       source ~/.bashrc
       ```

    3. Restart Spark and Livy.

       ```
       ./spark/sbin/stop-all.sh
       ./livy/bin/livy-server stop

       ./spark/sbin/start-all.sh
       ./livy/bin/livy-server start
       ```

33. SSH to the target server.

34. On the target server, restore your `/data/conf` configuration data file from your previous installation.

    ```
    sudo mv ~/backup-data-conf-2022.11.x /data/conf
    ```

35. Re-apply your analytics settings to your upgraded server if you made changes on your previous Ping Autonomous Identity machine. Log in to Ping Autonomous Identity, navigate to Administration > Analytics Settings, and edit your changes.

36. Log out, and then log back in to Ping Autonomous Identity.

You have successfully upgraded your Ping Autonomous Identity server to 2022.11.12.

## Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 using the deployer

The following instructions are for upgrading from Ping Autonomous Identity version 2022.11.0–2022.11.11 to the latest version **2022.11.12** in non air-gapped deployments using the **deployer**.

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you upgraded from any Ping Autonomous Identity version 2021.8.7 or earlier to version 2022.11.x, then you are using the `deployer`. |

Upgrade from 2022.11.x to 2022.11.12 (Non Air-Gap) using deployer:

1. Start on the target server, and back up your `/data/conf` configuration file. The upgrade overwrites this file when updating, so you must restore this file after running the upgrade.

   ```
   sudo mv /data/conf ~/backup-data-conf-2022.11.x
   ```

2. Next, if you changed any analytic settings on your deployment, make note of your configuration, so that you can replicate those settings on the upgraded server. Log in to Ping Autonomous Identity, navigate to Administration > Analytic Settings, and record your settings.

3. On the deployer machine, back up the 2022.11.x `~/autoid-config` directory or move it to another location.

   ```
   mv ~/autoid-config ~/backup-2022.11.x
   ```

4. Create a new `~/autoid-config` directory.

   ```
   mkdir ~/autoid-config
   ```

5. Copy your `autoid_registry_key.json` from your backup directory to `~/autoid-config`.

6. Copy your original SSH key into the new directory.

   ```
   cp ~/.ssh/id_rsa ~/autoid-config
   ```

7. Change the permission on the SSH key.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

8. Check if you can successfully SSH to the target server.

   ```
   ssh autoid@<Target-IP-Address>

   Last login: Mon Jan 23 12:20:18 2024
   ```

9. On the deployer node, change to the `~/autoid-config` directory.

   ```
   cd ~/autoid-config
   ```

10. Log in to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, see [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

    ```
    docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
    ```

    You should see:

    ```
    Login Succeeded
    ```

11. Run the `create-template` command to generate the `deployer.sh` script wrapper and configuration files. Note that the command sets the configuration directory on the target node to `/config`. The `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

    ```
    docker run --user=$(id -u) -v ~/autoid-config:/config \
    -it gcr.io/forgerock-autoid/deployer:2022.11.12 create-template
    ```

12. Configure your upgraded system by editing the `~/autoid-config/vars.yml` , `~/autoid-config/hosts` , and `~/autoid-config/vault.yml` files on the deployer machine.

    |   |                                                                                  |
    | - | -------------------------------------------------------------------------------- |
    |   | You must keep your configuration settings consistent from one system to another. |

13. Stop the stack.

    |   |                                                                                            |
    | - | ------------------------------------------------------------------------------------------ |
    |   | If you are upgrading a multi-node deployment, run this command on the Docker Manager node. |

    ```
    docker stack rm configuration-service consul-server consul-client nginx jas swagger-ui ui api notebook
    ```

    You should see:

    ```
    Removing service configuration-service_configuration-service
    Removing service consul-server_consul-server
    Removing service consul-client_consul-client
    Removing service nginx_nginx
    Removing service jas_jasnode
    Removing service swagger-ui_swagger-ui
    Removing service ui_zoran-ui
    Removing service api_zoran-api
    Nothing found in stack: notebook
    ```

14. Prune old Docker images before running the upgrade command:

    1. Get all of the Docker images:

       ```
       docker images
       ```

    2. Identify the images that are Ping Autonomous Identity-related. They start with the URL of the ForgeRock Google cloud registry (ForgeRock GCR). For example:

       ```
       REPOSITORY                                    TAG         IMAGE ID       CREATED       SIZE
       <ForgeRock GCR>/ci/develop/deployer           650879186   075481cea4c2   2 hours ago   823MB
       <ForgeRock GCR>/ci/develop/offline-packages   650879186   e1a90f389ccc   2 hours ago   3.03GB
       <ForgeRock GCR>/ci/develop/zoran-ui           650879186   bd303a28b5df   2 hours ago   35.3MB
       <ForgeRock GCR>/ci/develop/zoran-api          650879186   114d1aca5b0a   2 hours ago   421MB
       <ForgeRock GCR>/ci/develop/nginx              650879186   43b410661269   2 hours ago   16.7MB
       <ForgeRock GCR>/ci/develop/jas                650879186   2821e5c365d8   2 hours ago   491MB
       ```

    3. Remove the old images using the `docker rmi` command. For example:

       ```
       docker rmi -f <image ID>

       Example:
       docker rmi -f 075481cea4c2
       ```

    4. Repeat the previous command to remove all of the Ping Autonomous Identity-related Docker images.

15. For multinode deployments, run the following on the Docker Worker node:

    ```
    docker swarm leave
    ```

16. Enter `exit` to end your SSH session.

17. From the deployer, restart Docker command:

    ```
    sudo systemctl restart docker
    ```

18. Download the images. This step downloads software dependencies needed for the deployment and places them in the `autoid-packages` directory. Make sure you are in the `/autoid-config` directory.

    ```
    ./deployer.sh download-images
    ```

19. Run the upgrade:

    ```
    ./deployer.sh upgrade
    ```

20. SSH to the target server.

21. On the target server, restore your `/data/conf` configuration data file from your previous installation.

    ```
    sudo mv ~/backup-data-conf-2022.11.x /data/conf
    ```

22. Re-apply your analytics settings to your upgraded server if you made changes on your previous Ping Autonomous Identity machine. Log in to Ping Autonomous Identity, navigate to Administration > Analytics Settings, and edit your changes.

23. Log out, and then log back in to Ping Autonomous Identity.

You have successfully upgraded your Ping Autonomous Identity server to 2022.11.12.

## Upgrade from Ping Autonomous Identity 2022.11.x to 2022.11.12 Air-Gapped using the deployer

The following instructions are for upgrading from Ping Autonomous Identity version 2022.11.0–2022.11.11 to the latest version **2022.11.12** on air-gapped deployments using the **deployer**.

Upgrade from 2022.11.x to 2022.11.12 Air-Gapped using deployer:

1. Start on the target server, and back up your `/data/conf` configuration file. The upgrade overwrites this file when updating, so you must restore this file after running the upgrade.

   ```
   sudo mv /data/conf ~/backup-data-conf-2022.11.x
   ```

2. Next, if you changed any analytic settings on your deployment, make note of your configuration, so that you can replicate those settings on the upgraded server. Log in to Ping Autonomous Identity, navigate to Administration > Analytic Settings, and record your settings.

3. On the deployer machine, back up the 2022.11.x `~/autoid-config` directory or move it to another location.

   ```
   mv ~/autoid-config ~/backup-2022.11.x
   ```

4. Create a new `~/autoid-config` directory.

   ```
   mkdir ~/autoid-config
   ```

5. Copy your `autoid_registry_key.json` from your backup directory to `~/autoid-config`.

6. Copy your original SSH key into the new directory.

   ```
   cp ~/.ssh/id_rsa ~/autoid-config
   ```

7. Change the permission on the SSH key.

   ```
   chmod 400 ~/autoid-config/id_rsa
   ```

8. On the deployer node, change to the `~/autoid-config` directory.

   ```
   cd ~/autoid-config
   ```

9. Log in to the Ping Google Cloud Registry using the registry key. The registry key is only available to Ping Autonomous Identity customers. For specific instructions on obtaining the registry key, see [How To Configure Service Credentials (Push Auth, Docker) in Backstage](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771).

   ```
   docker login -u _json_key -p "$(cat autoid_registry_key.json)" https://gcr.io/forgerock-autoid
   ```

   You should see:

   ```
   Login Succeeded
   ```

10. Run the `create-template` command to generate the `deployer.sh` script wrapper and configuration files. Note that the command sets the configuration directory on the target node to `/config`. The `--user` parameter eliminates the need to use `sudo` while editing the hosts file and other configuration files.

    ```
    docker run --user=$(id -u) -v ~/autoid-config:/config \
    -it gcr.io/forgerock-autoid/deployer:2022.11.12 create-template
    ```

11. Configure your upgraded system by editing the `~/autoid-config/vars.yml` , `~/autoid-config/hosts` , and `~/autoid-config/vault.yml` files on the deployer machine.

    |   |                                                                                  |
    | - | -------------------------------------------------------------------------------- |
    |   | You must keep your configuration settings consistent from one system to another. |

12. Download the images. This step downloads software dependencies needed for the deployment and places them in the `autoid-packages` directory. Make sure you are in the `~/autoid-config` directory.

    ```
    ./deployer.sh download-images
    ```

13. Stop the stack.

    |   |                                                                                            |
    | - | ------------------------------------------------------------------------------------------ |
    |   | If you are upgrading a multi-node deployment, run this command on the Docker Manager node. |

    ```
    docker stack rm configuration-service consul-server consul-client nginx jas swagger-ui ui api notebook
    ```

    You should see:

    ```
    Removing service configuration-service_configuration-service
    Removing service consul-server_consul-server
    Removing service consul-client_consul-client
    Removing service nginx_nginx
    Removing service jas_jasnode
    Removing service swagger-ui_swagger-ui
    Removing service ui_zoran-ui
    Removing service api_zoran-api
    Nothing found in stack: notebook
    ```

14. Prune old Docker images before running the upgrade command:

    1. Get all of the Docker images:

       ```
       docker images
       ```

    2. Identify the images that are Ping Autonomous Identity-related. They start with the URL of the Ping Google Cloud Registry (Ping Identity GCR). For example:

       ```
       REPOSITORY                                    TAG         IMAGE ID       CREATED       SIZE
       <ForgeRock GCR>/ci/develop/deployer           650879186   075481cea4c2   2 hours ago   823MB
       <ForgeRock GCR>/ci/develop/offline-packages   650879186   e1a90f389ccc   2 hours ago   3.03GB
       <ForgeRock GCR>/ci/develop/zoran-ui           650879186   bd303a28b5df   2 hours ago   35.3MB
       <ForgeRock GCR>/ci/develop/zoran-api          650879186   114d1aca5b0a   2 hours ago   421MB
       <ForgeRock GCR>/ci/develop/nginx              650879186   43b410661269   2 hours ago   16.7MB
       <ForgeRock GCR>/ci/develop/jas                650879186   2821e5c365d8   2 hours ago   491MB
       ```

    3. Remove the old images using the `docker rmi` command. For example:

       ```
       docker rmi -f <image ID>

       Example:
       docker rmi -f 075481cea4c2
       ```

15. For multinode deployments, run the following on the Docker Worker node:

    ```
    docker swarm leave
    ```

16. From the deployer, restart Docker:

    ```
    sudo systemctl restart docker
    ```

17. Create a tar file containing all of the Autonomous Identity binaries.

    ```
    tar czf autoid-packages.tgz deployer.sh autoid-packages/*
    ```

18. Copy the `autoid-packages.tgz`, `deployer.sh`, and SSH key (id\_rsa ) to a portable hard drive.

19. On the air-gapped target machine, backup your previous `~/autoid-config` directory, and then create a new `~/autoid-config` directory.

    ```
    mkdir ~/autoid-config
    ```

20. Copy the `autoid-package.tgz` tar file, `deployer.sh`, and SSH key from the portable storage device to the `/autoid-config` folder.

21. Unpack the tar file.

    ```
    tar xf autoid-packages.tgz -C ~/autoid-config
    ```

22. Copy the SSH key to the `~/autoid-config` directory.

23. Change the privileges to the file.

    ```
    chmod 400 ~/autoid-config/id_rsa
    ```

24. Change to the configuration directory.

    ```
    cd ~/autoid-config
    ```

25. Import the deployer image.

    ```
    ./deployer.sh import-deployer
    ```

    You should see:

    ```
    …​
    db631c8b06ee: Loading layer [=============================================⇒]   2.56kB/2.56kB
    2d62082e3327: Loading layer [=============================================⇒]  753.2kB/753.2kB
    Loaded image: https://gcr.io/forgerock-autoid/deployer:2022.11.12
    ```

26. Create the configuration template using the `create-template` command. This command creates the configuration files: `ansible.cfg` , `vars.yml` , `vault.yml` and `hosts`.

    ```
    ./deployer.sh create-template
    ```

    You should see:

    ```
    Config template is copied to host machine directory mapped to /config
    ```

27. Configure your upgraded system by editing the `~/autoid-config/vars.yml` , `~/autoid-config/hosts` , and `~/autoid-config/vault.yml` files on the deployer machine.

    |   |                                                                                  |
    | - | -------------------------------------------------------------------------------- |
    |   | You must keep your configuration settings consistent from one system to another. |

28. Run the upgrade:

    ```
    ./deployer.sh upgrade
    ```

29. On the target server, restore your `/data/conf` configuration data file from your previous installation.

    ```
    sudo mv ~/backup-data-conf-2022.11.x /data/conf
    ```

30. Re-apply your analytics settings to your upgraded server if you made changes on your previous Ping Autonomous Identity machine. Log in to Ping Autonomous Identity, navigate to Administration > Analytics Settings, and edit your changes.

31. Log out, and then log back in to Ping Autonomous Identity.

You have successfully upgraded your Ping Autonomous Identity server to 2022.11.12.
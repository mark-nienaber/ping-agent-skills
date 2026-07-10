---
title: ABS Administration
description: Administering API Behavioral Security (ABS) requires the understanding of:
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_administration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_administration.html
revdate: April 3, 2024
---

# ABS Administration

Administering API Behavioral Security (ABS) requires the understanding of:

* Directory structure

* Obfuscating passwords for securing ABS

* Configuring Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">
  \<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
  \</div>)* for secure communication for between PingIntelligence products

* Different types of ABS users

* Understanding the port requirements

* Creating ABS cluster

* Understanding ABS log files

* Purging access logs from ABS

* ABS REST API format

---

---
title: ABS AI Engine
description: The API Behavioral Security (ABS) AI engine is a Java-based distributed system that analyzes application programming interface (API) traffic to provide API traffic insight, visibility, and security.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_ai_engine
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_ai_engine.html
revdate: April 3, 2024
---

# ABS AI Engine

The API Behavioral Security (ABS) AI engine is a Java-based distributed system that analyzes application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* traffic to provide API traffic insight, visibility, and security.

API traffic information is received from API Security Enforcer (ASE) nodes in log files containing:

* Client details such as device, browser, Internet Protocol (IP) *(tooltip: \<div class="paragraph">
  \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
  \</div>)* address, and operating system.

* Session information including HTTP or WebSocket connections and methods.

These logs are periodically (every 10 minutes) forwarded to ABS nodes for processing. Using machine learning algorithms, ABS generates API traffic insight, anomaly data, and attack insight that identifies clients responsible for attacks. To prevent future attacks, ABS can automatically program inline devices, such as the ASE , to block clients based on attack lists.

The ABS AI engine provides the following functionality:

* Collection and consolidation of access logs from ASE nodes

* Machine learning algorithms to identify anomalies and attacks

* Detection of attacks from HTTP(s) and WebSocket(s) traffic

* Optional sending of blacklists to ASE which blocks client access

* Centralized database for storing AI data

* Stateless cluster for scalability and resiliency

* REST APIs for fetching traffic metrics, anomalies, and attack information

* Email alerts

Configuring ABS consists of setting up two entities:

* Database system

  ABS uses a MongoDB database to store metadata and all Machine Learning (ML) analytics. The MongoDB database system is configured in a replica set for production deployments. MongoDB is separately installed before starting ABS.

* ABS AI engine

  One or more ABS instances are configured to receive and process logs and to store results in MongoDB. You should install ABS in a cluster for high availability deployments.

---

---
title: ABS AI-based security
description: The API Behavioral Security (ABS) AI Engine detects attacks using artificial intelligence (AI) algorithms.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_ai_based_security
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_ai_based_security.html
revdate: June 3, 2024
---

# ABS AI-based security

The API Behavioral Security (ABS) AI Engine detects attacks using artificial intelligence (AI) algorithms.

After receiving API Security Enforcer (ASE) access logs and application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* configuration files, ABS applies AI algorithms to track API connections and detect attacks. If the `enable_abs_attack` parameter is set to `true`, ABS sends the deny list to ASE, which blocks client identifiers, such as API keys, usernames, cookie, Internet Protocol (IP) *(tooltip: \<div class="paragraph">
\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
\</div>)* address, and OAuth token on the list.

![A diagram of data flow between ASE and ABS when detecting an attack.](../_images/nhg1564009020141.png)

---

---
title: ABS AI-based security
description: The API Behavioral Security (ABS) AI Engine detects attacks using artificial intelligence (AI) algorithms.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_inline_abs_ai_based_security
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_inline_abs_ai_based_security.html
revdate: June 3, 2024
---

# ABS AI-based security

The API Behavioral Security (ABS) AI Engine detects attacks using artificial intelligence (AI) algorithms.

After receiving API Security Enforcer (ASE) access logs and application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* configuration files, ABS applies AI algorithms to track API connections and detect attacks. If the `enable_abs_attack` parameter is set to `true`, ABS sends the deny list to ASE, which blocks client identifiers, such as API keys, usernames, cookie, Internet Protocol (IP) *(tooltip: \<div class="paragraph">
\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
\</div>)* address, and OAuth token on the list.

![A diagram of data flow between ASE and ABS when detecting an attack.](../_images/nhg1564009020141.png)

---

---
title: ABS alerts
description: API Behavioral Security (ABS) email alerts are sent based on the following category of events.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_alerts
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_alerts.html
revdate: April 3, 2024
---

# ABS alerts

API Behavioral Security (ABS) email alerts are sent based on the following category of events.

These events are also logged in the `abs.log` file. The threshold values for these events are pre-set. If you want to change the threshold values after the system is running, then you have to manually change the values in MongoDB.

* Dynamic Rate Limit: alert sent when CPU, disk, or memory crosses the configured threshold value.

* ABS Node: alert sent when ABS cluster nodes are added or removed.

* MongoDB: alert sent when a MongoDB node is added or becomes inaccessible.

* Percentage Disk Usage Limit: alert sent when the disk usage reaches the configured `percentage_diskusage_limit` value. When this limit is reached, ABS stops accepting any new access log files from ASE. The alert is also logged in the `abs.log` file. You can use `update.sh` script in`/abs/util/` directory to update the thresholds for `Percentage Disk Usage Limit`.

* License: The following license related alerts are sent:

  * ABS license invalid: alert is sent if the ABS license is found to be invalid. In this case ABS shuts down.

  * ABS license expiration: alert sent when ABS license is expired.

  * Transaction limit reached: alert sent when ABS reaches the licensed monthly transaction limit.

* Scale Up and Scale Down: alert sent when a system resource, such as CPU, memory, or disk utilization, is above or below its threshold value for a specified interval of time. If the value is above the threshold value, add ABS nodes to distribute the load. If the resource utilization is below the lower threshold, you may remove an ABS node from the ABS cluster.

* DDoS attack alert: ABS sends alerts for multi-client Login Attacks and for API DDoS Attack Type 1. The email alert provides a time period for the attack along with a URL to access information on all client IPs participating in the attack.

Following is a template for alerts:

```
Event:  <the type of event>
Value:  <the specific trigger for the event>
When:  <the date and time of the event>
Where:  <the IP address of the server where the event occured>
```

For example,

```
Event: Scale Down ABS Node
Value : 192.168.11.166
CPU scale down threshold reached.
When : 2019-Jun-05 18:02:33 UTC
Where: 192.168.11.166
```

The following table describes the various email alerts sent by ABS and their possible resolution. The resolution provided is only a starting point to understand the cause of the alert. If ABS is reporting an alert even after the following the resolution provided, contact Ping Identity support.

| Email alert                                                                                               | Possible cause and resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File System Maxed Out - Rate Limit Alert                                                                  | Cause: A possible reason for this alert could be that historical access log files from ASE have accumulated on the storage disk.Resolution: Purge or archive the old access log files from storage disk.                                                                                                                                                                                                                                                                                  |
| ABS node added to cluster                                                                                 | ABS sends an email alert when a node joins an ABS cluster.Confirm: ABS admin should verify whether the correct ABS node joined the ABS cluster.                                                                                                                                                                                                                                                                                                                                           |
| ABS node removed from cluster                                                                             | ABS sends an email alert when a node is removed from an ABS cluster.Confirm: ABS admin should check the reason for removal of ABS node from the cluster. ABS node could disconnect from cluster because of network issues, a manual stop of ABS, or change in IP address of the ABS machine.                                                                                                                                                                                              |
| Memory scale up or scale down                                                                             | Cause: ABS sends an email alert when the ABS node reaches the memory scale up or scale down limits in the configuration. The reason for reaching scale up limit can be because of large number of access log files coming from ASE. Scale down limit could be reached because of low number of access logs coming from ASE.Resolution: If ABS reaches scale up limit, add another ABS node to the cluster. If the system utilization is low, you can remove an ABS node from the cluster. |
| CPU scale up or scale down                                                                                | Cause: ABS sends an email alert when the ABS node reaches the CPU scale up or scale down limits in the configuration. The reason for reaching scale up limit can be because of large number of access log files coming from ASE. Scale down limit could be reached because of low number of access logs coming from ASE.Resolution: If ABS reaches scale up limit, add another ABS node to the cluster. If the system utilization is low, you can remove an ABS node from the cluster.    |
| Disk scale up or scale down                                                                               | Cause: ABS sends an email alert when the ABS node reaches the disk scale up or scale down limits in the configuration. The reason for reaching scale up limit can be because of large number of access log files coming from ASE. Scale down limit could be reached because of low number of access logs coming from ASE.Resolution: If ABS reaches scale up limit, add another ABS node to the cluster. If the system utilization is low, you can remove an ABS node from the cluster.   |
| License *\<path>* is invalid. ABS will shut down now                                                      | Cause: ABS sends this email alert when ABS does not have correct permissions to read the license file from the configured path, or there is a typing error in the name of the license file.Resolution: Validate current license file path. Also check for file permissions of the license file.                                                                                                                                                                                           |
| ABS license at *\<path>* has expired. Please renew your license.                                          | Cause: ABS sends this email alert when ABS license has expired. The license expires at the end of the license period.Resolution: Renew your ABS license.                                                                                                                                                                                                                                                                                                                                  |
| Maximum transaction limit reached for the current month                                                   | ABS sends this warning message when ABS crosses the licensed monthly transaction limit.                                                                                                                                                                                                                                                                                                                                                                                                   |
| API DDoS Attack Type 1 or Login DoS detected between *\<timestamp>* and *\<timestamp>* on node *\<value>* | ABS sends this warning message when it detects an API DDoS attack type 1 or a Login DoS attack.                                                                                                                                                                                                                                                                                                                                                                                           |
| MongoDB primary node is down                                                                              | Cause: ABS sends this email alert when MongoDB process is unavailable due to a shortage in memory or CPU. This alert can also trigger because of network issues for MongoDB node.Resolution: Check MongoDB Primary node status to bring it back online or add additional secondary node if needed.                                                                                                                                                                                        |

---

---
title: ABS CLI commands
description: The API Behavioral Security (ABS) command-line interface (CLI) provides basic commands and obfuscation commands.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_cli
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_cli.html
revdate: April 3, 2024
---

# ABS CLI commands

The API Behavioral Security (ABS) command-line interface (CLI) provides basic commands and obfuscation commands.

**Basic commands**

| Command         | Definition                                                             | Syntax                                                                                                                                                                                                                                                                                                   |
| --------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Start ABS       | Starts ABS. Run the command from`/opt/pingidentity/abs/bin` directory. | `./start.sh`                                                                                                                                                                                                                                                                                             |
| Stop ABS        | Stops ABS. Run the command from`/opt/pingidentity/abs/bin` directory.  | `./stop.sh`                                                                                                                                                                                                                                                                                              |
| Help            | Displays `cli.sh` help.                                                | `./cli.sh help`                                                                                                                                                                                                                                                                                          |
| Update Password | Changes ABS admin password.                                            | `./cli.sh update_password \{-u admin}`                                                                                                                                                                                                                                                                   |
| Update Keys     | Updates access and secret keys.                                        | `./cli.sh -u admin -p admin update_keys -ak <access key> -sk <secret key>`&#xA;&#xA;You should use the update\_keys command to change the keys. However, you can directly edit the abs\_init.js file when changing the default access and secret keys for the first time after installing ABS AI engine. |

**Obfuscation commands**

| Command             | Definition                                                          | Syntax                                       |
| ------------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| Generate Master Key | Generates the master obfuscation key `abs_master.key`.              | `./cli.sh -u admin -p admin generate_obfkey` |
| Obfuscate Password  | Obfuscates the passwords configured in various configuration files. | `./cli.sh -u admin -p admin obfuscate_keys`  |

---

---
title: ABS cluster
description: An API Behavioral Security (ABS ) cluster consists of stateless ABS nodes communicating with a MongoDB replica set.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_cluster
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_cluster.html
revdate: April 3, 2024
section_ids:
  configuring-an-abs-cluster: Configuring an ABS cluster
  about-this-task: About this task
  steps: Steps
---

# ABS cluster

An API Behavioral Security (ABS ) cluster consists of stateless ABS nodes communicating with a MongoDB replica set.

Each ABS node connects to the MongoDB cluster to obtain cluster configuration information that describes peer nodes. ABS nodes themselves do not communicate with each other; they periodically send heartbeats to MongoDB with status information. Each ABS node exposes:

* REST APIs for log streaming between ABS and API Security Enforcer (ASE)

* REST APIs between ABS and management applications which fetch metrics, anomalies, attack types, backend error, blocked connections, flow control, and cluster status.

An ABS cluster is depicted in the following diagram.

![ABS cluster as described in the text.](../_images/cmc1564009056695.png)

## Configuring an ABS cluster

### About this task

To configure an API Behavioral Security (ABS) cluster:

### Steps

1. [Install MongoDB in a replica set](../installing_pingintelligence_for_apis/pingintelligence_abs_engine_installation.html)

2. [Connect ABS to MongoDB](../installing_pingintelligence_for_apis/pingintelligence_connect_abs_to_mongodb.html)

3. To create an ABS cluster, add an ABS node and connect it to MongoDB primary node.

   |   |                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------- |
   |   | Since ABS forms a stateless cluster, the information of all the nodes in the cluster is fetched by ABS nodes from MongoDB. |

4. To scale down ABS cluster, [stop](pingintelligence_starting_stopping_abs.html) the ABS node that you wish to remove from the cluster.

   1. Edit the `abs.properties` file to remove MongoDB Internet Protocol (IP) *(tooltip: \<div class="paragraph">
      \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
      \</div>)* address.

---

---
title: ABS configuration - abs.properties
description: The API Behavioral Security (ABS) configuration file abs.properties is located in the ABS config directory.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_configuration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_configuration.html
revdate: April 3, 2024
---

# ABS configuration - abs.properties

The API Behavioral Security (ABS) configuration file `abs.properties` is located in the ABS `config` directory.

The following table explains the parameters and provides recommended values.

| Parameter                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ABS Internet Protocol (IP) *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)* , port, log level, and Java KeyStore (JKS) *(tooltip: \<div class="paragraph">&#xA;\<p>A repository of security certificates and corresponding private keys.\</p>&#xA;\</div>)* password |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `timezone`                                                                                                                                                                                                                                                                                                                                                                            | Set the timezone to `utc` or` local`. The default timezone is `utc`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `management_port`                                                                                                                                                                                                                                                                                                                                                                     | Port for ABS to API Security Enforcer (ASE) and REST application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* to ABS communication.The default value is 8080.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `log_level`                                                                                                                                                                                                                                                                                                                                                                           | Log detail captured. The default is INFO.Additional options - DEBUG, ERROR, WARN, FATAL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `jks_password`                                                                                                                                                                                                                                                                                                                                                                        | The password of the JKS Keystore. ABS ships with a default obfuscated password. You can reset the password and obfuscate it. This password should be the same that you would use in [importing your CA-signed certificate](pingintelligence_import_existing_ca_signed_certificates.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ABS performance configurations                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `system_memory`                                                                                                                                                                                                                                                                                                                                                                       | Memory size in MB allocated to run machine learning jobs. Recommended to be at least 50% of system memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `queue_size`                                                                                                                                                                                                                                                                                                                                                                          | Do not change the value of this parameter. The default is 10.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ABS email configurations for alerts and reporting                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `enable_emails`                                                                                                                                                                                                                                                                                                                                                                       | Enable (`true`) or disable (`false`) ABS email notifications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `sender_email`                                                                                                                                                                                                                                                                                                                                                                        | Email address used for sending email alerts and reports.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `receiver_email`                                                                                                                                                                                                                                                                                                                                                                      | Email address notified about alerts and reports. If you want more than one person to be notified, use an email alias.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `email_password`                                                                                                                                                                                                                                                                                                                                                                      | Password of sender's email account.&#xA;&#xA;You can leave this field blank if your SMTP server does not require authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `smtp_port`                                                                                                                                                                                                                                                                                                                                                                           | Port number of SMTP server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `smtp_host`                                                                                                                                                                                                                                                                                                                                                                           | Hostname of SMTP server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `smtp_ssl`                                                                                                                                                                                                                                                                                                                                                                            | Set to `true` if you want email communication to be over SSL. Make sure that the SMTP server supports SSL. If you set `smtp_ssl` to `true` and the SMTP server does not support SSL, email communication falls back to the non-SSL channel. The default value is `true`.Set it to false if email communication is over a non-SSL channel. The email communication will fail if you set the parameter to `false`, but the SMTP server only supports SSL communication.                                                                                                                                                                                                                                                                                                             |
| `smtp_cert_verification`                                                                                                                                                                                                                                                                                                                                                              | Set to `true` if you want ABS to verify the SMTP server's SSL certificate. The default value is `false`.If you set it to `false`, ASE does not verify SMTP server's SSL certificate; however, the communication is still over SSL.&#xA;&#xA;If you have configured an IP address as smtp\_host and set smtp\_cert\_verification to true, then make sure that the certificate configured on the SMTP server has the following:```
X509v3 extensions:
           X509v3 Key Usage:
              Key Encipherment, Data Encipherment
           X509v3 Extended Key Usage:
              TLS Web Server Authentication
           X509v3 Subject Alternative Name:
               IP Address: X.X.X.X
```Here `x.x.x.x` is the IP address is the address configured in `smtp_host`. |
| MongoDB configurations                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `mongo_rs`                                                                                                                                                                                                                                                                                                                                                                            | Comma separated MongoDB replica set URI. A maximum of three nodes can be configured.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `metadata_dbname`                                                                                                                                                                                                                                                                                                                                                                     | The MongoDB metadata database name.The default value is `abs_metadata`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `data_dbname`                                                                                                                                                                                                                                                                                                                                                                         | The MongoDB data database name.The default value is `abs_data`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `mldata_dbname`                                                                                                                                                                                                                                                                                                                                                                       | The MongoDB machine learning database name.The default value is `abs_mldata`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `mongo_auth_mechanism`                                                                                                                                                                                                                                                                                                                                                                | Defines the method in which MongoDB authenticates. The possible values can be:- `NONE` - Set it to `NONE`, if authentication is not configured in MongoDB

- `DEFAULT` - Set it to `DEFAULT`, if you want to use native MongoDB username and password. Prove the values in the next two variables.

- `PLAIN` - Set it to `PLAIN`, if you want to use LDAP authentication. In this case, provide the LDAP username and password in the next two variables.                                                                                                                                                                                                                                                                                                                        |
| `mongo_username`                                                                                                                                                                                                                                                                                                                                                                      | Username of MongoDB.&#xA;&#xA;Required for MongoDB authentication                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `mongo_password`                                                                                                                                                                                                                                                                                                                                                                      | MongoDB password                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `mongo_ssl`                                                                                                                                                                                                                                                                                                                                                                           | Set it to `true` if MongoDB is configured to use SSL connections. The default value is `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `mongo_certificate`                                                                                                                                                                                                                                                                                                                                                                   | Set it to `true` if you want to verify MongoDB SSL server certificate when ABS connects to MongoDB. The default value is `false`.&#xA;&#xA;Make sure mongo\_ssl is set to true before setting mongo\_certificate to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ABS reporting node                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `dashboard_node`                                                                                                                                                                                                                                                                                                                                                                      | When `true`, designated as a dedicated Reporting or Dashboard node. This ABS node does not process log data or participate in an ABS cluster.The default value is `false`.&#xA;&#xA;Multiple nodes can be Reporting or Dashboard nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cloud and OAuth configurations&#xA;&#xA;The following parameters are applicable when ABS is running in cloud mode. These are preset configurations, which should not be edited.                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `bucket_name`                                                                                                                                                                                                                                                                                                                                                                         | The Amazon Web Services (AWS) *(tooltip: \<div class="paragraph">&#xA;\<p>An Amazon subsidiary providing cloud computing platforms.\</p>&#xA;\</div>)* S3 bucket name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `env_id`                                                                                                                                                                                                                                                                                                                                                                              | The environment id of the tenant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `deployment_type`                                                                                                                                                                                                                                                                                                                                                                     | The ABS deployment mode. Valid values are `cloud` or `onprem`. The default value is `onprem`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `oauth_audience`                                                                                                                                                                                                                                                                                                                                                                      | The audience claim of the access token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `oauth_issuer_whitelist`                                                                                                                                                                                                                                                                                                                                                              | The list of valid JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)* issuers from whom the tokens are expected.                                                                                                                                                                                                                                                                                                                                                                         |
| `oauth_jwks_endpoint`                                                                                                                                                                                                                                                                                                                                                                 | The JWKS endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

A sample `abs.properties` file is displayed below.

```
# Ping Identity Corporation, ABS config file
# All the keys should be present, leave blank value if not applicable

# Set the timezone to utc or local. The default timezone is utc.
timezone=utc
# REST API port
management_port=8080
# Log levels (ALL > DEBUG > INFO > WARN > ERROR > FATAL > OFF)
log_level=DEBUG
# Java KeyStore password
jks_password=OBF:AES:Q3vcrnj7VZILTPdJnxkOsyimHRvGDQ==:daYWJ5QgzxZJAnTkuRlFpreM1rsz3FFCulhAUKj7ww4=
# MongoDB replica set URI. For example, mongodb://<IP1>:<Port>,<IP2>:<Port>,<IP3>:<Port>. Maximum three nodes can be configured.
mongo_rs=mongodb://localhost:27017
# MongoDB Database
metadata_dbname=abs_metadata
data_dbname=abs_data
mldata_dbname=abs_mldata
# MongoDB authentication
# If authentication is not enabled in MongoDB, set the mongo_auth_mechanism to NONE
# The supported MongoDB authentication mechanisms are DEFAULT and PLAIN.
# If authentication mechanism is DEFAULT, provide MongoDB username and password for mongo_username
# and mongo_password. If authentication mechanism is PLAIN, provide external
# LDAP username and password in mongo_username and mongo_password.
mongo_auth_mechanism=DEFAULT
mongo_username=absuser
mongo_password=OBF:AES:Q3vcrnj7VZILTPdJnxkOsyimHRvGDQ==:daYWJ5QgzxZJAnTkuRlFpreM1rsz3FFCulhAUKj7ww4=
# Mongo DB SSL
# Set to true if Mongo DB instance is configured in SSL mode.
# By default, ABS will try to connect to Mongo using non-SSL connection
mongo_ssl=false
# Mongo DB Server Certificate Verification
# Set to true if Mongo DB instance is configured in SSL mode and you want to do the server certificate verification
# By default ABS will not verify the MongoDB server certificate
mongo_certificate=false
# Job queue size per node
queue_size=10
# Setting as true makes an ABS node for dashboard query only and does not participate in ABS cluster for log processing
dashboard_node=false
# Memory for webserver and streaming server (unit is in MB)
system_memory=4096
# E-mail alerts
enable_emails=false
# SMTP host
smtp_host=smtp.example.com
# SMTP port
smtp_port=587
# Set this value to true if smtp host support SSL
smtp_ssl=true
# Set this value to true if SSL certificate verification is required
smtp_cert_verification=false
# Sender email id
sender_email=sender@example.com
# Sender's email password
email_password=OBF:AES:UXzB+y+69Bn3xiX6N822ad4hf5IfNfJY9w==:T+QzM6qtc0+6MVsx4gU5p0LMHAI/y+w8DDsWv6VxVAk=
# Receiver's email id
receiver_email=receiver@example.com
# Set this value to appropriate AWS S3 Bucket name, if ABS is running in cloud mode
bucket_name=
# Set this value to appropriate Env Id, if ABS is running in cloud mode
env_id=
# Set this value to either cloud / onprem, as per the ABS running mode. By default set to onprem
deployment_type=onprem
# Token validation params
# Audience
oauth_audience=
# Issuer whitelist
oauth_issuer_whitelist=
# JWKS endpoint
oauth_jwks_endpoint=
```

---

---
title: ABS deny list reporting
description: API Behavioral Security (ABS) provides attacklist REST application programming interface (API) to complete the following two operations:
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_blacklist_reporting
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_blacklist_reporting.html
revdate: April 3, 2024
section_ids:
  reporting-active-and-expired-client-identifiers: Reporting active and expired client identifiers
  about-this-task: About this task
  steps: Steps
  deleting-individual-client-identifiers: Deleting individual client identifiers
  about-this-task-2: About this task
  steps-2: Steps
  example: Example:
  using-the-bulk-delete-option-for-client-identifiers: Using the bulk delete option for client identifiers
  about-this-task-3: About this task
  steps-3: Steps
  example-2: Example:
---

# ABS deny list reporting

API Behavioral Security (ABS) provides `attacklist` REST application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* to complete the following two operations:

* List the various client identifiers (API Key, OAuth token, Username, Cookie, and Internet Protocol (IP) *(tooltip: \<div class="paragraph">
  \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
  \</div>)* address) which are related to probable attack

* Delete the client identifiers which may be a cause of false positive

## Reporting active and expired client identifiers

API Behavioral Security (ABS ) provides an `attacklist` REST API with GET method to list active attacks in the system, expired attacks, and consolidated (active and expired) attacks together.

### About this task

The list of detected client identifiers depends on the [TTL set for the client identifiers](pingintelligence_ttl_client_identifiers_in_abs.html). The attack list reports the detected client identifiers (active or expired) for the queried period. The time-period is part of the API query parameter. `URL: /v4/abs/attacklist`

### Steps

* To report active detected attacks, use the following REST API URL to report the active client identifiers: `/v4/abs/attacklist?earlier_date=<>&later_date=<>&status=active`

  The API lists the active client identifiers for a time-period between `earlier_date` and `later_date`. PingIntelligence ASE fetches the active client identifiers list from ABS for blocking the clients.

* To report expired detected attacks, use the following REST API URL to report the expired client identifiers: `/v4/abs/attacklist?earlier_date=<>&later_date=<>&status=expired`

  The API lists the expired client identifiers for a time-period between `earlier_date` and `later_date`. The expiry of detected attacks in the system depends on the configured TTL.

* To report consolidated (active and expired) detected attacks, use the following REST API URL to report the consolidated client identifiers attacks: `/v4/abs/attacklist?earlier_date=<>&later_date=<>`

  The API lists all the client identifiers for a time-period between `earlier_date` and `later_date`.

## Deleting individual client identifiers

You can delete active client identifiers.

### About this task

The API *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* requires only the message body with a client identifier in their respective sections, to delete active client identifiers. The API checks if the client identifier is present in the blocklist or not before deleting. If you provide a client identifier which is not part of the blocklist, the API ignores such client identifiers.

### Steps

* Use the attacklist API with PUT method to delete the client identifiers:

  * `URL: /v4/abs/attacklist`

  * `Method: PUT`

    |   |                                                                                                                                                                                                                                                                                       |
    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | You can provide only specific section of a client identifier in the message body. For example, if you only want to delete specific usernames, then provide only the username section in the message body. Make sure that the `JavaScript Object Notation (JSON)` file is well-formed. |

    #### Example:

    The following is a sample message body for the attacklist API to delete client identifiers:

    ```json
    {
            "ips": [
                "192.168.4.10",
                "10.10.10.73",
                "10.1.1.4",
                "10.9.8.7"
            ],
            "cookies": {
                "PHPSESSIONID": [
                "Cookie1",
                "Cookie2"
                ],
            "JSESSIONID": [
                "Cookie3",
                "AnyCookie",
                "Cookie4"

            },
            "oauth_tokens": [
                "Token1",
                "Token2",
                "Token3"
            ],
            "api_keys": [
                "type2_api_key",
                "api_key_1",
                "api_key_2",
             ],
            "usernames": [
                "username1",
                "username2",
                "username3",
             ]
    }
    ```

    The following is a sample message body showing the client identifiers that were deleted:

    ```json
    {
      "message": "Success: The following attacks have been removed:",
      "date": "Thu Jun 09 03:39:12 UTC 2019",
      "attacklist": {
        "ips": [
                "192.168.4.10",
                "10.10.10.73",
                "10.1.1.4",
                "10.9.8.7"
        ],
        "cookies": {
          "PHPSESSIONID": [
                "Cookie1",
                "Cookie2"
          ],
          "JSESSIONID": [
                "Cookie3",
                "AnyCookie",
                "Cookie4"
          ]
        },
        "oauth_tokens": [
                "Token1",
                "Token2",
                "Token3"
        ],
        "api_keys": [
                "type2_api_key",
                "api_key_1",
                "api_key_2",
        ],
        "usernames": [
                "username1",
                "username2",
                "username3",
        ]
      }
    }
    ```

## Using the bulk delete option for client identifiers

You can use the bulk delete option to clear large numbers of false positive client identifiers.

### About this task

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | You can also use the bulk delete option to clear the blocklist in case of a reset. |

### Steps

1. To bulk delete client identifiers, use the ABS attacklist REST API with the DELETE method:

   * `URL: /v4/abs/attacklist`

   * `Method: DELETE`

2. To bulk delete all the entries of a client identifier or all client identifiers, configure the body of the attacklist.

   #### Example:

   The following is an example of the API *(tooltip: \<div class="paragraph">
   \<p>A specification of interactions available for building software to access an application or service.\</p>
   \</div>)* request:

   ```json
   {
   	delete_all: false,
   	delete_all_ips: true,
   	delete_all_cookies: true,
   	delete_all_oauth_tokens: false,
   	delete_all_api_keys: true,
   	delete_all_usernames: false,
   }
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In the sample request body, the attacklist API deletes all entries for IP *(tooltip: \<div class="paragraph">&#xA;\<p>The method by which data is sent across the internet from the source host to the destination host.\</p>&#xA;\</div>)*, cookies, and API keys. If, in the next time interval, the AI engine flags the same client identifiers, the blocklist is populated again. |

3. To permanently stop a false positive from being reported, tune the thresholds using the PingIntelligence Web GUI for the specific client identifier.

   The following table describes the options.

   | Option                    | Description                                                                                                                                                                                                                                                  |
   | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | `delete_all`              | This option overrides all the other configured options in the message body. If it is set to `true`, all the client identifiers are deleted irrespective of what their individual configuration is. Set it to `false`, if you want to exercise other options. |
   | `delete_all_ips`          | Set it true to delete all the IP addresses across all attack types from the blocklist.                                                                                                                                                                       |
   | `delete_all_cookies`      | Set it true to delete all the cookies across all attack types from the blocklist.                                                                                                                                                                            |
   | `delete_all_oauth_tokens` | Set it true to delete all the OAuth token across all attack types from the blocklist.                                                                                                                                                                        |
   | `delete_all_api_keys`     | Set it true to delete all the API Keys across all attack types from the blocklist.                                                                                                                                                                           |
   | `delete_all_usernames`    | Set it true to delete all the usernames across all attack types from the blocklist.                                                                                                                                                                          |

---

---
title: ABS directory structure
description: API Behavioral Security (ABS) creates directories as part of the installation process.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_directory_structure
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_directory_structure.html
revdate: April 3, 2024
---

# ABS directory structure

API Behavioral Security (ABS) creates directories as part of the installation process.

The directories are shown in the following table.

| Directory | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `config`  | Contains `abs.properties`, a Java properties file used to configure ABS.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `data`    | Stores logs sent by application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* Security Enforcer.                                                                                                                                                                                                                                       |
| `logs`    | Stores all ABS related logs.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `lib`     | For internal use. Do not change anything in this directory.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `bin`     | Contains various scripts to start and stop ABS.&#xA;&#xA;Do not edit the scripts in the bin directory.                                                                                                                                                                                                                                                                                                                                                                                   |
| `mongo`   | Contains the `abs_init.js` file used to load the default schema, secret key, and access key.                                                                                                                                                                                                                                                                                                                                                                                             |
| `util`    | Contains utilities to:- Check and Open MongoDB Default Port

- Purge the Processed Access Logs from ABS

- Purge ABS Data from MongoDB

- Various service and systemctl scripts

- Reset MongoDB script, and

- Update script to change the values of global configuration defined in `/pingidentity/abs/mongo/abs_init.js` file

- `open_ports_abs.sh:`Open the default ports 8080 and 9090 for ABS REST API and connectivity from ASE respectively. Run the script on the ABS machine. |

---

---
title: ABS external REST APIs
description: The following is a list of Ping Identity API Behavioral Security (ABS) application programming interface (API).
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_external_rest_api
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_external_rest_api.html
revdate: April 3, 2024
---

# ABS external REST APIs

The following is a list of Ping Identity API Behavioral Security (ABS) application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*.

The sample outputs produced are for the Admin user. You can generate the output for the restricted user as well where the cookie, token, and API keys are obfuscated. For more information on different type of users for the ABS External REST APIs, see [ABS Users for API Reports and Dashboard](pingintelligence_abs_users_api_reports.html).

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | The ":" (colon) is a restricted character and cannot be used in access and secret key headers in ABS external REST APIs. |

* [Admin REST API](pingintelligence_admin_rest_api.html)

* [TTL Update REST API](pingintelligence_ttl_client_identifiers_in_abs.html)

* [Global Config Update REST API](pingintelligence_global_configuration_update_rest_api.html)

* [Discovery REST API](pingintelligence_discovery_rest_api.html)

* [Threshold REST API](pingintelligence_threshold_rest_api.html)

* [Reset Trained API](../managing_pingintelligence_for_apis/pingintelligence_resetting_trained_apis.html)

* [Decoy API](pingintelligence_decoy_rest_api.html)

* [IP Metrics REST API](pingintelligence_metrics_rest_api.html)

* [API Key Metrics REST API](pingintelligence_api_key_metrics_rest_api.html)

* [Token Metrics REST API](pingintelligence_oath2_token_metrics_rest_api.html)

* [Username Metrics REST API](pingintelligence_username_metrics_rest_api.html)

* [Anomalies REST API](pingintelligence_anomalies_rest_api.html)

* [Token Forensics REST API](pingintelligence_oath2_token_forensics_rest_api.html)

* [IP Forensics REST API](pingintelligence_ip_forensics_rest_api.html)

* [Cookie Forensics REST API](pingintelligence_cookie_forensics_rest_api.html)

* [API Key Forensics API REST](pingintelligence_api_keys_forensics_rest_api.html)

* [Username Forensics REST API](pingintelligence_username_forensics_rest_api.html)

* [Attack Type REST API](pingintelligence_attack_types_rest_websocket_apis.html)

* [Flow Control REST API](pingintelligence_flow_control_rest_api.html)

* [Blocked Connection REST API](pingintelligence_blocked_connection_rest_api.html)

* [Backend Error REST API](pingintelligence_backend_error_rest_api.html)

* [List Valid URLs REST API](pingintelligence_list_valid_urls_rest_api.html)

* [List Hacker's URLs REST API](pingintelligence_list_hackers_url_rest_api.html)

---

---
title: ABS log messages
description: The following table lists the critical log messages from abs.log and aad.log file.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_log_messages
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_log_messages.html
revdate: April 3, 2024
---

# ABS log messages

The following table lists the critical log messages from `abs.log` and `aad.log` file.

| Log message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Warning:-Maximum Transaction limit is reached for this month                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | This message is logged in `abs.log` when the transaction limit is reached for the allotted license usage. For more information, see [Configuring and updating an ABS license](pingintelligence_abs_license.html)                      |
| Warning:- Attempt to shutdown ABS from 127.0.0.1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | This message is logged in `abs.log` when shutdown of API Behavorial Security (ABS) AI engine is initiated.                                                                                                                            |
| Warning:- Failed to delete IPs from IOCs - try again                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | This message is logged in `abs.log` when the Attack list REST API encounters an issues while deleting the IP address from the deny list.                                                                                              |
| Warning:- Failed to delete tokens from IOCs - try again                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This message is logged in `abs.log` when the Attack list REST API encounters an issues while deleting the OAuth token from the deny list                                                                                              |
| Warning:- Failed to delete usernames from IOCs - try again                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | This message is logged in `abs.log` when the Attack list REST API encounters an issues while deleting the usernames from the deny list.                                                                                               |
| Warning:- Failed to delete API keys from IOCs - try again                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | This message is logged in `abs.log` when the Attack list REST API encounters an issues while deleting the API Keys from the deny list.                                                                                                |
| Warning:- License is Expired. Please renew your license                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This message is logged in `abs.log` when ABS license has expired. For more information, see [Configuring and updating an ABS license](pingintelligence_abs_license.html)                                                              |
| Warning:- MongoDB primary node is down                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | This message is logged in `abs.log` when a MongoDB connection failure occurs.                                                                                                                                                         |
| Warning:- Stream init-wait interrupted                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | This message is logged in `abs.log` when streaming of access log files is interrupted.                                                                                                                                                |
| Warning:- File system usage reached configured value of: 80% ABS will not accept new logs from ASE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This message is logged in `abs.log` when ABS stops accepting access log files from ASE because of maximum use of filesystem.                                                                                                          |
| Warning:- Error while closing mongo connections                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | This message is logged in `abs.log` when shutdown of MongoDB connection was not successful.                                                                                                                                           |
| Warning:- Error while loading anomaly dictionary from mongo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | This message is logged in `abs.log` when writing of anomalies to data directory fails.                                                                                                                                                |
| Warning:- Error while closing file handle for stream config                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | This message is logged in `abs.log` when an error occurs while closing the streaming configuration file.                                                                                                                              |
| Error: exception while parsing license file`/opt/pingidentity/abs/config/PingIntelligence.lic`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | This message is logged in `abs.log` when an error occurs while reading the license file.Add the file named `PingIntelligence.lic` to the specified path with read permission and restart the ABS AI engine                            |
| Error: License `/opt/pingidentity/abs/config/PingIntelligence.lic` is invalid. ABS will shut down now.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | This message is logged in `abs.log` when an error is encountered while validating the license file.Provide a valid license file and restart the ABS AI engine                                                                         |
| ABS will shut down now                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | This message is logged in `abs.log` when your free ABS license expires.                                                                                                                                                               |
| Attempting to initialize abs, but abs is already in *\<message>*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | This message is logged in `abs.log` when another ABS process is already running.                                                                                                                                                      |
| error while loading `abs.properties` *\<Custom run-time message>*The various custom error messages could be:- property *\<abs\_propertie>*is missing

- invalid value for property log\_level. Value should be string and member of \[ALL,DEBUG,INFO,WARN,ERROR,FATAL,OFF]

- property management\_port is missing

- invalid value for property management\_port, value should be integer and ( >=1 && ⇐65535 )

- invalid value for property jks\_password, obfuscation of password failed. Please make sure you are using the correct `config/abs_master.key` file

- invalid value for property jks\_password, value should be obfuscated using the 'bin/cli.sh -u admin -p \<password> obfuscate\_keys' command

- invalid value for property host\_ip, value should be string and ipv4 address

- property enable\_emails is missing

- invalid value for property smtp\_host value should be string and should be as per rfc1024 and rfc1123 | This message is logged in `abs.log` when:- Error occurs when `abs.properties` file is not configured with log\_level specifications

- Error occurs when `abs.properties` file is not configured with management\_port specifications |
| error while loading`abs_resources.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | This message is logged in `abs.log` when `abs_resources.properties` doesn't contain values for memory and CPU parameters.                                                                                                             |
| error while initializing mongodb replica set connections                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This message is logged in `abs.log` when MongoDB initialization fails and cannot access a read or write client for connections.                                                                                                       |
| error while reading enable\_ssl key from mongo master                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | This message is logged in `abs.log` when MongoDB client tries to fetch the key from MongoDB collections.                                                                                                                              |
| error while reading root\_api\_attack key from mongo master                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | This message is logged in `abs.log` when MongoDB client tries to fetch the key from MongoDB collections.                                                                                                                              |
| error while reading `/config/abs.properties`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | This message is logged in `abs.log` while loading and validating the `abs.properties` file. Check whether file exists and its permission.                                                                                             |
| invalid value for property jks\_password, value should be obfuscated using the 'bin/cli.sh -u admin -p *\<password>* obfuscate\_keys' command                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | This message is logged in `abs.log` when an error occurs while deobfuscating the jks\_password using the master\_key.                                                                                                                 |
| error while loading auth keys from metadata db in mongo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This message is logged in `abs.log` when MongoDB is not accessible.                                                                                                                                                                   |
| error while loading restricted user auth keys from metadata db in mongo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This message is logged in `abs.log` when MongoDB is not accessible.                                                                                                                                                                   |
| Unable to read `<abs_root_dir>/config/abs.jks` file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This message is logged in `abs.log` when `abs.jks` is not created properly or could not read the file or there is a permission issue.                                                                                                 |
| error while starting management server *\<runtime exception>*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | This message is logged in `abs.log` when there is an issue when ABS starts.                                                                                                                                                           |
| API Behavioral Security stopped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | This message is logged in `abs.log` when ABS is shut down.                                                                                                                                                                            |
| MongoDB heartbeat failure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | This message is logged in `abs.log` when ABS is unable to connect to MongoDB primary node.                                                                                                                                            |
| ABS started successfully                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This message is logged in `abs.log` when ABS starts.                                                                                                                                                                                  |

---

---
title: ABS logs
description: The active API Behavioral Security (ABS) log file abs.log is located in the logs directory and rotated every 24 hours at midnight local time.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_logs
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_logs.html
revdate: April 3, 2024
---

# ABS logs

The active API Behavioral Security (ABS) log file `abs.log` is located in the logs directory and rotated every 24 hours at midnight local time.

The rotated log files append timestamps to the name and follow the naming convention of `abs.log.`*\<yyyy>*-*\<mm>*-*\<dd>* (for example, `abs.log.2018-11-24`).

Here is an example:

```
-rw-r--r--. 1 root root 68K Apr 25 23:59 abs.log.2019-04-25
-rw-r--r--. 1 root root 68K Apr 25 23:59 abs.log.2019-04-24
-rw-r--r--. 1 root root 68K Apr 26 23:59 abs.log.2018-04-26
-rw-r--r--. 1 root root 158K Apr 27 23:59 abs.log.2018-04-27
-rw-r--r--. 1 root root 32K Apr 28 11:21 abs.log
```

The ABS log file contains `INFO` messages (for example, ABS started, MongoDB status) and `ERROR` messages (for example, MongoDB is not reachable). The log files also contains entry of all the email alerts sent.

Here is a snippet of an `abs.log` file:

```
2019-04-28 11:16:45 INFO - starting abs periodic actions
2019-04-28 11:16:45 INFO - MongoDB heartbeat success
2019-04-28 11:16:45 INFO - notification node not set.
2019-04-28 11:16:45 INFO - training period 1 hours.
2019-04-28 11:16:45 INFO - system threshold update interval 1 hour(s).
2019-04-28 11:16:45 INFO - api discovery interval 1 hour(s).
2019-04-28 11:16:45 INFO - subpath limit: 100
2019-04-28 11:16:45 INFO - ABS started successfully...
2019-04-28 11:17:45 INFO - MongoDB heartbeat success
2019-04-28 11:19:45 ERROR - MongoDB heartbeat failure
```

---

---
title: ABS ports
description: API Behavioral Security (ABS) uses ports 8080 and 27017. The table below shows a description of each port.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_ports
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_ports.html
revdate: April 3, 2024
section_ids:
  check-and-open-mongodb-default-port: Check and open MongoDB default port
  check-and-open-mongodb-default-port-2: Check and open MongoDB default port
---

# ABS ports

API Behavioral Security (ABS) uses ports 8080 and 27017. The table below shows a description of each port.

| Port number | Description                                                                                                                                                                                                                                                                                                                               |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 8080        | This port is used by API Security Enforcer (ASE) to log in to ABS and also used by Postman to access data to generate application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* reports |
| 27017       | Default port for MongoDB                                                                                                                                                                                                                                                                                                                  |

## Check and open MongoDB default port

MongoDB's default port for connection with ABS is 27017. Run the `check_ports_abs.sh` script on the ABS machine to determine whether MongoDB's default port is available. Provide MongoDB host IP address and default port as arguments. For example:`/opt/pingidentity/abs/util/check_ports_abs.sh \{MongoDB IPv4:[port]}`

## Check and open MongoDB default port

Run the `check_ports_abs.sh` script on the ABS machine to determine whether MongoDB's default port is available. Input the MongoDB host IP address and default port (27017) as arguments. For example:

`/opt/pingidentity/util/check_ports_abs.sh \{MongoDB IPv4:[port]}`

Run the script for MongoDB primary and secondary nodes. If the default ports are not accessible, open the port from the MongoDB machine.

---

---
title: ABS reports
description: API Behavioral Security (ABS) sends an e-mail report every 24 hours at midnight, 00:00:00 hours (local system time).
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_reports
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_reports.html
revdate: April 3, 2024
---

# ABS reports

API Behavioral Security (ABS) sends an e-mail report every 24 hours at midnight, 00:00:00 hours (local system time).

Each report includes values for the following parameters:

* ABS Node Status: resource utilization of CPU, file system, and operating system

* ASE Logs Processed: Compressed file size of ASE logs processed in 24 hours

* Total Requests: The number of requests in the processed log files in 24 hours

* Success: The total number of requests which got a 200-OK response

* Total Anomalies: Total number of anomalies detected across APIs in 24 hours

* Total IOC: Total number of attacks detected in 24 hours

* When: The time when the email report was sent

* Where: The ABS node that sent the email report

* MongoDB node IP address and status

Following is a sample ABS email template:

```
Dear DevOps,
    Please find the daily report generated by 192.168.11.166 at 2019-Jun-25 00:02:00 UTC
===================Cluster Details=============
ASE Logs Processed: 93.78MB
Total Request: 678590
Success: 596199
Total Anomalies: 7
Total IOC: 2
When : 2019-Jun-25 00:02:00 UTC
Where: 192.168.11.166

==================Node1 ===================
Host : 192.168.11.166
OS : Red Hat Enterprise Linux Server release 7.5 (Maipo)
CPU : 24
Memory : 62G
Filesystem : 39%
===========================================

================Mongo1 ====================
Host : 192.168.11.162
Status : up
===========================================

================Mongo2 ====================
Host :  192.168.11.164
Status : up
===========================================

================Mongo3 ====================
Host :  192.168.11.1685
Status : up
===========================================

===========================================
Best,
API Behavioral Security.
```

---

---
title: ABS REST API format
description: API Behavioral Security (ABS) provides external REST APIs.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_rest_api_format
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_rest_api_format.html
revdate: April 3, 2024
section_ids:
  abs-api-query-format: ABS API query format
---

# ABS REST API format

API Behavioral Security (ABS) provides external REST APIs.

External REST APIs are used to access JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* reports providing deep insight into the following:

* Attack Forensics and Compliance Reporting – attacks and anomalous behavior on APIs.

* API Metrics – API client and traffic details.

* Administrative – ABS system information.

* API Security Enforcer – decoy API, blocked connections, flow control, and backend error reporting.

A REST client can securely query each ABS API and receive data back in JSON format. REST client program options include using:

* Postman App for Google Chrome browser.

* Java, Python, C Sharp, or similar languages.

* Java client program (for example, Jersey).

* C sharp client program (for example, RestSharp).

The diagram shows the process for a REST API client to connect to an ABS API.

![Diagram process for REST API client to connect to an ABS API as described in the text.](../_images/qri1564009060356.png)

## ABS API query format

ABS API offers a common format with a consistent syntax for request parameters. Detailed information and format of all ABS REST APIs are included in [ABS external REST APIs](pingintelligence_abs_external_rest_api.html).

Query parameters for most APIs are shown in the table below:

| Field          | Description                                                                                                                                                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_name`     | The API name to query for results.                                                                                                                                                  |
| `earlier_date` | The time to check for results going back in time. For example, to check results from April, 10, 6:00 p.m. to April, 14, 3:00 p.m., the `earlier_date` would be April, 10, 6:00 p.m. |
| `later_date`   | The time to check the results back in time. For example, to check results from April 10 , 6:00 p.m. to April, 14, 3:00 p.m., the `later_date` would be April, 14, 6:00 p.m.         |

The following `access_key` and `secret_key` are the keys that were defined in the `abs_init.js` file.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | The ":" (colon) is a restricted character and cannot be used in access and secret key. |

* `x-abs-ak `and `x-abs-ak-ru: `access\_key

* `x-abs-sk `and `x-abs-sk-ru: `secret\_key

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The start and end time are based on the log file data, that is, the local time where data was captured and not of the location where results are analyzed. |

---

---
title: ABS users for API reports
description: API Behavioral Security (ABS) has two types of users to access the application programming interface (API) reports and PingIntelligence Dashboard.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_abs_users_api_reports
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_abs_users_api_reports.html
revdate: April 3, 2024
---

# ABS users for API reports

API Behavioral Security (ABS) has two types of users to access the application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* reports and PingIntelligence Dashboard.

The API reports displayed is based on the type of user accessing the reports. The two users are:

* Admin user: An Admin user has complete access to API reports. All the cookies, tokens, API keys, and Username are visible in the reports. Use the following headers in the API report URL to access API reports as an Admin user:

  * `x-abs-ak (access key header)`

  * `x-abs-sk (secret key header)`

* Restricted user: A Restricted user has limited access to the API reports. The Restricted user can view the API reports however the cookies, tokens, and API keys are obfuscated. Use the following headers in the API report URL to access API reports as an Admin user:

  * `x-abs-ak-ru (access key header)`

  * `x-abs-sk-ru (secret key header)`

  The restricted user can access all the API Reports except:

  * Threshold API

  * Cookie, OAuth2 Token, Internet Protocol (IP) *(tooltip: \<div class="paragraph">
    \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
    \</div>)*, API Key, and Username Forensics APIs

For a complete list of external REST APIs, see [ABS External REST APIs](pingintelligence_abs_external_rest_api.html).

The default access and secret key are configured in the `opt/pingidentity/mongo/abs_init.js` file. Following is a snippet of the `abs_init.js` showing the default passwords for both type of users.

```
db.auth_info.insert({
 "access_key": "abs_ak",
 "secret_key": "abs_sk",
 "access_key_ru" : "abs_ak_ru",
 "secret_key_ru" : "abs_sk_ru"
});
```

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use `update_keys` CLI command to change access and secret keys. For more information, see [ABS CLI commands](pingintelligence_abs_cli.html). |

---

---
title: Access logs
description: Access logs are generated for port 80 (default port) and 443 (default port) traffic. Each Balancer process has a corresponding Access log file (that is. two port 80 Balancer processes and two port 443 Balancer processes require four log files). The log file name format is <protocol><port>_pid<process-ID>access<date>.log.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_access_logs
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_access_logs.html
revdate: May 6, 2024
---

# Access logs

Access logs are generated for port 80 (default port) and 443 (default port) traffic. Each Balancer process has a corresponding Access log file (that is. two port 80 Balancer processes and two port 443 Balancer processes require four log files). The log file name format is `<protocol><port>_pid<process-ID>access<date>.log`.

The following are examples for port 80 and port 443:

* `http_ws_80_pid_19017_access_2018-01-22_13-10.log`

* `https_wss_443_pid_19018_access_2018-01-22_13-10.log`

Access logs are rotated every 10 minutes and archived. The archived log file format has `.gz` at the end of the log file name, for example `http_ws_80_pid_19017_access_2018-01-22_13-10.log.gz`.

ASE sends all archived log files to API Behavioral Security (ABS) to detect attacks using machine learning algorithms. The files are then moved to the `logs/abs_uploaded` directory.

The following snippet shows an example log file:

```
-rw-r--r--. 1 root root 0 Aug 10 13:10 http_ws_80_pid_0access2018-01-22_13-10.log
-rw-r--r--. 1 root root 0 Aug 10 13:10 https_wss_443_pid_0access2018-01-22_13-10.log
-rw-r--r--. 1 root root 0 Aug 10 13:10 http_ws_80_pid_19010access2018-01-22_13-10.log
-rw-r--r--. 1 root root 0 Aug 10 13:10 http_ws_80_pid_19009access2018-01-22_13-10.log
-rw-r--r--. 1 root root 0 Aug 10 13:10 https_wss_443_pid_19022access2018-01-22_13-10.log
-rw-r--r--. 1 root root 0 Aug 10 13:10 https_wss_443_pid_19017access2018-01-22_13-10.log
-rw-r--r--. 1 root root 33223 Aug 10 13:11 balancer.log
-rw-r--r--. 1 root root 20445 Aug 10 13:11 controller.log
-rw-r--r--. 1 root root 33244 Aug 10 13:11 balancer_ssl.log
```

---

---
title: Accessing the PingIntelligence Dashboard
description: "Access the PingIntelligence for APIs Dashboard from a browser at the default Uniform Resource Locator (URL): https://<pi_install_host>:8030."
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_access_dashboard
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_access_dashboard.html
revdate: May 30, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Accessing the PingIntelligence Dashboard

Access the PingIntelligence for APIs Dashboard from a browser at the default Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">
\<p>Identifies a resource according to its internet location.\</p>
\</div>)*: https\://*\<pi\_install\_host>*:8030.

## About this task

There are two preconfigured login users in PingIntelligence for APIs Dashboard:

* `admin`

* `ping_user`

Multiple users can share the `admin` and `ping_user` logins simultaneously on PingIntelligence Dashboard. The admin user has access to all PingIntelligence Dashboard functions. A `ping_user` can only view the application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* dashboards.

The PingIntelligence Dashboard is categorized into the following components:

| Dashboard Component   | Description                           |
| --------------------- | ------------------------------------- |
| **Main Dashboard**    | Available for `admin` and `ping_user` |
| **APIs**              | Available only for `admin` user       |
| **Discovered APIs**   | Available only for `admin` user       |
| **Attack Management** | Available only for `admin` user       |
| **License**           | Available only for `admin` user       |
| **Active Sessions**   | Available only for `admin` user       |
| **Settings**          | Available only for `admin` user       |

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For further information on dashboard features, usage, and administration, see [PingIntelligence Dashboard](pingintelligence_dashboard.html). |

## Steps

1. At the sign-on prompt, sign on as `admin` or `ping_user`.

   The default password for both the users is `changeme`.

   |   |                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must change the default password for production deployments. However, in a Docker Proof of Concept deployment, use the default password. |

   ![A screenshot of the PingIntelligence Dashboard sign-on page.](../_images/nfq1577157837946.png)

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | If the Dashboard is not accessible, check if the default port (8030) was changed by your system administrator. |

2. **Optional:** Change the password using the following command-line interface (CLI) command:

   ```
   #  <pi_install_dir>/webgui/bin/cli.sh -u admin update_ui_password --username -value  <admin or ping_user>  --new-password -p
   Enter admin password >  <current admin password>
   Enter new password >  <new password>
   Reenter new password >  <new password>
   success: password updated.
   ```

3. **Optional:** To configure the maximum number of active sessions, set the `pi.webgui.session.max-active-sessions` parameter in the `<pi_install_dir>/webgui/config/webgui.properties` file.

   The default value is 50.

4. **Optional:** To delete active sessions, enter the following command:

   ```
   #  <pi_install_dir>/webgui/bin/cli.sh -u  <username>  -p  <password>  delete_sessions
   ```

   |   |                                                                        |
   | - | ---------------------------------------------------------------------- |
   |   | You need to have admin user privileges to delete active user sessions. |

   ### Result:

   The current active users will be prompted to sign on again to the Dashboard.

---

---
title: Activating API cybersecurity
description: The API Security Enforcer (ASE) provides real-time application programming interface (API) cybersecurity using the list of attacks generated by the PingIntelligence for APIs AI Engine.
component: pingintelligence
version: 5.2
page_id: pingintelligence:pingintelligence_reference_guide:pingintelligence_activate_api_cybersecurity
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/pingintelligence_reference_guide/pingintelligence_activate_api_cybersecurity.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  example-4: Example:
---

# Activating API cybersecurity

The API Security Enforcer (ASE) provides real-time application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* cybersecurity using the list of attacks generated by the PingIntelligence for APIs AI Engine.

## Before you begin

To activate real-time API cybersecurity, you must enable the ASE firewall.

## About this task

To enable or disable ASE's API cybersecurity feature:

## Steps

* To enable ASE's API cybersecurity:

  1. Run the `enable_firewall` command in the ASE command-line interface (CLI).

     ### Example:

     ```
     /opt/pingidentity/ase/bin/cli.sh -u admin -p admin enable_firewall
     Firewall is now enabled
     ```

  2. After enabling API Security, run the `status` CLI command to verify cybersecurity is enabled.

     ### Example:

     ```
     /opt/pingidentity/ase/bin/cli.sh status
     Ping Identity Inc., API Security Enforcer
     status : started
     http/ws : port 80
     https/wss : port 443
     firewall : enabled
     abs : disabled
     abs attack : disabled
     audit : enabled
     ase detected attack : disabled
     attack list memory : configured 128.00 MB, used 25.60 MB, free 102.40 MB
     ```

* To disable ASE's API cybersecurity:

  1. Run the `disable_firewall` CLI command.

     ### Example:

     ```
     /opt/pingidentity/ase/bin/cli.sh -u admin -p admin disable_firewall
     Firewall is now disabled
     ```

  2. Run the `status` CLI command to verify that cybersecurity is disabled.

     ### Example:

     ```
     /opt/pingidentity/ase/bin/cli.sh status
     Ping Identity Inc., API Security Enforcer
     status : started
     http/ws : port 80
     https/wss : port 443
     firewall : disabled
     abs : disabled
     abs attack : disabled
     audit : enabled
     ase detected attack : disabled
     attack list memory : configured 128.00 MB, used 25.60 MB, free 102.40 MB
     ```
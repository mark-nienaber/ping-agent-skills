---
title: ABS engine installation
description: The ABS engine installation process is summarized below:
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_abs_engine_installation
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_abs_engine_installation.html
revdate: April 3, 2024
---

# ABS engine installation

The ABS engine installation process is summarized below:

* Provision systems based on the queries per second (QPS)

* Install MongoDB in a replica set

* Install ABS engine

* Connect ABS engine to MongoDB

---

---
title: ABS reporting
description: The ABS AI engine generates attack, metric, and forensics reports, which are accessed using the ABS REST API to access JSON formatted reports.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_abs_reporting
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_abs_reporting.html
revdate: April 3, 2024
---

# ABS reporting

The ABS AI engine generates attack, metric, and forensics reports, which are accessed using the ABS REST API to access JSON formatted reports.

Ping Identity provides Postman collections to generate various API reports. You can use any other tool to access the reports using the URLs documented in the ABS Admin Guide.

---

---
title: ABS variable settings
description: The following table lists the variables that you can set for ABS.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_abs_variable_settings
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_abs_variable_settings.html
revdate: May 6, 2024
---

# ABS variable settings

The following table lists the variables that you can set for ABS.

| Variable                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `management_port`                     | Port for ABS to ASE and REST API to ABS communication. The default value is 8080.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `mongo_username` and `mongo_password` | MongoDB username and password. The default username is `absuser`, and the default password is `abs123`.                                                                                                                                                                                                                                                                                                                                                                                           |
| `mongo_cache_size`                    | If you are running all the PingIntelligence components on the same instance, keep the MongoDB cache size to a maximum of 25% of the system memory. If you are running MongoDB on a separate instance, keep the MongoDB cache size to a maximum of 40% of the system memory.                                                                                                                                                                                                                       |
| `mongo_ssl`                           | Default value is `true`. PingIntelligence deployment ships with a default self-signed certificate. Setting it to `false` establishes non-SSL connection between ABS and Mongo.                                                                                                                                                                                                                                                                                                                    |
| `mongo_certificate_verify`            | Set it to `true` if you want to verify MongoDB Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">&#xA;\<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>&#xA;\</div>)* server certificate when ABS connects to MongoDB. The default value is `false`.&#xA;&#xA;Make sure mongo\_ssl is set to true before setting mongo\_certificate\_verify to true. |
| `mongo_replica_set`                   | Name of the MongoDB replica set. Default name is `absrs01`.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `attack_initial_training`             | The number of hours that you want to train the AI model before it moves to the prediction mode. Default value is 24 hours.                                                                                                                                                                                                                                                                                                                                                                        |
| `system_memory`                       | Memory size in MB allocated to run machine learning jobs. Recommended to be at least 50% of system memory.                                                                                                                                                                                                                                                                                                                                                                                        |
| `access_key` and `secret_key`         | The access key and secret for the admin user. For more information on different ABS users, see [ABS users](../pingintelligence_reference_guide/pingintelligence_abs_users_api_reports.html).&#xA;&#xA;":" (colon) is a restricted character and not allowed in access key and secret key.                                                                                                                                                                                                         |
| `access_key_ru` and `secret_key_ru`   | The access key and secret for the restricted user. For more information on different ABS users, see [ABS users](../pingintelligence_reference_guide/pingintelligence_abs_users_api_reports.html).&#xA;&#xA;":" (colon) is a restricted character and not allowed in access key and secret key.                                                                                                                                                                                                    |
| `jks_password`                        | The password of the Java KeyStore (JKS) *(tooltip: \<div class="paragraph">&#xA;\<p>A repository of security certificates and corresponding private keys.\</p>&#xA;\</div>)*. The default password is `abs123`.                                                                                                                                                                                                                                                                                   |
| `Email default settings`              | Configure the following settings:- `enable_emails`: Set it to `true` for ASE to send email notifications. Default value is false.

- `smtp_host` and `smtp_port`

- `sender_email`: Email address used from which email alerts and reports are sent.

- `email_password`: Password of sender's email account.

- `receiver_email`: Email address at which the email alerts and reports are sent.                                                                                                  |
| `CLI admin password`                  | The default value for command-line interface (CLI) admin is `admin`. To change the password, you need the current password.                                                                                                                                                                                                                                                                                                                                                                       |
| `poc_mode`                            | Sets the mode in which the artificial intelligence (AI) engine sets the thresholds for the AI models. If set to `true`, AI engine sets thresholds at a lower value. It should be set to `true` only for a proof-of-concept deployment.                                                                                                                                                                                                                                                            |
| `consumer_user`                       | ABS consumer user in Kafka.Default: `abs_consumer`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `producer_user`                       | ABS producer user in Kafka.Default: `abs_producer`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `abs_groupid`                         | ABS group in Kafka.Default: `pi4api.abs`                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `consumer_authentication_password`    | ABS consumer user password.Default: `changeme`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `producer_authentication_password`    | ABS producer user password.Default: `changeme`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `min_insync_replicas`                 | Minimum number of insync replicas for data in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `transactions_topic`                  | ABS transaction topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `attacks_topic`                       | ABS attack topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `anomalies_topic`                     | ABS anomalies topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `discovery_topic`                     | ABS discovery topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `topic_partitions`                    | Number of partitions for topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `replication_factor`                  | Replication factor for topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `retention_period`                    | Retention period of data on topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `kafka_server_url`                    | Pre-existing Kafka `ip:port` that must be configured in `config/abs-defaults.yml`.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `kafka_custom_truststore_password`    | Pre-existing Kafka truststore password in `config/abs-defaults.yml`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `management_port`                     | API Publish service port.Default: `8050`                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `jks_password`                        | API Publish service JKS password.You can change the password for the JKS file. It will be generated during installation.                                                                                                                                                                                                                                                                                                                                                                          |
| `mongo_certificate_verify`            | Mongodb Server Certificate Verification for API Publish service.Default: `false`                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `server_ssl_key_alias`                | Alias for API Publish service SSL JKS file.Default: `pingidentity`                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `data_dbname`                         | API Publish service database name.Default: `abs_data`                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `meta_database`                       | API Publish service metadatabase name.Default: `abs_metadata`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `current_admin_password`              | API Publish service CLI password.Default: `admin`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `new_admin_password`                  | API Publish service new admin password.Default: `admin`                                                                                                                                                                                                                                                                                                                                                                                                                                           |

---

---
title: Accessing the PingIntelligence Dashboard
description: "Access the PingIntelligence for APIs Dashboard from a browser at the default Uniform Resource Locator (URL): https://<pi_install_host>:8030."
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_docker_access_dashboard
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_docker_access_dashboard.html
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

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For further information on dashboard features, usage, and administration, see [PingIntelligence Dashboard](../pingintelligence_reference_guide/pingintelligence_dashboard.html). |

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
title: Accessing the PingIntelligence security hardening guide
description: The PingIntelligence for APIs security hardening guide provides administrators with a single point of reference for configurations and best practices available to harden their PingIntelligence for APIs platform.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_security_hardening
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_security_hardening.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Accessing the PingIntelligence security hardening guide

The PingIntelligence for APIs security hardening guide provides administrators with a single point of reference for configurations and best practices available to harden their PingIntelligence for APIs platform.

## Before you begin

You must have a registered account to the [Ping Identity support and community portal](https://www.pingidentity.com/en/account/sign-on.html).

## About this task

One of the key security principles we follow at Ping is to make configurations secure by default. However, it is not always possible to create one-size-fits-all security configurations. This guide contains recommendations on how PingIntelligence administrators can further harden their platform based on their individual needs.

The recommendations are grouped by different PingIntelligence functional components. When deploying a component in PingIntelligence, see the corresponding section in the [PingIntelligence security hardening guide](https://support.pingidentity.com/s/article/PingIntelligence-Security-Hardening-Guide).

To access to PingIntelligence security hardening guide:

## Steps

* Go to the [PingIntelligence security hardening guide](https://support.pingidentity.com/s/article/PingIntelligence-Security-Hardening-Guide) and sign on to your Ping account.

## Next steps

If you need further assistance, contact the Ping Identity Sales team.

---

---
title: Adding APIs to ASE
description: After the policy has been deployed to Apigee using the PingIntelligence automated policy tool, add APIs to ASE.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_add_apis_ase
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_add_apis_ase.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# Adding APIs to ASE

After the policy has been deployed to Apigee using the PingIntelligence automated policy tool, add APIs to ASE.

## About this task

Refer to the following topics to define and add APIs to ASE:

## Steps

* [API naming guidelines](https://docs.pingidentity.com/bundle/PingIntelligence_API_Security_Enforcer_3.2_pingintel_32/page/api_naming_guidelines_1.html)

* [Define and add an API JSON](https://docs.pingidentity.com/bundle/PingIntelligence_API_Security_Enforcer_3.2_pingintel_32/page/defining_an_api___api_json_configuration_file_0.html)

## Next steps

For more information on ASE sideband deployment, see [Sideband API Security Enforcer](https://docs.pingidentity.com/bundle/PingIntelligence_API_Security_Enforcer_3.2_pingintel_32/page/api_security_enforcer___sideband.html).

---

---
title: API discovery
description: API Behavioral Security (ABS) discovers the APIs when the discovery is enabled.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_api_discovery
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_api_discovery.html
revdate: April 3, 2024
---

# API discovery

API Behavioral Security (ABS) discovers the APIs when the discovery is enabled.

The automated setup sets up the discovery mode. APIs are discovered by ABS when a global application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* is defined in the PingIntelligence API Security Enforcer (ASE). The discovered APIs from ABS are added to ASE. API model training starts after the APIs are added in ASE.

For more information, see [API discovery and configuration](../managing_pingintelligence_for_apis/pingintelligence_api_discovery_configuration.html).

---

---
title: API Publish Service
description: The API Publish Service publishes the changes made to the discovered APIs from the PingIntelligence Dashboard to the AI engine.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_api_publish_service
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_api_publish_service.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  installing-the-api-publish-service: Installing the API Publish Service
  before-you-begin: Before you begin
  about-this-task-2: About this task
  steps: Steps
  choose-from: Choose from:
  example-tar-zxvf-pi-api-abs-5-1-tar-gz: Example:# tar –zxvf pi-api-abs-5.1.tar.gz
  default-settings: Default settings
  obfuscating-passwords: Obfuscating passwords
  before-you-begin-2: Before you begin
  about-this-task-3: About this task
  steps-2: Steps
  next-steps: Next steps
  importing-existing-ca-signed-certificates: Importing existing CA-signed certificates
  before-you-begin-3: Before you begin
  about-this-task-4: About this task
  steps-3: Steps
  example: Example:
  example-2: Example:
  starting-and-stopping-the-api-publish-service: Starting and stopping the API Publish Service
  before-you-begin-4: Before you begin
  about-this-task-5: About this task
  steps-4: Steps
  choose-from-2: Choose from:
  choose-from-3: Choose from:
---

# API Publish Service

The API Publish Service publishes the changes made to the discovered APIs from the PingIntelligence Dashboard to the AI engine.

## About this task

Complete the following steps to install the API Publish Service in your environment.

## Installing the API Publish Service

Install the API Publish Service.

### Before you begin

Before installing the API Publish Service:

* Install OpenJDK 11.0.2 on a 64-bit architecture machine. To verify the Java version, run the following command:

  ```
  # java -version
  ```

* Verify the supported operating systems.PingIntelligence supports RHEL 7.9 and Ubuntu 18.04 LTS.

### About this task

You can install the API Publish Service as a root user or as a non-root user. The installation path in the steps below assumes that you are root user. The installation works in a similar way for a non-root user.

|   |                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The download site has a link to the consolidated build for ABS and API Publish. When extracting the tar in the `pingidentity` folder, there will be two folders:- `abs`

- `apipublish` |

### Steps

1. Go to the [Ping Identity Product Downloads site](https://www.pingidentity.com/en/resources/downloads.html).

2. Under PingIntelligence for APIs, click **View Now**.

3. Click **Download** under **PingIntelligence for APIs Software**.

4. Under **Download AI Engine and Tools**, click **AI Engine 5.1.0.1**.

5. After downloading:

   #### Choose from:

   * If you are installing as a root user, copy the build file to the `/opt` directory.

   * If you are installing as a non-root user, choose any other location.

6. At the command prompt, enter `# tar –zxvf <file_name>.`

   #### Example:`# tar –zxvf pi-api-abs-5.1.tar.gz`

## Default settings

The API Publish configuration file (`apipublish.properties`) is located in the `/pingidentity/apipublish/config/` directory. The following table explains the parameters and provides recommended values. You can change the default values based on your requirements.

| Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pi.apipublish.ssl.enabled-protocols`           | The supported SSL protocols. The default value is `TLSv1.2`.                                                                                                                                                                                                                                                                                                                                                                                  |
| `pi.apipublish.ssl.ciphers`                     | The supported `.ssl` ciphers. For the list of valid cipher names, see .oracle.com/en/java/javase/11/docs/specs/security/standard-names.html//\[]. For multiple cipher names, use a comma to separate names in the list. For example: `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`,`TLS_DHE_RSA_WITH_AES_256_CBC_SHA256`.                                                                                                                             |
| `pi.apipublish.ssl.key-store`                   | The directory path of the key store. The default value is `config/ssl/apipublish.jks`.                                                                                                                                                                                                                                                                                                                                                        |
| `pi.apipublish.ssl.key-store-type`              | The key store type. The default value is `JKS`.                                                                                                                                                                                                                                                                                                                                                                                               |
| `pi.apipublish.ssl.key-store-password`          | The password of the JKS key store. PingIntelligence ships with a default obfuscated password. You can reset the password and obfuscate it.                                                                                                                                                                                                                                                                                                    |
| `pi.apipublish.ssl.key-alias`                   | Alias for the SSL key. The default value is `pingidentity`.                                                                                                                                                                                                                                                                                                                                                                                   |
| `pi.apipublish.server.port`                     | Port for the API Publish Service and PingIntelligence Dashboard communication. The default value is `8050`.                                                                                                                                                                                                                                                                                                                                   |
| `pi.apipublish.server.timezone`                 | Set the time zone to `utc` or `local`. The default timezone is `utc`.                                                                                                                                                                                                                                                                                                                                                                         |
| `pi.apipublish.server.deployment_type`          | The API Publish Service deployment mode. Valid values are `cloud` or `onprem`. The default value is `onprem`.                                                                                                                                                                                                                                                                                                                                 |
| `pi.apipublish.datasource.data_dbname`          | The MongoDB data database name. The default value is `abs_data`.                                                                                                                                                                                                                                                                                                                                                                              |
| `pi.apipublish.datasource.metadata_dbname`      | The MongoDB metadata database name.The default value is `abs_metadata`.                                                                                                                                                                                                                                                                                                                                                                       |
| `pi.apipublish.datasource.mongo_rs`             | Comma separated MongoDB replica set URI.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `pi.apipublish.datasource.mongo_ssl`            | Set to `true` if MongoDB is configured to use SSL connections. The default value is `false`.                                                                                                                                                                                                                                                                                                                                                  |
| `pi.apipublish.datasource.mongo_auth_mechanism` | Defines the method in which MongoDB authenticates. The possible values are:- `NONE`: Set to `NONE` if authentication is not configured in MongoDB.

- `DEFAULT`: Set to `DEFAULT` if you want to use a native MongoDB username and password. Provide the values in the next two variables.

- `PLAIN`: Set to `PLAIN` if you want to use LDAP authentication. In this case, provide the LDAP username and password in the next two variables. |
| `pi.apipublish.datasource.mongo_certificate`    | Set to true if you want to verify MongoDB SSL server certificate when the API Publish Service connects to MongoDB. The default value is `false`.&#xA;&#xA;Make sure pi.apipublishservice.datasource.mongo\_ssl is set to true before setting pi.apipublishservice.datasource.mongo\_certificate to true.                                                                                                                                      |
| `pi.apipublish.datasource.username`             | MongoDB username. The default value is `absuser`.                                                                                                                                                                                                                                                                                                                                                                                             |
| `pi.apipublish.datasource.password`             | MongoDB password. The default value is `abs123`.                                                                                                                                                                                                                                                                                                                                                                                              |

## Obfuscating passwords

Using the command line interface (CLI), you can obfuscate the keys and passwords configured in `apipublish.properties`.

### Before you begin

### About this task

The API Publish Service is shipped with a default `apipublish_master.key`, which is used to obfuscate the various keys and passwords. It is recommended to generate your own `apipublish_master.key`. A default `jks_password` is configured in the `apipublish.properties` file.

The following keys and passwords are obfuscated:

* `mongo_password`

* `jks_password`

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | During the process of obfuscation of keys and password, the API Publish Service must be stopped. |

The following diagram summarizes the obfuscation process.

![A diagram of the API Publish Service obfuscation flow.](../_images/vxw1636544066014.png)

### Steps

1. To generate the `apipublish_master.key`, run the `generate_obfkey` command in the CLI:

   ```
   /pingidentity/apipublish/bin/cli.sh generate_obfkey -u admin -p admin
   ```

   The new `apipublish_master.key` is used to obfuscate the passwords in `apipublish.properties` file.

2. Enter the keys and passwords in clear text in the `apipublish.properties` file.

3. Run the `obfuscate_keys` command to obfuscate keys and passwords:

   ```
   /pingidentity/apipublish/bin/cli.sh obfuscate_keys -u admin -p admin
   ```

4. After the passwords are obfuscated, start the API Publish Service.

### Next steps

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | After the keys and passwords are obfuscated, the `apipublish_master.key` must be moved to a secure location. |

## Importing existing CA-signed certificates

Import existing CA-signed certificates.

### Before you begin

To import the certificate authority (CA)-signed certificate, stop the API Publish Service if it is already running.

### About this task

You can import your existing CA-signed certificate in the API Publish Service. Complete the following steps to import the CA-signed certificate.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The API Publish Service is shipped with a default self-signed certificate with the Java key store at `/config/ssl/apipublish.jks`. The default password is set in the `apipublish.properties` file. The default password is obfuscated in the file. It is recommended to change the default passwords and obfuscate the new passwords. See [Obfuscating passwords](pingintelligence_api_publish_service_obfuscating_passwords.html) for steps to obfuscate passwords. |

### Steps

1. Export your CA-signed certificate to the PKCS12 store by entering the following command:

   ```
   # openssl pkcs12 -export -in  <your_CA_cerficate.crt>  -inkey  <your_certificate_key.key>  -out abs.p12 -name  <alias_name>
   ```

   #### Example:

   ```
   # openssl pkcs12 -export -in ping.crt -inkey ping.key -out abs.p12 -name exampleCAcertificate
   Enter Export Password:
   Verifying - Enter Export Password:
   ```

   |   |                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------- |
   |   | If you have an intermediate certificate from a CA, then append the content to the `<your_CA_certificate>.crt` file. |

2. Import the certificate and key from the PKCS12 store to the Java key store by entering the command below.

   ```
   # keytool -importkeystore -destkeystore apipublish.jks -srckeystore abs.p12 -srcstoretype PKCS12 -alias <alias_name> -storetype jks
   ```

   The command requires the destination key store password. The destination key store password entered in the command should be same that is configured in the `apipublish.properties` file.

   The following is a snippet of the `apipublish.properties` file where the destination key store password is stored. The password is obfuscated.

   ```
   # Java Keystore password
   jks_password=OBF:AES:Q3vcrnj7VZILTPdJnxkOsyimHRvGDQ==:daYWJ5QgzxZJAnTkuRlFpreM1rsz3FFCulhAUKj7ww4=
   ```

   #### Example:

   ```
   # keytool -importkeystore -destkeystore apipublish.jks -srckeystore abs.p12 -srcstoretype PKCS12 -alias exampleCAcertificate -storetype jks
   Importing keystore apipublish.p12 to abs.jks...
   Enter destination keystore password:
   Re-enter new password:
   Enter source keystore password:
   ```

3. Copy the `apipublish.jks` file created in step 2 to `/config/ssl` directory.

4. Start the API Publish Service by running the following command:

   ```
   # ./bin/start.sh
   ```

## Starting and stopping the API Publish Service

Start and stop the API Publish Service.

### Before you begin

For the API Publish Service to start, the `apipublish_master.key` must be present in the `apipublish/config` directory. If you have moved the master key to a secured location for security reasons, copy it to the `config` directory before starting the service.

### About this task

You can start the API Publish Service in one of the following two ways:

* Using a service script available in the `bin` directory

* Using the `start.sh` script available in the `bin` directory

### Steps

1. Start API Publish.

   #### Choose from:

   * To start API Publish as a service:

     1. Navigate to the `bin` directory and run the following command to install API Publish as a service:

        ```
        #sudo ./install-systemctl-service.sh pi-apipublish
        ```

     2. Start the service by entering the following command:

        ```
        systemctl start pi-apipublish.service
        ```

   * To start API Publish using the `start.sh` script:

     1. Run the `start.sh` script located in the `/pingidentity/apipublish/bin` directory:

        ```shell
        $ ../bin/start.sh
        ```

2. Stop API Publish.

   #### Choose from:

   * To stop API Publish using a service script:

     1. Run the following command to stop the API Publish Service:

        ```
        systemctl stop pi-apipublish.service
        ```

   * To stop API Publish using the `stop.sh` script:

     1. Run the `stop.sh` script available in the `bin` directory:

        ```
        # ../bin/stop.sh
        ```

---

---
title: ASE and ABS integration
description: Integrate ASE and ABS.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_ase_abs_integration
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_ase_abs_integration.html
revdate: April 3, 2024
---

# ASE and ABS integration

Integrate ASE and ABS.

The ABS engine installation process is summarized below:

* Connect ASE to the ABS AI engine for ASE to send access log files to ABS.

* Enable ASE to ABS engine communication: Just connecting ASE and the ABS engine does not mean that access logs are sent by ASE to ABS. ASE to ABS communication has to be enabled separately.

* Add API JSON files to ASE. The API JSON files define your API and its various parameters. For more information, see [Defining an API using API JSON configuration file in inline mode](../pingintelligence_reference_guide/pingintelligence_defining_api_json_configuration_inline.html).

* Train the ABS AI engine models to analyze and report on your API traffic.

---

---
title: ASE deployment modes
description: API Security Enforcer (ASE) supports REST and WebSocket APIs and can dynamically scale and secure system infrastructure.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_ase_deployment_modes
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_ase_deployment_modes.html
revdate: April 3, 2024
section_ids:
  inline-mode: Inline mode
  sideband-mode: Sideband mode
---

# ASE deployment modes

API Security Enforcer (ASE) supports REST and WebSocket APIs and can dynamically scale and secure system infrastructure.

ASE can be deployed in inline or sideband mode.

## Inline mode

In the inline deployment mode, ASE sits at the edge of your network to receive the API traffic. It can also be deployed behind an existing load balancer, such as AWS ELB. In inline mode, ASE deployed at the edge of the datacenter terminates SSL connections from API clients. ASE then forwards the requests directly to the correct APIs and app servers, such as Node.js, WebLogic, Tomcat, PHP, etc.

![Diagram of ASE inline deployment mode.](../_images/oep1564009146604.png)

To configure ASE to work in the inline mode, set `mode=inline` in the `/opt/pingidentity/ase/config/ase.conf` file.

Some load balancers (for example, AWS ELB) require responses to keep alive messages from all devices receiving traffic. In an inline mode configuration, ASE should be configured to respond to these keep alive messages by updating the `enable_ase_health` variable in the `/opt/pingidentity/ase/config/ase.conf` file. When `enable_ase_health` is true, load balancers can perform an ASE health check using the following URL: `http(s)://<ASE Name>/ase` where *\<ASE Name>* is the ASE domain name. ASE will respond to these health checks.

## Sideband mode

When deployed in sideband mode, ASE works behind an existing API gateway. The API request and response data between the client and the backend resource or API server is sent to ASE. In this case, ASE does not directly terminate the client requests.

To configure ASE to work in inline mode, set `mode=sideband` in the `/opt/pingidentity/ase/config/ase.conf` file.

![Diagram of ASE sideband deployment mode.](../_images/zpg1564009147496.png)

The following is a description of the traffic flow through the API gateway and Ping Identity ASE.

1. The API client sends a request to the API gateway.

2. The API gateway makes an API call to send the request detail in JSON format to ASE

3. ASE checks the request against a registered set of APIs and checks the origin IP against the AI-generated deny list. If all checks pass, ASE returns a `200-OK` response to the API gateway. Otherwise, a different response code is sent to the gateway. The request is also logged by ASE and sent to the AI engine for processing.

4. If the API gateway receives a `200-OK` response from ASE, then it forwards the request to the backend server. Otherwise, the gateway returns a different response code to the client.

5. The response from the backend server is received by the API gateway.

6. The API gateway makes a second API call to pass the response information to ASE, which sends the information to the AI engine for processing.

7. ASE receives the response information and sends a `200-OK` to the API gateway.

8. API gateway sends the response received from the backend server to the client.

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To complete the ASE sideband mode deployment, see the [Integrate API gateways for sideband deployment](pingintelligence_integration_api_gateways.html). |

---

---
title: ASE installation
description: This section summarizes the key processes involved in API Enforcer Enforcer (ASE) installation.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_ase_installation
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_ase_installation.html
revdate: April 3, 2024
section_ids:
  after-installation: After Installation
---

# ASE installation

This section summarizes the key processes involved in API Enforcer Enforcer (ASE) installation.

A new ASE installation involves the following steps:

1. [Understanding and determining ASE deployment modes](pingintelligence_ase_deployment_modes.html).

2. Provisioning the host system based on the number of APIs and the expected queries per second (QPS).

   For information on sizing, contact the Ping Identity support team.

3. [Reviewing port requirements](pingintelligence_ase_ports.html).

4. [Installing ASE](pingintelligence_install_ase.html).

5. [Copying ASE license](pingintelligence_manage_ase_license.html).

6. [Changing default settings](pingintelligence_ase_changing_default_settings.html).

7. [Obfuscating keys and passwords](pingintelligence_obfuscating_ase.html).

8. [Tuning host system for high performance](../pingintelligence_reference_guide/pingintelligence_tuning_host_system.html).

9. [Starting ASE](pingintelligence_starting_stopping_ase.html).

10. [Configuring SSL for client-side connection or external APIs](pingintelligence_configure_ssl_client_side_connection.html)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | ASE cluster setup facilitates high availability and increases both performance and overall system throughput. It is recommended to set up a cluster of ASE nodes for production environments. For more information on setting up an ASE cluster, see [Setting up an ASE cluster (optional)](pingintelligence_setting_up_ase_cluster.html) and [Administering an ASE cluster](../pingintelligence_reference_guide/pingintelligence_administering_ase_cluster.html). |

## After Installation

After installing ASE, proceed with the following tasks:

* Configuring ASE: ASE system-level configuration entails modifying parameters in the `ase.conf` file located in the `config` directory. For more information, see [Sideband ASE configuration](../pingintelligence_reference_guide/pingintelligence_sideband_ase_configuration.html) or [Inline ASE configuration](../pingintelligence_reference_guide/pingintelligence_inline_ase_configuration.html)

* Configuring deployment method: PingIntelligence supports on-premise deployment. For more information, see [Configure deployment method](../pingintelligence_reference_guide/pingintelligence_ase_to_abs_conntectivity.html).

---

---
title: ASE ports
description: ASE uses default ports as defined in the table below.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_ase_ports
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_ase_ports.html
revdate: April 3, 2024
---

# ASE ports

ASE uses default ports as defined in the table below.

If any ports configured in the `ase.conf` file is unavailable, ASE will not start.

| Port Number | Usage                                                                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 80          | Data port for HTTP and WebSocket connections. Accessible from any client (not secure). If you are installing ASE as a non-root user, choose a port that is greater than or equal to 1024.  |
| 443         | Data port for HTTPS and Secure WebSocket (wss) connections. Accessible from any client. If you are installing ASE as a non-root user, choose a port that is greater than or equal to 1024. |
| 8010        | Management port used by CLI and REST API for managing ASE. Accessible from management systems and administrators.                                                                          |
| 8020        | Cluster port used by ASE for cluster communication. Accessible from all cluster nodes.                                                                                                     |
| 8080        | ABS ports used by ASE for outbound connections to ABS for sending access logs and receive client identifiers of suspected attacks.                                                         |

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Management ports 8010 and 8020 should not be exposed to the Internet. If you are setting up the deployment in an AWS environment with security groups, use private IPs for ASE to ABS connections to avoid security group issues. |

---

---
title: Building the PingIntelligence Docker images
description: Use the build.sh script available in the bin directory to build the Docker images.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_build_docker_images
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_build_docker_images.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
---

# Building the PingIntelligence Docker images

Use the `build.sh` script available in the `bin` directory to build the Docker images.

## About this task

You can build all the following Docker images at once, or you can choose to build the images individually. The following Docker images are built:

* API Security Enforcer (ASE)

* API Behavioral Security (ABS)

* Dashboard

* MongoDB

* API Publish

* Kafka

* Zookeeper

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | You should obfuscate the various keys and password in ASE, ABS, and the Dashboard before building the Docker images. |

For more information on obfuscating keys and passwords, see the following topics:

* ASE - [Obfuscating keys and passwords](../pingintelligence_reference_guide/pingintelligence_obfuscating_keys_and_passwords.html)

* ABS - [Obfuscate passwords](../pingintelligence_reference_guide/pingintelligence_obfuscate_passwords.html)

* Dashboard - [Obfuscate keys and passwords](../pingintelligence_reference_guide/pingintelligence_obfuscate_keys_passwords.html)

* API Publish - [Obfuscating passwords](pingintelligence_api_publish_service_obfuscating_passwords.html)

To build the Docker images:

## Steps

1. Configure the base image name and base image operating system details in the `config/docker.conf` file.

2. Download the following PingIntelligence software to the `software` directory:

   1. ASE

   2. ABS

   3. PingIntelligence Dashboard

3. Download OpenJDK 11.0.2, Elasticsearch 7.13.4, Kafka 2.5.0, Zookeeper 3.5.7, and MongoDB 4.2.0 in the `external` directory and save them with their respective names shown in the following table.

   |   |                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Make sure that MongoDB is as per the base image configured in the `docker.conf` file. Always build Kafka and Zookeeper images first, if building individually. |

   | Software       | File Name                                                                                                                                                         |
   | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Elasticsearch  | `elasticsearch.tar.gz`                                                                                                                                            |
   | OpenJDK 11.0.2 | `openjdk11.tar.gz`                                                                                                                                                |
   | Kafka          | `kafka.tar.gz`Download the Kafka tar version 2.5.0 tar from <https://archive.apache.org/dist/kafka/2.5.0/kafka_2.12-2.5.0.tgz>                                    |
   | Zookeeper      | `zookeeper.tar.gz`Download the Zookeeper tar version 3.5.7 tar from <https://archive.apache.org/dist/zookeeper/zookeeper-3.5.7/apache-zookeeper-3.5.7-bin.tar.gz> |
   | MongoDB        | `mongodb.tgz`                                                                                                                                                     |

4. Run the `build.sh` script to build the Docker images:

   ```shell
   docker-setup# ./bin/build.sh all
   Base image os: rhel
   Creating build context for ASE
   Creating Image
   Image created with tag pingidentity/ase:5.0
   Image saved to /home/ubuntu/docker-setup/images/pingidentity_ase.tar
   Creating build context for abs
   Creating Image
   Image created with tag pingidentity/abs:5.0
   Image saved to /home/ubuntu/docker-setup/images/pingidentity_abs.tar
   Creating build context for dashboard
   Creating Image
   Image created with tag pingidentity/dashboard:5.0
   Image saved to /home/ubuntu/docker-setup/images/pingidentity_dashboard.tar
   Creating build context for mongo
   Creating Image
   Image created with tag pingidentity/mongo:4.2.0
   Image saved to /home/ubuntu/docker-setup/images/pingidentity_mongo.tar
   root@ip-172-31-25-146:/home/ubuntu/docker-setup# vim lib/dashboard/context/entrypoint.sh
   Creating build context for apipublish
   Creating Image
   Image created with tag pingidentity/apipublish:5.1
   Image saved to /home/ubuntu/docker-setup/images/pingidentity_apipublish.tar
   Creating build context for kafka
   Creating Image
   Image created with tag pingidentity/kafka:5.1
   Image saved to /home/ubuntu/docker-setup/images/pingidentity_kafka.tar
   Creating build context for zookeeper
   Creating Image
   Image created with tag pingidentity/zookeeper:5.1
   Image saved to /home/ubuntu/docker-setup/images/pingidentity_zookeeper.tar
   ```

   The other options that you can give with `build.sh` are:

   * `ase`

   * `abs`

   * `dashboard`

   * `mongo`

   * `apipublish`

   * `kafka`

   * `zookeeper`

5. Verify that the images are created by checking the local registry. Run the following command:

   ```
   sudo docker image ls | grep pingidentity
   ```

   ### Example:

   ```
   pingidentity/dashboard                5.1       e9bbbb21c14d   18 hours ago    1.69GB
   pingidentity/apipublish               5.1       bc3878f8a340   23 hours ago    777MB
   pingidentity/mongo                    4.2.0     21a8177c0a35   23 hours ago    640MB
   pingidentity/abs                      5.1       540c5c384fba   23 hours ago    766MB
   pingidentity/ase                      5.1       262d9207d5de   23 hours ago    424MB
   pingidentity/zookeeper                5.1       1cf24526f8cf   23 hours ago    690MB
   pingidentity/kafka                    5.1       f9118757f234   23 hours ago    737MB
   ```

6. Verify that the Docker images are saved in the `images` directory:

   ```shell
   docker-setup# ls -ltra images/
   ```

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | The Docker images do not install any additional packages like `vi` editor and so on. |

   ### Example:

   ```
   -rw-------.  1 root root  601075200 Dec  2 00:24 pingidentity_kafka.tar
   -rw-------.  1 root root  554516992 Dec  2 00:24 pingidentity_zookeeper.tar
   -rw-------.  1 root root  287269376 Dec  2 00:24 pingidentity_ase.tar
   -rw-------.  1 root root  628353024 Dec  2 00:24 pingidentity_abs.tar
   -rw-------.  1 root root 1549656576 Dec  2 00:25 pingidentity_dashboard.tar
   -rw-------.  1 root root  503818752 Dec  2 00:26 pingidentity_mongo.tar
   -rw-------.  1 root root  637405184 Dec  2 00:26 pingidentity_apipublish.tar
   ```

---

---
title: "Changing <code class=\"filepath\">abs_master.key</code>"
description: Create your own ABS master key to obfuscate keys and password in ABS.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_changing_abs_master_key
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_changing_abs_master_key.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Changing `abs_master.key`

Create your own ABS master key to obfuscate keys and password in ABS.

## Before you begin

ABS must be stopped before creating a new `abs_master.key`.

## About this task

To create your own ABS master key:

## Steps

1. Run the following command: `generate_obfkey`.

2. If ABS is running, then stop ABS before generating a new ABS master key. Enter the following command to stop ABS:

   ```
   # /opt/pingidentity/abs/bin/stop.sh
   checking API Behavioral Security status
   sending shutdown signal to ABS, please wait...
   API Behavioral Security stopped
   ```

3. To change `abs_master.key`, enter the `generate_obfkey` command to change the default ABS master key:

   ```
   /opt/pingidentity/abs/bin/cli.sh generate_obfkey -u admin -p admin
   Please take a backup of config/abs_master.key before proceeding.
   Warning: Once you create a new obfuscation master key, you should obfuscate all config keys also using cli.sh -obfuscate_keys
   Warning: Obfuscation master key file
   /pingidentity/abs/config/abs_master.key already exists. This command will delete it and create a new key in the same file
   Do you want to proceed [y/n]: y
   Creating new obfuscation master key
   Success: created new obfuscation master key at /pingidentity/abs/config/abs_master.key
   ```

---

---
title: "Changing <code class=\"filepath\">ase_master.key</code>"
description: Create your own ASE master key to obfuscate keys and password in ASE.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_changing_ase_master_key
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_changing_ase_master_key.html
revdate: April 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Changing `ase_master.key`

Create your own ASE master key to obfuscate keys and password in ASE.

## Before you begin

ASE must be stopped before creating a new `ase_master.key`.

## About this task

To create your own ASE master key:

## Steps

1. Run the following command to create your own ASE master key to obfuscate keys and password in ASE: `generate_obfkey`.

   ```
   /opt/pingidentity/ase/bin/cli.sh generate_obfkey -u admin -p admin
   API Security Enforcer is running. Please stop ASE before generating new obfuscation master key
   ```

2. Stop ASE by running the following command:

   ```
   /opt/pingidentity/ase/bin/stop.sh -u admin –p admin
   checking API Security Enforcer status…sending stop request to ASE. please wait…
   API Security Enforcer stopped
   ```

3. Enter the `generate_obfkey` command to change the default ASE master key:

   ```
   /opt/pingidentity/ase/bin/cli.sh -u admin -p admin generate_obfkey
   Please take a backup of config/ase_master.key, config/ase.conf,
   config/abs.conf, config/cluster.conf before proceeding
   Warning: Once you create a new obfuscation master key, you should
   obfuscate all config keys also using cli.sh obfuscate_keys
   Warning: Obfuscation master key file /opt/pingidentity/ase/config/ase_master.key already exist.
   This command will delete it create a new key in the same file
   Do you want to proceed [y/n]:
   ```

4. After a new ASE master key is generated, start ASE by entering the following command:

   ```
   /opt/pingidentity/ase/bin/start.sh
   Starting API Security Enforcer 4.0...
   please see /opt/pingidentity/ase/logs/controller.log for more details
   ```

---

---
title: Changing ABS default settings
description: You can change the default settings in ABS by editing the abs-defaults.yml file.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_change_abs_settings
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_change_abs_settings.html
revdate: April 3, 2024
section_ids:
  abs-variable-settings: ABS variable settings
  changing-the-abs-default-system-memory: Changing the ABS default system memory
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Changing ABS default settings

You can change the default settings in ABS by editing the `abs-defaults.yml` file.

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | Make a backup of the `abs-defaults.yml` file on a secure machine after the automated installation is complete. |

The following is a sample `abs-defaults.yml` file.

```
---
abs:
 # Define ports for the PingIntelligence ABS
 # Make sure ports are not same for single server installation
 management_port: 8080

 # Mongo DB User and password
 mongo_username: absuser
 mongo_password: abs123
 # Define cache size for MongoDB (% of total RAM).
 # MongoDB will be configured to use this percentage of host memory.
 mongo_cache_size: 25
 # Communication between mongo and ABS
 mongo_ssl: true
 # Mongo DB Server Certificate Verification
 # Set to true if Mongo DB instance is configured in SSL mode and you want to do the server certificate verification
 # By default ABS will not verify the MongoDB server certificate
 mongo_certificate_verify: false
 # Mongo replica set name
 mongo_replica_set: absrs01

 # When kafka is set to false in config/hosts, this url will be used
 # Give the host:port combination of mutiple kafka server in comma seperated.
 # Make sure kafka_server_url is accessible from ansible management host, dataengine, and abs nodes.
 #This will be used via dashboard dataengine module too.

 kafka_server_url: kafka_1:9093

 # When kafka is set to false in config/hosts, this passoword for jks will be used
 #This will be used via dashboard dataengine module too.

 kafka_custom_truststore_password: custom



 # Duration of initial training period (units in hours)
 # This value will be set in the mongo nodes
 attack_initial_training: 24

 # Memory for webserver and streaming server (unit is in MB)
 system_memory: 4096

 # Access keys and secret keys to access ABS
 access_key: abs_ak
 secret_key: abs_sk
 access_key_ru: abs_ak_ru
 secret_key_ru: abs_sk_ru

 # Password for ABS keystore
 jks_password: abs123

 #Users in Kafka for abs
 consumer_user: abs_consumer
 producer_user: abs_producer
 abs_groupid: pi4api.abs

 # Kafka Consumer Producer Password
 consumer_authentication_password: changeme
 producer_authentication_password: changeme

 #Kafka Relicas
 min_insync_replicas: 1
 #topics to be created in kafka
 transactions_topic: pi4api.queuing.transactions
 attacks_topic: pi4api.queuing.ioas
 anomalies_topic: pi4api.queuing.anomalies
 discovery_topic: pi4api.queuing.apis

  #Topic partition ,replication_factor and retention_period(in milli seconds)
  #These will be used when install_kafka is true and topics are created as part of deployment.
 topic_partitions: 1
 replication_factor: 1
 retention_period: 172800000

 # Configure Email Alert. Set enable_emails to true to configure
 # email settings for ABS
 enable_emails: false
 smtp_host: smtp.example.com
 smtp_port: 587
 sender_email: sender@example.com
 email_password: password
 receiver_email: receiver@example.com

 # CLI admin password
 current_admin_password: admin
 new_admin_password: admin

 poc_mode: false

api_publishing_service:
 # Define ports for the PingIntelligence API Publish Service
 # Make sure ports are not same for single server installation
 management_port: 8050

 # Password for APIPublish keystore
 jks_password: api123

 # Mongo DB Server Certificate Verification
 # Set to true if Mongo DB instance is configured in SSL mode and you want to do the server certificate verification
 # By default apipublish will not verify the MongoDB server certificate
 mongo_certificate_verify: false

 server_ssl_key_alias: pingidentity

 # MongoDB Database names
 data_dbname: abs_data
 meta_database: abs_metadata

 # MongoDB authentication
 # If authentication is not enabled in MongoDB, set the mongo_auth_mechanism to NONE
 # The supported MongoDB authentication mechanisms are DEFAULT and PLAIN.
 # If authentication mechanism is DEFAULT, provide MongoDB username and password for mongo_username
 # and mongo_password. If authentication mechanism is PLAIN, provide external
 # LDAP username and password in mongo_username and mongo_password.
 mongo_authentication_mechanism: DEFAULT

 # CLI admin password
 current_admin_password: admin
 new_admin_password: admin
```

## ABS variable settings

The following table lists the variables that you can set for ABS.

| Variable                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `management_port`                     | Port for ABS to ASE and REST API to ABS communication. The default value is 8080.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `mongo_username` and `mongo_password` | MongoDB username and password. The default username is `absuser`, and the default password is `abs123`.                                                                                                                                                                                                                                                                                                                                                                                           |
| `mongo_cache_size`                    | If you are running all the PingIntelligence components on the same instance, keep the MongoDB cache size to a maximum of 25% of the system memory. If you are running MongoDB on a separate instance, keep the MongoDB cache size to a maximum of 40% of the system memory.                                                                                                                                                                                                                       |
| `mongo_ssl`                           | Default value is `true`. PingIntelligence deployment ships with a default self-signed certificate. Setting it to `false` establishes non-SSL connection between ABS and Mongo.                                                                                                                                                                                                                                                                                                                    |
| `mongo_certificate_verify`            | Set it to `true` if you want to verify MongoDB Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">&#xA;\<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>&#xA;\</div>)* server certificate when ABS connects to MongoDB. The default value is `false`.&#xA;&#xA;Make sure mongo\_ssl is set to true before setting mongo\_certificate\_verify to true. |
| `mongo_replica_set`                   | Name of the MongoDB replica set. Default name is `absrs01`.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `attack_initial_training`             | The number of hours that you want to train the AI model before it moves to the prediction mode. Default value is 24 hours.                                                                                                                                                                                                                                                                                                                                                                        |
| `system_memory`                       | Memory size in MB allocated to run machine learning jobs. Recommended to be at least 50% of system memory.                                                                                                                                                                                                                                                                                                                                                                                        |
| `access_key` and `secret_key`         | The access key and secret for the admin user. For more information on different ABS users, see [ABS users](../pingintelligence_reference_guide/pingintelligence_abs_users_api_reports.html).&#xA;&#xA;":" (colon) is a restricted character and not allowed in access key and secret key.                                                                                                                                                                                                         |
| `access_key_ru` and `secret_key_ru`   | The access key and secret for the restricted user. For more information on different ABS users, see [ABS users](../pingintelligence_reference_guide/pingintelligence_abs_users_api_reports.html).&#xA;&#xA;":" (colon) is a restricted character and not allowed in access key and secret key.                                                                                                                                                                                                    |
| `jks_password`                        | The password of the Java KeyStore (JKS) *(tooltip: \<div class="paragraph">&#xA;\<p>A repository of security certificates and corresponding private keys.\</p>&#xA;\</div>)*. The default password is `abs123`.                                                                                                                                                                                                                                                                                   |
| `Email default settings`              | Configure the following settings:- `enable_emails`: Set it to `true` for ASE to send email notifications. Default value is false.

- `smtp_host` and `smtp_port`

- `sender_email`: Email address used from which email alerts and reports are sent.

- `email_password`: Password of sender's email account.

- `receiver_email`: Email address at which the email alerts and reports are sent.                                                                                                  |
| `CLI admin password`                  | The default value for command-line interface (CLI) admin is `admin`. To change the password, you need the current password.                                                                                                                                                                                                                                                                                                                                                                       |
| `poc_mode`                            | Sets the mode in which the artificial intelligence (AI) engine sets the thresholds for the AI models. If set to `true`, AI engine sets thresholds at a lower value. It should be set to `true` only for a proof-of-concept deployment.                                                                                                                                                                                                                                                            |
| `consumer_user`                       | ABS consumer user in Kafka.Default: `abs_consumer`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `producer_user`                       | ABS producer user in Kafka.Default: `abs_producer`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `abs_groupid`                         | ABS group in Kafka.Default: `pi4api.abs`                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `consumer_authentication_password`    | ABS consumer user password.Default: `changeme`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `producer_authentication_password`    | ABS producer user password.Default: `changeme`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `min_insync_replicas`                 | Minimum number of insync replicas for data in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `transactions_topic`                  | ABS transaction topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `attacks_topic`                       | ABS attack topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `anomalies_topic`                     | ABS anomalies topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `discovery_topic`                     | ABS discovery topic in Kafka.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `topic_partitions`                    | Number of partitions for topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `replication_factor`                  | Replication factor for topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `retention_period`                    | Retention period of data on topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `kafka_server_url`                    | Pre-existing Kafka `ip:port` that must be configured in `config/abs-defaults.yml`.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `kafka_custom_truststore_password`    | Pre-existing Kafka truststore password in `config/abs-defaults.yml`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `management_port`                     | API Publish service port.Default: `8050`                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `jks_password`                        | API Publish service JKS password.You can change the password for the JKS file. It will be generated during installation.                                                                                                                                                                                                                                                                                                                                                                          |
| `mongo_certificate_verify`            | Mongodb Server Certificate Verification for API Publish service.Default: `false`                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `server_ssl_key_alias`                | Alias for API Publish service SSL JKS file.Default: `pingidentity`                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `data_dbname`                         | API Publish service database name.Default: `abs_data`                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `meta_database`                       | API Publish service metadatabase name.Default: `abs_metadata`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `current_admin_password`              | API Publish service CLI password.Default: `admin`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `new_admin_password`                  | API Publish service new admin password.Default: `admin`                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Changing the ABS default system memory

### About this task

To change the default system memory in the `abs.properties` file of ABS:

### Steps

1. Go to the `software` directory.

2. Untar the ABS binary by entering the following command:

   ```
   # tar –zxvf pi-api-abs-5.0.tar.gz
   ```

3. Edit the `config/abs.properties` file to change the default value of `system_memory` to 50% of host memory.

   ```
   # vi pingidentity/abs/config/abs.properties
   ```

   #### Example:

   If host ABS system has 16 GB of memory, set the value to `8192` MB.

4. Save the file.

5. Tar the ABS binary and save it with the same file name (`pi-api-abs-5.0.tar.gz`) in the `software` directory by entering the following command:

   ```
   # tar -czf pi-api-abs-5.0.tar.gz pingidentity/abs
   ```

---

---
title: Changing ASE default settings
description: You can change the default settings in ASE by editing the ase-defaults.yml file.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_changing_ase_default_settings
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_changing_ase_default_settings.html
revdate: April 3, 2024
---

# Changing ASE default settings

You can change the default settings in ASE by editing the `ase-defaults.yml` file.

The following table lists the variables that you can set for ASE.

| Variable                       | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `mode`                         | Sets the mode in which ASE is deployed. The default value is `inline`. Set the value to `sideband` if you want ASE to work in sideband mode.                                                                                                                                                                                                                                                     |
| `http_ws_port`                 | Data port used for HTTP or WebSocket protocol. The default value is 8000.                                                                                                                                                                                                                                                                                                                        |
| `https_wss_port`               | Data port used for HTTPS or secure WebSocket protocol. The default value is 8443.                                                                                                                                                                                                                                                                                                                |
| `management_port`              | Management port used for command-line interface (CLI) and REST application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* management. The default value is 8010.                                                                                |
| `cluster_manager_port`         | ASE node uses this port number to communicate with other ASE nodes in the cluster. The default value is 8020.                                                                                                                                                                                                                                                                                    |
| `keystore_password`            | The password for ASE keystore. The default password is `asekeystore`.                                                                                                                                                                                                                                                                                                                            |
| `cluster_secret_key`           | This key is used for authentication among ASE cluster node. All the nodes of the cluster must have the same `cluster_secret_key`. This key must be entered manually on each node of the ASE cluster for the nodes to communicate with each other. The default value is `yourclusterkey`.                                                                                                         |
| `enable_ase_detected_attack`   | This key is used to enable ASE to block auto detected attacks. Set this value to `true` to allow ASE to block auto detected attacks. The default value is `false`.                                                                                                                                                                                                                               |
| `enable_abs_attack`            | This key is used to enable ASE to fetch attack list from ABS. Set this value to `true` to fetch the list from ABS. The default value is `false`.                                                                                                                                                                                                                                                 |
| `enable_sideband_keepalive`    | This key is used only in ASE sideband mode. If set to `true`, ASE sends a keep-alive in response header for the TCP connection between API gateway and ASE. With the default `false` value, ASE sends a connection close in response header for connection between API gateway and ASE.                                                                                                          |
| `Email default settings`       | Configure the following settings:- `enable_emails`: Set it to `true` for ASE to send email notifications. Default value is false.

- `smtp_host` and `smtp_port`

- `sender_email`: Email address used from which email alerts and reports are sent.

- `email_password`: Password of sender's email account.

- `receiver_email`: Email address to which the email alerts and reports are sent. |
| `CLI admin password`           | The default value for CLI admin is `admin`. To change the password, you need the current password.                                                                                                                                                                                                                                                                                               |
| `enable_abs_publish`           | Determines whether the ASE fetches the published API list from ABS.Default: `true`                                                                                                                                                                                                                                                                                                               |
| `abs_publish_request_minutes`  | Determines in minutes how often ASE will get the published API list from ABS.Default: `10`                                                                                                                                                                                                                                                                                                       |
| `enable_strict_request_parser` | Determines whether ASE parsing blocks requests with invalid header starts.Default: `true`                                                                                                                                                                                                                                                                                                        |

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | Make a backup of the `ase-defaults.yml` file on a secure machine after the automated installation is complete. |

The following is a sample `ase-defaults.yml` file.

```
---
ase:
 # Deployment mode for ASE. Valid values are inline or sideband
 mode: inline

 # Define ports for the PingIntelligence API Security Enforcer
 # Make sure ports are not same for single server installation
 http_ws_port: 8000
 https_wss_port: 8443
 management_port: 8010
 cluster_manager_port: 8020

 # Password for ASE keystore
 keystore_password: asekeystore

 # cluster_secret_key for ASE cluster
 cluster_secret_key: yourclusterkey

 # Set this value to true, to allow API Security Enforcer to block auto detected attacks.
 enable_ase_detected_attack: false
 # Set this value to true, to allow API Security Enforcer to fetch attack list from ABS.
 enable_abs_attack: true

 # enable keepalive for ASE in sideband mode
 enable_sideband_keepalive: false

 # Set this value to true, to allow API Security Enforcer to fetch published API list from ABS.
 enable_abs_publish: true

 #This value determines how often API Security Enforcer will get published API list from ABS.
 abs_publish_request_minutes: 10


 # enable strict parsing checks for client requests
 # If enabled, ASE will block request with invalid header start
 # If disabled, it will allow requests
 enable_strict_request_parser: true

 # Configure Email Alert. Set enable_emails to true to configure
 # email settings for ASE
 enable_emails: false
 smtp_host: smtp.example.com
 smtp_port: 587
 sender_email: sender@example.com
 email_password: password
 receiver_email: receiver@example.com

 # CLI admin password
 current_admin_password: admin
 new_admin_password: admin
```

---

---
title: Changing CLI admin password
description: You can change the default admin password.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_changing_cli_admin_password
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_changing_cli_admin_password.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Changing CLI admin password

You can change the default admin password.

## About this task

To change the CLI admin password:

## Steps

1. Enter the following command:

   ```
   /opt/pingidentity/abs/bin/cli.sh update_password -u admin -p admin
   New Password>
   Reenter New Password>
   Success. Password updated for CLI
   ```

---

---
title: Changing Dashboard default settings
description: You can change the default settings of PingIntelligence for APIs Dashboard.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_changing_dashboard_default_settings
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_changing_dashboard_default_settings.html
revdate: April 3, 2024
section_ids:
  changing-settings-in-dashboard-defaults-yml: Changing settings in dashboard-defaults.yml
  changing-settings-in-ilm-json: Changing settings in ilm.json
---

# Changing Dashboard default settings

You can change the default settings of PingIntelligence for APIs Dashboard.

To change the default settings, edit the `dashboard-defaults.yml` file and `ilm.json` file.

## Changing settings in `dashboard-defaults.yml`

You can change the default settings of PingIntelligence Dashboard by editing the `/<pi-install-path>/pingidentity/pi-api-deployment/config/dashboard-defaults.yml` file.

The following table lists the variables that you can set for PingIntelligence Dashboard in various configurations.

| Variable                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `port`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Port number to connect to PingIntelligence Dashboard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `authentication_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Defines the mode in which Dashboard authenticates. The valid values are `native` and `sso`.&#xA;&#xA;You should use native authentication for proof-of-concept deployments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `session_max_age`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Defines the maximum time for a session. The configured values should be in the form of *\<number>\<duration\_suffix>*. Duration should be > 0. Allowed `duration_suffix` values: `m` for minutes, `h` for hours, and `d` for days.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `max_active_sessions`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Defines the maximum number of active UI sessions at any given time. The value should be greater than 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `admin_password` and `ping_user_password`                                                                                                                                                                                                                                                                                                                                                                                                                                   | The passwords for webgui `admin` and `ping_user` accounts.&#xA;&#xA;admin\_password and ping\_user\_password are applicable in native authentication\_mode only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Single sign-on (SSO) configurations - Applicable only when `authentication_mode` is set as `sso`                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sso_oidc_client_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Client ID value in configured in the identity provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `sso_oidc_client_secret`                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Client secret configured for the corresponding Client ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `sso_oidc_client_authentication_method`                                                                                                                                                                                                                                                                                                                                                                                                                                     | OpenID Connect (OIDC) client authentication mode. The valid values are `BASIC`, `POST`, or `NONE`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `sso_oidc_provider_issuer_uri`                                                                                                                                                                                                                                                                                                                                                                                                                                              | HTTPS IP address of OIDC provider. Also, place the SSO provider's issuer-certificate in the following path: `<installation_path>/pingidentity/certs/webgui/`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `sso_oidc_provider_user_uniqueid_claim_name`                                                                                                                                                                                                                                                                                                                                                                                                                                | Claim name for unique ID of the user in UserInfo response. A new user is provisioned using this unique ID value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `sso_oidc_provider_user_first_name_claim_name`                                                                                                                                                                                                                                                                                                                                                                                                                              | Claim name for first name of the user in UserInfo response. Either first name or last name can be empty, but both should not be empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `sso_oidc_provider_user_last_name_claim_name`                                                                                                                                                                                                                                                                                                                                                                                                                               | Claim name for last name of the user in UserInfo response. Either first name or last name can be empty, but both should not be empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `sso_oidc_provider_user_role_claim_name`                                                                                                                                                                                                                                                                                                                                                                                                                                    | Claim name for role of the user in UserInfo response. The default value is `role`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `sso_oidc_client_additional_scopes`                                                                                                                                                                                                                                                                                                                                                                                                                                         | Additional scopes in authorization request. Multiple scopes should be comma (,) separated values. OpenID profile scopes are always requested.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| End-of-SSO configurations                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SSL configuration for PingIntelligence Dashboard- `server_ssl_key_store_password`

- `server_ssl_key_alias`                                                                                                                                                                                                                                                                                                                                                                 | Configure the passwords for key store and key alias.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| H2 database configuration:- `h2_db_password`

- `h2_db_encryption_password`                                                                                                                                                                                                                                                                                                                                                                                                 | Password for H2 database and password for encryption                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Discovery configuration - The following variables configure discovery settings for Dashboard:- `discovery_source`

- `discovery_mode`

- `discovery_mode_auto_polling_interval`

- `discovery_mode_auto_delete_non_discovered_apis`Discovery source - Defines the details of discovery source for PingAccess or Axway API gateway.PingAccess:- `pingaccess_url`

- `pingaccess_username`

- `pingaccess_password`Axway- `axway_url`

- `axway_username`

- `axway_password` | * `discovery_source` - Defines the source of discovered APIs. The discovery source can be `abs`, `pingaccess`, or `axway`

* `discovery_mode` - Defines the mode in which Dashboard publishes APIs to ASE. It can either `auto` or `manual` mode. For more information on discovery mode, see[Discovered APIs](../managing_pingintelligence_for_apis/pingintelligence_discovered_apis.html)

* `discovery_mode_auto_polling_interval` - If the mode is set to `auto` in previous option, then configure the time interval in minutes for publishing the APIs to ASE. It recommended to keep a minimum time interval of 10 minutes.

* `discovery_mode_auto_delete_non_discovered_apis` - If the mode is set to `auto`, you can configure whether you want to delete the other APIs from ASE when Dashboard publishes the discovered APIs.Configure PingAccess or Axway URL, username and password if the discovery source is `pingaccess` or `axway`. |
| `enable_xpack`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Configures whether the deployment package installs Xpack. The default value is `true`. If you are using an existing Elasticsearch and authentication is not configured for Xpack, set `enable_xpack` to `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `elasticsearch_url`                                                                                                                                                                                                                                                                                                                                                                                                                                                         | If you have set `install_elasticsearch` as `false` in the `hosts` file, configure the Elasticsearch Uniform Resource Locator (URL) *(tooltip: \<div class="paragraph">&#xA;\<p>Identifies a resource according to its internet location.\</p>&#xA;\</div>)*. Enter the complete URL, including `http/https`. For example, <https://myelasticsearchurl.pi.com:443>. NOTE: Providing the port number in the URL is mandatory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `elasticsearch_distro_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Configure the distribution type of Elasticsearch. Allowed values are `default` or `aws`.&#xA;&#xA;This variable is available for configuration in PingIntelligence for APIs 4.4.1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `elastic_username`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | If you want to use an already available Elasticsearch username, configure it in `elastic_username`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `elastic_password`                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Elasticsearch password. The default value is `changeme`.&#xA;&#xA;Do not change the elastic\_password after PingIntelligence installation is complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `elasticsearch_purge_schedule`                                                                                                                                                                                                                                                                                                                                                                                                                                              | The schedule for Elasticsearch purge to run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `elasticsearch_purge_days`                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The number of days for Elasticsearch purge.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `consumer_user`                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Consumer user in Kafka.Default: `pi4api_de_user`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `consumer_authentication_password`                                                                                                                                                                                                                                                                                                                                                                                                                                          | Consumer user password.Default: `changeme`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `dataengine_groupid`                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Group in Kafka for data engine consumer.Default: `pi4api.data-engine`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `ping_user_password`                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Password for the default user name `ping_user`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `ping_admin_password`                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Password for the admin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Syslog configuration:* `enable_syslog`

* `host, port`

* `facility`                                                                                                                                                                                                                                                                                                                                                                                                        | Configure `syslog` details.Setting `enable_syslog` to `true` lets dashboard engine log the ABS detected attacks in the `syslog` server.Provide the host and port number of the `syslog` server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | Make a backup of the `dashboard-defaults.yml` file on a secure machine after the automated installation is complete. |

The following is a sample `dashboard-defaults.yml` file.

```
---
webgui:
 # Define ports for PingIntelligence WebGUI
 # Make sure ports are not same for single server installation
 port: 8030

 # allowed values: native, sso.
 # In native mode, webgui users are self managed and stored in webgui.
 # In sso mode, webgui users are managed and stored in an Identity provider.
 authentication_mode: native
 # Maximum duration of a session.
 # Value should be in the form of <number><duration_suffix>
 # Duration should be > 0.
 # Allowed duration_suffix values: m for minutes, h for hours, d for days.
 session_max_age: 6h

 # Number of active UI sessions at any time.
 # Value should be greater than 1.
 max_active_sessions: 50

  admin_password and ping_user_password are applicable in native authentication_mode only.
 # webgui "admin" account password
 admin_password: changeme
 # webgui "ping_user" account password
 ping_user_password: changeme

  Below sso configuration properties are applicable in sso authentication_mode only.
 # Client ID value in Identity provider.
 sso_oidc_client_id: pingintelligence
 # Client Secret of the above Client ID.
 sso_oidc_client_secret: changeme
 # OIDC Client authentication mode.
 # Valid values: BASIC, POST, or NONE
 sso_oidc_client_authentication_method: BASIC
 # OIDC Provider uri
 # WebGUI queries <issuer-uri>/.well-known/openid-configuration to get OIDC provider metadata
 # issuer ssl certificate is not trusted by default. So import issuer ssl certificate into config/webgui.jks
 # issuer should be reachable from both back-end and front-end
 sso_oidc_provider_issuer_uri: https://127.0.0.1:9031

 # Place the sso provider issuer-certificate in the following path => <installation_path>/pingidentity/certs/webgui/
 # Name of the file should be => webgui-sso-oidc-provider.crt

 # claim name for unique id of the user in UserInfo response
 # a new user is provisioned using this unique id value
 sso_oidc_provider_user_uniqueid_claim_name: sub
 # claim name for first name of the user in UserInfo response
 # either first name or last name can be empty, but both should not be empty
 sso_oidc_provider_user_first_name_claim_name: given_name
 # claim name for last name of the user in UserInfo response
 # either first name or last name can be empty, but both should not be empty
 sso_oidc_provider_user_last_name_claim_name: family_name
 # claim name for role of the user in UserInfo response
 sso_oidc_provider_user_role_claim_name: role
 # additional scopes in authorization request
 # multiple scopes should be comma (,) separated
 # openid,profile scopes are always requested
 sso_oidc_client_additional_scopes:
 ## End of sso configuration

 # ssl key store password of webgui hosts
 server_ssl_key_store_password: changeme
 server_ssl_key_alias: webgui

 # local h2 db datasource properties
 h2_db_password: changeme
 h2_db_encryption_password: changeme

 # allowed values: abs/pingaccess/axway
 discovery_source: abs
 # allowed values: auto/manual
 discovery_mode: auto
 # value is in minutes
 discovery_mode_auto_polling_interval: 10
 discovery_mode_auto_delete_non_discovered_apis: false

 # valid only if discovery_source is set to pingaccess
 pingaccess_url: https://127.0.0.1:9000/
 pingaccess_username: Administrator
 pingaccess_password:

 # valid only if discovery_source is set to axway
 axway_url: https://127.0.0.1:8075/
 axway_username: apiadmin
 axway_password:


dataengine:
 ui:
   # Install elasticsearch with xpack enabled
   # If there is no authentication on pre-existing elasticsearch, set this to false
   enable_xpack: true
   server_port: 8040
   # When install_elasticsearch is set to false in config/hosts, this url will be used
   # Give the complete url with https/http and elasticsearch port number
   # Make sure elasticsearch_url is accessible from ansible management host, dataengine, webgui nodes.
   elasticsearch_url: https://search-giueibohzd6pfijfysjfsxucty.pingidentity.com:443
   # Configuration distribution type of elasticsearch. Allowed values are default or aws
   elasticsearch_distro_type: default

   # User with permission set similar to "elastic" user
   elastic_username: elastic

   # Passwords for "elasticsearch","ping_user" and "ping_admin" users
   # dataengine will be accessible for these accounts
   # Please set strong passwords
   # If enable_xpack is set to false, below passwords are ignored
   elastic_password: changeme

    # ssl key store password of webgui hosts
   server_ssl_key_store_password: changeme
   server_ssl_key_alias: dataengine

   #Users ,passowrd and groupid for dataengine in kafka
   consumer_user: pi4api_de_user
   consumer_authentication_password: changeme
   dataengine_groupid: pi4api.data-engine

   #Elastic Search Purge Schedule
   elasticsearch_purge_schedule: "0 23 * * * * "
   elasticsearch_purge_days: "30"

 syslog:
   # Configuration for syslog
   enable_syslog: false
   host: localhost
   port: 614
   facility: LOCAL0
```

## Changing settings in `ilm.json`

You can change the default settings of Index Lifecycle Management (ILM) policy by editing the `/<pi-install-path>/pingidentity/pi-api-deployment/config/ilm.json` file.

The ILM policy allows you to manage the lifecycle of the Elasticsearch indices. The following table lists the variables that you can set in the `ilm.json` file. For more information on `ilm.json` configuration, see [Automatic rollover index](../pingintelligence_reference_guide/pingintelligence_automatic_rollover_index.html).

| Variable   | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_size` | Defines the maximum size of the Elasticsearch rollover index. When the index size reaches the defined value, it rolls over.`max_size` value should be a positive non-zero number. Allowed units are MB and GB.                                                                                                                                                                           |
| `max_age`  | Defines the maximum age of the Elasticsearch rollover index configuration. The `max_age` value should be a positive non-zero number. Allowed units are `h` for hours and `d` for the number of days. If both `max_size` and`max_age` are configured, then the index rolls over based on the value that is achieved first.                                                                |
| `min_age`  | Defines the minimum age, after which the Elasticsearch rollover index enters into a different phase. Allowed units are `h` for hours and `d` for the number of days. Every index starts from `hot` phase. For more information on the phases in an index life cycle, see [Automatic rollover index](../pingintelligence_reference_guide/pingintelligence_automatic_rollover_index.html). |
| `priority` | Defines the sequence in which indices are reloaded back into memory when Elasticsearch restarts. Use a positive integer number to set the priority.                                                                                                                                                                                                                                      |

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Rollover index configuration takes effect only when `enable_xpack` is set to `true`in the `dashboard-default.yml` file. For more information, see [Changing settings in `dashboard-defaults.yml`](pingintelligence_changing_settings_dashboard_defaults_yml.html). |

The following is a sample `ilm.json` file.

```json
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_size": "7GB",
            "max_age": "7d"
          },
          "set_priority": {
            "priority": 100
          }
        }
      },
      "warm": {
        "min_age": "30d",
        "actions": {
          "set_priority": {
            "priority": 50
          }
        }
      },
      "cold": {
        "min_age": "90d",
        "actions": {
          "freeze": {},
          "set_priority": {
            "priority": 0
          }
        }
      }
    }
  }
}
```

---

---
title: Changing default access and secret key in MongoDB
description: You can change default access and the secret key in MongoDB.
component: pingintelligence
version: 5.2
page_id: pingintelligence:installing_pingintelligence_for_apis:pingintelligence_changing_default_access_secret_key_mongodb
canonical_url: https://docs.pingidentity.com/pingintelligence/5.2/installing_pingintelligence_for_apis/pingintelligence_changing_default_access_secret_key_mongodb.html
revdate: April 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Changing default access and secret key in MongoDB

You can change default access and the secret key in MongoDB.

## About this task

To change the default access and secret key, complete the following steps.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | ":" (colon) is a restricted character and not allowed in the access key or secret key. |

## Steps

1. Connect to MongoDB by entering the following command:

   ```
   mongo --host <mongo-host> --port <mongo-port> --authenticationDatabase admin -u absuser -p abs123
   ```

   |   |                                                                           |
   | - | ------------------------------------------------------------------------- |
   |   | `absuser` and `abs123` are the default username and password for MongoDB. |

2. On the MongoDB prompt, run the following command:

   ```
   use abs_metadata
   db.auth_info.updateOne( { access_key: "<new-access-key>", secret_key: "<new-secret-key>"} )
   ```
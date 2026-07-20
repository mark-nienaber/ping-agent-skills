---
title: Checking the installation completed successfully
description: This page describes how to check that the installation of PingOne Recognize on-premise was successful.
component: recognize
page_id: recognize:on-premise:on-premise-checking-installation-successful
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-checking-installation-successful.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  execution-of-the-diagnostic: Execution of the diagnostic
  configurable-options: Configurable options
---

# Checking the installation completed successfully

After the installation is complete, the state of the system can be tested using the `cct` testing tool.

As with other assets, access to this tool is provided during the initial setup phase.

## Execution of the diagnostic

This tool is containerized and can be run from anywhere, provided a connection to the `core-daemon` service is available. The most convenient way to run it is with a `kubectl run` command:

```bash
kubectl run -i cct --rm --image=quay.io/keyless_technologies/kl-cct-tester:master --env="APIKEY=some_valid_api_key" --env="HOST=http://core-daemon" --env="FULL_LOG=0" --image-pull-policy="IfNotPresent"
```

Example result:

```text
If you don't see a command prompt, try pressing enter.
Starting tests..
> Performing ENROLL...
> ENROLL completed successfully!
> Performing AUTH...
> AUTH completed successfully!

All tests passed.
Goodbye.
pod "cct" deleted
```

This indicates that the system is running correctly.

## Configurable options

* `APIKEY`

  Must be set to a valid API key recognized by the current installation.

* `HOST`

  Must point to the `core-daemon` host.

* `FULL_LOG`

  `0` for minimal logging, `1` for verbose logging (useful for debugging).

---

---
title: Components
description: Components of the PingOne Recognize backend.
component: recognize
page_id: recognize:on-premise:on-premise-backend-installation-components
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-backend-installation-components.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Components

PingOne Recognize infrastructure components are deployed using Helm charts.

Both chart versions and component versions are communicated by PingOne Recognize. Only officially communicated version combinations are supported.

* **Operations Service:** Provides REST APIs for transaction confirmation and other backend services.

* **Metrics Collector:** Gathers BI data.

* **Core Daemon:** Acts as the central orchestrator and manages the high-level logic of the authentication and authorization flow. It exposes the REST authentication endpoint, performs authentication, and implements the authorization logic and abstraction layers for persistence.

* **Administration Dashboard:** A web UI that allows clients to administer users.

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | Only install charts that are explicitly mentioned in this manual. Installing unlisted charts may result in a non-functioning system. |

---

---
title: Infrastructural Requirements
description: This page describes the infrastructural requirements for deploying PingOne Recognize on-premise.
component: recognize
page_id: recognize:on-premise:on-premise-infrastructural-requirements
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-infrastructural-requirements.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  kubernetes-version: Kubernetes Version
  postgresql-version: PostgreSQL Version
  s3-compatible-storage: S3-Compatible Storage
  helm-docker-repository: Helm / Docker Repository
---

# Infrastructural Requirements

## Kubernetes Version

Kubernetes version 1.34 and OpenShift 4.14 on GCP are officially supported. Any 1.34.x version should work, but is not officially supported. PingOne Recognize is tested on AWS EKS and GCP GKE, respecting the Kubernetes versions mentioned. Nodes must be x86\_64. ARM architecture is not supported.

## PostgreSQL Version

PostgreSQL 14+ and 15+ are officially supported. A PostgreSQL database is used by the following services to store data:

* Core Daemon Service

* Administration Dashboard Service

## S3-Compatible Storage

An S3-compatible backend (e.g. GCS) is required by the following services to store data:

* Core Daemon Service

## Helm / Docker Repository

The Helm charts are stored in a private Helm repository. Connection details and authentication credentials are provided by PingOne Recognize upon request.

The Helm charts are configured to retrieve Docker images from the PingOne Recognize private `quay.io` repository. Access to the Docker repository must be granted by PingOne Recognize before installing the service.

---

---
title: Monitoring
description: This page describes the monitoring capabilities of PingOne Recognize on-premise
component: recognize
page_id: recognize:on-premise:on-premise-monitoring
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-monitoring.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Monitoring

PingOne Recognize is natively ready to be integrated with DataDog.

Logs can be retrieved and sent to different providers, but the APM is only supported in a Datadog integration scenario.

Kubernetes/Openshift metrics are to be retrieved from the cluster itself.

---

---
title: On-premise deployment
description: This page describes the deployment procedure for PingOne Recognize on-premise.
component: recognize
page_id: recognize:on-premise:on-premise-deployment
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-deployment.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  kubernetes-deployment: Kubernetes deployment
  components: Components
  access-the-repositories: Access the repositories
  deployment-steps: Deployment steps
  configuration: Configuration
  global: Global
  circuit-storage-service: Circuit storage service
  expose-circuit-storage-service: Expose circuit storage service
  custom-certificate-to-access-the-database-or-the-s3-compatible-backend: Custom certificate to access the database or the S3-compatible backend
  exposed-java-springboot-endpoints: Exposed Java SpringBoot endpoints
  datadog-integration: Datadog integration
  adding-java-options-to-circuit-storage: Adding Java options to circuit storage
  database-connection: Database Connection
  database-initialization: Database Initialization
  mutual-tls-support-for-oracle-database: Mutual TLS Support for Oracle Database
  override-circuit-storage-resource-came: Override circuit storage resource came
  pingone-recognize-node: PingOne Recognize node
  expose-pingone-recognize-node-service: Expose PingOne Recognize node service
  override-pingone-recognize-node-resource-name: Override PingOne Recognize node resource name
  operations-api: Operations API
  expose-operations-api-service: Expose Operations API service
  override-operations-api-resource-name: Override Operations API resource name
  node-persistence: Node persistence
  exposed-java-springboot-endpoints-2: Exposed Java SpringBoot endpoints
  datadog-integration-2: Datadog integration
  adding-java-options-to-node-persistence: Adding Java options to node persistence
  setting-database-type: Setting database type
  database-connection-2: Database connection
  database-initialization-2: Database initialization
  mutual-tls-support-for-oracle-database-2: Mutual TLS support for Oracle database
  override-node-persistence-resource-name: Override node persistence resource name
  logging: Logging
  infrastructure-testing: Infrastructure testing
  testing-service-manually: Testing service manually
  circuit-storage: Circuit storage
  pingone-recognize-node-2: PingOne Recognize node
  operations-api-2: Operations API
  testing-services-automatically: Testing services automatically
  configuring-circuit-storage-operations-api-and-node-persistence-test: Configuring circuit storage, Operations API, and node persistence test
  configuring-keylessd-node-test: Configuring Keylessd node test
  resources: Resources
---

# On-premise deployment

## Kubernetes deployment

### Components

The method PingOne Recognize adopts to ship its infrastructure components is Helm chart deployment.

The following diagram illustrates a general overview of the infrastructure components.

![Diagram shows the key components, their relationships, and includes relevant product/platform terms (PingOne Recognize and OpenShift) for search indexing and accessibility.](_images/openshift-k8s-diagram.png)

The PingOne Recognize infrastructure is composed of the following components:

**PingOne Recognize Node:** responsible for implementing the distributed privacy-preserving protocol for PingOne Recognize zero-proof biometric authentication

**Node Persistence Service**: service implementing a database abstraction layer (Postgres and OracleDB currently supported)

**Database**: database used by PingOne Recognize to store user data

**Circuit Storage Service**: service offering internal-use REST APIs to allow PingOne Recognize node to store circuits needed to authenticate users

**Database + S3 Storage**: used by Circuit Storage Service to store circuits and metadata

**PingOne Recognize REST API (Operations API)**: offers REST APIs for transaction confirmation and other backend services.

Each of the PingOne Recognize components has its own chart and can be deployed standalone, but we strongly suggest using our main Keylessd Helm chart to deploy all needed components together. For more information, see [Deployment Steps](#deployment-steps).

### Access the repositories

The customer is going to use two repositories:

**A Docker Image Registry**: *quay.io/keyless.technologies*

**A Helm Chart Registry**: *keylesstech.github.io*

To access the Docker repository the following command needs to be executed:

```bash
docker login quay.io -u < username > -p < password >
```

There is no need for authentication against the Helm Chart Registry.

### Deployment steps

1. Add the PingOne Recognize helm repository to your helm repository list with the following command:

   ```bash
   helm repo add keyless https://keylesstech.github.io
   ```

2. List the charts:

   ```bash
   helm search repo keyless
   ```

   ![Helm search repo results](_images/charts.png)

3. Get the `values.yaml` from the global `keylessd` chart.

   ```bash
   helm show values keyless/keylessd
   ```

   ![Helm show values results](_images/show-values.png)

   |   |                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | To manage secrets and dependencies, **include** the PingOne Recognize Helm chart, `keylessd`, as a dependency of your own chart. This increases your control and opportunities. By doing so, you could deploy custom monitoring agents alongside `keylessd`. |

4. After you're satisfied with your configuration, you can apply it with:

   ```bash
   helm upgrade --install \<release-name (for example keylessd)> keyless/keylessd
   ```

### Configuration

The deployment configuration is customizable using the Helm `values.yaml` file which is divided into the following sections:

```yaml
global: {}

keylessd:

  circuit-storage:
    ...
  node:
    ...
  operations-api:
    ...
  node-persistence:
    ...
```

**global** : global values such as :

* namespace: namespace name where to deploy the resources ( optional ), defaults to `default`

* token: to authenticate to the registry ( optional )

* createNamespace: to create the namespace if it doesn't already exists

**circuit-storage:** configuration specific to Circuit Storage Service

**node**: configuration specific to PingOne Recognize Node

**operations-api**: configuration for the Operation API component

**node-persistence**: configuration for the Node Persistence API component

#### Global

As stated above, the global section is optional and it is used if you do not desire to deploy each component into its own namespace but prefer to have all in a single namespace. You will then need to provide the name of the namespace and to set `createNamespace` variable to true as shown below

```yaml
global:
  token: # eyJhd.....................
  namespace: keyless
  createNamespace: true
```

**global.token** variable is used if you want PingOne Recognize chart to create the `imagePullSecret` secret used by the deployment to access the Docker registry. This is typical when you want to deploy each service into a separate namespace.

![JSON fragment showing how to specify imagePullSecrets](_images/global-token.png)

Secrets must be created within each namespace to pull the associated Docker image.

You can also create a secret **registry** of type `kubernetes.io/dockerconfigjson` to hold secrets accessed by the deployment.

|   |                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To know more about the format of the secret **registry** please refer to the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/secret/#docker-config-secrets). |

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | The **token** variable isn't needed if the registry doesn't require authentication. |

#### Circuit storage service

This service reads from and writes to s3-compatible storage. It requires an access key, a secret key, and a database to store metadata.

Skip this section to if you plan to supply the corresponding Secret to hold the credentials.

##### Expose circuit storage service

```yaml
keylessd:
  circuit-storage:
    publicRoute: true
    createRoute: true
    createIngress: false
    host: circuit-storage
    domain: keyless.local
```

Use the **publicRoute** variable to expose the circuit storage service outside the cluster.

You can also specify if Kubernetes should create an Ingress or a Route, depending if you're running on a generic cluster or an OpenShift cluster.

The circuit storage service is a backend service, so the default values are **false**.

If these values are set to `true`, the following values are also required:

* host

* domain

The corresponding ingress or route object should be configured to receive traffic from `<host>.<domain>`.

##### Custom certificate to access the database or the S3-compatible backend

```yaml
keylessd:
  circuit-storage:
    customCA: true
    certificates:
      - name: storage-cert
        mountPath: "/etc/ssl/custom-ca/storage-cert.pem"
        subPath: "storage-cert.pem"
        readOnly: true
      - name: db-cert
        mountPath: "/etc/ssl/custom-ca/db-cert.pem"
        subPath: "db-cert.pem"
        readOnly: true
```

Custom CA certificates are supported. Set the **customCA** variable to `true` and then add a ConfigMap object to your chart:

```yaml
---
kind: ConfigMap
apiVersion: v1
metadata:
  name: storage-cert
  namespace: my-namespace-name
data:
  storage-cert.pem: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
---
kind: ConfigMap
apiVersion: v1
metadata:
  name: db-cert
  namespace: my-namespace-name
data:
  db-cert.pem: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
```

This can be used when the s3-compatible backend exposes a secure connection that requires a certificate or if the database has additional authentication requirements.

The certificates are mounted to a specific location in the pod and added at runtime to the internal application keystore.

|   |                                                                                       |
| - | ------------------------------------------------------------------------------------- |
|   | The **mountPath** must always be in the format `/etc/ssl/custom-ca/<certificate>.pem` |

##### Exposed Java SpringBoot endpoints

The **endpoints** section of the `values.yaml` file, lets you customize the endpoints exposed by circuit storage. By default, the following `env` variables are exposed: `metrics` and `health-check`. (Passwords aren't displayed.)

```yaml
keylessd:
  circuit-storage:
    configMap:
      endpoints:
        web: health,env,metrics
        metrics: true
        health: true
        env: true
        # ...
```

##### Datadog integration

We support Datadog integration for circuit storage by setting up the **datadogApiKey** in the secrets section and the **datadog.uri**, which can vary depending according to your DataDog URI server.

```yaml
keylessd:
  circuit-storage:
    configMap:
      datadog:
        uri: https://api.datadoghq.eu
    secrets:
      datadogApiKey: "..."
```

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Leave blank if you don't want to use this integration. |

##### Adding Java options to circuit storage

The **javaOpts** variable customizes java options which might need to be adjusted to meet individual requirements.

```yaml
keylessd:
  circuit-storage:
    configMap:
      javaOpts: >-
        -XX:MaxRAMPercentage=75.0
        -Dspring.profiles.active=oracle,onprem
        -Dlogging.level.com.amazonaws=DEBUG
```

##### Database Connection

**configMap.springDatasource.url** variable holds the jdbc-formatted string to allow Circuit Storage to connect to its own database. The Instance needs a dedicated schema to be available ( default "circuit-storage")

```yaml
keylessd:
  circuit-storage:
    configMap:
      springDatasource:
        # Oracle
        url: jdbc:oracle:thin:@//<hostname>:1521/<service>
        # Or use Postgres instead:
        # url: jdbc:postgresql://<hostname>:5432/<dbName>
```

##### Database Initialization

To manage the database schema Circuit Storage makes use of the [Flyway](https://www.baeldung.com/database-migrations-with-flyway) library.

```yaml
keylessd:
  circuit-storage:
    configMap:
      springFlyway:
        enabled: true
        locations: oracle
```

**configMap.springFlyway.enabled** variable allows you to enable or disable database initialization scripts to be run at start time.

**configMap.springFlyway.locations** variable allows you to set "oracle" or "postgres" location depending on which database you're using ( currently only the two mentioned are supported).

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Disabling Flyway means that you'll need to initialize the database yourself, so please, if that's the case, reach out to us so that we can provide you the database initialization script to you |

##### Mutual TLS Support for Oracle Database

Starting with release 0.1.4 it is possible to connect to Oracle Database using mutual TLS authentication.

To achieve this the Oracle Wallet archive is needed.

To configure Circuit Storage to use Oracle Wallet follow this procedure:

* Unzip the Oracle Wallet

```shell
unzip wallet.zip -d mywallet
Archive:  wallet.zip
  inflating: mywallet/ewallet.pem
  inflating: mywallet/README
  inflating: mywallet/cwallet.sso
  inflating: mywallet/tnsnames.ora
  inflating: mywallet/truststore.jks
  inflating: mywallet/ojdbc.properties
  inflating: mywallet/sqlnet.ora
  inflating: mywallet/ewallet.p12
  inflating: mywallet/keystore.jks
```

* Execute the following command to create a Secret containing all files inside the wallet.

  ```
  In the example below the name of the secret will be "`wallet`"
  ```

```bash
$ kubectl create secret generic wallet --from-file=./mywallet/ -n <namespace-name>
secret/wallet created
```

* Modify `values.yaml`, given the following tnsnames.ora example file

`tnsnames.ora`

```none
circuitstoragetest_high = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
circuitstoragetest_low = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
circuitstoragetest_medium = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
circuitstoragetest_tp = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
circuitstoragetest_tpurgent = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
```

and `TNS_ADMIN=/network/admin` as the directory which the wallet secret will be mounted into, as such:

```yaml
keylessd:
  circuit-storage:
    mtls:
      secretName: wallet
    configMap:
      springDatasource:
        url: jdbc:oracle:thin:@circuitstoragetest_high?TNS_ADMIN=/network/admin
```

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Remember that you will still need to provide database username and password as the following secrets:- secrets.datasourceUsername

- secrets.datasourcePassword |

##### Override circuit storage resource came

It is possible to override the default resource name of Circuit Storage using the **fullnameOverride** variable. Otherwise, the assumed resource name is `circuit-storage-<release-name>`.

#### PingOne Recognize node

##### Expose PingOne Recognize node service

```yaml
keylessd:
  node:
    publicRoute: true
    createRoute: false
    createIngress: true
    host: node
    domain: keyless.technology
```

To expose PingOne Recognize Node service outside the Cluster, **publicRoute** variable needs be used.

In addition to this, it is possible to specify if Kubernetes should create an Ingress or a Route , depending if you're running on a vanilla cluster or on OpenShift.

As Keylessd Node needs to be exposed the default values for `publicRoute`, `createRoute` and `createIngress` are as shown above.

You will also need to set the following two variables:

* **host**

* **domain**

as shown above, so that the corresponding Ingress/Route object will be configured to get traffic from `<host>.<domain>`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As there can be edge cases where you would prefer to manage Ingresses outside our Chart it is possible to set **publicRoute** to falseIn this case you'll need to provide the Ingress/Route configuration, but keep in mind that the traffic needs to flow from the Ingress controller to the PingOne Recognize Node in **passthrough mode** as the TLS termination happens at the node level. |

As the PingOne Recognize node will use a certificate that will be mounted at runtime into the pod, to terminate the TLS connection, regardless of the value of **publicRoute**, it is required to specify the **host** and **domain** to be used, which need to corresponds to ones used to generate the certificate.

As an example, let's say that our final endpoint is node.keyless.technology, and that we have a certificate generated using the correct CN (again node.keyless.technology) then in this case the **host** variable will correspond to "node", meanwhile **domain** will correspond to "keyless.technology".

```yaml
keylessd:
  node:
    host: node
    domain: keyless.technology
```

**certName** variable is used to reference the secret name that hosts the certificate.

```yaml
keylessd:
  node:
    certName: node
```

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The expected format for the certificate is the one refecenced here: [Kubernetes TLS secret documentation](https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets) |

**configMap.nodeConfig.storageUrl** variable is used to reference Circuit Storage service in the format `http://<service-name>.<namespace>.svc.cluster.local`

**configMap.nodeConfig.databaseUrl** variable is used to reference Node Persistence service in the format `http://<service-name>.<namespace>.svc.cluster.local`

```yaml
keylessd:
  node:
    configMap:
      nodeConfig:
        storageUrl: http://circuit-storage-keylessd.keyless.svc.cluster.local
        databaseUrl: http://node-persistence-keylessd.keyless.svc.cluster.local
```

##### Override PingOne Recognize node resource name

It is possible to override the default resource name of PingOne Recognize Node using the **fullnameOverride** variable. Otherwise, the assumed resource name is `node-<release-name>`.

#### Operations API

##### Expose Operations API service

```yaml
keylessd:
  operations-api:
    publicRoute: true
    createRoute: false
    createIngress: true
    host: operations-api
    domain: keyless.local
```

To expose Operations API service outside the Cluster, **publicRoute** variable can be used.

In addition to this, it is possible to specify if Kubernetes should create an Ingress or a Route , depending if you're running on a vanilla cluster or on OpenShift.

As Operations API needs to be exposed the default values for `publicRoute`, `createRoute` and `createIngress` are as shown above.

You will also need to set the following two variables:

* **host**

* **domain**

as shown above, so that the corresponding Ingress/Route object will be configured to get traffic from `<host>.<domain>`.

|   |                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | As there can be edge cases where you would prefer to manage Ingresses outside our Chart it is possible to set **publicRoute** to falseIn this case you'll need to provide the Ingress/Route configuration, but keep in mind that the traffic needs to flow from the Ingress controller to Operations API in **edge mode** as the TLS termination happens at the cluster level. |

**configMap.nodePersistenceApiUrl** variable is used to reference Node Persistence service in the format `http://<service-name>.<namespace>.svc.cluster.local`

```yaml
keylessd:
  operations-api:
    configMap:
      nodePersistenceApiUrl: https://node-persistence.default.svc.cluster.local:8080
```

##### Override Operations API resource name

It is possible to override the default resource name of Operations API using the **fullnameOverride** variable. Otherwise, the assumed resource name is `operations-api-<release-name>`.

#### Node persistence

Because this service reads fom and writes to a database, a secret is required for access.

##### Exposed Java SpringBoot endpoints

The **endpoints** section of the `values.yaml` file, allows you to customize the amount of endpoints exposed by Node Persistence, usually the defaults are set to expose `env` variables ( passwords are **not** shown), `metrics` and `health-check`.

```yaml
keylessd:
  node-persistence:
    configMap:
      endpoints:
        web: health,env,metrics
        metrics: true
        health: true
        env: true
        # ...
```

##### Datadog integration

We support Datadog Integration for node persistence by setting up the **datadogApiKey** in the secrets section and the **datadog.uri**, which can vary depending on whether you use datadog.eu, datadog.com, or other servers.)

```yaml
keylessd:
  node-persistence:
    configMap:
      datadog:
        uri: https://api.datadoghq.eu
    secrets:
      datadogApiKey: "..."
```

|   |                                                        |
| - | ------------------------------------------------------ |
|   | Leave blank if you don't wish to use this integration. |

##### Adding Java options to node persistence

The **javaOpts** variable customizes java options which might need to be adjusted according to individual requirements.

```yaml
keylessd:
  node-persistence:
    configMap:
      javaOpts: >-
        -XX:MaxRAMPercentage=75.0
        -Dlogging.level.com.amazonaws=DEBUG
```

##### Setting database type

At the moment of writing Node Persistence supports Oracle and Postgres databases

To set which database type Node Persistence will need to use, it is possible to set springProfile variable to either "oracle" or "postgres"

```yaml
keylessd:
  node-persistence:
    configMap:
      springProfile: oracle
```

##### Database connection

**configMap.springDatasource.url** variable holds the jdbc-formatted string to allow Node Persistence to connect to its own database. The Instance needs a dedicated schema to be available ( default "keylessd")

```yaml
keylessd:
  node-persistence:
    configMap:
      springDatasource:
        # Oracle
        url: jdbc:oracle:thin:@//<hostname>:1521/<service>
        # Or use Postgres instead:
        # url: jdbc:postgresql://<hostname>:5432/<dbName>
```

##### Database initialization

To manage the database schema Node Persistence makes use of the [Flyway](https://www.baeldung.com/database-migrations-with-flyway) library.

```yaml
keylessd:
  node-persistence:
    configMap:
      springFlyway:
        enabled: true
        locations: oracle
```

**configMap.springFlyway.enabled** variable allows you to enable or disable database initialization scripts to be run at start time.

**configMap.springFlyway.locations** variable allows you to set "oracle" or "postgres" location depending on which database you're using ( currently only the two mentioned are supported).

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Disabling Flyway means that you'll need to initialize the database yourself, so please, if that's the case, reach out to us so that we can provide you the database initialization script to you |

##### Mutual TLS support for Oracle database

Starting with release 0.1.4 it is possible to connect to Oracle Database using mutual TLS (mTLS) authentication.

To achieve this the Oracle Wallet archive is needed.

To configure Node Persistence to use Oracle Wallet follow this procedure:

* Unzip the Oracle Wallet

```shell
unzip wallet.zip -d mywallet
Archive:  wallet.zip
  inflating: mywallet/ewallet.pem
  inflating: mywallet/README
  inflating: mywallet/cwallet.sso
  inflating: mywallet/tnsnames.ora
  inflating: mywallet/truststore.jks
  inflating: mywallet/ojdbc.properties
  inflating: mywallet/sqlnet.ora
  inflating: mywallet/ewallet.p12
  inflating: mywallet/keystore.jks
```

* Execute the following command to create a Secret containing all files inside the wallet.

  ```
  In the example below the name of the secret will be "`wallet`"
  ```

```bash
$ kubectl create secret generic wallet --from-file=./mywallet/ -n <namespace-name>
secret/wallet created
```

* Modify `values.yaml`, given the following tnsnames.ora example file

`tnsnames.ora`

```none
nodepersistencetest_high = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
nodepersistencetest_low = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
nodepersistencetest_medium = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
nodepersistencetest_tp = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
nodepersistencetest_tpurgent = (description= (address=(protocol=...)(port=...)(host=...))(connect_data=(service_name=...))(security=(ssl_server_cert_dn="CN=..., OU=..., O..., L..., ST=..., C=..")))
```

and `TNS_ADMIN=/network/admin` as the directory which the wallet secret will be mounted into, as such:

```yaml
keylessd:
  node-persistence:
    mtls:
      secretName: wallet
    configMap:
      springDatasource:
        url: jdbc:oracle:thin:@nodepersistencetest_high?TNS_ADMIN=/network/admin
```

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Remember that you will still need to provide database username and password as the following secrets:- secrets.datasourceUsername

- secrets.datasourcePassword |

##### Override node persistence resource name

It is possible to override the default resource name of Node Persistence using the **fullnameOverride** variable. Otherwise, the assumed resource name is `node-persistence-<release-name>`.

### Logging

Log levels are configurable for all applications except **keylessd**.

**Operations API:**

The log level is configurable over the "configMap.logLevel" configuration key in the helm chart which by default is set to "info", the following values are valid (debug, info, warning, error, critical)

**Node Persistence / Circuit Storage:**

The log level is configurable over the "configMap.loggingLevel.root" configuration key in the helm chart which by default is set to "info", the following values are valid (trace, debug, info, warn, error)

## Infrastructure testing

Testing the correct deployment of PingOne Recognize service can be done with the following methods.

### Testing service manually

#### Circuit storage

To test the correct configuration of Circuit Storage it is possible to use the following commands to upload a file from your local environment to the storage.

If Circuit Storage is exposed outside the cluster ( meaning it has been deployed with `publicRoute: true` ) you can issue the following command to test the service

```bash
$ curl --location --request POST '<host>.<domain>:<port which the ingress controller is listening on>/api/v1/circuits/qqF0FC59D87AA45dC15DA1F8A3377A17E423E1F0833343A5865D5E365133090A/qqqB155F07FA55A74FDB3C244B600D5E727EC0982392B89EEDF72DB37A346235/ad000008374B155F07FA55A7000000106F54E35F5FC8C87BF8E4691E9AA98CB8/a4aqa107D779ABDEA0CC5DEF5623F1BB2691D49AFD0A7DDBB6FB0FF3CF0B00101D75AE93C21C3' --form 'pipelineId="pipeline_1"' --form 'blob=@"/home/$USER/<a test file>.txt"'
```

If Circuit Storage is not exposed with an Ingress object or it is not possible to reach it directly from outside the cluster you can issue a port-forward command so that the Circuit Storage service is exposed on localhost:

```bash
$ kubectl port-forward service/circuit-storage-keylessd -n <namespace> 8080:8080
```

Then it is possible to issue the following command from your local machine to upload a test file

```bash
$ curl --location --request POST 'localhost:8080/api/v1/circuits/qqF0FC59D87AA45dC15DA1F8A3377A17E423E1F0833343A5865D5E365133090A/qqqB155F07FA55A74FDB3C244B600D5E727EC0982392B89EEDF72DB37A346235/ad000008374B155F07FA55A7000000106F54E35F5FC8C87BF8E4691E9AA98CB8/a4aqa107D779ABDEA0CC5DEF5623F1BB2691D49AFD0A7DDBB6FB0FF3CF0B00101D75AE93C21C3' --form 'pipelineId="pipeline_1"' --form 'blob=@"/home/$USER/<a test file>.txt"'
```

#### PingOne Recognize node

It is possible to test PingOne Recognize Node, running a dedicated containerized test tool as shown below:

```bash
docker run -it -e KL_API_KEY="<your_sdk_key>" -e KL_HOSTNAME_PORT="<fqdn_of_node>:<port>" quay.io/keyless_technologies/kl-node-test:v2.2.3_int
```

As the docker is hosted on our quay.io registry make sure to [be authenticated](#access-the-repositories) to it before running the command.

#### Operations API

To test the correct configuration of Operations API it is possible to use the following commands to upload a file from your local environment to the storage.

If Operations API is exposed outside the cluster ( meaning it has been deployed with `publicRoute: true` ) you can issue the following command to test the service:

```bash
curl -H "X-Api-Key:<you-sdk-key>" -vv http://<host>.<domain>:<port which the ingress controller is listening on>/v2/operations/<operation-id>
```

If Operations API is not exposed with an Ingress object or it is not possible to reach it directly from outside the cluster you can issue a port-forward command so that the Circuit Storage service is exposed on localhost:

```bash
kubectl port-forward service/operations-api-keylessd -n <namespace> 8080:8080
```

Then it is possible to issue the following command to read an operation-id, given that it is available in the database:

```bash
curl -H "X-Api-Key:<you-sdk-key>" -vv http://localhost:8080/v2/operations/<operation-id>
```

### Testing services automatically

Starting from release 0.1.3 it is possible to test PingOne Recognize deployment automatically, using helm testing feature as show below

After deploying the PingOne Recognize service stack successfully ( please refer to [this page](#kubernetes-deployment) to know how to do so) it is sufficient to invoke the following command

```none
# with 'keylessd' as the release name
helm test keylessd --logs
```

The above command will trigger individual test pods, one per each service.

It is also possible to adjust test configurations to fit customer's needs, in the `test` section of each service in `values.yaml`, as shown below:

```yaml
keylessd:
  circuit-storage:
    # ...
    test:
      image: postman/newman
      resources: {}
  operations-api:
    # ...
    test:
      image: postman/newman
      resources: {}
  node-persistence:
    # ...
    test:
      image: postman/newman
      resources: {}
  node:
    # ...
    # The following variables are used to test the deployment
    # running `helm test <release-name>`
    test:
      # -- Name of the docker containing the test tool
      image: quay.io/keyless_technologies/kl-node-test:v2.2.3_int
      # -- Hostname endpoint of the Node (FQDN)
      hostname: ""
      # -- Test suit is shipped with 2 certificates
      # /ca/rootCA.crt is a test certificate for local development
      # keylessCA.crt is used for client testing purposes, please use this one if in doubt
      cert: "/ca/rootCA.crt"
      # -- Api key available in the database
      apiKey: ""
      # -- Port where the service is expected to be exposed
      # If test is executed with hostname = fqdn it is the port
      # the cluster exposes as part of the external endpoint
      # probably 443
      port: ""
      resources: {}
```

#### Configuring circuit storage, Operations API, and node persistence test

Circuit Storage, Operations API and Node Persistence services have a similar setup:

Tests for these services need a container with Postman so the default one from Docker Hub is set as default. It is still possible to change the image ( for example if you have an internal Postman image or if Docker Hub registry cannot be exposed internally )

In any case tests are executed from within the Kubernetes Cluster.

#### Configuring Keylessd node test

Node tests are instead conducted from a proprietary container image. This test simulates a client connecting to the node from outside the cluster.

**hostname**: It is possible to specify the FQDN of the node ( i.e. the DNS record the node will be exposed outside the cluster, given that the endpoint is reachable)

**cert**: make sure the value is set to `keylessCA.crt` as this certificate is generated and trusted by the internal CA of PingOne Recognize.

**apiKey**: this is the same API Key we release to customers.

**port**: if the service is exposed externally the traffic flows from the internet towards the Ingress Controller which usually exposes this services with an https endpoint, so in most cases this port is `443`.

#### Resources

For any service it is possible to limit the resources used by the test pod specifying them as shown below:

```yaml
resources:
  ## -- Limits
  limits:
    cpu: 1000m
    memory: 1024Mi
  ## -- Requests
  requests:
    cpu: 800m
    memory: 1024Mi
```

---

---
title: On-premise installation manual
description: On-Premise installation manual for PingOne Recognize.
component: recognize
page_id: recognize:on-premise:on-premise-installation-manual
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-installation-manual.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# On-premise installation manual

PingOne Recognize is a privacy-first (zero-knowledge) biometrics and identity management platform that eliminates the need for businesses to centrally store and manage passwords, sensitive cryptographic keys, and other authentication data, without compromising on convenience and privacy for their users.

If preferred, customers can store the entire PingOne Recognize backend within their own infrastructure. This installation manual takes you through all of the necessary steps to get set up.

---

---
title: On-premise installation procedure
description: This page describes the installation procedure for PingOne Recognize on-premise.
component: recognize
page_id: recognize:on-premise:on-premise-installation-procedure
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-installation-procedure.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  general-configuration: General configuration
  namespace: Namespace
  helm-setup: Helm setup
  core-daemon: Core Daemon
  metrics-collector: Metrics Collector
  database-connection-and-sizing: Database connection and sizing
  operations-service: Operations Service
  administrator-dashboard: Administrator Dashboard
---

# On-premise installation procedure

## General configuration

PingOne Recognize is provided as a series of Helm charts. Helm charts contain configuration entries that can be overridden.

The following sections describe the relevant and supported configuration entries.

Other configuration entries can be overridden to suit customer needs, but are not explicitly supported by PingOne Recognize. For example:

```yaml
resources: {}
  # limits:
  #   cpu: 100m
  #   memory: 128Mi
  # requests:
  #   cpu: 100m
  #   memory: 128Mi

---
autoscaling:
# -- Enable Pod autoscaling
enabled: false
minReplicas: 1
maxReplicas: 100
targetCPUUtilizationPercentage: 80
targetMemoryUtilizationPercentage: 80

---
# -- List of certificates to be included in the pod
certificates: []
#  - name: storage-certificate
#    mountPath: "/etc/ssl/custom-ca/storage-cert.pem"
#    subPath: "storage-cert.pem"
#    readOnly: true
#  - name: db-cert
#    mountPath: "/etc/ssl/custom-ca/db-cert.pem"
#    subPath: "db-cert.pem"
#    readOnly: true
```

## Namespace

Namespaces can be overridden, but take extra care when configuring the endpoint in `values.yml`. For example:

```yaml
configMap:
  # Metrics Collector URI
  # `default` in this context references the namespace for the metrics-collector service
  metricsCollectorUrl: http://metrics-collector.default.svc.cluster.local
```

## Helm setup

The first step is to add the PingOne Recognize Helm repository to your Helm repository list with the following command:

```bash
helm repo add keyless https://example.com (the actual FQDN will be shared upon request)
```

The charts can then be listed:

```bash
helm search repo keyless
```

!["Helm search repo results](_images/keyless-helm-search.png)

The list of required values for each chart can be obtained using the `helm show values` command:

```bash
helm show values keyless/core-daemon
```

![Helm show values results](_images/keyless-helm-show-values.png)

Save and configure the reference `values.yaml` to suit your installation needs. Once configured, apply it with the following command:

```bash
helm upgrade --install <release-name (for example core-daemon)> keyless/core-daemon --atomic --wait
```

To allow container images to be pulled from the `quay.io` repository, a registry secret is required. This secret must contain the provided credentials in the format specified in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/secret/#docker-config-secrets).

## Core Daemon

To set up this service, the cluster's internal endpoint is required to allow Core Daemon to connect to PostgreSQL and S3. The default values are sufficient unless each service is deployed in its own dedicated namespace.

If not using AWS, a key must be generated and mounted inside the Core Daemon pods:

```bash
openssl ecparam -name secp256k1 -genkey -noout -out private.pem
openssl ec -in private.pem -pubout -out public.pem

kubectl create secret generic keypair -n <core-daemon-namespace> --from-file=tls.crt=public.pem --from-file=tls.key=private.pem
```

```yaml
global:
  namespace: <core-daemon-namespace>

image:
  tag: 2.30.0

configMap:
  # -- REQUIRED IF NOT USING AWS
  keysFileSystemPublicPath: /etc/ssl/keypair/tls.crt
  keysFileSystemPrivatePath: /etc/ssl/keypair/tls.key

  coreDaemonConfigEnvironment: <environment>
  cloudAwsRegionStatic: <aws-region>
  awsRegion: <aws-region>
  springProfilesActive: json-logging
  cloudAwsS3BucketName: <bucket-name>
  csSpringDatasourceUrl: jdbc:postgresql://<hostname>:5432/<dbName>
  npSpringDatasourceUrl: jdbc:postgresql://<hostname>:5432/<dbName>
  loggingLevelCoreRequest: DEBUG

# -- REQUIRED IF NOT USING AWS
certificates:
  - name: keypair
    mountPath: /etc/ssl/keypair
    readOnly: true

# -- Suggested sizing
resources:
  ## -- Limits
  limits:
    cpu: 1800m
    memory: 2048Mi
  ## -- Requests
  requests:
    cpu: 100m
    memory: 512Mi
```

## Metrics Collector

This service reads and writes from a database for a BI function. A secret is required to access it.

### Database connection and sizing

The `configMap.springDatasource.url` variable holds the JDBC-formatted string to allow Metrics Collector to connect to its own database. The instance requires a dedicated schema (default: `metricscollector`):

```yaml
global:
  namespace: <metrics-collector-namespace>

image:
  tag: 1.13.3

configMap:
  springDatasource:
    url: jdbc:postgresql://<hostname>:5432/<dbName>

# -- Suggested sizing
resources:
  ## -- Limits
  limits:
    cpu: 1800m
    memory: 2048Mi
  ## -- Requests
  requests:
    cpu: 100m
    memory: 700Mi
```

## Operations Service

To set up this service, the cluster's internal endpoint is required to allow Operations Service to connect to Core Daemon. The default values are sufficient unless each service is deployed in its own dedicated namespace:

```yaml
global:
  namespace: <operations-service-namespace>

image:
  tag: 2.34.0

configMap:
  # -- Core Daemon URI
  apiCoreDaemonBasePath: http://core-daemon.default.svc.cluster.local/

# -- Suggested sizing
resources:
  ## -- Limits
  limits:
    cpu: 1800m
    memory: 2048Mi
  ## -- Requests
  requests:
    cpu: 100m
    memory: 512Mi
```

## Administrator Dashboard

To set up this service, the cluster's internal endpoint is required to allow the Administrator Dashboard to connect to Core Daemon. The default values are sufficient unless each service is deployed in its own dedicated namespace:

```yaml
global:
  namespace: <administrator-dashboard-namespace>

image:
  tag: v1.3.5

configMap:
  typeormUsername: sdk-customer-dashboard-user
  typeormDatabase: sdkcustomerdashboard
  typeormConnection: postgres
  typeormHost: <hostname>
  typeormMigrations: "./migrations/*.ts"
  typeormPort: 5432
  typeormSslRejectUnauthorized: true
  metricsCollectorUrl: http://metrics-collector
  coreDaemonUrl: http://core-daemon
  #The port the service is exposed on
  port: 3000
# -- Suggested sizing
resources:
  ## -- Limits
  limits:
    cpu: 800m
    memory: 2000Mi
  ## -- Requests
  requests:
    cpu: 50m
    memory: 400Mi
```

---

---
title: On-premise upgrade procedure
description: This page describes the upgrade procedure for PingOne Recognize on-premise
component: recognize
page_id: recognize:on-premise:on-premise-upgrade-procedure
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-upgrade-procedure.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  cluster-and-runtime: Cluster and runtime
  breaking-changes: Breaking changes
  release-1-4-0: Release 1.4.0
  release-1-3-0: Release 1.3.0
  circuit-storage: Circuit Storage
  operations-service: Operations Service
  core-daemon: Core Daemon
  databases: Databases
---

# On-premise upgrade procedure

## Cluster and runtime

Helm charts are updated from time to time. Customers will be notified of each upgrade.

To upgrade the system, run a command similar to the following:

```bash
helm upgrade --install node-persistence keyless/core-daemon --version 1.0.0 --timeout 10m --wait --set image.tag=1.0.0  --atomic -f values.yaml -f secrets.yaml
```

Applications are also updated from time to time. For each update, customers are notified of a specific tag to set in the overrides of the corresponding `values.yml` file. After updating the file, the Helm chart must be upgraded, which causes pods to be recreated with the new code.

|   |                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------ |
|   | Running an unsupported component version combination may result in a non-functional installation and/or data loss. |

### Breaking changes

#### Release 1.4.0

No breaking change has been introduced between 1.3.0 and 1.4.0.

#### Release 1.3.0

In release 1.3.0, some configmap keys have been renamed. If you are upgrading from version 1.2.5, ensure you update your configurations accordingly to prevent issues.

##### Circuit Storage

```none
configMap.springDatasource.url --> configMap.springDatasourceUrl
configMap.bucket.name --> configMap.cloudAwsS3BucketName
configMap.bucket.region --> configMap.cloudAwsRegionStatic
configMap.bucket.endpointUrl --> configMap.cloudAwsS3EndpointUrl
configMap.api.nodePersistence.basePath --> configMap.apiNodePersistenceBasePath
```

##### Operations Service

```none
configMap.api.nodePersistence.basePath --> configMap.apiNodePersistenceBasePath
```

##### Core Daemon

```none
configMap.api.nodePersistence.basePath --> configMap.apiNodePersistenceBasePath
configMap.api.circuitStorage.basePath --> configMap.apiCircuitStorageBasePath
```

## Databases

All the components that use a DB have automatic migrations set up. This is the only supported setting.

While it is possible to disable automatic migrations and perform manual migrations instead, this approach is discouraged. If manual migrations are used, please contact support to get the schema changes.

Deactivation of automatic migrations may lead to a non functioning installation and/or data loss.

---

---
title: Planning for installation
description: Planning for installation of PingOne Recognize.
component: recognize
page_id: recognize:on-premise:on-premise-planning-for-installation
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-planning-for-installation.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Planning for installation

The PingOne Recognize backend is a Kubernetes-based solution. It's compatible with OpenShift 4.10 and is provided through a series of Helm charts. The installation process is intended for system administrators with expertise in Helm and Kubernetes.

The PingOne Recognize backend service is provided in a flexible format, allowing overrides to adapt to various customer deployment scenarios. The only hard dependencies are Kubernetes (on x86\_64 architecture), PostgreSQL, and an S3-compatible storage. More details are provided in the requirements section.

To ensure a functioning system, customers should plan for an adequate number of Kubernetes pods. They should also ensure sufficient storage and connection capacity for both the PostgreSQL database and the S3 layers, and ensure observability.
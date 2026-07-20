---
title: Additional servlet filters
description: Register and configure PingIDM Jetty servlet filters for CORS and large-payload protection (custom servlet filters removed in 8.0)
component: pingidm
version: 8.1
page_id: pingidm:install-guide:register-servlet-filters
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/register-servlet-filters.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Jetty", "Configuration", "Servlet Filter"]
---

# Additional servlet filters

|   |                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Custom servlet filters aren't supported in IDM 8.0 and later. The only `servletfilter-*` configurations you can continue to use are `CrossOriginFilter` and `LargePayloadServletFilter`. Learn more in [Discontinued functionality](../release-notes/removed-functionality.html#removed-custom-servlet-filters-80). |

You can register and customize only the `org.eclipse.jetty.ee10.servlets.CrossOriginFilter` and `org.forgerock.openidm.jetty.LargePayloadServletFilter` servlet filters. These filters are available to protect against cross-site request forgery and overly large request payloads.

A sample servlet filter configuration is provided in the `/path/to/openidm/conf/servletfilter-cors.json` file:

```json
{
    "initParams" : {
        "allowedOrigins" : "https://localhost:&{openidm.port.https}",
        "allowedMethods" : "GET,POST,PUT,DELETE,PATCH",
        "allowedHeaders" : "accept,x-openidm-password,x-openidm-nosession,
                           x-openidm-username,content-type,origin,
                           x-requested-with",
        "allowCredentials" : true,
        "chainPreflight" : false
    },
    "urlPatterns" : [
        "/*"
    ],
    "filterClass" : "org.eclipse.jetty.servlets.CrossOriginFilter"
}
```

The sample configuration includes the following properties:

* `filterClass`

  (String) The servlet filter to register.

The following additional properties can be configured for the filter:

* `httpContextId`

  (String) The HTTP context in which to register the filter. Default value `"openidm"`.

* `servletNames`

  (Array of strings) A list of servlet names where the filter should apply. Default value `["OpenIDM REST"]`.

* `urlPatterns`

  (Array of strings) A list of URL patterns where the filter applies. Default value `["/*"]`.

* `initParams`

  (Object) A map of initialization parameters passed to the servlet filter's `init` method. Keys are strings, and values can be strings, booleans, or numbers. For parameters that accept multiple values, use a comma-delimited string. Learn more in the [Interface FilterConfig](https://docs.oracle.com/javaee/5/api/javax/servlet/FilterConfig.html) documentation.

---

---
title: Case insensitivity for a JDBC repo
description: Configure case-insensitive collation for PingIDM JDBC repositories, including MySQL, PostgreSQL, Oracle DB, SQL Server, and DB2
component: pingidm
version: 8.1
page_id: pingidm:install-guide:repo-case-insensitive
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/repo-case-insensitive.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "JDBC"]
---

# Case insensitivity for a JDBC repo

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | The following topic only applies if you have set up a JDBC repository, as described in [Select a repository](chap-repository.html) |

A DS repository is case-insensitive by default. The supported JDBC repositories are generally case-sensitive by default. Case-sensitivity can cause issues if queries expect results to be returned, regardless of case.

For example, with the default configuration of a MySQL database, a search for an email address of `scarter@example.com` might return a result, while a search for `scarter@EXAMPLE.COM` might return an `Unable to find account` error.

If you need to support case-insensitive queries, you must configure a case-insensitive collation in your JDBC repository, on the specific columns that require it. For example:

* For a generic managed object mapping in MySQL or MariaDB, change the default collation of the `managedobjectproperties.propvalue` column to `utf8_general_ci`. Note that this changes case-sensitivity for *all* managed object properties. To change case-sensitivity for all the properties of a specific object, specify a different table for the `propertiesTable` entry in your `repo.jdbc.json` for that object, and adjust the collation on that table. To change case-sensitivity only for certain properties of an object, use an explicit mapping.

* For a PostgreSQL repository, use an explicit table structure if you require case-insensitivity. Managing case-insensitivity at scale with generic tables in PostgreSQL is not supported. For more information about object mappings, refer to [Mappings with a JDBC repository](../objects-guide/explicit-generic-mapping-jdbc.html).

* For an Oracle DB repository, refer to the corresponding [Oracle documentation](https://docs.oracle.com/database/121/NLSPG/ch5lingsort.htm#NLSPG0051).

* For a SQL Server repository, refer to the corresponding [Windows documentation](https://docs.microsoft.com/en-us/sql/t-sql/statements/windows-collation-name-transact-sql?view=sql-server-2017).

* For a DB2 repository, refer to the corresponding [DB2 documentation](https://developer.ibm.com/articles/making-db2-case-insensitive/).

---

---
title: Cluster standby mode
description: Enable PingIDM cluster standby mode to segment instances into active and standby groups, and manage transitions using the cluster activation endpoint
component: pingidm
version: 8.1
page_id: pingidm:install-guide:cluster-standby
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/cluster-standby.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  enable-standby-mode: Enable standby mode
  activate-standby-nodes: Transition active nodes
  activate_a_standby_node: Activate a standby node
  set_an_active_node_to_standby: Set an active node to standby
  read_the_current_state: Read the current state
  standby-node-behavior: Standby node behavior
  standby-authentication: Configure standby endpoint authentication
  standby-failover-procedure: Failover procedure
---

# Cluster standby mode

The cluster standby feature lets you segment a set of IDM instances into two groups: *active* and *standby*.

Active instances process schedules (including clustered reconciliation schedules) and mappings configured for queued sync. Standby instances don't process these operations, functioning as hot spares that can be activated on demand.

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Standby instances still respond to direct client API requests, such as managed object mutations and client-dispatched reconciliation invocations. A load balancer or reverse proxy must ensure that standby nodes are not targeted by client-dispatched requests. |

|   |                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Setting up and maintaining an active-standby deployment architecture is complex. The cluster standby endpoint gives you control over individual node behavior, but the broader deployment configuration (such as, networking, load balancing, database replication, and failover orchestration) is the responsibility of the deployer and is outside the boundaries of product support. |

## Enable standby mode

To enable the cluster standby feature, set both of the following properties to `true` in `resolver/boot.properties` for each instance that participates in standby mode:

```properties
org.forgerock.feature.cluster.active.passive=true
org.forgerock.feature.cluster.improved=true
```

Instances with both properties set to `true` startup into standby mode by default.

## Transition active nodes

Use the `openidm/cluster/active` endpoint to transition a node between active and standby states.

Learn more about the [cluster activation endpoint](../rest-api-reference/endpoints/rest-cluster-active.html).

### Activate a standby node

To transition a standby node to active:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request PUT \
--header "Accept-API-Version: resource=1.0" \
--header 'Content-Type: application/json' \
--header 'If-Match: *' \
--data '{"state":"ACTIVE"}' \
'http://localhost:8080/openidm/cluster/active'
```

### Set an active node to standby

To transition an active node to standby:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request PUT \
--header "Accept-API-Version: resource=1.0" \
--header 'Content-Type: application/json' \
--header 'If-Match: *' \
--data '{"state":"STANDBY"}' \
'http://localhost:8080/openidm/cluster/active'
```

### Read the current state

To check the current state of a node:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--request GET \
--header "Accept-API-Version: resource=1.0" \
'http://localhost:8080/openidm/cluster/active'
```

## Standby node behavior

When a node is in standby mode:

* The node doesn't execute persistent schedules.

* The node doesn't participate in clustered reconciliation.

* The node doesn't process queued sync mappings.

* The node does respond to direct API requests (REST calls for managed objects, configuration, and so on).

When a node transitions from standby to active, it resumes processing schedules, clustered reconciliation, and queued sync.

## Configure standby endpoint authentication

Access to the `openidm/cluster/active` endpoint is authenticated using credentials stored as a secret. Configure the username and password through the purpose identified by `idm.cluster.activation.credentials`.

Learn more in [Store username and password as a secret](../security-guide/secret-stores.html#store-user-pass-as-secret).

## Failover procedure

The following is a typical failover procedure:

1. Transition the formerly active nodes by sending a `PUT` request with `{"state":"STANDBY"}` to each applicable node.

2. Activate the formerly standby nodes by sending a `PUT` request with `{"state":"ACTIVE"}` to each applicable node.

3. Update the load balancer configuration to route traffic to the newly active nodes.

To failback, reverse the procedure.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Both active and standby IDM instances must access a database layer with consistent state during failover transitions. Ensure that database replication latencies between the repositories supporting active and standby nodes are less than the time required to complete the failover cutover. |

---

---
title: Configuration updates in a cluster
description: Configure how PingIDM cluster nodes read configuration updates, using repository-based or file-based strategies through system.properties settings
component: pingidm
version: 8.1
page_id: pingidm:install-guide:cluster-config-changes
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/cluster-config-changes.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Cluster", "Configuration", "Properties"]
section_ids:
  repo-based-config: Repository-based configuration
  file-based-config: File-based configuration
---

# Configuration updates in a cluster

IDM can read its configuration from the following locations:

* *Repository.* Each instance reads its configuration from the `configobjects` and `configobjectproperties` tables in a JDBC repository, or from the `ou=config,dc=openidm,dc=forgerock,dc=com` baseDN in a DS repository.

* *Filesystem.* Each instance reads its configuration from the JSON files under its `conf` directory and stores the configuration locally in memory.

  In a clustered deployment, file-based configuration changes must be applied manually across all instances.

* *Memory.* The configuration can diverge if an instance is cut from its cluster due to a networking issue or a misconfigured load balancer. In this case, configuration changes made in the repository might not be detected and the configuration in memory will not be updated.

There are two properties in the `conf/system.properties` file that determine how configuration changes are handled for each instance:

* openidm.config.repo.enabled

  When this property is set to `true`, the instance reads configuration changes from the repository.

  The default setting (`# openidm.config.repo.enabled=false`) indicates that the parameter is true. Uncomment that line to prevent the instance from reading configuration changes from the repository.

* openidm.fileinstall.enabled

  When this property is set to `true`, the instance reads its configuration from the files in its `conf/` directory.

  The default setting (`# openidm.fileinstall.enabled=false`) indicates that the parameter is true. Uncomment that line to prevent the instance from reading file-based configuration changes.

|   |                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Every node in the cluster must have the identical configuration setting. For example, if you set `openidm.config.repo.enabled=true, openidm.fileinstall.enabled=false` on one node, you must set exactly the same options on every node in the cluster. |

## Repository-based configuration

Traditional clustered deployments share a *mutable* configuration that is read from a shared repository. The repository initially loads the configuration from the JSON files in the `conf` directory of the first instance that is configured in the cluster. However configuration changes are made, they are written to the repository, and the repository is the authoritative configuration source.

Therefore, a traditional clustered deployment generally has the following configuration:

```
openidm.config.repo.enabled=true
openidm.fileinstall.enabled=false
```

## File-based configuration

A file-based configuration lets you store the system configuration in a version-controlled filesystem and push a new version out to all nodes when the configuration changes. This makes versioning and rolling out new configuration easier than pushing it out over REST.

Container deployments often require an *immutable* configuration that is read from a filesystem (such as a Docker image) and stored in memory. The filesystem is the authoritative configuration source and configuration changes are *not* written to the repository.

For more information on building an IDM Docker image, refer to [Manage configuration with Docker](docker.html).

A typical container deployment includes the following configuration:

```
openidm.config.repo.enabled=false
openidm.fileinstall.enabled=true
```

If file-based configuration is used, you *must* ensure that the configuration across instances remains consistent. Because the file-based configuration is not shared between instances, changes made to one node's configuration must be applied manually to all nodes across the cluster.

By default, IDM polls JSON configuration files in each `conf/` directory for changes. Ping recommends you disable automatic polling of configuration files to prevent untested configuration changes from disrupting your identity service.

For more information, refer to [Disable automatic configuration updates](../security-guide/disabling-auto-config-updates.html).

---

---
title: Embedded Jetty configuration
description: "Configure PingIDM's embedded Jetty web server, including global settings, listener connectors, and key store and trust store setup"
component: pingidm
version: 8.1
page_id: pingidm:install-guide:appendix-jetty
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/appendix-jetty.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Jetty", "Configuration"]
section_ids:
  jetty-key-store-trust-store: Jetty key store and trust store
  understanding-jetty-config-apache-felix: Understanding Jetty configuration and Apache Felix
---

# Embedded Jetty configuration

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In IDM 8.0, `jetty.xml` is no longer supported.When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment.Learn more in [Jetty 12 support](../release-notes/whats-new.html#jetty_12_support). |

PingIDM includes an embedded Jetty web server. The Jetty web server configuration is included in IDM's configuration service, allowing for Jetty properties to be modified at runtime. The configuration includes:

* A `webserver.json` that contains the global Jetty settings

* A `webserver.listener-*.json` that configures a Jetty connector to listen on a specific port

  |   |                                                                                          |
  | - | ---------------------------------------------------------------------------------------- |
  |   | At least one `webserver.listener-*.json` must be defined and enabled for Jetty to start. |

  Learn more about the configuration properties for `webserver.json` and `webserver.listener-*.json` in [Jetty configuration properties](idm-config-properties-jetty.html).

## Jetty key store and trust store

Jetty depends on IDM to supply the `mainKeyStore` and `mainTrustStore` configured in `secrets.json`. If the `mainTrustStore` is not defined, the `mainKeyStore` is used as Jetty's trust store.

## Understanding Jetty configuration and Apache Felix

IDM runs in the [Apache Felix](https://felix.apache.org/documentation/index.html) framework, which allows the Jetty configuration to be specified and managed through [OSGI](https://www.osgi.org/resources/what-is-osgi/) components. If there is a change to the Jetty configuration in `webserver.json`, Apache Felix rebuilds the Jetty instance.

Learn more about OSGI and Apache Felix in the [Architectural overview](../setup-guide/chap-overview.html).

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Changes to `webserver.listener-*.json` files don't cause Jetty to restart. Only the Jetty connector configured by the changed file is restarted or removed if the file is deleted or disabled. |

---

---
title: Host and port information
description: Reference for PingIDM default HTTP, HTTPS, and mutual-auth ports and how to change them in boot.properties
component: pingidm
version: 8.1
page_id: pingidm:install-guide:appendix-ports-used
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/appendix-ports-used.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Ports", "Hosts"]
---

# Host and port information

To change the default IDM hostname or listening ports, edit the applicable entry in `openidm/resolver/boot.properties`:

```none
openidm.port.http=8080
openidm.port.https=8443
openidm.port.mutualauth=8444
openidm.host=localhost

openidm.auth.clientauthonlyports=8444
```

* `8080`

  HTTP access to the REST API, requiring IDM authentication. This port is not secure, exposing clear text passwords and all data that is not encrypted. This port is therefore not suitable for production use.

* `8443`

  HTTPS access to the REST API, requiring IDM authentication

* `8444`

  HTTPS access to the REST API, requiring SSL mutual authentication. Clients that present certificates found in the truststore (`openidm/security/`) are granted access to the system.

---

---
title: IBM DB2 repository
description: Configure IBM DB2 as a PingIDM repository, including JDBC driver setup, schema import, and optional Kerberos authentication
component: pingidm
version: 8.1
page_id: pingidm:install-guide:repository-db2
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/repository-db2.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "IBM DB2"]
section_ids:
  db2-kerberos-auth: Kerberos authentication with a DB2 repository
---

# IBM DB2 repository

This section makes the following assumptions about the DB2 environment. If these assumptions do not match your DB2 environment, adapt the subsequent instructions accordingly.

* DB2 is running on the localhost, and is listening on the default port (50000).

* The user `db2inst1` is configured as the DB2 instance owner, and has the password `Passw0rd1`.

* You are using a supported version of DB2. Refer to [Supported repositories](../release-notes/before-you-install.html#prerequisites-repositories).

This section assumes that you will use basic username/password authentication. You can also [configure Kerberos authentication with a DB2 repository](#db2-kerberos-auth).

Before you start, make sure that the server is stopped.

```
/path/to/openidm/shutdown.sh
OpenIDM is not running, not stopping.
```

Configure IDM to use the DB2 repository, as described in the following steps:

1. Download the DB2 JDBC driver for your database version from the [IBM download site](https://www-01.ibm.com/support/docview.wss?uid=swg21363866) and place it in the `openidm/bundle` directory.

   |   |                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Ping recommends using the `db2jcc4.jar` driver, as the `db2jcc.jar` driver is deprecated. For more information, refer to the [DB2 JDBC Driver Versions](https://www-01.ibm.com/support/docview.wss?uid=swg21363866).For a list of supported DB2 versions, refer to [Supported repositories](../release-notes/before-you-install.html#prerequisites-repositories). |

2. Remove the default DS repository configuration file (`repo.ds.json`) from your project's `conf/` directory. For example:

   ```
   cd /path/to/openidm/my-project/conf/
   rm repo.ds.json
   ```

3. Copy the database connection configuration file for DB2 (`datasource.jdbc-default.json`) and the database table configuration file (`repo.jdbc.json`) to your project's configuration directory. For example:

   ```
   cp /path/to/openidm/db/db2/conf/datasource.jdbc-default.json my-project/conf/
   cp /path/to/openidm/db/db2/conf/repo.jdbc.json my-project/conf/
   ```

4. Update the connection configuration to reflect your DB2 deployment. The default connection configuration in the `datasource.jdbc-default.json` file is as follows:

   ```json
   {
       "driverClass" : "com.ibm.db2.jcc.DB2Driver",
       "jdbcUrl" : "jdbc:db2://&{openidm.repo.host}:&{openidm.repo.port}/dopenidm:retrieveMessagesFromServerOnGetMessage=true;",
       "databaseName" : "sopenidm",
       "username" : "openidm",
       "password" : "openidm",
       "connectionTimeout" : 30000,
       "connectionPool" : {
           "type" : "hikari",
           "minimumIdle" : 20,
           "maximumPoolSize" : 50
       }
   }
   ```

   Specify the values for `openidm.repo.host` and `openidm.repo.port` in one of the following ways:

   > **Collapse: Set in an IDM Properties File**
   >
   > Set the values in `resolver/boot.properties` or your project's `conf/system.properties` file, for example:
   >
   > ```json
   > openidm.repo.host = localhost
   > openidm.repo.port = 50000
   > ```

   > **Collapse: Set as an Environment Variable**
   >
   > Set the properties in the `OPENIDM_OPTS` environment variable and export that variable before startup. You must include the JVM memory options when you set this variable. For example:
   >
   > ```
   > export OPENIDM_OPTS="-Xmx2048m -Xms2048m -Dopenidm.repo.host=localhost -Dopenidm.repo.port=50000"
   > /path/to/openidm/startup.sh -p my-project
   > Executing ./startup.sh...
   > Using OPENIDM_HOME:   /path/to/openidm
   > Using PROJECT_HOME:   /path/to/openidm
   > Using OPENIDM_OPTS:   -Xmx2048m -Xms2048m -Dopenidm.repo.host=localhost -Dopenidm.repo.port=50000
   > ...
   > Using boot properties at /path/to/openidm/resolver/boot.properties
   > -> OpenIDM version "8.1.1"
   > OpenIDM ready
   > ```

5. Create a user database for IDM (`dopenidm`).

   ```
   db2 create database dopenidm
   ```

6. Import the IDM data definition language script into your DB2 instance.

   ```
   cd /path/to/openidm
   db2 -i -tf db/db2/scripts/openidm.sql
   ```

   The database schema is defined in the `SOPENIDM` database.

7. You can show the list of tables in the repository, using the `db2 list` command, as follows:

   ```
   db2 LIST TABLES for all
   Table/View                      Schema          Type  Creation time
   ------------------------------- --------------- ----- --------------------------
   CLUSTEROBJECTPROPERTIES         SOPENIDM        T     2015-10-01-11.58.05.968933
   CLUSTEROBJECTS                  SOPENIDM        T     2015-10-01-11.58.05.607075
   CONFIGOBJECTPROPERTIES          SOPENIDM        T     2015-10-01-11.58.01.039999
   CONFIGOBJECTS                   SOPENIDM        T     2015-10-01-11.58.00.570231
   GENERICOBJECTPROPERTIES         SOPENIDM        T     2015-10-01-11.57.59.583530
   GENERICOBJECTS                  SOPENIDM        T     2015-10-01-11.57.59.152221
   INTERNALUSER                    SOPENIDM        T     2015-10-01-11.58.04.060990
   LINKS                           SOPENIDM        T     2015-10-01-11.58.01.349194
   MANAGEDOBJECTPROPERTIES         SOPENIDM        T     2015-10-01-11.58.00.261556
   MANAGEDOBJECTS                  SOPENIDM        T     2015-10-01-11.57.59.890152
   ...
   ```

8. Connect to the `openidm` database, and run the script that creates the tables required by the workflow engine:

   ```
   db2 connect to dopenidm
   db2 -i -tf /path/to/openidm/db/db2/scripts/flowable.db2.all.create.sql
   ```

9. If you plan to direct audit logs to this repository, run the script that sets up the audit tables:

   ```
   db2 -i -tf /path/to/openidm/db/db2/scripts/audit.sql
   ```

When you have set up DB2 for use as the internal repository, make sure that the server starts without errors.

## Kerberos authentication with a DB2 repository

By default, IDM uses the username and password configured in the repository connection configuration file (`conf/datasource.jdbc-default.json`) to connect to the DB2 repository. You can configure IDM to use Kerberos authentication instead.

In this scenario, IDM acts as a *client* and requests a Kerberos ticket for a *service*, which is DB2, through the JDBC driver.

This section assumes that you have configured DB2 for Kerberos authentication. If that is not the case, follow the instructions in the corresponding [DB2 documentation](https://www-01.ibm.com/support/knowledgecenter/SSEPGG_10.1.0/com.ibm.db2.luw.admin.sec.doc/doc/c0058525.html) before you read this section.

The following diagram shows how the ticket is obtained and how the keytab is referenced from IDM's `jaas.conf` file.

![db2-kerberos](_images/db2-kerberos.png)Figure 1. Using Kerberos to Connect to a DB2 Repository

> **Collapse: Configure IDM for Kerberos Authentication**
>
> 1. Create a keytab file, specifically for use by IDM.
>
>    A Kerberos keytab file (`krb5.keytab`) is an encrypted copy of the host's key. The keytab enables DB2 to validate the Kerberos ticket that it receives from IDM. You must create a keytab file on the host that IDM runs on. The keytab file must be secured in the same way that you would secure any password file. Specifically, only the user running IDM should have read and write access to this file.
>
>    Create a keytab for DB2 authentication, in the file `openidm/security/idm.keytab/`:
>
>    ```
>    kadmin -p kadmin/admin -w password
>    kadmin: ktadd -k /path/to/openidm/security/idm.keytab db2/idm.example.com
>    ```
>
> 2. Make sure that the DB2 user has read access to the keytab.
>
> 3. Copy the DB2 Java Authentication and Authorization Service (JAAS) configuration file to the IDM `security` directory:
>
>    ```
>    cp /path/to/openidm/db/db2/conf/jaas.conf /path/to/openidm/security/
>    ```
>
>    By default, IDM assumes that the keytab is in the file `openidm/security/idm.keytab` and that the principal identity is `db2/idm.example.com@EXAMPLE.COM`. Change the following lines in the `jaas.conf` file if you are using a different keytab:
>
>    ```
>    keyTab="security/idm.keytab"
>    principal="db2/idm.example.com@EXAMPLE.COM"
>    ```
>
> 4. Adjust the authentication details in your DB2 connection configuration file (`conf/datasource.jdbc-default.json`) to remove the `password` field and change the username to the instance owner (`db2`). The following excerpt shows the modified file:
>
>    ```json
>    {
>        ...
>        "databaseName" : "sopenidm",
>        "username" : "db2",
>        "connectionTimeout" : 30000,
>        ...
>    }
>    ```
>
> 5. Edit your project's `conf/system.properties` file, to add the required Java options for Kerberos authentication.
>
>    In particular, add the following two lines to that file:
>
>    ```none
>    db2.jcc.securityMechanism=11
>    java.security.auth.login.config=security/jaas.conf
>    ```
>
> 6. Restart IDM.

---

---
title: IDM as a Linux service
description: Install PingIDM as a Linux service using Systemd, SysV (Red Hat), or SysV (Ubuntu) init scripts so it starts automatically on boot
component: pingidm
version: 8.1
page_id: pingidm:install-guide:install-linux-service
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/install-linux-service.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Linux Service", "Systemd Service", "SysV Service"]
---

# IDM as a Linux service

IDM provides a script that can generate `SysV` or `Systemd` service initialization scripts. You can start the script as the root user, or configure it to start during the boot process.

When IDM runs as a service, logs are written to the installation directory.

1. If you have not yet installed IDM, follow the steps in [Install IDM](chap-install.html#install-openidm).

2. Review the options by running the following script:

   ```
   /path/to/openidm/bin/create-openidm-rc.sh
   Usage: ./create-openidm-rc.sh --[systemd|chkconfig|lsb]
   Outputs OpenIDM init file to stdout for the given system

   --systemd    Generate Systemd init script. This is preferred for all modern distros.
   --chkconfig  Generate SysV init script with chkconfig headers (RedHat/CentOS)
   --lsb        Generate SysV init script with LSB headers (Debian/Ubuntu)
   ...
   ```

These examples describe how to create each of these scripts:

> **Collapse: Set up a Systemd Service**
>
> If you're running relatively standard versions of Red Hat Enterprise Linux (CentOS Linux) version 7.x, or Ubuntu 16.04 and later, you'll want to set up a systemd service script. To set up such a script, navigate to the `/path/to/openidm/bin` directory, and run the following command:
>
> ```
> /path/to/openidm/bin/create-openidm-rc.sh --systemd
> ```
>
> As noted in the output, you can set up the IDM service on a standard systemd-based Linux distribution with the following commands:
>
> ```
> /path/to/openidm/bin/create-openidm-rc.sh --systemd > openidm.service
> sudo cp openidm.service /etc/systemd/system/
> systemctl enable openidm
> systemctl start openidm
> ```
>
> To stop the IDM service, run the following command:
>
> ```
> systemctl stop openidm
> ```
>
> You can modify the `openidm.service` script. The following excerpt would run IDM with a startup script in the `/home/idm/project` directory:
>
> ```none
> [Unit]
> Description=ForgeRock OpenIDM
> After=network.target auditd.target
>
> [Service]
> Type=simple
> SuccessExitStatus=143
> Environment=JAVA_HOME=/usr
> User=testuser
> ExecStart=/root/openidm/startup.sh -p /home/idm/project
> ExecStop=/root/openidm/shutdown.sh
>
> [Install]
> WantedBy=multi-user.target
> ```
>
> Run the following command to reload the configuration and then start the IDM service script:
>
> ```
> systemctl daemon-reload
> systemctl start openidm
> ```

> **Collapse: Set up a SysV Service (Red Hat)**
>
> If you are running standard versions of Red Hat Enterprise Linux (CentOS Linux) version 6.x, set up a SysV service script with runlevels controlled through the `chkconfig` command. To set up such a script, run the following command:
>
> ```
> /path/to/openidm/bin/create-openidm-rc.sh --chkconfig
> ```
>
> You can then set up and start the IDM service on a Linux distribution that uses SysV init scripts, with the following commands:
>
> ```
> /path/to/openidm/bin/create-openidm-rc.sh --chkconfig  > openidm
> sudo cp openidm /etc/init.d/
> sudo chmod u+x /etc/init.d/openidm
> sudo chkconfig --add openidm
> sudo chkconfig openidm on
> sudo service openidm start
> ```
>
> To stop the IDM service, run the following command:
>
> ```
> sudo service openidm stop
> ```
>
> You can modify the `/etc/init.d/openidm` script. The following excerpt would run IDM with the `startup.sh` script in the `/path/to/openidm` directory:
>
> ```
> START_CMD="PATH=$JAVA_BIN_PATH:$PATH;nohup $OPENIDM_HOME/startup.sh >$OPENIDM_HOME/logs/server.out 2>&1 &"
> ```
>
> You can modify this line to point to some `/path/to/production` directory:
>
> ```
> START_CMD="PATH=$JAVA_BIN_PATH:$PATH;nohup $OPENIDM_HOME/startup.sh -p /path/to/production >$OPENIDM_HOME/logs/server.out 2>&1 &"
> ```
>
> Run the following command to reload the configuration and then start the IDM service script:
>
> ```
> sudo service openidm start
> ```
>
> If you run Linux with SELinux enabled, change the file context of the newly copied script with the following command:
>
> ```
> sudo restorecon /etc/init.d/openidm
> ```
>
> Verify the change to SELinux contexts with the `ls -Z /etc/init.d` command. For consistency, change the user context to match other scripts in the same directory with the `sudo chcon -u system_u /etc/init.d/openidm` command.

> **Collapse: Set up a SysV Service (Ubuntu)**
>
> If you're running an older version of Ubuntu Linux that supports SysV services, set up a SysV service script, with runlevels controlled through the `update-rc.d` command. To set up such a script, run the following command:
>
> ```
> /path/to/openidm/bin/create-openidm-rc.sh --lsb
> ```
>
> You can then set up and start the IDM service on a Linux distribution that uses SysV init scripts, with the following commands:
>
> ```
> /path/to/openidm/bin/create-openidm-rc.sh --lsb  > openidm
> sudo cp openidm /etc/init.d/
> sudo chmod u+x /etc/init.d/openidm
> sudo update-rc.d openidm defaults
> sudo service openidm start
> ```
>
> To stop the IDM service, run the following command:
>
> ```
> sudo service openidm stop
> ```
>
> You can modify the `/etc/init.d/openidm` script. The following excerpt would run IDM with the `startup.sh` script in the `/path/to/openidm` directory:
>
> ```
> START_CMD="PATH=$JAVA_BIN_PATH:$PATH;nohup $OPENIDM_HOME/startup.sh >$OPENIDM_HOME/logs/server.out 2>&1 &"
> ```
>
> You can modify this line to point to some `/path/to/production` directory:
>
> ```
> START_CMD="PATH=$JAVA_BIN_PATH:$PATH;nohup $OPENIDM_HOME/startup.sh -p /path/to/production >$OPENIDM_HOME/logs/server.out 2>&1 &"
> ```
>
> You can then run the following command to reload the configuration and then start the IDM service script:
>
> ```
> sudo service openidm restart
> ```

---

---
title: IDM as a Windows service
description: Install and manage PingIDM as a Windows service using service.bat and prunmgr.exe so it starts automatically with Windows
component: pingidm
version: 8.1
page_id: pingidm:install-guide:install-windows-service
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/install-windows-service.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Windows Service"]
---

# IDM as a Windows service

You can install IDM to run as a Windows service so that it automatically starts and stops with Windows. You must be logged in as an administrator to install a Windows service.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | On a 64-bit Windows server, you must have a 64-bit Java version installed to start the service. If a 32-bit Java version is installed, you will be able to install IDM as a service, but starting the service will fail.*Before* you launch the `service.bat` file, which registers the service within the Windows registry, make sure that your `JAVA_HOME` environment variable points to a valid 64-bit version of the JRE or JDK. If you have already installed the service with the `JAVA_HOME` environment variable pointing to a 32-bit JRE or JDK, delete the service first, then reinstall the service. |

1. Unpack the IDM-8.1.1.zip file, as described previously, and navigate to the `install-directory\bin` directory:

   ```
   C:\> cd openidm\bin
   C:\openidm\bin>
   ```

2. Run the `service.bat` command with the `/install` option, specifying the name that the service should run as:

   ```
   C:\openidm\bin> service.bat /install openidm
   ForgeRock Identity Management Server successfully installed as "openidm" service
   ```

3. Use the Windows Service manager to manage the IDM service.

   ![windows-service](_images/windows-service.png)Figure 1. Running as a Windows Service

4. By default, the IDM service is run by `Local System`, which is a system-level service account built in to Windows. Before you deploy IDM in production, you should switch to an account with fewer permissions. The account running the IDM service must be able to read, write, and execute only the directories related to IDM.

5. Use the Windows Service Manager to start, stop, or restart the service.

6. If you want to uninstall the IDM service, first use the Windows Service Manager to stop IDM and then run the following command:

   ```
   C:\install-directory\openidm\bin> service.bat /uninstall openidm
   Service "openidm" removed successfully
   ```

7. If desired, you can then set up IDM with a specific project directory:

   ```
   C:\install-directory\openidm\bin> service.bat /install openidm -p C:\project-directory
   ForgeRock Identity Management Server successfully installed as "openidm" service
   ```

You can also manage configuration details with the Procrun monitor application. IDM includes the associated `prunmgr.exe` executable in the `C:\install-directory\openidm\bin` directory.

For example, you can open the Windows service configuration application for IDM with the following command, where `ES` stands for *Edit Service Configuration*

```
C:\install-directory\openidm\bin> prunmgr.exe //ES/openidm
```

![windows-config](_images/windows-config.png)

The `prunmgr.exe` executable also includes the monitor application functionality described in the following Apache Commons page on the: [Procrun monitor Application](https://commons.apache.org/proper/commons-daemon/procrun.html). However, IDM does not include the Procrun service application.

For example, if you've configured IDM as a Windows service, you can start and stop it with the following commands:

```
C:\install-directory\openidm\bin> prunmgr.exe //MR/openidm
C:\install-directory\openidm\bin> prunmgr.exe //MQ/openidm
```

In these commands, `MR` is the option to *Monitor and Run* IDM, and `MQ` stands for *Monitor Quit*, which stops the IDM service.

---

---
title: IDM cluster configuration
description: Configure multiple PingIDM instances in a cluster, including shared repository, unique node IDs, cluster.json settings, and keystore sharing
component: pingidm
version: 8.1
page_id: pingidm:install-guide:cluster-config
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/cluster-config.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Cluster", "Configuration"]
---

# IDM cluster configuration

Setting up multiple IDM instances in a cluster involves the following main steps:

1. Ensure that each instance is shut down.

2. Configure each instance to use the same external repository and the same keystore and truststore.

3. Set a unique node ID for each instance.

4. Configure the entire clustered system to use a load balancer or reverse proxy.

To configure an IDM instance as a part of a clustered deployment, follow these steps:

1. Shut down the server if it is running.

2. If you have not already done so, set up a supported repository, as described in [Select a repository](chap-repository.html).

   Each instance in the cluster must be configured to use the same repository; that is, the database connection configuration file (`datasource.jdbc-default.json` ) for each instance must point to the same port number and IP address for the database.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | The configuration file `datasource.jdbc-default.json` must be the same on all nodes. |

   Do not run the data definition language script file in [Select a repository](chap-repository.html) for each instance in the cluster—run it just once to set up the tables required for IDM.

   |   |                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If an instance is *not* participating in the cluster, it must *not* share a repository with nodes that are participating in the cluster. Having non-clustered nodes use the same repository as clustered nodes will result in unexpected behavior. |

3. Specify a unique node ID (`openidm.node.id`) for each instance, in one of the following ways:

   * Set the value of `openidm.node.id` in the `resolver/boot.properties` file of the instance. For example:

     ```json
     openidm.node.id = node1
     ```

   * Set the value in the `OPENIDM_OPTS` environment variable and export that variable before starting the instance. You must include the JVM memory options when you set this variable. For example:

     ```
     export OPENIDM_OPTS="-Xmx2048m -Xms2048m -Dopenidm.node.id=node1" ./startup.sh
     Executing ./startup.sh...
     Using OPENIDM_HOME:   /path/to/openidm
     Using PROJECT_HOME:   /path/to/openidm
     Using OPENIDM_OPTS:   -Xmx2048m -Xms2048m -Dopenidm.node.id=node1
     ...
     Using boot properties at /path/to/openidm/resolver/boot.properties
     -> OpenIDM version "8.1.1"
     OpenIDM ready
     ```

     You can set any value for the `openidm.node.id`, as long as the value is unique within the cluster. The cluster manager detects unavailable instances by their node ID.

     You *must* set a node ID for each instance, otherwise the instance fails to start. The default `resolver/boot.properties` file sets the node ID to `openidm.node.id=node1`.

4. Set the cluster configuration in the `conf/cluster.json` file.

   By default, configuration changes are persisted in the repository so changes that you make in this file apply to all nodes in the cluster.

   The default version of the `cluster.json` file assumes that the cluster management service is enabled:

   ```json
   {
     "instanceId" : "&{openidm.node.id}",
     "instanceTimeout" : 30000,
     "instanceRecoveryTimeout" : 30000,
     "instanceCheckInInterval" : 5000,
     "instanceCheckInOffset" : 0,
     "enabled" : true
   }
   ```

   * instanceId

     The ID of this node in the cluster. By default, this is set to the value of the instance's `openidm.node.id` that you set in the previous step.

   * instanceTimeout

     The length of time (in milliseconds) that a member of the cluster can be "down" before the cluster manager considers that instance to be in *recovery mode*.

     Recovery mode indicates that the `instanceTimeout` of an instance has expired, and that another instance in the cluster has detected that event. The scheduler component of the second instance then moves any incomplete jobs into the queue for the cluster.

   * instanceRecoveryTimeout

     Specifies the time (in milliseconds) that an instance can be in recovery mode before it is considered to be offline.

     This property sets a limit after which other members of the cluster stop trying to access an unavailable instance.

   * instanceCheckInInterval

     Specifies the frequency (in milliseconds) that instances check in with the cluster manager to indicate that they are still online.

   * instanceCheckInOffset

     Specifies an offset (in milliseconds) for the check-in timing, when multiple instances in a cluster are started simultaneously.

     The check-in offset prevents multiple instances from checking in simultaneously, which would strain the cluster manager resource.

   * enabled

     Specifies whether the cluster management service is enabled when you start the server. This property is set to `true` by default.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you disable the cluster manager while clustered nodes are running (by setting `"enabled" : false` in an instance's `cluster.json` file), the following happens:- The cluster manager thread that causes instances to *check in* is not deactivated.

     - Nodes in the cluster no longer receive cluster *events*, which are used to broadcast configuration changes when they occur over the REST interface.

     - Nodes are unable to detect and attempt to recover failed instances within the cluster.

     - Persisted schedules associated with failed instances cannot be recovered by other nodes. |

5. Specify how the instance reads configuration changes. Learn more in [Configuration updates in a cluster](cluster-config-changes.html).

6. If you're using scheduled tasks, configure [persistent schedules](../schedules-guide/persistent-schedules.html) so that jobs and tasks are launched only once across the cluster.

7. Configure each node in the cluster to work with host headers. If you're using a load balancer, adjust the default `conf/webserver.listener-*json` configuration, as described in [Deploy Securely Behind a Load Balancer](../security-guide/chap-connections.html#clustering-load-balancer)

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In IDM 8.0, `jetty.xml` is no longer supported.When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment.Learn more in [Jetty 12 support](../release-notes/whats-new.html#jetty_12_support). |

8. Make sure that each node in the cluster has the same keystore and truststore. You can do this in one of the following ways:

   * When the first instance has been started, copy the initialized keystore (`/path/to/openidm/security/keystore.jceks` ) and truststore (`/path/to/openidm/security/truststore` ) to all other instances in the cluster.

   * Use a single keystore that is shared between all the nodes. The shared keystore might be on a mounted filesystem, a [Hardware Security Module (HSM)](../security-guide/secret-stores-hardware.html) or something similar. If you use this method, set the following properties in the `resolver/boot.properties` file of each instance to point to the shared keystore:

     ```none
     openidm.keystore.location=path/to/keystore
     openidm.truststore.location=path/to/truststore
     ```

   * The configuration file `secrets.json` in the `/path/to/openidm/conf` directory must be the same on all the nodes.

9. Start each instance in the cluster.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The [audit service](../audit-guide/audit.html) logs configuration changes only on the modified instance. Although configuration changes are persisted in the repository, and replicated on other instances by default, those changes are not logged separately for each instance.Configuration changes are persisted by default, but changes to workflows and scripts, and extensions to the UI are not. Any changes that you make in these areas must be manually copied to each node in the cluster. |

---

---
title: IDM in a cluster
description: Overview of deploying PingIDM in a cluster for high availability, covering active-active and active-standby modes, MVCC, and clock synchronization
component: pingidm
version: 8.1
page_id: pingidm:install-guide:chap-cluster
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/chap-cluster.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Cluster"]
section_ids:
  cluster-standby-overview: Active-standby mode
  considerations: Considerations
  clock_synchronization: Clock synchronization
---

# IDM in a cluster

To ensure that your identity management service remains available in the event of system failure, you can deploy multiple IDM instances in a cluster. In a clustered environment, each instance points to the same external repository.

If one instance in a cluster shuts down or fails to check in with the cluster management service, a second instance will detect the failure. For example, if an instance named `instance1` loses connectivity while executing a scheduled task, the cluster manager notifies the scheduler service that `instance1` is not available. The scheduler service then attempts to clean up any jobs that `instance1` was running at that time. Note that clustered instances claim scheduled tasks in a random order. For more information, refer to [Scheduled tasks across a cluster](clustering-scheduled-tasks.html).

Consistency and concurrency across cluster instances is ensured using multi-version concurrency control (MVCC). MVCC provides consistency because each instance updates only the particular revision of the object that was specified in the update.

All instances in a cluster run simultaneously. When a clustered deployment is configured with a load balancer, the deployment works as an active-active high availability cluster. If the database is also clustered, IDM points to the database cluster as a single system.

IDM requires a single, consistent view of all the data it manages, including the user store, roles, schedules, and configuration. If you can guarantee this consistent view, the number and locations of IDM nodes in a cluster will be limited only by your network latency and other network factors that affect performance.

The following diagram shows an IDM deployment where both the IDM instances and the databases are clustered, and accessed through a load balancer:

![You can set up a cluster with two or more IDM instances](_images/cluster-config.svg)

## Active-standby mode

In addition to an active-active deployment, you can segment IDM instances into *active* and *standby* groups. Active instances process schedules, clustered reconciliation, and queued sync. Standby instances don't process these operations, functioning as hot spares that you can activate on demand using the `openidm/cluster/active` endpoint.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Standby mode controls whether a node processes schedules, clustered reconciliation, and queued sync. Standby nodes still respond to direct API requests. Configuring load balancing, database replication, and failover orchestration for an active-standby deployment is the responsibility of the deployer. |

Learn more in [Cluster standby mode](cluster-standby.html).

## Considerations

The cluster subtopics don't include instructions on configuring the various third-party load balancing options.

### Clock synchronization

A clustered deployment relies on system heartbeats to assess the cluster state. For the heartbeat mechanism to work, you *must* synchronize the system clocks of all machines in the cluster using a time synchronization service that runs regularly.

The system clocks must be within one second of each other. For information on how you can achieve this using the Network Time Protocol (NTP) daemon, refer to the [NTP RFC](https://www.rfc-editor.org/rfc/rfc5905.html).

Virtual machine clocks can drift from the hypervisor host clock due to CPU scheduling, VM migration, or suspend and resume operations. To keep cluster heartbeats accurate, run a time synchronization service such as NTP independently on each VM, even if the hypervisor host is already synchronized.

---

---
title: Install and run IDM
description: Install, start, stop, uninstall, and debug PingIDM, including running as a background process or in JPDA debug mode
component: pingidm
version: 8.1
page_id: pingidm:install-guide:chap-install
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/chap-install.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Startup", "Shutdown", "Uninstall", "Debug"]
section_ids:
  install-openidm: Install IDM
  run-openidm: Start IDM
  run_idm_as_a_background_process: Run IDM as a background process
  stop-openidm: Stop IDM
  chap-uninstall: Uninstall IDM
  starting-in-debug-mode: Start IDM in debug mode
  change-jvm-heap: Change the JVM heap size
---

# Install and run IDM

Use the procedures in this section to install, start, run, and stop IDM.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | Before you can use IDM, you must [select and configure a repository](chap-repository.html). |

## Install IDM

Follow these steps to install IDM:

1. Make sure you have an appropriate version of Java installed:

   ```console
   java -version
   openjdk version "21.0.9" 2025-10-21 LTS
   OpenJDK Runtime Environment Temurin-21.0.9+10 (build 21.0.9+10-LTS)
   OpenJDK 64-Bit Server VM Temurin-21.0.9+10 (build 21.0.9+10-LTS, mixed mode, sharing)
   ```

   For a description of the Java requirements, refer to [Before you install](../release-notes/before-you-install.html).

2. []()Download IDM from [Backstage](https://backstage.forgerock.com/downloads/).

3. Unpack the contents of the .zip file into the install directory:

   ```
   unzip ~/Downloads/IDM-8.1.1.zip
   Archive:  IDM-8.1.1.zip
     inflating: openidm/.checksums.csv
      creating: openidm/bundle/
    extracting: openidm/bundle/openidm-audit-8.1.1.jar
   ...
   ```

4. By default, IDM listens for HTTP and HTTPS connections on ports 8080 and 8443, respectively. To change these port numbers, edit the following settings in your `resolver/boot.properties` file:

   * `openidm.port.http`

   * `openidm.port.https`

   When you deploy IDM in production, you *must* set `openidm.host` to the URL of your deployment in the `resolver/boot.properties` file. Otherwise, calls to the `/admin` endpoint are not properly redirected.

   Deployment URLs will vary, depending on whether you're using a load balancer. While IDM documentation does not specify how you'd configure a load balancer, you'll need to configure IDM in a cluster as described in [IDM cluster configuration](cluster-config.html), and specifically in [Deploy Securely Behind a Load Balancer](../security-guide/chap-connections.html#clustering-load-balancer).

## Start IDM

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | To adjust the JVM heap size before starting IDM, refer to [Change the JVM heap size](#change-jvm-heap). |

Follow these steps to run IDM interactively:

1. Start the Felix container, load all services, and start a command shell to allow you to manage the container:

   * Bash

   * PowerShell

   ```
   /path/to/openidm/startup.sh
   Using OPENIDM_HOME:   /path/to/openidm
   Using PROJECT_HOME:   /path/to/openidm
   Using OPENIDM_OPTS:   -Xmx2048m -Xms2048m
   \...
   -> OpenIDM version "8.1.1"
   OpenIDM ready
   ```

   ```
   \path\to\openidm\startup.bat
   "Using OPENIDM_HOME:   \path\to\openidm"
   "Using PROJECT_HOME:   \path\to\openidm"
   "Using OPENIDM_OPTS:   -Xmx2048m -Xms2048m -Dfile.encoding=UTF-8"
   \...
   -> OpenIDM version "8.1.1"
   OpenIDM ready
   ```

2. At the OSGi console `->` prompt, you can enter commands, such as `help` for usage or `ps` to view the bundles installed.

   Startup errors and messages are logged to the console by default. You can also view these messages in the log files at `/path/to/openidm/logs`.

## Run IDM as a background process

You can also start IDM as a background process on UNIX and Linux systems. Follow these steps, preferably before you start IDM for the first time:

1. If you have already started the server, shut it down and remove the Felix cache files under `openidm/felix-cache/` :

   ```
   shutdown
   ...
   rm -rf felix-cache/*
   ```

2. Start the server in the background. The `nohup` survives a logout, and the `2>&1&` redirects standard output and standard error to the noted `console.out` file:

   ```
   nohup ./startup.sh > logs/console.out 2>&1&
   [1] 2343
   ```

To stop the server running as a background process, use the `shutdown.sh` script:

```
./shutdown.sh
Stopping OpenIDM (2343)
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although installations on macOS systems are not supported in production, you might want to run IDM on macOS in a demo or test environment. To run IDM in the background on a macOS system, take the following additional steps:- Remove the `org.apache.felix.shell.tui-*.jar` bundle from the `openidm/bundle` directory.

- Disable [ConsoleHandler logging](../monitoring-guide/server-logs.html#log-disabling). |

## Stop IDM

You can stop IDM from the `->` prompt in the OSGi console.

1. In the OSGi console, enter the `shutdown` command at the `->` prompt.

2. On Unix systems, you can stop IDM by using the `shutdown.sh` script:

   ```
   /path/to/openidm/shutdown.sh
   Stopping OpenIDM (31391)
   ```

## Uninstall IDM

1. Stop the server if it is running, as described in [Stop IDM](#stop-openidm).

2. Remove the directory where you installed the software:

   ```
   rm -rf /path/to/openidm
   ```

3. If you use a JDBC database for the repository, drop the `openidm` database.

## Start IDM in debug mode

To debug custom libraries, start the server with the Java Platform Debugger Architecture (JPDA):

1. Start IDM with the `jpda` option:

   ```
   /path/to/openidm/startup.sh jpda
   Executing ./startup.sh...
   Using OPENIDM_HOME:   /path/to/openidm
   Using OPENIDM_OPTS:   -Xmx2048m -Xms2048m -Djava.compiler=NONE -Xnoagent -Xdebug -Xrunjdwp:transport=dt_socket,address=5005,server=y,suspend=n
   ...
   Listening for transport dt_socket at address: 5005
   Using boot properties at /path/to/openidm/resolver/boot.properties
   -> OpenIDM version "8.1.1" (revision: xxxx)
   OpenIDM ready
   ```

   The relevant JPDA options are listed in the startup script (`startup.sh`).

2. In your IDE, attach a Java debugger to the JVM via socket on port 5005.

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | This interface is internal and subject to change. If you depend on this interface, contact Ping support. |

## Change the JVM heap size

Changing the JVM heap size can improve performance and reduce the time it takes to run reconciliations.

You can set the JVM heap size via the `OPENIDM_OPTS` environment variable. If `OPENIDM_OPTS` is undefined, the JVM maximum heap size defaults to 2GB. For example, to set the minimum and maximum heap sizes to 4GB, enter the following before starting IDM:

* Unix/Linux

* Windows

```
cd /path/to/openidm/
export OPENIDM_OPTS="-Xms4096m -Xmx4096m"
./startup.sh
Using OPENIDM_HOME:   /path/to/openidm
Using PROJECT_HOME:   /path/to/openidm
Using OPENIDM_OPTS:   -Xms4096m -Xmx4096m
...
OpenIDM ready
```

```
cd \path\to\openidm
set OPENIDM_OPTS=-Xms4096m -Xmx4096m
startup.bat
"Using OPENIDM_HOME:   \path\to\openidm"
"Using PROJECT_HOME:   \path\to\openidm"
"Using OPENIDM_OPTS:   -Xms4096m -Xmx4096m -Dfile.encoding=UTF-8"
...
OpenIDM ready
```

You can also edit the `OPENIDM_OPTS` values in `startup.sh` or `startup.bat`.

|   |                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------ |
|   | For more information about tuning and load testing, refer to [Load testing](../monitoring-guide/load-testing.html) |

---

---
title: Installation
description: Guide to installing and uninstalling PingIDM software that offers flexible services for automating management of the identity life cycle
component: pingidm
version: 8.1
page_id: pingidm:install-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation"]
page_aliases: ["index.adoc"]
---

# Installation

> Guide to installing, and uninstalling PingIDM software. This software offers flexible services for automating management of the identity life cycle.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

This guide shows you how to install PingIDM services for identity management, provisioning, and compliance. You do not need a complete understanding of PingIDM software to learn something from this guide, although a background in identity management and maintaining web application software can help. You do need some background in managing services on your operating systems and in your web application containers. Unless you are planning an evaluation or test installation, read the [Release notes](../release-notes/preface.html) before you get started.

Quick Start

[icon: download, set=fad, size=3x]

#### [Install IDM](chap-install.html)

Download the IDM software and get a minimal deployment up and running.

[icon: desktop, set=fad, size=3x]

#### [Interact with IDM](interact-with-idm.html)

Introduction to the IDM REST API and browser-based user interface.

[icon: database, set=fad, size=3x]

#### [Repository](chap-repository.html)

Configure IDM to use your selected production repository.

[icon: cogs, set=fad, size=3x]

#### [Startup Configuration](startup-configuration.html)

Learn about the startup configuration and how to verify system health.

[icon: sitemap, set=fad, size=3x]

#### [Install in a Cluster](chap-cluster.html)

IDM in a cluster for availability.

[icon: server, set=fad, size=3x]

#### [Jetty Configuration](appendix-jetty.html)

Configure the embedded Jetty server.

---

---
title: Installed modules and features
description: "(Deprecated) Query PingIDM's info/features endpoint over REST to list active bundles, enabled features, and their REST endpoints"
component: pingidm
version: 8.1
page_id: pingidm:install-guide:installed-modules-and-features
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/installed-modules-and-features.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Modules", "Features"]
---

# Installed modules and features

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `info/features` endpoint is [deprecated](../release-notes/deprecated-functionality.html#deprecation-info-features-endpoint) and will be removed in a future release of IDM. |

You can query the enabled features over REST at the `info/features` endpoint. The feature availability service determines the set of possible features from the active bundles and provides the following information:

* The name and `_id` of the feature

* Whether the feature is enabled

* If the feature is enabled, the REST endpoint on which that feature can be accessed

Example

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/info/features?_queryFilter=true"
{
  "result": [
    {
      "_id": "retrieveUsername",
      "name": "retrieveUsername",
      "enabled": false,
      "endpoints": []
    },
    {
      "_id": "endpoint",
      "name": "endpoint",
      "enabled": true,
      "endpoints": [
        "endpoint/oauthproxy",
        "endpoint/updateInternalUserAndInternalRoleEntries/*",
        "endpoint/getavailableuserstoassign/*",
        "endpoint/gettasksview/*",
        "endpoint/repairMetadata/*",
        "util/validateQueryFilter",
        "endpoint/mappingDetails",
        "endpoint/getprocessesforuser/*",
        "endpoint/removeRepoPathFromRelationships/*"
      ]
    },
    {
      "_id": "workflow",
      "name": "workflow",
      "enabled": false,
      "endpoints": []
    },
    ...
  ],
  ...
}
```

---

---
title: Interact with IDM
description: Introduction to PingIDM REST API access and browser-based user interfaces, including the admin UI and end-user UI options
component: pingidm
version: 8.1
page_id: pingidm:install-guide:interact-with-idm
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/interact-with-idm.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "REST", "User Interfaces"]
section_ids:
  first-steps-with-rest: REST interface introduction
  rest-output-format: Format REST output for readability
  openidm-uis: IDM user interfaces
---

# Interact with IDM

There are two primary ways to interact with IDM; programmatically, using REST to access IDM's API endpoints, or using the browser-based user interfaces.

## REST interface introduction

IDM provides RESTful access to users in its repository, and to its configuration. To access the repository over REST, you can use a browser-based REST client, such as the *Simple REST Client* for Chrome, or *RESTClient* for Firefox. You can also use applications such as *Postman* to create, run, and manage collections of REST calls. Alternatively you can use the `curl` command-line utility, included with most operating systems. For more information about `curl`, refer to <https://github.com/curl/curl>.

IDM is accessible over the regular and secure HTTP ports of the Jetty Servlet container, 8080, and 8443. Most of the command-line examples in this documentation set use the regular HTTP port, so that you don't have to use certificates just to test IDM. In a production deployment, install a CA-signed certificate and restrict REST access to a secure (HTTPS) port.

To run `curl` over the secure port, 8443, you must either include the `--insecure` option, or follow the instructions in [Restrict REST Access to the HTTPS Port](../security-guide/chap-connections.html#security-https). You can use those instructions with the self-signed certificate that is generated when IDM starts, or with a `*.crt` file provided by a certificate authority.

|   |                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some of the examples in this documentation set use client-assigned IDs (such as `bjensen` and `scarter`) when creating objects because it makes the examples easier to read. If you create objects using the admin UI, they are created with server-assigned IDs (such as `55ef0a75-f261-47e9-a72b-f5c61c32d339`). Generally, immutable server-assigned UUIDs are used in production environments. |

> **Collapse: Try Out IDM Using REST**
>
> 1. Use the following REST query to list all users in the IDM repository:
>
>    ```
>    curl \
>    --header "X-OpenIDM-Username: openidm-admin" \
>    --header "X-OpenIDM-Password: openidm-admin" \
>    --header "Accept-API-Version: resource=1.0" \
>    --request GET \
>    "http://localhost:8080/openidm/managed/user/?_queryFilter=true&_fields=_id"
>    ```
>
>    When you first install IDM with an empty repository, no users exist.
>
> 2. Create a user `joe` by sending a RESTful POST.
>
>    The following `curl` command creates a managed user in the repository, and set the user's ID to `jdoe`:
>
>    * Bash
>
>    * PowerShell
>
>    ```
>    curl \
>    --header "Content-Type: application/json" \
>    --header "X-OpenIDM-Username: openidm-admin" \
>    --header "X-OpenIDM-Password: openidm-admin" \
>    --header "Accept-API-Version: resource=1.0" \
>    --request POST \
>    --data '{
>      "userName": "joe",
>      "givenName": "joe",
>      "sn": "smith",
>      "mail": "joe@example.com",
>      "telephoneNumber": "555-123-1234",
>      "password": "TestPassw0rd",
>      "description": "My first user",
>      "_id": "joe"
>    }' \
>    http://localhost:8080/openidm/managed/user?_action=create
>    {
>      "_id": "joe",
>      "_rev": "00000000c03fd7aa",
>      "userName": "joe",
>      "givenName": "joe",
>      "sn": "smith",
>      "mail": "joe@example.com",
>      "telephoneNumber": "555-123-1234",
>      "description": "My first user",
>      "accountStatus": "active",
>      "effectiveRoles": [],
>      "effectiveAssignments": []
>    }
>    ```
>
>    ```
>    curl `
>    --header "Content-Type: application/json" `
>    --header "X-OpenIDM-Username: openidm-admin" `
>    --header "X-OpenIDM-Password: openidm-admin" `
>    --header "Accept-API-Version: resource=1.0" `
>    --request POST `
>    --data '{
>      "userName": "joe",
>      "givenName": "joe",
>      "sn": "smith",
>      "mail": "joe@example.com",
>      "telephoneNumber": "555-123-1234",
>      "password": "TestPassw0rd",
>      "description": "My first user",
>      "_id": "joe"
>    }' `
>    http://localhost:8080/openidm/managed/user?_action=create
>    {
>      "_id": "joe",
>      "_rev": "00000000c03fd7aa",
>      "userName": "joe",
>      "givenName": "joe",
>      "sn": "smith",
>      "mail": "joe@example.com",
>      "telephoneNumber": "555-123-1234",
>      "description": "My first user",
>      "accountStatus": "active",
>      "effectiveRoles": [],
>      "effectiveAssignments": []
>    }
>    ```
>
> 3. Fetch the newly created user from the repository with a RESTful GET:
>
>    * Bash
>
>    * PowerShell
>
>    ```
>    curl \
>    --header "X-OpenIDM-Username: openidm-admin" \
>    --header "X-OpenIDM-Password: openidm-admin" \
>    --header "Accept-API-Version: resource=1.0" \
>    --request GET \
>    http://localhost:8080/openidm/managed/user/joe
>    {
>      "_id": "joe",
>      "_rev": "00000000c03fd7aa",
>      "userName": "joe",
>      "givenName": "joe",
>      "sn": "smith",
>      "mail": "joe@example.com",
>      "telephoneNumber": "555-123-1234",
>      "description": "My first user",
>      "accountStatus": "active",
>      "effectiveRoles": [],
>      "effectiveAssignments": []
>    }
>    ```
>
>    ```
>    curl `
>    --header "X-OpenIDM-Username: openidm-admin" `
>    --header "X-OpenIDM-Password: openidm-admin" `
>    --header "Accept-API-Version: resource=1.0" `
>    --request GET `
>    http://localhost:8080/openidm/managed/user/joe
>    {
>      "_id": "joe",
>      "_rev": "00000000c03fd7aa",
>      "userName": "joe",
>      "givenName": "joe",
>      "sn": "smith",
>      "mail": "joe@example.com",
>      "telephoneNumber": "555-123-1234",
>      "description": "My first user",
>      "accountStatus": "active",
>      "effectiveRoles": [],
>      "effectiveAssignments": []
>    }
>    ```

### Format REST output for readability

By default, `curl`-based REST calls return the JSON object on one line, which can be difficult to read. For example:

```
{"mail":"joe@example.com","sn":"smith","passwordAttempts":"0",
"lastPasswordAttempt":"Mon Apr 14 2014 11:13:37 GMT-0800 (GMT-08:00)",
"givenName":"joe","effectiveRoles":["internal/role/openidm-authorized"],
"password":{"$crypto":{"type":"x-simple-encryption","value":{"data":
"OBFVL9cG8uaLoo1N+SMJ3g==","cipher":"AES/CBC/PKCS5Padding","iv":
"7rlV4EwkwdRHkt19F8g22A==","key":"openidm-sym-default"}}},"country":"",
"city":"","_rev": "00000000c03fd7aa","lastPasswordSet":"","postalCode":"",
"_id":"joe3","description":"My first user","accountStatus":"active","telephoneNumber":
"555-123-1234","roles":["internal/role/openidm-authorized"],"effectiveAssignments":{},
"postalAddress":"","stateProvince":"","userName":"joe3"}
```

At least two options are available to clean up this output:

> **Collapse: Format Output Using a JSON Parser**
>
> The standard way to format JSON output is with a JSON parser such as [jq](http://stedolan.github.io/jq/). `jq` is not installed by default on most operating systems, but you can install it and then "pipe" the output of a REST call to `jq`, as follows:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/managed/user/joe" \
> | jq .
> ```

> **Collapse: Format Output Using the REST API**
>
> The Ping REST API includes an optional `_prettyPrint` request parameter. The default value is `false`. To use the REST API to format output, add a parameter such as `?_prettyPrint=true` or `&_prettyPrint=true`, depending on whether it is added to the end of an existing request parameter. In this case, the following command would return formatted output:
>
> ```
> curl \
> --header "X-OpenIDM-Username: openidm-admin" \
> --header "X-OpenIDM-Password: openidm-admin" \
> --header "Accept-API-Version: resource=1.0" \
> --request GET \
> "http://localhost:8080/openidm/managed/user/joe?_prettyPrint=true"
> ```
>
> |   |                                                                                                                   |
> | - | ----------------------------------------------------------------------------------------------------------------- |
> |   | Most command-line examples in this guide do not show this parameter, but the output is formatted for readability. |

## IDM user interfaces

IDM has two types of user interfaces, an administrative UI for managing the IDM deployment and an end-user UI for letting end users manage certain aspects of their own accounts. These UIs aren't bundled with IDM. You can download and install each separately from the [Backstage download site](https://backstage.forgerock.com/downloads).

* Administrative UI

  You have two options for the administrative UI:

  * The [Platform admin UI](../setup-guide/platform-admin-ui.html) is the replacement for the legacy admin UI and is the recommended option for new deployments. Deploy it behind a standalone Nginx server or as a Docker container.

  * The [legacy admin UI](../setup-guide/legacy-admin-ui.html) is deprecated, but remains available for customers who still depend on it.

* End-user UI

  The [IDM end-user UI](../setup-guide/idm-enduser-ui.html) provides role-based access to specific tasks and allows users to manage certain aspects of their own accounts.

Learn more in [User interfaces](../setup-guide/chap-ui.html).

---

---
title: Java requirements
description: Verify Java requirements for PingIDM, including supported versions, and set the JAVA_HOME environment variable on Windows and Linux
component: pingidm
version: 8.1
page_id: pingidm:install-guide:verify-java
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/verify-java.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Java"]
---

# Java requirements

Before you start, follow these steps to ensure that your Java environment is suitable:

1. Verify that your computer has a supported Java version installed:

   **Supported Java Versions**

   | Vendor                                                                                                                                                                                                                                 | Versions |
   | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
   | OpenJDK, including OpenJDK-based distributions:- AdoptOpenJDK/Eclipse Temurin

   - Amazon Corretto

   - Azul Zulu

   - Red Hat OpenJDK	Ping tests most extensively with AdoptOpenJDK/Eclipse Temurin. Ping recommends using the HotSpot JVM. | 21       |
   | Oracle Java                                                                                                                                                                                                                            | 21       |

2. Read the [pre-installation requirements](../release-notes/before-you-install.html).

3. Set the `JAVA_HOME` environment variable:

   > **Collapse: Set JAVA\_HOME on Windows**
   >
   > 1. Locate the JRE installation directory (typically, `C:\Program Files\Java\`).
   >
   > 2. Click Start > Control Panel > System and Security > System.
   >
   > 3. Click Advanced System Settings.
   >
   > 4. Click Environment Variables.
   >
   > 5. Under System Variables, click New.
   >
   > 6. Enter the Variable name (`JAVA_HOME`) and set the Variable value to the JRE installation directory; for example `C:\Program Files\Java\jre8`.
   >
   > 7. Click OK.

   > **Collapse: Set JAVA\_HOME on Linux**
   >
   > 1. Open the user shell configuration file found in your home directory.
   >
   > 2. Add the `JAVA_HOME` variable to the user shell configuration file, setting the value to `/usr`. In Bash, this would appear as `export JAVA_HOME="/usr"`.

---

---
title: JDBC database access rights
description: Minimum JDBC database access rights required for PingIDM daily operation, including permissions needed for the openidm service account
component: pingidm
version: 8.1
page_id: pingidm:install-guide:repository-minimum-rights
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/repository-minimum-rights.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "JDBC"]
---

# JDBC database access rights

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | The following topic only applies if you have set up a JDBC repository, as described in [Select a repository](chap-repository.html). |

In general, IDM requires minimal access rights to the JDBC repository for daily operation. This section lists the minimum permissions required, and suggests a strategy for restricting database access in your deployment.

The JDBC repository used by IDM requires only one *relevant* user — the service account that is used to create the tables. Generally, the details of this account are configured in the repository connection file (`datasource.jdbc-default.json`). By default, the username and password for this account are `openidm` and `openidm`, regardless of the database type.

All other users are created by the `db/database-type/scripts/openidm.sql` script. The `openidm` user account must have SELECT, UPDATE, INSERT, and DELETE permissions on all the `openidm` tables that are created by this script, by the scripts that create the tables specific to the Flowable workflow engine, and by the script that sets up the audit tables if you are using the repository audit event handler.

---

---
title: JDBC over SSL
description: Configure PingIDM to connect to a JDBC repository over SSL, including certificate setup, keystore import, and jdbcUrl configuration for MySQL
component: pingidm
version: 8.1
page_id: pingidm:install-guide:jdbc-repos-ssl
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/jdbc-repos-ssl.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "JDBC", "SSL"]
---

# JDBC over SSL

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | The following topic only applies if you have set up a JDBC repository, as described in [Select a repository](chap-repository.html) |

This procedure assumes that you have already set up your JDBC repository, as described in the previous sections. The exact steps to connect to a JDBC repository over SSL depend on your repository. This procedure describes the steps for a MySQL 8 repository. If you are using a different JDBC repository, use the corresponding documentation for that repository, and adjust the steps accordingly.

1. Change the `jdbcUrl` property in your repository connection configuration file (`conf/datasource.jdbc-default.json`).

   The exact value of the `jdbcUrl` property will depend on your JDBC database, and on the version of your JDBC driver:

   > **Collapse: Configuration for MySQL with JDBC Driver Version 8.0.12 or Earlier**
   >
   > ```none
   > "jdbcUrl" : "jdbc:mysql://&{openidm.repo.host}:&{openidm.repo.port}/openidm?allowMultiQueries=true&characterEncoding=utf8&useSSL=true&verifyServerCertificate=true&requireSSL=true"
   > ```

   > **Collapse: Configuration for MySQL with JDBC Driver Version 8.0.13 or Later**
   >
   > ```none
   > "jdbcUrl" : "jdbc:mysql://&{openidm.repo.host}:&{openidm.repo.port}/openidm?allowMultiQueries=true&characterEncoding=utf8&sslMode=VERIFY_CA&requireSSL=true"
   > ```

   |   |                                                               |
   | - | ------------------------------------------------------------- |
   |   | For Azure MySQL, JDBC Driver Version 8.0.17+ is **required**. |

2. Create and verify the SSL certificate and key files required to support encrypted connections to the JDBC repository.

   For MySQL 8, use one of the procedures in the [MySQL docs](https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-rsa-files.html).

3. Configure the JDBC repository to use encrypted connections.

   For MySQL 8, follow the [MySQL docs](https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html).

4. Check that the connection to the database is over SSL by running a command similar to the following:

   ```
   mysql -u root -P 3306 -p
   mysql> show variables like "%have_ssl%";
   +---------------+-------+
   | Variable_name | Value |
   +---------------+-------+
   | have_ssl      | YES   |
   +---------------+-------+
   1 row in set (0.00 sec)
   ```

5. Convert your MySQL client key and certificate files to a PKCS #12 archive. For example:

   ```
   openssl pkcs12 -export \
   -in client-cert.pem \
   -inkey client-key.pem \
   -name "mysqlclient" \
   -passout pass:changeit \
   -out client-keystore.p12
   ```

6. Import the `client-keystore.p12` into the IDM keystore:

   ```
   keytool \
   -importkeystore \
   -srckeystore client-keystore.p12 \
   -srcstoretype pkcs12 \
   -srcstorepass changeit \
   -destkeystore /path/to/openidm/security/keystore.jceks \
   -deststoretype jceks \
   -deststorepass changeit
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | For AWS RDS MySQL **and** Azure MySQL, no client certificates are provided. In this case, you must create an empty keystore for client certificates, and add the following to the `jdbcUrl` property in your repository connection configuration file (`conf/datasource.jdbc-default.json `):```none
   &clientCertificateKeyStoreUrl=file:/opt/idm/security/empty.jks&clientCertificateKeyStorePassword=changeit
   ``` |

7. Import your MySQL CA certificate into the IDM truststore.

   ```
   keytool \
   -importcert \
   -trustcacerts \
   -file ca-cert.pem \
   -alias "DB cert" \
   -keystore /path/to/openidm/security/truststore
   ```

   You are prompted for a keystore password. You must use the same password as is shown in your `resolver/boot.properties` file. The default truststore password is:

   ```
   openidm.truststore.password=changeit
   ```

   After entering a keystore password, you are prompted with the following question. Assuming you have included an appropriate `ca-cert.pem` file, enter `yes`.

   ```
   Trust this certificate? [no]:
   ```

8. Open your project's `conf/system.properties` file. Add the following line to that file. If appropriate, substitute the path to your own truststore:

   ```
   # Set the truststore
   javax.net.ssl.trustStore=&{idm.install.dir}/security/truststore
   ```

   Even if you are setting up this instance of IDM as part of a [cluster](chap-cluster.html), you must configure this initial truststore. After this instance joins a cluster, the SSL keys in this particular truststore are replaced.

---

---
title: Jetty configuration properties
description: Reference for PingIDM Jetty web server configuration properties in webserver.json and webserver.listener-*.json, including TLS, threads, and QoSHandler
component: pingidm
version: 8.1
page_id: pingidm:install-guide:idm-config-properties-jetty
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/idm-config-properties-jetty.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  jetty-property-reference: Jetty property reference
  config-jetty-thread-settings-gzip-compression: Jetty thread settings and Gzip compression
  config-jetty-qos-handler: Jetty QoSHandler
---

# Jetty configuration properties

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In IDM 8.0, `jetty.xml` is no longer supported.When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment.Learn more in [Jetty 12 support](../release-notes/whats-new.html#jetty_12_support). |

The configuration for PingIDM's embedded Jetty web server includes a `webserver.json` and a `webserver.listener-*.json`.

By default, the Jetty web server uses the HTTP, SSL, and Mutual Authentication ports defined in IDM.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | The default settings are intended for evaluation only. Adjust them according to your production requirements. |

## Jetty property reference

**webserver.json reference**

| Field                       | Description                                                                                                                                                                                 | Default value                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `maxThreads`                | The maximum number of threads used to handle requests.                                                                                                                                      | `200`                                                                                 |
| `maxQueueSize`              | []()The maximum number of requests allowed in the [QoSHandler](#config-jetty-qos-handler) queue. This setting controls [readiness probe](system-healthcheck.html#readiness-probe) behavior. | `-1`  The default value allows for an unbounded queue.                                |
| []()`maxRequestSuspendTime` | The number of milliseconds a request can remain in the QosHandler queue.                                                                                                                    | `0`  The default value allows requests to remain in the unbounded queue indefinitely. |
| `gzip`                      | Contains the settings for the global Gzip compression handler.                                                                                                                              |                                                                                       |
| `gzip/enabled`              | Toggles the Gzip compression handler on or off.                                                                                                                                             | `false`                                                                               |
| `gzip/minGzipSize`          | The minimum response size in bytes required to enable compression of the response.                                                                                                          | `2048`                                                                                |
| `gzip/inflateBufferSize`    | The size in bytes of the buffer used to inflate compressed requests.                                                                                                                        | `0`                                                                                   |
| `gzip/syncFlush`            | Toggles the usage of the [SYNC\_FLUSH mode](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/zip/Deflater.html#SYNC_FLUSH) when compressing responses.                | `false`                                                                               |
| `gzip/includedMethods`      | The allow list of HTTP methods that compression will be applied to.                                                                                                                         |                                                                                       |
| `gzip/excludedMethods`      | The block list of HTTP methods that compression will not be applied to.                                                                                                                     |                                                                                       |

**webserver.listener-\*.json properties**

| Field                         | Description                                                                                                                                                                                                                                                                                                                                                                                     | Default value                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                     | Toggles the listener on or off.                                                                                                                                                                                                                                                                                                                                                                 | `false`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `port`                        | The port to listen to.                                                                                                                                                                                                                                                                                                                                                                          | `8080`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `secure`                      | Toggles the use of TLS on or off.                                                                                                                                                                                                                                                                                                                                                               | `false`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `mutualAuth`                  | Toggles the use of `mTLS` on or off. Does nothing if secure is false.                                                                                                                                                                                                                                                                                                                           | `false`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `wantClientAuth`              | Toggles the `wantClientAuth` setting on or off.When `true`, the server requests a client certificate but doesn't require it for the TLS handshake to succeed. If a client provides a certificate, it must be valid.This enables support for mixed traffic, allowing clients with or without certificates to connect on the same port.For proper function, you must set `mutualAuth` to `false`. | `false`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sslCertAlias`                | The key alias IDM uses when choosing the certificate to present for HTTPS connections.                                                                                                                                                                                                                                                                                                          | `openidm-localhost`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `includedProtocols`           | The allow-list of acceptable TLS protocols.                                                                                                                                                                                                                                                                                                                                                     | `TLSv1.3`,`TLSv1.2`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `excludedProtocols`           | The block-list of non-acceptable TLS protocols.                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `includedCiphers`             | The allow-list of acceptable TLS ciphers.                                                                                                                                                                                                                                                                                                                                                       | ```json
"TLS_AES_128_GCM_SHA256",
"TLS_AES_256_GCM_SHA384",
"TLS_CHACHA20_POLY1305_SHA256",
"TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
"TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
"TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
"TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
"TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
"TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
"TLS_DHE_RSA_WITH_AES_256_GCM_SHA384",
"TLS_DHE_RSA_WITH_AES_128_GCM_SHA256"
``` |
| `excludedCiphers`             | The block-list of non-acceptable TLS ciphers.                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `acceptorThreads`             | The number of threads used to accept TCP socket connections. Learn more in the [Jetty description of acceptor threads](https://jetty.org/docs/jetty/12/programming-guide/server/http.html#connector-acceptors).                                                                                                                                                                                 | `1`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `selectorThreads`             | The number of threads used to manage the set of accepted TCP sockets. Learn more in the [Jetty description of selector threads](https://jetty.org/docs/jetty/12/programming-guide/server/http.html#connector-selectors).                                                                                                                                                                        | `5`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `timeout`                     | The amount of time to wait in milliseconds before closing a connection if no data has been sent or received.                                                                                                                                                                                                                                                                                    | `30000`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `outputBufferSize`            | The maximum size in bytes of a server response buffer.                                                                                                                                                                                                                                                                                                                                          | `32768`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `inputBufferSize`             | The maximum size in bytes of the client request buffer.                                                                                                                                                                                                                                                                                                                                         | `8192`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `headerBufferSize`            | The maximum size in bytes of the response and request header buffers.                                                                                                                                                                                                                                                                                                                           | `16384`                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sniHostCheckEnabled`         | Toggles the Jetty SNI host check. When enabled, Jetty checks that the incoming host header matches the server certificate's subject. This setting does nothing if `secure` is `false`.                                                                                                                                                                                                          | `true`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `proxyLoadBalancerConnection` | Toggles the handling of proxied requests. Enable this property when running IDM behind a proxy or load balancer.                                                                                                                                                                                                                                                                                | `false`                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Jetty thread settings and Gzip compression

To change the Jetty thread pool and Gzip compression settings, make changes to your project's `conf/webserver.json` file:

```json
{
  "maxThreads": {
    "$int": "&{openidm.webserver.max.threads|&{org.ops4j.pax.web.server.maxThreads|200}}"
  }
}
```

## Jetty QoSHandler

The Jetty [QoSHandler](https://jetty.org/docs/jetty/12/programming-guide/server/http.html#handler-use-qos) limits the number of threads most PingIDM requests can run on. The handler is configured to use all but two threads to ensure requests to critical endpoints are always handled.

The critical endpoints include:

* `openidm/health/live`

* `openidm/metrics/*`

Learn more about these endpoints at [Liveness and readiness probes](system-healthcheck.html#liveness-readiness-probes) and in the [Metrics reference](../monitoring-guide/metrics.html).

The QoSHandler keeps its own queue of requests rather than allowing requests to queue in the Jetty `QueuedThreadPool`. Because of this, the `jetty.thread.queue` (API) and the `idm_jetty_thread_queue` (Prometheus) metric should remain at `0`.The queued requests are handled by the [`jetty.qos.queue.count`](../monitoring-guide/api-metrics.html#api-jetty-qos-queue-count) API metric and the [`idm_jetty_qos_queue_count`](../monitoring-guide/prometheus-metrics.html#prometheus-jetty-qos-queue-count) gauge metric in Prometheus.

---

---
title: Manage configuration with Docker
description: Build a base Docker image for PingIDM using the provided Custom.Dockerfile to support file-based configuration in containerized deployments
component: pingidm
version: 8.1
page_id: pingidm:install-guide:docker
canonical_url: https://docs.pingidentity.com/pingidm/8.1/install-guide/docker.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Installation", "Cluster", "Configuration", "Docker"]
section_ids:
  build_a_base_image: Build a base image
---

# Manage configuration with Docker

Docker is a set of products that allows you to run IDM instances in *containers*. A container is a software package that can be virtualized. Containerization is one way to use a [file-based configuration](cluster-config-changes.html#file-based-config) strategy to manage IDM clusters in a repeatable and reliable way.

You can download Docker from [the official Docker homepage](https://www.docker.com).

## Build a base image

After you have downloaded and installed Docker, you must build a *base image* for IDM. Ping supplies a `Custom.Dockerfile`, which contains our expected structure. To build a base image with it, do the following:

1. As a prerequisite, you must build the `java-21` base image:

   1. Clone the `https://github.com/ForgeRock/forgeops-extras.git` repository.

   2. Build the `java-21` base image from the `forgeops-extras/images/java-21` directory:

      ```
      cd /path/to/forgeops-extras/images/java-21
      docker build --tag my-repo/java-21 .

       => [internal] load build definition from Dockerfile       0.0s
       => => transferring dockerfile: 2.38kB                     0.0s
       ...
       => => writing image sha256:7674...f7f5                    0.0s
       => => naming to docker.io/my-repo/java-21                 0.0s
      ```

2. Build the base image for IDM:

   1. Download the latest version of the IDM `.zip` file from the [Backstage](https://backstage.forgerock.com/downloads) download site.

   2. Unzip the IDM `.zip` file.

   3. Edit the `Custom.Dockerfile` in the `openidm/bin` directory. Change the line:

      ```
      FROM gcr.io/forgerock-io/java-21:latest
      ```

      to:

      ```
      FROM my-repo/java-21
      ```

   4. Build the `IDM` base image from the `openidm/bin` directory:

      ```
      cd /path/to/openidm/bin
      docker build . --file Custom.Dockerfile --tag my-repo/idm:8.1.1

       => [internal] load build definition from Custom.Dockerfile       0.0s
       => => transferring dockerfile: 648B                              0.0s
       ...
       => => writing image sha256:9550...5788                           0.0s
       => => naming to docker.io/my-repo/idm:8.1.1                      0.0s
      ```

3. Run the `docker images` command to verify that you built the base images:

   ```
   docker images | grep my-repo

   REPOSITORY                   TAG      IMAGE ID        CREATED        SIZE
   my-repo/idm                  8.1.1    0cc1b7f70ce6    1 hour ago     387MB
   my-repo/java-21              latest   76742b285ddf    1 hour ago     146MB
   ```

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you use IDM as part of a platform deployment, refer to [Base Docker images](https://docs.pingidentity.com/forgeops/2025.1/reference/base-docker-images.html). |

After you build your base images, you can push them to your Docker repository. Refer to your registry provider documentation for detailed instructions.
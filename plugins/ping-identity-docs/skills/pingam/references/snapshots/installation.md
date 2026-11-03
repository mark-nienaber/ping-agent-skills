---
title: Prepare identity stores
description: Configure PingAM to access user identity data from LDAP directory servers or prepare a new PingDS instance for identity storage
component: pingam
version: 8.1
page_id: pingam:installation:prepare-identity-repository
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-identity-repository.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install", "Identity Store"]
page_aliases: ["install-guide:prepare-identity-repository.adoc"]
section_ids:
  prepare-idrepo: Install and configure PingDS for identity data
  prepare-existing-identity-repository: Configure existing directory servers for identity data
  prepare-idrepo-considerations: Create a directory server user for AM connections
  ad-bind-account: Create a bind account in Active Directory for AM connections
  prepare-idrepo-schema: Update the schema in an identity store
  prepare-idrepo-manual-schema-steps: Prepare an identity store with manual schema updates
  prepare-idrepo-auto-schema-steps: Prepare an identity store with automatic schema updates
---

# Prepare identity stores

AM accesses user identity data from one or more identity stores, also called identity repositories.

In most deployments, AM connects to existing LDAP directory servers for user identity data, because it shares data in an identity store with other applications.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Be careful when you configure more than one identity store in a single realm:- **Writes**: AM tries to perform write operations on each writable identity store configured in a realm, and there's no way to configure which store is written to. Don't configure more than one writable identity store per realm.

- **Reads**: AM reads from all identity stores in a realm. If multiple stores are present, attribute mappings used by agents, SAML 2.0 logins, or other features may draw values from any of the configured stores.To manage identities and reconcile differences between multiple identity stores, use [PingIDM](https://docs.pingidentity.com/pingidm/8.1). |

To prepare identity stores, read the following sections:

* If you're installing a new PingDS instance for identity data, read [Install and configure PingDS for identity data](#prepare-idrepo).

* If you're connecting AM to an existing identity store, read [Configure existing directory servers for identity data](#prepare-existing-identity-repository).

Find more information on configuring your identity stores in [Identity stores](../setup/setting-up-identity-stores.html).

## Install and configure PingDS for identity data

This section shows how to install and set up a new DS server for identity data. Make sure DS replicas use the same configuration.

Installing DS with a [setup profile](https://docs.pingidentity.com/pingds/8.1/install-guide/setup-profiles.html) creates the required backend, schema, bind user, and indexes.

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The bind account for the identity store is fetched when AM starts up. If you change the account (DN or password) while AM is running, you must restart AM to take account of the changes. Otherwise, you'll encounter bind failures with persistent searches. |

1. Follow the steps in [Install DS for AM identities](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-idrepo.html) in the PingDS documentation.

2. Share the identity store certificate with the AM container to prepare for TLS/LDAPS. Communication with the identity store *must* use a secure connection.

   * On the DS host, export the DS CA certificate.

     DS uses a deployment ID and password to generate a CA key pair. Learn more in [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-ids).

     Use the `dskeymgr` command to export the CA certificate:

     ```bash
     $ /path/to/opendj/bin/dskeymgr \
     export-ca-cert \
     --deploymentId $DEPLOYMENT_ID \
     --deploymentIdPassword password \
     --outputFile /path/to/ca-cert.pem
     ```

   * Copy the `ca-cert.pem` file to an accessible location on the AM host.

   - Import the DS CA certificate into the AM truststore:

     ```bash
     $ keytool \
     -importcert \
     -file /path/to/ca-cert.pem \
     -keystore /path/to/am/security/keystores/truststore
     -storepass truststore-password
     ```

   Learn more about configuring AM's truststore, in [Prepare the truststore](prepare-trust-store.html).

3. If you didn't install DS using a setup profile, perform the following steps to update the permissions in a PingDS identity store.

   If you are using a directory server other than PingDS, apply the relevant LDIF files using the appropriate tools.

   * Edit the `opendj_userinit.ldif` LDIF file in the `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj` directory, replacing all variables that are surrounded by *at* (`@` ) symbols with a value specific to your directory server.

     For example, in the `opendj_userinit.ldif` LDIF file you must replace all instances of *@userStoreRootSuffix@* with the root suffix you specified when configuring the DS identity store. The default is `ou=identities`.

   * Use the `ldapmodify` command to add the updated LDIF data to the DS instance.

     For example:

     ```bash
     $ /path/to/opendj/bin/ldapmodify \
     --hostname 'ds.example.com' \
     --port 1636 \
     --useSsl \
     --usePkcs12TrustStore /path/to/opendj/config/keystore \
     --truststorepassword:file /path/to/opendj/config/keystore.pin \
     --continueOnError \
     --bindDN uid=admin \
     --bindPassword str0ngAdm1nPa55word \
     /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_userinit.ldif
     ```

     You can find more information on this LDIF file, and equivalent files for supported directory servers, in [Set up directory schemas with LDIF](supported-ldifs.html).

   * If you intend to use web authentication, or perform device profiling with the Ping SDKs, you might need to update the directory server schema. For a PingDS repository, you can update the schema by applying the following LDIF files:

     * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_webauthndevices.ldif`

     * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_deviceprofiles.ldif`

       For example:

       ```bash
       $ /path/to/opendj/bin/ldapmodify \
       --hostname 'ds.example.com' \
       --port 1636 \
       --useSsl \
       --usePkcs12TrustStore /path/to/opendj/config/keystore \
       --truststorepassword:file /path/to/opendj/config/keystore.pin \
       --continueOnError \
       --bindDN uid=admin \
       --bindPassword str0ngAdm1nPa55word \
       /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_webauthndevices.ldif\
       /path/to/tomcat/webapps/am/WEB-INF/template/ldif/opendj/opendj_deviceprofiles.ldif
       ```

       You can find more information on these LDIF files in [Set up directory schemas with LDIF](supported-ldifs.html). For directory servers other than PingDS, adapt the `opendj_*.ldif` files accordingly.

4. Proceed to [configure the identity store](../setup/setting-up-identity-stores.html#realm-data-store) in AM.

   The bind DN of the service account to use when configuring the identity store in AM is `uid=am-identity-bind-account,ou=admins,ou=identities`.

## Configure existing directory servers for identity data

It is common for AM to access identity data from an existing directory server. AM requires a user account to connect to the directory server, and AM LDAP schema to update entries with AM-related identity data.

You can find a list of supported directory servers in [Directory servers](https://docs.pingidentity.com/pingam/release-notes/requirements.html#directory-servers).

The following sections show you how to prepare an existing identity store for use in AM:

* [Create a directory server user for AM connections](#prepare-idrepo-considerations)

* [Update the schema in an identity store](#prepare-idrepo-schema)

### Create a directory server user for AM connections

AM connects to a directory server with a service account that you specify in the AM identity store configuration. This service account is known as the *AM bind account*.

Specifying the directory administrator as the AM bind account isn't recommended for production deployments as it would give AM directory administrator privileges to the identity store.

Instead, create a separate AM bind account with fewer access privileges than the directory administrator so that you can assign the appropriate level of privileges for the AM bind account.

You need to consider two areas of permission for the AM bind account:

* Schema Update Privileges

  AM needs to update the directory schema when you configure a new identity store and when you upgrade AM software. If the AM bind account has schema update privileges, AM can update the schema dynamically during identity store configuration and during AM upgrades. If the AM bind account doesn't have schema update privileges, you must update the schema manually before configuring a new identity store and before upgrading AM.

* Directory Read and Write Access Privileges

  If you want AM to create, update, and delete user entries, then the AM bind account must have full read and write access to the identity data in the directory. If you are using an identity store as a read-only user directory, then the AM bind account needs read privileges only.

The level of access privileges you give the AM bind account is specific to each AM deployment. Work with your directory server administrator to determine the appropriate level of privileges as part of the process of preparing your identity stores.

#### Create a bind account in Active Directory for AM connections

The following procedure gives an example of creating a bind account in Active Directory:

Perform these steps to create a user that AM can use to connect to Active Directory. These steps are one example, consult with your Active Directory administrator on how best to create an account.

1. Create a new user account in the Active Directory domain. For example, in Windows 2019:

   * In the Active Directory Users and Computers tool, right-click Users in the domain, and select New > User.

   * Provide descriptive values for the new user, and a logon name such as `AM-Bind-Account`.

   * Click Next.

   * Enter a strong password for the bind account, disable the *User must change password at next logon* option, and click Next.

   * Review the details of the new account, and click Finish.

2. Give the new bind account access to the directory data:

   * In the Active Directory Users and Computers tool, right-click the domain that contains your users, and select Delegate Control.

   * Add the bind account you created in the previous step, and click Next.

   * Select the tasks you want to allow the AM bind account to perform from the list.

     For example, to allow read and write access to users, enable the `Create, delete, and manage inetOrgPerson accounts` task.

   * After assigning the tasks you want to allow the AM bind account to perform, click Finish.

     You can now set up the necessary schema in the directory server.

   The bind account to use when configuring the identity store in AM is the full DN of the user, for example `uid=AM-Bind-Account,ou=Users,dc=example,dc=org`.

### Update the schema in an identity store

AM can add the necessary LDAP schema definitions itself, if it has sufficient privileges to do so, or you can apply the LDAP schema definition LDIF files manually if required. Read the following procedures:

* [Prepare an identity store with manual schema updates](#prepare-idrepo-manual-schema-steps)

* [Prepare an identity store with automatic schema updates](#prepare-idrepo-auto-schema-steps)

#### Prepare an identity store with manual schema updates

If the AM bind account doesn't have permission to update schema then you must configure existing datastores using manual schema updates. To do this, you must update the directory server schema of the existing identity store manually at the following times:

* Before you configure the identity store as part of initial AM configuration.

* Before you configure an identity store after initial AM configuration.

* Whenever you upgrade AM.

A number of LDIF files are provided in the AM `.war` file for supported identity directory servers. The path is `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/directory-type`, where `directory-type` is one of the following:

* `ad` for Microsoft Active Directory

* `adam` for Microsoft Active Directory Lightweight Directory Services

* `opendj` for PingDS and Oracle Unified Directory

* `pingdirectory` for PingDirectory

You can find more information on the LDIF files in [Set up directory schemas with LDIF](supported-ldifs.html).

The following steps update the schema in an Active Directory identity store. For other directory servers, apply the relevant LDIF files using the appropriate tools.

1. Edit the LDIF files in the `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/ad` directory, replacing any variables that are surrounded by *at* (`@` ) symbols with a value specific to your directory server.

   For the Active Directory LDIF files you must replace all instances of *@userStoreRootSuffix@* with the root suffix used by your Active Directory identity store, for example `DC=example,DC=org`.

2. Using an Active Directory administrator account, add the required AM schema extensions to your identity store.

   For example, in PowerShell, run the `ldifde` command to import the user, device print, and dashboard schema extensions:

   ```powershell
   PS C:\Users\Administrator> cd \path\to\am\WEB-INF\template\ldif\ad
   PS C:\path\to\am\WEB-INF\template\ldif\ad> ldifde -i -f .\ad_user_schema.ldif
   Connecting to "domain.example.org"
   Logging in as current user using SSPI
   Importing directory from file ".\ad_user_schema.ldif"
   Loading entries.................................................................
   64 entries modified successfully.

   The command has completed successfully

   PS C:\path\to\am\WEB-INF\template\ldif\ad> ldifde -i -f .\ad_deviceprint.ldif
   Connecting to "domain.example.org"
   Logging in as current user using SSPI
   Importing directory from file ".\ad_deviceprint.ldif"
   Loading entries.................................................................
   6 entries modified successfully.

   The command has completed successfully

   PS C:\path\to\am\WEB-INF\template\ldif\ad> ldifde -i -f .\ad_dashboard.ldif
   Connecting to "domain.example.org"
   Logging in as current user using SSPI
   Importing directory from file ".\ad_dashboard.ldif"
   Loading entries.................................................................
   6 entries modified successfully.

   The command has completed successfully
   ```

3. If you intend to use push or web authentication, apply the following LDIF files:

   * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/ad/ad_pushdevices.ldif`

   * `/path/to/tomcat/webapps/am/WEB-INF/template/ldif/ad/ad_webauthndevices.ldif`

   You can find more information on these LDIF files, and the equivalent files for supported directory servers, in [Set up directory schemas with LDIF](supported-ldifs.html).

4. Proceed to [configure the identity store](../setup/setting-up-identity-stores.html#realm-data-store) in AM.

   |   |                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you updated the schema to use web authentication, you must add `webauthnDeviceProfilesContainer` to the LDAP User Object Class property when configuring the identity store in a realm. This property is located on the User Configuration tab. |

#### Prepare an identity store with automatic schema updates

If the bind account has permission to update schema then you can allow AM to update the schema automatically.

To allow AM to update the schema, you must first configure AM to be able to access the directory server, and enable the Load Schema option, by performing the following steps:

1. Configure the directory server in AM by following the instructions in [Configure an identity store](../setup/setting-up-identity-stores.html#realm-data-store).

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | Enable the Load Schema option before saving your changes, and AM will apply the necessary schema to the directory server. |

   The schema is loaded as part of configuring the identity store in AM. No further configuration is required.

2. Verify that the new identity store is correctly configured in AM by following the instructions in [Test identity store access](../setup/prepare-idrepo-testing.html).

---

---
title: Prepare the environment
description: Prepare your environment for PingAM installation by configuring networking, Java, and file descriptor settings
component: pingam
version: 8.1
page_id: pingam:installation:prepare-env-install
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-env-install.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install"]
page_aliases: ["install-guide:prepare-env-install.adoc"]
---

# Prepare the environment

Perform the following tasks to prepare your environment for AM:

[icon: id-card, set=fad, size=3x]

#### [Prepare an FQDN](prepare-networking.html)

AM cookies require a fully qualified domain name.

[icon: coffee, set=fad, size=3x]

#### [Prepare a Java environment](prepare-java.html)

AM requires a JDK to run.

[icon: cogs, set=fad, size=3x]

#### [Configure maximum file descriptors](prerequisites-file-descriptors.html)

Data stores use file descriptors for concurrent connections.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Find details of supported operating systems and Java requirements in [Requirements](https://docs.pingidentity.com/pingam/release-notes/requirements.html) in the Release notes. |

---

---
title: Prepare the Java environment
description: Prepare the Java environment and configure JVM settings for PingAM deployments
component: pingam
version: 8.1
page_id: pingam:installation:prepare-java
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-java.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install"]
page_aliases: ["install-guide:prepare-java.adoc"]
section_ids:
  prepare-java-oracle: Settings for Oracle Java environments
  prepare-java-openjdk: Settings for OpenJDK Java environments
  tuning-jvm-for-openam: Tune JVM settings
---

# Prepare the Java environment

AM software depends on a Java runtime environment. Check the output of the `java -version` command to make sure your version is supported according to the [Java requirements](https://docs.pingidentity.com/pingam/release-notes/requirements.html#prerequisites-java).

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Keep your Java software up-to-date with the latest supported version. Make sure your `JAVA_HOME` environment variable always points to the latest supported Java version. |

The following table summarizes the high-level tasks required to configure your Java environment:

| Task                                                                                                                                                                                                                                                                                                                                                               | Resources                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Prepare your JDKThe suggestions in these sections apply to AM deployments with the following characteristics:- The deployment has a dedicated DS server for the Core Token Service (CTS). The host running this directory server is a high-end server with a large amount of memory and multiple CPUs.

- The AM server is configured to use server-side sessions. | * [Settings for Oracle Java environments](#prepare-java-oracle)

* [Settings for OpenJDK Java environments](#prepare-java-openjdk) |
| Tune the JVM for AMThis document provides guidance on tuning the JVM for production, but you must also tune it for garbage collection based on your environment.                                                                                                                                                                                                   | - [Tune JVM settings](#tuning-jvm-for-openam)                                                                                      |

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can find information on configuring JVM properties for proxy support in [Configuring AM for Outbound Communication](../security/reverse-proxy.html#outbound-communication). |

## Settings for Oracle Java environments

When using an Oracle Java environment, set at least the following options:

* `-Xmx1g` (minimum)

  AM requires at least a 1 GB heap. Higher volume and higher performance deployments require additional heap space.

* `-XX:MetaspaceSize=256m`

  Set the metaspace memory size to 256 MB.

* `-XX:MaxMetaspaceSize=256m`

  Set the maximum metaspace memory size to 256 MB.

You can find additional JVM tuning and security recommendations in [Tune JVM settings](#tuning-jvm-for-openam).

## Settings for OpenJDK Java environments

When using an OpenJDK Java environment, set at least the following options.

* `-Xmx1024m` (minimum)

  AM requires at least a 1 GB heap. Higher volume and higher performance deployments require additional heap space.

  Recommended: `-Xmx2048m`.

* `-XX:MetaspaceSize=256m`

  Set the initial metadata space size to 256 MB.

## Tune JVM settings

This section gives some initial guidance on configuring the JVM for running AM when the deployment has a dedicated CTS token store, and AM is configured to use server-side sessions.

These settings provide a strong foundation to the JVM before a more detailed garbage collection tuning exercise, or as best practice configuration for production:

**Heap size settings**

| JVM parameters                               | Suggested value                                                                                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-Xms` & `-Xmx`                              | At least 1 GB. In production environments, at least 2 to 3 GB. This setting depends on the available physical memory and whether a 32- or 64-bit JVM is used.                                                                                                                                                                                                                   |                                                                                                                                                                                                                                 |
| `-XX:MetaspaceSize` & `-XX:MaxMetaspaceSize` | Set both to 256 MB	Metadata space (Metaspace) is a dedicated region within Native Memory. It can grow automatically if you don't set a maximum size. The ideal Metaspace size depends on your deployment and the number of scripts you're running. 256 MB is considered a safe value for production deployments, but you might need to tweak this for your specific deployment. | Controls the size of the metaspace in the JVM.                                                                                                                                                                                  |
| `-Dsun.net.client.defaultReadTimeout`        | 60000                                                                                                                                                                                                                                                                                                                                                                           | Controls the read timeout in the Java HTTP client implementation.This applies only to the Sun/Oracle HotSpot JVM.                                                                                                               |
| `-Dsun.net.client.defaultConnectTimeout`     | High setting: 30000 (30 seconds)                                                                                                                                                                                                                                                                                                                                                | Controls the connect timeout in the Java HTTP client implementation.When you have hundreds of incoming requests per second, reduce this value to avoid a huge connection queue.This applies only to the Sun/Oracle HotSpot JVM. |

**Security settings**

| JVM parameters                                        | Suggested value | Description                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-Dhttps.protocols`                                   | `TLSv1.2`       | Controls the protocols used for outbound HTTPS connections from AM.Specify one or more of the following values, separated by commas:- TLSv1.2

- TLSv1.3This setting applies only to Sun/Oracle Java environments.                                                                                                                                     |
| `-Dorg.forgerock.openam.ldap.secure.protocol.version` | `TLSv1.2`       | Controls the protocol AM uses to connect to affected external resources.Specify one or more of the following values, separated by commas:- TLSv1.2

- TLSv1.3This setting overrides the default server value. Learn more in [advanced properties](../setup/deployment-configuration-reference.html#org.forgerock.openam.ldap.secure.protocol.version). |

**Garbage collection settings**

| JVM parameters                    | Suggested value                                      | Description                                                                                                                            |
| --------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `-verbose:gc`                     |                                                      | Verbose garbage collection reporting.                                                                                                  |
| `-Xlog:gc*`                       | `-Xlog:gc=info:file=$CATALINA_HOME/logs/gc-info.log` | Logs detailed information about garbage collection. When using the `-Xlog:gc` option, you can also specify the level, and output file. |
| `-XX:+HeapDumpOnOutOfMemoryError` |                                                      | Out of Memory errors generate a heap dump automatically.                                                                               |
| `-XX:HeapDumpPath`                | `$CATALINA_HOME/logs/heapdump.hprof`                 | Location of the heap dump.                                                                                                             |
| `-XX:+PrintClassHistogram`        |                                                      | Prints a heap histogram when the JVM receives a SIGTERM signal.                                                                        |

**Other settings**

| JVM parameters                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--add-opens java.xml/com.sun.org.apache.xerces.internal.dom=ALL-UNNAMED`    | When running AM, SAML Artifact flows, WS-Federation flows and any flows that use Xerces SOAP libraries can fail with the following error:`Caused by: java.lang.IllegalAccessError: superclass access check failed: class com.sun.xml.messaging.saaj.soap.SOAPDocumentImpl (in unnamed module @0x774ca796) cannot access class com.sun.org.apache.xerces.internal.dom.DocumentImpl (in module java.xml) because module java.xml does not export com.sun.org.apache.xerces.internal.dom to unnamed module @0x774ca796`Set these JVM parameters to avoid this error. |
| `--add-exports java.xml/com.sun.org.apache.xerces.internal.jaxp=ALL-UNNAMED` |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `--add-exports java.xml/com.sun.org.apache.xerces.internal.util=ALL-UNNAMED` |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Prepare the truststore
description: Create and configure a truststore to enable PingAM to make secure LDAPS and HTTPS connections to PingDS and external sites
component: pingam
version: 8.1
page_id: pingam:installation:prepare-trust-store
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-trust-store.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-10-01T10:22:10Z
keywords: ["Install", "Security"]
page_aliases: ["install-guide:prepare-trust-store.adoc"]
section_ids:
  prepare-am-trust-store: Create a truststore for AM
---

# Prepare the truststore

PingDS requires secure connections using LDAPS. To connect to a DS server securely, AM needs access to DS's CA certificate. AM also needs access to CA certificates for making secure connections to other sites; for example, connections to social providers using HTTPS.

To give AM access to these certificates, you create a *truststore* that contains the certificates, and configure AM's web application container to use that truststore when starting up.

AM uses a single truststore for LDAPS and outbound HTTPS connections. This truststore *must* contain the CA certificates of the sites with which AM communicates securely.

By default, Apache Tomcat loads the truststore configured for its JVM (for example, `$JAVA_HOME/JRE/lib/security/cacerts`). The default JVM truststore contains multiple CA certificates. Its password, by default, is `changeit`.

As a best practice, create a *new* truststore with the certificates required for your AM deployment, then configure your container to use it. Don't add the DS CA certificate to the JVM's truststore because JVM updates are likely to overwrite the `cacerts` file.

To keep all existing CA certificates, you can copy the `cacerts` keystore file, change its password to a secure one, and import the DS CA certificate into it. Then, configure your web application container, for example, Apache Tomcat, to load that file as its truststore.

|   |                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Using a separate truststore for AM means updates to the JVM truststore in patch releases aren't taken into account. This can cause operational issues, for example, when distrusted root CA certificates are removed, or when new root CA certificates are added.To mitigate this risk, update the AM truststore periodically to reflect the latest JVM truststore settings. |

## Create a truststore for AM

These steps create a copy of the default JVM truststore, and configure the AM web application container to use the new truststore:

1. Copy the default truststore. For example, `$JAVA_HOME/lib/security/cacerts`, name it `truststore`, and place it in a directory of your choice:

   ```bash
   $ cp $JAVA_HOME/lib/security/cacerts /path/to/truststore
   ```

   |   |                                                                                                                                                                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you place the truststore in the `/path/to/am` directory *before* you install AM, the installation process detects the directory isn't empty and the installation fails.After AM is installed, you can move the truststore to a different directory. For example, the `/path/to/am/security/keystores` directory. |

2. For improved security, change the default password for the truststore.

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | The default password of the `$JAVA_HOME/lib/security/cacerts` truststore is `changeit`. |

   Use the `keytool -storepasswd` option to change the default password:

   ```bash
   $ keytool -storepasswd -keystore /path/to/truststore
   Enter keystore password: changeit
   New keystore password: new-password
   Re-enter new keystore password: new-password
   ```

3. Export the DS certificate.

   * On the DS host, export the DS CA certificate.

     DS uses a deployment ID and password to generate a CA key pair. Learn more in [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-ids).

     Use the `dskeymgr` command to export the CA certificate:

     ```bash
     $ /path/to/opendj/bin/dskeymgr \
     export-ca-cert \
     --deploymentId $DEPLOYMENT_ID \
     --deploymentIdPassword password \
     --outputFile /path/to/ca-cert.pem
     ```

   * Copy the `ca-cert.pem` file to an accessible location on the AM host.

4. Import the DS CA certificate into the new truststore:

   ```bash
   $ keytool \
   -importcert \
   -file /path/to/ca-cert.pem \
   -keystore /path/to/truststore
   -storepass truststore-password
   ```

   Confirm you trust this certificate when prompted.

5. To configure the truststore in Apache Tomcat so that AM can access it, append the truststore settings to the `CATALINA_OPTS` variable in the `setenv` file.

   For example:

   * Unix/Linux

   * Windows (Command Prompt)

   In `$CATALINA_BASE/bin/setenv.sh`:

   ```bash
   export CATALINA_OPTS="$CATALINA_OPTS -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m \
   -Djavax.net.ssl.trustStore=/path/to/truststore \
   -Djavax.net.ssl.trustStorePassword=new-password \
   -Djavax.net.ssl.trustStoreType=jks"
   ```

   In `$CATALINA_BASE/bin/setenv.bat`:

   ```powershell
   set "CATALINA_OPTS=%CATALINA_OPTS% -server -Xmx2g -XX:MetaspaceSize=256m -XX:MaxMetaspaceSize=256m -
   -Djavax.net.ssl.trustStore=/path/to/truststore -
   -Djavax.net.ssl.trustStorePassword=new-password -
   -Djavax.net.ssl.trustStoreType=jks"
   ```

   Read your specific container's documentation for information on configuring truststores.

   After AM is installed, you can move the truststore to a different location. For example, the `/path/to/am/security/keystores/`. If you do, remember to update the truststore path in the container configuration.

---

---
title: Run AM as a service
description: Configure PingAM to run as a systemd service on Linux distributions and manage it using systemctl commands
component: pingam
version: 8.1
page_id: pingam:installation:run-am-service
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/run-am-service.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install"]
page_aliases: ["install-guide:run-am-service.adoc"]
section_ids:
  configure-am-service: Configure AM as a service
  manage-am-service: Use systemctl commands to manage the AM service
---

# Run AM as a service

AM can run as a service on a standard `systemd`-based Linux distribution. Once you have configured AM as a service, you can stop and start AM using `systemd`.

These instructions assume you have deployed AM on Apache Tomcat.

|   |                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A service file (called `tomcat`) is created if you install Tomcat using a package manager such as `yum`. You can use this service file instead of creating your own.You can [enable](#enable) this service to run on startup and [manage the Tomcat service](#manage-am-service) using `systemctl` commands. Replace `am.service` in these example commands with `tomcat`. |

## Configure AM as a service

1. Create a service file using your preferred text editor:

   ```bash
   $ sudo vim /etc/systemd/system/am.service
   ```

2. Add the following content to this file, update all the values as needed, and save:

   ```ini
   [Unit]
   Description=AM (Apache Tomcat)
   After=network.target

   [Service]
   Type=forking

   Environment=JAVA_HOME=/path/to/jdk
   Environment=CATALINA_PID=/path/to/tomcat/temp/tomcat.pid
   Environment=CATALINA_HOME=/path/to/tomcat
   Environment=CATALINA_BASE=/path/to/tomcat
   Environment='CATALINA_OPTS=-Xmx2048m -server -XX:+UseParallelGC'
   Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

   ExecStart=/path/to/tomcat/bin/startup.sh
   ExecStop=/path/to/tomcat/bin/shutdown.sh

   User=tomcat_user
   Group=tomcat_user

   [Install]
   WantedBy=multi-user.target
   ```

3. Reload the daemon:

   ```bash
   $ sudo systemctl daemon-reload
   ```

4. []()Make the new service launch on startup:

   ```bash
   $ sudo systemctl enable am.service
   ```

5. Check the service is enabled:

   ```bash
   $ systemctl is-enabled am.service
   ```

   This command returns `enabled` or `disabled` as appropriate.

## Use systemctl commands to manage the AM service

Once you've configured AM as a service and checked it's enabled, use `systemctl` commands to manage the AM service:

* Start the service:

  ```bash
  $ sudo systemctl start am.service
  ```

* Stop the service:

  ```bash
  $ sudo systemctl stop am.service
  ```

* Restart the service:

  ```bash
  $ sudo systemctl restart am.service
  ```

* Check the service status:

  ```bash
  $ sudo systemctl status am.service
  ```

  This command returns the service state (whether the service has started or stopped as expected) and the first few entries of the AM log file.

---

---
title: Secure connections to the AM container
description: Configure Apache Tomcat to use CA-signed or self-signed certificates for secure HTTPS connections to PingAM
component: pingam
version: 8.1
page_id: pingam:installation:configure-container-HTTPS
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/configure-container-HTTPS.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install", "Web Container"]
page_aliases: ["install-guide:configure-container-HTTPS.adoc"]
section_ids:
  openam-with-https-on-tomcat: Configure Apache Tomcat for HTTPS
  share-self-signed-certs: Share self-signed certificates
---

# Secure connections to the AM container

There are many ways to deploy and configure your environment for AM, but we recommend that you enforce HTTPS connections to AM. For more information about securing AM, see [Security](../security/preface.html).

The container where AM runs requires a certificate to set up secure connections. You can install either CA-signed or self-signed certificates in the container where AM runs, although you should have in mind that you will need to configure your applications to trust your self-signed certificates.

The following is an example about how to configure Apache Tomcat for HTTPS:

## Configure Apache Tomcat for HTTPS

There are several ways of completing the tasks ahead, and it is beyond the scope of this document to explore them all. If this procedure does not suit your environment, refer to your CA vendor documentation, the `keytool` command documentation, or Java container documentation for more information.

1. Stop Apache Tomcat.

2. Ensure you have a keystore containing the appropriate certificates:

   * If you have CA certificates, import them in a new keystore using the `keytool` command. For example, if you have root, intermediate, and primary certificates, import them in the same keystore you used when generating your certificate signing request (CSR):

     ```
     $ keytool -importcert -alias root -file myrootCA.cert \
     -keystore /path/to/tomcat_keystore.pfx -storetype PKCS12
     $ keytool -importcert -alias intermediate -file myintCA.cert \
     -keystore /path/to/tomcat_keystore.pfx -storetype PKCS12
     $ keytool -importcert -alias mysite.example.com -file mypriCA.cert \
     -keystore /path/to/tomcat_keystore.pfx -storetype PKCS12
     ```

   * If you need a self-signed certificate, create a new self-signed key pair with the `keytool` command.

     For example:

     ```
     $ cd /path/to/tomcat/conf/
     $ keytool -genkey -alias am.example.com -storetype PKCS12 -keyalg RSA -validity 730 \
       -keysize 2048 -keystore tomcat_keystore.pfx -dname 'CN=am.example.com' -ext 'san=dns:am.example.com'
     ```

3. Create an SSL connector configuration in Apache Tomcat's `conf/server.xml` configuration file, and specify your keystore file, type, and password.

   Note that there are different types of SSL connectors, and that implementation details may change across Tomcat versions. This example creates a JSSE connector in Tomcat as provided as part of the Java runtime:

   ```xml
   <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"
    maxThreads="200" SSLEnabled="true" scheme="https" secure="true"
    keystoreFile="/path/to/tomcat_keystore.pfx"
    keystoreType="PKCS12" keystorePass="keystore_password"
    clientAuth="false" sslProtocol="TLS" />
   ```

   You may need different settings depending on your configuration and version of Apache Tomcat. See the documentation for your version for more information.

4. Start Tomcat.

5. Verify that you can connect to Apache Tomcat on port 8443 over HTTPS.

   If you used self-signed certificates, your browser would not trust the certificate, because the certificate is self-signed and not signed by any of the CAs stored in your browser.

   ![The browser displays pages to let you decide to trust the self-signed certificate.](_images/browser-unknown-cert.png)Figure 1. Unknown Certificate

   If you recognize the subject and issuer of your certificate, and so can choose to trust the certificate, save it into your browser's trust store.

6. Deploy and configure AM.

7. To share the self-signed certificate in your container with other applications or servers, see [Share self-signed certificates](#share-self-signed-certs).

## Share self-signed certificates

How you configure the containers where AM and your applications run to use self-signed certificates depends on your web application server or web server software. The following basic principles apply:

* First, your container requires its own certificate for setting up secure connections.

* Second, the clients connecting must be able to trust the container's certificate. Generally, this means that clients recognize the container's certificate because they have a copy of the public certificate stored somewhere the client trusts.

* Third, if you use certificate authentication in AM, AM must also be able to find a copy of the client's public certificate to trust the client, most likely by finding a match with the certificate stored in the client profile from the identity store. How you include client certificates in their identity store entries depends on your identity store more than it depends on AM.

Some client applications let you trust certificates blindly. This can be helpful when working in your lab or test environment with self-signed certificates. For example, you might want to use HTTPS with the AM RESTful API without having the client recognize the self-signed server certificate:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Ch4ng31t" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
{
    curl: (60) Peer certificate cannot be authenticated with known CA certificates
}
```

The `curl` command performs SSL certificate verification by default, using a "bundle" of CA-signed public keys. If the default bundle file is not adequate, you can specify an alternate file using the `--cacert` option.

If this HTTPS server uses a certificate signed by a CA represented in the bundle, the certificate verification probably failed due to a problem with the certificate (it might be expired, or the name might not match the domain name in the URL). If you would like to turn off curl's verification of the certificate *for test purposes only*, use the `--insecure` option.

```bash
$ curl \
--request POST \
--insecure \
--header "Content-Type: application/json" \
--header "X-OpenAM-Username: bjensen" \
--header "X-OpenAM-Password: Ch4ng31t" \
--header "Accept-API-Version: resource=2.0, protocol=1.0" \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
{
  "tokenId":"rMLhJjWVo…​MAAlMxAAA.*",
  "successUrl":"/am/console",
  "realm":"/alpha"
}
```

When you use a self-signed certificate for your container, clients connecting must be able to trust the container certificate. Your browser makes this an easy, but manual process. For other client applications, you must import the certificate into the truststore used by the client. By default, Java applications can use the `$JAVA_HOME/lib/security/cacerts` store. The default password is `changeit`.(1)

The following steps demonstrate how to import a self-signed certificate into the Java `cacerts` store:

1. Export the certificate from the keystore:

   ```bash
   $ cd /path/to/tomcat/conf/
   $ keytool \
   -exportcert \
   -alias am.example.com \
   -file am.crt \
   -storetype JCEKS
   -keystore keystore.jceks
   Enter keystore password:
   Certificate stored in file <am.crt>;
   ```

2. Import the certificate into the trust store:

   ```bash
   $ keytool \
   -importcert \
   -alias am.example.com \
   -file am.crt
   -trustcacerts \
   -keystore $JAVA_HOME/lib/security/cacerts
   Enter keystore password:
   Owner: CN=am.example.com, OU=Admin, O=example.com
   Issuer: CN=am.example.com, OU=Admin, O=example.com
   Serial number: 4e789e40
   Valid from: Tue Sep 20 16:08:00 CEST 2011 until: Mon Dec 19 15:08:00 CET 2011
   Certificate fingerprints:
   MD5:  31:08:11:3B:15:75:87:C2:12:08:E9:66:00:81:61:8D
   SHA1: AA:90:2F:42:0A:F4:A9:A5:0C:90:A9:FC:69:FD:64:65:D9:78:BA:1D
   Signature algorithm name: SHA1withRSA
   Version: 3
   Trust this certificate? [no]: yes
   Certificate was added to keystore
   ```

(1) Alternatively, you can specify the trust store for a Java application, such as `-Djavax.net.ssl.trustStore=/path/to/truststore.jks -Djavax.net.ssl.trustStorePassword=changeit`.

---

---
title: Set up directory schemas with LDIF
description: Deploy LDIF files to create directory schemas required by PingAM for supported directory servers including PingDS, Active Directory, and Active Directory Lightweight Directory Services
component: pingam
version: 8.1
page_id: pingam:installation:supported-ldifs
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/supported-ldifs.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install", "Directory Server"]
page_aliases: ["install-guide:supported-ldifs.adoc"]
---

# Set up directory schemas with LDIF

The AM installation deploys several LDIF files that can be used to create the schemas required by AM. Find these LDIF files in the `/path/to/tomcat/webapps/am/WEB-INF/template/ldif` directory.

LDIF files are available for the following directory servers:

* PingDS

  > **Collapse: PingDS LDIF Files**
  >
  > | LDIF file                   | Description                                                                                                                                                                                                           |
  > | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  > | opendj_bounddevices.ldif    | LDIF to support bound devices.                                                                                                                                                                                        |
  > | opendj_config_schema.ldif   | LDIF to support user services.                                                                                                                                                                                        |
  > | opendj_dashboard.ldif       | LDIF to support the dashboard service.                                                                                                                                                                                |
  > | opendj_deviceprint.ldif     | LDIF to support the device print service.                                                                                                                                                                             |
  > | opendj_deviceprofiles.ldif  | LDIF to support storage of device information, collected by the SDK device authentication nodes.Apply this LDIF if you intend to use the [Ping SDKs](https://docs.pingidentity.com/sdks/latest) for device profiling. |
  > | opendj_iot_schema.ldif      | LDIF to support the IoT service.                                                                                                                                                                                      |
  > | opendj_kba.ldif             | LDIF to support the User Self-Service's knowledge-based questions and answers.                                                                                                                                        |
  > | opendj_oathdevices.ldif     | LDIF to support registered devices for the OATH authentication service.                                                                                                                                               |
  > | opendj_pushdevices.ldif     | LDIF to support registered devices for the PUSH notification service.                                                                                                                                                 |
  > | opendj_user_index.ldif      | LDIF for the user repository indexes.                                                                                                                                                                                 |
  > | opendj_user_schema.ldif     | LDIF for the user repository schema.                                                                                                                                                                                  |
  > | opendj_userinit.ldif        | LDIF to set up user session initialization.                                                                                                                                                                           |
  > | opendj_webauthndevices.ldif | LDIF to support registered devices for the Web Authentication (WebAuthn) authentication service.                                                                                                                      |

* PingDirectory

  > **Collapse: PingDirectory LDIF Files**
  >
  > | LDIF file                          | Description                                                                                                                                                                                                           |
  > | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  > | pingdirectory_bounddevices.ldif    | LDIF to support bound devices.                                                                                                                                                                                        |
  > | pingdirectory_config_schema.ldif   | LDIF to support user services.                                                                                                                                                                                        |
  > | pingdirectory_dashboard.ldif       | LDIF to support the dashboard service.                                                                                                                                                                                |
  > | pingdirectory_deviceprint.ldif     | LDIF to support the device print service.                                                                                                                                                                             |
  > | pingdirectory_deviceprofiles.ldif  | LDIF to support storage of device information, collected by the SDK device authentication nodes.Apply this LDIF if you intend to use the [Ping SDKs](https://docs.pingidentity.com/sdks/latest) for device profiling. |
  > | pingdirectory_iot_schema.ldif      | LDIF to support the IoT service.                                                                                                                                                                                      |
  > | pingdirectory_kba.ldif             | LDIF to support the User Self-Service's knowledge-based questions and answers.                                                                                                                                        |
  > | pingdirectory_oathdevices.ldif     | LDIF to support registered devices for the OATH authentication service.                                                                                                                                               |
  > | pingdirectory_pushdevices.ldif     | LDIF to support registered devices for the PUSH notification service.                                                                                                                                                 |
  > | pingdirectory_user_index.ldif      | LDIF for the user repository indexes.                                                                                                                                                                                 |
  > | pingdirectory_user_schema.ldif     | LDIF for the user repository schema.                                                                                                                                                                                  |
  > | pingdirectory_userinit.ldif        | LDIF to set up user session initialization.                                                                                                                                                                           |
  > | pingdirectory_webauthndevices.ldif | LDIF to support registered devices for the Web Authentication (WebAuthn) authentication service.                                                                                                                      |

* Microsoft Active Directory

  > **Collapse: Microsoft Active Directory LDIF Files**
  >
  > | LDIF File               | Description                                                                                      |
  > | ----------------------- | ------------------------------------------------------------------------------------------------ |
  > | ad_config_schema.ldif   | LDIF to support user services.                                                                   |
  > | ad_dashboard.ldif       | LDIF to support the dashboard service.                                                           |
  > | ad_deviceprint.ldif     | LDIF to support the device print service.                                                        |
  > | ad_kba.ldif             | LDIF to support the User Self-Service's knowledge-based questions and answers service.           |
  > | ad_oathdevices.ldif     | LDIF to support registered devices for the OATH authentication service.                          |
  > | ad_pushdevices.ldif     | LDIF to support registered devices for the PUSH notification service.                            |
  > | ad_user_schema.ldif     | LDIF for the user schema.                                                                        |
  > | ad_webauthndevices.ldif | LDIF to support registered devices for the Web Authentication (WebAuthn) authentication service. |

* Microsoft Active Directory Lightweight Directory Services

  > **Collapse: Microsoft Active Directory Lightweight Directory Services LDIF Files**
  >
  > | LDIF file                 | Description                                                                                      |
  > | ------------------------- | ------------------------------------------------------------------------------------------------ |
  > | adam_dashboard.ldif       | LDIF to support the dashboard service.                                                           |
  > | adam_deviceprint.ldif     | LDIF to support the device print service.                                                        |
  > | adam_kba.ldif             | LDIF to support the User Self-Service's knowledge-based questions and answers.                   |
  > | adam_oathdevices.ldif     | LDIF to support registered devices for the OATH authentication service.                          |
  > | adam_pushdevices.ldif     | LDIF to support registered devices for the PUSH notification service.                            |
  > | adam_user_schema.ldif     | LDIF for the user schema.                                                                        |
  > | adam_webauthndevices.ldif | LDIF to support registered devices for the Web Authentication (WebAuthn) authentication service. |

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `odsee_` and `tivoli_` LDIF files are obsolete because Oracle Directory Server Enterprise Edition and Tivoli aren't supported as identity stores. |

---

---
title: Start AM
description: Start the PingAM web application deployed in a web container like Apache Tomcat, and learn how to override bootstrap settings using configuration files or environment variables
component: pingam
version: 8.1
page_id: pingam:installation:startup-openam
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/startup-openam.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install"]
page_aliases: ["install-guide:startup-openam.adoc"]
section_ids:
  startup-openam-dynamic: Override startup settings
  startup-openam-replace-bootstrap: Replace the bootstrap File
  startup-openam-env-vars: Override startup settings using environment variables
  startup-openam-java-properties: Override startup settings using Java properties
---

# Start AM

AM is a web application installed in a web container, such as Apache Tomcat. Starting the web container starts the AM application.

At the beginning of its startup process, AM performs an operation called *bootstrapping*, during which AM obtains startup settings from a bootstrap file in its configuration directory, then uses those settings to initiate its operation. AM creates the bootstrap file, `boot.json`, during installation.

> **Collapse: How is the bootstrap file created?**
>
> The installation or upgrade process creates the file after configuring the instance, provided it can find the AM keystore and its password files in either of the following locations:
>
> * Configure > Server Defaults > Security > Key Store
>
> * Deployment > Servers > *server name* > Security > Key Store
>
> Change the AM default keystore configuration at Server Default level so the environment is homogeneous.

> **Collapse: When is the bootstrap file updated?**
>
> After every successful startup, AM rewrites the bootstrap file using the current information for the AM keystore.
>
> If you change the configuration of the AM keystore, for example, the path to its files, AM will save the changes to the bootstrap file the next time it starts successfully.
>
> This is why, if you want to [override AM's startup settings](#startup-openam-dynamic), you need to replace the bootstrap file manually before AM starts.

## Override startup settings

Users who deploy AM with DevOps tooling, such as Docker and Kubernetes, might want to launch multiple AM instances from a single image, providing startup settings dynamically when AM starts up instead of reading the settings from the bootstrap file created during AM installation.

You can replace the bootstrap file and provide your own static and dynamic startup settings. The following sections describe how to override the bootstrap file created during AM installation:

* [Replace the bootstrap File](#startup-openam-replace-bootstrap) covers how to specify a custom bootstrap file, and describes all the startup settings in the bootstrap file.

* [Override startup settings using environment variables](#startup-openam-env-vars) covers how to dynamically override startup settings in the bootstrap file with environment variables.

* [Override startup settings using Java properties](#startup-openam-java-properties) covers how to dynamically override startup settings in the bootstrap file with Java properties.

### Replace the bootstrap File

AM's bootstrap file is located at the path `/path/to/am/config/boot.json`, where `/path/to/am/config` is the AM configuration directory.

> **Collapse: How is the AM configuration directory specified?**
>
> You specify it during an AM installation, as follows:
>
> * In the Configuration Directory field on the Server Settings page when using the GUI installation. You can find details in [Interactive install](interactive-install.html).
>
> * In the `com.sun.identity.configuration.directory` environment variable when performing an [FBC installation](passive-install-fbc.html).
>
> * In the `BASE_DIR` property when [installing over REST](passive-install-rest.html).
>
> * In the `--cfgDir` option when [installing using Amster](passive-install-amster.html).

To override AM's startup configuration, modify the `boot.json` bootstrap file then overwrite the existing bootstrap file with your modified file *before every AM restart*.

You must overwrite the file each time you start AM because after startup, AM overwrites the bootstrap file with the initial startup settings created during AM installation, removing any modifications you might have made to startup settings in the bootstrap file.

Make changes to supporting files and passwords before changing bootstrap file properties—AM will fail to start up if bootstrap properties don't correspond to actual configuration. For example, if you change the value of the `keyStorePasswordFile` property to a file that doesn't exist, AM won't be able to start up.

> **Collapse: Bootstrap file example, with properties**
>
> ```json
> {
>   "instance": "https://am.example.com:8443/am",
>   "dsameUser": "cn=dsameuser,ou=DSAME Users,ou=am-config",
>   "keystores": {
>     "default": {
>       "keyStorePasswordFile": "/path/to/am/security/secrets/default/.storepass",
>       "keyPasswordFile": "/path/to/am/security/secrets/default/.keypass",
>       "keyStoreType": "JCEKS",
>       "keyStoreFile": "/path/to/am/security/keystores/keystore.jceks"
>     }
>   },
>   "configStoreList": [
>     {
>       "baseDN": "ou=am-config",
>       "dirManagerDN": "uid=am-config,ou=admins,ou=am-config",
>       "ldapHost": "ds.example.com",
>       "ldapPort": 1636,
>       "ldapProtocol": "ldaps"
>     }
>   ]
> }
> ```
>
> **Startup settings in the bootstrap file**
>
> | Property                                 | Description and Derivation                                                                                                                                                                                                                                                                                                                                                                                                                                        |
> | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `instance`                               | AM server URL.Defaults to the Server URL field on the Server Settings page (GUI configurator) or the `SERVER_URL` configuration property (command-line configurator).This property's value is the URL for directly accessing an AM instance, *not* an AM site using a load balancer URL.Do not modify this bootstrap file property. If you need to change the AM instance URL, reinstall AM.                                                                      |
> | `dsameUser`                              | An internal account that AM uses to connect to the configuration store. AM generates the password for this account on startup and you can't read or change it.The first part of the user's DN is always created initially as `cn=dsameuser,ou=DSAME Users`. The second part of the DN defaults to the Root Suffix field on the Configuration Data Store Settings page (GUI configurator) or the `ROOT_SUFFIX` configuration property (command-line configurator). |
> | `keystores.default`                      | The AM keystore. Currently, no other keystores are referenced in the bootstrap file.                                                                                                                                                                                                                                                                                                                                                                              |
> | `keystores.default.keyStorePasswordFile` | Path to the file that contains the password required to open the AM keystore. Always created initially as `/path/to/am/security/secrets/default/.storepass`.When creating a new `.storepass` file, ensure that there are no hidden trailing characters after the password. For example, use the `echo -n` command to add the password to the new file.                                                                                                            |
> | `keystores.default.keyPasswordFile`      | Path to the file that contains the password used to encrypt individual keystore entries. Always created initially as `/path/to/am/security/secrets/default/.keypass`.When creating a new `.keypass` file, ensure that there are no hidden trailing characters after the password. For example, use the `echo -n` command to add the password to the new file.                                                                                                     |
> | `keystores.default.keyStoreType`         | AM keystore type. Currently, the only valid value is `JCEKS`.                                                                                                                                                                                                                                                                                                                                                                                                     |
> | `keystores.default.keyStoreFile`         | Path to the AM keystore. Always created initially as `/path/to/am/security/keystores/keystore.jceks`.The AM keystore is required for startup because it contains the password of the directory manager user of the AM configuration store.                                                                                                                                                                                                                        |
> | `configStoreList[*]`                     | Array of one or more objects that describe AM configuration stores. The initial object in the array is mandatory and defines the primary configuration store. Additional objects are optional and define failover configuration stores.                                                                                                                                                                                                                           |
> | `configStoreList[*].baseDN`              | Root suffix of the AM configuration store.Defaults to the Root Suffix field on the Configuration Data Store Settings page (GUI configurator) or the `ROOT_SUFFIX` configuration property (command-line configurator).                                                                                                                                                                                                                                             |
> | `configStoreList[*].dirManagerDN`        | DN of the configuration store directory manager user.Defaults to `uid=am-config,ou=admins,ou=am-config` (GUI configurator) or the `DS_DIRMGRDN` configuration property (command-line configurator).                                                                                                                                                                                                                                                               |
> | `configStoreList[*].ldapHost`            | fully qualified domain name (FQDN) of the configuration store's host.Defaults to the Host Name field on the Configuration Data Store Settings page (GUI configurator) or the `DIRECTORY_SERVER` configuration property (command-line configurator).                                                                                                                                                                                                               |
> | `configStoreList[*].ldapPort`            | LDAP or LDAPS port number on which to access the configuration store.Defaults to the Port field on the Configuration Data Store Settings page (GUI configurator) or the `DIRECTORY_PORT` configuration property (command-line configurator).                                                                                                                                                                                                                      |
> | `configStoreList[*].ldapProtocol`        | Protocol with which to access the directory service running the configuration store. The value can be `ldap` or `ldaps`.Defaults to the SSL/TLS Enabled field on the Configuration Data Store Settings page (GUI configurator) or the `DIRECTORY_SSL` configuration property (command-line configurator).                                                                                                                                                         |

### Override startup settings using environment variables

You can dynamically override startup settings in the bootstrap file by defining environment variables in the shell that starts AM and referencing the variables in a modified version of the bootstrap file.

Specify JSON properties that reference environment variables in a modified bootstrap file that uses the notation `${env.MY_ENVIRONMENT_VARIABLE}`.

For example, you could dynamically change the AM instance URL as follows:

1. Set an environment variable named `MY_INSTANCE` in the shell that starts AM.

2. Create a modified version of the bootstrap file with the following line:

   ```
   "instance" : "${env.MY_INSTANCE}",
   ```

3. Overwrite the initial bootstrap file with the modified bootstrap file.

4. Start AM.

### Override startup settings using Java properties

You can dynamically override startup settings in the bootstrap file by referencing Java system properties in a modified version of the bootstrap file. You can reference both built-in Java system properties and properties specified with the `-D` option in the web container that runs AM.

Specify JSON properties that reference Java properties in a modified bootstrap file that uses the notation `${MY_JAVA_PROPERTY}`.

For example, you could dynamically change the AM keystore's path to the user's home directory as follows:

1. Create a modified version of the bootstrap file, specifying the default AM keystore as follows:

   ```
   "keystores" : {
       "default" : {
          "keyStorePasswordFile" : "${user.home}/.storepass",
          "keyPasswordFile" : "${user.home}/.keypass",
          "keyStoreType" : "JCEKS",
          "keyStoreFile" : "${user.home}/keystore.jceks"
       }
   },
   ```

2. Overwrite the initial bootstrap file with the modified bootstrap file.

3. Start AM.

---

---
title: Store configuration data in JSON files
description: Configure PingAM to store configuration data in JSON files instead of directory servers, enabling file-based configuration management across deployment layers
component: pingam
version: 8.1
page_id: pingam:installation:fbc
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/fbc.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install", "Configuration Store", "File Based Config", "FBC"]
page_aliases: ["install-guide:fbc.adoc"]
section_ids:
  how-am-reads-FBC: How AM reads FBC
  fbc-and-am-sites: FBC and AM sites
---

# Store configuration data in JSON files

AM can read its configuration from JSON files instead of directory servers. Configuration stored in JSON files is called *file-based configuration* (FBC).

File-based configuration (FBC) is best-suited to a DevOps-style deployment, with the associated tools and practices of that approach.

Static FBC data is written to configuration files in the file system and checked into a source control system, such as Git.

AM instances are created as Docker images, with the FBC incorporated into the image.

![Kubernetes deployment using file-based configuration.](../_images/docker-deployment.png)

You can insert variables into these configuration files before you check them into source control. The variables are substituted with the appropriate values at runtime when you start the Docker container. Using variables lets you reuse the same base configuration files for multiple instances, and different staging environments. For example, development, QA, or pre-production, which are then promoted to production.

In an existing deployment, you can [migrate to FBC](../upgrade/migrate-to-fbc.html) after you've upgraded to AM 8.

If you're setting up an AM deployment from scratch, read [Passive install with FBC](passive-install-fbc.html) to create a file-based configuration store.

## How AM reads FBC

An initial startup with FBC enabled writes configuration files with the following structure:

* noninteractive-install.properties

  You specify a limited set of environment variables on startup. AM writes these environment variables to a configuration properties file, `/path/to/am/config/services/noninteractive-install.properties`, when the server starts.

  The values in the `noninteractive-install.properties` file are used on subsequent startups, *unless you set these properties in the deployment configuration layer*.

* Baseline configuration layer

  The baseline configuration files are read-only and are located under `/path/to/am/baseline/config/services`.

  These files include placeholders that are resolved with values of environment variables. The baseline layer lets you define a configuration that works across different environments, with a few distinct parameters that are specific to each server instance.

  For example, three instances might have the same configuration but different keystore locations and URLs. Those differences are resolved with environment variables at startup.

* Deployment configuration layer

  The deployment configuration files are read/write and are located under `/path/to/am/config/services`.

  Changes made through the AM admin UI and REST API are written to the deployment configuration layer.

  This layer overrides the baseline configuration on a file-by-file basis. In other words, AM reads its configuration from the baseline configuration until you add corresponding files to the deployment configuration layer.

In summary, AM looks for its configuration in the following order:

1. Deployment configuration layer

2. Baseline configuration layer

3. `noninteractive-install.properties`

## FBC and AM sites

A *site* refers to multiple AM servers that share a single configuration store.

When your configuration is stored in files, you don't need to group AM servers into sites because each AM server has its configuration stored locally.

Instead of pointing at a shared configuration store, servers using FBC are exact copies of each other. Each server is assumed to be in its own discrete site, along with its configuration.

The following diagram illustrates the difference between configuration stored in an LDAP store and configuration stored in files on the file system:

![File-based configuration vs LDAP configuration store](_images/FBC-vs-LDAP.png)

If you migrate to FBC from an LDAP configuration store, the migration utility enforces a *single* site and a *single* server instance. If your deployment has more than one server or more than one site, the migration retains the first site and uses this site in the resulting output configuration. If your deployment has no sites configured, a single site is added.

---

---
title: Troubleshoot installations
description: Resolve PingAM installation issues using debug logging and SSL troubleshooting techniques
component: pingam
version: 8.1
page_id: pingam:installation:install-troubleshooting
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/install-troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install", "Troubleshooting"]
page_aliases: ["install-guide:install-troubleshooting.adoc"]
section_ids:
  debug-logging: Debug logging
  ssl-connection-issues: SSL connection issues
---

# Troubleshoot installations

## Debug logging

AM can capture information in debug log files that are useful when troubleshooting AM problems. [Debug logging](../monitoring/debug-logging.html) describes how to enable debug logging after AM has been started.

It's also possible to capture debug logs while installing AM. This can be useful if you need to troubleshoot an installation problem.

Follow these steps to capture debug logs while installing AM on Tomcat:

1. If Tomcat is already started, stop it.

2. Specify the `-Dcom.iplanet.services.debug.level=message` option in the `CATALINA_OPTS` environment variable:

   ```
   $ export CATALINA_OPTS=-Dcom.iplanet.services.debug.level=message
   ```

   There are several ways that you can specify the `CATALINA_OPTS` environment variable. You can set the variable:

   * In the `/path/to/tomcat/bin/setenv.sh` file

   * In the login shell of the user who runs Tomcat

3. Run the AM installation. Debug log files containing troubleshooting information appear in the `/path/to/am/var/debug` directory.

4. When you have completed the AM installation and no longer need to capture debug logs, stop Tomcat, revert the debug logging options, and restart Tomcat.

## SSL connection issues

Connection issues during an AM installation are often caused by certificate or truststore misconfigurations.

> **Collapse: Example connection error**
>
> The following error is seen when AM can't connect to DS during the installation:
>
> ```none
> AMSetupServlet.processRequest: error com.sun.identity.setup.ConfiguratorException: Cannot connect to Directory Server, the error was: Client-Side Timeout
> ```

Perform the following steps to troubleshoot connection issues:

1. Check you can connect to the DS server by running the following `openssl` command with the `hostname:port` of your DS server:

   ```none
   $ openssl s_client -connect ds.example.com:1636 -showcerts
   ```

   The output from this command confirms that you can establish a secure connection to the DS server independent of AM. If you can connect, the command returns the entire certificate chain for DS.

2. Check the AM truststore contains the DS CA certificate by running the following `keytool` command:

   ```none
   $ keytool -list -v -keystore /path/to/truststore -storetype jks -storepass password
   ```

   This command returns the contents of the truststore so you can check it includes the DS CA certificate.

3. Enable SSL debugging on Tomcat by adding the `-Djavax.net.debug=SSL,handshake,trustmanager` JVM option.

   To do this, add the following debug option to the `setenv.sh` file and restart Tomcat:

   ```none
   export CATALINA_OPTS="$CATALINA_OPTS -Djavax.net.debug=ssl,handshake,trustmanager"
   ```

   The SSL debug logs are written to `catalina.out`. They provide detailed information about the SSL handshake process to help you identify where the issue is occurring.

   Learn more about this option in [Debugging Utilities](https://docs.oracle.com/en/java/javase/25/security/java-secure-socket-extension-jsse-reference-guide.html#GUID-31B7E142-B874-46E9-8DD0-4E18EC0EB2CF) in the Java documentation.

4. When you have completed the AM installation and no longer need to capture SSL debug logs, stop Tomcat, revert the SSL debugging option, and restart Tomcat.

---

---
title: Tune the underlying datastores
description: Tune PingDS instances to handle multiple client connections and optimize performance in your PingAM environment
component: pingam
version: 8.1
page_id: pingam:installation:tune-ds
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/tune-ds.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install", "Performance", "Scaling"]
page_aliases: ["prerequisites-file-descriptors.adoc", "install-guide:tune-ds.adoc"]
---

# Tune the underlying datastores

AM is not file-descriptor intensive, but you may need to tune each DS instance in your environment to handle multiple client connections.

Learn more about tuning DS in the [DS performance tuning](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/tuning.html) documentation.

---

---
title: Uninstall AM
description: Remove PingAM software from your deployment, including configuration files, directory server data, and web application files
component: pingam
version: 8.1
page_id: pingam:installation:removing-instances
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/removing-instances.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install"]
page_aliases: ["install-guide:removing-instances.adoc"]
---

# Uninstall AM

This page describes how to remove AM software.

To remove a single server from a multi-server deployment, select Deployment > Servers > *server name* then click [icon: ellipsis-v, set=fas]and [icon: times, set=fas]Delete.

You can find instructions on removing agents in the [Web Agents Installation Guide](https://docs.pingidentity.com/web-agents/2025.3/installation-guide/uninstallation.html) and the [Java Agents Installation Guide](https://docs.pingidentity.com/java-agents/2025.3/installation-guide/uninstallation.html).

After you have deployed and configured AM, you might have as many as four locations where AM files are stored on your system.

The following steps remove the AM software. After removing all the software, remove the AM configuration data.

1. Shut down the web application container where you deployed AM.

   ```bash
   $ /etc/init.d/tomcat stop
   Password:
   Using CATALINA_BASE:   /path/to/tomcat
   Using CATALINA_HOME:   /path/to/tomcat
   Using CATALINA_TMPDIR: /path/to/tomcat/temp
   Using JRE_HOME:        /path/to/jdk/jre
   Using CLASSPATH:       /path/to/tomcat/bin/bootstrap.jar:
    /path/to/tomcat/bin/tomcat-juli.jar
   ```

1) Unconfigure AM by removing the configuration files in the $HOME directory of the user running the web application container.

   For example:

   ```bash
   $ rm -rf $HOME/am $HOME/.openamcfg
   ```

   To uninstall AM and its associated configuration files, delete the following directories:

   * *The configuration directory*.

     If you didn't use the default configuration location (`$HOME/am`), check the value of the `Base installation directory` property under Deployment > Servers > *server name* > General > System.

   * *The hidden directory that holds a file pointing to the configuration directory*.

     For example, if you are using Apache Tomcat as the web container, this file could be `$HOME/.openamcfg/AMConfig_path_to_tomcat_webapps_am_`.

2) Remove the configuration manually from your directory server. The default base DN for AM configuration data is `ou=am-config`.

   |   |                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | At this point, you can restart the web container and reconfigure AM if you only want to start over with a clean configuration rather than removing AM completely. |

3) Undeploy the AM web application.

   For example, if you are using Apache Tomcat as the web container, remove the `.war` file and expanded web application from the container:

   ```bash
   $ cd /path/to/tomcat/webapps/
   $ rm -rf am.war am/
   ```

---

---
title: Use stronger encryption algorithms
description: Configure PingAM to use AES Key Wrap encryption with PBKDF2 and HMAC-SHA1 for stronger password and key protection during installation
component: pingam
version: 8.1
page_id: pingam:installation:prepare-aeswrap
canonical_url: https://docs.pingidentity.com/pingam/8.1/installation/prepare-aeswrap.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["Install", "Security"]
page_aliases: ["install-guide:prepare-aeswrap.adoc"]
section_ids:
  configure-aeswrap-tomcat: Configure AES Key Wrap encryption for Tomcat
---

# Use stronger encryption algorithms

AM encrypts and decrypts system passwords and the keys used in the configuration, and by components such as agents. The default encryption algorithm is Java Cryptography Extension (JCE) [PBEWithMD5AndDES](https://docs.oracle.com/en/java/javase/25/docs/specs/security/standard-names.html#algorithmparameters-algorithms).

If you need a more secure encryption algorithm, use the Advanced Encryption Standard (AES) Key Wrap algorithm ([RFC3394](https://www.rfc-editor.org/info/rfc3394)). AM's implementation of AES Key Wrap uses the Password-Based Key Derivation Function 2 (PBKDF2) ([RFC2898](https://www.rfc-editor.org/info/rfc2898)) with HMAC-SHA1. This lets you choose key size hash algorithms, such as SHA256, SHA384, or SHA512.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The AES Key Wrap encryption algorithm is only enabled when installing AM. There is no current upgrade path for existing installations.AES key wrap is a symmetric encryption method, which means the same key is used for encrypting and decrypting. Make sure you use the same secret (secret label: `am.global.services.session.clientbased.encryption.AES`) on all AM instances to allow any AM instance to decrypt the encrypted passwords and keys. |

## Configure AES Key Wrap encryption for Tomcat

Edit your container startup scripts, for example `setenv.sh`, to set the following JVM system properties in Tomcat:

```none
JAVA_OPTS="$JAVA_OPTS -Dcom.iplanet.security.encryptor=org.forgerock.openam.shared.security.crypto.AESWrapEncryption"  1
JAVA_OPTS="$JAVA_OPTS -Dorg.forgerock.openam.encryption.key.iterations=10000"                                          2
JAVA_OPTS="$JAVA_OPTS -Dorg.forgerock.openam.encryption.useextractandexpand=true"                                      3
JAVA_OPTS="$JAVA_OPTS -Dorg.forgerock.openam.encryption.key.size=256"                                                  4
JAVA_OPTS="$JAVA_OPTS -Dorg.forgerock.openam.encryption.key.digest=SHA512"                                             5
```

1 Enables use of AES Key Wrap encryption.

2 Specifies the iteration count of the encryption key. Large iteration counts, for example, of 20,000, slow down brute-force attacks when passwords are of low quality (less than 20 characters and easy to predict). AM does not have an iteration count requirement. However, it will log a warning if both of the following conditions are true: - The number of iterations is less than 10,000. - The AM encryption key is less than 20 characters long.

3 Enables the algorithm to reduce the performance cost of AES Key Wrap encryption even when high-iteration counts are used. If this property is unset, and you configured a large iteration count, AM startup times may see a performance impact if there are many agents in your deployment. Determine the optimal iteration count based on the security and performance requirements of your deployment.

4 Specifies the size of the encryption key. Configure the key size to meet the needs of your deployment.

5 Specifies the digest algorithm. Possible values are `SHA1`, `SHA256`, `SHA384`, or `SHA512`. Configure the digest algorithm to meet the needs of your deployment.

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | You can't change these configuration parameters once AM has been installed. |
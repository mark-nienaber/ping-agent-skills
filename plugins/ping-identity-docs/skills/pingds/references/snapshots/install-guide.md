---
title: File layout
description: Reference for the files and directories that PingDS creates when you install and run the server.
component: pingds
version: 8.1
page_id: pingds:install-guide:file-layout
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/file-layout.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Install", "LDAP"]
---

# File layout

DS software installs and creates the following files and directories. The following table is not meant to be exhaustive.

| File or directory                       | Description                                                                                                                                                                                                                                                                   |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bak`                                   | Directory intended for local backup data.                                                                                                                                                                                                                                     |
| `bat`                                   | Windows command-line tools.                                                                                                                                                                                                                                                   |
| `bin`                                   | Linux command-line tools.                                                                                                                                                                                                                                                     |
| `changelogDb`                           | Backend for replication changelog data.                                                                                                                                                                                                                                       |
| `classes`                               | Directory added to the server classpath, permitting individual classes to be patched.                                                                                                                                                                                         |
| `config`                                | (Optionally) immutable server configuration files.                                                                                                                                                                                                                            |
| `config/audit-handlers`                 | Templates for configuring external Common Audit event handlers.                                                                                                                                                                                                               |
| `config/config.ldif`                    | LDIF representation of current DS server configuration.                                                                                                                                                                                                                       |
| `config/keystore` `config/keystore.pin` | Keystore and password (`.pin`) files for servers using PKI based on a deployment ID and password.                                                                                                                                                                             |
| `config/MakeLDIF`                       | Templates for use with the `makeldif` LDIF generation tool.                                                                                                                                                                                                                   |
| `db`                                    | Default directory for backend database files.For details, refer to [Data storage](../config-guide/import-export.html).                                                                                                                                                        |
| `extlib`                                | Directory for additional .jar files used by your custom plugins.If the instance path is not the same as the binaries, copy additional files into the `instance-path/extlib/` directory.                                                                                       |
| `import-tmp`                            | Working directory used when importing LDIF data.                                                                                                                                                                                                                              |
| `ldif`                                  | Directory for saving LDIF export files.                                                                                                                                                                                                                                       |
| `legal-notices`                         | License information.                                                                                                                                                                                                                                                          |
| `lib`                                   | Scripts and libraries shipped with DS servers.                                                                                                                                                                                                                                |
| `lib/extensions`                        | Directory for custom plugins.                                                                                                                                                                                                                                                 |
| `locks`                                 | Lock files that prevent more than one process from using the same backend.                                                                                                                                                                                                    |
| `logs`                                  | Access, errors, and audit logs.                                                                                                                                                                                                                                               |
| `logs/server.pid`                       | Contains the process ID for a running server.                                                                                                                                                                                                                                 |
| `README`                                | About DS servers.                                                                                                                                                                                                                                                             |
| `samples`(1)                            | Samples for use with DS servers, such as:- A sample `Dockerfile` and related files for building custom DS Docker images.

- A sample Grafana dashboard demonstrating how to graph DS server metrics stored in a Prometheus database.

- Sample server plugins and extensions. |
| `setup`                                 | Linux setup tool.                                                                                                                                                                                                                                                             |
| `setup.bat`                             | Windows setup tool.                                                                                                                                                                                                                                                           |
| `template`                              | Templates for setting up a server instance.                                                                                                                                                                                                                                   |
| `template/setup-profiles`               | Profile scripts to configure directory servers for specific use cases.                                                                                                                                                                                                        |
| `upgrade`                               | Linux upgrade tool.                                                                                                                                                                                                                                                           |
| `upgrade.bat`                           | Windows upgrade tool.                                                                                                                                                                                                                                                         |
| `var`                                   | Files the DS server writes to during operation.Do not modify or move files in the `var` directory.                                                                                                                                                                            |
| `var/archived-configs`                  | Snapshots of the main server configuration file, `config/config.ldif`.The server writes a compressed snapshot file when the configuration is changed.                                                                                                                         |
| `var/config.ldif.startok`               | The most recent version of the main server configuration file that the server successfully started with.                                                                                                                                                                      |

(1) The samples are provided on an "as is" basis. Ping Identity does not guarantee the individual success developers may have in implementing the samples on their development platforms or in production configurations.

For details about how to try the samples, refer to the accompanying `README.md` files.

---

---
title: FIPS 140–3 compliance
description: Configure PingDS to use the Bouncy Castle FIPS libraries to achieve FIPS 140-3 compliance.
component: pingds
version: 8.1
page_id: pingds:install-guide:fips
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/fips.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-12T08:58:52Z
keywords: ["Bouncy Castle FIPS", "LDAP", "Security", "Setup &amp; Configuration"]
section_ids:
  download-bouncy-castle-libraries: Download the Bouncy Castle libraries
  set-up-server-before-bouncy-castle: Set up DS
  configure-server-bouncy-castle: Configure DS to use Bouncy Castle FIPS support
  create_key_providers: Create key providers
  use_the_new_key_providers: Use the new key providers
  disable_the_default_key_providers: Disable the default key providers
  share_keys_across_crypto_managers: Share keys across Crypto Managers
  enable-bouncy-castle: Enable the Bouncy Castle FIPS provider
  start-ds-bouncy-castle: Start DS
  command-support-bouncy-castle: Command support for Bouncy Castle FIPS
---

# FIPS 140–3 compliance

To achieve [FIPS 140–3](https://csrc.nist.gov/publications/detail/fips/140/3/final) compliance, configure the [Bouncy Castle FIPS libraries](https://www.bouncycastle.org/fips-java/) with DS. This enables the use of the Bouncy Castle FIPS keystore and security provider in FIPS-approved mode.

Bouncy Castle FIPS is useful when dealing with government data, where meeting the FIPS 140–3 security requirements is necessary for regulatory compliance. Bouncy Castle FIPS doesn't require use of an HSM through a PKCS#11 interface.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Bouncy Castle FIPS is less performant than other keystores. The destroyable keys can't be cached and must be read from the keystore with every use. |

To configure DS to use Bouncy Castle FIPS:

1. [Download the Bouncy Castle libraries](#download-bouncy-castle-libraries).

2. [Set up DS](#set-up-server-before-bouncy-castle).

3. [Configure DS to use Bouncy Castle FIPS support](#configure-server-bouncy-castle).

4. [Enable the Bouncy Castle FIPS provider](#enable-bouncy-castle).

5. [Start DS](#start-ds-bouncy-castle).

For information on running DS commands after configuring Bouncy Castle FIPS, read [Command support for Bouncy Castle FIPS](#command-support-bouncy-castle).

## Download the Bouncy Castle libraries

Before you begin, download the [Bouncy Castle FIPS libraries](https://www.bouncycastle.org/fips-java/):

| File                            | Description                                         | Tested version          |
| ------------------------------- | --------------------------------------------------- | ----------------------- |
| `bc-fips-latestVersion.jar`     | Bouncy Castle FIPS security provider implementation | `bc-fips-2.0.0.jar`     |
| `bcpkix-fips-latestVersion.jar` | Certificate generation support                      | `bcpkix-fips-2.0.7.jar` |
| `bctls-fips-latestVersion.jar`  | TLS support                                         | `bctls-fips-2.0.19.jar` |
| `bcutil-fips-latestVersion.jar` | ASN.1 Utility Classes                               | `bcutil-fips-2.0.3.jar` |

## Set up DS

Set up *but don't start* DS before you enable the Bouncy Castle FIPS provider in the JVM.

1. Set up DS for your use case and omit the `--start` option.

   The following example command uses the evaluation setup profile but doesn't start the server:

   ```console
   $ ./opendj/setup \
    --serverId evaluation-only \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword StrongPassword \
    --monitorUserPassword StrongPassword \
    --hostname localhost \
    --adminConnectorPort 4444 \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --replicationPort 8989 \
    --bootstrapReplicationServer localhost:8989 \
    --profile ds-evaluation \
    --acceptLicense
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | As in the example command, make sure passwords used to connect are at least 14 characters (14 bytes) long. If the passwords are too short, commands display the following error message:```
   Other: password must be at least 112 bits
   ```This example uses deployment ID-based PKI. For most FIPS-compliant deployments, [use your own cryptographic keys](setup-own-keys.html). |

2. Copy the Bouncy Castle libraries you downloaded to the DS `extlib` folder:

   ```console
   $ ~/Downloads/bc*jar opendj/extlib/
   ```

3. Create a Bouncy Castle FIPS format keystore from the DS default keystore:

   ```console
   $ keytool \
   -importkeystore \
   -srckeystore opendj/config/keystore \
   -srcstoretype PKCS12 \
   -srcstorepass:file opendj/config/keystore.pin \
   -destkeystore opendj/config/keystore.bcfks \
   -deststoretype BCFKS \
   -deststorepass:file opendj/config/keystore.pin \
   -providerpath opendj/extlib/bc-fips-2.0.0.jar \
   -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
   -noprompt
   ```

   The new keystore holds the same keys created at setup time.

4. (Optional) Perform other offline configuration required before starting DS.

   This step depends on the deployment. For the evaluation profile, there's nothing to do.

## Configure DS to use Bouncy Castle FIPS support

Before you start DS, configure the server offline to use the Bouncy Castle FIPS format keystore.

### Create key providers

Create key providers for the Bouncy Castle FIPS format keystore.

1. Create a key manager provider:

   ```console
   $ ./opendj/bin/dsconfig \
   create-key-manager-provider \
   --provider-name BCFIPS \
   --type file-based \
   --set enabled:true \
   --set key-store-file:/path/to/opendj/config/keystore.bcfks \
   --set "key-store-pin:&{file:config/keystore.pin}" \
   --set key-store-type:BCFKS \
   --offline \
   --no-prompt
   ```

   Here, /path/to/opendj is the path to the folder where you installed DS.

2. Create a trust manager provider:

   ```console
   $ ./opendj/bin/dsconfig \
   create-trust-manager-provider \
   --provider-name BCFIPS \
   --type file-based \
   --set enabled:true \
   --set trust-store-file:/path/to/opendj/config/keystore.bcfks \
   --set "trust-store-pin:&{file:config/keystore.pin}" \
   --set trust-store-type:BCFKS \
   --offline \
   --no-prompt
   ```

   Here, /path/to/opendj is the path to the folder where you installed DS.

### Use the new key providers

1. Update DS connection handlers to use the new key providers.

   The following commands correspond to the connection handlers created by the example `setup` command in [Set up DS](#set-up-server-before-bouncy-castle). If DS uses other connection handlers in your deployment, update them as well.

   1. Update the LDAP connection handler:

      ```console
      $ ./opendj/bin/dsconfig \
      set-connection-handler-prop \
      --handler-name LDAP \
      --set key-manager-provider:BCFIPS \
      --set trust-manager-provider:BCFIPS \
      --offline \
      --no-prompt
      ```

   2. Update the LDAPS connection handler:

      ```console
      $ ./opendj/bin/dsconfig \
      set-connection-handler-prop \
      --handler-name LDAPS \
      --set key-manager-provider:BCFIPS \
      --set trust-manager-provider:BCFIPS \
      --offline \
      --no-prompt
      ```

   3. Update the HTTPS connection handler:

      ```console
      $ ./opendj/bin/dsconfig \
      set-connection-handler-prop \
      --handler-name HTTPS \
      --set key-manager-provider:BCFIPS \
      --set trust-manager-provider:BCFIPS \
      --offline \
      --no-prompt
      ```

2. Update the administration connector to use the new key providers:

   ```console
   $ ./opendj/bin/dsconfig \
   set-administration-connector-prop \
   --set key-manager-provider:BCFIPS \
   --set trust-manager-provider:BCFIPS \
   --offline \
   --no-prompt
   ```

3. Update the replication provider to use the new key providers:

   ```console
   $ ./opendj/bin/dsconfig \
   set-synchronization-provider-prop \
   --provider-name "Multimaster Synchronization" \
   --set key-manager-provider:BCFIPS \
   --set trust-manager-provider:BCFIPS \
   --offline \
   --no-prompt
   ```

### Disable the default key providers

The default key providers don't support FIPS compliance and aren't used any longer. Disable them:

1. Disable the default key manager provider:

   ```console
   $ ./opendj/bin/dsconfig \
   set-key-manager-provider-prop \
   --provider-name PKCS12 \
   --set enabled:false \
   --offline \
   --no-prompt
   ```

2. Disable the default trust manager provider:

   ```console
   $ ./opendj/bin/dsconfig \
   set-trust-manager-provider-prop \
   --provider-name PKCS12 \
   --set enabled:false \
   --offline \
   --no-prompt
   ```

### Share keys across Crypto Managers

In many deployments, the [master key](../security-guide/pki.html#about-deployment-ids), derived from the deployment ID, does both key wrapping and backup signing.

FIPS compliance requires separate keys for these operations.

The DS Crypto Manager configuration points to the keys for these operations. Each server's Crypto Manager must use the same keys for key wrapping and signing across the entire deployment. This ensures any server can unwrap keys and verify signed backup files.

To use separate keys for key wrapping and for signing backups, follow these steps once for the entire deployment to prepare a shared keystore:

1. In the shared keystore, generate separate key pairs for key wrapping and for signing backups.

   When using a file-based shared keystore, use the Bouncy Castle FIPS format (BCFKS type).

   Record the key pair aliases for use in the Crypto Manager configuration.

For each server in the deployment:

1. Share the keystore with the server.

   When using a file-based shared keystore, copy it to the DS `config` folder.

2. Create a key manager provider to access the shared keystore.

3. Update the DS Crypto Manager configuration to set the provider, key wrapping mode, and key aliases:

   ```console
   $ ./opendj/bin/dsconfig \
   set-crypto-manager-prop \
   --set key-manager-provider:<crypto-manager-key-manager-provider> \
   --set key-wrapping-mode:wrap \
   --set master-key-alias:<key-wrapping-key-alias> \
   --set signing-key-alias:<signing-key-alias> \
   --offline \
   --no-prompt
   ```

When rotating keys in the shared keystore:

* Add new keys but don't delete the existing keys.

  Keep the existing keys in the keystore so DS can use them to unwrap keys and verify signed backup files.

* Overwrite the old copies of the shared keystore on all servers.

* Update the Crypto Manager `master-key-alias` and `signing-key-alias` properties as necessary to target the new keys.

## Enable the Bouncy Castle FIPS provider

Before you start DS, update the DS Java settings to use Bouncy Castle FIPS support:

1. Copy `$JAVA_HOME/conf/security/java.security` to the `opendj/config/` folder.

2. Update the `opendj/config/java.security` file to use the Bouncy Castle FIPS provider:

   1. Replace the list of security providers with the following:

      ```properties
      security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
      # If entropy in the system is too limited to use the default
      # deterministic random bits generator, try with C:HYBRID;ENABLE{All};
      #security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider C:HYBRID;ENABLE{All};
      security.provider.2=org.bouncycastle.jsse.provider.BouncyCastleJsseProvider fips:BCFIPS
      security.provider.3=SUN
      ```

   2. Update the default key manager factory algorithm:

      ```properties
      ssl.KeyManagerFactory.algorithm=PKIX
      ```

3. Update the DS `opendj/config/java.properties` file to use the Bouncy Castle FIPS provider.

   Add the following flags to all server tools settings. Put all the flags on the same line each time. The following example shows one flag per line for readability:

   ```properties
   -Dorg.bouncycastle.fips.approved_only=true
   -Djava.security.properties==/path/to/opendj/config/java.security
   ```

   Here, /path/to/opendj is the path to the folder where you installed DS.

   The following example shows an updated `/path/to/opendj/config/java.properties` file:

   ```properties
   default.java-home=$JAVA_HOME
   # Default for client tools (make it the default because we are more likely to add client tools than server tools)
   default.java-args=-server -Xms256m -Xmx256m
   # Server tools need a bigger heap: opt-out of client tools heap sizing
   addrate.java-args=-server
   authrate.java-args=-server
   backendstat.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   changelogstat.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   dsbackup.online.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   dsbackup.offline.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   dsrepl-offline.java-args=-server
   dsrepl.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   encode-password.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   export-ldif.offline.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   import-ldif.offline.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   ldifdiff.java-args=-server
   makeldif.java-args=-server
   modrate.java-args=-server
   rebuild-index.offline.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   searchrate.java-args=-server
   setup-profile.java-args=-server
   start-ds.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   upgrade.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   verify-index.java-args=-server -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties==/path/to/opendj/config/security/java.security
   ```

## Start DS

1. Start DS:

   ```console
   $ ./opendj/bin/start-ds
   ```

   When DS finishes starting up, it displays a message containing:

   ```
   The Directory Server has started successfully
   ```

2. Verify you can run administrative tools, such as the `status` command:

   ```console
   $ ./opendj/bin/status \
   --bindDn uid=admin \
   --bindPassword StrongPassword \
   --hostname localhost \
   --port 4444
   ```

   As you haven't specified a truststore, the command prompts you to trust the server certificate.

   On success, the `status` command displays output about the DS server.

|   |                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When running DS with Bouncy Castle FIPS, use the Java `keytool` command or other external command to manage keys.The `dskeymgr` command doesn't support Bouncy Castle FIPS format keystores or providers, so you can't use it to create or renew TLS key pairs or to create and replace deployment IDs.For most FIPS-compliant deployments, [use your own cryptographic keys](setup-own-keys.html). |

## Command support for Bouncy Castle FIPS

When running online server commands, use these arguments:

```console
--trustStorePath /path/to/opendj/config/security/keystore.bcfks \
--trustStoreType BCFKS \
--trustStorePassword:file /path/to/opendj/config/keystore.pin \
--trustStoreProviderClass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
```

When running server commands with the `--offline` option, the `java.properties` settings suffice.

---

---
title: Install a directory proxy
description: Install and configure a PingDS directory proxy server that forwards LDAP requests to remote directory servers using proxied authorization.
component: pingds
version: 8.1
page_id: pingds:install-guide:setup-proxy
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/setup-proxy.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Install", "LDAP", "Setup &amp; Configuration"]
section_ids:
  proxy-support: Check compatibility
  test-proxy: Try DS directory proxy
  proxy-account: Create a service account
  setup-server-proxy: Set up a directory proxy
  setup-proxy-ds: Proxy to DS servers
  setup-proxy-others: Proxy to non-DS servers
  setup-proxy-access-control: Configure access control
  default_global_policies: Default global policies
  proxy-schema: Align LDAP schema
  proxy-troubleshooting: Troubleshooting
---

# Install a directory proxy

Directory proxy servers forward LDAP requests for user data to remote directory servers. Proxy servers make it possible to provide a single point of access to a directory service, and to hide implementation details from client applications.

## Check compatibility

DS proxy servers connect to remote LDAP directory servers using proxied authorization. The proxied authorization control (object identifier (OID) *(tooltip: \<div class="paragraph">
\<p>A hierarchical string of digits and dots to uniquely identify an object.\</p>
\</div>)*: `2.16.840.1.113730.3.4.18`) is defined by [RFC 4370](https://www.rfc-editor.org/info/rfc4370) *Lightweight Directory Access Protocol (LDAP) Proxied Authorization Control*. If the LDAP directory server does not support proxied authorization, *it cannot be used with DS directory proxy server*.

The following list of LDAP servers *do not support* proxied authorization, and so, do not work with DS directory proxy server:

* Microsoft Active Directory

* Oracle Internet Directory

The following list of LDAP servers support proxied authorization according to their documentation. Ping Identity does not test all servers listed:

* PingDS

* PingDirectory

* ApacheDS

* NetIQ eDirectory

* OpenDJ

* OpenLDAP

* Oracle Directory Server Enterprise Edition

* Red Hat Directory Server

If your LDAP server does not appear in the lists above, check its documentation regarding support for proxied authorization. Alternatively, check the list of `supportedControl` values on the server's root DSE.

## Try DS directory proxy

Before installing DS directory proxy server in production, or with a non-DS directory server, try it on your computer.

![Configuration with proxy and directory servers](../_images/test-proxy.png)Figure 1. Proxy Configuration

The following examples demonstrate DS directory proxy server forwarding LDAP requests to two DS replicas on your computer. This demonstration includes the following high-level tasks:

* Install two DS directory server replicas as proxied servers.

* Set up the DS directory proxy server to forward requests to the DS directory servers.

* Send LDAP requests to the DS directory proxy server, and observe the results.

The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The DS directory proxy server does not have backup files or directory data to encrypt and decrypt. But it does open secure connections to the remote directory servers, and so must trust the certificates that the remote directory servers present to negotiate TLS.By default, DS deployments use TLS keys and a CA generated from the deployment ID and deployment ID password. This is the same deployment ID and password used to configure the DS directory servers. Therefore, use the same deployment ID and password when configuring DS directory proxy servers, so they can trust the directory server certificates. |

Install two DS directory server replicas with the evaluation and proxied server profiles:

```shell
# Unpack server files:
unzip -q ~/Downloads/DS-8.1.1.zip -d /tmp

# Copy server files before setting up each replica:
mkdir /path/to/opendj && cp -r /tmp/opendj/* /path/to/opendj
mkdir /path/to/replica && cp -r /tmp/opendj/* /path/to/replica

# Set up the servers as replicas of each other
# with StartTLS support for the proxy connections:
/path/to/opendj/setup \
  --deploymentId $DEPLOYMENT_ID \
  --deploymentIdPassword password \
  --hostname localhost \
  --ldapPort 11389 \
  --enableStartTls \
  --ldapsPort 11636 \
  --adminConnectorPort 14444 \
  --rootUserDN uid=admin \
  --rootUserPassword password \
  --profile ds-evaluation \
  --profile ds-proxied-server \
  --set ds-proxied-server/baseDn:dc=example,dc=com \
  --replicationPort 18989 \
  --bootstrapReplicationServer localhost:28989 \
  --acceptLicense \
  --start \
  --quiet

/path/to/replica/setup \
  --deploymentId $DEPLOYMENT_ID \
  --deploymentIdPassword password \
  --hostname localhost \
  --ldapPort 21389 \
  --enableStartTls \
  --ldapsPort 21636 \
  --adminConnectorPort 24444 \
  --rootUserDN uid=admin \
  --rootUserPassword password \
  --profile ds-evaluation \
  --profile ds-proxied-server \
  --set ds-proxied-server/baseDn:dc=example,dc=com \
  --replicationPort 28989 \
  --bootstrapReplicationServer localhost:18989 \
  --acceptLicense \
  --start \
  --quiet

# Update PATH to include DS tools:
export PATH=/path/to/opendj/bin:${PATH}
```

Notice that the examples apply two setup profiles to each replica:

* The DS evaluation setup profile adds sample Example.com data.

  For details, refer to [Install DS for evaluation](setup-ds.html).

* The DS proxied server setup profile adds a service account for the proxy server, and sets ACIs *(tooltip: \<div class="paragraph">
  \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
  \</div>)* to grant the account permission to use proxied authorization. The proxy authenticates to the directory servers with its certificate, whose subject DN is `CN=DS, O=PingIdentity.com`.

  For details, refer to [Install DS for use with DS proxy](profile-ds-proxied-server.html).

Set up a directory proxy server to forward requests to the replicas:

```shell
# Copy server files before setting up the proxy:
mkdir /path/to/proxy && cp -r /tmp/opendj/* /path/to/proxy

# Set up the proxy server to access the replicas:
/path/to/proxy/setup \
 --serverId proxy \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --rootUserDN uid=admin \
 --rootUserPassword password \
 --hostname localhost \
 --ldapPort 1389 \
 --enableStartTls \
 --ldapsPort 1636 \
 --adminConnectorPort 4444 \
 --profile ds-proxy-server \
 --set ds-proxy-server/bootstrapReplicationServer:"localhost:14444" \
 --set ds-proxy-server/bootstrapReplicationServer:"localhost:24444" \
 --set ds-proxy-server/rsConnectionSecurity:start-tls \
 --set ds-proxy-server/certNickname:ssl-key-pair \
 --set ds-proxy-server/keyManagerProvider:PKCS12 \
 --set ds-proxy-server/trustManagerProvider:PKCS12 \
 --start \
 --acceptLicense

# Grant access to data through the proxy server:
dsconfig \
 create-global-access-control-policy \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --policy-name "Authenticated access to example.com data" \
 --set authentication-required:true \
 --set request-target-dn-equal-to:"dc=example,dc=com" \
 --set request-target-dn-equal-to:"**,dc=example,dc=com" \
 --set permission:read \
 --set permission:write \
 --set allowed-attribute:"*" \
 --set allowed-attribute:isMemberOf \
 --set allowed-attribute-exception:authPassword \
 --set allowed-attribute-exception:userPassword \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

As you set up only DS servers which all use the same default schema, there is no need to manually align the proxy LDAP schema with the directory server schema.

Send LDAP requests to the DS directory proxy server, and observe the results.

The following example searches the directory through the proxy:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN "ou=people,dc=example,dc=com" \
 "(|(cn=Babs Jensen)(cn=Sam Carter))" \
 cn
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
>
> dn: uid=scarter,ou=People,dc=example,dc=com
> cn: Sam Carter
> ```

The following example modifies directory data through the proxy:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=people,dc=example,dc=com \
 --bindPassword hifalutin << EOF
dn: uid=bjensen,ou=People,dc=example,dc=com
changetype: modify
replace: description
description: Modified by Babs Jensen
EOF
```

> **Collapse: Show output**
>
> ```
> # MODIFY operation successful for DN uid=bjensen,ou=People,dc=example,dc=com
> ```

Notice that the bind DNs and passwords are those of the users in the remote directory service.

For more background on each high-level task, read the rest of this page.

## Create a service account

When preparing to use DS directory proxy servers with directory servers that are not DS servers, create a service account for the proxy to connect to the non-DS remote directory service.

The directory proxy server binds with this service account, and then forwards LDAP requests on behalf of other users.

For DS directory servers, use the proxied server setup profile if possible. For details, refer to [Install DS for use with DS proxy](profile-ds-proxied-server.html).

The service account must have the following on all remote directory servers:

* The same bind credentials.

  If possible, use mutual TLS to authenticate the proxy user with the backend servers.

* The right to perform proxied authorization.

  Make sure the LDAP servers support proxied authorization (control OID: `2.16.840.1.113730.3.4.18`).

  For details, refer to [RFC 4370](https://www.rfc-editor.org/info/rfc4370), *Lightweight Directory Access Protocol (LDAP) Proxied Authorization Control*.

* When using a replication discovery mechanism with remote DS directory servers, the service account requires the `config-read` and `monitor-read` privileges for the service discovery mechanism. It requires the `proxied-auth` privilege and an ACI *(tooltip: \<div class="paragraph">
  \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
  \</div>)* to perform proxied authorization.

The following listing shows an example service account that you could use with DS replicas. Adapt the account as necessary for your directory service:

```ldif
dn: uid=proxy
objectClass: top
objectClass: account
objectClass: ds-certificate-user
uid: proxy
ds-certificate-subject-dn: CN=DS, O=PingIdentity.com
ds-privilege-name: config-read
ds-privilege-name: monitor-read
ds-privilege-name: proxied-auth
aci: (targetcontrol="ProxiedAuth")
  (version 3.0; acl "Allow proxied authorization";
  allow(read) userdn="ldap:///uid=proxy";)
```

## Set up a directory proxy

The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

### Proxy to DS servers

1. Before proceeding, install the server files.\
   For details, refer to [Unpack files](install-files.html).

2. Run the `setup --profile ds-proxy-server` command.

   The command is located where you installed the files, `/path/to/opendj/setup`:

   The following example sets up a directory proxy server that discovers remote servers based on the DS replication topology. It works with replicas set up using the `ds-proxied-server` setup profile.

   This feature works only with DS servers. If the remote LDAP servers in your deployment are not DS servers, refer to [Proxy to non-DS servers](#setup-proxy-others).

   This proxy forwards all requests to public naming contexts of remote servers. Generally, this means requests targeting user data, as opposed to the proxy's configuration, schema, or monitoring statistics:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword str0ngAdm1nPa55word \
    --hostname ds.example.com \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --adminConnectorPort 4444 \
    --profile ds-proxy-server \
    --set ds-proxy-server/bootstrapReplicationServer:"rs.example.com:4444" \
    --set ds-proxy-server/rsConnectionSecurity:start-tls \
    --set ds-proxy-server/certNickname:ssl-key-pair \
    --set ds-proxy-server/keyManagerProvider:PKCS12 \
    --set ds-proxy-server/trustManagerProvider:PKCS12 \
    --start \
    --acceptLicense
   ```

   This example uses mutual TLS with a certificate generated with a deployment ID and password. Adjust the security settings as required for your deployment.

### Proxy to non-DS servers

1. Before proceeding, install the server files.\
   For details, refer to [Unpack files](install-files.html).

2. Run the `setup --profile ds-proxy-server` command.

   The command is located where you installed the files, `/path/to/opendj/setup`:

   The following example sets up a directory proxy server that has a static list of remote servers to connect to. It forwards only requests targeting `dc=example,dc=com`.

   1. Configure the server with a fake replication service discovery mechanism:

      ```console
      $ /path/to/opendj/setup \
       --deploymentId $DEPLOYMENT_ID \
       --deploymentIdPassword password \
       --rootUserDN uid=admin \
       --rootUserPassword str0ngAdm1nPa55word \
       --hostname ds.example.com \
       --ldapPort 1389 \
       --enableStartTls \
       --ldapsPort 1636 \
       --adminConnectorPort 4444 \
       --profile ds-proxy-server \
       --set ds-proxy-server/bootstrapReplicationServer:"fake-rs.example.com:4444" \
       --set ds-proxy-server/rsConnectionSecurity:start-tls \
       --start \
       --acceptLicense
      ```

   2. Create a static service discovery mechanism:

      ```console
      $ dsconfig \
       create-service-discovery-mechanism \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword str0ngAdm1nPa55word \
       --mechanism-name "Static Service Discovery Mechanism" \
       --type static \
       --set primary-server:local1.example.com:636 \
       --set primary-server:local2.example.com:636 \
       --set secondary-server:remote1.example.com:636 \
       --set secondary-server:remote2.example.com:636 \
       --set ssl-cert-nickname:ssl-key-pair \
       --set key-manager-provider:PKCS12 \
       --set trust-manager-provider:"JVM Trust Manager" \
       --set use-ssl:true \
       --set use-sasl-external:true \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin \
       --no-prompt
      ```

   3. Replace the fake replication service discovery mechanism with the static one:

      ```console
      $ dsconfig \
       set-backend-prop \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword str0ngAdm1nPa55word \
       --backend-name proxyRoot \
       --set shard:"Static Service Discovery Mechanism" \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin \
       --no-prompt
      ```

   This example uses mutual TLS with a certificate generated with a deployment ID and password. Adjust the security settings as required for your deployment.

### Configure access control

1. Explicitly grant appropriate access to remote data.

   The following example grants authenticated users access to data under `dc=example,dc=com`:

   ```console
   $ dsconfig \
    create-global-access-control-policy \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword str0ngAdm1nPa55word \
    --policy-name "Authenticated access to example.com data" \
    --set authentication-required:true \
    --set request-target-dn-equal-to:"dc=example,dc=com" \
    --set request-target-dn-equal-to:"**,dc=example,dc=com" \
    --set permission:read \
    --set permission:write \
    --set allowed-attribute:"*" \
    --set allowed-attribute:isMemberOf \
    --set allowed-attribute-exception:authPassword \
    --set allowed-attribute-exception:userPassword \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   DS proxy servers do not use ACIs for access control. Instead, they use global access control policies. By default, the access rights are configured the same as the default settings for a directory server. You no doubt need to adapt these policies for your deployment. For additional examples, refer to [Access control](../security-guide/access.html).

2. Make sure the backend directory servers are properly prepared, as described [Create a service account](#proxy-account).

For more background on LDAP proxy features, refer to [LDAP proxy](../config-guide/proxy.html).

#### Default global policies

Access control rules are defined using individual access control policy entries. A user's access is defined as the union of all access control rules that apply to that user. In other words, an individual access control rule can only grant additional access and can not remove rights granted by another rule. This approach results in an access control policy which is easier to understand and audit, since all rules can be understood in isolation.

| Policy                                              | Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anonymous extended operation and control access     | * `authentication-required`

  * `false`

* `allowed-extended-operation`

  * `Cancel`

  * `GetSymmetricKey`

  * `PasswordModify`

  * `StartTLS`

  * `WhoAmI`

* `allowed-control`

  * `Assertion`

  * `MatchedValues`

  * `NoOp`

  * `PasswordQualityAdvice`

  * `PermissiveModify`

  * `PostRead`

  * `PreRead`

  * `RealAttrsOnly`

  * `SimplePagedResults`

  * `VirtualAttrsOnly`

  * `AuthorizationIdentity`

  * `PasswordPolicy`

  * `TransactionId`

  * `Vlv`

  * `W3cTraceContext`                         |
| Authenticated extended operation and control access | - `authentication-required`

  * `true`

- `allowed-extended-operation`

  * `PasswordPolicyState`

- `allowed-control`

  * `ManageDsaIt`

  * `SubEntries`

  * `RelaxRules`

  * `SubtreeDelete`

  * `ServerSideSort`                                                                                                                                                                                                                                                                                                             |
| Schema access                                       | * `authentication-required`

  * `true`

* `request-target-dn-equal-to`

  * `cn=schema`

* `permission`

  * `read`

* `allowed-attribute`

  * `objectClass`

  * `@subschema`

  * `etag`

  * `ldapSyntaxes`

  * `modifiersName`

  * `modifyTimestamp`                                                                                                                                                                                                                                                                          |
| Root DSE access                                     | - `authentication-required`

  * `false`

- `request-target-dn-equal-to`

  * `""`

- `permission`

  * `read`

- `allowed-attribute`

  * `objectClass`

  * `namingContexts`

  * `subSchemaSubEntry`

  * `supportedAuthPasswordSchemes`

  * `supportedControl`

  * `supportedExtension`

  * `supportedFeatures`

  * `supportedLDAPVersion`

  * `supportedSASLMechanisms`

  * `supportedTLSCiphers`

  * `supportedTLSProtocols`

  * `vendorName`

  * `vendorVersion`

  * `fullVendorVersion`

  * `alive`

  * `healthy` |
| Monitor access                                      | * `authentication-required`

  * `true`

* `request-target-dn-equal-to`

  * `cn=monitor`

* `permission`

  * `read`

* `allowed-attribute`

  * `*`

  * `+`                                                                                                                                                                                                                                                                                                                                                                        |

## Align LDAP schema

Directory servers can reject LDAP change requests that do not comply with LDAP schema. LDAP client applications read LDAP schema definitions from directory servers to determine in advance whether a change request complies with LDAP schema.

When an LDAP client requests LDAP schema from the proxy, the proxy returns *its* LDAP schema. Ideally, the LDAP schema definitions on the proxy match the LDAP schema definitions on the remote directory servers. Otherwise, client applications might check their requests against the proxy's LDAP schema, and yet still have their requests fail with schema violations when the proxy forwards a request to a directory server.

If, after installation, the LDAP schema definitions on the directory servers and the proxy server differ, align the LDAP schema of the proxy server with the LDAP schema of the remote directory servers.

For more information, refer to [LDAP schema](../config-guide/schema.html). Schema definitions on a non-DS remote directory server might require translation from another format before you add them on DS directory proxy servers.

## Troubleshooting

Common errors with DS directory proxy server installations include the following:

* 49 (Invalid Credentials)

  When LDAP bind requests through the proxy invariably result in an invalid credentials error, but bind requests to the directory server with the same credentials do not, the problem lies with the proxy service account.

  The proxy service account must allow bind requests to the directory server. The following example demonstrates a request sent directly to a directory server. The command makes a bind request and then a search request. The directory server is set up according to the instructions in [Try DS directory proxy](#test-proxy):

  ```console
  $ ldapsearch \
   --hostname localhost \
   --port 1636 \
   --useSsl \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=kvaughan,ou=people,dc=example,dc=com \
   --bindPassword bribery \
   --baseDN "ou=people,dc=example,dc=com" \
   "(|(cn=Babs Jensen)(cn=Sam Carter))" \
   cn
  ```

  > **Collapse: Show output**
  >
  > ```
  > dn: uid=bjensen,ou=People,dc=example,dc=com
  > cn: Barbara Jensen
  > cn: Babs Jensen
  >
  > dn: uid=scarter,ou=People,dc=example,dc=com
  > cn: Sam Carter
  > ```

  Start with the filtered directory server access log, `logs/filtered-ldap-access.audit.json`, to debug bind failures.

* 123 (Authorization Denied)

  Make sure that access control on the remote LDAP servers allows the proxy service account to use the [proxied authorization control](../ldap-guide/proxied-authz.html).

  Proxied authorization does not allow operations on remote LDAP servers as the directory superuser (`uid=admin`). Do not connect as directory superuser when trying to access a directory server through the proxy. For administrative requests on remote LDAP servers, access the servers directly. This includes monitoring requests.

  It is possible to configure proxied authorization so that an anonymous user (no bind DN, no bind password) can make a request through the proxy server to the remote directory server. Avoid doing this, however, as it is less secure.

  Many applications perform some operations anonymously, such as reading the root DSE or LDAP schema. These operations are in fact requests to the proxy, not forwarded to remote LDAP servers. For applications to receive an appropriate response for LDAP schema requests, align LDAP schema on the proxy with LDAP schema on the remote LDAP servers as described above.

---

---
title: Install an HDAP gateway
description: Install and configure the PingDS HDAP gateway web application that translates HTTP directory requests into LDAP requests.
component: pingds
version: 8.1
page_id: pingds:install-guide:install-hdap
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/install-hdap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-14T11:03:55Z
keywords: ["Install", "Integration", "LDAP", "REST API", "Setup &amp; Configuration"]
page_aliases: ["install-rest.adoc"]
section_ids:
  install-hdap: Installation
  verification: Verification
---

# Install an HDAP gateway

The DS HDAP *(tooltip: HTTP Directory Access Protocol)* gateway web application translates HTTP requests in LDAP requests:

![HDAP translates HTTP to LDAP.](../_images/hdap.svg)

The HDAP gateway functions as a web application in a web application container. It runs independently of the LDAPv3 directory service.

The LDAPv3 directory service must support [proxied authorization](../ldap-guide/proxied-authz.html). In particular, this means you can use the HDAP gateway with current and previous versions of DS.

## Installation

1. [Review requirements for installation](https://docs.pingidentity.com/pingds/release-notes/requirements.html) to verify the HDAP gateway supports your web application container.

2. Deploy the .war file according to the instructions for your web application container; for example:

   ```console
   $ mv DS-hdap-servlet-8.1.1.war hdap.war
   $ cp hdap.war /path/to/tomcat/webapps/
   ```

   If you use Wildfly, you must unzip the .war file into the deployment directory.

3. Edit the configuration in the deployed gateway web application:

   * `WEB-INF/classes/config.json`

     This file defines how the HDAP gateway connects to and interacts with LDAP directory servers.

     At minimum, set the directory server hostnames, port numbers, and proxy user credentials:

     * The default configuration connects to `localhost:1389`. When you set up DS for evaluation, port `1389` is a cleartext port. The default password policies allow simple binds for authentication only on secure connections. To let the gateway authenticate to DS on a cleartext port, update the relevant password policies to set `require-secure-authentication:false`.

       When connecting to the remote directory service over LDAPS or LDAP and StartTLS (recommended), configure the gateway client-side trust manager to trust the server certificates. Find examples in [Trust certificates](../security-guide/key-management.html#trust-certs).

     * The proxy user LDAP account performs proxied authorization. In the default gateway configuration, the proxy user is the default directory superuser, `uid=admin`.

       In a [DS directory server set up for evaluation](setup-ds.html), the directory superuser *can't act as the proxy user* by default. The account with simple bind credentials `cn=My App,ou=Apps,dc=example,dc=com` and `password` can act as a proxy user. If you keep the directory superuser as the proxy user, adapt the instructions in [proxied authorization](../ldap-guide/proxied-authz.html) to grant proxied authorization access and privileges to the directory superuser.

     * By default, the HDAP gateway returns resources with normalized field names. If applications expect resources from the gateway to use the names specified in the LDAP entries or `_fields` query parameter, set `"normalizeAttributeNames": false` in the configuration.

   * `WEB-INF/classes/logging.properties`

     This file defines logging properties when you run the gateway in Apache Tomcat.

4. (Optional) Adjust the log level.

   At the default log level of `INFO`, the HDAP gateway logs messages about HTTP requests. Find more information about log level definitions in [java.util.logging.Level](https://docs.oracle.com/en/java/javase/25/docs/api/java.logging/java/util/logging/Level.html).

   If the HDAP gateway runs in Apache Tomcat, edit the `logging.properties` file. Otherwise, set the log level as described in the container documentation.

5. (Recommended) Configure the web application container to use HTTPS for secure connections to the gateway.

   Learn more in the container documentation.

6. Restart the HDAP gateway or the web application container.

   The gateway reloads its configuration.

7. Verify the directory service is up and the gateway connects correctly.

## Verification

1. Set up a [DS directory server for evaluation](setup-ds.html).

2. [Install and configure the HDAP gateway](#install-hdap).

3. Read Babs Jensen's resource through the gateway.

   If necessary, adjust the protocol (`https`), port (`8443`), and base path (`/hdap`) for your configuration:

   ```console
   $ curl \
    --user dc=com/dc=example/ou=People/uid=bjensen:hifalutin \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=cn&_prettyPrint=true'
   ```

   Output

   ```json
   {
     "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
     "_rev" : "<revision>",
     "cn" : [ "Barbara Jensen", "Babs Jensen" ]
   }
   ```

You have demonstrated the HDAP gateway works as expected.

---

---
title: Install DS as an IDM repository
description: Install PingDS as a PingIDM repository using the idm-repo setup profile.
component: pingds
version: 8.1
page_id: pingds:install-guide:profile-idm-repo
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/profile-idm-repo.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Identities", "Identity Store", "Install", "LDAP", "Repository", "Setup &amp; Configuration"]
---

# Install DS as an IDM repository

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When IDM uses multiple DS replicas, configure IDM for [failover](https://docs.pingidentity.com/pingidm/8.1/install-guide/external-ds.html#two-ds-active-passive). |

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the `setup` command with the `--profile idm-repo` option:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword str0ngAdm1nPa55word \
    --hostname localhost \
    --adminConnectorPort 34444 \
    --ldapPort 31389 \
    --enableStartTls \
    --profile idm-repo \
    --set idm-repo/domain:forgerock.com \
    --acceptLicense
   ```

   * The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

   * The administrative account to use in IDM when connecting to DS has:

     * Bind DN: The DN set with the `--rootUserDN` option.

     * Password: The password set with the `--rootUserPassword` option.

   * The base DN for IDM data is `dc=openidm,dc=example,dc=com`.

     AM and IDM expect exclusive access to the data in each setup profile. *Keep the data separate by using distinct base DNs and domains for each setup profile.* Don't accidentally mix the data by choosing a base DN under another base DN.

   * IDM requires change number indexing with the default settings.

   For the full list of profiles and parameters, refer to [Default setup profiles](setup-profiles.html#default-setup-profiles).

5. Finish configuring the server *before you start it*.

   For a list of optional steps at this stage, refer to [Install DS for custom cases](custom-replica.html).

6. If all access to DS goes through IDM, IDM manages password policy.

   In this case, relax the default password policy settings:

   ```console
   $ dsconfig \
    set-password-policy-prop \
    --policy-name "Default Password Policy" \
    --reset password-validator \
    --offline \
    --no-prompt
   $ dsconfig \
    set-password-policy-prop \
    --policy-name "Root Password Policy" \
    --reset password-validator \
    --offline \
    --no-prompt
   ```

7. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

---

---
title: Install DS for AM configuration
description: Install PingDS as a configuration data store for PingAM using the am-config setup profile.
component: pingds
version: 8.1
page_id: pingds:install-guide:profile-am-config
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-config.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Configuration Store", "Install", "LDAP", "Setup &amp; Configuration"]
---

# Install DS for AM configuration

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the `setup` command with the `--profile am-config` option:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword str0ngAdm1nPa55word \
    --monitorUserPassword str0ngMon1torPa55word \
    --hostname ds.example.com \
    --adminConnectorPort 4444 \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --replicationPort 8989 \
    --bootstrapReplicationServer rs1.example.com:8989 \
    --bootstrapReplicationServer rs2.example.com:8989 \
    --profile am-config \
    --set am-config/amConfigAdminPassword:5up35tr0ng \
    --acceptLicense
   ```

   * The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

   * The service account to use in AM when connecting to DS has:

     * Bind DN: `uid=am-config,ou=admins,ou=am-config`.

     * Password: The password you set with `am-config/amConfigAdminPassword`.

   * The base DN for AM configuration data is `ou=am-config`.

     AM and IDM expect exclusive access to the data in each setup profile. *Keep the data separate by using distinct base DNs and domains for each setup profile.* Don't accidentally mix the data by choosing a base DN under another base DN.

   For the full list of profiles and parameters, refer to [Default setup profiles](setup-profiles.html#default-setup-profiles).

5. Finish configuring the server *before you start it*.

   For a list of optional steps at this stage, refer to [Install DS for custom cases](custom-replica.html).

6. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

---

---
title: Install DS for AM CTS
description: Install PingDS as a CTS token store for PingAM, with options for managing token expiration using PingAM or PingDS.
component: pingds
version: 8.1
page_id: pingds:install-guide:profile-am-cts
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-cts.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-27T13:21:24Z
keywords: ["CTS Store (Sessions &amp; Tokens)", "Install", "LDAP", "Setup &amp; Configuration"]
---

# Install DS for AM CTS

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the appropriate `setup` command with the `--profile am-cts` option.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Installation settings depend on AM token expiration and session capability requirements. Letting DS expire tokens is efficient, but affects sending AM notifications about session expiration and timeouts to AM policy agents.- Learn about AM token expiration options in [Manage expired CTS tokens](https://docs.pingidentity.com/pingam/8.1/cts/cts-reaper.html).

   - Learn about the mechanism DS uses to expire tokens in [Entry expiration](../config-guide/import-export.html#backend-ttl). |

   1. AM reaper manages all token expiration (AM default):

      ```console
      $ /path/to/opendj/setup \
       --deploymentId $DEPLOYMENT_ID \
       --deploymentIdPassword password \
       --rootUserDN uid=admin \
       --rootUserPassword str0ngAdm1nPa55word \
       --monitorUserPassword str0ngMon1torPa55word \
       --hostname ds.example.com \
       --adminConnectorPort 4444 \
       --ldapPort 1389 \
       --enableStartTls \
       --ldapsPort 1636 \
       --httpsPort 8443 \
       --replicationPort 8989 \
       --bootstrapReplicationServer rs1.example.com:8989 \
       --bootstrapReplicationServer rs2.example.com:8989 \
       --profile am-cts \
       --set am-cts/amCtsAdminPassword:5up35tr0ng \
       --acceptLicense
      ```

   2. AM reaper manages only SESSION token expiration:

      ```console
      $ /path/to/opendj/setup \
       --deploymentId $DEPLOYMENT_ID \
       --deploymentIdPassword password \
       --rootUserDN uid=admin \
       --rootUserPassword str0ngAdm1nPa55word \
       --monitorUserPassword str0ngMon1torPa55word \
       --hostname ds.example.com \
       --adminConnectorPort 4444 \
       --ldapPort 1389 \
       --enableStartTls \
       --ldapsPort 1636 \
       --httpsPort 8443 \
       --replicationPort 8989 \
       --bootstrapReplicationServer rs1.example.com:8989 \
       --bootstrapReplicationServer rs2.example.com:8989 \
       --profile am-cts \
       --set am-cts/amCtsAdminPassword:5up35tr0ng \
       --set am-cts/tokenExpirationPolicy:am-sessions-only \
       --acceptLicense
      ```

   3. DS manages all token expiration:

      ```console
      $ /path/to/opendj/setup \
       --deploymentId $DEPLOYMENT_ID \
       --deploymentIdPassword password \
       --rootUserDN uid=admin \
       --rootUserPassword str0ngAdm1nPa55word \
       --monitorUserPassword str0ngMon1torPa55word \
       --hostname ds.example.com \
       --adminConnectorPort 4444 \
       --ldapPort 1389 \
       --enableStartTls \
       --ldapsPort 1636 \
       --httpsPort 8443 \
       --replicationPort 8989 \
       --bootstrapReplicationServer rs1.example.com:8989 \
       --bootstrapReplicationServer rs2.example.com:8989 \
       --profile am-cts \
       --set am-cts/amCtsAdminPassword:5up35tr0ng \
       --set am-cts/tokenExpirationPolicy:ds \
       --acceptLicense
      ```

   In the preceding example commands:

   * The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

   * The service account to use in AM when connecting to DS has:

     * Bind DN: `uid=openam_cts,ou=admins,ou=famrecords,ou=openam-session,ou=tokens`.

     * Password: The password you set with `am-cts/amCtsAdminPassword`.

   * The base DN for AM CTS tokens is `ou=famrecords,ou=openam-session,ou=tokens`.

     AM and IDM expect exclusive access to the data in each setup profile. *Keep the data separate by using distinct base DNs and domains for each setup profile.* Don't accidentally mix the data by choosing a base DN under another base DN.

   * The `am-cts` profile excludes the base DN from change number indexing.

   For the full list of profiles and parameters, refer to [Default setup profiles](setup-profiles.html#default-setup-profiles).

5. Finish configuring the server *before you start it*.

   For a list of optional steps at this stage, refer to [Install DS for custom cases](custom-replica.html).

6. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

---

---
title: Install DS for custom cases
description: Install PingDS as a replica with a custom configuration, including offline setup steps for schema, backends, indexes, and replication initialization.
component: pingds
version: 8.1
page_id: pingds:install-guide:custom-replica
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/custom-replica.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Customization", "Extensibility", "Install", "Integration", "LDAP", "Setup &amp; Configuration"]
---

# Install DS for custom cases

Follow these steps to install a DS replica with your own custom configuration:

1. Before proceeding, install the server files.

   For details, refer to [Unpack files](install-files.html).

2. Run the `setup` command with any required setup profiles.

3. Finish configuring the server.

   Perform any of the following optional steps *before starting the server*.

   Use the `--offline` option with commands instead of the credentials and connection information shown in many examples:

   * Add custom syntaxes and matching rules.

     For examples, refer to [Custom indexes for JSON](../config-guide/idx-config.html#configure-json-index).

   * Configure password storage.

     For details, refer to [Configure password policies](../security-guide/pwp-configure.html).

     Take care to configure the password policy import plugin as well. For details on the settings, refer to [Password Policy Import Plugin](../configref/objects-password-policy-import-plugin.html).

   * Add custom LDAP schema.

     For details, refer to [LDAP schema](../config-guide/schema.html).

   * Configure one or more backends for your data.

     For details, refer to [Create a backend](../config-guide/import-export.html#create-database-backend). When you create the backend, unless you choose *not* to replicate the data, follow each step of the procedure, adapting the example commands for offline use:

     * Configure the new backend using the `dsconfig create-backend` as shown.

     * Verify that replication is enabled using the `dsconfig get-synchronization-provider-prop` command as shown.

     * Let the server replicate the base DN of the new backend, using the `dsconfig create-replication-domain` command as shown to configure the replication domain.

     * If you have existing data for the backend, make appropriate plans to initialize replication, as described in [Manual initialization](../config-guide/repl-init.html).

   * Configure indexes for the backends you configured.

     For details, refer to [Indexes](../config-guide/indexing.html).

   * Make sure the server has the shared master key for encrypted data and backups.

     If you set up the servers with a known deployment ID and password, you have nothing to do.

     If you do not know the deployment ID and password, refer to [Replace deployment IDs](../security-guide/key-management.html#replace-deployment-ids).

   * Initialize replication.

     For example, import the data from LDIF, or restore the data from backup.

     For details, refer to [Manual initialization](../config-guide/repl-init.html), [Import LDIF](../config-guide/import-export.html#import-ldif), or [Restore](../maintenance-guide/backup-restore.html#restore).

4. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

When you start the server, it generates initial state identifiers (generation IDs) for its replicated base DNs. If you perform the above configuration steps on replicas separately after starting them, their generation IDs can be out of sync.

When generation IDs do not match on different replicas for a particular base DN, DS must assume that the replicas do not have the same data. As a result, replication cannot proceed. To fix the mismatch of this replica's generation IDs with other replicas, stop the server and clear all replication data:

```console
$ /path/to/opendj/bin/stop-ds
$ /path/to/opendj/bin/dsrepl clear-changelog
```

|   |                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Clearing the changelog before all the changes have been sent to other replication servers can cause you to lose data.Use the `dsrepl clear-changelog` command only when initially setting up the replica, unless specifically instructed to do so by a qualified technical support engineer. |

Complete any further configuration necessary while the replica is stopped to align it with other replicas. When you start the replica again with the `start-ds` command, other replication servers update it with the data needed to resume replication.

For details on replication, refer to [Replication](../config-guide/replication.html) and the related pages.

---

---
title: Install DS for evaluation
description: Install a PingDS directory server for evaluation using the ds-evaluation setup profile, which provides sample data and permissive access settings.
component: pingds
version: 8.1
page_id: pingds:install-guide:setup-ds
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/setup-ds.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Evaluation", "Install", "LDAP", "Setup &amp; Configuration"]
section_ids:
  about-ds-evaluation: About the evaluation setup profile
  evaluation_profile_acis: Evaluation profile ACIs
---

# Install DS for evaluation

To set up the server, use the [setup](../tools-reference/setup.html) command-line tool. The following steps set up a single DS server on your computer for trying examples in the documentation.

When used without options, the `setup` command is interactive. When performing a non-interactive, silent installation, specify at least all mandatory options.

> **Collapse: About mandatory options**
>
> The following `setup` options are mandatory. If you use only these options, the command sets up a server listening only on an administration port. The administration port is protected by a key pair specified or generated at setup time:
>
> * `--adminConnectorPort {port}` (The documentation uses `4444`.)
>
> * `--deploymentId {deploymentId}`
>
> * `--deploymentIdPassword {deploymentIdpassword}`
>
> * `--hostname {hostname}`
>
> * `--rootUserDN {rootUserDN}` (The documentation uses uid=admin.)
>
> * `--rootUserPassword {rootUserPassword}`

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the `setup` command to install a directory server replica with the evaluation profile:

   ```console
   $ /path/to/opendj/setup \
    --serverId evaluation-only \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword password \
    --monitorUserPassword password \
    --hostname localhost \
    --adminConnectorPort 4444 \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --replicationPort 8989 \
    --bootstrapReplicationServer localhost:8989 \
    --profile ds-evaluation \
    --start \
    --acceptLicense
   ```

   Notice the following about the command:

   * Its location depends on where you installed the files.

   * It requires your generated deployment ID and its password.

   * It prepares a single server for evaluation on your computer.

     This example uses the hostname `localhost`. When you install servers on multiple computers or need remote access to your server, use fully qualified domain names, such as `ds.example.com`.

   * It prepares the server to replicate sample data with other servers.

     Because there are no other replicas yet, this server points to itself as a bootstrap replication server (`--bootstrapReplicationServer localhost:8989`).

     Learn more in [Learn replication](../getting-started/replication.html) and [Bootstrap replication servers](../config-guide/repl-bootstrap.html).

   * It sets a password for the default monitoring user account.

     The default DN, which is not shown, is `uid=Monitor`.

   * It prepares the server to listen for requests on the ports used in examples throughout the documentation.

   * For evaluation purposes, no further configuration is required.

     The `--start` option starts the server at the end of the setup process.

## About the evaluation setup profile

The evaluation setup profile helps you learn and demonstrate directory services. Unlike other setup profiles, which use secure, production-ready access control settings, the evaluation setup profile provides easy access to sample data with the following features:

* Sample Example.com data.

  The sample data has the base DN `dc=example,dc=com`. It includes more than 100 handwritten entries for users, groups, and devices.

  By default, it also includes 100,000 generated users, with DNs from `uid=user.0,ou=people,dc=example.dc=com` to `uid=user.99999,ou=people,dc=example.dc=com`.

  Use the `--set ds-evaluation/generatedUsers:number` option to generate a different number of additional entries. Each generated user has the same password, which is `password`.

  The handwritten sample Example.com data includes a group of directory administrators, `cn=Directory Administrators,ou=Groups,dc=example,dc=com`. Members of this group, such as `kvaughan`, have full access to directory data.

  Examples throughout the documentation demonstrate features using this sample data.

* Global permission to perform operations over insecure connections.

* HDAP enabled by default.

* Additional schema for examples demonstrating class of service and JSON attributes.

* Custom matching rule providers for JSON attributes.

* Many permissions, such as anonymous read and search access, listed in the table that follows.

  The evaluation setup profile lets you learn and demonstrate most directory features without adding any ACIs.

## Evaluation profile ACIs

| Name                                          | Description                                                                                                                                                                                                                                                                                     | ACI definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Anonymous extended operation access           | Anonymous and authenticated users can request the LDAP extended operations that are specified by OID or alias. Modification or removal may affect applications.                                                                                                                                 | `(targetcontrol="Assertion\|\|AuthorizationIdentity\|\|MatchedValues\|\|NoOp\|\|PasswordPolicy\|\|PasswordQualityAdvice\|\|PermissiveModify\|\|PostRead\|\|PreRead\|\|RealAttrsOnly\|\|SimplePagedResults\|\|StructuredError\|\|TransactionId\|\|VirtualAttrsOnly\|\|Vlv\|\|W3cTraceContext") (version 3.0; acl "Anonymous extended operation access"; allow(read) userdn="ldap:///anyone";)`                                                                                                                |
| Anonymous extended operation access           | Anonymous and authenticated users can request the LDAP extended operations that are specified by OID or alias. Modification or removal may affect applications.                                                                                                                                 | `(extop="Cancel\|\|GetSymmetricKey\|\|PasswordModify\|\|StartTls\|\|WhoAmI") (version 3.0; acl "Anonymous extended operation access"; allow(read) userdn="ldap:///anyone";)`                                                                                                                                                                                                                                                                                                                                 |
| Anonymous read and search access              | Anonymous and authenticated Example.com users can read the user data attributes that are specified by their names.                                                                                                                                                                              | `(targetattr!="userPassword\|\|authPassword\|\|debugsearchindex") (version 3.0; acl "Anonymous read and search access"; allow (read,search,compare) userdn="ldap:///anyone";)`                                                                                                                                                                                                                                                                                                                               |
| Authenticated control use                     | Authenticated Example.com users can proxy and examine CSNs.                                                                                                                                                                                                                                     | `(targetcontrol="ProxiedAuth\|\|Csn") (version 3.0; acl "Authenticated control use"; allow(read) userdn="ldap:///all";)`                                                                                                                                                                                                                                                                                                                                                                                     |
| Authenticated users extended operation access | Authenticated users can request the LDAP extended operations that are specified by OID or alias. Modification or removal may affect applications.                                                                                                                                               | `(targetcontrol="ManageDsaIt\|\|RelaxRules\|\|ServerSideSort\|\|SubEntries\|\|SubtreeDelete") (version 3.0; acl "Authenticated users extended operation access"; allow(read) userdn="ldap:///all";)`                                                                                                                                                                                                                                                                                                         |
| Authenticated users extended operation access | Authenticated users can request the LDAP extended operations that are specified by OID or alias. Modification or removal may affect applications.                                                                                                                                               | `(extop="PasswordPolicyState") (version 3.0; acl "Authenticated users extended operation access"; allow(read) userdn="ldap:///all";)`                                                                                                                                                                                                                                                                                                                                                                        |
| Directory administrator full access           | Example.com directory administrators have access to read and write Example.com directory data, rename and move entries, and use proxied authorization.                                                                                                                                          | `(targetattr="* \|\| +") (version 3.0; acl "Directory administrator full access"; allow (all,export,import,proxy) groupdn="ldap:///cn=Directory Administrators,ou=Groups,dc=example,dc=com";)`                                                                                                                                                                                                                                                                                                               |
| Proxied authorization for apps                | Example.com applications can make requests on behalf of other users.                                                                                                                                                                                                                            | `(targetattr="*") (version 3.0; acl "Proxied authorization for apps"; allow (all,proxy) (userdn="ldap:///cn=*,ou=Apps,dc=example,dc=com");)`                                                                                                                                                                                                                                                                                                                                                                 |
| Self entry modification                       | Authenticated users can modify the specified attributes on their own entries.                                                                                                                                                                                                                   | `(targetattr=" audio \|\| authPassword \|\| description \|\| displayName \|\| givenName \|\| homePhone \|\| homePostalAddress \|\| initials \|\| jpegPhoto \|\| labeledURI \|\| mobile \|\| pager \|\| postalAddress \|\| postalCode \|\| preferredLanguage \|\| telephoneNumber \|\| userPassword") (version 3.0; acl "Self entry modification"; allow (write) userdn="ldap:///self";)`                                                                                                                     |
| Self entry read for passwords                 | Authenticated users can read the password values on their own entries. By default, the server applies a one-way hash algorithm to the password value before writing it to the entry, so it is computationally difficult to recover the plaintext version of the password from the stored value. | `(targetattr="userPassword\|\|authPassword") (version 3.0; acl "Self entry read for passwords"; allow (read,search,compare) userdn="ldap:///self";)`                                                                                                                                                                                                                                                                                                                                                         |
| Self service group creation                   | Authenticated Example.com users can create self service groups.                                                                                                                                                                                                                                 | `(targattrfilters="add=objectClass:(objectClass=groupOfNames)")(version 3.0; acl "Self service group creation";allow (add) (userdn="ldap:///uid=*,ou=People,dc=example,dc=com");)`                                                                                                                                                                                                                                                                                                                           |
| Self service group deletion                   | The authenticated owner of a self service group can delete the group.                                                                                                                                                                                                                           | `(version 3.0; acl "Self service group deletion";allow (delete) (userattr="owner#USERDN");)`                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Self service group registration               | Authenticated Example.com users can sign themselves up as members of self service groups.                                                                                                                                                                                                       | `(targetattr="member") (version 3.0; acl "Self service group registration"; allow (selfwrite) (userdn="ldap:///uid=*,ou=People,dc=example,dc=com");)`                                                                                                                                                                                                                                                                                                                                                        |
| User-Visible Monitor Attributes               | Authenticated users can read monitoring information if they have the monitor read privilege. Modification or removal may affect applications.                                                                                                                                                   | `(target="ldap:///cn=monitor")(targetattr="*\|\|+") (version 3.0; acl "User-Visible Monitor Attributes"; allow (read,search,compare) userdn="ldap:///all";)`                                                                                                                                                                                                                                                                                                                                                 |
| User-visible operational attributes           | Anonymous and authenticated users can read attributes that identify entries and that contain information about modifications to entries.                                                                                                                                                        | `(targetattr=" createTimestamp \|\| creatorsName \|\| modifiersName \|\| modifyTimestamp \|\| entryDN \|\| entryUUID \|\| subschemaSubentry \|\| etag \|\| governingStructureRule \|\| structuralObjectClass \|\| hasSubordinates \|\| numSubordinates \|\| isMemberOf") (version 3.0; acl "User-visible operational attributes"; allow (read,search,compare) userdn="ldap:///anyone";)`                                                                                                                     |
| User-Visible Root DSE Operational Attributes  | Anonymous and authenticated users can read attributes that describe what the server supports. Modification or removal may affect applications.                                                                                                                                                  | `(target="ldap:///")(targetscope="base") (targetattr="objectClass\|\|namingContexts\|\|subSchemaSubEntry\|\|supportedAuthPasswordSchemes\|\|supportedControl\|\|supportedExtension\|\|supportedFeatures\|\|supportedLDAPVersion\|\|supportedSASLMechanisms\|\|supportedTLSCiphers\|\|supportedTLSProtocols\|\|vendorName\|\|vendorVersion\|\|fullVendorVersion\|\|alive\|\|healthy")(version 3.0; acl "User-Visible Root DSE Operational Attributes"; allow (read,search,compare) userdn="ldap:///anyone";)` |
| User-Visible Schema Operational Attributes    | Authenticated users can read LDAP schema definitions. Modification or removal may affect applications.                                                                                                                                                                                          | `(target="ldap:///cn=schema")(targetscope="base") (targetattr="objectClass\|\|attributeTypes\|\|dITContentRules\|\|dITStructureRules \|\|ldapSyntaxes\|\|matchingRules\|\|matchingRuleUse\|\|nameForms\|\|objectClasses\|\|etag\|\|modifiersName\|\|modifyTimestamp") (version 3.0; acl "User-Visible Schema Operational Attributes"; allow (read,search,compare) userdn="ldap:///all";)`                                                                                                                    |

---

---
title: Install DS for platform identities
description: Install PingDS as a platform identity repository for PingAM or a shared identity store for PingAM and PingIDM.
component: pingds
version: 8.1
page_id: pingds:install-guide:profile-am-idrepo
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-idrepo.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-27T13:21:24Z
keywords: ["Identities", "Identity Store", "Install", "LDAP", "Setup &amp; Configuration"]
---

# Install DS for platform identities

Use this profile when setting up DS as an identity repository and user data store for AM alone or shared with IDM in a Ping Identity Platform deployment. It includes the additional LDAP schema and indexes required to store the identities:

|   |                                                                                                                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When AM and IDM share multiple DS replicas for identities:- Configure IDM for [failover](https://docs.pingidentity.com/pingidm/8.1/install-guide/external-ds.html#two-ds-active-passive).

- Configure AM to fail over when [connecting to DS replicas](https://docs.pingidentity.com/pingam/8.1/setup/data-stores-opendj.html#ldap_server) in the same order as IDM. |

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the `setup` command with the `--profile am-identity-store` option:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword str0ngAdm1nPa55word \
    --monitorUserPassword str0ngMon1torPa55word \
    --hostname ds.example.com \
    --adminConnectorPort 4444 \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --replicationPort 8989 \
    --bootstrapReplicationServer rs1.example.com:8989 \
    --bootstrapReplicationServer rs2.example.com:8989 \
    --profile am-identity-store \
    --set am-identity-store/amIdentityStoreAdminPassword:5up35tr0ng \
    --acceptLicense
   ```

   * The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

   * The service account to use in AM when connecting to DS has:

     * Bind DN: `uid=am-identity-bind-account,ou=admins,ou=identities`.

     * Password: The password you set with `am-identity-store/amIdentityStoreAdminPassword`.

   * The base DN for AM identities is `ou=identities`.

     AM and IDM expect exclusive access to the data in each setup profile. *Keep the data separate by using distinct base DNs and domains for each setup profile.* Don't accidentally mix the data by choosing a base DN under another base DN.

   For the full list of profiles and parameters, refer to [Default setup profiles](setup-profiles.html#default-setup-profiles).

5. Finish configuring the server *before you start it*.

   For a list of optional steps at this stage, refer to [Install DS for custom cases](custom-replica.html).

6. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

---

---
title: Install DS for use with DS proxy
description: Install PingDS as a proxied directory server, adding the service account and access control required by a PingDS proxy.
component: pingds
version: 8.1
page_id: pingds:install-guide:profile-ds-proxied-server
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/profile-ds-proxied-server.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Install", "LDAP", "Setup &amp; Configuration"]
---

# Install DS for use with DS proxy

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the `setup` command with the `--profile ds-proxied-server` option.

   The example shows the profile used with the evaluation profile. *Add this profile to the list* so proxy servers can access other profiles' data:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword str0ngAdm1nPa55word \
    --monitorUserPassword str0ngMon1torPa55word \
    --hostname ds.example.com \
    --adminConnectorPort 4444 \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --replicationPort 8989 \
    --bootstrapReplicationServer rs1.example.com:8989 \
    --bootstrapReplicationServer rs2.example.com:8989 \
    --profile ds-evaluation \
    --profile ds-proxied-server \
    --set ds-proxied-server/baseDn:dc=example,dc=com \
    --acceptLicense
   ```

   * The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

   * The account the DS proxy can use to connect to DS replicas has:

     * Bind DN: The DN from the `--set ds-proxied-server/proxyUserDn` option.

       Default: `uid=proxy`.

     * Certificate subject DN: The DN from the `--set ds-proxied-server/proxyUserCertificateSubjectDn` option.

       Default: `CN=DS, O=ForgeRock.com`.

     * Access to use proxied authorization in the base DNs specified by the multivalued `--set ds-proxied-server/baseDn` option.

       If you do not specify any values for `ds-proxied-server/baseDn`, the proxy user can perform operations with any account as authorization identity. This includes administrator accounts.

       To understand what this means, read [Proxied authorization](../ldap-guide/proxied-authz.html).

   * The DS proxy server binds using certificate-based authentication with the SASL EXTERNAL mechanism.

     Make sure that the DS replicas' truststores lets them trust the proxy's certificate.

   * The DS proxy server uses proxied authorization to perform operations on the DS replicas.

     The authorization identity for the operations must have appropriate access to the data on the DS replicas.

   For the full list of profiles and parameters, refer to [Default setup profiles](setup-profiles.html#default-setup-profiles).

5. Finish configuring the server *before you start it*.

   For a list of optional steps at this stage, refer to [Install DS for custom cases](custom-replica.html).

6. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

---

---
title: Install DS for user data
description: Install PingDS for generic user data with inetOrgPerson indexes, for deployments that do not use PingAM or PingIDM identities.
component: pingds
version: 8.1
page_id: pingds:install-guide:profile-user-data
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/profile-user-data.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Identities", "Identity Store", "Install", "LDAP", "Setup &amp; Configuration"]
---

# Install DS for user data

This profile includes indexes for `inetOrgPerson` entries. It is not intended for deployments with AM or IDM identities.

It does not include the additional LDAP schema and indexes required to store AM identities. To set up a user data store for AM or for sharing between AM and IDM, refer to [Install DS for platform identities](profile-am-idrepo.html) instead.

To import generated sample user data, refer to [Install DS for evaluation](setup-ds.html) instead:

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the `setup` command with the `--profile ds-user-data` option:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword str0ngAdm1nPa55word \
    --monitorUserPassword str0ngMon1torPa55word \
    --hostname ds.example.com \
    --adminConnectorPort 4444 \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --replicationPort 8989 \
    --bootstrapReplicationServer rs1.example.com:8989 \
    --bootstrapReplicationServer rs2.example.com:8989 \
    --profile ds-user-data \
    --set ds-user-data/baseDn:dc=example,dc=com \
    --set ds-user-data/ldifFile:/tmp/user-data.ldif \
    --acceptLicense
   ```

   In this example, the `/tmp/user-data.ldif` file contains the user data entries to import. This is just a placeholder. When you run the command, replace it with your LDIF file containing your own user data.

   * The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

   * The data is stored in the `userData` backend.

   For the full list of profiles and parameters, refer to [Default setup profiles](setup-profiles.html#default-setup-profiles).

5. Finish configuring the server *before you start it*.

   For a list of optional steps at this stage, refer to [Install DS for custom cases](custom-replica.html).

6. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

This setup profile creates the following indexes for user data:

| Index                        | Approx.                         | Equality | Ordering | Presence | Substring | Entry Limit |
| ---------------------------- | ------------------------------- | -------- | -------- | -------- | --------- | ----------- |
| `aci`                        | -                               | -        | -        | Yes      | -         | 4000        |
| `cn`                         | -                               | Yes      | -        | -        | Yes       | 4000        |
| `dn2id`                      | Non-configurable internal index |          |          |          |           |             |
| `ds-certificate-fingerprint` | -                               | Yes      | -        | -        | -         | 4000        |
| `ds-certificate-subject-dn`  | -                               | Yes      | -        | -        | -         | 4000        |
| `ds-sync-conflict`           | -                               | Yes      | -        | -        | -         | 4000        |
| `ds-sync-hist`               | -                               | -        | Yes      | -        | -         | 4000        |
| `entryUUID`                  | -                               | Yes      | -        | -        | -         | 4000        |
| `givenName`                  | -                               | Yes      | -        | -        | Yes       | 4000        |
| `id2children`                | Non-configurable internal index |          |          |          |           |             |
| `id2subtree`                 | Non-configurable internal index |          |          |          |           |             |
| `mail`                       | -                               | Yes      | -        | -        | Yes       | 4000        |
| `member`                     | -                               | Yes      | -        | -        | -         | 4000        |
| `objectClass`                | -                               | Yes      | -        | -        | -         | 4000        |
| `sn`                         | -                               | Yes      | -        | -        | Yes       | 4000        |
| `telephoneNumber`            | -                               | Yes      | -        | -        | Yes       | 4000        |
| `uid`                        | -                               | Yes      | -        | -        | -         | 4000        |
| `uniqueMember`               | -                               | Yes      | -        | -        | -         | 4000        |

---

---
title: Install standalone servers (advanced)
description: Install standalone PingDS replication servers and directory servers for advanced deployments with dedicated replication topology.
component: pingds
version: 8.1
page_id: pingds:install-guide:setup-rs
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/setup-rs.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Architecture", "Install", "LDAP", "Replication", "Setup &amp; Configuration"]
section_ids:
  setup-rs-only: Set up standalone replication servers
  add-ds-only: Set up standalone directory servers
---

# Install standalone servers (advanced)

|   |                                                     |
| - | --------------------------------------------------- |
|   | This information applies to *advanced* deployments. |

* Standalone replication servers have no application data backends. They store only changes to directory data. They're dedicated to transmitting replication messages and maintaining a replication change log.

* Standalone directory servers store replicated copies of application data. These replicas send updates to and receive updates from replication servers. They connect to one replication server at a time and don't maintain a replication change log.

Each replication server in a deployment connects to all other replication servers. The total number of replication connections, Totalconn, increases like the number of replication servers squared. Large deployments that span slow, high-latency links can benefit from having fewer replication servers.

Totalconn = (NRS \* (NRS-1))/2 + NDS

Here, NRS is the number of replication servers (standalone or running in a directory server), and NDS is the number of standalone directory servers.

A deployment with only a few standalone replication servers and many standalone directory servers, significantly limits the number of connections for replication over slow links:

![Dedicated servers are suited to advanced deployments with many replicas.](../_images/standalone-repl.png)Figure 1. Deployment for multiple data centers

The deployment ID for installing the server is stored in the environment variable `DEPLOYMENT_ID`. Install all servers in the same deployment with the same deployment ID and deployment ID password. For details, read [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

## Set up standalone replication servers

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Set up a server as a standalone replication server:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword password \
    --hostname rs-only.example.com \
    --adminConnectorPort 4444 \
    --replicationPort 8989 \
    --bootstrapReplicationServer rs-only.example.com:8989 \
    --bootstrapReplicationServer rs-only2.example.com:8989 \
    --acceptLicense
   ```

   The standalone replication server has no application data.

   It does have LDAP schema and changelog data. If you plan to add any additional schema to the replicas as part of the setup process, also add the schema to this server before starting it.

5. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

6. Repeat the previous steps on additional systems until you have sufficient replication servers to meet your availability requirements.

   To ensure availability, add at least one additional replication server per location. The following example adds a second standalone replication server:

   ```console
   $ /path/to/opendj/setup \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword password \
    --hostname rs-only2.example.com \
    --adminConnectorPort 4444 \
    --replicationPort 8989 \
    --bootstrapReplicationServer rs-only.example.com:8989 \
    --bootstrapReplicationServer rs-only2.example.com:8989 \
    --acceptLicense
   ```

   The standalone replication servers use each other as bootstrap servers to discover other servers in the deployment.

## Set up standalone directory servers

1. Before proceeding, install the server files.\
   For details, refer to [Unpack files](install-files.html).

2. Set up the server as a directory server.

   Notice that the `--bootstrapReplicationServer` references the replication servers set up according to the steps in [Set up standalone replication servers](#setup-rs-only).

   The `--replicationPort` option is not used, because this is a standalone directory server:

   ```console
   $ /path/to/opendj/setup \
    --serverId evaluation-only \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --rootUserDN uid=admin \
    --rootUserPassword password \
    --adminConnectorPort 4444 \
    --hostname ds-only.example.com \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --bootstrapReplicationServer rs-only.example.com:8989 \
    --bootstrapReplicationServer rs-only2.example.com:8989 \
    --profile ds-evaluation \
    --acceptLicense
   ```

3. Finish configuring the server *before you start it*.

   For a list of optional steps at this stage, refer to [Install DS for custom cases](custom-replica.html).

4. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```

5. Repeat the previous steps on additional systems until you have sufficient directory servers to meet your availability and performance requirements.

   To ensure availability, add at least one additional directory server per location.

---

---
title: Installation
description: Overview of PingDS installation options, including the directory server, HDAP gateway, and Java APIs.
component: pingds
version: 8.1
page_id: pingds:install-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Install", "LDAP"]
page_aliases: ["index.adoc"]
---

# Installation

These pages show you how to install and remove PingDS software.

[icon: server, set=fas, size=3x]

#### [Evaluate DS](setup-ds.html)

Try DS software.

[icon: database, set=fas, size=3x]

#### [DS for CTS](profile-am-cts.html)

Store AM CTS tokens.

[icon: id-card, set=fas, size=3x]

#### [DS for Identities](profile-am-idrepo.html)

Store AM identities.

[icon: users, set=fas, size=3x]

#### [DS as IDM Repo](profile-idm-repo.html)

Store IDM data.

[icon: info, set=fas, size=3x]

#### [Setup Hints](setup-parameters.html)

Review setup options.

[icon: exchange-alt, set=fas, size=3x]

#### [DS Proxy](setup-proxy.html)

Install an LDAP proxy.

| Component                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Directory server and tools | Pure Java, high-performance server that can be configured as:- An LDAPv3 directory server with the additional capability to serve directory data to REST applications over HTTP.

- An LDAPv3 directory proxy server providing a single point of access to underlying directory servers.

- A replication server handling replication traffic with directory servers and with other replication servers, receiving, sending, and storing changes to directory data.Server distributions include command-line tools for installing, configuring, and managing servers. The tools make it possible to script all operations. |
| HDAP gateway               | The HDAP gateway is a Java web application offering REST access to a remote LDAPv3 directory service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Java APIs                  | Java server-side APIs for server plugins that extend directory services.All Java APIs have interface stability: *Evolving*. *Be prepared for incompatible changes in both major and minor releases.*                                                                                                                                                                                                                                                                                                                                                                                                                       |

Read the [release notes](https://docs.pingidentity.com/pingds/release-notes/index.html) before installing DS software.

---

---
title: Setup hints
description: Reference hints for each PingDS setup command option, covering instance path, IDs, ports, security, and setup profiles.
component: pingds
version: 8.1
page_id: pingds:install-guide:setup-parameters
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/setup-parameters.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-19T10:36:26Z
keywords: ["Install", "LDAP", "Security", "Setup &amp; Configuration"]
---

# Setup hints

The following table provides extensive hints for using `setup` command options in the order they are presented in interactive mode, when you run the command without options.

Find reference information in [setup](../tools-reference/setup.html):

| Parameter                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Option(s)                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instance path                                        | Server setup uses tools and templates installed with the software to generate the instance files required to run an instance of a server. By default, all the files are co-located.This parameter lets you separate the files. Set the instance path to place generated files in a different location from the tools, templates, and libraries you installed.Interactive setup suggests co-locating the software with the instance files.You cannot use a single software installation for multiple servers. Tools for starting and stopping the server process, for example, work with a single configured server. They do not have a mechanism to specify an alternate server location.If you want to set up another server, install another copy of the software, and run that copy's `setup` command.                                                                                                                                                                                                                                                                                                                                                                                     | `--instancePath`                                                                                                                                                                                                                                                                                                                                                                                                    |
| Unique server ID                                     | A server identifier string that is unique for your deployment. Choose a relatively short string, as the value is recorded repeatedly in replicated historical data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `--serverId`                                                                                                                                                                                                                                                                                                                                                                                                        |
| Deployment ID                                        | The *deployment ID* is a random string generated using the `dskeymgr` command. It is paired with a *deployment ID password*, a random string you choose and must keep secret.Together, the deployment ID and password serve to generate the shared master key that DS servers in the deployment require for protecting shared encryption secrets. By default, they also serve to generate a private CA and keys for TLS to protect communication between DS servers.When you deploy multiple servers together, reuse the same deployment ID and password for each server installation.For details, refer to [Deployment IDs](../security-guide/pki.html#about-deployment-ids).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `--deploymentId`                                                                                                                                                                                                                                                                                                                                                                                                    |
| Deployment ID password                               | This is a random string that you choose, and that you must keep secret. It is paired with the deployment ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `--deploymentIdPassword[:env\|:file]`                                                                                                                                                                                                                                                                                                                                                                               |
| Root user DN                                         | The root user DN identifies the initial directory superuser (superuser) *(tooltip: \<div class="paragraph">&#xA;\<p>An account with full administration privileges to bypass access control evaluation, change access controls, and change administrative privileges. Analogous to the Linux root and Windows Administrator accounts.\</p>&#xA;\</div>)*. This user has privileges to perform all administrative operations, and isn't subject to access control. It's called the root user due to the similarity to the Linux root user.The default name is: `uid=admin`.For additional security in production environments, use a different name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `-D, --rootUserDn`                                                                                                                                                                                                                                                                                                                                                                                                  |
| Root user password                                   | The root user authenticates with simple, password-based authentication.Use a strong password here unless this server is only for evaluation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `-j, --rootUserPassword[:env\|:file]`                                                                                                                                                                                                                                                                                                                                                                               |
| Monitor user DN                                      | The monitor user DN identifies a user with the privilege to read monitoring data (`monitor-read`).The account is replicated by default, so use the same DN on each server.The name used in the documentation is the default name: `uid=monitor`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `--monitorUserDn`                                                                                                                                                                                                                                                                                                                                                                                                   |
| Monitor user password                                | The monitor user authenticates with simple, password-based authentication.The account is replicated by default, so use the same password on each server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `--monitorUserPassword[:env\|:file]`                                                                                                                                                                                                                                                                                                                                                                                |
| Fully qualified directory server domain name         | The server uses the fully qualified domain name (FQDN) for identification between replicated servers.Interactive setup suggests the hostname of the local host.If this server is only for evaluation, then you can use `localhost`.Otherwise, use an FQDN that other hosts can resolve to reach your server, and that matches the FQDN in the server certificate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `-h, --hostname`                                                                                                                                                                                                                                                                                                                                                                                                    |
| Administration port                                  | This is the service port to configure the server, run tasks, and respond to administrative requests.The port used in the documentation is `4444`.If the suggested port isn't free, interactive setup adds 1000 to the port number and tries again, adding 1000 until a free port is found.*Configure the firewall to allow access to this port from all connecting DS servers.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `--adminConnectorPort`                                                                                                                                                                                                                                                                                                                                                                                              |
| Securing the deployment                              | Setup requires a keystore with the keys for securing connections to the administration port, and to any other secure ports you configure during setup.You can choose to use the private PKI derived from the deployment ID and passwords. Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).You can also choose to use an existing keystore supported by the JVM, which can be either a file-based keystore or a PKCS#11 token. An existing keystore must protect the keystore and all private keys with the same PIN or password. For a PKCS#11 token, first configure access through the JVM.The `setup` command can take a PIN as the `--keyStorePassword` or `--trustStorePassword` to access the PKCS#11 token. In some cases, you provide the PKCS#11 token credentials in the configuration instead. In these cases, you don't need to provide the PIN in an argument to the `setup` command.Public key security is often misunderstood. Before making security choices for production systems, read [Cryptographic keys](../security-guide/pki.html).                                                                                                   | `--keyStorePath` `--keyStoreType` `-W, --keyStorePassword[:env\|:file]` `--keyStoreProviderName` (for PKCS#11) `--keyStoreProviderArg` (for PKCS#11) `--keyStoreProviderClass` (for FIPS) `-N, --certNickname``--trustStorePath` `--trustStoreType` `-T, --trustStorePassword[:env\|:file]` `--trustStoreProviderName` (for PKCS#11) `--trustStoreProviderArg` (for PKCS#11) `--trustStoreProviderClass` (for FIPS) |
| Start the server                                     | By default, the `setup` command does not start the server. Finish configuring the server, then use the `/path/to/opendj/bin/start-ds` command.If no further configuration is required, use the `setup --start` option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `-s, --start`                                                                                                                                                                                                                                                                                                                                                                                                       |
| LDAP and LDAPS port                                  | The reserved port for LDAP is `389`. The reserved port for LDAPS is `636`.Examples in the documentation use `1389` and `1636`, which are accessible to non-privileged users.If you install the server with access to privileged ports (< `1024`), and the reserved port is not yet in use, then interactive setup suggests the reserved port number. If the port is not free or cannot be used due to lack of privileges, interactive setup adds 1000 to the port number and tries again, repeatedly adding 1000 until a free port is found.The LDAP StartTLS extended operation negotiates a secure connection starting on the insecure LDAP port.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `-p, --ldapPort` `-q, --enableStartTls` `-Z, --ldapsPort`                                                                                                                                                                                                                                                                                                                                                           |
| HTTP and HTTPS ports                                 | The reserved port for HTTP is `80`. The reserved port for HTTPS is `443`. The interactive setup initially suggests `8080` and `8443` instead.If the initially suggested port is not free or cannot be used due to lack of privileges, interactive setup adds 1000 to the port number and tries again, repeatedly adding 1000 until a free port is found.Examples in the documentation use HTTPS on port `8443`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `--httpPort` `--httpsPort`                                                                                                                                                                                                                                                                                                                                                                                          |
| Replication port                                     | Port used for data replication messages. This port must be accessible externally from other DS servers.If this port is configured, the server acts as a replication server. It maintains a replication change log, which it exposes as an external change log by default.If the initially suggested port is not free or cannot be used due to lack of privileges, interactive setup adds 1000 to the port number and tries again, repeatedly adding 1000 until a free port is found.Examples in the documentation use `8989`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `-r, --replicationPort`                                                                                                                                                                                                                                                                                                                                                                                             |
| Bootstrap replication servers                        | Specify bootstrap server `host:port` pairs, where port is the server's replication port. The current server contacts the bootstrap servers to discover other servers in the deployment. The `host:port` pair may represent the current server if it is a bootstrap server.Specify the same list of bootstrap servers each time you set up a replica or standalone replication server.This option interacts with the `-r, --replicationPort` option as follows:- If both options are set, the server acts as a replication server. It connects to the specified bootstrap replication server(s) to discover other servers.

- If only the `-r, --replicationPort` option is set, the server acts as a replication server. It counts only itself as the bootstrap replication server. In production, specify the same list of at least two bootstrap servers every time, including when you set up the bootstrap servers.

- If only the `--bootstrapReplicationServer` option is set, the server acts as a standalone directory server. It connects to the specified bootstrap replication server(s).

- If neither option is set, the server is not configured for replication at setup time. | `--bootstrapReplicationServer`                                                                                                                                                                                                                                                                                                                                                                                      |
| Configure the server for use with other applications | For details, refer to [Setup profiles](setup-profiles.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `--profile` `--set`                                                                                                                                                                                                                                                                                                                                                                                                 |

---

---
title: Setup profiles
description: Learn how PingDS setup profiles configure a server for specific use cases, and review the default setup profiles and their parameters.
component: pingds
version: 8.1
page_id: pingds:install-guide:setup-profiles
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/setup-profiles.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-03-26T15:30:00Z
keywords: ["Extensibility", "Install", "LDAP", "Setup &amp; Configuration"]
section_ids:
  setup-profiles-base-dn: Different data under different base DNs
  check_profiles: Check profiles
  default_indexes: Default indexes
  default-setup-profiles: Default Setup Profiles
  am-config-6.5.0: AM Configuration Data Store 6.5.0
  am-cts-6.5.0: AM CTS Data Store 6.5.0
  am-identity-store-8.0.0: AM Identity Data Store 8.0.0
  am-identity-store-7.5.0: AM Identity Data Store 7.5.0
  am-identity-store-7.3.0: AM Identity Data Store 7.3.0
  am-identity-store-7.2.0: AM Identity Data Store 7.2.0
  am-identity-store-7.1.0: AM Identity Data Store 7.1.0
  am-identity-store-7.0.0: AM Identity Data Store 7.0.0
  am-identity-store-6.5.0: AM Identity Data Store 6.5.0
  ds-evaluation-8.0.0: DS Evaluation 8.0.0
  ds-proxied-server-7.0.0: DS Proxied Server 7.0.0
  ds-proxy-server-7.0.0: DS Proxy Server 7.0.0
  ds-user-data-7.0.0: DS User Data Store 7.0.0
  idm-repo-8.1.0: IDM External Repository 8.1.0
  idm-repo-8.0.0: IDM External Repository 8.0.0
  idm-repo-7.5.0: IDM External Repository 7.5.0
  idm-repo-7.4.0: IDM External Repository 7.4.0
  idm-repo-7.3.0: IDM External Repository 7.3.0
  idm-repo-7.2.0: IDM External Repository 7.2.0
  idm-repo-7.1.0: IDM External Repository 7.1.0
  idm-repo-7.0.0: IDM External Repository 7.0.0
  idm-repo-6.5.0: IDM External Repository 6.5.0
---

# Setup profiles

A setup profile lets you configure a server for a specific use case. Profiles greatly simplify the directory server setup process for such use cases, such as preparing a directory server to serve another Ping Identity Platform component product.

You can configure a setup profile using the `setup` command, or the `setup-profile` command after initial setup. The `setup-profile` command runs on a server that is offline.

Select a profile with the `--profile` option. Each profile has its own parameters, some of which have default values. You specify profile parameters with `--set` options.

The profile selection option takes the form `--profile profileName[:version]`. If you do not specify the optional `:version` portion of the argument, the `setup` command uses the current DS software version, falling back to the previous version if the current version does not match an available profile. Repeat the `--profile` option to apply multiple setup profiles.

An option to set a parameter takes the form `--set[:env|:file] profileName/parameterName:value` where:

* `profileName/` indicates which profile the parameter applies to.

  This part is only required when you specify multiple profiles and the parameter is available in more than one of the specified profiles.

  The `profileName` is case-insensitive.

* `parameterName` specifies the parameter to set.

* `value` specifies the value the parameter takes when the `setup` command applies the profile.

Use the `setup --help-profiles` or `setup-profile --help` command to list available profiles.

Use the `--help-profile profileName[:version]` option to list the parameters for the specified profile.

## Different data under different base DNs

Nothing prevents you from configuring multiple setup profiles to use the same base DN for different directory data. Keep different directory data under different base DNs.

When the different data sets are incompatible, reusing a base DN can lead to errors, such as the following:

```
category=CONFIG severity=ERROR msgID=116 msg=An error occurred while trying
to initialize a backend loaded from class org.opends.server.backends.jeb.JEBackend
with the information in configuration entry ds-cfg-backend-id=cfgStore,cn=Backends,cn=config:
An error occurred while attempting to register the base DNs [dc=reused,dc=base,dc=dn] in the Directory Server:
Unwilling to Perform: Unable to register base DN dc=reused,dc=base,dc=dn with the Directory Server
for backend cfgStore because that base DN is already registered for backend amCts.
This backend will be disabled.
```

## Check profiles

The `opendj/profiles.version` file lists the profiles selected at setup time:

```console
$ cat /path/to/opendj/config/profiles.version
```

Output

```none
ds-evaluation:8.1.1
```

## Default indexes

For new backends, setup profiles create the following default indexes:

* `ds-certificate-fingerprint` (equality index)

* `ds-certificate-subject-dn` (equality index)

* `member` (equality index)

* `uid` (equality index)

* `uniqueMember` (equality index)

When a profile adds a backend with default user indexes, it also creates the following default indexes:

* `cn` (equality and substring indexes)

* `givenName` (equality and substring indexes)

* `mail` (equality and substring indexes)

* `sn` (equality and substring indexes)

* `telephoneNumber` (equality and substring indexes)

## Default Setup Profiles

This page lists default profiles with their parameters.

### AM Configuration Data Store 6.5.0

The `am-config:6.5.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing config\
  Default: `--set am-config/backendName:cfgStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store AM's configuration in\
  Default: `--set am-config/baseDn:ou=am-config`\
  Syntax: DN

* `amConfigAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### AM CTS Data Store 6.5.0

The `am-cts:6.5.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing tokens\
  Default: `--set am-cts/backendName:amCts`\
  Syntax: Name

* `baseDn`

  The base DN to use to store AM's tokens in\
  Default: `--set am-cts/baseDn:ou=tokens`\
  Syntax: DN

* `amCtsAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

* `tokenExpirationPolicy`

  Token expiration and deletion\
  Default: `--set am-cts/tokenExpirationPolicy:am`\
  \
  This parameter takes one of the following values:

  * `am`: AM CTS reaper manages token expiration and deletion

  * `am-sessions-only`: AM CTS reaper manages SESSION token expiration and deletion. DS manages expiration and deletion for all other token types. AM continues to send notifications about session expiration and timeouts to agents

  * `ds`: DS manages token expiration and deletion. AM session-related functionality is impacted and notifications are not sent

### AM Identity Data Store 8.0.0

The `am-identity-store:8.0.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing identities\
  Default: `--set am-identity-store/backendName:amIdentityStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store identities in\
  Default: `--set am-identity-store/baseDn:ou=identities`\
  Syntax: DN

* `amIdentityStoreAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### AM Identity Data Store 7.5.0

The `am-identity-store:7.5.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing identities\
  Default: `--set am-identity-store/backendName:amIdentityStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store identities in\
  Default: `--set am-identity-store/baseDn:ou=identities`\
  Syntax: DN

* `amIdentityStoreAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### AM Identity Data Store 7.3.0

The `am-identity-store:7.3.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing identities\
  Default: `--set am-identity-store/backendName:amIdentityStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store identities in\
  Default: `--set am-identity-store/baseDn:ou=identities`\
  Syntax: DN

* `amIdentityStoreAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### AM Identity Data Store 7.2.0

The `am-identity-store:7.2.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing identities\
  Default: `--set am-identity-store/backendName:amIdentityStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store identities in\
  Default: `--set am-identity-store/baseDn:ou=identities`\
  Syntax: DN

* `amIdentityStoreAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### AM Identity Data Store 7.1.0

The `am-identity-store:7.1.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing identities\
  Default: `--set am-identity-store/backendName:amIdentityStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store identities in\
  Default: `--set am-identity-store/baseDn:ou=identities`\
  Syntax: DN

* `amIdentityStoreAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### AM Identity Data Store 7.0.0

The `am-identity-store:7.0.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing identities\
  Default: `--set am-identity-store/backendName:amIdentityStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store identities in\
  Default: `--set am-identity-store/baseDn:ou=identities`\
  Syntax: DN

* `amIdentityStoreAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### AM Identity Data Store 6.5.0

The `am-identity-store:6.5.0` profile has the following parameters:

* `backendName`

  Name of the backend for storing identities\
  Default: `--set am-identity-store/backendName:amIdentityStore`\
  Syntax: Name

* `baseDn`

  The base DN to use to store identities in\
  Default: `--set am-identity-store/baseDn:ou=identities`\
  Syntax: DN

* `amIdentityStoreAdminPassword`

  Password of the administrative account that AM uses to bind to OpenDJ\
  Syntax: Password

### DS Evaluation 8.0.0

The `ds-evaluation:8.0.0` profile has the following parameters:

* `generatedUsers`

  Specifies the number of generated user entries to import. The evaluation profile always imports entries used in documentation examples, such as uid=bjensen. Optional generated users have RDNs of the form uid=user.%d, yielding uid=user.0, uid=user.1, uid=user.2 and so on. All generated users have the same password, "password". Generated user entries are a good fit for performance testing with tools like addrate and searchrate\
  Default: `--set ds-evaluation/generatedUsers:100000`\
  Syntax: Number

* `useOutdatedPasswordStorage`

  Use Salted SHA-512 as the password storage scheme for the import and default password policy for users.\
  Default: `--set ds-evaluation/useOutdatedPasswordStorage:false`\
  \
  This parameter takes one of the following values:

  * `true`

  * `false`

### DS Proxied Server 7.0.0

The `ds-proxied-server:7.0.0` profile has the following parameters:

* `proxyUserDn`

  The proxy user service account DN. This will be used for authorization and auditing proxy requests.\
  Default: `--set ds-proxied-server/proxyUserDn:uid=proxy`\
  Syntax: DN

* `proxyUserCertificateSubjectDn`

  The subject DN of the proxy user's certificate. The proxy must connect using mutual TLS with a TLS client certificate whose subject DN will be mapped to the proxy service account.\
  Default: `--set ds-proxied-server/proxyUserCertificateSubjectDn:CN=DS,O=ForgeRock.com`\
  Syntax: DN

* `baseDn`

  Base DN for user information in the server. Multiple base DNs may be provided by using this option multiple times. If no base DNs are defined then the server will allow proxying as any user, including administrator accounts.\
  Syntax: DN

### DS Proxy Server 7.0.0

The `ds-proxy-server:7.0.0` profile has the following parameters:

* `backendName`

  Name of the proxy backend for storing proxy configuration\
  Default: `--set ds-proxy-server/backendName:proxyRoot`\
  Syntax: Name

* `bootstrapReplicationServer`

  Bootstrap replication server(s) to contact periodically in order to discover remote servers\
  Syntax: host:port or configuration expression

* `rsConnectionSecurity`

  Connection security type to use to secure communication with remote servers\
  Default: `--set ds-proxy-server/rsConnectionSecurity:ssl`\
  \
  This parameter takes one of the following values:

  * `ssl`: Use SSL

  * `start-tls`: Use Start TLS

* `keyManagerProvider`

  Name of the key manager provider used for authenticating the proxy in mutual-TLS communications with backend server(s)\
  Default: `--set ds-proxy-server/keyManagerProvider:PKCS12`\
  Syntax: Name or configuration expression

* `trustManagerProvider`

  Name of the trust manager provider used for trusting backend server(s) certificate(s)\
  Syntax: Name or configuration expression

* `certNickname`

  Nickname(s) of the certificate(s) that should be sent to the server for SSL client authentication.\
  Default: `--set ds-proxy-server/certNickname:ssl-key-pair`\
  Syntax: Name or configuration expression

* `primaryGroupId`

  Replication domain group ID of directory server replicas to contact when available before contacting other replicas. If this option is not specified then all replicas will be treated the same (i.e all remote servers are primary)\
  Syntax: String or configuration expression

* `baseDn`

  Base DN for user information in the Proxy Server.Multiple base DNs may be provided by using this option multiple times.If no base DNs are defined then the proxy will forward requests to all public naming contexts of the remote servers\
  Syntax: DN or configuration expression

### DS User Data Store 7.0.0

The `ds-user-data:7.0.0` profile has the following parameters:

* `backendName`

  Name of the backend to be created by this profile\
  Default: `--set ds-user-data/backendName:userData`\
  Syntax: Name

* `baseDn`

  Base DN for your users data.\
  Syntax: DN

* `ldifFile`

  Path to an LDIF file containing data to import. Use this option multiple times to specify multiple LDIF files. The path is absolute, or relative to the directory where the profile is defined\
  Syntax: File or directory path

* `addBaseEntry`

  Create entries for specified base DNs when the 'ldifFile' parameter is not used. When this option is set to 'false' and the 'ldifFile' parameter is not used, create an empty backend.\
  Default: `--set ds-user-data/addBaseEntry:true`\
  \
  This parameter takes one of the following values:

  * `true`

  * `false`

### IDM External Repository 8.1.0

The `idm-repo:8.1.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 8.0.0

The `idm-repo:8.0.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 7.5.0

The `idm-repo:7.5.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 7.4.0

The `idm-repo:7.4.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 7.3.0

The `idm-repo:7.3.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 7.2.0

The `idm-repo:7.2.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 7.1.0

The `idm-repo:7.1.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 7.0.0

The `idm-repo:7.0.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

### IDM External Repository 6.5.0

The `idm-repo:6.5.0` profile has the following parameters:

* `backendName`

  IDM repository backend database name\
  Default: `--set idm-repo/backendName:idmRepo`\
  Syntax: Name

* `domain`

  Domain name translated to the base DN for IDM external repository data. Each domain component becomes a "dc" (domain component) of the base DN. This profile prefixes "dc=openidm" to the result. For example, the domain "example.com" translates to the base DN "dc=openidm,dc=example,dc=com".\
  Default: `--set idm-repo/domain:example.com`\
  Syntax: Domain name

---

---
title: Uninstallation
description: Remove PingDS server files installed from the zip, Debian package, RPM package, or Windows MSI.
component: pingds
version: 8.1
page_id: pingds:install-guide:uninstall
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/uninstall.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Install", "LDAP"]
section_ids:
  uninstall-cli: Uninstall .zip
  uninstall-deb: Uninstall the Debian package
  uninstall-rpm: Uninstall the RPM package
  uninstall-msi: Uninstall the Windows MSI
  gui: GUI
  powershell: PowerShell
---

# Uninstallation

## Uninstall .zip

Follow these steps to remove software installed from the cross-platform .zip:

1. Log in as the user who installed and runs the server.

2. Stop the server:

   ```console
   $ /path/to/opendj/bin/stop-ds --quiet
   ```

3. Delete the files manually:

   ```console
   $ rm -rf /path/to/opendj
   ```

## Uninstall the Debian package

When you uninstall the Debian package from the command-line, the server is stopped if it is running:

1. Purge the package from your system:

   ```console
   $ sudo dpkg --purge opendj
   ```

2. Remove any remaining server configuration files and directory data:

   ```console
   $ sudo rm -rf /opt/opendj
   ```

## Uninstall the RPM package

When you uninstall the RPM package from the command-line, the server is stopped if it is running:

1. Remove the package from your system:

   ```none
   root# rpm -e opendj
   ```

2. Remove the server configuration files and any directory data:

   ```console
   $ sudo rm -rf /opt/opendj
   ```

## Uninstall the Windows MSI

When you uninstall the files installed from the Windows installer package, only the installed files are removed.

### GUI

1. Open Control Panel as Windows Administrator.

2. Browse to the page to uninstall a program.

3. Find PingDS in the list and uninstall it.

4. Manually remove the server configuration files and any directory data.

### PowerShell

1. Open PowerShell as Windows Administrator.

2. Use the `msiexec` command.

   The following command quietly removes installed files:

   ```powershell
   msiexec /x DS-8.1.1.msi /q
   ```

3. Manually remove the server configuration files and any directory data.

---

---
title: Unpack files
description: Unpack PingDS server files using the cross-platform zip, Debian package, RPM package, or Windows MSI installer before running setup.
component: pingds
version: 8.1
page_id: pingds:install-guide:install-files
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/install-files.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-03-04T12:00:00Z
keywords: ["Install", "LDAP"]
section_ids:
  install-files-zip: Unpack the cross-platform zip
  install-files-deb: Use the Debian package
  install-files-rpm: Use the RPM package
  install-files-msi: Use the Windows MSI
  gui: GUI
  powershell: PowerShell
---

# Unpack files

The following procedures only unpack the server files. You must then run the `setup` command to set up the server:

## Unpack the cross-platform zip

You can use the .zip delivery on any supported operating system.

1. [Review requirements for installation](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

2. Unpack the cross-platform .zip file in the file system directory where you want to install the server.

   Perform this step as a user with the same file system permissions as the user who will run the `setup` command.

   The `setup` command uses the directory where you unzipped the files as the installation directory. It does not ask you where to install the server. If you want to install elsewhere on the file system, unzip the files in that location.

## Use the Debian package

On Debian and related Linux distributions, such as Ubuntu, you can unpack files using the Debian package:

1. [Review requirements for installation](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

   In particular, install a Java runtime environment (JRE) if none is installed yet.

2. Install the server package:

   ```console
   $ sudo dpkg -i DS*.deb
   ```

   The Debian package:

   * Installs server files in the `/opt/opendj` directory.

   * Adds documentation files under the `/usr/share/doc/opendj` directory.

   * Adds man pages under the `/opt/opendj/share/man` directory.

   * Generates systemd service files `/etc/default/opendj` and `/etc/systemd/system/opendj.service`.

   By default, the system superuser (`root`) owns the files. The DS server can listen on privileged ports like `389` and `636`.

3. (Optional) Change the systemd configuration:

   * Edit `/etc/default/opendj` directly to set any environment variables DS requires.

     For example, set environment variables for [property value substitutions](../configref/expressions.html).

   * Use the `systemctl edit` command to change the service configuration; for example, to run DS as a specific user.

     The command makes the changes in a new `override.conf` file that systemd reads automatically.

   The changes you make in this way are independent of upgrades and changes to the package defaults. To avoid compatibility problems, don't edit `/etc/systemd/system/opendj.service` directly.

4. Set up the server with the `setup` command, `sudo /opt/opendj/setup`.

## Use the RPM package

On Red Hat and related Linux distributions, such as Fedora and CentOS, you can unpack files using the RPM package:

1. [Review requirements for installation](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

   In particular, install a Java runtime environment (JRE) if none is installed yet. You might need to download an RPM to install the Java runtime environment, and then install the RPM by using the `rpm` command:

   ```none
   $ su
   Password:
   root# rpm -ivh jre-*.rpm
   ```

2. Install the server package:

   ```none
   root# rpm -i DS*.rpm
   ```

   The RPM package:

   * Installs server files in the `/opt/opendj` directory.

   * Adds man pages under the `/opt/opendj/share/man` directory.

   * Generates systemd service files `/etc/default/opendj` and `/etc/systemd/system/opendj.service`.

   By default, the system superuser (`root`) owns the files. The DS server can listen on privileged ports like `389` and `636`.

3. (Optional) Change the systemd configuration:

   * Edit `/etc/default/opendj` directly to set any environment variables DS requires.

     For example, set environment variables for [property value substitutions](../configref/expressions.html).

   * Use the `systemctl edit` command to change the service configuration; for example, to run DS as a specific user.

     The command makes the changes in a new `override.conf` file that systemd reads automatically.

   The changes you make in this way are independent of upgrades and changes to the package defaults. To avoid compatibility problems, don't edit `/etc/systemd/system/opendj.service` directly.

4. Set up the server with the `setup` command, `/opt/opendj/setup`.

   By default, the server starts in run levels 2, 3, 4, and 5.

## Use the Windows MSI

Make sure you can log on as Windows Administrator to install the files and run the `setup.bat` command.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Prevent antivirus and intrusion detection systems from interfering with DS software.Before using DS software with antivirus or intrusion detection software, consider the following potential problems:- **Interference with normal file access**

  Antivirus and intrusion detection systems that perform virus scanning, sweep scanning, or deep file inspection are not compatible with DS file access, particularly write access.

  Antivirus and intrusion detection software have incorrectly marked DS files as suspect to infection, because they misinterpret normal DS processing.

  *Prevent antivirus and intrusion detection systems from scanning DS files*, except these folders:

  * `C:\path\to\opendj\bat\`

    Windows command-line tools

  * `/path/to/opendj/bin/`

    Linux command-line tools

  * `/path/to/opendj/extlib/`

    Optional `.jar` files used by custom plugins

  * `/path/to/opendj/lib/`

    Scripts and libraries shipped with DS servers

- **Port blocking**

  Antivirus and intrusion detection software can block ports that DS uses to provide directory services.

  Make sure that your software does not block the ports that DS software uses. For details, refer to [Administrative access](../security-guide/os.html#os-admin).

- **Negative performance impact**

  Antivirus software consumes system resources, reducing resources available to other services including DS servers.

  Running antivirus software can therefore have a significant negative impact on DS server performance. Make sure that you test and account for the performance impact of running antivirus software before deploying DS software on the same systems. |

### GUI

1. [Review requirements for installation](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

2. Start the wizard as Windows Administrator:

   1. If you are logged on as Administrator, double-click the Windows installer package, `DS-8.1.1.msi`.

   2. If you are logged on as a regular user, hold the shift key while right-clicking `DS-8.1.1.msi`, select Run as different user, and run the installer as Windows Administrator.

3. (Optional) Set the Destination Folder to the location for DS server files.

   * The default location is under `Program Files` on the system drive.

     For example, if the system drive is `C:`, the default location is `C:\Program Files (x86)\PingDS Server\`.

   * The Windows installer has 32-bit dependencies but DS runs as a 64-bit Java application.

4. Complete the wizard.

   The installation program writes DS server files to the destination folder.

   You must run the `setup.bat` command in the destination folder *as Administrator* to set up DS.

### PowerShell

1. [Review requirements for installation](https://docs.pingidentity.com/pingds/release-notes/requirements.html).

2. Start PowerShell as Windows Administrator:

   1. If you are logged on as Windows Administrator, double-click Start > Windows PowerShell.

   2. If you are logged on as a regular user, hold the shift key while right-clicking Start > Windows PowerShell and select Run as Administrator.

3. Use the Microsoft `msiexec.exe` command to install the files.

   The following example installs DS server files under `C:\Users\opendj\ds`. It writes an `install.log` file in the current folder:

   ```powershell
   msiexec /i C:\Users\opendj\Downloads\DS-8.1.1.msi /l* install.log /q INSTALLDIR="C:\Users\opendj\ds"
   ```

   The installation program writes DS server files to the destination folder.

   You must run the `setup.bat` command in the destination folder *as Administrator* to set up DS.

---

---
title: Use your own cryptographic keys
description: Install PingDS using your own cryptographic keys, with guidance on keystore options, certificate requirements, and TLS configuration.
component: pingds
version: 8.1
page_id: pingds:install-guide:setup-own-keys
canonical_url: https://docs.pingidentity.com/pingds/8.1/install-guide/setup-own-keys.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-28T18:16:26Z
keywords: ["Install", "LDAP", "Security", "Setup &amp; Configuration"]
section_ids:
  setup_options: Setup options
  important_features: Important features
  replication_and_tls: Replication and TLS
  client_operations_and_tls: Client operations and TLS
  example: Example
---

# Use your own cryptographic keys

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you set up a DS server with your own keys for PKI, account for the following points:- Use a deployment ID and password.

  Some DS features depend on the shared master key generated from the [deployment ID and password](../security-guide/pki.html#about-deployment-ids). For example, the `dsbackup` command depends on the shared master key for encryption.

- If you plan to store the shared master key in an HSM, read the documentation carefully *before you install DS*.

  When you set up the server, you must avoid accidentally encrypting data while using the wrong shared master key. For details, refer to [PKCS#11 HSM](../security-guide/pki-hsm.html).

- Make sure AM, IDM, and all other client applications can trust DS server certificates.

  Learn about trusting server certificates in the documentation for each client application. |

## Setup options

The `setup` command has options to simplify setting up a server with existing keys:

| For                                                           | Use                                                                                                                                                                                                            |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Keystores containing server key pairs                         | `--keyStorePath` `--keyStoreType` `-W, --keyStorePassword[:env\|:file]` `--keyStoreProviderName` (for PKCS#11) `--keyStoreProviderArg` (for PKCS#11) `--keyStoreProviderClass` (for FIPS) `-N, --certNickname` |
| Truststores containing trusted CA or self-signed certificates | `--trustStorePath` `--trustStoreType` `-T, --trustStorePassword[:env\|:file]` `--trustStoreProviderName` (for PKCS#11) `--trustStoreProviderArg` (for PKCS#11) `--trustStoreProviderClass` (for FIPS)          |

## Important features

* If the keystore file that holds the server key pair protects the server key with a password, that password must match the password for the entire store.

  DS doesn't support accessing a keystore and accessing keystore entries with separate passwords.

* If you are using an HSM, also read [PKCS#11 HSM](../security-guide/pki-hsm.html).

* If you are using PEM format keys, read [PEM format keys](../security-guide/key-management.html#use-pem-keys).

* CAs can optionally set X.509 key usage extensions in server certificates.

  If the CA does set key usage extensions, make sure it includes at least the required settings:

  | Protocol    | X.509 extension    | Required settings                                                                                                                                                                        |
  | ----------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | HTTP        | `KeyUsage`         | `digitalSignature` `keyEncipherment`                                                                                                                                                     |
  |             | `ExtendedKeyUsage` | `serverAuth` (TLS server authentication)                                                                                                                                                 |
  | LDAP        | `KeyUsage`         | `digitalSignature` `keyEncipherment`                                                                                                                                                     |
  |             | `ExtendedKeyUsage` | `serverAuth` (TLS server authentication)                                                                                                                                                 |
  | Replication | `KeyUsage`         | `digitalSignature` `keyEncipherment`                                                                                                                                                     |
  |             | `ExtendedKeyUsage` | `clientAuth` (TLS client authentication)(1) `serverAuth` (TLS server authentication) `1.3.6.1.4.1.36733.2.1.10.1` (for [Trusted replicas (advanced)](../config-guide/repl-trusted.html)) |

  (1) Replication requires both TLS server and TLS client roles.

### Replication and TLS

Public CAs sign certificates for public networks where servers and client applications are separate entities. By default, these CAs issue separate certificates for servers and client applications. This makes sense in a network of web servers and web browsers.

In contrast, replication traffic is peer-to-peer. In replication, each server plays both client and server roles using the same certificate for mutual TLS (mTLS) authentication. Whether it's requesting or responding, it's still the same server.

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For replication, ask your CA for an mTLS certificate for server-to-server authentication, not a web server certificate.Work with your CA to make sure the replication certificate has `clientAuth` and `serverAuth` in its `ExtendedKeyUsage`. |

### Client operations and TLS

Make sure certificates have the `clientAuth` extension when the server acts as a client *and the remote server requires certificate-based client authentication for TLS*.

This can arise when DS acts as:

* An [LDAP proxy](../config-guide/proxy.html), a client of remote LDAP servers.

* An [OpenTelemetry](../monitoring-guide/opentelemetry.html) client, pushing data to a remote OTLP endpoint.

* A client of IDM for [password synchronization](https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/chap-sync-dj.html).

## Example

Follow steps similar to these to install a DS replica with existing cryptographic keys:

1. [Install the server files](install-files.html).

2. Generate a deployment ID unless you already have one:

   ```console
   $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-id
   ```

   Save the deployment ID and its deployment password. Keep the ID and the password safe, and keep the password secret. Use the same deployment ID and password for all the servers in the same environment.

   > **Collapse: About deployment IDs**
   >
   > A *deployment ID* is a random string generated using the `dskeymgr` command. It's a deployment identifier, not a key, but it is used with a password to generate keys.
   >
   > A *deployment ID password* is a secret string at least 8 characters long that you choose.
   >
   > The two form a pair. You must have the deployment ID password to use the deployment ID.
   >
   > Each deployment requires a *single, unique deployment ID and its password*. DS uses the pair to:
   >
   > * Protect the keys to encrypt and decrypt backup files and directory data.
   >
   > * Generate the TLS key pairs to protect secure connections, unless you provide your own.
   >
   > Store your deployment ID and password in a safe place, and reuse them when configuring other servers in the same deployment.
   >
   > The DS `setup` and `dskeymgr` commands use the pair to generate the following:
   >
   > * (Required) A shared master key for the deployment.
   >
   >   DS replicas share secret keys for data encryption and decryption. DS servers encrypt backend data, backup files, and passwords, and each replica must be able to decrypt data encrypted on another peer replica.
   >
   >   To avoid exposing secret keys, DS servers encrypt secret keys with a shared master key. DS software uses a deployment ID and its password to derive the master key.
   >
   > * (Optional) A private PKI for trusted, secure connections.
   >
   >   A PKI serves to secure network connections from clients and other DS servers. The PKI is a trust network, requiring trust in the CA that signs public key certificates.
   >
   >   Building a PKI can be complex. You can use self-signed certificates, but you must distribute each certificate to each server and client application. You can pay an existing CA to sign certificates, but that has a cost, and leaves control of trust with a third party. You can set up a CA or certificate management software, but that can be a significant effort and cost. As a shortcut to setting up a private CA, DS software uses deployment IDs and passwords.
   >
   >   DS software uses the deployment ID and its password to generate key pairs without storing the CA private key.
   >
   > Learn more in [Deployment IDs](../security-guide/pki.html#about-deployment-ids).

3. Set the deployment ID as the value of the environment variable, `DEPLOYMENT_ID`:

   ```console
   $ export DEPLOYMENT_ID=your-deployment-id
   ```

   Examples in the documentation show this environment variable as a reminder to use your own deployment ID.

4. Run the `setup` command with the appropriate options.

   The example command uses these keys:

   * A CA certificate with alias `ca-cert` in a `truststore` file.

     You provide this.

   * A server key pair with alias `ssl-key-pair` in a `keystore` file.

     You provide this.

   * A shared master key with alias `master-key`.

     You don't provide this directly. It's based on the deployment ID and password.

   The example has your keys in separate PKCS#12 truststore and keystore files for emphasis. Use a single store file for all your keys if it's easier to deploy and manage.

   Set up a directory server using your own keys. Adapt the command for your use:

   ```console
   $ /path/to/opendj/setup \
    --serverId own-keys \
    --deploymentId $DEPLOYMENT_ID \
    --deploymentIdPassword password \
    --trustStorePath /path/to/truststore \
    --trustStoreType PKCS12 \
    --trustStorePassword password \
    --certNickname ssl-key-pair \
    --keyStorePath /path/to/keystore \
    --keyStoreType PKCS12 \
    --keyStorePassword password \
    --rootUserDN uid=admin \
    --rootUserPassword password \
    --monitorUserPassword password \
    --hostname localhost \
    --adminConnectorPort 4444 \
    --ldapPort 1389 \
    --enableStartTls \
    --ldapsPort 1636 \
    --httpsPort 8443 \
    --replicationPort 8989 \
    --bootstrapReplicationServer rs1.example.com:8989 \
    --bootstrapReplicationServer rs2.example.com:8989 \
    --acceptLicense
   ```

   **Uses of keys in the example**

   | Store                             | Key            | Uses                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | --------------------------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `/path/to/keystore`               | `ssl-key-pair` | Server key pair presented to client applications when establishing a secure TLS connection as a server.The connectors for administration, HTTP, LDAP, and replication use this through the [Key Manager Provider](../configref/objects-key-manager-provider.html) configuration.Include one key pair for all secure TLS connections.                                                                                                                                                                                                                                                                                                |
   | `/path/to/truststore`             | `ca-cert`      | CA certificate to trust other server certificates:- When establishing a TLS connection as a client.

     Replication uses mTLS. For the server certificates used for replication, always trust the CA certificate or certificates for each server if they're self-signed.

   - To trust client application certificates when a connector's `ssl-client-auth-policy` is `required` or `optional`.The connectors for administration, HTTP, LDAP, and replication use this through the [Trust Manager Provider](../configref/objects-trust-manager-provider.html) configuration.Trust as many CA or self-signed certificates as necessary. |
   | `/path/to/opendj/config/keystore` | `master-key`   | Shared master key to wrap and unwrap symmetric keys for data encryption.The DS Crypto Manager uses this.All the DS servers in the deployment must share the same master key for wrapping and unwrapping symmetric keys. Provide the same deployment ID and password for each DS server in the same replicated deployment.                                                                                                                                                                                                                                                                                                           |

   When DS uses existing store files, its configuration directly references the files. Don't move the files without changing any applicable [Key Manager Provider](../configref/objects-key-manager-provider.html) and [Trust Manager Provider](../configref/objects-trust-manager-provider.html) settings in the server configuration.

   When you provide keystore and truststore passwords as strings like this example, the `setup` command records them in `opendj/config/ssl-filename.pin` files. filename represents the name of the store file. In this example, the password files are:

   * `/path/to/opendj/config/ssl-keystore.pin`

   * `/path/to/opendj/config/ssl-truststore.pin`

   Read [Property value substitution](../configref/expressions.html) to learn about using variables instead in the DS configuration.

5. Finish configuring the server.

6. Start the server:

   ```console
   $ /path/to/opendj/bin/start-ds
   ```
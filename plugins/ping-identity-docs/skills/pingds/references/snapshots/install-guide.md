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
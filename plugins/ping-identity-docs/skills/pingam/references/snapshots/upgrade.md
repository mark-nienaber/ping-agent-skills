---
title: Configure secret stores after upgrade
description: Configure secret stores on all servers in your site after upgrading PingAM to ensure all cryptographic keys and credentials are available across instances
component: pingam
version: 8.1
page_id: pingam:upgrade:upgrade-create-secret-stores
canonical_url: https://docs.pingidentity.com/pingam/8.1/upgrade/upgrade-create-secret-stores.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Upgrade", "Security"]
page_aliases: ["upgrade-guide:upgrade-create-secret-stores.adoc"]
section_ids:
  upgrade-secret-stores: Redeploy secret stores to a site after upgrade
---

# Configure secret stores after upgrade

Secret stores are repositories of cryptographic keys, key pairs, and credentials.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The upgrade process doesn't create all the demo key aliases created during a fresh install. This includes, for example, the aliases required for the [IoT service](../security/secret-mapping.html#iot-default-secret-IDs). If you want to use services that require these demo aliases, add the corresponding keys and mappings after you have upgraded.

* Although the configuration for secret stores is available to any upgraded server in the site, **the upgrade process only creates the relevant secret store files on the AM instance where you run the upgrade process**. |

Follow these steps to make the secret stores available to other servers in the site:

## Redeploy secret stores to a site after upgrade

You can reconfigure the secret stores and their mappings after upgrade. However, we recommend that you follow the steps in this procedure to ensure all secrets are available to all the instances in the site, and later on, you make additional changes to your environment.

The upgrade process creates several secret stores, globally and by realm, depending on the features configured in AM:

1. Go to Configuration > Secret Stores, and review the global secret stores created for your environment.

   * Make sure the keystores configured exist on the other servers within the site. You might need to copy the keystores across or make them available in some other way.

   * Make sure directories configured in file system secret stores and their content exist on the other servers within the site. You might need to copy the directories across or make them available in some other way.

2. Go to Realms > *realm name* > Secret Stores, and perform the same actions you took for the global secret stores.

   Realm-based secret stores are created for those features that support different keystore configurations by realm. For example, SAML 2.0, or the persistent cookie decision node.

   To find the realm-based secret stores, go to Realms > *realm name* > Secret Stores. The secrets themselves are stored in the `/path/to/am/security/secrets/realms/root/realm-name/secret-store-name` directory.

   Repeat this step for each of the realms you have configured.

3. Deploy the new AM `.war` file on the rest of the AM servers.

4. When the site is up, and before opening the service to end users, review the secret label mappings of the new secret stores and change them as required.

   For example, the upgrade process could have created secret stores for features you aren't using. These secret stores could have mappings to secrets that don't exist. It's advisable to remove unused secret mappings in production environments.

   Learn more about available secret labels in [Secret label default mappings](../security/secret-mapping.html#secret-label-mappings).

   > **Collapse: Reference: SAML 2.0 mappings after upgrade**
   >
   > AM is flexible regarding the configuration of secrets for SAML 2.0. Therefore, migrating the different combinations may create a high number of secret labels in your environment.
   >
   > As a rule of thumb, AM configures providers that were using the same key aliases *in the same order*, to use the same secret labels. If this rule can't be satisfied, the upgrade process creates new secret labels for the provider by assigning it a secret label identifier.

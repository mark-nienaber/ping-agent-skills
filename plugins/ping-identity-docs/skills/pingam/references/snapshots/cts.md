---
title: Manage CTS tokens
description: Configure PingAM to encrypt or compress CTS tokens stored in the token store, and manage encryption and compression properties across your deployment
component: pingam
version: 8.1
page_id: pingam:cts:cts-token-managing
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-token-managing.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration"]
page_aliases: ["cts-guide:cts-token-managing.adoc"]
section_ids:
  proc-enable-encryption-compression-CTS: Configure AM to encrypt and compress CTS tokens for storage
---

# Manage CTS tokens

You can configure AM to encrypt or compress CTS tokens as they are stored in the token store. The following properties, disabled by default, are associated with token encryption and compression:

* `com.sun.identity.session.repository.enableEncryption`

  Supports encryption of CTS tokens. Default: `false`.

* `com.sun.identity.session.repository.enableCompression`

  Enables GZip-based compression of CTS tokens. Default: `false`.

* `com.sun.identity.session.repository.enableAttributeCompression`

  Supports compression over and above the GZip-based compression of CTS tokens. Default: `false`.

|   |                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Compression can undermine the security of encryption. You should evaluate this threat, according to your use case, before you enable compression *and* encryption. |

## Configure AM to encrypt and compress CTS tokens for storage

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When encryption or compression properties are changed, all previous tokens in the LDAP store will be unreadable, and any authenticated sessions will be invalidated. As a result, the user will need to log in again. |

1. Go to Configure > Server Defaults > Advanced.

2. Find the property you want to enable in the Property Name column.

3. Replace the `false` value with `true` in the Property Value column.

4. Click Save Changes.

5. Enable the same property on every AM instance within the site.

   Failure to do so may cause unexpected issues storing and reading tokens across the environment.

6. Restart the AM servers for the changes to take effect.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configuring the CTS to encrypt and store tokens incurs a performance penalty for AM. If you need to encrypt the stored tokens in your environment, consider configuring the CTS token store DS instance to encrypt the data instead. For more information about encrypting a DS instance, see the [Data encryption](https://docs.pingidentity.com/pingds/8.1/security-guide/data.html) in the PingDS documentation. |

---

---
title: Manage expired CTS tokens
description: "Manage expired CTS tokens by configuring PingAM's reaper or delegating to PingDS to free resources in PingAM servers"
component: pingam
version: 8.1
page_id: pingam:cts:cts-reaper
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-reaper.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-01T14:11:17Z
keywords: ["CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Directory Server"]
page_aliases: ["cts-guide:cts-reaper.adoc"]
section_ids:
  manage_expired_tokens_with_the_am_cts_reaper: Manage expired tokens with the AM CTS reaper
  manage_expired_tokens_using_ds: Manage expired tokens using DS
  cts-ds-reaper-all-tokens: Let DS manage CTS tokens (ignore session capabilities)
  cts-ds-reaper-no-sessions: Let DS manage CTS tokens (retain session capabilities)
  cts-am-reaper: Re-enable the AM reaper
---

# Manage expired CTS tokens

Tokens in the CTS store have a limited *time to live*, after which they expire and must be pruned. By default, AM manages expired tokens by using its own reaper. You can, however, delegate this task to DS.

Although both solutions work equally well, using DS to manage token expiration instead of AM's reaper frees up resources in AM servers that can then be used for policy or authorization requests.

The following topics explain the two methods of managing expired CTS tokens in detail.

## Manage expired tokens with the AM CTS reaper

When an AM server modifies a token in the CTS token store, it takes responsibility for managing that token when it expires. Each AM server maintains a local cache of expired tokens to delete, and when to delete them.

Using the local reaper cache reduces the number of searches to the CTS store to determine expired tokens to delete. This improves overall cluster performance. Servers still search the CTS store for expired tokens occasionally, to ensure expired tokens aren't missed when a server in the cluster goes down.

The AM CTS reaper is enabled by default and requires no extra configuration. If you've configured the DS expiration and deletion feature instead, and then want to re-enable the AM CTS reaper, read [Re-enable the AM reaper](#cts-am-reaper).

## Manage expired tokens using DS

If you disable the AM CTS reaper, AM relies on DS capabilities to delete expired tokens.

DS doesn't reap its contents by default–you must configure DS to expire and delete entries. Entry expiration and deletion uses an *ordering index* to find CTS tokens that have reached their time to live then expire and delete them.

Before you configure DS to manage CTS token expiration, consider the following points:

* DS doesn't replicate entry deletion across servers. You *must* make sure all CTS store replicas are configured in the same way. For details, refer to [Entry expiration](https://docs.pingidentity.com/pingds/8.1/config-guide/import-export.html#backend-ttl) in the DS documentation.

* Disabling the AM reaper impacts session-related functionality, such as sending notifications about session expiration or timeouts to agents.

  When you completely disable the AM reaper, the following session functionality becomes *unavailable*:

  * Implementations of `org.forgerock.openam.cts.reaper.TokenDeletionStrategy`, responsible for deleting expiring tokens.

    Custom logic for specific token types (unrelated to simply deleting tokens) no longer works.

  * Implementations of `org.forgerock.openam.cts.continuous.watching.ContinuousListener` and `org.forgerock.openam.cts.continuous.watching.ContinuousWatcher` no longer receive deletion notifications in case of session timeout.

    Active logout is not impacted.

  * Code built on top of `com.iplanet.dpro.session.service.SessionEventListener` no longer receives `IDLE_TIMEOUT` or `MAX_TIMEOUT` events. This affects:

    * Session timeout monitoring

    * Session timeout auditing

    * Session timeout logging

    * Session timeout notifications for agents (PLL, WebSockets)

    * Timeout handlers configured through the `openam-session-timeout-handler-list`

    * Session web hooks registered during authentication

  * Code built on top of `com.iplanet.dpro.session.watchers.listeners.SessionDeletionListener` no longer receives notifications when the session idle or maximum lifetime is exceeded (common usage includes caches).

  * Listeners built on top of `com.sun.identity.plugin.session.SessionListener` no longer receive notifications on active logout or when the maximum session time is reached (idle timeout is ignored).

  If you don't need these session capabilities, refer to [Let DS manage CTS tokens (ignore session capabilities)](#cts-ds-reaper-all-tokens).

  If you do need these session capabilities, refer to [Let DS manage CTS tokens (retain session capabilities)](#cts-ds-reaper-no-sessions).

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A common CTS token management strategy is to configure AM to reap *session tokens* only, and to use DS to manage non-session tokens. This configuration lets you retain session-related functionality, while benefiting from DS's token management capabilities.If your environment requires it, you can also configure the AM reaper to manage different subsets of tokens other than session tokens. |

### Let DS manage CTS tokens (ignore session capabilities)

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These steps assume you **don't need the session capabilities impacted by disabling the AM CTS reaper**. They configure DS to manage expiration and deletion of *all* CTS tokens in your environment. |

1. Perform one of the following steps, depending on whether you're installing a new DS instance for CTS, or modifying an existing instance:

   * If you're installing a new DS instance, use the [CTS setup profile](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-cts.html).

     Choose the option "DS manages all token expiration".

   * If you have an existing DS instance that you're using as a CTS store, configure the DS entry expiration and deletion feature for the `coreTokenExpirationDate` attribute.

     |   |                                                                                      |
     | - | ------------------------------------------------------------------------------------ |
     |   | This attribute is already *indexed*, but you must enable the TTL-related properties: |

     ```bash
     $ /path/to/opendj/bin/dsconfig set-backend-index-prop \
     --hostname 'ds.example.com' \
     --port 4444 \
     --usePkcs12TrustStore /path/to/opendj/config/keystore \
     --truststorepassword:file /path/to/opendj/config/keystore.pin \
     --bindDN uid=admin \
     --bindPassword str0ngAdm1nPa55word \
     --backend-name amCts \
     --index-name coreTokenExpirationDate \
     --set ttl-enabled:true \
     --set ttl-age:10s \
     --no-prompt
     ```

     DS doesn't replicate entry deletion across servers. You must configure all CTS store replicas in the same way. Learn more in [Entry expiration](https://docs.pingidentity.com/pingds/8.1/config-guide/import-export.html#backend-ttl) in the DS documentation.

2. Disable the AM CTS reaper.

   Go to Configure > Server Defaults > Advanced and set the `org.forgerock.services.cts.store.reaper.enabled` property to `false`.

   This change doesn't require a server restart. Learn more about this advanced server property in [Advanced properties](../setup/server-advanced.html).

   Perform this step on all AM servers in your deployment.

### Let DS manage CTS tokens (retain session capabilities)

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These steps assume you **need the session capabilities that would be impacted by disabling the AM CTS reaper**. They configure AM to reap SESSION tokens, while using DS capabilities to manage other tokens. |

1. Perform one of the following steps, depending on whether you're installing a new DS instance for CTS, or modifying an existing instance:

   * If you're installing a new DS instance, use the [CTS setup profile](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-cts.html).

     Choose the option "AM reaper manages only SESSION token expiration".

   * If you're modifying an *existing DS instance*, follow these steps:

     1. Copy the value of the `coreTokenExpirationDate` attribute to the `coreTokenTtlDate` for all existing tokens **except** for `SESSION` tokens.

        AM will manage the `SESSION` tokens separately.

        If you don't perform this step, neither the AM reaper nor the DS expiration feature will delete these tokens. They'll remain in the CTS store until you remove them manually.

     2. Create an ordering index for the `coreTokenTtlDate` attribute:

        ```bash
        $ /path/to/opendj/bin/dsconfig create-backend-index \
        --hostname 'ds.example.com' \
        --port 4444 \
        --usePkcs12TrustStore /path/to/opendj/config/keystore \
        --truststorepassword:file /path/to/opendj/config/keystore.pin \
        --bindDN uid=admin \
        --bindPassword str0ngAdm1nPa55word \
        --backend-name amCts \
        --index-name coreTokenTtlDate \
        --set index-type:ordering \
        --no-prompt
        ```

     3. Rebuild the new index using the `rebuild-index` command:

        ```bash
        $ /path/to/opendj/bin/rebuild-index \
        --hostname 'ds.example.com' \
        --clearDegradedState \
        --port 4444 \
        --usePkcs12TrustStore /path/to/opendj/config/keystore \
        --truststorepassword:file /path/to/opendj/config/keystore.pin \
        --bindDN uid=admin \
        --bindPassword str0ngAdm1nPa55word \
        --baseDN "dc=cts,dc=example,dc=com" \
        --index coreTokenTtlDate
        ```

     4. Configure entry expiration and deletion for the `coreTokenTtlDate` index you created in the previous step:

        ```bash
        $ /path/to/opendj/bin/dsconfig set-backend-index-prop \
        --hostname 'ds.example.com' \
        --port 4444 \
        --usePkcs12TrustStore /path/to/opendj/config/keystore \
        --truststorepassword:file /path/to/opendj/config/keystore.pin \
        --bindDN uid=admin \
        --bindPassword str0ngAdm1nPa55word \
        --index-name coreTokenTtlDate \
        --backend-name amCts \
        --set ttl-enabled:true \
        --set ttl-age:10s \
        --no-prompt
        ```

     |   |                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------- |
     |   | DS doesn't replicate deletion of entries across servers. You must configure all CTS store replicas in the same way. |

     Learn more in [Entry expiration](https://docs.pingidentity.com/pingds/8.1/config-guide/import-export.html#backend-ttl) in the DS documentation.

2. In the AM admin UI, go to Configure > Server Defaults > Advanced and configure the following advanced server properties for each AM server that shares the CTS store cluster:

   * Set `org.forgerock.services.cts.store.ttlsupport.enabled` to `true`.

   * Set `org.forgerock.services.cts.store.ttlsupport.exclusionlist` to `SESSION`.

   * Set `org.forgerock.services.cts.store.reaper.enabled` to `true`.

   The changes are effective immediately. Learn more about these advanced server properties in [Advanced properties](../setup/server-advanced.html).

## Re-enable the AM reaper

Follow these steps if you previously enabled the DS expiration and deletion feature but want to disable it and re-enable the AM reaper.

1. If you enabled the DS expiration and deletion feature following the steps in [Let DS manage CTS tokens (ignore session capabilities)](#cts-ds-reaper-all-tokens), follow these steps to enable the AM CTS reaper for all tokens:

   * Disable DS entry expiration and deletion for the `coreTokenExpirationDate` index:

     ```bash
     $ /path/to/opendj/bin/dsconfig set-backend-index-prop \
     --hostname 'ds.example.com' \
     --port 4444 \
     --usePkcs12TrustStore /path/to/opendj/config/keystore \
     --truststorepassword:file /path/to/opendj/config/keystore.pin \
     --bindDN uid=admin \
     --bindPassword str0ngAdm1nPa55word \
     --backend-name amCts \
     --index-name coreTokenExpirationDate \
     --set ttl-enabled:false \
     --no-prompt
     ```

     |   |                                                                             |
     | - | --------------------------------------------------------------------------- |
     |   | Don't *delete* the index. Configure all CTS store replicas in the same way. |

   * Re-enable the AM CTS reaper:

     On each AM server in your deployment, go to Configure > Server Defaults > Advanced and set the `org.forgerock.services.cts.store.reaper.enabled` property to `true`.

2. If you enabled the DS expiration and deletion feature following the steps in [Let DS manage CTS tokens (retain session capabilities)](#cts-ds-reaper-no-sessions), follow these steps to enable the AM CTS reaper for all tokens:

   * Disable the DS entry expiration and deletion feature for the `coreTokenTtlDate` index. For example:

     ```bash
     $ /path/to/opendj/bin/dsconfig set-backend-index-prop \
     --hostname 'ds.example.com' \
     --port 4444 \
     --usePkcs12TrustStore /path/to/opendj/config/keystore \
     --truststorepassword:file /path/to/opendj/config/keystore.pin \
     --bindDN uid=admin \
     --bindPassword str0ngAdm1nPa55word \
     --index-name coreTokenTtlDate \
     --backend-name amCts \
     --set ttl-enabled:false
     ```

     |   |                                                   |
     | - | ------------------------------------------------- |
     |   | Configure all CTS store replicas in the same way. |

   * Delete the index created for the `coreTokenTtlDate` attribute. For example:

     ```bash
     $ /path/to/opendj/bin/dsconfig delete-backend-index \
     --hostname 'ds.example.com' \
     --port 4444 \
     --usePkcs12TrustStore /path/to/opendj/config/keystore \
     --truststorepassword:file /path/to/opendj/config/keystore.pin \
     --bindDN uid=admin \
     --bindPassword str0ngAdm1nPa55word \
     --backend-name amCts \
     --index-name coreTokenTtlDate \
     --no-prompt
     ```

     |   |                                                   |
     | - | ------------------------------------------------- |
     |   | Configure all CTS store replicas in the same way. |

   * Go to Configure > Server Defaults > Advanced and configure the following advanced server properties in all of the AM servers sharing the CTS store cluster:

     * Set `org.forgerock.services.cts.store.ttlsupport.enabled` to `false`.

     * Remove the `org.forgerock.services.cts.store.ttlsupport.exclusionlist` property from the configuration.

     * Set `org.forgerock.services.cts.store.reaper.enabled` to `true`.

   The changes are effective immediately. For more information about these advanced server properties, see [Advanced properties](../setup/server-advanced.html).

---

---
title: Tune the CTS
description: Optimize PingAM CTS token store performance by tuning reaper cache size, search limits, OAuth 2.0 storage schemes, and logout user cache poll intervals
component: pingam
version: 8.1
page_id: pingam:cts:cts-tuning-considerations
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-tuning-considerations.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-19T14:32:08Z
keywords: ["CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Tuning"]
page_aliases: ["cts-guide:cts-tuning-considerations.adoc"]
section_ids:
  cts-tuning-cache-size: Reaper cache size
  cts-tuning-tokenlimit: Reaper search size
  cts-oauth2-storage-scheme: OAuth 2.0 CTS storage scheme
  cts-logout-user-poll-interval: CTS poll interval
  cts-tuning-vlv-denylist: VLV indexes for denylist queries
---

# Tune the CTS

There are several tuning considerations for the efficient processing of your CTS token store:

| Task                                                                                                                                                                                                              | Resources                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Configure the reaper cache size**The reaper process prunes tokens in the store that have reached their maximum time-to-live.                                                                                    | [Reaper cache size](#cts-tuning-cache-size)                |
| **Manage the reaper search size**In addition to the cache, the reaper also uses a search to find expired tokens. You can tune the maximum number of tokens the reaper can find and delete in a single invocation. | [Reaper search size](#cts-tuning-tokenlimit)               |
| **Change the OAuth 2.0 Storage Scheme**Configure the `grant-set` scheme to improve the performance of OAuth 2.0-related operations.                                                                               | [OAuth 2.0 CTS storage scheme](#cts-oauth2-storage-scheme) |
| **Set the poll interval for the logout user cache**In a multi-server deployment, servers poll the CTS at a specified interval to update their logout user token cache with the tokens from other servers.         | [CTS poll interval](#cts-logout-user-poll-interval)        |

## Reaper cache size

The size of the AM reaper cache is controlled by the `org.forgerock.services.cts.reaper.cache.size` advanced property. The default size is `500000` tokens.

If an AM server is under sustained heavy load, the reaper cache may reach capacity, causing degraded performance due to the additional slower searches of the CTS store. If the reaper cache is full, messages are logged in the `Session` debug log, such as the following:

```
The CTS token reaper cache is full. This will result in degraded performance.
You should increase the cache size by setting the advanced server property
'org.forgerock.services.cts.reaper.cache.size' to a number higher than 500000.
```

If this debug message appears frequently in the debug logs, increase the value of the `org.forgerock.services.cts.reaper.cache.size` property. To alter the value, in the AM admin UI, go to Configure > Server Defaults > Advanced, and add the property and increased value to the list.

Increasing the size of the reaper cache causes higher memory usage on the AM server. If a cache of the default size of 500000 entries is nearly full, the server memory used could be up to approximately 100 megabytes.

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | Tune the AM reaper cache size only if the `org.forgerock.services.cts.store.reaper.enabled` advanced server property is set to `true`. |

## Reaper search size

The reaper uses its [cache](#cts-tuning-cache-size) to make sure expired tokens are removed from the CTS token store, but it also has a built-in mechanism to search for expired tokens that haven't been purged. This could happen, for example, due to an AM instance crash.

When the reaper searches for expired tokens, DS returns a page of records, and the reaper deletes these tokens.

To configure the maximum number of records that DS returns, use the `org.forgerock.services.cts.reaper.search.tokenLimit` advanced server property. The default is `5000`.

To configure how often the search runs, and the grace period for the tokens the reaper deletes, configure the following properties:

* `org.forgerock.services.cts.reaper.search.pollFrequencyMilliseconds`.

  Specifies how often to perform a search for expired tokens. The default is `5000` milliseconds.

  The value of this setting should never be higher than a few seconds. You want to launch the search frequently to prevent expired tokens accumulating.

* `org.forgerock.services.cts.reaper.search.gracePeriodMilliseconds`.

  Specifies the grace period used when searching for expired tokens. Any tokens that expired more than the specified duration ago are returned. The default is `300000` milliseconds.

  Set the grace period larger than the value controlled by the `org.forgerock.services.cts.reaper.cache.pollFrequencyMilliseconds` advanced property. This allows an AM instance sufficient time to delete the token using its cache, rather than search.

  Deleting from the cache is preferred because it avoids expensive searches against the CTS store.

To tune the reaper searches, run load tests in your environment with the default reaper parameters, and then watch if the expired tokens build up. If there is no token build-up, then the reaper is sufficiently tuned. If you see token build-up, tune the [reaper cache](#cts-tuning-cache-size) first, as it is the less expensive of the two reaping mechanisms.

A small number of expired tokens left on each iteration of the reaper search is ok, providing tokens are cleared up during lower activity periods.

Keeping a large number of expired tokens in the CTS store results in increased disk space usage, and prevents AM from sending expiration notifications in a timely fashion.

Setting the token limit too high could negatively affect the performance of the DS instance. It is better to launch more runs of the reaper search with fewer records, than fewer runs with a large number of records.

## OAuth 2.0 CTS storage scheme

The following schemes are available for storing OAuth 2.0 tokens in the CTS store:

* `grant-set`

  The `grant-set` scheme groups multiple authorizations for a given OAuth 2.0 client and resource owner pair and stores them in a single CTS `OAUTH2_GRANT_SET` entry. This implementation reduces the size and quantity of entries stored, as well as the number of calls required to perform OAuth 2.0 operations. You should consider upgrading to the `grant-set` scheme.

  The `grant-set` scheme is backwards-compatible with existing entries stored in the CTS store. Therefore, any access or refresh token issued before configuring the `grant-set` scheme is still valid. The CTS store retains an existing token in its original form until the refresh token expires or the token is actively revoked.

  Users won't notice any change in the tokens they receive.

* `one-to-one`

  The `one-to-one` scheme stores the state of multiple authorizations for a given OAuth 2.0 client and resource owner pair across multiple `OAUTH` and `OAUTH2_STATELESS_GRANT` entries and is more resource intensive.

Learn more about these tokens in [CTS token types](cts-token-types.html).

To enable the `grant-set` scheme:

1. Go to Configure > Global Services > OAuth2 Provider > Global Attributes.

2. In the CTS Storage Scheme drop-down, choose Grant-Set Storage Scheme.

3. Click Save Changes.

New OAuth 2.0 tokens stored in the CTS after the change use the new scheme automatically.

## CTS poll interval

If [client-side session logout](../am-sessions/managing-sessions-REST.html#invalidate-sessions-user) is enabled, AM stores the logout user tokens in a local cache. In a multi-server deployment, servers poll the CTS at a specified interval to update their logout user token cache with the tokens from other servers.

The poll interval is specified by the global session property [Enable Invalidation of Sessions Based on User Identifier](../setup/services-configuration.html#global-session-client-side-logout), and is set to `60` seconds by default.

A very long polling interval gives malicious users time to connect to other AM servers within a site and use stolen session cookies. A very short polling interval improves security by invalidating authenticated sessions across servers in a shorter timeframe, but can incur a performance cost.

A value of `0` disables polling of the CTS. Don't disable polling in a multi-server site because this prevents `logoutByUser` session invalidation data from being shared between servers.

## VLV indexes for denylist queries

When you've enabled [client-side session denylisting](../security/session-state-session-termination.html#session-state-configure-denylist) or [client-side OAuth 2.0 token denylisting](../am-oauth2/stateless-oauth2.html#configuring-client-side-oauth-denylisting), AM queries the CTS token store for every denylisted token issued after the epoch (January 1, 1970).

In deployments with a large number of denylisted tokens, this initial query can return a very large result set. AM uses a virtual list view (VLV) request to page through the results, so DS needs a matching VLV index for each denylist query AM issues.

In these commands, substitute the base DN with the CTS root suffix configured in your environment.

1. Create the VLV index that matches the session denylist query:

   ```bash
   $ /path/to/opendj/bin/dsconfig create-backend-vlv-index \
   --hostname 'ds.example.com' \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --backend-name amCts \
   --index-name session-denylist \
   --set filter:"(&(&(coreTokenType=SESSION_BLACKLIST)(coreTokenDate01>=19700101000000Z))(objectClass=frCoreToken))" \
   --set scope:whole-subtree \
   --set base-dn:ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com \
   --set sort-order:coreTokenId \
   --no-prompt
   ```

   |   |                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The filter uses the internal token type name `SESSION_BLACKLIST`. This is the actual value stored in the CTS and must match exactly. |

2. If you use client-side OAuth 2.0 token denylisting, create the VLV index that matches the OAuth 2.0 denylist query:

   ```bash
   $ /path/to/opendj/bin/dsconfig create-backend-vlv-index \
   --hostname 'ds.example.com' \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --backend-name amCts \
   --index-name oauth2-denylist \
   --set filter:"(&(&(coreTokenType=OAUTH_BLACKLIST)(coreTokenDate01>=19700101000000Z))(objectClass=frCoreToken))" \
   --set scope:whole-subtree \
   --set base-dn:ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com \
   --set sort-order:coreTokenId \
   --no-prompt
   ```

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | The filter uses the internal token type name `OAUTH_BLACKLIST`. This is the actual value stored in the CTS and must match exactly. |

3. Rebuild the indexes:

   ```bash
   $ /path/to/opendj/bin/rebuild-index \
   --hostname 'ds.example.com' \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --truststorepassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --backend-name amCts \
   --rebuildAll
   ```

   Depending on the number of tokens in your CTS store, rebuilding the indexes can take a long time.

Tune the AM CTS [VLV Page Size](../setup/server-cts.html#cts-tokenstore) property to a value at or below the DS search size limit configured for the CTS bind account. Use either the global `size-limit` property or the `ds-rlim-size-limit` operational attribute if you've overridden it for that account. The DS global `size-limit` default is `1000`, but CTS deployments commonly raise the size limit for the CTS bind account to allow larger denylist queries. In testing with up to five million denylisted tokens and a CTS bind account with a raised size limit, a VLV page size of `9000` performed well.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Treat these example values as starting points, not universal defaults. Validate them in your own environment before rolling them out to production. |
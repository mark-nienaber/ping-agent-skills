---
title: Configure CTS token stores
description: Configure PingAM to use an external CTS token store for managing sessions and tokens with PingDS, including TLS setup and high-availability testing
component: pingam
version: 8.1
page_id: pingam:cts:cts-openam-config
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-openam-config.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Availability", "Directory Server"]
page_aliases: ["cts-guide:cts-openam-config.adoc"]
section_ids:
  cts-deployment-steps: Install and configure PingDS for CTS data
  cts-openam-gui: Configure the CTS
  cts-testing-ha: Test session availability
---

# Configure CTS token stores

The following table summarizes the high-level tasks you must perform to configure a new instance of the CTS token store:

| Task                                                                                                                                                                                                                                                                                        | Resources                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Prepare a DS server**Prepare the DS schema for CTS data.                                                                                                                                                                                                                                  | [Install and configure PingDS for CTS data](#cts-deployment-steps)         |
| **Configure AM to use the new CTS token store**Configuring a new CTS datastore *doesn't* migrate existing data from the old store to the new one. Usually, users will need to sign on again so that AM stores their sessions and tokens in the new token store.                             | [Configure the CTS](#cts-openam-gui)                                       |
| **(Optional) Configure mTLS authentication to the CTS store**By default, AM authenticates to the CTS store using simple (username/password) authentication. To enhance security, you can configure mutual TLS (mTLS) authentication which lets AM authenticate using a trusted certificate. | [Secure authentication to datastores](../security/secure-data-stores.html) |
| **Test session availability**For this test, you must have a site with more than one instance. The idea is to sign on a user into the first instance, shut it down, and check that the session is still available to the second instance.                                                    | [Test session availability](#cts-testing-ha)                               |

## Install and configure PingDS for CTS data

Installing DS with a [setup profile](https://docs.pingidentity.com/pingds/8.1/install-guide/setup-profiles.html) creates the required backend, schema, bind user, and indexes:

1. Follow the steps in [Install DS for AM CTS](https://docs.pingidentity.com/pingds/8.1/install-guide/profile-am-cts.html) in the DS documentation.

2. Share the CTS store certificate with the AM container to prepare for TLS/LDAPS. The CTS store should communicate over secure connections for security reasons.

   DS requires secure connections by default. Share its certificate with the AM container before continuing.

   > **Collapse: Share the DS certificate with AM**
   >
   > * On the DS host, export the DS CA certificate.
   >
   >   DS uses a deployment ID and password to generate a CA key pair. Learn more in [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-ids).
   >
   >   Use the `dskeymgr` command to export the CA certificate:
   >
   >   ```bash
   >   $ /path/to/opendj/bin/dskeymgr \
   >   export-ca-cert \
   >   --deploymentId $DEPLOYMENT_ID \
   >   --deploymentIdPassword password \
   >   --outputFile /path/to/ca-cert.pem
   >   ```
   >
   > * Copy the `ca-cert.pem` file to an accessible location on the AM host.
   >
   > - Import the DS CA certificate into the AM truststore:
   >
   >   ```bash
   >   $ keytool \
   >   -importcert \
   >   -file /path/to/ca-cert.pem \
   >   -keystore /path/to/am/security/keystores/truststore
   >   -storepass truststore-password
   >   ```
   >
   > Learn more about configuring AM's truststore in [Prepare the truststore](../installation/prepare-trust-store.html).

3. Configure the CTS store in AM.

   Learn more in [Configure the CTS](#cts-openam-gui).

   The bind DN of the service account to use when configuring the CTS store in AM is `uid=openam_cts,ou=admins,ou=famrecords,ou=openam-session,ou=tokens`.

## Configure the CTS

These steps assume the AM instances communicate with a single CTS instance (or load balancer), which has an FQDN of `cts.example.com` and is running on port `1636`.

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If AM can't access the CTS token store, you'll not be able to sign on to the AM admin UI.Back up your deployment before making any changes to your CTS token store configuration. |

Perform the following steps to configure a CTS token store:

1. In the AM admin UI, go to Configure > Server Defaults, and click CTS.

2. On the CTS Token Store tab, set the following parameters:

   **CTS Token Store Parameters**

   | Parameter   | Value                                       | Notes |
   | ----------- | ------------------------------------------- | ----- |
   | Store Mode  | `External Token Store`                      |       |
   | Root Suffix | `ou=famrecords,ou=openam-session,ou=tokens` |       |

3. On the External Store Configuration tab, configure the parameters as follows:

   **External Store Configuration Parameters**

   | Parameter            | Value                                                                | Notes                                                                                                                                                                                 |
   | -------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | SSL/TLS Enabled      | True                                                                 | Enable secure connections when connecting to DS. When you enable SSL/TLS, make sure the AM server can trust the DS server certificate and the certificate matches the CTS store FQDN. |
   | Connection String(s) | `cts.example.com:1636`                                               | Use the LDAPS port or the LDAP port with StartTLS (`cts.example.com:1389`).                                                                                                           |
   | Login ID             | `uid=openam_cts,ou=admins,ou=famrecords,ou=openam-session,ou=tokens` | The bind DN of the service account AM uses to connect to the directory service.                                                                                                       |
   | Password             | *5up35tr0ng*                                                         | Use a strong bind password for production systems.                                                                                                                                    |
   | Heartbeat            | `10`                                                                 | Tune this value for production systems.                                                                                                                                               |

4. Save your work.

5. Restart AM or the web container where it runs for the changes to take effect.

## Test session availability

To test session availability, use two browsers: Chrome and Firefox. You can use any two browser types, or run the browsers in incognito mode. You can also view tokens using an LDAP browser.

1. In Chrome, sign on to the second AM instance with the `amAdmin` user, click the realm, and click Sessions.

2. In Firefox, sign on to the first AM instance with a test user.

3. In Chrome, verify that the test user exists in the first AM instance's session list and not in the second instance.

4. Shut down the first AM instance.

5. In Firefox, rewrite the URL to point to the second AM instance.

   If successful, the browser won't prompt you to sign on.

6. Confirm the session is still available.

   In Chrome, list the sessions on the second instance and observe the test user's session.

7. Restart the first AM instance to complete the testing.

---

---
title: Core Token Service (CTS)
description: Configure the Core Token Service to manage session and token storage, including deployment architecture, token encryption and compression, and token lifecycle management
component: pingam
version: 8.1
page_id: pingam:cts:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CTS Store (Sessions &amp; Tokens)"]
page_aliases: ["cts-guide:preface.adoc", "index.adoc"]
---

# Core Token Service (CTS)

These pages describe how to configure the Core Token Service, and how to manage the tokens stored in it.

[icon: cubes, set=fad, size=3x]

#### [Deployment architecture](cts-deployment-architectures.html)

Choose the best architecture for your deployment.

[icon: cogs, set=fad, size=3x]

#### [Configure a dedicated CTS store](cts-openam-config.html)

Prepare a DS instance to host a dedicated CTS token store.

[icon: archive, set=fad, size=3x]

#### [Manage tokens](cts-token-managing.html)

Learn how to encrypt and/or compress tokens.

[icon: minus-circle, set=fad, size=3x]

#### [Manage expired CTS tokens](cts-reaper.html)

Configure how CTS tokens are pruned after they reach their maximum time-to-live.

---

---
title: CTS backups and DS replication purge delay
description: Understand how Directory Server replication purge delay affects CTS backups and recovery in distributed deployments
component: pingam
version: 8.1
page_id: pingam:cts:cts-backup-repl-purge-delay
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-backup-repl-purge-delay.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CTS Store (Sessions &amp; Tokens)", "Backup &amp; Restore", "Replication", "Directory Server"]
page_aliases: ["cts-guide:cts-backup-repl-purge-delay.adoc"]
---

# CTS backups and DS replication purge delay

*Replication* replays each update on all directory servers, so they eventually converge on the same directory, token, session, SAML 2.0, and OAuth 2.0 data. DS data replication ensures directory services remain available for reads and writes when a server crashes or network connection goes down.

The directory servers store historical information to replay updates in the right order. DS servers periodically purge this historical information to prevent it from growing indefinitely. The setting that governs how long to retain historical information is the DS `replication-purge-delay`.

The default DS `replication-purge-delay` is 3 days. Although this setting is generally appropriate for most data, it may be too long for volatile CTS data in high-volume deployments.

If you have separated your DS servers for CTS from DS servers for other data, you can lower the replication purge delay on all DS replicas. For example, the following command sets it to 12 hours for a single DS replica on `cts.example.com`:

```bash
$ /path/to/opendj/bin/dsconfig \
set-synchronization-provider-prop \
--provider-name "Multimaster Synchronization" \
--set replication-purge-delay:12h \
--hostname cts.example.com \
--port 4444 \
--usePkcs12TrustStore /path/to/opendj/config/keystore \
--truststorepassword:file /path/to/opendj/config/keystore.pin \
--bindDN uid=admin \
--bindPassword str0ngAdm1nPa55word \
--no-prompt
```

You must decide whether CTS data backups are important in your deployment. It may not be worth backing up the CTS data. Losing CTS tokens may be acceptable if the worst-case scenario means users have to log in again.

For deployments with critical long-lived sessions or long-lived refresh tokens, losing tokens may not be acceptable. If losing CTS tokens is not acceptable, back up CTS data.

When backing up CTS data, be aware that DS backups older than the replication purge delay are useless. DS replication can only bring a replica up to date when it has the historical information to replay changes in the right order. If you restore a DS server from data older than the replication purge delay, the other DS servers will have already purged the historical information needed to replay the pending changes. For details, refer to [Backup and restore](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html) in the PingDS documentation.

---

---
title: CTS overview
description: Understand Core Token Service (CTS) storage for sessions and tokens, session high availability, and configuration recommendations for PingAM deployments
component: pingam
version: 8.1
page_id: pingam:cts:cts-overview
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-overview.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration"]
page_aliases: ["cts-guide:cts-overview.adoc"]
section_ids:
  cts-general-recommend: CTS configuration recommendations
---

# CTS overview

The Core Token Service (CTS) provides generalized, persistent, and highly available storage for sessions and tokens. AM uses CTS as the authoritative source for [server-side](../am-sessions/cts-based-sessions.html) sessions and caches these sessions in its memory heap to improve performance.

CTS supports *session high availability*, which lets AM manage a session as long as one of the AM servers in a clustered deployment is available. After a user has successfully authenticated, AM creates a server-side authenticated session. Any AM instance that's configured to use the same CTS can retrieve the session and allow access to it. The user doesn't need to sign on again unless the entire deployment goes down.

CTS provides storage for the following: \* Server-side journey and authenticated sessions

* Session denylist (if enabled for [client-side](../am-sessions/client-based-sessions.html) authenticated sessions)

* Journey session allowlist (if enabled for [client-side](../security/auth-session-whitelist.html) journey sessions)

* SAML 2.0-related data (if enabled for Security Token Service token validation and cancellation)

* OAuth 2.0 and UMA 2.0 server-side tokens, and OAuth 2.0 client-side token denylist

* Push notification data during authentication

* Site-wide notification, such as logout or session termination notifications. Learn more about these tokens in [CTS token types](cts-token-types.html).

The CTS token store is created at installation time in the configuration store.

In general, the Core Token Service causes more volatile replication traffic due to the possibility of short-lived entries compared to regular configuration data. To handle the data volatility in high-load deployments, configure an additional DS service, separate from your configuration store, to isolate session and token information.

## CTS configuration recommendations

CTS helps your deployment avoid single points of failure by providing high availability to sessions and tokens stored in its token store.

For high-volume, demanding deployments, consider the following recommendations:

* **Consider separate CTS storage for high volumes**. If you require a higher-level performance threshold, you can move the CTS token storage to one or more dedicated systems rather than sharing your configuration store, as CTS generally causes much more replication traffic than less volatile configuration data. The CTS token store is the primary source for session tokens and will experience both high read and write activity depending on session usage.

* **Isolate different stores for high volumes**. CTS entries are large, around 5KB, but are short-lived, whereas configuration data is static and long-lived. User entries are more dynamic than configuration data but much less volatile than CTS data.

  For high-volume deployments, consider putting CTS data in a separate DS datastore and using different tuning and storage settings

* **Tune DS servers**. For high performance, properly size and tune DS servers for your external CTS store.

  In addition, you can enable token compression as discussed in [Manage CTS tokens](cts-token-managing.html). When enabled, token compression reduces load requirements on the network connection between token stores in exchange for processing time-compressing tokens.

* **Limit DS replication traffic over slow links**. DS servers replicate CTS data transmitted from AM servers. For each change to a CTS token, DS replication replays the change on all DS servers in the CTS datastore. The volume of replication traffic is potentially problematic over slow links.

  For high volumes when low latency is required, consider limiting the replication traffic as described in the DS documentation on [standalone servers](https://docs.pingidentity.com/pingds/8.1/install-guide/setup-rs.html).

---

---
title: CTS token types
description: Reference information about Core Token Service token types, including LDAP attributes, data storage, and example formats for OAuth 2.0, SAML 2.0, session, and notification tokens
component: pingam
version: 8.1
page_id: pingam:cts:cts-token-types
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-token-types.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CTS Store (Sessions &amp; Tokens)"]
page_aliases: ["reference:cts-token-types.adoc", "cts-guide:cts-token-types.adoc"]
section_ids:
  oauth2-grant-set-tokens: OAuth 2.0 grant-set tokens
  ldap_attributes: LDAP attributes
  token_examples: Token examples
  client-side-oauth2-tokens: Client-side OAuth 2.0 tokens
  ldap_attributes_2: LDAP attributes
  token_examples_2: Token examples
  server-side-oauth2-tokens: Server-side OAuth 2.0 tokens
  ldap_attributes_3: LDAP attributes
  token_examples_3: Token examples
  other-oauth2-tokens: Other OAuth 2.0 tokens
  ldap_attributes_4: LDAP attributes
  token_examples_4: Token examples
  saml2-tokens: SAML 2.0 tokens
  ldap_attributes_5: LDAP attributes
  token_examples_5: Token examples
  session-tokens: Session tokens
  ldap_attributes_6: LDAP attributes
  token_examples_6: Token examples
  notification-tokens: Notification tokens
  ldap_attributes_7: LDAP attributes
  token_example: Token example
---

# CTS token types

The Core Token Service (CTS) uses a generic LDAP schema for all token types.

The following sections provide information about the different token types, including what LDAP attributes they use, the data stored in those attributes, and example token formats:

* [OAuth 2.0 grant-set tokens](#oauth2-grant-set-tokens)

* [Client-side OAuth 2.0 tokens](#client-side-oauth2-tokens)

* [Server-side OAuth 2.0 tokens](#server-side-oauth2-tokens)

* [Other OAuth 2.0 tokens](#other-oauth2-tokens)

* [SAML 2.0 tokens](#saml2-tokens)

* [Session tokens](#session-tokens)

* [Notification tokens](#notification-tokens)

|   |                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use this information to query the CTS using [LDAP searches](https://docs.pingidentity.com/pingds/8.1/ldap-guide/search-ldap.html).For example, if you want to list user OAuth 2.0 refresh tokens, you can filter on `coreTokenString03=user` and `coreTokenString10=refresh_token`. |

## OAuth 2.0 grant-set tokens

OAuth 2.0 grant-set tokens are created when the [grant-set](cts-tuning-considerations.html#cts-oauth2-storage-scheme) scheme is used.

The grant-set acts as a container for all authorizations:

* Client-side access code tokens and grant tokens.

* Server-side access code tokens, access tokens, and refresh tokens.

### LDAP attributes

| LDAP attribute         | OAuth 2.0 grant-set token                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| coreTokenUserId        |                                                                                                   |
| coreTokenType          | `OAUTH2_GRANT_SET`                                                                                |
| coreTokenString01      |                                                                                                   |
| coreTokenString02      |                                                                                                   |
| coreTokenString03      | *user*                                                                                            |
| coreTokenString04      |                                                                                                   |
| coreTokenString05      |                                                                                                   |
| coreTokenString06      |                                                                                                   |
| coreTokenString07      |                                                                                                   |
| coreTokenString08      | *realm*                                                                                           |
| coreTokenString09      | *client ID*                                                                                       |
| coreTokenString10      |                                                                                                   |
| coreTokenString11      |                                                                                                   |
| coreTokenString12      |                                                                                                   |
| coreTokenString13      |                                                                                                   |
| coreTokenString14      |                                                                                                   |
| coreTokenString15      |                                                                                                   |
| coreTokenString16      |                                                                                                   |
| coreTokenMultiString03 | *JSON representation of the OAuth 2.0 grant (access codes, refresh tokens, and access tokens)*(1) |

(1) The following abbreviations are used in this JSON representation:

* `g`: Unique identifier for the grant in the CTS

* `gx`: Grant expiry time

* `_s`: Scope

* `a`: Authorization code

* `ax`: Authorization code expiry time

* `asi`: Journey session ID token

* `aati`: Audit tracking ID

* `au`: Redirect URI

* `ast`: State

* `_am`: Authentication node in AM

* `_acr`: Authentication context class reference, if applicable

* `gt`: Grant type, if applicable

### Token examples

> **Collapse: Client-side grant-set token**
>
> ```bash
> dn: coreTokenId=kOrkxaDZ6fYcUrcE0c3PEMFIGNk,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: frCoreToken
> objectClass: top
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenId: kOrkxaDZ6fYcUrcE0c3PEMFIGNk
> coreTokenMultiString03: {"g":"kOrkxaDZ6fYcUrcE0c3PEMFIGNk.xuPxwKKadXjWvMfKg9WFzvqIOC4","gx":1529062484276,"_s":["openid","profile"],"a":"kOrkxaDZ6fYcUrcE0c3PEMFIGNk.vm6gyeD5t8mF8nTYQ1XQBYTskMo","ax":1528454203638,"aati":"809b87b3-4fad-4ca1-9312-a7f0c669fd6c-34347","ai":true,"au":"https://example.com","asi":"AQIC5w...2NzEz*","ast":"1234","_am":"DataStore","_acr":"0","gt":[]}
> coreTokenMultiString03: {"g":"C7mzozs1XJKVvCT63JwQatoI-og.Xf_gOFNZOeGcY6ZLnGxX11N9NKQ","gx":1579098268014,"_s":["read"],"a":"C7mzozs1XJKVvCT63JwQatoI-og.BXUyATQtb9GoyrFvAacc6b20S4A","ax":1578489985511,"aati":"0e4db3cf-14e5-4d44-9f36-8e2fc6ac78a6-15583","ai":true,"an":"123456","au":"https://example.com","asi":"AQIC5w...2NzEz*","ast":"eHI6","_am":"DataStore","_acr":"0","r":"C7mzozs1XJKVvCT63JwQatoI-og.IbiBbTo1bCKelDu4hj5tb_2qbrk","gt":[]}
> coreTokenString03: bjensen
> coreTokenString08: /myRealm
> coreTokenString09: myClient
> coreTokenType: OAUTH2_GRANT_SET
> ```

> **Collapse: Server-side grant-set token**
>
> ```bash
> dn: coreTokenId=fx-GTfShtRhmJ89qMNVkxLx339U,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: frCoreToken
> objectClass: top
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenId: fx-GTfShtRhmJ89qMNVkxLx339U
> coreTokenMultiString03: {"g":"fx-GTfShtRhmJ89qMNVkxLx339U.BwOWUGadbho7rKgCYj5Uq1XuRPc","gx":0,"_s":["openid","profile"],"a":"fx-GTfShtRhmJ89qMNVkxLx339U.0g7urZwlwyK_5gUOlC49t4PVUPo","ax":1540546982500,"aati":"fb479915-c2aa-42b3-ad76-b7eb3de950c5-338537161","ai":true,"au":"https://example.com","asi":"AQIC5w...2NzEz*","ast":"1234","_am":"DataStore","_acr":"0","r":"fx-GTfShtRhmJ89qMNVkxLx339U.vXS04FRzuWulPMomSoVDnZvj-6s","rx":1541151662549,"rgt":"authorization_code","rtt":"Bearer","rtn":"refresh_token","rati":"fb479915-c2aa-42b3-ad76-b7eb3de950c5-338537554","ro":"jS474J1xvNZwD-uLeJJeTDWjAzI","_at":1540546862,"_al":0,"gt":[{"t":"fx-GTfShtRhmJ89qMNVkxLx339U.SGEDFJ5BkuuKXKHVeV24_IzoHRg","tx":1540550462814,"tgt":"authorization_code","ts":["openid","profile"],"ttn":"access_token","tati":"fb479915-c2aa-42b3-ad76-b7eb3de950c5-338537841","tck":null}]}
> coreTokenString03: bjensen
> coreTokenString08: /myRealm
> coreTokenString09: myClient
> coreTokenType: OAUTH2_GRANT_SET
> ```

## Client-side OAuth 2.0 tokens

* Access code tokens

  Client-side access code tokens are created when the [one-to-one](cts-tuning-considerations.html#cts-oauth2-storage-scheme) scheme is used.

  They are used in the OAuth 2.0 authorization code flow and in the OIDC authorization code and hybrid flows. They provide the state for the code used by the client to retrieve an access token.

  Additionally, the value of the access code is used to form the unique identity of the subsequent grant token.

* OAuth 2.0 grant tokens

  Client-side OAuth 2.0 grant tokens are created when the [one-to-one](cts-tuning-considerations.html#cts-oauth2-storage-scheme) scheme is used.

  They replace individual access and refresh tokens with a single token indicating that a grant took place. This prevents additional data from being written to the CTS when a new access token is issued based on an existing refresh token with an existing grant ID. They use the grant ID value from the preceding access code if this token was generated with the OAuth 2.0 authorization code flow.

  The grant ID in the client-side OAuth 2.0 JWT matches the DN of the token in the CTS.

### LDAP attributes

| LDAP attribute    | Client-side access code token                         | Client-side OAuth 2.0 grant token            |
| ----------------- | ----------------------------------------------------- | -------------------------------------------- |
| coreTokenUserId   |                                                       | *user*                                       |
| coreTokenType     | `OAUTH`                                               | `OAUTH2_STATELESS_GRANT`                     |
| coreTokenString01 | *scopes*                                              |                                              |
| coreTokenString02 |                                                       |                                              |
| coreTokenString03 | *user*                                                |                                              |
| coreTokenString04 | *redirect\_uri*                                       | *client ID*                                  |
| coreTokenString05 |                                                       |                                              |
| coreTokenString06 | `true` (when the code is used and consent is granted) | *scope*                                      |
| coreTokenString07 | `Bearer`                                              |                                              |
| coreTokenString08 | *realm*                                               |                                              |
| coreTokenString09 | *client ID*                                           |                                              |
| coreTokenString10 | `access_code`                                         |                                              |
| coreTokenString11 | *nonce*                                               | *realm*                                      |
| coreTokenString12 |                                                       | *jti*                                        |
| coreTokenString13 |                                                       | *refresh token ID*(1)                        |
| coreTokenString14 |                                                       |                                              |
| coreTokenString15 | *grant ID*                                            |                                              |
| coreTokenString16 |                                                       |                                              |
| coreTokenDate01   |                                                       | *grace period end time for refresh token*(1) |

(1) These attributes are only populated when there's been at least one successful attempt to use a refresh token and the [refresh token grace period](../am-oauth2/oauth2-refresh-tokens.html#settings_for_refresh_tokens) is enabled.

### Token examples

> **Collapse: Client-side access code token**
>
> ```bash
> dn: coreTokenId=4e915f7a-08ec-4c65-915f-2256d6c3a503,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenObject: {"redirectURI":["https://example.com"],"clientID":["myClient"],"ssoTokenId":["AQIC5w...2NzEz*"],"auditTrackingId":["a7180708-c39b-4f92-90ea-b2b8bb79ec75-83912"],"tokenName":["access_code"],"authModules":[],"code_challenge_method":[],"userName":["bjensen"],"nonce":["abcdef"],"authGrantId":["f58f19f9-7f3f-43db-be90-466643414143"],"acr":[],"expireTime":["1523281431770"],"scope":["openid","profile"],"claims":[null],"realm":["/myRealm"],"id":["4e915f7a-08ec-4c65-915f-2256d6c3a503"],"state":[],"tokenType":["Bearer"],"code_challenge":[],"issued":["true"]}
> coreTokenString11: abcdef
> coreTokenString01: openid,profile
> coreTokenString10: access_code
> coreTokenString04: https://example.com
> coreTokenString15: f58f19f9-7f3f-43db-be90-466643414143
> coreTokenString03: bjensen
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenString08: /myRealm
> coreTokenString09: myClient
> coreTokenId: 4e915f7a-08ec-4c65-915f-2256d6c3a503
> coreTokenString06: true
> coreTokenString07: Bearer
> coreTokenType: OAUTH
> ```

> **Collapse: Client-side OAuth 2.0 grant token**
>
> ```bash
> dn: coreTokenId=f58f19f9-7f3f-43db-be90-466643414143,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenObject: {}
> coreTokenString11: /myRealm
> coreTokenString04: myClient
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenUserId: bjensen
> coreTokenId: f58f19f9-7f3f-43db-be90-466643414143
> coreTokenString06: openid,profile
> coreTokenType: OAUTH2_STATELESS_GRANT
> ```
>
> An example access token issued from this CTS grant token:
>
> ```json
> {
>   "sub": "bjensen",
>   "auth_level": 0,
>   "auditTrackingId": "610b705d-51a9-43e1-b59a-47b372b9d3ae",
>   "iss": "https://am.example.com:8443/am/oauth2/myRealm",
>   "tokenName": "access_token",
>   "token_type": "Bearer",
>   "authGrantId": "f58f19f9-7f3f-43db-be90-466643414143",
>   "nonce": "abcdef",
>   "aud": "myClient",
>   "nbf": 1523281312,
>   "grant_type": "authorization_code",
>   "scope": [
>     "openid",
>     "profile"
>   ],
>   "auth_time": 1523281311000,
>   "realm": "/myRealm",
>   "exp": 1523284912,
>   "iat": 1523281312,
>   "expires_in": 3600,
>   "jti": "c35e5c2a-081b-417f-82c5-2708781816d6"
> }
> ```

## Server-side OAuth 2.0 tokens

* Access tokens

  Server-side OAuth 2.0 access tokens are created when the [one-to-one](cts-tuning-considerations.html#cts-oauth2-storage-scheme) scheme is used.

  They are used in all OAuth 2.0 and OIDC flows and are issued when the OAuth 2.0 provider uses server-side tokens.

  These tokens are typically short-lived.

* Refresh tokens

  Server-side OAuth 2.0 refresh tokens are created when the [one-to-one](cts-tuning-considerations.html#cts-oauth2-storage-scheme) scheme is used.

  They are used in the OAuth 2.0 authorization code grant and resource owner password credentials flows and in the OIDC authorization code and hybrid flows. They are issued when the OAuth 2.0 provider uses server-side tokens.

  These tokens are often long-lived and exchanged for access tokens by clients.

### LDAP attributes

| LDAP attribute    | Server-side OAuth 2.0 access token | Server-side OAuth 2.0 refresh token |
| ----------------- | ---------------------------------- | ----------------------------------- |
| coreTokenUserId   |                                    |                                     |
| coreTokenType     | `OAUTH`                            | `OAUTH`                             |
| coreTokenString01 | *scopes*                           | *scopes*                            |
| coreTokenString02 |                                    |                                     |
| coreTokenString03 | *user*                             | *user*                              |
| coreTokenString04 | *redirect\_uri*                    | *redirect\_uri*                     |
| coreTokenString05 |                                    |                                     |
| coreTokenString06 |                                    |                                     |
| coreTokenString07 | `Bearer`                           | `Bearer`                            |
| coreTokenString08 | *realm*                            | *realm*                             |
| coreTokenString09 | *client ID*                        | *client ID*                         |
| coreTokenString10 | `access_token`                     | `refresh_token`                     |
| coreTokenString11 | *nonce*                            |                                     |
| coreTokenString12 | *grant type*                       | *grant type*                        |
| coreTokenString13 |                                    |                                     |
| coreTokenString14 |                                    |                                     |
| coreTokenString15 | *grant ID*                         | *grant ID*                          |
| coreTokenString16 |                                    |                                     |

### Token examples

> **Collapse: Server-side OAuth 2.0 access token**
>
> ```bash
> dn: coreTokenId=daaa2a39-ffe9-40a0-b0df-71dc6e278628,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenString11: abcdef
> coreTokenObject: {"redirectURI":["https://example.com"],"parent":["cafdd8cc-b155-464a-a020-15013532578c"],"clientID":["myClient"],"auditTrackingId":["ff85ab51-f0b6-48e2-85af-bc26feca5a98-290"],"tokenName":["access_token"],"userName":["bjensen"],"authGrantId":["6f10ad62-1be7-4ebe-aeea-81b7c9eb3735"],"nonce":["abcdef"],"expireTime":["1502145569132"],"grant_type":["authorization_code"],"scope":["openid","profile"],"realm":["/myRealm"],"id":["daaa2a39-ffe9-40a0-b0df-71dc6e278628"],"tokenType":["Bearer"],"refreshToken":["21f89047-4bcf-4d62-853b-d4fa22d632e5"]}
> coreTokenString12: authorization_code
> coreTokenString01: openid,profile
> coreTokenString10: access_token
> coreTokenString15: 6f10ad62-1be7-4ebe-aeea-81b7c9eb3735
> coreTokenString04: https://example.com
> coreTokenString05: 21f89047-4bcf-4d62-853b-d4fa22d632e5
> coreTokenString02: cafdd8cc-b155-464a-a020-15013532578c
> coreTokenString03: bjensen
> coreTokenString08: /myRealm
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenString09: myClient
> coreTokenId: daaa2a39-ffe9-40a0-b0df-71dc6e278628
> coreTokenString07: Bearer
> coreTokenType: OAUTH
> ```

> **Collapse: Server-side OAuth 2.0 refresh token**
>
> ```bash
> dn: coreTokenId=21f89047-4bcf-4d62-853b-d4fa22d632e5,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenObject: {"redirectURI":["https://example.com"],"clientID":["myClient"],"auditTrackingId":["ff85ab51-f0b6-48e2-85af-bc26feca5a98-289"],"tokenName":["refresh_token"],"authModules":[],"userName":["bjensen"],"authGrantId":["6f10ad62-1be7-4ebe-aeea-81b7c9eb3735"],"acr":[],"expireTime":["1502746769129"],"grant_type":["authorization_code"],"scope":["openid","profile"],"realm":["/myRealm"],"id":["21f89047-4bcf-4d62-853b-d4fa22d632e5"],"tokenType":["Bearer"]}
> coreTokenString12: authorization_code
> coreTokenString01: openid,profile
> coreTokenString10: refresh_token
> coreTokenString15: 6f10ad62-1be7-4ebe-aeea-81b7c9eb3735
> coreTokenString04: https://example.com
> coreTokenString03: bjensen
> coreTokenString08: /myRealm
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenString09: MyClient
> coreTokenId: 21f89047-4bcf-4d62-853b-d4fa22d632e5
> coreTokenString07: Bearer
> coreTokenType: OAUTH
> ```

## Other OAuth 2.0 tokens

* OIDC operations (OPS) tokens

  OIDC OPS tokens provide a link between the OIDC ID token and the authenticated session that generated it. They contain a copy of the user's SSO token. This can make the token large when used with a realm that uses client-side sessions.

  These tokens are issued by the authorization code and implicit flows when the `openid` scope is requested, and session management is enabled in the OAuth 2.0 provider. You can disable [session management](../setup/services-configuration.html#enable-session-management) in the OAuth 2.0 provider if you don't use the `endSession` and `checkSession` endpoints; disabling session management reduces the load on the CTS.

* OAuth 2.0 device code tokens

  OAuth 2.0 device code tokens are used to persist the code in the device code flow. The format is the same whether client-side tokens are used or not, and they are typically short-lived.

### LDAP attributes

| LDAP attribute    | OIDC OPS token | OAuth 2.0 device code token |
| ----------------- | -------------- | --------------------------- |
| coreTokenUserId   |                |                             |
| coreTokenType     | **OAUTH**      | **OAUTH**                   |
| coreTokenString01 |                | *scopes*                    |
| coreTokenString02 |                |                             |
| coreTokenString03 |                | *user*                      |
| coreTokenString04 |                |                             |
| coreTokenString05 |                |                             |
| coreTokenString06 |                |                             |
| coreTokenString07 |                |                             |
| coreTokenString08 |                | *realm*                     |
| coreTokenString09 |                | *client ID*                 |
| coreTokenString10 |                | `device_code`               |
| coreTokenString11 |                |                             |
| coreTokenString12 |                |                             |
| coreTokenString13 |                |                             |
| coreTokenString14 |                | *device\_code*              |
| coreTokenString15 |                |                             |
| coreTokenString16 |                |                             |

### Token examples

> **Collapse: Server-side session realm OPS token**
>
> ```bash
> dn: coreTokenId=c23b5787-ace5-43c4-aeb3-369bbf4e07be,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenObject: {"id":["c23b5787-ace5-43c4-aeb3-369bbf4e07be"],"ops":["AQIC5wM2LY4S...kyNgACUzEAAjAx*"],"expireTime":["1502145569141"]}
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenId: c23b5787-ace5-43c4-aeb3-369bbf4e07be
> coreTokenType: OAUTH
> ```

> **Collapse: Client-side session realm OPS token**
>
> ```bash
> dn: coreTokenId=938fbe6a-cab6-48fc-ba42-3dbe82af61f3,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenObject: {"id":["938fbe6a-cab6-48fc-ba42-3dbe82af61f3"],"ops":["AQIC5wM2LY4S...PXN0YXRlbGVzc3JlYWx...kyNgACUzEAAjAx*"],"expireTime":["1502145569471"]}
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenId: 938fbe6a-cab6-48fc-ba42-3dbe82af61f3
> coreTokenType: OAUTH
> ```

> **Collapse: Device code token**
>
> ```bash
> dn: coreTokenId=501905e0-b350-47d5-92cc-161a4291116f,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenObject: {"clientID":["myClient"],"expireTime":["1502142269359"],"user_code":["PDRxhXht"],"auditTrackingId":["ff85ab51-f0b6-48e2-85af-bc26feca5a98-311"],"scope":["profile"],"tokenName":["device_code"],"response_type":["token"],"realm":["/myRealm"],"id":["501905e0-b350-47d5-92cc-161a4291116f"],"userName":["bjensen"],"AUTHORIZED":["true"]}
> coreTokenString01: profile
> coreTokenString10: device_code
> coreTokenString14: PDRxhXht
> coreTokenString03: bjensen
> coreTokenString08: /myRealm
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenString09: myClient
> coreTokenId: 501905e0-b350-47d5-92cc-161a4291116f
> coreTokenType: OAUTH
> ```

## SAML 2.0 tokens

* SAML 2.0 tokens

  SAML 2.0 tokens are only saved to the CTS when SAML 2.0 failover is enabled, which it is by default.

* Assertion tokens

  Assertions are saved to the CTS when SAML 2.0 failover is enabled, the [Assertion Cache](../am-saml2/saml2-reference.html#assertion-cache) is enabled for the IdP, and AM is acting as the IdP.

* AuthnRequest tokens

  AuthnRequests are saved to the CTS when SAML 2.0 failover is enabled and AM is acting as the SP.

The `coreTokenObject` can be either JSON or a base64 encoded string.

### LDAP attributes

| LDAP attribute    | SAML 2.0 token                                  | SAML 2.0 assertion token | SAML 2.0 AuthnRequest token                           |
| ----------------- | ----------------------------------------------- | ------------------------ | ----------------------------------------------------- |
| coreTokenUserId   |                                                 |                          |                                                       |
| coreTokenType     | `SAML2`                                         | `SAML2`                  | `SAML2`                                               |
| coreTokenString01 | `com.sun.identity.saml2.profile.IDPSessionCopy` | `java.lang.String`       | `com.sun.identity.saml2.profile.AuthnRequestInfoCopy` |
| coreTokenString02 |                                                 |                          |                                                       |
| coreTokenString03 |                                                 |                          |                                                       |
| coreTokenString04 |                                                 |                          |                                                       |
| coreTokenString05 |                                                 |                          |                                                       |
| coreTokenString06 |                                                 |                          |                                                       |
| coreTokenString07 |                                                 |                          |                                                       |
| coreTokenString08 |                                                 |                          |                                                       |
| coreTokenString09 |                                                 |                          |                                                       |
| coreTokenString10 |                                                 |                          |                                                       |
| coreTokenString11 |                                                 |                          |                                                       |
| coreTokenString12 |                                                 |                          |                                                       |
| coreTokenString13 |                                                 |                          |                                                       |
| coreTokenString14 |                                                 |                          |                                                       |
| coreTokenString15 |                                                 |                          |                                                       |
| coreTokenString16 |                                                 |                          |                                                       |

### Token examples

> **Collapse: SAML 2.0 token**
>
> ```bash
> dn: coreTokenId=733237633231656432303961383835626662623039343434653564666532323964366632376466343032,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenId: 733237633231656432303961383835626662623039343434653564666532323964366632376466343032
> coreTokenType: SAML2
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenObject:: eyJkb0xvZ291dEFsbCI6ZmFsc2UsIm1ldGFBbGlhcyI6Ii9pZHAiLCJuYW1lSURhbmRTUHBhaXJzIjpbeyJuYW1lSUQiOnsiQGNsYXNzIjoiY29tLnN1bi5pZGVudGl0eS5zYW1sMi5hc3NlcnRpb24uaW1wbC5OYW1lSURJbXBsIiwiZm9ybWF0IjoidXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6cGVyc2lzdGVudCIsImlzTXV0YWJsZSI6dHJ1ZSwibmFtZVF1YWxpZmllciI6Imh0dHBzOi8vaWRwLmV4YW1wbGUuY29tOjQ0My9pZHAiLCJzcE5hbWVRdWFsaWZpZXIiOiJodHRwczovL3NwLmV4YW1wbGUuY29tOjg0NDMvc3AiLCJzcFByb3ZpZGVkSUQiOm51bGwsInZhbHVlIjoiK3h4dXQxc3BCR0lWUWJLMDJMbHBNTUhDS1loVyJ9LCJzcEVudGl0eUlEIjoiaHR0cHM6Ly9zcC5leGFtcGxlLmNvbTo4NDQzL3NwIn1dLCJvcmlnaW5hdGluZ0xvZ291dFJlcXVlc3RCaW5kaW5nIjpudWxsLCJvcmlnaW5hdGluZ0xvZ291dFJlcXVlc3RJRCI6bnVsbCwib3JpZ2luYXRpbmdMb2dvdXRTUEVudGl0eUlEIjpudWxsLCJwZW5kaW5nTG9nb3V0UmVxdWVzdElEIjpudWxsLCJzc29Ub2tlbklEIjoiVWxNY0luVlVfR1VnWEdHbTdwTTA0R2h1WHdvLipBQUpUU1FBQ01ETUFBbE5MQUJ4dldYTlNkbTE0U1cxVUszUnpOVkJLVjFwcU5FODJaVGxxYWpnOUFBUjBlWEJsQUFORFZGTUFBbG14QUFJd01nLi4qIn0
> coreTokenString01: com.sun.identity.saml2.profile.IDPSessionCopy
> ```
>
> If the `coreTokenObject` is a string, you can base64 decode it. For example, the above string decodes as follows:
>
> ```json
> {
>    "doLogoutAll":false,
>    "metaAlias":"/idp",
>    "nameIDandSPpairs":[
>       {
>          "nameID":{
>             "@class":"com.sun.identity.saml2.assertion.impl.NameIDImpl",
>             "format":"urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
>             "isMutable":true,
>             "nameQualifier":"https://idp.example.com:443/idp",
>             "spNameQualifier":"https://sp.example.com:8443/sp",
>             "spProvidedID":null,
>             "value":"+xxut1spBGIVQbK02LlpMMHCKYhW"
>          },
>          "spEntityID":"https://sp.example.com:8443/sp"
>       }
>    ],
>    "originatingLogoutRequestBinding":null,
>    "originatingLogoutRequestID":null,
>    "originatingLogoutSPEntityID":null,
>    "pendingLogoutRequestID":null,
>    "ssoTokenID":"UlMcInVU_GUgXGGm7pM04GhuXwo.*AAJTSQACMDMAAlNLABxvWXNSdm14SW1UK3RzNVBKV1pqNE82ZTlqajg9AAR0eXBlAANDVFMAAlMxAAIwMg..*"
> }
> ```

> **Collapse: Assertion token**
>
> ```bash
> dn: coreTokenId=4141514141465630674d52516d69643478435642777932316a714463507a5733566f62703738524a624b36523866755737303567545070624d44453d,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> control: 1.3.6.1.4.1.36733.2.1.5.1 false: bcb3efeb-14a9-47be-8716-9c18918322c8-19593/8
> changetype: add
> objectClass: frCoreToken
> objectClass: top
> coreTokenId: 4141514141465630674d52516d69643478435642777932316a714463507a5733566f62703738524a624b36523866755737303567545070624d44453d
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenType: SAML2
> coreTokenObject: "<samlp:Response xmlns:samlp=\"urn:oasis:names:tc:SAML:2.0:protocol\" ID=\"s2d254cb2c6567979aa293a25d1e0c2c185c976524\" Version=\"2.0\" IssueInstant=\"2024-08-08T14:21:36Z\" Destination=\"https://sp.example.com:8443/am/Consumer/metaAlias/sp\"><saml:Issuer xmlns:saml=\"urn:oasis:names:tc:SAML:2.0:assertion\">IdP</saml:Issuer><samlp:Status xmlns:samlp=\"urn:oasis:names:tc:SAML:2.0:protocol\">\n<samlp:StatusCode xmlns:samlp=\"urn:oasis:names:tc:SAML:2.0:protocol\" Value=\"urn:oasis:names:tc:SAML:2.0:status:Success\">\n</samlp:StatusCode>\n</samlp:Status><saml:Assertion xmlns:saml=\"urn:oasis:names:tc:SAML:2.0:assertion\" Version=\"2.0\" ID=\"s2f4d9640d71d59c81f145d17cdb738c8ff4d9e5fc\" IssueInstant=\"2024-08-08T14:21:36Z\">\n<saml:Issuer>IdP</saml:Issuer><saml:Subject>\n<saml:NameID NameQualifier=\"IdP\" SPNameQualifier=\"SP\" Format=\"urn:oasis:names:tc:SAML:2.0:nameid-format:persistent\">L+OjhuzCtalCRDSox+F3eMcjxjt2</saml:NameID><saml:SubjectConfirmation Method=\"urn:oasis:names:tc:SAML:2.0:cm:bearer\">\n<saml:SubjectConfirmationData NotOnOrAfter=\"2024-08-08T14:21:36Z\" Recipient=\"https://sp.example.com:8443/am/Consumer/metaAlias/sp\" ></saml:SubjectConfirmationData></saml:SubjectConfirmation>\n</saml:Subject><saml:Conditions NotBefore=\"2024-08-08T14:21:36Z\" NotOnOrAfter=\"2024-08-08T14:21:36Z\">\n<saml:AudienceRestriction>\n<saml:Audience>SP</saml:Audience>\n</saml:AudienceRestriction>\n</saml:Conditions>\n<saml:AuthnStatement AuthnInstant=\"2024-08-08T14:21:36Z\" SessionIndex=\"s251a8cdd305404bdf8a4d493860732c2f75842f01\"><saml:AuthnContext><saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></saml:AuthnContext></saml:AuthnStatement></saml:Assertion>\n</samlp:Response>"
> coreTokenString01: java.lang.String
> ```

> **Collapse: AuthnRequest token**
>
> ```bash
> dn: coreTokenId=733230323466363833626637636133316239333932316532616263653035616164656531323931613964,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: frCoreToken
> objectClass: top
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenId: 733230323466363833626637636133316239333932316532616263653035616164656531323931613964
> coreTokenObject: {"authnRequest":"<samlp:AuthnRequest xmlns:samlp=\"urn:oasis:names:tc:SAML:2.0:protocol\" ID=\"s2024f683bf7ca31b93921e2abce05aadee1291a9d\" Version=\"2.0\" IssueInstant=\"2024-08-08T14:21:36Z\" Destination=\"https://idp.example.com:443/am/SSORedirect/metaAlias/idp\" ForceAuthn=\"false\" IsPassive=\"false\" ProtocolBinding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" AssertionConsumerServiceURL=\"https://am.example.com:8443/am/Consumer/metaAlias/sp\">\n<saml:Issuer xmlns:saml=\"urn:oasis:names:tc:SAML:2.0:assertion\">https://am.example.com:8443/am</saml:Issuer>\n<samlp:NameIDPolicy xmlns:samlp=\"urn:oasis:names:tc:SAML:2.0:protocol\" Format=\"urn:oasis:names:tc:SAML:2.0:nameid-format:persistent\" SPNameQualifier=\"https://am.example.com:8443/am\" AllowCreate=\"true\"></samlp:NameIDPolicy>\n<samlp:RequestedAuthnContext xmlns:samlp=\"urn:oasis:names:tc:SAML:2.0:protocol\" Comparison=\"exact\"><saml:AuthnContextClassRef xmlns:saml=\"urn:oasis:names:tc:SAML:2.0:assertion\">urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport</saml:AuthnContextClassRef></samlp:RequestedAuthnContext>\n</samlp:AuthnRequest>","idpEntityID":"myIdP","paramsMap":{"binding":["HTTP-POST"]},"realm":"/myRealm","relayState":null,"spEntityID":"mySP"}
> coreTokenString01: com.sun.identity.saml2.profile.AuthnRequestInfoCopy
> coreTokenType: SAML2
> ```

## Session tokens

* Session tokens

  The server-side session token is created in the CTS when a user authenticates to a realm configured for server-side sessions. This token allows a user to remain authenticated, even when the AM instance they authenticated to has been shut down.

* Session denylist tokens

  The client-side session denylist token keeps a record of client-side sessions that were ended by logging out. This token is only created when [client-side sessions denylisting](../security/session-state-session-termination.html#session-state-configure-denylist) is enabled.

### LDAP attributes

| LDAP attribute         | Server-side session token | Client-side session denylist token |
| ---------------------- | ------------------------- | ---------------------------------- |
| coreTokenUserId        | *AM internal user DN*     |                                    |
| coreTokenType          | `SESSION`                 | `SESSION_BLACKLIST`                |
| coreTokenString01      |                           | *server id*                        |
| coreTokenString02      |                           |                                    |
| coreTokenString03      |                           |                                    |
| coreTokenString04      |                           |                                    |
| coreTokenString05      | *session token*           |                                    |
| coreTokenString06      | *session handle*          |                                    |
| coreTokenString07      |                           |                                    |
| coreTokenString08      |                           |                                    |
| coreTokenString09      |                           |                                    |
| coreTokenString10      |                           |                                    |
| coreTokenString11      | *realm*                   |                                    |
| coreTokenString12      |                           |                                    |
| coreTokenString13      |                           |                                    |
| coreTokenString14      |                           |                                    |
| coreTokenString15      |                           |                                    |
| coreTokenString16      |                           |                                    |
| coreTokenMultiString01 | *listeners*               |                                    |

### Token examples

> **Collapse: Server-side session token**
>
> ```bash
> dn: coreTokenId=-8288022266790569769,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenString11: /myRealm
> coreTokenObject: {"clientDomain":"dc=example,dc=com","clientID":"id=amadmin,ou=user,dc=example,dc=com",
> "cookieMode":true,"cookieStr":null,"creationTimeInMillis":1502229535517,"isSessionUpgrade":false,
> "listeners":{"9d16b2e1-50c2-43f8-86ce-97a67be1661a":true,"4bd2e5b4-22c8-4172-a2a6-b9f028e86dc8":true},
> "maxCachingTimeInMinutes":3,"maxIdleTimeInMinutes":30,"maxSessionTimeInMinutes":120,"restrictedTokensBySessionID":{},"sessionEventURLs":{},"sessionID":{"comingFromAuth":false,"cookieMode":null,"encryptedString":"AQIC5wM2LY4S...kyNgACUzEAAjAx*","sessionDomain":"dc=example,dc=com","sessionServer":"am.example.com","sessionServerID":"01","sessionServerPort":"8443","sessionServerProtocol":"https","sessionServerURI":"/am"},"sessionProperties":{"Locale":"en","authInstant":"2024-08-08T15:21:03Z","Organization":"dc=example,dc=com","UserProfile":"Required","Principals":"amadmin","successURL":"/am/console","CharSet":"UTF8","Service":"ldapService","Host":"192.0.2.0","cookieSupport":"true","FullLoginURL":"/am/XUI/?realm=%2FmyRealm","AuthLevel":"0","clientType":"genericHTML","AMCtxId":"77a740625b90bc6301","loginURL":"/am/XUI","UserId":"amadmin","AuthType":"DataStore","sun.am.UniversalIdentifier":"id=amadmin,ou=user,dc=example,dc=com","amlbcookie":"01","HostName":"192.0.2.0","Principal":"id=amadmin,ou=user,dc=example,dc=com","UserToken":"amadmin"},"sessionState":"VALID","sessionType":"USER","timedOutTimeInSeconds":0}
> coreTokenInteger07: 30
> coreTokenString12: 1502229535517
> coreTokenInteger06: 120
> coreTokenString04: 1502229797863
> coreTokenString05: AQIC5wM2LY4S...kyNgACUzEAAjAx*
> coreTokenMultiString01: 9d16b2e1-50c2-43f8-86ce-97a67be1661a
> coreTokenMultiString01: 4bd2e5b4-22c8-4172-a2a6-b9f028e86dc8
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenUserId: id=amadmin,ou=user,dc=example,dc=com
> coreTokenId: -8288022266790569769
> coreTokenString06: shandle:AQIC5wM2LY4S...kyNgACUzEAAjAx*
> coreTokenType: SESSION
> ```

> **Collapse: Client-side denylist token**
>
> ```bash
> dn: coreTokenId=7fac1a04-f358-4ed5-958b-48aac6dd5a34,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: top
> objectClass: frCoreToken
> coreTokenString01: 01
> coreTokenDate01: 20240808142103.155Z
> coreTokenExpirationDate:20240808152103.155Z
> coreTokenId: 7fac1a04-f358-4ed5-958b-48aac6dd5a34
> coreTokenType: SESSION_BLACKLIST
> ```

## Notification tokens

The notification token provides alerts for session changes, such as when the maximum session time is reached or there is an active logout. This notification system is used by Agents and PingGateway over WebSockets to receive notifications about these session changes.

### LDAP attributes

| LDAP attribute    | Notification token |
| ----------------- | ------------------ |
| coreTokenUserId   |                    |
| coreTokenType     | `NOTIFICATION`     |
| coreTokenString01 |                    |
| coreTokenString02 |                    |
| coreTokenString03 |                    |
| coreTokenString04 |                    |
| coreTokenString05 |                    |
| coreTokenString06 |                    |
| coreTokenString07 |                    |
| coreTokenString08 |                    |
| coreTokenString09 |                    |
| coreTokenString10 |                    |
| coreTokenString11 |                    |
| coreTokenString12 |                    |
| coreTokenString13 |                    |
| coreTokenString14 |                    |
| coreTokenString15 |                    |
| coreTokenString16 |                    |

### Token example

> **Collapse: Notification token**
>
> ```bash
> dn: coreTokenId=b66384d2-4792-8bb1-f59f-aa5cff6f2e6c-5460,ou=famrecords,ou=openam-session,ou=tokens,dc=example,dc=com
> objectClass: frCoreToken
> objectClass: top
> coreTokenExpirationDate: 20240808152103.155Z
> coreTokenId: b36284d2-f59f-4692-8bb1-aa5cff6f2e6c-5460
> coreTokenObject:: eJyLrlYqyS/ITFayUtJPTE/NK9EvTi0uzszPU9JRSs7PKwGKKFlVK0EFSzNTgAqTjM2MLExSjHTTTC3TdE3MLI10LZKSDHUTE02T09LM0oxSzZJ1TcxNDYBmpJYBTQipLEgF6vPxd/cPDVGqrY0FAOjbJRI=
> coreTokenType: NOTIFICATION
> ```

---

---
title: Deployment architectures
description: Deploy CTS token stores using affinity load balancing for high availability in one data center or site deployment for high availability across multiple data centers
component: pingam
version: 8.1
page_id: pingam:cts:cts-deployment-architectures
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-deployment-architectures.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["CTS Store (Sessions &amp; Tokens)", "Deployment", "Load Balancer"]
page_aliases: ["cts-guide:cts-deployment-architectures.adoc"]
section_ids:
  cts-affinity: CTS affinity deployment
  cts-site-deployments: CTS site deployment
---

# Deployment architectures

You can deploy CTS token stores in a number of deployment architectures, depending on your system requirements:

[icon: sort-alpha-down, set=fad, size=3x]

#### [Affinity CTS token store](#cts-affinity)

For high availability in the same data center.

[icon: globe-americas, set=fad, size=3x]

#### [Site CTS token store](#cts-site-deployments)

For high availability across data centers.

## CTS affinity deployment

With *affinity* load balancing for CTS, AM balances request across available DS servers, always routing LDAP requests for the same CTS token to the same directory server. This prevents AM from reading a token before DS has replicated pending changes. Affinity is well suited for deployments with many AM servers.

Configure AM's Connection String(s) property using the AM admin UI to use server affinity without a load balancer. Find more information on the Connection String(s) property in the [External store configuration](../setup/deployment-configuration-reference.html#cts-external-tokenstore).

Learn more about CTS affinity deployments in the Knowledge Base article [Best practice for using Core Token Service (CTS) Affinity based load balancing in PingAM](https://support.pingidentity.com/s/article/Best-practice-for-using-Core-Token-Service-CTS-Affinity-based-load-balancing-in-PingAM).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The connection strings to the data or identity stores are static and not hot-swappable. This means that, if you expand or contract your DS affinity deployment, AM will not detect the change.To work around this, either:- Manually add or remove the instances from the connection string and restart AM or the container where it runs.

- Configure a [DS proxy](https://docs.pingidentity.com/pingds/8.1/config-guide/proxy.html) in front of the DS instances to distribute data across multiple DS *shards*, and configure the proxy's URL in the connection string. |

## CTS site deployment

CTS supports uninterrupted session availability in deployments with multiple sites when all sites use the same globally replicated CTS store. If an entire site fails or becomes unavailable, AM servers in another site detect the failure of the site's load balancer and attempt to use sessions from the global Core Token Service.

In the event of a failure, client applications can connect to an AM server in an active data center.

![A global Core Token Service replicated across two data centers](_images/global-cts.svg)Figure 1. Global CTS with affinity

For details on DS replication, refer to [Replication](https://docs.pingidentity.com/pingds/8.1/config-guide/replication.html) in the PingDS documentation.

---

---
title: Manage CTS tokens
description: Configure PingAM to encrypt or compress CTS tokens stored in the token store, and manage encryption and compression properties across your deployment
component: pingam
version: 8.1
page_id: pingam:cts:cts-token-managing
canonical_url: https://docs.pingidentity.com/pingam/8.1/cts/cts-token-managing.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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
keywords: ["CTS Store (Sessions &amp; Tokens)", "Setup &amp; Configuration", "Tuning"]
page_aliases: ["cts-guide:cts-tuning-considerations.adoc"]
section_ids:
  cts-tuning-cache-size: Reaper cache size
  cts-tuning-tokenlimit: Reaper search size
  cts-oauth2-storage-scheme: OAuth 2.0 CTS storage scheme
  cts-logout-user-poll-interval: CTS poll interval
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
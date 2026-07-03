---
title: Account lockout
description: Configure account lockout to lock user accounts after repeated failed login attempts, slowing down brute-force attacks and compensating for weak password policies
component: pingam
version: 8.1
page_id: pingam:security:account-lockout
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/account-lockout.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Identities", "Features"]
page_aliases: ["security-guide:account-lockout.adoc"]
section_ids:
  to-configure-acct-lockout: Configure account lockout
  customize-lockout-messages: Customize account lockout messages
---

# Account lockout

*Account lockout* is a security mechanism that locks a user account after repeated failed login attempts. Use it to slow down brute-force attacks and compensate for weak password policies.

Most deployments use the identity store's password policy to control account lockout. If this isn't an option in your deployment, configure account lockout as explained in this section.

Use persistent lockout where possible. If that's not compatible with your company policy, use a duration lockout of at least 15 minutes.

You can configure account lockout in *one* of the following ways:

* Persistent lockout

  Persistent (physical) lockout locks the user's account indefinitely until unlocked by an administrator.

  This is the default type of account lockout and the best way to mitigate brute-force attacks.

  For persistent lockout, AM sets the user account status to `inactive` in the user profile, and tracks failed authentication attempts by writing to the user repository. The `inactive` status makes it easier for an administrator to search for user accounts with persistent lockout.

  Persistent lockout works independently of account lockout mechanisms in the underlying directory server that serves as the user datastore.

* Duration lockout

  Duration lockout locks the user account for a specified duration, keeping track of the locked state either in memory or in the datastore.

  The default configuration is to record invalid authentication attempts in the datastore. This avoids the need for sticky load balancing. If you choose to store the count of invalid attempts in memory, the counter applies to the current AM instance only. Also, if you restart AM and lockout is stored in memory, duration lockouts on all accounts are released. Otherwise, the lock is released automatically after the specified duration.

  Unlike persistent lockout, the user account status remains `active` for duration lockout.

|   |                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Failed login attempts during the [transactional authorization](../am-authorization/transactional-authorization.html) flow don't increment account lockout counters.If login failures are stored in AM's memory, this might result in user accounts not being locked out, even after multiple login failures. To avoid this issue, implement persistent lockout instead. |

## Configure account lockout

1. Configure account lockout:

   * In the AM admin UI, go to Realms > *realm name* > Authentication > Settings > Account Lockout.

   * Enable lockout by checking Login Failure Lockout Mode, then set the number of attempts and the lockout interval.

     You can also opt to warn users after several consecutive failures.

   * Enable Store Invalid Attempts in Data Store to save account login failures to the datastore. This setting is necessary when using server-side or client-side journey sessions. If you don't set this, users might not be locked out even after multiple login failures.

     When you store the number of failed attempts in the datastore, other AM servers accessing the user datastore also have access to that information.

   * If AM is configured to [send mail](../setup/deployment-configuration-reference.html#general-mailserver), you can set up email notification of lockouts to an administrator.

2. Configure persistent lockout:

   * Set Login Failure Lockout Duration to `0`.

   * Optionally, set Lockout Attribute Name and Lockout Attribute Value to specify an additional attribute to update on lockout.

     By default, AM sets the value of the user's `inetuserstatus` attribute to `Inactive`.

   * Optionally, set Invalid Attempts Data Attribute Name to specify a custom attribute to store the number of failed authentication attempts.

3. Configure duration lockout:

   * Set Login Failure Lockout Duration to a positive value representing the duration in minutes.

     A value of at least 15 minutes is recommended.

   * Optionally, set Lockout Duration Multiplier to increase the lockout duration on each successive lockout.

   * Enable Store Invalid Attempts in Data Store so that lockout attempts aren't stored in memory, but persisted in the repository, and applied across all AM instances.

   * Set Invalid Attempts Data Attribute Name to the default attribute `sunAMAuthInvalidAttemptsData` to prevent invalid attempts from being stored only in memory.

   Learn more in [account lockout configuration](../am-authentication/authn-core-settings.html#authn-core-account-lockout).

|   |                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To unlock a user's account:- Locate the user under Realms > *realm name* > Identities.

- Choose the user you want to unlock.

- Set their User Status property to Active.

- Click Save. |

Find information on how authentication trees handle account lockout in [Account lockout for trees](../am-authentication/auth-nodes-and-journeys.html#account-lockout-trees).

## Customize account lockout messages

To customize the messages shown to end users when their accounts are locked, follow these steps:

1. Locate the `openam-core-8.1.1.jar` file in the `WEB-INF/lib/` folder where AM is deployed.

2. Extract the `amAuth.properties` file.

3. Change the value of the `lockOut` field to control the lockout message. For example:

   ```
   lockOut=Your example.com account has been locked. Please contact your support agent.|user_inactive.jsp
   ```

4. Copy the amended `amAuth.properties` file to the `WEB-INF/classes/` folder where AM is deployed.

5. When a user whose account is locked attempts to authenticate, the custom lockout message is displayed:

   ![Custom account lockout message](_images/custom-lockout-message.png)

---

---
title: Additional cookie security
description: Configure PingAM cookie security beyond session cookies, including SameSite rules, secure cookie filters, and sticky load balancing cookie naming
component: pingam
version: 8.1
page_id: pingam:security:additional-cookie-considerations
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/additional-cookie-considerations.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Sessions"]
page_aliases: ["security-guide:additional-cookie-considerations.adoc"]
---

# Additional cookie security

Although the session cookie is the most important cookie to keep track of when securing AM, there are other points you must consider, such as:

* Which cookie are you using for sticky load balancing?

  By default, AM creates the `amlbcookie` cookie and sets it to the ID of the instance that first responded to a request. You should change the name of this cookie to something unique in your environment.

* Which other cookies, relevant for your environment, interact with AM or are sent to AM as part of a chain of requests?

The following table summarizes the tasks and information to review to manage cookie security that is not strictly related to the session cookie:

| Task                                                                                                                                                                               | Resources                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Enable support for `SameSite` rules**Configure AM to apply `SameSite` rules, such that you can declare that your cookies are restricted to a first-party or a same-site context. | [SameSite cookie rules](enable-samesite-cookies.html)                       |
| **Review the secure cookie filter**AM provides a filter that upgrades cookies to secure cookies if the conditions are met.                                                         | [Secure cookie filter](secure-cookie-filter.html)                           |
| **Change the name of the sticky load balancing cookie**Name the cookie something relevant and unique for your environment.                                                         | [Change the sticky load balancing cookie name](change-amlbcookie-name.html) |

---

---
title: AM features that use keys
description: Configure PingAM features to use keys for signing or encryption through the keystore or secrets API, with specific requirements varying by feature
component: pingam
version: 8.1
page_id: pingam:security:features-with-keys
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/features-with-keys.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "OAuth 2.0", "SAML 2.0", "Features"]
page_aliases: ["security-guide:features-with-keys.adoc"]
---

# AM features that use keys

Features that require secrets for signing or encryption can use one of the following mechanisms:

* The AM keystore, configured at Configure > Server Defaults > Security > Key Store.

* The secrets API (secret stores).

Certain features *require* secret stores and some support either secret mechanism. This list outlines which features can use which secret mechanism:

* Features that only use the AM keystore

  * **User self-service**

    Requires a JCEKS keystore with a key pair alias for encryption and a key alias for signing.

    Learn more in [Create a user self-service service instance](../user-self-service/configuring-uss.html#create-uss-service).

  * **Amster**

    Requires an `sms.transport.key` key alias to export and import encrypted passwords.

    Learn more in [Create transport keys to export configuration data](../amster/transport-keys.html).

  * **IDM user self-registration**

    Requires copying signing and encryption keys from IDM into the AM keystore.

    Learn more in [Delegate user self-registration to IDM](../user-self-service/configuring-user-self-registration.html#configure-user-self-registration-idm).

* Features that use secret stores

  * **Client-side sessions**

    Require keys or secrets for signing and encrypting client-side journey and authenticated sessions.

    Learn more in [Client-side session security](session-state-configure-cookie-security.html).

  * **Authentication trees**

    Requires a key alias to encrypt values stored in the authentication tree's transient state.

    Learn more in [Store values in a tree's node states](../auth-nodes/store-values-shared-state.html#store-values-in-transient-state).

  * **OAuth 2.0 providers**

    Require a key alias for signing [client-side tokens](../am-oauth2/stateless-oauth2.html#configure-client-side-signatures) and [OpenID Connect ID tokens](../am-oidc1/managing-jwk_uri.html#oauth2-oidc-digital-signatures). Also require a key alias for encryption of client-side OAuth 2.0 access and refresh tokens.

    Learn more in [Configure client-side OAuth 2.0 token encryption](../am-oauth2/stateless-oauth2.html#oauth2-client-side-encryption).

  * **Web and Java agents**

    Web agents and Java agents communicate with AM using a built-in OAuth 2.0 provider, configured globally in AM. This communication requires a key alias for signing tokens.

    Learn more in the [Web Agents User Guide](https://docs.pingidentity.com/web-agents/2025.3/user-guide) and the [Java Agents User Guide](https://docs.pingidentity.com/java-agents/2025.3/user-guide).

  * **Remote Consent service**

    Requires a key alias for signing consent responses, and another key alias for encrypting consent responses.

    Learn more in [Remote consent](../am-oauth2/oauth2-remote-consent.html).

  * **SAML 2.0 federation**

    Requires key pairs for signing and encrypting messages, responses, and assertions; for example, a key to encrypt the JWT stored in the local storage of supported browsers.

    You could also require a key to sign exported metadata.

    Learn more in [Sign and encrypt messages](../am-saml2/saml2-encryption.html). You can find a list of the secret label mappings in [Secret label default mappings](secret-mapping.html#secret-label-mappings).

  * **Persistent cookie nodes**

    Requires a key pair alias for encryption.

    Learn more in [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/8.1/set-persistent-cookie.html).

* Features that support different keystore configurations

  * **ForgeRock Authenticator (OATH), ForgeRock Authenticator (PUSH), and the WebAuthn Profile Encryption services**

    Support configuring a different keystore to encrypt device profiles. Also support keystore types that aren't available to other features.

    Learn more in [Multi-factor authentication](../am-authentication/authn-introduction-authn.html#about-mfa).

  * **AM's startup (bootstrap) process**

    Requires two password strings. Use the AM keystore as the bootstrap keystore where possible. If you configure a different bootstrap keystore, you must:

    * Keep the password strings updated.

    * Overwrite the `boot.json` file before AM starts up.

    Learn more in [Replace the AM keystore](am-keystore.html#proc-bootstrap-keystore).

* Features that require different keystore configurations

  * **Java fedlets**

    Require a keystore containing a key pair to sign and verify XML assertions and to encrypt and decrypt SAML assertions. Keystore and key information are configurable in the `FederationConfig.properties` file. Learn more in [Configure Java fedlet properties](../am-saml2/create-configure-fedlet.html#unconfigured-fedlet-properties).

  * **Security token service**

    Requires a JKS keystore for encrypting SAML 2.0 and OpenID Connect tokens. Doesn't require files to store the keystore password or the key aliases' passwords.

    Learn more in [Configure STS instances](../sts/sts-using-console.html).

  * **CSV audit logging handler**

    Requires a keystore for tamper-proofing. Doesn't require a file to store the keystore password; the password is configured in the AM admin UI. Learn more in [Configure CSV audit event handlers](../monitoring/implementing-audit.html#configuring-csv-audit-event-handlers).

---

---
title: Change default key aliases
description: Replace demo key aliases in PingAM with production keys for security-sensitive features including OAuth 2.0, OpenID Connect, SAML2, persistent cookies, and authentication trees
component: pingam
version: 8.1
page_id: pingam:security:change-signing-key
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/change-signing-key.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration"]
page_aliases: ["security-guide:change-signing-key.adoc"]
---

# Change default key aliases

For demo and test purposes, AM includes [demo key aliases](secrets-certs-keys.html#about-default-keystores) for several features.

|   |                                                                                                  |
| - | ------------------------------------------------------------------------------------------------ |
|   | Don't use the default key aliases, keys, keystores, or secret stores in production environments. |

When possible, the following list includes the Global Services or Server Default paths where the demo key aliases are configured. If you have already configured any of the features in a realm, ensure that the key alias is replaced in the realm configuration as well.

To replace the default key aliases:

1. Create the required key aliases following the tasks in [Key aliases and passwords](configuring-keys.html).

2. Change the default key aliases:

   * Web agents and Java agents

     Agents use the secret labels specified in the [Web Agents Installation Guide](https://docs.pingidentity.com/web-agents/2025.3/installation-guide/post-installation.html#configuring-agent-communication) and the [Java Agents Installation Guide](https://docs.pingidentity.com/java-agents/2025.3/installation-guide/pre-installation.html#configuring-agent-communication).

   * Persistent Cookie node

     To change the default mapping for the Persistent Cookie node, go to Realms > *realm name* > Authentication > Settings > Security. Replace the `test` key alias in the Persistent Cookie Encryption Certificate Alias field with the alias you created for persistent cookies in your secret stores.

     You can find more information about the secret labels used by this feature in [Secret label mappings for persistent cookies](secret-mapping.html#secrets-persistent-cookie).

   * OAuth 2.0 and OpenID Connect providers

     Review the list of secret labels and their defaults [here](secret-mapping.html#oauth2-default-secret-IDs) and [here](secret-mapping.html#oidc-social-registration-secret-IDs).

   * SAML 2.0 hosted providers

     Review the list of secret labels and their defaults [here](secret-mapping.html#saml2-default-secret-IDs).

   * Client-side sessions

     Review the list of secret labels and their defaults [here](secret-mapping.html#secrets-client-based-sessions-encryption) and [here](secret-mapping.html#secrets-client-based-sessions-signing).

   * User self-service

     Go to Realms > *realm name* > Services > User Self-Service and do one of the following:

     * Enable the Use Secret Store property and configure the following secret IDs in the secret store:

       * `am.services.selfservice.token.encryption`

       * `am.services.selfservice.token.signing`

     * Populate the values of the Encryption Key Pair Alias and the Signing Secret Key Alias properties.

       |   |                                                                                         |
       | - | --------------------------------------------------------------------------------------- |
       |   | The name of the demo keys displays in grey. This doesn't mean the fields are filled in. |

   * Authentication trees

     Authentication trees use the secret label specified in [Secret label mappings for encrypting authentication trees' secure state data](secret-mapping.html#secrets-authn-trees-transient-encryption).

     |   |                                                                                                                                            |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | You must map this secret label to an existing, resolvable secret or key alias. Otherwise, authentication trees might not work as expected. |

   * IoT

     The IoT Service uses the secret labels specified in [Secret label mappings for the IoT trusted JWT issuer](secret-mapping.html#secrets-am-services-iot-jwt-issuer-signing).

---

---
title: Change the cookie domain
description: "Configure PingAM's cookie domain to ensure only users and entities from trusted domains can be authenticated"
component: pingam
version: 8.1
page_id: pingam:security:changing-cookie-domain
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/changing-cookie-domain.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration"]
page_aliases: ["security-guide:changing-cookie-domain.adoc"]
---

# Change the cookie domain

Configure AM's cookie domain to ensure only users and entities from trusted domains can be authenticated.

By default, the AM installer sets the cookie domain based on the fully qualified hostname of the server on which it installs AM, such as `am.example.com`.

After installation, you may want to change the cookie domain to `example.com` so AM can communicate with any host in the sub-domain.

1. In the AM admin UI, go to Configure > Global Services > Platform > Cookie Domain.

2. In the Cookie Domain field, set the list of domains into which AM should write cookies. Consider the following points:

   * Configure as many cookie domains as your environment requires. For example, for the realms configured with DNS aliases. (For more information, see [Realms](../setup/am-realms.html).) Browsers ignore any cookies that do not match the current domain to ensure the correct one is used.

   * If you do not specify any cookie domain, AM uses the fully qualified name of the server, which implies that a host cookie is set rather than a domain cookie.

     When configuring AM for Cross-Domain Single Sign-On (CDSSO), you must protect your AM deployment against cookie hijacking by setting a host cookie rather than a domain cookie. For more information, see [Restrict tokens for CDSSO session cookies](enable-cdsso-cookie-hijacking-protection.html).

   * Do not configure a top-level domain as your cookie domain because browsers will reject them. Top-level domains are browser-specific. For example, Firefox considers special domains like Amazon's web service (for example, `ap-southeast-2.compute.amazonaws.com`) to be a top-level domain. (For a list of effective top-level domains, see <https://publicsuffix.org/list/effective_tld_names.dat>.)

   * Do not configure the cookie domain such that it starts with a dot (`.`) character. For example, configure `example.com` instead of `.example.com`.

   * If you are using Wildfly as the AM web container with multiple cookie domains, you must set the advanced server property, `com.sun.identity.authentication.setCookieToAllDomains`, to `false`.

     Set this property in the AM admin UI, under Configure > Server Defaults > Advanced.

3. Save your changes.

4. Restart AM or the container where it runs.

---

---
title: Change the session cookie name
description: Change the session cookie name from the default iPlanetDirectoryPro to a unique value that does not reveal its contents
component: pingam
version: 8.1
page_id: pingam:security:change-name-of-SSO-cookie
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/change-name-of-SSO-cookie.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Sessions", "Authentication", "Setup &amp; Configuration"]
page_aliases: ["security-guide:change-name-of-SSO-cookie.adoc"]
---

# Change the session cookie name

By default, the session cookie name is `iPlanetDirectoryPro`.

You must change this value to something unique in your environment that does not give away its contents. Do not use names such as `sessionCookie`.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | If you change the cookie name on a production system, you invalidate the sessions for any users who still had a valid cookie. |

1. In the AM admin UI, go to Configure > Server Defaults > Security > Cookie.

2. Change the name in the Cookie Name field.

3. Click Save Changes.

4. Restart AM or the container where it runs.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Web agents need to know the name of the session cookie to authenticate with AM. Learn more in [SSO token cookie name](https://docs.pingidentity.com/web-agents/2025.3/user-guide/cookie-reset.html#sso-cookie-name). |

---

---
title: Change the sticky load balancing cookie name
description: Change the sticky load balancing cookie name from the default amlbcookie to a unique value in your environment
component: pingam
version: 8.1
page_id: pingam:security:change-amlbcookie-name
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/change-amlbcookie-name.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Sessions", "Setup &amp; Configuration"]
page_aliases: ["security-guide:change-amlbcookie-name.adoc"]
---

# Change the sticky load balancing cookie name

By default, the sticky load balancing cookie name is `amlbcookie`. Change this value to something that is unique in your environment, and configure the name of the cookie in your load balancers to achieve session stickiness.

Perform the following steps to change the name of the cookie:

1. Go to Configure > Server Defaults > Advanced.

2. Change the value of the `com.iplanet.am.lbcookie.name` advanced server property to the new cookie name.

   By default, AM sets the value of the load balancing cookie to the ID of the instance that first responded to a request. You can change it, but we recommend that you keep this configuration when using web agents.

   For more information, see [Load balancing](../setup/configure-lb.html).

3. Restart AM or the container where it runs.

---

---
title: Client-side session security
description: Configure PingAM to sign and encrypt client-side session JWTs to prevent tampering and protect sensitive session data from man-in-the-middle attacks
component: pingam
version: 8.1
page_id: pingam:security:session-state-configure-cookie-security
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/session-state-configure-cookie-security.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration", "Sessions"]
page_aliases: ["security-guide:session-state-configure-cookie-security.adoc"]
section_ids:
  session-state-configure-jwt-signature: Configure the JWT signature
  session-state-configure-jwt-encryption: Configure JWT encryption
  policy_agent5_client-based: Client-side session security and agents
---

# Client-side session security

AM can issue *server-side* sessions, which contain a reference to the real session stored in the CTS store, or *client-side* sessions, which contain all the information that would be held in the CTS store.

While both types are susceptible to cookie hijacking, client-side sessions are even more vulnerable, since they contain all the information for the session. Therefore, a malicious user could tamper with the session data to their benefit.

When using client-side journey and authenticated sessions, you should configure AM to sign and/or encrypt the JWT containing session information:

* JWT signing

  AM verifies that the JWT is authentic by validating a signature configured in the Session Service. AM thwarts attackers who might attempt to tamper with the contents of the JWT or its signature, or who might attempt to sign the JWT with an incorrect signature.

- JWT encryption

  Knowledgeable users can easily decode JWTs. Because an AM journey or authenticated session contains information that could be considered sensitive, encrypting the JWT that contains it protects its contents, ensuring opaqueness.

  Encrypting the JWT prevents man-in-the-middle attacks that could log the state of every AM session. Encryption also ensures that end users are unable to access the information in their AM session.

**Client-side journey and authenticated sessions share the same encryption and signing configuration.**

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Web agents and Java agents don't support both signing *and* encrypting the session cookie. This ensures that the client-side session cookie size isn't greater than the browser supported size.Learn more in [Client-side session security and agents](#policy_agent5_client-based). |

## Configure the JWT signature

Configure a JWT signature to prevent malicious tampering of client-side journey and authenticated session JWTs. Follow these steps to configure the JWT signature:

1. Go to Configure > Global Services > Session > Client-Side Sessions.

2. From the Signing Algorithm Type drop-down menu, choose a suitable algorithm for your environment.

   The default value is `HS256`.

3. Map a suitable secret that corresponds to the algorithm you selected:

   * For an HMAC signing algorithm, map a suitable secret to the `am.global.services.session.clientbased.signing.HMAC` secret label.

   * For the RS256 signing algorithm, map a suitable secret to the `am.global.services.session.clientbased.signing.RSA` secret label.

   * For the elliptic curve algorithms, map a suitable secret to one of the corresponding secret labels:

     * `am.global.services.session.clientbased.signing.ES256`

     * `am.global.services.session.clientbased.signing.ES384`

     * `am.global.services.session.clientbased.signing.ES512`

   You can only configure these secrets at a global level.

   Learn more about mapping secrets to secret labels in [Secret stores](secret-stores.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't sign the JWT if you plan to encrypt it with the Direct AES Encryption algorithm, because the signature will be redundant.To disable JWT signing:1. Go to Configure > Global Services > Session > Client-Side Sessions.

2. From the Signing Algorithm Type drop-down list, choose `NONE`.

3. Go to Configure > Server Defaults > Advanced.

4. Set `org.forgerock.openam.session.stateless.signing.allownone` to `true`.

   > **Collapse: How do I configure advanced server properties?**
   >
   > * To configure advanced server properties for all instances of the AM environment, go to Configure > Server Defaults > Advanced in the AM admin UI.
   >
   > * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
   >
   > If the property you want to add or edit is already configured, click on the pencil ([icon: pencil-alt, set=fas]) button to edit it. When you are finished, click on the tick ([icon: check, set=fas]) button.
   >
   > Click Save Changes.

5. Save your work. |

Learn more about Session service configuration attributes in [Session](../setup/services-configuration.html#global-session).

## Configure JWT encryption

Configure JWT encryption to prevent man-in-the-middle attackers from accessing users' session details, and to prevent end users from examining the content in the JWT.

For FBC installations, if you use client-side sessions for authentication, you must set an encryption key after the initial install, even if you map a secret label to this key. The key that's generated by default doesn't work for client-side authentication sessions.

Follow these steps to encrypt the JWT:

1. Go to Global Services > Session > Client-Side Sessions.

2. From the Encryption Algorithm drop-down list, choose a suitable algorithm:

   1. If you select the `RSA` algorithm, also follow these steps:

      * [Configure JWT encryption](#session-state-configure-jwt-encryption).

      * Map a suitable secret to the `am.global.services.session.clientbased.encryption.RSA` secret label.

        You can only configure this secret at a global level.

        Learn more about configuring secrets in [Secret stores](secret-stores.html).

      * Configure one of the following paddings in the `org.forgerock.openam.session.stateless.rsa.padding` advanced server property:

        **RSA1\_5**. RSA with PKCS#1 v1.5 padding.\
        **RSA-OAEP**. RSA with OAEP and SHA-1.\
        **RSA-OAEP-256**. RSA with OAEP padding and SHA-256.

        The default is `RSA-OAEP-256`.

        > **Collapse: How do I configure advanced server properties?**
        >
        > * To configure advanced server properties for all instances of the AM environment, go to Configure > Server Defaults > Advanced in the AM admin UI.
        >
        > * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
        >
        > If the property you want to add or edit is already configured, click on the pencil ([icon: pencil-alt, set=fas]) button to edit it. When you are finished, click on the tick ([icon: check, set=fas]) button.
        >
        > Click Save Changes.

   2. If you select the AES KeyWrapping or Direct AES Encryption algorithms, also map a suitable secret to the `am.global.services.session.clientbased.encryption.AES` secret label.

      You can only configure this secret at a global level.

      Learn more about configuring secrets in [Secret stores](secret-stores.html).

      |   |                                                                                                                                                                                                                             |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | AES key wrap is a symmetric encryption method, which means the same key is used for encrypting and decrypting. Make sure you use the same secret on all AM instances to allow any AM instance to decrypt the encrypted JWT. |

      * For direct encryption with AES-GCM, or for AES-KeyWrap with any content encryption method, the secret must be 128, 192, or 256 bits long.

      * For direct encryption with AES-CBC-HMAC, the secret must be 256, 384, or 512 bits long.

      * For the underlying content encryption method, configure one of the following encryption methods in the `org.forgerock.openam.session.stateless.encryption.method` advanced server property:

        **A128CBC-HS256**. AES 128-bit in CBC mode with HMAC-SHA-256-128 hash (HS256 truncated to 128 bits)\
        **A192CBC-HS384**. AES 192-bit in CBC mode with HMAC-SHA-384-192 hash (HS384 truncated to 192 bits)\
        **A256CBC-HS512**. AES 256-bit in CBC mode with HMAC-SHA-512-256 hash (HS512 truncated to 256 bits)\
        **A128GCM**. AES 128-bit in GCM mode\
        **A192GCM**. AES 192-bit in GCM mode\
        **A256GCM**. AES 256-bit in GCM mode

        The default is `A128CBC-HS256`.

        > **Collapse: How do I configure advanced server properties?**
        >
        > * To configure advanced server properties for all instances of the AM environment, go to Configure > Server Defaults > Advanced in the AM admin UI.
        >
        > * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
        >
        > If the property you want to add or edit is already configured, click on the pencil ([icon: pencil-alt, set=fas]) button to edit it. When you are finished, click on the tick ([icon: check, set=fas]) button.
        >
        > Click Save Changes.

3. To compress the session state, choose Deflate Compression from the Compression Algorithm drop-down list.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When set to Deflate compression, this option may lead to a possible vulnerability with session state information leakage. Because the session token compression depends on the data in the session, an attacker can vary one part of the session (for example, the username or some other property) and then deduce some secret parts of the session state by examining how the session compresses. You should evaluate this threat depending on your use cases before enabling compression and encryption together. |

   By default, AM rejects compressed session JWTs that expand to a size larger than 32 KiB (32768 bytes). Learn more in [Control the size of compressed JWTs](control-maximum-size-decompressed-JWT.html).

4. Save your work.

Learn more about Session service configuration attributes in [Session](../setup/services-configuration.html#global-session).

## Client-side session security and agents

To prevent the client-side session cookie size exceeding the browser supported size, web agents and Java agents don't support both signing and encrypting the session cookie. To configure agents with client-side sessions, implement one of the following configurations:

* Configure signing and compression:

  1. Enable HS256 signing for the client-side session cookie.

     Learn more in [Configure the JWT signature](#session-state-configure-jwt-signature).

  2. Enable compression. Go to Configure > Global Services > Session > Client-Side Sessions and choose Deflate Compression from the Compression Algorithm drop-down list.

* Configure encryption and compression:

  1. Set the `org.forgerock.openam.session.stateless.signing.allownone` advanced server property to `true` for all the instances in the environment.

  > **Collapse: How do I configure advanced server properties?**
  >
  > * To configure advanced server properties for all instances of the AM environment, go to Configure > Server Defaults > Advanced in the AM admin UI.
  >
  > * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
  >
  > If the property you want to add or edit is already configured, click on the pencil ([icon: pencil-alt, set=fas]) button to edit it. When you are finished, click on the tick ([icon: check, set=fas]) button.
  >
  > Click Save Changes.

  1. Disable signing for the client-side session cookie. Go to Configure > Global Services > Session > Client-Side Sessions and choose NONE from the Signing Algorithm Type drop-down list.

  2. Enable Direct AES Encryption.

     Learn more in [Configure JWT encryption](#session-state-configure-jwt-encryption).

  3. Enable compression. Go to Configure > Global Services > Session > Client-Side Sessions and choose Deflate Compression from the Compression Algorithm drop-down list.

Failure to set up client-side sessions correctly can cause unexpected errors when accessing a protected resource, such as blank pages and redirection loops.

Client-side sessions don't support restricted tokens. Therefore, web agents and Java agents configured in a realm configured for client-side sessions aren't protected against cookie hijacking. Use web or Java agents with server-side sessions where possible.

---

---
title: Configure AM behind a reverse proxy
description: Configure PingAM behind a reverse proxy to provide security benefits including denial of service protection, SSL termination, and restricted access to internal endpoints
component: pingam
version: 8.1
page_id: pingam:security:reverse-proxy
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/reverse-proxy.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Deployment", "Setup &amp; Configuration"]
page_aliases: ["security-guide:reverse-proxy.adoc"]
section_ids:
  reverse_proxy_deployment_examples: Reverse proxy deployment examples
  expose_only_the_reverse_proxy_to_the_internet: Expose only the reverse proxy to the internet
  protect_am_with_pinggateway: Protect AM with PingGateway
  high_level_tasks_to_configure_am_behind_a_proxy: High-level tasks to configure AM behind a proxy
  outbound-communication: Configure AM for outbound communication
  configure-base-url-source: Configure the Base URL source service
---

# Configure AM behind a reverse proxy

Reverse proxies (such as PingGateway) are proxy servers that sit between clients and application servers. Their main function is to act on behalf of the application server, forwarding resources to the client as if they were the application server itself.

Modern reverse proxies provide additional functionality such as load balancing, compression, SSL termination, web acceleration, and firewall capabilities.

Configuring a reverse proxy in front of your AM instances provides the following security benefits:

* Protecting AM servers from denial of service attacks.

  A reverse proxy will terminate incoming connections and reopen them against the AM servers, effectively masking the AM IP addresses. This makes it more difficult for attackers to launch DoS attacks against them. A firewall can prevent direct access to the AM servers.

* SSL termination/SSL offloading.

  Since reverse proxies terminate incoming connections to AM, they also decrypt the HTTPS requests and pass them unencrypted to the container where AM runs.

  This has several benefits, such as removing the need to install certificates in the containers, which simplifies the management of SSL/TLS.

  Depending on your environment, you could decide to configure SSL/TLS between AM and the reverse proxy, or to configure the proxy to pass-through the SSL traffic to the container where AM runs.

  These topics assume that AM is configured to use HTTPS communication.

* Unique point of access to AM.

  Configuring a reverse proxy in front of AM creates a channel between the public network and the internal network.

  Because all communication to AM must come from the reverse proxy, you can, for example, restrict access to a set of trusted networks. You can fine-tune the access restrictions for each request and apply rate-limiting and load balancing such that a possible attack does not bring down your whole infrastructure.

* Protecting endpoints

  In the same way that you can restrict access to trusted networks, you can also restrict access to any endpoint AM is exposing.

  AM exposes a number of internal administration endpoints, such as the `/sessionservice` endpoint. You must ensure those are not reachable over the Internet.

  You can find a list of internal endpoints that you should protect in [Service endpoints](../am-reference/endpoints-reference.html).

  Regarding feature endpoints, AM makes endpoints accessible the moment an administrator creates a service. For example, the OAuth 2.0 endpoints are not available by default, but configuring an instance of the OAuth 2.0 provider service in a realm will make the endpoints available for that realm.

  You must ensure you are exposing the correct endpoints to the Internet.

## Reverse proxy deployment examples

Providing recommendations on setting up your network infrastructure is beyond the scope of this document. There are too many permutations that are valid use cases; for example, some environments may deploy a reverse proxy for its load balancing capabilities instead of dedicated, hardware-based load balancers. More complex deployments may have multiple layers of firewalls, load balancers, and reverse proxies.

This section covers two basic deployment examples.

### Expose only the reverse proxy to the internet

The following figure illustrates a deployment architecture where AM services are protected behind an internet-facing reverse proxy.

![Expose only the necessary endpoints outside your infrastructure.](_images/securing-openam-rp.png)

### Protect AM with PingGateway

In its role as a reverse proxy, PingGateway can protect AM.

Learn more in [Protect PingAM](https://docs.pingidentity.com/pinggateway/2025.11/gateway-guide/protect-am.html) in the PingGateway documentation.

## High-level tasks to configure AM behind a proxy

The following table summarizes the high-level tasks required to configure AM when it is behind a proxy:

| Task                                                                                                                                                                                  | Resources                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Configure the proxy's details**Configure AM or the container where it runs to route outbound traffic through the proxy.                                                             | [Configure AM for outbound communication](#outbound-communication)  |
| **Configure the Base URL service**Services configure their endpoints based on AM's URL. The Base URL service remaps the endpoints of the services that require it to the proxy's URL. | [Configure the Base URL source service](#configure-base-url-source) |

## Configure AM for outbound communication

Clients from different networks connect to AM to use its functionality. These clients initiate communication with AM and the container where it runs. However, when AM acts as a client to a third-party application, it makes outbound calls outside its container to retrieve information or services.

If your network requires outbound traffic to go through a proxy, you must configure AM to route its client requests accordingly. To do this, provide the proxy's details to AM and the container where it runs:

1. Set the relevant proxy JVM options in the container where AM runs.

   > **Collapse: HTTPS options**
   >
   > * `-Dhttps.proxyHost`
   >
   >   IP address or hostname of the proxy server. For example, `proxy.example.com`.
   >
   > * `-Dhttps.proxyPort`
   >
   >   Port number of the proxy server. For example, `8443`.
   >
   > * `-Dhttp.nonProxyHosts`
   >
   >   A pipe-separated (`|`) list of IP addresses or hostnames that should be reached directly, bypassing the proxy configuration. For example, `localhost|internal.example.com`.
   >
   >   Use wildcards (`*`) at the beginning or the end of the address or hostname. For example, `*.example.com` or `internal*`.

   > **Collapse: HTTP options**
   >
   > * `-Dhttp.proxyHost`
   >
   >   IP address or hostname of the proxy server. For example, `proxy.example.com`.
   >
   > * `-Dhttp.proxyPort`
   >
   >   Port number of the proxy server. For example, `8080`.
   >
   > * `-Dhttp.nonProxyHosts`
   >
   >   A pipe-separated (`|`) list of IP addresses or hostnames that should be reached directly, bypassing the proxy configuration. For example, `localhost|internal.example.com`.
   >
   >   Use wildcards (`*`) at the beginning or the end of the address or hostname. For example, `*.example.com` or `internal*`.

   For example, set the properties in the `JAVA_OPTS` variable of the `$CATALINA_BASE/bin/setenv.sh` Apache Tomcat file.

2. Check whether your proxy requires authentication:

   1. If the proxy requires authentication:

      * In the `org.forgerock.openam.httpclienthandler.system.proxy.uri` advanced server property, configure the URI of the proxy.

        The URI must be in the format `scheme://hostname:port`.

        For example, `https://myproxy.example.com:443`.

      * Set the `org.forgerock.openam.httpclienthandler.system.proxy.username` advanced property.

      * Store the proxy password in a [secret store](secret-stores.html), instead of in the configuration. Use the secret label `am.servers.httpclienthandler.proxy.secret` to map an alias for the password.

        If AM finds a matching secret for the `am.servers.httpclienthandler.proxy.secret` label in a secret store, AM ignores the `org.forgerock.openam.httpclienthandler.system.proxy.password` advanced server property.

      * In the `org.forgerock.openam.httpclienthandler.system.nonProxyHosts` advanced server property, provide one or more target hosts for which resulting HTTP client requests should *not* be proxied.

        The list must be comma-separated, for example `[localhost,127.*,*.example.com]`.

   2. If the proxy does not require authentication:

      * Set the `org.forgerock.openam.httpclienthandler.system.proxy.enabled` advanced server property to `true`.

        This lets features using the HTTPClientHandler access the JVM proxy settings.

Learn more in [Advanced properties](../setup/server-advanced.html).

> **Collapse: How do I configure advanced server properties?**
>
> * To configure advanced server properties for all the instances of the AM environment, in the AM admin UI, go to Configure > Server Defaults > Advanced.
>
> * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
>
> * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
>
> If the property you want to add or edit is already configured, click on the pencil ([icon: pencil-alt, set=fa]) button to edit it. When you are finished, click on the tick ([icon: check, set=fa]) button.
>
> Click Save Changes.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can tune the connection factory behavior of the features that use the [HttpClientHandler](../_attachments/apidocs/org/forgerock/http/handler/HttpClientHandler.html). For example, the scripting engine, or the social provider authentication nodes.> **Collapse: Client connection handler properties**
>
> The following advanced server properties control aspects of the connection factory:
>
> * `org.forgerock.openam.httpclienthandler.system.clients.connection.timeout`
>
> * `org.forgerock.openam.httpclienthandler.system.clients.max.connections`
>
> * `org.forgerock.openam.httpclienthandler.system.clients.pool.ttl`
>
> * `org.forgerock.openam.httpclienthandler.system.clients.response.timeout`
>
> * `org.forgerock.openam.httpclienthandler.system.clients.retry.failed.requests.enabled`
>
> * `org.forgerock.openam.httpclienthandler.system.clients.reuse.connections.enabled`
>
> They have sensible defaults configured. If you need to change them, read [Advanced properties](../setup/server-advanced.html). |

## Configure the Base URL source service

In many deployments, AM determines the base URL of a provider using the incoming HTTP request. However, there are often cases when the base URL of a provider cannot be determined from the incoming request alone, especially if the provider is behind a proxying application. For example, if an AM instance is part of a site where the external connection is over SSL but the request to the AM instance is over plain HTTP, AM will have difficulty reconstructing the base URL of the provider.

In these cases, AM supports a provider service that lets you configure a realm to obtain the base URL, including the protocol, for components that need to return a URL to the client.

1. In the AM admin UI, go to Realms > *realm name* > Services, and click Add a Service.

2. Click Base URL Source, and click Create. Leave the fields empty.

3. For Base URL Source, choose one of the following options:

   **Base URL source options**

   | Option                                        | Description                                                                                                                                                                                                                      |
   | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Extension class                               | Click the Extension class to return a base URL from a provided `HttpServletRequest` object. In the Extension class name field, enter org.forgerock.openam.services.baseurl.BaseURLProvider.                                      |
   | Fixed value                                   | Click Fixed value to enter a specific base URL value. In the Fixed value base URL field, enter the base URL.                                                                                                                     |
   | Forwarded header                              | Click Forwarded header to retrieve the base URL from the Forwarded header field in the HTTP request. The Forwarded HTTP header field is standardized and specified in [RFC 7239](https://datatracker.ietf.org/doc/html/rfc7239). |
   | Host/protocol from incoming request (default) | Click Host/protocol from incoming request to get the hostname, server name, and port from the HTTP request.                                                                                                                      |
   | X-Forwarded-\* headers                        | Click X-Forwarded-\* headers to use non-standard header fields, such as `X-Forwarded-For`, `X-Forwarded-By`, and `X-Forwarded-Proto`.                                                                                            |

4. In the Context path, enter the context path for the base URL.

   If provided, the base URL includes the deployment context path appended to the calculated URL. For example, `/am`.

5. Click Finish to save your configuration.

---

---
title: Configure CORS support
description: Configure cross-origin resource sharing (CORS) in PingAM to allow requests across domains, set accepted origins, HTTP methods, and headers
component: pingam
version: 8.1
page_id: pingam:security:enable-cors-support
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/enable-cors-support.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration", "Features"]
page_aliases: ["security-guide:enable-cors-support.adoc"]
section_ids:
  cors-ui: Configure CORS in the UI
  cors-ui-enable: Enable the CORS filter
  add-cors-config-ui: Add a CORS configuration
  delete-cors-config-ui: Delete a CORS configuration
  cors-rest: Configure CORS over REST
  add-cors-config: Add a CORS configuration
  delete-cors-config: Delete a CORS configuration
---

# Configure CORS support

Cross-origin resource sharing (CORS) allows requests to be made across domains from user agents.

To configure CORS support in AM, use the global CORS service UI, or use the `/global-config/services/CorsService` REST endpoint.

The configurations you create with either method are combined to form the entire set of rules for resource sharing. The CORS service also collects the values of the [JavaScript Origins](../am-oauth2/oauth2-register-client.html#javascript-origins) property in each OAuth 2.0 client configured, and adds them to the list of accepted origins.

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ensure that customers allowlist *all* headers for CORS and OAuth 2.0 client integration with AM.Learn more in [Journey session allowlisting](auth-session-whitelist.html). |

Any changes you make to CORS configurations, using either the UI or REST, take effect immediately without requiring a restart.

|   |                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In previous AM releases, you configured CORS filters in the deployment descriptor file (`web.xml`). This method of configuring CORS is not supported, from AM version 7 onwards. |

## Configure CORS in the UI

You can use the UI to add multiple CORS configurations to AM, which are combined and used to ensure that only your trusted clients and applications can access your AM instance's resources.

For example, you could use the REST endpoint to add a base configuration, allowing a broad set of headers, and then add a stricter configuration; for example, for your OAuth 2.0 clients.

### Enable the CORS filter

To enable CORS globally, go to Configure > Global Services > CORS Service > Configuration, and enable the Enable the CORS filter property.

If this property is not enabled, no CORS headers are added to any responses from AM, and CORS is disabled.

### Add a CORS configuration

To add a CORS configuration, go to Configure > Global Services > CORS Service > Secondary Configurations, and click Add a Secondary Configuration.

The initial page contains the following properties:

* Name

  Provide a descriptive name for the configuration to make management of multiple rules easier.

* Accepted Origins

  Add the *origins* allowed when making CORS requests to AM. Wildcards are not supported; each value should be an exact match for the origin of the CORS request.

  The CORS service automatically collects the values of the JavaScript Origins property in each OAuth 2.0 client configured, and adds them to an internal list of accepted origins. You do not need to add them manually, unless you plan to use non-standard headers. Refer to [JavaScript Origins](../am-oauth2/oauth2-register-client.html#javascript-origins) for details.

  |   |                                                                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | During development, you may not be using FQDNs as the origin of a CORS request; for example, when you are using the `file://` protocol locally.If so, you can add these non-FQDN origins to the list; for example, `file://` and `null`. |

* Accepted Methods

  Add the HTTP methods allowed when making CORS requests to AM. The list is included in pre-flight responses, in the `Access-Control-Allow-Methods` header.

  The method names are case-sensitive, ensure they are entered in all uppercase characters.

* Accepted Headers

  Add the request header names allowed when making CORS requests to AM. The list is included in pre-flight responses, in the `Access-Control-Allow-Headers` header.

  The header names are case-insensitive.

  By default, the following simple headers are explicitly accepted:

  * `Cache-Control`

  * `Content-Language`

  * `Expires`

  * `Last-Modified`

  * `Pragma`

  If you do not specify values for this element, the presence of any header in the CORS request, other than the simple headers listed above, will cause the request to be rejected.

> **Collapse: What are the commonly used headers?**
>
> Headers commonly used when accessing an AM server include the following:
>
> **Commonly used headers**
>
> | Header                                  | Information                                                                                                                                                                                          |
> | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `iPlanetDirectoryPro`                   | Used for [session information](../am-sessions/about-sessions.html).                                                                                                                                  |
> | `X-OpenAM-Username` `X-OpenAM-Password` | Used to pass credentials in [REST calls](../am-authentication/authn-rest.html) that use the HTTP POST method.                                                                                        |
> | `Accept-API-Version`                    | Used to request a specific AM [endpoint version](../am-rest/rest-api-versioning.html).                                                                                                               |
> | `Content-Type`                          | Required for cross-origin calls to AM REST API endpoints.                                                                                                                                            |
> | `If-Match` `If-None-Match`              | Used to ensure the correct version of a resource will be affected when making a REST call, for example when [updating an UMA resource](../uma/uma-resource-sets.html#to-update-an-uma-resource-set). |

* Exposed Headers

  Add the response header names that AM returns in the `Access-Control-Expose-Headers` header.

  The header names are case-insensitive.

  User agents can make use of any headers that are listed in this property, as well as the simple response headers, which are as follows:

  * `Cache-Control`

  * `Content-Language`

  * `Expires`

  * `Last-Modified`

  * `Pragma`

  * `Content-Type`

  User agents must filter out all other response headers.

Example:

![Example of a CORS configuration in the UI.](_images/cors-ui-initial.png)

After you have completed the initial form fields, click Create.

The main CORS configuration page has the following additional properties:

* Enable the CORS filter

  Specifies whether the values specified in this CORS configuration instance will be active.

* Max Age

  The maximum length of time, in seconds, that the browser is allowed to cache the pre-flight response. The value is included in pre-flight responses, in the `Access-Control-Max-Age` header.

* Allow Credentials

  Whether to allow requests with credentials in either HTTP cookies or HTTP authentication information.

  Enable this property if you send `Authorization` headers as part of the CORS requests, or need to include information in cookies when making requests.

  When enabled, AM sets the `Access-Control-Allow-Credentials: true` header.

### Delete a CORS configuration

To delete a CORS configuration, go to Configure > Global Services > CORS Service > Secondary Configurations. Then, find the configuration to delete and click its Delete button.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can disable a CORS configuration, and enable it again later, by choosing the rule and toggling the Enable the CORS filter property. |

## Configure CORS over REST

You can use the endpoint to add multiple CORS configurations to AM, which are combined and used to ensure that only your trusted clients and applications can access your AM instance's resources.

For example, you could use the REST endpoint to add a base configuration, allowing a broad set of headers, and then add a stricter configuration; for example, for your OAuth 2.0 clients.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For information about the `/global-config/services/CorsService` endpoint, refer to the [API Explorer](../am-rest/about-api-explorer.html) available in the AM admin UI. |

These examples demonstrate managing a CORS configuration by using REST:

### Add a CORS configuration

To *add* a new CORS configuration, send an HTTP POST request, with the `create` action to the `/global-config/services/CorsService/configuration` endpoint.

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You will require the SSO token of an administrative user; for example, `amAdmin`.For information on obtaining an SSO token over REST, refer to [Authenticate over REST](../am-authentication/authn-rest.html). |

The payload of the request must contain the CORS configuration:

* `enabled`

  Specifies whether the values specified in the CORS configuration instance will be active (`true`), or not (`false`).

  |   |                                                               |
  | - | ------------------------------------------------------------- |
  |   | At least one instance must be enabled for AM to enforce CORS. |

* `acceptedOrigins`

  A comma-separated list of the *origins* allowed when making CORS requests to AM. Wildcards are not supported; each value should be an exact match for the origin of the CORS request.

  Example:

  ```json
  {
      "acceptedOrigins": [
          "http://example.com",
          "https://example.org:8433"
      ]
  }
  ```

  The CORS service automatically collects the values of the JavaScript Origins property in each OAuth 2.0 client configured, and adds them to an internal list of accepted origins. You do not need to add them manually, unless you plan to use non-standard headers. Refer to [JavaScript Origins](../am-oauth2/oauth2-register-client.html#javascript-origins) for details.

  |   |                                                                                                                                                                                                                                                                                                     |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | During development, you may not be using fully qualified domain names as the origin of a CORS request; for example, you are using the `file://` protocol locally.If so, you can add these non-FQDN origins to the list; for example, `http://example.com, https://example.org:8433, file://, null`. |

* `acceptedMethods`

  A list of HTTP methods allowed when making CORS requests to AM. The list is included in pre-flight responses, in the `Access-Control-Allow-Methods` header.

  The method names are case-sensitive, ensure they are entered in all uppercase characters.

  Example:

  ```json
  {
      "acceptedMethods": [
          "GET",
          "POST",
          "PUT",
          "PATCH",
          "OPTIONS",
          "DELETE"
      ]
  }
  ```

* `acceptedHeaders`

  A list of request header names allowed when making CORS requests to AM. The list is included in pre-flight responses, in the `Access-Control-Allow-Headers` header.

  The header names are case-insensitive.

  Example:

  ```json
  {
      "acceptedHeaders": [
          "iPlanetDirectoryPro",
          "X-OpenAM-Username",
          "X-OpenAM-Password",
          "Accept-API-Version",
          "Content-Type",
          "If-Match",
          "If-None-Match"
      ]
  }
  ```

  By default, the following simple headers are explicitly accepted:

  * `Cache-Control`

  * `Content-Language`

  * `Expires`

  * `Last-Modified`

  * `Pragma`

  If you do not specify values for this element, the presence of any header in the CORS request, other than the simple headers listed above, will cause the request to be rejected.

> **Collapse: What are the commonly used headers?**
>
> Headers commonly used when accessing an AM server include the following:
>
> **Commonly used headers**
>
> | Header                                  | Information                                                                                                                                                                                                         |
> | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `iPlanetDirectoryPro`                   | Used for [session information](../am-sessions/about-sessions.html).                                                                                                                                                 |
> | `X-OpenAM-Username` `X-OpenAM-Password` | Used to pass credentials in [REST calls](../am-authentication/authn-rest.html) that use the HTTP POST method.                                                                                                       |
> | `Accept-API-Version`                    | Used to request a specific [endpoint version](../am-rest/rest-api-versioning.html).                                                                                                                                 |
> | `Content-Type`                          | Required for cross-origin calls to AM REST API endpoints.                                                                                                                                                           |
> | `If-Match` `If-None-Match`              | Used to ensure the correct version of a resource will be affected when making a REST call.For an example, refer to [Update an UMA resource over REST](../uma/uma-resource-sets.html#to-update-an-uma-resource-set). |

* `exposedHeaders`

  A list of response header names that AM returns in the `Access-Control-Expose-Headers` header.

  The header names are case-insensitive.

  User agents can make use of any headers that are listed in this property, as well as the simple response headers, which are as follows:

  * `Cache-Control`

  * `Content-Language`

  * `Expires`

  * `Last-Modified`

  * `Pragma`

  * `Content-Type`

    User agents must filter out all other response headers.

    Example:

    ```json
    {
        "exposedHeaders": [
            "Access-Control-Allow-Origin",
            "Access-Control-Allow-Credentials",
            "Set-Cookie"
        ]
    }
    ```

* `maxAge`

  The maximum length of time, in seconds, that the browser is allowed to cache the pre-flight response. The value is included in pre-flight responses, in the `Access-Control-Max-Age` header.

* `allowCredentials`

  Whether to allow requests with credentials in either HTTP cookies or HTTP authentication information.

  Set to `true` if you send `Authorization` headers as part of the CORS requests, or need to include information in cookies when making requests.

  When enabled, AM sets the `Access-Control-Allow-Credentials: true` header.

The following shows an example of configuring CORS rules by using the `/global-config/services/CorsService` endpoint:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "X-Requested-With: XMLHttpRequest" \
--header 'Accept-API-Version: protocol=1.0,resource=1.0' \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
--data '{
    "enabled": true,
    "acceptedOrigins": [
        "http://localhost:8000",
        "null",
        "file://",
        "https://example.org:8443"
    ],
    "acceptedMethods": [
        "POST",
        "PUT",
        "OPTIONS"
    ],
    "acceptedHeaders": [
        "iPlanetDirectoryPro",
        "X-OpenAM-Username",
        "X-OpenAM-Password",
        "X-OpenIDM-Username",
        "X-OpenIDM-Password",
        "X-OpenIDM-NoSession",
        "Accept",
        "Accept-API-Version",
        "Authorization",
        "Cache-Control",
        "Content-Type",
        "If-Match",
        "If-None-Match",
        "X-Requested-With"
    ],
    "exposedHeaders": [
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Credentials",
        "WWW-Authenticate",
        "Set-Cookie"
    ],
    "maxAge": 1800,
    "allowCredentials": true
}' \
https://am.example.com:8443/am/json/global-config/services/CorsService/configuration?_action=create
{
    "_id": "ef61e99c-6c83-4044-a1f5-71f472531b71",
    "_rev": "-1255664842",
    "maxAge": 1800,
    "exposedHeaders": [
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Credentials",
        "WWW-Authenticate",
        "Set-Cookie"
    ],
    "acceptedOrigins": [
        "null",
        "file://",
        "https://example.org:8443",
        "http://localhost:8000"
    ],
    "acceptedMethods": [
        "POST",
        "OPTIONS",
        "PUT"
    ],
    "acceptedHeaders": [
        "iPlanetDirectoryPro",
        "X-OpenAM-Username",
        "X-OpenAM-Password",
        "X-OpenIDM-Username",
        "X-OpenIDM-Password",
        "X-OpenIDM-NoSession",
        "Accept",
        "Accept-API-Version",
        "Authorization",
        "Cache-Control",
        "Content-Type",
        "If-Match",
        "If-None-Match",
        "X-Requested-With"
    ],
    "enabled": true,
    "allowCredentials": true,
    "_type": {
        "_id": "CORSService",
        "name": "CORS Service",
        "collection": true
    }
}
```

On success, AM returns an HTTP 201 response code, and a representation of the CORS settings, in JSON format. AM generates a UUID for the configuration, returned as the value of the `_id` property. You can use this ID value to update or delete the configuration with additional REST calls.

The new settings take effect immediately.

### Delete a CORS configuration

To delete a CORS configuration, create an HTTP DELETE request to the `/global-config/services/CorsService` REST endpoint.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You will need the SSO token of an administrative user; for example, `amAdmin`.For information on obtaining an SSO token by using REST, refer to [Authenticate over REST](../am-authentication/authn-rest.html). |

Add the ID of the configuration to delete to the URL.

The following shows an example of deleting CORS rules by using the `/global-config/services/CorsService` endpoint:

```bash
$ curl \
--request DELETE \
--header "X-Requested-With: XMLHttpRequest" \
--header "iPlanetDirectoryPro: AQIC5w…​2NzEz*" \
https://am.example.com:8443/am/json/global-config/services/CorsService/ef61e99c-6c83-4044-a1f5-71f472531b71
{
    "_id": "ef61e99c-6c83-4044-a1f5-71f472531b71",
    "_rev": "-1255664842",
    "maxAge": 1800,
    "exposedHeaders": [
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Credentials",
        "WWW-Authenticate",
        "Set-Cookie"
    ],
    "acceptedOrigins": [
        "null",
        "file://",
        "https://example.org:8443",
        "http://localhost:8000"
    ],
    "acceptedMethods": [
        "POST",
        "OPTIONS",
        "PUT"
    ],
    "acceptedHeaders": [
        "iPlanetDirectoryPro",
        "X-OpenAM-Username",
        "X-OpenAM-Password",
        "X-OpenIDM-Username",
        "X-OpenIDM-Password",
        "X-OpenIDM-NoSession",
        "Accept",
        "Accept-API-Version",
        "Authorization",
        "Cache-Control",
        "Content-Type",
        "If-Match",
        "If-None-Match",
        "X-Requested-With"
    ],
    "enabled": true,
    "allowCredentials": true,
    "_type": {
        "_id": "CORSService",
        "name": "CORS Service",
        "collection": true
    }
}
```

On success, AM returns an HTTP 200 response code, and a representation of the CORS settings that were deleted, in JSON format.

The changes to the CORS settings take effect immediately.

---

---
title: Control the size of compressed JWTs
description: Control the maximum size of decompressed JWTs that PingAM accepts to prevent out-of-memory errors and security issues
component: pingam
version: 8.1
page_id: pingam:security:control-maximum-size-decompressed-JWT
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/control-maximum-size-decompressed-JWT.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "OAuth 2.0", "OpenID Connect (OIDC)", "Setup &amp; Configuration"]
page_aliases: ["security-guide:control-maximum-size-decompressed-JWT.adoc"]
---

# Control the size of compressed JWTs

A number of AM features accept JWTs to receive information. Some examples are:

* [Remote consent](../am-oauth2/oauth2-remote-consent.html), when it receives consent responses.

* The OAuth 2.0/OpenID Connect authorization service, when:

  * OpenID Connect clients send [request](../am-oauth2/oauth2-client-endpoints.html#the-request-parameter) parameters as a JWT instead of as HTTP parameters.

  * OpenID Connect clients register dynamically using [software statements](../am-oidc1/oauth2-dynamic-client-registration.html).

* The Authentication service, when configured to issue [client-side sessions](../am-sessions/impl-client-based-sessions.html).

The JWTs that AM receives can be signed and/or encrypted. Sometimes, larger JWTs are compressed to improve delivery speeds to AM.

Decompressing a JWT makes it expand in size. By default, AM rejects any JWT that expands to more than 32 KiB (32768 bytes), and throws an exception with a message similar to `JWT payload decompressed to larger than maximum allowed size`.

Ensure that the JWTs your clients send to AM are smaller than 32 KiB before compression.

Alternatively, increase the 32 KiB value to a reasonable limit. Take into account that AM performs decryption and decompression operations in its heap, and that you do not want to allow very large JWTs to, potentially, leave AM out of memory.

If you need to change the default value, perform the following steps:

1. Configure the `org.forgerock.json.jose.jwe.compression.max.decompressed.size.bytes` Java system property on the container where AM runs.

   For example, edit the `setenv.sh` file of the Apache Tomcat instance, and set the property with the new size in bytes:

   ```bash
   JAVA_OPTS="$JAVA_OPTS -Dorg.forgerock.json.jose.jwe.compression.max.decompressed.size.bytes=40960"
   ```

2. Restart the container for the changes to make effect.

---

---
title: Customize session quota exhaustion actions
description: AM provides built-in session quota exhaustion actions that you can configure for your deployment. If none of the built-in actions address your use case, you can build a custom session quota exhaustion action plugin. The plugin is a Java class that implements the QuotaExhaustionAction interface and is dynamically loaded by AM using the ServiceLoader mechanism.
component: pingam
version: 8.1
page_id: pingam:security:custom-quota-exhaustion-action
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/custom-quota-exhaustion-action.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Sessions", "Setup &amp; Configuration"]
page_aliases: ["security-guide:custom-quota-exhaustion-action.adoc"]
section_ids:
  sample-plugin: Sample plugin
  build_the_sample_plugin: Build the sample plugin
  try_the_sample_session_quota_exhaustion_action: Try the sample session quota exhaustion action
---

# Customize session quota exhaustion actions

AM provides built-in [session quota exhaustion actions](session-quotas.html) that you can configure for your deployment. If none of the built-in actions address your use case, you can build a custom session quota exhaustion action plugin. The plugin is a Java class that implements the `QuotaExhaustionAction` interface and is dynamically loaded by AM using the [ServiceLoader](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/ServiceLoader.html) mechanism.

Only build a custom session quota exhaustion action plugin if the built-in actions aren't flexible enough for your deployment.

|   |                                                           |
| - | --------------------------------------------------------- |
|   | Session quotas aren't available for client-side sessions. |

This page demonstrates a custom session quota exhaustion action plugin.

## Sample plugin

The sample plugin demonstrates a simple session quota exhaustion action that removes the first session it finds when the session quota is met.

Learn about downloading and building PingAM sample source code in the following *Knowledge Base* article: [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM).

Get a local clone so that you can try the sample on your system. You'll find the relevant files in the `/path/to/openam-samples/openam-examples-quotaexhaustionaction` directory.

> **Collapse: Files in the sample**
>
> * `pom.xml`
>
>   Apache Maven project file for the module.
>
>   This file specifies how to build the sample plugin, and also specifies its dependencies on AM components and on the Servlet API.
>
> * `src/main/java/org/forgerock/openam/examples/quotaexhaustionaction/SampleQuotaExhaustionAction.java`
>
>   Core class for the sample quota exhaustion action plugin.
>
>   This file:
>
>   * Implements the `QuotaExhaustionAction` interface.
>
>   * Annotates the implementation class with `@I18nKey("customActionI18nKey")`.
>
>   * Overrides the `action` method to perform the action when the session quota is met.
>
> * `src/main/resources/META-INF/services/com.iplanet.dpro.session.service.QuotaExhaustionAction`
>
>   Service provider configuration file.
>
>   This file is used by the `ServiceLoader` mechanism to load the plugin class. It contains the fully qualified name of the plugin class, which is `org.forgerock.openam.examples.quotaexhaustionaction.SampleQuotaExhaustionAction` in the sample.

## Build the sample plugin

1. If you haven't already done so, download and build the sample code.

   Learn about downloading and building PingAM sample source code in the following *Knowledge Base* article: [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM).

2. When the build completes, copy the `quotaexhaustionaction-8.1.1.jar` file to the `WEB-INF/lib` directory where you deployed AM:

   ```bash
   $ cp target/quotaexhaustionaction-8.1.1.jar /path/to/tomcat/webapps/am/WEB-INF/lib/
   ```

3. Extract `amSession.properties` (and, if necessary, the localized versions of this file) from `openam-core-8.1.1.jar` to `WEB-INF/classes/` where AM is deployed. For example, if AM is deployed under `/path/to/tomcat/webapps/am`:

   ```bash
   $ cd /path/to/tomcat/webapps/am/WEB-INF/classes/
   $ jar -xvf ../lib/openam-core-8.1.1.jar amSession.properties
   inflated: amSession.properties
   ```

4. Add the following line to `amSession.properties`:

   ```properties
   customActionI18nKey=Randomly Destroy Session
   ```

5. Restart AM or the container in which it runs to load the plugin.

## Try the sample session quota exhaustion action

1. In the AM admin UI, go to Configure > Global Services, click Session, and select the Session Quotas tab.

2. Select the custom session quota exhaustion action (`Randomly Destroy Session`) from the Resulting behavior if session quota exhausted list, and click Save Changes.

   If you don't provide a value for the `customActionI18nKey` in `amSession.properties`, the plugin class name is used instead.

3. Open multiple browser windows and log in with the same user until you exceed the session quota.

4. Observe that one of the sessions is removed when the session quota is met.

---

---
title: Default ports used by AM
description: Reference of default network ports used by PingAM, including JMX, RADIUS, administration connector, web container, and monitoring ports
component: pingam
version: 8.1
page_id: pingam:security:am-ports-used
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/am-ports-used.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Monitoring", "Ports"]
page_aliases: ["reference:am-ports-used.adoc", "security-guide:am-ports-used.adoc"]
---

# Default ports used by AM

The software uses a number of ports by default:

**Default ports used**

| Port number | Protocol | Description                                                            |
| ----------- | -------- | ---------------------------------------------------------------------- |
| 1689        | TCP/IP   | Port for Java Management extension (JMX) traffic, disabled by default. |
| 1812        | UDP      | Port for AM's RADIUS server, disabled by default.                      |
| 4444        | TCP/IP   | Port for the embedded administration connector, enabled by default.    |
| 8080        | TCP/IP   | Web application container port number.                                 |
| 8082        | TCP/IP   | HTTP port for monitoring AM, disabled by default.                      |
| 9999        | TCP/IP   | RMI port for monitoring AM, disabled by default.                       |

Sometimes multiple services are configured on a single system with slightly different port numbers. For example, while the default port number for a servlet container, such as Tomcat, is 8080, a second instance of Tomcat might be configured with a port number of 18080. In all cases shown, communications proceed using the protocol shown in the table.

When you configure a firewall for AM, make sure to include open ports for any installed and related components, including web services (80, 443), servlet containers (8009, 8080, 8443), and external applications.

Additional ports may be used, depending on other components of your deployment. If you are using PingDS, see [Administrative access](https://docs.pingidentity.com/pingds/8.1/security-guide/os.html#os-admin) in the DS documentation, for the list of default ports used by DS.

---

---
title: FIPS 140–3 compliance
description: Configure the Bouncy Castle FIPS libraries with PingAM to achieve FIPS 140-3 compliance for government data security requirements
component: pingam
version: 8.1
page_id: pingam:security:fips
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/fips.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Bouncy Castle FIPS", "Keystores", "Cryptographic Keys", "Secrets", "JSON", "Configuration", "JVM"]
section_ids:
  download-bouncy-castle-libraries: Download the Bouncy Castle libraries
  enable-bouncy-castle-for-container: Enable the Bouncy Castle FIPS provider for your web container
  manage-bcfks-keystores: Use a Bouncy Castle keystore
  disable_bouncy_castle_fips_approved_mode: Disable Bouncy Castle FIPS-approved mode
  allow-rsa-key-multi-use: Allow RSA key multi-use
---

# FIPS 140–3 compliance

To achieve [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) compliance, configure the [Bouncy Castle FIPS libraries](https://www.bouncycastle.org/fips-java/) with AM. This enables the use of the Bouncy Castle FIPS keystore and security provider in FIPS-approved mode.

Bouncy Castle FIPS is useful when dealing with government data, where you must meet the FIPS 140-3 security requirement for regulatory compliance.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Bouncy Castle FIPS is less performant than other keystores. The destroyable keys can't be cached and must be read from the keystore with every use. |

## Download the Bouncy Castle libraries

Before you begin, download the following [Bouncy Castle FIPS library](https://www.bouncycastle.org/fips-java/):

`bc-fips-latestVersion.jar`

This is the Bouncy Castle FIPS security provider implementation.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity supports PingAM and its use of the Bouncy Castle libraries. Ping Identity doesn't support third-party libraries themselves. |

## Enable the Bouncy Castle FIPS provider for your web container

These example commands assume you're using Apache Tomcat. Adjust the examples for your web container.

1. Create a dedicated folder to house the Bouncy Castle library and copy the downloaded library to that folder. For example:

   ```bash
   $ mkdir /path/to/bcfips
   $ cp ~/Downloads/bc-fips-latestVersion.jar /path/to/bcfips
   ```

2. Create a custom `java.security` file by copying your default JVM security file to the `/path/to/bcfips` folder. For example:

   ```bash
   $  cp $JAVA_HOME/conf/security/java.security /path/to/bcfips
   ```

3. Add the Bouncy Castle FIPS security provider as the first provider in the custom `java.security` file:

   ```bash
   security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
   security.provider.2=SUN
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * The Bouncy Castle security provider must be number 1 in this file.

   * The Bouncy Castle provider requires the `SUN provider`, so leave this provider configured even if you remove other providers from the list.

   * You should only have these providers listed to make sure only FIPS-compliant algorithms are used. Including other providers in the list risks the use of a non-compliant algorithm. Learn more in the [Bouncy Castle FIPS Java API User Guide](https://downloads.bouncycastle.org/fips-java/docs/BC-FJA-UserGuide-2.0.0.pdf). |

4. Edit Tomcat's container startup script, for example `setenv.sh`, to set the FIPs-related JVM system properties and to let Tomcat locate the Bouncy Castle library:

   ```none
   export JAVA_OPTS="$JAVA_OPTS -Djava.security.properties==/path/to/bcfips/java.security"
   export JAVA_OPTS="$JAVA_OPTS -Dorg.bouncycastle.fips.approved_only=true"
   export CLASSPATH=$CLASSPATH:/path/to/bc-fips-[.var]_latestVersion_.jar
   ```

   |   |                                                                            |
   | - | -------------------------------------------------------------------------- |
   |   | The `==` shown for the `-Djava.security.properties` property is necessary. |

5. Restart Tomcat.

## Use a Bouncy Castle keystore

BCFKS (Bouncy Castle FIPS Keystore) is a type of Java keystore designed to work with the Bouncy Castle FIPS cryptographic provider. A BCFKS keystore lets you securely store cryptographic keys and certificates in a format that's FIPS 140-3-compliant.

To use the Java `keytool` command to manage BCFKS keystores you must do one of the following:

* Set your system `JAVA_HOME` environment variable to the BCFIPS path. This ensures that any `keytool` commands you run use the BCFIPS provider.

* Add the following parameters to `keytool` commands:

  ```bash
  -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
  -providerpath /path/to/bcfips/bc-fips-version.jar \
  ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | - Aliases in BCFKS keystores are case-sensitive.

- If you're migrating from other keystore types, you might encounter limitations when migrating *passwords* (as opposed to cryptographic keys) to BCFKS. This is because BCFKS keystores don't support storing secrets with the `RAW` algorithm.

  Before you migrate passwords from the old keystore, change the storage algorithm to one that doesn't enforce length restrictions during storage or retrieval of the key, for example, `HmacSHA512`. There are no length restrictions on *using* the key, just on *storing* the key. |

For example, this command creates an asymmetric key pair and self-signed certificate, with alias `newkey` in a new BCFKS keystore named `keystore.bcfks`:

```bash
$ cd /path/to/am/security/keystores/
$ keytool \
-genkeypair \
-providername BCFIPS \
-providerpath /path/to/bcfips/bc-fips-version.jar \
-providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
-alias newkey \
-keyalg RSA \
-keysize 2048 \
-keystore keystore.bcfks \
-validity 365 \
-storetype BCFKS \
-storepass password \
-keypass password \
-dname "CN=newkey"
```

To use a BCFKS keystore for any global or realm keystore, in the AM admin UI:

* Set the Keystore type to `BCFKS`.

* Set the Provider name to `BCFIPS`.

Also read [Use a Bouncy Castle keystore as the AM keystore](am-keystore.html#bouncy-castle-keystore-as-am-keytore).

## Disable Bouncy Castle FIPS-approved mode

To disable Bouncy Castle FIPS-compliant mode:

1. Edit your web container's startup script to remove or comment out the BCFKS-specific Java options. For example, in `setenv.sh`:

   ```none
   ## export JAVA_OPTS="$JAVA_OPTS -Djava.security.properties==/path/to/bcfips/java.security"
   ## export JAVA_OPTS="$JAVA_OPTS -Dorg.bouncycastle.fips.approved_only=true"
   ## export CLASSPATH=$CLASSPATH:/path/to/bc-fips-[.var]_latestVersion_.jar
   ```

2. Restart AM.

## Allow RSA key multi-use

By default, the Bouncy Castle FIPS module prevents an RSA modulus from being used for both encryption and signing operations. This is a security measure to avoid potential vulnerabilities.

However, specific scenarios might require an RSA key to be used for both purposes. To allow this, set the following JVM property in your web container's startup script:

```bash
export JAVA_OPTS="$JAVA_OPTS -Dorg.bouncycastle.rsa.allow_multi_use=true"
```

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Enabling this property relaxes a security control. Understand the implications before setting `org.bouncycastle.rsa.allow_multi_use=true`. Consult relevant security best practices and the [Bouncy Castle documentation](https://www.bouncycastle.org/fips-java/) for more information. |

---

---
title: General security considerations
description: Learn general security considerations for protecting PingAM deployments, including keeping systems patched, enabling certificate verification, limiting server access, and restricting Java class...
component: pingam
version: 8.1
page_id: pingam:security:general-security
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/general-security.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration", "Deployment"]
page_aliases: ["security-guide:general-security.adoc"]
section_ids:
  keep_up_to_date_on_patches: Keep up to date on patches
  keep_up_to_date_on_cryptographic_methods_and_algorithms: Keep up to date on cryptographic methods and algorithms
  enable_certificate_verification: Enable certificate verification
  turn_off_unnecessary_features: Turn off unnecessary features
  limit_access_to_the_servers_hosting_am: Limit access to the servers hosting AM
  enforce_security: Enforce security
  audit_access_and_changes: Audit access and changes
  restrict_access_to_java_classes_in_scripts: Restrict access to Java classes in scripts
  protect-secrets: Protect system passwords and secrets
---

# General security considerations

This list does not intend to show you best practices in network and system administration. Rather, it suggests a number of security mechanisms that you can expand upon.

## Keep up to date on patches

Security vulnerabilities are the reason why you should keep your operating systems, web and application servers, and any other application in your environment up to date. Knowledge of vulnerabilities spread fast across malicious users, who would not hesitate in trying to exploit them.

Ping Identity maintains a list of [security advisories](https://backstage.pingidentity.com/knowledge/advisories/feed/AWxfnseig-tyvndie93SE) you should follow. You should also follow similar lists from all your vendors.

## Keep up to date on cryptographic methods and algorithms

Different algorithms and methods are discovered and tested over time, and communities of experts decide which are the most secure for different uses. Do not use outdated algorithms such as RSA for generating your keys.

## Enable certificate verification

The Online Certificate Status Protocol (OCSP) lets AM determine the revocation status for digital certificates.

To enable OCSP verification, set the following server properties under Deployment > Servers > *server name* > Security > Online Certificate Status Protocol Check:

1. Click [icon: lock, set=fa]then turn on Check Enabled.

2. Click [icon: lock, set=fa]and enter the URL of the issuing certificate authority's OCSP server in the Responder URL field.

3. Save your changes.

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These settings enable certificate verification across the server. Individual services that rely on certificate verification (such as the WebAuthn Metadata Service) have finer grained settings that override the values set here. |

## Turn off unnecessary features

The more features you have turned on, the more features you need to secure, patch, and audit. If something is not being used, disable it or uninstall it.

## Limit access to the servers hosting AM

A large part of protecting your environment is making sure only authorized people can access your servers and applications through the appropriate network, using the appropriate ports, and presenting strong-enough credentials.

Ensure users connect through SSL / TLS to the systems and audit system access periodically.

Find a list of the default ports in [Default ports used by AM](am-ports-used.html).

## Enforce security

Don't expect your users to follow security practices on their own; enforce security when possible by requiring secure connections, password resets, and strong authentication methods.

Learn more in [Secure HTTP and LDAP connections](secure-connections.html) and [Secure authentication to datastores](secure-data-stores.html).

## Audit access and changes

Audit logs record all events that have happened. Some applications store them with their engine logs, some others use specific files or send the information to a different server for archiving. Operating systems have audit logs as well, to detect unauthorized login attempts and changes to the software.

AM has its own audit logging service that adheres to the log structure common across the Ping Advanced Identity Software.

Learn more in [Audit logging](../monitoring/audit-logging.html).

## Restrict access to Java classes in scripts

You can limit access to the Java classes invoked by scripts in the following ways:

* Create or migrate scripts to use the next-generation scripting engine.

  A next-generation script prevents direct access to Java classes by providing a set of predefined bindings instead.

* Configure the allowlists and denylists used by legacy scripts with great care.

  Only allowlist stable and secure Java classes that are necessary for the functionality of your scripts. Make sure you denylist any potentially unsafe Java classes.

Follow the recommendations described in [Scripting security considerations](../am-scripting/scripting-env.html#scripting-env-security).

Learn more about allowlisting and denylisting Java classes in the [scripting service configuration](../setup/services-configuration.html#javaclass-allowlist).

## Protect system passwords and secrets

Put secrets like passwords and symmetric keys in secret stores or files, or enter them interactively.

When you set file permissions correctly, the operating system grants access only to authorized accounts, such as the account to run a server process. Other accounts can't read the secret from a properly protected file.

Don't put secrets in commands, environment variables, or Java system properties. Example commands in the documentation favor ease of use for evaluation, often including passwords. When you harden services for deployment, don't sacrifice security for ease of use.

Including secrets in commands, environment variables, or Java system properties isn't secure:

* Operating system processes can access the full command to run another process. Those processes can read any secrets you set in the command to run a service, for example.

* Operating system processes can access the environment variables of a server process.

* Monitoring software, command-line tools, and support tools extract values of Java system properties and can share them with other systems.

---

---
title: HttpOnly session cookies
description: Configure PingAM session cookies with the HttpOnly flag to protect against cross-site scripting attacks and prevent client-side scripts from accessing session tokens
component: pingam
version: 8.1
page_id: pingam:security:sec-rest-httponly
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/sec-rest-httponly.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration"]
page_aliases: ["security-guide:sec-rest-httponly.adoc"]
section_ids:
  configure-httponly: Verify the httpOnly flag is enabled
---

# HttpOnly session cookies

To help protect against cross-site scripting (XSS) attacks, configure session cookies with the `HttpOnly` flag. When a cookie has this flag, browsers prevent client-side scripts from accessing it. This is an effective way to prevent attackers from stealing session information.

By default, AM enables the `HttpOnly` flag on its session cookies.

|   |                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When the `HttpOnly` flag is enabled, a successful call to the `/json/authenticate` endpoint returns a response with an empty `tokenId` field. This happens because the session token is sent in the `HttpOnly` cookie and is not available to the script to be included in the JSON payload.For example:```json
{
  "tokenId":"",
  "successUrl":"/am/console",
  "realm":"/alpha"
}
``` |

## Verify the `httpOnly` flag is enabled

The `httpOnly` flag is enabled by default. To verify that it's enabled, follow these steps:

1. In the AM admin UI, go to Configure > Server Defaults > Advanced.

2. Find the `com.sun.identity.cookie.httponly` advanced server property and make sure it's set to `true`.

3. If you change the value, save your changes and restart AM or the container where it runs.

4. If you have a site with multiple AM servers, verify this setting on each server.

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM also uses the `Secure` flag for cookies. When a request is made over HTTPS, AM adds the `Secure` flag to all cookies (except `amlbcookie`). This flag tells the browser to only send the cookie over an encrypted connection. |

---

---
title: Import PEM-formatted keys
description: Import PEM-formatted certificates, keys, and secrets into PingAM using supported secret stores
component: pingam
version: 8.1
page_id: pingam:security:using-pem-keys
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/using-pem-keys.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration"]
page_aliases: ["security-guide:using-pem-keys.adoc"]
---

# Import PEM-formatted keys

AM supports loading certificates, keys, and secrets in [PEM format](https://datatracker.ietf.org/doc/html/rfc7468) in the following secret stores:

* [The environment and system property secret store](secret-stores.html#property-secret-store)

* [File system secret volumes secret stores](secret-stores.html#file-system-secret-volumes)

* [Google GSM secret stores](secret-stores.html#google-GSM-secret-stores)

1. Create or obtain PEM-formatted secrets.

   > **Collapse: Supported PEM formats**
   >
   > **Standard PEM-formatted secrets**
   >
   > * Elliptic Curve and RSA private keys, in OpenSSL and PKCS#8 formats.
   >
   > * Elliptic Curve and RSA public keys, in OpenSSL and X.509 formats.
   >
   > **Non-standard PEM-formatted secrets**
   >
   > * AES and HMAC secrets.
   >
   > * UTF-8-encoded generic secrets, such as passwords and API keys.

   You may obtain standard PEM-formatted secrets from your CA authority, or you can create your own files using, for example, the `openssl` utility. Standard PEM-formatted private keys can also be password-encrypted using the `openssl` utility.

   To create non-standard PEM-formatted secrets, perform the following steps:

   * To create AES or HMAC secrets, create a string of random bytes to work as cryptographic material, and base64-encode it.

     For example:

     ```bash
     $ head -c32 /dev/urandom | base64 > myEncodedSecret.txt
     ```

   * To create generic secrets, base64-encode the secret or key.

     For example:

     ```
     $ base64 myDecodedSecret.txt > myEncodedSecret.txt
     ```

   * Open the file with the secret and wrap it in PEM labels, such as the following:

     * HMAC Secrets

     * AES Secrets

     * Generic Secrets

     ```none
     -----BEGIN HMAC SECRET KEY-----
     Base64-encoded cryptographic material
     -----END HMAC SECRET KEY-----
     ```

     ```none
     -----BEGIN AES SECRET KEY-----
     Base64-encoded cryptographic material
     -----END AES SECRET KEY-----
     ```

     ```none
     -----BEGIN GENERIC SECRET-----
     Base64-encoded secret
     -----END GENERIC SECRET-----
     ```

   * Encrypt the contents of the non-standard PEM-formatted file using the `https://am.example.com:8443/am/encode.jsp` page, and save it to a file.

     The encryption process will create a string that is not PEM-formatted: do not add the PEM labels again. When AM reads the secret from the secret store that you will configure in the following step, it will decrypt it automatically and use it as a PEM secret.

2. Save the secret in the relevant place:

   1. For file system secret volume stores, copy the file with the secret to the location defined as the source of the store.

      For information on the file name to use, see [Map files in file system secret volumes secret stores](secret-mapping.html#creating-mappings-FS).

   2. For the environment and system property secrets store, add the contents of the file to an environment variable, or Java system property.

      For information on the variable or property name to use, see [Environment and system property secret store](secret-stores.html#property-secret-store).

   3. For Google GSM secret stores, add the contents of the file to a GSM secret.

      For information on the secret name to use, see [Google GSM secret stores](secret-stores.html#google-GSM-secret-stores).

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can concatenate the contents of several related PEM-formatted files in a single GSM secret; for example, a private key and its associated certificate chain. AM will correctly extract the different components.> **Collapse: Example**
      >
      > Concatenate keys and multiple certificates in a PEM file in order, such that the following certificate directly certifies the one preceding it:
      >
      > ```
      > -----BEGIN RSA PRIVATE KEY-----
      > The Private Key: domain_name.key
      > -----END RSA PRIVATE KEY-----
      > -----BEGIN CERTIFICATE-----
      > The Primary SSL certificate: domain_name.crt
      > -----END CERTIFICATE-----
      > -----BEGIN CERTIFICATE-----
      > The Intermediate certificate: CA_cert.crt
      > -----END CERTIFICATE-----
      > -----BEGIN CERTIFICATE-----
      > The Root certificate: Root.crt
      > -----END CERTIFICATE-----
      > ``` |

3. If the standard PEM-formatted secret is password-encrypted, make the password available to AM as follows:

   * Encode the password using the `https://am.example.com:8443/am/encode.jsp` page.

   * Write the result to a file system secret, or environment variable, that maps to the `am.global.services.secret.pem.decryption` secret label:

     * File system secret

     * Environment variable

     ```bash
     $ echo -n AQICmX1ntZv3XETMgDo+0zFynC8UMGJgop+K > am.global.services.secret.pem.decryption
     ```

     ```bash
     $ export AM_GLOBAL_SERVICES_SECRET_PEM_DECRYPTION=AQICmX1ntZv3XETMgDo+0zFynC8UMGJgop+K
     ```

   * Make the password available to AM in either the environment and system property secrets store or a file system secret volumes secret store, depending on how you created the secret in the previous step.

     |   |                                                                                                                                                                                                                                                                                  |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | AM only checks global stores for the passwords used to decrypt PEM-formatted files. You can configure and use the PEM-formatted secret in any realm but the decryption password must be available in a global store.To configure global stores, go to Configure > Secret Stores. |

4. Configure AM to use the new PEM-formatted certificate or key.

   See [Map and rotate secrets](secret-mapping.html).

---

---
title: Journey session allowlisting
description: Enable journey session allowlisting to protect PingAM journey sessions from replay attacks by validating session tokens at each authentication node
component: pingam
version: 8.1
page_id: pingam:security:auth-session-whitelist
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/auth-session-whitelist.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Sessions", "Authentication", "Setup &amp; Configuration"]
page_aliases: ["security-guide:auth-session-whitelist.adoc"]
section_ids:
  proc-configure-auth-session-whitelisting: Configure journey session allowlisting
---

# Journey session allowlisting

Enable journey session allowlisting to protect journey sessions from replay attacks.

When journey session allowlisting is enabled, AM generates a key-value pair for each journey session and stores it for the length of the journey in the following ways:

* For client-side journey sessions, AM stores the key-value pair in the CTS token store.

* For server-side journey sessions, AM creates the key-value pair as a session property in the journey session.

* For in-memory journey sessions, AM creates the key-value pair as a session property in the journey session.

Each time the journey flow reaches an authentication node, AM modifies the value of the stored key-value pair and sends it to the user or client that it is progressing through the journey. The next request to AM to continue the journey must contain the key-value pair and must match the value expected by AM.

If the user or client can't provide the key-value pair with the values AM expects, AM doesn't continue the journey, therefore protecting the journey against malicious users wanting to rewind to a previous node.

Perform the following steps to configure journey session allowlisting:

## Configure journey session allowlisting

1. Go to Realms > *realm name* > Authentication > Settings > Trees.

2. Choose Enable Allowlisting.

3. Click Save.

---

---
title: Key aliases and passwords
description: Create and manage key aliases and passwords for PingAM keystores, including creating new key aliases, copying keys between keystores, and changing key and keystore passwords
component: pingam
version: 8.1
page_id: pingam:security:configuring-keys
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/configuring-keys.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration"]
page_aliases: ["security-guide:configuring-keys.adoc"]
section_ids:
  creating-new-keys: Create key aliases
  create-signing-keys-new-keystore: Create a keystore and key aliases for keystore-type secret stores
  create-signing-keys: Create key aliases in an existing keystore
  changing-uss-keys: Create self-service key aliases
  keys-copying: Copy key aliases between keystores
  changing-key-passwords: Change key alias passwords
  changing-keystore-password: Change keystore passwords
---

# Key aliases and passwords

You might need to create new key aliases because you are using additional AM features, or because you are installing a new environment. In either case, consider these points:

* First, review the list of AM features to understand which features use the AM keystore and which ones do not.

  For more information, see [AM features that use keys](features-with-keys.html).

* Avoid sharing certificates between features when possible, even if this means you need to configure multiple different keystores or secret stores.

* Make sure keystores, key aliases, and certificates are maintained on every instance; in a site environment, every instance has its own keystore files.

* Make sure keystores and secret stores are in the same location across all instances in the site.

The following table lists the tasks related to managing key aliases in your environment:

| Task                                                                                                                                                                                                                                                                                              | Resources                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Create a new key alias in an existing keystore or in a new keystore.	A suitable certificate must exist in the keystore before you map secrets to that keystore. If you change the default mapping before installing the required certificates, the features that require those secrets will fail. | [Create key aliases](#creating-new-keys)                 |
| Copy key aliases between keystores; for example, when configuring IDM's provisioning.                                                                                                                                                                                                             | [Copy key aliases between keystores](#keys-copying)      |
| Change key alias passwords.                                                                                                                                                                                                                                                                       | [Change key alias passwords](#changing-key-passwords)    |
| Change keystore passwords.                                                                                                                                                                                                                                                                        | [Change keystore passwords](#changing-keystore-password) |

## Create key aliases

Several AM features require key aliases for signing and encryption. AM provides default key aliases for all features, but you should create new key aliases in production.

You can create key aliases in a new keystore that will be configured later as the AM keystore, or you can create key aliases in the existing AM keystore:

* [Create a keystore and key aliases for keystore-type secret stores](#create-signing-keys-new-keystore)

* [Create key aliases in an existing keystore](#create-signing-keys)

* [Create self-service key aliases](#changing-uss-keys)

### Create a keystore and key aliases for keystore-type secret stores

These instructions are for keystore-type secret stores. To create a new AM keystore, see [The AM keystore](am-keystore.html) instead.

1. Obtain a new key from your certificate authority and add it to a new keystore, or generate a self-signed key in a new keystore.

   |   |                                                                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | A suitable certificate must exist in the keystore *before* you map secrets to that keystore. If you change the default mapping before installing the required certificates, the features that require those secrets will fail. |

   This example creates an asymmetric key pair and self-signed certificate, with alias `newkey` in a new keystore file named `keystoreA.jceks`. The RSA algorithm is used to generate the key pair.

   |   |                                                                             |
   | - | --------------------------------------------------------------------------- |
   |   | In production environments you should use the strongest possible algorithm. |

   ```bash
   $ cd /path/to/am/security/keystores/
   $ keytool \
   -genkeypair \
   -alias newkey \
   -keyalg RSA \
   -keysize 2048 \
   -validity 730 \
   -storetype JCEKS \
   -dname 'CN=newkey' \
   -keystore keystoreA.jceks
   Enter keystore password:
   Reenter new password:
   Enter key password for <newkey> (RETURN if same as keystore password):
   Reenter new password:
   ```

   Take note of the passwords. You need to make them available within another secret store; for example, by using a file system volume secret store, as shown below:

   * Go to the directory that the filesystem volume secret store will point to.

     For example, `/path/to/am/security/secrets/mydir`.

     You can use different methods to encode the content of the files. Consider creating a directory for each encoding method you plan to use.

   * Create two files, one for the keystore password, and another for the password of the keys inside the keystore.

     The files will contain the encoded passwords expected by the file system secret volume store.

     For example, if you chose `Base64 encoded` as the encoding, you must base64-encode the passwords, and then add them to their respective files.

     For example:

     ```bash
     $ echo -n bmV3c3RvcmVwYXNzd29yZA== > keystoreA_storepass
     $ echo -n bmV3a2V5cGFzc3dvcmQ= > keystoreA_keypass
     ```

     |   |                                                                                                                                                                                                         |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Use `echo -n` to avoid inserting hidden trailing newline characters. Even if the `keytool` command is able to use the password in the file, AM may not be able to open the keystore or the key aliases. |

   * Make sure the password files have read-only permission for their owner.

     For example:

     ```bash
     $ chmod 400 keystoreA_storepass
     $ chmod 400 keystoreA_keypass
     ```

2. Create any other keys and keystores required by your environment by repeating the steps in this procedure and/or following the steps in [Create key aliases in an existing keystore](#create-signing-keys).

3. Ensure that password files and keystores are maintained on every instance in your environment. Every AM instance has its own keystores and password files.

4. Configure the keystore in a keystore-type secret store.

   See [Keystore secret stores](secret-stores.html#keystores-secret-store).

   To configure the file system secret store too, see [File system secret volumes](secret-stores.html#file-system-secret-volumes).

### Create key aliases in an existing keystore

Perform the following steps to create new key aliases in an existing keystore. For example, the AM keystore:

1. Change directories to the keystore location, for example, `/path/to/am/security/keystores/`.

2. Acquire a new key from your certificate authority, or generate a new self-signed key.

   When you create or import a new key, the `keytool` command adds the new alias to the specified keystore if it exists, or creates a new keystore if it does not exist.

   This example creates a self-signed key alias in the AM keystore, `am_keystore.jceks`, with a new asymmetric RSA key alias called `mynewkey`.

   Note than in production environments you should use the strongest algorithm you can use.

   ```bash
   $ cd /path/to/am/security/keystores/
   $ keytool \
   -genkeypair \
   -alias mynewkey \
   -keyalg RSA \
   -keysize 2048 \
   -validity 730 \
   -storetype JCEKS \
   -dname 'CN=mynewkey' \
   -keystore am_keystore.jceks
   Enter keystore password: Enter the password in the .keystore_storepass file.
   Enter key password for <mynewkey> (RETURN if same as keystore password): Enter the password in the .keystore_keypass file.
   Reenter new password: Enter the password in the .keystore_keypass file.
   ```

   Remember:

   * The contents of the password files of the AM keystore are in cleartext.

   * The contents of the password files in a file system volume secret store are *not* in cleartext by default. This means that you need to decode them before you can use them in the `keytool` command.

3. Ensure that password files and keystores are maintained on every instance in your environment.

   Every AM instance has its own keystores and password files.

4. (AM keystore) Restart the AM instances affected by the configuration changes to use the new key aliases.

5. Configure the new key aliases in AM.

   For a list of features that use key aliases and links to their relevant sections, see [AM features that use keys](features-with-keys.html).

### Create self-service key aliases

User self-service requires a key pair for encryption and a signing secret key to be available in the AM keystore before configuring any of its features. Follow the steps in this procedure to create new key aliases for the user self-service features in the AM keystore:

1. Acquire a new key from your certificate authority, or generate new self-signed keys.

   The password of the new keys for the user self-service features must match the passwords of those keys already present in the keystore, and configured in the `/path/to/am/security/secrets/default/.am_keystore_keypass` file.

   This example generates a self-signed key for encryption and a new signing secret key in the `am_keystore.jceks` keystore, but you could also import CA-provided keys to the keystore.

   * Create the new self-signed encryption key alias:

     ```bash
     $ cd /path/to/am/security/keystores/
     $ keytool \
     -genkeypair \
     -alias newenckey \
     -keyalg RSA \
     -keysize 2048 \
     -validity 730 \
     -storetype JCEKS \
     -dname 'CN=newenckey' \
     -keystore am_keystore.jceks
     Enter keystore password: Enter the password in the .am_keystore_storepass file.
     Enter key password for <newenckey> (RETURN if same as keystore password): Enter the password in the .am_keystore_keypass file.
     Reenter new password: Enter the password in the .am_keystore_keypass file.
     ```

   * Create the new signing secret key alias:

     ```bash
     $ cd /path/to/am/security/keystores/
     $ keytool \
     -genseckey \
     -alias newsigkey \
     -keyalg HmacSHA256 \
     -keysize 256 \
     -storetype JCEKS \
     -keystore am_keystore.jceks
     Enter keystore password: Enter the password in the .am_keystore_storepass file.
     Enter key password for <newsigkey> (RETURN if same as keystore password): Enter the password in the .am_keystore_keypass file.
     Reenter new password: Enter the password in the .am_keystore_keypass file.
     ```

2. Ensure that password files and keystores are maintained on every instance in your environment.

   Every AM instance has its own keystores and password files.

3. Restart the AM instances affected by the configuration changes.

4. Configure user self-service to use the new keys.

   For instructions, see [Create a user self-service instance](../user-self-service/configuring-uss.html#create-uss-service).

## Copy key aliases between keystores

Some AM features require access to the key aliases used by other components of the Ping Advanced Identity Software. For example, the IDM Provisioning feature requires access to the key aliases that IDM uses to sign and encrypt data.

This section covers copying key aliases from the keystore of a Ping Advanced Identity Software component to AM's default keystore.

1. Use the `keytool` command to export the required key from the source keystore into a temporary keystore:

   ```bash
   $ keytool -importkeystore -srcstoretype jceks -srcalias "myKeyAlias" \
   -deststoretype jceks -destalias "myKeyAlias" \
   -srckeystore "/path/to/openidm/security/keystore.jceks" \
   -destkeystore "/path/to/openidm/security/temp_keystore.jceks" \
   -srckeypass "changeit" \
   -srcstorepass "changeit" \
   -destkeypass "myT3mPK3yP4ssword" \
   -deststorepass "myT3mPK3yP4ssword"
   ```

   This command exports the `myKeyAlias` key alias, specified by the `srcalias` argument, to a temporary keystore file `/path/to/openidm/security/temp_keystore.jceks`. The store and key password is set to `myT3mPK3yP4ssword`. You need to use the temporary passwords when importing to the AM instance.

2. Move the temporary keystore file created in the previous step, in this example `temp_keystore.jceks`, to the filesystem of the target AM server.

3. On the target AM server, import the key alias into the AM keystore:

   ```bash
   $ keytool -importkeystore -srcstoretype jceks -srcalias "myKeyAlias" \
   -deststoretype jceks -destalias "myKeyAlias" \
   -srckeystore "/path/to/am/security/keystores/temp_keystore.jceks" \
   -destkeystore "/path/to/am/security/keystores/am_keystore.jceks" \
   -srckeypass "myT3mPK3yP4ssword" \
   -srcstorepass "myT3mPK3yP4ssword" \
   -destkeypass:file "/path/to/am/security/secrets/default/.am_keystore_keypass" \
   -deststorepass:file "/path/to/am/security/secrets/default/.am_keystore_storepass"
   ```

   This command imports the key alias from the temporary `temp_keystore.jceks` keystore file, which was copied from the IDM instance, into the AM keystore. The command also sets the passwords to match those used by the default AM keystore.

4. Repeat the previous steps to copy any additional key aliases from the source keystore to the destination keystore.

5. Restart the AM instance for the key change to take effect.

   The AM instance will now be able to correctly encrypt, decrypt, sign or verify data and share it with the source Ping Advanced Identity Software component.

## Change key alias passwords

Decrypting a key alias in a keystore requires a password. This password is initially specified when you generate the key, or when you import the key into a keystore, but you might need to update the password at a later time.

1. Back up your keystore and password files.

2. Depending on the location of the key alias whose password you are changing, perform one of the following steps:

   1. To change the password that opens the **AM keystore**:

      Replace the old password in the `.am_keystore_keypass` file with the new one:

      ```bash
      $ echo -n newpassword > /path/to/am/security/secrets/default/.am_keystore_keypass
      ```

      |   |                                                                                                                                                                                                                                                        |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Use `echo -n` to avoid inserting hidden trailing newline characters. Even if the `keytool` command can use the password in the file, AM may not be able to use the key aliases if there are hidden, trailing, newline characters in the password file. |

   2. To change the password that opens a **secret store**:

      Replace the old password in the secret containing it with the new one. If the secret is a file in a file system volume secret store, ensure that the new password is encoded appropriately.

      For example, for base64-encoded passwords, use the following command:

      ```bash
      $ echo -n bmV3a2V5cGFzc3dvcmQ= > keystoreA_keypass
      ```

   3. To change a password value used to decrypt a **PEM-formatted secret**:

      Encode the new password using the https\://am.example.com:8443/am/encode.jsp page, and write the result to a file system secret or environment variable that uses the `am.global.services.secret.pem.decryption` secret label:

      * File system secret

      * Environment variable

      ```bash
      $ echo -n AQICmX1ntZv3XETMgDo+0zFynC8UMGJgop+K > am.global.services.secret.pem.decryption
      ```

      ```bash
      $ export AM_GLOBAL_SERVICES_SECRET_PEM_DECRYPTION=AQICmX1ntZv3XETMgDo+0zFynC8UMGJgop+K
      ```

3. Depending on the location of the secret, perform one of the following steps to update the secret's password to match the value you configured in the previous step:

   1. To change the password of key aliases in the **AM Keystore**:

      Use the `keytool` command to change the password of each of the key aliases, for example:

      ```bash
      $ keytool -keypasswd -storetype JCEKS -keystore /path/to/am/security/keystores/am_keystore.jceks -alias mykey
      Enter keystore password: Enter the password in the .am_keystore_storepass file
      New key password for <mykey> Enter the password in the .am_keystore_keypass file
      Re-enter new key password for <mykey> Enter the password in the .am_keystore_keypass file
      ```

      Remember to change the password of the `configstorepwd` alias. If you don't do this, you won't be able to start AM.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * You can use the `keytool` command to list the keys and password strings in the AM keystore. For example:

        ```bash
        $ keytool -list -storetype JCEKS -keystore /path/to/am/security/keystores/am_keystore.jceks
        ```

      * If you store the configuration store password in a [BCFKS keystore](fips.html#manage-bcfks-keystores), the alias appears as `configStorePwd` in the keystore. Aliases in BCFKS keystores are case-sensitive. |

   2. To change the password of key aliases in a **secret store**:

      Use the `keytool` command to change the password of each key alias, for example:

      ```bash
      $ keytool -keypasswd -storetype JCEKS -keystore /path/to/am/security/keystores/keystoreA.jceks -alias mykey
      Enter keystore password: Enter the password in the keystoreA_storepass file
      New key password for <mykey> Enter the password in the keystoreA_keypass file
      Re-enter new key password for <mykey> Enter the password in the keystoreA_keypass file
      ```

      Secrets in file system volume secret stores are, by default:

      ```bash
      $ `keytool -keypasswd -storetype JCEKS -keystore /path/to/am/security/keystores/keystoreA.jceks -alias mykey
      Enter keystore password: Enter the password in the keystoreA_storepass file
      New key password for <mykey> Enter the password in the keystoreA_keypass file
      Re-enter new key password for <mykey> Enter the password in the keystoreA_keypass file
      ```

      Secrets in file system volume secret stores are, by default, *not* in cleartext. You need to decode them before using them with the `keytool` command.

      |   |                                                                                                                                                                                                 |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can list the keys and password strings contained in a secret store using this command:```bash
      $ keytool -list -storetype JCEKS -keystore /path/to/am/security/keystores/keystoreA.jceks
      ``` |

   3. To change the password of a **PEM-formatted secret**:

      Use the `openssl` command to open, and then export the secret alias with a new password:

      ```bash
      $ openssl rsa -aes256 -in originalkey.pem -out new_password_key.pem
      Enter pass phrase for originalkey.pem: Enter the original password
      writing RSA key
      Enter PEM pass phrase: Enter the new password
      Verifying - Enter PEM pass phrase: Re-enter new password
      ```

      |   |                                                          |
      | - | -------------------------------------------------------- |
      |   | The algorithm you specify must match the input PEM file. |

      When completed, overwrite the original PEM file with the replacement, for example:

      ```bash
      $ mv new_password_key.pem originalkey.pem
      ```

4. If you also need to change the keystore password, see [Change keystore passwords](#changing-keystore-password).

5. Ensure that password files and keystores are maintained on every instance in your environment.

   Every AM instance has its own keystores and password files.

6. (AM keystore) Restart the AM instances affected by the configuration changes.

## Change keystore passwords

Decrypting and viewing the contents of a keystore requires a password. This password is specified by the user at the time the keystore is created, but you might need to update the password at a later time.

1. (AM keystore) Replace the old password in the `.am_keystore_storepass` file with the new one:

   ```bash
   $ echo -n newpassword > /path/to/am/security/secrets/default/.am_keystore_storepass
   ```

   |   |                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use `echo -n` to avoid inserting hidden trailing newline characters. Even if the `keytool` command is able to use the password in the file, AM may not be able to use the key aliases if there are hidden trailing newline characters in the password file. |

2. (Secret stores) Replace the old password in the secret containing it with the new one.

   If the secret is a file in a file system volume secret store, ensure that the new password is encoded appropriately.

   For example, base64-encode the password, and add it to the file:

   ```bash
   $ echo -n bmV3c3RvcmVwYXNzd29yZA== > keystoreA_storepass
   ```

3. Change the password of the keystore:

   * AM keystore

   * Secret stores

   ```bash
   $ keytool -storepasswd -storetype JCEKS -keystore /path/to/am/security/keystores/am_keystore.jceks
   Enter keystore password: Enter the password in the .am_keystore_storepass file.
   New keystore password: Enter the new password.
   Re-enter new keystore password:
   ```

   ```bash
   $ keytool -storepasswd -storetype JCEKS -keystore /path/to/am/security/keystores/keystoreA.jceks
   Enter keystore password: Enter the password in the keystoreA_storepass file.
   New keystore password: Enter the new password.
   Re-enter new keystore password:
   ```

   Secrets in file system volume secret stores are, by default, *not* in cleartext. You need to decode them before using them with the `keytool` command.

4. If you also need to change the key aliases' password, see [Change keystore passwords](#changing-keystore-password).

5. Ensure that password files and keystores are maintained on every instance in your environment.

   Each AM instance has its own keystores and password files.

6. (AM keystore only) Restart the AM instance or instances affected by the configuration changes.

---

---
title: Limit the size of the request body
description: Configure PingAM to reject HTTP requests exceeding the maximum allowed body size to prevent denial of service attacks
component: pingam
version: 8.1
page_id: pingam:security:limit-request-body-size
canonical_url: https://docs.pingidentity.com/pingam/8.1/security/limit-request-body-size.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration"]
page_aliases: ["security-guide:limit-request-body-size.adoc"]
---

# Limit the size of the request body

HTTP requests are not limited by the specification. Rather, the method used limits the amount of data that a client can send. The GET and DELETE methods, for example, are limited by the size of the URL. The POST method is not. Instead, browsers and application servers limit the amount of data a request can send to your applications.

Ensure that the amount of data that reaches your applications and AM is not large enough to overwhelm them.

Application servers usually can mitigate against denial of service (DoS) attacks that POST large amounts of form data, but AM endpoints may receive large amounts of POST data in different ways, such as in JSON, JWT, or JWK formats.

By default, AM rejects incoming requests with a body larger than 1 MB (1048576 bytes) in size. It also returns an HTTP 413 error response, and logs a message similar to the following:

* `ERROR: Request Content-Length exceeds maximum allowed`, if the content's length was specified in the request.

* `ERROR: Counted request entity size exceeds maximum allowed`, if the content's length was not specified.

To change the default value, perform the following steps:

1. Change the value of the `org.forgerock.openam.request.max.bytes.entity.size` advanced server property to the new size, in bytes.

   The property is hot-swappable. You do not need to restart AM for the changes to take effect.

> **Collapse: How do I configure advanced server properties?**
>
> * To configure advanced server properties for all instances of the AM environment, go to Configure > Server Defaults > Advanced in the AM admin UI.
>
> * To configure advanced server properties for a particular instance, go to Deployment > Servers > *server name* > Advanced.
>
> If the property you want to add or edit is already configured, click on the pencil ([icon: pencil-alt, set=fas]) button to edit it. When you are finished, click on the tick ([icon: check, set=fas]) button.
>
> Click Save Changes.
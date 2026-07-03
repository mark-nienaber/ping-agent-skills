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

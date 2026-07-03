---
title: Changing certificates from SHA-1 to SHA-2 in PingFederate
description: Use your Java Virtual Machine (JVM) to generate SHA-2 certificates and import them into PingFederate to replace default SHA-1 certificates for better security.
component: solution-guides
page_id: solution-guides:single_sign-on_use_cases:htg_change_certs_from_sha_1_to_sha_2_pf
canonical_url: https://docs.pingidentity.com/solution-guides/single_sign-on_use_cases/htg_change_certs_from_sha_1_to_sha_2_pf.html
revdate: February 16, 2022
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Changing certificates from SHA-1 to SHA-2 in PingFederate

Use your Java Virtual Machine (JVM) to generate SHA-2 certificates and import them into PingFederate to replace default SHA-1 certificates for better security.

## Before you begin

**Component**

* PingFederate earlier than version 8

Ensure that you have installed a JVM.

## About this task

PingFederate generates SHA-1 certificates by default prior to version 8. Use these instructions to create an SHA-2 certificate with `keytool` and import it into PingFederate.

## Steps

1. **If using JDK 1.9 or later, skip to step 4.** If using an earlier version, see <https://www.oracle.com/java/technologies/javase-jce-all-downloads.html>.

   |   |                                                                                           |
   | - | ----------------------------------------------------------------------------------------- |
   |   | Java versions 1.9 and later include the appropriate policy files and use them by default. |

2. Copy `local_policy.jar` and `US_export_policy.jar` to `$JAVA_HOME/jre/lib/security`. These .jar files already exist in the JCE, so you must overwrite them. If you have a cluster, do this for each node.

3. Restart PingFederate.

4. When signing keypairs, use `keytool` to generate a self-signed certificate in a `pkcs12` keystore instead of the default `.jks` type.

   ```
   keytool -genkeypair -alias sha256 -keyalg RSA -keysize 2048 -sigalg SHA256withRSA -keystore sha256.p12 -storepass 2Federate -storetype pkcs12
   ```

5. Import the `sha256.p12` file into the appropriate PingFederate keystore using the administration console. Replicate the configuration change to all nodes within a cluster by clicking **Cluster Management → Replicate Cluster Configuration**.

6. Export the public key certificate using either the administration console or the following command:

   ```
   keytool -exportcert -alias sha256 -keystore sha256.p12 -storepass 2Federate -storetype pkcs12 -file  cert_name.crt
   ```

7. To view the contents of the public key certificate, enter the following command:

   ```
   keytool -printcert -file  cert_name.crt
   ```

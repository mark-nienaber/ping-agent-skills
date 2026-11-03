---
title: About encrypting log files
description: "Encrypt log files as they're written."
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_encrypt_log_files
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_encrypt_log_files.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 1, 2025
section_ids:
  configuring-log-signing: Configuring log signing
  steps: Steps
  example: Example:
  example-2: Example:
  validating-a-signed-file: Validating a signed file
  steps-2: Steps
  example-3: Example:
  result: Result:
  configuring-log-file-encryption: Configuring log file encryption
  steps-3: Steps
  example-4: Example:
  example-5: Example:
  result-2: Result:
---

# About encrypting log files

The server lets you encrypt log files as they're written.

The `encrypt-log` configuration property controls whether encryption is enabled for the logger. Enabling encryption causes the log file to have an `.encrypted` extension. If both encryption and compression are enabled, the extension is `.gz.encrypted`. Any change that affects the name used for the log file could prevent older files from getting properly cleaned up.

Like compression, encryption can only be enabled when the logger is created. Encryption cannot be turned on or off after the logger is configured. For any log file that is encrypted, enabling compression is also recommended to reduce the amount of data that needs to be encrypted. This reduces the overall size of the log file. The `encrypt-file` tool or custom code, using the LDAP SDK's `com.unboundid.util.PassphraseEncryptedInputStream`, is used to access the encrypted data.

To enable encryption, at least one encryption settings definition must be defined in the server. Use the one created during setup, or create a new one with the `encryption-settings create` command. By default, the encryption is performed with the server's preferred encryption settings definition.

To explicitly specify which definition should be used for the encryption, set the `encryption-settings-definition-id` property with the ID of that definition. You should set the encryption settings definition to be created from a passphrase so that the file can be decrypted by providing that passphrase even if the original encryption settings definition is no longer available. You can also create a randomly generated encryption settings definition, but the log file can only be decrypted using a server instance that has that encryption settings definition.

When using encrypted logging, a small amount of data might remain in an in-memory buffer until the log file is closed. The encryption is performed using a block cipher, and it cannot write an incomplete block of data until the file is closed. This is not an issue for any log file that is not being actively written.

To examine the contents of a log file that is being actively written, use the `rotate-log` tool to force the file to be rotated before attempting to examine it.

## Configuring log signing

Configure log signing for a log publisher.

### Steps

1. To enable log signing for a log publisher, use `dsconfig`.

   #### Example:

   In this example, the `sign-log` property is set on the File-based Audit Log Publisher.

   ```shell
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set sign-log:true
   ```

2. Disable and then re-enable the log publisher for the change to take effect.

   #### Example:

   ```shell
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set enabled:false
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set enabled:true
   ```

## Validating a signed file

The server provides a tool, `validate-file-signature`, that checks if a file has not been tampered with in any way.

### Steps

* Run the `validate-file-signature` tool to check if a signed file has been tampered with.

  #### Example:

  For this example, assume that the `sign-log` property was enabled for the File-Based Audit Log Publisher.

  ```shell
  $ bin/validate-file-signature --file logs/audit
  ```

  #### Result:

  ```
  All signature information in file 'logs/audit' is valid
  ```

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If any validations errors occur, you will see a message similar to the one as follows.```
  One or more signature validation errors were encountered
  while validating the contents of file 'logs/audit':
  * The end of the input stream was encountered without
    encountering the end of an active signature block.
    The contents of this signed block cannot be trusted
    because the signature cannot be verified
  ``` |

## Configuring log file encryption

Configure log file encryption for a log publisher.

### Steps

1. To enable encryption for a log publisher, use `dsconfig`.

   #### Example:

   In this example, the File-based Access Log Publisher `"Encrypted Access"` is created, compression is set, and rotation and retention policies are set.

   ```shell
   $ bin/dsconfig create-log-publisher-prop --publisher-name "Encrypted Access" \
     --type file-based-access \
     --set enabled:true \
     --set compression-mechanism:gzip \
     --set encryption-settings-definition-id:332C846EF0DCD1D5187C1592E4C74CAD33FC1E5FC20B726CD301CDD2B3FFBC2B \
     --set encrypt-log:true \
     --set log-file:logs/encrypted-access \
     --set "rotation-policy:24 Hours Time Limit Rotation Policy" \
     --set "rotation-policy:Size Limit Rotation Policy" \
     --set "retention-policy:File Count Retention Policy" \
     --set "retention-policy:Free Disk Space Retention Policy" \
     --set "retention-policy:Size Limit Retention Policy"
   ```

2. Decrypt and decompress the file.

   #### Example:

   ```shell
   $ bin/encrypt-file --decrypt \
     --decompress-input \
     --input-file logs/encrypted-access.20180216040332Z.gz.encrypted \
     --output-file decrypted-access
   ```

   #### Result:

   ```
   Initializing the server's encryption framework...Done
   Writing decrypted data to file '/ds/Data-Sync/decrypted-access' using a
   key generated from encryption settings definition '332c846ef0dcd1d5187c1592e4c74cad33fc1e5fc20b726cd301cdd2b3ffbc2b'
   Successfully wrote 123,456,789 bytes of decrypted data
   ```

---

---
title: About log compression
description: The server supports the ability to compress log files as they are written.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_log_compression
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_log_compression.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 2, 2023
---

# About log compression

The server supports the ability to compress log files as they are written.

This feature can significantly increase the amount of data that can be stored in a given amount of space so that log information can be kept for a longer period of time.

Because of the inherent problems with mixing compressed and uncompressed data, compression can only be enabled at the time the logger is created. Compression cannot be turned on or off when the logger is configured. Because of problems in trying to append to an existing compressed file, if the server encounters an existing log file at startup, it rotates that file and begin a new one rather than attempting to append to the previous file.

Compression is performed using the standard gzip algorithm, so compressed log files can be accessed using readily available tools. The `summarize-access-log` tool can also work directly on compressed log files rather than requiring them to be decompressed first.

However, because it can be useful to have a small amount of uncompressed log data available for troubleshooting purposes, administrators using compressed logging might want to have a second logger defined that does not use compression and has rotation and retention policies that minimizes the amount of space consumed by those logs while still making them useful for diagnostic purposes without the need to decompress the files before examining them.

Configure compression by setting the `compression-mechanism` property to have the value of `gzip` when creating a new logger.

---

---
title: About log signing
description: The server supports the ability to cryptographically sign a log to ensure that it has not been modified in any way.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_log_signing
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_log_signing.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 2, 2023
---

# About log signing

The server supports the ability to cryptographically sign a log to ensure that it has not been modified in any way.

For example, financial institutions require audit logs for all transactions to check for correctness. Tamper-proof files are needed to ensure that these transactions can be properly validated and ensure that they have not been modified by any third-party entity or internally by unscrupulous employees.

Use the `dsconfig` tool to enable the `sign-log` property on a log publisher to turn on cryptographic signing.

When enabling signing for a logger that already exists and was enabled without signing, the first log file is not completely verifiable because it still contains unsigned content from before signing was enabled. Only log files whose entire content was written with signing enabled are considered completely valid. For the same reason, if a log file is still open for writing, then signature validation does not indicate that the log is completely valid because the log doesn't include the necessary end signed content indicator at the end of the file.

To validate log file signatures, use the `validate-file-signature` tool provided in the `bin` directory of the server or the `bat` directory for Windows systems.

After you have enabled this property, you must disable and then re-enable the log publisher for the changes to take effect.

---

---
title: About manage-certificates check-certificate-usability
description: The manage-certificates tool offers a check-certificate-usability subcommand to examine a specified entry in a key store and to identify potential issues that might interfere with secure communication.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_manage_certs_check_cert
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_manage_certs_check_cert.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# About manage-certificates check-certificate-usability

The `manage-certificates` tool offers a `check-certificate-usability` subcommand to examine a specified entry in a key store and to identify potential issues that might interfere with secure communication.

The `check-certificate-usability` tool completes the following tasks:

* Ensures that a specified entry in the key store includes a private key and a complete certificate chain

* Checks whether the certificate at the root of the chain is found in the Java virtual machine's (JVM's) default set of trusted certificates

* Ensures that the current time lies is within the validity window for all certificates in the chain

* Validates the signatures for all certificates in the chain

* Warns if the end-entity certificate is self-signed

* Warns if the end-entity certificate does not contain an extended key usage extension with the `serverAuth` usage

* Warns if the issuer certificates do not have a key usage extension with the `keyCertSign` usage

* Warns if the issuer certificates do not have a basic constraints extension indicating that it can operate as a certification authority

  If the chain violates a path length constraint, the `check-certificate-usability` tool reports an error.

* Ensures that the signature algorithm uses a strong message digest algorithm, like SHA-256

  The `check-certificate-usability` tool reports an error for weak digest algorithms like MD5 or SHA-1, and reports a warning for unrecognized digest algorithms.

* Ensures that none of the certificates that use an RSA key pair have a key size less than 2048 bits

The following example demonstrates the usage for the `manage-certificates check-certificate-usability` command and its output when no problems are identified.

```shell
$ bin/manage-certificates check-certificate-usability \
     --keystore config/keystore \
     --keystore-password-file config/keystore.pin \
     --alias server-cert

Successfully retrieved the certificate chain for alias 'server-cert':

Subject DN:  CN=ds1.example.com,O=Example Corp,C=US
Issuer DN:  CN=Example Intermediate CA,O=Example Corp,C=US
Validity Start Time: Tuesday, November 12, 2019 at 03:52:44 PM CST
                     (5 minutes, 45 seconds ago)
Validity End Time: Wednesday, November 11, 2020 at 03:52:44 PM CST
                   (364 days, 23 hours, 54 minutes, 14 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with RSA
Public Key Algorithm:  RSA (2048-bit)
SHA-1 Fingerprint: 84:e4:00:b9:f0:6b:58:bb:ac:67:79:28:2f:43:9f:e3:ac:24:ee:98
SHA-256 Fingerprint: 63:85:4d:2c:50:ea:a8:84:54:e0:73:9a:e7:5b:e7:1b:06:85:0e:
                     28:2b:76:a9:8b:57:fc:27:f7:60:81:48:41

Subject DN:  CN=Example Intermediate CA,O=Example Corp,C=US
Issuer DN:  CN=Example Root CA,O=Example Corp,C=US
Validity Start Time: Tuesday, November 12, 2019 at 03:52:42 PM CST
                     (5 minutes, 47 seconds ago)
Validity End Time: Monday, November 7, 2039 at 03:52:42 PM CST
                   (7299 days, 23 hours, 54 minutes, 12 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with RSA
Public Key Algorithm:  RSA (4096-bit)
SHA-1 Fingerprint: de:da:3d:fc:d4:1f:67:79:0a:a1:5a:cd:ca:4a:7e:a5:d3:46:88:27
SHA-256 Fingerprint:
   02:3c:af:ad:b7:07:81:89:45:48:d0:09:31:a8:90:c4:17:11:1c:00:11:fd:49:b2:2c:
   ba:ac:dd:c4:9f:03:36

Subject DN:  CN=Example Root CA,O=Example Corp,C=US
Issuer DN:  CN=Example Root CA,O=Example Corp,C=US
Validity Start Time: Tuesday, November 12, 2019 at 03:52:38 PM CST
                     (5 minutes, 51 seconds ago)
Validity End Time: Monday, November 7, 2039 at 03:52:38 PM CST
                   (7299 days, 23 hours, 54 minutes, 8 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with RSA
Public Key Algorithm:  RSA (4096-bit)
SHA-1 Fingerprint: 8e:03:e4:58:e6:e3:59:9a:55:77:c0:88:3c:fa:d7:29:f4:ff:de:6c
SHA-256 Fingerprint: 95:54:0d:e2:aa:48:29:c1:25:7c:20:69:c0:27:33:31:81:07:02:
                     2e:00:24:ae:49:5e:98:bd:a3:72:a5:05:26

OK:  The certificate chain is complete.  Each subsequent certificate is
the issuer for the previous certificate in the chain, and the chain ends
with a self-signed certificate.

OK:  Certificate 'CN=ds1.example.com,O=Example Corp,C=US' has a valid
signature.

OK:  Certificate 'CN=Example Intermediate CA,O=Example Corp,C=US' has a
valid signature.

OK:  Certificate 'CN=Example Root CA,O=Example Corp,C=US' has a valid
signature.

OK:  Certificate 'CN=ds1.example.com,O=Example Corp,C=US' will expire at
Wednesday, November 11, 2020 at 03:52:44 PM CST (364 days, 23 hours, 54
minutes, 14 seconds from now), which is not in the near future.

OK:  Issuer certificate 'CN=Example Intermediate CA,O=Example Corp,C=US'
will expire at Monday, November 7, 2039 at 03:52:42 PM CST (7299 days, 23
hours, 54 minutes, 12 seconds from now), which is not in the near future.

OK:  Issuer certificate 'CN=Example Root CA,O=Example Corp,C=US' will
expire at Monday, November 7, 2039 at 03:52:38 PM CST (7299 days, 23
hours, 54 minutes, 8 seconds from now), which is not in the near future.

OK:  Certificate 'CN=ds1.example.com,O=Example Corp,C=US' at the head of
the chain includes an extended key usage extension, and that extension
includes the serverAuth usage.

OK:  Issuer certificate 'CN=Example Intermediate CA,O=Example Corp,C=US'
includes a basic constraints extension, and the certificate chain
satisfies those constraints.

OK:  Issuer certificate 'CN=Example Intermediate CA,O=Example Corp,C=US'
includes a key usage extension with the keyCertSign usage flag set to
true.

OK:  Issuer certificate 'CN=Example Root CA,O=Example Corp,C=US' includes
a basic constraints extension, and the certificate chain satisfies those
constraints.

OK:  Issuer certificate 'CN=Example Root CA,O=Example Corp,C=US' includes
a key usage extension with the keyCertSign usage flag set to true.

OK:  Certificate 'CN=ds1.example.com,O=Example Corp,C=US' uses a signature
algorithm of 'SHA-256 with RSA', which is is considered strong.

OK:  Certificate 'CN=Example Intermediate CA,O=Example Corp,C=US' uses a
signature algorithm of 'SHA-256 with RSA', which is is considered strong.

OK:  Certificate 'CN=Example Root CA,O=Example Corp,C=US' uses a signature
algorithm of 'SHA-256 with RSA', which is is considered strong.

OK:  Certificate 'CN=ds1.example.com,O=Example Corp,C=US' has a 2048-bit
RSA public key, which is considered strong.

OK:  Certificate 'CN=Example Intermediate CA,O=Example Corp,C=US' has a
4096-bit RSA public key, which is considered strong.

OK:  Certificate 'CN=Example Root CA,O=Example Corp,C=US' has a 4096-bit
RSA public key, which is considered strong.

No usability errors or warnings were identified while validating the
certificate chain.
```

If any usability issues are identified, they might be responsible for communication problems.

---

---
title: About Periodic Stats Loggers
description: The Periodic Stats Logger plugin records server performance metrics at fixed intervals, enabling you to monitor and analyze server behavior over time.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_prof_server_perf_stats
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_prof_server_perf_stats.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 8, 2025
---

# About Periodic Stats Loggers

The Periodic Stats Logger plugin records server performance metrics at fixed intervals, enabling you to monitor and analyze server behavior over time. You can control which statistics are collected and adjust their level of detail. The logger captures historical information, such as LDAP operation metrics, host details, and gauge data.

At each interval, the logger writes server statistics to either a JSON file or a comma-separated value (`.csv`) log. The logger has a negligible impact on server performance unless the `log-interval` property is set to a value less than 1 second.

You can create multiple loggers with different configurations, depending on your monitoring needs.

Learn more about the Periodic Stats Logger in the following topics:

* [Enabling the Periodic Stats Logger plugin](paz_enable_periodic_stats_logger.html)

* [Configuring the Periodic Stats Logger](paz_config_periodic_stats_logger.html)

* [Enabling HTTP metrics in the Periodic Stats Logger](paz_enable_http_metrics_stats_logger.html)

* [Sending Periodic Stats Logger metrics to Splunk with the Splunk Universal Forwarder](paz_send_metrics_periodic_stats_logger_splunk_univ_forwarder.html)

---

---
title: About representing certificates, private keys, and certificate signing requests
description: X.509 is an encoding format that uses the ASN.1 distinguished encoding rules (DER), which exist in binary format. When writing a certificate to a file, either a raw DER format or a plaintext format called PEM can be used.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_rep_certs_keys_signing_reqs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_rep_certs_keys_signing_reqs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# About representing certificates, private keys, and certificate signing requests

X.509 is an encoding format that uses the ASN.1 distinguished encoding rules (DER), which exist in binary format. When writing a certificate to a file, either a raw DER format or a plaintext format called PEM can be used.

PEM encoding consists of a line that contains the text `-----BEGIN CERTIFICATE-----`, followed by a set of lines that contains the base64-encoded representation of the raw DER bytes (typically with no more than 64 characters per line), followed by a line that contains the text `-----END CERTIFICATE-----`.

The X.509 encoding contains a certificate's public key, but not its private key. The PKCS #8 specification in [RFC 5958](https://www.ietf.org/rfc/rfc5958.txt) describes the encoding for private keys. This approach uses a DER encoding with a PEM variant that instead uses the following header and footer, respectively.

```
-----BEGIN PRIVATE KEY-----
-----END PRIVATE KEY-----
```

RFC 5958 also describes an encrypted representation of the private key, but that format is currently unsupported.

The PKCS #10 specification in [RFC 2986](https://www.ietf.org/rfc/rfc2986.txt) describes the CSR format. This format uses a DER encoding with a PEM variant that uses the following header and footer, respectively.

```
-----BEGIN CERTIFICATE REQUEST-----
-----END CERTIFICATE REQUEST-----
```

Some implementations use the following alternate, nonstandard forms.

```
-----BEGIN NEW CERTIFICATE REQUEST-----
-----END NEW CERTIFICATE REQUEST-----
```

---

---
title: About SCIM searches
description: Search requests are used to return System for Cross-domain Identity Management (SCIM) resources. You can constrain search requests using filters.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_about_scim_searches
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_about_scim_searches.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# About SCIM searches

Search requests are used to return System for Cross-domain Identity Management (SCIM) resources. You can constrain search requests using filters.

A request that potentially causes the return of multiple SCIM resources is considered a search request. Perform such requests in one of the following manners:

* Make a `GET` request to `/scim/v2/<resourceType>`.

* Make a `POST` request to `/scim/v2/<resourceType>/.search`.

To constrain the search results, clients should supply a search filter through the `filter` parameter. For example, a `GET` request to `/scim/v2/Users?filter=st+eq+"TX"` returns all SCIM resources of the `Users` resource type in which the `st` attribute possesses a value of `"TX"`. Additionally, the `Add Filter` policy can add a filter automatically to search requests.

---

---
title: About the API security gateway
description: When you configure PingAuthorize Server for the API gateway pattern, the server and gateway provide dynamic authorization management between a client and a REST API.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_api_security_gw
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_api_security_gw.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 24, 2026
---

# About the API security gateway

When you configure PingAuthorize Server for the API gateway pattern, the server and gateway provide dynamic authorization management between a client and a REST API.

You can find specific details about the functionality of the API security gateway in the following topics:

* [API gateway request and response flow](paz_sec_gw_request_response_flow.html)

* [Gateway configuration basics](paz_gw_config_basics.html)

* [API security gateway authentication](paz_api_security_gw_authn.html)

* [API security gateway policy requests](paz_api_security_gw_policy_reqs.html)

* [API security gateway HTTP 1.1 support](paz_api_security_gw_http_support.html)

* [Gateway error templates](paz_gateway_error_templates.html)

* [Tuning API security gateway performance](paz_api_security_gw_performance_tuning.html)

---

---
title: Authenticating to the JSON PDP API
description: The JSON PDP API can require a client to authenticate to it by using a shared secret.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_authenticate_json_pdp_api
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_authenticate_json_pdp_api.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  json_create_shared_secret: Creating a shared secret
  steps: Steps
  example: Example:
  example-2: Example:
  json_delete_shared_secret: Deleting a shared secret
  steps-2: Steps
  example-3: Example:
  example-4: Example:
  rotating-shared-secrets: Rotating shared secrets
  steps-3: Steps
  customizing-the-shared-secret-header: Customizing the shared secret header
  steps-4: Steps
  example-5: Example:
---

# Authenticating to the JSON PDP API

The JSON PDP API can require a client to authenticate to it by using a shared secret.

To define shared secrets, use JSON PDP API Shared Secret configuration objects. To manage shared secrets, use the JSON PDP API HTTP Servlet Extension.

## Creating a shared secret

Define the authentication credentials that the JSON PDP API might require a client to present.

### Steps

1. To create a shared secret, run the following example `dsconfig` command, substituting values of your choosing.

   #### Example:

   ```
   PingAuthorize/bin/dsconfig create-authorization-policy-decision-shared-secret \
     --secret-name "Shared Secret A" \
     --set "shared-secret:secret123"
   ```

   |   |                                                                                                                                                                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * The `shared-secret` property sets the value that the JSON PDP API requires the client to present. After you set this value, it is no longer visible.

   * The `secret-name` property is a label that allows an administrator to distinguish one JSON PDP API Shared Secret from another. |

2. To update the `shared-secrets` property, run the following example `dsconfig` command.

   #### Example:

   ```
   PingAuthorize/bin/dsconfig set-http-servlet-extension-prop \
     --extension-name "JSON PDP API" \
     --add "shared-secrets:Shared Secret A"
   ```

   A new JSON PDP API Shared Secret is not used until the `shared-secrets` property of the JSON PDP API HTTP Servlet Extension is updated.

## Deleting a shared secret

You can remove a shared secret from use or delete it entirely.

### Steps

* To remove a JSON PDP API Shared Secret from use, run the following example `dsconfig` command, substituting values of your choosing.

  #### Example:

  ```json
  {pingauthorize}/bin/dsconfig set-http-servlet-extension-prop \
    --extension-name "JSON PDP API" \
    --remove "shared-secrets:Shared Secret A"
  ```

* To delete a JSON PDP API Shared Secret, run the following example `dsconfig` command.

  #### Example:

  ```json
  {pingauthorize}/bin/dsconfig delete-authorization-policy-decision-shared-secret \
    --secret-name "Shared Secret A"
  ```

## Rotating shared secrets

To avoid service interruptions, the JSON PDP API allows multiple, distinct shared secrets to be accepted at the same time.

You can configure a new shared secret that the JSON PDP API accepts alongside an existing shared secret. This allows time to update the client to use the new shared secret.

### Steps

1. Create a new JSON PDP API shared secret and assign it to the JSON PDP API HTTP Servlet Extension. Learn more in [Creating a shared secret](#json_create_shared_secret).

2. Update the client to use the new shared secret.

3. Remove the previous JSON PDP API shared secret. Learn more in [Deleting a shared secret](#json_delete_shared_secret).

## Customizing the shared secret header

By default, the JSON PDP API accepts a shared secret from a client through the CLIENT-TOKEN header.

### Steps

* To customize a shared secret header, change the value of the JSON PDP API HTTP Servlet Extension's `shared-secret-header` property.

  #### Example:

  The following command changes the shared secret header to `x-shared-secret`.

  ```json
  {pingauthorize}/bin/dsconfig set-http-servlet-extension-prop \
    --extension-name "JSON PDP API" \
    --set shared-secret-header-name:x-shared-secret
  ```

  The following command resets the shared secret header to its default value.

  ```json
  {pingauthorize}/bin/dsconfig set-http-servlet-extension-prop \
    --extension-name "JSON PDP API" \
    --reset shared-secret-header-name
  ```

---

---
title: Auto-healing for unavailable servers
description: Using gauges, set up auto-healing in a container deployment to address an unavailable server.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_auto_healing
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_auto_healing.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
section_ids:
  steps: Steps
---

# Auto-healing for unavailable servers

Using gauges, set up auto-healing in a container deployment to address an unavailable server.

## Steps

1. Configure one or more of the gauges described in [Server availability](paz_server_availability.html).

2. Configure the gauges to trigger the UNAVAILABLE status.

   By default, the gauges do not trigger the UNAVAILABLE status.

   As discussed in [Endpoint Average Response Time (Milliseconds) gauge](paz_endpoint_avg_resp.html) and [HTTP Processing (Percent) gauge](paz_http_proc_gauge.html), use the `dsconfig` command to adjust the following values for your environment. Each system is different so you might need to adjust the values several times to determine your ideal configuration.

   1. For the `Endpoint Average Response Time (Milliseconds)` gauge, set `critical-value`.

   2. For the `HTTP Processing (Percent)` gauge, set both `critical-value` and `server-unavailable-severity-level`.

3. Configure the container orchestrator to use the `available-or-degraded-state` endpoint to detect whether the server is alive.

   For information about the endpoint, see [Availability servlet](paz_server_status.html#availability_servlet).

---

---
title: Automatic backend LDAP server discovery
description: Instead of explicitly specifying all backend LDAP servers in the configuration as LDAP external servers, you can configure PingAuthorize Server to automatically discover its backend servers.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_auto_backend_discovery
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_auto_backend_discovery.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Automatic backend LDAP server discovery

Instead of explicitly specifying all backend LDAP servers in the configuration as LDAP external servers, you can configure PingAuthorize Server to automatically discover its backend servers.

|   |                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature requires that all backend LDAP servers be PingDirectory Servers running version 8.0.0.0 or later. Automatic backend discovery is not supported for PingDirectoryProxy Server or third-party LDAP servers. |

To configure automatic backend discovery, you must complete these tasks:

* Join the PingAuthorize Server to the same topology as the PingDirectory Servers.

* Configure the PingAuthorize Server's load-balancing algorithm with an LDAP external server template. This template provides the connection and health check settings that PingAuthorize Server uses for all PingDirectory Servers.

* Configure the topology registry entry for each PingDirectory Server to indicate the name of the PingAuthorize Server load-balancing algorithm.

---

---
title: Available gauges
description: PingAuthorize makes the following gauges available. You can manage these gauges using the administrative console or the dsconfig tool.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_available_gauges
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_available_gauges.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Available gauges

PingAuthorize makes the following gauges available. You can manage these gauges using the administrative console or the `dsconfig` tool.

| Gauge name                                    | Enabled by default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available File Descriptors                    | true               | Monitors the number of file descriptors available to the server process. The server allows for an unlimited number of connections by default but is restricted by the file descriptor limit on the operating system.You can configure the number of file descriptors that the server uses by either setting the `NUM_FILE_DESCRIPTORS` environment variable or by creating a `config/num-file-descriptors` file with a single line such as, `NUM_FILE_DESCRIPTORS=12345`. If you do not use either of these options, the server uses the default of 65535.Running out of available file descriptors can lead to unpredictable behavior and severe system instability.                                                                                                                                                                                                             |
| Certificate Expiration (Days)                 | true               | Monitors the expiration dates of key server certificates.A server certificate expiring can cause server unavailability, degradation, or loss of key server functionality.Replace certificates nearing the end of their validity as soon as possible.For more information about server certificates and how they are managed, see the `status` tool or **Status** in the administrative console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CPU Usage (Percent)                           | true               | Monitors server CPU use and provides an averaged percentage for the interval defined.The monitored resource is the host system's CPU, which does not include a resource identifier. If CPU use is high, check the server's current workload and other processes on the system and make any needed adjustments. Reducing the load on the system will lead to better response times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Disk Busy (Percent)                           | true               | Monitors the percentage of disk use time averaged over the specified update interval.This gauge requires that you enable the Host System Monitor Provider and that you register any monitored disks by using the `disk-devices` property of that configuration object.The resource identifier for this gauge is the disk device name. Use the `iostat` command or a similar system utility to see a list of disk device names. A separate gauge monitor entry is created for each monitored disk.                                                                                                                                                                                                                                                                                                                                                                                 |
| Endpoint Average Response Time (Milliseconds) | false              | Monitors the average response time across all endpoints since the server was started. This number does not include requests to the upstream server.There is no resource identifier associated with this gauge.The monitored resource is overall response time of all requests to PingAuthorize servlets since the server was started.High response times might be indicative of a number of factors including a disk-bound server, network latency, or misconfiguration. Enabling the Stats Logger plugin can help isolate problems.For more information, see [Endpoint Average Response Time (Milliseconds) gauge](paz_endpoint_avg_resp.html).                                                                                                                                                                                                                                  |
| HTTP Processing (Percent)                     | true               | Monitors the percentage of time that request handler threads spend processing HTTP requests. This percentage represents the inverse of the server's ability to handle new requests without queueing.For more information, see [HTTP Processing (Percent) gauge](paz_http_proc_gauge.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| JVM Memory Usage (Percent)                    | true               | Monitors the percentage of Java Virtual Machine memory that is in use. This value naturally fluctuates due to garbage collection, so the minimum value within an interval is reported because it is a better indication of overall memory growth.When the memory usage exceeds 90%, open a case with [Ping Identity Support](https://support.pingidentity.com/) because the server is either misconfigured or has a memory leak.As memory usage approaches 100%, the server is more and more likely to experience garbage collection pauses, which leave the server unresponsive for a long time. Restarting the server is likely the only remedy for this situation. Before you restart the server, run `collect-support-data` and capture the output of `jmap -histo <server-pid>` to provide to customer support. The PID of the server is in `<server-root>/logs/server.pid`. |
| License Expiration (Days)                     | true               | Monitors the expiration date of the product license. An expired license causes warnings to appear in the server's logs and in the `status` tool output.Request a license key through the Ping Identity licensing website <https://www.pingidentity.com/en/account/request-license-key.html> or contact <sales@pingidentity.com>.Use the `dsconfig` tool to update the License configuration's license key property.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Memory Usage (Percent)                        | false              | Monitors the percentage of memory use averaged over the update interval defined. The monitored resource is the host system's memory use, which does not have a resource identifier.Some operating systems, including Linux, use the majority of memory for file system cache, which is freed as applications need it. If memory use is high, check the applications that are running on the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Policy Decision Service Availability          | true               | Monitors availability of the Policy Decision Service.If the Policy Decision Service is misconfigured or cannot reach the deployment package store, PingAuthorize services will be unavailable.Ensure that the `pdp-mode` and `trust-framework-version` are correctly set, and that the deployment package store is reachable.For more information, see [Policy Decision Service Availability gauge](paz_policy_dec_srv_avial_gauge.html).                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Strong Encryption Not Available               | true               | Indicates the JVM does not appear to support strong encryption algorithms, like 256-bit AES. The server will fall back to using weaker algorithms, like 128-bit AES.To enable support for strong encryption, update your JVM to a newer version that supports it by default; alternatively, install or enable the unlimited encryption strength jurisdiction policy files in your Java installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| User Store Availability                       | true               | Monitors availability of the SCIM user store.If the LDAP directory servers are unavailable, the "UserStoreAdapter" cannot forward requests. Also, the server cannot process SCIM requests or perform token owner lookups.Ensure that LDAP directory servers are available.For more information, see [User Store Availability gauge](paz_user_store_avail_gauge.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

---

---
title: Available manage-certificates subcommands
description: The manage-certificates tool uses the following subcommands to indicate which function to invoke:
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_available_subcmds
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_available_subcmds.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Available manage-certificates subcommands

The `manage-certificates` tool uses the following subcommands to indicate which function to invoke:

| Subcommand                                 | Function                                                                                                                                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `list-certificates`                        | Lists the certificates in a keystore.                                                                                                                                                |
| `import-certificate`                       | Imports a certificate into a trusted certificate entry or imports a certificate chain and private key into a private key entry.                                                      |
| `export-certificate`                       | Exports a certificate from a keystore.                                                                                                                                               |
| `export-private-key`                       | Exports a private key from a keystore.                                                                                                                                               |
| `generate-self-signed-certificate`         | Generates a self-signed certificate.                                                                                                                                                 |
| `generate-certificate-signing-request`     | Generates a certificate-signing request that can be provided to a certification authority.                                                                                           |
| `sign-certificate-signing-request`         | Signs a certificate-signing request with a specified issuer certificate.                                                                                                             |
| `check-certificate-usability`              | Checks a specified certificate in a keystore to verify whether it is suitable for use as a listener certificate.                                                                     |
| `trust-server-certificate`                 | Initiates the TLS-negotiation process with a specified server to obtain its certificate chain so that a truststore can be updated with the necessary information to trust the chain. |
| `display-certificate-file`                 | Displays the contents of a file that contains one or more PEM-encoded or DER-encoded X.509 certificates.                                                                             |
| `display-certificate-signing-request-file` | Displays the contents of a file that contains a PEM-encoded or DER-encoded PKCS #10 certificate-signing request (CSR).                                                               |
| `change-certificate-alias`                 | Changes the alias for an entry in a keystore.                                                                                                                                        |
| `change-keystore-password`                 | Changes the password for a keystore.                                                                                                                                                 |
| `change-private-key-password`              | Changes the password that protects the private key for a specified entry in a keystore.                                                                                              |

---

---
title: Certificate chains
description: A certificate chain is an ordered list of one or more certificates. In such a chain, each subsequent certificate is the issuer of the previous certificate.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_chains
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_chains.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate chains

A certificate chain is an ordered list of one or more certificates. In such a chain, each subsequent certificate is the issuer of the previous certificate.

During TLS negotiation, the server presents a certificate chain to the client, which determines whether to trust the chain and continue with the negotiation. The client can also present its own certificate chain to the server.

If a certificate is self-signed, its chain contains only that single certificate. If a certificate is signed by a self-signed certificate authority (CA) certificate, such as a root CA, the chain contains two certificates: the server certificate and the CA certificate that follows it. If a single intermediate CA (a CA certificate that is signed by a root CA) is present, the chain contains the server certificate, followed by the intermediate CA, and then the root CA.

Intermediate certificate authorities are useful for security purposes, especially in commercial authorities. If a client trusts a root CA certificate, it is likely to trust anything with that root CA certificate at the base of its chain. Consequently, the root CA certificate must be kept secure.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | If the root CA certificate is compromised, any certificate that is directly or indirectly signed by it can no longer be trusted. |

With intermediate CA certificates, the root certificate can be kept offline in secure storage and used only when a new intermediate CA certificate must be signed. The intermediate CA certificates can be used to sign end-entity certificates, but must be protected to avoid compromising any of the certificates. A compromised certificate must be revoked along with all of the certificates that it signed. In such a scenario, the root CA can be used to sign a new certificate.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The certificate chain that the server presents to the client, or that the client presents to the server, during TLS negotiation does not always need to be the complete chain. If the root CA at the end of the chain is widely trusted, the server can assume that the client already has that root CA in its default set of trusted certificates. The server can leave that root CA off the chain with the assumption that the client will retrieve it from its default trust store. While the same assumption could theoretically be true for intermediate CA certificates, only the root CA certificate is commonly omitted. When a client receives an incomplete chain, the client looks in its default trust store to determine whether the trust store contains the issuer certificate, which it can identify by using properties like the issuer distinguished name (DN) or an authority key identifier extension. |

The certificate at the head of a certificate chain, which appears as the first one in the list, is often called the end-entity certificate. If this certificate appears at the head of the chain that a server presents during TLS negotiation, it is referred to as the server certificate. If the certificate appears at the head of a chain that a client presents, it is referred to as a client certificate. The certificate at the end of a complete chain must be a root CA certificate. In the case of a self-signed certificate, the chain contains only a single certificate that serves both roles.

---

---
title: Certificate extensions
description: Extensions provide additional context for a certificate.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_extensions
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_extensions.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate extensions

Extensions provide additional context for a certificate.

Some of the more common extension types include the following:

* Subject key identifier

  Holds a unique identifier for the certificate, which is generally derived from the certificate's public key.

* Authority key identifier

  Holds the subject key identifier for the issuer certificate. This extension type helps to identify the issuer certificate, especially when presented with an incomplete certificate chain.

* Subject alternative name

  Holds a list of ways that clients are expected to reference a server when establishing a connection to it.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Clients must take this information into account when deciding whether to trust a server's certificate.The most common types of values include DNS names, IP addresses, and URIs. DNS names must be fully qualified, but can optionally use an asterisk in the leftmost component to match any single name in that component. For example, `*.example.com` could match `www.example.com` or `ldap.example.com`, but would not match `ldap.east.example.com` or `example.com`. |

* Key usage

  Provides information about the manner in which the certificate is expected to be used. The following key usages are allowed:

  * `digitalSignature`

    Indicates that the certificate can be used for digitally signing data, excluding certificates and certificate revocation lists (CRL).

  * `nonRepudiation`

    Indicates that the certificate can be used to prevent denying the authenticity of a message. `nonRepudiation` is also known as `contentCommitment`.

  * `keyEncipherment`

    Indicates that the certificate can be used to protect encryption keys, such as symmetric keys that are derived during TLS key agreement.

  * `dataEncipherment`

    Indicates that the certificate can be used for encrypting data directly.

  * `keyAgreement`

    Indicates that the certificate's public key can be used for key agreement, such as deriving the symmetric key that protects TLS communication.

  * `keyCertSign`

    Indicates that the certificate can act as a certification authority and be used for signing other certificates.

  * `cRLSign`

    Indicates that the certificate can be used to sign CRLs.

  * `encipherOnly`

    When used in conjunction with `keyEncipherment`, indicates that the public key can be used only for encrypting data during key agreement.

  * `decipherOnly`

    When used in conjunction with `keyEncipherment`, indicates that the public key can be used only for decrypting data during key agreement.

* Extended key usage

  Acts as an alternative to the key usage extension and provides additional high-level functionality. The following extended key usages are allowed:

  * `serverAuth`

    Indicates that the server can present the certificate to the client during TLS negotiation.

  * `clientAuth`

    Indicates that the client can present the certificate to the server during TLS negotiation.

  * `codeSigning`

    Indicates that the certificate can be used to sign source and compiled code.

  * `emailProtection`

    Indicates that the certificate can be used to sign or encrypt email messages.

  * `timeStamping`

    Indicates that the certificate can be used to assert the time that an event occurred.

  * `ocspSigning`

    Indicates that the certificate can be used to sign an online certificate status protocol (OCSP) response.

* Basic constraints

  Indicates whether the certificate can act as a certification authority and, if so, the maximum number of intermediate certificates that can follow it in a certificate chain.

---

---
title: Certificate key pairs
description: Each certificate contains a key pair that consists of two keys that are linked cryptographically. If you encrypt data with one key, the data can be only decrypted with the other key.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_key_pairs
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_key_pairs.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate key pairs

Each certificate contains a key pair that consists of two keys that are linked cryptographically. If you encrypt data with one key, the data can be only decrypted with the other key.

Although a key pair can be created easily when both keys are generated simultaneously, the process of deriving one key from the other is extremely difficult, a process categorized in cryptographic terms as computationally infeasible.

When generating a key pair, one key is designated as the public key, and the other key is designated the private key. The public key can be made widely available, but the private key must be kept secret and not shared with anyone.

As long as the secrecy of the private key is maintained, the key pair can be used to perform the following functions:

* Encryption, sometimes referred to as confidentiality

  If someone wants to send you a secret message without anyone else viewing it, the message can be encrypted with your public key. Only you possess the private key, so only you can decrypt the message.

* Digital signatures

  If you encrypt data with your private key, it can be decrypted only with your public key. Because your public key can be made widely available, this encryption method does not actually protect the content. However, digital signatures prove that a message came from you because only your private key could have generated it.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When generating a digital signature, the entire message is generally not encrypted. Only a hash of the message is encrypted, typically by using a digest algorithm like SHA-256.This approach protects the integrity of a message. A decrypted signature that matches the digest of the original message guarantees that the message came from you and that it has remained unaltered since you signed it. |

The following public key algorithms are used primarily in certificates that facilitate TLS communication:

* RSA, which is based on the multiplication of large prime numbers

* EC, which is based on computations that involve special types of elliptical curves

Although RSA is supported more widely than EC, it is slower and requires larger keys to achieve the same level of security. To support legacy clients, you should use an RSA certificate and choose a key size of at least 2,048 bits.

If all of your clients support EC certificates, you should use an EC certificate with a key size of at least 256 bits.

---

---
title: Certificate subject DNs
description: A certificate's subject distinguished name (DN) provides information about how the certificate should be used.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_subject_dns
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_subject_dns.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificate subject DNs

A certificate's subject distinguished name (DN) provides information about how the certificate should be used.

Like an LDAP DN, a certificate's subject DN consists of a comma-delimited series of attribute-value pairs. However, unlike an LDAP DN, the attribute names in a certificate subject DN are typically written in all uppercase characters.

A certificate's subject DN is also referred to as its subject. The following attributes commonly appear in a certificate subject.

| Attribute name | Attribute description                                                                                                                                                                                                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CN`           | Common name&#xA;&#xA;For a listener certificate, the CN attribute typically identifies the host name that clients use to access the certificate. However, the subject alternative name extension is recommended more highly for accomplishing the same task. Most certificate subject DNs include at least the CN attribute. |
| `E`            | Email address                                                                                                                                                                                                                                                                                                                |
| `OU`           | Name of the organizational unit, such as the relevant department                                                                                                                                                                                                                                                             |
| `O`            | Name of the organization or company                                                                                                                                                                                                                                                                                          |
| `L`            | Name of the locality, such as the appropriate city                                                                                                                                                                                                                                                                           |
| `ST`           | Full name of the state or province                                                                                                                                                                                                                                                                                           |
| `C`            | ISO 3166 country code                                                                                                                                                                                                                                                                                                        |

A certificate subject includes at least one attribute-value pair, and the `CN` attribute is typically present. Other attributes can be omitted, although the `O` and `C` attributes are also common. For example, a listener certificate for a server with an address of `ldap.example.com`, which is run by the US-based company Example Corp, might have a subject of `CN=ldap.example.com,O=Example Corp,C=US`.

---

---
title: Certificate trust
description: When a server presents its certificate chain to a client during TLS negotiation, the client decides whether to trust the certificate chain and concludes whether it is communicating with a legitimate server instead of an impostor.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_cert_trust
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_cert_trust.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2022
section_ids:
  processing-steps: Processing steps
---

# Certificate trust

When a server presents its certificate chain to a client during TLS negotiation, the client decides whether to trust the certificate chain and concludes whether it is communicating with a legitimate server instead of an impostor.

If a client is tricked through DNS hijacking into communicating with a rogue application instead of with a legitimate server, the application can steal the client's credentials, or can fool the client into concluding that it has performed an action that it has not performed. If a rogue application acts as a broker between the client and the legitimate server, the client might be unable to detect the change, and the malicious application might be capable of stealing data or altering the communication. Consequently, you should avoid `trust all` or `blind trust` options in a production environment.

When determining whether to trust a server certificate chain, a client performs the following steps.

![Diagram of a client's step-by-step evaluation of a certificate chain for trust purposes](_images/jjt1610752070457.png)

## Processing steps

1. Verifies that it has received the complete certificate chain.

   If a server presents an incomplete chain, the client must ensure that it can complete the chain with information in an explicitly provided trust store or default trust store. If the client cannot complete the certificate chain, the chain is not trusted.

2. Verifies that each subsequent certificate in the chain is the issuer certificate for, and that its private key was used to sign, the certificate that precedes it.

   |   |                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If a certificate chain contains extraneous certificates, or if a subsequent certificate did not issue the certificate that precedes it, the chain is not trusted. |

3. Confirms that it has a reason to trust the certificate at the root of the chain.

   |   |                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This step is generally performed by ensuring that the root certificate authority (CA) certificate can be found in either a default trust store or a trust store that is configured for use by the client. If the client has no prior knowledge of the root CA certificate, the chain is not trusted. |

4. Verifies that the current time lies within the validity window for each certificate in the chain.

   |   |                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The chain is not trusted under the following conditions:- When the `notBefore` value of any certificate in the chain is later than the current time.

   - When the `notAfter` value of any certificate in the chain is earlier than the current time. |

5. Verifies that the server certificate at the head of the chain is suitable for the server with which the client thinks it is communicating.

   |   |                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The client must verify that the address used to connect to the server matches one of the following values:- The `CN` attribute of the certificate's subject.

   - One of the values of any subject alternative name extension. |

These steps represent a starting point. If necessary, the client can perform additional types of validation. For example, if a root or intermediate certification authority maintains a certificate revocation list (CRL) or supports the online certificate status protocol (OCSP), the client must verify that none of the certificates in the chain has been revoked. The client can also verify that the CA certificates include the basic constraints extension, and that the server certificate does not contain too many levels. Other checks, like those that use certificate policy extensions, can also be performed.

---

---
title: Certificate trust
description: When a server presents its certificate chain to a client during TLS negotiation, the client decides whether to trust the certificate chain and concludes whether it is communicating with a legitimate server instead of an impostor.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_certificate_chain_trust
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_certificate_chain_trust.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Aprul 28, 2025
section_ids:
  processing-steps: Processing steps
---

# Certificate trust

When a server presents its certificate chain to a client during TLS negotiation, the client decides whether to trust the certificate chain and concludes whether it is communicating with a legitimate server instead of an impostor.

If a client is tricked through DNS hijacking into communicating with a rogue application instead of with a legitimate server, the application can steal the client's credentials, or can fool the client into concluding that it has performed an action that it has not performed. If a rogue application acts as a broker between the client and the legitimate server, the client might be unable to detect the change, and the malicious application might be capable of stealing data or altering the communication. Consequently, you should avoid `trust all` or `blind trust` options in a production environment.

When determining whether to trust a server certificate chain, a client performs the following steps.

![jjt1610752070457](_images/jjt1610752070457.png)

## Processing steps

1. Verifies that it has received the complete certificate chain.

   If a server presents an incomplete chain, the client must ensure that it can complete the chain with information in an explicitly provided trust store or default trust store. If the client cannot complete the certificate chain, the chain is not trusted.

2. Verifies that each subsequent certificate in the chain is the issuer certificate for, and that its private key was used to sign, the certificate that precedes it.

   |   |                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If a certificate chain contains extraneous certificates, or if a subsequent certificate did not issue the certificate that precedes it, the chain is not trusted. |

3. Confirms that it has a reason to trust the certificate at the root of the chain.

   |   |                                                                                                                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This step is generally performed by ensuring that the root certificate authority (CA) certificate can be found in either a default trust store or a trust store that is configured for use by the client. If the client has no prior knowledge of the root CA certificate, the chain is not trusted. |

4. Verifies that the current time lies within the validity window for each certificate in the chain.

   |   |                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The chain is not trusted under the following conditions:- When the `notBefore` value of any certificate in the chain is later than the current time.

   - When the `notAfter` value of any certificate in the chain is earlier than the current time. |

5. Verifies that the server certificate at the head of the chain is suitable for the server with which the client thinks it is communicating.

   |   |                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The client must verify that the address used to connect to the server matches one of the following values:- The `CN` attribute of the certificate's subject.

   - One of the values of any subject alternative name extension. |

These steps represent a starting point. If necessary, the client can perform additional types of validation. For example, if a root or intermediate certification authority maintains a certificate revocation list (CRL) or supports the online certificate status protocol (OCSP), the client must verify that none of the certificates in the chain has been revoked. The client can also verify that the CA certificates include the basic constraints extension, and that the server certificate does not contain too many levels. Other checks, like those that use certificate policy extensions, can also be performed.

---

---
title: Certificates
description: The server presents a server certificate when a client uses a protocol like LDAPS or HTTPS to initiate a secure connection. A client must trust the server's certificate to obtain a secure connection to it.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_certificates
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_certificates.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# Certificates

The server presents a server certificate when a client uses a protocol like LDAPS or HTTPS to initiate a secure connection. A client must trust the server's certificate to obtain a secure connection to it.

PingAuthorize Server uses server certificates.

During setup, administrators have the option of using self-signed certificates or certificate authority (CA)-signed certificates for the server certificate. Use CA-signed certificates wherever possible. Use self-signed certificates for demonstration and proof-of-concept environments only.

If you specify the option `--generateSelfSignedCertificate` during setup, the server certificate generates automatically with the alias `server-cert`. The key pair consists of the private key and the self-signed certificate, and is stored in a file named `keystore`, which resides in the server's `/config` directory. The certificates for all the servers that the server trusts are stored in the `truststore` file, which is also located under the server's `/config` directory.

To override the server certificate alias and the files that store the key pair and certificates, use the following arguments during setup:

* `--certNickname`

* `--use*Keystore`

* `--use*Truststore`

For more information about these arguments, see the setup tool's *Help and the Installation Guide*.
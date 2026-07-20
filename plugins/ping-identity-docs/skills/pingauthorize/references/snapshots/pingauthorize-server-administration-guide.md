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
title: About the Authorization Policy Decision APIs
description: The PingAuthorize Server provides Authorization Policy Decision APIs to support non-API use cases needing attribute-based access control (ABAC).
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_authr_policy_decision
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_authr_policy_decision.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2023
---

# About the Authorization Policy Decision APIs

The PingAuthorize Server provides Authorization Policy Decision APIs to support non-API use cases needing attribute-based access control (ABAC).

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Authorization Policy Decision APIs feature requires PingAuthorize Premier. For more information, contact your Ping Identity account representative. |

The PingAuthorize Server's main functionality is to enforce fine-grained policies for data accessed through an application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)*. However, organizations might need to use the core Policy Decision Service for non-API use cases. For example, an application server might use it to request policy decisions when generating dynamic web content. In this configuration, PingAuthorize Server becomes the policy decision point (PDP), and the application server becomes the policy enforcement point (PEP).

The Authorization Policy Decision APIs consist of the following PDP APIs:

* XACML-JSON PDP API

  This API provides a standards-based interface.

  Standards-based enforcement points request policy decisions based on a subset of the XACML-JSON standard. For more information, see [XACML 3.0 JSON Profile 1.1](http://docs.oasis-open.org/xacml/xacml-json-http/v1.1/csprd01/xacml-json-http-v1.1-csprd01.html).

* JSON PDP API

  This API provides a simpler interface.

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The Authorization Policy Decision APIs can indicate when a request or response triggers statements, but the application server must implement the statement. |

To make a PDP API available, you must:

* Configure the PingAuthorize Server with a feature-enabled license during setup.

* Configure the Policy Decision Point Service. For more information, see [Use policies in a production environment](paz_config_embedded_pdp.html).

* For the XACML-JSON PDP API, configure an access token *(tooltip: \<div class="paragraph">
  \<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
  \</div>)* validator or use token validation within your rules and policies. For more information, see [Access token validators](paz_access_token_validators.html) or [Policy conditions](../pingauthorize_policy_administration_guide/paz_conditions.html).

---

---
title: About the config-diff tool
description: The config-diff tool compares server configurations and produces a dsconfig batch file that lists the differences.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_config_diff_tool
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_config_diff_tool.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
section_ids:
  example: Example
---

# About the config-diff tool

The `config-diff` tool compares server configurations and produces a `dsconfig` batch file that lists the differences.

When run without arguments, the `config-diff` tool produces a list of changes to the configuration, as compared to the server's baseline or out-of-the-box configuration. Because this list captures the customizations of your server configuration, it is useful when you transition from a development environment to a staging or production environment.

## Example

```shell
$  {pingauthorize}/bin/config-diff
# No comparison arguments provided, so using "--sourceLocal --sourceTag postSetup --targetLocal" to compare the local configuration with the post-setup configuration.
# Run "config-diff --help" to get a full list of options and example usages.

# Configuration changes to bring source (config-postSetup.gz) to target (config.ldif)
# Comparison options:
#   Ignore differences on shared host
#   Ignore differences by instance
#   Ignore differences in configuration that is part of the topology registry

dsconfig create-external-server --server-name "DS API Server" --type api
--set base-url:https://localhost:1443 --set hostname-verification-method:allow-all --set "trust-manager-provider:Blind Trust" --set user-name:cn=root --set "password:AADaK6dtmjJQ7W+urtx9RGhSvKX9qCS8q5Q="

dsconfig create-external-server --server-name "FHIR Sandbox" --type api
--set base-url:https://fhir-open.sandboxcerner.com[https://fhir-open.sandboxcerner.com]
...
```

---

---
title: About the configuration audit log
description: The configuration audit log records the configuration commands that represent configuration changes, as well as the configuration commands that undo the changes.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_config_audit_log
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_config_audit_log.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
section_ids:
  example: Example
---

# About the configuration audit log

The configuration audit log records the configuration commands that represent configuration changes, as well as the configuration commands that undo the changes.

All successful configuration changes are recorded to the file `logs/config-audit.log`.

## Example

```shell
$ tail -n 8  {pingauthorize}/logs/config-audit.log
# [23/Feb/2019:23:16:24.667 -0600] conn=4 op=12 dn='cn=Directory Manager,cn=Root DNs,cn=config' authtype=[Simple] from=127.0.0.1 to=127.0.0.1
# Undo command: dsconfig delete-external-server --server-name "{pingauthorize}  PAP"
dsconfig create-external-server --server-name "{pingauthorize}  PAP" --type policy --set base-url:http://localhost:4200 --set "branch:Default Policies"

# [23/Feb/2019:23:16:24.946 -0600] conn=5 op=22 dn='cn=Directory Manager,cn=Root DNs,cn=config' authtype=[Simple] from=127.0.0.1 to=127.0.0.1
# This change was made to mirrored configuration data, which is automatically kept in sync across all servers.
# Undo command: dsconfig set-policy-decision-service-prop --set "policy-server:{pingauthorize}  (Gateway Policy Example)"
dsconfig set-policy-decision-service-prop --set "policy-server:{pingauthorize}  PAP"
```

---

---
title: About the dsconfig tool
description: The dsconfig tool provides a command-line interface to configure the underlying server configuration.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_dsconfig_tool
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_dsconfig_tool.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 22, 2024
section_ids:
  example: Example
  example-2: Example
---

# About the dsconfig tool

The `dsconfig` tool provides a command-line interface to configure the underlying server configuration.

Use the `dsconfig` tool whenever you administer the server from a shell. When run without arguments, `dsconfig` enters an interactive mode that lets you browse and update the configuration from a menu-based interface. Use this interface to list, update, create, and delete configuration objects.

When viewing any configuration object in `dsconfig`, use the `d` command to display the command line that is necessary to recreate a configuration object. You can use a command line in this form directly from a shell or placed in a `dsconfig` batch file, along with other commands.

Batch files are a powerful feature that enable scripted deployments. By convention, these scripts use a file extension of `dsconfig`. Batch files support comments by using the `#` character, and they support line continuation by using the `\`, or backslash, character.

## Example

This example `dsconfig` script configures the PingAuthorize Server policy service.

```
# Define an external  {pingauthorize}  PAP
dsconfig create-external-server \
  --server-name "{pingauthorize}  {PAP_Name}" \
  --type policy \
  --set base-url:http://localhost:4200 \
  --set user-id:admin \
  --set "branch:Default Policies"
# Configure the policy service
dsconfig set-policy-decision-service-prop \
  --type scim \
  --set pdp-mode:external \
  --set "policy-server:{pingauthorize}  PAP" \
  --set "decision-response-view:request" \
  --set "decision-response-view:decision-tree"
```

## Example

To load a `dsconfig` batch file, run `dsconfig` with the `--batch-file` argument.

```shell
$  {pingauthorize}/bin/dsconfig -n --batch-file example.dsconfig

Batch file 'example.dsconfig' contains 2 commands.

Pre-validating with the local server ..... Done

Executing: create-external-server -n --server-name "{pingauthorize}  PAP" --type policy --set base-url:http://localhost:4200 --set "branch:Default Policies"

Arguments from tool properties file:  --useSSL  --hostname localhost --port 8636 --bindDN cn=root --bindPassword * --trustAll

The Policy External Server was created successfully.

Executing: set-policy-decision-service-prop -n --set pdp-mode:external --set "policy-server:{pingauthorize}  PAP" --set
decision-response-view:request --set decision-response-view:decision-tree

The Policy Decision Service was modified successfully.
```

---

---
title: About the layout of the PingAuthorize Server folders
description: The following table describes the contents of the PingAuthorize Server distribution file. In addition, the table describes items created as you use PingAuthorize Server.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_layout_server_folders
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_layout_server_folders.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# About the layout of the PingAuthorize Server folders

The following table describes the contents of the PingAuthorize Server distribution file. In addition, the table describes items created as you use PingAuthorize Server.

**PingAuthorize Server directories, files, and tools**

| Directories, files, and tools | Description                                                                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `README`                      | README file that describes the steps to set up and start PingAuthorize Server.                                                                      |
| `bak`                         | Stores the physical backup files used with the backup command-line tool.                                                                            |
| `bat`                         | Stores Windows-based command-line tools for PingAuthorize Server.                                                                                   |
| `bin`                         | Stores UNIX/Linux-based command-line tools for PingAuthorize Server.                                                                                |
| `build-info.txt`              | Contains build and version information for PingAuthorize Server.                                                                                    |
| `collector`                   | Used by the server to make monitored statistics available to PingDataMetrics Server.                                                                |
| `config`                      | Stores the configuration files for the backends (admin, config) as well as the directories for messages, schema, tools, and updates.                |
| `docs`                        | Provides the product documentation.                                                                                                                 |
| `extensions`                  | Stores Server SDK extensions.                                                                                                                       |
| `ldif`                        | Serves as the default location for LDIF exports and imports.                                                                                        |
| `legal`                       | Stores any legal notices for dependent software used with PingAuthorize Server.                                                                     |
| `lib`                         | Stores any scripts, jar, and library files needed for the server and its extensions.                                                                |
| `locks`                       | Stores any lock files in the backends.                                                                                                              |
| `logs`                        | Stores log files for PingAuthorize Server.                                                                                                          |
| `metrics`                     | Stores the metrics that can be gathered for this server and surfaced in PingDataMetrics Server.                                                     |
| `resource`                    | Stores supporting files such as default policies, a sample server profile template, and MIB files for SNMP.                                         |
| `revert-update`               | The revert-update tool for UNIX/Linux systems.                                                                                                      |
| `revert-update.bat`           | The revert-update tool for Windows systems.                                                                                                         |
| `setup`                       | The setup tool for UNIX/Linux systems.                                                                                                              |
| `setup.bat`                   | The setup tool for Windows systems.                                                                                                                 |
| `tmp`                         | Stores temporary files and directories used by the server, including extracted WAR files and compiled JSP files used by Web Application Extensions. |
| `uninstall`                   | The uninstall tool for UNIX/Linux systems.                                                                                                          |
| `uninstall.bat`               | The uninstall tool for Windows systems.                                                                                                             |
| `update`                      | The update tool for UNIX/Linux systems.                                                                                                             |
| `update.bat`                  | The update tool for Windows systems.                                                                                                                |
| `velocity`                    | Stores any customized Velocity templates and other artifacts (CSS, Javascript, images), or Velocity applications hosted by the server.              |
| `webapps`                     | Stores web application files such as the administrative console.                                                                                    |

---

---
title: About the layout of the Policy Editor folders
description: The following table describes the contents of the Policy Editor distribution file:
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_layout_pe_folders
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_layout_pe_folders.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
---

# About the layout of the Policy Editor folders

The following table describes the contents of the Policy Editor distribution file:

**Policy Editor directories, files, and tools**

| Directories, files, and tools | Description                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `admin-point-application`     | Stores any `.jar` and library files needed for the server.                                                                                                                                                                                                                                                                                                                                                                   |
| `bin`                         | Stores UNIX/Linux-based command-line tools for the Policy Editor.                                                                                                                                                                                                                                                                                                                                                            |
| `build-info.txt`              | Contains build and version information for the Policy Editor.                                                                                                                                                                                                                                                                                                                                                                |
| `config`                      | Stores the configuration, including the keystore for the web server HTTPS certificate.                                                                                                                                                                                                                                                                                                                                       |
| `lib`                         | Stores any `.jar` and library files needed by the command-line tools.To make a custom Spring Expression Language (SpEL) resolver available to the Policy Editor, add the resolver's `.jar` library to the `/extensions` subdirectory and add the SpEL Java class to the [allow list](paz_prepare_policies_production.html#paz_add_spel_java_classes). For example, `PingAuthorize-PAP/lib/extensions/addl-spel-classes.jar`. |
| `logs`                        | Stores log files for the Policy Editor.                                                                                                                                                                                                                                                                                                                                                                                      |
| `policy-backup`               | Stores H2 [policy database backups](paz_policy_db_backups.html) when such backups are enabled.                                                                                                                                                                                                                                                                                                                               |
| `resource`                    | Stores supporting files such as policy snapshots.                                                                                                                                                                                                                                                                                                                                                                            |

---

---
title: About the manage-certificates tool
description: "PingAuthorize Server offers a manage-certificates tool that enables interaction with Java KeyStore (JKS) and PKCS #12 key stores."
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_manage_certs_tool
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_manage_certs_tool.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
---

# About the manage-certificates tool

PingAuthorize Server offers a `manage-certificates` tool that enables interaction with Java KeyStore (JKS) and PKCS #12 key stores.

Although it behaves similarly to the `keytool` utility that accompanies most Java distributions, `manage-certificates` is easier to use, provides improved usage information, and offers additional functionality.

---

---
title: About the manage-profile tool
description: The manage-profile tool is provided with the server to work with server profiles. It includes subcommands for creating, applying, and replacing server profiles, all of which significantly reduce the effort required by an administrator to configure a server appropriately.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_about_manage_profile_tool
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_about_manage_profile_tool.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 29, 2022
section_ids:
  manage-profile-generate-profile: manage-profile generate-profile
  manage-profile-setup: manage-profile setup
  manage-profile-replace-profile: manage-profile replace-profile
---

# About the manage-profile tool

The `manage-profile` tool is provided with the server to work with server profiles. It includes subcommands for creating, applying, and replacing server profiles, all of which significantly reduce the effort required by an administrator to configure a server appropriately.

The following sections describe these subcommands in more detail. For more information about the `manage-profile` tool, run `manage-profile --help`. For more information about each individual subcommand and its options, run `manage-profile <subcommand> --help`.

## manage-profile generate-profile

To create a server profile from a configured server, use the `generate-profile` subcommand. The generated profile contains the following information, which provides a base for completing a profile:

* Command-line arguments that were used to set up the server

* `dsconfig` commands necessary to configure the server

* Installed server SDK extensions

* Files that are added to the server root

To produce a complete profile, some parts of the generated profile might require modifications, such as adding password files that `setup-arguments.txt` uses. The `--instanceName` and `--localHostName` arguments in `setup-arguments.txt` are made variables by `generate-profile`, and must be provided values when other `manage-profile` subcommands use the generated profile.

LDIF files must also be added manually to the generated profile.

The `--excludeSetupArguments` option generates a server profile without a setup-arguments.txt file. This is useful when generating server profiles for use with Docker images.

## manage-profile setup

To apply a server profile to a fresh, unconfigured server, use the `setup` subcommand, which replaces the normal setup tool when using a server profile. Run `manage-profile setup` to complete the following tasks:

* Copies the pre-setup files to the server root

* Runs the setup tool

* Copies the post-setup files to the server root

* Installs any server SDK extensions

* Runs any dsconfig batch files

* Imports any LDIF files

* Starts the server

While manage-profile setup is running, a copy of the profile is created in a temporary directory that can be specified by using the `--tempProfileDirectory` argument. The command leaves the server in a complete and running state when finished, unless the `--doNotStart` argument is specified.

## manage-profile replace-profile

Run the `replace-profile` subcommand on a server that was originally set up with a server profile to replace its configuration with a new profile. The tool applies a specified server profile to an existing server while preserving its data, topology configuration, and replication configuration. New LDIF files from the replacement server profile are not imported.

While `manage-profile replace-profile` is running, the existing server is stopped and moved to a temporary directory that the `--tempServerDirectory` argument can specify. A fresh, new server is subsequently installed and set up with the new profile. The final server is left running if it was running before the command was started, and remains stopped if it was stopped.

Run `manage-profile replace-profile` from a second unzipped server install package on the same host as the existing server, similar to the `update` tool. Use the `--serverRoot` argument to specify the root of the existing server that will have its profile replaced.

If files have been added or modified in the server root since the most recent `manage-profile setup` or `manage-profile replace-profile` was run, they are included in the final server with the replaced profile. Otherwise, files specifically added from the `server-root` directory of the previous server profile are absent from the final server with the replaced profile. If errors occur during the subcommand, such as the new profile having an invalid `setup-arguments.txt` file, the existing server returns to its original state from before `manage-profile replace-profile` was run.

The `--skipValidation` option skips the validation step when running on an offline server

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `manage-profile replace-profile` tool can update the server version when needed. This tool can also directly apply configuration changes when there are no other changes in the new profile. This is a shorter process when making small changes to `dsconfig`. |

---

---
title: About the SCIM service
description: PingAuthorize Server's built-in System for Cross-domain Identity Management (SCIM) service provides a REST API for data that is stored in one or more external datastores, based on the SCIM 2.0 standard.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_about_scim_service
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_about_scim_service.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2025
---

# About the SCIM service

PingAuthorize Server's built-in System for Cross-domain Identity Management (SCIM) service provides a REST API for data that is stored in one or more external datastores, based on the [SCIM 2.0 standard](https://datatracker.ietf.org/doc/html/rfc7644).

For information about the SCIM service, see the following topics:

* [SCIM API request and response flow](paz_scim_request_response_flow.html)

* [SCIM configuration basics](paz_scim_config_basics.html)

* [SCIM endpoints](paz_scim_endpoints.html)

* [SCIM authentication](paz_scim_authentication.html)

* [SCIM policy requests](paz_scim_policy_requests.html)

* [Lookthrough limit for SCIM searches](paz_lookthrough_limit.html)

* [Disabling the SCIM REST API](paz_disable_scim_rest_api.html)

---

---
title: About the SCIM user store
description: This topic focuses on the relationship between the PingAuthorize Server SCIM subsystem and its backend data stores, particularly LDAP directory servers.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_about_scim_user_store
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_about_scim_user_store.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2022
---

# About the SCIM user store

This topic focuses on the relationship between the PingAuthorize Server SCIM subsystem and its backend data stores, particularly LDAP directory servers.

For general information about SCIM configuration, see [SCIM configuration basics](paz_scim_config_basics.html).

The PingAuthorize Server SCIM 2.0 REST API and SCIM token resource lookup methods rely on external data stores, collectively called a *user store*, to locate user records. Typically, a user store is composed of a set of PingDirectory Servers, optionally fronted by a set of PingDirectoryProxy Servers. The SCIM subsystem manages communication with the user store through a *store adapter*, which translates SCIM requests into requests native to the data stores. The following diagram shows an example setup.

![Diagram that shows an LDAP store adapter that feeds into a load-balancing algorithm. The algorithm feeds traffic to LDAP external servers that front servers](_images/swa1591876161868.png)

PingAuthorize Server includes a store adapter type for use with LDAP data stores, the *LDAP store adapter*. The LDAP store adapter manages communications to a pool of LDAP servers using a *load-balancing algorithm*. PingAuthorize Server supports two types of load-balancing algorithms.

| Load-balancing algorithm type              | Description                                                                                                                                                                                           |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Failover load-balancing algorithm          | Attempts to always send requests to the same backend LDAP server. If the preferred server is not available, then it fails over to alternate servers.                                                  |
| Fewest operations load-balancing algorithm | Forwards requests to the backend LDAP server with the fewest operations currently in progress.You should only use this load-balancing algorithm when all backend servers are Directory Proxy Servers. |

Typically, you connect a load-balancing algorithm to its backend LDAP servers by defining *LDAP external servers* in the configuration and attaching them to the load-balancing algorithm configuration. An LDAP external server configuration manages the actual LDAP connections to a backend LDAP server, such as PingDirectory Server.

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Alternatively, if all backend LDAP servers are PingDirectory Servers (version 8.0.0.0 and later), you can configure a load-balancing algorithm to automatically discover the backend servers. See [Automatic backend LDAP server discovery](paz_auto_backend_discovery.html). |

LDAP external servers monitor and report the availability of backend LDAP servers using LDAP health checks. See [LDAP health checks](paz_ldap_health_checks.html).

---

---
title: About the Sideband API
description: The sideband API provides dynamic authorization management for requests and responses and returns them in a potentially modified form, which the API gateway forwards to the backend REST API or the client.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_about_sideband_api
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_about_sideband_api.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 7, 2022
---

# About the Sideband API

The sideband API provides dynamic authorization management for requests and responses and returns them in a potentially modified form, which the API gateway forwards to the backend REST API or the client.

As a gateway, PingAuthorize Server functions as a reverse proxy that performs the following steps:

* Intercepts client traffic to a backend REST API service

* Authorizes the traffic to a policy decision point (PDP) that operates either within the PingAuthorize process, called embedded PDP mode, or outside the PingAuthorize process, called external PDP mode

Using the sideband API, you can configure the PingAuthorize Server instead as an adapter *(tooltip: \<div class="paragraph">
\<p>Plug-in software that allows Ping products to interact with web applications and authentication systems.\</p>
\</div>)* to an external API gateway. In sideband mode, an API gateway integration point intercepts client traffic to a backend REST API service and passes intercepted traffic to the PingAuthorize sideband API.

---

---
title: About the Trust Framework
description: The Trust Framework defines all the entities that your organization can use to build policies. These entities include, for example, the HTTP request attributes that describe API requests protected by PingAuthorize Server and the services that identify the REST APIs themselves.
component: pingauthorize
version: 11.1
page_id: pingauthorize:pingauthorize_server_administration_guide:paz_about_trust_framework
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/pingauthorize_server_administration_guide/paz_about_trust_framework.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 16, 2023
section_ids:
  trust-framework-versions: Trust Framework versions
---

# About the Trust Framework

The Trust Framework defines all the entities that your organization can use to build policies. These entities include, for example, the HTTP request attributes that describe API requests protected by PingAuthorize Server and the services that identify the REST APIs themselves.

To understand how PingAuthorize Server uses the Trust Framework, you must understand how PingAuthorize Server interacts with its policy engine, also called the policy decision point (PDP). In general, the flow is:

1. PingAuthorize Server receives a SCIM 2.0 or API request and translates it to a *policy request*.

2. PingAuthorize Server submits the policy request to the PDP for evaluation.

3. The PDP applies any matching policies to the policy request and then issues a policy decision.

4. PingAuthorize Server uses the policy decision to determine how to proceed with the request, depending on the decision result (typically PERMIT or DENY) and any statements included with the decision.

Consider these simple examples.

* A policy decision with a DENY result could cause PingAuthorize Server to reject a request because it originates from an untrusted IP address.

* A policy decision with the Exclude Attributes statement could cause PingAuthorize Server to remove specific attributes from an API response because the requesting user lacks a necessary entitlement.

Each policy request that PingAuthorize Server generates includes a specific set of attributes. These attributes vary based on the service being used. For more information, see the following topics:

* [API security gateway policy requests](paz_api_security_gw_policy_reqs.html)

* [Sideband API policy requests](paz_sideband_api_policy_reqs.html)

* [SCIM policy requests](paz_scim_policy_requests.html)

Policy request structure is tightly coupled to the Trust Framework. If the Trust Framework entity definitions do not match the policy requests generated by PingAuthorize Server, then PingAuthorize Server does not function as expected. For this reason, your Trust Framework should always be based on the default policies included with the server installation package in the file `resource/policies/defaultPolicies.SNAPSHOT`.

For information about working with the Trust Framework to customize your organization's policies, see [Trust Framework](../pingauthorize_policy_administration_guide/paz_trust_framework.html).

## Trust Framework versions

The policy request structure used by PingAuthorize Server is versioned so that it can evolve across releases of the server. You configure the version in the Policy Decision Service using the `trust-framework-version` property. PingAuthorize Server always supports a minimum of two Trust Framework versions, the current (and preferred) Trust Framework version and the previous Trust Framework version.

When an instance of PingAuthorize Server is first installed, the Trust Framework version is undefined. The server raises an alarm to indicate this condition and to provide instructions about how to set the preferred version.

You should explicitly set the version to the preferred version. For example, the following `dsconfig` command configures the Policy Decision Service to form policy requests using Trust Framework version v2.

```
dsconfig set-policy-decision-service-prop \
  --set trust-framework-version:{TRUST_FRAMEWORK_VERSION}
```

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | When the Trust Framework version is set, add the configuration to the server profile that you use to deploy new server instances. |

New releases of PingAuthorize Server might introduce changes to the way that the server generates policy requests, potentially in ways that are not backward-compatible with the Trust Framework and policies used in a previous release. In these cases, PingAuthorize Server will prefer the new Trust Framework version and raises an alarm with instructions to move to the new Trust Framework version. Existing policies will continue to work with the older Trust Framework version. However, the older Trust Framework version will be deprecated, so transitioning to the new Trust Framework version is imperative.

For more information about upgrading the Trust Framework version, see [Upgrading the Trust Framework and policies](../upgrading_pingauthorize/paz_upgrade_trust_framework_policies.html).
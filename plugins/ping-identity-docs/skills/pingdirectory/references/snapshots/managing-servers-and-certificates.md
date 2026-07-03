---
title: About representing certificates, private keys, and certificate signing requests
description: X.509 is an encoding format that uses the ASN.1 distinguished encoding rules (DER), which exist in binary format. When writing a certificate to a file, either a raw DER format or a plain-text format called PEM can be used.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_rep_certs_pvt_keys_cert_signing_reqs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_rep_certs_pvt_keys_cert_signing_reqs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# About representing certificates, private keys, and certificate signing requests

X.509 is an encoding format that uses the ASN.1 distinguished encoding rules (DER), which exist in binary format. When writing a certificate to a file, either a raw DER format or a plain-text format called PEM can be used.

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
title: Available subcommands
description: The manage-certificates tool uses the following subcommands to indicate which function to invoke:
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_available_subcommands
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_available_subcommands.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# Available subcommands

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
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_certificate_chains
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_certificate_chains.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_certificate_extensions
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_certificate_extensions.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
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
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_certificate_key_pairs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_certificate_key_pairs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_certificate_subject_dns
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_certificate_subject_dns.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
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
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_certificate_trust
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_certificate_trust.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
section_ids:
  processing-steps: Processing steps
---

# Certificate trust

When a server presents its certificate chain to a client during TLS negotiation, the client decides whether to trust the certificate chain and concludes whether it is communicating with a legitimate server instead of an impostor.

If a client is tricked through DNS hijacking into communicating with a rogue application instead of with a legitimate server, the application can steal the client's credentials, or can fool the client into concluding that it has performed an action that it has not performed. If a rogue application acts as a broker between the client and the legitimate server, the client might be unable to detect the change, and the malicious application might be capable of stealing data or altering the communication. Consequently, you should avoid `trust all` or `blind trust` options in a production environment.

When determining whether to trust a server certificate chain, a client performs the following steps.

![A process diagram that summarizes the steps described in detail in the following list.](_images/jjt1610752070457.png)

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
title: Common arguments
description: "Most of the manage-certificates subcommands require access to a Java KeyStore (JKS) or PKCS #12 keystore. In such instances, use the --keystore argument to specify the path to the keystore."
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_common_arguments
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_common_arguments.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Common arguments

Most of the `manage-certificates` subcommands require access to a Java KeyStore (JKS) or PKCS #12 keystore. In such instances, use the `--keystore` argument to specify the path to the keystore.

If the keystore already exists, the tool detects automatically whether it is a JKS or PKCS #12 keystore. If the operation creates a new keystore, you can specify the type explicitly by using the `--keystore-type` argument, followed by a value of `JKS` or `PKCS12`. If you do not specify the keystore type, a default value of `JKS` is used.

Some situations require you to provide the password that is needed to access the keystore. For a JKS keystore, you might need to provide a keystore password only for operations that involve creating a keystore or accessing a private key. However, you will likely need to provide the password for all operations that involve a PKCS #12 keystore.

To provide a keystore password, use one of the following arguments:

* `--keystore-password`, followed by the clear-text password for the keystore.

* `--keystore-password-file`, followed by the path to a file that contains the password for the keystore. The file might contain the password in the clear, or it might be encrypted with a definition from the server's encryption-settings database.

* `--prompt-for-keystore-password`. If this argument is provided, the tool prompts you interactively to provide the password.

If a private key is protected with a different password than the keystore itself, specify one of the following arguments to provide the private key password:

* `--private-key-password`, followed by the plain-text password.

* `--private-key-password-file`, followed by the path to a file that contains the clear-text or encrypted password.

* `--prompt-for-private-key-password`, which causes the tool to prompt interactively for the password.

Several operations require you to specify the keystore entry to target. In such scenarios, provide the `--alias` argument, followed by the name of the alias for that entry.

---

---
title: Enabling low-level debugging
description: This topic applies only to the PingDirectoryProxy server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_proxy_enable_low_level_debugging
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_proxy_enable_low_level_debugging.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling low-level debugging

## About this task

|   |                                                           |
| - | --------------------------------------------------------- |
|   | This topic applies only to the PingDirectoryProxy server. |

|   |                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because this approach requires multiple server restarts, it is not a popular option. You might be able to obtain more information without a restart by using the debugging support that is built into the server. For more information and to enable this level of support, see [Using the debug log publisher](pd_proxy_use_debug_log_publisher.html). |

To enable low-level debugging:

## Steps

1. In the `config/java.properties` file, add `-Djavax.net.debug=all` to the `start-server.java-args` property.

2. Run `bin/dsjavaproperties`.

3. Restart the server.

---

---
title: Enabling TLS support after setup
description: If the server has been set up without support for TLS, enable TLS support later by completing the following tasks.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_enable_tls_support_after_setup
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_enable_tls_support_after_setup.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
page_aliases: ["pd_ds_config_key_trust_mgr_providers.adoc", "pd_ds_config_connection_handlers.adoc", "pd_ds_update_topology_registry.adoc"]
section_ids:
  steps: Steps
  key_trust_mgrs: Configuring key and trust manager providers
  caching-key-and-trust-managers: Caching key and trust managers
  invalidating-the-cache: Invalidating the cache
  enabling-or-disabling-caching-optional: Enabling or disabling caching (optional)
  configuring-connection-handlers: Configuring connection handlers
  steps-2: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  updating-the-topology-registry: Updating the topology registry
---

# Enabling TLS support after setup

If the server has been set up without support for TLS, enable TLS support later by completing the following tasks.

## Steps

1. Obtain a certificate chain.

   To prepare a Java KeyStore JKS or PKCS #12 key store with an appropriate certificate chain and private key, use the `manage-certificates` tool. We also recommend that you create a trust store that the server can use. Learn more in [Certificate chains](pd_ds_certificate_chains.html).

2. Configure the key and trust manager providers.

3. Configure connection handlers.

## Configuring key and trust manager providers

After you have a key store, configure a key manager provider to access it.

The server is preconfigured with key manager providers, `JKS` and `PKCS12`, that you can use with JKS or PKCS #12 key stores, respectively. In most cases, you can update the appropriate key manager provider to reference the key store that you plan to use, as shown in the following example:

```
dsconfig set-key-manager-provider-prop \
    --provider-name JKS \
    --set enabled:true \
    --set key-store-file:config/keystore \
    --set key-store-pin-file:config/keystore.pin
```

A similar change configures a trust manager provider to reference the appropriate trust store, as shown in the following example:

```
dsconfig set-trust-manager-provider-prop \
    --provider-name JKS \
    --set enabled:true \
    --set include-jvm-default-issuers:true \
    --set trust-store-file:config/truststore \
    --set trust-store-pin-file:config/truststore.pin
```

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If all clients and servers use certificates that are signed by issuers and are included in the JVM's default trust store, you can use the `JVM-Default` trust manager provider to accomplish this task. |

### Caching key and trust managers

When you create key and trust manager providers, caching is enabled by default, allowing the manager providers to avoid loading key store and trust store files from disk when establishing connections to process requests.

#### Invalidating the cache

The manager provider reloads files from the configured key store or trust store and refreshes the cache under any of the following conditions:

* The cached manager for the configured store has a `null` value.

* The path to the cached store doesn't match the path of the configured store.

* The length of the cached store doesn't match the length of the configured store.

* The last-updated time for the cached store doesn't match the last-updated time for the configured store.

#### Enabling or disabling caching (optional)

You can define whether caching is enabled by using the `enable-key-manager-caching` or `enable-trust-manager-caching` properties. Supply a value of `false` to disable caching, causing manager providers to load managers for each connection. Supply a value of `true` to re-enable caching.

To create a key manager provider with caching disabled, supply the `enable-key-manager-caching` property with a value of `false`, as shown in the following example:

```
dsconfig create-key-manager-provider \
    --provider-name JKS \
    --type file-based \
    --set enabled:true \
    --set key-store-file:config/keystore \
    --set key-store-type:JKS \
    --set key-store-pin-file:config/keystore.pin \
    --set enable-key-manager-caching:false
```

To create a trust manager provider with caching disabled, supply the `enable-trust-manager-caching` property with a value of `false`, as shown in the following example:

```
dsconfig create-trust-manager-provider \
    --provider-name JKS \
    --type file-based \
    --set enabled:true \
    --set trust-store-file:config/truststore \
    --set trust-store-type:JKS \
    --set enable-trust-manager-caching:false
```

To re-enable caching, set a value of `true` for the same caching property used to create the manager provider, as shown in the following example:

```
dsconfig set-trust-manager-provider-prop \
    --provider-name JKS \
    --set enable-trust-manager-caching:true
```

## Configuring connection handlers

After you configure the key and trust manager providers, update the connection handlers to use the key and trust manager providers.

### Steps

* For the LDAP connection handler, use the following command to enable StartTLS with a configuration change. By default, the LDAP connection handler accepts non-secure connections.

  #### Example:

  ```
  dsconfig set-connection-handler-prop \
    --handler-name "LDAP Connection Handler" \
    --set allow-start-tls:true \
    --set key-manager-provider:JKS \
    --set trust-manager-provider:JKS \
    --set ssl-cert-nickname:server-cert \
    --set ssl-client-auth-policy:optional
  ```

* If you did not configure secure communication during setup, the LDAPS connection handler is disabled. To configure LDAPS support in this scenario, enable the connection handler and configure most of the same settings. You must set `allow-start-tls` to `false` and `use-ssl` to `true`. See the following code for an example configuration.

  #### Example:

  ```
  dsconfig set-connection-handler-prop \
    --handler-name "LDAPS Connection Handler" \
    --set enabled:true \
    --set key-manager-provider:JKS \
    --set trust-manager-provider:JKS \
    --set ssl-cert-nickname:server-cert \
    --set ssl-client-auth-policy:optional
  ```

  #### Example:

  The following example uses a similar configuration change to enable the HTTPS connection handler.

  ```
  dsconfig set-connection-handler-prop \
    --handler-name "HTTPS Connection Handler" \
    --set enabled:true \
    --set listen-port:443 \
    --set key-manager-provider:JKS \
    --set trust-manager-provider:JKS \
    --set ssl-cert-nickname:server-cert
  ```

## Updating the topology registry

After the server connection handlers are updated to enable TLS, update the topology registry to provide information about the new configuration.

The topology registry holds information about server instances that are part of the environment, and it helps to facilitate inter-server communication, such as replication, mirroring portions of the configuration, and the PingDirectory server's automatic backend server-discovery functionality.

The following table details the two types of entries that require updating:

**Configuration types and their update descriptions**

| Configuration Type                     | Update description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Server instance listener configuration | * Provides information that is needed to trust the TLS certificates that instances in the topology present.

* The server instance listener configuration must include the server certificate, which is defined as the certificate at the head of the chain. This version must be the multi-line, PEM-formatted representation of the certificate. You can use `dsconfig` to import the certificate from a file, as shown in the following example.

  ```
  bin/dsconfig set-server-instance-listener-prop \
    --instance-name ds1 \
    --listener-name ldap-listener-mirrored-config \
    --set server-ldap-port:636 \
    --set connection-security:ssl \
    --set 'listener-certificate>/ca/ds1-cert.pem'
  ```&#xA;&#xA;The less-than operator > in the final line indicates that the value is read from a file rather than provided directly. In addition, you might not need to enclose the property name and path within single straight quotes to prevent the shell from interpreting the less-than symbol as an attempt to redirect input. |
| Server instance configuration          | - Provides information about options for communicating with those instances.

- Update the server instance configuration object to reflect the new methods that are available for communication with the instance. For example, the `preferred-security` property identifies the mechanism by which other instances in the topology attempt to communicate with the instance.The following example code sets the LDAPS and HTTPS ports, indicates that StartTLS support is enabled, and instructs other instances to use SSL (LDAPS) when communicating with the instance.```
dsconfig set-server-instance-prop \
  --instance-name ds1 \
  --set ldaps-port:636 \
  --set https-port:443 \
  --set preferred-security:ssl \
  --set start-tls-enabled:true
```                                                                                                                                                                                                                                                                                           |

---

---
title: Enabling TLS support during setup
description: Enable TLS support in the server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_enable_tls_support_during_setup
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_enable_tls_support_during_setup.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# Enabling TLS support during setup

Enable TLS support in the server.

To enable TLS support in the server, you should complete one of the following tasks during the setup procedure:

* Provide a key store that contains the certificate to use.

* Make the installer generate a self-signed certificate.

When using the `setup` tool in interactive mode, it prompts you for the information that it needs to configure secure communication, as shown in the following example.

```
Do you want to enable the Directory Server services (Available State,
Available or Degraded State, Configuration, Consent, Directory REST API,
Documentation, and SCIM2) and Administrative Console over
HTTPS?  After setup, you can selectively enable or disable individual
services and applications by configuring the HTTPS Connection Handler
(yes / no) [yes]: yes

On which port should the Directory Server accept connections from HTTPS
clients? [443]: 443

On which port should the Directory Server accept connections from LDAP
clients? [389]: 389

Do you want to enable LDAPS? (yes / no) [yes]: yes
On which port should the Directory Server accept connections from LDAPS
clients? [636]: 636

Do you want to enable StartTLS? (yes / no) [yes]: yes

Certificate server options:

    1)  Generate self-signed certificate (recommended for testing purposes
        only)
    2)  Use an existing certificate located on a Java Keystore (JKS)
    3)  Use an existing certificate located on a PKCS12 keystore
    4)  Use an existing certificate on a PKCS11 token

Enter option [1]: 2

Java Keystore (JKS) path: /ca/ds1-keystore
Keystore PIN: {password}

Truststore options:

    1)  Generate a default JKS truststore
    2)  Use an existing JKS truststore
    3)  Use an existing PKCS12 truststore

Enter option [1]: 2

JKS truststore path: /ca/truststore
Truststore password (can be blank): {password}
```

When using `setup` in non-interactive mode, use the following arguments to configure TLS support.

| Argument                          | Description                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--ldapsPort {port}`              | Server enables support for LDAPS (LDAP over TLS) on the specified TCP port.                                                                                                                                                                                                                                |
| `--httpsPort {port}`              | Server enables support for HTTPS for SCIM, the Directory REST API, and the web-based admin console on the specified TCP port.                                                                                                                                                                              |
| `--enableStartTLS`                | LDAP connection handler enables support for the StartTLS extended operation.                                                                                                                                                                                                                               |
| `--generateSelfSignedCertificate` | `setup` generates a self-signed certificate that is presented to clients that use LDAPS, HTTPS, and the StartTLS extended operation.                                                                                                                                                                       |
| `--useJavaKeyStore {path}`        | Server uses the specified Java KeyStore (JKS) key store to obtain the certificate chain that it presents to clients that use LDAPS, HTTPS, and the StartTLS extended operation.                                                                                                                            |
| `--usePKCS12KeyStore {path}`      | Server uses the specified PKCS #12 key store to obtain the certificate chain that it presents to clients that use LDAPS, HTTPS, and the StartTLS extended operation.                                                                                                                                       |
| `--usePKCS11KeyStore`             | Server uses a PKCS #11 key store, like a hardware security module, to obtain the certificate chain that it presents to clients that use LDAPS, HTTPS, and the StartTLS extended operation. The Java Virtual Machine (JVM) must already be configured to access the appropriate key store through PKCS #11. |
| `--keyStorePassword {password}`   | Password that is needed to interact with the specified JKS, PKCS #12, or PKCS #11 key store. The `setup` tool assumes that the private key password matches the key store password.                                                                                                                        |
| `--keyStorePasswordFile {path}`   | Path to the file that contains the password needed to interact with the specified JKS, PKCS #12, or PKCS #11 key store.                                                                                                                                                                                    |
| `--certNickname {alias}`          | Alias of the private key entry in the specified key store that contains the certificate chain to present to clients during TLS negotiation. This argument is optional but recommended if the key store contains multiple certificates.                                                                     |
| `--useJavaTrustStore {path}`      | Server uses the specified JKS trust store to determine whether to trust certificate chains that are presented to it during TLS negotiation.                                                                                                                                                                |
| `--usePKCS12TrustStore {path}`    | Server uses the specified PKCS #12 trust store to determine whether to trust certificate chains that are presented to it during TLS negotiation                                                                                                                                                            |
| `--trustStorePassword {password}` | Password that is needed to interact with the specified JKS or PKCS #11 trust store.                                                                                                                                                                                                                        |
| `--trustStorePasswordFile {path}` | Path to the file that contains the password needed to interact with the specified JKS or PKCS #11 trust store.                                                                                                                                                                                             |

The following example command sets up the PingDirectory server in non-interactive mode with an existing certificate.

```shell
$ ./setup \
     --no-prompt \
     --acceptLicense \
     --ldapPort 389 \
     --ldapsPort 636 \
     --httpsPort 443 \
     --enableStartTLS \
     --useJavaKeyStore config/keystore \
     --keyStorePasswordFile config/keystore.pin \
     --certNickname server-cert \
     --useJavaTrustStore config/truststore \
     --trustStorePasswordFile config/truststore.pin \
     --baseDN dc=example,dc=com \
     --rootUserDN "cn=Directory Manager" \
     --rootUserPasswordFile root-pw.txt \
     --maxHeapSize 10g \
     --encryptDataWithPassphraseFromFile encryption-settings-password.txt \
     --instanceName ds1 \
     --location Austin \
     --noPropertiesFile


Ping Identity Directory Server 8.0.0.0

Initializing ..... Done
Configuring Directory Server ..... Done
Configuring Certificates ..... Done
Starting Directory Server ..... Done

Access product documentation from docs/index.html
```

---

---
title: Exporting certificates
description: Use the export-certificate subcommand to export a single certificate or a certificate chain from a key store to a file in PEM or DER format.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_export_certificates
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_export_certificates.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
---

# Exporting certificates

Use the `export-certificate` subcommand to export a single certificate or a certificate chain from a key store to a file in PEM or DER format.

The `export-certificate` subcommand supports the normal arguments about the key store and certificate alias, in addition to the following arguments:

* `--output-file {path}`

  Path to the file to which exported certificates are written. If this value is not provided, the certificates are written to standard output rather than a file.

* `--output-format {format}`

  Format in which exported certificates are written. The value can be `PEM` or `DER`, but the DER format can be used only if the output is written to a file. Defaults to `PEM` if no value is specified.

* `--export-certificate-chain`

  Indicates that a certificate chain, rather than the end-entity certificate only, is to be exported.

* `--separate-file-per-certificate`

  Indicates the use of separate output files for each exported certificate, rather than placing all of the certificates in a single file. If this argument is provided and multiple certificates are to be exported, then `.1` is appended to the path for the indicated output file for the first certificate in the chain, `.2` is appended for the second certificate, and so on.

The following example exports a certificate chain.

```shell
$ bin/manage-certificates export-certificate \
     --keystore config/keystore \
     --keystore-password-file config/keystore.pin \
     --alias server-cert \
     --output-file server-cert.pem \
     --output-format PEM \
     --export-certificate-chain \
     --separate-file-per-certificate

Successfully exported the following certificate to '/ds/server-cert.pem.1':
Subject DN:  CN=ds.example.com,O=Example Corp,C=US
Issuer DN:  CN=Example Root CA,O=Example Corp,C=US
Validity Start Time: Sunday, November 10, 2019 at 09:09:23 PM CST
                     (3 hours, 26 minutes, 23 seconds ago)
Validity End Time: Monday, November 9, 2020 at 09:09:23 PM CST
                           (364 days, 20 hours, 33 minutes, 36 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with ECDSA
Public Key Algorithm:  EC (secP256r1)
SHA-1 Fingerprint: 02:51:25:43:3e:68:f5:71:36:e3:5d:df:74:de:f6:a1:5a:db:0f:eb
SHA-256 Fingerprint:
1d:b5:eb:3c:f5:ff:bf:79:a2:a5:86:b8:e4:33:76:4d:d7:50:dc:a4:34:95:37:be:89:45:
86:1f:5d:79:c3:93

Successfully exported the following certificate to '/ds/server-cert.pem.2':
Subject DN:  CN=Example Root CA,O=Example Corp,C=US
Issuer DN:  CN=Example Root CA,O=Example Corp,C=US
Validity Start Time: Sunday, November 10, 2019 at 09:00:07 PM CST
                     (3 hours, 35 minutes, 39 seconds ago)
Validity End Time: Saturday, November 5, 2039 at 10:00:07 PM CDT
                   (7299 days, 20 hours, 24 minutes, 20 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with ECDSA
Public Key Algorithm:  EC (secP384r1)
SHA-1 Fingerprint: 0e:5c:21:c9:a5:36:0a:24:eb:aa:55:b6:a5:94:0e:e0:56:03:22:e6
SHA-256 Fingerprint:
   77:cf:66:d7:3c:8a:fd:67:2d:b7:36:fd:60:1d:ca:eb:1b:03:b1:12:7b:10:1f:26:
   05:b7:b9:0d:02:e0:38:3e
```

The `export-certificate` subcommand exports only the public portion of a certificate. Its private key is not included. To export the private key, use the `export-private-key` subcommand, which supports the following arguments, in addition to the usual key store and alias arguments:

* `--output-file {path}`

  Path to the file to which the exported private key is written. If this value is not provided, the key is written to standard output rather than a file.

* `--output-format {format}`

  Format in which the exported private key is written. The value can be `PEM` or `DER`, but the DER format is used only if the output is written to a file. Defaults to `PEM` if no value is specified.

The following code provides an example of the `export-private-key` subcommand .

```shell
$ bin/manage-certificates export-private-key \
     --keystore config/keystore \
     --keystore-password-file config/keystore.pin \
     --alias server-cert \
     --output-file server-cert-key.pem \
     --output-format PEM

Successfully exported the private key.
```

---

---
title: Generating certificate signing requests
description: A certificate signing request (CSR) contains all of the information that a certification authority requires to issue a certificate.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_generate_cert_signing_requests
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_generate_cert_signing_requests.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Generating certificate signing requests

A certificate signing request (CSR) contains all of the information that a certification authority requires to issue a certificate.

[RFC 2986](https://tools.ietf.org/rfc/rfc2986.txt) defines the request format, also known as PKCS #10, and includes the following elements:

* Certificate signing request version

* Requested subject distinguished name (DN) for the certificate

* Public key for the requested certificate

* Requested set of extensions for the certificate

* Signature that proves the requester has the private key for the given public key

To create a certificate signing request, use the `manage-certificates generate-certificate-signing-request` command, which performs the following steps:

1. Generated a public and private key pair.

2. Stores the key pair in a key store with a given alias.

3. Outputs the certificate signing request to the terminal.

4. Optionally writes the certificate signing request to a file.

Because a certificate signing request contains many of the same elements as a certificate, the command to generate one takes most of the same arguments as for generating a self-signed certificate. The following arguments are unavailable when generating a CSR:

* `--replace-existing-certificate`

* `--days-valid {number}`

* `--validity-start-time {timestamp}`

The following arguments are available when generating a certificate signing request but not when generating a self-signed certificate:

* `--output-file {path}`

  Path to a file to which the certificate signing request is written. If this value is not provided, the request is written only to the terminal in PEM form.

* `--output-format {value}`

  Format to use when writing the certificate signing request. This value can be `PEM` or `DER`, but the DER format is used only in conjunction with the `--output-file` argument. Defaults to `PEM` if the `--output-format {value}` argument is not provided.

* `--use-existing-key-pair`

  Indicates that the CSR uses a key pair that already exists in the key store with the given alias, rather than generating a new key pair, in which case the specified alias must not already be in use in the key store.

The following example command creates a CSR.

```
bin/manage-certificates generate-certificate-signing-request \
     --output-file ds1-cert.csr \
     --output-format PEM \
     --keystore config/keystore \
     --keystore-password-file config/keystore.pin \
     --keystore-type JKS \
     --alias server-cert \
     --subject-dn "CN=ds.example.com,O=Example Corp,C=US" \
     --key-algorithm EC \
     --key-length-bits 256 \
     --signature-algorithm SHA256withECDSA \
     --subject-alternative-name-dns ds.example.com \
     --subject-alternative-name-dns ds1.example.com \
     --subject-alternative-name-dns localhost \
     --subject-alternative-name-ip-address 1.2.3.4 \
     --subject-alternative-name-ip-address 127.0.0.1 \
     --subject-alternative-name-ip-address 0:0:0:0:0:0:0:1 \
     --key-usage digital-signature \
     --key-usage key-encipherment \
     --key-usage key-agreement \
     --extended-key-usage server-auth \
     --extended-key-usage client-auth

Successfully created a new JKS keystore.

Successfully generated the key pair to use for the certificate signing
request.

Successfully wrote the certificate signing request to file
'/ds/build/package/PingDirectory/ds1-cert.csr'.
```

If the contents of the resulting CSR file are made available to a certification authority to be signed, the resulting signed certificate can be imported into the key store.

To print the contents of a certificate signing request file, use the `display-certificate-signing-request-file` subcommand, which supports the following arguments:

* `--certificate-signing-request-file {path}`

  Path to the file that contains the certificate signing request to display.

* `--verbose`

  Indicates that the command is expected to display verbose information about the request, rather than a basic information set.

The following example demonstrates the basic output from the command.

```shell
$ bin/manage-certificates display-certificate-signing-request-file \
				--certificate-signing-request-file ds1-cert.csr

				PKCS #10 Certificate Signing Request Version:  v1
				Subject DN:  CN=ds.example.com,O=Example Corp,C=US
				Signature Algorithm:  SHA-256 with ECDSA
				Public Key Algorithm:  EC (secP256r1)
```

The following example demonstrates the verbose output.

```shell
$ bin/manage-certificates display-certificate-signing-request-file \
     --certificate-signing-request-file ds1-cert.csr \
     --verbose

PKCS #10 Certificate Signing Request Version:  v1
Subject DN:  CN=ds.example.com,O=Example Corp,C=US
Signature Algorithm:  SHA-256 with ECDSA
Signature Value:
     30:45:02:20:46:31:be:9e:6d:2f:0e:e3:d0:80:5c:88:ef:da:86:07:fd:15:b7:62:
     83:45:39:0a:c9:f2:f9:17:eb:08:94:ff:02:21:00:c8:bd:df:57:fa:ea:8c:04:
     df:c5:27:76:e5:b3:3b:4f:df:ec:d3:e4:09:5b:c0:6c:7b:86:39:ec:d0:0e:c1:64
Public Key Algorithm:  EC (secP256r1)
Elliptic Curve Public Key Is Compressed:  false
Elliptic Curve X-Coordinate:
   2086285379047579631978894716670982397622966387996624365020701122793024
   3221133
Elliptic Curve Y-Coordinate:
   479697739226644990505743464941788269420922508654777168408919906254139
   60212095
Certificate Extensions:
     Subject Key Identifier Extension:
          OID:  2.5.29.14
          Is Critical:  false
          Key Identifier:
               f2:de:fd:bf:d3:2f:96:ef:01:70:2d:0e:85:f5:fb:17:d5:a0:9e:67
     Subject Alternative Name Extension:
          OID:  2.5.29.17
          Is Critical:  false
          DNS Name:  ds.example.com
          DNS Name:  ds1.example.com
          DNS Name:  localhost
          IP Address:  1.2.3.4
          IP Address:  127.0.0.1
          IP Address:  0:0:0:0:0:0:0:1
     Key Usage Extension:
          OID:  2.5.29.15
          Is Critical:  false
          Key Usages:
               Digital Signature
               Key Encipherment
               Key Agreement
     Extended Key Usage Extension:
          OID:  2.5.29.37
          Is Critical:  false
          Key Purpose ID:  TLS Server Authentication
          Key Purpose ID:  TLS Client Authentication
```

---

---
title: Generating self-signed certificates
description: The process of creating a self-signed certificate is straightforward because a self-signed certificate claims itself as its own issuer.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_generate_self_signed_certs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_generate_self_signed_certs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  example: Example
---

# Generating self-signed certificates

The process of creating a self-signed certificate is straightforward because a self-signed certificate claims itself as its own issuer.

Although self-signed certificates are convenient for testing environments, clients do not trust them by default. Consequently, you should not use them as listener certificates in production environments.

The `manage-certificates` tool offers a `generate-self-signed-certificate` subcommand that can create a self-signed certificate. In addition to the arguments that provide information about the keystore, certificate alias, and optional private key password, the following arguments are available.

| Argument                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--subject-dn {subject}`                             | Subject DN for the certificate to create. This value is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `--days-valid {number}`                              | Number of days that the certificate remains valid. Defaults to `365` if no value is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--validity-start-time {timestamp}`                  | Indicates the time at which the certificate begins its validity window. This value is assumed to reflect the local time zone, and must be expressed in the form `YYYYMMDDhhmmss`, where a value of `20190102030405` indicates January 2, 2019, at 3:04:05 AM.Defaults to the current time if no value is specified.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `--key-algorithm {name}`                             | Name of the algorithm to use when generating the key pair. For a listener certificate, this value is typically `RSA` or `EC`.Defaults to `RSA` if no value is specified.&#xA;&#xA;This argument cannot be used in conjunction with the --replace-existing-certificate argument.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `--key-size-bits {number}`                           | Length of the key, in bits, to generate. If the `--key-algorithm` argument is given, then `--key-size-bits {number}` must also be specified. Conversely, if the `--replace-existing-certificate` argument is given, then `--key-size-bits {number}` must not be specified. Typical key sizes are:- RSA key – 2048 or 4096 bits If a default RSA key is used but this argument is not provided, a default key size of 2048 bits is used.

- Elliptic curve key – 256 or 384 bits                                                                                                                                                                                                                                                                            |
| `--signature-algorithm {name}`                       | Name of the algorithm to use to sign the certificate. If the `--key-algorithm` argument is used to specify an algorithm other than `RSA`, then `--signature-algorithm {name}` must also be specified.If the `--replace-existing-certificate` argument is used, then `--signature-algorithm {name}` must not be specified.Typical signature algorithms include `SHA256withRSA` for certificates with RSA keys, and `SHA256withECDSA` for certificates with elliptic curve keys. If a default key algorithm is used but the `--signature-algorithm {name}` argument is not provided, a default value of `SHA256withRSA` is used.                                                                                                                             |
| `--replace-existing-certificate`                     | Uses the new certificate to replace an existing certificate in the key store (within the same alias), and reuses the key for that certificate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `--inherit-extensions`                               | Indicates that, when replacing an existing certificate, the new certificate contains the same set of extensions as the existing certificate. If the `--replace-existing-certificate` argument is provided, but the `--inherit-extensions` argument is omitted, the new certificate contains only arguments that are provided explicitly.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `--subject-alternative-name-dns {name}`              | Indicates that the certificate is expected to have a subject alternative name extension with the provided DNS name. The given name must be fully qualified, although it can contain an asterisk (`*`) as a wildcard in the leftmost component.To include multiple DNS names in the subject alternative name extension, specify the `--subject-alternative-name-dns {name}` argument multiple times.                                                                                                                                                                                                                                                                                                                                                        |
| `--subject-alternative-name-ip-address {address}`    | Indicates that the certificate is expected to have a subject alternative name extension with the provided IP address. The given address must be a valid IPv4 or IPv6 address. No wildcards are allowed.To include multiple IP addresses in the subject alternative name extension, specify the `--subject-alternative-name-ip-address {address}` argument multiple times.                                                                                                                                                                                                                                                                                                                                                                                  |
| `--subject-alternative-name-email-address {address}` | Indicates that the certificate is expected to have a subject alternative name extension with the provided email address.To include multiple email addresses in the subject alternative name extension, specify the `--subject-alternative-name-email-address {address}` argument multiple times.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `--subject-alternative-name-uri {uri}`               | Indicates that the certificate is expected to have a subject alternative name extension with the provided URI.To include multiple URIs in the subject alternative name extension, specify the `--subject-alternative-name-uri {uri}` argument multiple times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `--subject-alternative-name-oid {oid}`               | Indicates that the certificate is expected to have a subject alternative name extension with the provided object identifier (OID). The given value must be a valid OID.To include multiple OIDs in the subject alternative name extension, specify the `--subject-alternative-name-oid {oid}` argument multiple times.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `--basic-constraints-is-ca {value}`                  | Indicates that the certificate is expected to have a basic constraints extension, with a specified value of `true` or `false`, for the flag indicating whether to consider the certificate a certification authority that can be used to sign other certificates.- For root and intermediate certificate authority (CA) certificates, the `--basic-constraints-is-ca {value}` argument must be present with a value of `true`.

- For end-entity certificates, the `--basic-constraints-is-ca {value}` argument can optionally be present with a value of `false`.

- For a self-signed certificate, specify the `--basic-constraints-is-ca {value}` argument with a value of `false` to indicate that the certificate is not considered a CA certificate. |
| `--basic-constraints-maximum-path-length {number}`   | Indicates that the basic constraints extension is expected to include a path length constraint element with the specified value. Use this argument only if `--basic-constraints-is-ca` is provided with a value of `true`.A path length constraint value of `0` indicates that the certificate can be used to issue only end-entity certificates. A path length constraint value of `1` indicates that the certificate can be used to sign end-entity certificates or intermediate CA certificates, the latter of which can be used to sign only end-entity certificates.A value greater than `1` indicates the presence of several intermediate CA certificates between it and the end-entity certificate at the head of the chain.                       |
| `--key-usage {value}`                                | Indicates that the certificate is expected to have a key usage extension with the specified value. The following values are allowed:- `digital-signature`

- `non-repudiation`

- `key-encipherment`

- `data-encipherment`

- `key-agreement`

- `key-cert-sign`

- `crl-sign`

- `encipher-only`

- `decipher-only`To include multiple key usages, specify the `--key-usage {value}` argument multiple times.                                                                                                                                                                                                                                                                                                                                            |
| `--extended-key-usage {value}`                       | Indicates that the certificate is expected to have an extended key usage extension with the specified value. The following values are allowed:- `server-auth`

- `client-auth`

- `code-signing`

- `email-protection`

- `time-stamping`

- `ocsp-signing`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Example

For example, the following command can be used to generate a self-signed server certificate.

```
bin/manage-certificates generate-self-signed-certificate \
     --keystore config/keystore \
     --keystore-password-file config/keystore.pin \
     --keystore-type JKS \
     --alias server-cert \
     --subject-dn "CN=ds.example.com,O=Example Corp,C=US" \
     --key-algorithm EC \
     --key-length-bits 256 \
     --signature-algorithm SHA256withECDSA \
     --subject-alternative-name-dns ds.example.com \
     --subject-alternative-name-dns ds1.example.com \
     --subject-alternative-name-dns localhost \
     --subject-alternative-name-ip-address 1.2.3.4 \
     --subject-alternative-name-ip-address 127.0.0.1 \
     --subject-alternative-name-ip-address 0:0:0:0:0:0:0:1 \
     --key-usage digital-signature \
     --key-usage key-encipherment \
     --key-usage key-agreement \
     --extended-key-usage server-auth \
     --extended-key-usage client-auth

Successfully created a new JKS keystore.

Successfully generated the following self-signed certificate:
Subject DN:  CN=ds.example.com,O=Example Corp,C=US
Issuer DN:  CN=ds.example.com,O=Example Corp,C=US
Validity Start Time: Monday, January 27, 2020 at 03:40:13 PM CST
                     (0 seconds ago)
Validity End Time: Tuesday, January 26, 2021 at 03:40:13 PM CST
                   (364 days, 23 hours, 59 minutes, 59 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with ECDSA
Public Key Algorithm:  EC (secP256r1)
SHA-1 Fingerprint: 4f:41:82:7f:08:e9:d8:05:8c:19:8b:3e:5b:bc:59:98:d3:15:71:3a
SHA-256 Fingerprint:
   76:e6:8e:c5:c8:8d:27:ce:2b:85:b9:8c:9d:49:3c:06:f4:40:f1:d0:70:67:39:24:fc:
   31:bc:f8:51:83:f2:42
```

---

---
title: Importing signed and trusted certificates
description: Use the manage-certificates import-certificate command to import certificates into a keystore.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_import_signed_trusted_certs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_import_signed_trusted_certs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# Importing signed and trusted certificates

Use the `manage-certificates import-certificate` command to import certificates into a keystore.

This command is used to accomplish the following tasks:

* Import a certificate that a certification authority has signed into the keystore in which the key pair was generated. In this scenario, the certificate is imported into a private key entry and must be imported as a certificate chain rather than an end-entity certificate.

* Import a trusted issuer certificate into a trust store. In this scenario, the certificate is imported into a trusted certificate entry as a single certificate instead of as a chain.

* Import a certificate chain, along with the private key for the end-entity certificate. This approach imports certificates that were generated through another library, like OpenSSL.

In addition to the arguments that provide information about the key store and the alias into which the certificate or certificate chain is imported, the `manage-certificates import-certificate` command accepts the following arguments:

* `--certificate-file {path}`

  Path to the file that contains the certificate to import. The certificate can be in PEM or DER format and can be a single certificate or a certificate chain. If the certificates in the chain reside in separate files, specify the `--certificate-file {path}` argument multiple times when you import a certificate chain.

* `--private-key-file {path}`

  Path to the file containing the private key that corresponds to the certificate at the head of the imported chain. The private key can be in PEM or DER format.

* `--no-prompt`

  Indicates that the certificate is to be imported without prompting for confirmation. By default, a summary of the certificate is displayed, and you must confirm that you want to import it.

The following example command imports a signed certificate into the key store that generates the certificate signing request.

```shell
$ bin/manage-certificates import-certificate \
     --keystore config/keystore \
     --keystore-password-file config/keystore.pin \
     --alias server-cert \
     --certificate-file ds1-cert.pem \
     --certificate-file ca-cert.pem

The following certificate chain will be imported into the keystore into alias
'server-cert', preserving the existing private key associated with that alias:

Subject DN:  CN=ds.example.com,O=Example Corp,C=US
Issuer DN:  CN=Example Root CA,O=Example Corp,C=US
Validity Start Time: Sunday, November 10, 2019 at 09:09:23 PM CST
                     (4 minutes, 16 seconds ago)
Validity End Time: Monday, November 9, 2020 at 09:09:23 PM CST
                   (364 days, 23 hours, 55 minutes, 43 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with ECDSA
Public Key Algorithm:  EC (secP256r1)
SHA-1 Fingerprint: 02:51:25:43:3e:68:f5:71:36:e3:5d:df:74:de:f6:a1:5a:db:0f:eb
SHA-256 Fingerprint: 1d:b5:eb:3c:f5:ff:bf:79:a2:a5:86:b8:e4:33:76:4d:d7:
                     50:dc:a4:34:95:37:be:89:45:86:1f:5d:79:c3:93

Subject DN:  CN=Example Root CA,O=Example Corp,C=US
Issuer DN:  CN=Example Root CA,O=Example Corp,C=US
Validity Start Time: Sunday, November 10, 2019 at 09:00:07 PM CST
                     (13 minutes, 32 seconds ago)
Validity End Time: Saturday, November 5, 2039 at 10:00:07 PM CDT
                   (7299 days, 23 hours, 46 minutes, 27 seconds from now)
Validity State:  The certificate is currently within the validity window.
Signature Algorithm:  SHA-256 with ECDSA
Public Key Algorithm:  EC (secP384r1)
SHA-1 Fingerprint: 0e:5c:21:c9:a5:36:0a:24:eb:aa:55:b6:a5:94:0e:e0:56:03:22:e6
SHA-256 Fingerprint: 77:cf:66:d7:3c:8a:fd:67:2d:b7:36:fd:60:1d:ca:eb:1b:03:b1:
                     12:7b:10:1f:26:05:b7:b9:0d:02:e0:38:3e

Do you want to import this certificate chain into the keystore? yes

Successfully imported the certificate chain.
```

If you do not provide the `--no-prompt` argument, the `manage-certificates import-certificate` tool still displays information about the certificates to import. To view additional information about a certificate before you import it, use the `display-certificate-file` subcommand, which supports the following arguments:

* `--certificate-file {path}`

  Path to the file that contains the certificate to view.

* `--verbose`

  Displays verbose information about the certificate.

The output of the `display-certificate-file` subcommand has the same format and content as the `list-certificates` subcommand.

---

---
title: Inter-server certificates
description: Each server instance in a topology has an inter-server certificate that is generated during the setup process.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_inter_server_certificates
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_inter_server_certificates.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
---

# Inter-server certificates

Each server instance in a topology has an inter-server certificate that is generated during the setup process.

The inter-server certificate is not exposed to clients, so a trusted issuer does not need to sign it. Instead, the topology registry, representing a mirrored portion of the configuration with information about every PingDirectory server instance in the environment, contains the information that each instance needs to trust the inter-server certificates for all other instances.

Inter-server certificates can be used to protect certain secrets that are shared among servers within the topology, like the secrets that are used to digitally sign log files, backups, and LDIF exports. Inter-server certificates include the encryption keys that reversible password-storage schemes use.

The inter-server certificate is generated with a long lifespan. Replace it only when you suspect that its private key is compromised.

---

---
title: Key agreement
description: Key agreement processing provides a critical component of TLS negotiation.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_key_agreement
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_key_agreement.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Key agreement

Key agreement processing provides a critical component of TLS negotiation.

It allows the client and server to select the symmetric key that encrypts the remainder of the communication, but does not reveal the key to anyone who can access the communication. Although several key agreement algorithms are available, the following types are the most common:

* RSA key exchange

  The client generates random data, uses the server's public key to encrypt it, and provides it to the server, which uses its private key to decrypt it. The client and server alike derive the encryption key from the randomly generated data.

* Diffie-Hellman (DH) key exchange

  The client and server agree publicly on a pair of mathematically linked numbers, and each participant chooses its own secret value. Through a special computation, they generate a key that can be discovered only by someone who knows one of the secret values. Although several variants of the Diffie-Hellman algorithm can be used in key exchange, we recommend the ECHDE and DHE versions because they use ephemeral keys with no relation to the server's certificate. Of those two versions, ECDHE is faster and uses smaller keys.

When possible, use ECHDE over DHE, and either of those options over RSA. The DH algorithms provide a substantial benefit over RSA in the form of forward secrecy. Because RSA key exchange uses the server certificate's public key to encrypt data, the encryption can be broken if the certificate's private key is compromised. This warning applies to previously captured data as well as to communication on new TLS connections. The use of ephemeral keys in ECDHE and DHE ensures that, even if the certificate's private key is compromised, the encrypted communication remains indecipherable to anyone but the client and server, although anyone with the private key can still impersonate the legitimate server.

---

---
title: Keystores and truststores
description: A keystore is a type of database that holds certificates.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_keystores_truststores
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_keystores_truststores.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
---

# Keystores and truststores

A keystore is a type of database that holds certificates.

The following examples represent the most common forms of keystores:

* File that uses the Java-specific Java KeyStore (JKS) format

* File that uses the standard PKCS #12 format

* Collection of files that holds certificates and private keys, typically in PEM or DER format

* Hardware security module (HSM) that makes the certificate information available through an interface like PKCS #11

The server supports file-based keystores by using the JKS and PKCS #12 formats and by using hardware security modules that are accessible through PKCS #11. The server does not currently support a keystore format that consists of individual certificate and private key files. To import these files into a JKS or PKCS #12 keystore, use the `manage-certificates` tool.

A keystore also represents a collection of entries, each of which is identified by a name that an alias calls. Keystores can have the following entry types:

* Private key entries

  Contain a certificate chain and a private key. When a server accepts a TLS-based connection, it uses a private key entry to obtain the certificate chain that it presents to the client. The server can also use the private key from the same entry to process its key agreement. Similarly, a client uses a private key entry when presenting its own certificate chain to a server.

* Trusted certificate entries

  Contain a single certificate without a private key. As the name implies, a trusted certificate entry is intended primarily for use when determining whether to trust a certificate chain that is presented during TLS negotiation.

* Secret key entries

  Contain a secret key only, without an associated certificate. These types of entries are not used for TLS processing. Instead, they hold symmetric encryption keys or other types of secrets.

A password, sometimes called a PIN, protects the contents of a keystore. In some cases, like with JKS keystores, some content might be accessible without a password, and a password might be required only when trying to access private keys or secret keys. In other cases, like with PKCS #12 keystores, you might need a password for any interaction with the keystore.

Additional passwords can further protect private keys. This approach is often the same as with the keystore password, but the password can be different. This tactic is useful when a single keystore is shared for multiple purposes, for example, and when merely having access to the keystore does not guarantee access to all of the data that it contains.

|   |                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A truststore is another name for a keystore that is intended primarily for use when determining whether to trust a certificate chain that has been presented. Truststores generally contain primarily trusted certificate entries, but that case is not required. |

Java runtime environments typically include a default truststore, often `jre/lib/security/cacerts` or `lib/security/cacerts`, that is pre-populated with several widely trusted certification authority certificates. When presented with a certificate that one of these authorities has signed, the default truststore can allow the certificate to be trusted without any additional configuration. When presented with a self-signed certificate, or when presented with a certificate that is signed by an issuer not in the default truststore, such as a private corporate certification authority, a separate truststore is required.

---

---
title: LDAP StartTLS extended operation
description: In most scenarios, a client that uses TLS establishes a connection to a port that is dedicated to its use, like 636 (LDAPS) or 443 (HTTPS).
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_ldap_starttls_extended_operation
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_ldap_starttls_extended_operation.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# LDAP StartTLS extended operation

In most scenarios, a client that uses TLS establishes a connection to a port that is dedicated to its use, like 636 (LDAPS) or 443 (HTTPS).

The client begins the TLS-negotiation process by sending a `client hello` message over the connection. In some scenarios, the client establishes a non-secure connection and later converts it to a secure one. In LDAP, this task is accomplished by using the `StartTLS` extended operation.

The `StartTLS` extended operation provides the following advantages over a dedicated LDAPS connection:

* To enable secure as well as insecure communication, only one port needs to be opened through a firewall.

* A client can use opportunistic encryption, in which the client performs the following steps:

  1. Queries the root DSE to determine whether the server supports StartTLS.

  2. Secures the connection, if possible.

  Opportunistic encryption is useful in scenarios like following referrals because LDAP URLs do not officially support LDAPS as a scheme.

To ensure that a communication is always secure, use LDAPS instead of establishing an insecure connection that you secure later with the `StartTLS` extended operation. If you enable support for unencrypted LDAP communication, as `StartTLS` requires, a client might send a password-containing bind request or other sensitive data over an unencrypted connection. A server can be configured to reject unencrypted communication, but it cannot prevent a client from sending an unencrypted request.

|   |                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although you can use `StartTLS` to temporarily secure a connection before falling back on an unencrypted LDAP communication, the server does not support this strategy. |

---

---
title: ldapsearch
description: The ldapsearch command-line utility is a powerful tool for issuing searches against an LDAP directory server. It also provides a convenient method for troubleshooting a variety of issues, including problems that are relevant to TLS communication.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_ldapsearch
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_ldapsearch.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  example: Example
  trust-stores-and-trust-related-arguments: Trust stores and trust-related arguments
  example-2: Example
  client-certificate-chains-and-key-stores: Client certificate chains and key stores
  example-3: Example
  if-you-need-to-further-troubleshoot-a-tls-related-issue: If you need to further troubleshoot a TLS-related issue
---

# ldapsearch

The `ldapsearch` command-line utility is a powerful tool for issuing searches against an LDAP directory server. It also provides a convenient method for troubleshooting a variety of issues, including problems that are relevant to TLS communication.

The following table details arguments that are the most useful for TLS-related communication.

**TLS-related communication arguments and their descriptions**

| Argument                          | Description                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--hostname {address}`            | Address of the server to which the connection is established                                                                                                                                                                                                                                                                                                                          |
| `--port {port}`                   | TCP port of the server to which the connection is established. The standard port for non-secure LDAP, or LDAP to be secured with StartTLS, is `389`, and the standard port for secure LDAPS is `636`. Many deployments use alternate ports, especially non-privileged ports above `1024`.                                                                                             |
| `--useSSL`                        | The tool establishes an initially insecure LDAP connection, which is secured later with the StartTLS extended operation.                                                                                                                                                                                                                                                              |
| `--trustStorePath {path}`         | Path to the trust store that is used when determining whether to trust the certificate chain that the server presents during TLS negotiation. If neither this argument nor the `--trustAll` argument is provided, the tool prompts you interactively whether to trust server certificates that are not signed by an issuer in the Java virtual machine's (JVM's) default trust store. |
| `--trustStoreFormat {format}`     | Format for the trust store, which is typically `JKS` or `PKCS12`.                                                                                                                                                                                                                                                                                                                     |
| `--trustStorePassword {password}` | Password that is required to access the contents of the trust store.                                                                                                                                                                                                                                                                                                                  |
| `--trustStorePasswordFile {path}` | Path to the file that contains the password that is required to access the contents of the trust store.                                                                                                                                                                                                                                                                               |
| `--trustAll`                      | The tool blindly trusts all TLS certificate chains that are presented to it. Although this argument can prove useful for troubleshooting purposes, it is not recommended for general use.                                                                                                                                                                                             |
| `--keyStorePath {path}`           | Path to the key store to use if a client certificate chain is presented to the server.&#xA;&#xA;Use this argument only when one of the following conditions is satisfied:&#xA;&#xA;The server is configured to require clients to present a certificate.&#xA;&#xA;You intend to use the certificate to authenticate through SASL EXTERNAL.                                            |
| `--keyStoreFormat {format}`       | Format for the key store, which is typically `JKS` or `PKCS12`.                                                                                                                                                                                                                                                                                                                       |
| `--keyStorePassword {password}`   | Password to access the key store.                                                                                                                                                                                                                                                                                                                                                     |
| `--keyStorePasswordFile {path}`   | Path to the file that contains the password necessary to access the key store.                                                                                                                                                                                                                                                                                                        |
| `--certNickname {alias}`          | Alias of the private key entry in the key store. Use when obtaining the certificate chain to present to the server.                                                                                                                                                                                                                                                                   |
| `--useSASLExternal`               | The client authenticates with the EXTERNAL SASL mechanism, which typically identifies the client using the certificate chain that is presented during TLS negotiation.                                                                                                                                                                                                                |
| `--enableSSLDebugging`            | The tool activates the low-level TLS-debugging feature that the JVM provides.                                                                                                                                                                                                                                                                                                         |

The following command provides an example of the simplest method for testing TLS communication with the PingDirectory server.

## Example

```shell
$ bin/ldapsearch \
     --hostname ds1.example.com \
     --port 636 \
     --useSSL \
     --baseDN "" \
     --scope base \
     "(objectClass=*)"
The server presented the following certificate chain:

     Subject: CN=ds1.example.com,O=Example Corp,C=US
     Valid From: Tuesday, November 12, 2019 at 08:28:08 PM CST
     Valid Until: Wednesday, November 11, 2020 at 08:28:08 PM CST
     SHA-1 Fingerprint:
        6a:22:2a:bd:0b:1b:09:35:63:bc:12:3e:2c:9e:e7:70:bc:a4:73:de
     256-bit SHA-2 Fingerprint:
        7a:8c:e4:76:d4:47:15:fd:65:f5:26:0e:d2:55:77:d7:03:7a:e6:79:9f:bc:
        ae:93:2c:76:9c:01:fc:ef:15:38
     -
     Issuer 1 Subject: CN=Example Intermediate CA,O=Example Corp,C=US
     Valid From: Tuesday, November 12, 2019 at 08:28:06 PM CST
     Valid Until: Monday, November 7, 2039 at 08:28:06 PM CST
     SHA-1 Fingerprint: 01:b3:70:8b:6c:11:43:87:3b:e9:bb:73:27:99:ea:fd:08:c4:db:ec
     256-bit SHA-2 Fingerprint: 49:60:69:df:33:9d:26:d0:66:c9:6d:7b:0b:cb:3b:96:
                                40:22:dc:6d:11:32:b7:c0:30:47:d6:7c:6a:19:cd:60
     -
     Issuer 2 Subject: CN=Example Root CA,O=Example Corp,C=US
     Valid From: Tuesday, November 12, 2019 at 08:28:03 PM CST
     Valid Until: Monday, November 7, 2039 at 08:28:03 PM CST
     SHA-1 Fingerprint: b4:83:55:db:82:e4:63:5c:3a:44:13:8f:88:44:e3:60:f2:53:80:48
     256-bit SHA-2 Fingerprint:
        e8:af:6f:ed:b9:0e:df:94:9c:20:29:53:a9:74:44:a9:17:b4:08:65:c8:19:c1:fb:
        34:34:a1:90:83:8a:d5:12

Do you wish to trust this certificate?  Enter 'y' or 'n': y
dn:
objectClass: top
objectClass: ds-root-dse
startupUUID: 8d574122-4584-4522-96d9-0cdcb9d2e339
startTime: 20191113061149Z

# Result Code:  0 (success)
# Number of Entries Returned:  1
```

## Trust stores and trust-related arguments

If no trust-related arguments are provided, the tool uses the JVM's default trust store to verify whether to trust the certificate chain, based on the information that it contains. If a trusted authority has signed the server certificate, the negotiation process continues without further interaction.

If the chain cannot be trusted, based on the information in the JVM-default trust store, `ldapsearch` prompts you interactively about whether to trust the certificate. If you accept the chain, the client and server complete the negotiation process, and the client sends the search request to the server. If the search succeeds, the server can communicate over TLS.

To test with a trust store instead of being prompted interactively, use the `--trustStorePath` argument that points to the appropriate trust store. If you are using a Java Keystore (JKS) trust store, you might not need to provide the trust store password. If you are using a PKCS #12 trust store, you need to provide the trust store password. The following code provides an example.

## Example

```shell
$ bin/ldapsearch \
     --hostname ds1.example.com \
     --port 636 \
     --useSSL \
     --trustStorePath config/truststore.p12 \
     --trustStorePasswordFile config/truststore.pin \
     --trustStoreFormat PKCS12 \
     --baseDN "" \
     --scope base \
     "(objectClass=*)"
dn:
objectClass: top
objectClass: ds-root-dse
startupUUID: c8724159-8c37-45eb-b210-879bfcf74ad6
startTime: 20191113154023Z

# Result Code:  0 (success)
# Number of Entries Returned:  1
```

## Client certificate chains and key stores

To present a client certificate chain to the server, either because the server's connection handler is configured with an `ssl-client-auth-policy` value of `required` or because you plan to use the certificate to authenticate by way of the SASL EXTERNAL mechanism, provide at least the key store and its corresponding password. You can also specify the alias of the certificate chain to present, which is recommended if your client key store contains multiple certificates. The following code provides an example.

## Example

```shell
$ bin/ldapsearch \
     --hostname ds1.example.com \
     --port 636 \
     --useSSL \
     --trustStorePath config/truststore.p12 \
     --trustStorePasswordFile config/truststore.pin \
     --trustStoreFormat PKCS12 \
     --keyStorePath client-keystore \
     --keyStorePasswordFile client-keystore.pin \
     --certNickname client-cert \
     --useSASLExternal \
     --baseDN "" \
     --scope base \
     "(objectClass=*)"
dn:
objectClass: top
objectClass: ds-root-dse
startupUUID: c8724159-8c37-45eb-b210-879bfcf74ad6
startTime: 20191113154023Z

# Result Code:  0 (success)
# Number of Entries Returned:  1
```

## If you need to further troubleshoot a TLS-related issue

If you encounter a TLS-related issue that you cannot resolve by examining the `ldapsearch` output or the server logs, use the `--enableSSLDebugging` option to enable the JVM's support for low-level debugging of TLS processing. For more information, see [Using low-level TLS debugging](pd_ds_low_level_tls_debugging.html).
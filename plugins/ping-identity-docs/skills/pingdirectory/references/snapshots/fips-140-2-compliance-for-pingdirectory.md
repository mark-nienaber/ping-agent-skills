---
title: Comparison of FIPS-compliant and non-FIPS-compliant modes
description: Servers running in FIPS-compliant mode and servers running in non-FIPS-compliant mode differ and have certain incompatibilities.
component: pingdirectory
version: 11.1
page_id: pingdirectory:fips_140-2_compliance_for_pingdirectory:pd_met_diff_fips_compliant_non_compliant
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/fips_140-2_compliance_for_pingdirectory/pd_met_diff_fips_compliant_non_compliant.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  incompatibilities-between-fips-compliant-and-non-fips-compliant-servers: Incompatibilities between FIPS-compliant and non-FIPS-compliant servers
  changes-in-supported-key-store-types: Changes in supported key store types
  tls-for-network-communication: TLS for network communication
  data-encryption: Data encryption
  strong-administrative-passwords: Strong administrative passwords
  reduced-available-password-storage-schemes-in-fips-compliant-mode: Reduced available password storage schemes in FIPS-compliant mode
  reduced-available-sasl-mechanisms: Reduced available SASL mechanisms
---

# Comparison of FIPS-compliant and non-FIPS-compliant modes

Servers running in FIPS-compliant mode and servers running in non-FIPS-compliant mode differ and have certain incompatibilities.

Some of these are incompatibilities imposed by the specification or the Bouncy Castle FIPS provider. Others allow for better out-of-the-box security in a manner that isn't possible without breaking backward compatibility with existing deployments.

## Incompatibilities between FIPS-compliant and non-FIPS-compliant servers

Although the server doesn't have any known substantial cryptographic issues when running in the default non-FIPS-compliant mode, some of the algorithms it uses are either not permitted by the FIPS specification or aren't allowed by the Bouncy Castle FIPS provider.

To preserve backward compatibility with earlier versions, the server still uses those same algorithms when operating in non-FIPS-compliant mode, however it uses a different set of algorithms when set up in FIPS-compliant mode.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although this shouldn't substantially impact compatibility with clients, it does mean that servers running in FIPS-compliant mode cannot participate in the same topology as servers running in non-FIPS-compliant mode, nor is it possible to directly replicate between servers running in FIPS-compliant mode and servers running in non-FIPS-compliant mode.It's also not possible to update or reconfigure an existing server running in non-FIPS-compliant mode to operate in FIPS-compliant mode. |

To migrate an existing non-FIPS-compliant topology to one operating in FIPS-compliant mode, you must:

1. Create a second topology in which the servers are set up in FIPS-compliant mode.

2. Migrate the data to the new topology.

3. Start serving client requests from that new topology.

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although you can't replicate data directly between FIPS-compliant and non-FIPS-compliant instances, the PingDataSync server supports synchronizing changes between the topologies. |

|   |                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're not using automatic backend server discovery for both types of servers, the PingDirectoryProxy server can forward requests to a mix of FIPS-compliant and non-FIPS-compliant servers. This allows you to migrate from one topology to another in a manner that's transparent to clients. |

## Changes in supported key store types

The server uses key stores to hold certificates needed for TLS negotiation and authentication. Historically, it supported the Java KeyStore (JKS) and PKCS #12 (a standard format described in [RFC 7292](https://www.ietf.org/rfc/rfc7292.txt)) file-based key store types. However, these key store types could use cryptographic algorithms that aren't permitted in FIPS-compliant mode. Instead, use the Bouncy Castle FIPS-compliant Key Store (BCFKS) format. BCFKS is similar to PKCS #12 but relies only on cryptographic algorithms that are allowed by the Bouncy Castle FIPS provider in approved-only mode.

The `manage-certificates` tool has been updated to provide support for BCFKS key store types. For servers operating in non-FIPS-compliant mode, it can interact with any of the JKS, PKCS #12 or BCFKS key store types, and the `copy-keystore` subcommand is used to convert a JKS or PKCS #12 key store to a BCFKS key store.

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | For servers operating in FIPS-compliant mode, only the BCFKS key store format is allowed. |

The server also supports the standard PKCS #11 cryptographic API that can be used to interact with tokens like hardware security modules (HSMs). PKCS #11 tokens can be used in either FIPS-compliant mode or non-FIPS-compliant mode, however you should use a FIPS-compliant HSM when running in FIPS-compliant mode. The `manage-certificates` tool also supports interacting with PKCS #11 tokens.

## TLS for network communication

When running in non-FIPS-compliant mode, you can configure the server to accept only encrypted, only unencrypted, or a mix of encrypted and unencrypted network communication.

When setting up the server in FIPS-compliant mode, you must enable TLS encryption. Unencrypted communication won't be enabled. The server can optionally accept connections that are initially unencrypted, but the StartTLS extended request must be used to secure communication on those connections before other types of requests are allowed.

Because secure communication is required, you must configure the server with appropriate certificate key and trust stores during setup. Learn more in [Setting up certificate key and trust stores](pd_met_set_up_server_fips_compliant_mode.html#fips_key_trust).

## Data encryption

Using data encryption to protect data at rest is optional in non-FIPS-compliant mode but is required when setting up the server in FIPS-compliant mode.

You must configure the server with at least one encryption settings definition. Learn more in [Setting up data encryption](pd_met_set_up_server_fips_compliant_mode.html#fips_data_encrypt).

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When creating an encryption settings definition from a passphrase (whether user-supplied or automatically generated), servers running in non-FIPS-compliant mode default to using a 128-bit AES encryption key. When setting up a server in FIPS-compliant mode, `setup` uses a 256-bit AES encryption key. |

## Strong administrative passwords

When setting up the server in non-FIPS-compliant mode, you should choose a strong password for the initial root user that conforms to the following requirements:

* The password must be at least 12 characters long.

* The password must not be contained in a dictionary of words from a variety of languages.

* The password must not be contained in a dictionary of commonly used passwords.

In non-FIPS-compliant mode, you can ignore those rules and choose a weaker password through the `--allowWeakRootUserPassword` argument. You can't use this argument when setting up the server in FIPS-compliant mode, and you will be required to provide what the server considers a strong password.

The minimum password length requirement is increased from 12 characters to 14 characters because this is the minimum length required by the Bouncy Castle FIPS-compliant PBKDF2 implementation when running in approved-only mode.

## Reduced available password storage schemes in FIPS-compliant mode

More password storage schemes are available in the out-of-the-box configuration when setting up a server in non-FIPS-compliant mode than in FIPS-compliant mode.

The only schemes available in the out-of-the-box configuration for a FIPS-compliant server are:

* AES256

* PBKDF2

* SSHA256

* SSHA384

* SSHA512

The PBKDF2 password storage scheme is the default scheme for root users and topology administrators. The SSHA256 password scheme is the default scheme for non-administrative users.

|   |                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In FIPS-compliant mode, the server defaults to the PBKDF2WithHmacSHA256 algorithm rather than PBKDF2WithHmacSHA1, which is used by default for backwards compatibility in non-FIPS-compliant mode. The SSHA256, SSHA384, and SSHA512 schemes use a default salt length of 128 bits in FIPS-compliant mode as opposed to the default length of 64 bits in non-FIPS-compliant mode. |

The following password storage schemes aren't available in FIPS-compliant mode because they depend on the non-FIPS-compliant Bouncy Castle library, which is not compatible with the FIPS-compliant library:

* ARGON2

* BCRYPT

* SCRYPT

The following schemes are available in the default configuration for non-FIPS-compliant mode for the purpose of backward compatibility and are excluded from the out-of-the-box configuration for a FIPS-compliant server:

* AES

* BASE64

* BLOWFISH

* CLEAR

* CRYPT

* MD5

* SHA

* SMD5

* SSHA

|   |                                                                          |
| - | ------------------------------------------------------------------------ |
|   | You should avoid using these password storage schemes whenever possible. |

## Reduced available SASL mechanisms

When running in non-FIPS-compliant mode, the server has some non-recommended Simple Authentication and Security Layer (SASL) mechanisms available in the out-of-the-box configuration for purposes of backward compatibility that aren't included in the FIPS-compliant mode default configuration.

These mechanisms include:

* ANONYMOUS

* CRAM-MD5

* DIGEST-MD5

---

---
title: FIPS Compliance for PingDirectory
description: The Federal Risk and Authorization Management Program (FedRAMP) could require that United States government agencies and organizations that work with those agencies ensure that their cloud-based services adhere to either the FIPS 140-2 or FIPS 140-3 specification. These specifications define requirements for cryptographic processing.
component: pingdirectory
version: 11.1
page_id: pingdirectory:fips_140-2_compliance_for_pingdirectory:pd_fips_compliance
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/fips_140-2_compliance_for_pingdirectory/pd_fips_compliance.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_met_intro_fips_compliance.adoc"]
---

# FIPS Compliance for PingDirectory

The [Federal Risk and Authorization Management Program](https://www.fedramp.gov/) (FedRAMP) could require that United States government agencies and organizations that work with those agencies ensure that their cloud-based services adhere to either the [FIPS 140-2](https://csrc.nist.gov/pubs/fips/140-2/upd2/final) or [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) specification. These specifications define requirements for cryptographic processing.

The PingDirectory, PingDirectoryProxy, and PingDataSync servers support running in FIPS-compliant mode using either the FIPS 140-2 or FIPS 140-3 specification.

When setting up in FIPS-compliant mode, the server uses the [Bouncy Castle FIPS Java API](https://www.bouncycastle.org/fips-java/) in approved-only mode, which rejects attempts to use non-FIPS-compliant cryptography.

---

---
title: Setting up the server in FIPS-compliant mode
description: You can't have both FIPS-compliant and non-FIPS-compliant servers in the same topology, and you can't update an existing non-FIPS-compliant server to run in FIPS-compliant mode.
component: pingdirectory
version: 11.1
page_id: pingdirectory:fips_140-2_compliance_for_pingdirectory:pd_met_set_up_server_fips_compliant_mode
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/fips_140-2_compliance_for_pingdirectory/pd_met_set_up_server_fips_compliant_mode.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_fips_ensure_sufficient_entropy.adoc", "pd_fips_resolve_entropy_exhaustion.adoc", "pd_fips_set_up_cert_key_trust_stores.adoc", "pd_fips_set_up_data_encryption.adoc", "pd_fips_install_server_fips140_2_compliant_mode.adoc"]
section_ids:
  ensure-sufficient-entropy: Ensure sufficient entropy
  resolve-entropy-exhaustion: Resolve entropy exhaustion
  fips_key_trust: Setting up certificate key and trust stores
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  fips_data_encrypt: Setting up data encryption
  about-this-task-2: About this task
  steps-2: Steps
  choose-from-2: Choose from:
  installing-the-server-in-fips-compliant-mode: Installing the server in FIPS-compliant mode
  about-this-task-3: About this task
  steps-3: Steps
  choose-from-3: Choose from:
  example: Example:
  check_FIPS_level: Checking the level of FIPS compliance
  about-this-task-4: About this task
  steps-4: Steps
  example-2: Example:
  changing-the-level-of-fips-compliance: Changing the level of FIPS compliance
  about-this-task-5: About this task
  before-you-begin: Before you begin
  steps-5: Steps
  choose-from-4: Choose from:
  troubleshooting: Troubleshooting:
---

# Setting up the server in FIPS-compliant mode

You can't have both FIPS-compliant and non-FIPS-compliant servers in the same topology, and you can't update an existing non-FIPS-compliant server to run in FIPS-compliant mode.

Because of this, if you want to run a server in FIPS-compliant mode, you must set up a new instance. This can be done in the following two ways:

* Use `setup` with an appropriate set of arguments.

* Use `manage-profile setup` with a profile that includes the necessary setup arguments, along with any other configuration changes, extensions, and other files that you might want included in the installation.

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | You can run servers with different levels of FIPS compliance in the same topology. |

## Ensure sufficient entropy

Strong cryptography requires a reliable source of high-quality random data.

On some systems, the OS-provided random number generator, such as `/dev/random` on Linux systems, might block if there's not enough entropy available to keep up with the demand for strong random data, which can severely impede server performance. This is especially likely when running the server in a virtual machine or in a container because it's less likely to have access to the entropy stream from the underlying host system.

When running in non-FIPS-compliant mode, the server can work around this problem by using an alternative random number generator, such as `/dev/urandom` on Linux, that uses cryptographic techniques to ensure that it can still provide a high-quality stream of random data that won't block even when available entropy is exhausted on the underlying system. However, the Bouncy Castle FIPS-compliant random number generator doesn't support this alternative, and it's likely to block for long periods of time if the server is installed in a container or virtual machine.

This isn't a problem that's likely to go unnoticed because the server is likely to appear completely unresponsive for many minutes at a time if the random number generator blocks because of a lack of entropy. It's likely to block for long periods of time, especially if the server is installed in a container or virtual machine.

## Resolve entropy exhaustion

To help diagnose the problem, the installer attempts to monitor available system entropy when setting up the server in FIPS-compliant mode and displays a warning message if entropy drops too low. Similarly, if the server is running in FIPS-compliant mode, it continuously monitors available system entropy and logs a warning message and raises an alarm if entropy drops low enough that the server is likely to become unresponsive.

If entropy exhaustion is a problem, the best options to address it include:

* If the server is running in a virtual machine or container, you might be able to configure it with access to the underlying host system's entropy pool if that's not already the case.

* Install a hardware random number generator on the system and ensure that the server can access it even when running in a container or virtual machine.

* Install an entropy-supplementing daemon, such as [rngd](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/security_guide/sect-security_guide-encryption-using_the_random_number_generator), to keep the OS-provided random number generator topped off and able to generate high-quality random data without blocking.

## Setting up certificate key and trust stores

### About this task

Because FIPS-compliant mode requires secure communication, you must provide arguments that indicate how the server should obtain the certificate chain, private key, and trusted certificate information that it should use during TLS negotiation.

### Steps

* Configure the server with appropriate key and trust stores during setup.

  #### Choose from:

  * If you have existing key and trust stores in the BCFKS format:

    * Use the `--useBCFKSKeyStore` and `--useBCFKSTrustStore` arguments to provide the paths to those stores.

    * Use either the `--keyStorePassword` or `--keyStorePasswordFile` argument to specify the PIN needed to access the contents of the key store.

    * Use either the `--trustStorePassword` or `--trustStorePasswordFile` argument to specify the PIN needed to access the contents of the trust store.

      |   |                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------- |
      |   | Unlike the JKS format, a PIN is always required when using a BCFKS key store, even if you don't need to access the private key. |

  * If you have existing key and trust stores in a non-BCFKS format:

    * Convert the non-BCFKS files using `manage-certificates copy-keystore` with the `--destination-key-store-type BCFKS` argument.

    * Follow the steps for existing key and trust stores in the BCFKS format.

  * If you have PEM files containing the certificate chain and private key from a certificate authority, and you want to use them to generate new BCFKS key and trust stores:

    * Use the `--certificateChainPEMFile` and `--certificatePrivateKeyPEMFile` arguments to specify the paths to those files.

    * If you have PEM files containing trusted certificates that you want to include in a new BCFKS trust store, you can use the `--trustedCertificatePEMFile` argument to provide the paths to those files.

  * If the listener certificate chain and private key that you want to use reside in a PKCS #11 token:

    * Use the `--usePKCS11KeyStore` argument to enable that support for creating a BCFKS key store.

      |   |                                                                                                                                                                                                                                              |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | PingDirectory only supports key store creation using PKCS #11 tokens. In order to create a trust store, you must use either the `--useBCFKSTrustStore` or `--trustedCertificatePEMFile` arguments in conjunction with `--usePKCS11KeyStore`. |

    * If the Java virtual machine (JVM) has not been pre-configured with the necessary PKCS #11 provider, then use the `--pkcs11ProviderConfigFile` argument to specify the path to the necessary provider configuration file.

    * Use either the `--keyStorePassword` or `--keyStorePasswordFile` argument to specify the PIN needed to access the token.

  * If you want the server to generate a self-signed certificate and use it to create BCFKS key and trust stores, use the `--generateSelfSignedCertificate` argument.

    |   |                                                                                                                                                                                   |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Self-signed certificates are convenient for testing or evaluation purposes, but they aren't trusted by any clients (by default) and shouldn't be used in production environments. |

## Setting up data encryption

### About this task

Setting up the server in FIPS-compliant mode requires that you enable data encryption.

### Steps

* Configure the server with at least one encryption settings definition.

  #### Choose from:

  * If you want the server to generate an encryption settings definition from a passphrase that you provide, use the `--encryptDataWithPassphraseFromFile` argument to specify the path to a file containing that passphrase.

    |   |                                                                                                                                                                                                                                                                                                                                                                              |
    | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you provide the same passphrase to each instance, they will generate the same encryption settings definition and will encrypt data in the same way. Also, in many cases, if you know the passphrase used to generate an encryption settings definition, you can use that passphrase to decrypt encrypted data even if the encryption settings definition isn't available. |

  * If you have one or more encryption settings definitions that have been exported from another instance:

    1. Use the `--encryptDataWithSettingsImportedFromFile` argument to specify the path to that export file.

    2. Provide the `--encryptionSettingsExportPassphraseFile` argument to specify the path to a file containing the passphrase used to protect the contents of that export.

  * If you want the server to generate an encryption settings definition with a randomly generated passphrase, use the `--encryptDataWithRandomPassphrase` argument.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you use this argument when setting up multiple instances, then each instance will have a different encryption settings definition, and data encrypted on one instance might not be accessible to other instances. However, you can use it when setting up the first instance in a topology and then export the generated definition and use the `--encryptDataWithSettingsImportedFromFile` argument to import it when setting up additional instances.Because the random passphrase the server generated when creating the definition will not be exposed, you can't use it to decrypt data if that encryption settings definition is not available. |

## Installing the server in FIPS-compliant mode

Install the server in FIPS-compliant mode with TLS negotiation and data encryption.

### About this task

Interactive setup doesn't provide an option to enable FIPS-compliant mode, and there are currently no other supported providers that can be used to enable FIPS-compliant mode.

### Steps

* Install the server with one of the supported FIPS specifications.

  #### Choose from:

  * To set up the server for FIPS 140-2 compliance, add `--fips-provider BCFIPS1` to the set of arguments used when running setup in non-interactive mode or to the server profile's `setup-arguments.txt` file when using `manage-profile setup`.

    #### Example:

    The following example provides a sample command line that demonstrates the process for setting up the server in FIPS 140-2-compliant mode. The server only accepts TLS-encrypted LDAP on port 636 and TLS-encrypted HTTP on port 443, but doesn't allow unencrypted connections from either LDAP or HTTP clients. BCFKS key and trust stores are generated from information provided in PEM files, and an encryption settings definition is generated from a specified passphrase.

    ```
    ./setup \
      --fips-provider BCFIPS1 \
      --no-prompt \
      --acceptLicense \
      --localHostName ds1.example.com \
      --ldapsPort 636 \
      --httpsPort 443 \
      --baseDN "dc=example,dc=com" \
      --rootUserDN "cn=Directory Manager" \
      --rootUserPasswordFile /path/to/root-pw.txt \
      --maxHeapSize 2g \
      --primeDB \
      --sampleData 10001 \
      --certificateChainPEMFile /path/to/server-cert.pem \
      --certificateChainPEMFile /path/to/ca-cert.pem \
      --certificatePrivateKeyPEMFile /path/to/server-key.pem \
      --trustedCertificatePEMFile /path/to/ca-cert.pem \
      --encryptDataWithPassphraseFromFile /path/to/encryption-passphrase.txt \
      --instanceName ds1 \
      --location example-location \
      --noPropertiesFile
    ```

  * To set up the server for FIPS 140-3 compliance, add `--fips-provider BCFIPS2` to the set of arguments used when running setup in non-interactive mode or to the server profile's `setup-arguments.txt` file when using `manage-profile setup`.

## Checking the level of FIPS compliance

You can check a server's level of FIPS compliance by reviewing the properties of its `cn=Version,cn=monitor` entry.

### About this task

The following table details the properties to review within the monitor entry:

| Property                    | Values                                                                                                                                                                                   |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fips-compliant-mode`       | * `true` indicates that the server is installed in FIPS-compliant mode (using any supported specification).

* `false` indicates that the server isn't installed in FIPS-compliant mode. |
| `fips-140-2-compliant-mode` | - `true` indicates that the server is configured with the FIPS 140-2 specification.

- `false` indicates that the server isn't configured with the FIPS 140-2 specification.             |
| `fips-140-3-compliant-mode` | * `true` indicates that the server is configured with the FIPS 140-3 specification.

* `false` indicates that the server isn't configured with the FIPS 140-3 specification.             |

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A FIPS-compliant server returns a value of `true` for the `fips-compliant-mode` property and one of the FIPS specification properties. It returns `false` for all other FIPS specification properties. |

### Steps

* Run `ldapsearch` to return the `cn=Version,cn=monitor` entry.

  #### Example:

  The following example includes an `ldapsearch` and the resulting entry, which indicates that the server is installed in FIPS 140-2-compliant mode:

  ```
  $ bin/ldapsearch \
    --hostname <hostname> --port <port> --useSSL --trustAll \
    --bindDN "cn=Directory Manager" --bindPasswordFile <password_file> \
    --baseDN cn=Version,cn=monitor "(&)" fips-compliant-mode fips-140-2-compliant-mode fips-140-3-compliant-mode


    dn: cn=Version,cn=monitor
    fips-compliant-mode: true
    fips-140-2-compliant-mode: true
    fips-140-3-compliant-mode: false

    # Result Code:  0 (success)
    # Number of Entries Returned:  1
  ```

## Changing the level of FIPS compliance

You can change the level of FIPS compliance for an existing FIPS-compliant server.

### About this task

You can update a server's FIPS compliance level to any [supported FIPS specification](pd_fips_compliance.html). For example, your organization might be required by regulation to update an existing topology of FIPS 140-2-compliant servers to FIPS 140-3 compliance. Alternatively, you might need to transition a FIPS 140-3-compliant server to the FIPS 140-2 specification for technical reasons.

### Before you begin

To update the FIPS specification on a FIPS-compliant server, you need to know the following:

* The server's [current FIPS specification](#check_FIPS_level)

* The server's installation method:

  * Using `manage-profile setup`

  * Using `setup`

* The encoded value of the target FIPS specfication:

  * `BCFIPS1` for FIPS 140-2

  * `BCFIPS2` for FIPS 140-3

### Steps

* Follow the appropriate steps based upon the type of server installation method.

  #### Choose from:

  * For servers installed using `manage-profile setup`, run `manage-profile replace-profile`. Supply the `--fips-provider` argument using the encoded value of the target FIPS specification. Learn more [about the `manage-profile` tool](../pingdirectory_server_administration_guide/pd_ds_manage_profile_tool.html).

  * For servers installed using `setup`:

    1. In `config/java.properties`, edit the value of `-Dcom.unboundid.crypto.FIPS_PROVIDER` to the encoded value of the target FIPS specification.

    2. Run `bin/dsjavaproperties`.

    3. Restart the server.

  #### Troubleshooting:

  If the server doesn't operate as expected after the update, revert the server to the previous FIPS compliance level.
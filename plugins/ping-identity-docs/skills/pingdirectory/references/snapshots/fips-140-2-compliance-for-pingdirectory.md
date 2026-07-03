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

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

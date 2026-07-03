---
title: Configure the Active Directory password synchronization plugin
description: Configure the Active Directory password synchronization plugin registry keys for authentication, encryption, sync, and logging
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:conf-ad-pwd-sync
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/conf-ad-pwd-sync.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Active Directory", "Configuration"]
section_ids:
  create-edit-regkey-values: Create or edit registry key values
  regkey-values: Registry key values
  authentication_method: Authentication method
  password_encryption: Password encryption
  connection_synchronization: Connection & synchronization
  ad-sync-keys-noidm: IDM availability
  logging_configuration: Logging configuration
  other: Other
  regkey-encryption: Registry key value encryption
  regkey-validation: Registry key value validation
  ad-pwd-userAttribute-mod: Example userAttribute modification
---

# Configure the Active Directory password synchronization plugin

If you need to change any settings after installation, access the settings using the Registry Editor. For the full list of available registry key values, refer to [Registry Key Values](#regkey-values). For information about creating registry keys, refer to the corresponding [Windows documentation](https://docs.microsoft.com/en-us/system-center/scsm/registry-keys).

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | After you change a registry key value associated with the password synchronization plugin, [perform validation](#regkey-validation). |

## Create or edit registry key values

1. Click the Start Menu, type registry, and click Registry Editor Desktop app.

2. In the left pane of Registry Editor, expand the node:

   ```
   HKEY_LOCAL_MACHINE > SOFTWARE > ForgeRock > OpenIDM > PasswordSync
   ```

   For Example:

   ![Registry Editor Screenshot](_images/ad-regedit.png)

3. From here you can edit the registry key values, or create new ones.

   * To edit a value, double-click any item in the Name column. An Edit String window displays.

     ![Edit String window](_images/ad-regedit-edit.png)

   * To create a new string value, right-click the last folder of the expanded node (PasswordSync), select New > String Value, and enter the applicable information.

     ![Registry Editor new string value](_images/ad-regedit-new-value.png)

## Registry key values

### Authentication method

The following registry key values let you customize the authorization method between the plugin and IDM.

| Key Value                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authType`(Required)         | The authentication type:- `basic`

  Plain HTTP or SSL authentication.

- `idm`

  Plain HTTP or SSL authentication using IDM headers.

- `oauth2`

  Oauth2 authentication using AM bearer tokens.

- `cert`

  Mutual SSL authentication using a certificate.

  By default, the plugin does not validate the IDM certificate. To enable validation, create the registry key value netSslVerifyPeer set to True.                                                                                 |
| `netSslVerifyPeer`(Optional) | When using `cert` as the authentication type, you can create this value set to `True` to force validation of the IDM certificate.                                                                                                                                                                                                                                                                                                                                                                  |
| `authToken0`(Required)       | The username or certificate path for authentication.For example, for plain HTTP or SSL authentication, `authToken0` might be set to `openidm-admin`.For certificate authentication, set `authToken0` to the certificate path. For example, `path/to/certificate/cert.p12`. Only PKCS #12 format certificates are supported.                                                                                                                                                                        |
| `authToken1`(Required)       | The authentication password.For example, for plain HTTP or SSL authentication, `authToken1` might be set to `openidm-admin`.For certificate authentication, set `authToken1` to the keystore password.                                                                                                                                                                                                                                                                                             |
| `encKey`(Optional)           | The encryption key used to encrypt the values of `authToken1` and `certPassword`. These values are encrypted automatically when the plugin is installed, but when you change the settings, you can encrypt the values manually by setting the `encKey` registry key. For more information, refer to [Registry Key Value Encryption](#regkey-encryption).	If you do not want to encrypt the values of authToken1 and certPassword, you must remove the registry key value encKey from the registry. |

### Password encryption

The following registry key values let you customize the encryption method for captured passwords.

| Key Value                | Description                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `certFile`(Required)     | The path to the keystore used for encrypting captured passwords. For example, `path/to/keystore.p12`. Only PKCS #12 keystores are supported. |
| `certPassword`(Required) | The `certFile` keystore password.                                                                                                            |
| `keyAlias`(Required)     | The `certFile` keystore alias.                                                                                                               |
| `keyType`(Optional)      | The `certFile` keystore encryption algorithm. For example, `aes128`. If not set, defaults to `aes128`.                                       |

### Connection & synchronization

The password synchronization plugin assumes that the Active Directory user attribute is `sAMAccountName`. Although the default attribute works in most deployments, you can specify an alternative attribute. For an example, refer to [Example `userAttribute` Modification](#ad-pwd-userAttribute-mod).

| Key Value                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userAttribute`(Optional)              | The attribute that identifies the Active Directory user. The password synchronization plugin assumes that the Active Directory user attribute is `sAMAccountName`. Used with `userSearchFilter`.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `userSearchFilter`(Optional)           | The search filter for locating Active Directory users.Can only be used if `userAttribute` is also specified (even if the value is the default attribute `sAMAccountName`).	To use userSearchFilter with a special attribute such as memberOf, the filter only tests for immediate group memberships, and not for membership in the primary group (typically, cn=Users or cn=Domain Users) of your domain. The filter does not handle nested memberships. For example, User A is member of Group A, which is a member of Group B—although User A is technically a member of Group B, the filter will not interpret it as such. |
| `idmURL`(Required)                     | The URL where IDM is deployed, including the query that targets each user account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `passwordAttr`(Required)               | The password attribute for the `managed/user` object, such as `adPassword`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `oauth2Url`(Optional)                  | For the authentication type `OAuth2 Access Token`, the token URL. For example:```
https://am.example.com/am/oauth2/realms/root/access_token
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `oauth2Scope`(Optional)                | For the authentication type `OAuth2 Access Token`, the OAuth2 token scope. For example `fr:idm:*`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `userSearchBaseDn`(Optional)           | The bind BaseDN used in the Active Directory user search. Use to set a different base dn for attribute search. Default value is derived from `defaultNamingContext`.Can only be used if `userAttribute` is also specified (even if the value is the default attribute `sAMAccountName`). Used with `userSearchFilter`.                                                                                                                                                                                                                                                                                                        |
| `userSearchBindPass`(Optional)         | The bind password used in the Active Directory user search.Can only be used if `userAttribute` is also specified (even if the value is the default attribute `sAMAccountName`). Used with `userSearchFilter`.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `userSearchBindUser`(Optional)         | The bind user used in the Active Directory user search.Can only be used if `userAttribute` is also specified (even if the value is the default attribute `sAMAccountName`). Used with `userSearchFilter`.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []()`userSearchFilterStrict`(Optional) | Additional control for the behavior of `userSearchFilter`:- If set to `true`, requires `userSearchFilter` to return a value, which you can use to filter out Active Directory users/groups from being password-synced.

- The default behavior is `false`, which results in `userSearchFilter` only being used to look up the Active Directory user attribute, and if it fails, password synchronization is still attempted with a default attribute.                                                                                                                                                                         |

### IDM availability

When IDM is unavailable, or when an update fails, the password synchronization plugin stores the user password change in a JSON file on the Active Directory system and attempts to resend the password change at regular intervals.

You can modify this behaviour with the following registry key values:

| Key Value                | Description                                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataPath`(Required)     | The location where the password synchronization plugin stores the unsent changes. When any unsent changes have been delivered successfully, files in this path are deleted. The plugin creates one file for each user. This means that if a user changes their password three times in a row, you will refer to only one file containing the last change. |
| `maxFileRetry`(Optional) | The maximum number of password change retry attempts after which the plugin stops attempting to send changes.                                                                                                                                                                                                                                             |
| `netTimeout`(Optional)   | The length of time (in milliseconds) before the plugin stops attempting a connection.                                                                                                                                                                                                                                                                     |
| `pollEach`(Optional)     | The interval (in seconds) between each attempt to send changes.                                                                                                                                                                                                                                                                                           |

### Logging configuration

| Key Value            | Description                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `logPath`(Optional)  | The path to the log file.	If you change this parameter, you must restart the machine for the new setting to take effect. If you change the logPath and do not restart the machine, the service will write the logs to the new location, but the sync module will continue to write logs to the old location until the machine is restarted. |
| `logSize`(Optional)  | The maximum log size (in Bytes) before the log is rotated. When the log file reaches this size, it is renamed `idm.log.0` and a new `idm.log` file is created.                                                                                                                                                                              |
| `logLevel`(Optional) | The severity of messages to log:- `debug`

- `info`

- `warning`

- `error`

- `fatal`                                                                                                                                                                                                                                                      |

### Other

| Key Value                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pwdChangeInterval`(Optional) | Infinite password sync loop prevention.When Active Directory syncs passwords with IDM bidirectionally, it is possible to enter an infinite loop, where Active Directory and IDM are constantly updating the password and telling the other system to do the same. To help prevent this situation, you can set the `pwdChangeInterval` key to the number of seconds that must elapse between password updates.	This feature requires AD Password Synchronization Plugin version 1.4.0 or later. Because version 1.4.0 can fail to make a secure connection with certain Windows versions, Ping recommends using a later version. |

## Registry key value encryption

For security reasons, you should encrypt the values of the `authToken1` and `certPassword` keys. During password synchronization plugin installation, they are encrypted automatically. If you need to change the values, you can encrypt the values manually by setting the `encKey` registry key value.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you do not want to encrypt the values of the `authToken1` and `certPassword` keys, you *must* delete `encKey` from the registry. In this case, all password attributes can be set in cleartext (unencrypted). |

To encrypt the values of the `authToken1` and `certPassword`:

1. Optionally, generate a new encryption key; otherwise, you can use the existing encryption key and skip this step.

   ```none
   PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --key

   keyValue
   ```

2. Encrypt the sensitive registry key values:

   ```
   PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --encrypt "keyValue" "authToken1Value"

   authToken1-keyValue
   ```

   ```
   PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --encrypt "keyValue" "certPasswordValue"

   certPasswordValue-keyValue
   ```

3. Replace the existing values of `encKey`, `authToken1` and `certPassword` keys with the generated values.

   For instructions on editing registry key values, refer to [Create or Edit Registry Key Values](#create-edit-regkey-values).

## Registry key value validation

After you change a registry key value associated with the password synchronization plugin, run `path\to\idmsync.exe --validate` to perform validation. For example:

```none
PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --validate

OpenIDM Password Sync Service

Validating configuration parameters as user "Administrator"

Logging parameters:
logPath:
   "Z:\" has read/write access permissions.

logLevel:
   "error" is a valid logLevel entry.

logSize:
   "" is not a valid logSize entry. Will use default 5120000 byte file size limit.

Service and data storage parameters:
dataPath:
   "Z:\" has read/write access permissions.

pollEach:
   "75" is a valid pollEach entry.

OpenIDM service parameters:
idmURL:
   "https://localhost:8444/openidm/managed/user?_action=patch&_queryId=for-userName&uid=${samaccountname}" is a valid idmURL entry.

keyAlias:
   "openidm-cert" is a valid keyAlias entry.

passwordAttr:
   "adPassword" is a valid passwordAttr entry.

idm2Only:
   Service is configured to run with OpenIDM version 3.x or newer.

netTimeout:
   "" is not a valid netTimeout entry. Will use default 16 second network timeout.

authType, authToken0 and authToken1:
   Service is configured to use "OAuth2 Access Token" authentication
   "oauth2" is a valid authType entry.

Password encryption parameters:
certFile and certPassword:
   "Z:\openidm-localhost.crt" file is a valid entry.
```

## Example `userAttribute` modification

The password synchronization plugin assumes that the Active Directory user attribute is `sAMAccountName`. The default attribute will work in most deployments. If you cannot use the `sAMAccountName` attribute to identify the Active Directory user, set the following registry keys on your Active Directory server, specifying an alternative attribute. The examples in the following table use the `employeeId` attribute instead of `sAMAccountName`.

For instructions on editing registry key values, refer to [Create or Edit Registry Key Values](#create-edit-regkey-values).

| Key Value          | Data                                                                                          |
| ------------------ | --------------------------------------------------------------------------------------------- |
| `userAttribute`    | `employeeId`                                                                                  |
| `userSearchFilter` | `(&(objectClass=user)(sAMAccountName=%s))`                                                    |
| `idmURL`           | `https://localhost:8444/openidm/managed/user?_action=patch&_queryFilter=uid+eq+${employeeId}` |

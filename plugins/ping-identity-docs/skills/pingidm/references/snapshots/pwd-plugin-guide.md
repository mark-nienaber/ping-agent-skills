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

---

---
title: Help command
description: Reference for the idmsync.exe help command, listing available command-line options for the Active Directory password synchronization plugin
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:help-ad-pwd
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/help-ad-pwd.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Active Directory", "Help"]
---

# Help command

The password synchronization plugin executable file includes a help command that prints the available command line options.

```none
PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --help

OpenIDM Password Sync Service usage:

install service:
 idmsync.exe --install

uninstall service:
 idmsync.exe --remove

start service:
 idmsync.exe --start

stop service:
 idmsync.exe --stop

query service:
 idmsync.exe --status

validate configuration:
 idmsync.exe --validate

generate encryption key:
 idmsync.exe --key

encrypt password:
 idmsync.exe --encrypt "key" "password"

build and version info:
 idmsync.exe --version
```

---

---
title: Install the Active Directory password synchronization plugin
description: Install the Active Directory password synchronization plugin using the installation wizard, including connection, authentication, and encryption settings
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:install-ad-pwd-sync
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/install-ad-pwd-sync.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Active Directory", "Installation"]
section_ids:
  self-signed-cert-test: Generate a self-signed certificate
  add-windows-cert-store: Add a certificate to the Windows certificate store
---

# Install the Active Directory password synchronization plugin

The following steps install the password synchronization plugin on an Active Directory server:

1. [Download the Active Directory password synchronization plugin](https://backstage.forgerock.com/downloads).

2. Launch the installation wizard using one of the following methods:

   * In Windows Explorer, double-click the ad-passwordchange-handler-1.8.0.exe file.

   * From a PowerShell command-line, enter the executable name (`.\ad-passwordchange-handler-1.8.0.exe`), and press `Enter`.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | When starting the installation wizard from the command-line, the following options are available:- To save the settings in a configuration file, use the `/saveinf` switch:

       ```none
       PS C:\path\to\dir> .\ad-passwordchange-handler-1.8.0.exe /saveinf=C:\temp\adsync.inf
       ```

     - If you have a configuration file with installation parameters, you can install the password plugin in silent mode as follows:

       ```none
       PS C:\path\to\dir> .\ad-passwordchange-handler-1.8.0.exe /verysilent /loadinf=C:\temp\adsync.inf
       ``` |

3. In the Setup - OpenIDM Password Sync window, on the License Agreement page, you must accept the license agreement to continue, and then click Next.

   > **Collapse: Show Me**
   >
   > ![ad-setup-license.png](_images/ad-setup-license.png)

4. On the OpenIDM Information: Connection page, enter the applicable information in the following fields, and click Next.

   > **Collapse: Show Me**
   >
   > ![ad-setup-connection.png](_images/ad-setup-connection.png)

   |                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | OpenIDM URL                     | The URL where IDM is deployed, including the query that targets each user account. For example:```none
   https://localhost:8444/openidm/managed/user?_action=patch&_queryFilter=userName+eq+'${samaccountname}'
   ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | OpenIDM User Password attribute | The password attribute for the `managed/user` object, such as `adPassword`.&#xA;&#xA;If the password attribute does not exist in the IDM managed/user object, the password sync service will return an error when it attempts to replay a password update that has been made in Active Directory. If your managed user objects do not include passwords, you can add an onCreate script to the Active Directory > Managed Users mapping that sets an empty password when managed user accounts are created. The following excerpt of a sample sync.json file shows such a script in the mapping:&#xA;&#xA;"mappings" : \[&#xA;    {&#xA;        "name" : "systemAdAccounts\_managedUser",&#xA;        "source" : "system/ad/account",&#xA;        "target" : "managed/user",&#xA;        "properties" : \[&#xA;            {&#xA;                "source" : "sAMAccountName",&#xA;                "target" : "userName"&#xA;            }&#xA;        ],&#xA;        "onCreate" : {&#xA;            "type" : "text/javascript",&#xA;            "source" : "target.password=''"&#xA;        },&#xA;        ...&#xA;    }&#xA;]&#xA;&#xA;The onCreate script creates an empty password in the managed/user object, so that the password attribute exists and can be patched. |

5. On the OpenIDM Information: Authentication page, enter the applicable information in the following fields, and click Next.

   > **Collapse: Show Me**
   >
   > ![ad-setup-auth.png](_images/ad-setup-auth.png)

   |                            |                                                                                                                                                                                                                                                                  |
   | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | User name                  | An administrative user that can authenticate to IDM. For example, `openidm-admin`.                                                                                                                                                                               |
   | Password                   | The above, specified user's password.                                                                                                                                                                                                                            |
   | OAuth2 Access Token URL    | If you're using the authentication type `OAuth2 Access Token`, enter the token URL. For example:```
   https://am.example.com/am/oauth2/realms/root/access_token
   ```                                                                                                |
   | OAuth2 Scope               | If you're using the authentication type `OAuth2 Access Token`, enter the OAuth2 token scope. For example `fr:idm:*`.                                                                                                                                             |
   | Select authentication type | Select the authentication type that Active Directory will use to authenticate to IDM:- To use plain HTTP authentication, select OpenIDM Header.

   - To use mutual SSL authentication, select Certificate.

   - To use AM bearer tokens, select OAuth2 Access Token. |

6. If you selected Certificate as the authentication type, complete this step; otherwise, skip to the next step.

   On the OpenIDM Information: Certificate Authentication page, enter the applicable information in the following fields, and click Next.

   > **Collapse: Show Me**
   >
   > ![ad-setup-cert-auth.png](_images/ad-setup-cert-auth.png)

   |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Select Certificate file...        | Browse to select the certificate file that Active Directory will use to authenticate to IDM.&#xA;&#xA;The certificate file must be configured with an appropriate encoding, cryptographic hash function, and digital signature. The password synchronization plugin can read a public or a private key from a PKCS #12 archive file.&#xA;&#xA;For production, you should use a certificate issued by a certificate authority (CA). For testing, you can generate a self-signed certificate.You must also import the certificate into the IDM truststore. On the machine that's running IDM, import the certificate. For example:```console
   keytool \
   -importkeystore \
   -srckeystore /path/to/ad-pwd-plugin-localhost.p12 \
   -srcstoretype PKCS12 \
   -destkeystore /path/to/openidm/security/truststore \
   -deststoretype <TRUSTSTORE-TYPE> (1)
   ```1	Replace \<TRUSTSTORE-TYPE> with your IDM truststore type. For example, JKS, JCEKS, or PKCS12. |
   | Password to open certificate file | The keystore password (`changeit`, in the previous example).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

7. On the Password Encryption page, enter the applicable information in the following fields, and click Next.

   > **Collapse: Show Me**
   >
   > ![ad-setup-data-encrypt.png](_images/ad-setup-data-encrypt.png)

   |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Select Certificate file...        | Browse to select the certificate that will be used for password encryption. The certificate format must be PKCS #12.&#xA;&#xA;The certificate file must be configured with an appropriate encoding, cryptographic hash function, and digital signature. The plugin can read a public or a private key from a PKCS #12 archive file.&#xA;&#xA;For production, you should use a certificate issued by a CA. For testing, you can generate a self-signed certificate.You must also import the certificate into the IDM keystore. The keystore type and filename depend on your deployment. For example, `keystore.jceks` for JCEKS or `keystore.pkcs12` for PKCS12.On the machine that's running IDM, import the certificate. For example:```console
   keytool \
   -importkeystore \
   -srckeystore /path/to/ad-pwd-plugin-localhost.p12 \
   -srcstoretype PKCS12 \
   -destkeystore /path/to/openidm/security/<idm-keystore-file> \ (1)
   -deststoretype <IDM-KEYSTORE-TYPE> (2)
   ```1	Replace \<idm-keystore-file> with the name of your IDM keystore file. For example, keystore.jceks or keystore.pkcs12.&#xA;2	Replace \<IDM-KEYSTORE-TYPE> with the corresponding keystore type. For example, JCEKS or PKCS12. |
   | Private key alias                 | The certificate alias, such as `ad-pwd-plugin-localhost`. The password sync plugin sends the alias when communicating with IDM, which uses the alias to retrieve the corresponding private key in IDM's keystore.Update the IDM secret store (`conf/secrets.json`) to add this certificate alias to the `idm.default` secretId:```json
   "mappings": [
       {
           "secretId": "idm.default",
           "types": [ "ENCRYPT", "DECRYPT" ],
           "aliases": [ "&{openidm.config.crypto.alias|openidm-sym-default}", "ad-pwd-plugin-localhost" ] },
           ...
       }
   ]
   ```Learn more about [Secret stores](../security-guide/secret-stores.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | Password to open certificate file | The password to access the PFX keystore file, such as `changeit`, from the previous example.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | Select encryption...              | The encryption standard to use when encrypting the password value (AES-128, AES-192, or AES-256).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

8. On the Data Storage page, enter the applicable information in the following fields, and click Next.

   > **Collapse: Show Me**
   >
   > ![ad-setup-data-storage.png](_images/ad-setup-data-storage.png)

   |                                                                     |                                                                                                                                                                                 |
   | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Select the folder in which Service will store its output data files | Browse to select the folder for data output files. The server should prevent access to this folder except for the `Password Sync service`.	The path name cannot include spaces. |
   | Directory poll interval (seconds)                                   | The number of seconds between calls to check whether IDM is available. For example, `60`, to poll IDM every minute.                                                             |

9. On the Log Storage page, enter the applicable information in the following fields, and click Next.

   > **Collapse: Show Me**
   >
   > ![ad-setup-log-storage.png](_images/ad-setup-log-storage.png)

   |                                                             |                                                                                   |
   | ----------------------------------------------------------- | --------------------------------------------------------------------------------- |
   | Select the folder in which Service will store its log files | Browse to select the folder for log files.	The path name cannot include spaces.   |
   | Select logging level                                        | The severity of messages to log: `error`, `info`, `warning`, `fatal`, or `debug`. |

10. On the Select Destination Location page, browse to select the installation folder (default `C:\Program Files\OpenIDM Password Sync`), and click Next.

    > **Collapse: Show Me**
    >
    > ![ad-setup-intsall-loc.png](_images/ad-setup-intsall-loc.png)

11. On the Ready to Install page, verify the details are acceptable, and click Install to continue. If you need to change any installation options, click Back.

    > **Collapse: Show Me**
    >
    > ![ad-setup-ready-to-install.png](_images/ad-setup-ready-to-install.png)

12. On the Completing the OpenIDM Password Sync Setup Wizard page, select one of the following, and click Finish:

    > **Collapse: Show Me**
    >
    > ![ad-setup-install-complete.png](_images/ad-setup-install-complete.png)

    * Yes, restart the computer now

    * No, I will restart the computer later

      |   |                                                                               |
      | - | ----------------------------------------------------------------------------- |
      |   | If you select this option, you must restart the computer before you continue. |

13. If you selected `Certificate` as the authentication type during setup, complete [Add a Certificate to the Windows Certificate Store](#add-windows-cert-store); otherwise, your setup is now complete.

Password synchronization should now be configured and working. To test that the setup was successful, change a user password in Active Directory. That password should be synchronized to the corresponding IDM managed user account, and you should be able to query the user's own entry in IDM using the new password.

## Generate a self-signed certificate

For production, you should use a certificate issued by a CA. For testing, you can generate a self-signed certificate.

1. On the Active Directory host, generate a private key, which will be used to generate a self-signed certificate with the alias `ad-pwd-plugin-localhost`. The following example uses a JCEKS keystore, but you can use any keystore type supported by your environment:

   ```console
   > keytool.exe ^
    -genkey ^
    -alias ad-pwd-plugin-localhost ^
    -keyalg rsa ^
    -dname "CN=localhost, O=AD-pwd-plugin Self-Signed Certificate" ^
    -keystore keystore.jceks ^
    -storetype JCEKS
   Enter keystore password:changeit
   Re-enter new password: changeit
   Enter key password for <ad-pwd-plugin-localhost>
         <RETURN if same as keystore password>
   ```

2. Now use the private key, stored in the keystore file, to generate the self-signed certificate:

   ```console
   > keytool.exe ^
    -selfcert ^
    -alias ad-pwd-plugin-localhost ^
    -validity 365 ^
    -keystore keystore.jceks ^
    -storetype JCEKS ^
    -storepass changeit
   ```

3. Export the certificate. For example, the following `keytool` command exports the certificate in a PKCS #12 archive file format (`ad-pwd-plugin-localhost.p12`):

   ```console
   > keytool.exe ^
    -importkeystore ^
    -srckeystore keystore.jceks ^
    -srcstoretype jceks ^
    -srcstorepass changeit ^
    -srckeypass changeit ^
    -srcalias ad-pwd-plugin-localhost ^
    -destkeystore ad-pwd-plugin-localhost.p12 ^
    -deststoretype PKCS12 ^
    -deststorepass changeit ^
    -destkeypass changeit ^
    -destalias ad-pwd-plugin-localhost ^
    -noprompt
   ```

4. Transfer the file created in the previous command (`ad-pwd-plugin-localhost.p12`) to the IDM host system, and then import it into the IDM keystore. For example:

   ```console
   keytool \
   -importkeystore \
   -srckeystore /path/to/ad-pwd-plugin-localhost.p12 \
   -srcstoretype PKCS12 \
   -destkeystore /path/to/openidm/security/<idm-keystore-file> \ (1)
   -deststoretype <IDM-KEYSTORE-TYPE> (2)
   ```

   |       |                                                                                                                            |
   | ----- | -------------------------------------------------------------------------------------------------------------------------- |
   | **1** | Replace `<idm-keystore-file>` with the name of your IDM keystore file. For example, `keystore.jceks` or `keystore.pkcs12`. |
   | **2** | Replace `<IDM-KEYSTORE-TYPE>` with the corresponding keystore type. For example, `JCEKS` or `PKCS12`.                      |

## Add a certificate to the Windows certificate store

|   |                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------- |
|   | If you selected `Certificate` as the authentication type during setup, you must complete this procedure. |

The Password Sync Service uses Windows certificate stores to verify IDM's identity. The certificate that IDM uses must therefore be added to the list of trusted certificates on the Windows machine.

In a production environment, use a certificate that has been issued by a certificate authority. For test purposes, you can use the self-signed certificate that is generated by IDM on first startup.

To add the IDM certificate to the list of trusted certificates, use the Microsoft Management Console:

1. Click the Start Menu, type mmc, and click mmc Run Command.

2. In the Console window, select File > Add/Remove Snap-in.

   ![mmc-add-rem-snapin.png](_images/mmc-add-rem-snapin.png)

3. From the Available snap-ins area, select Certificates, and click Add >.

   ![mmc-snapin-window.png](_images/mmc-snapin-window.png)

4. In the Certificates snap-in window, select My user account, and click Finish.

   ![mmc-cert-snapin-window.png](_images/mmc-cert-snapin-window.png)

5. From the Available snap-ins area, select Certificates, and click Add >.

   ![mmc-snapin-window2.png](_images/mmc-snapin-window2.png)

6. In the Certificates snap-in window, select Service account, and click Next >.

   ![mmc-cert-snapin-window2.png](_images/mmc-cert-snapin-window2.png)

7. In the Select Computer window, select Local Computer, and click Next >.

   ![mmc-select-comp.png](_images/mmc-select-comp.png)

8. In the Certificates snap-in window, select the service account OpenIDM Password Sync Service, and click Finish.

   ![mmc-select-serv-acct.png](_images/mmc-select-serv-acct.png)

9. From the Available snap-ins area, select Certificates, and click Add >.

   ![mmc-snapin-window3.png](_images/mmc-snapin-window3.png)

10. In the Certificates snap-in window, select Computer account, and click Next >.

    ![mmc-cert-snapin-window3.png](_images/mmc-cert-snapin-window3.png)

11. In the Select Computer window, select Local Computer, and click Finish.

    ![mmc-select-comp2.png](_images/mmc-select-comp2.png)

12. In the Add or Remove Snap-ins window, verify that you have three certificates in the Selected snap-ins area, and click OK. If you're missing any certificates, please review the earlier steps in this procedure, and add the missing certificate(s).

    ![mmc-snapin-window4.png](_images/mmc-snapin-window4.png)

13. For each of the following nodes, import the certificate, as follows:

    **List of Nodes**

    |                                                                                       |
    | ------------------------------------------------------------------------------------- |
    | Certificates - Current User > Personal                                                |
    | Certificates - Current User > Trusted Root Certification Authorities                  |
    | Certificates - Service > OpenIDM Password Sync\Personal                               |
    | Certificates - Service > OpenIDM Password Sync\Trusted Root Certification Authorities |
    | Certificates > Local Computer > Personal                                              |
    | Certificates > Local Computer > Trusted Root Certification Authorities                |

    1. Expand the node, and select the appropriate item. For example, Certificates - Current User > Personal:

       ![mmc-select-cert-current-user.png](_images/mmc-select-cert-current-user.png)

    2. From the menu bar, select Action > All Tasks > Import.

       ![mmc-action-all-import.png](_images/mmc-action-all-import.png)

    3. In the Certificate Import Wizard window, click Next.

       ![mmc-cert-import-wiz.png](_images/mmc-cert-import-wiz.png)

    4. On the File to Import page, click Browse, locate the IDM certificate, and then click Next. If you [exported IDM's self-signed certificate](chap-sync-dj.html#export-idm-cert), the certificate is `openidm-localhost.crt`.

       ![mmc-cert-import-wiz-file.png](_images/mmc-cert-import-wiz-file.png)

    5. On the Certificate Store page, leave the default option selected, and click Next. For example:

       ![mmc-cert-import-store.png](_images/mmc-cert-import-store.png)

    6. On the final page of the wizard, review the details, and click Finish. For example:

       ![mmc-cert-import-wiz-done.png](_images/mmc-cert-import-wiz-done.png)

    7. The Certificate Import Wizard window displays the success or failure of the import, click OK.

       ![mmc-wiz-success.png](_images/mmc-wiz-success.png)

       The main window of the Microsoft Management Console now displays the added certificate in a sub-node. For example:

       ![mmc-added-cert.png](_images/mmc-added-cert.png)

       |   |                                                                                        |
       | - | -------------------------------------------------------------------------------------- |
       |   | Make sure to repeat this sub-procedure for [all required nodes](#list-nodes-add-cert). |

---

---
title: Password synchronization plugins
description: Overview of PingIDM password synchronization plugins that intercept and sync password changes in PingDS and Active Directory
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:chap-overview
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/chap-overview.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins"]
---

# Password synchronization plugins

Password synchronization ensures uniform password changes across the resources that store the password. After password synchronization, a user can authenticate with the same password on each resource. No centralized directory or authentication server is required for performing authentication. Password synchronization reduces the number of passwords users need to remember, so they can use fewer, stronger passwords.

IDM can propagate passwords to the resources that store a user's password. In addition, you can download plugins from the [Backstage download site](https://backstage.forgerock.com/downloads) to intercept and synchronize passwords that are changed natively in PingDS (DS) and Active Directory.

If you use these plugins to synchronize passwords, set up password policy enforcement on the LDAP resource, rather than on IDM. Alternatively, ensure that all password policies that are enforced are identical to prevent password updates on one resource from being rejected by IDM or by another resource.

The password synchronization plugin intercepts password changes on the LDAP resource before the passwords are stored in encrypted form. The plugin then sends the intercepted password value to IDM, using an HTTP POST request to patch the corresponding managed user object.

|   |                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------- |
|   | The plugins do not use the LDAP connector to transmit passwords, but send a generic HTTP POST request with a `patch` action. |

If the IDM instance is unavailable when a password is changed in either DS or Active Directory, the respective password plugin intercepts the change, encrypts the password, and stores the encrypted password in a JSON file. The plugin then checks whether the IDM instance is available, at a predefined interval. When IDM becomes available, the plugin performs a PATCH on the managed user record, to replace the password with the encrypted password stored in the JSON file.

To be able to synchronize passwords, both password synchronization plugins require that the corresponding managed user object exist in the IDM repository.

---

---
title: Password synchronization plugins
description: Guide to configuring and integrating the password synchronization plugins into your PingIDM deployment
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins"]
page_aliases: ["index.adoc"]
---

# Password synchronization plugins

Password synchronization ensures uniform password changes across the resources that store the password. This guide shows you how to use password synchronization plugins to synchronize passwords between PingIDM (IDM) and an LDAP server, either PingDS (DS) or Active Directory.

[icon: sync-alt, set=fad, size=3x]

#### [Password Sync Plugins](chap-overview.html)

Discover how password synchronization works in IDM and learn about the plugins provided for synchronizing passwords with LDAP servers.

![](_images/DirectoryServer.svg)

#### [Synchronize With DS](chap-sync-dj.html)

Use the PingDS password synchronization plugin.

[icon: microsoft, set=fab, size=3x]

#### [Synchronize With AD](chap-sync-ad.html)

Use the Active Directory password synchronization plugin.

---

---
title: Start or stop the plugin
description: Start, stop, and check the status of the Active Directory password synchronization plugin using Windows Service Manager or the command line
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:start-stop-ad-pwd
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/start-stop-ad-pwd.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Active Directory", "Startup", "Shutdown"]
section_ids:
  windows_service_manager: Windows Service Manager
  command_line: Command line
  plugin_status: Plugin status
---

# Start or stop the plugin

The password synchronization plugin runs as OpenIDM Password Sync Service. You can start and stop the service using Windows Service Manager or the command line.

## Windows Service Manager

1. Click the Start Menu, type services.msc, and click Services Desktop App.

2. In the Services windows, right-click OpenIDM Password Sync Service, and select the applicable option (Start, Stop, or Restart):

   ![Windows Service Manager](_images/win-services-ad-pwd.png)

## Command line

You can use the following commands to start and stop the service from the command line.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service will not start from the command line if any registry key value [fails validation](conf-ad-pwd-sync.html#regkey-validation). |

```none
PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --start
```

```none
PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --stop
```

### Plugin status

You can also check the status of the plugin:

```none
PS C:\Program Files\OpenIDM Password Sync> .\idmsync.exe --status
Service is running.
```

---

---
title: Synchronize passwords with Active Directory
description: Install and use the Active Directory password synchronization plugin to sync passwords between PingIDM and Active Directory
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:chap-sync-ad
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/chap-sync-ad.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Active Directory"]
---

# Synchronize passwords with Active Directory

Use the Active Directory (AD) password synchronization plugin to synchronize passwords between IDM and Active Directory.

Install the plugin on Active Directory domain controllers (DCs) to intercept password changes, and send the password values to IDM over an encrypted channel. You must have Administrator privileges to install the plugin. In a clustered Active Directory environment, you must install the plugin on all DCs.

---

---
title: Synchronize passwords with DS
description: Install, configure, and manage the PingDS password synchronization plugin to intercept and sync password changes to PingIDM
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:chap-sync-dj
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/chap-sync-dj.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Directory Server"]
section_ids:
  dj-pwd-sync-prerequisites: Set up IDM and DS
  dj-pwd-sync-prepare-idm: Prepare IDM
  dj-pwd-sync-prepare-ds: Prepare DS
  dj-pwd-sync-security: Secure communication between IDM and DS
  import-openidm-cert: Enable DS to trust the IDM certificate
  import-ds-cert: Enable IDM to trust DS certificates
  pwd-sync-am-tokens: Configure the plugin for AM bearer tokens
  dj-pwd-sync-install: Install and configure the DS plugin
  install-ds-password-sync-plugin-no-AM: For regular IDM authentication
  pwd-sync-idm-config: Configure IDM for password synchronization
  for_authentication_with_am_bearer_tokens: For authentication with AM bearer tokens
  dj-pwd-sync-test: Test the DS plugin
  dj-upgrade-plugin: Update the DS plugin
  dj-pwd-sync-uninstall: Uninstall the DS plugin
---

# Synchronize passwords with DS

The PingDS (DS) password synchronization plugin intercepts passwords that are changed natively in the DS server and propagates these password changes to IDM. The password synchronization plugin captures password changes in clear text, encrypts them, and transmits them to IDM. If IDM is unavailable when a password change occurs, the password change is queued for subsequent retry.

The password synchronization plugin requires keys to encrypt changed passwords and certificates to secure communication between DS and IDM. The examples that follow use the keys generated when you set up the DS and IDM servers.

## Set up IDM and DS

The following examples prepare a demonstration of password synchronization from DS to IDM. After this preparation:

* DS and IDM are installed and running on your computer, with default security settings.

  In particular, both servers have key pairs used later in the demonstration:

  * DS has a generated TLS key pair (alias: `ssl-key-pair` and certificate subject DN: `CN=DS, O=ForgeRock.com`) signed by the DS deploymentId-based CA (certificate subject DN: `CN=Deployment key, O=ForgeRock.com`).

    DS uses the certificate to set up TLS connections, and to authenticate to IDM.

  * IDM has a generated key pair, alias `openidm-localhost`. The certificate is self-signed, and has certificate subject DN `CN=openidm-localhost, O=OpenIDM Self-Signed Certificate, OU=None, L=None, ST=None, C=None`.

    DS uses the public key certificate to encrypt passwords before sending them to IDM.

* IDM does not otherwise synchronize DS data with its own.

  This lets you confirm that DS, not synchronization, provides the updated password to IDM.

* DS and IDM both have a user account for Barbara Jensen.

  After you have configured password synchronization, when Barbara Jensen's password changes in DS, DS sends the change to IDM.

### Prepare IDM

1. Update your hosts file.

   The IDM self-signed certificate uses the domain alias `openidm-localhost`. When testing the DS plugin on your computer, add the alias to your `/etc/hosts` file:

   ```none
   127.0.0.1       localhost openidm-localhost
   ```

2. Unzip IDM.

3. Start IDM:

   ```bash
   /path/to/openidm/startup.sh
   ```

4. Add Barbara Jensen's account to IDM:

   ```none
   curl \
   --request PUT \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept: application/json" \
   --header "If-None-Match: *" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --data  '{"userName":"bjensen","password":"Password1","mail":"bjensen@example.com","sn":"Jensen","givenName":"Barbara"}' \
   "http://localhost:8080/openidm/managed/user/bjensen"
   {
     "_id": "bjensen",
     "_rev": "revision",
     "userName": "bjensen",
     "mail": "bjensen@example.com",
     "sn": "Jensen",
     "givenName": "Barbara",
     "accountStatus": "active",
     "effectiveAssignments": [],
     "effectiveRoles": []
   }
   ```

### Prepare DS

1. [Download DS 8.1](https://backstage.forgerock.com/downloads).

2. Unzip DS:

   ```
   unzip -q ~/Downloads/DS-8.1.zip -d /path/to
   ```

3. Generate a DS deploymentId for DS setup and managing deployments:

   ```
   /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-ID
   ```

4. Set up and start DS with data from an IDM example that includes Barbara Jensen's entry:

   ```
   /path/to/opendj/setup \
   --serverId evaluation-only \
   --deploymentId your-deployment-ID \
   --deploymentIdPassword password \
   --rootUserDn uid=admin \
   --rootUserPassword password \
   --hostname localhost \
   --adminConnectorPort 4444 \
   --ldapsPort 1636 \
   --profile ds-user-data \
   --set ds-user-data/baseDn:dc=com \
   --set ds-user-data/ldifFile:/path/to/openidm/samples/sync-with-ldap/data/Example.ldif \
   --start \
   --acceptLicense
   ```

   The sample data includes an entry for Barbara Jensen. The rest of the sample configuration is not used here.

5. Check that the directory superuser can read Barbara Jensen's entry in the directory:

   ```
   /path/to/opendj/bin/ldapsearch \
   --port 1636 \
   --useSSL \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDn uid=admin \
   --bindPassword password \
   --baseDn dc=com \
   "(uid=bjensen)"
   dn: uid=bjensen,ou=People,dc=example,dc=com
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   objectClass: top
   cn: Barbara Jensen
   description: Created for OpenIDM
   givenName: Barbara
   mail: bjensen@example.com
   sn: Jensen
   telephoneNumber: 1-360-229-7105
   uid: bjensen
   userPassword: {PBKDF2-HMAC-SHA256}10:hash
   ```

   Notice that this entry differs from the account you added to IDM. However, the user identifier is `bjensen` in both cases. This will let IDM identify Barbara Jensen's account as the one whose password has changed when it receives the notification from DS.

## Secure communication between IDM and DS

The password synchronization plugin encrypts passwords using IDM's public key. IDM then uses its private key to decrypt the password.

This section describes how to export IDM's certificate, containing its public key, to DS so that the password synchronization plugin can use the public key to encrypt the password. The same certificate is used by the plugin to trust the SSL certificate that is provided by IDM.

There are four possible modes of communication between the DS password synchronization plugin and IDM:

* SSL Authentication

  For this communication mode, you must import [IDM's certificate into the DS truststore](#import-openidm-cert) (either the self-signed certificate that is generated the first time IDM starts, or a CA-signed certificate).

* Mutual SSL Authentication

  |   |                                                                                                |
  | - | ---------------------------------------------------------------------------------------------- |
  |   | Mutual SSL authentication is the default configuration of the password synchronization plugin. |

  For this communication mode, you must:

  * [Import the IDM certificate into the DS truststore](#import-openidm-cert).

  * [Import the DS CA certificate into the IDM truststore](#import-ds-cert).

  * [Add the DS certificate subject DN](#pwd-sync-idm-config) as a value of the `allowedAuthenticationIdPatterns` property in your project's `conf/authentication.json` file.

* AM Bearer Tokens

  When you use IDM and AM together as a platform, configure the password synchronization plugin to use AM bearer tokens for authentication.

  For this communication mode, you must:

  * [Import the IDM certificate into the DS truststore](#import-openidm-cert).

  * [Import the DS CA certificate into the IDM truststore](#import-ds-cert).

  * [Configure the password synchronization plugin to accept AM bearer tokens](#pwd-sync-am-tokens).

* HTTP Basic Authentication

  |   |                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------- |
  |   | IDM supports basic authentication for ***testing purposes only***. Do *not* use basic authentication in production. |

  For this mode, the connection is secured using a username and password, rather than any exchange of certificates. Because the password sync plugin requires the IDM certificate to encrypt/decrypt passwords, you must [import the IDM certificate into the DS truststore](#import-openidm-cert).

  For this communication mode, you must:

  * [Import the IDM certificate into the DS truststore](#import-openidm-cert).

  * Set the following properties in the plugin configuration:

    * `openidm-url`

    * `openidm-username`

    * `openidm-password`

### Enable DS to trust the IDM certificate

The first time IDM starts, it generates a self-signed certificate. This procedure uses the self-signed certificate to demonstrate how to get the password synchronization plugin up and running. In a production environment, use a certificate that has been signed by a Certificate Authority (CA).

The default Java truststore contains signing certificates from well-known CAs. If your CA certificate is not in the default truststore, or if you are using a self-signed certificate, import it into the DS keystore, as described here.

1. Export the IDM self-signed certificate to a file, as follows:

   ```
   keytool \
   -export \
   -alias openidm-localhost \
   -file openidm-localhost.crt \
   -keystore /path/to/openidm/security/keystore.jceks \
   -storetype jceks \
   -storepass changeit
   Certificate stored in file <openidm-localhost.crt>
   ```

   The default IDM keystore password is `changeit`.

2. Import the self-signed certificate into the DS keystore:

   ```
   keytool \
   -import \
   -alias openidm-localhost \
   -file openidm-localhost.crt \
   -keystore /path/to/opendj/config/keystore \
   -storepass:file /path/to/opendj/config/keystore.pin \
   -storetype PKCS12 \
   -noprompt
   Certificate was added to keystore
   ```

3. Check that the IDM certificate is in the DS keystore:

   ```
   keytool \
   -list \
   -keystore /path/to/opendj/config/keystore \
   -storepass:file /path/to/opendj/config/keystore.pin
   ...
   openidm-localhost, date, trustedCertEntry,
   Certificate fingerprint (SHA-256): fingerprint
   ...
   ```

### Enable IDM to trust DS certificates

For mutual SSL authentication, you must also import a trusted DS certificate into the IDM truststore, either a trusted CA certificate, or the CA certificate that is generated by the DS deploymentId and deploymentIdPassword. For more information, refer to [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-keys) in the *DS Security Guide*. This procedure uses the CA certificate generated by the DS deploymentId and deploymentIdPassword.

1. Run the following command on your DS server to export the CA certificate to a file. Substitute the values for `--deploymentId` and `--deploymentIdPassword` with the values from when you set up the DS server:

   ```
   /path/to/opendj/bin/dskeymgr \
   export-ca-cert \
   --deploymentId your-deployment-ID \
   --deploymentIdPassword password \
   --outputFile ssl-key-pair.pem
   ```

2. Import the DS CA certificate into the IDM truststore:

   ```
   keytool \
   -importcert \
   -alias ssl-key-pair \
   -keystore /path/to/openidm/security/truststore \
   -storepass changeit \
   -file ssl-key-pair.pem
   Owner: CN=Deployment key, O=ForgeRock.com
   Issuer: CN=Deployment key, O=ForgeRock.com
   ...
   Trust this certificate? [no]: yes
   Certificate was added to keystore
   ```

3. Check that the DS CA certificate is in the IDM truststore:

   ```
   keytool \
   -list \
   -keystore /path/to/openidm/security/truststore \
   -storepass changeit...
   ssl-key-pair, date, trustedCertEntry,
   Certificate fingerprint (SHA-256): fingerprint...
   ```

4. Restart IDM:

   ```
   /path/to/openidm/shutdown.sh; /path/to/openidm/startup.sh
   ```

### Configure the plugin for AM bearer tokens

This procedure uses the [sample platform setup](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/preface.html) documentation as the basis for setting up IDM to use AM bearer tokens for authentication and may need adjustment for your specific environment.

1. Perform [sample platform setup - shared identity store](https://backstage.forgerock.com/docs/platform/7.5/platform-setup-guide/deployment2.html) using the following settings during the applicable steps:

   > **Collapse: Configuration Store**
   >
   > * adminConnectorPort 4444
   >
   > * ldapPort 1389
   >
   > * enableStartTls
   >
   > * ldapsPort 1636
   >
   > * httpsPort 8443
   >
   > * replicationPort 8989
   >
   > * deploymentId your-deployment-ID

   > **Collapse: Identity Store**
   >
   > * adminConnectorPort 4445
   >
   > * ldapPort 1390
   >
   > * ldapsPort 1637
   >
   > * replicationPort 8990
   >
   > * deploymentId your-deployment-ID

   > **Collapse: Tomcat - AM**
   >
   > * port: 8080
   >
   > * redirects: 8444

   > **Collapse:&#x20;**
   >
   > * openidm.port.http=8081
   >
   > * openidm.port.https=8445
   >
   > * openidm.port.mutualauth=8446
   >
   > * openidm.host=openidm.example.com
   >
   > * openidm.auth.clientauthonlyports=8446

2. Configure a `ds-password-sync-plugin` OAuth Client for the Password Sync Plugin:

   * If you're not currently logged in to the AM console as the `amAdmin` user, log in.

   * In the Top Level Realm, select Applications > OAuth 2.0 > Clients, and click Add Client.

   * Enter the following details:

     * Client ID : `ds-password-sync-plugin`

     * Client secret : `ds-password-sync-plugin`

     * Scopes : `fr:idm:*, openid, am-introspect-all-tokens, am-introspect-all-tokens-any-realm`

   * Click Create.

   * On the Advanced tab:

     * Token Endpoint Authentication Method: Select `client_secret_post`.

     * Grant Types: Add `Client Credentials`.

   * Click Save Changes.

3. If you haven't performed the following procedures, do that now:

   * [Import the IDM certificate into the DS truststore](#import-openidm-cert).

   * [Import the DS CA certificate into the IDM truststore](#import-ds-cert).

4. Add `openidm-localhost` to the `idm.default` mapping alias array in your project's `conf/secrets.json` file:

   ```json
   "mappings": [
     {
       "secretId": "idm.default",
       "types": [ "ENCRYPT", "DECRYPT" ],
       "aliases": [ "&{openidm.config.crypto.alias|openidm-sym-default}", "openidm-localhost" ]
     },
     ...
   ]
   ```

5. Log in to the IDM admin UI as `amAdmin` and create a new managed/user:

   * On the navigation bar of the admin UI, select Manage > User, and then click + New User.

   * On the New User page, enter the Username`ds-password-sync-plugin`, other information, as necessary, and click Save.

   * On the ds-password-sync-plugin user page, select the Authorization Roles tab.

   * Click Add Authorization Roles, select all of the following roles, and then click Add:

     * `openidm-admin`

     * `openidm-authorized`

     * `openidm-cert`

     * `openidm-reg`

6. Add a `staticUserMapping` for the `ds-password-sync-plugin` user to the `conf/authentication.json` file:

   ```json
   {
     "subject" : "ds-password-sync-plugin",
     "localUser" : "managed/user/ds-password-sync-plugin",
     "roles" : [
       "internal/role/openidm-authorized",
       "internal/role/openidm-admin"
     ]
   }
   ```

## Install and configure the DS plugin

The following steps install the password synchronization plugin on a DS directory server that is running on the same host as IDM (localhost). If you are running DS on a different host, use the fully qualified domain name instead of `localhost`.

You must use the plugin version that corresponds to your IDM and DS versions. For more information, refer to [Supported Password Synchronization Plugins](../release-notes/before-you-install.html#plugin-compatibility). This procedure assumes that you are using IDM 8.1, DS 8.1, and version 8.1 of the password synchronization plugin.

Depending on whether you are using IDM with AM, select one of the following plugin installation and configuration procedures:

### For regular IDM authentication

1. [Download the password synchronization plugin](https://backstage.forgerock.com/downloads).

2. Extract the .zip file contents to the DS installation directory:

   ```
   unzip ~/Downloads/DS-IDM-account-change-notification-handler-8.1.zip -d /path/to/opendj/
   ```

3. Restart DS to load the additional schema from the password synchronization plugin:

   ```
   /path/to/opendj/bin/stop-ds --restart
   Stopping Server...
   ...msg=Loaded extension from file '/path/to/opendj/lib/extensions/opendj-openidm-account-change-notification-handler-8.1.jar'
   ...
   ...msg=The Directory Server has started successfully
   ```

4. Configure the password synchronization plugin:

   ```
   /path/to/opendj/bin/dsconfig \
   create-account-status-notification-handler \
   --type openidm \
   --handler-name "OpenIDM Notification Handler" \
   --set enabled:true \
   --set openidm-url:https://openidm-localhost:8444/openidm/managed/user \
   --set private-key-alias:openidm-localhost \
   --set certificate-subject-dn:"CN=openidm-localhost, O=OpenIDM Self-Signed Certificate, OU=None, L=None, ST=None, C=None" \
   --set ssl-cert-nickname:ssl-key-pair \
   --set key-manager-provider:PKCS12 \
   --set trust-manager-provider:PKCS12 \
   --set password-attribute:password \
   --set attribute-type:entryUUID \
   --set attribute-type:uid \
   --set query-id:for-userName \
   --set log-file:logs/pwsync \
   --set update-interval:5s \
   --set request-retry-attempts:5000 \
   --hostname localhost \
   --port 4444 \
   --bindDn uid=admin \
   --bindPassword password \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --no-prompt
   The Openidm Account Status Notification Handler was created successfully
   ```

   Adapt the settings to match your DS and IDM deployments:

   | Setting                  | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | `enabled`                | Enables the plugin.Leave this setting as shown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | `openidm-url`            | The endpoint where the plugin finds IDM managed user accounts.Port `8444` is the IDM default for mutual TLS connections.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | `private-key-alias`      | The IDM private key, used to decrypt the JSON objects from DS that contain passwords.The example references the default IDM private key of the self-signed key pair generated at setup time.                                                                                                                                                                                                                                                                                                                                                                                   |
   | `certificate-subject-dn` | The certificate subject DN for the IDM public key.The DS plugin encrypts JSON objects with the IDM public key, so this must match the certificate for the IDM private key specified for the `private-key-alias` property.The example shows the subject DN of the default IDM self-signed certificate.                                                                                                                                                                                                                                                                          |
   | `ssl-cert-nickname`      | The alias of the DS TLS certificate used to authenticate to IDM.The example uses the default DS server certificate generated at setup time.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | `key-manager-provider`   | The provider for the keystore where DS finds its TLS key pair specified in `ssl-cert-nickname`.The example uses the default DS provider configured at setup time.                                                                                                                                                                                                                                                                                                                                                                                                              |
   | `trust-manager-provider` | The provider for the keystore where DS finds the IDM public key specified in `certificate-subject-dn`.The example uses the default DS provider configured at setup time, and updated in [Enable DS to Trust the IDM Certificate](#import-openidm-cert).                                                                                                                                                                                                                                                                                                                        |
   | `password-attribute`     | The name of the password field in the JSON that DS sends to IDM for a password change.This attribute type must be defined in the managed object schema in IDM, and it must have either the user password or auth password syntax.                                                                                                                                                                                                                                                                                                                                              |
   | `attribute-type`         | LDAP attributes that the DS plugin sends to IDM with the password. IDM can use these to uniquely identify the user, even if the user's account has moved.If no attribute types are specified, DS sends only the DN and the new password to IDM.                                                                                                                                                                                                                                                                                                                                |
   | `query-id`               | The query-id for the patch-by-query request.Leave this setting as shown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | `log-file`               | The DS directory where the plugin writes log files containing encrypted passwords before notifying IDM.This setting has no effect in the example, where the `update-interval` is zero seconds.                                                                                                                                                                                                                                                                                                                                                                                 |
   | `update-interval`        | The interval at which the DS plugin sends password changes to IDM.If this value is zero, the plugin sends updates synchronously. No encrypted passwords are stored in the configured `log-file` directory. The plugin does not retry failed requests, irrespective of the `request-retry-attempts` setting.                                                                                                                                                                                                                                                                    |
   | `request-retry-attempts` | The number of times the plugin attempts a synchronization request if the first attempt fails. If this value is zero, the request is not retried. If the value is greater than zero, the plugin retries the specified number of times before giving up and removing the request from its queue.When a request fails due to a transient condition, such as failure to contact IDM, or a connection timeout, the plugin does not decrement the number of retry attempts. The plugin logs a message with the reason the request failed, and continues to retry until IDM responds. |

5. Restart DS for the new configuration to take effect:

   ```
   /path/to/opendj/bin/stop-ds --restart
   ```

6. Update DS password policies to use the password synchronization plugin.

   The following example updates the default DS password policy:

   ```
   /path/to/opendj/bin/dsconfig \
   set-password-policy-prop \
   --policy-name "Default Password Policy" \
   --set account-status-notification-handler:"OpenIDM Notification Handler" \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --no-prompt
   ```

   For details on configuring DS password policies, refer to [Passwords](https://docs.pingidentity.com/pingds/8.1/security-guide/passwords.html) in the *DS Security Guide*.

#### Configure IDM for password synchronization

The password synchronization plugin uses client certificate authentication to authenticate to IDM. You must also update your security configuration to add the IDM key alias.

1. If your authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint, or directly in the conf/authentication.json file.)* does not already include client certificate authentication, configure it as follows:

   1. Add the `CLIENT_CERT` authentication module to your authentication configuration *(tooltip: You can manage the authentication configuration over REST at the config/authentication endpoint, or directly in the conf/authentication.json file.)*.

   2. Set the `allowedAuthenticationIdPatterns` property to the certificate DN of the DS SSL certificate (`ssl-key-pair` by default).

   3. Add `internal/role/openidm-cert` to the array of `defaultUserRoles`.

   The following example assumes that you are using the default DS `ssl-key-pair` certificate that has a certificate subject DN of `CN=DS, O=ForgeRock`:

   ```json
   "authModules" : [
       ...
       {
           "name" : "CLIENT_CERT",
           "properties" : {
               "queryOnResource" : "managed/user",
               "defaultUserRoles" : [
                   "internal/role/openidm-cert",
                   "internal/role/openidm-authorized"
               ],
               "allowedAuthenticationIdPatterns" : [
                   ".*CN=DS, O=ForgeRock.com.*"
               ]
           },
           "enabled" : true
       },
       ...
   ]
   ```

   For more information about client certificate authentication, refer to [CLIENT\_CERT](../auth-guide/auth-session-modules.html#client-cert-module).

2. Update the IDM secret store (`conf/secrets.json` ) to add the alias used in the `private-key-alias` plugin setting to the `idm.default` secretId:

   ```json
   "mappings": [
       {
           "secretId" : "idm.default",
           "types": [ "ENCRYPT", "DECRYPT" ],
           "aliases": [ "&{openidm.config.crypto.alias|openidm-sym-default}", "openidm-localhost" ]
       },
       ...
   ]
   ```

   For more information about secret stores, refer to [Secret stores](../security-guide/secret-stores.html).

### For authentication with AM bearer tokens

1. [Download the password synchronization plugin](https://backstage.forgerock.com/downloads).

2. Extract the .zip file contents to the DS identity store installation directory:

   ```
   unzip ~/Downloads/DS-IDM-account-change-notification-handler-8.1.zip -d /path/to/opendj-identity/
   ```

3. Configure the password synchronization plugin to use AM bearer token authentication:

   ```
   /path/to/opendj-identity/bin/dsconfig \
   create-account-status-notification-handler \
   --type openidm \
   --handler-name "OpenIDM Notification Handler" \
   --set certificate-subject-dn:"CN=openidm-localhost,O=OpenIDM Self-Signed Certificate,OU=None,L=None,ST=None,C=None" \
   --set enabled:true \
   --set attribute-type:entryUUID \
   --set attribute-type:uid \
   --set trust-manager-provider:PKCS12 \
   --set key-manager-provider:PKCS12 \
   --hostname identities.example.com \
   --port 4445 \
   --bindDn uid=admin \
   --trustAll \
   --bindPassword str0ngAdm1nPa55word \
   --set log-file:logs/pwsync \
   --set password-attribute:password \
   --set query-id:for-userName \
   --set private-key-alias:openidm-localhost \
   --set openidm-url:https://openidm-localhost:8445/openidm/managed/user \
   --set oauth2-access-token-url:http://am.example.com:8080/openam/oauth2/realms/root/access_token \
   --set oauth2-scope:"openid fr:idm:*" \
   --set oauth2-client-id:ds-password-sync-plugin \
   --set oauth2-client-secret:ds-password-sync-plugin \
   --set request-retry-attempts:5000 \
   --set update-interval:5s \
   --no-prompt
   The Openidm Account Status Notification Handler was created successfully
   ```

   |   |                                                                     |
   | - | ------------------------------------------------------------------- |
   |   | Adapt the above settings to match your DS, IDM, and AM deployments. |

4. Restart DS for the new configuration to take effect:

   ```
   /path/to/opendj-identity/bin/stop-ds --restart
   ```

5. Configure the DS password policy to use the password synchronization plugin. The following example updates the default DS password policy:

   ```
   /path/to/opendj-identity/bin/dsconfig \
   set-password-policy-prop \
   --policy-name "Default Password Policy" \
   --set account-status-notification-handler:"OpenIDM Notification Handler" \
   --hostname identities.example.com \
   --port 4445 \
   --bindDN uid=admin \
   --bindPassword str0ngAdm1nPa55word \
   --usePkcs12TrustStore /path/to/opendj-identity/config/keystore \
   --trustStorePassword:file /path/to/opendj-identity/config/keystore.pin \
   --no-prompt
   ```

   Learn more about DS [passwords policies](https://docs.pingidentity.com/pingds/8.1/security-guide/passwords.html) in the *DS Security Guide*.

6. Generate an AM bearer token. For example:

   ```
   curl -k \
   --request POST \
   --user "ds-password-sync-plugin:ds-password-sync-plugin" \
   --data "grant_type=client_credentials" \
   --data "scope=openid fr:idm:*" \
   "http://am.example.com:8080/openam/oauth2/realms/root/access_token"
   {
     "access_token": "access_token",
     "scope": "openid fr:idm:*",
     "id_token": "id_token",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

7. Optionally, to test the AM bearer token, create a new managed user using the token as the authorization. For example:

   ```
   curl -v \
   --header "Authorization: Bearer access_token" \
   --header "accept: application/json" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST "http://openidm-localhost:8081/openidm/managed/user?_action=create" \
   --data '{"userName":"jdoe", "password": "6fNcHgBF", "mail": "jdoe@example.com", "sn": "Doe", "givenName": "Jane"}'
   {
     "_id": "7884b8ab-a226-4ee5-b9b9-0718f5a19335",
     "_rev": "00000000f527116e",
     "userName": "jdoe",
     "accountStatus": "active",
     "givenName": "Jane",
     "sn": "Doe",
     "mail": "jdoe@example.com"
   }
   ```

## Test the DS plugin

With the plugin installed and configured, and with secure communications enabled between DS and IDM, you can test that the setup has been successful as follows:

1. Change a user password in DS:

   ```
   /path/to/opendj/bin/ldappasswordmodify \
   --hostname localhost \
   --port 1636 \
   --useSsl \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --bindDN uid=admin \
   --bindPassword password \
   --authzID dn:uid=bjensen,ou=people,dc=example,dc=com \
   --newPassword Chngth5pwd
   The LDAP password modify operation was successful
   ```

   The message `The LDAP password modify operation was successful` only indicates that the password change succeeded for DS. This does not mean that DS has propagated the change to IDM.

   When you have successfully updated the password in DS, DS attempts to synchronize the change to the corresponding IDM managed user account.

2. You should now be able to log in to the end-user UI (https\://localhost:8443/#login/) as that user ID with the new password.

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

   > **Collapse: Show login process**
   >
   > ```
   > chromium --ignore-certificate-errors https://localhost:8443/#login
   > ```
   >
   > ![Image shows Barbara Jensen's credentials on the login page.](_images/dj-pwd-sync-login-as-bjensen.png)
   >
   > ![Image shows Barbara Jensen's account page.](_images/dj-pwd-sync-logged-in.png)

## Update the DS plugin

Additional steps may be necessary when updating the DS password synchronization plugin after upgrading DS. Check the corresponding [Knowledge Base article](https://backstage.forgerock.com/knowledge/kb/article/a23668219) for more information.

## Uninstall the DS plugin

To uninstall the plugin, change the DS configuration as follows:

1. Reset your DS password policy configuration so that it no longer uses the password synchronization plugin.

   The following command resets the default password policy:

   ```
   /path/to/opendj/bin/dsconfig \
   set-password-policy-prop \
   --policy-name "Default Password Policy" \
   --reset account-status-notification-handler \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --no-prompt
   ```

2. Delete the IDM Notification Handler from the DS configuration:

   ```
   /path/to/opendj/bin/dsconfig \
   delete-account-status-notification-handler \
   --handler-name "OpenIDM Notification Handler" \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --no-prompt
   The Account Status Notification Handler was deleted successfully
   ```

3. Remove the password synchronization plugin from the DS extensions:

   ```
   rm /path/to/opendj/lib/extensions/opendj-openidm-account-change-notification-handler
   ```

4. Restart DS for the new configuration to take effect:

   ```
   /path/to/opendj/bin/stop-ds --restart
   ```

---

---
title: Uninstall the Active Directory password synchronization plugin
description: Uninstall the Active Directory password synchronization plugin and remove its authentication certificates from Windows
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:remove-ad-pwd-sync
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/remove-ad-pwd-sync.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Active Directory", "Uninstall"]
section_ids:
  ad-remove-certificates: Remove installed authentication certificates
---

# Uninstall the Active Directory password synchronization plugin

You can uninstall the Active Directory Password Synchronization plugin from multiple locations:

* Uninstall from the Windows Control Panel (Control Panel > Programs and Features, select `OpenIDM Password Sync` from the list and select Uninstall).

* Run the uninstaller (`unins000.exe` ) found in the OpenIDM Password Sync install directory (by default, `C:\Program Files\OpenIDM Password Sync`).

After the uninstaller finishes, Windows will prompt you to restart. Restart to complete the uninstall process.

## Remove installed authentication certificates

If you selected to authenticate with mutual SSL authentication, you can manually remove the IDM certificates using the Microsoft Management Console:

1. Click the Start Menu, type mmc, and click mmc Run Command.

2. For each of the following nodes, expand the node, and delete the certificate.

   **List of Nodes**

   |                                                                                       |
   | ------------------------------------------------------------------------------------- |
   | Certificates - Current User > Personal                                                |
   | Certificates - Current User > Trusted Root Certification Authorities                  |
   | Certificates - Service > OpenIDM Password Sync\Personal                               |
   | Certificates - Service > OpenIDM Password Sync\Trusted Root Certification Authorities |
   | Certificates > Local Computer > Personal                                              |
   | Certificates > Local Computer > Trusted Root Certification Authorities                |

3. If the OpenIDM Password Sync Service is still listed with stored certificates:

   1. Select File > Add/Remove Snap-in.

   2. From the Selected snap-ins area, select Certificates - OpenIDM Password Sync, and click Remove.

   3. Click OK.

---

---
title: Upgrade the Active Directory password synchronization plugin
description: Upgrade the Active Directory password synchronization plugin by running the installer over an existing configuration
component: pingidm
version: 8.1
page_id: pingidm:pwd-plugin-guide:upgrade-ad-pwd
canonical_url: https://docs.pingidentity.com/pingidm/8.1/pwd-plugin-guide/upgrade-ad-pwd.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Password", "Synchronization", "Plugins", "Active Directory", "Upgrade"]
---

# Upgrade the Active Directory password synchronization plugin

To upgrade the Active Directory password synchronization plugin, you can run the installer over an existing configuration. For more information about installation, refer to [Install the Active Directory password synchronization plugin](install-ad-pwd-sync.html).
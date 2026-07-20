---
title: Adjust log levels
description: Set PingIDM log levels to INFO in production to capture diagnostic information without exposing unnecessary details
component: pingidm
version: 8.1
page_id: pingidm:security-guide:security-adjust-log-levels
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/security-adjust-log-levels.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Logs"]
---

# Adjust log levels

In production, set log levels to `INFO` to ensure that you capture enough information to help diagnose issues, but do not expose unnecessary information. For more information, refer to [Server logs](../monitoring-guide/server-logs.html).

At startup and shutdown, `INFO` can produce many messages. During stable operation, `INFO` generally results in log messages only when coarse-grain operations such as scheduled reconciliation start or stop.

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default IDM log formatter encodes all control characters (such as newline characters) using URL-encoding, to protect against log forgery. For more information, refer to [Server logs](../monitoring-guide/server-logs.html). |

---

---
title: CA-signed certificates
description: Import CA-signed certificates into the PingIDM keystore and truststore, and delete unused default and root CA certificates
component: pingidm
version: 8.1
page_id: pingidm:security-guide:ca-signed-certs
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/ca-signed-certs.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Certificates", "CA-signed Certificates", "Root-CA Certificates", "Keystores", "Keytool", "Truststores", "Java"]
section_ids:
  import-signed-cert: Import CA-signed certificates
  delete-certificates: Delete certificates
  security-keystore: Delete root CA certificates
---

# CA-signed certificates

You can use existing CA-signed certificates to secure connections and data by importing the certificates into the keystore, and referencing them your `boot.properties` file. Use the `keytool` command to import an existing certificate into the keystore.

## Import CA-signed certificates

The following process imports a CA-signed certificate into the keystore, with the alias example-com. Replace this alias with the alias of your certificate:

1. Stop the server if it is running.

2. Back up your existing `openidm/security/keystore` and `openidm/security/truststore` files.

3. Use the `keytool` command to import your existing certificate into the keystore, substituting your specific information:

   |                                 |                                    |
   | ------------------------------- | ---------------------------------- |
   | `example-cert.p12`              | The name of your certificate file. |
   | `srcstorepass`                  | The certificate password.          |
   | `example-com`                   | The existing certificate alias.    |
   | `destination keystore password` | The password for the keystore.     |

   ```bash
   keytool \
   -importkeystore \
   -srckeystore example-cert.p12 \
   -srcstoretype PKCS12 \
   -srcstorepass changeit \
   -srcalias example-com \
   -destkeystore keystore.jceks \
   -deststoretype JCEKS \
   -destalias openidm-localhost
   Importing keystore example-cert.p12 to keystore.jceks...
   Enter destination keystore password: changeit
   ```

   The keytool command creates a trusted certificate entry with the specified alias and associates it with the imported certificate. The certificate is imported into the keystore with the alias `openidm-localhost`. If you want to use a different alias, you must modify your `resolver/boot.properties` file to reference that alias, as shown in the following step.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The certificate entry password must be the same as the IDM keystore password. If the source certificate entry password is different from the target keystore password, use the `-destkeypass` option with the same value as the `-deststorepass` option to make the certificate password match the target keystore password. If you do not make these passwords the same, no error is generated when you import the certificate (or when you read the certificate entry in the destination keystore), but IDM will fail to start with the following exception:```
   java.security.UnrecoverableKeyException: Given final block not properly padded.
   ``` |

4. If you specified an alias other than `openidm-localhost` for the new certificate, change the value of `openidm.https.keystore.cert.alias` in your `resolver/boot.properties` file to that alias. For example, if your new certificate alias is `example-com`, change the `boot.properties` file as follows:

   ```properties
   openidm.https.keystore.cert.alias=example-com
   ```

5. Restart the server.

## Delete certificates

When using CA-signed certificates for encryption, it is a best practice to delete *all* unused default certificates from the keystore and truststore using the `keytool` command, as shown in the following examples:

* To delete the `openidm-localhost` certificate from the keystore:

  ```
  keytool \
  -delete \
  -alias openidm-localhost \
  -keystore /path/to/openidm/security/keystore.jceks \
  -storetype JCEKS \
  -storepass changeit
  ```

* To delete the `openidm-localhost` certificate from the truststore:

  ```
  keytool \
  -delete \
  -alias openidm-localhost \
  -keystore /path/to/openidm/security/truststore \
  -storepass changeit
  ```

You can use similar commands to delete custom certificates from the keystore and truststore, specifying the certificate alias in the request.

## Delete root CA certificates

The Java and IDM truststore files include a number of root CA certificates. Although the probability of a compromised root CA certificate is low, it is a best practice to delete unused root CA certificates.

To review the list of root CA certificates in the IDM truststore:

```
keytool \
-list \
-keystore /path/to/openidm/security/truststore \
-storepass changeit
```

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | On UNIX/Linux systems, you can find additional lists of root CA certificates in files named `cacerts`. These include root CA certificates associated with your Java environment, typically located in the `${JAVA_HOME}/jre/lib/security/cacerts` directory. |

Before making changes to Java environment keystore files, verify any Java-related `cacerts` files are up-to-date and that you have a [supported Java version installed](../install-guide/verify-java.html).

You can delete root CA certificates with the `keytool` command. For example, to remove the hypothetical `examplecomca2` certificate from the truststore:

```
keytool \
-delete \
-keystore /path/to/openidm/security/truststore \
-storepass changeit \
-alias examplecomca2
```

|   |                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | On Windows systems, you can manage certificates with the Microsoft Management Console (MMC) snap-in tool. For more information, refer to [Working With Certificates](https://msdn.microsoft.com/en-us/library/ms788967\(v=vs.110\).aspx). |

---

---
title: Disable automatic configuration updates
description: Disable PingIDM automatic configuration updates and file-based config writes to prevent untested changes in production
component: pingidm
version: 8.1
page_id: pingidm:security-guide:disabling-auto-config-updates
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/disabling-auto-config-updates.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Configuration", "Updates"]
section_ids:
  disable_configuration_file_writes: Disable configuration file writes
---

# Disable automatic configuration updates

By default, IDM monitors files in the `conf` directory periodically for any changes to the configuration. This functionality is configured in the following properties in your `conf/system.properties` file:

* `openidm.fileinstall.poll`

  Sets the interval at which files are polled for changes. `2000` milliseconds by default.

* `openidm.fileinstall.enabled`

  Specifies whether files should be monitored. `true` by default. In a production system, you should disable automatic polling for updates to prevent untested configuration changes from disrupting your identity service. Setting this property to `false` also disables the file-based configuration view, which means that IDM reads its configuration only from the repository.

  |   |                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If `openidm.fileinstall.enabled=true`, IDM immediately uses any changes made to scripts embedded directly in your JSON configuration files. |

* `openidm.config.bootstrap.enabled`

  Allows IDM to start up and load configuration when there aren't currently any configs stored in the repository. `true` by default.

* `openidm.fileinstall.filter`

  Specify which file types should be monitored (if `openidm.fileinstall.enabled=true`). File types are specified in a pipe-separated list, for example:

  ```properties
  openidm.fileinstall.filter=.*\\.cfg|.*\\.json
  ```

## Disable configuration file writes

To disable *writes* to configuration files, set the following property to `false` in your `conf/config.properties` file:

```properties
felix.fileinstall.enableConfigSave=false
```

This setting is suitable for read-only installations.

---

---
title: Encrypt and decrypt properties over REST
description: Encrypt and decrypt property values over the PingIDM REST interface using the openidm.encrypt and openidm.decrypt script functions
component: pingidm
version: 8.1
page_id: pingidm:security-guide:keystore-encrypt-decrypt
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/keystore-encrypt-decrypt.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Encryption", "Decryption", "REST"]
---

# Encrypt and decrypt properties over REST

The `openidm.encrypt` and `openidm.decrypt` functions of the Resource API enable you to encrypt and decrypt property values. To use these functions over the REST interface, run the `?_action=eval` action on the `script` endpoint.

The following example uses the `openidm.encrypt` function to encrypt a password value:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--cacert ca-cert.pem \
--request POST \
--data '{
  "type": "text/javascript",
  "globals": {
    "val": {
      "myKey": "myPassword"
    }
  },
  "source":"openidm.encrypt(val,null,\"idm.password.encryption\");"
}' \
"https://localhost:8443/openidm/script?_action=eval"
{
  "$crypto": {
    "type": "x-simple-encryption",
    "value": {
      "cipher": "AES/CBC/PKCS5Padding",
      "stableId": "openidm-sym-default",
      "salt": "qAS/eG7zdnFyK5H8lXvqTA==",
      "data": "zewf6hR1yjp34EFJqUGpdnzzFCPJs2IaX4V97jdQlSI=",
      "keySize": 16,
      "purpose": "idm.password.encryption",
      "iv": "A4pIiY6kG6t0uLyLmJAoWQ==",
      "mac": "sFDJqg0Mmp0Ftl+1q1Bjzw=="
    }
  }
}
```

The following example uses the `openidm.decrypt` function to decrypt the password value:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Content-Type: application/json" \
--cacert ca-cert.pem \
--request POST \
--data '{
  "type": "text/javascript",
  "globals": {
    "val": {
      "$crypto": {
        "type": "x-simple-encryption",
        "value": {
          "cipher": "AES/CBC/PKCS5Padding",
          "stableId": "openidm-sym-default",
          "salt": "qAS/eG7zdnFyK5H8lXvqTA==",
          "data": "zewf6hR1yjp34EFJqUGpdnzzFCPJs2IaX4V97jdQlSI=",
          "keySize": 16,
          "purpose": "idm.password.encryption",
          "iv": "A4pIiY6kG6t0uLyLmJAoWQ==",
          "mac": "sFDJqg0Mmp0Ftl+1q1Bjzw=="
        }
      }
    }
  },
  "source":"openidm.decrypt(val);"
}' \
"https://localhost:8443/openidm/script?_action=eval"
{
  "myKey": "myPassword"
}
```

For more information, refer to [`openidm.encrypt`](../scripting-guide/scripting-func-ref.html#function-encrypt) and [`openidm.decrypt`](../scripting-guide/scripting-func-ref.html#function-decrypt).

---

---
title: Encrypted objects
description: Understand the structure of PingIDM encrypted objects, including the $crypto blob format, cipher properties, key alias, and secret ID
component: pingidm
version: 8.1
page_id: pingidm:security-guide:encrypted-objects
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/encrypted-objects.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Encryption", "Objects"]
---

# Encrypted objects

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `$crypto` blob is classified as an [IDM internal object](../release-notes/appendix-interface-stability.html#table-interface-stability) and is subject to change. Don't rely on the format of this object. |

Encrypted objects and properties, such as passwords, include a `$crypto` object, that has the following structure:

```json
"password": {
  "$crypto": {
    "type": "x-simple-encryption",
    "value": {
      "cipher": "AES/CBC/PKCS5Padding",
      "stableId": "openidm-sym-default",
      "salt": "Gwi+AGrn+VBOTmyq+TTuuw==",
      "data": "+9i7XAXpWZBXYTVEOBkM+w==",
      "keySize": 16,
      "purpose": "idm.password.encryption",
      "iv": "4xtI88eFu5tgfm8ooq+yqQ==",
      "mac": "N1zsYo71M/b/G6iLOhNohA=="
    }
  }
}
```

Most of the properties in the encrypted object `value` are self-explanatory and indicate how the property was encrypted. Specific IDM properties include the following:

* The `stableId` indicates the key alias that was used to encrypt the property value.

* The `purpose` refers to the secret ID used to encrypt the property value. For more information about secret IDs, refer to [Secret stores](secret-stores.html).

---

---
title: Encryption key management
description: Rotate PingIDM encryption keys manually or on a schedule using triggerSyncCheck to re-encrypt managed objects with updated key aliases
component: pingidm
version: 8.1
page_id: pingidm:security-guide:key-mgmt
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/key-mgmt.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Encryption Keys", "Secrets", "JSON", "Managed Object", "Key Rotation"]
section_ids:
  rotating-encryption-keys: Manual key rotation
  scheduled-key-rotation: Scheduled key rotation
  changing-active-alias: Change the active alias for managed object encryption
---

# Encryption key management

Most regulatory requirements mandate that the keys used to decrypt sensitive data be rotated out and replaced with new keys on a regular basis. The main purpose of rotating encryption keys is to reduce the amount of data encrypted with that key, so that the potential impact of a security breach with a specific key is reduced. You can update encryption keys in several ways, including the following:

## Manual key rotation

IDM evaluates keys in `secrets.json` sequentially. For example, assume that you have [added a new key](ca-signed-certs.html#import-signed-cert) named `my-new-key` to the keystore. To use this new key to encrypt passwords, you would include `my-new-key` as the *first alias* in the `idm.password.encryption` secret:

```json
{
    "secretId" : "idm.password.encryption",
    "types": [ "ENCRYPT", "DECRYPT" ],
    "aliases": [ "my-new-key", "&{openidm.config.crypto.alias|openidm-sym-default}" ]
}
```

The properties that use this key (in this case, passwords) are re-encrypted with the new key the next time the managed object is *updated*. You do not need to restart the server.

|   |                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you rotate an encryption key, the *active* encryption key might not be the correct key to use for decryption of properties that have already been encrypted with a previous key.You must therefore keep all applicable keys in `secrets.json` until every object that is encrypted with old keys have been updated with the latest key. |

You can force key rotation on all managed objects by running the `triggerSyncCheck` action on the entire managed object data set. The `triggerSyncCheck` action examines the crypto blob of each object and updates the encrypted property with the correct key.

For example, the following command forces all managed user objects to use the new key:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
--header "Content-Type: application/json" \
--request POST \
"https://localhost:8443/openidm/managed/user/?_action=triggerSyncCheck"
{
    "status": "OK",
    "countTriggered": 10
}
```

In a large managed object set, the `triggerSyncCheck` action can take a long time to run on only a single node. You should therefore avoid using this action if your data set is large. An alternative to running `triggerSyncCheck` over the entire data set is to iterate over the managed data set and call `triggerSyncCheck` on each individual managed object. You can call this action manually or by using a script.

The following example shows the manual commands that must be run to launch the `triggerSyncCheck` action on all managed users. The first command uses a query filter to return all managed user IDs. The second command iterates over the returned IDs calling `triggerSyncCheck` on each ID:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
"https://localhost:8443/openidm/managed/user?_queryFilter=true&_fields=_id"
{
  "result": [
    {
      "_id": "9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb",
      "_rev": "000000004988917b"
    },
    {
      "_id": "55ef0a75-f261-47e9-a72b-f5c61c32d339",
      "_rev": "00000000dd89d671"
    },
    {
      "_id": "998a6181-d694-466a-a373-759a05840555",
      "_rev": "000000006fea54ad"
    },
    ...
  ]
}
```

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--cacert ca-cert.pem \
--header "Content-Type: application/json" \
--request POST \
"https://localhost:8443/openidm/managed/user/9dce06d4-2fc1-4830-a92b-bd35c2f6bcbb?_action=triggerSyncCheck"
```

In large data sets, the most efficient way to achieve key rotation is to use the scheduler service to launch these commands. The following section shows how to use the scheduler service for this purpose.

### Scheduled key rotation

This example uses a script to generate multiple scheduled tasks. Each scheduled task iterates over a subset of the managed object set (defined by the `pageSize`). The generated scheduled task then calls another script that launches the `triggerSyncCheck` action on each managed object in that subset.

To schedule key rotation, set up a similar schedule:

1. Create a schedule configuration named `schedule-triggerSyncCheck.json` in your project's `conf` directory. That schedule should look as follows:

   ```json
   {
       "enabled" : true,
       "persisted" : true,
       "type" : "cron",
       "schedule" : "0 * * * * ? *",
       "concurrentExecution" : false,
       "invokeService" : "script",
       "invokeContext" : {
           "waitForCompletion" : false,
           "script": {
               "type": "text/javascript",
               "name": "sync/scheduleTriggerSyncCheck.js"
           },
           "input": {
               "pageSize": 2,
               "managedObjectPath" : "managed/user",
               "quartzSchedule" : "0 * * * * ? *"
           }
       }
   }
   ```

   You can change the following parameters of this schedule configuration to suit your deployment:

   * `pageSize`

     The number of objects that each generated schedule will handle. This value should be high enough not to create too many schedules. The number of schedules that is generated is equal to the number of objects in the managed object store, divided by the page size.

     For example, if there are 500 managed users and a page size of 100, five schedules will be generated (500/100).

   * `managedObjectPath`

     The managed object set over which the scheduler iterates. For example, `managed/user` if you want to iterate over the managed user object set.

   * `quartzSchedule`

     The schedule at which these tasks should run. For example, to run the task every minute, this value would be `0 * * * * ? *`.

2. The schedule calls a `scheduleTriggerSyncCheck.js` script, located in a directory named `project-dir/script/sync`. Create the `sync` directory, and add the script:

   ```javascript
   var managedObjectPath = object.managedObjectPath;
   var pageSize = object.pageSize;
   var quartzSchedule = object.quartzSchedule;

   var managedObjects = openidm.query(managedObjectPath, {
       "_queryFilter": "true",
       "_fields": "_id"
   });

   var numberOfManagedObjects = managedObjects.result.length;

   for (var i = 0; i < numberOfManagedObjects; i += pageSize) {
       var scheduleId = java.util.UUID.randomUUID().toString();
       var ids = managedObjects.result.slice(i, i + pageSize).map(function(obj) {
           return obj._id
       });
       var schedule = newSchedule(scheduleId, ids);
       openidm.create("/scheduler", scheduleId, schedule);
   }

   function newSchedule(scheduleId, ids) {
       var schedule = {
           "enabled": true,
           "persisted": true,
           "type": "cron",
           "schedule": quartzSchedule,
           "concurrentExecution": false,
           "invokeService": "script",
           "invokeContext": {
               "waitForCompletion": true,
               "script": {
                   "type": "text/javascript",
                   "name": "sync/triggerSyncCheck.js"
               },
               "input": {
                   "ids": ids,
                   "managedObjectPath": managedObjectPath,
                   "scheduleId": scheduleId
               }
           }
       };
       return schedule;
   }
   ```

3. Each generated scheduled task calls a script named `triggerSyncCheck.js`. Create the script in your project's `script/sync` directory:

   ```javascript
   var ids = object.ids;
   var scheduleId = object.scheduleId;
   var managedObjectPath = object.managedObjectPath;

   for (var i = 0; i & lt; ids.length; i++) {
       openidm.action(managedObjectPath + "/" + ids[i], "triggerSyncCheck", {}, {});
   }

   openidm.delete("scheduler/" + scheduleId, null);
   ```

4. Test the key rotation:

   1. Edit your project's `conf/managed.json` file to return user passwords by default by setting `"scope" : "public"`.

      ```json
      "password" : {
          ...
          "encryption" : {
              "purpose" : "idm.password.encryption"
          },
          "scope" : "public",
          ...
      }
      ```

      Because passwords are not returned by default, you will not be able to refer to the new encryption on the password unless you change the property's `scope`.

   2. Perform a GET request to return any managed user entry in your data set:

      ```
      curl \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --cacert ca-cert.pem \
      --request GET \
      "https://localhost:8443/openidm/managed/user/ccd92204-aee6-4159-879a-46eeb4362807"
      {
        "_id" : "ccd92204-aee6-4159-879a-46eeb4362807",
        "_rev" : "0000000009441230",
        "preferences" : {
          "updates" : false,
          "marketing" : false
        },
        "mail" : "bjensen@example.com",
        "sn" : "Jensen",
        "givenName" : "Babs",
        "userName" : "bjensen",
        "password" : {
          "$crypto" : {
            "type" : "x-simple-encryption",
            "value" : {
              "cipher" : "AES/CBC/PKCS5Padding",
              "stableId" : "openidm-sym-default",
              "salt" : "CVrKDuzfzunXfTDbCwU1Rw==",
              "data" : "1I5tWT5aRH/12hf5DgofXA==",
              "keySize" : 16,
              "purpose" : "idm.password.encryption",
              "iv" : "LGE+jnC3ZtyvrE5pfuSvtA==",
              "mac" : "BEXQ1mftxA63dXhJO6dDZQ=="
            }
          }
        },
        "accountStatus" : "active",
        "effectiveRoles" : [ ],
        "effectiveAssignments" : [ ]
      }
      ```

      Notice that the user's password is encrypted with the default encryption key (`openidm-sym-default`).

   3. Create a new encryption key in the IDM keystore:

      ```
      keytool \
      -genseckey \
      -alias my-new-key \
      -keyalg AES \
      -keysize 128 \
      -keystore /path/to/openidm/security/keystore.jceks \
      -storetype JCEKS
      ```

   4. Shut down the server for keystore to be reloaded.

   5. Change your project's `conf/managed.json` file to change the encryption purpose for managed user passwords:

      ```json
      "password" : {
          ...
          "encryption" : {
              "purpose" : "idm.password.encryption2"
          },
          "scope" : "public",
          ...
      }
      ```

   6. Add the corresponding `purpose` to the `secrets.json` file in the `mainKeyStore` code block:

      ```json
      "idm.password.encryption2": {
        "types": [ "ENCRYPT", "DECRYPT" ],
        "aliases": [
          {
            "alias": "my-new-key"
          }
        ]
      }
      ```

   7. Restart the server and wait one minute for the scheduled task to start.

   8. Perform a GET request again to return the entry of the managed user that you returned previously:

      ```
      curl \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --cacert ca-cert.pem \
      --request GET \
      "https://localhost:8443/openidm/managed/user/ccd92204-aee6-4159-879a-46eeb4362807"
      {
        "_id" : "ccd92204-aee6-4159-879a-46eeb4362807",
        "_rev" : "0000000009441230",
        "preferences" : {
          "updates" : false,
          "marketing" : false
        },
        "mail" : "bjensen@example.com",
        "sn" : "Jensen",
        "givenName" : "Babs",
        "userName" : "bjensen",
        "password" : {
          "$crypto" : {
            "type" : "x-simple-encryption",
            "value" : {
              "cipher" : "AES/CBC/PKCS5Padding",
              "stableId" : "my-new-key",
              "salt" : "CVrKDuzfzunXfTDbCwU1Rw==",
              "data" : "1I5tWT5aRH/12hf5DgofXA==",
              "keySize" : 16,
              "purpose" : "idm.password.encryption2",
              "iv" : "LGE+jnC3ZtyvrE5pfuSvtA==",
              "mac" : "BEXQ1mftxA63dXhJO6dDZQ=="
            }
          }
        },
        "accountStatus" : "active",
        "effectiveRoles" : [ ],
        "effectiveAssignments" : [ ]
      }
      ```

      The user password is now encrypted with `my-new-key`.

## Change the active alias for managed object encryption

This example describes how to configure and then change the managed object encryption key with a scheduled task. You'll create a new key, set up a managed user, add the key to `secrets.json`, restart IDM, run a `triggerSyncCheck`, and review the result.

1. Create a new key for the IDM keystore in the `security/keystore.jceks` file:

   ```
   keytool \
   -genseckey \
   -alias my-new-key \
   -keyalg AES \
   -keysize 128 \
   -keystore /path/to/openidm/security/keystore.jceks \
   -storetype JCEKS
   ```

2. For the purpose of this example, in `managed.json`, set `"scope" : "public"` to expose the applied password encryption key.

3. Create a managed user:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --cacert ca-cert.pem \
   --header "Content-Type: application/json" \
   --request PUT \
   --data '{
     "userName": "rsutter",
     "sn": "Sutter",
     "givenName": "Rick",
     "mail": "rick@example.com",
     "telephoneNumber": "6669876987",
     "description": "Another user",
     "country": "USA",
     "password": "Passw0rd"
   }' \
   "https://localhost:8443/openidm/managed/user/ricksutter"
   ```

4. Add the newly created `my-new-key` alias to your `conf/secrets.json` file, in the `idm.password.encryption` code block:

   ```json
   "idm.password.encryption": {
     "types": [ "ENCRYPT", "DECRYPT" ],
     "aliases": [ "my-new-key", "&{openidm.config.crypto.alias|openidm-sym-default}" ]
   }
   ```

5. To apply the new key to your configuration, shut down and restart IDM.

6. Force IDM to update the key for your users with the `triggerSyncCheck` action:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --cacert ca-cert.pem \
   --header "Content-Type: application/json" \
   --request POST \
   "https://localhost:8443/openidm/managed/user/?_action=triggerSyncCheck"
   ```

7. Review the result for the newly created user, `ricksutter`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --cacert ca-cert.pem \
   --request GET  \
   "https://localhost:8443/openidm/managed/user/ricksutter"
   ```

8. In the output, you should see the new `my-new-key` encryption key applied to that user's password:

   ```json
   ...
    "password": {
      "$crypto": {
        "type": "x-simple-encryption",
        "value": {
          "cipher": "AES/CBC/PKCS5Padding",
          "stableId": "my-new-key",
          "salt": "bGyKG3PKmwHONOfxerr1Qg==",
          "data": "6vXZiJ3ZNN/UUnsrT7dTQw==",
          "keySize": 16,
          "purpose": "idm.password.encryption",
          "iv": "doAdtxfWfFbrPIIfubGi5g==",
          "mac": "OML6xd9qvDtD5AvMc1Tc3A=="
        }
      }
    },
   ...
   ```

---

---
title: Filesystem secret stores
description: Configure PingIDM filesystem secret stores to read secrets from files, with support for encoding schemes, automatic encryption, and versioning
component: pingidm
version: 8.1
page_id: pingidm:security-guide:secret-stores-filesystem
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/secret-stores-filesystem.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Secret Stores", "Encryption"]
section_ids:
  fs-automatic-encryption: Configuring automatic encryption
  fs-create-new-user-example: "Example: Create a new user type"
  fs-configure-purpose-versions: Configuring purpose versions
---

# Filesystem secret stores

A filesystem secret store maps to a directory storing an arbitrary number of files that each contain one secret. When filesystem secret stores are used, IDM reads the contents of a file with a name matching the `secretId` field in the secret store's mapping list.

Filesystem secret stores are useful to provide secrets from third-party secret stores like AWS Secrets Manager or Google Secrets Manager. They can also be used to separate your secrets from your configuration files.

Filesystem secret stores can be encoded with the following encoding schemes:

* PLAIN

* PEM

* BASE64

* BASE64URL

The following configuration is an example of a filesystem secret store which is configured to use the `/secrets` directory and contains a mapping for the `idm.admin.password` secret:

```json
{
    "name":"secretVolume",
    "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
    "config": {
        "format": "PLAIN",
        "directory": "&{idm.install.dir}/secrets",
        "mappings": [
          {
            "secretId": "idm.admin.password",
            "types": [
              "GENERIC"
            ]
          }
        ]
    }
}
```

## Configuring automatic encryption

You can add automatic encryption to the filesystem secret store by adding the `encryptionKey` field. The following example demonstrates encrypting the `idm.admin.password` secret with the `idm.default` encryption key:

```json
{
    "name": "fileSystemStore",
    "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
    "config": {
        "directory": "&{idm.install.dir}/secrets",
        "format": "PLAIN",
        "encryptionKey": "idm.default",
        "mappings": [
            {
                "secretId": "idm.admin.password",
                "types": [
                    "GENERIC"
                ]
            }
        ]
    }
}
```

By default, IDM uses `AES Key Wrap with a 128-bit key` for JSON Web Token (JWT) key management and `AES_128_CBC_HMAC_SHA_256` for content encryption. These can be configured by setting the `encryptionAlgorithm` and `encryptionMethod` fields on the store configuration respectively.

## Example: Create a new user type

The following example creates a new type of static user, `openidm-super`, with the secret, `idm.admin.password`, kept in the filesystem secret store. To configure the user:

1. In `conf/authentication.json`, add the following new user configuration:

   ```json
   {
       "name": "STATIC_USER",
       "properties": {
           "queryOnResource": "internal/user",
           "username": "openidm-super",
           "password": {
               "$purpose": {
                   "name": "idm.admin.password"
               }
           },
           "defaultUserRoles": [
               "internal/role/openidm-authorized",
               "internal/role/openidm-admin"
           ],
           "enabled": true
       }
   }
   ```

2. In `conf/secrets.json`, use the existing mapping for the `idm.admin.password` secret and optionally add the `format` parameter:

   ```json
   {
       "secretId": "idm.admin.password",
       "format": "PLAIN",
       "types": [
           "GENERIC"
       ]
   }
   ```

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | Only use the optional `format` parameter if the secret is encoded using a different scheme than the rest of the secret volume. |

## Configuring purpose versions

The filesystem secret store supports multiple versions of the same purpose. To configure this, specify the `versionSuffix` property in the store's definition in `conf/secrets.json`. The following example adds the `.v` suffix to the `idm.admin.password` purpose:

```json
{
  "name": "pemStore",
  "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
  "config": {
    "format": "PEM",
    "directory": "&{idm.install.dir}/secrets",
    "versionSuffix": ".v",
    "mappings": [
      {
        "secretId": "idm.admin.password",
        "types": [
          "GENERIC"
        ]
      }
    ]
  }
}
```

After `versionSuffix` is defined, you can version your purpose files by adding it to the file name. Following the previous example, the files could be named `idm.admin.password.v1`, `idm.admin.password.v2`, and so on. The latest version number is the active secret.

---

---
title: FIPS 140-3 compliance
description: Configure PingIDM for FIPS 140-3 compliance using Bouncy Castle FIPS libraries, including key store setup and secrets.json configuration
component: pingidm
version: 8.1
page_id: pingidm:security-guide:security-bouncy-castle-fips
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/security-bouncy-castle-fips.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Bouncy Castle FIPS", "Keystores", "Cryptographic Keys", "Secrets", "JSON", "Configuration", "JVM"]
section_ids:
  download-bouncy-castle-libraries: Download the Bouncy Castle libraries
  enable-bouncy-castle-in-jvm: Enable the Bouncy Castle FIPS provider in the JVM
  add-bouncy-castle-existing-jvm: Add Bouncy Castle providers to the existing JVM
  add-bouncy-castle-idm-config: Add Bouncy Castle providers to IDM conf/java.security
  create-bouncy-castle-crypto-keys: Create the IDM Bouncy Castle key store and cryptographic keys
  bouncy-castle-jvm-to-idm: Provide the JVM to IDM
  configure-bouncy-castle-keystore: Configure the Bouncy Castle key store in secrets.json
  disable_bouncy_castle_fips_approved_mode: Disable Bouncy Castle FIPS-approved mode
  allow-rsa-key-multi-use: Allow RSA key multi-use
---

# FIPS 140-3 compliance

To achieve [FIPS 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) compliance, configure the [Bouncy Castle FIPS libraries](https://www.bouncycastle.org/fips-java/) with IDM. This enables the use of the Bouncy Castle FIPS key store and security provider in FIPS-approved mode.

Bouncy Castle FIPS is crucial when dealing with government data, where you must meet the FIPS 140-3 security requirement for regulatory compliance.

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Bouncy Castle FIPS is less performant than other key stores. The destroyable keys cannot be cached and must be read from the key store with every use. |

To configure IDM to use Bouncy Castle FIPS:

1. [Download the Bouncy Castle libraries](#download-bouncy-castle-libraries).

2. [Enable the Bouncy Castle FIPS provider in the JVM](#enable-bouncy-castle-in-jvm).

3. [Create the IDM cryptographic keys](#create-bouncy-castle-crypto-keys).

4. [Provide the JVM to IDM](#bouncy-castle-jvm-to-idm).

5. [Configure the Bouncy Castle key store in `secrets.json`](#configure-bouncy-castle-keystore).

## Download the Bouncy Castle libraries

|   |                                                                                          |
| - | ---------------------------------------------------------------------------------------- |
|   | The [IDM CLI](../setup-guide/chap-cli.html) does not work when using Bouncy Castle FIPS. |

To use Bouncy Castle FIPS with IDM, download the libraries:

1. Download the following libraries from [Bouncy Castle](https://www.bouncycastle.org/fips-java/) to the server/machine where IDM is deployed:

   | File                                     | Description                                                             |
   | ---------------------------------------- | ----------------------------------------------------------------------- |
   | `bc-fips-latestVersionNumber.jar`(1)     | Contains the Bouncy Castle FIPS security provider implementation.       |
   | `bcpkix-fips-latestVersionNumber.jar`(2) | Provides FIPS support for cert generation.                              |
   | `bctls-fips-latestVersionNumber.jar`(3)  | Provides TLS support using FIPS compliance.                             |
   | `bcmail-fips-latestVersionNumber.jar`(4) | The Bouncy Castle Java APIs for doing S/MIME with JavaMail.             |
   | `bcutil-fips-latestVersionNumber.jar`(5) | The Bouncy Castle Java APIs for ASN.1 extension and other utility APIs. |

   (1) The tested version is `bc-fips-2.1.2.jar`.

   (2) The tested version is `bcpkix-fips-2.1.9.jar`.

   (3) The tested version is `bctls-fips-2.1.20.jar`.

   (4) The tested version is `bcmail-fips-2.1.6.jar`.

   (5) The tested version is `bcutil-fips-2.1.4.jar`.

2. Copy the downloaded files to `/path/to/openidm/bundle`.

3. Restart IDM.

## Enable the Bouncy Castle FIPS provider in the JVM

To enable the Bouncy Castle FIPS provider in your JVM, do one of the following:

* [Add Bouncy Castle providers to the existing JVM](#add-bouncy-castle-existing-jvm)

* [Add Bouncy Castle providers to IDM `conf/java.security`](#add-bouncy-castle-idm-config)

### Add Bouncy Castle providers to the existing JVM

If the existing JVM supports Bouncy Castle, then you can add the security providers to the JVM.

Add the Bouncy Castle security providers to `$JAVA_HOME/conf/security/java.security` as the first and second security providers:

```bash
security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider C:HYBRID;ENABLE{All};
security.provider.2=org.bouncycastle.jsse.provider.BouncyCastleJsseProvider
```

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | The Bouncy Castle security providers should be 1 and 2. You should add any other security providers necessary for your use case. |

### Add Bouncy Castle providers to IDM `conf/java.security`

If the existing JVM supports Bouncy Castle, then you can add the security providers to the `/path/to/openidm/conf/java.security`.

Add the Bouncy Castle security providers to `/path/to/openidm/conf/java.security`:

```bash
security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider C:HYBRID;ENABLE{All};
security.provider.2=org.bouncycastle.jsse.provider.BouncyCastleJsseProvider
```

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This file overrides the `$JAVA_HOME/conf/security/java.security` file. You should also add any additional security providers from that file which are necessary for your use case. |

## Create the IDM Bouncy Castle key store and cryptographic keys

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you create the cryptographic keys, you must [Enable the Bouncy Castle FIPS provider in the JVM](#enable-bouncy-castle-in-jvm). |

To create the necessary IDM cryptographic keys:

1. Create the Bouncy Castle key store. This can be done in conjunction with creating the first cryptographic key:

   ```bash
   keytool \
   -genseckey \
   -alias openidm-sym-default \
   -keyalg aes \
   -keysize 256 \
   -keystore /location/to/keystore.bcfks \
   -storepass changeit -storetype BCFKS \
   -provider org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
   -providerpath /path/to/bc-fips-2.1.2.jar
   ```

   This creates the `openidm-sym-default` key in a key store called /location/to/keystore.bcfks while also creating that keystore if it does not exist.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must use the JVM specific keytool that the Bouncy Castle security provider uses.For example, if you enable the security providers in the [system default JVM](#add-bouncy-castle-existing-jvm), you must use the system default keytool command.The keytool command is in the `bin` directory of the JVM Java home.Failure to use the `keytool` command you configure for Bouncy Castle results in the following error:```bash
   keytool error: java.lang.Exception: Provider "org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider" not found
   ``` |

2. Create the remaining keys:

   Create the `openidm-selfservice-key`

   ```bash
   keytool \
   -genseckey \
   -alias openidm-selfservice-key \
   -keyalg aes \
   -keysize 256 \
   -keystore /location/to/keystore.bcfks \
   -storepass changeit \
   -storetype BCFKS \
   -provider org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
   -providerpath /path/to/bc-fips-2.1.2.jar
   ```

   Create the `openidm-jwtsessionhmac-key`

   ```bash
   keytool \
   -genseckey \
   -alias openidm-jwtsessionhmac-key \
   -keyalg aes \
   -keysize 256 \
   -keystore /location/to/keystore.bcfks \
   -storepass changeit \
   -storetype BCFKS \
   -provider org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
   -providerpath /path/to/bc-fips-2.1.2.jar
   ```

   Create the `openidm-localhost` key

   ```bash
   keytool \
   -genkey \
   -alias openidm-localhost \
   -keyalg RSA \
   -keysize 2048 \
   -keystore /location/to/keystore.bcfks \
   -storepass changeit \
   -storetype BCFKS \
   -provider org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
   -providerpath /path/to/bc-fips-2.1.2.jar
   ```

   Create the `selfservice` key

   ```bash
   keytool \
   -genkey \
   -alias selfservice \
   -keyalg RSA \
   -keysize 2048 \
   -keystore /location/to/keystore.bcfks \
   -storepass changeit \
   -storetype BCFKS \
   -provider org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
   -providerpath /path/to/bc-fips-2.1.2.jar
   ```

## Provide the JVM to IDM

IDM uses only the default system Java and `JAVA_HOME` defined in the `/path/to/openidm/startup.sh` file:

Default `startup.sh` file

```bash
if which java &>/dev/null; then
    JAVA=java
elif [ -n "$JAVA_HOME" ] && [ -x "$JAVA_HOME/bin/java" ];  then
    JAVA="$JAVA_HOME/bin/java"
else
    echo JAVA_HOME not available, Java is needed to run IDM
    echo Please install Java and set JAVA_HOME accordingly
    exit 1
fi
```

Learn more about limitations in [Bouncy Castle FIPS with custom JVM](../release-notes/limitations.html#limitations-bouncy-castle-fips).

## Configure the Bouncy Castle key store in `secrets.json`

After you add the [Bouncy Castle security providers](#enable-bouncy-castle-in-jvm) and [create the key store and keys](#create-bouncy-castle-crypto-keys), you must replace the default IDM key store with the new Bouncy Castle key store in `/path/to/openidm/conf/secrets.json`:

```bash
        {
            "name" : "mainKeyStore",
            "class" : "org.forgerock.openidm.secrets.config.KeyStoreSecretStore",
            "config" : {
                "file" : "&{idm.install.dir}/security/keystore.bcfks",
                "storetype" : "BCFKS",
                "providerName" : "BCFIPS",
                "storePassword" : "changeit",
                "mappings" : [
                    {
                        "secretId" : "idm.default",
                        "types" : [
                            "ENCRYPT",
                            "DECRYPT"
                        ],
                        "aliases" : [
                            "&{openidm.config.crypto.alias|openidm-sym-default}"
                        ]
                    },
                    {
                        "secretId" : "idm.config.encryption",
                        "types" : [
                            "ENCRYPT",
                            "DECRYPT"
                        ],
                        "aliases" : [
                            "&{openidm.config.crypto.alias|openidm-sym-default}"
                        ]
                    },
                    {
                        "secretId": "idm.password.encryption",
                        "types": [
                            "ENCRYPT",
                            "DECRYPT"
                        ],
                        "aliases" : [
                            "&{openidm.config.crypto.alias|openidm-sym-default}"
                        ]
                    },
                    {
                        "secretId" : "idm.jwt.session.module.encryption",
                        "types" : [
                            "ENCRYPT",
                            "DECRYPT"
                        ],
                        "aliases" : [
                            "&{openidm.https.keystore.cert.alias|openidm-localhost}"
                        ]
                    },
                    {
                        "secretId" : "idm.jwt.session.module.signing",
                        "types" : [
                            "SIGN",
                            "VERIFY"
                        ],
                        "aliases" : [
                            "&{openidm.config.crypto.jwtsession.hmackey.alias|openidm-jwtsessionhmac-key}"
                        ]
                    },
                    {
                        "secretId" : "idm.selfservice.encryption",
                        "types" : [
                            "ENCRYPT",
                            "DECRYPT"
                        ],
                        "aliases" : [
                            "selfservice"
                        ]
                    },
                    {
                        "secretId" : "idm.selfservice.signing",
                        "types" : [
                            "SIGN",
                            "VERIFY"
                        ],
                        "aliases" : [
                            "&{openidm.config.crypto.selfservice.sharedkey.alias|openidm-selfservice-key}"
                        ]
                    },
                    {
                        "secretId" : "idm.assignment.attribute.encryption",
                        "types" : [
                            "ENCRYPT",
                            "DECRYPT"
                        ],
                        "aliases" : [
                            "&{openidm.config.crypto.alias|openidm-sym-default}"
                        ]
                    }
                ]
            }
        },
```

IDM is now configured to start using the Bouncy Castle key store.

## Disable Bouncy Castle FIPS-approved mode

By default, IDM turns on Bouncy Castle in FIPS-approved mode. This makes Bouncy Castle FIPS 140-3 compliant.

IDM sets the configuration in `/path/to/openidm/startup.sh` and `/path/to/openidm/bin/docker-entrypoint.sh` using the following property:

```bash
org.bouncycastle.fips.approved_only=true
```

To disable FIPS-approved mode, change `org.bouncycastle.fips.approved_only` to `false`.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In `startup.sh` and `docker-entrypoint.sh`, the `org.bouncycastle.jca.enable_jks` property enables the JKS-format Java key store for FIPS. To maintain compliance, this key store can only be used for reading JKS key stores containing certificates.By default, this property is `false`. To enable the key store, set it to `true`. |

|   |                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These settings must take place early in the IDM start process per the [Bouncy Castle documentation](https://www.bouncycastle.org/fips-java/). |

## Allow RSA key multi-use

By default, the Bouncy Castle FIPS module prevents an RSA modulus from being used for both encryption and signing operations. This is a security measure to avoid potential vulnerabilities.

However, specific scenarios might require an RSA key to be used for both purposes. To allow this, set:

```bash
org.bouncycastle.rsa.allow_multi_use=true
```

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Enabling this property relaxes a security control. Understand the implications before setting `org.bouncycastle.rsa.allow_multi_use=true`. Consult relevant security best practices and the [Bouncy Castle documentation](https://www.bouncycastle.org/fips-java/) for more information. |

---

---
title: General security considerations
description: General security considerations for PingIDM, covering patching, cryptography, minimal features, access control, enforcement, and audit logging
component: pingidm
version: 8.1
page_id: pingidm:security-guide:general-security
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/general-security.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Patching", "Cryptography", "Access Control", "Audit Logging"]
---

# General security considerations

This list does not provide best practices in network and system administration; rather, it suggests a number of security mechanisms that you can expand upon.

* Keep up-to-date on patches

  To minimize security vulnerabilities, keep your operating systems, web and application servers, and other software up-to-date. Malicious users will not hesitate to exploit the latest vulnerabilities.

  Learn how to find security advisories in the Ping Identity [support portal](https://support.pingidentity.com/s/article/Support-Portal-Guide#SecurityAdvisories) (requires sign-on). You should also follow similar lists from all of your vendors.

* Keep up-to-date on cryptographic methods and algorithms

  Different cryptographic methods and algorithms are discovered and tested over time. Do not generate your keys with outdated or insecure algorithms like RSA or SHA-1.

* Turn off unnecessary features

  The more features you enable, the more features you need to secure, patch, and audit. If you are not using something, disable or uninstall it.

* Limit access to the servers hosting IDM

  A large part of protecting your environment is ensuring only authorized people can access your servers and applications through the appropriate network, using the appropriate ports, and presenting strong enough credentials.

  Ensure users connect to the systems through SSL/TLS and audit system access periodically.

* Enforce security

  Do not expect your users to follow security practices on their own; enforce it when possible by requiring secure connections, password resets, and strong authentication methods.

* Audit access and changes

  Audit logs record all events that occurred. Operating systems also have audit logs to detect unauthorized login attempts and changes to the software.

  IDM has its own [Audit logging service](../audit-guide/preface.html) that adheres to the log structure common across the Ping Identity Platform.

---

---
title: Hardware secret stores
description: "Configure PingIDM to use a PKCS #11 hardware security module to store and manage encryption keys, certificates, and secret mappings"
component: pingidm
version: 8.1
page_id: pingidm:security-guide:secret-stores-hardware
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/secret-stores-hardware.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Secret Stores", "Keystores", "Truststores", "Encryption", "Keys", "Hardware Security Modules (HSM)", "Secrets", "Mappings", "PKCS #11"]
section_ids:
  hsm-conf: HSM configuration
  hsm-default-keys: HSM default encryption keys
  openidm-hsm-conf: Configure IDM to support an HSM provider
---

# Hardware secret stores

This topic demonstrates how to use a PKCS #11 device, such as a hardware security module (HSM), to store the keys used to secure communications. IDM supports retrieval of secrets from HSMs either locally or over the network.

|   |                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | On Windows systems using the 64-bit JDK, the Sun PKCS #11 provider is available *only* from JDK version 1.8b49. If you want to use a PKCS #11 device on Windows, use the 32-bit version of the JDK, or upgrade your 64-bit JDK to version 1.8b49 or higher. |

## HSM configuration

This section assumes that you have access to an HSM device (or a software emulation of an HSM device, such as SoftHSM) and that the HSM provider has been configured and initialized.

The command-line examples in this section use SoftHSM for testing purposes. Before you start, set the correct environment variable for the SoftHSM configuration, for example:

```bash
export SOFTHSM2_CONF=/path/to/softhsm/2.0.0/etc/softhsm2.conf
```

Also initialize slot `0` on the provider, with a command similar to the following:

```bash
softhsm2-util --init-token --slot 0 --label "My token 1"
```

This token initialization requests two PINs—an SO PIN and a user PIN. You can use the SO PIN to reinitialize the token. The user PIN is provided to IDM so that it can interact with the token. Remember the values of these PINs because you will use them later in this section.

The PKCS #11 standard uses a configuration file to interact with the HSM device. The following example shows a basic configuration file for SoftHSM:

```properties
name = softHSM
library = /path/to/softhsm/2.0.0/lib/softhsm/libsofthsm2.so
slot = 1
attributes(generate, *, *) = {
   CKA_TOKEN = true
}
attributes(generate, CKO_CERTIFICATE, *) = {
   CKA_PRIVATE = false
}
attributes(generate, CKO_PUBLIC_KEY, *) = {
   CKA_PRIVATE = false
}
attributes(*, CKO_SECRET_KEY, *) = {
   CKA_PRIVATE = false
   CKA_EXTRACTABLE = true
}
```

Your HSM configuration file *must* include at least the following settings:

* `name`

  A suffix to identify the HSM provider. This example uses the `softHSM` provider.

* `library`

  The path to the PKCS #11 library.

* `slot`

  The slot number to use, specified as a string. Make sure that the slot you specify here has been initialized on the HSM device.

The `attributes` specify additional PKCS #11 attributes that are set by the HSM. For a complete list of these attributes, refer to the [PKCS #11 Reference](https://docs.oracle.com/en/java/javase/21/security/pkcs11-reference-guide.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using the JWT Session Module, you *must* set `CKA_EXTRACTABLE = true` for secret keys in your HSM configuration file. For example:```properties
attributes(*, CKO_SECRET_KEY, *) = {
   CKA_PRIVATE = false
   CKA_EXTRACTABLE = true
}
```The HSM provider must allow secret keys to be extractable because the authentication service serializes the JWT Session Module key and passes it to the authentication framework as a base 64-encoded string. |

## HSM default encryption keys

When IDM first starts up, it generates a number of encryption keys required to encrypt specific data. If you are using an HSM provider, you must generate these keys manually. The secret keys must use an HMAC algorithm.

|   |                                                                                                |
| - | ---------------------------------------------------------------------------------------------- |
|   | This procedure assumes that your HSM configuration file is located at `/path/to/hsm/hsm.conf`. |

1. The `openidm-sym-default` key is the default symmetric key required to encrypt the configuration. The following command generates that key in the HSM provider. The `-providerArg` must point to the HSM configuration file described in [HSM configuration](#hsm-conf).

   ```
   keytool \
   -genseckey \
   -alias openidm-sym-default \
   -keyalg HmacSHA256 \
   -keysize 256 \
   -keystore NONE \
   -storetype PKCS11 \
   -providerClass sun.security.pkcs11.SunPKCS11 \
   -providerArg /path/to/hsm/hsm.conf
   Enter keystore password:
   ```

   Enter the password of your HSM device. If you are using SoftHSM, enter your user PIN as the keystore password.

2. The `openidm-selfservice-key` is used to encrypt certain managed user passwords and other sensitive data. Generate the `openidm-selfservice-key` key:

   ```
   keytool \
   -genseckey \
   -alias openidm-selfservice-key \
   -keyalg HmacSHA256 \
   -keysize 256 \
   -keystore NONE \
   -storetype PKCS11 \
   -providerClass sun.security.pkcs11.SunPKCS11 \
   -providerArg /path/to/hsm/hsm.conf
   Enter keystore password: user PIN
   ```

   Enter the password of your HSM device. If you are using SoftHSM, enter your user PIN as the keystore password.

3. The `openidm-jwtsessionhmac-key` is used by the [JWT session module](../auth-guide/authentication.html#jwt-session-module) to encrypt JWT session cookies. Generate the JWT session module key:

   ```
   keytool \
   -genseckey \
   -alias openidm-jwtsessionhmac-key \
   -keyalg HmacSHA256 \
   -keysize 256 \
   -keystore NONE \
   -storetype PKCS11 \
   -providerClass sun.security.pkcs11.SunPKCS11 \
   -providerArg /path/to/hsm/hsm.conf
   Enter keystore password: user PIN
   ```

4. The `openidm-localhost` certificate is used to support SSL/TLS. Generate the certificate:

   ```
   keytool \
   -genkey \
   -alias openidm-localhost \
   -keyalg RSA \
   -keysize 2048 \
   -keystore NONE \
   -storetype PKCS11 \
   -providerClass sun.security.pkcs11.SunPKCS11 \
   -providerArg /path/to/hsm/hsm.conf
   Enter keystore password: user PIN
   What is your first and last name?
     [Unknown]:  localhost
   What is the name of your organizational unit?
     [Unknown]:
   What is the name of your organization?
     [Unknown]:  OpenIDM Self-Signed Certificate
   What is the name of your City or Locality?
     [Unknown]:
   What is the name of your State or Province?
     [Unknown]:
   What is the two-letter country code for this unit?
     [Unknown]:
   Is CN=localhost, OU=Unknown, O=OpenIDM Self-Signed Certificate, L=Unknown, ST=Unknown, C=Unknown correct?
     [no]:  yes
   ```

5. The `selfservice` certificate secures requests from the end-user UI. Generate the certificate:

   ```
   keytool \
   -genkey \
   -alias selfservice \
   -keyalg RSA \
   -keysize 2048 \
   -keystore NONE \
   -storetype PKCS11 \
   -providerClass sun.security.pkcs11.SunPKCS11 \
   -providerArg /path/to/hsm/hsm.conf
   Enter keystore password: user PIN
   What is your first and last name?
     [Unknown]:  localhost
   What is the name of your organizational unit?
     [Unknown]:
   What is the name of your organization?
     [Unknown]:  OpenIDM Self Service Certificate
   What is the name of your City or Locality?
     [Unknown]:
   What is the name of your State or Province?
     [Unknown]:
   What is the two-letter country code for this unit?
     [Unknown]:
   Is CN=localhost,O=OpenIDM Self Service Certificate,OU=None,L=None,ST=None,C=None?
     [no]:  yes
   ```

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

6. If you are *not* using the HSM provider for the truststore, you must add the certificates generated in the previous two steps to the default IDM truststore.

   If you *are* using the HSM provider for the truststore, you can skip this step.

   To add the `openidm-localhost` certificate to the IDM truststore, export the certificate from the HSM provider, then import it into the truststore:

   ```
   keytool \
   -export \
   -alias openidm-localhost \
   -file exportedCert \
   -keystore NONE \
   -storetype PKCS11 \
   -providerClass sun.security.pkcs11.SunPKCS11 \
   -providerArg /path/to/hsm/hsm.conf
   Enter keystore password: user PIN
   Certificate stored in file exportedCert keytool \
   -import \
   -alias openidm-localhost \
   -file exportedCert \
   -keystore /path/to/openidm/security/truststore
   Enter keystore password: changeit
   Owner: CN=localhost, OU=Unknown, O=OpenIDM Self-Signed Certificate, L=...
   Issuer: CN=localhost, OU=Unknown, O=OpenIDM Self-Signed Certificate, L=...
   Serial number: 5d2554bd
   Valid from: Fri Aug 19 13:11:54 SAST 2016 until: Thu Nov 17 13:11:54 SAST 2016
   Certificate fingerprints:
   	 MD5:  F1:9B:72:7F:7B:79:58:29:75:85:82:EC:79:D8:F9:8D
   	 SHA1: F0:E6:51:75:AA:CB:14:3D:C5:E2:EB:E5:7C:87:C9:15:43:19:AF:36
   	 SHA256: 27:A5:B7:0E:94:9A:32:48:0C:22:0F:BB:7E:3C:22:2A:64:B5:45:24:14:70:...
   	 Signature algorithm name: SHA256withRSA
   	 Version: 3

   Extensions:

   #1: ObjectId: 2.5.29.14 Criticality=false
   SubjectKeyIdentifier [
   KeyIdentifier [
   0000: 7B 5A 26 53 61 44 C2 5A   76 E4 38 A8 52 6F F2 89  .Z&SaD.Zv.8.Ro..
   0010: 20 04 52 EE                                         .R.
   ]
   ]
   Trust this certificate? [no]:  yes
   Certificate was added to keystore
   ```

   The default truststore password is changeit.

## Configure IDM to support an HSM provider

To enable IDM to use an HSM provider, make the following configuration changes:

1. In your secret store configuration (`conf/secrets.json` ), change the `mainKeyStore` and `mainTrustStore` to reference the HSM. For example:

   ```json
   {
     "stores": [
       {
         "name": "mainKeyStore",
         "class": "org.forgerock.openidm.secrets.config.HsmBasedStore",
         "config": {
           "storetype": "&{openidm.keystore.type|PKCS11}",
           "providerName": "&{openidm.keystore.provider|SunPKCS11-softHSM}",
           "storePassword": "&{openidm.keystore.password|changeit}",
           "mappings": [
             {
               "secretId" : "idm.default",
               "types": [ "ENCRYPT", "DECRYPT" ],
               "aliases": [ "&{openidm.config.crypto.alias|openidm-sym-default}" ]
             },
             {
               "secretId" : "idm.config.encryption",
               "types": [ "ENCRYPT", "DECRYPT" ],
               "aliases": [ "&{openidm.config.crypto.alias|openidm-sym-default}" ]
             },
             {
               "secretId" : "idm.password.encryption",
               "types": [ "ENCRYPT", "DECRYPT" ],
               "aliases": [ "&{openidm.config.crypto.alias|openidm-sym-default}" ]
             },
             {
               "secretId" : "idm.jwt.session.module.encryption",
               "types": [ "ENCRYPT", "DECRYPT" ],
               "aliases": [ "&{openidm.https.keystore.cert.alias|openidm-localhost}" ]
             },
             {
               "secretId" : "idm.jwt.session.module.signing",
               "types": [ "SIGN", "VERIFY" ],
               "aliases": [ "&{openidm.config.crypto.jwtsession.hmackey.alias|openidm-jwtsessionhmac-key}" ]
             },
             {
               "secretId" : "idm.selfservice.signing",
               "types": [ "SIGN", "VERIFY" ],
               "aliases": [ "selfservice" ]
             },
             {
               "secretId" : "idm.selfservice.encryption",
               "types": [ "ENCRYPT", "DECRYPT" ],
               "aliases": [ "&{openidm.config.crypto.selfservice.sharedkey.alias|openidm-selfservice-key}" ]
             }
           ]
         }
       },
       {
         "name": "mainTrustStore",
         "class": "org.forgerock.openidm.secrets.config.HsmBasedStore",
         "config": {
           "storetype": "&{openidm.keystore.type|PKCS11}",
           "providerName": "&{openidm.keystore.provider|SunPKCS11-softHSM}",
           "storePassword": "&{openidm.keystore.password|changeit}",
           "mappings": [
           ]
         }
       }
     ],
     "populateDefaults": false
   }
   ```

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | The `"populateDefaults": false` turns off the default key generation. This setting is *required* for an HSM key provider. |

2. In the IDM Java security file (`conf/java.security` ), Specify the location of your PKCS #11 configuration file. For example:

   ```properties
   security.provider.14=SunPKCS11 /path/to/pkc11/config/pkcs11.conf
   ```

   Templates for the `pkcs11.conf` file are included in your PKCS package.

   You should now be able to start IDM with the keys in the HSM provider.

---

---
title: Manage password policies
description: Manage PingIDM password policies, history, multiple passwords per resource, random password generation, and the password property configuration
component: pingidm
version: 8.1
page_id: pingidm:security-guide:passwords
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/passwords.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Password", "Policy", "Password Change", "Password Reset", "Password Expiration", "Password Recovery", "Password History"]
page_aliases: ["chap-passwords.adoc"]
section_ids:
  enforce-password-policy: Password policy
  password-history: Password history policy
  multiple-passwords: Multiple passwords per linked resource
  random-passwords: Random passwords
  password-property: password property
  email_rate_limiting: Email rate limiting
---

# Manage password policies

IDM provides password management features that help you enforce password policies, limit the number of passwords users must remember, and allow users to reset and change their passwords.

## Password policy

A password policy is a set of rules defining what sequence of characters constitutes an acceptable password. Acceptable passwords generally are too complex for users or automated programs to generate or guess.

Password policies set requirements for password length, character sets that passwords must contain, dictionary words and other values that passwords must not contain. Password policies also require that users not reuse old passwords, and that users change their passwords on a regular basis.

IDM enforces password policy rules as part of the general [policy service](../objects-guide/policies.html). The default password policy applies the following rules to passwords as they are created and updated:

* A password property is required for any user object.

* The value of a password cannot be empty.

* The password must include at least one capital letter.

* The password must include at least one number.

* The minimum length of a password is 8 characters.

* The password cannot contain the user name, given name, or family name.

You can change these validation requirements, or include additional requirements, by configuring the [policy](../objects-guide/policies.html#configuring-default-policy) for passwords.

Passwords are validated in several situations:

* Password change and password reset

  Password *change* refers to users changing their own passwords. Password *reset* refers to an administrator setting a user or account password on behalf of a user.

  By default, IDM validates password values as they are provisioned.

* Password recovery

  Password recovery involves recovering a password or setting a new password when the password has been forgotten.

* Password history

  You can add validation to prevent reuse of previous password values. For more information, refer to [Password history policy](#password-history).

* Password expiration

  You can use workflows to ensure that users are able to change expiring passwords or to reset expired passwords.

### Password history policy

The sample described in [Store multiple passwords for managed users](../samples-guide/multiple-passwords.html) shows how to set up a password history policy in a scenario where users have multiple different passwords across resources. You can use the scripts provided in that sample to set up a simple password history policy that prevents managed users from setting the same password that they used previously. ***The default scripts do not evaluate the current password.***

To create a password history policy based on the scripts in the multiple passwords sample, make the following changes to your project:

1. Copy the `pwpolicy.js` script from the multiple passwords sample to your project's `script` directory:

   ```bash
   cp /path/to/openidm/samples/multiple-passwords/script/pwpolicy.js /path/to/openidm/my-project-dir/script/
   ```

   The `pwpolicy.js` script contains an `is-new` policy definition that compares a new field value with the list of historical values for that field.

   The `is-new` policy takes a `historyLength` parameter that specifies the number of historical values on which the policy should be enforced. This number must not exceed the `historySize` that you set in `conf/managed.json` to be passed to the `onCreate` and `onUpdate` scripts.

2. Copy the `onCreate-user-custom.js` and `onUpdate-user-custom.js` scripts to your project's `script` directory:

   ```bash
   cp samples/multiple-passwords/script/onCreate-user-custom.js /my-project-dir/script/
   cp samples/multiple-passwords/script/onUpdate-user-custom.js /my-project-dir/script/
   ```

   These scripts validate the password history policy when a managed user is created or updated.

3. Update your policy configuration (`conf/policy.json` ) to reference the new policy definition by adding the policy script to the `additionalFiles` array:

   ```json
   {
       "type" : "text/javascript",
       "file" : "policy.js",
       "additionalFiles": [ "script/pwpolicy.js" ],
       ...
   }
   ```

4. Update your project's `conf/managed.json` file as follows:

   1. Add a `fieldHistory` property to the managed user object:

      ```json
      "fieldHistory" : {
          "title" : "Field History",
          "type" : "object",
          "viewable" : false,
          "searchable" : false,
          "userEditable" : false,
          "scope" : "private"
      }
      ```

      The value of this field is a map of field names to a list of historical values for that field. These lists of values are used by the `is-new` policy to determine if a new value has already been used.

   2. Update the managed user object to call the scripts when a user is created or updated:

      ```json
      "name" : "user",
      "onCreate" : {
          "type" : "text/javascript",
          "file" : "script/onCreate-user-custom.js",
          "historyFields" : [
              "password"
          ],
          "historySize" : 4
      },
      "onUpdate" : {
          "type" : "text/javascript",
          "file" : "script/onUpdate-user-custom.js",
          "historyFields" : [
              "password"
          ],
          "historySize" : 4
      },
      ...
      ```

      |   |                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you have any other script logic that is executed on these events, you must update the scripts to include that logic, or add the password history logic to your current scripts. |

   3. Add the `is-new` policy to the list of policies enforced on the `password` property of a managed user. Specify the number of historical values that the policy should check in `historyLength` property:

      ```json
      "password" : {
         ...
         "policies" : [
             {
                 "policyId" : "at-least-X-capitals",
                 "params" : {
                     "numCaps" : 1
                 }
             },
             ...
             {
                 "policyId" : "is-new",
                 "params" : {
                     "historyLength" : 4
                 }
             },
             ...
         ]
      }
      ```

You should now be able to test the password history policy by creating a new managed user, and having that user update their password. If the user specifies the same password used within the previous four passwords, the update request is denied with a policy error.

## Multiple passwords per linked resource

You can store multiple passwords in a single managed user entry to enable synchronization of different passwords on different external resources.

To store multiple passwords, extend the managed user schema to include additional properties for each target resource. You can set separate policies on each of these new properties, to ensure that the stored passwords adhere to the password policies of the specific external resources.

To use this custom managed object property and its policies to update passwords on an external resource, you must make the corresponding configuration and script changes in your deployment. For a detailed sample that implements multiple passwords, refer to [Store multiple passwords for managed users](../samples-guide/multiple-passwords.html). That sample can also help you set up password history policies.

## Random passwords

In certain situations, you might want to generate a random password when users are created.

You can customize your user creation logic to include a randomly generated password that complies with the default password policy. This functionality is included in the default crypto script, `bin/defaults/script/crypto.js`, but is not invoked by default. For an example of how this functionality might be used, refer to the `openidm/bin/defaults/script/onCreateUser.js` script. The following section of that file (commented out by default) means that users created through the admin UI, or directly over the REST interface, will have a randomly generated password added to their entry:

```javascript
if (!object.password) {

    // generate random password that aligns with policy requirements
    object.password = require("crypto").generateRandomString([
        { "rule": "UPPERCASE", "minimum": 1 },
        { "rule": "LOWERCASE", "minimum": 1 },
        { "rule": "INTEGERS", "minimum": 1 },
        { "rule": "SPECIAL", "minimum": 1 }
    ], 16);

}
```

|   |                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The changes made to scripts take effect after the time set in the `recompile.minimumInterval`, described in [Script configuration](../scripting-guide/script-config.html). |

The generated password can be encrypted or hashed, in accordance with the managed user schema, defined in `conf/managed.json` . For more information, refer to [Encoding Attribute Values](encoding-attribute-values.html). Synchronizing hashed passwords is not supported.

You can use this random string generation in a number of situations. Any script handler that is implemented in JavaScript can call the `generateRandomString` function.

## `password` property

To use a property other than the default `password` property to store passwords, you must change the following files:

* `policy.json`

  If you want to enforce password validation rules on a different property, change the `password` property in this file.

* `managed.json`

  Modify the `password` object in this file, which also includes password complexity policies.

* `sync.json`

  If you change the `password` property, make sure that you limit the change to the appropriate system, designated as `source` or `target`.

* Every UI file that includes `password` as a property name

  Whenever there's a way for a user to enter a password, the associated `HTML` page will include a password entry. For example, the `LoginTemplate.html` file includes the `password` property. A full list of default files with the `password` property include:

  * `_passwordFields.html`

  * `_resetPassword.html`

  * `ConfirmPasswordDialogTemplate.html`

  * `EditPasswordPageView.html`

  * `LoginTemplate.html`

  * `MandatoryPasswordChangeDialogTemplate.html`

  * `resetStage-initial.html`

  * `UserPasswordTab.html`

  |   |                                                         |
  | - | ------------------------------------------------------- |
  |   | This list does not include any created custom UI files. |

## Email rate limiting

No rate limiting is applied to password reset emails, or any emails sent by the IDM server. This means that an attacker can potentially spam a known user account with an infinite number of emails, filling that user's inbox. In the case of password reset, the spam attack can obscure an actual password reset attempt.

In a production environment, you must configure email rate limiting through the network infrastructure in which IDM runs. Configure the network infrastructure to detect and prevent frequent repeated requests to publicly accessible web pages, such as the password reset page. You can also handle rate limiting within your email server.

---

---
title: Property secret stores
description: Configure a PingIDM property secret store to read PEM-encoded keys from boot.properties for encrypting and decrypting managed object values
component: pingidm
version: 8.1
page_id: pingidm:security-guide:secret-stores-property
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/secret-stores-property.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Certificates", "Keystores", "Keytool", "Truststores", "Privacy-Enhanced Mail (PEM)", "Secret Store", "JSON"]
---

# Property secret stores

IDM servers can read keys and trusted certificates from properties that contain keys in Privacy-Enhanced Mail (PEM) format.

The following example configures a property-based secret store, and adds an RSA PEM secret whose purpose is to encrypt and decrypt managed user passwords:

1. Add a `PropertyBasedStore` secret store definition to your `conf/secrets.json` file:

   ```json
   {
       "name": "pemStore",
       "class": "org.forgerock.openidm.secrets.config.PropertyBasedStore",
       "config": {
           "format": "PEM",
           "algorithm": "RSA",
           "mappings": [
               {
                   "secretId": "idm.pem.purpose",
                   "types": [
                       "ENCRYPT",
                       "DECRYPT"
                   ]
               }
           ]
       }
   }
   ```

2. Create an RSA PEM key:

   ```
   openssl genrsa -out private-key.pem 3072
   ```

3. Display the private key. For example:

   ```none
   more private-key.pem
   -----BEGIN RSA PRIVATE KEY-----
   MIIG4w...lrDgao
   -----END RSA PRIVATE KEY-----
   ```

4. Use a text editor to convert your certificate to a single line, replacing line breaks with newline characters (`\n`). For example, on UNIX systems:

   ```none
   awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' private-key.pem
   -----BEGIN RSA PRIVATE KEY-----\nMIIG4w...lrDgao\n-----END RSA PRIVATE KEY-----\n%
   ```

5. Copy the single-line private key and paste it into your `resolver/boot.properties` file, as a value of the `secretId` that you specified in Step 1. For example:

   ```properties
   idm.pem.purpose=-----BEGIN RSA PRIVATE KEY-----\nMIIG4w...lrDgao\n-----END RSA PRIVATE KEY-----\n%
   ```

6. Modify the encryption purpose for the managed user `password` in your managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* to use the `PropertyBaseStore` secret store that you created in Step 1:

   ```json
   "password" : {
       "title" : "Password",
       "description" : "Password",
       "type" : "string",
       "viewable" : false,
       "searchable" : false,
       "userEditable" : true,
       "encryption" : {
           "purpose" : "idm.pem.purpose",
           "cipher" : "RSA/ECB/OAEPWithSHA-256AndMGF1Padding"
       }
       ...
   }
   ```

   IDM now encrypts and decrypts passwords with the RSA PEM key.

---

---
title: Read-only installation
description: Install PingIDM on a read-only filesystem and redirect audit, logging, and cache data to writable volumes for a locked-down deployment
component: pingidm
version: 8.1
page_id: pingidm:security-guide:read-only-volume
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/read-only-volume.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Volumes", "Filesystem"]
section_ids:
  prep: Prep
  redirect_audit_and_logging_data: Redirect audit and logging data
  finishing_touches: Finishing touches
---

# Read-only installation

One method of locking down the server is to install IDM on a read-only filesystem. To accomplish this, complete the procedure on this page.

This procedure assumes that you have prepared the read-only volume appropriate for your Linux/UNIX installation environment and that you have set up a regular Linux user named `idm` and a dedicated volume for the `/idm` directory.

## Prep

1. Configure the dedicated volume device, `/dev/volume` in the `/etc/fstab` file, as follows:

   ```properties
   /dev/volume/idm   ext4   ro,defaults   1,2
   ```

   When you run the `mount -a` command, the `/dev/volume` volume device is mounted on the `/idm` directory.

2. You can switch between read-write and read-only mode for the `/idm` volume with the following commands:

   ```bash
   sudo mount -o remount,rw /idm
   sudo mount -o remount,ro /idm
   ```

3. Confirm the result with the `mount` command, which should show that the `/idm` volume is mounted in read-only mode:

   ```properties
   /dev/volumeon /idm type ext4 (ro)
   ```

4. Set up the `/idm` volume in read-write mode:

   ```bash
   sudo mount -o remount,rw /idm
   ```

5. With the following commands, you can unpack the IDM binary in the `/idm` directory, and give user `idm` ownership of all files in that directory:

   ```bash
   sudo unzip /idm/IDM-8.1.1.zip
   sudo chown -R idm.idm /idm
   ```

## Redirect audit and logging data

After you have installed IDM on a read-only filesystem, redirect audit and logging data to writable volumes. This procedure assumes a user `idm` with Linux administrative (superuser) privileges.

1. Create an external directory where IDM can send logging, auditing, and internal repository information:

   ```bash
   sudo mkdir -p /var/log/openidm/audit
   sudo mkdir /var/log/openidm/logs
   sudo mkdir -p /var/cache/openidm/felix-cache
   sudo mkdir /var/run/openidm
   ```

   Alternatively, route audit data to a remote data store. For an example of how to send audit data to a MySQL repository, refer to [Direct audit information to MySQL](../samples-guide/audit-jdbc.html).

2. Give the `idm` user ownership of the newly created directories:

   ```bash
   sudo chown -R idm.idm /var/log/openidm
   sudo chown -R idm.idm /var/cache/openidm
   sudo chown -R idm.idm /var/run/openidm
   ```

3. Modify the following configuration files:

   * conf/audit.json

     Make sure the `handlerForQueries` is the JSON audit event handler and change the `logDirectory` property to the `/var/log/openidm/audit` subdirectory:

     ```json
     "eventHandlers" : [
         {
             "class" : "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
             "config" : {
                 "name" : "json",
                 "logDirectory" : "/var/log/openidm/audit",
                 ...
             },
             ...
         }
     ]
     ```

   * conf/logback.xml

     Add a writable log directory property and point the [`RollingFileAppender`](../monitoring-guide/server-logs.html#logging-file-appender) to that directory:

     ```xml
     <configuration scan="true" scanPeriod="30 seconds">
         ...
         <property name="LOG_DIR" value="/var/log/openidm/logs"/> (1)
         ...
         <appender name="file" class="RollingFileAppender">
             <file>${LOG_DIR}/openidm.log</file> (2)
             ...
             <rollingPolicy class="TimeBasedRollingPolicy">
                 <fileNamePattern>${LOG_DIR}/openidm-%d{yyyy-MM-dd}.log</fileNamePattern> (3)
                 ...
             </rollingPolicy>
         </appender>
         ...
     </configuration>
     ```

     |       |                                                           |
     | ----- | --------------------------------------------------------- |
     | **1** | Define a property for the writable log directory.         |
     | **2** | Redirect the log file appender to the writable directory. |
     | **3** | Redirect the rolling log files to the writable directory. |

   * conf/config.properties

     Activate and redirect the `org.osgi.framework.storage` property as follows:

     ```properties
     # If this value is not absolute, then the felix.cache.rootdir controls
     # how the absolute location is calculated. (See buildNext property)
     org.osgi.framework.storage=&{felix.cache.rootdir|&{user.dir}}/felix-cache

     # The following property is used to convert a relative bundle cache
     # location into an absolute one by specifying the root to prepend to
     # the relative cache path. The default for this property is the
     # current working directory.
     felix.cache.rootdir=/var/cache/openidm
     ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Your setup may require additional redirection for the following:- Connectors. Depending on the connector, and the read-only volume, consider configuring connectors to direct output to writable volumes.

- Scripts. If you are using Groovy, examine the script configuration *(tooltip: You can manage the script configuration over REST at the config/script endpoint, or directly in the conf/script.json file.)* for your project. Make sure that output such as to the `groovy.target.directory` is directed to an appropriate location, such as `idm.data.dir`. |

## Finishing touches

1. Adjust the value of the `OPENIDM_PID_FILE` in the `startup.sh` and `shutdown.sh` scripts. To do so for a default bash shell, set the value of `OPENIDM_PID_FILE` for user `idm` by adding the following line to `/home/idm/.bashrc`:

   ```bash
   export OPENIDM_PID_FILE=/var/run/openidm/openidm.pid
   ```

   |   |                                                    |
   | - | -------------------------------------------------- |
   |   | For other shells, adjust your changes accordingly. |

   When you log in again as user `idm`, your `OPENIDM_PID_FILE` variable should redirect the process identifier file, `openidm.pid` to the `/var/run/openidm` directory, ready for access by the `shutdown.sh` script.

2. While the volume is still mounted in read-write mode, start IDM normally:

   ```bash
   path/to/openidm/startup.sh -p project-dir
   ```

   The first startup of IDM either processes the signed certificate that you added, or generates a self-signed certificate, and encrypts any passwords in the various configuration files.

3. Stop IDM.

4. You can now mount the `/idm` directory in read-only mode. The configuration in `/etc/fstab` ensures that Linux mounts the `/idm` directory in read-only mode on next system boot.

   ```bash
   sudo mount -o remount,ro /idm
   ```

5. Reboot the system.

6. You can now start IDM, configured on a secure read-only volume.

   ```bash
   path/to/openidm/startup.sh -p project-dir
   ```

---

---
title: Secret stores
description: Configure PingIDM secret stores, map secretIDs to key aliases, and rotate secrets for connectors, email, databases, and proxy services
component: pingidm
version: 8.1
page_id: pingidm:security-guide:secret-stores
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/secret-stores.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Secret Stores", "Keystores", "Truststores", "Encryption", "Keys", "Hardware Security Modules (HSM)", "Mappings"]
page_aliases: ["configure-secrets.adoc"]
section_ids:
  configure_secret_stores: Configure secret stores
  secret-mappings: Mapping secretIDs to key aliases
  secret-rotation-email: Configure email service secret rotation
  store_password_as_secret: Store password as secret
  store-user-pass-as-secret: Store username and password as a secret
  secret-rotation-connectors: Configure secret rotation for connectors
  store_the_credentials_as_a_secret: Store the credentials as a secret
  store_the_principal_and_credentials_as_a_secret: Store the principal and credentials as a secret
  secret-rotation-rsfilter: Store rsFilter client secret as a secret
  secret-rotation-hikari: Rotate Hikari credentials
  configure_whole_account_rotation: Configure whole account rotation
  configure_password_rotation: Configure password rotation
  secret-rotation-prometheus: Store Prometheus credentials as a secret
  rotate_prometheus_credentials: Rotate Prometheus credentials
  proxy-secret-rotation: Configure proxy secret rotation
  default_proxy_credentials: Default proxy credentials
  external_service_proxy_credentials: External service proxy credentials
  rotate_proxy_credentials: Rotate proxy credentials
---

# Secret stores

Secret stores are repositories for cryptographic keys and credentials. IDM supports the following secret store types:

* *File* secret stores, which have one file that stores many secrets

* *Filesystem* secret stores, which have many files that each store one secret

* *Property* secret stores, which store secrets in properties

* *Hardware Security Module* (HSM) secret stores, which involve security devices (for example, a YubiKey)

## Configure secret stores

You can configure secret stores in your project's `conf/secrets.json` file, which has the following default configuration:

```json
{
    "stores" : [
        {
            "name" : "mainKeyStore",
            "class" : "org.forgerock.openidm.secrets.config.KeyStoreSecretStore",
            "config" : {
                "file" : "&{idm.data.dir}/security/keystore.jceks",
                "storetype" : "JCEKS",
                "providerName" : "SunJCE",
                "storePassword" : "changeit",
                "mappings" : [
                    {
                        "secretId" : "decrypt",
                        "aliases" : [
                            "openidm-sym-default"
                        ],
                        "types" : [
                            "ENCRYPT",
                            "DECRYPT"
                        ]
                    }
                ]
            }
        },
        {
            "name" : "mainTrustStore",
            "class" : "org.forgerock.openidm.secrets.config.KeyStoreSecretStore",
            "config" : {
                "file" : "&{idm.data.dir}/security/truststore",
                "storetype" : "JKS",
                "providerName" : "SUN",
                "storePassword" : "changeit",
                "mappings" : [
                    {
                        "secretId" : "sign",
                        "aliases" : [
                            "server-cert"
                        ],
                        "types" : [
                            "SIGN"
                        ]
                    }
                ]
            }
        }
    ],
    "populateDefaults" : true
}
```

The `mainKeyStore` and `mainTrustStore` properties configure the default secret stores. IDM requires these properties in order to start up. Do not change the property names because they are also provided to third-party products that need a single keystore and a single truststore.

* `mainKeyStore`

  The main keystore references a Java Cryptography Extension Keystore (JCEKS) located at `/path/to/openidm/security/keystore.jceks`.

* `mainTrustStore`

  The main truststore references a file-based truststore located at `/path/to/openidm/security/truststore`.

You can manage these keystores and truststores using the `keytool` command, included in your Java installation. Learn more about the [`keytool` command](https://docs.oracle.com/en/java/javase/21/docs/specs/man/keytool.html).

Each configured store has a `name` and `class`, and the following configuration properties:

* `file`

  For file-based secret stores, this property references the path to the store file, for example, `&{idm.install.dir}/security/keystore.jceks}`. Hardware security modules do not have a `file` property.

* `storetype`

  The type of secret store. IDM supports a number of store types, including JCEKS, JKS, PKCS #11, and PKCS #12.

* `providerName`

  Sets the name of the cryptographic service provider; for example, `SunPKCS11` or `softHSM`. If no provider is specified, the JRE default is used.

* `storePassword`

  The password to the secret store. For the default IDM keystore and truststore, the password is `changeit`. You should change this password in a production deployment, as described in [Changing the default keystore password](stores-certs-keys.html#security-keystore-password).

* `mappings`

  This object lets you map keys and certificates in the secret stores to functionality in IDM. A secrets mapping object has the following structure:

  ```json
  {
      "secretId" : "idm.config.encryption",
      "types": [ "ENCRYPT", "DECRYPT" ],
      "aliases": [ "&{openidm.config.crypto.alias|openidm-sym-default}" ]
  }
  ```

  * `secretId` is the name of the secret. The `secretId` should indicate the purpose that the secret should be used for. For example, `idm.config.encryption` indicates that the mapping is used to encrypt and decrypt sensitive configuration properties, while `idm.password.encryption` indicates that the mapping is used to encrypt and decrypt passwords.

  * `types` indicates what the keys are used for. The supported types are:

    | Type      | Definition                              |
    | --------- | --------------------------------------- |
    | `GENERIC` | Used for credentials, such as passwords |
    | `ENCRYPT` | Used to encrypt data                    |
    | `DECRYPT` | Used to decrypt data                    |
    | `SIGN`    | Used to sign data                       |
    | `VERIFY`  | Used to verify data                     |

  * `aliases` are the key aliases in the secret store that are used for this purpose. You can add as many aliases as necessary. The first alias in the list determines which alias is the active one. Active secrets are used for signature generation and encryption.

    The aliases in the default keystore are described in [The IDM keystore](default-keystore.html).

  The default secret IDs and the aliases they are mapped to are listed in [Mapping secretIDs to key aliases](#secret-mappings).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All these properties have a resolvable property value by default; for example `&{openidm.keystore.location}`, that allows you to use *property value substitution*. If no *configuration expression* has been set for a specific property, the value following the vertical bar (`\|`) is used. In the following property, the password is `changeit` unless you have set a configuration expression in one of the property resolver locations:```properties
"storePassword": "&{openidm.keystore.password|changeit}"
```For more information, refer to [Property value substitution](../setup-guide/using-property-substitution.html). |

## Mapping secretIDs to key aliases

The following table describes the default secrets and their alias mappings:

| `secretId`                                                         | `alias`                                                                                                                                               | Description                                                                                                | Supported `types`    |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------- |
| `idm.default`                                                      | `openidm-sym-default`                                                                                                                                 | Encryption keystore for legacy JSON objects that do not contain a `purpose` value in their `$crypto` block | `ENCRYPT`, `DECRYPT` |
| `idm.config.encryption`                                            | `openidm-sym-default`                                                                                                                                 | Encrypts configuration information                                                                         | `ENCRYPT`, `DECRYPT` |
| `idm.password.encryption`                                          | `openidm-sym-default`                                                                                                                                 | Encrypts managed user passwords                                                                            | `ENCRYPT`, `DECRYPT` |
| `idm.jwt.session.module.encryption`                                | `openidm-localhost`                                                                                                                                   | Encrypts JWT session tokens                                                                                | `ENCRYPT`, `DECRYPT` |
| `idm.jwt.session.module.signing`                                   | `openidm-jwtsessionhmac-key`                                                                                                                          | Signs JWT session tokens using HMAC                                                                        | `SIGN`, `VERIFY`     |
| `idm.assignment.attribute.encryption`                              | `openidm-sym-default`                                                                                                                                 | Encrypts confidential assignment attributes                                                                | `ENCRYPT`, `DECRYPT` |
| `idm.rs.filter.client.secret`                                      | `rsFilter/clientSecret` field in `authentication.json`	You can use a secret to contain this value. Refer to Store rsFilter client secret as a secret. | The `rsFilter` `client_secret`                                                                             | `GENERIC`            |
| `idm.prometheus.password`[\*](#deprecated-prometheus-footnote)     | `openidm.prometheus.password`[\*](#deprecated-prometheus-footnote) property in `boot.properties`                                                      | The password for Prometheus                                                                                | `GENERIC`            |
| `idm.workflow.email.password`                                      | `mail/password` property in `workflow.json`                                                                                                           | The password for Workflow emails                                                                           | `GENERIC`            |
| `idm.http.client.proxy.password`[\*\*](#deprecated-proxy-footnote) | `openidm.http.client.proxy.password`[\*\*](#deprecated-proxy-footnote) property in `boot.properties`                                                  | The password for the default HTTP client proxy                                                             | `GENERIC`            |

\* []()The `idm.prometheus.password` purpose and `openidm.prometheus.password` property are [deprecated](../release-notes/deprecated-functionality.html#deprecation-prometheus-properties-purpose).

\*\* []()The `idm.http.client.proxy.password` purpose and `openidm.http.client.proxy.password` property are [deprecated](../release-notes/deprecated-functionality.html#deprecation-proxy-properties-purpose).

## Configure email service secret rotation

You can store the basic auth credentials for the email service using purposes. You can store both the username and password or just the password.

### Store password as secret

To store the email service password credential as a secret:

1. Configure a purpose called `idm.basic.auth.email` in your `conf/secrets.json` file. The purpose must resolve to the password for the basic auth connection to the email service. For example:

   ```json
   {
       "name":"secretVolume",
       "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
       "config": {
           "format": "PLAIN",
           "directory": "&{idm.install.dir}/secrets",
           "mappings": [
             {
               "secretId": "idm.basic.auth.email",
               "types": [
                 "GENERIC"
               ]
             }
           ]
       }
   }
   ```

2. In the `auth` settings of your email configuration *(tooltip: You can edit the email service over REST at the config/external.email endpoint, or in the external.email.json file in your project's conf directory.)*, update the `password` value to use the purpose:

   ```json
   {
     ...
     "auth" : {
           "enable" : true,
           "username" : "example",
           "password": {
             "$purpose" : {
               "name" : "idm.basic.auth.email"
             }
           }
     },
     ...
   }
   ```

### Store username and password as a secret

To store the username and password as a secret:

1. Configure a purpose called `idm.basic.auth.email` in your `conf/secrets.json` file:

   ```json
   {
       "name":"secretVolume",
       "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
       "config": {
           "format": "PLAIN",
           "directory": "&{idm.install.dir}/secrets",
           "mappings": [
             {
               "secretId": "idm.basic.auth.email",
               "types": [
                 "GENERIC"
               ]
             }
           ]
       }
   }
   ```

   The purpose must resolve to a JSON object with two fields, `username` and `password`:

   ```json
   {
     "username" : "exampleUsername",
     "password" : "changeit"
   }
   ```

2. In the `auth` settings of your email configuration *(tooltip: You can edit the email service over REST at the config/external.email endpoint, or in the external.email.json file in your project's conf directory.)*, update the `username` and `password` values to use the purpose. You must supply a `jsonPointer` value that indicates the property name in the secret's JSON structure. For example:

   ```json
   {
     ...
     "auth" : {
       "enable" : true,
       "username" : {
         "$purpose" : {
           "name" : "idm.basic.auth.email",
           "jsonPointer" : "/username"
           }
         },
         "password" : {
           "$purpose" : {
           "name" : "idm.basic.auth.email",
           "jsonPointer" : "/password"
           }
         }
     },
     ...
   }
   ```

## Configure secret rotation for connectors

Connectors that support encrypted credentials support storing them in a secret. You can store the `principal` and `credentials`, or just the `credentials`.

### Store the credentials as a secret

1. Configure a purpose called `icf.ldap.credentials` in your `conf/secrets.json` file. The purpose must resolve to the connector's `credentials` value:

   ```json
   {
       "name":"secretVolume",
       "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
       "config": {
           "format": "PLAIN",
           "directory": "&{idm.install.dir}/secrets",
           "mappings": [
             {
               "secretId": "icf.ldap.credentials",
               "types": [
                 "GENERIC"
               ]
             }
           ]
       }
   }
   ```

2. In the `configurationProperties` property of the connector's provisioner file, update the `credentials` value to use the new secret:

   ```json
   {
   ...
     "credentials" : {
       "$purpose": {
         "name": "icf.ldap.credentials"
       }
     },
   ...
   }
   ```

### Store the principal and credentials as a secret

The following procedure demonstrates how to store the LDAP connector's `principal` and `credentials` in a file system based secret store:

1. Configure a purpose called `icf.ldap.credentials` in your `conf/secrets.json` file:

   ```json
   {
       "name":"secretVolume",
       "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
       "config": {
           "format": "PLAIN",
           "directory": "&{idm.install.dir}/secrets",
           "mappings": [
             {
               "secretId": "icf.ldap.credentials",
               "types": [
                 "GENERIC"
               ]
             }
           ]
       }
   }
   ```

   The purpose must resolve to a JSON object with two fields, `principal` and `secret`:

   ```json
   {
     "principal" : "uid=admin",
     "secret" : "changeit"
   }
   ```

2. In the `configurationProperties` property of the connector's provisioner file, update the `principal` and `credentials` values to use the new purpose. You must supply a `jsonPointer` value that indicates the property name in the secret's JSON structure. For example:

   ```json
   {
     ...
     "configurationProperties" : {
       "principal" :  {
         "$purpose": {
           "name": "icf.ldap.credentials",
           "jsonPointer": "/principal"
           }
         },
       "credentials" : {
         "$purpose": {
           "name": "icf.ldap.credentials",
           "jsonPointer": "/secret"
         }
       }
     }
     ...
   }
   ```

If you change the value of the secret after the initial configuration, you must call the `reloadSecrets` connector action on the connector to complete the update:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request POST \
--header "content-type: application/json" \
--data '' \
"http://localhost:8080/openidm/system/ldap?_action=reloadSecrets"
{
    "status": "ok"
}
```

## Store rsFilter client secret as a secret

You can use a secret to store the rsFilter's client secret:

1. Remove the `rsFilter/clientSecret` field from `conf/authentication.json`.

2. In `conf/secrets.json`, define a purpose called `idm.rs.filter.client.secret`. This example shows how to do this using a filesystem secret store:

   ```json
   {
     "name":"secretVolume",
     "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
     "config": {
       "format": "PLAIN",
       "directory": "&{idm.install.dir}/secrets",
       "mappings": [{
           "secretId": "idm.rs.filter.client.secret",
           "types": [
             "GENERIC"
           ]
         }
       ]
     }
   }
   ```

3. Ensure that secret's value resolves to the client secret of the OAuth2 client in PingAM.

## Rotate Hikari credentials

You can store the credentials for the Hikari connection pooling datasource using purposes. This lets you enable whole account or password rotation, depending on your needs.

Credentials are rotated when the existing threads in Hikari expire and new ones are spawned. You can set the time-to-live in your configuration by adding a `maxLifetime` property to the `connectionPool` object. The value of `maxLifetime` should be an integer with a minimum value of `30000`. If `maxLifetime` is set to `0`, credentials will never rotate.

|   |                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------- |
|   | If an account lockout mechanism is configured, ensure that the lockout threshold is greater than the number of IDM instances. |

### Configure whole account rotation

To enable whole account rotation, update `conf/datasource.jdbc-default.json` to read `username` and `password` from a purpose. The following procedure demonstrates how to do this using a file system based secret store:

1. Configure a purpose called, for example, `jdbc.hikari.credentials` in your `conf/secrets.json` file:

   ```json
   {
       "name":"secretVolume",
       "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
       "config": {
           "format": "PLAIN",
           "directory": "&{idm.install.dir}/secrets",
           "mappings": [
             {
               "secretId": "jdbc.hikari.credentials",
               "types": [
                 "GENERIC"
               ]
             }
           ]
       }
   }
   ```

   The purpose must resolve to a JSON object with two fields, here called `username` and `password`:

   ```json
   {
     "username": "example-admin",
     "password": "changeit"
   }
   ```

2. In `conf/datasource.jdbc-default.json`, update the `username` and `password` definitions to resolve to the value provided by your purpose. You must supply a `jsonPointer` value that indicates the property name in the secret's JSON structure. For example:

   ```json
   {
       "driverClass" : "org.postgresql.Driver",
       "jdbcUrl" : "jdbc:postgresql://&{openidm.repo.host}:&{openidm.repo.port}/openidm",
       "databaseName" : "openidm",
       "username" : {
           "$purpose" : {
               "name" : "jdbc.hikari.credentials",
               "jsonPointer" : "/username"
           }
       },
       "password" : {
           "$purpose" : {
               "name" : "jdbc.hikari.credentials",
               "jsonPointer" : "/password"
           }
       },
       "connectionTimeout" : 30000,
       "connectionPool" : {
           "type" : "hikari",
           "minimumIdle" : 20,
           "maximumPoolSize" : 50
       }
   }
   ```

### Configure password rotation

To enable password rotation, update `conf/datasource.jdbc-default.json` to read `password` from a purpose. The following procedure demonstrates how to do this using a file system based secret store:

1. Configure a purpose called, for example, `jdbc.hikari.password` in your `conf/secrets.json` file:

   ```json
   {
       "name":"secretVolume",
       "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
       "config": {
           "format": "PLAIN",
           "directory": "&{idm.install.dir}/secrets",
           "mappings": [
             {
               "secretId": "jdbc.hikari.password",
               "types": [
                 "GENERIC"
               ]
             }
           ]
       }
   }
   ```

2. In `conf/datasource.jdbc-default.json`, update the `password` definition to resolve to the value provided by your purpose. For example:

   ```json
   {
       "driverClass" : "org.postgresql.Driver",
       "jdbcUrl" : "jdbc:postgresql://&{openidm.repo.host}:&{openidm.repo.port}/openidm",
       "databaseName" : "openidm",
       "username" : "openidm",
       "password" : {
           "$purpose" : {
               "name" : "jdbc.hikari.password"
           }
       },
       "connectionTimeout" : 30000,
       "connectionPool" : {
           "type" : "hikari",
           "minimumIdle" : 20,
           "maximumPoolSize" : 50
       }
   }
   ```

## Store Prometheus credentials as a secret

You can use the `idm.prometheus.credentials` well-defined purpose to store your Prometheus credentials:

1. Remove `openidm.prometheus.password` and `openidm.prometheus.username` from `resolver/boot.properties`.

2. In `conf/secrets.json`, define a versioned file system secret store for the `idm.prometheus.credentials` purpose. For example:

   ```json
   {
     "name": "fileSystemStore",
     "class": "org.forgerock.openidm.secrets.config.FileSystemStore",
     "config": {
       "versionSuffix": ".v",
       "directory":"&{idm.install.dir}/secrets",
       "format":"PLAIN",
       "mappings":[
         {
           "secretId":"idm.prometheus.credentials",
           "types":["GENERIC"]
         }
       ]
     }
   }
   ```

3. In the `/secrets` directory, create the `idm.prometheus.credentials.v1` file storing the initial Prometheus username and password:

   ```json
   {
     "username": "prometheus",
     "password":"prometheus1"
   }
   ```

### Rotate Prometheus credentials

1. In `conf/metrics.json`, configure metrics collection by setting `enabled: true`. For more information on configuring Prometheus metrics, refer to [Enable metrics](../monitoring-guide/monitoring.html#enable-metrics).

2. Start IDM.

3. Verify that the Prometheus endpoint is up and can be accessed with the initial password. For more information on verifying the Prometheus endpoint, refer to [Enable metrics](../monitoring-guide/monitoring.html#enable-metrics).

4. In the `/secrets` directory, create the `idm.prometheus.credentials.v2` file storing a new password:

   ```json
   {
     "username": "prometheus",
     "password":"prometheus2"
   }
   ```

5. Verify that the Prometheus endpoint can be accessed with both the initial and new password. The new password may require a few seconds before activating. For more information on verifying the Prometheus endpoint, refer to [Enable metrics](../monitoring-guide/monitoring.html#enable-metrics).

6. Delete `secrets/idm.prometheus.credentials.v1`.

7. Verify that the Prometheus endpoint can be accessed only with the `v2` password. The old password could require a few seconds before deactivating. Learn more about verifying the Prometheus endpoint in [Enable metrics](../monitoring-guide/monitoring.html#enable-metrics).

## Configure proxy secret rotation

You can configure proxies in IDM in two ways:

* The default proxy settings use a combination of system properties and specific secret purposes.

* External services, such as email, REST connectors, and connections between IDM instances, allow direct proxy configuration within their JSON files. These settings override the default proxy configuration when specified.

### Default proxy credentials

IDM provides two ways to handle credentials for the default proxy configuration:

* `idm.http.client.proxy.credentials`: The recommended purpose for managing default proxy credentials. It resolves to a JSON object containing both the username and password.

* `idm.http.client.proxy.password`: A [deprecated](../release-notes/deprecated-functionality.html#deprecation-proxy-properties-purpose) purpose that resolves only to the proxy password. You should migrate away from using this purpose.

The secret referenced by the `idm.http.client.proxy.credentials` purpose should contain a JSON object like this:

```json
{
  "username": "<proxy_username>",
  "password": "<proxy_password>"
}
```

Replace `<proxy_username>` and `<proxy_password>` with the actual credentials for your proxy server.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use the `idm.http.client.proxy.credentials` purpose:- Ensure the corresponding system property `openidm.http.client.proxy.password` is **not** set in your `boot.properties` file.

- Ensure no secret value is defined for the deprecated `idm.http.client.proxy.password` purpose in your `secrets.json` file.Using `idm.http.client.proxy.credentials` allows you to manage the username and password together as a single secret. |

### External service proxy credentials

You can configure proxy credentials for specific external services that offer a `proxy` configuration block in their JSON files, for example, `external.rest.json`.

Set the `proxy.userName` and `proxy.password` fields to reference a secret containing a credential pair:

```json
"proxy": {
    "proxyUri": "http://your-proxy.example.com:8888",
    "userName": {
        "$purpose": {
            "name": "idm.external.proxy.credentials",
            "jsonPointer": "/username"
        }
    },
    "password": {
        "$purpose": {
            "name": "idm.external.proxy.credentials",
            "jsonPointer": "/password"
        }
    }
}
```

The `name` must match the `secretId` you defined in your `conf/secrets.json` file for these external proxy credentials.

The `jsonPointer` values (`/username` and `/password` in this example) must correspond to the keys used within the JSON secret object stored for the `idm.external.proxy.credentials` purpose.

### Rotate proxy credentials

To rotate the credentials IDM uses to authenticate with a proxy:

* If using a non-versioned secret store, such as a plain file system store, update the content of the secret file or value.

* If using a versioned secret store, such as a versioned file system store, add a new version of the secret (for example, add a `.v2` file).

|   |                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------- |
|   | For zero-downtime rotation, your proxy must support multiple user accounts simultaneously during the transition. |

The general steps for zero-downtime rotation are:

1. Add the new user account credentials to your proxy configuration, keeping the old ones active for now.

2. Update the secret value in IDM to use the new account details, either by modifying the existing secret file, value, or adding a new version. IDM will start using the new credentials as connections are refreshed or new versions are picked up.

3. After confirming IDM is using the new credentials, you can safely remove the old user account from the proxy configuration.

---

---
title: Secure IDM data
description: Secure PingIDM data using TLS/SSL, explicit encryption for data in transit and at rest, and automatic encryption of sensitive configuration values
component: pingidm
version: 8.1
page_id: pingidm:security-guide:chap-data
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/chap-data.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "TLS/SSL", "Encryption", "Password", "Secrets", "JSON"]
---

# Secure IDM data

Beyond relying on end-to-end availability of TLS/SSL to protect data, IDM also supports explicit encryption of data that goes on the network. This can be important if the TLS/SSL termination happens prior to the final endpoint.

IDM also supports encryption of data stored in the repository, using the symmetric keys specified in `conf/secrets.json`. This protects against some attacks on the data store. Explicit table mapping is supported for encrypted string values.

IDM automatically encrypts sensitive data (such as passwords) in configuration files, and replaces cleartext values when the system first reads the configuration file. Take care with configuration files that contain clear text values that IDM has not yet read and encrypted.

---

---
title: Secure network connections
description: Configure PingIDM to secure network connections using TLS/SSL, HSTS, mutual authentication, payload size limits, and CSRF protection
component: pingidm
version: 8.1
page_id: pingidm:security-guide:chap-connections
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/chap-connections.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "TLS/SSL", "Network", "Connections", "Ports", "CA-Signed Certificates", "Proxy Server", "Load Balancer"]
section_ids:
  security-ssl: Use TLS/SSL
  security-https: Restrict REST access to the HTTPS port
  security-urls: Protect sensitive REST interface URLs
  strict-transport-security: Enable HTTP Strict-Transport-Security
  mixed-client-auth: Enable mixed client authentication
  sni-host-check: Disable SNI host check
  max-payload-size: Restrict the HTTP payload size
  clustering-load-balancer: Deploy securely behind a load balancer
  configuring-proxy: Connect to IDM through a proxy server
  csrf-filter: Protect against Cross-Site Request Forgery
---

# Secure network connections

This topic explains how to secure incoming connections and ports. As a general precaution in production environments, avoid communication over insecure HTTP.

## Use TLS/SSL

Use TLS/SSL to access IDM, ideally with mutual authentication so that only trusted systems can invoke each other. TLS/SSL protects data on the network. Mutual authentication with strong certificates, imported into the truststore and keystore of each application, provides a level of confidence for trusting application access.

## Restrict REST access to the HTTPS port

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In IDM 8.0, `jetty.xml` is no longer supported.When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment.Learn more in [Jetty 12 support](../release-notes/whats-new.html#jetty_12_support). |

In a production environment, you should restrict REST access to a secure port:

Delete the following embedded Jetty web server configuration in your project's `conf/webserver.listener-http.json` file that includes the `openidm.port.http` property:

```json
{
  "enabled": {
    "$bool": "&{openidm.http.enabled|true}"
  },
  "port": {
    "$int": "&{openidm.port.http|8080}"
  }
}
```

Use a certificate to secure REST access over HTTPS. You can use self-signed certificates in a test environment. In production, all certificates should be signed by a certificate authority (CA). The examples in this guide assume a CA-signed certificate named `ca-cert.pem`.

## Protect sensitive REST interface URLs

Anything attached to the router is accessible with the default policy, including the repository. If you do not need such access, deny it in the authorization policy to reduce the attack surface.

In addition, you can deny direct HTTP access to system objects in production, particularly access to `action`. As a rule of thumb, do not expose anything that is not used in production.

For an example that shows how to protect sensitive URLs, refer to [Configure Access Control in access.json](../auth-guide/authorization-and-roles.html#access-json).

## Enable HTTP Strict-Transport-Security

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In IDM 8.0, `jetty.xml` is no longer supported.When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment.Learn more in [Jetty 12 support](../release-notes/whats-new.html#jetty_12_support). |

[HTTP Strict-Transport-Security (HSTS)](https://www.tunetheweb.com/security/http-security-headers/hsts/) is a web security policy that forces browsers to make secure HTTPS connections to specified web applications. HSTS can protect websites against passive eavesdropper and active man-in-the-middle attacks.

Enabled by default, IDM provides an HSTS configuration for the following configuration files:

* `webserver.listener-https.json`

* `webserver.listener-mutualAuth.json`

To enable HSTS for additional `webserver.listener-*.json` configurations:

1. Set `secure` to `true`.

2. Set `sslCertAlias` to the certificate alias you want the server to present.

The following example shows this configuration in `conf/webserver.listener-https.json`:

```json
{
  "enabled": {
    "$bool": "&{openidm.https.enabled|true}"
  },
  "port": {
    "$int": "&{openidm.port.https|8443}"
  },
  "secure": true,
  "sslCertAlias": "&{openidm.https.keystore.cer.alias|openidm-localhost}"
}
```

## Enable mixed client authentication

You can configure IDM to request a client certificate during the TLS handshake without requiring it. This allows a single port to support mixed traffic, accepting connections from clients that present a valid certificate (mTLS) as well as those that don't (standard TLS).

To enable this configuration, set `wantClientAuth` to `true` and `mutualAuth` to `false` in the appropriate `conf/webserver.listener-*.json` file.

The following example configures this behavior for the HTTPS listener:

```json
{
  "enabled": {
    "$bool": "&{openidm.https.enabled|true}"
  },
  "port": {
    "$int": "&{openidm.port.https|8443}"
  },
  "secure": true,
  "mutualAuth": false,
  "wantClientAuth": true,
  "sslCertAlias": "&{openidm.https.keystore.cer.alias|openidm-localhost}"
}
```

## Disable SNI host check

By default, IDM uses Jetty Server Name Indication (SNI) to check the requested hostname against the certificate. This feature is implemented with Jetty's `SecureRequestCustomizer`.

Although not recommended for security reasons, disabling this check might be necessary in certain proxy configurations, such as SSL pass-through.

To disable SNI host checking, add the `"sniHostCheckEnabled": false` property to your project's applicable `conf/webserver.listener-*.json` files.

Example `sniHostCheckEnabled`

```json
{
  "enabled": {
    "$bool": "&{openidm.https.enabled|true}"
  },
  "port": {
    "$int": "&{openidm.port.https|8443}"
  },
  "secure": true,
  "sslCertAlias": "&{openidm.https.keystore.cer.alias|openidm-localhost}",
  "sniHostCheckEnabled": false
}
```

Learn more in the [Jetty 12 documentation](https://javadoc.jetty.org/jetty-12/org/eclipse/jetty/server/SecureRequestCustomizer.html#setSniHostCheck%28boolean%29).

## Restrict the HTTP payload size

Restricting the size of HTTP payloads can protect the server against large payload HTTP DDoS attacks. IDM includes a servlet filter that limits the size of an incoming HTTP request payload, and returns a `413 Request Entity Too Large` response when the maximum payload size is exceeded.

By default, the maximum payload size is 5MB. You can configure the maximum size in your project's `conf/servletfilter-payload.json` file. That file has the following structure by default:

```json
{
    "classPathURLs" : [ ],
    "systemProperties" : { },
    "requestAttributes" : { },
    "scriptExtensions" : { },
    "initParams" : {
        "maxRequestSizeInMegabytes" : 5
    },
    "urlPatterns" : [
        "/*"
    ],
    "filterClass" : "org.forgerock.openidm.jetty.LargePayloadServletFilter"
}
```

Change the value of the `maxRequestSizeInMegabytes` property to set a different maximum HTTP payload size.

The remaining properties in this file are described in [Additional servlet filters](../install-guide/register-servlet-filters.html).

## Deploy securely behind a load balancer

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In IDM 8.0, `jetty.xml` is no longer supported.When serving SSL requests, Jetty 12 checks that the incoming host header matches the server certificate's subject and returns a `400 Bad Request` error on a mismatch. If you're upgrading to IDM 8.0, you must ensure your IDM server certificate subject matches the host name used by your deployment.Learn more in [Jetty 12 support](../release-notes/whats-new.html#jetty_12_support). |

If you're deploying IDM behind a system such as a load balancer, firewall, or a reverse proxy, you must set the `"proxyLoadBalancerConnection"` field to `true` in your `conf/webserver.listener-*.json` configurations:

```json
{
  "enabled": {
    "$bool": "&{openidm.http.enabled|true}"
  },
  "port": {
    "$int": "&{openidm.port.http|8080}"
  },
  "proxyLoadBalancerConnection": true
}
```

## Connect to IDM through a proxy server

If you're connecting to IDM through a proxy server, you must set the `"proxyLoadBalancerConnection"` field to `true` in your `conf/webserver.listener-*.json` configurations:

```json
{
 "enabled": {
   "$bool": "&{openidm.http.enabled|true}"
 },
 "port": {
   "$int": "&{openidm.port.http|8080}"
 },
 "proxyLoadBalancerConnection": true
}
```

## Protect against Cross-Site Request Forgery

IDM provides a filter to protect against [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf). The filter is disabled by default. To enable it, set the following property in `resolver/boot.properties`:

```properties
openidm.csrfFilter.enabled=true
```

The filter requires the client to send a CSRF cookie (`X-CSRF-Token`) on every request. By default, this cookie is the JWT session cookie (`session-jwt`), obtained on authentication. If your client uses a different cookie for authentication, set the name of that cookie in the following property in `resolver/boot.properties`:

```properties
openidm.csrfFilter.authCookieName=session-jwt
```

If there are HTTP request paths that the CSRF filter should always allow, set these paths as comma-separated values of the `openidm.csrfFilter.pathWhitelistCSV` property in `resolver/boot.properties`. For example:

```properties
openidm.csrfFilter.pathWhitelistCSV=/openidm/example,/openidm/my-project
```

---

---
title: Secure sensitive values
description: Encode PingIDM managed object attribute values using reversible encryption or salted hash algorithms such as SHA-256, Bcrypt, and PBKDF2
component: pingidm
version: 8.1
page_id: pingidm:security-guide:encoding-attribute-values
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/encoding-attribute-values.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Password", "Encryption", "Salted Hash", "Algorithms", "HMAC", "SHA-256", "SHA-384", "SHA-512"]
section_ids:
  encoding-encryption: Reversible encryption
  encrypt-ui: Configure encryption using the admin UI
  encoding-salted-hash: Salted hash algorithms
  secure-hash-ui: Configure hashing using the admin UI
---

# Secure sensitive values

There are two ways to encode attribute values for managed objects—reversible encryption and salted hashing algorithms. Examples of encoded attribute values include passwords, authentication questions, credit card numbers, and social security numbers. If passwords are already encoded on the external resource, they are generally excluded from the synchronization process. For more information, refer to [Manage password policies](passwords.html).

You configure attribute value encoding, per schema property, in the managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)*. The following sections show how to use reversible encryption and salted hash algorithms to encode attribute values.

## Reversible encryption

Reversible encryption secures your data by encrypting it with a key. You should use encryption in cases where you need to decrypt the sensitive data to synchronize it or provide it to another system.

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Encryption keys are mapped to *purposes* in your project's `conf/secrets.json` file. For more information, refer to [Secret stores](secret-stores.html). |

The following managed object configuration *(tooltip: You can edit the managed object configuration over REST at the config/managed endpoint, or directly in the conf/managed.json file.)* encrypts and decrypts the `password` attribute using the default `idm.password.encryption` purpose:

```json
{
    "objects" : [
        {
            "name" : "user",
            ...
            "schema" : {
                ...
                "properties" : {
                    ...
                    "password" : {
                        "title" : "Password",
                        ...
                        "encryption" : {
                            "purpose" : "idm.password.encryption"
                        },
                        "scope" : "private",
                    }
            ...
        }
    ]
}
```

You specify the encryption cipher or keysize by specifying a `cipher` property of the related `encryption` object in your configuration.

The `cipher` property must be a valid *transformation* string as described in the [javax.crypto.Cipher reference](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/javax/crypto/Cipher.html). The following example demonstrates using the transformation `AES/GCM/NoPadding`:

```json
...
    "encryption" : {
        "purpose": "idm.password.encryption",
        "cipher": "AES/GCM/NoPadding"
},
```

By default, IDM uses `AES/CBC/PKCS5Padding`—the Advanced Encryption Standard (AES) algorithm with cipher block chaining, PKCS#5 padding, and a key size of 128.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you change the default cipher, you must specify the algorithm, mode, and padding. If the algorithm does not require a mode, use `NONE`. If the algorithm does not require padding, use `NoPadding`. |

To encrypt attribute values from the command-line, refer to [encrypt](../setup-guide/chap-cli.html#cli-encrypt).

### Configure encryption using the admin UI

1. Select Configure > Managed Objects, and select the object type whose property values you want to encrypt (for example, User).

2. On the Properties tab, select the property whose value should be encrypted and select the Encrypt checkbox.

## Salted hash algorithms

To encode attribute values with salted hash algorithms, add the `secureHash` property to the attribute definition and define the hashing configuration. The configuration depends on the algorithm that you choose.

If you do not specify an algorithm, `SHA-256` is used by default. MD5 and SHA-1 are supported for legacy reasons, but should not be used in production environments.

**Supported Hashing Algorithms and Configuration Properties**

| Algorithm                                        | Config Property and Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BCRYPT`\[[1](#_footnotedef_1 "View footnote.")] | * `cost`

  Value between 4 and 31. Default is `13`.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `PBKDF2`                                         | - `hashLength`

  Byte-length of the generated hash. Default is `16`.

- `saltLength`

  Byte-length of the salt value. Default is `16`.

- `iterations`

  Number of cryptographic iterations. Default is `20000`.

- `hmac`

  HMAC algorithm. Default is `SHA3-256`.

  Supported values:

  * `SHA-224`

  * `SHA-256`

  * `SHA-384`

  * `SHA-512`

  * `SHA3-224`

  * `SHA3-256`

  * `SHA3-384`

  * `SHA3-512`                                                                                          |
| `SCRYPT`\[[1](#_footnotedef_1 "View footnote.")] | * `hashLength`

  Byte-length of the generated hash, must be greater than or equal to 8. Default is `16`.

* `saltLength`

  Byte-length of the salt value. Default is `16`.

* `n`

  CPU/Memory cost. Must be greater than 1, a power of 2, and less than *2^(128 \* r / 8)*. Default is `32768`.

* `p`

  Parallelization. Must be a positive integer less than or equal to *Integer.MAX\_VALUE / (128 \* r \* 8)*. Default is `1`.

* `r`

  Block size. Must be greater than or equal to 1. Default is `8`. |
| `SHA-256`                                        | - `saltLength`

  Byte-length of the salt value. Default is `16`.	This is the default hashing.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `SHA-384`                                        | * `saltLength`

  Byte-length of the salt value. Default is `16`.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `SHA-512`                                        | - `saltLength`

  Byte-length of the salt value. Default is `16`.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

The following list displays supported hash algorithms and example configurations:

* `SHA-256`

  ```json
  "secureHash" : {
      "algorithm" : "SHA-256",
      "saltLength" : 16
  }
  ```

* `SHA-384`

  ```json
  "secureHash" : {
      "algorithm" : "SHA-384",
      "saltLength" : 16
  }
  ```

* `SHA-512`

  ```json
  "secureHash" : {
      "algorithm" : "SHA-512",
      "saltLength" : 16
  }
  ```

* `Bcrypt`\[[1](#_footnotedef_1 "View footnote.")]

  ```json
  "secureHash" : {
      "algorithm" : "BCRYPT",
      "cost" : 16
  }
  ```

* `Scrypt`\[[1](#_footnotedef_1 "View footnote.")]

  ```json
  "secureHash" : {
      "algorithm" : "SCRYPT",
      "hashLength" : 16,
      "saltLength" : 16,
      "n" : 32768,
      "r" : 8,
      "p" : 1
  }
  ```

* Password-Based Key Derivation Function 2 (`PBKDF2`)

  ```json
  "secureHash" : {
      "algorithm" : "PBKDF2",
      "hashLength" : 16,
      "saltLength" : 16,
      "iterations" : 10,
      "hmac" : "SHA-256"
  }
  ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some one-way hash functions are designed to be computationally *expensive*. Functions such as PBKDF2, Bcrypt, and Scrypt are designed to be relatively slow even on modern hardware. This makes them generally less susceptible to brute force attacks. *However*, computationally expensive functions can dramatically increase response times. If you use these functions, be aware of the performance impact and perform extensive testing before deploying your service in production. Do not use functions like PBKDF2 and Bcrypt for any accounts that are used for frequent, short-lived connections.Hashing is a one-way operation, such that the original value cannot be recovered. Therefore, if you hash the value of any property, you cannot synchronize that property value to an external resource. For managed object properties with hashed values, you must either exclude those properties from the mapping or set a random default value if the external resource requires the property. |

The following excerpt of a managed object configuration shows that values of the `password` attribute are hashed using the `SHA-256` algorithm:

```json
{
    "objects" : [
        {
            "name" : "user",
            ...
            "schema" : {
                ...
                "properties" : {
                    ...
                    "password" : {
                        "title" : "Password",
                        ...
                        "secureHash" : {
                            "algorithm" : "SHA-256"
                        },
                        "scope" : "private",
                    }
            ...
        }
    ]
}
```

To hash attribute values from the command-line, refer to [secureHash](../setup-guide/chap-cli.html#cli-secure-hash).

### Configure hashing using the admin UI

You can set a property hash algorithm using the admin UI. However, only some algorithms and none of the enhanced configuration options are supported.

> **Collapse: Show Me**
>
> ![Admin UI hash property](_images/Admin-UI-hash-property.gif)

1. Select Configure > Managed Objects, and select an object type (for example, User).

2. On the Properties tab, select a property to hash.

3. On the Property *Name* page, click the Privacy & Encryption tab, and select Hashed.

4. From the adjacent drop-down menu, select an algorithm.

5. Click Save.

***

[1](#_footnoteref_1). This hashing algorithm is not supported by [Bouncy Castle FIPS](security-bouncy-castle-fips.html)

---

---
title: Secure the repository
description: Secure the PingIDM repository by setting strong passwords for JDBC or PingDS connections and encrypting stored credentials at startup
component: pingidm
version: 8.1
page_id: pingidm:security-guide:security-protect-repo
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/security-protect-repo.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "JDBC", "User Data", "Password", "Directory Server"]
---

# Secure the repository

Configuration data and, in most deployments, user data, are stored in the IDM repository. In production deployments, you must secure access to the repository, and encrypt sensitive stored data.

For JDBC repositories, use a strong password for the connection to the repository and change at least the password of the database user (`openidm` by default). When you change the database username and/or password, update your database connection configuration file (`conf/datasource.jdbc-default.json`).

For a DS repository, change the `bindDN` and `bindPassword` for the directory server user in the `ldapConnectionFactories` property in the `repo.ds.json` file.

In both cases, the password is encrypted on server startup, using the key specified in the `idm.password.encryption` secret ID in `conf/secrets.json`.

---

---
title: Security
description: Guide to securing PingIDM deployments
component: pingidm
version: 8.1
page_id: pingidm:security-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security"]
page_aliases: ["index.adoc"]
---

# Security

> Secure PingIDM deployments.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

Out-of-the-box, IDM is set up for ease of development and deployment. When you deploy IDM in production, there are specific precautions you should take to minimize security breaches. This guide describes the IDM security mechanisms and strategies you can use to reduce risk and mitigate threats to IDM security.

[icon: key, set=fad, size=3x]

#### [Certificates and keys](stores-certs-keys.html)

Manage secrets, certificates, and keys.

[icon: asterisk, set=fad, size=3x]

#### [Passwords](passwords.html)

Store and manage passwords securely.

[icon: network-wired, set=fad, size=3x]

#### [Network](chap-connections.html)

Secure network connections to IDM resources.

[icon: database, set=fad, size=3x]

#### [Data](chap-data.html)

Secure IDM stored data.

---

---
title: Sensitive files and directories
description: Protect sensitive PingIDM files and directories from unauthorized access on Unix and Windows by restricting ownership and permissions
component: pingidm
version: 8.1
page_id: pingidm:security-guide:security-files
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/security-files.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Filesystem", "UNIX", "Windows"]
section_ids:
  security-files-unix: Protect sensitive files in Unix
  security-files-windows: Protect sensitive files in Windows
---

# Sensitive files and directories

Protect IDM files from access by unauthorized users. In particular, prevent other users from reading files in at least the `openidm/resolver/` and `openidm/security/` directories.

The objective is to limit access to the user that is running the service. Depending on the operating system and configuration, that user might be `root`, `Administrator`, `openidm`, or something similar.

## Protect sensitive files in Unix

1. Make sure that user and group ownership of the installation and project directories is limited to the user running the IDM service.

2. Disable access of any sort for `other` users. One simple command for that purpose, from the `/path/to/openidm` directory, is:

   ```bash
   chmod -R o-rwx .
   ```

## Protect sensitive files in Windows

The IDM process in Windows is typically run by the `Local System` service account.

If you are concerned about the security of this account, you can set up a service account that only has permissions for IDM-related directories, then remove User access to the directories noted above. You should also configure the service account to deny local and remote login. For more information, refer to the [User Rights Assignment](https://technet.microsoft.com/en-us/library/dn221963.aspx) article in Microsoft's documentation.
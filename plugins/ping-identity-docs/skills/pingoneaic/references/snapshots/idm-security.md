---
title: Secure identity data
description: Secure managed object sensitive data using reversible encryption or salted hashing
component: pingoneaic
page_id: pingoneaic:idm-security:secure-sensitive-data
canonical_url: https://docs.pingidentity.com/pingoneaic/idm-security/secure-sensitive-data.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Password", "Encryption", "Salted Hash", "Algorithms", "HMAC", "SHA-256", "SHA-384", "SHA-512"]
section_ids:
  ssd-reversible-encryption: Reversible encryption
  encrypt-ui: Encrypt and decrypt properties using the IDM admin console
  keystore-encrypt-decrypt: Encrypt and decrypt properties using REST
  encoding-salted-hash: Salted hashing
  secure-hash-ui: Configure hashing using the IDM admin console
---

# Secure identity data

Some managed objects contain data which you want to secure. Examples of sensitive data include:

* Passwords

* Authentication questions

* Credit card numbers

* Social security numbers

There are two ways to secure a managed object's sensitive data properties: *reversible encryption* and *salted hashing*. To configure encryption or hashing, update the managed object's configuration at the `openidm/config/managed` endpoint.

## Reversible encryption

Reversible encryption secures your data by encrypting it with a key. It should be used in cases where you may need to decrypt the sensitive data in order to synchronize it or provide it to another system.

### Encrypt and decrypt properties using the IDM admin console

To encrypt or decrypt a property of a managed object using the IDM admin console:

1. On the top navigation bar, select Configure > Managed Objects. A list of the system's managed objects displays.

2. Select an object type (for example, User). A page displays where you can configure the managed object's properties, details, and scripts.

3. On the Properties tab, select the property to be encrypted. A page displays where you can can manage the property.

4. On the Privacy & Encryption tab, select the Encrypted toggle. If encryption is enabled, the toggle is green and displays a white checkmark. If encryption is disabled, the toggle is grey and no checkmark displays.

5. In the Encryption Purpose field, type `idm.password.encryption`.

   |   |                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------- |
   |   | A blank or invalid purpose may cause errors. Do not leave the field blank or provide an invalid purpose. |

6. Click Save.

### Encrypt and decrypt properties using REST

You can encrypt and decrypt property values over REST by calling the `openidm.encrypt` or `openidm.decrypt` scripts on the `openidm/script?_action=eval` endpoint.

Refer to [Functions available in identity-related scripts](../idm-scripting/scripting-func-engine.html) for more information about the [openidm.encrypt](../idm-scripting/scripting-func-engine.html#function-encrypt) and [openidm.decrypt](../idm-scripting/scripting-func-engine.html#function-decrypt) functions.

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud tenants only support the AES-128 encryption algorithm and the `idm.password.encryption` alias. |

This `curl` command demonstrates using `openidm.encrypt` to encrypt a key-value pair (`{"myKey": "myPassword"}`):

```
curl \
--header "Authorization: Bearer <access-token>" \
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
  "source":"openidm.encrypt(val,null,'idm.password.encryption');"
}' \
"https://<tenant-env-fqdn>/openidm/script?_action=eval"
{
  "$crypto": {
    "type": "x-simple-encryption",
    "value": {
      "cipher": "AES/CBC/PKCS5Padding",
      "stableId": "openidm-sym-default",
      "salt": "qAS/eG7zdnFyK5H8lXvqTA==",
      "data": "zewf6hR1yjp34EFJqUGpdnzzFCPJs2IaX4V97jdQlSI=",
      "keySize": 128,
      "purpose": "idm.password.encryption",
      "iv": "A4pIiY6kG6t0uLyLmJAoWQ==",
      "mac": "sFDJqg0Mmp0Ftl+1q1Bjzw=="
    }
  }
}
```

This `curl` command demonstrates decrypting an object using `openidm.decrypt`:

```
curl \
--header "Authorization: Bearer <access-token>" \
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
          "keySize": 128,
          "purpose": "idm.password.encryption",
          "iv": "A4pIiY6kG6t0uLyLmJAoWQ==",
          "mac": "sFDJqg0Mmp0Ftl+1q1Bjzw=="
        }
      }
    }
  },
  "source":"openidm.decrypt(val);"
}' \
"https://<tenant-env-fqdn>/openidm/script?_action=eval"
{
  "myKey": "myPassword"
}
```

The `$crypto` object

|   |                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `$crypto` blob is classified as an Advanced Identity Cloud internal object and is subject to change. Don't rely on the format of this object. |

Encrypted objects and properties include a `$crypto` object which indicate how the property was encrypted. This object should be provided when you use `openidm.decrypt`. For example:

```json
"password": {
  "$crypto": {
    "type": "x-simple-encryption",
    "value": {
      "cipher": "AES/CBC/PKCS5Padding",
      "stableId": "openidm-sym-default",
      "salt": "Gwi+AGrn+VBOTmyq+TTuuw==",
      "data": "+9i7XAXpWZBXYTVEOBkM+w==",
      "keySize": 128,
      "purpose": "idm.password.encryption",
      "iv": "4xtI88eFu5tgfm8ooq+yqQ==",
      "mac": "N1zsYo71M/b/G6iLOhNohA=="
    }
  }
}
```

## Salted hashing

*Hashing* is a one-way process of transforming a key or string of characters into a different fixed-length value. *Salting* is a process of improving the hash's security by adding random data as additional input. If you do not need to synchronize your secure data or provide it to another system in an unencrypted form, hash and salt it.

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | Hashed data cannot be decrypted. Do not secure your data by hashing it if you will need the unencrypted value. |

The following table displays supported hashing algorithms:

| Algorithm | Attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BCRYPT`  | * `cost`

  Value between 4 and 31. The default is `13`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `PBKDF2`  | - `hashLength`

  Byte-length of the generated hash. The default is `16`.

- `saltLength`

  Byte-length of the salt value. The default is `16`.

- `iterations`

  Number of cryptographic iterations. The default is `20000`.

- `hmac`

  HMAC algorithm. The default is `SHA3-256`.

  Supported values:

  * `SHA-224`

  * `SHA-256`

  * `SHA-384`

  * `SHA-512`

  * `SHA3-224`

  * `SHA3-256`

  * `SHA3-384`

  * `SHA3-512`                                                                                              |
| `SCRYPT`  | * `hashLength`

  Byte-length of the generated hash, must be greater than or equal to 8. The default is `16`.

* `saltLength`

  Byte-length of the salt value. The default is `16`.

* `n`

  CPU/Memory cost. Must be greater than 1, a power of 2, and less than *2^(128 \* r / 8)*. The default is `32768`.

* `p`

  Parallelization. Must be a positive integer less than or equal to *Integer.MAX\_VALUE / (128 \* r \* 8)*. The default is `1`.

* `r`

  Block size. Must be greater than or equal to 1. The default is `8`. |
| `SHA-256` | - `saltLength`

  Byte-length of the salt value. The default is `16`.	This is the default algorithm.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `SHA-384` | * `saltLength`

  Byte-length of the salt value. The default is `16`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `SHA-512` | - `saltLength`

  Byte-length of the salt value. The default is `16`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

Choosing a hashing function

PBKDF2, Bcrypt, and Scrypt are relatively slow algorithms even on modern hardware. If you use them, be aware of the performance impact. Accounts which are used for frequent, short-lived connections should not be secured using slow algorithms.

|   |                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The MD5 and SHA-1 algorithms are not considered secure and are only supported for legacy reasons. Do not use them in production environments. |

### Configure hashing using the IDM admin console

You can set a property hash algorithm using the IDM admin console. Only some algorithms and none of the enhanced configuration options are supported.

> **Collapse: Show Me**
>
> ![Admin UI hash property](_images/Admin-UI-hash-property.gif)

1. Select Configure > Managed Objects, and select an object type (for example, User).

2. On the Properties tab, select a property to hash.

3. On the Property page, click the Privacy & Encryption tab, and select Hashed.

4. From the adjacent drop-down menu, select an algorithm.

5. Click Save.
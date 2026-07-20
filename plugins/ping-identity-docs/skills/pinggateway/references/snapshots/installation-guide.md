---
title: Downloading PingGateway
description: Download the PingGateway software package to install and run it in your environment
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:download
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/download.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Install", "Configuration"]
---

# Downloading PingGateway

The .zip file unpacks into a `/path/to/ping-gateway-2026.6.0` directory with the following content:

* `bin`: Start and stop executables

* `classes`: Initially empty; used to install patches from support

* `docker/Dockerfile`: Dockerfile and README to build a PingGateway Docker image

* `legal-notices`: Licenses and copyrights

* `lib`: PingGateway and third-party libraries

  1. Create a local installation directory for PingGateway like `/path/to`.

     |   |                                                                                                                                               |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The installation directory should be a new, empty directory. Installing PingGateway into an existing installation directory can cause errors. |

  2. Download `PingGateway-2026.6.0.zip` from the [Ping Identity Download Center](https://product-downloads.pingidentity.com/), and copy the .zip file to the installation directory:

     ```console
     $ cp PingGateway-2026.6.0.zip /path/to/PingGateway-2026.6.0.zip
     ```

  3. Unzip the file:

     ```console
     $ unzip PingGateway-2026.6.0.zip
     ```

     The directory `/path/to/ping-gateway-2026.6.0` is created.

---

---
title: Encrypting and sharing PingGateway JWT sessions
description: Configure authenticated encryption for PingGateway JWT sessions and share encrypted JWT sessions across multiple PingGateway instances
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:jwtsession-using
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/jwtsession-using.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-23T12:00:00Z
keywords: ["Configuration", "HMAC", "JSON", "Encryption"]
section_ids:
  jwtsession-encrypt: Encrypt JWT sessions
  jwtsession-sharesecrets: Share JWT sessions between multiple instances of PingGateway
---

# Encrypting and sharing PingGateway JWT sessions

PingGateway JWT-based sessions store session information in JWT cookies on the user-agent. Learn more in [PingGateway sessions](../about/about-sessions.html).

This page describes how to set authenticated encryption for JWT-based sessions using symmetric keys.

With [authenticated encryption](https://en.wikipedia.org/wiki/Authenticated_encryption), PingGateway encrypts data and signs it with HMAC in a single step.

## Encrypt JWT sessions

This section describes how to set up a keystore with a symmetric key for authenticated encryption of a JWT session.

1. Set up a keystore to contain the encryption key, where the keystore and the key have the password `password`:

   1. Locate a directory for secrets and go to it:

      ```console
      $ cd /path/to/secrets
      ```

   2. Generate the key:

      ```console
      $ keytool \
        -genseckey \
        -alias symmetric-key \
        -keystore jwtsessionkeystore.pkcs12 \
        -storepass password \
        -storetype pkcs12 \
        -keyalg HmacSHA512 \
        -keysize 512
      ```

      |   |                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------- |
      |   | Because keytool converts all characters in its key aliases to lowercase, use only lowercase in alias definitions of a keystore. |

2. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/jwt-session-encrypt.json`

   * Windows

     `%appdata%\OpenIG\config\routes\jwt-session-encrypt.json`

   ```json
   {
     "name": "jwt-session-encrypt",
     "heap":  [{
       "name": "KeyStoreSecretStore-1",
       "type": "KeyStoreSecretStore",
       "config": {
         "file": "/path/to/secrets/jwtsessionkeystore.pkcs12",
         "storeType": "PKCS12",
         "storePasswordSecretId": "keystore.secret.id",
         "secretsProvider": ["SystemAndEnvSecretStore-1"],
         "mappings": [{
           "secretId": "jwtsession.symmetric.secret.id",
           "aliases": ["symmetric-key"]
         }]
       }
     },
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       }
     ],
     "session": {
       "type": "JwtSessionManager",
       "config": {
         "authenticatedEncryptionSecretId": "jwtsession.symmetric.secret.id",
         "encryptionMethod": "A256CBC-HS512",
         "secretsProvider": ["KeyStoreSecretStore-1"],
         "cookie": {
           "name": "IG",
           "domain": ".example.com"
         }
       }
     },
     "handler": {
       "type": "StaticResponseHandler",
       "config": {
         "status": 200,
         "headers": {
           "Content-Type": [ "text/plain; charset=UTF-8" ]
         },
         "entity": "Hello world!"
       }
     },
     "condition": "${request.uri.path == '/jwt-session-encrypt'}"
   }
   ```

   Source: [jwt-session-encrypt.json](../_attachments/config/routes/jwt-session-encrypt.json)

   Notice the following features of the route:

   * The route matches requests to `/jwt-session-encrypt`.

   * The KeyStoreSecretStore uses the SystemAndEnvSecretStore in the heap to manage the store password.

   * The JWTSessionManager uses the KeyStoreSecretStore in the heap to manage the session encryption secret.

3. In the terminal where you will run the PingGateway instance, create an environment variable for the value of the keystore password:

   ```console
   $ export KEYSTORE_SECRET_ID='cGFzc3dvcmQ='
   ```

   The password is retrieved by the SystemAndEnvSecretStore, and must be base64-encoded.

## Share JWT sessions between multiple instances of PingGateway

This section shows how to set up a deployment with three PingGateway servers sharing JWT-based sessions.

![Three servers sharing a JWT-based session](_images/ig-jwt-session.png)

1. Set up a keystore to contain the encryption key, where the keystore and the key have the password `password`:

   1. Locate a directory for secrets and go to it:

      ```console
      $ cd /path/to/secrets
      ```

   2. Generate the key:

      ```console
      $ keytool \
        -genseckey \
        -alias symmetric-key \
        -keystore jwtsessionkeystore.pkcs12 \
        -storepass password \
        -storetype pkcs12 \
        -keyalg HmacSHA512 \
        -keysize 512
      ```

      |   |                                                                                                                                 |
      | - | ------------------------------------------------------------------------------------------------------------------------------- |
      |   | Because keytool converts all characters in its key aliases to lowercase, use only lowercase in alias definitions of a keystore. |

2. Prepare the PingGateway installation:

   1. Create an installation directory for PingGateway in `/path/to`.

   2. Download and unzip PingGateway-2026.6.0.zip in `/path/to`, as described in the [Installing PingGateway](preface.html). The directory `/path/to/ping-gateway-2026.6.0` is created.

3. Set up the first instance of PingGateway, which acts as the load balancer:

   1. Create a configuration directory for the instance and go to it:

      ```console
      $ mkdir -p /path/to/config-instance1/config/routes
      ```

   2. Add the following route:

      * Linux

        `/path/to/config-instance1/config/routes/instance1-loadbalancer.json`

      * Windows

        `%appdata%\path\to\config-instance1\config\routes\instance1-loadbalancer.json`

      ```json
      {
        "name": "instance1-loadbalancer",
        "heap": [{
          "name": "KeyStoreSecretStore-1",
          "type": "KeyStoreSecretStore",
          "config": {
            "file": "/path/to/secrets/jwtsessionkeystore.pkcs12",
            "storeType": "PKCS12",
            "storePasswordSecretId": "keystore.secret.id",
            "secretsProvider": ["SystemAndEnvSecretStore-1"],
            "mappings": [{
              "secretId": "jwtsession.symmetric.secret.id",
              "aliases": ["symmetric-key"]
            }]
          }
        },
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          }
        ],
        "session": {
          "type": "JwtSessionManager",
          "config": {
            "authenticatedEncryptionSecretId": "jwtsession.symmetric.secret.id",
            "encryptionMethod": "A256CBC-HS512",
            "secretsProvider": ["KeyStoreSecretStore-1"],
            "cookie": {
              "name": "IG",
              "domain": ".example.com"
            }
          }
        },
        "handler": {
          "type": "DispatchHandler",
          "config": {
            "bindings": [{
              "condition": "${find(request.uri.path, '/webapp/browsing') and (contains(request.uri.query, 'one') or empty(request.uri.query))}",
              "baseURI": "http://ig.example.com:8002",
              "handler": "ReverseProxyHandler"
            }, {
              "condition": "${find(request.uri.path, '/webapp/browsing') and contains(request.uri.query, 'two')}",
              "baseURI": "http://ig.example.com:8003",
              "handler": "ReverseProxyHandler"
            }, {
              "condition": "${find(request.uri.path, '/log-in-and-generate-session')}",
              "handler": {
                "type": "Chain",
                "config": {
                  "filters": [{
                    "type": "AssignmentFilter",
                    "config": {
                      "onRequest": [{
                        "target": "${session.authUsername}",
                        "value": "Sam Carter"
                      }]
                    }
                  }],
                  "handler": {
                    "type": "StaticResponseHandler",
                    "config": {
                      "status": 200,
                      "headers": {
                        "Content-Type": [ "text/html; charset=UTF-8" ]
                      },
                      "entity": "<html><body>Sam Carter logged IN. (JWT session generated)</body></html>"
                    }
                  }
                }
              }
            }]
          }
        },
        "capture": "all"
      }
      ```

      Source: [instance1-loadbalancer.json](../_attachments/config/routes/instance1-loadbalancer.json)

      Notice the following features of the route:

      * The route has no condition, so it matches all requests.

      * When the request matches `/log-in-and-generate-session`, the DispatchHandler creates a JWT session, whose `authUsername` attribute contains the name `Sam Carter`.

      * When the request matches `/webapp/browsing`, the DispatchHandler dispatches the request to instance 2 or instance 3, depending on the rest of the request path.

   3. Add the following configuration:

      * Linux

        `/path/to/config-instance1/config/admin.json`

      * Windows

        `%appdata%\path\to\config-instance1\config\admin.json`

      ```json
      {
        "connectors": [{
          "port": 8001
        }]
      }
      ```

   4. In the terminal where you will run the PingGateway instance, create an environment variable for the value of the keystore password:

      ```console
      $ export KEYSTORE_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by the SystemAndEnvSecretStore, and must be base64-encoded.

   5. Start PingGateway:

      * Linux

        `/path/to/ping-gateway-2026.6.0/bin/start.sh /path/to/config-instance1/`

      * Windows

        `C:\path\to\ping-gateway-2026.6.0\bin\start.bat %appdata%\path\to\config-instance1`

4. Set up and start the second instance of PingGateway:

   1. Create a configuration directory for the instance:

      ```console
      $ mkdir -p /path/to/config-instance2/config/routes
      ```

   2. Add the following route:

      * Linux

        `/path/to/config-instance2/config/routes/instance2-retrieve-session-username.json`

      * Windows

        `%appdata%\path\to\config-instance2\config\routes\instance2-retrieve-session-username.json`

      ```json
      {
        "name": "instance2-retrieve-session-username",
        "heap":  [{
          "name": "KeyStoreSecretStore-1",
          "type": "KeyStoreSecretStore",
          "config": {
            "file": "/path/to/secrets/jwtsessionkeystore.pkcs12",
            "storeType": "PKCS12",
            "storePasswordSecretId": "keystore.secret.id",
            "secretsProvider": ["SystemAndEnvSecretStore-1"],
            "mappings": [{
              "secretId": "jwtsession.symmetric.secret.id",
              "aliases": ["symmetric-key"]
            }]
          }
        },
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          }
        ],
        "session": {
          "type": "JwtSessionManager",
          "config": {
            "authenticatedEncryptionSecretId": "jwtsession.symmetric.secret.id",
            "encryptionMethod": "A256CBC-HS512",
            "secretsProvider": ["KeyStoreSecretStore-1"],
            "cookie": {
              "name": "IG",
              "domain": ".example.com"
            }
          }
        },
        "handler": {
          "type": "StaticResponseHandler",
          "config": {
            "status": 200,
            "headers": {
              "Content-Type": [ "text/html; charset=UTF-8" ]
            },
            "entity": [
              "<html>",
              "  <body>",
              "    ${session.authUsername!= null?'Hello, '.concat(session.authUsername).concat(' !'):'Session.authUsername is not defined'}! (instance2)",
              "  </body>",
              "</html>"
            ]
          }
        },
        "condition": "${find(request.uri.path, '/webapp/browsing')}",
        "capture": "all"
      }
      ```

      Source: [instance2-retrieve-session-username.json](../_attachments/config/routes/instance2-retrieve-session-username.json)

      Notice the following features of the route compared to the route for instance 1:

      * The route matches the condition `/webapp/browsing`. When a request matches `/webapp/browsing`, the DispatchHandler dispatches it to instance 2.

      * The StaticResponseHandler displays information from the session context.

   3. Add the following configuration:

      * Linux

        `/path/to/config-instance2/config/admin.json`

      * Windows

        `%appdata%\path\to\config-instance2\config\admin.json`

      ```json
      {
        "connectors": [{
          "port": 8002
        }]
      }
      ```

   4. In the terminal where you will run the PingGateway instance, create an environment variable for the value of the keystore password:

      ```console
      $ export KEYSTORE_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by the SystemAndEnvSecretStore, and must be base64-encoded.

   5. Start PingGateway:

      * Linux

        `/path/to/ping-gateway-2026.6.0/bin/start.sh /path/to/config-instance2/`

      * Windows

        `C:\path\to\ping-gateway-2026.6.0\bin\start.bat %appdata%\path\to\config-instance2`

5. Set up and start the third instance of PingGateway:

   1. Create a configuration directory:

      ```console
      $ mkdir -p /path/to/config-instance3/config/routes
      ```

   2. Add the following route:

      * Linux

        `/path/to/config-instance3/config/routes/instance3-retrieve-session-username.json`

      * Windows

        `%appdata%\path\to\config-instance3\config\routes\instance3-retrieve-session-username.json`

      ```json
      {
        "name": "instance3-retrieve-session-username",
        "heap":  [{
          "name": "KeyStoreSecretStore-1",
          "type": "KeyStoreSecretStore",
          "config": {
            "file": "/path/to/secrets/jwtsessionkeystore.pkcs12",
            "storeType": "PKCS12",
            "storePasswordSecretId": "keystore.secret.id",
            "secretsProvider": ["SystemAndEnvSecretStore-1"],
            "mappings": [{
              "secretId": "jwtsession.symmetric.secret.id",
              "aliases": ["symmetric-key"]
            }]
          }
        },
          {
            "name": "SystemAndEnvSecretStore-1",
            "type": "SystemAndEnvSecretStore"
          }
        ],
        "session": {
          "type": "JwtSessionManager",
          "config": {
            "authenticatedEncryptionSecretId": "jwtsession.symmetric.secret.id",
            "encryptionMethod": "A256CBC-HS512",
            "secretsProvider": ["KeyStoreSecretStore-1"],
            "cookie": {
              "name": "IG",
              "domain": ".example.com"
            }
          }
        },
        "handler": {
          "type": "StaticResponseHandler",
          "config": {
            "status": 200,
            "headers": {
              "Content-Type": [ "text/html; charset=UTF-8" ]
              },
              "entity": [
                "<html>",
                "  <body>",
                "    ${session.authUsername!= null?'Hello, '.concat(session.authUsername).concat(' !'):'Session.authUsername is not defined'}! (instance3)",
                "  </body>",
                "</html>"
              ]
            }
          },
        "condition": "${find(request.uri.path, '/webapp/browsing')}",
        "capture": "all"
      }
      ```

      Source: [instance3-retrieve-session-username.json](../_attachments/config/routes/instance3-retrieve-session-username.json)

      Notice that the route is the same as for instance 2, apart from the text in the entity of the StaticResponseHandler.

   3. Add the following configuration:

      * Linux

        `/path/to/config-instance3/config/admin.json`

      * Windows

        `%appdata%\path\to\config-instance3\config\admin.json`

      ```json
      {
        "connectors": [{
          "port": 8003
        }]
      }
      ```

   4. In the terminal where you will run the PingGateway instance, create an environment variable for the value of the keystore password:

      ```console
      $ export KEYSTORE_SECRET_ID='cGFzc3dvcmQ='
      ```

      The password is retrieved by the SystemAndEnvSecretStore, and must be base64-encoded.

   5. Start PingGateway:

      * Linux

        `/path/to/ping-gateway-2026.6.0/bin/start.sh /path/to/config-instance3/`

      * Windows

        `C:\path\to\ping-gateway-2026.6.0\bin\start.bat %appdata%\path\to\config-instance3`

6. Test the setup:

   1. Access instance 1, to generate a session:

      ```console
      $ curl -v http://ig.example.com:8001/log-in-and-generate-session
      ```

      Output

      ```
      GET /log-in-and-generate-session HTTP/1.1
      ...

      HTTP/1.1 200 OK
      Content-Length: 84
      Set-Cookie: IG=eyJ...HyI; Path=/; Domain=.example.com; HttpOnly
      ...
      Sam Carter logged IN. (JWT session generated)
      ```

   2. Using the JWT cookie returned in the previous step, access instance 2:

      ```console
      $ curl -v http://ig.example.com:8001/webapp/browsing\?one --header "cookie:IG=eyJ...HyI"
      ```

      Output

      ```
      GET /webapp/browsing?one HTTP/1.1
      ...
      cookie: IG=eyJ...HyI
      ...
      HTTP/1.1 200 OK
      ...
      Hello, Sam Carter !! (instance2)
      ```

      Note that instance 2 can access the session info.

   3. Using the JWT cookie again, access instance 3:

      ```console
      $ curl -v http://ig.example.com:8001/webapp/browsing\?two --header "cookie:IG=eyJ...HyI"
      ```

      Output

      ```
      GET /webapp/browsing?two HTTP/1.1
      ...
      cookie: IG=eyJ...HyI
      ...
      HTTP/1.1 200 OK
      ...
      Hello, Sam Carter !! (instance3)
      ```

      Note that instance 3 can access the session info.

---

---
title: FIPS 140–3 compliance with PingGateway
description: Configure PingGateway to achieve FIPS 140–3 compliance using the Bouncy Castle FIPS libraries, keystore, and security provider
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:fips
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/fips.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-06-15T20:05:56Z
keywords: ["Bouncy Castle FIPS", "Security", "Setup &amp; Configuration"]
section_ids:
  download-bouncy-castle-libraries: Download the Bouncy Castle libraries
  set-up-server-before-bouncy-castle: Add the libraries to PingGateway
  enable-bouncy-castle: Enable the Bouncy Castle FIPS provider
---

# FIPS 140–3 compliance with PingGateway

To achieve [FIPS 140–3](https://csrc.nist.gov/publications/detail/fips/140/3/final) compliance, configure the [Bouncy Castle FIPS libraries](https://www.bouncycastle.org/fips-java/) with PingGateway. This enables the use of the Bouncy Castle FIPS keystore and security provider in FIPS-approved mode.

Bouncy Castle FIPS is useful when dealing with government data, where meeting the FIPS 140–3 security requirements is necessary for regulatory compliance. Bouncy Castle FIPS doesn't require use of an HSM through a PKCS#11 interface.

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Bouncy Castle FIPS is less performant than other keystores. The destroyable keys can't be cached and must be read from the keystore with every use. |

To configure PingGateway to use Bouncy Castle FIPS:

1. [Download the Bouncy Castle libraries](#download-bouncy-castle-libraries).

2. [Add the libraries to PingGateway](#set-up-server-before-bouncy-castle).

3. [Enable the Bouncy Castle FIPS provider](#enable-bouncy-castle).

## Download the Bouncy Castle libraries

Before you begin, download the [Bouncy Castle FIPS libraries](https://www.bouncycastle.org/fips-java/):

| File                            | Description                                         |
| ------------------------------- | --------------------------------------------------- |
| `bc-fips-latestVersion.jar`     | Bouncy Castle FIPS security provider implementation |
| `bcpkix-fips-latestVersion.jar` | PKI support                                         |
| `bctls-fips-latestVersion.jar`  | TLS support                                         |
| `bcutil-fips-latestVersion.jar` | ASN.1 utility classes                               |

Ping Identity supports PingGateway and its use of the Bouncy Castle libraries. Ping Identity doesn't support third-party libraries themselves.

## Add the libraries to PingGateway

1. Create an `extra` folder to hold additional `.jar` files:

   * Linux

     `$HOME/.openig/extra`

   * Windows

     `%appdata%\OpenIG\extra`

2. Copy the Bouncy Castle libraries you downloaded into the PingGateway `extra` folder.

3. Create Bouncy Castle FIPS format keystores or truststores from any PingGateway keystores or truststores.

   The following example command creates a BCFKS keystore from a PKCS12 `gateway-keystore` file, where the `gateway-keystore.pin` file holds the keystore password:

   ```console
   $ keytool \
   -importkeystore \
   -srckeystore /path/to/secrets/gateway-keystore \
   -srcstoretype PKCS12 \
   -srcstorepass:file /path/to/secrets/gateway-keystore.pin \
   -destkeystore /path/to/secrets/gateway-keystore.bcfks \
   -deststoretype BCFKS \
   -deststorepass:file /path/to/secrets/gateway-keystore.pin \
   -providerpath $HOME/.openig/extra/bc-fips-2.0.0.jar \
   -providerclass org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider \
   -noprompt
   ```

   Make sure you do this for all your PingGateway keystore and truststore files.

## Enable the Bouncy Castle FIPS provider

Update the PingGateway Java settings to use Bouncy Castle FIPS support:

1. Copy the `$JAVA_HOME/conf/security/java.security` file into the PingGateway `$HOME/.openig` (Linux) or `%appdata%\OpenIG` (Windows) folder.

2. Update the `java.security` file you copied to use the Bouncy Castle FIPS provider:

   1. Replace the list of security providers with the following:

      ```properties
      security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
      # If entropy in the system is too limited to use the default
      # deterministic random bits generator, try with C:HYBRID;ENABLE{All};
      #security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider C:HYBRID;ENABLE{All};
      security.provider.2=org.bouncycastle.jsse.provider.BouncyCastleJsseProvider BCFIPS
      security.provider.3=SUN
      ```

   2. Update the default key manager factory algorithm:

      ```properties
      ssl.KeyManagerFactory.algorithm=PKIX
      ```

   3. Save your work.

3. Update the PingGateway [IG\_OPTS environment variable](envvar-sysprop.html) to use the Bouncy Castle FIPS provider:

   * Linux

   * Windows

   ```none
   export IG_OPTS="${IG_OPTS} -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties=$HOME/.openig/java.security"
   ```

   ```none
   set "IG_OPTS=%IG_OPTS% -Dorg.bouncycastle.fips.approved_only=true -Djava.security.properties=%appdata%\OpenIG\java.security"
   ```

4. Start PingGateway.

You have successfully configured PingGateway to use Bouncy Castle FIPS.

---

---
title: Installing PingGateway
description: Introduction to installing and removing PingGateway software, with links to release notes and evaluation guides
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Install", "Configuration"]
page_aliases: ["index.adoc"]
---

# Installing PingGateway

These pages describe how to install and remove PingGateway software. Learn how to install PingGateway for evaluation in [Getting started with PingGateway](../getting-started/preface.html).

Read the [Release notes](https://docs.pingidentity.com/pinggateway/release-notes/preface.html) before you install PingGateway.

Product names changed when ForgeRock became part of Ping Identity. PingGateway was formerly known as ForgeRock Identity Gateway, for example. Learn more about the name changes from [New names for ForgeRock products](https://support.pingidentity.com/s/article/new-names-for-forgerock-products).

---

---
title: Preparing PingGateway for load balancing and failover
description: Configure PingGateway for load balancing and failover by managing state, JWT sessions, session stickiness, and SAML in multi-instance deployments
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:load-balancing
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/load-balancing.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-20T12:00:00Z
keywords: ["Configuration", "Load Balancer"]
section_ids:
  manage_state_information: Manage state information
  prepare_jwt_based_sessions: Prepare JWT-based sessions
  saml_in_deployments_with_multiple_instances_of_pinggateway: SAML in deployments with multiple instances of PingGateway
---

# Preparing PingGateway for load balancing and failover

For high scale or highly available deployments, consider using a pool of PingGateway servers with nearly identical configurations. Load balance requests across the pool to handle more load. Route around any servers that become unavailable.

## Manage state information

Before spreading requests across multiple servers, decide how to manage state information. PingGateway manages state information in the following ways:

* Stores state information in a context

  By using filters that can store information in the context. Most filters depend on information in the request, response, or context, some of which is first stored by PingGateway. For a summary of filters that can populate a context, refer to [Summary of contexts](../reference/Contexts.html#contexts-summary).

  By using a handler such as the [ScriptableHandler](../reference/ScriptableHandler.html) that can store state information in the context. Most handlers depend on information in the context, some of which is first stored by PingGateway.

* Retrieves state information to local memory

  By using filters and handlers that depend on the configuration of the local file system, such as the following filters:

  * [FileAttributesFilter](../reference/FileAttributesFilter.html)

  * [ScriptableFilter](../reference/ScriptableFilter.html)

  * [ScriptableHandler](../reference/ScriptableHandler.html)

  * [SqlAttributesFilter](../reference/SqlAttributesFilter.html)

  When a server becomes unavailable, state information held in local memory is lost. To prevent data loss when a server becomes unavailable, set up failover. Server failover should be transparent to client applications.

## Prepare JWT-based sessions

Find example configurations in [Encrypting and sharing PingGateway JWT sessions](jwtsession-using.html).

* JWT-based sessions

  Use a [JwtSessionManager](../reference/JwtSessionManager.html). PingGateway stores session content in a JWT cookie on the user-agent.

  So that any server can read or update a JWT cookie from any other server in the same cookie domain, encrypt JWT sessions and share keys and secret across all PingGateway configurations.

  [Encrypt JWT sessions](jwtsession-using.html#jwtsession-encrypt). The maximum size of the JWT session cookie is 4 KBytes, as defined by the browser. If the cookie exceeds this size, PingGateway automatically splits it into multiple cookies.

* Session stickiness

  Session stickiness helps to ensure that a client request goes to the server holding the original session data.

  If data attached to a context must be stored on the server-side, configure session stickiness so that the load balancer sends all requests from the same client session to the same server.

  For an example configuration, refer to [Share JWT sessions between multiple instances of PingGateway](jwtsession-using.html#jwtsession-sharesecrets).

## SAML in deployments with multiple instances of PingGateway

PingGateway uses AM federation libraries to implement SAML. When PingGateway acts as a SAML service provider, some internal state information is maintained in the fedlet instead of the session cookie. In deployments that use multiple instances of PingGateway as a SAML service provider, set up sticky sessions so that requests go to the server that started the SAML interaction.

Learn more in the AM documentation on [Session state considerations](https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-configuration.html#saml2-and-session-state).

---

---
title: Preparing to install PingGateway
description: Steps to complete before installing PingGateway, including release notes requirements, network preparation, and identity service setup
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:prepare
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/prepare.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-22T12:00:00Z
keywords: ["Install", "Configuration", "Account", "Authentication", "Agents", "Journeys", "Nodes &amp; Trees", "Users"]
section_ids:
  run-from-service-account: Create a PingGateway service account
  configure-network: Preparing the network for PingGateway
  setup-idc: Set up PingOne Advanced Identity Cloud
  authenticate-agent-idc: About authentication to PingOne Advanced Identity Cloud
  register-agent-idc: Register a PingGateway agent in PingOne Advanced Identity Cloud
  idc-use-the-secret-store-for-the-password: Use an ESV for the password
  optional_settings: Optional settings
  setup-user-idc: Set up a demo user in PingOne Advanced Identity Cloud
  idc-recommendations: Recommendations
  setup-am: Set up AM
  authenticate-agent-am: About authentication to AM
  register-agent-am: Register PingGateway with AM
  setup-user-am: Set up a demo user in AM
  am-session-cookie: Find the AM session cookie name
---

# Preparing to install PingGateway

|   |                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you install PingGateway, make sure your installation meets the requirements in the [release notes](https://docs.pingidentity.com/pinggateway/release-notes). |

## Create a PingGateway service account

To limit the impact of a security breach, install and run PingGateway from a dedicated service account. This is optional when evaluating PingGateway, but essential in production installations.

A hacker is constrained by the rights granted to the user account where PingGateway runs; therefore, never run PingGateway as root user.

1. In a terminal window, use a command similar to the following to create a service account:

   * Linux

   * Windows

   ```console
   $ sudo /usr/sbin/useradd \
   --create-home \
   --comment "Account for running PingGateway" \
   --shell /bin/bash PingGateway
   ```

   ```none
   net user username password /add /comment:"Account for running PingGateway"
   ```

2. Apply the principle of least privilege to the account, for example:

   * Read/write permissions on the installation directory, `/path/to/ping-gateway-2026.6.0`.

   * Execute permissions on the scripts in the installation `bin` directory, `/path/to/ping-gateway-2026.6.0/bin`.

## Preparing the network for PingGateway

Configure the network to include hosts for PingGateway, AM, and the sample application. Learn more about hosts files in [Hosts (file)](https://en.wikipedia.org/wiki/Hosts_\(file\)).

Add the following entry to your hosts file:

```none
127.0.0.1  localhost ig.example.com app.example.com am.example.com
```

The hosts file path depends on the platform:

* Linux

  `/etc/hosts`

* Windows

  `%SystemRoot%\system32\drivers\etc\hosts`

## Set up PingOne Advanced Identity Cloud

This documentation contains procedures for setting up items in PingOne Advanced Identity Cloud that you can use with PingGateway. For more information about setting up PingOne Advanced Identity Cloud, refer to the [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/home.html).

### About authentication to PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud provides an authentication journey to validate the agent credentials with an Agent Data Store Decision node.

When you register PingGateway with PingOne Advanced Identity Cloud, PingOne Advanced Identity Cloud uses the journey to authenticate PingGateway.

### Register a PingGateway agent in PingOne Advanced Identity Cloud

This procedure registers an agent profile for PingGateway.

1. Sign on to the Advanced Identity Cloud admin UI as an administrator.

2. Click [icon: verified_user, set=material, size=inline] Gateways & Agents > [icon: plus, set=fa]New Gateway/Agent > Identity Gateway > Next and use the hints in the following table to create the agent profile:

   | Field                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                    |
   | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
   | ID                            | Set the unique agent profile name PingGateway uses to connect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `ig_agent`                                                                                                 |
   | Password                      | Store the password PingGateway uses to connect in the agent profile.Record the password to use when configuring PingGateway.                                                                                                                                                                                                                                                                                                                                                                                                                                   | A strong password.The examples in the documentation use `password` and its base64-encoding `cGFzc3dvcmQ=`. |
   | Use Secret Store for password | Optionally store the password in a secret and reference the secret by its label.After you create an agent profile with this option enabled, make sure you follow the steps in [Use an ESV for the password](#idc-use-the-secret-store-for-the-password).                                                                                                                                                                                                                                                                                                       | Click to enable                                                                                            |
   | Secret Label Identifier       | This field appears when you select Use Secret Store for password.This value represents the `identifier` part of the secret label for the agent. PingOne Advanced Identity Cloud uses the identifier to generate a secret label in the following format: `am.application.agents.identifier.secret`. Learn more in [Secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#secret-labels).After setting this, make sure you follow the steps in [Use an ESV for the password](#idc-use-the-secret-store-for-the-password). | `ig`                                                                                                       |

   |   |                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------- |
   |   | Use secure passwords in a production environment. Consider using a password manager to generate secure passwords. |

3. Click Save Profile > Done to display the new agent profile.

4. (Optional) Add the list of Redirect URLs used in PingGateway routes and click Save to update the profile.

5. Switch to the AM admin UI, go to Applications > Agents > Identity Gateway > *agent ID*, and update the Login URL Template for CDSSO.

   Advanced Identity Cloud doesn't set a default. Configure this property to ensure Advanced Identity Cloud notifies PingGateway on authentication failure. PingGateway uses the notification to remove stale session data.

   * When using the default Advanced Identity Cloud login pages, add the following template all one line, replacing \<tenantHostname> to match your deployment:

     ```none
     https://<tenantHostname>/am/login?
     <#if service??>&service=${service}</#if>
     &goto=${goto}
     &gotoOnFail=${gotoOnFail}
     <#if acrValues??>&acr_values=${acrValues}</#if>
     <#if realm??>&realm=${realm}</#if>
     <#if module??>&module=${module}</#if>
     <#if locale??>&locale=${locale}</#if>
     ```

   * When using a custom login page outside Advanced Identity Cloud, use a template matching the login page requirements.

     Make sure to include a `${gotoOnFail}` parameter in the template. Update the custom login page to use the new parameter, verify its value is valid to protect against open redirect attacks, and redirect the user-agent when authentication fails.

#### Use an ESV for the password

When you select Use Secret Store for password and set a secret label for the agent profile, PingOne Advanced Identity Cloud creates the secret label. You must create an ESV secret for the password and map the ESV to the label:

1. Use the Advanced Identity Cloud admin UI to define an ESV secret, such as `esv-ig-agent`, holding the password for PingGateway to connect.

   The examples in the documentation use `password`.

   Learn how in the PingOne Advanced Identity Cloud documentation on [creating ESV secrets](https://docs.pingidentity.com/pingoneaic/tenants/esvs-manage-ui.html#create_secrets). In production deployments, [restrict access to the password](https://docs.pingidentity.com/pingoneaic/tenants/esvs.html#control-access-to-secrets) from configuration placeholder and script contexts.

2. Use the AM admin UI to map the ESV to the label created when you set the Secret Label Identifier:

   1. Click [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management > Secret Stores > ESV > Mappings > [icon: plus, set=fa]Add mappings.

   2. In the Add Mapping modal, select the label, such as `am.application.agents.ig.secret`, in the Secret Label list.

   3. In the aliases field, enter the ESV secret, such as `esv-ig-agent`, and click Add:

      ![agent password mapping](../aic/_images/agent-password-mapping.png)

   4. Click Create to add the mapping.

   Learn more in the Advanced Identity Cloud documentation on [mapping ESV secrets to secret labels](https://docs.pingidentity.com/pingoneaic/tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels).

Note the following points:

* If you update or delete the Secret Label Identifier, AM updates or deletes the corresponding mapping for the previous identifier unless another agent shares the mapping.

* When you rotate a secret, update the corresponding mapping.

#### Optional settings

In the AM admin UI, consider the following additional optional settings for the agent profile under Applications > Agents > Identity Gateway > *agent ID*:

1. To apply a different introspection scope, click Token Introspection and select a scope from the list.

2. Click Save to update the profile.

### Set up a demo user in PingOne Advanced Identity Cloud

This procedure sets up a demo user in the alpha realm.

1. Log in to the Advanced Identity Cloud admin UI as an administrator.

2. Go to [icon: group, set=material, size=inline] Identities > Manage > [icon: settings_system_daydream, set=material, size=inline] Alpha realm - Users, and add a user with the following values:

   * Username: `demo`

   * First name: `demo`

   * Last name: `user`

   * Email Address: `demo@example.com`

   * Password: `Ch4ng3!t`

### Recommendations

Use PingGateway with PingOne Advanced Identity Cloud as you would with any other service.

* During updates, individual PingOne Advanced Identity Cloud tenant servers go offline temporarily. PingGateway can receive HTTP 502 Bad Gateway responses for some requests during the update.

  In your [ClientHandler](../reference/ClientHandler.html) and [ReverseProxyHandler](../reference/ReverseProxyHandler.html) configurations, configure PingGateway to retry operations when this occurs:

  ```json
  "retries": {
      "enabled": true,
      "condition": "${response.status.code == 502}"
  }
  ```

* Update PingGateway to use the latest version you can to benefit from fixes and improvements.

## Set up AM

This section helps you prepare to use PingGateway with AM.

### About authentication to AM

Unless you upgrade from an earlier version using the file-based configuration, AM 8 and later provide an [authentication journey](https://docs.pingidentity.com/pingam/8.1/am-authentication/auth-nodes-and-journeys.html) called `Agent`. The `Agent` tree validates the agent credentials with an [Agent Data Store Decision](https://docs.pingidentity.com/auth-node-ref/8.1/auth-node-agent-data-store-decision.html) node. All PingGateway, Java agent, and Web agent profiles use the `Agent` tree. Don't change its configuration.

For AM 7.3 and later, when AM is [installed with a default configuration](https://docs.pingidentity.com/pingam/8.1/evaluation/preface.html), PingGateway authenticates to AM with a tree. Otherwise, PingGateway authenticates to AM with an AM authentication module. AM 7 deprecated authentication chains and modules and AM 8 removed support for them.

### Register PingGateway with AM

Follow these steps to register an PingAM agent that acts on behalf of PingGateway.

1. In the AM admin UI, select the top-level realm, and then select Applications > Agents > Identity Gateway.

2. Add an agent with the following configuration, leaving other options blank or with the default value:

   * For SSO

   * For CDSSO

   - Agent ID : `ig_agent`

   - Password : `password`

   * Agent ID : `ig_agent`

   * Password : `password`

   * Redirect URL for CDSSO : `https://ig.ext.com:8443/home/cdsso/redirect`

   * Login URL Template for CDSSO:

     For AM 8 and earlier, configure this property to direct login to a custom URL instead of the default AM login page. Leave this property blank to use the default AM login page.

     For AM 8.1 and later, AM doesn't set a default. Configure this property to ensure AM notifies PingGateway on authentication failure. PingGateway uses the notification to remove stale session data.

     * When using the default AM login pages or a custom login page in AM, add the following template all one line, replacing \<am-base-url> to match your deployment:

       ```none
       https://<am-base-url>/login?
       <#if service??>&service=${service}</#if>
       &goto=${goto}
       &gotoOnFail=${gotoOnFail}
       <#if acrValues??>&acr_values=${acrValues}</#if>
       <#if realm??>&realm=${realm}</#if>
       <#if module??>&module=${module}</#if>
       <#if locale??>&locale=${locale}</#if>
       ```

     * When using a custom login page outside AM, use a template matching the login page requirements.

       Make sure to include a `${gotoOnFail}` parameter in the template. Update the custom login page to use the new parameter, verify its value is valid to protect against open redirect attacks, and redirect the user-agent when authentication fails.

3. (Optional - From AM 7.5) Use AM's secret service to manage the agent profile password.

   If AM finds a matching secret in a secret store, it uses that secret instead of a password in the agent profile.

   1. In the agent profile page, set a label for the agent password in Secret Label Identifier.

      AM uses the identifier to generate a secret label for the agent.

      The secret label has the format `am.application.agents.identifier.secret`, where identifier is the Secret Label Identifier.

      The Secret Label Identifier can contain only characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

   2. Select [icon: eye-slash, set=fa]Secret Stores and configure a secret store.

   3. Map the label to the secret. Learn more from AM's [mapping](https://docs.pingidentity.com/pingam/8.1/security/secret-mapping.html).

   Note the following points for using AM's secret service:

   * Set a Secret Label Identifier that clearly identifies the agent.

   * If you update or delete the Secret Label Identifier, AM updates or deletes the corresponding mapping for the previous identifier provided no other agent shares the mapping.

   * When you rotate a secret, update the corresponding mapping.

### Set up a demo user in AM

AM is provided with a demo user in the top-level realm, with the following credentials:

* ID/username: `demo`

* Last name: `user`

* Password: `Ch4ng31t`

* Email address: `demo@example.com`

* Employee number: `123`

Learn more about managing identities in AM's [Identity stores](https://docs.pingidentity.com/pingam/8.1/setup/setting-up-identity-stores.html) documentation.

### Find the AM session cookie name

In routes that use an AmService, PingGateway retrieves AM's SSO cookie name from the `ssoTokenHeader` property or from AM's `/serverinfo/*` endpoint.

In other circumstances where you need to find the SSO cookie name, access `http://am-base-url/serverinfo/*`. For example, access the AM endpoint with `curl`:

```console
$ curl http://am.example.com:8088/openam/json/serverinfo/*
```

---

---
title: Securing connections with PingGateway
description: Configure HTTPS/TLS connections for PingGateway, including client-side HTTPS, server-side TLS, and mutual TLS setup
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:securing-connections
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/securing-connections.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Configuration", "Security", "Certificates", "Java"]
section_ids:
  client-side-https: Configure PingGateway for TLS (client-side)
  server-side-tls: Configure PingGateway for TLS (server-side)
  server-side-tls-keyManager: Serve one certificate for TLS connections to all server names
  server-side-tls-sni: Use Server Name Indication (SNI) to serve different certificates for TLS connections to different server names
  server-side-mtls: Configure PingGateway for mutual TLS (server-side)
---

# Securing connections with PingGateway

PingGateway is often deployed to replay credentials or other security information. In a real world deployment, this information must be communicated over a secure connection using HTTPS, meaning HTTP over encrypted Transport Layer Security (TLS). Never send real credentials, bearer tokens, or other security information unprotected over HTTP.

Learn about how to use well-known CA-signed certificates from the documentation for the Java Virtual Machine (JVM).

After installing certificates for client-server trust, consider which cipher suites to use. PingGateway inherits the list of cipher suites from the underlying Java environment.

PingGateway uses the JSSE to secure connections. You can set security and system properties to configure the JSSE. For a list of properties to customize the JSSE in Oracle Java, refer to the *Customization* section of the [JSSE Reference guide](https://docs.oracle.com/en/java/javase/25/security/java-secure-socket-extension-jsse-reference-guide.html#GUID-A41282C3-19A3-400A-A40F-86F4DA22ABA9).

## Configure PingGateway for TLS (client-side)

When PingGateway sends requests over HTTP to a proxied application, or requests services from a third-party application, PingGateway is acting as a client of the application, and the application is acting as a server. PingGateway is *client-side*.

When PingGateway sends requests securely over HTTPS, PingGateway must be able to trust the server. By default, PingGateway uses the Java environment truststore to trust server certificates. The Java environment truststore includes public key signing certificates from many well-known Certificate Authorities (CAs).

When servers present certificates signed by trusted CAs, then PingGateway can send requests over HTTPS to those servers, without any configuration to set up the HTTPS client connection. When server certificates are self-signed or signed by a CA whose certificate is not automatically trusted, the following objects can be required to configure the connection:

* [KeyStoreSecretStore](../reference/KeyStoreSecretStore.html), to manage a secret store for cryptographic keys and certificates, based on a standard Java keystore.

* [SecretsTrustManager](../reference/SecretsTrustManager.html), to manage trust material that verifies the credentials presented by a peer.

* (Optional) [SecretsKeyManager](../reference/SecretsKeyManager.html), to manage keys that authenticate a TLS connection to a peer.

* ClientHandler and ReverseProxyHandler reference to [ClientTlsOptions](../reference/ClientTlsOptions.html), for connecting to TLS-protected endpoints.

The following procedure describes how to set up PingGateway for HTTPS (client-side), when server certificates are self-signed or signed by untrusted CAs.

Set up PingGateway for HTTPS (client-side) for untrusted servers

1. Locate or set up the following directories:

   * Directory containing the `PingGateway-sample-application-2026.6.0.jar` file: \<sampleapp\_install\_dir>

   * Directory to store the sample application certificate and PingGateway keystore: `/path/to/secrets`

2. Get the public certificate from the sample application in one of the following ways:

   * Download the [sampleapp.cert.pem](../_attachments/tls/sampleapp.cert.pem) file and save it in a `tls` folder.

   * Extract it from the PingGateway-sample-application-2026.6.0.jar file:

     ```console
     $ cd /path/to/secrets
     ```

     ```console
     $ jar --verbose --extract \
     --file <sampleapp_install_dir>/PingGateway-sample-application-2026.6.0.jar tls/sampleapp.cert.pem
     ```

     Output

     ```
     inflated: tls/sampleapp.cert.pem
     ```

3. Import the certificate into the PingGateway keystore, and answer `yes` to trust the certificate:

   ```console
   $ keytool -importcert \
   -alias ig-sampleapp \
   -file tls/sampleapp.cert.pem \
   -keystore reverseproxy-truststore.p12 \
   -storetype pkcs12 \
   -storepass password
   ```

   Output

   ```none
   ...
   Trust this certificate? [no]: yes

   Certificate was added to keystore
   ```

   |   |                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because keytool converts all characters in its key aliases to lowercase, use only lowercase in alias definitions of a keystore. |

4. List the keys in the PingGateway keystore to make sure that a key with the alias `ig-sampleapp` is present:

   ```console
   $ keytool -list \
   -v \
   -keystore /path/to/secrets/reverseproxy-truststore.p12 \
   -storetype pkcs12 \
   -storepass password
   ```

   Output

   ```
   Keystore type: PKCS12
   Keystore provider: SUN
   Your keystore contains 1 entry
   Alias name: ig-sampleapp
   ...
   ```

5. Add the following route to PingGateway to serve the sample application .css and other static resources:

   * Linux

     `$HOME/.openig/config/routes/00-static-resources.json`

   * Windows

     `%appdata%\OpenIG\config\routes\00-static-resources.json`

   ```json
   {
     "name" : "00-static-resources",
     "baseURI" : "https://app.example.com:8444",
     "condition": "${find(request.uri.path,'^/css') or matchesWithRegex(request.uri.path, '^/.*\\\\.ico$') or matchesWithRegex(request.uri.path, '^/.*\\\\.gif$')}",
     "handler": "ReverseProxyHandler"
   }
   ```

   Source: [00-static-resources.json](../_attachments/config/routes/00-static-resources.json)

6. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/client-side-https.json`

   * Windows

     `%appdata%\OpenIG\config\routes\client-side-https.json`

   ```json
   {
     "name": "client-side-https",
     "condition": "${find(request.uri.path, '/home/client-side-https')}",
     "baseURI": "https://app.example.com:8444",
     "heap": [
       {
         "name": "Base64EncodedSecretStore-1",
         "type": "Base64EncodedSecretStore",
         "config": {
           "secrets": {
             "keystore.secret.id": "cGFzc3dvcmQ="
           }
         }
       },
       {
         "name": "KeyStoreSecretStore-1",
         "type": "KeyStoreSecretStore",
         "config": {
           "file": "/path/to/secrets/reverseproxy-truststore.p12",
           "storeType": "PKCS12",
           "storePasswordSecretId": "keystore.secret.id",
           "secretsProvider": "Base64EncodedSecretStore-1",
           "mappings": [
             {
               "secretId": "trust.manager.secret.id",
               "aliases": [ "ig-sampleapp" ]
             }
           ]
         }
       },
       {
         "name": "SecretsTrustManager-1",
         "type": "SecretsTrustManager",
         "config": {
           "verificationSecretId": "trust.manager.secret.id",
           "secretsProvider":"KeyStoreSecretStore-1"
         }
       },
       {
         "name": "ReverseProxyHandler-1",
         "type": "ReverseProxyHandler",
         "config": {
           "tls": {
             "type": "ClientTlsOptions",
             "config": {
               "trustManager": "SecretsTrustManager-1",
               "hostnameVerifier": "ALLOW_ALL"
             }
           }
         },
         "capture": "all"
       }
     ],
     "handler": "ReverseProxyHandler-1"
   }
   ```

   Source: [client-side-https.json](../_attachments/config/routes/client-side-https.json)

   Notice the following features of the route:

   * The route matches requests to `/home/client-side-https`.

   * The `baseURI` changes the request URI to point to the HTTPS port for the sample application.

   * The Base64EncodedSecretStore provides the keystore password.

   * The SecretsTrustManager points to the secret bound to the sample application certificate, coming from the KeyStoreSecretStore.

   * The KeyStoreSecretStore contains the sample application certificate to validate the TLS connection. The password to access the keystore is provided by the SystemAndEnvSecretStore.

   * The ReverseProxyHandler uses the SecretsTrustManager for the connection to TLS-protected endpoints. All hostnames are allowed.

7. Test the setup:

   1. Start the sample application.

      ```console
      $ java -jar <sampleapp_install_dir>/PingGateway-sample-application-2026.6.0.jar
      ```

   2. Go to <http://ig.example.com:8080/home/client-side-https>.

      The request is proxied transparently to the sample application, on the TLS port `8444`.

   3. Check the route log for a line like this:

      ```none
      GET https://app.example.com:8444/home/client-side-https
      ```

## Configure PingGateway for TLS (server-side)

When PingGateway is *server-side*, applications send requests to PingGateway or request services from PingGateway. PingGateway is acting as a server of the application, and the application is acting as a client.

To run PingGateway as a server over TLS:

* In the `admin.json` heap, add a [SecretsKeyManager](../reference/SecretsKeyManager.html) to authenticate PingGateway to the client. Key material is a private key and its certificate for PingGateway.

* In `admin.json`, update the `connectors` list to include a connector for the HTTPS port. The connector `tls` property must refer to a [ServerTlsOptions](../reference/ServerTlsOptions.html).

* The ServerTlsOptions must configure `keyManager` to refer to the SecretsKeyManager.

The following example connector includes a ServerTlsOptions that refers to a SecretsKeyManager in the heap:

```
"connectors": [
  {
    "port": 8443,
    "tls": {
      "type": "ServerTlsOptions",
      "config": {
        "keyManager": "SecretsKeyManager-1"
      }
    }
  }
]
```

Learn more from [About keys and certificates](../security-guide/keys.html#using-certs-in-examples).

### Serve one certificate for TLS connections to all server names

This example uses PEM files and a PKCS#12 keystore for self-signed certificates, but you can adapt it to use official (non self-signed) keys and certificates.

Before you start, install PingGateway, as described in the [Installing PingGateway](preface.html).

1. Locate a directory for the secrets, for example, `/path/to/secrets`.

2. Create self-signed keys in one of the following ways. If you have your own keys, use them and skip this step.

   > **Collapse: Use your own keys**
   >
   > If you have your own keys, use them and skip this step.

   > **Collapse: Set up a self-signed certificate in a (PKCS#12) keystore**
   >
   > 1. Create the keystore:
   >
   >    ```console
   >    $ keytool \
   >    -genkey \
   >    -alias https-connector-key \
   >    -keyalg RSA \
   >    -keystore /path/to/secrets/keystore.pkcs12 \
   >    -storepass password \
   >    -keypass password \
   >    -dname "CN=ig.example.com,O=Example Corp,C=FR"
   >    ```
   >
   >    |   |                                                                                                                                 |
   >    | - | ------------------------------------------------------------------------------------------------------------------------------- |
   >    |   | Because keytool converts all characters in its key aliases to lowercase, use only lowercase in alias definitions of a keystore. |
   >
   > 2. In the secrets directory, add a file called `keystore.pass`, containing the keystore password `password`:
   >
   >    ```console
   >    $ cd /path/to/secrets
   >    $ echo -n 'password' > keystore.pass
   >    ```
   >
   >    Make sure the password file contains only the password, with no trailing spaces or carriage returns.

   > **Collapse: Set up self-signed certificate stored in a PEM file**
   >
   > 1. Locate a directory for secrets and go to it:
   >
   >    ```console
   >    $ cd /path/to/secrets
   >    ```
   >
   > 2. Create the following secret key and certificate pair as PEM files:
   >
   >    ```console
   >    $ openssl req \
   >    -newkey rsa:2048 \
   >    -new \
   >    -nodes \
   >    -x509 \
   >    -days 3650 \
   >    -subj "/CN=ig.example.com/OU=example/O=com/L=fr/ST=fr/C=fr" \
   >    -keyout ig.example.com-key.pem \
   >    -out ig.example.com-certificate.pem
   >    ```
   >
   >    Two PEM files are created, one for the secret key, and another for the associated certificate.
   >
   > 3. Map the key and certificate to the same secret ID in PingGateway:
   >
   >    ```console
   >    $ cat ig.example.com-key.pem ig.example.com-certificate.pem > key.manager.secret.id.pem
   >    ```

3. Set up TLS on PingGateway in one of the following ways:

   > **Collapse: Keys stored in a (PKCS#12) keystore**
   >
   > Add the following file to PingGateway, replacing `/path/to/secrets` with your path:
   >
   > * Linux
   >
   >   `$HOME/.openig/config/admin.json`
   >
   > * Windows
   >
   >   `%appdata%\OpenIG\config\admin.json`
   >
   > ```json
   > {
   >   "connectors": [
   >     {
   >       "port": 8080
   >     },
   >     {
   >       "port": 8443,
   >       "tls": "ServerTlsOptions-1"
   >     }
   >   ],
   >   "heap": [
   >     {
   >       "name": "ServerTlsOptions-1",
   >       "type": "ServerTlsOptions",
   >       "config": {
   >         "keyManager": {
   >           "type": "SecretsKeyManager",
   >           "config": {
   >             "signingSecretId": "key.manager.secret.id",
   >             "secretsProvider": "ServerIdentityStore"
   >           }
   >         }
   >       }
   >     },
   >     {
   >       "type": "FileSystemSecretStore",
   >       "name": "SecretsPasswords",
   >       "config": {
   >         "directory": "/path/to/secrets",
   >         "format": "PLAIN"
   >       }
   >     },
   >     {
   >       "name": "ServerIdentityStore",
   >       "type": "KeyStoreSecretStore",
   >       "config": {
   >         "file": "/path/to/secrets/IG-keystore",
   >         "storePasswordSecretId": "keystore.pass",
   >         "secretsProvider": "SecretsPasswords",
   >         "mappings": [
   >           {
   >             "secretId": "key.manager.secret.id",
   >             "aliases": ["https-connector-key"]
   >           }
   >         ]
   >       }
   >     }
   >   ]
   > }
   > ```
   >
   > Source: [admin-https.json](../_attachments/config/admin-https.json)
   >
   > Notice the following features of the file:
   >
   > * PingGateway listens for:
   >
   >   * Administrative HTTP requests on port `8085` (default).
   >
   >   * HTTP requests on port `8080`.
   >
   >   * HTTPS requests on port `8443`.
   >
   > * PingGateway's private keys for TLS are managed by the SecretsKeyManager, whose ServerIdentityStore references a KeyStoreSecretStore.
   >
   > * The KeyStoreSecretStore maps the keystore alias to the secret ID for retrieving the server keys (private key + certificate).
   >
   > * The password of the KeyStoreSecretStore is provided by the FileSystemSecretStore.

   > **Collapse: Keys stored in PEM file**
   >
   > Add the following file to PingGateway, replacing `/path/to/secrets` with your path:
   >
   > * Linux
   >
   >   `$HOME/.openig/config/admin.json`
   >
   > * Windows
   >
   >   `%appdata%\OpenIG\config\admin.json`
   >
   > ```json
   > {
   >   "connectors": [
   >     {
   >       "port": 8080
   >     },
   >     {
   >       "port": 8443,
   >       "tls": "ServerTlsOptions-1"
   >     }
   >   ],
   >   "heap": [
   >     {
   >       "name": "ServerTlsOptions-1",
   >       "type": "ServerTlsOptions",
   >       "config": {
   >         "keyManager": {
   >           "type": "SecretsKeyManager",
   >           "config": {
   >             "signingSecretId": "key.manager.secret.id",
   >             "secretsProvider": "ServerIdentityStore"
   >           }
   >         }
   >       }
   >     },
   >     {
   >       "name": "ServerIdentityStore",
   >       "type": "FileSystemSecretStore",
   >       "config": {
   >         "format": "PLAIN",
   >         "directory": "/path/to/secrets",
   >         "suffix": ".pem",
   >         "mappings": [{
   >           "secretId": "key.manager.secret.id",
   >           "format": {
   >             "type": "PemPropertyFormat"
   >           }
   >         }]
   >       }
   >     }
   >   ]
   > }
   > ```
   >
   > Source: [admin-https-pem.json](../_attachments/config/admin-https-pem.json)
   >
   > Notice how this file differs to that for the keystore-based approach:
   >
   > * The ServerIdentityStore is a FileSystemSecretStore.
   >
   > * The FileSystemSecretStore reads the keys that are stored as files in the PEM standard format.

4. Start PingGateway:

   * Linux

     `/path/to/ping-gateway-2026.6.0/bin/start.sh`

   * Windows

     `C:\path\to\ping-gateway-2026.6.0\bin\start.bat`

   By default, PingGateway configuration files are located under `$HOME/.openig` on Linux, `%appdata%\OpenIG` on Windows. Learn how to use a different location, in [Configuration location](../configure/configure.html#configuration-location).

5. Test the connection by going to the PingGateway welcome page, <https://ig.example.com:8443/>.

   The browser won't recognize the certificate, but you can safely access the page.

### Use Server Name Indication (SNI) to serve different certificates for TLS connections to different server names

This example uses PEM files for self-signed certificates, but you can adapt it to use official (non self-signed) keys and certificates.

Before you start, install PingGateway, as described in the [Installing PingGateway](preface.html).

1. Locate a directory for secrets and go to it.

   ```console
   $ cd /path/to/secrets
   ```

2. Create the following secret key and certificate pair as PEM files:

   1. For `ig.example.com`:

      1. Create a key and certificate:

         ```console
         $ openssl req \
         -newkey rsa:2048 \
         -new \
         -nodes \
         -x509 \
         -days 3650 \
         -subj "/CN=ig.example.com/OU=example/O=com/L=fr/ST=fr/C=fr" \
         -keyout ig.example.com-key.pem \
         -out ig.example.com-certificate.pem
         ```

         Two PEM files are created, one for the secret key, and another for the associated certificate.

      2. Map the key and certificate to the same secret ID in PingGateway:

         ```console
         $ cat ig.example.com-key.pem ig.example.com-certificate.pem > key.manager.secret.id.pem
         ```

   2. For servers grouped by a wildcard:

      1. Create a key and certificate:

         ```console
         $ openssl req \
         -newkey rsa:2048 \
         -new \
         -nodes \
         -x509 \
         -days 3650 \
         -subj "/CN=*.example.com/OU=example/O=com/L=fr/ST=fr/C=fr" \
         -keyout wildcard.example.com-key.pem \
         -out wildcard.example.com-certificate.pem
         ```

      2. Map the key and certificate to the same secret ID in PingGateway:

         ```console
         $ cat wildcard.example.com-key.pem wildcard.example.com-certificate.pem > wildcard.secret.id.pem
         ```

   3. For other, unmapped servers

      1. Create a key and certificate:

         ```console
         $ openssl req \
         -newkey rsa:2048 \
         -new \
         -nodes \
         -x509 \
         -days 3650 \
         -subj "/CN=un.mapped.com/OU=example/O=com/L=fr/ST=fr/C=fr" \
         -keyout default.example.com-key.pem \
         -out default.example.com-certificate.pem
         ```

      2. Map the key and certificate to the same secret ID in PingGateway:

         ```console
         $ cat default.example.com-key.pem default.example.com-certificate.pem > default.secret.id.pem
         ```

3. Add the following file to PingGateway, replacing `/path/to/secrets` with your path, and restart PingGateway:

   * Linux

     `$HOME/.openig/config/admin.json`

   * Windows

     `%appdata%\OpenIG\config\admin.json`

   ```json
   {
     "connectors": [
       {
         "port": 8080
       },
       {
         "port": 8443,
         "tls": "ServerTlsOptions-1"
       }
     ],
     "heap": [
       {
         "name": "ServerTlsOptions-1",
         "type": "ServerTlsOptions",
         "config": {
           "sni": {
             "serverNames": {
               "ig.example.com": "key.manager.secret.id",
               "*.example.com": "wildcard.secret.id"
             },
             "defaultSecretId" : "default.secret.id",
             "secretsProvider": "ServerIdentityStore"
           }
         }
       },
       {
         "name": "ServerIdentityStore",
         "type": "FileSystemSecretStore",
         "config": {
           "format": "PLAIN",
           "directory": "path/to/secrets",
           "suffix": ".pem",
           "mappings": [
             {
               "secretId": "key.manager.secret.id",
               "format": {
                 "type": "PemPropertyFormat"
               }
             },
             {
               "secretId": "wildcard.secret.id",
               "format": {
                 "type": "PemPropertyFormat"
               }
             },
             {
               "secretId": "default.secret.id",
               "format": {
                 "type": "PemPropertyFormat"
               }
             }
           ]
         }
       }
     ]
   }
   ```

   Source: [admin-https-sni.json](../_attachments/config/admin-https-sni.json)

   Notice the following features of the file:

   * The [ServerTlsOptions](../reference/ServerTlsOptions.html) object maps two servers to secret IDs, and includes a default secret ID

   * The secret IDs correspond to the secret IDs in the FileSystemSecretStore, and the PEM files generated in an earlier step.

4. Run the following commands to request TLS connections to different servers, using different certificates:

   1. Connect to `ig.example.com`, and note that the certificate subject corresponds to the certificate created for `ig.example.com`:

      ```console
      $ openssl s_client -connect localhost:8443 -servername ig.example.com
      ```

      Output

      ```
      ...
      Server certificate
      -----BEGIN CERTIFICATE-----
      MII...dZC
      -----END CERTIFICATE-----
      subject=/CN=ig.example.com/OU=example/O=com/L=fr/ST=fr/C=fr
      issuer=/CN=ig.example.com/OU=example/O=com/L=fr/ST=fr/C=fr
      ```

   2. Connect to `other.example.com`, and note that the certificate subject corresponds to the certificate created with the wildcard, `*.example.com`:

      ```console
      $ openssl s_client -connect localhost:8443 -servername other.example.com
      ```

      Output

      ```
      ...
      Server certificate
      -----BEGIN CERTIFICATE-----
      MII...fY=
      -----END CERTIFICATE-----
      subject=/CN=*.example.com/OU=example/O=com/L=fr/ST=fr/C=fr
      issuer=/CN=*.example.com/OU=example/O=com/L=fr/ST=fr/C=fr
      ```

   3. Connect to `unmapped.site.com`, and note that the certificate subject corresponds to the certificate created for the default secret ID:

      ```console
      $ openssl s_client -connect localhost:8443 -servername unmapped.site.com
      ```

      Output

      ```
      ...
      Server certificate
      -----BEGIN CERTIFICATE-----
      MII..rON
      -----END CERTIFICATE-----
      subject=/CN=un.mapped.com/OU=example/O=com/L=fr/ST=fr/C=fr
      issuer=/CN=un.mapped.com/OU=example/O=com/L=fr/ST=fr/C=fr
      ```

## Configure PingGateway for mutual TLS (server-side)

When PingGateway is *server-side*, applications send requests to PingGateway or request services from PingGateway. PingGateway is acting as a server of the application, and the application is acting as a client.

To run PingGateway as a server for mutual TLS:

* Using information from [Configure PingGateway for TLS (server-side)](#server-side-tls), configure PingGateway for TLS connections.

* In `admin.json`, add a [SecretsTrustManager](../reference/SecretsTrustManager.html) to verify the credentials presented by the client:

  * The trust material is a public key certificate for a client or certificate authority.

  * The SecretsTrustManager must refer to a secret in a secrets store, where the secret is mapped to the certificate.

  * ServerTlsOptions must configure `trustManager` to refer to that SecretsTrustManager and `clientAuth` to require or request the client to authenticate.

  The following example is used in [Mutual TLS with PingAM](../gateway-guide/oauth2-rs-introspect-mtls.html).

  * Linux

    `$HOME/.openig/config/admin.json`

  * Windows

    `%appdata%\OpenIG\config\admin.json`

  ```json
  {
    "mode": "DEVELOPMENT",
    "properties": {
      "ig_keystore_directory": "/path/to/ig/secrets",
      "oauth2_client_keystore_directory": "/path/to/client/secrets"
    },
    "connectors": [
      {
        "port": 8080
      },
      {
        "port": 8443,
        "tls": {
          "type": "ServerTlsOptions",
          "config": {
            "alpn": {
              "enabled": true
            },
            "clientAuth": "REQUEST",
            "keyManager": "SecretsKeyManager-1",
            "trustManager": "SecretsTrustManager-1"
          }
        }
      }
    ],
    "heap": [
      {
        "name": "SecretsPasswords",
        "type": "FileSystemSecretStore",
        "config": {
          "directory": "&{ig_keystore_directory}",
          "format": "PLAIN"
        }
      },
      {
        "name": "SecretsKeyManager-1",
        "type": "SecretsKeyManager",
        "config": {
          "signingSecretId": "key.manager.secret.id",
          "secretsProvider": "ServerIdentityStore"
        }
      },
      {
        "name": "SecretsTrustManager-1",
        "type": "SecretsTrustManager",
        "config": {
          "verificationSecretId": "trust.manager.secret.id",
          "secretsProvider": {
            "type": "KeyStoreSecretStore",
            "config": {
              "file": "&{oauth2_client_keystore_directory}/cacerts.p12",
              "storePasswordSecretId": "keystore.pass",
              "secretsProvider": "SecretsPasswords",
              "mappings": [
                {
                  "secretId": "trust.manager.secret.id",
                  "aliases": ["client-cert"]
                }
              ]
            }
          }
        }
      },
      {
        "name": "ServerIdentityStore",
        "type": "FileSystemSecretStore",
        "config": {
          "format": "PLAIN",
          "directory": "&{ig_keystore_directory}",
          "suffix": ".pem",
          "mappings": [{
            "secretId": "key.manager.secret.id",
            "format": {
              "type": "PemPropertyFormat"
            }
          }]
        }
      }
    ]
  }
  ```

  Source: [admin-mtls.json](../_attachments/config/admin-mtls.json)

---

---
title: Setting up PingGateway environment variables and system properties
description: Configure environment variables and system properties for PingGateway, including startup options, JVM settings, and router scan interval
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:envvar-sysprop
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/envvar-sysprop.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-28T13:04:58Z
keywords: ["Install", "Configuration", "Certificates"]
section_ids:
  start_pinggateway_with_a_customized_router_scan_interval: Start PingGateway with a customized router scan interval
  envvar-sysprop-variables: Define environment variables for startup, runtime, and stop
---

# Setting up PingGateway environment variables and system properties

Configure environment variables and system properties as follows:

* By adding environment variables on the command line when you start PingGateway.

* By adding environment variables in `$HOME/.openig/bin/env.sh`, where `$HOME/.openig` is the instance directory. After changing `env.sh`, restart PingGateway to load the new configuration.

## Start PingGateway with a customized router scan interval

By default, PingGateway scans every 10 seconds for changes to the route configuration files. Any changes to the files are automatically loaded into the configuration without restarting PingGateway. Learn more about the router scan interval in [Router](../reference/Router.html).

The following example overwrites the default value of the Router scan interval to 2 seconds when you start up PingGateway:

* Linux

* Windows

```console
$ IG_ROUTER_SCAN_INTERVAL='2 seconds' /path/to/ping-gateway-2026.6.0/bin/start.sh
```

```none
C:\IG_ROUTER_SCAN_INTERVAL='2 seconds'
C:\start.bat %appdata%\OpenIG
```

## Define environment variables for startup, runtime, and stop

PingGateway provides the following environment variables for Java runtime options:

* IG\_OPTS

  (Optional) Java runtime options for PingGateway and its startup process, such as JVM memory sizing options.

  Include all options that aren't shared with the `stop` script.

  The following example specifies environment variables in the `env.sh` file to customize JVM options and keys:

  * Linux

  * Windows

  ```shell
  # Specify JVM options
  JVM_OPTS="-XX:+UseG1GC -Xmx2048m"

  # Specify the DH key size for stronger ephemeral DH keys and to protect against weak keys
  JSSE_OPTS="-Djdk.tls.ephemeralDHKeySize=2048"

  # Wrap them up into the IG_OPTS environment variable
  export IG_OPTS="${IG_OPTS} ${JVM_OPTS} ${JSSE_OPTS}"
  ```

  ```none
  set "JVM_OPTS=-XX:+UseG1GC -Xmx2048m"
  set "JSSE_OPTS=-Djdk.tls.ephemeralDHKeySize=2048"
  set "IG_OPTS=%IG_OPTS% %JVM_OPTS% %JSSE_OPTS%"
  ```

* JAVA\_OPTS

  (Optional) Java runtime options for PingGateway include all options that are shared by the `start` and `stop` script.

---

---
title: Starting and stopping PingGateway
description: Start and stop PingGateway using default or custom settings, including port and TLS configuration, graceful shutdown, and forcible shutdown with a time limit
component: pinggateway
version: 2026
page_id: pinggateway:installation-guide:start-stop
canonical_url: https://docs.pingidentity.com/pinggateway/2026/installation-guide/start-stop.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-21T12:00:00Z
section_ids:
  starting-default: Start PingGateway with default settings
  starting-options: Start PingGateway with custom settings
  pidFileMode: Allow startup when there is an existing PID file
  stopping: Stop PingGateway
  forcible-shutdown: Forcible shutdown
---

# Starting and stopping PingGateway

## Start PingGateway with default settings

When you start PingGateway, specify the configuration directory where PingGateway looks for configuration files.

1. Start PingGateway:

   * Linux

     `/path/to/ping-gateway-2026.6.0/bin/start.sh`

   * Windows

     `C:\path\to\ping-gateway-2026.6.0\bin\start.bat`

   By default, PingGateway configuration files are located under `$HOME/.openig` on Linux, `%appdata%\OpenIG` on Windows. Learn how to use a different location in [Configuration location](../configure/configure.html#configuration-location).

2. Check that PingGateway is running in one of the following ways:

   * Check the PingGateway endpoint at `http://ig.example.com:8085/health/startup` to make sure PingGateway it returns `HTTP 200 OK`.

     If PingGateway hasn't finished starting up or is shutting down, the endpoint returns `HTTP 503 Service Unavailable`.

   * Display the product version and build information at `http://ig.example.com:8085/api/info`.

## Start PingGateway with custom settings

By default, PingGateway runs on HTTP, on port `8080`, from the instance directory `$HOME/.openig`.

To start PingGateway with custom settings, add the configuration file `admin.json` with the following properties, and restart PingGateway:

* `vertx`: Finely tune Vert.x instances.

* `connectors`: Customize server port, TLS, and Vert.x-specific configurations. Each `connectors` object represents the configuration of an individual port.

The following example starts PingGateway on non-default ports, and configures Vert.x-specific options for the connection on port 9091:

```json
{
  "connectors": [{
    "port": 9090
  },
  {
    "port": 9091,
    "vertx": {
      "maxWebSocketFrameSize": 128000,
      "maxWebSocketMessageSize": 256000,
      "compressionLevel": 4
    }
  }]
}
```

For more information, refer to [AdminHttpApplication (`admin.json`)](../reference/AdminHttpApplication.html).

## Allow startup when there is an existing PID file

By default, if there is an existing PID file during startup the startup fails. Use one of the following ways to allow startup when there is an existing PID file. PingGateway then removes the existing PID file and creates a new one during startup.

1. Add the following configuration to `admin.json` and restart PingGateway:

   ```json
   {
     "pidFileMode": "override"
   }
   ```

   Source: [admin-pidfilemode.json](../_attachments/config/admin-pidfilemode.json)

2. Define an environment variable for the configuration token `ig.pid.file.mode`, and then start PingGateway in the same terminal:

   * Linux

   * Windows

   ```console
   $ IG_PID_FILE_MODE=override /path/to/ping-gateway-2026.6.0/bin/start.sh
   ```

   ```none
   C:\IG_PID_FILE_MODE=override
   C:\path\to\ping-gateway-2026.6.0\bin\start.bat %appdata%\OpenIG
   ```

3. Define a system property for the configuration token `ig.pid.file.mode` when you start PingGateway:

   * Linux

     `$HOME/.openig/env.sh`

   * Windows

     `%appdata%\OpenIG\env.sh`

   ```shell
   export "IG_OPTS=-Dig.pid.file.mode=override"
   ```

## Stop PingGateway

Use the `stop.sh` script to stop an instance of PingGateway, specifying the instance directory as an argument.

If the instance directory isn't specified, PingGateway uses the default instance directory as in these examples:

* Linux

  `/path/to/ping-gateway-2026.6.0/bin/stop.sh $HOME/.openig`

* Windows

  `C:\path\to\ping-gateway-2026.6.0\bin\stop.bat %appdata%\OpenIG`

### Forcible shutdown

By default, the `stop.sh` and `stop.bat` scripts let the PingGateway process terminate gracefully.

You can set a time limit in milliseconds after which the script forces PingGateway to shut down. Specify the time limit after the instance directory argument.

The following examples kill the PingGateway process after 20 seconds if it has failed to terminate gracefully:

* Linux

  `/path/to/ping-gateway-2026.6.0/bin/stop.sh $HOME/.openig 20000`

* Windows

  `C:\path\to\ping-gateway-2026.6.0\bin\stop.bat %appdata%\OpenIG 20000`

Make sure the time limit is longer than the grace period for connections to close (default: 1 second/1000 milliseconds). Learn about the `"gracePeriod"` settings in the `admin.json` reference documentation for [administrative connections](../reference/AdminHttpApplication.html#AdminHttpApplication-adminConnector-gracePeriod) and [client connections](../reference/AdminHttpApplication.html#AdminHttpApplication-connectors-gracePeriod)
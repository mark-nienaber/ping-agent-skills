---
title: Auditing the PingGateway deployment
description: "Configure auditing for a PingGateway deployment: set up audit event handlers, safelist fields, trust transaction IDs, and add custom data"
component: pinggateway
version: 2026
page_id: pinggateway:maintenance-guide:auditing
canonical_url: https://docs.pingidentity.com/pinggateway/2026/maintenance-guide/auditing.html
revdate: 2026-04-02T14:30:00Z
keywords: ["Maintenance", "Configuration", "Deployment", "Audit", "JSON", "Logs", "Safelist", "OpenID Connect (OIDC)", "SAML 2.0", "Authentication"]
section_ids:
  audit-csv: Record access audit events in CSV
  audit-jms: Record access audit events with a JMS audit event handler
  audit-json: Record access audit events with a JSON audit event handler
  audit-jsonstdout: Record access audit events to standard output
  trust-transaction-id: Trust transaction IDs from other products
  common-audit-safelist: Safelist audit event fields for the logs
  maint-audit-include-exclude: Include or exclude audit event fields in logs
  proc-audit-exclude: Exclude safelisted audit event fields from logs
  audit-userid: Record user ID in audit events
  record_user_id_in_audit_logs_after_sso_authentication: Record user ID in audit logs after SSO authentication
  record_user_id_in_audit_logs_after_openid_connect_authentication: Record user ID in audit logs after OpenID connect authentication
  extend-audit-events-custom-data: Extend audit events with custom data
---

# Auditing the PingGateway deployment

The following sections describe how to set up auditing for your deployment. You can find information on how to include user ID in audit logs in [Recording User ID in Audit Events](#audit-userid).

You can find more information about configuring the JMS event handler in [PingGateway audit framework](../reference/AuditFramework.html).

## Record access audit events in CSV

This section describes how to record access audit events in a CSV file.

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The CSV handler doesn't sanitize messages when writing to CSV log files.Don't open CSV logs in spreadsheets or other applications that treat data as code. |

Before you start, prepare PingGateway and the sample application as described in the [Getting started with PingGateway](../getting-started/preface.html).

1. Set up PingGateway

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   3. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/30-csv.json`

      * Windows

        `%appdata%\OpenIG\config\routes\30-csv.json`

      ```json
      {
        "name": "30-csv",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/csv-audit')}",
        "heap": [
          {
            "name": "AuditService",
            "type": "AuditService",
            "config": {
              "eventHandlers": [
                {
                  "class": "org.forgerock.audit.handlers.csv.CsvAuditEventHandler",
                  "config": {
                    "name": "csv",
                    "logDirectory": "/tmp/logs",
                    "topics": [
                      "access"
                    ]
                  }
                }
              ],
              "config": {}
            }
          }
        ],
        "auditService": "AuditService",
        "handler": {
          "type": "Chain",
          "config": {
            "filters": [
              "TransactionIdOutboundFilter"
            ],
            "handler": "ReverseProxyHandler"
          }
        }
      }
      ```

      Source: [30-csv.json](../_attachments/config/routes/30-csv.json)

      The route calls an audit service configuration for publishing log messages to the CSV file, `/tmp/logs/access.csv`.

      When a request matches `audit`, PingGateway logs audit events to the CSV file.

      The route uses the `TransactionIdOutboundFilter` in its handler. This filter includes the `X-ForgeRock-TransactionId` header in requests.

2. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/csv-audit> and accept the server certificate.

      The sample application displays the home page and PingGateway updates the `/tmp/logs/access.csv` file.

## Record access audit events with a JMS audit event handler

|   |                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The [JmsAuditEventHandler](../reference/JmsAuditEventHandler.html) is deprecated. Use an alternative audit event handler.

* This procedure is an example of how to record access audit events with a JMS audit event handler configured to use the ActiveMQ message broker. This example isn't tested on all configurations, and can be more or less relevant to your configuration. |

Before you start, prepare PingGateway as described in the [Getting started with PingGateway](../getting-started/preface.html).

1. Download the following files:

   * [ActiveMQ binary](https://activemq.apache.org/components/classic/download/). PingGateway is tested with ActiveMQ Classic 5.15.11.

   * [ActiveMQ Client](https://repository.apache.org/content/repositories/releases/org/apache/activemq/activemq-client). Use a version that corresponds to your ActiveMQ version.

   * [Apache Geronimo J2EE management bundle](https://repo1.maven.org/maven2/org/apache/geronimo/specs/geronimo-j2ee-management_1.1_spec/1.0.1/).

   * [hawtbuf-1.11 JAR](https://repo1.maven.org/maven2/org/fusesource/hawtbuf/hawtbuf/1.11/).

2. Add the files to the configuration:

   * Create the directory `$HOME/.openig/extra`, where `$HOME/.openig` is the instance directory, and add .jar files to the directory.

3. Create a consumer that subscribes to the `audit` topic.

   From the ActiveMQ installation directory, run the following command:

   ```console
   $ ./bin/activemq consumer --destination topic://audit
   ```

4. Set up PingGateway

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/30-jms.json`

      * Windows

        `%appdata%\OpenIG\config\routes\30-jms.json`

      ```json
      {
        "name": "30-jms",
        "MyCapture" : "all",
        "condition" : "${request.uri.path == '/activemq_event_handler'}",
        "heap": [
          {
            "name": "AuditService",
            "type": "AuditService",
            "config": {
              "eventHandlers" : [
                {
                  "class" : "org.forgerock.audit.handlers.jms.JmsAuditEventHandler",
                  "config" : {
                    "name" : "jms",
                    "topics": [ "access" ],
                    "deliveryMode" : "NON_PERSISTENT",
                    "sessionMode" : "AUTO",
                    "jndi" : {
                      "contextProperties" : {
                        "java.naming.factory.initial" : "org.apache.activemq.jndi.ActiveMQInitialContextFactory",
                        "java.naming.provider.url" : "tcp://am.example.com:61616",
                        "topic.audit" : "audit"
                      },
                      "topicName" : "audit",
                      "connectionFactoryName" : "ConnectionFactory"
                    }
                  }
                }
              ],
              "config" : { }
            }
          }
        ],
        "auditService": "AuditService",
        "handler" : {
          "type" : "StaticResponseHandler",
          "config" : {
            "status" : 200,
            "headers" : {
              "Content-Type" : [ "text/plain; charset=UTF-8" ]
            },
            "entity" : "Message from audited route"
          }
        }
      }
      ```

      Source: [30-jms.json](../_attachments/config/routes/30-jms.json)

      When a request matches the `/activemq_event_handler` route, this configuration publishes JMS messages containing audit event data to an ActiveMQ managed JMS topic, and the StaticResponseHandler displays a message.

5. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/activemq_event_handler> and accept the server certificate.

      Depending on how ActiveMQ is configured, audit events are displayed on the ActiveMQ console or written to file.

## Record access audit events with a JSON audit event handler

This section describes how to record access audit events with a JSON audit event handler. You can find more information about configuring the JSON event handler in [JsonAuditEventHandler](../reference/JsonAuditEventHandler.html).

1. Set up PingGateway

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   3. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/30-json.json`

      * Windows

        `%appdata%\OpenIG\config\routes\30-json.json`

      ```json
      {
        "name": "30-json",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/json-audit')}",
        "heap": [
          {
            "name": "AuditService",
            "type": "AuditService",
            "config": {
              "eventHandlers": [
                {
                  "class": "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
                  "config": {
                    "name": "json",
                    "logDirectory": "/tmp/logs",
                    "topics": [
                      "access"
                    ],
                    "rotationRetentionCheckInterval": "1 minute",
                    "buffering": {
                      "maxSize": 100000,
                      "writeInterval": "100 ms"
                    }
                  }
                }
              ]
            }
          }
        ],
        "auditService": "AuditService",
        "handler": "ReverseProxyHandler"
      }
      ```

      Source: [30-json.json](../_attachments/config/routes/30-json.json)

      Notice the following features of the route:

      * The route calls an audit service configuration for publishing log messages to the JSON file, `/tmp/audit/access.audit.json`. When a request matches `/home/json-audit`, a single line per audit event is logged to the JSON file.

      * The route uses the `ForgeRockClientHandler` as its handler to send the `X-ForgeRock-TransactionId` header with its requests to external services.

2. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/json-audit> and accept the server certificate.

      The home page of the sample application is displayed and the file `/tmp/logs/access.audit.json` is created or updated with a message. The following example message is formatted for easy reading, but it is produced as a single line for each event:

      ```json
      {
        "_id": "830...-41",
        "timestamp": "2019-...540Z",
        "eventName": "OPENIG-HTTP-ACCESS",
        "transactionId": "830...-40",
        "client": {
          "ip": "0:0:0:0:0:0:0:1",
          "port": 51666
        },
        "server": {
          "ip": "0:0:0:0:0:0:0:1",
          "port": 8080
        },
        "http": {
          "request": {
            "secure": false,
            "method": "GET",
            "path": "http://ig.example.com:8080/home/json-audit",
            "headers": {
              "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8"],
              "host": ["ig.example.com:8080"],
              "user-agent": ["Mozilla/5.0 ... Firefox/66.0"]
            }
          }
        },
        "response": {
          "status": "SUCCESSFUL",
          "statusCode": "200",
          "elapsedTime": 212,
          "elapsedTimeUnits": "MILLISECONDS"
        },
        "ig": {
          "exchangeId": "b3f...-29",
          "routeId": "30-json",
          "routeName": "30-json"
        }
      }
      ```

## Record access audit events to standard output

This section describes how to record access audit events to standard output. You can find more information about the event handler in [JsonStdoutAuditEventHandler](../reference/JsonStdoutAuditEventHandler.html).

Before you start, prepare PingGateway and the sample application as described in the [Getting started with PingGateway](../getting-started/preface.html).

1. Set up PingGateway

   1. Set up PingGateway for HTTPS, as described in [Configure PingGateway for TLS (server-side)](../installation-guide/securing-connections.html#server-side-tls).

   2. Make sure PingGateway connects to the sample application over HTTPS with a route to access static resources.

      Learn more in [Using the sample application](../getting-started/start-sampleapp.html).

   3. Add the following route to PingGateway:

      * Linux

        `$HOME/.openig/config/routes/30-jsonstdout.json`

      * Windows

        `%appdata%\OpenIG\config\routes\30-jsonstdout.json`

      ```json
      {
        "name": "30-jsonstdout",
        "baseURI": "https://app.example.com:8444",
        "condition": "${find(request.uri.path, '^/home/jsonstdout-audit')}",
        "heap": [
          {
            "name": "AuditService",
            "type": "AuditService",
            "config": {
              "eventHandlers": [
                {
                  "class": "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
                  "config": {
                    "name": "jsonstdout",
                    "elasticsearchCompatible": false,
                    "topics": [
                      "access"
                    ]
                  }
                }
              ],
              "config": {}
            }
          }
        ],
        "auditService": "AuditService",
        "handler": "ReverseProxyHandler"
      }
      ```

      Source: [30-jsonstdout.json](../_attachments/config/routes/30-jsonstdout.json)

      Notice the following features of the route:

      * The route matches requests to `/home/jsonstdout-audit`.

      * The route calls the audit service configuration for publishing access log messages to standard output. When a request matches `/home/jsonstdout-audit`, a single line per audit event is logged.

2. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/jsonstdout-audit> and accept the server certificate.

   The home page of the sample application is displayed, and a message like this is published to standard output:

   ```json
   {
     "_id": "830...-61",
     "timestamp": "2019-...89Z",
     "eventName": "OPENIG-HTTP-ACCESS",
     "transactionId": "830...-60",
     "client": {
       "ip": "0:0:0:0:0:0:0:1",
       "port": 51876
     },
     "server": {
       "ip": "0:0:0:0:0:0:0:1",
       "port": 8080
     },
     "http": {
       "request": {
         "secure": false,
         "method": "GET",
         "path": "http://ig.example.com:8080/home/jsonstdout-audit",
         "headers": {
           "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8"],
           "host": ["ig.example.com:8080"],
           "user-agent": ["Mozilla/5.0 ... Firefox/66.0"]
         }
       }
     },
     "response": {
       "status": "SUCCESSFUL",
       "statusCode": "200",
       "elapsedTime": 10,
       "elapsedTimeUnits": "MILLISECONDS"
     },
     "ig": {
       "exchangeId": "b3f...-41",
       "routeId": "30-jsonstdout",
       "routeName": "30-jsonstdout"
     },
     "source": "audit",
     "topic": "access",
     "level": "INFO"
   }
   ```

## Trust transaction IDs from other products

Each audit event is identified by a unique transaction ID that can be communicated across products and recorded for each local event. By using the transaction ID, requests can be tracked as they traverse the platform, making it easier to monitor activity and to enrich reports.

PingGateway sets the `X-ForgeRock-TransactionId` header in outgoing HTTP calls to other platform products. You can also set this header in your applications or scripts that call into the Ping Identity Platform.

To reduce the risk of malicious attacks, by default PingGateway doesn't trust transaction ID headers from client applications.

If you trust the transaction IDs sent by your client applications, consider setting Java system property `org.forgerock.http.TrustTransactionHeader` to `true`.

Add the following system property in `env.sh`:

```shell
# Specify a JVM option
TX_HEADER_OPT="-Dorg.forgerock.http.TrustTransactionHeader=true"

# Include it into the JAVA_OPTS environment variable
export JAVA_OPTS="${TX_HEADER_OPT}"
```

All incoming `X-ForgeRock-TransactionId` headers are trusted, and monitoring or reporting systems that consume the logs can allow requests to be correlated as they traverse multiple servers.

## Safelist audit event fields for the logs

To prevent logging of sensitive data for an audit event, PingGateway uses a safelist to specify which audit event fields appear in the logs.

By default, only safelisted audit event fields are included in the logs. You can find information about how to include non-safelisted audit event fields or exclude safelisted audit event fields in [Include or exclude audit event fields in logs](#maint-audit-include-exclude).

Audit event fields use JSON pointer notation, and are taken from the JSON schema for the audit event content. The following event fields are safelisted:

* `/_id`

* `/timestamp`

* `/eventName`

* `/transactionId`

* `/trackingIds`

* `/userId`

* `/client`

* `/server`

* `/ig/exchangeId`

* `/ig/routeId`

* `/ig/routeName`

* `/ig/ext`

* `/http/request/secure`

* `/http/request/method`

* `/http/request/path`

* `/http/request/headers/accept`

* `/http/request/headers/accept-api-version`

* `/http/request/headers/content-type`

* `/http/request/headers/host`

* `/http/request/headers/user-agent`

* `/http/request/headers/x-forwarded-for`

* `/http/request/headers/x-forwarded-host`

* `/http/request/headers/x-forwarded-port`

* `/http/request/headers/x-forwarded-proto`

* `/http/request/headers/x-original-uri`

* `/http/request/headers/x-real-ip`

* `/http/request/headers/x-request-id`

* `/http/request/headers/x-requested-with`

* `/http/request/headers/x-scheme`

* `/request`

* `/response`

## Include or exclude audit event fields in logs

The safelist is designed to prevent logging of sensitive data for audit events by specifying which audit event fields appear in the logs. You can add or remove messages from the logs as follows:

* To include audit event fields in logs that aren't safelisted, configure the `includeIf` property of AuditService.

  |   |                                                                                                                                                                                                                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Before you include non-safelisted audit event fields in the logs, consider the impact on security. Including some headers, query parameters, or cookies in the logs could cause credentials or tokens to be logged, and allow anyone with access to the logs to impersonate the holder of these credentials or tokens. |

* To exclude safelisted audit event fields from the logs, configure the `excludeIf` property of AuditService. You can find an example in [Exclude safelisted audit event fields from logs](#proc-audit-exclude).

### Exclude safelisted audit event fields from logs

Before you start, set up and test the example in [Recording access audit events in JSON](#audit-json). Note the audit event fields in the log file `access.audit.json`.

1. Replace `30-json.json` with the following route:

   * Linux

     `$HOME/.openig/config/routes/30-json-excludeif.json`

   * Windows

     `%appdata%\OpenIG\config\routes\30-json-excludeif.json`

   ```json
   {
     "name": "30-json-excludeif",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/json-audit-excludeif$')}",
     "heap": [
       {
         "name": "AuditService",
         "type": "AuditService",
         "config": {
           "config": {
             "filterPolicies": {
               "field": {
                 "excludeIf": [
                   "/access/http/request/headers/host",
                   "/access/http/request/path",
                   "/access/server",
                   "/access/response"
                 ]
               }
             }
           },
           "eventHandlers": [
             {
               "class": "org.forgerock.audit.handlers.json.JsonAuditEventHandler",
               "config": {
                 "name": "json",
                 "logDirectory": "/tmp/logs",
                 "topics": [
                   "access"
                 ],
                 "rotationRetentionCheckInterval": "1 minute",
                 "buffering": {
                   "maxSize": 100000,
                   "writeInterval": "100 ms"
                 }
               }
             }
           ]
         }
       }
     ],
     "auditService": "AuditService",
     "handler": "ReverseProxyHandler"
   }
   ```

   Source: [30-json-excludeif.json](../_attachments/config/routes/30-json-excludeif.json)

   Notice that the AuditService is configured with an `excludeIf` property to exclude audit event fields from the logs.

2. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/json-audit-excludeif> and accept the server certificate.

   The home page of the sample application is displayed and the file `/tmp/logs/access.audit.json` is updated:

   ```json
   {
     "_id": "830...-41",
     "timestamp": "2019-...540Z",
     "eventName": "OPENIG-HTTP-ACCESS",
     "transactionId": "830...-40",
     "client": {
       "ip": "0:0:0:0:0:0:0:1",
       "port": 51666
     },
     "http": {
       "request": {
         "secure": false,
         "method": "GET",
         "headers": {
           "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
           "user-agent": ["Mozilla/5.0 ... Firefox/66.0"]
         }
       }
     },
     "ig": {
       "exchangeId": "b3f...-56",
       "routeId": "30-json-excludeif",
       "routeName": "30-json-excludeif"
     }
   }
   ```

3. Compare the audit event fields in `access.audit.json` with those produced in [Recording access audit events in JSON](#audit-json), and note that the audit event fields specified by the `excludeIf` property no longer appear in the logs.

## Record user ID in audit events

The following sections provide examples of how to capture the AM user ID in audit logs.

Sample scripts are available in the `openig-samples.jar` file, to capture the user ID after SSO, CDSSO, OpenID, or SAML authentication. The scripts inject the user ID into the RequestAuditContext so that it is available when the audit event is written.

Using the notes in the sample scripts, adapt the script for your deployment. For example, configure which `user_info` field to capture in the audit event.

The audit service in these examples use a JsonStdoutAuditEventHandler, which writes audit events to standard output, but can be any other audit service.

### Record user ID in audit logs after SSO authentication

Before you start, set up and test the example in [Cross-domain single sign-on for PingAM](../gateway-guide/cdsso.html).

1. Add the following script to PingGateway:

   * Linux

     `$HOME/.openig/scripts/groovy/InjectUserIdSso.groovy`

   * Windows

     `%appdata%\OpenIG\scripts\groovy\InjectUserIdSso.groovy`

   ```java
   package scripts.groovy

   import org.forgerock.openig.openam.SsoTokenContext
   import org.forgerock.services.context.RequestAuditContext

   /**
    * Sample ScriptableFilter implementation to capture the user id from the session
    * and inject it into the RequestAuditContext for later use when the audit event
    * is written.
    *
    * This ScriptableFilter should be added in the filter chain at whatever point the
    * desired user id is available - e.g. on the session after SSO.
    *
    * "handler": {
    *   "type": "Chain",
    *   "config": {
    *     "filters": [ {
    *        "name": "SingleSignOnFilter-1",
    *         "type": "SingleSignOnFilter",
    *         "config": {
    *           "amService": "AmService-1"
    *         }
    *       }, {
    *         "type" : "ScriptableFilter",
    *         "config" : {
    *           "file" : "InjectUserIdSso.groovy",
    *           "type": "application/x-groovy"
    *         }
    *       }
    *     ],
    *     "handler" : "ReverseProxyHandler",
    * }
    *
    * When using the SSO/ CDSSO flow then the SsoTokenContext is guaranteed to exist and
    * be populated if there was no error. The RequestAuditContext is also guaranteed to
    * be available. Note also that if the SessionInfoFilter is present in the route then
    * a SessionInfoContext would be available in the context chain and could be queried
    * for user info.
    *
    * Implementors may decide which user id field to capture in the audit event:
    * - The sessionInfo universalId - 'universalId' - is always available as
    *   provided by AM and resembles -
    *   e.g. "id=bonnie,ou=user,o=myrealm,ou=services,dc=openam,dc=forgerock,dc=org".
    * - The sessionInfo username - mapped to 'username') resembles - e.g. "bonnie".
    *   Field 'username' should be preferred to 'uid', which also points to 'username'.
    *
    * Additional error handling may be required.
    *
    * @see RequestAuditContext
    * @see SsoTokenContext
    * @see org.forgerock.openig.openam.SessionInfoContext
    */

   def requestAuditContext = context.asContext(RequestAuditContext.class)
   def ssoTokenContext = context.asContext(SsoTokenContext.class)

   // The sessionInfo 'universalId' is always available, though 'username' may be unknown
   requestAuditContext.setUserId(ssoTokenContext.universalId)

   // Propagate the request to the next filter/ handler in the chain
   next.handle(context, request)
   ```

   Source: [InjectUserIdSso.groovy](../_attachments/scripts/groovy/InjectUserIdSso.groovy)

   The script captures the user ID after SSO or CDSSO authentication, and injects it into the RequestAuditContext so that it is available when the audit event is written.

2. Replace `sso.json` with the following route:

   * Linux

     `$HOME/.openig/config/routes/audit-sso.json`

   * Windows

     `%appdata%\OpenIG\config\routes\audit-sso.json`

   ```json
   {
     "name": "audit-sso",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/audit-sso$')}",
     "heap": [
       {
         "name": "AuditService",
         "type": "AuditService",
         "config": {
           "eventHandlers": [
             {
               "class": "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
               "config": {
                 "name": "jsonstdout",
                 "elasticsearchCompatible": false,
                 "topics": [
                   "access"
                 ]
               }
             }
           ],
           "config": {}
         }
       },
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       },
       {
         "name": "AmService-1",
         "type": "AmService",
         "config": {
           "agent": {
             "username": "ig_agent",
             "passwordSecretId": "agent.secret.id"
           },
           "secretsProvider": "SystemAndEnvSecretStore-1",
           "url": "http://am.example.com:8088/openam/"
         }
       }
     ],
     "auditService": "AuditService",
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "name": "SingleSignOnFilter-1",
             "type": "SingleSignOnFilter",
             "config": {
               "amService": "AmService-1"
             }
           },
           {
             "type" : "ScriptableFilter",
             "config" : {
               "file" : "InjectUserIdSso.groovy",
               "type": "application/x-groovy"
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     }
   }
   ```

   Source: [audit-sso.json](../_attachments/config/routes/audit-sso.json)

   Notice the following features of the route compared to `sso.json`:

   * The route matches requests to `/home/audit-sso`.

   * An audit service is included to publish access log messages to standard output.

   * The chain includes a scriptable filter that refers to `InjectUserIdSso.groovy`.

3. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/audit-sso> and accept the server certificate. The SingleSignOnFilter redirects the request to AM for authentication.

   2. Log in to AM as user `demo`, password `Ch4ng31t`, and then allow the application to access user information.

      The profile page of the sample application is displayed. The script captures the user ID from the session, and the audit service includes it with the audit event.

   3. Search the standard output for a message like this, containing the user ID:

      ```json
      {
        "_id": "23a...-23",
        "timestamp": "...",
        "eventName": "OPENIG-HTTP-ACCESS",
        "transactionId": "23a...-22",
        "userId": "id=demo,ou=user,dc=openam,dc=forgerock,dc=org",
        "client": {
          "ip": "0:0:0:0:0:0:0:1",
          "port": 57843
        },
        "server": {
          "ip": "0:0:0:0:0:0:0:1",
          "port": 8080
        },
        "http": {
          "request": {
            "secure": false,
            "method": "GET",
            "path": "http://ig.example.com/home/audit-sso",
            "headers": {
              "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8"],
              "host": ["ig.example.com:8080"],
              "user-agent": [...]
            }
          }
        },
        "response": {
          "status": "SUCCESSFUL",
          "statusCode": "200",
          "elapsedTime": 276,
          "elapsedTimeUnits": "MILLISECONDS"
        },
        "ig": {
          "exchangeId": "1dc...-26",
          "routeId": "audit-sso",
          "routeName": "audit-sso"
        },
        "source": "audit",
        "topic": "access",
        "level": "INFO"
      }
      ```

### Record user ID in audit logs after OpenID connect authentication

1. Set up and test the example in [AM as OIDC provider](../gateway-guide/oidc-am.html).

2. Make sure the token signature algorithm in the `oidc_client` profile uses HMAC with the client password as the symmetric key:

   1. In the AM admin UI, select Applications > OAuth 2.0 > Clients > `oidc_client`.

   2. Under Signing and Encryption, set ID Token Signing Algorithm to `HS256` and click Save Changes.

3. Add the following example script to PingGateway:

   * Linux

     `$HOME/.openig/scripts/groovy/InjectUserIdOpenId.groovy`

   * Windows

     `%appdata%\OpenIG\scripts\groovy\InjectUserIdOpenId.groovy`

   ```java
   package scripts.groovy

   import org.forgerock.services.context.RequestAuditContext
   import org.forgerock.openig.filter.oauth2.client.OAuth2InfoContext

   /**
    * Sample script implementation supporting user id injection in an OpenId scenario.
    *
    * <p>This sample captures the user id and injects it into the RequestAuditContext for later use when the audit event is
    * written.
    *
    * <p>This ScriptableFilter should be added in the filter chain at whatever point the desired user id is available -
    * e.g. after OpenId client authentication (in the OAuth2 authentication filter chain) - as follows:
    * <pre>
    * {@code
    * "handler" : {
    *   "type" : "Chain",
    *   "config" : {
    *     "filters" : [ {
    *       "type" : "AuthorizationCodeOAuth2ClientFilter",
    *       "config" : {
    *         ...
    *         "registrations" : [ "ClientRegistrationWithOpenIdScope" ],
    *       }
    *     }, {
    *       "type" : "ScriptableFilter",
    *       "config" : {
    *         "file" : "InjectUserIdOpenId.groovy",
    *         "type": "application/x-groovy"
    *       }
    *     } ],
    *     "handler" : "display-user-info-groovy-handler"
    *   }
    * }
    * }
    * </pre>
    *
    * <p>The ClientRegistration associated with the above AuthorizationCodeOAuth2ClientFilter config will require the
    * 'openid' scope. The {@link OAuth2InfoContext} and {@link RequestAuditContext} are guaranteed to exist and be
    * populated on successful authentication.
    *
    * <p>Implementors may decide which 'user_info' field to capture in the audit event:
    * <ul>
    *   <li>The userinfo 'sub' field is the user's "complex" ID marked with a type - e.g. "(usr!bonnie)".
    *   <li>The userinfo 'subName' field is the user's username (or resource name) - e.g. "bonnie".
    *   <li>To capture the universalId (consistent with the session info universalId), it is necessary to configure AM to
    *   provide it as a claim in the id-token. To do this, edit the OIDC Claims Script to include the following line just
    *   prior to the UserInfoClaims creation: computedClaims["universalId"] = identity.universalId
    *   <li>This will include 'universalId' in the userinfo which we can use with audit e.g.
    *   "id=bonnie,ou=user,o=myrealm,ou=services,dc=openam,dc=forgerock,dc=org"
    * </ul>
    *
    * <p>Additional error handling may be required.
    */

   def requestAuditContext = context.asContext(RequestAuditContext.class)
   def oauth2InfoContext = context.asContext(OAuth2InfoContext.class)

   // The AuthorizationCodeOAuth2ClientFilter captures userinfo in a dedicated OAuth2Info context. We can query this for
   // 'userInfo' values: 'sub', 'subName' or anything else made available via the OIDC Claims Script (see above).
   requestAuditContext.setUserId(oauth2InfoContext.userInfo["sub"])

   // Propagate the request to the next filter/ handler in the chain
   next.handle(context, request)
   ```

   Source: [InjectUserIdOpenId.groovy](../_attachments/scripts/groovy/InjectUserIdOpenId.groovy)

   The script captures the user ID and injects it into the RequestAuditContext so that it is available when the audit event is written.

4. Replace `07-openid.json` with the following route:

   * Linux

     `$HOME/.openig/config/routes/audit-oidc.json`

   * Windows

     `%appdata%\OpenIG\config\routes\audit-oidc.json`

   ```json
   {
     "name": "audit-oidc",
     "baseURI": "https://app.example.com:8444",
     "condition": "${find(request.uri.path, '^/home/id_token')}",
     "heap": [
       {
         "name": "AuditService",
         "type": "AuditService",
         "config": {
           "eventHandlers": [
             {
               "class": "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
               "config": {
                 "name": "jsonstdout",
                 "elasticsearchCompatible": false,
                 "topics": [
                   "access"
                 ]
               }
             }
           ],
           "config": {}
         }
       },
       {
         "name": "SystemAndEnvSecretStore-1",
         "type": "SystemAndEnvSecretStore"
       },
       {
         "name": "AuthenticatedRegistrationHandler-1",
         "type": "Chain",
         "config": {
           "filters": [
             {
               "name": "ClientSecretBasicAuthenticationFilter-1",
               "type": "ClientSecretBasicAuthenticationFilter",
               "config": {
                 "clientId": "oidc_client",
                 "clientSecretId": "oidc.secret.id",
                 "secretsProvider": "SystemAndEnvSecretStore-1"
               }
             }
           ],
           "handler": "ForgeRockClientHandler"
         }
       }
     ],
     "auditService": "AuditService",
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "name": "AuthorizationCodeOAuth2ClientFilter-1",
             "type": "AuthorizationCodeOAuth2ClientFilter",
             "config": {
               "clientEndpoint": "/home/id_token",
               "failureHandler": {
                 "type": "StaticResponseHandler",
                 "config": {
                   "status": 500,
                   "headers": {
                     "Content-Type": [
                       "text/plain"
                     ]
                   },
                   "entity": "Error in OAuth 2.0 setup."
                 }
               },
               "registrations": [
                 {
                   "name": "oidc-user-info-client",
                   "type": "ClientRegistration",
                   "config": {
                     "clientId": "oidc_client",
                     "issuer": {
                       "name": "Issuer",
                       "type": "Issuer",
                       "config": {
                         "wellKnownEndpoint": "http://am.example.com:8088/openam/oauth2/.well-known/openid-configuration"
                       }
                     },
                     "scopes": [
                       "openid",
                       "profile",
                       "email"
                     ],
                     "authenticatedRegistrationHandler": "AuthenticatedRegistrationHandler-1",
                     "clientSecretIdUsage": "ID_TOKEN_VALIDATION_ONLY",
                     "clientSecretId": "oidc.secret.id",
                     "secretsProvider": "SystemAndEnvSecretStore-1"
                   }
                 }
               ],
               "requireHttps": false,
               "cacheExpiration": "disabled"
             }
           },
           {
             "type": "ScriptableFilter",
             "config": {
               "file": "InjectUserIdOpenId.groovy",
               "type": "application/x-groovy"
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     }
   }
   ```

   Source: [audit-oidc.json](../_attachments/config/routes/audit-oidc.json)

   Notice the following features of the route compared to `07-openid.json`:

   * An audit service is included to publish access log messages to standard output.

   * The chain includes a scriptable filter that refers to `InjectUserIdOpenId.groovy`.

5. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/id_token>. The AM login page is displayed.

   2. Log in to AM as user `demo`, password `Ch4ng31t`, and then allow the application to access user information.

      The home page of the sample application is displayed. The script captures the user ID from the `openid` target, and the audit service includes it with the audit event.

   3. Search the standard output for a message like this, containing the user ID:

      ```json
      {
        "_id": "<uuid>",
        "timestamp": "<timestamp>",
        "eventName": "OPENIG-HTTP-ACCESS",
        "transactionId": "<uuid>",
        "userId": "(usr!demo)",
        "client": {
          "ip": "127.0.0.1",
          "port": 62056
        },
        "server": {
          "ip": "127.0.0.1",
          "port": 8443
        },
        "http": {
          "request": {
            "secure": true,
            "method": "GET",
            "path": "https://ig.example.com:8443/home/id_token",
            "headers": {
              "accept": [
                "..."
              ],
              "user-agent": [
                "..."
              ]
            }
          }
        },
        "response": {
          "status": "SUCCESSFUL",
          "statusCode": "200",
          "elapsedTime": 29,
          "elapsedTimeUnits": "MILLISECONDS"
        },
        "ig": {
          "exchangeId": "<uuid>",
          "routeId": "openid",
          "routeName": "audit-oidc"
        },
        "source": "audit",
        "topic": "access",
        "level": "INFO"
      }
      ```

## Extend audit events with custom data

This section describes how to add custom data to access audit logs using the `accessAuditExtension` context. When this context is present, PingGateway logs `key:value` pairs with custom data in an extension object (`ext`) under the `ig` section of the event in access audit logs.

Before you start, set up and test the example in [Record access audit events with a JSON audit event handler](#audit-json).

1. Add the following script to PingGateway:

   * Linux

     `$HOME/.openig/scripts/groovy/AuditResponse.groovy`

   * Windows

     `%appdata%\OpenIG\scripts\groovy\AuditResponse.groovy`

   ```java
   next.handle(context, request)
       .thenOnResult(response -> {
           if (!response.status.isSuccessful()) {
               logger.info("Error response, skipping audit")
               return
           }

           // NO_CONTENT is typically returned by deletes
           if (response.status == Status.NO_CONTENT) {
               logger.info("No Content response, skipping audit")
               return
           }

           responseId = response.entity.json['id']

           if (responseId == null) {
               logger.info("Response ID is null, skipping audit")
               return
           }

           contexts.accessAuditExtension.extendWith('response-id', responseId)

       })
   ```

   Source: [AuditResponse.groovy](../_attachments/scripts/AuditResponse.groovy)

   The script extends the audit event with custom data from the response of the sample application using the [`accessAuditExtension` context](../reference/AccessAuditExtensionContext.html).

2. Test the setup:

   1. In your browser's privacy or incognito mode, go to <https://ig.example.com:8443/home/json-audit> and accept the server certificate.

      The home page of the sample application is displayed and the file `/tmp/logs/access.audit.json` is updated:

      ```json
      {
        "_id": "830...-41",
        "timestamp": "2026-...540Z",
        "eventName": "OPENIG-HTTP-ACCESS",
        "transactionId": "830...-40",
        "client": {
          "ip": "0:0:0:0:0:0:0:1",
          "port": 51666
        },
        "server": {
          "ip": "0:0:0:0:0:0:0:1",
          "port": 8080
        },
        "http": {
          "request": {
            "secure": false,
            "method": "GET",
            "path": "http://ig.example.com:8080/home/json-audit",
            "headers": {
              "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8"],
              "host": ["ig.example.com:8080"],
              "user-agent": ["Mozilla/5.0 ... Firefox/66.0"]
            }
          }
        },
        "response": {
          "status": "SUCCESSFUL",
          "statusCode": "200",
          "elapsedTime": 212,
          "elapsedTimeUnits": "MILLISECONDS"
        },
        "ig": {
          "exchangeId": "b3f...-29",
          "routeId": "30-json",
          "routeName": "30-json",
          "ext": {
            "response-id": "<uuid>"
          }
        }
      }
      ```

Notice that the custom data is now logged.

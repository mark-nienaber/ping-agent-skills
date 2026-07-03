---
title: Migrating from web container mode to PingGateway standalone mode
description: Migrate PingGateway from .war web container delivery to standalone .zip mode, covering session replication, TLS, access logs, and configuration changes
component: pinggateway
version: 2026
page_id: pinggateway:upgrade:upgrade-war-to-zip
canonical_url: https://docs.pingidentity.com/pinggateway/2026/upgrade/upgrade-war-to-zip.html
revdate: 2025-04-01T17:53:34Z
keywords: ["Install", "Configuration", "Migration", "Authentication", "Certificates"]
section_ids:
  session_replication_between_pinggateway_instances: Session replication between PingGateway instances
  streaming_asynchronous_responses_and_events: Streaming asynchronous responses and events
  connection_reuse_when_client_certificates_are_used_for_authentication: Connection reuse when client certificates are used for authentication
  replacement_settings_for_migration_from_web_container_mode_with_tomcat: Replacement settings for migration from web container mode with Tomcat
---

# Migrating from web container mode to PingGateway standalone mode

An PingGateway .war file isn't created or delivered from PingGateway 2024.3. Consider these points when migrating from a .war delivery to a .zip delivery.

## Session replication between PingGateway instances

High-availability of sessions isn't supported by PingGateway in the .zip delivery.

## Streaming asynchronous responses and events

In [ClientHandler](../reference/ClientHandler.html) and [ReverseProxyHandler](../reference/ReverseProxyHandler.html), use only the default mode of `asyncBehavior:non_streaming`; responses are processed when the entity content is entirely available.

If the property is set to `streaming`, the setting is ignored.

## Connection reuse when client certificates are used for authentication

In [ClientHandler](../reference/ClientHandler.html) and [ReverseProxyHandler](../reference/ReverseProxyHandler.html), use only the default mode of `stateTrackingEnabled:true`; when a client certificate is used for authentication, connections can't be reused.

If the property is set to `false`, the setting is ignored.

## Replacement settings for migration from web container mode with Tomcat

| Feature                         | Setting for web container mode with Tomcat                                                                                                                                       | Replacement setting                                                                                                                                                                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Port number                     | Configure in the `Connector` element of `/path/to/tomcat/conf/server.xml`:```xml
<Connector port="8080" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />
``` | Configure the `connectors` property of [admin.json](../reference/AdminHttpApplication.html).                                                                                                                                                                                             |
| HTTPS server-side configuration | Create a keystore, and set up the SSL port in the `Connector` element of `/path/to/tomcat/conf/server.xml`.                                                                      | Create a keystore, set up secrets, and configure secrets stores, ports, and ServerTlsOptions in [admin.json](../reference/AdminHttpApplication.html).For information, refer to [Configure PingGateway for TLS (server-side)](../installation-guide/envvar-sysprop.html#server-side-tls). |
| Session cookie name             | Configure `WEB-INF/web.xml` when you unpack the PingGateway .war file.                                                                                                           | Configure the `session` property of [admin.json](../reference/AdminHttpApplication.html).                                                                                                                                                                                                |
| Access logs                     | Configure with `AccessLogValve`.                                                                                                                                                 | Configure in the Audit framework.For information, refer to [Auditing the PingGateway deployment](../maintenance-guide/auditing.html) and [PingGateway audit framework](../reference/AuditFramework.html).                                                                                |
| JDBC datasource                 | Configure in the `GlobalNamingResources` element of `/path/to/tomcat/conf/server.xml`.                                                                                           | Configure with the JdbcDataSource object.For information, refer to [JdbcDataSource](../reference/JdbcDataSource.html).For an example, refer to [Password replay from a database](../gateway-guide/credentials-database.html).                                                            |
| Environment variables           | Configure in `/path/to/tomcat/bin/setenv.sh`.                                                                                                                                    | Configure in `$HOME/.openig/bin/env.sh`, where `$HOME/.openig` is the instance directory.                                                                                                                                                                                                |
| Jar files                       | Add to to web container classpath; for example `/path/to/tomcat/webapps/ROOT/WEB-INF/lib`.                                                                                       | Add to `$HOME/.openig/extra`, where `$HOME/.openig` is the instance directory.                                                                                                                                                                                                           |

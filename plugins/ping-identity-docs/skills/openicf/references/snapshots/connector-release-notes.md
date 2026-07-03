---
title: .NET RCS release notes
description: Release notes for the .NET Remote Connector Server, covering fixes, connection improvements, and dependency updates by version
component: openicf
page_id: openicf:connector-release-notes:dotnet-server-release
canonical_url: https://docs.pingidentity.com/openicf/connector-release-notes/dotnet-server-release.html
section_ids:
  1_5_7_0_net_rcs: 1.5.7.0 .NET RCS
---

# .NET RCS release notes

Subscribe for automatic updates: [icon: rss-square, set=fa][ICF release notes RSS Feed](./feed.xml)

Refer to [Connector framework release notes](framework.html) for details regarding any changes to the ICF Connector Framework that can affect Remote Connector Server (RCS) behavior.

Downloads are available on [Backstage](https://backstage.forgerock.com/downloads/browse/idm/featured/connectors).

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Unless you have a specific need for the .NET version of the RCS, such as needing the [PowerShell connector toolkit](../connector-reference/powershell.html), we recommend using the [Java RCS](connector-server.html) instead. |

## 1.5.7.0 .NET RCS

* Connection improvements

  * .NET RCS should be able to initiate connection to IDM (OPENICF-731)

  * Client mode should support IDM authentication (OPENICF-1311)

  * Unable to start in client mode when no intervals used (OPENICF-1314)

  * When we attempt to stop in client mode, the connection is re-initiated (OPENICF-1315)

  * ConnectorObject should default the Name to Uid if Name is not present (OPENICF-1318)

  * Add the ability to connect to multiple IDM endpoints (OPENICF-1376)

  * Connection TTL should be in seconds (OPENICF-1626)

  * ConnectionGroup fixes for improved connection handling (OPENICF-1630)

  * Handle failure HTTP status codes when requesting OAuth 2.0 tokens (OPENICF-1631)

  * Fix handshake timing problem (OPENICF-1682)

  * Prevent use of websockets that are about to be closed (OPENICF-1685)

  * Ensure that IDM gets notification that a websocket is about to be closed (OPENICF-1700)

  * Stagger connection starts if webSocketConnections > 1 (OPENICF-1706)

  * SocketClosingSoonException introduces null values that break protobuf3 (OPENICF-2001)

  * Improve stability of RCS WebSocket connection management (OPENICF-2008)

  * If OAuth token endpoint is defined, .NET RCS still tries to use Basic Auth to connect to ID Cloud (OPENICF-2188)

  * Support for HTTP proxy authentication (OPENICF-2197)

  * Closing WebSockets are not handled properly (OPENICF-2217)

* Configuration improvements

  * Separate config properties in the ConnectorServerService.exe.Config (OPENICF-1313)

  * Make Pong interval configurable (OPENICF-1362)

  * Update default properties values (OPENICF-1628)

  * Support for hostId (OPENICF-1512)

  * Align HTTP proxy property names with Java RCS (OPENICF-2204)

* PowerShell connector now included with .NET connector server

  * Embed the PowerShell connector with the .NET connector server (OPENICF-1906)

  * Align PowerShell connector version number with the .NET RCS version (OPENICF-1962)

  * Integrate the PowerShell samples in the project (OPENICF-1970)

  * PowerShell connector: Query might return HTTP 500 when sorting by some properties (OPENICF-2205)

  * AD PowerShell samples should filter \_\_NAME\_\_ as a sort key (OPENICF-2172)

* Dependency updates and cleanup

  * Update and cleanup some dependencies. (OPENICF-1963, OPENICF-1971)

  * Upgrade protocol buffer version and package (OPENICF-1836, OPENICF-2173)

  * Upgrade .NET framework (OPENICF-1707)

  * Fix the Wix project, get rid of legacy dlls (OPENICF-1913)

  * Exception upon start due to a missing dependency (OPENICF-1951)

* General fixes and improvements

  * Sporadic issues managing RCS-hosted connectors through IDM Native Admin Console (OPENICF-2011)

  * Query filter on name attribute with pageSize and pagedResultsCookie returns HTTP 500 (OPENICF-1954)

  * PagedResultsCookie should be set to null if empty when deserialized from protobuf message (OPENICF-1679)

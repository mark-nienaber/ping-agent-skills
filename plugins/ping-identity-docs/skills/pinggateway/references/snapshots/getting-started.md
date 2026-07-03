---
title: Downloading PingGateway
description: Download PingGateway from the Ping Identity software distribution portal
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:download-product
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/download-product.html
revdate: 2025-04-01T17:53:34Z
keywords: ["Install", "Configuration"]
---

# Downloading PingGateway

The .zip file unpacks into a `/path/to/ping-gateway-2026.3.0` directory with the following content:

* `bin`: Start and stop executables

* `classes`: Initially empty; used to install patches from support

* `docker/Dockerfile`: Dockerfile and README to build a PingGateway Docker image

* `legal-notices`: Licenses and copyrights

* `lib`: PingGateway and third-party libraries

  1. Create a local installation directory for PingGateway like `/path/to`.

     |   |                                                                                                                                               |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The installation directory should be a new, empty directory. Installing PingGateway into an existing installation directory can cause errors. |

  2. Download `PingGateway-2026.3.0.zip` from the [Ping Identity Download Center](https://product-downloads.pingidentity.com/), and copy the .zip file to the installation directory:

     ```console
     $ cp PingGateway-2026.3.0.zip /path/to/PingGateway-2026.3.0.zip
     ```

  3. Unzip the file:

     ```console
     $ unzip PingGateway-2026.3.0.zip
     ```

     The directory `/path/to/ping-gateway-2026.3.0` is created.

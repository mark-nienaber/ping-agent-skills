---
title: Downloading PingGateway
description: Download PingGateway from the Ping Identity software distribution portal
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:download-product
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/download-product.html
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
title: Getting started with PingGateway
description: "Get a hands-on introduction to PingGateway: download, install, and configure it on your local computer to see what it can do"
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:preface
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Install", "Configuration"]
page_aliases: ["index.adoc"]
---

# Getting started with PingGateway

Use this guide to get a quick, hands-on look at what PingGateway software can do. You will download, install, and use PingGateway on your local computer. Find more installation options in [Installing PingGateway](../installation-guide/preface.html).

This guide assumes familiarity with the following topics:

* HTTP, including how clients and servers exchange messages, and the role that a reverse proxy (gateway) plays

* JSON, the format for PingGateway configuration files

* Managing services on operating systems and application servers

* Configuring network connections on operating systems

Product names changed when ForgeRock became part of Ping Identity. PingGateway was formerly known as ForgeRock Identity Gateway, for example. Learn more about the name changes from [New names for ForgeRock products](https://support.pingidentity.com/s/article/new-names-for-forgerock-products).

---

---
title: Next steps with PingGateway
description: "Configure PingGateway after installation: edit the base config file, add a default route, switch operating modes, and explore PingGateway Studio"
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:next-steps
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/next-steps.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Install", "Configuration", "Security", "Authentication", "JSON", "User Interface"]
section_ids:
  add-base-conf: Edit the base configuration file
  add-default-route: Add a default route
  dev-mode-switch: Switch from production mode to development mode
  using-studio: Use PingGateway Studio
---

# Next steps with PingGateway

This section describes some basic options to help you with PingGateway. Learn about other installation options in [Installing PingGateway](../installation-guide/preface.html).

## Edit the base configuration file

The entry point for requests to PingGateway is a JSON-encoded configuration file. Its default location is:

* Linux

  `$HOME/.openig/config/config.json`

* Windows

  `%appdata%\OpenIG\config\config.json`

This base configuration file initializes a heap of objects and defines the main handler to receive incoming requests. All applicable configuration objects inherit the configuration defined in this file.

When PingGateway doesn't find a base configuration file at startup, it uses the [default configuration](../reference/GatewayHttpApplication.html#GatewayHttpApplication-default-config). The default configuration loads routes from the following location:

* Linux

  `$HOME/.openig/config/routes`

* Windows

  `%appdata%\OpenIG\config\routes`

When [trusting the sample application](start-sampleapp.html#sampleapp-trust), you added a custom `config.json` file. The default configuration trusts only certificates signed by CAs in the Java truststore, not the sample application self-signed certificate.

You can customize the base configuration file include properties and configuration objects for use throughout PingGateway the base and route configuration files.

Learn more in [GatewayHttpApplication (`config.json` )](../reference/GatewayHttpApplication.html), [Heap objects](../reference/heap-objects.html), and [Router](../reference/Router.html).

After adding or editing the `config.json` file, restart PingGateway to bring the changes into effect:

1. Add or edit the base configuration file at the following location:

   * Linux

     `$HOME/.openig/config/config.json`

   * Windows

     `%appdata%\OpenIG\config\config.json`

   For example, use the following configuration to trust the sample application self-signed certificate:

   ```json
   {
     "handler": {
       "type": "Router",
       "name": "_router",
       "config": {
         "directory": "${openig.configDirectory}/routes"
       }
     },
     "heap": [
       {
         "name": "capture",
         "type": "CaptureDecorator",
         "config": {
           "captureEntity": true,
           "_captureContext": true
         }
       },
       {
         "name": "ClientTlsOptions",
         "type": "ClientTlsOptions",
         "config": {
           "trustManager": {
             "type": "SecretsTrustManager",
             "config": {
               "certificateVerificationSecretId": "sampleapp.cert",
               "secretsProvider": {
                 "type": "FileSystemSecretStore",
                 "config": {
                   "directory": "&{ig.instance.dir}/tls",
                   "format": "PLAIN",
                   "suffix": ".pem",
                   "mappings": [
                     {
                       "secretId": "sampleapp.cert",
                       "format": {
                         "type": "PemPropertyFormat"
                       }
                     }
                   ]
                 }
               }
             }
           }
         }
       },
       {
         "name": "ReverseProxyHandler",
         "type": "ReverseProxyHandler",
         "config": {
           "tls": "ClientTlsOptions"
         }
       }
     ],
     "session": {
       "type": "JwtSessionManager"
     }
   }
   ```

   Source: [config.json](../_attachments/config/config.json)

   Notice the following features of this configuration:

   * The handler defines a main router named `_router`.

     This `_router` routes each incoming request to the first route whose `condition` the request satisfies.

   * The `capture` decorator serves to capture HTTP request and response bodies.

   * The `ReverseProxyHandler` has TLS settings to trust the sample application self-signed certificate.

   * The `session` configuration uses JWT-based sessions.

     Learn more in [PingGateway sessions](../about/about-sessions.html).

2. Stop and start PingGateway.

   On successful startup, the PingGateway log includes a message similar to the following:

   ```none
   ... @system - Reading the configuration from .../config/config.json
   ```

## Add a default route

When there are multiple routes in the PingGateway configuration, they are ordered lexicographically, by route name. For example, `01-static.json` is ordered before `zz-default.json`.

When PingGateway processes a request, the request traverses the routes in the configuration. If the request matches the condition for `01-static.json` it is processed by that route. Otherwise, it passes to the next route in the configuration. If a route has no condition, it can process any request.

A default route is the last route in a configuration to which a request is routed. If a request matches no other route in the configuration, it is processed by the default route.

Add a default route to prevent errors described in [No handler to dispatch to](../maintenance-guide/troubleshooting.html#troubleshoot-no-handler).

1. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/zz-default.json`

   * Windows

     `%appdata%\OpenIG\config\routes\zz-default.json`

   ```json
   {
     "baseURI": "https://app.example.com:8444",
     "handler": "ReverseProxyHandler"
   }
   ```

   Source: [zz-default.json](../_attachments/config/routes/zz-default.json)

   Notice the following features of the route:

   * The route name starts with `zz`, so it is the last route loaded into the configuration.

   * There is no `condition` property, so the route processes all requests.

   * The route calls a ReverseProxyHandler with the default configuration, which proxies the request to the application and returns the response, without changing either the request or the response.

2. Check that the route system log includes a message that the file is loaded into the config:

   ```none
   INFO  o.f.o.handler.router.RouterHandler - Loaded the route with id
   'zz-default' registered with the name 'zz-default'
   ```

## Switch from production mode to development mode

To prevent unwanted changes to the configuration, PingGateway is by default in production mode after installation. For a description of the modes and information about switching between modes, refer to [PingGateway operating modes](../configure/operating-modes.html).

## Use PingGateway Studio

PingGateway Studio is a user interface to help you build and deploy your PingGateway configuration. Learn more in [PingGateway Studio](../studio-guide/preface.html).

---

---
title: Preparing the network for PingGateway
description: Configure the network hosts file to include entries for PingGateway, PingAM, and the sample app
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:prepare-network
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/prepare-network.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2024-07-10T09:15:32Z
keywords: ["Install", "Configuration"]
---

# Preparing the network for PingGateway

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

---

---
title: Protecting an application with PingGateway
description: Configure PingGateway to protect an application using a StaticRequestFilter to intercept requests and log users in with hard-coded credentials
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:using
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/using.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
keywords: ["Install", "Configuration", "Security", "Authentication"]
---

# Protecting an application with PingGateway

This section gives a simple example of how to use PingGateway to protect an application. For many more examples of how to protect applications with PingGateway, refer to the [Gateway guide](../gateway-guide/preface.html#preface).

In the following example, a browser requests access to the sample application, and PingGateway intercepts the request to log the user into the application. The following image shows the flow of data in the example:

![The data flow when PingGateway performs login with hard-coded credentials and a static request filter.](_images/hard-coded-login.svg)

1. The browser sends an HTTP GET request to the HTTP server on `ig.example.com`.

2. PingGateway replaces the HTTP GET request with an HTTP POST login request containing credentials to authenticate.

3. The sample application validates the credentials, and returns the page for the user `demo`.

   If PingGateway did not provide the credentials, or if the sample application couldn't validate the credentials, the sample application returns the login page.

4. PingGateway returns this response to the browser.

Configure PingGateway to log you in to an application

1. Set up PingGateway and the sample application as described in this guide.

2. Add the following route to PingGateway to serve the sample application .css and other static resources:

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

3. Add the following route to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/01-static.json`

   * Windows

     `%appdata%\OpenIG\config\routes\01-static.json`

   ```json
   {
     "handler": {
       "type": "Chain",
       "config": {
         "filters": [
           {
             "type": "StaticRequestFilter",
             "config": {
               "method": "POST",
               "uri": "https://app.example.com:8444/login",
               "form": {
                 "username": [
                   "demo"
                 ],
                 "password": [
                   "Ch4ng31t"
                 ]
               }
             }
           }
         ],
         "handler": "ReverseProxyHandler"
       }
     },
     "condition": "${find(request.uri.path, '^/static')}"
   }
   ```

   Source: [01-static.json](../_attachments/config/routes/01-static.json)

   Notice the following features of the route:

   * The route matches requests to `/static`.

   * The StaticRequestFilter replaces the request with an HTTP POST, specifying the resource to post the request to, and a form to include in the request. The form includes credentials for the username `demo`.

   * The ReverseProxyHandler replays the request to the sample application.

4. Check that the route system log includes a message that the new files are loaded into the config:

   ```none
   INFO  o.f.o.handler.router.RouterHandler - Loaded the route with id '00-static-resources' registered with the name '00-static-resources'
   INFO  o.f.o.handler.router.RouterHandler - Loaded the route with id '01-static' registered with the name '01-static'
   ```

5. Go to <http://ig.example.com:8080/static>.

   You are directed to the sample application, and logged in automatically with the username `demo`.

---

---
title: Starting and stopping PingGateway
description: Start and stop PingGateway using default settings, configuration directories, and the stop script for Linux and Windows.
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:start-stop
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/start-stop.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-04-01T17:53:34Z
section_ids:
  starting-default: Start PingGateway with default settings
  stopping: Stop PingGateway
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

## Stop PingGateway

Use the `stop.sh` or `stop.bat` script to stop an instance of PingGateway, specifying the instance directory as an argument.

If the instance directory isn't specified, PingGateway uses the default instance directory as in these examples:

* Linux

  `/path/to/ping-gateway-2026.6.0/bin/stop.sh $HOME/.openig`

* Windows

  `C:\path\to\ping-gateway-2026.6.0\bin\stop.bat %appdata%\OpenIG`

---

---
title: Using the sample application
description: Download, start, stop, and configure the sample application mockup web app used for testing PingGateway configurations
component: pinggateway
version: 2026
page_id: pinggateway:getting-started:start-sampleapp
canonical_url: https://docs.pingidentity.com/pinggateway/2026/getting-started/start-sampleapp.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-15T18:45:22Z
keywords: ["Install", "Configuration"]
section_ids:
  start-sampleapp-download: Download the sample application
  start-sampleapp-start: Start the sample application
  sampleapp-trust: Trust the sample application
  start-sampleapp-stop: Stop the sample application
  start-sampleapp-conf: Configuration options
---

# Using the sample application

Ping Identity provides a mockup web application for testing PingGateway configurations. The sample application is used in the examples throughout the PingGateway documentation.

## Download the sample application

1. Download `PingGateway-sample-application-2026.6.0.jar`, from the [Ping Identity Download Center](https://product-downloads.pingidentity.com/).

## Start the sample application

1. Start the sample application:

   ```console
   $ java -jar PingGateway-sample-application-2026.6.0.jar
   ```

   Output

   ```
   ...
   [...] [INFO   ] Press Ctrl+C to stop the server.
   ```

   (Optional) port numbers

   By default, this server listens for HTTP on port 8081 and for HTTPS on port 8444. If one or both of those ports aren't free, specify other ports:

   ```console
   $ java -jar PingGateway-sample-application-2026.6.0.jar 8888 8889
   ```

   (Optional) OpenTelemetry support

   By default, OpenTelemetry support is disabled in the sample application. To enable it, set `OTEL_SDK_DISABLED=false` when starting the sample application:

   ```console
   $ OTEL_SDK_DISABLED=false java -jar PingGateway-sample-application-2026.6.0.jar
   ```

   The tracing configuration for the sample application uses automatic configuration. For example, to enable OpenTelemetry support and publish to a remote service:

   ```console
   $ OTEL_SDK_DISABLED=false \
   OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://collector.example.com/v1/traces \
   java -jar PingGateway-sample-application-2026.6.0.jar
   ```

   Learn more about configuration options in the OpenTelemetry documentation on [automatic configuration](https://opentelemetry.io/docs/languages/java/instrumentation/#automatic-configuration). The sample application supports only `http/protobuf` for the exporter protocol.

2. Check that the sample application responds to requests in one of the following ways:

   * In your browser's privacy or incognito mode, go to <https://app.example.com:8444/home> to access the home page of the sample application and accept the self-signed certificate.

     The browser displays information about the request.

   * In your browser's privacy or incognito mode, go to <https://app.example.com:8444/login> to access the login page of the sample application, accept the self-signed certificate, and sign on with username `demo` and password `Ch4ng31t`.

     The browser displays the username and information about the request.

## Trust the sample application

The sample application uses a self-signed TLS certificate for HTTPS. Browsers and HTTP clients like PingGateway won't connect as they don't trust self-signed certificates. You must explicitly trust the sample application certificate.

In the browser, this means accepting the risk and adding an exception for the self-signed certificate. In client applications like PingGateway, this means getting the sample application certificate and configuring the client to trust it:

1. Get the sample application certificate in one of the following ways:

   * Download the [sampleapp.cert.pem](../_attachments/tls/sampleapp.cert.pem) file and save it in a `tls` folder.

   * Extract it from the `PingGateway-sample-application-2026.6.0.jar` file:

     ```console
     $ jar --verbose --extract --file PingGateway-sample-application-2026.6.0.jar tls/sampleapp.cert.pem
     ```

     The command extracts the certificate to `tls/sampleapp.cert.pem` in the current directory.

2. [Start the sample application](#start-sampleapp-start) and check the certificate's trusted for an HTTPS request:

   ```console
   $ curl --head --cacert tls/sampleapp.cert.pem --url https://app.example.com:8444/home
   ```

   Output

   ```
   HTTP/2 200
   ```

3. Move or copy the `tls` directory containing the certificate under the PingGateway directory:

   * Linux

     `$HOME/.openig/tls/sampleapp.cert.pem`

   * Windows

     `%appdata%\OpenIG\tls\sampleapp.cert.pem`

4. Configure PingGateway to trust the sample application certificate when acting as a reverse proxy.

   Add the following as `config.json` in the PingGateway configuration directory:

   * Linux

     `$HOME/.openig/config/config.json`

   * Windows

     `%appdata%\OpenIG\config\config.json`

   ```json
   {
     "handler": {
       "type": "Router",
       "name": "_router",
       "config": {
         "directory": "${openig.configDirectory}/routes"
       }
     },
     "heap": [
       {
         "name": "capture",
         "type": "CaptureDecorator",
         "config": {
           "captureEntity": true,
           "_captureContext": true
         }
       },
       {
         "name": "ClientTlsOptions",
         "type": "ClientTlsOptions",
         "config": {
           "trustManager": {
             "type": "SecretsTrustManager",
             "config": {
               "certificateVerificationSecretId": "sampleapp.cert",
               "secretsProvider": {
                 "type": "FileSystemSecretStore",
                 "config": {
                   "directory": "&{ig.instance.dir}/tls",
                   "format": "PLAIN",
                   "suffix": ".pem",
                   "mappings": [
                     {
                       "secretId": "sampleapp.cert",
                       "format": {
                         "type": "PemPropertyFormat"
                       }
                     }
                   ]
                 }
               }
             }
           }
         }
       },
       {
         "name": "ReverseProxyHandler",
         "type": "ReverseProxyHandler",
         "config": {
           "tls": "ClientTlsOptions"
         }
       }
     ],
     "session": {
       "type": "JwtSessionManager"
     }
   }
   ```

   Source: [config.json](../_attachments/config/config.json)

5. Restart PingGateway to pick up the change.

6. Add a route to PingGateway to serve the sample application static resources that don't need protection:

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

Optionally check PingGateway trusts the sample application:

1. Add a route for the sample application to PingGateway:

   * Linux

     `$HOME/.openig/config/routes/00-home.json`

   * Windows

     `%appdata%\OpenIG\config\routes\00-home.json`

   ```json
   {
     "name": "00-home",
     "condition": "${find(request.uri.path, '^/home')}",
     "baseURI": "https://app.example.com:8444",
     "handler": "ReverseProxyHandler"
   }
   ```

   Source: [00-home.json](../_attachments/config/routes/00-home.json)

2. Go to <https://ig.example.com:8080/home> to access the home page of the sample application.

   The browser displays information about the request.

## Stop the sample application

In the terminal where the sample application is running, enter CTRL+C to stop the sample application.

## Configuration options

To view the command-line options for the sample application, start it with the `-h` option:

```console
$ java -jar PingGateway-sample-application-2026.6.0.jar -h
```

Output

```
Usage: <main class> [options]
  Options:
    --http
      The HTTP port number.
      Default: 8081
    --https
      The HTTPS port number.
      Default: 8444
    --session
      The session timeout in seconds.
      Default: 60
    --am-discovery-url
      The AM URL base for OpenID Provider Configuration.
      Default: http://openam.example.com:8088/openam/oauth2
    --latency
      The simulated request latency in seconds.
      Default: 2
    --latency-requests-frequency
      The frequency at which latency is applied to requests.
      Default: 1
    --latency-requests-chunks-count
      The number of chunks into which the request payload will be divided,
      with latency applied to each chunk.
      Default: 1
    -h, --help
      Default: false
```
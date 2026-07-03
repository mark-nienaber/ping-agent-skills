---
title: Adding PingGateway configuration to a Docker image
description: Add PingGateway configuration to a Docker image using a mutable mounted configuration or an immutable baked-in configuration
component: pinggateway
version: 2026
page_id: pinggateway:devops-guide:docker-add-conf
canonical_url: https://docs.pingidentity.com/pinggateway/2026/devops-guide/docker-add-conf.html
revdate: 2025-04-01T17:53:34Z
keywords: ["Deployment", "Configuration", "Devops", "Docker"]
section_ids:
  docker-add-conf-mutable: Run an image with a mutable configuration
  docker-add-conf-immutable: Run an image with an immutable configuration
---

# Adding PingGateway configuration to a Docker image

The following sections describe how to add configuration to your Docker image. Before working through this section, complete the procedures in [Building and running a PingGateway Docker image](docker-basic.html).

## Run an image with a mutable configuration

This section describes how to add a basic route to your local PingGateway configuration folder, and mount the configuration to the Docker container.

If you change your configuration in a way that doesn't require PingGateway to restart, you see the change in your running Docker image without restarting it or rebuilding it. For information changes that require restart, refer to [When to restart PingGateway after changing the configuration](../configure/configure.html#restart-required).

Use this procedure to manage configuration externally to the Docker image. For example, use it when developing routes.

1. Add the following route to your local PingGateway configuration as `$HOME/.openig/config/routes/hello.json`:

   ```json
   {
     "name": "hello",
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
     "condition": "${find(request.uri.path, '^/hello')}"
   }
   ```

   Source: [hello.json](../_attachments/config/routes/hello.json)

   The configuration contains a static response handler to return a "Hello world!" statement when the URI of a request finishes with `/hello`.

2. Run the Docker image, using the option to mount the local PingGateway configuration directory:

   ```console
   $ docker run -p 8080:8080 -v $HOME/.openig:/var/gateway/ ig-image
   ```

3. Go to <http://localhost:8080/hello> to access the route in the mounted configuration.

   The "Hello world!" statement is displayed.

4. Edit `hello.json` to change the "Hello world!" statement, and save the file.

   Go again to <http://localhost:8080/hello> to see that the message changed without changing your Docker image.

## Run an image with an immutable configuration

This section describes how to add a basic route to your local PingGateway configuration folder, copy it into a new Docker image, and run that Docker image.

Unlike the previous example, the Docker image is immutable. If you change your configuration locally, the Docker image is not changed.

Use this procedure to manage configuration within the Docker image. For example, use it when you want to deploy the same configuration multiple times.

1. Add the following route to your local PingGateway configuration as `$HOME/.openig/config/routes/hello.json`:

   ```json
   {
     "name": "hello",
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
     "condition": "${find(request.uri.path, '^/hello')}"
   }
   ```

   Source: Source: [hello.json](../_attachments/config/routes/hello.json)

   The configuration contains a static response handler to return a "Hello world!" statement when the URI of a request finishes with `/hello`.

2. Add the following file to your local PingGateway configuration as `$HOME/.openig/Dockerfile`, where `$HOME/.openig` is the instance directory:

   ```dockerfile
   FROM ig-image
   COPY config/routes/hello.json "$IG_INSTANCE_DIR"/config/routes/hello.json
   ```

   The Dockerfile copies `hello.json` into the Docker image. The `$IG_INSTANCE_DIR` environment variable is defined in the PingGateway base image.

3. Build the Docker image:

   ```console
   $ docker build . -t ig-custom
   ```

   Output

   ```
   Sending build context to Docker daemon
    Step 1/2 : FROM ig-image
    Step 2/2 : COPY config/routes/hello.json "$IG_INSTANCE_DIR"/config/routes/hello.json
    Successfully tagged ig-custom:latest
   ```

4. Make sure the Docker image is available:

   ```console
   $ docker image list
   ```

   Output

   ```
   REPOSITORY               TAG                IMAGE ID
   ig-custom                image_tag          51b...3b7
   gcr.io/forgerock-io/ig   image_tag          404...a2b
   ```

5. Run the Docker image on port `8080`:

   ```console
   $ docker run -p 8080:8080 ig-custom
   ```

6. Go to <http://localhost:8080/hello>. The "Hello world!" statement is displayed.

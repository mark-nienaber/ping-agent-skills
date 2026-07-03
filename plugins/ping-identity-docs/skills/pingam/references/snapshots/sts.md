---
title: Configure STS instances
description: Configure Security Token Service instances to perform token transformations and expose REST endpoints for SAML2 and OIDC token encryption or signing
component: pingam
version: 8.1
page_id: pingam:sts:sts-using-console
canonical_url: https://docs.pingidentity.com/pingam/8.1/sts/sts-using-console.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security Token Service (STS)", "Rest"]
page_aliases: ["sts-guide:sts-using-console.adoc"]
section_ids:
  sts-rest-console: Configure an STS instance in the UI
  sts-rest-rest: Configure an STS instance over REST
---

# Configure STS instances

You configure Security Token Service (STS) *instances* to perform one or more token transformations. Each instance provides configuration details about how SAML 2.0 and/or OIDC output tokens are encrypted or signed. Deployments that support multiple SAML 2.0 and/or OIDC service providers require multiple STS instances.

When you publish an STS instance, you create an STS instance with a given configuration. You can publish instances using the AM admin UI or the REST API.

When you publish an STS instance, AM exposes a REST endpoint for accessing the instance, and the instance is immediately available for use to callers.

## Configure an STS instance in the UI

To configure an STS instance using the AM admin UI, go to Realms > *realm name* > STS, and click Add Rest STS.

Read [STS configuration properties](sts-configure-rest-properties.html) for detailed information about STS configuration properties.

## Configure an STS instance over REST

To publish an STS instance programmatically, use the Publish service. This service is a collection of endpoints you can use to publish instances instead of accessing the AM admin UI.

Learn more in [The Publish service](sts-publish-service.html).

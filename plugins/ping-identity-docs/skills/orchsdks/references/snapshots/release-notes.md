---
title: Deprecated
description: Deprecated. Track functionality deprecated in the Orchestration SDKs and likely to be removed in a future release
component: orchsdks
page_id: orchsdks:release-notes:deprecations/deprecations
canonical_url: https://developer.pingidentity.com/orchsdks/release-notes/deprecations/deprecations.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 25 May 2023 13:44:17 +0100
section_ids:
  dep-JS400: Deprecated since Orchestration SDK for JavaScript 4.0
---

# Deprecated

The functionality listed here is deprecated, and likely to be removed in a future release.

## Deprecated since Orchestration SDK for JavaScript 4.0

* JavaScript `support` configuration property

  The `support` configuration property has been removed in Orchestration SDK for JavaScript 4.0.

  This property could be used to change the way the SDK would make requests to the `/authorize` endpoint in OAuth 2.0 interactions.

  If you configured the SDK to use the `modern` option, you might notice that your app uses the default iframe method to call the `/authorize` endpoint if you upgrade to this version of the SDK. This technical difference will not negatively impact your app's user-experience or require any code changes.

  If you were using the `legacy` option or not providing a value for the `support` property at all, you will likely obtain improvements in latency and a reduction of errors in the logs when upgrading to Orchestration SDK for JavaScript 4.0.

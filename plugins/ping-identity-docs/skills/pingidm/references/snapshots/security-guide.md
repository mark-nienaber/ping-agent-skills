---
title: Adjust log levels
description: Set PingIDM log levels to INFO in production to capture diagnostic information without exposing unnecessary details
component: pingidm
version: 8.1
page_id: pingidm:security-guide:security-adjust-log-levels
canonical_url: https://docs.pingidentity.com/pingidm/8.1/security-guide/security-adjust-log-levels.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Logs"]
---

# Adjust log levels

In production, set log levels to `INFO` to ensure that you capture enough information to help diagnose issues, but do not expose unnecessary information. For more information, refer to [Server logs](../monitoring-guide/server-logs.html).

At startup and shutdown, `INFO` can produce many messages. During stable operation, `INFO` generally results in log messages only when coarse-grain operations such as scheduled reconciliation start or stop.

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The default IDM log formatter encodes all control characters (such as newline characters) using URL-encoding, to protect against log forgery. For more information, refer to [Server logs](../monitoring-guide/server-logs.html). |

---
title: Audit logging
description: Understand how PingAM captures and manages audit logs for security, compliance, and troubleshooting across multiple topics and event handlers
component: pingam
version: 8.1
page_id: pingam:monitoring:audit-logging
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Compliance"]
page_aliases: ["security-guide:audit-logs.adoc", "security-guide:audit-logging.adoc", "monitoring-guide:audit-logging.adoc"]
section_ids:
  log_messages: Log messages
  audit-log-topics: Audit topics
  log-mgmt-agents: Web and Java agent audit events
---

# Audit logging

AM's common REST-based audit logging service captures key auditing events, critical for system security, troubleshooting, and regulatory compliance.

Audit logs gather operational information about events that occur within an AM deployment. They track processes and security data, such as authentication mechanisms, system access, user and administrator activity, error messages, and configuration changes.

The audit logging service provides a versatile and rich feature set:

* Global and realm-based log configuration

  You can configure audit logging globally, which ensures that all realms inherit your global log settings. You can also configure audit logging by realm, which allows you to set different log settings for each realm.

* Audit event handlers

  The audit logging service supports a variety of audit event handlers that allow you to write logs to different types of datastores. You can find a list of event handlers available in AM in [Configuring audit event handlers](implementing-audit.html#configuring-audit-event-handlers).

* Audit event buffering

  By default, AM writes each log message separately as they are generated. AM supports message buffering, a type of batch processing, that stores log messages in memory and flushes the buffer after a preconfigured time interval or after a certain number of log messages reaches the configured threshold value.

* Tamper-evident logging

  For the CSV audit event handler, you can digitally sign audits to enable the detection of tampering.

* Log rotation and retention policies

  AM rotates JSON and CSV audit logs when it reaches a specified maximum size. You can also configure a time-based rotation policy, which disables the max-size rotation policy and implements log rotation based on a preconfigured time sequence. AM also provides the option to disable log rotation completely for these file types. AM doesn't support external log rotation for JSON and CSV audit logs.

  For Syslog, JDBC, and JMS handlers, AM doesn't control log rotation and retention as they are handled by each respective service.

* Allowlist and denylist support

  The audit logging service supports allowlist and denylist-filtering to show or hide sensitive values or fields in logs, such as HTTP headers, query parameters, cookies, profile attributes, or the entire field value.

* Reverse DNS lookup

  The audit logging service supports a reverse DNS lookup feature for network troubleshooting purposes. Reverse DNS lookup is disabled by default because it reduces operation throughput.

## Log messages

AM writes log messages generated from audit events triggered by its instances, web or Java agents, and connected Ping Advanced Identity Software implementations.

The audit logging service uses a structured message format that adheres to a consistent log structure across the Ping Advanced Identity Software. This common structure allows correlation between log messages of the different platform components if the transaction IDs are *trusted*. Find more information in [Trust transaction headers](implementing-audit.html#configuring-trusttransactionheader-system-property).

|   |                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although the PingDS JSON logger is enabled by default, transaction IDs are not trusted by default. You must set `trust-transaction-ids:true` to correlate DS log messages with AM log messages. For more information, see [Log LDAP Access to Files > JSON Format](https://docs.pingidentity.com/pingds/8.1/logging-guide/ldap-access.html#log-common-audit-ldap-json) in the DS documentation. |

## Audit topics

AM assigns log messages to four different audit topics. A *topic* is a category of audit log event that has a one-to-one mapping with a schema type.

The following table shows the different event topics and associated audit log files for AM's default audit logging configuration, which uses a JSON audit event handler:

**Audit log topics**

| Event topic    | File name                   | Description                                                                                                                                                                                                                                                                     |
| -------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access         | `access.audit.json`         | Captures who, what, when, and output for every access request.                                                                                                                                                                                                                  |
| Activity       | `activity.audit.json`       | Captures state changes to objects that have been created, updated, or deleted by end users (that is, non-administrators). Session, user profile, and device profile changes are captured in the logs.                                                                           |
| Authentication | `authentication.audit.json` | Captures when and how a subject is authenticated and related events.                                                                                                                                                                                                            |
| Configuration  | `config.audit.json`         | Captures configuration changes to the product with a timestamp and by whom. Note that the `userId` indicating the subject who made the configuration change is not captured in the `config.audit.json` but can be tracked using the `transactionId` in the `access.audit.json`. |

## Web and Java agent audit events

Web and Java agents log audit events for security, troubleshooting, and regulatory compliance. You can store web or Java agent audit event logs in the following ways:

* **Remotely**. Log audit events to the audit event handler configured in the AM realm.

* **Locally**. Log audit events to a file in the web or Java agent installation directory.

Learn more in the [Web Agents Maintenance Guide](https://docs.pingidentity.com/web-agents/2025.3/maintenance-guide/auditing.html) and the [Java Agents Maintenance Guide](https://docs.pingidentity.com/java-agents/2025.3/maintenance-guide/auditing.html).

---
title: Observability and logging
description: Our Support team and the Site Reliability Engineers proactively monitor your infrastructure and deployments and attempt to address issues before they become problems. If outages occur, we'll notify you using standard support methods.
component: pgic
page_id: pgic::pgic_observability
canonical_url: http://docs.pingidentity.com/pgic/pgic_observability.html
---

# Observability and logging

Our Support team and the Site Reliability Engineers proactively monitor your infrastructure and deployments and attempt to address issues before they become problems. If outages occur, we'll notify you using standard support methods.

You're responsible for monitoring your Ping Identity applications and configurations, but we will stream log files to you, which will help you identify, monitor, and quickly resolve any issues you might encounter.

Although the on-premise products you might be accustomed to using allow you to customize your log files, the log files in Ping Government Identity Cloud are limited.

Items to keep in mind regarding Ping Government Identity Cloud observability and logging include:

* Logs are shipped from the kubernetes cluster to the SIEM in AWS GovCloud and an S3 bucket. You will have access to this S3 bucket to set up or ingest to their Splunk deployment in the native Ping Identity formats.

* Ping Government Identity Cloud runs in ephemeral containers and all logs are shipped off immediately to the SIEM processor. There are queues both on the ephemeral containers and in the SIEM pipeline in case there are problems with ingestion. Log files aren't written to traditional virtual machines.

* Only the default product logs are available, and log fields can't be customized.

* Per FedRamp guidelines, OpenSearch is configured to move indices into a cold state after 90 days and delete them after 1 year. This timeframe can be adjusted, if necessary. You are responsible for reading the log content from the S3 buckets if you're required to keep them longer than 1 year.

* Debugging is turned off for the Production and Staging environments, but can be turned on for brief periods of time for troubleshooting purposes.

* If integration kits are used with Ping Government Identity Cloud, they must be provided by Ping Identity product or engineering teams. Kits created by customers or other third parties are not allowed.

* Parsed log files are available on a best-effort basis in OpenSearch for 30 days, which is subject to change.

* S3 Log Replay is an internal tool used only by internal teams for troubleshooting purposes.

* Customer-requested log replay isn't available for either OpenSearch or customer endpoints.

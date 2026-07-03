---
title: Configuring logging
description: Instructions for configuring logging for PingCentral.
component: pingcentral
version: 3.1.1
page_id: pingcentral:pingcentral_for_iam_administrators:pingcentral_installing_configuring/pingcentral_logging
canonical_url: https://docs.pingidentity.com/pingcentral/3.1.1/pingcentral_for_iam_administrators/pingcentral_installing_configuring/pingcentral_logging.html
revdate: October 9, 2025
section_ids:
  steps: Steps
---

# Configuring logging

The log file serves as a record of events that occurred within the system and is often used for troubleshooting purposes. This section explains how to access the log file, interpret the entries within it, and change the level of detail the log file captures.

## Steps

1. Access the PingCentral log file from the following location: `/<pingcentral_install>/log/application.log`.

   The level of detail that the log file contains depends on how the logging level is set. Logging levels are a means of categorizing the entries in your log file by severity, and are described in the following table. Detailed log files require more system resources, so PingCentral only records errors, warnings, and some information events by default.

   | Logging level | Description                                                                                                                                                                |
   | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | ERROR         | Indicates a failure within the application occurred.                                                                                                                       |
   | WARNING       | Indicates the system detected an unusual situation and errors might occur.                                                                                                 |
   | INFO          | Provide basic information about activities that occurred. For example, a service was started and stopped, or a new user was added to the application.                      |
   | DEBUG         | Provides additional detail regarding the events that occurred, and is often used to diagnose and troubleshoot reported issues.                                             |
   | TRACE         | Provides even more detailed information than the Debug level regarding the application's behavior. This logging level is not used often and can affect system performance. |

2. Changing the logging level to have the system record additional details can help with troubleshooting. To change the logging level:

   1. Open the configuration file at `/<pingcentral_install>/conf/log4j2.xml`.

   2. Scroll down, locate the Logger line item shown below, and change the logging level within the quotations. The` DEBUG` logging level provides enough information to troubleshoot most issues.

      ```
      <Logger name="com.pingidentity" level="INFO" additivity="false" includeLocation="false">
      	<!--<AppenderRef ref="console"/>-->
      	<AppenderRef ref="file"/>
      </Logger>
      ```

   3. Save and close the file and repeat the task you performed when the error occurred.

   4. For optimal system performance, open the `log4j2.xml` file again and change the logging level back to `INFO`.

   5. Access the `application.log` file again and review the information that was recorded in `DEBUG` mode. If you are working with a technical support team to troubleshoot an issue, you can send them the log file that recorded your activities.

---
title: Additional logging
description: "The following logging options can be updated in log4j2.xml after the section AsyncLogger name=\"com.pingidentity.provisioner\". This will provide additional logging details in the provisioner.log for troubleshooting purposes."
component: box
page_id: box:troubleshooting:pf_box_connector_additional_logging
canonical_url: https://docs.pingidentity.com/integrations/box/troubleshooting/pf_box_connector_additional_logging.html
revdate: June 27, 2024
---

# Additional logging

The following logging options can be updated in `log4j2.xml` after the section `AsyncLogger name="com.pingidentity.provisioner"`. This will provide additional logging details in the `provisioner.log` for troubleshooting purposes.

Learn more about log4j2 in [Log4j 2 logging service and configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_log4j_2_loggin_service_and_config.html). You can also learn more from Ping Identity [Support & Community](https://support.pingidentity.com/s/).

```
<AsyncLogger name="com.pingidentity.integrations"
                     level="INFO" additivity="false" includeLocation="false">
            <appender-ref ref="ProvisionerLog" />
            <!--
                <appender-ref ref="CONSOLE-PROVISIONER" />
                <appender-ref ref="ProvisionerLogToOracleDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToSQLServerDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToMySQLDB-FAILOVER"/>
            -->
        </AsyncLogger>

<AsyncLogger name="com.pingidentity.saas"
                     level="INFO" additivity="false" includeLocation="false">
            <appender-ref ref="ProvisionerLog" />
            <!--
                <appender-ref ref="CONSOLE-PROVISIONER" />
                <appender-ref ref="ProvisionerLogToOracleDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToSQLServerDB-FAILOVER"/>
                <appender-ref ref="ProvisionerLogToMySQLDB-FAILOVER"/>
            -->
</AsyncLogger>
```

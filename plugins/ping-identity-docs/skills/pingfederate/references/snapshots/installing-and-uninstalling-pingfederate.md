---
title: Compatible database drivers
description: PingFederate is compatible with the following vendor-specific Java database connectivity (JDBC) drivers.
component: pingfederate
version: 13.1
page_id: pingfederate:installing_and_uninstalling_pingfederate:pf_compatible_database_drivers
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/installing_and_uninstalling_pingfederate/pf_compatible_database_drivers.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 4, 2026
---

# Compatible database drivers

PingFederate is compatible with the following vendor-specific Java database connectivity (JDBC) *(tooltip: \<div class="paragraph">
\<p>A Java API that allows Java programs to interact with databases.\</p>
\</div>)* drivers.

| Database server                                                      | Driver information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Aurora MySQL 3.12.0 (compatible with MySQL 8.0.44)            | * Driver version information

  aws-advanced-jdbc-wrapper version 2.6.6 with mysql-connector-j version 9.5.0&#xA;&#xA;If you use the AWS wrapper driver, you must deploy the original driver and the wrapper driver together. Learn more in Using the AWS Advanced Wrapper in the AWS documentation.* Driver class

  `software.amazon.jdbc.Driver`

* JDBC URL

  `jdbc:mysql://databaseservername/databasename`

* Database location

  Regional

* Database features

  One writer and multiple readers	If you're using Aurora's high-availability features, the AWS JDBC Driver for MySQL client driver may be used instead of the MySQL Connector/J driver.                       |
| Amazon Aurora PostgreSQL (compatible with PostgreSQL 16.13 and 17.9) | - Driver version information

  aws-advanced-jdbc-wrapper version 2.6.6 with postresql versions 42.7.5&#xA;&#xA;If you use the AWS wrapper driver, you must deploy the original driver and the wrapper driver together. Learn more in Using the AWS Advanced Wrapper in the AWS documentation.- Driver class

  `software.amazon.jdbc.Driver`

- JDBC URL

  `jdbc:postgresql://databaseservername/databasename`

- Database features

  One writer and multiple readers                                                                                                                                                                                                               |
| Microsoft SQL Server 2016 SP2, 2017, 2019, and 2022                  | * Driver version information

  sqljdbc version 13.4.0

* Driver class

  `com.microsoft.sqlserver.jdbc.SQLServerDriver`

* JDBC URL

  `jdbc:sqlserver://databaseservername;databaseName=databasename`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Microsoft Azure SQL Managed Instance                                 | - Driver version information

  sqljdbc version 13.5.0

- Driver class

  `com.microsoft.sqlserver.jdbc.SQLServerDriver`

- JDBC URL

  `jdbc:sqlserver://databaseservername;databaseName=databasename`&#xA;&#xA;PingFederate supports additional authentication methods which can be specified in the JDBC URL. For example, jdbc:sqlserver://databaseservername;databaseName=databasenameauthentication=ActiveDirectoryManagedIdentity&#xA;&#xA;You need to add extra dependencies to PingFederate to use these methods. These dependencies vary according to the JDBC driver and the authentication method. Learn more in Client setup requirements in the Microsoft documentation. |
| Oracle Database 12c Release 2 and 19c                                | * Driver version information

  ojdbc11 version 23.26.2.0.0

* Driver class

  `oracle.jdbc.OracleDriver`

* JDBC URL

  `jdbc:oracle:thin:@databaseservername/servicename`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Oracle MySQL 8.0 and 8.4                                             | - Driver version information

  mysql-connector-j version 9.7.0&#xA;&#xA;Don't use MySQL driver version 9.3, as it isn't compatible with PingFederate.- Driver class

  `com.mysql.cj.jdbc.Driver`

- JDBC URL

  `jdbc:mysql://databaseservername/databasename`                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PostgreSQL 13.4, 16.4, 17.0, and 18.0                                | * Driver version information

  postgresql version 42.7.11

* Driver class

  `org.postgresql.Driver`

* JDBC URL

  `jdbc:postgresql://databaseservername/databasename`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

For additional information about these drivers, contact the respective vendors.

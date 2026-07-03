---
title: Accessing Log Files
description: Ping Autonomous Identity provides different log files to monitor or troubleshoot your system.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-access-logs
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-access-logs.html
section_ids:
  getting_docker_container_information: Getting Docker Container Information
  getting_cassandra_logs: Getting Cassandra Logs
  other_useful_cassandra_monitoring_tools_and_files: Other Useful Cassandra Monitoring Tools and Files
  apache_spark_logs: Apache Spark Logs
---

# Accessing Log Files

Ping Autonomous Identity provides different log files to monitor or troubleshoot your system.

## Getting Docker Container Information

1. On the target node, get system wide information about the Docker deployment. The information shows the number of containers running, paused, and stopped containers as well as other information about the deployment.

   ```
   $ docker info
   ```

2. If you want to get debug information, use the `-D` option. The option specifies that all docker commands will output additional debug information.

   ```
   $ docker -D info
   ```

3. Get information on all of your containers on your system.

   ```
   $ docker ps -a
   ```

4. Get information on the docker images on your system.

   ```
   $ docker images
   ```

5. Get docker service information on your system.

   ```
   $ docker service ls
   ```

6. Get docker the logs for a service.

   ```
   $ docker service logs <service-name>
   ```

   For example, to access the nginx service logs:

   ```
   $ docker service logs nginx_nginx
   ```

   Other useful arguments:

   * `--details`. Show extra details.

   * `--follow, -f`. Follow log output. The command will stream new output from STDOUT and STDERR.

   * `--no-trunc`. Do not truncate output.

   * `--tail {n|all}`. Show the number of lines from the end of log files, where `n` is the number of lines or `all` for all lines.

   * `--timestamps, -t`. Show timestamps.

## Getting Cassandra Logs

The Apache Cassandra output log is kicked off at startup. Ping Autonomous Identity pipes the output to a log file in the directory, `/opt/autoid/`.

1. On the target node, get the log file for the Cassandra install.

   ```
   $ cat /opt/autoid/cassandra/installcassandra.log
   ```

2. Get startup information. Cassandra writes to `cassandra.out` at startup.

   ```
   $ cat /opt/autoid/cassandra.out
   ```

3. Get the general Cassandra log file.

   ```
   $ cat /opt/autoid/apache-cassandra-3.11.2/logs/system.log
   ```

   By default, the log level is set to `INFO`. You can change the log level by editing the `/opt/autoid/apache-cassandra-3.11.2/conf/logback.xml` file. After any edits, the change will take effect immediately. No restart is necessary. The log levels from most to least verbose are as follows:

   * `TRACE`

   * `DEBUG`

   * `INFO`

   * `WARN`

   * `ERROR`

   * `FATAL`

4. Get the JVM garbage collector logs.

   ```
   $ cat /opt/autoid/apache-cassandra-3.11.2/logs/gc.log.<number>.current
   ```

   For example:

   ```
   $ cat /opt/autoid/apache-cassandra-3.11.2/logs/gc.log.0.current
   ```

   The output is configured in the `/opt/autoid/apache-cassandra-3.11.2/conf/cassandra-env.sh` file. Add the following JVM properties to enable them:

   * `JVM_OPTS="$JVM_OPTS -XX:+PrintGCDetails"`

   * `JVM_OPTS="$JVM_OPTS -XX:+PrintGCDateStamps"`

   * `JVM_OPTS="$JVM_OPTS -XX:+PrintHeapAtGC"`

   * `JVM_OPTS="$JVM_OPTS -XX:+PrintGCApplicationStoppedTime"`

5. Get the debug log.

   ```
   $ cat /opt/autoid/apache-cassandra-3.11.2/logs/debug.log
   ```

## Other Useful Cassandra Monitoring Tools and Files

Apache Cassandra has other useful monitoring tools that you can use to observe or diagnose and issue. To access the complete list of options, refer to the Apache Cassandra documentation.

1. View statistics for a cluster, such as IP address, load, number of tokens,

   ```
   $ /opt/autoid/apache-cassandra-3.11.2/bin/nodetool status
   ```

2. View statistics for a node, such as uptime, load, key cache hit, rate, and other information.

   ```
   $ /opt/autoid/apache-cassandra-3.11.2/bin/nodetool info
   ```

3. View the Cassandra configuration file to determine how properties are pre-set.

   ```
   $ cat /opt/autoid/apache-cassandra-3.11.2/conf/cassandra.yaml
   ```

## Apache Spark Logs

Apache Spark provides several ways to monitor the server after an analytics run.

1. To get an overall status of the Spark server, point your browser to `http://<spark-master-ip>:8080`.

2. Print the logging message sent to the output file during an analytics run.

   ```
   $ cat /opt/autoid/spark/spark-2.4.4-bin-hadoop2.7/logs/<file-name>
   ```

   For example:

   ```
   $ cat /opt/autoid/spark/spark-2.4.4-bin-hadoop2.7/logs/spark-org.apache.spark.deploy.master.Master-1-autonomous-id-test.out
   ```

3. Print the data logs that were written during an analytics run.

   ```
   $ cat /data/log/files/<filename>
   ```

   For example:

   ```
   $ cat /data/log/files/f6c0870e-5782-441e-b145-b0e662f05f79.log
   ```

---

---
title: Admin user tasks
description: The Admin user functionality is similar to that of a system administration superuser. Admin users have the access rights to company-wide entitlement data on the Ping Autonomous Identity console. Admin users can approve or revoke a user's entitlement.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-admin-user-tasks
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-admin-user-tasks.html
section_ids:
  investigate-most-critical-entitlements: Investigate Most Critical Entitlements
  approve-revoke-access-an-entitlement-for-a-user: Approve or revoke access an entitlement for a user
  check-not-scored-users: Check not-scored users
  apply-filters: Apply filters
  change-elasticsearch-client-request-timeout: Changing the API's elasticsearch client request timeout
---

# Admin user tasks

The Admin user functionality is similar to that of a system administration *superuser*. Admin users have the access rights to company-wide entitlement data on the Ping Autonomous Identity console. Admin users can approve or revoke a user's entitlement.

## Investigate Most Critical Entitlements

One important task that an administrator must perform is to examine all critical entitlements. Critical entitlements are assigned entitlements that have are highly-assigned but have a low confidence score associated with it. The Ping Autonomous Identity console provides a means to examine these entitlements.

Follow these steps to evaluate the most critical entitlements list:

1. On the Dashboard, scroll down to the Most Critical Entitlements section. This section displays the entitlements that have low confidence scores and a high number of employees who have this entitlement.

2. Click an entitlement to view its details.

3. On the Entitlements detail page, review the key metrics.

4. Click the right arrow in one of the category ranges to view the users, and then click one of the users in the list.

5. On the User's Entitlements page, scroll down to review the Confidence Score Comparison table to display the differences between the user's attribute and the driving factor attributes.

6. Click Employees associated with this entitlement to review other uses who have this entitlement.

7. Click Actions, and then click Approve or Revoke for this entitlement. You can also bulk approve more than one entitlement. You can only revoke one entitlement at a time.

> **Collapse: Click an example**
>
> ![investigate most critical](_images/investigate-most-critical.gif)

## Approve or revoke access an entitlement for a user

Follow these steps to investigate a confidence score and approve or revoke access an entitlement assigned to a specific user:

1. On Ping Autonomous Identity console, click Identities, and enter a name of a supervisor. The only way to access a user's entitlements is through the Most Critical Entitlements section or the Identities page.

2. On the Identities page, click a circle, and then click the user in the list on the right.

3. On the User Entitlement page, click a confidence circle on the graph to highlight the entitlement below.

4. For the selected entitlement, click the down arrow on the right to view the Driving Factor Comparison.

5. Click Employees associated with this entitlement to view the justifications for those users with high confidence scores with this entitlement.

6. Click Actions, and then click Approve Access or Revoke access. If you have more than one entitlement that you want to approve, select them all and do a bulk Approval. You can only do one Revoke Access at a time.

> **Collapse: Click an example**
>
> ![approve revoke access admin](_images/approve-revoke-access-admin.gif)

## Check not-scored users

Follow these steps to check Not Scored entitlements. Not-scored indicates that it doesn't have a justification associated with the entitlement:

1. On Ping Autonomous Identity console, click Identities, and enter a name of a supervisor. The only way to access a user's entitlements is through the Most Critical Entitlements section or the Identities page.

2. On the Identities page, click a circle, and then click the user in the list on the right.

3. On the User Entitlement page, click Not Scored.

4. On the Not Scored Entitlements page, click the down arrow to view the driving factors comparison.

5. Click Employees associated with this entitlement to view the justifications for those users with high confidence scores with this entitlement.

6. Click Actions, and then click Approve Access or Revoke access. At a later date, you can re-click the Approve or Revoke button to cancel the operation.

> **Collapse: Click an example**
>
> ![entitlements not scored admin](_images/entitlements-not-scored-admin.gif)

## Apply filters

Follow these steps to apply filters to your confidence score graphs on the Identities and Entitlements pages:

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The Filters for the Identities and Entitlements are similar. The filters for the Applications and Rules pages offer different options to filter your searches. |

1. On the Identities or Entitlements page, view the average confidence score graph.

2. On the right, click Filters.

3. Under filters, do one or all of the following:

   * Click Remove High Scores from Average or enable any filter in the Application Filters section.

   * Under Applications, click one or more applications to display the identities or entitlements asssociated with the selected application.

   * Click Add Filters to further display only those identities or entitlements based on a user attribute, such as `city`. When ready, click Apply Filters.

4. Click Clear Filters to remove your filters.

> **Collapse: Click an example**
>
> ![apply filters admin](_images/apply-filters-admin.gif)

## Changing the API's elasticsearch client request timeout

The following steps outline how to change the Ping Autonomous Identity API's Elasticsearch client timeout to override the default of 30 seconds.

1. Open the `/opt/autoid/res/api/docker-compose.yml` file, and edit the `ELASTICSEARCH_CLIENT_TIMEOUT` variable as necessary (time in milliseconds):

   ```
   environment:
     …​
     - ELASTICSEARCH_CLIENT_TIMEOUT=30000
   ```

   For example:

   ```
   environment:
     …​
     - ELASTICSEARCH_CLIENT_TIMEOUT=60000
   ```

2. Remove the currently running `zoran-api` container, and redeploy the `zoran-api` Docker image:

   ```
   docker stack rm api
   docker stack deploy --with-registry-auth --compose-file /opt/autoid/res/api/docker-compose.yml api
   ```

3. Restart the `zoran-api` and nginx containers:

   ```
   docker service update --force ui_zoran-ui && docker service update --force nginx_nginx
   ```

4. Verity that Ping Autonomous Identity is running by opening the UI in a web browser.

---

---
title: Administrator tasks
description: This chapter is written for administrators who must manage and maintain Ping Autonomous Identity.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:preface
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/preface.html
---

# Administrator tasks

This chapter is written for administrators who must manage and maintain Ping Autonomous Identity.

Ping® Autonomous Identity is an entitlements and roles analytics system that lets you fully manage your company's access to your data.

An entitlement refers to the rights or privileges assigned to a user or thing for access to specific resources. A company can have millions of entitlements without a clear picture of what they are, what they do, and who they are assigned to. Ping Autonomous Identity solves this problem by using advanced artificial intelligence (AI) and automation technology to determine the full entitlements landscape for your company. The system also detects potential risks arising from incorrect or over-provisioned entitlements that lead to policy violations. Ping Autonomous Identity eliminates the manual re-certification of entitlements and provides a centralized, transparent, and contextual view of all access points within your company.

[icon: user-plus, set=fas, size=3x]

#### [Self service](chap-self-service.html)

Run self-service tasks.

[icon: user-friends, set=fas, size=3x]

#### [Manage identities](chap-manage-identities.html)

Add, edit, or remove user identities.

[icon: table, set=fas, size=3x]

#### [Prepare data](chap-data-preparation.html)

Prepare your data for ingestion.

[icon: wrench, set=fas, size=3x]

#### [Deployment tasks](chap-deployment-tasks.html)

Run deployment-related tasks.

[icon: file-import, set=fas, size=3x]

#### [Set entity definitions](set-entity-definitions.html)

Set your attribute entity definitions.

[icon: file-upload, set=fas, size=3x]

#### [Set data sources](set-data-sources.html)

Set your data sources.

[icon: equals, set=fas, size=3x]

#### [Set attribute mappings](set-attribute-mappings.html)

Set attribute mappings.

[icon: digital-tachograph, set=fas, size=3x]

#### [Set analytics settings](set-analytics-settings.html)

Set analytic settings.

[icon: chart-bar, set=fas, size=3x]

#### [Run analytics](chap-analytics-pipeline.html)

Run the analytics pipeline.

[icon: desktop, set=fas, size=3x]

#### [Admin tasks](chap-admin-user-tasks.html)

Run admin tasks.

[icon: server, set=fas, size=3x]

#### [Server maintenance](chap-server-maintenance.html)

Run server maintenance-related tasks.

[icon: user-cog, set=fas, size=3x]

#### [Roles management](chap-roles-tasks.html)

Manage your roles.

For installation instructions, refer to the [Ping Autonomous Identity Installation Guide](../install-guide/preface.html).

For a description of the Ping Autonomous Identity UI console, refer to the [Ping Autonomous Identity Users Guide](../users-guide/preface.html).

---

---
title: "Appendix A: Default User Permissions"
description: "Table: Summary of Default Ping Autonomous Identity Users Permissions"
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:appendix-default-user-privileges
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/appendix-default-user-privileges.html
---

# Appendix A: Default User Permissions

**Table: Summary of Default Ping Autonomous Identity Users Permissions**

| Permission                                    | App Owner | Entitlement Owner | Executive | Supervisor | User |
| --------------------------------------------- | --------- | ----------------- | --------- | ---------- | ---- |
| SHOW\_\_APPLICATION\_PAGE                     |          |                   |           |            |      |
| SHOW\_\_USER                                  |          |                  |           |           |     |
| SEARCH\_\_USER                                |          |                   |          |           |      |
| SEARCH\_\_USER\_ENTITLEMENTS\_BY\_APP\_OWNER  |          |                   |           |            |      |
| SEARCH\_\_USER\_ENTITLEMENTS\_BY\_ENTT\_OWNER |           |                  |           |            |      |
| SHOW\_\_OVERVIEW\_PAGE                        |          |                  |           |           |      |
| SHOW\_\_ASSIGNMENTS\_STATS                    |           |                   |          |            |      |
| SHOW\_\_COMPANY\_PAGE                         |           |                   |          |            |      |
| SHOW\_\_COMPANY\_ENTITLEMENTS\_DATA           |           |                   |          |            |      |
| SHOW\_\_ENTITLEMENTS                          |          |                  |           |           |     |
| SHOW\_\_ENTITLEMENT\_USERS                    |          |                  |           |            |      |
| SHOW\_\_CRITICAL\_ENTITLEMENTS                |           |                   |          |            |      |
| SHOW\_\_ENTITLEMENT\_AVG\_GROUPS              |           |                   |          |            |      |
| SHOW\_\_APP\_OWNER\_FILTER\_OPTIONS           |          |                   |           |            |      |
| SHOW\_\_ENTT\_OWNER\_FILTER\_OPTIONS          |           |                  |           |            |      |
| SHOW\_\_SUPERVISOR\_FILTER\_OPTIONS           |           |                   |           |           |      |
| SHOW\_\_ENTT\_OWNER\_UNSCORED\_ENTITLEMENTS   |          |                  |           |            |      |
| SHOW\_\_ENTT\_OWNER\_PAGE                     |          |                  |           |            |      |
| SHOW\_\_ENTT\_OWNER\_ENT\_PAGE                |          |                  |           |            |      |
| SHOW\_\_ENTT\_OWNER\_USER\_PAGE               |          |                  |           |            |      |
| SHOW\_\_SUPERVISOR\_PAGE                      |           |                   |           |           |      |
| SHOW\_\_SUPERVISOR\_ENTITLEMENT\_USERS        |           |                   |           |           |      |
| SHOW\_\_SUPERVISOR\_USER\_ENTITLEMENTS        |           |                   |           |           |      |
| SEARCH\_\_SUPERVISOR\_USER\_ENTITLEMENTS      |           |                   |           |           |      |
| SHOW\_\_SUPERVISOR\_UNSCORED\_ENTITLEMENTS    |           |                   |           |           |      |
| SHOW\_\_USER\_ENTITLEMENTS                    |          |                  |          |            |      |
| SHOW\_\_RULES\_BY\_APP\_OWNER                 |          |                   |           |            |      |
| SHOW\_\_RULES\_BY\_ENTT\_OWNER                |           |                  |           |            |      |
| SHOW\_\_CERTIFICATIONS                        |          |                  |           |           |     |
| REVOKE\_\_CERTIFY\_ACCESS                     |          |                  |           |           |      |

---

---
title: "Appendix A: The analytics_init_config.yml File"
description: The analytics_init_config.yml is an important configuration file in Ping Autonomous Identity. For each deployment, you customize the parameters to the environment. Deployers should configure this file before ingesting the input data into Cassandra.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:appendix-analytics-init-config
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/appendix-analytics-init-config.html
---

# Appendix A: The analytics\_init\_config.yml File

The `analytics_init_config.yml` is an important configuration file in Ping Autonomous Identity. For each deployment, you customize the parameters to the environment. Deployers should configure this file before ingesting the input data into Cassandra.

The process to use the `analytics_init_config.yml` is as follows:

* On the target node, use the `analytics create-template` command to generate the `analytics_init_config.yml` file.

* Make changes to the `analytics_init_config.yml` tailored to your deployment and production environment.

* Run the `analytics apply-template` command to apply your changes. The output file is `analytics_config.yml` file that is used for the other analytics jobs.

|   |                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not make changes to the `analytics_config.yml` . If you want to make changes to the configuration, update the `analytics_init_config.yml` file and then re-run the `analytics create-template` command. |

The file is used to do the following:

* Sets the input and output paths.

* Configures the association rule options.

* Sets the user attributes to be used for training.

* Sets up connection to the Cassandra database.

* Configures column names and mappings for the UI dataload.

The following `analytics_init_config.yml` file version is v0.32.0. The file is not expected to change much for each release, but some revision will occur intermittently.

```

# Common configuration options #

common:
  base_path:                /data/              # Base directory for analytics I/O. Configurable.

  
  # Data-related configuration options #
  # (Input & Output of files/rules)    #
  
data:
  # input data
  input:
    input_path:             input               # Input file directory under base_path. Configurable.
    features_file:          features.csv        # Contains user attribute data
    labels_file:            labels.csv          # Contains user-to-entitlement mappings.
    application_file:       AppToEnt.csv        # Contains entitlements-to-applications mappings.
    role_owner_file:        RoleOwner.csv       # Contains entitlement IDs to employees who "own the
                                                #   entitlements"
    account_name_file:      HRName.csv          # Contains user ID mappings to names.
    entitlement_name_file:  EntName.csv         # Contains entitlement IDs to their names.
    job_dept_desc_file:     JobAndDeptDesc.csv  # Contains user ID mappings to the departments where
                                                #   they work plus job descriptions

#
# Extract Transform Load to Database    #
# (Database Technologies i.e. Cassandra #
#
etl:
  med_conf:                 0.35                # Confidence threshold for medium confidence assignments
  high_conf:                0.75                # Confidence threshold for high confidence assignments
  edf_thresh:               0.75                # Confidence threshold for driving factor rules
  org_column_value:         test                # Use client organization identifier
  app_source_column:        test                # Use client organization identifier
  filtering_columns:        CITY                # Specifies any filtering columns

#
# Association Rules configuration options  #
# (Training & As-Is/Recommend Predictions) #

assoc_rules:
  # base config
  features_filter:        USR_KEY,CITY,USR_DEPARTMENT_NAME,        # update with columns you want to be
                          COST_CENTER,JOBCODE_NAME,                #   used in training (must contain
                          LINE_OF_BUSINESS,                        #   USR_KEY or equivalent)
                          LINE_OF_BUSINESS_SUBGROUP,
                          CHIEF_YES_NO,USR_EMP_TYPE,
                          USR_DISPLAY_NAME,MANAGER_NAME,
                          USR_MANAGER_KEY,IS_ACTIVE
  features_table_columns: USR_KEY,CITY,USR_DEPARTMENT_NAME,        # update with list of all columns in
                          COST_CENTER,JOBCODE_NAME,                #   features
                          LINE_OF_BUSINESS,
                          LINE_OF_BUSINESS_SUBGROUP,
                          CHIEF_YES_NO,USR_EMP_TYPE,
                          USR_DISPLAY_NAME,MANAGER_NAME,
                          USR_MANAGER_KEY,IS_ACTIVE


# User Column Description for the Feature CSV Headers
# ( user_name : User Name , user_manager :Manager Name)

ui_config:                                                 # Configurable column descriptions in the UI.
  user_column_descriptions: USR_KEY:User Key,CITY:City Location Building,USR_DEPARTMENT_NAME:User Department Name,
  COST_CENTER:User Cost Center,JOBCODE_NAME:Job Code Name,LINE_OF_BUSINESS:LOB,CHIEF_YES_NO:Manager Flag,
  USR_EMP_TYPE:Employee Type,USER_DISPLAY_NAME:User name,MANAGER_NAME:Manager Name,USR_MANAGER_KEY:Manager Key,
  IS_ACTIVE:Active

#
# Spark-related configuration options   #
##
spark:
  logging_level:  WARN                 # Logging level
  config:
    spark.executor.memory:            6G        # Recommended value >= 6
    spark.driver.memory:              4G        # Memory allocation to job on master.
    spark.driver.maxResultSize:       2G        # Maximum size of results storage capacity.
    spark.executor.cores:             3         # Number of executor cores
    spark.total.cores:                3         # Modify this value based on the cluster size. Number of
                                                #  executors will be calculated automatically.
    spark.scheduler.mode:             FAIR      # Set the scheduler for resources.
    spark.sql.shuffle.partitions:     6
    spark.task.maxFailures:           200
    spark.driver.blockManager.port:   39999
    spark.blockManager.port:          40016
ingestion:
  drop_if_create: true
  catalog_step: false
  staging: false
  connector:
    type: iiq
    batchsize: 100
    timeout: 30
    change_reconciliation:
      enabled: false
      time: '2013-05-17T00:00:00Z'
    features_mappings:
      chief_yes_no: User:CHIEF_YES_NO
      city: User:CITY
      jobcode_name: User:JOBCODE_NAME
      line_of_business: User:LINE_OF_BUSINESS
      line_of_business_subgroup: User:LINE_OF_BUSINESS_SUBGROUP
      usr_manager_name: User:MANAGER_NAME
      usr_dep_name: User:USR_DEPARTMENT_NAME
      usr_display_name: User:USR_DISPLAY_NAME
      usr_emp_type: User:USR_EMP_TYPE
      costcenter: User:COST_CENTER
```

---

---
title: "Appendix B: The ui-config.json File"
description: The ui-config.json file contains configuration properties for the Ping Autonomous Identity user interface and API services that are loaded as key-value pairs into Hashicorp Consul. The values are loaded through the Configuration Service that are shared across Ping Autonomous Identity's microservices.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:appendix-analytics-ui-config
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/appendix-analytics-ui-config.html
---

# Appendix B: The ui-config.json File

The `ui-config.json` file contains configuration properties for the Ping Autonomous Identity user interface and API services that are loaded as key-value pairs into Hashicorp Consul. The values are loaded through the Configuration Service that are shared across Ping Autonomous Identity's microservices.

The process to use the `ui-config.json` is as follows:

* On the target node, run the `analytics create-ui-config` command to generate the `ui_config.json` file in the `/data/conf/` directory.

* Make changes to the `ui_config.json` tailored to your deployment and production environment.

* Run the `analytics apply-ui-config` command to apply your changes.

The file is used to do the following:

* Define DB schemas used by the API to interface with the data layer. These schemas all contain a `table_name` property.

* Defines the organization name property, `OrgNameConf`, used for data displaoyed on the Company Overview Dashboard page.

* Defines various confidence score or count criteria, such as high, medium, and low score threshold levels and a minimum score threshold level to allow auto-certify or auto-request actions. The key properties are:

  * `ConfidenceScorethresholdsConf`

  * `ConfigThresholdsConf`

  * `MostAssigned`

  * `HighVolume`

  * `HighRiskConf`

* Defines the permissions that are applied to each Ping Autonomous Identity user group. The key property is `PermissionsConf`.

* Maps database columns to user-friendly titles for fields, labels, and headings in the UI. The key properties are:

  * `UIConfig`

  * `UIHRData`

  * `UIJustifications`

* Defines the user and entitlement attributes to be used as filters in the UI. The key properties are:

  * `FilteringOptionsConf`

  * `AllowedAttributesForFiltering`

* Defines the character delimiter used in the raw justification string data to separate the justification key from its value. The key property is: `JustificationDelimeter`.

The following `ui-config.json` file version is v0.32.0. The file is not expected to change much for each release, but some revision may occur intermittently.

```
{
    "RecommendPredictionsConf": {
        "name": "RecommendPredictions",
        "modelDefinition": {
            "fields": {
                "usr_key": "text",
                "ent": "text",
                "conf": "decimal",
                "freq": "decimal",
                "frequnion": "decimal",
                "rule": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "last_usage": "text"
            },
            "key": [
                "usr_key",
                "ent"
            ],
            "table_name": "recommend_predictions"
        }
    },
    "CompanyViewOverviewConf": {
        "name": "CompanyViewOverview",
        "modelDefinition": {
            "fields": {
                "key": "text",
                "total_employees": "int",
                "employees_wo_manager": "int",
                "employees_w_manager": "int",
                "entitlements_without_roleowners": "int",
                "entitlements_with_roleowners": "int",
                "total_entitlements": "int",
                "entitlements_covered_by_model": "int",
                "entitlements_not_covered": "int",
                "entitlements_w_no_users": "int",
                "entitlements_w_one_user": "int",
                "entitlements_w_zero_to_five_users": "int",
                "entitlements_w_five_to_ten_users": "int",
                "entitlements_w_ten_to_hundred_users": "int",
                "entitlements_w_hundred_to_onek_user": "int",
                "entitlements_w_onek_to_tenk_users": "int",
                "entitlements_w_tenk_users": "int",
                "entitlements_w_hundredk_users": "int"
            },
            "key": [
                "key"
            ],
            "table_name": "company_view_overview"
        }
    },
    "CompanyViewEmployeeTypeConf": {
        "name": "CompanyViewEmployeeType",

    "EntitlementUserManagerScoresConf": {
        "name": "EntitlementUserManagerScores",
        "modelDefinition": {
            "fields": {
                "entitlement": "text",
                "entitlement_name": "text",
                "user": "text",
                "user_name": "text",
                "manager": "text",
                "score": "float",
                "justification": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "app_id": "text",
                "app_name": "text"
            },
            "key": [
                "entitlement",
                "score",
                "user",
                "manager"
            ],
            "table_name": "entitlement_user_manager_scores"
        }
    },
    "GraphByRoleConf": {
        "name": "GraphByRole",
        "modelDefinition": {
            "fields": {
                "role": "text",
                "entitlement": "text",
                "entitlement_name": "text",
                "app_id": "text",
                "app_name": "text",
                "high_risk": "text"
            },
            "key": [
                "entitlement",
                "app_id",
                "role"
            ],
            "indexes": [
                "entitlement_name"
            ],
            "table_name": "graph_by_role"
        }
    },
    "GraphConf": {
        "name": "Graph",
        "modelDefinition": {
            "fields": {
                "manager": "text",
                "user": "text",
                "manager_name": "text",

    "RoleOwnerConf": {
        "name": "RoleOwner",
        "modelDefinition": {
            "fields": {
                "role": "text",
                "role_name": "text",
                "entitlement": "text",
                "entitlement_name": "text",
                "user": "text",
                "user_name": "text",
                "score": "decimal",
                "justification": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "app_id": "text",
                "app_name": "text",
                "high_risk": "text"
            },
            "key": [
                "role",
                "entitlement",
                "score",
                "app_id",
                "user"
            ],
            "table_name": "usr_scores_by_role"
        }
    },
    "RuleAccessDecisionConf": {
        "name": "RuleAccessDecision",
        "modelDefinition": {
            "fields": {
                "entitlement": "text",
                "justification": {
                    "type": "frozen",
                    "typeDef": "<list<text>>"
                },
                "is_autocertify": "boolean",
                "date_autocertified": "timestamp",
                "is_autorequest": "boolean",
                "date_autorequested": "timestamp",
                "author": "text",
                "author_name": "text",
                "author_type": "text",
                "reason": "text"
            },
            "key": [
                "entitlement",
                "justification"
            ],
            "table_name": "rule_access_decisions"
        }
    },
    "RuleAccessDecisionHistoryConf": {
        "name": "RuleAccessDecisionHistory",
        "modelDefinition": {
            "fields": {
                "entitlement": "text",
                "justification": {
                    "type": "frozen",
                    "typeDef": "<list<text>>"
                },
                "is_autocertify": "boolean",
                "date_autocertified": "timestamp",
                "is_autorequest": "boolean",
                "date_autorequested": "timestamp",
                "author": "text",
                "author_name": "text",
                "author_type": "text",
                "reason": "text",
                "date_created": "timestamp"
            },
            "key": [
                "entitlement",
                "justification",
                "date_created"
            ],
            "table_name": "rule_access_decisions_history"
        }
    },
    "UserAccessDecisionConf": {
        "name": "UserAccessDecision",
        "modelDefinition": {
            "fields": {
                "user": "text",
                "entitlement": "text",
                "is_certified": "boolean",
                "date_certified": "timestamp",
                "is_revoked": "boolean",
                "date_revoked": "timestamp",
                "is_requested": "boolean",
                "date_requested": "timestamp",
                "author": "text",
                "author_name": "text",
                "author_type": "text",
                "reason": "text",
                "is_processed": "boolean",
                "is_archived": "boolean"
            },
            "key": [
                "user",
                "entitlement"
            ],
            "table_name": "user_access_decisions"
        }
    },
    "UserAccessDecisionHistoryConf": {
        "name": "UserAccessDecisionHistory",
        "modelDefinition": {
            "fields": {
                "user": "text",
                "entitlement": "text",
                "is_certified": "boolean",
                "date_certified": "timestamp",
                "is_revoked": "boolean",
                "date_revoked": "timestamp",
                "is_requested": "boolean",
                "date_requested": "timestamp",
                "author": "text",
                "author_name": "text",
                "author_type": "text",
                "reason": "text",
                "is_processed": "boolean",
                "is_archived": "boolean",
                "date_created": "timestamp"
            },
            "key": [
                "user",
                "entitlement",
                "date_created"
            ],
            "table_name": "user_access_decisions_history"
        }
    },
    "UserConf": {
        "name": "User",
        "modelDefinition": {
            "fields": {
                "user": "text",
                "chiefyesno": "text",
                "city": "text",
                "costcenter": "text",
                "jobcodename": "text",
                "lineofbusiness": "text",
                "managername": "text",
                "usrdepartmentname": "text",
                "userdisplayname": "text",
                "usremptype": "text",
                "usrmanagerkey": "text",
                "isactive": "text"
            },
            "key": [
                "user"
            ],
            "table_name": "user"
        }
    },
    "UserScoreConf": {
        "name": "UserScore",
        "modelDefinition": {
            "fields": {
                "manager": "text",
                "user": "text",
                "manager_name": "text",
                "user_name": "text",
                "score": "decimal",
                "entitlement": "text",
                "entitlement_name": "text",
                "justification": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "app_id": "text",
                "app_name": "text",
                "high_risk": "text"
            },
            "key": [
                "app_id",
                "manager",
                "user",
                "entitlement"
            ],
            "table_name": "usr_scores_by_manager"
        }
    },
    "UserEntitlementMappingsConf": {
        "name": "UserEntitlementMappings",
        "modelDefinition": {
            "fields": {
                "user": "text",
                "ent": "text",
                "high_risk": "text",
                "is_assigned": "text",
                "last_usage": "timestamp"
            },
            "key": [
                "user",
                "ent"
            ],
            "table_name": "user_entitlement_mappings"
        }
    },
    "SupervisorAppEnttConf": {
        "name": "SupervisorAppEntt",
        "modelDefinition": {
            "fields": {
                "manager": "text",
                "entitlement": "text",
                "app_id": "text"
            },
            "key": [
                "manager",
                "app_id"
            ],
            "table_name": "app_entitlement_by_manager"
        }
    },
    "FilteringOptionsModelConf": {
        "name": "FilteringOptions",
        "modelDefinition": {
            "fields": {
                "role": "text",
                "type": "text",
                "owner_id": "text",
                "group": "text",
                "id": "text",
                "name": "text",
                "objects": {
                    "type": "list",
                    "typeDef": "<text>"
                }
            },
            "key": [
                "id"
            ],
            "table_name": "filtering_options"
        }
    },
    "CompanyViewMostCriticalEnttConf": {
        "name": "CompanyViewMostCriticalEntt",
        "modelDefinition": {
            "fields": {
                "org": "text",
                "entt_id": "text",
                "entt_name": "text",
                "high": "int",
                "medium": "int",
                "seq": "int",
                "low": "int",
                "total_employees": "int",
                "avg_conf_score": "float"
            },
            "key": [
                "org",
                "entt_id"
            ],
            "table_name": "company_view_most_critical_entt"
        }
    },
    "AutoprovisionEntitlementResults": {
        "name": "AutoprovisionEntitlementResults",
        "modelDefinition": {
            "fields": {
                "decision": "int",
                "score": "float",
                "threshold": "float",
                "app_id": "text",
                "app_name": "text",
                "entitlement_name": "text",
                "entitlement": "text",
                "user": "text",
                "user_name": "text",
                "created": "timestamp",
                "updated": "timestamp"
            },
            "key": [
                "decision",
                "entitlement",
                "user"
            ],
            "table_name": "autoprovision_entitlement_results"
        }
    },
    "EntitlementsCounts": {
        "name": "EntitlementsCounts",
        "modelDefinition": {
            "fields": {
                "type": "text",
                "count": "int",
                "entitlement": "text"
            },
            "key": [
                "type",
                "count",
                "entitlement"
            ],
            "clustering_order": {
                "count": "desc",
                "entitlement": "desc"
            },
            "table_name": "entitlements_counts"
        }
    },
    "MaxScoreEntitlementsUserCount": {
        "name": "MaxScoreEntitlementsUserCount",
        "modelDefinition": {
            "fields": {
                "max_score": "float",
                "users_count": "int",
                "entitlement": "text"
            },
            "key": [
                "max_score",
                "users_count",
                "entitlement"
            ],
            "table_name": "max_score_entitlements_user_count"
        }
    },
    "MinScoreEntitlementsUserCount": {
        "name": "MinScoreEntitlementsUserCount",
        "modelDefinition": {
            "fields": {
                "min_score": "float",
                "users_count": "int",
                "entitlement": "text"
            },
            "key": [
                "min_score",
                "users_count",
                "entitlement"
            ],
            "table_name": "min_score_entitlements_user_count"
        }
    },
    "EntitlementDrivingFactorConf": {
        "name": "EntitlementDrivingFactor",
        "modelDefinition": {
            "fields": {
                "ent": "text",
                "attribute": "text",
                "count": "int"
            },
            "key": [
                "ent",
                "attribute"
            ],
            "table_name": "entitlement_driving_factor"
        }
    },
    "ReportsConf": {
        "RoleMining": "RoleMining",
        "Automatic Re-certification Feed": "AutomaticRecertificationFeed",
        "Full Output (IDM) Feed": "FullOutputFeed",
        "Anomaly Report": "AnomalyReport",
        "Recommend Predictions": "RecommendPredictions",
        "Event Based Certification": "EventBasedCertification"
    },
    "RoleMining": {
        "name": "RoleMining",
        "modelDefinition": {
            "fields": {
                "policy": {
                    "type": "frozen",
                    "typeDef": "<list<text>>"
                },
                "total_employees": "int",
                "entt_id": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "entt_name": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "total_entts": "int",
                "role": "int"
            },
            "key": [
                "policy"
            ],
            "table_name": "role_mining"
        }
    },
    "AutomaticRecertificationFeed": {
        "name": "AutomaticRecertificationFeed",
        "modelDefinition": {
            "fields": {
                "user": "text",
                "entitlement": "text",
                "app_id": "text",
                "app_name": "text",
                "auto_recert": "text",
                "chiefyesno": "text",
                "city": "text",
                "costcenter": "text",
                "ent_size": "decimal",
                "entitlement_name": "text",
                "event_recert": "text",
                "freq": "decimal",
                "frequnion": "decimal",
                "jobcodename": "text",
                "justification": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "lineofbusiness": "text",
                "lineofbusinesssubgroup": "text",
                "managername": "text",
                "score": "decimal",
                "user_name": "text",
                "userdepartmentname": "text",
                "userdisplayname": "text",
                "usremptype": "text",
                "usrmanagerkey": "text"
            },
            "key": [
                "user",
                "entitlement"
            ],
            "table_name": "master_feed"
        }
    },
    "FullOutputFeed": {
        "name": "FullOutputFeed",
        "modelDefinition": {
            "fields": {
                "user": "text",
                "entitlement": "text",
                "app_id": "text",
                "app_name": "text",
                "auto_recert": "text",
                "chiefyesno": "text",
                "city": "text",
                "costcenter": "text",
                "ent_size": "decimal",
                "entitlement_name": "text",
                "event_recert": "text",
                "freq": "decimal",
                "frequnion": "decimal",
                "jobcodename": "text",
                "justification": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "lineofbusiness": "text",
                "lineofbusinesssubgroup": "text",
                "managername": "text",
                "score": "decimal",
                "user_name": "text",
                "userdepartmentname": "text",
                "userdisplayname": "text",
                "usremptype": "text",
                "usrmanagerkey": "text"
            },
            "key": [
                "user",
                "entitlement"
            ],
            "table_name": "master_feed"
        }
    },
    "RecommendPredictions": {
        "name": "RecommendPredictions",
        "modelDefinition": {
            "fields": {
                "usr_key": "text",
                "ent": "text",
                "conf": "decimal",
                "freq": "decimal",
                "frequnion": "decimal",
                "rule": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "last_usage": "text"
            },
            "key": [
                "usr_key",
                "ent"
            ],
            "table_name": "recommend_predictions"
        }
    },
    "AnomalyReport": {
        "name": "AnomalyReport",
        "modelDefinition": {
            "fields": {
                "user": "text",
                "user_name": "text",
                "manager_name": "text",
                "entitlement": "text",
                "entitlement_name": "text",
                "justification": {
                    "type": "list",
                    "typeDef": "<text>"
                },
                "app_name": "text",
                "confidence": "float",
                "avg_conf_score": "float",
                "total_assignees": "int",
                "num_below_conf_threshold": "int",
                "percent_below_threshold": "float",
                "freq": "decimal",
                "frequnion": "decimal",
                "median": "float",
                "last_usage": "timestamp"
            },
            "key": [
                "user_name",
                "avg_conf_score"
            ],
            "table_name": "anomaly_report"
        }
    },
  "EventBasedCertification": {
        "name": "EventBasedCertification",
        "modelDefinition": {
            "fields": {
                "id": "text",
                "type": "text",
                "batch_id": "int",
                "original": "text",
                "update": "text"
            },
            "key": [
                "id",
                "type",
                "batch_id"
            ],
            "table_name": "event_based_certification"
        }
    },
    "FilteringOptionsConf": {
        "filteringOptions": [
            {
                "groupName": "CITY",
                "title": "CITY",
                "optionTextField": "id"
            }
        ]
    },
    "JobStatus": {
        "name": "JobStatus",
        "modelDefinition": {
            "fields": {
                "job_name": "text",
                "start_time": "text",
                "batch_id": "int",
                "end_time": "text",
                "flag": "text"
            },
            "key": [
                "job_name",
                "start_time",
                "batch_id"
            ],
            "table_name": "job_status"
        }
    },
    "EntitlementAssignmentConfSummary": {
        "name": "EntitlementAssignmentConfSummary",
        "modelDefinition": {
            "fields": {
                "timestamp": "timestamp",
                "num_high_conf_assignments": "int",
                "num_low_conf_assignments": "int",
                "num_med_conf_assignments": "int"
            },
            "key": [
                "timestamp"
            ],
            "table_name": "entitlement_assignment_conf_summary"
        }
    },
    "OrgNameConf": {
        "orgName": "test"
    },
    "ConfidenceScoreThresholdsConf": {
        "thresholds": {
            "top": 1.01,
            "high": 0.75,
            "medium": 0.35,
            "low": 0,
            "autoAccess": 0.5
        }
    },
    "ConfigThresholdsConf": {
        "volumeThresholds": {
            "high": 90,
            "low": 20
        }
    },
    "MostAssigned": {
        "count": 100
    },
    "HighVolume": {
        "high": {
            "minScore": 0.9,
            "minUsersCount": 100
        },
        "low": {
            "maxScore": 0.2,
            "minUsersCount": 100
        }
    },
    "UIConfig": {
        "userDisplayNameKey": "userdisplayname"
    },
    "UIHRData": {
        "user": "User",
        "chiefyesno": "Chief",
        "city": "City",
        "costcenter": "Cost Center",
        "jobcodename": "Job Code Name",
        "lineofbusiness": "Line of Business",
        "managername": "Manager",
        "usrdepartmentname": "Department",
        "userdisplayname": "User Display Name",
        "usremptype": "Employee Type",
    "UIJustifications": {
        "USR_KEY": "User",
        "CITY": "City",
        "USR_DEPARTMENT_NAME": "Department",
        "COST_CENTER": "Cost Center",
        "JOBCODE_NAME": "Job Code Name",
        "LINE_OF_BUSINESS": "Line of Business",
        "LINE_OF_BUSINESS_SUBGROUP": "Line of Business Subgroup",
        "CHIEF_YES_NO": "Chief",
        "USR_EMP_TYPE": "Employee Type",
        "MANAGER_NAME": "Manager",
        "USR_DISPLAY_NAME": "User Display Name",
        "USR_MANAGER_KEY": "Manager Key"
    },
    "HighRiskConf": {
        "filterValue": "1"
    },
    "JustificationDelimeter": {
        "justificationDelimeter": "_"
    },
    "SearchConf": {
        "name": "Search",
        "modelDefinition": {
            "fields": {
                "userdisplayname": "text",
                "user": "text",
                "isentitlementowner": "boolean",
                "issupervisor": "boolean",
                "isapplicationowner": "boolean"
            },
            "indexes": [
                "userdisplayname"
            ],
            "key": [
                "user"
            ],
            "table_name": "search_user"
        }
    },
    "EntitlementsConf": {
        "name": "Entitlements",
        "modelDefinition": {
            "fields": {
                "id": "text",
                "app_id": "text",
                "app_name": "text",
                "entt_id_at_app": "text",
                "entt_name": "text"
            },
            "indexes": [
                "entt_name"
            ],
            "key": [
                "id"
            ],
            "table_name": "entitlements"
        }
    },
   "PermissionsConf": {
        "permissions": {
            "Zoran Admin": {
                "title": "Admin",
                "can": "*"
            },
            "Zoran Application Owner": {
                "title": "Application Owner",
                "can": [
                    "SHOWAPPLICATION_VIEW",
                    "FILTERENTITLEMENTS",
                    "SEARCHUSER_ENTITLEMENTS",
                    "SHOW_OVERVIEW_PAGE",
                    "SHOWENTITLEMENT",
                    "SHOWENTITLEMENT_USERS",
                    "SHOWFILTER_OPTIONS",
                    "SHOWROLEOWNER_UNSCORED_ENTITLEMENTS",
                    "SHOWROLE_OWNER_PAGE",
                    "SHOWROLE_OWNER_USER_PAGE",
                    "SHOWROLE_OWNER_ENT_PAGE",
                    "SHOWROLE_OWNER_AUTO_DATA",
                    "SHOWUSER_ENTITLEMENTS",
                    "SHOWUNSCORED_ENTITLEMENTS",
                    "SHOWRULES_BY_APP_OWNER",
                    "CERTIFYENTITLEMENTS_TO_USERS",
                    "CERTIFYUSERS_TO_ENTITLEMENTS",
                    "REVOKECERTIFY_ACCESS"
                ]
            },
            "Zoran Entitlement Owner": {
                "title": "Entitlement Owner",
                "can": [
                    "FILTERENTITLEMENTS",
                    "SEARCHUSER_ENTITLEMENTS",
                    "SHOW_OVERVIEW_PAGE",
                    "SHOWENTITLEMENT",
                    "SHOWENTITLEMENT_USERS",
                    "SHOWFILTER_OPTIONS",
                    "SHOWROLEOWNER_UNSCORED_ENTITLEMENTS",
                    "SHOWROLE_OWNER_PAGE",
                    "SHOWROLE_OWNER_USER_PAGE",
                    "SHOWROLE_OWNER_ENT_PAGE",
                    "SHOWROLE_OWNER_AUTO_DATA",
                    "SHOWUSER_ENTITLEMENTS",
                    "SHOWUNSCORED_ENTITLEMENTS",
                    "SHOWRULES_BY_ENTT_OWNER",
                    "CERTIFYENTITLEMENTS_TO_USERS",
                    "CERTIFYUSERS_TO_ENTITLEMENTS",
                    "REVOKECERTIFY_ACCESS"
                ]
            },
            "Zoran Executive": {
                "title": "Executive",
                "can": [
                    "SEARCHUSER",
                    "SHOWASSIGNMENTS_STATS",
                    "SHOWCOMPANY_PAGE",
                    "SHOWCOMPANY_COVERAGE_PAGE",
                    "SHOWCOMPANY_ENTITLEMENTS_PAGE",
                    "SHOWCOMPANY_ENTITLEMENTS_DATA",

                    "SEARCHUSER",
                    "FILTERENTITLEMENTS",
                    "SHOW_OVERVIEW_PAGE",
                    "SHOWEMPLOYEE",
                    "SHOWFILTER_OPTIONS",
                    "SHOWSUPERVISOR_PAGE",
                    "SHOWSUPERVISOR_DETAILS_PAGE",
                    "SHOWSUPERVISOR_ENT_DATA",
                    "SHOWSUPERVISOR_USER_DATA",
                    "SHOWSUPERVISOR_ENTITLEMENT_USERS",
                    "SHOWSUPERVISOR_USER_ENTITLEMENTS",
                    "SEARCHSUPERVISOR_USER_ENTITLEMENTS",
                    "SHOWSUPERVISOR_UNSCORED_ENTITLEMENTS",
                    "CERTIFYENTITLEMENTS_TO_USERS",
                    "CERTIFYUSERS_TO_ENTITLEMENTS",
                    "REVOKECERTIFY_ACCESS"
                ]
            },
            "Zoran User": {
                "title": "User",
                "can": [
                    "SHOWENTITLEMENT",
                    "SHOWUSER",
                    "SHOW__CERTIFICATIONS"
                ]
            }
        }
    },
    "AllowedAttributesForFiltering": {
        "entitlement": [
            "risk_level",
            "criticality",
            "owner"
        ],
        "user": [
            "usr_department_name",
            "line_of_business_subgroup",
            "city",
            "jobcode_name",
            "usr_emp_type",
            "chief_yes_no",
            "manager_name",
            "line_of_business",
            "cost_center"
        ]
    },
    "UIJustification": {
        "USR_KEY": "User",
        "CHIEF_YES_NO": "Chief",
        "CITY": "City",
        "COST_CENTER": "Cost Center",
        "JOBCODE_NAME": "Job Code Name",
        "LINE_OF_BUSINESS": "Line of Business",
        "MANAGER_NAME": "Manager",
        "USR_DEPARTMENT_NAME": "Department",
        "USR_DISPLAY_NAME": "User Display Name",
        "USR_EMP_TYPE": "Employee Type",
        "USR_MANAGER_KEY": "Manager Key",
        "IS_ACTIVE": "Active"
    }
}
```

---

---
title: Backing up and restoring
description: Ping Autonomous Identity stores its entitlement analytics results, association rules, predictions, and confidence scores in the Apache Cassandra, MongoDB, and Opensearch databases. Cassandra is an open-source, NoSQL database system where data is distributed across multiple nodes in a master-less cluster. MongoDB is a popular schema-free database that uses JSON-like documents. Opensearch is a distributed search engine based on Apache Lucene.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-backup-restore
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-backup-restore.html
section_ids:
  backing_up_cassandra: Backing up Cassandra
  restore_cassandra: Restore Cassandra
  backing_up_assignment_index_data_in_opensearch: Backing up assignment index data in Opensearch
  restoring_assignment_index_data_in_opensearch: Restoring assignment index data in Opensearch
  accessing_opensearch_index_data_using_opensearch_dashboards: Accessing Opensearch index data using Opensearch dashboards
---

# Backing up and restoring

Ping Autonomous Identity stores its entitlement analytics results, association rules, predictions, and confidence scores in the Apache Cassandra, MongoDB, and Opensearch databases. Cassandra is an open-source, NoSQL database system where data is distributed across multiple nodes in a master-less cluster. MongoDB is a popular schema-free database that uses JSON-like documents. Opensearch is a distributed search engine based on Apache Lucene.

For single-node deployments, however, you need to back up Cassandra or MongoDB on a regular basis. If the machine goes down for any reason, you need to restore the database as required.

To simplify the backup process, Ping Identity provides backup and restore scripts in the target directory.

## Backing up Cassandra

1. On the Ping Google Cloud Registry, download the `cassandra-backup.sh` script.

2. Move the script to the Cassandra home directory on your deployment.

3. Run the backup.

   ```
   $ ./cassandra-backup.sh \
       -d <Cassandra Database path> \
       -b <Backup folder path> \
       -u <Cassandra Username> \
       -p <Cassandra Password> \
       -s <SSL enable true/false> \
       -k <Keyspace (optional) default value: zoran>
   ```

## Restore Cassandra

1. On the Ping Google Cloud Registry, download the `cassandra-restore.sh` script.

2. Move the script to the Cassandra home directory on your deployment.

3. Run the restore.

   ```
   $ ./cassandra-restore.sh \
       -d <Cassandra Database path> \
       -b <Snapshot Backup tar file> \
       -f <Schema file> \
       -u <Cassandra Username> \
       -p <Cassandra Password> \
       -c <Cassandra commitlog path> \
       -i <Cassandra install path> \
       -s <SSL enable true/false> \
       -k <Keyspace (optional) default value: zoran>
   ```

## Backing up assignment index data in Opensearch

1. From the deployer node, SSH to the target node.

2. Change to the `/opt/autoid/elastic` directory. The directory was configured during the `./deployer.sh run`.

   ```
   $ cd /opt/autoid/elastic
   ```

3. Run the backup.

   ```
   $ ./assignment-index-backup.sh

   Elastic Host: 10.128.0.52
   Elastic Server Status : 200
   Elastic server is up and running …​
   assignment index exists status : 200
    registerSnapshotStatus 200
   backup snapshot name with time stamp : assignment_snapshot_2020_10_07__19_31_53
    entitlement-assignment backup status : 200
   * entitlement-assignment backup successful *
   ```

4. Make note of the snapshot name. For example, `assignment_snapshot_2020_10_07__19_31_53`.

## Restoring assignment index data in Opensearch

1. From the deployer node, SSH to the target node.

2. Change to the `/opt/autoid/elastic` directory.

   ```
   $ cd /opt/autoid/elastic
   ```

3. Run the restore using the snapshot taken from the previous procedure. When prompted if you want to close the existing index, enter `Y`. When prompted for the snapshot name, enter the name of the snapshot.

   ```
   $ ./assignment-index-restore.sh

   [Elastic Host: 10.128.0.55
    Elastic Server Status : 200
    Elastic server is up and running …​
    assignment index exists status : 200
    index with alias name -→ entitlement-assignment exists and is in open state…​
    Do you want to close the existing index -→ entitlement-assignment. (Required for restoring from snapshot ) (Y/N) ?
     y
    Restore snapshot ? true
     registerSnapshotStatus 200
    registering assignment_index_backup successful…​
    proceeding with index restore…​
    Enter the snapshot name to restore [snapshot_01]: assignment_snapshot_2020_10_0719_31_53
    snapshot to restore -→ assignment_snapshot_2020_10_0719_31_53
    entitlement-assignment index restore status -→ 200
    * entitlement-assignment restore successful *
   ```

## Accessing Opensearch index data using Opensearch dashboards

During the Ping Autonomous Identity deployment, Opensearch is installed to facilitate the efficient searching of entitlement data within the system. A typical deployment may have millions of different entitlements and assignments that require fast search processing. Opensearch provides that performance.

Opensearch comes bundled with its visualization console, Opensearch Dashboards, that lets you monitor and manage your Opensearch data. Once you run the `analytics create-assignment-index` command that populates the Opensearch index, you can configure an SSL tunnel to access Opensearch Dashboards. This is particularly useful when you want to retrieve a list of your backup snapshots.

1. Open a local terminal, and set up an SSL tunnel to your target node. The syntax is as follows:

   ```
   $ ssh -L < local-port >:<private-ip-remote>:<remote-port> -i <private-key> <user@public-ip-remote>
   ```

   For example:

   ```
   $ ssh -L 5601:10.128.0.71:5601 -i ~/.ssh/id_rsa autoid@34.70.190.144

   Last login: Fri Oct  9 20:10:59 2020
   ```

2. Open a browser and point it to `localhost:5601` Login in as `elasticadmin`. Enter your password that you set in the `~/autoid-config/vault.yml` file on the deployer node during install.

3. On the Opensearch page, click Explore on my own.

4. On the Opensearch Home page, click the menu in the top left corner, and click Dev Tools.

1) On the Dev Tools page, get a total count of indices.

   ```
   $ GET /entitlement-assignment/_count
   ```

2) On the Dev Tools page, search the indices.

   ```
   $ GET /entitlement-assignment/_search
   ```

3) On the Dev Tools page, get the list of snapshot backups.

   ```
   $ GET /_cat/snapshots/assignment_index_backup
   ```

---

---
title: Change the Vault Passwords
description: Ping Autonomous Identity uses the ansible vault to store passwords in encrypted files, rather than in plaintext. Ping Autonomous Identity stores the vault file at /autoid-config/vault.yml saves the encrypted passwords to /config/.autoid_vault_password . The /config/ mount is internal to the deployer container. The default encryption algorithm used is AES256.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-change-vault-passwords
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-change-vault-passwords.html
---

# Change the Vault Passwords

Ping Autonomous Identity uses the ansible vault to store passwords in encrypted files, rather than in plaintext. Ping Autonomous Identity stores the vault file at `/autoid-config/vault.yml` saves the encrypted passwords to `/config/.autoid_vault_password` . The `/config/` mount is internal to the deployer container. The default encryption algorithm used is AES256.

By default, the `/autoid-config/vault.yml` file uses the following parameters:

```
configuration_service_vault:
  basic_auth_password: Welcome123

openldap_vault:
  openldap_password: Welcome123

cassandra_vault:
  cassandra_password: Welcome123
  cassandra_admin_password: Welcome123

mongo_vault:
  mongo_admin_password: Welcome123
  mongo_root_password: Welcome123

elastic_vault:
  elastic_admin_password: Welcome123
  elasticsearch_password: Welcome123
```

Assume that the vault file is encrypted during the installation. To edit the file:

Edit the Vault file:

1. Change to the `/autoid-config/` directory.

   ```
   $ cd ~/autoid-config/
   ```

2. First, decrypt the vault file.

   ```
   $ ./deployer.sh decrypt-vault
   ```

3. Open a text editor and edit the `vault.yml` file.

4. Encrypt the file again.

   ```
   $ ./deployer.sh encrypt-vault
   ```

---

---
title: Configuring LDAP
description: Ping Autonomous Identity installs an OpenLDAP Docker image on the target server to hold user data. Administrators can add or remove users or change their group privileges using the phpldapadmin command (refer to Creating and Removing Users).
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-configure-ldap
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-configure-ldap.html
---

# Configuring LDAP

Ping Autonomous Identity installs an OpenLDAP Docker image on the target server to hold user data. Administrators can add or remove users or change their group privileges using the `phpldapadmin` command (refer to [Creating and Removing Users](chap-creating-users.html)).

You can configure the OpenLDAP repository specific to your environment using the `~/autoid-config/vars.yml` file.

1. Determine the LDAP domain, base DN, URL, group search base DN, and phpldapadmin port for your OpenLDAP repository.

2. On the deployer node, add the OpenLDAP configuration settings specific to your system to the `~/autoid-config/vars.yml` file:

   ```
   openldap:
       ldap_domain: zoran.com
       ldap_base_dn: dc=zoran,dc=com
       ldap_url: ldap://openldap
       ldap_groupsearchbase: ou=Groups,dc=zoran,dc=com
       ldap: true
       phpldapadmin_port: 80
   ```

---

---
title: Configuring Your Filters
description: The filters on the Applications pages let you focus your searches based on entitlement and user attributes. In most cases, the default filters should suffice for most environments. However, if you need to customize the filters, you can do so by accessing the configuration service API endpoint as show below.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-configure-filters
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-configure-filters.html
---

# Configuring Your Filters

The filters on the Applications pages let you focus your searches based on entitlement and user attributes. In most cases, the default filters should suffice for most environments. However, if you need to customize the filters, you can do so by accessing the configuration service API endpoint as show below.

The default filters for an entitlement are the following:

* Risk Level

* Criticality

The default filters for an user attributes are the following:

* User Department Name

* Line of Business Subgroup

* City

* Jobcode Name

* User Employee Type

* Chief Yes No

* Manager Name

* Line of Business

* Cost Center

Configure the Filters:

1. From the deployer node, SSH to the target node.

2. Run the `curl` command to retrieve the current filters configuration.

   ```
   $ curl -i -k -u configadmin:<configadmin-password> --header "Content-Type: application/json" --request GET
     https://autoid-configuration-service.forgerock.com/api/configuration/AllowedAttributesForFiltering

   {
     "entitlement": [
       "risk_level",
       "criticality",
       "owner"
     ],
     "user": [
       "usr_department_name",
       "line_of_business_subgroup",
       "city",
       "jobcode_name",
       "usr_emp_type",
       "chief_yes_no",
       "manager_name",
       "line_of_business",
       "cost_center"
     ]
   }
   ```

1) Update the filters configuration. The syntax is as follows:

   ```
   $ curl -i -k -u configadmin:<configadmin-password> \
         --request PUT \
         --header "Content-Type: application/json" \
         --data '{<UPDATED_FILTERING_JSON_DATA>}' \
       https://autoid-configuration-service.forgerock.com/api/configuration/AllowedAttributesForFiltering
   ```

   For example, update the filters list with fewer attributes:

   ```
   $ curl -i -k -u configadmin:<configadmin-password> \
         --request PUT \
         --header "Content-Type: application/json"
         --data '{ "entitlement":["risk_level","criticality","owner"], \
           "user":["usr_department_name","line_of_business_subgroup","city","jobcode_name"]}' \
       https://autoid-configuration-service.forgerock.com/api/configuration/AllowedAttributesForFiltering

   configuration item updated
   ```

---

---
title: Creating and Removing Users
description: You can set up users within Ping Autonomous Identity using the phpldapadmin command.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-creating-users
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-creating-users.html
section_ids:
  log_in_to_phpldapadmin: Log in to phpldapadmin
  add_user_to_a_group: Add User to a Group
  delete_a_user: Delete a User
---

# Creating and Removing Users

You can set up users within Ping Autonomous Identity using the `phpldapadmin` command.

## Log in to `phpldapadmin`

1. Make sure you have Ping Autonomous Identity successfully installed and deployed in your environment.

2. Add the phpldapadmin URL to your `/etc/hosts` file. Add your specific IP address to the file.

   ```
   <IP-Address>    autoid-openldap.forgerock.com
   ```

3. Access the phpldapadmin tool via your browser. Enter the following URL:

   ```
   https://autoid-openldap.forgerock.com
   ```

4. On the phpldapadmin page, click login in the navigation bar on the left side.

5. On the Authenticate to server openldap page, enter `cn=admin,dc=zoran,dc=com`, and then enter your admin password. Click Authenticate to proceed.

6. On the left-hand navigation bar, expand the menu, and then click ou=People.

7. Under `ou=People`, select any user to access their profile, and then click \<user> or move this entry.

8. On the Destination DN, change the name of the user to the user you want to add, and then click Copy. For example, let's create a new user: Mary Smith

   ```
   cn=mary.smith@forgerock.com,ou=People,dc=zoran,dc=com
   ```

9. On the Create Object page, change the following fields, and then click Create Object.

   * displayName. `Mary Smith`

   * givenName. `Smith`

   * homeDirectory. `/home/users/mary.smith`

   * Password. Enter a password for this user.

   * sn. `Mary`

   * title. Enter a title: admin, supervisor, entitlement owner, or user.

   * uidNumber. Enter a unique `uid` number.

   * User Name. Enter `mary.smith`.

10. On the Create LDAP Entry page, review the entry, and click Commit.

## Add User to a Group

The user that you created must be assigned to one of six groups: User, Supervisor, Executive, Entitlement Owner, Application Owner, and Admin.

1. On the phpldapadmin screen, click a user group. For this example, click cn=Zoran User.

2. Under uniqueMember, click Add Value, and then enter the user DN. For this example, enter `cn=mary.smith@forgerock.com,ou=People,dc=zoran,dc=com`.

3. Under uniqueMember, click Update Object.

4. Verify that you want to add the user under the New Value column, and then click Update Object.

## Delete a User

1. On the phpldapadmin screen, click ou=People to expand it, and then click the user who you want to delete.

2. At the top, click Delete this entry.

3. Under uniqueMember, click Update Object.

4. Verify that you want to delete the user. Click Delete. The user will be removed from the branch and from the `ou=Groups` branch.

---

---
title: Customize the Domain and Namespace
description: By default, the Ping Autonomous Identity URL and domain for the UI console is set to autoid-ui.forgerock.com, and the URL and domain for the self-service feature is autoid-selfservice.forgerock.com.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-customize-domain
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-customize-domain.html
---

# Customize the Domain and Namespace

By default, the Ping Autonomous Identity URL and domain for the UI console is set to `autoid-ui.forgerock.com`, and the URL and domain for the self-service feature is `autoid-selfservice.forgerock.com`.

Customize domain and namespace:

1. Customize the domain name and target environment by editing the `/autoid-config/vars.xml` file. By default, the domain name is set to `forgerock.com` and the target environment is set to `autoid`. The default Ping Autonomous Identity URL will be: `https://autoid-ui.forgerock.com`. For example, we set the domain name to `abc.com` and the target environment to `myid`:

   ```
   domain_name: forgerock.com
   target_environment: autoid
   ```

2. If you set up your domain name and target environment in the previous step, you need to change the certificates to reflect the changes. Ping Autonomous Identity generates self-signed certificates for its default configuration. You must generate new certificates as follows:

   1. Generate the private key (that is, `privatekey.pem`).

      ```
      $ openssl genrsa 2048 > privatekey.pem
      ```

   2. Generate the certificate signing request.

      ```
      $ openssl req -new -key privatekey.pem -out csr.pem
      ```

   3. Generate the Diffie-Hellman (DH) parameters file (dhparam4096.pem).

      ```
      $ openssl dhparam -out dhparam4096.pem 4096
      ```

   4. Create a self-signing certificate.

      ```
      $ openssl x509 -req -days 365 -in csr.pem -signkey privatekey.pem -out server.crt
      ```

   5. Use your Certificate Authority (CA) to sign the certificate. The certificate must be `server.crt`.

   6. Copy the files to the `/autoid-config/certs` directory.

   7. Make the domain changes on your DNS server or update your `/etc/hosts` file locally on your machine.

---

---
title: Data Ingestion
description: After running the analytics create-template command, you can configure the analytics pipeline run by editing the /data/conf/analytics_init_config.yml file.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-data-ingestion
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-data-ingestion.html
---

# Data Ingestion

After running the `analytics create-template` command, you can configure the analytics pipeline run by editing the `/data/conf/analytics_init_config.yml` file.

Ping Autonomous Identity supports data ingestion for three types of Identity Governance systems: general `csv` files, `iiq` for Sailpoint IdentityIQ files, and `oim` for Oracle Identity Manager files. You can configure the `/data/conf/analytics_init_config.yml` file for `iiq` or `oim` files.

**Data Ingestion**

|                         |                                              |                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Field                   | Sample                                       | Description                                                                                                                                                                                                                                                                                                                                                      |
| **ingestion:**          |                                              |                                                                                                                                                                                                                                                                                                                                                                  |
| drop\_if\_create:       | True/False                                   | Not used by these connectors                                                                                                                                                                                                                                                                                                                                     |
| catalog\_step           | True/False                                   | Creates a csv file with possible attributes from the client system. If set to `True`, the data pull doesn't occur. This property only needs to be set true in the first ingestion run to identify possible attributes.                                                                                                                                           |
| staging:                | True/False                                   | Determines whether to pull data to `autoid_staging` or `autoid_base` keyspaces. If `staging` is set to `True`, the system pulls to `autoid_staging` keyspace; while set to `False`, it pulls to `autoid_base` keyspace. The `autoid_staging` keyspace lets us pull data without on-the-fly transformations, while also supporting pulling from multiple sources. |
| connector:              |                                              |                                                                                                                                                                                                                                                                                                                                                                  |
| type:                   | `csv`, `iiq`, `oim`                          | Connector for type of source data. Currently only supporting three options.                                                                                                                                                                                                                                                                                      |
| batchsize:              | 1000                                         | Integer. Specifies the number of rows or pages pulled as part of each batch.                                                                                                                                                                                                                                                                                     |
| timeout:                | 10                                           | Integer representing seconds. Specifies the amount of time to wait before timeout.                                                                                                                                                                                                                                                                               |
| change\_reconciliation: |                                              |                                                                                                                                                                                                                                                                                                                                                                  |
| enabled:                | True/False                                   | Determines whether to pull data that filters only results that been modified after a certain date, specified by the `time` property.                                                                                                                                                                                                                             |
| time:                   | '2013-05-17T00:00:00Z','2020-05-17 00:00:00' | Specifies the data-time after which the data should be pulled. Note IIQ requires a time zone (first value).                                                                                                                                                                                                                                                      |
| features\_mappings:     |                                              |                                                                                                                                                                                                                                                                                                                                                                  |
| chief\_yes\_no          | 'User:CHIEF\_YES\_NO'                        | Value take from the csv generated in the catalog step. Note that `chief_yes_no` is not required, but is included here as an example. For reference, refer to [Appendix: analytics-init-config.yml](appendix-analytics-init-config.html).                                                                                                                         |

---

---
title: Data Preparation
description: Once you have deployed Ping Autonomous Identity, you can prepare your dataset into a format that meets the schema.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-data-preparation
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-data-preparation.html
section_ids:
  sec-data-collection: Data collection
  sec-csv-files-schema: CSV files and schema
---

# Data Preparation

Once you have deployed Ping Autonomous Identity, you can prepare your dataset into a format that meets the schema.

The initial step is to obtain the data as agreed upon between Ping Identity and your company. The files contain a subset of user attributes from the HR database and entitlement metadata required for the analysis. Only the attributes necessary for analysis are used.

There are a number of steps that must be carried out before your production entitlement data is input into Ping Autonomous Identity. The summary of these steps are outlined below:

## Data collection

Typically, the raw client data is not in a form that meets the Ping Autonomous Identity schema. For example, a unique user identifier can have multiple names, such as `user_id`, `account_id`, `user_key`, or `key`. Similarly, entitlement columns can have several names, such as `access_point`, `privilege_name`, or `entitlement`.

To get the correct format, here are some general rules:

* Submit the raw client data in `.csv` file format. The data can be in a single file or multiple files. Data includes application attributes, entitlement assignments, entitlements decriptions, and identities data.

* Duplicate values should be removed.

* Add optional columns for additional training attributes, for example, `MANAGERS_MANAGER` and `MANAGER_FLAG`. You can add these additional attributes to the schema using the Ping Autonomous Identity UI. For more information, refer to [Set Entity Definitions](set-entity-definitions.html).

* Make a note of those attributes that differ from the Ping Autonomous Identity schema, which is presented below. This is crucial for setting up your attribute mappings. For more information, refer to [Set Attribute Mappings](set-attribute-mappings.html).

## CSV files and schema

The required attributes for the schema are as follows:

**CSV Files Schema**

| Files            | Schema                                                                                                                                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| applications.csv | This file depends on the attributes that the client wants to include. Here are some required columns:- **app\_id**. Specifies the applications's unique ID.

- **app\_name**. Specifies the applications's name.

- **app\_owner\_id**. Specifies the ID of the application's owner. |
| assignments.csv  | * **user\_id**. Specifies the unique user ID to which the entitlement is assigned.

* **ent\_id**. Specifies the entitlements's unique ID.                                                                                                                                           |
| entitlements.csv | - **ent\_id**. Specifies the entitlements's unique ID.

- **ent\_name**. Specifies the entitlement name.

- **ent\_owner\_id**. Specifies the entitlement's owner.

- **app\_id**. Specifies the applications's unique ID.                                                           |
| identities.csv   | * **usr\_id**. Specifies the user's unique ID.

* **user\_name**. Specifies a human readable username. For example, `John Smith`.

* **usr\_manager\_id**. Specifies the user's manager ID.                                                                                          |

---

---
title: Deployment tasks
description: Ping Autonomous Identity administrators and deployers must set up additional tasks during installment.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-deployment-tasks
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-deployment-tasks.html
section_ids:
  customize_the_domain_and_namespace: Customize the domain and namespace
  customize_domain_and_namespace_new_deployments: Customize domain and namespace (new deployments)
  customize-domain-existing: Customize domain and namespace (existing deployments)
  configuring_your_filters: Configuring your filters
  change_the_vault_passwords: Change the Vault Passwords
  edit_the_vault_file: Edit the Vault file
  set_up_single_sign_on_sso: Set Up single sign-on (SSO)
  setup-sso-initial: Set up SSO in initial deployments
  setup-sso-existing: Set up SSO in existing deployments
  setting_the_session_duration: Setting the session duration
  custom_certificates: Custom certificates
  pre_requisites: Pre-requisites
  update-certs-cassandra: Update certificates on Cassandra
  update-certs-mongodb: Update certificates on MongoDB
  update-certs-jas: Update certificates on JAS
  update-certs-nginx: Update the certificates on NGINX
  update-certs-elastic: Update certificates on Opensearch
---

# Deployment tasks

Ping Autonomous Identity administrators and deployers must set up additional tasks during installment.

The following are some deployments tasks that may occur:

## Customize the domain and namespace

By default, the Ping Autonomous Identity URL and domain for the UI console is set to `autoid-ui.forgerock.com`, and the URL and domain for the self-service feature is `autoid-selfservice.forgerock.com`.

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These instructions are for new deployments. To change the domain and certificates in existing deployments, refer to [Customize domain and namespace (existing deployments)](#customize-domain-existing). |

### Customize domain and namespace (new deployments)

1. Customize the domain name and target environment by editing the `/autoid-config/vars.xml` file. By default, the domain name is set to `forgerock.com` and the target environment is set to `autoid`. The default Ping Autonomous Identity URL will be: `https://autoid-ui.forgerock.com`. For example, set the domain name to the following:

   ```
   domain_name: example.com
   target_environment: autoid
   ```

2. If you set up your domain name and target environment in the previous step, you need to change the certificates to reflect the changes. Ping Autonomous Identity generates self-signed certificates for its default configuration. You must generate new certificates as follows:

   1. Generate the private key (that is, `server.key`).

      ```
      openssl genrsa -out server.key 2048
      ```

   2. Generate the certificate signing request using your key. When prompted enter attributes sent with your certificate request:

      ```
      openssl req -new -key server.key -out server.csr

      Country Name (2 letter code) [XX]:US
      State or Province Name (full name) {}:Texas
      Locality Name (eg, city) [Default City]:Austin
      Organization Name (eg, company) [Default Company Ltd]:Ping
      Organizational Unit Name (eg, section) []:Eng
      Common Name (eg, your name or your server's hostname) []:autoid-ui.example.com
      Email Address []:

      A challenge password []:
      An optional company name []:
      ```

3. Generate the self-signed certificate.

   ```
   openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
   ```

4. Copy the certificate to the `/autoid-config/certs` directory. Make sure to use the following filename: `nginx-jas-wildcard.pem.`

   ```
   openssl x509 -in server.crt -out nginx-jas-wildcard.pem
   cp nginx-jas-wildcard.pem ~/autoid-config/certs
   ```

5. Copy the key to the `/autoid-config/certs` directory. Make sure to use the following filename: ``nginx-jas.key', depending on where your `/autoid-config/certs/`` resides.

   ```
   cp -i ~/.ssh/server.key /autoid-config/certs/nginx-jas.key

   or

   scp -i ~/.ssh/server.key autoid@remotehost:/autoid-config/certs/nginx-jas.key
   ```

6. Run the Ping Autonomous Identity deployer. Make sure that there are no errors after running the `./deployer.sh run` command.

   ```
   ./deployer.sh run
   ```

   1. Make the domain changes on your DNS server or update your `/etc/hosts` (Linux/Unix) file or `C:\Windows\System32\drivers\etc\hosts` (Windows) locally on your machine.

### Customize domain and namespace (existing deployments)

1. Modify the server name values with your updated domain name in the following files under `/opt/autoid/mounts/nginx/conf.d`:

   * api.conf

   * ui.conf

   * kibana.conf

   * jas.conf

2. Copy the SSL certificate file and corresponding SSL certificate key to the `/opt/autoid/mounts/nginx/cert` directory. The `/opt/autoid/mounts/nginx/cert` directory is mounted under `/etc/nginx/cert` in the container.

3. Modify `ssl_certificate` and `ssl_certificate_key` in `/opt/autoid/mounts/nginx/nginx.conf` with the correct filenames. Only the name of the files need to be updated, the path stays the same.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When using self-signed certificates, you need to import the new certificates in the JAS keystore and truststore at: `/opt/autoid/certs/jas/jas-client-keystore.jks` and `/opt/autoid/certs/jas/jas-server-truststore.jks`:```
   keytool -importcert -keystore jas-client-keystore.jks -alias myalias -file /opt/autoid/mounts/nginx/cert/cert.crt -noprompt -keypass mypass -storepass mypass

   keytool -importcert -keystore jas-server-truststore.jks -alias myalias -file /opt/autoid/mounts/nginx/cert/cert.crt -noprompt -keypass mypass -storepass mypass
   ``` |

4. Restart the nginx container:

   ```
   docker stack rm nginx
   docker stack deploy -c /opt/autoid/res/nginx/docker-compose.yml nginx
   ```

5. Update the new domain name in your hosts file where an entry exists for `JAS`. For example, the default JAS url is `autoid-jas.forgerock.com.` Change the JAS URL with your domain name.

6. Update the `JAS_URL` environment variable on all nodes by updating and sourcing your `.bashrc` file.

7. Restart Spark and Livy.

## Configuring your filters

The filters on the Applications pages let you focus your searches based on entitlement and user attributes. In most cases, the default filters should suffice for most environments. However, if you need to customize the filters, you can do so by accessing Searchable attribute under entity definitions. For information, refer to [Set Entity Definitions](set-entity-definitions.html).

The default filters for an entitlement are the following:

* Risk Level

* Criticality

The default filters for an user attributes are the following:

* User Department Name

* Line of Business Subgroup

* City

* Jobcode Name

* User Employee Type

* Chief Yes No

* Manager Name

* Line of Business

* Cost Center

## Change the Vault Passwords

Ping Autonomous Identity uses the ansible vault to store passwords in encrypted files, rather than in plaintext. Ping Autonomous Identity stores the vault file at `/autoid-config/vault.yml` saves the encrypted passwords to `/config/.autoid_vault_password` . The `/config/` mount is internal to the deployer container. The default encryption algorithm used is AES256.

By default, the `/autoid-config/vault.yml` file uses the following parameters:

```
configuration_service_vault:
  basic_auth_password: Welcome123

openldap_vault:
  openldap_password: Welcome123

cassandra_vault:
  cassandra_password: Welcome123
  cassandra_admin_password: Welcome123

mongo_vault:
  mongo_admin_password: Welcome123
  mongo_root_password: Welcome123

elastic_vault:
  elastic_admin_password: Welcome123
  elasticsearch_password: Welcome123
```

Assume that the vault file is encrypted during the installation. To edit the file:

### Edit the Vault file

1. Change to the `/autoid-config/` directory.

   ```
   $ cd ~/autoid-config/
   ```

2. First, decrypt the vault file.

   ```
   $ ./deployer.sh decrypt-vault
   ```

3. Open a text editor and edit the `vault.yml` file.

4. Encrypt the file again.

   ```
   $ ./deployer.sh encrypt-vault
   ```

## Set Up single sign-on (SSO)

Ping Autonomous Identity supports single sign-on (SSO) using OpenID Connect (OIDC) JWT tokens. SSO lets you log in once and access multiple applications without the need to re-authenticate yourself. You can use any third-party identity provider (IdP) to connect to Ping Autonomous Identity.

There are two scenarios for SSO configuration:

* **Set up SSO for initial deployments**. In this example, we use ForgeRock Access Management (AM) as an OpenID Connect (OIDC) IdP for Ping Autonomous Identity during the original installation of Ping Autonomous Identity. Refer to [Set up SSO in initial deployments](#setup-sso-initial).

* **Set up SSO for existing deployments**. For procedures to set up SSO in an existing Ping Autonomous Identity deployment, see [Set up SSO in existing deployments](#setup-sso-existing).

|   |                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you set up SSO-only, be aware that the following services are not deployed with this setting:* Self Service

* Manage IdentitiesIf you want to use these services and SSO, set up the authentication as `"LocalAndSSO"` in the `vars.yml` file. Otherwise, for SSO-only, you must use the user services provided by your SSO provider. |

### Set up SSO in initial deployments

The following procedure requires a running instance of AM. For more information, refer to [PingOne Access Management Authentication and Single Sign-On Guide](https://docs.pingidentity.com/pingam/7.1/authentication-guide/about-sso.html).

1. First, set up your hostnames locally in `/etc/hosts` (Linux/Unix) file or `C:\Windows\System32\drivers\etc\hosts` (Windows):

   ```
   35.189.75.99  autoid-ui.forgerock.com autoid-selfservice.forgerock.com
   35.246.65.234 openam.example.com
   ```

2. Open a browser and point to `http://openam.example.com:8080/openam`. Log in with username: `amadmin`, password: `cangetinam`.

3. In AM, select Realm > Identities > Groups tab, and add the following groups:

   * AutoIdAdmin

   * AutoIdEntitlementOwner

   * AutoIdExecutive

   * AutoIdSupervisor

   * AutoIdUser

   * AutoIdAppOwner

   * AutoIdRoleOwner

   * AutoIdRoleEngineer

     |   |                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The group names above are arbitrary and are defined in the `/autoid-config/vars.yml` file. Ensure that the groups you create in AM match the values in the `vars.yml` file. |

4. Add the `demo` user to each group.

5. Go back to the main AM Admin UI page. Click Configure OAuth Provider.

6. Click Configure OpenID Connect, and then Create.

7. Select desired Realm > Go to Applications > OAuth 2.0, and then click Add Client. Enter the following properties, specific to your deployment:

   ```
   Client ID:         <autoid>
   Client secret:     <password>
   Redirection URIs:  https://<autoid-ui>.<domain>/api/sso/finish
   Scope(s):          openid profile
   ```

   For example:

   ```
   Client ID:         autoid
   Client secret:     Welcome123
   Redirection URIs:  https://autoid-ui.forgerock.com/api/sso/finish
   Scope(s):          openid profile
   ```

8. On the New Client page, go to to the Advanced tab, and enable `Implied Consent`. Next, change the `Token Endpoint Authentication Method` to `client_secret_post`.

9. Edit the OIDC claims script to return `roles (groups)`, so that AM can match the Ping Autonomous Identity groups. Additionally, add the groups as a claim in the script:

   ```
   "groups": { claim, identity -> [ "groups" : identity.getMemberships(IdType.GROUP).collect { group -> group.name }]}
   ```

   In the `utils.setScopeClaimsMap` block, add:

   ```
   groups: ['groups']
   ```

   |   |                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For more information about the OIDC claims script, refer to the [ForgeRock Knowledge Base](https://backstage.forgerock.com/knowledge/kb/article/a15751293). |

   The `id_token` returns the content that includes the group names.

   ```
   {
     "at_hash": "QJRGiQgr1c1sOE4Q8BNyyg",
     "sub": "demo",
     "auditTrackingId": "59b6524d-8971-46da-9102-704694cae9bc-48738",
     "iss": "http://openam.example.com:8080/openam/oauth2",
     "tokenName": "id_token",
     "groups": [
       "AutoIdAdmin",
       "AutoIdSupervisor",
       "AutoIdUser",
       "AutoIdExecutive",
       "AutoIdEntitlementOwner",
       "AutoIdAppOwner",
       "AutoIdRoleOwner",
       "AutoIdRoleEngineer"
     ],
     "given_name": "demo",
     "aud": "autoid",
     "c_hash": "SoLsfc3zjGq9xF5mJG_C9w",
     "acr": "0",
     "org.forgerock.openidconnect.ops": "B15A_wXm581fO8INtYHHcwSQtJI",
     "s_hash": "bOhtX8F73IMjSPeVAqxyTQ",
     "azp": "autoid",
     "auth_time": 1592390726,
     "name": "demo",
     "realm": "/",
     "exp": 1592394729,
     "tokenType": "JWTToken",
     "family_name": "demo",
     "iat": 1592391129,
     "email": "demo@example.com"
   }
   ```

   |   |                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For more information on how to retrieve the `id_token` for observation, refer to [OpenID Connect 1.0 Endpoints](https://docs.pingidentity.com/pingam/7.1/oidc1-guide/rest-api-oidc-idtoken-validation.html}). |

   You have successfully configured AM as an OIDC provider.

10. Next, we set up Ping Autonomous Identity. Change to the Ping Autonomous Identity install directory on the deployer machine.

    ```
    cd ~/autoid-config/
    ```

11. Open a text editor, and set the SSO parameters in the `/autoid-config/vars.yml` file. Make sure to change `LDAP` to `SSO`.

    ```
    authentication_option: "SSO"

    oidc_issuer: "http://openam.example.com:8080/openam/oauth2"
    oidc_auth_url: "http://openam.example.com:8080/openam/oauth2/authorize"
    oidc_token_url: "http://openam.example.com:8080/openam/oauth2/access_token"
    oidc_user_info_url: "http://openam.example.com:8080/openam/oauth2/userinfo"
    oidc_jwks_url: "http://openam.example.com:8080/openam/oauth2/connect/jwk_uri"
    oidc_callback_url: "https://autoid-ui.forgerock.com/api/sso/finish"
    oidc_client_scope: 'openid profile'
    oidc_groups_attribute: groups
    oidc_uid_attribute: sub
    oidc_client_id: autoid
    oidc_client_secret: Welcome1
    admin_object_id: AutoIdAdmin
    entitlement_owner_object_id: AutoIdEntitlementOwner
    executive_object_id: AutoIdExecutive
    supervisor_object_id: AutoIdSupervisor
    user_object_id: AutoIdUser
    application_owner_object_id: AutoIdAppOwner
    role_owner_object_id: AutoIdRoleOwner
    role_engineer_object_id: AutoIdRoleEngineer
    oidc_end_session_endpoint: "http://openam.example.com:8080/openam/oauth2/logout"
    oidc_logout_redirect_url: "http://openam.example.com:8088/openam/logout"
    ```

12. On the target machine, edit the `/etc/hosts` file or your DNS server, and add an entry for `openam.example.com`.

    ```
    35.134.60.234  openam.example.com
    ```

13. On the deployer machine, run `deployer.sh` to push the new configuration.

    ```
    $ deployer.sh run
    ```

14. Test the connection now. Access `https://autoid-ui/forgerock.com`. The redirect should occur with the following:

    ```
    http://openam.example.com:8080/openam/XUI/?realm=%2F&goto=http%3A%2F%2Fopenam.example.com%3A8080%2Fopenam%2Foauth2%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dautoid
    ```

### Set up SSO in existing deployments

1. First, update the permissions configuration object as follows:

   1. Obtain an Ping Autonomous Identity admin level JWT bearer token. You can obtain it using curl and the Ping Autonomous Identity login endpoint with administrator credentials. Use your admin username and password:

      ```
      curl -X POST \
      https://autoid-ui.forgerock.com/api/authentication/login \
      -k \
      -H 'Content-Type: application/json' \
      -d '{
        "username": "bob.rodgers@forgerock.com",
        "password": "Welcome123"
      }'
      ```

      The response is:

      ```
      {
        "user": {
        "dn": "cn=bob.rodgers@zoran.com,ou=People,dc=zoran,dc=com",
        "controls": [],
        "displayName": "Bob Rodgers",
        "gidNumber": "999",
        "uid": "bob.rodgers",
        "_groups": [ "Zoran Admin" ]
        },
        "token": "eyJhbGciOiJIUzI1NiIsInR5 …"
      }
      ```

   2. Use curl and the bearer token from the previous step to obtain the Ping Autonomous Identity JAS tenant ID:

      ```
      curl -k -L -X GET 'https://autoid-ui.forgerock.com/jas/tenants' \
      -H 'Authorization: Bearer <token_value>'
      ```

      The response is:

      ```
      [
        {
          "id": "31092f95-3eed-418e-8ffb-f1b707bc9372",
          "name": "autonomous-iam",
          "description": "System Tenancy",
          "created": "2023-03-02T20:15:30.166Z"
        }
      ]
      ```

   3. To open the current permissions object, run the following curl command with the bearer token and tenant ID from the previous steps:

      ```
      curl -k -L -X POST 'https://autoid-ui.forgerock.com/jas/entity/search/common/config' \
      -H 'X-TENANT-ID: <tenant_id>' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer <token_value> \
      -d '{
        "query": {
          "query": {
            "bool": {
              "must": {
                "match": {
                  "name": "PermissionsConf"
                }
              }
            }
          }
        }
      }'
      ```

      An example response is as follows:

      |   |                                                                                                  |
      | - | ------------------------------------------------------------------------------------------------ |
      |   | You can find the permissions value under the `hits` object > `hits` array > `_source` > `value`. |

      ```
      {
        "took": 1,
        "timed_out": false,
        "_shards": {
          "total": 3,
          "successful": 3,
          "skipped": 0,
          "failed": 0
        },
        "hits": {
          "total": {
            "value": 1,
            "relation": "eq"
          },
          "max_score": 0.9808291,
          "hits": [
            {
              "_index": "autonomous-iam_common_config_latest",
              "_type": "_doc",
              "_id": "f72a58dd8bf5a38205c2d4c9eeafe85ebbaa1c3a2670b45c57f0219022b90ea6fc50ebf88e720c98410600e427528f0fe702b55f70975c8f49cb73c64ab1e101",
              "_score": 0.9808291,
              "_source": {
                "name": "PermissionsConf",
                "value": {
                  "permissions": {
                    "Zoran Admin": {
                      "title": "Admin",
                      "can": "*"
                    },
      …​
      ```

   4. Edit the Permissions object in the template by replacing the "###Zoran\_..\_Token###" fields with the SSO group ID. For example, the Permissions object would appear as follows before the change:

      ```
      "###Zoran_Admin_Token###":
      {
        "title": "Admin",
        "can": "*"
      },
      ```

      For SSO only setup, the following is used:

      |   |                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------- |
      |   | `f5bd09ca-096c-4a6e-b06d-65decc22cb09` is an example group ID for an organization's administrators. |

      ```
      "f5bd09ca-096c-4a6e-b06d-65decc22cb09":
      {
        "title": "Admin",
        "can": "*"
      },
      ```

      For SSO and local setup, use the following:

      ```
      "###Zoran_Admin_Token###":
      {
        "title": "Admin",
        "can": "*"
      },
      "f5bd09ca-096c-4a6e-b06d-65decc22cb09":
      {
        "title": "Admin",
        "can": "*"
      },
      ```

   5. Update the Permissions object in JAS with the edited JSON file:

      ```
      curl -k -L -X PATCH 'https://autoid-ui.forgerock.com/jas/entity/upsert/common/config' \
      -H 'X-TENANT-ID: <tenant_id>' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer <token_value>' \
      -d @<path/to/SSO.json>
      ```

      A successful response is:

      ```
      {
        "indexName": "autonomous-iam_common_config_latest",
        "indices":
        {
          "latest": "autonomous-iam_common_config_latest",
          "log": "autonomous-iam_common_config"
        }
      }
      ```

   6. Depending on how you want to configure SSO, use one of the following templates:

      |   |                                                                                                     |
      | - | --------------------------------------------------------------------------------------------------- |
      |   | The ContextID is an arbitrary UUID that can be any UUID. It is used just to track this transaction. |

      > **Collapse: localAndSSO template ()**
      >
      > ```
      > {
      >   "branch": "actual",
      >   "contextId": "ecba1baa-66d1-4548-8c74-6012bea9b838",
      >   "indexingRequired": true,
      >   "tags": {},
      >   "indexInSync": true,
      >   "entityData": [
      >     {
      >       "name": "PermissionsConf",
      >       "value":
      >       {
      >         "permissions":
      >         {
      >           "Zoran Admin":
      >           {
      >             "title": "Admin",
      >             "can": "*"
      >           },
      >           "###Zoran_Admin_Token###":
      >           {
      >             "title": "Admin",
      >             "can": "*"
      >           },
      >           "Zoran Role Engineer":
      >           {
      >             "title": "Role Engineer",
      >             "can": [
      >               "SHOW__ROLE_PAGE",
      >               "SEARCH__ALL_ROLES",
      >               "CREATE__ROLE",
      >               "UPDATE__ROLE",
      >               "DELETE__ROLE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "STATS_ALL__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "###Zoran_Role_Engineer_Token###":
      >           {
      >             "title": "Role Engineer",
      >             "can": [
      >               "SHOW__ROLE_PAGE",
      >               "SEARCH__ALL_ROLES",
      >               "CREATE__ROLE",
      >               "UPDATE__ROLE",
      >               "DELETE__ROLE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "STATS_ALL__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "Zoran Role Owner":
      >           {
      >             "title": "Role Owner",
      >             "can": [
      >               "SHOW__ROLE_PAGE",
      >               "SEARCH__ROLES",
      >               "CREATE__ROLE",
      >               "UPDATE__ROLE",
      >               "DELETE__ROLE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "STATS__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLES",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "###Zoran_Role_Owner_Token###":
      >           {
      >             "title": "Role Owner",
      >             "can": [
      >               "SHOW__ROLE_PAGE",
      >               "SEARCH__ROLES",
      >               "CREATE__ROLE",
      >               "UPDATE__ROLE",
      >               "DELETE__ROLE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "STATS__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLES",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "Zoran Role Auditor":
      >           {
      >             "title": "Role Auditor",
      >             "can": [
      >               "SEARCH__ALL_ROLES",
      >               "STATS_ALL__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS"
      >             ]
      >           },
      >           "###Zoran_Role_Auditor_Token###":
      >           {
      >             "title": "Role Auditor",
      >             "can": [
      >               "SEARCH__ALL_ROLES",
      >               "STATS_ALL__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS"
      >             ]
      >           },
      >           "Zoran Application Owner":
      >           {
      >             "title": "Application Owner",
      >             "can": [
      >               "SHOW__APPLICATION_PAGE",
      >               "SEARCH__USER",
      >               "SEARCH__ENTITLEMENTS_BY_APP_OWNER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__ENTITLEMENT_USERS",
      >               "SHOW__APP_OWNER_FILTER_OPTIONS",
      >               "SHOW__ENTT_OWNER_UNSCORED_ENTITLEMENTS",
      >               "SHOW__ENTT_OWNER_PAGE",
      >               "SHOW__ENTT_OWNER_USER_PAGE",
      >               "SHOW__ENTT_OWNER_ENT_PAGE",
      >               "SHOW__USER_ENTITLEMENTS",
      >               "SHOW__RULES_BY_APP_OWNER",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "###Zoran_Application_Owner_Token###":
      >           {
      >             "title": "Application Owner",
      >             "can": [
      >               "SHOW__APPLICATION_PAGE",
      >               "SEARCH__USER",
      >               "SEARCH__ENTITLEMENTS_BY_APP_OWNER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__ENTITLEMENT_USERS",
      >               "SHOW__APP_OWNER_FILTER_OPTIONS",
      >               "SHOW__ENTT_OWNER_UNSCORED_ENTITLEMENTS",
      >               "SHOW__ENTT_OWNER_PAGE",
      >               "SHOW__ENTT_OWNER_USER_PAGE",
      >               "SHOW__ENTT_OWNER_ENT_PAGE",
      >               "SHOW__USER_ENTITLEMENTS",
      >               "SHOW__RULES_BY_APP_OWNER",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "Zoran Entitlement Owner":
      >           {
      >             "title": "Entitlement Owner",
      >             "can": [
      >               "SEARCH__ENTITLEMENTS_BY_ENTT_OWNER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__ENTITLEMENT_USERS",
      >               "SHOW__ENTT_OWNER_FILTER_OPTIONS",
      >               "SHOW__ENTT_OWNER_UNSCORED_ENTITLEMENTS",
      >               "SHOW__ENTT_OWNER_PAGE",
      >               "SHOW__ENTT_OWNER_USER_PAGE",
      >               "SHOW__ENTT_OWNER_ENT_PAGE",
      >               "SHOW__USER_ENTITLEMENTS",
      >               "SHOW__RULES_BY_ENTT_OWNER",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "LOOKUP_USER",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "###Zoran_Entitlement_Owner_Token###":
      >           {
      >             "title": "Entitlement Owner",
      >             "can": [
      >               "SEARCH__ENTITLEMENTS_BY_ENTT_OWNER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__ENTITLEMENT_USERS",
      >               "SHOW__ENTT_OWNER_FILTER_OPTIONS",
      >               "SHOW__ENTT_OWNER_UNSCORED_ENTITLEMENTS",
      >               "SHOW__ENTT_OWNER_PAGE",
      >               "SHOW__ENTT_OWNER_USER_PAGE",
      >               "SHOW__ENTT_OWNER_ENT_PAGE",
      >               "SHOW__USER_ENTITLEMENTS",
      >               "SHOW__RULES_BY_ENTT_OWNER",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "LOOKUP_USER",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "Zoran Executive":
      >           {
      >             "title": "Executive",
      >             "can": [
      >               "SEARCH__USER",
      >               "SHOW__ASSIGNMENTS_STATS",
      >               "SHOW__COMPANY_PAGE",
      >               "SHOW__COMPANY_ENTITLEMENTS_DATA",
      >               "SHOW__CRITICAL_ENTITLEMENTS",
      >               "SHOW__ENTITLEMENT_AVG_GROUPS",
      >               "SHOW__USER_ENTITLEMENTS"
      >             ]
      >           },
      >           "###Zoran_Executive_Token###":
      >           {
      >             "title": "Executive",
      >             "can": [
      >               "SEARCH__USER",
      >               "SHOW__ASSIGNMENTS_STATS",
      >               "SHOW__COMPANY_PAGE",
      >               "SHOW__COMPANY_ENTITLEMENTS_DATA",
      >               "SHOW__CRITICAL_ENTITLEMENTS",
      >               "SHOW__ENTITLEMENT_AVG_GROUPS",
      >               "SHOW__USER_ENTITLEMENTS"
      >             ]
      >           },
      >           "Zoran Supervisor":
      >           {
      >             "title": "Supervisor",
      >             "can": [
      >               "SEARCH__USER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__SUPERVISOR_FILTER_OPTIONS",
      >               "SHOW__SUPERVISOR_PAGE",
      >               "SHOW__SUPERVISOR_ENTITLEMENT_USERS",
      >               "SHOW__SUPERVISOR_USER_ENTITLEMENTS",
      >               "SHOW__SUPERVISOR_UNSCORED_ENTITLEMENTS",
      >               "SEARCH__SUPERVISOR_USER_ENTITLEMENTS",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "###Zoran_Supervisor_Token###":
      >           {
      >             "title": "Supervisor",
      >             "can": [
      >               "SEARCH__USER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__SUPERVISOR_FILTER_OPTIONS",
      >               "SHOW__SUPERVISOR_PAGE",
      >               "SHOW__SUPERVISOR_ENTITLEMENT_USERS",
      >               "SHOW__SUPERVISOR_USER_ENTITLEMENTS",
      >               "SHOW__SUPERVISOR_UNSCORED_ENTITLEMENTS",
      >               "SEARCH__SUPERVISOR_USER_ENTITLEMENTS",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "Zoran User":
      >           {
      >             "title": "User",
      >             "can": [
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "###Zoran_User_Token###":
      >           {
      >             "title": "User",
      >             "can": [
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "Zoran Service Connector":
      >           {
      >             "title": "Service Connector",
      >             "can": [
      >               "SERVICE_CONNECTOR",
      >               "SHOW__API_KEY_MGMT_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "SHOW__RULES",
      >               "REVOKE__CERTIFY_ACCESS"
      >             ]
      >           },
      >           "###Zoran_Service_Connector_Token###":
      >           {
      >             "title": "Service Connector",
      >             "can": [
      >               "SERVICE_CONNECTOR",
      >               "SHOW__API_KEY_MGMT_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "SHOW__RULES",
      >               "REVOKE__CERTIFY_ACCESS"
      >             ]
      >           }
      >         }
      >       }
      >     }
      >   ]
      > }
      > ```

      > **Collapse: SSO template ()**
      >
      > ```
      > {
      >   "branch": "actual",
      >   "contextId": "ecba1baa-66d1-4548-8c74-6012bea9b838",
      >   "indexingRequired": true,
      >   "tags": {},
      >   "indexInSync": true,
      >   "entityData": [
      >     {
      >       "name": "PermissionsConf",
      >       "value":
      >       {
      >         "permissions":
      >         {
      >           "###Zoran_Admin_Token###":
      >           {
      >             "title": "Admin",
      >             "can": "*"
      >           },
      >           "###Zoran_Role_Engineer_Token###":
      >           {
      >             "title": "Role Engineer",
      >             "can": [
      >               "SHOW__ROLE_PAGE",
      >               "SEARCH__ALL_ROLES",
      >               "CREATE__ROLE",
      >               "UPDATE__ROLE",
      >               "DELETE__ROLE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "STATS_ALL__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "###Zoran_Role_Owner_Token###":
      >           {
      >             "title": "Role Owner",
      >             "can": [
      >               "SHOW__ROLE_PAGE",
      >               "SEARCH__ROLES",
      >               "CREATE__ROLE",
      >               "UPDATE__ROLE",
      >               "DELETE__ROLE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "STATS__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLES",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "###Zoran_Role_Auditor_Token###":
      >           {
      >             "title": "Role Auditor",
      >             "can": [
      >               "SEARCH__ALL_ROLES",
      >               "STATS_ALL__USERS",
      >               "SEARCH_ALL__USERS",
      >               "SEARCH_ALL__ENTITLEMENTS",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS"
      >             ]
      >           },
      >           "###Zoran_Application_Owner_Token###":
      >           {
      >             "title": "Application Owner",
      >             "can": [
      >               "SHOW__APPLICATION_PAGE",
      >               "SEARCH__USER",
      >               "SEARCH__ENTITLEMENTS_BY_APP_OWNER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__ENTITLEMENT_USERS",
      >               "SHOW__APP_OWNER_FILTER_OPTIONS",
      >               "SHOW__ENTT_OWNER_UNSCORED_ENTITLEMENTS",
      >               "SHOW__ENTT_OWNER_PAGE",
      >               "SHOW__ENTT_OWNER_USER_PAGE",
      >               "SHOW__ENTT_OWNER_ENT_PAGE",
      >               "SHOW__USER_ENTITLEMENTS",
      >               "SHOW__RULES_BY_APP_OWNER",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "###Zoran_Entitlement_Owner_Token###":
      >           {
      >             "title": "Entitlement Owner",
      >             "can": [
      >               "SEARCH__ENTITLEMENTS_BY_ENTT_OWNER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__ENTITLEMENT_USERS",
      >               "SHOW__ENTT_OWNER_FILTER_OPTIONS",
      >               "SHOW__ENTT_OWNER_UNSCORED_ENTITLEMENTS",
      >               "SHOW__ENTT_OWNER_PAGE",
      >               "SHOW__ENTT_OWNER_USER_PAGE",
      >               "SHOW__ENTT_OWNER_ENT_PAGE",
      >               "SHOW__USER_ENTITLEMENTS",
      >               "SHOW__RULES_BY_ENTT_OWNER",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "LOOKUP_USER",
      >               "SEARCH__ROLE_USERS",
      >               "SEARCH__ROLE_ENTITLEMENTS",
      >               "SEARCH__ROLE_JUSTIFICATIONS",
      >               "SHOW_ROLE_METADATA",
      >               "SHOW_ROLE_ATTRIBUTES",
      >               "WORKFLOW__REQUESTS",
      >               "WORKFLOW__TASKS",
      >               "WORKFLOW__TASK_APPROVE"
      >             ]
      >           },
      >           "###Zoran_Executive_Token###":
      >           {
      >             "title": "Executive",
      >             "can": [
      >               "SEARCH__USER",
      >               "SHOW__ASSIGNMENTS_STATS",
      >               "SHOW__COMPANY_PAGE",
      >               "SHOW__COMPANY_ENTITLEMENTS_DATA",
      >               "SHOW__CRITICAL_ENTITLEMENTS",
      >               "SHOW__ENTITLEMENT_AVG_GROUPS",
      >               "SHOW__USER_ENTITLEMENTS"
      >             ]
      >           },
      >           "###Zoran_Supervisor_Token###":
      >           {
      >             "title": "Supervisor",
      >             "can": [
      >               "SEARCH__USER",
      >               "SHOW_OVERVIEW_PAGE",
      >               "SHOW__SUPERVISOR_FILTER_OPTIONS",
      >               "SHOW__SUPERVISOR_PAGE",
      >               "SHOW__SUPERVISOR_ENTITLEMENT_USERS",
      >               "SHOW__SUPERVISOR_USER_ENTITLEMENTS",
      >               "SHOW__SUPERVISOR_UNSCORED_ENTITLEMENTS",
      >               "SEARCH__SUPERVISOR_USER_ENTITLEMENTS",
      >               "REVOKE__CERTIFY_ACCESS",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "###Zoran_User_Token###":
      >           {
      >             "title": "User",
      >             "can": [
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS"
      >             ]
      >           },
      >           "###Zoran_Service_Connector_Token###":
      >           {
      >             "title": "Service Connector",
      >             "can": [
      >               "SERVICE_CONNECTOR",
      >               "SHOW__API_KEY_MGMT_PAGE",
      >               "SHOW__ENTITLEMENT",
      >               "SHOW__USER",
      >               "SHOW__CERTIFICATIONS",
      >               "SHOW__RULES",
      >               "REVOKE__CERTIFY_ACCESS"
      >             ]
      >           }
      >         }
      >       }
      >     }
      >   ]
      > }
      > ```

   7. Verify your changes by opening the permissions object as shown in step 1c.

2. Next, update the JAS container environment variables:

   1. On the instance where Docker is running, create a backup of the `/opt/autoid/res/jas/docker-compose.yml` file, and edit the variables in the environment section. For example, change the following variables:

      From:

      ```
      - OIDC_ENABLED=False
      - GROUPS_ATTRIBUTE=_groups
      - OIDC_JWKS_URL=na
      ```

      To:

      ```
      - OIDC_ENABLED=True
      - GROUPS_ATTRIBUTE=groups
      - OIDC_JWKS_URL= <Same value as in the zoran-api. Refer to step 3 below>
      ```

      |   |                                                                                                                        |
      | - | ---------------------------------------------------------------------------------------------------------------------- |
      |   | The `GROUPS_ATTRIBUTE` variable must match the `OIDC_GROUPS_ATTRIBUTE` variable used in the `docker-compose.yml` file. |

   2. Remove the running JAS container and re-deploy:

      ```
      docker stack rm jas
      docker stack deploy --with-registry-auth --compose-file /opt/autoid/res/jas/docker-compose.yml jas
      ```

3) Next, update the `zoran-api` container environment variables:

   1. On the instance where Docker is running, create a backup of the `/opt/autoid/res/api/docker-compose.yml` file, and edit the following variables in the file replacing the `\$\{…​\}` placeholders:

      ```
      - OIDC_ISSUER=${OIDC_ISSUER}
      - OIDC_AUTH_URL=${OIDC_AUTH_URL}
      - OIDC_TOKEN_URL=${OIDC_TOKEN_URL}
      - OIDC_USER_INFO_URL=${OIDC_USER_INFO_URL}
      - OIDC_CLIENT_ID=${OIDC_CLIENT_ID}
      - OIDC_CLIENT_SECRET=${OIDC_CLIENT_SECRET}
      - OIDC_CALLBACK_URL=${OIDC_CALLBACK_URL}
      - OIDC_JWKS_URL=${OIDC_JWKS_URL}
      - OIDC_CLIENT_SCOPE=${OIDC_CLIENT_SCOPE}
      - OIDC_GROUPS_ATTRIBUTE=${OIDC_GROUPS_ATTRIBUTE}
      - OIDC_UID_ATTRIBUTE=${OIDC_UID_ATTRIBUTE}
      - OIDC_END_SESSION_ENDPOINT=${OIDC_END_SESSION_ENDPOINT}
      - OIDC_LOGOUT_REDIRECT_URL=${OIDC_LOGOUT_REDIRECT_URL}
      ```

      For example, Ping Autonomous Identity displays something similar below (the example uses Asure links and object IDs):

      ![zoran api docker env variables](_images/zoran-api-docker-env-variables.png)

      |   |                                                                                                                                                                                                                                                                            |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | If you are configuring SSO only for the login mode, set `LOCAL_AUTH_MODE` to `false` (for example, LOCAL\_AUTH\_MODE=false). If you keep `LOCAL_AUTH_MODE` to `true`, Ping Autonomous Identity defaults to `LocalAndSSO,` which uses the OIDC and email options for login. |

   2. Remove the running zoran-api Docker container and re-deploy:

      ```
      docker stack rm api
      docker stack deploy --with-registry-auth --compose-file /opt/autoid/res/api/docker-compose.yml api
      ```

   3. Restart the UI and Nginx Docker containers:

      ```
      docker service update --force ui_zoran-ui
      docker service update --force nginx_nginx
      ```

3. Open the Ping Autonomous Identity UI to verify the SSO login.

   ![sso login page](_images/sso-login-page.png)

## Setting the session duration

By default, the session duration is set to 30 minutes. You can change this value at installation by setting the `JWT_EXPIRY` property in the `/autoid-config/vars.yml` file.

If you did not set the value at installation, you can make the change after installation by setting the `JWT_EXPIRY` property using the API service.

1. Log in to the Docker manager node.

2. Verify the `JWT_EXPIRY` property.

   ```
   $ docker inspect api_zoran-api
   ```

3. Go to the API folder.

   ```
   $ cd /opt/autoid/res/api
   ```

4. Edit the `docker-compose.yml` file and update the `JWT_EXPIRY` property. The `JWT_EXPIRY` property is set to minutes.

5. Redeploy the Docker stack API.

   ```
   $ docker stack deploy --with-registry-auth --compose-file docker-compose.yml api
   ```

   If the command returns any errors, such as "image could not be accessed by the registry," then try the following command:

   ```
   $ docker stack deploy --with-registry-auth --resolve-image changed \
       --compose-file /opt/autoid/res/api/docker-compose.yml api
   ```

6. Verify the new `JWT_EXPIRY` property.

   ```
   $ docker inspect api_zoran-api
   ```

7. Log in to the Docker worker node.

8. Stop the worker node.

   ```
   $ docker stop [container ID]
   ```

   The Docker manager node re-initiates the worker node. Repeat this step on any other worker node.

## Custom certificates

By default, Ping Autonomous Identity uses self-signed certificates in its services. You can replace these self-signed certificates with a certificate issued by a Certificate Authority (CA). This section provides instructions on how to replace your self-signed certificates and also update your existing certificates when expired.

* [Update certificates on Cassandra](#update-certs-cassandra)

* [Update certificates on MongoDB](#update-certs-mongodb)

* [Update certificates on JAS](#update-certs-jas)

* [Update the certificates on NGINX](#update-certs-nginx)

* [Update certificates on Opensearch](#update-certs-elastic)

### Pre-requisites

The following items were used to test the custom certificate procedures:

* **Private key file**. The procedure uses a private key file **privkey.pem**.

* **Full trust chain**. The procedure also uses a full trust certificate chain, **fullchain.pem**.

* **Keystore password**. The procedure was tested using the keystore password is **Acc#1234**.

* **NGINX certificate**. The NGINX certificate must support subject alternative name (SAN) for the following domains:

  * **autoid-ui.\<domain-name>**

  * **autoid-jas.\<domain-name>**

  * **autoid-configuration-service.\<domain-name>**

  * **autoid-kibana.\<domain-name>**

  * **autoid-api.\<domain-name>**

* **Domain name**. The domain name used in the procedure below is `certupdate.autoid.me.` Change the value in various places to the domain name applicable to your deployment.

* **Ping Autonomous Identity version**. The procedures were tested on Ping Autonomous Identity versions 2021.8.5 and 2021.8.6.

### Update certificates on Cassandra

1. Create the Java keystore and truststore files for the server using `keytool.` The commands generate two JKS files: `cassandra-keystore.jks` and `cassandra-truststore.jks.` You need these files for configuring Cassandra and the Java API Service (JAS).

   ```
   openssl pkcs12 -export -in fullchain.pem -inkey privkey.pem -out server.p12 -name cassandranode

   keytool -importkeystore -deststorepass Acc#1234 -destkeypass Acc#1234 -destkeystore cassandra-keystore.jks -srckeystore server.p12 -srcstoretype PKCS12 -srcstorepass Acc#1234 -alias cassandranode

   keytool -importcert -keystore cassandra-truststore.jks -alias rootCa -file fullchain.pem -noprompt -keypass Acc#1234 -storepass Acc#1234
   ```

2. Create the client certificate. The client certificate is used by external clients, such as JAS and `cqlsh` to authenticate to Cassandra. In the following example, use the same client certificate for the Cassandra nodes to authenticate with each other.

   |   |                                                                          |
   | - | ------------------------------------------------------------------------ |
   |   | You can create a different certificate, if desired, using similar steps. |

   ```
   # Create client.conf with following contents
   [ req ]
   distinguished_name = CA_DN
   prompt             = no
   default_bits       = 2048

   [ CA_DN ]
   C  = cc
   O  = eng
   OU = cass
   CN = CA_CN

   # Create client key and CSR
   openssl req -newkey rsa:2048 -nodes -keyout client.key -out signing_request.csr -config client.conf

   # Create client certificate
   openssl x509 -req -CA fullchain.pem -CAkey privkey.pem -in signing_request.csr -out client.crt -days 3650 -CAcreateserial

   # Import client cert into a Java keystore for JAS
   openssl pkcs12 -export -in client.crt -inkey client.key -out client.p12 -name jas

   keytool -importkeystore -deststorepass Acc#1234 -destkeypass Acc#1234 -destkeystore client-keystore.jks -srckeystore client.p12 -srcstoretype PKCS12 -srcstorepass Acc#1234 -alias jas
   ```

3. View the files that are needed in later steps:

   ```
   $ ls -1 .

   cassandra-keystore.jks
   cassandra-truststore.jks
   client.conf
   client.crt
   client.key
   client-keystore.jks
   client.p12
   fullchain.pem
   fullchain.srl
   privkey.pem
   server.p12
   signing_request.csr
   ```

4. Copy the following files to the `/opt/autoid/apache-cassandra-3.11.2/conf/certs` directory on each Cassandra node:

   * **cassandra-keystore.jks**

   * **cassandra-truststore.jks**

   * **client-keystore.jks**

5. Copy the following files to the `<autoid-user-home-dir>/.cassandra` directory on each Cassandra node:

   * **client.key**

   * **client.crt**

   * **fullchain.pem**

6. Make the following edits in the `/opt/autoid/apache-cassandra-3.11.2/conf/cassandra.yaml` file on each Cassandra node:

   1. Change the keystore and truststore paths in the `server_encryption_options` and `client_encryption_options` sections:

      ```
      keystore: /opt/autoid/apache-cassandra-3.11.2/conf/certs/client-keystore.jks
      truststore: /opt/autoid/apache-cassandra-3.11.2/conf/certs/cassandra-truststore.jks
      ```

7. Update the `<autoid-user-home-dir>/.cassandra/cqlshrc` file with the following edits:

   ```
   [authentication]
   username = zoranuser
   password = <password>
   [connection]
   hostname = <ip address>
   factory = cqlshlib.ssl.ssl_transport_factory

   [ssl]
   certfile = <autoid-user-home-dir>/.cassandra/fullchain.pem
   validate = false
   version = SSLv23
   # Next 2 lines must be provided when require_client_auth = true in the cassandra.yaml file
   userkey = <autoid-user-home-dir>/.cassandra/client_key.key
   usercert = <autoid-user-home-dir>/.cassandra/client.crt
   ```

8. Restart Cassandra.

   ```
   ps auxf | grep cassandra
   kill <pid>
   cd /opt/autoid/apache-cassandra-3.11.2/bin
   nohup ./cassandra >/opt/autoid/apache-cassandra-3.11.2/cassandra.out 2>&1 &
   ```

9. Make sure that Cassandra is running normally using `cqlsh.` Use your server's IP. :

   ```
   $ cqlsh --ssl
   Connected to Zoran Cluster at <server-ip>:9042.
   [cqlsh 5.0.1 | Cassandra 3.11.2 | CQL spec 3.4.4 | Native protocol v4]
   Use HELP for help.
   zoranuser@cqlsh> describe keyspaces;

   autonomous_iam  system_auth  system_distributed  autoid_analytics
   autoid          system       system_traces       autoid_base
   system_schema   autoid_meta  autoid_staging

   zoranuser@cqlsh>
   ```

### Update certificates on MongoDB

1. Create the keystore and truststore using `keytool.`

   ```
   openssl pkcs12 -export -in fullchain.pem -inkey privkey.pem -out server.p12 -name mongonode

   keytool -importkeystore -deststorepass Acc#1234 -destkeypass Acc#1234 -destkeystore mongo-client-keystore.jks -srckeystore server.p12 -srcstoretype PKCS12 -srcstorepass Acc#1234 -alias mongonode

   keytool -importcert -keystore mongo-server-truststore.jks -alias rootCa -file fullchain.pem -noprompt -keypass Acc#1234 -storepass Acc#1234
   ```

2. Create a new mongodb.pem file.

   ```
   cat fullchain.pem privkey.pem > mongodb.pem
   ```

3. Download the `isg root x1` root certificate from Lets Encrypt at <https://letsencrypt.org/certs/isgrootx1.pem>, and save it as `rootCA.pem.`

4. Back up the MongoDB certificates.

   ```
   cd /opt/autoid/mongo/certs/
   mkdir backup
   mv mongodb.pem backup/
   mv rootCA.pem backup/
   mv mongo-*.jks backup
   ```

5. Copy the new certificates to the mongodb installation.

   ```
   cp mongodb.pem /opt/autoid/mongo/certs/
   cp rootCA.pem /opt/autoid/mongo/certs/
   ```

6. Restart Mongo DB.

   ```
   sudo systemctl stop mongo-autoid
   sudo systemctl start mongo-autoid
   ```

7. Check for logs for errors in `/opt/autoid/mongo/mongo-autoid.log.` The log may show connection errors until JAS has been updated and restarted.

8. Add the hostname to the hosts file. For example, we are using: `autoid-mongo.certupdate.autoid.me.`

9. Check the MongoDB connection from the command line.

   ```
   mongo --tls --host autoid-mongo.certupdate.autoid.me --tlsCAFile /opt/autoid/mongo/certs/rootCA.pem --tlsCertificateKeyFile /opt/autoid/mongo/certs/mongodb.pem --username mongoadmin
   ```

10. Back up and copy the new keystore and truststore to JAS.

    ```
    cd /opt/autoid/mounts/jas
    mkdir backup
    mv mongo-*.jks backup

    cp mongo-server-truststore.jks /opt/autoid/mounts/jas
    cp mongo-client-keystore.jks /opt/autoid/mounts/jas
    ```

11. Update the JAS configuration. On each Docker manager and worker node, copy the following files to the `/opt/autoid/mount/jas` directory.

    * mongo-client-keystore.jks

    * mongo-server-truststore.jks

      |   |                                                                                  |
      | - | -------------------------------------------------------------------------------- |
      |   | The certificates must exist on all Docker nodes (all managers and worker nodes). |

12. On each Docker *manager* node, update `/opt/autoid/res/jas/docker-compose.yml` file and set the Mongo keystore, truststore, and host, and add the `extra_hosts` line as follows:

    ```
    MONGO_KEYSTORE_PATH=/db-certs/mongo-client-keystore.jks
    MONGO_TRUSTSTORE_PATH=/db-certs/mongo-server-truststore.jks
    MONGO_HOST=autoid-mongo.certupdate.autoid.me

    extra_hosts:
      - "autoid-mongo.certupdate.autoid.me:<ip of mongodb host>"
    ```

13. Restart JAS.

    ```
    docker stack rm jas nginx
    docker stack deploy -c /opt/autoid/res/jas/docker-compose.yml jas
    docker stack deploy -c /opt/autoid/res/nginx/docker-compose.yml nginx
    ```

14. Check JAS logs for errors.

    ```
    docker service logs -f jas_jasnode
    ```

### Update certificates on JAS

1. On each Docker manager and worker node, copy the following keystore and truststore files to `/opt/autoid/mounts/jas` directory:

   * client-keystore.jks

   * cassandra-truststore.jks

2. On each Docker *manager* node, update `/opt/autoid/res/jas/docker-compose.yml` with the correct keystore and truststore paths:

   ```
   CASSANDRA_KEYSTORE_PATH=/db-certs/client-keystore.jks
   CASSANDRA_TRUSTSTORE_PATH=/db-certs/cassandra-truststore.jks
   ```

3. Redeploy the JAS server.

   ```
   docker stack rm jas
   docker stack deploy jas -c /opt/autoid/res/jas/docker-compose.yml
   ```

4. Make sure JAS has no errors.

   ```
   docker service logs -f jas_jasnode
   ```

### Update the certificates on NGINX

1. Copy the following files to `/opt/autoid/mounts/nginx/cert/`:

   * privkey.pem

   * fullchain.pem

2. In the `/opt/autoid/mounts/nginx/nginx.conf` file, update the `ssl_certificate` and `ssl_certificate_key` properties as follows:

   ```
   #SSL Settings
   ssl_certificate         /etc/nginx/cert/fullchain.pem;
   ssl_certificate_key     /etc/nginx/cert/privkey.pem;
   ```

3. Make sure that the domain names in the configuration files (`/opt/autoid/mounts/nginx/conf.d`) matches the domain names used for certificate generation.

4. Restart the Docker container.

   ```
   docker stack rm nginx
   docker stack deploy -c /opt/autoid/res/nginx/docker-compose.yml nginx
   ```

### Update certificates on Opensearch

1. Create a keystore and truststore using `keystore`.

   ```
   openssl pkcs12 -export -in fullchain.pem -inkey privkey.pem -out server.p12 -name esnodekey

   keytool -importkeystore -deststorepass Acc#1234 -destkeypass Acc#1234 -destkeystore elastic-client-keystore.jks -srckeystore server.p12 -srcstoretype PKCS12 -srcstorepass Acc#1234 -alias esnodekey

   keytool -importcert -keystore elastic-server-truststore.jks -alias rootCa -file fullchain.pem -noprompt -keypass Acc#1234 -storepass Acc#1234
   ```

2. Create backups.

   ```
   cd /opt/autoid/certs/elastic
   mkdir backup
   mv *.jks backup
   ```

3. Copy the new jks files, `fullchain.pem`, `privkey.pem`, and `chain.pem` to `/opt/autoid/certs/elastic`.

4. Also, copy the `fullchain.pem`, `privkey.pem`, and `chain.pem` certificates to `/opt/autoid/elastic/Opensearch-1.3.13/config/.`

5. Update the following attributes in the `/opt/autoid/elastic/Opensearch-1.3.13/config/elasticsearch.yml` file:

   ```
   Opensearch_security.ssl.transport.pemcert_filepath: fullchain.pem
   Opensearch_security.ssl.transport.pemkey_filepath: privkey.pem
   Opensearch_security.ssl.transport.pemtrustedcas_filepath: chain.pem

   Opensearch_security.ssl.http.pemcert_filepath: fullchain.pem
   Opensearch_security.ssl.http.pemkey_filepath: privkey.pem
   Opensearch_security.ssl.http.pemtrustedcas_filepath: chain.pem

   Opensearch_security.nodes_dn:

     - CN=elastic.certupdate.autoid.me
   ```

6. Restart Opensearch on all Opensearch nodes:

   ```
   sudo systemctl restart elastic
   ```

7. Check `/opt/autoid/elastic/logs/elasticcluster.log` for errors. The file shows any certificate error until all nodes have been restarted.

8. In the `/opt/autoid/res/jas/docker-compose.yml` file, add the following:

   ```
   extra_hosts:
   - "elastic.certupdate.autoid.me:<ip of ES host>"

   update ES_HOST env var:
   ES_HOST=elastic.certupdate.autoid.me
   ```

9. Restart the JAS container:

   ```
   docker stack rm jas
   docker stack rm nginx
   docker stack deploy -c /opt/autoid/res/jas/docker-compose.yml jas
   docker stack deploy -c /opt/autoid/res/nginx/docker-compose.yml nginx
   ```

10. Test the connection from the JAS container to Opensearch:

    ```
    docker container exec -it <jas container id> sh
    apk add curl
    curl -v --cacert /elastic-certs/fullchain.pem -u elasticadmin https://elastic.certupdate.autoid.me:9200
    ```

11. Update the configuration in the JAS service using curl:

    1. First log in using `curl`.

       ```
       curl -X POST https://autoid-ui.certupdate.autoid.me:443/api/authentication/login -k -H 'Content-Type: application/json' -H 'X-TENANT_ID: <tenant_id >' -d '{
       "username": "bob.rodgers@forgerock.com",
       "password": "Welcome123"
       }'
       ```

    2. Pull in the current configuration using `curl`.

       ```
       curl -k -H "Content-Type: application/json" -H 'X-TENANT-ID: <tenant_id>' -H 'Authorization: Bearer <bearer_token>' --request GET https://jasnode:10081/config/analytics_env_config
       ```

    3. Modify value for `elasticsearch" to "host":`elastic.certupdate.autoid.me\`\`.

    4. Push the updated configuration:

       ```
       curl -k  -H "Content-Type: application/json" -H 'X-TENANT-ID: <tenant_id>'  -H 'Authorization: Bearer <bearer_token>' --request PUT https://jasnode:10081/config/analytics_env_config -d '<updated json config>'
       ```

12. Update the environment variable in your `.bashrc` on all Opensearch nodes and Spark nodes:

    ```
    ES_HOST=elastic.certupdate.autoid.me
    ```

---

---
title: Exporting and Importing Data
description: If you are migrating data, for example, from a development server to a QA server, then follow this section to export your data from your current deployment. Ping Autonomous Identity provides a python script to export your data to .csv files and stores them to a folder in your home directory.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-export-import-data
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-export-import-data.html
section_ids:
  export-data: Export Your Data
  import-data: Import the Data into the Ping Autonomous Identity Keyspace
---

# Exporting and Importing Data

## Export Your Data

If you are migrating data, for example, from a development server to a QA server, then follow this section to export your data from your current deployment. Ping Autonomous Identity provides a python script to export your data to .csv files and stores them to a folder in your home directory.

1. On the target machine, change to the `dbutils` directory.

   ```
   $ cd /opt/autoid/dbutils
   ```

2. Export the database.

   ```
   $ python dbutils.py export ~/backup
   ```

## Import the Data into the Ping Autonomous Identity Keyspace

If you are moving your data from another server, import your data to the target environment using the following steps.

1. First, create a `zoran_user.cql` file. This file is used to drop and re-create the Ping Autonomous Identity `user` and `user_history` tables. The file should go to the same directory as the other .csv files. Make sure to create this file from the source node, for example, the development server, from where we exported the data.

   Start cqlsh in the source environment, and use the output of these commands to create the `zoran_user.cql` file:

   ```
   $ describe zoran.user;
   ```

   ```
   $ describe zoran.user_history;
   ```

   Make sure the `DROP TABLE` cql commands precedes the `CREATE TABLE` commands as shown in the `zoran_user.cql` example file below:

   ```
   USE zoran ;

   DROP TABLE IF EXISTS  zoran.user_history ;

   DROP TABLE IF EXISTS zoran.user ;

   CREATE TABLE zoran.user (
       user text PRIMARY KEY,
       chiefyesno text,
       city text,
       costcenter text,
       isactive text,
       jobcodename text,
       lineofbusiness text,
       lineofbusinesssubgroup text,
       managername text,
       usrdepartmentname text,
       userdisplayname text,
       usremptype text,
       usrmanagerkey text
   ) WITH bloom_filter_fp_chance = 0.01
       AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
       AND comment = ''
       AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
       AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
       AND crc_check_chance = 1.0
       AND dclocal_read_repair_chance = 0.1
       AND default_time_to_live = 0
       AND gc_grace_seconds = 864000
       AND max_index_interval = 2048
       AND memtable_flush_period_in_ms = 0
       AND min_index_interval = 128
       AND read_repair_chance = 0.0
       AND speculative_retry = '99PERCENTILE';

   CREATE TABLE zoran.user_history (
       user text,
       batch_id int,
       chiefyesno text,
       city text,
       costcenter text,
       isactive text,
       jobcodename text,
       lineofbusiness text,
       lineofbusinesssubgroup text,
       managername text,
       usrdepartmentname text,
       userdisplayname text,
       usremptype text,
       usrmanagerkey text,
       PRIMARY KEY (user, batch_id)
   ) WITH CLUSTERING ORDER BY (batch_id ASC)
       AND bloom_filter_fp_chance = 0.01
       AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
       AND comment = ''
       AND compaction = {'class': 'org.apache.cassandra.db.compaction.SizeTieredCompactionStrategy', 'max_threshold': '32', 'min_threshold': '4'}
       AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
       AND crc_check_chance = 1.0
       AND dclocal_read_repair_chance = 0.1
       AND default_time_to_live = 0
       AND gc_grace_seconds = 864000
       AND max_index_interval = 2048
       AND memtable_flush_period_in_ms = 0
       AND min_index_interval = 128
       AND read_repair_chance = 0.0
       AND speculative_retry = '99PERCENTILE';
   ```

2. Copy the `ui-config.json` from the source environment where you ran an analytics pipeline, usually under `/data/config,` to the same folder where you have your .csv files.

3. On the target machine, change to the `dbutils` directory.

   ```
   $ cd /opt/autoid/dbutils
   ```

4. Use the `dbutils.py import` command to populate the Ping Autonomous Identity keyspace with the .csv files, generated from the `export` command from the source environment using the previous steps. Note that before importing the data, the script truncates the existing tables to remove duplicates. Again, make sure the `zoran_user.cql` and the `ui-config.json` are in the `/import-dir`.

   ```
   $ python dbutils.py import /import-dir
   ```

   For example:

   ```
   $ python dbutils.py import ~/import/AutoID-data
   ```

5. Verify that the data is imported in the directory on your server.

---

---
title: Features
description: Ping Autonomous Identity provides the following features:
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-autoid-features
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-autoid-features.html
---

# Features

Ping Autonomous Identity provides the following features:

* **Broad Support for Major Identity Governance and Administration (IGA) Providers**. Ping Autonomous Identity supports a wide variety of Identity as a Service (IDaaS) and Identity Management (IDM) data including but not limited to comma-separated values (CSV), Lightweight Directory Access Protocol (LDAP), human resources (HR), database, and IGA solutions.

* **Highly-Scalable Architecture**. Ping Autonomous Identity deploys using a microservices architecture, either on-prem, cloud, or hybrid-cloud environments. Ping Autonomous Identity's architecture supports scalable reads and writes for efficient processing.

* **Powerful UI dashboard**. Ping Autonomous Identity displays your company's entitlements graphically on its UI console. You can immediately investigate those entitlement outliers as possible security risks. The UI also lets you quickly identify those entitlements that are good candidates for automated low-risk approvals or re-certifications. Users can also view a trend-line indicating how well they are managing their entitlements. The UI also provides an application-centric view and a single-page rules view for a different look at your entitlements.

* **Powerful Analytics Engine**. Ping Autonomous Identity's analytics engine is capable of processing millions of access points within a short period of time. Ping Autonomous Identity lets you configure the machine learning process and prune less productive rules. Customers can run analyses, predictions, and recommendations frequently to improve the machine learning process.

* **UI-Driven Schema Extension**. Ping Autonomous Identity lets administrators discover and extend the schema, and set up attribute mappings using the UI.

* **UI-Driven Data Ingestion and Mappings**. Ping Autonomous Identity provides improved data ingestion tools to define multiple csv input files needed for analysis and their attribute mappings to the schema using the UI.

* **UI-Driven Data Ingestion and Mappings**. Ping Autonomous Identity provides improved data ingestion tools to define multiple csv input files needed for analysis and their attribute mappings to the schema using the UI.

* **Broad Database Support**. Ping Autonomous Identity supports both Apache Cassandra and MongoDB databases. Both are highly distributed databases with wide usage throughout the industry.

* **Improved Search Support**. Ping Autonomous Identity now incorporates Opensearch, a distributed, open-source search engine based on Lucene, to improve database search results and performance.

---

---
title: Manage identities
description: The Manage Identities page lets administrators add or edit, assign roles, and deactivate users to Ping Autonomous Identity.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-manage-identities
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-manage-identities.html
section_ids:
  view-default-roles: View the default roles
  create_a_new_user: Create a new user
  reset_a_users_password: Reset a user's password
  add_a_role_to_an_existing_user: Add a role to an existing user
  deactivate_an_existing_user: Deactivate an existing user
---

# Manage identities

The Manage Identities page lets administrators add or edit, assign roles, and deactivate users to Ping Autonomous Identity.

## View the default roles

1. On the Ping Autonomous Identity UI, click the administration icon on the navigation menu, and then click Manage.

2. On the Manage Identities page, click Roles.

3. Select a specific role, and then click Edit to view its details.

4. Click through the Details and Permissions to view its details. You cannot change the permissions in these roles.

5. Click Role Members to access the members associated with this role. If you want to add a user to this Role group, click New Role Member and enter the user's name. You can enter multiple users. When finished, click Save.

   > **Collapse: Click an example**
   >
   > ![manage identities view roles](_images/manage-identities-view-roles.gif)

## Create a new user

1. On the Ping Autonomous Identity UI, click the administration icon on the navigation menu, and then click Manage.

2. On the Manage Identities page, click New User.

3. Enter the Display Name, Email Address, DN, Gid Number, Uid, and Password for the user.

4. Click Save.

5. Click Authorization Roles, and then click New Authorization Roles. This step is important to assign the proper role to the user.

6. Select a role to assign the user, and then click Save.

   > **Collapse: Click an example**
   >
   > ![manage identities new user](_images/manage-identities-new-user.gif)

## Reset a user's password

1. On the Ping Autonomous Identity UI, click the administration icon on the navigation menu, and then click Manage.

2. On the Manage Identities page, search for a user.

3. For a specific user, click Edit.

4. Click Reset Password, enter a temporary password, and then click Save.

   > **Collapse: Click an example**
   >
   > ![manage identities reset password](_images/manage-identities-reset-password.gif)

## Add a role to an existing user

Often administrators need to assign roles to existing members. There are two ways to do this: from the user's detail page and through the role's Role Members page (refer to [View the default roles](#view-default-roles)).

1. On the Ping Autonomous Identity UI, click the administration icon on the navigation menu, and then click Manage.

2. On the Manage Identities page, search for a user.

3. For a specific user, click Edit.

4. Click Authorization Roles, and then click New Authorization Roles.

5. Select one or more roles to add, and then click Save.

   > **Collapse: Click an example**
   >
   > ![manage identities add role](_images/manage-identities-add-role.gif)

## Deactivate an existing user

1. On the Ping Autonomous Identity UI, click the administration icon on the navigation menu, and then click Manage.

2. On the Manage Identities page, search for a user.

3. For a specific user, click Deactivate. The user's status changes to "In-active".

   > **Collapse: Click an example**
   >
   > ![manage identities deactivate](_images/manage-identities-deactivate.gif)

---

---
title: Overview of the Deployment Process
description: Ping Autonomous Identity provides a flexible and modular architecture that lets you deploy it in a variety of network environments. The deployment process does involve a number steps necessary to run accurate analyses of a company's entitlements.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-deployment-process
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-deployment-process.html
---

# Overview of the Deployment Process

Ping Autonomous Identity provides a flexible and modular architecture that lets you deploy it in a variety of network environments. The deployment process does involve a number steps necessary to run accurate analyses of a company's entitlements.

This chapter presents a summary of the overall deployment process to get an Ping Autonomous Identity system up-and-running.

> **Collapse: Click to display an illustration of the deployment process**
>
> ![auto-id-deployment-path](_images/auto-id-deployment-path.png)

---

---
title: Prepare Configuration File
description: "Before you can install Ping Autonomous Identity, update the configuration file, zoran.yml with changes specific to your deployment. The configuration file is located at: /opt/zoran/python-3.6/bin/. For reference to the zoran.yml file, refer to [admin-guide:]."
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:admin-guide:chap-prepare-config-file
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/admin-guide/chap-prepare-config-file.html
---

# Prepare Configuration File

Before you can install Ping Autonomous Identity, update the configuration file, `zoran.yml` with changes specific to your deployment. The configuration file is located at: `/opt/zoran/python-3.6/bin/`. For reference to the `zoran.yml` file, refer to [\[admin-guide:\]](#admin-guide:).

Make the following changes:

1. **Set the base path**. The base path is the path on the machine where all client data and output should reside.

   * If using a multi-machine environment, this path will be on the shared mount; for example, `/shared/`.

   * For single machine environment, the base path is set to a folder within the root directory; for example, `/data/`.

2. **Set the input and output paths**. These paths are set up to allow for multiple analytics runs. The paths should be relative to the base path. The best file structure is to set the output path to exist within the input path, as some analytics outputs are used as inputs for various reporting scripts.

3. **Configure database connection**. Follow these substeps:

   1. Select the relevant database (for example, cassandra).

   2. Configure the database IP address and port number.

   3. If using SSL encryption, the SSL flag needs to be set to `TRUE` and the configuration file must be pointed to the four SSL certificates that exists on the analytics machine. If SSL is not being used, then set the SSL flag to `FALSE`.
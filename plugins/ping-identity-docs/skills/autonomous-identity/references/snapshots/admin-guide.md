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

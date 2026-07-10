---
title: About Performance Tuning
description: This section shows you to how to fine-tune a few simple application and system level settings to enable PingFederate to achieve maximum performance of the hardware chosen for your deployment.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_about_performance_tuning
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_about_performance_tuning.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# About Performance Tuning

This section shows you to how to fine-tune a few simple application and system level settings to enable PingFederate to achieve maximum performance of the hardware chosen for your deployment.

The default configuration since PingFederate 10.2 is acceptable for most small size deployments. Mission-critical and high-transaction volume deployments might require additional tuning.

This guide addresses several areas of tuning such as logging, concurrency, memory, and Java-specific tuning options. It is not designed as a one-size-fits-all set of instructions to optimize PingFederate, but more as a checklist of suggestions for areas of the product that can be tuned to improve performance, and any tradeoffs associated with those changes. For ultimate reassurance that any fine-tuned settings will meet your expectations, performance testing in a lab environment is recommended.

---

---
title: Concurrency
description: This section describes how to configure PingFederate to support more concurrent requests to optimize your deployment.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_concurrency
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_concurrency.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  caveats: Caveats
---

# Concurrency

This section describes how to configure PingFederate to support more concurrent requests to optimize your deployment.

The more requests processed in parallel, the more requests processed over all. Given the appropriate amount of hardware, processing *N* requests concurrently is typically faster than processing *N* requests serially.

In PingFederate, there are two main pools of threads that control the level of concurrent user requests: Acceptor Threads and Server Threads. Acceptor threads receive the HTTPS requests and pass those requests on to available server threads to be processed.

## Caveats

This topic serves as a guideline for optimizing the concurrency of your deployment. On a large system with multiple CPUs, or cores, a thread pool that is too small will under-utilize the available processor resources. A thread pool that is too large can cause the system to become flooded and unusable.

A good target for the CPU is between 60%-80% utilization when under nominal, standard user load. This way CPU resources are not under-utilized while still allowing room for occasional load spikes. The level of concurrency in PingFederate might need to be decreased, or even increased, depending on the system's configuration, the adapters in use, available memory, and other processes competing for resources. All deployments are different. This section serves as a guideline of where to start when tuning the server.

---

---
title: Configuration at scale
description: You can configure PingFederate to improve the administrative-console experience for your scaling needs.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_config_at_scale
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_config_at_scale.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Configuration at scale

You can configure PingFederate to improve the administrative-console experience for your scaling needs.

For deployments that have hundreds of connections or OAuth clients, or both, and observe noticeable delays in the administrative console, administrators can optionally configure PingFederate to create configuration archives during off-peak hours and disable automatic connection validation to improve the administrative-console experience.

## Related links

* [Configuring a backup schedule](../administrators_reference_guide/pf_config_backup_schedule.html)

* [Configuring automatic connection validation](../administrators_reference_guide/pf_configuring_automatic_connection_validation.html)

---

---
title: Configuring connection pools to datastores
description: Java Database Connectivity (JDBC) and LDAP datastores use connection pooling to improve the performance and efficiency of communicating with external systems. For optimal performance, a number of connections are required to handle most or all the requests in parallel.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_config_connec_pool_to_datastor
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_config_connec_pool_to_datastor.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 8, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring connection pools to datastores

Java Database Connectivity (JDBC) and LDAP datastores use connection pooling to improve the performance and efficiency of communicating with external systems. For optimal performance, a number of connections are required to handle most or all the requests in parallel.

## About this task

In the **Data & Credential Stores** page, set the minimum and maximum values for connection pools to JDBC and LDAP data stores.

Connection pools improve efficiency by maintaining persistent connections to the JDBC or LDAP server preventing the expense of creating the connection on demand. Connection pools also allow more control over the load placed on the back-end server. It might not be necessary to have a connection available for every concurrent request received by the server, but having too few available will cause requests to wait when accessing JDBC and LDAP resources.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Size the connection pool based on the capacity and limitation of the database or LDAP server. Sizing the connection pool beyond the capability of the back-end server could lead to PingFederate flooding the datastore without any performance improvement. For optimal performance, size connection pools large enough to handle between 50% and 100% of the number of concurrent requests the server is expected to encounter often. Learn more about optimizing the connection pool in [Best practices for tuning the JDBC connection pool](https://support.pingidentity.com/s/article/Best-practices-for-tuning-the-JDBC-Connection-Pool) in the Ping Identity Knowledge Base. |

## Steps

1. Choose from configuring connection pools to JDBC or LDAP datastores:

   | Datastore type                                  | Configuration steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Configuring connection pools to JDBC datastores | 1. Go to **System > Data & Credential Stores > Data Stores**, and select the applicable JDBC datastore.

   2. Go to **Database Config > Advanced**.

   3. On the **Advanced Database Options** page:

      1. Set the **Minimum Pool Size** value to 50% of the `maxThreads` value.

      2. Set the **Maximum Pool Size** value to between 75% and 100% of the `maxThreads` value, subject to the capability of the back-end database server.&#xA;&#xA;The maxThreads value is defined in the \<pf\_install>/pingfederate/etc/run.properties file. Learn more in Tuning the server thread pool. |
   | Configuring connection pools to LDAP datastores | 1) Go to **System > Data & Credential Stores > Data Stores**, and select the applicable LDAP datastore.

   2) Go to the **LDAP Configuration > Advanced > Advanced LDAP Options**.

   3) Set the **Minimum Connections** value to 50% of the `maxThreads` value.

   4) Set the **Maximum Connections** value to between 75% and 100% of the `maxThreads` value, subject to the capability of the back-end database server.                                                                                                                                                                     |

2. For a clustered PingFederate environment, replicate the changes to all engine nodes on the **System > Server > Cluster Management** page.

---

---
title: Configuring HTTP connection pools
description: Optimize connections with external services by adjusting the number and duration of connections.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_configuring_http_connection_pool
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_configuring_http_connection_pool.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  about-this-task: About this task
  steps: Steps
  http-connection-pool-settings: HTTP connection pool settings
---

# Configuring HTTP connection pools

Optimize connections with external services by adjusting the number and duration of connections.

## About this task

PingFederate uses an HTTP connection pool to communicate with external systems, including PingOne communication, Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* gateways, some PingFederate adapters, and many other functions.

Most environments don't need to tune HTTP connection pool values. Before you adjust timeout values, first investigate network latency, external-system capacity, and overall environment sizing.

If you tune the HTTP connection pool, adjust and test `max-connections` and `max-connections-per-route` first.

Use `pf.runtime.threads.max` as the starting point for sizing HTTP connection pools, represented as `M`. Because PingFederate maintains persistent connections, set `max-connections-per-route` to `M`. If the busiest flow can call `D` external destinations, set `max-connections` to `M × D` as a worst-case starting point. This helps prevent one high-volume route from delaying other routes.

In a clustered environment with `P` PingFederate engines, an external system might need up to `P × M` concurrent connections. Before you increase these values, verify that the external system can handle the concurrent load. Size the pool according to the capacity and limits of the back-end system, because increasing pool sizes beyond back-end capacity can increase load without improving performance.

Also ensure that the PingFederate host environment can support the additional resource usage, including open file limits and thread stack settings. Thread memory usage varies by operating system, architecture, and runtime behavior, so avoid assuming a fixed per-thread amount. When you scale connection pools, consider the cumulative committed-memory impact of many concurrent threads and datastore *(tooltip: \<div class="paragraph">
\<p>A database or directory location containing user account records and associated user attributes.\</p>
\</div>)* operations. If memory demand grows beyond available system memory, the operating system might terminate the process.

Learn more about sizing `pf.runtime.threads.max` in [Tuning the server thread pool](pf_tuning_server_thread_pool.html), and learn more about connection pool behavior and back-end capacity in [Configuring connection pools to datastores](pf_config_connec_pool_to_datastor.html).

## Steps

1. In a text editor, open the `<pf_install>/pingfederate/server/default/data/config-store/http-connection-pooling-manager.xml` file.

2. Modify the appropriate setting in `http-connection-pooling-manager.xml`. Refer to the HTTP connection pool settings table for more information.

3. (Optional) Update an HTTP connection pool setting by using a REST request to the PingFederate administrative API. Learn more in [Accessing the API interactive documentation](../developers_reference_guide/pf_access_api_interact_documentation.html).

4. If you updated the file directly, save and close the file.

5. Restart PingFederate.

6. For a clustered PingFederate environment, perform these steps on the administrative console node. Then go to **System > Server > Cluster Management** and click **Replicate**. Learn more in [Replicating configurations](../administrators_reference_guide/pf_replicat_config.html).

## HTTP connection pool settings

The `http-connection-pooling-manager.xml` file contains the following HTTP connection pool settings:

| Setting                     | Default value | Description                                                                                         |
| --------------------------- | ------------- | --------------------------------------------------------------------------------------------------- |
| `max-connections`           | `350`         | The maximum number of connections in the pool.                                                      |
| `max-connections-per-route` | `100`         | The maximum number of connections per route (port or URL).                                          |
| `connection-timeout`        | `60000`       | The time, in milliseconds, available to establish a connection with the remote host.                |
| `request-timeout`           | `120000`      | The time, in milliseconds, available to retrieve a connection from the connection pool.             |
| `connection-idle-timeout`   | `30000`       | The time, in milliseconds, that a connection can stay idle before cleanup.                          |
| `keepalive-timeout`         | `1000`        | The time, in milliseconds, that a connection can stay idle before it returns to the pool for reuse. |
| `cleanup-delay-secs`        | `10`          | The delay, in seconds, before the HTTP client cache is cleaned up.                                  |

---

---
title: Fine-tuning JVM options
description: Edit the JVM options jvm-memory.options file to customize minimum and maximum heap sizing, garbage collection, and generation specific sizing for your memory use and to optimize PingFederate's performance.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_fine_tuning_jvm_option
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_fine_tuning_jvm_option.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 30, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
---

# Fine-tuning JVM options

Edit the JVM options `jvm-memory.options` file to customize minimum and maximum heap sizing, garbage collection, and generation specific sizing for your memory use and to optimize PingFederate's performance.

## About this task

PingFederate reads Java virtual machine (JVM) options from the `jvm-memory.options` file, located in the `<pf_install>/pingfederate/bin` directory. Any manual modifications or additions should be made in this file. For more information on JVM tuning options, see [HotSpot Virtual Machine Garbage Collection Tuning Guide](https://docs.oracle.com/en/java/javase/11/gctuning/index.html) in the Oracle documentation.

|   |                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before making any edits to the file, consider the following:- Make a backup copy prior to any manual edits.

- The empty lines and comments, indicated by a leading `#` character, are ignored.

- JVM options do not need a specific organization or order.

- You can add any JVM flag to the file to configure and customize the JVM, not just memory-related options. |

## Steps

1. Edit the `<pf_install>/pingfederate/bin/jvm-memory.options` file.

2. To add additional JVM options, insert the applicable options to the file.

   ### Example:

   For example, to enable the aggressive options flag, configure the file as follows.

   ```
   ...

   # Enable the aggressive options flag
   -XX:+AggressiveOpts
   ```

   The comment is optional.

3. When finished, save your changes.

4. If PingFederate is configured to run as a service on a Windows server, follow these steps:

   1. Open command prompt and go to the `<pf_install>/pingfederate/sbin/wrapper` directory.

   2. Run `generate-wrapper-jvm-options.bat`.

      ### Result:

   This helper utility reads the JVM options from the `jvm-memory.options` file and creates a resource file that the PingFederate Windows service requires to configure its JVM options.

   1. Close the command prompt.

5. Restart PingFederate.

6. For a clustered PingFederate environment, repeat these steps on each engine node as needed.

---

---
title: Hardware security modules
description: When configuring PingFederate to use a hardware security module, be aware of the following performance impact considerations.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_hardware_secur_modules
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_hardware_secur_modules.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  performance-considerations: Performance considerations
---

# Hardware security modules

When configuring PingFederate to use a hardware security module, be aware of the following performance impact considerations.

You can configure PingFederate to use a hardware security module (HSM) for cryptographic material storage and operations. When configured, private keys and their corresponding certificate are stored on the HSM. Related signing and decryption operations are processed there for enhanced security. By default, even in HSM mode, dynamic OAuth and OpenID Connect signing and decryption keys are generated and stored in the memory of PingFederate cluster nodes. To ensure continuity after a full cluster restart, the decryption keys are also persisted to disk, and encrypted there with PingFederate's active [configuration encryption key](../administrators_reference_guide/pf_managing_configuration_encryption_keys.html). To ensure OAuth and OpenID Connect keys are instead stored on the HSM, you must [enable static keys](../administrators_reference_guide/pf_config_static_signing_keys.html).

For more information on supported configurations for secure material storing and processing, see [Supported hardware security modules](../getting_started_with_pingfederate/pf_supported_hardware_security_modules.html).

## Performance considerations

Configuring PingFederate to use an HSM for cryptographic material storage and operations can introduce an impact on performance. The level of impact depends on the performance of cryptographic functionality provided by the HSM and the network latency between PingFederate and the HSM. Consult your HSM vendor for performance tuning and optimization recommendations if you plan to use an HSM as part of your PingFederate deployment.

---

---
title: JVM heap
description: The most important tuning for the Java Virtual Machine (JVM) is the size of the heap memory, which ensures adequate memory is available to manage garbage collection and optimize overall performance.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_jvm_heap
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_jvm_heap.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 30, 2022
section_ids:
  additional-considerations: Additional considerations
---

# JVM heap

The most important tuning for the Java Virtual Machine (JVM) is the size of the heap memory, which ensures adequate memory is available to manage garbage collection and optimize overall performance.

If the demands require more memory than what is currently available, the JVM must grow the heap, if it can, or perform garbage collection to provide memory to allocate. Resizing the heap and garbage collecting can be an expensive processes and negatively impact performance. Sizing the heap to ensure an adequate amount of memory is available but still manageable to garbage collection is important to optimize overall performance.

PingFederate attempts to optimize JVM heap and garbage collector settings at the time of installation and upgrade. Regardless of available memory, PingFederate uses the Garbage-First (G1) garbage collector (GC). These settings assume PingFederate will be the only service on the server and consume a majority of the memory. Depending on your environment, you can override these settings at a later time.

## Additional considerations

The JVM can grow the heap from the minimum heap variable value up to the maximum heap variable value. However, growing the heap is often an expensive exercise and requests memory from the operating system. In addition, the JVM must also reorganize the heap to account for the memory being added. To conserve memory in your deployment, set a lower value for the minimum heap than that of the maximum heap to ensure you are not reserving unused memory. If you have enough memory that a certain amount is easily earmarked for the PingFederate server, adjust the size of the heap by setting the minimum heap and maximum heap to the same value. This allows the JVM to reserve its entire heap and decrease the amount of resizing that the JVM needs to perform if the amount of memory in use exceeds the value of the minimum heap.

---

---
title: Linux tuning
description: Follow these recommendations for your Linux environment to prevent deployment issues, to increase the performance and capacity of the networking stack, particularly TCP and the file descriptor usage, and to enable PingFederate to handle a high volume of concurrent requests.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_linux_tuning
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_linux_tuning.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  networktcp-tuning: Network/TCP tuning
  increase-file-descriptor-limits: Increase file descriptor limits
---

# Linux tuning

Follow these recommendations for your Linux environment to prevent deployment issues, to increase the performance and capacity of the networking stack, particularly TCP and the file descriptor usage, and to enable PingFederate to handle a high volume of concurrent requests.

## Network/TCP tuning

For `SystemV`, add or modify the following entries in the `/etc/sysctl.conf` file.

For `systemd`, you can create a sysctl preload/configuration file in `/etc/sysctl.d` (for example, `99-sysctl.conf`) in which to add and modify the following entries.

```
#TCP Tuning#
# Controls the use of TCP syncookies (default is 1)
# and increase the number of outstanding syn requests allowed.
net.ipv4.tcp_syncookies=1
net.ipv4.tcp_max_syn_backlog=8192

# Increase number of incoming connections.
# somaxconn defines the number of request_sock structures allocated
# per each listen call.
# The queue is persistent through the life of the listen socket.
net.core.somaxconn=4096

# Increase number of incoming connections backlog queue.
# Sets the maximum number of packets, queued on the INPUT side,
# when the interface receives packets faster
# than kernel can process them.
net.core.netdev_max_backlog=65536

# increase system IP port limits
net.ipv4.ip_local_port_range=2048 65535

# Turn on window scaling which can enlarge the transfer window:
net.ipv4.tcp_window_scaling=1

# decrease TCP timeout
net.ipv4.tcp_fin_timeout=10

# Allow reuse of sockets in TIME_WAIT state for new connections
# (While this may increase performance, use with caution according
# to the kernel documentation.  This setting should only be enabled
# after the system administrator reviews security considerations.)
net.ipv4.tcp_tw_reuse=1

# Increase the read and write buffer space allocatable
# (minimum size, initial size, and maximum size in bytes)
net.ipv4.tcp_rmem = 4096 65536 16777216
net.ipv4.tcp_wmem = 4096 65536 16777216

# The maximum number of packets which may be queued
# for each unresolved address by other network layers
net.ipv4.neigh.default.unres_qlen=100
net.ipv4.neigh.eth0.unres_qlen=100
net.ipv4.neigh.em1.unres_qlen=100

# Default Socket Receive and Write Buffer
net.core.rmem_default=8388608
net.core.wmem_default=8388608
```

## Increase file descriptor limits

Add or modify the following lines in the `/etc/security/limits.conf` file where *pf\_user* is the user account used to run the PingFederate java process or `*` for all user accounts.

```
pf_user  soft nofile 10400
 pf_user  hard nofile 10400
```

---

---
title: Logging
description: This section explains the logging practices of PingFederate and discusses minimizing the system's overall performance impact.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_logging
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_logging.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Logging

This section explains the logging practices of PingFederate and discusses minimizing the system's overall performance impact.

Logging tracks various aspects of the system's overall performance and requires a certain amount of system resources, which affects the system's overall performance. In particular, writing to the log files takes the greatest amount of resources. To minimize the performance impact, PingFederate uses the high-performance asynchronous logger from Log4j 2 for logging runtime and administrative events, including status and error messages used for troubleshooting. To preserve transactional integrity, audit information logs synchronously.

Although the bulk of logging is executed asynchronously, decreasing the amount of information written to log files always provides the best possible performance.

PingFederate only records messages tagged with log level `INFO`, `WARN`, `ERROR`, and `FATAL` to the server log and the provisioner log. Messages with `DEBUG`, or `TRACE` tags, are not recorded to optimize performance. Console logging is also disabled for the same reason.

For troubleshooting purposes, you can enable console logging or [verbose messages](../administrators_reference_guide/help_logsettingstasklet_logsettingsstate.html).

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you no longer require console logging or verbose messages, turn them off. On Windows, never highlight the console output because it might slow or stop PingFederate from processing requests. |

## Related links

* [Enabling console logging](../administrators_reference_guide/pf_enabling_debug_message_and_console_logging.html)

---

---
title: Memory
description: After the CPU, memory is the most important resource for sizing Java virtual machine (JVM) heap, managing garbage collection, and optimizing the overall performance of your PingFederate deployment.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_memory
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_memory.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Memory

After the CPU, memory is the most important resource for sizing Java virtual machine (JVM) heap, managing garbage collection, and optimizing the overall performance of your PingFederate deployment.

The Concurrency section describes how to configure PingFederate to support more concurrent requests. This section highlights how supporting increasing concurrency requests can affect PingFederate's performance because these requests require an increase in memory. Because PingFederate is a Java application, it is important to consider how tuning affects, or is affected by, garbage collection. This section is not a guide to garbage collection theory or ergonomics.

---

---
title: memoryoptions and installation
description: When the PingFederate installer for Windows runs the memoryoptions utility tool or when changes are made from a manual edit, expect the following behaviors to the installation medium.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_memoryoptions_install
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_memoryoptions_install.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 13, 2023
---

# memoryoptions and installation

When the PingFederate installer for Windows runs the `memoryoptions` utility tool or when changes are made from a manual edit, expect the following behaviors to the installation medium.

The PingFederate installer for Windows runs the `memoryoptions` utility in an attempt to optimize the Java virtual machine (JVM) heap. Regardless of available memory, PingFederate uses the Garbage-First (G1) garbage collector (GC). The script assumes that PingFederate will be the only service on the server and consume a majority of the memory.

The G1GC is designed to achieve high throughput while meeting its pause times goal for garbage collection, and the collector self-tunes by adjusting the size and nature of the various heap regions to meet the pause time goal. As needed, administrators can rerun the utility or manually edit these options at a later time.

When the PingFederate installer is executed for Windows or a subsequent rerun of the `memoryoptions` utility, it creates a backup copy of the current `jvm-memory.options` and records the G1GC options in the `jvm-memory.options` file. Changes made as a result of the execution of the utility or a manual edit are activated after a restart of PingFederate.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You should not use the `memoryoptions` script when you deploy PingFederate inside of a container. Instead, you should edit the `jvm-memory.options` file directly. In containers, you should use the `InitialRAMPercentage` and `MaxRAMPercentage` JVM options to control the size of the heap. |

See the following table for information regarding expected behaviors.

**PingFederate installation mediums and their expected behaviors from the execution of the memoryoptions utility tool**

| Installation medium                        | Expected behavior                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingFederate installer for Windows         | * The installer creates a new PingFederate installation.

* The installer runs the `memoryoptions` utility. Regardless of available memory, PingFederate uses the G1GC as a default. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory.

* The installer configures PingFederate to run as a service.

* The `memoryoptions` options are activated as the PingFederate service starts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PingFederate product distribution ZIP file | The default `jvm-memory.options` file becomes part of the new installation as program and default configuration files are extracted from the PingFederate product distribution `.zip` file.* PingFederate as a console application on Windows *or* as a console application or a service on Linux

  * The JVM options set in the default jvm-memory.options file are activated as PingFederate starts.

  * The default JVM options are conservative. For most deployment scenarios using various physical or virtual resources, run the `memoryoptions` utility. Regardless of available memory, PingFederate uses the G1GC. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory.

  * As a result of the execution of the memoryoptions utility or a manual edit of the jvm-memory.options file, the JVM options are activated as PingFederate restarts.

* PingFederate as a service on Windows

  * When administrators run the PingFederate service-installation program `install-service.bat`, located in the `<pf_install>/pingfederate/sbin/win-x86-64` directory, to install the PingFederate Windows service manually, the program runs the `memoryoptions` utility. Regardless of available memory, PingFederate uses the G1GC. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory. The service-installation program then runs a helper utility `generate-wrapper-jvm-options.bat`, located in the `<pf_install>/pingfederate/sbin/wrapper` directory, to read the JVM options from the `jvm-memory.options` file and create a resource file that the PingFederate Windows service requires to configure its JVM options

  * The default JVM options are activated as the PingFederate service starts. |

---

---
title: memoryoptions and upgrade
description: Upgrade paths behave differently when changes are executed based on the recommendations and execution of the memoryoptions utility tool.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_memoryoptions_upgrade
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_memoryoptions_upgrade.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 13, 2023
---

# memoryoptions and upgrade

Upgrade paths behave differently when changes are executed based on the recommendations and execution of the `memoryoptions` utility tool.

Depending upon the selected tool and whether the `jvm-memory.options` file exists in the source installation, the expected behavior of the `memoryoptions` utility differs. In general, the `jvm-memory.options` file from the source installation is preserved without new recommended values.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You should not use the `memoryoptions` script when you deploy PingFederate inside of a container. Instead, you should edit the `jvm-memory.options` file directly. In containers, you should use the `InitialRAMPercentage` and `MaxRAMPercentage` JVM options to control the size of the heap. |

See the following table for information regarding expected behaviors.

**PingFederate upgrade paths and their expected behaviors from the execution of the memoryoptions utility tool**

| Upgrade path                               | Expected behavior when thejvm-memory.optionsfile does not exist in the source installation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingFederate installer for Windows         | * The installer creates a new PingFederate installation.

* The installer runs the `memoryoptions` utility. Regardless of available memory, PingFederate uses the Garbage-First (G1) garbage collector (GC). The script assumes that PingFederate will be the only service on the server and consume a majority of the memory. The script records the defaults in the `jvm-memory.options` file.

* The installer configures PingFederate to run as a service.

* The recommended options are activated as the PingFederate service starts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PingFederate Upgrade Utility (upgrade.bat) | The upgrade utility creates a new PingFederate installation based on the source installation and the PingFederate product distribution `.zip` file.The default `jvm-memory.options` file becomes part of the new installation as the upgrade utility extracts files from the PingFederate product distribution `.zip`file.* PingFederate as a console application on Windows

  * The G1GC JVM options set in the default `jvm-memory.options` file are activated as PingFederate starts.

  * The default JVM options are conservative. For most deployment scenarios using various physical or virtual resources, run the `memoryoptions` utility. Regardless of available memory, PingFederate uses the G1GC. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory.

  * As a result of the execution of the memoryoptions utility or a manual edit of the jvm-memory.options file, the JVM options are activated as PingFederate restarts.

* PingFederate as a service on Windows

  * When administrators run the PingFederate service-installation program `install-service.bat`, located in the `<pf_install>/pingfederate/sbin/win-x86-64` directory, to install the PingFederate Windows service manually, the program runs the `memoryoptions` utility. Regardless of available memory, PingFederate uses the G1GC. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory. The service-installation program then runs a helper utility, `generate-wrapper-jvm-options.bat`, located in the `<pf_install>/pingfederate/sbin/wrapper` directory, to read the JVM options from the `jvm-memory.options` file and create a resource file that the PingFederate Windows service requires to configure its JVM options

  * The default options are activated as the PingFederate service starts. |
| PingFederate Upgrade Utility (upgrade.sh)  | - The upgrade utility creates a new PingFederate installation based on the source installation and the PingFederate product distribution zip file. The default `jvm-memory.options` file becomes part of the new installation as the upgrade utility extracts files from the PingFederate product distribution zip file.

- The JVM options set in the default `jvm-memory.options` file are activated as PingFederate starts.

- The default JVM options are conservative. For most deployment scenarios using various physical or virtual resources, run the `memoryoptions` utility. Regardless of available memory, PingFederate uses the G1GC. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory. The default options are recorded in the `jvm-memory.options` file.

- As a result of the execution of the `memoryoptions` utility or a manual edit of the `jvm-memory.options` file, the JVM options are activated as PingFederate restarts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

| Upgrade path                               | Expected behavior when the jvm-memory.optionsfile exists in the source installation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingFederate installer for Windows         | * The installer creates a new PingFederate installation based on the source installation and copies the `jvm-memory.options` file from the source installation to the new installation.

* At the end of the installation, the installer runs the PingFederate service-installation program, which runs a helper utility `generate-wrapper-jvm-options.bat`, located in the \<pf\_install>/pingfederate/sbin/wrapper directory, to read the JVM options from the `jvm-memory.options` file and create a resource file that the PingFederate Windows service requires to configure its JVM options.

* The preserved Java virtual machine (JVM) options are activated as the PingFederate service starts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PingFederate Upgrade Utility (upgrade.sh)  | - The installer creates a new PingFederate installation based on the source installation and copies the `jvm-memory.options` file from the source installation to the new installation.

- The preserved JVM options are activated as the PingFederate service starts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PingFederate Upgrade Utility (upgrade.bat) | The installer creates a new PingFederate installation based on the source installation and copies the `jvm-memory.options` file from the source installation to the new installation.- PingFederate as a console application on Windows

  The preserved JVM options are activated as the PingFederate service starts.

- PingFederate as a service on Windows

  * When administrators run the PingFederate service-installation program `install-service.bat`, located in the `<pf_install>/pingfederate/sbin/win-x86-64` directory, to install the PingFederate Windows service manually, the program runs the `memoryoptions` utility. Regardless of available memory, PingFederate uses the G1GC. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory. The default options are recorded in the `jvm-memory.options` file. The service-installation program then runs a helper utility, `generate-wrapper-jvm-options.bat`, located in the `<pf_install>/pingfederate/sbin/wrapper` directory, to read the JVM options from the `jvm-memory.options` file and create a resource file that the PingFederate Windows service requires to configure its JVM options

  * The new recommended options are activated as the PingFederate service starts.&#xA;&#xA;To restore the preserved JVM options from the source installation, see Restoring the preserved JVM. |

---

---
title: Operating system tuning
description: This section contains tuning recommendations for your operating system.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_operat_sys_tuning
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_operat_sys_tuning.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Operating system tuning

This section contains tuning recommendations for your operating system.

The tuning recommendations provided here work best in preventing deployment issues in high capacity environments.

---

---
title: References
description: For more information on memory management and Hotspot Java virtual machine (JVM) arguments for garbage collection tuning, see the following resources.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_references
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_references.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# References

For more information on memory management and Hotspot Java virtual machine (JVM) arguments for garbage collection tuning, see the following resources.

* Memory management

  For more information, see [Java Platform, Standard Edition HotSpot Virtual Machine Garbage Collection Tuning Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/) from Oracle.

* Hotspot JVM arguments

  Learn more in [Java HotSpot VM Options](https://www.oracle.com/java/technologies/javase/vmoptions-jsp.html) in the Oracle documentation.

---

---
title: Restoring the preserved JVM options
description: When administrators run the PingFederate service-installation program install-service.bat, the upgrade utility creates a new installation based on the source installation and copies the jvm-memory.options file from the source installation to the new installation. You can edit the jvm-memory.options file with a time stamp to restore the preserved JVM options that exist in the jvm-memory.options file from the source installation.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_restore_preserve_jvm
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_restore_preserve_jvm.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 10, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Restoring the preserved JVM options

When administrators run the PingFederate service-installation program `install-service.bat`, the upgrade utility creates a new installation based on the source installation and copies the `jvm-memory.options` file from the source installation to the new installation. You can edit the `jvm-memory.options` file with a time stamp to restore the preserved JVM options that exist in the `jvm-memory.options` file from the source installation.

## About this task

Use the command prompt to edit the `jvm-memory.options` file with a time stamp.

## Steps

1. Rename the current`jvm-memory.options` file. For example,`jvm-memory.options.backup`.

2. Look for the preserved `jvm-memory.options` file.

   |   |                                                   |
   | - | ------------------------------------------------- |
   |   | The preserved file was renamed with a time stamp. |

3. Remove the time stamp from the file name.

   |   |                                                                              |
   | - | ---------------------------------------------------------------------------- |
   |   | The `jvm-memory.options` is the file preserved from the source installation. |

4. Open a command prompt and go to the `<pf_install>/pingfederate/sbin/wrapper` directory.

5. Run `generate-wrapper-jvm-options.bat`.

   |   |                                                                                                                                                                                       |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This helper utility reads the JVM options from the `jvm-memory.options` file and creates a resource file that the PingFederate Windows service requires to configure its JVM options. |

6. Close the command prompt.

   The preserved file was renamed with a time stamp.

7. Restart the PingFederate Windows service.

## Result

The preserved JVM options are activated as the PingFederate service starts.

---

---
title: Snapshot isolation for high-volume transactions
description: Because deadlocks can occur in some tables in high-concurrency environments with contention for shared data, you can enable READ_COMMITTED_SNAPSHOT in SQL Server to improve the performance and scalability of applications with long-running transactions.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_snapshot_isolation
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_snapshot_isolation.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 11, 2023
---

# Snapshot isolation for high-volume transactions

Because deadlocks can occur in some tables in high-concurrency environments with contention for shared data, you can enable READ\_COMMITTED\_SNAPSHOT in SQL Server to improve the performance and scalability of applications with long-running transactions.

When snapshot isolation is enabled, each transaction reads data from a snapshot of the database taken at the start of the transaction rather than directly from the database itself.

Because there can be some overhead with snapshot isolation, evaluate and test this setting carefully before deploying in production environments. For more information on snapshot isolation and how to configure the option, see [Snapshot Isolation in SQL Server](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/snapshot-isolation-in-sql-server) in the Microsoft documentation.

---

---
title: The memoryoptions utility
description: Where to find the memoryoptions utility in a PingFederate installation and how the utility's expected behavior differs in a Linux or Windows system.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_memoryoptions_utility
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_memoryoptions_utility.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 13, 2023
section_ids:
  installation-and-upgrade: Installation and upgrade
  related-links: Related links
---

# The memoryoptions utility

Where to find the `memoryoptions` utility in a PingFederate installation and how the utility's expected behavior differs in a Linux or Windows system.

PingFederate installation and upgrade tools use the `memoryoptions` utility to record the default options for the Java heap and the garbage collector (GC) in a configuration file. Regardless of available memory, PingFederate uses the Garbage-First (G1) GC. The script assumes that PingFederate will be the only service on the server and consume a majority of the memory. As needed, administrators can re-run the utility or manually edit the configuration file.

The `memoryoptions` utility, located in the `<pf_install>/pingfederate/bin` directory, comes in two variants:

* `memoryoptions.bat` for Windows

* `memoryoptions.sh` for Linux

The configuration file, `jvm-memory.options`, is located in the same `bin` directory.

|   |                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You should not use the `memoryoptions` script when you deploy PingFederate inside of a container. Instead, you should edit the `jvm-memory.options` file directly. In containers, you should use the `InitialRAMPercentage` and `MaxRAMPercentage` JVM options to control the size of the heap. |

## Installation and upgrade

When the PingFederate installer is executed for Windows or a subsequent rerun of the `memoryoptions` utility, it creates a backup copy of the current `jvm-memory.options` and records the G1GC options in the `jvm-memory.options` file. Changes made as a result of the execution of the utility or a manual edit are activated after a restart of PingFederate.

Depending upon the selected tool and whether the `jvm-memory.options` file exists in the source installation, the expected behavior of the `memoryoptions` utility differs. In general, the `jvm-memory.options` file from the source installation is preserved without new recommended values.

## Related links

* [memoryoptions and installation](pf_memoryoptions_install.html)

* [memoryoptions and upgrade](pf_memoryoptions_upgrade.html)

---

---
title: Tuning the acceptor queue size
description: For optimal performance, particularly in larger deployments, PingFederate uses a non-blocking I/O model to process requests. You can tune the acceptor queue size parameters for your environment.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_tuning_acceptor_queue_size
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_tuning_acceptor_queue_size.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Tuning the acceptor queue size

For optimal performance, particularly in larger deployments, PingFederate uses a non-blocking I/O model to process requests. You can tune the acceptor queue size parameters for your environment.

## About this task

If the request queue reaches its maximum size, additional requests will receive a connection refused error. If this occurs in your environment, you can increase the values of the acceptor queue size parameters `pf.admin.acceptQueueSize` and `pf.runtime.acceptQueueSize`. The `pf.admin.acceptQueueSize` parameter applies to the administrative console and the `pf.runtime.acceptQueueSize` parameter applies to the engine nodes.

## Steps

1. Stop PingFederate.

2. Open the `<pf_install>/pingfederate/bin/run.properties` file in an editor.

   |   |                                             |
   | - | ------------------------------------------- |
   |   | Consider making a backup copy of this file. |

3. Go to the following section and change the values of the `pf.admin.acceptQueueSize` and `pf.runtime.acceptQueueSize` parameters.

   ```
   # HTTP Connector Queue Size Settings
   # ----------------------------------
   # The following properties control the queue size of the HTTP connector.
   #
   # Please refer to the performance tuning guide for further tuning guidance.
   pf.admin.acceptQueueSize=512
   pf.runtime.acceptQueueSize=512
   ```

4. Save your changes and restart PingFederate.

5. For a clustered PingFederate environment, repeat the previous steps on each engine node.

---

---
title: Tuning the server thread pool
description: When tuning the server thread pool, set the minimum and maximum number of threads to optimize PingFederate for your needs.
component: pingfederate
version: 13.1
page_id: pingfederate:performance_tuning_guide:pf_tuning_server_thread_pool
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/performance_tuning_guide/pf_tuning_server_thread_pool.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Tuning the server thread pool

When tuning the server thread pool, set the minimum and maximum number of threads to optimize PingFederate for your needs.

## About this task

Set the minimum and maximum numbers according to the expected user load:

* Set the minimum number of threads to between 75% and 100% of the number of requests you expect the system to handle most often.

* Set the maximum number of threads to between 25% and 50% higher than the minimum to handle load spikes.

Performance testing offers an alternative guideline. Testing shows that PingFederate performs well when the server thread pool has 25 to 50 server threads per available CPU core, assuming sufficient memory. For example, if your PingFederate system has one CPU with four cores, the total available cores is four. In that case, the minimum thread value would be 100 and the maximum thread value would be 200.

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This alternative guideline might not apply to larger systems. For example, if PingFederate is running on a system with 24 CPU cores, it doesn't make sense to size the thread pool at a minimum of 600 threads and a maximum of 1200 unless you expect to normally handle at least 800 concurrent requests. |

For more information on managing memory for PingFederate, see [Memory](pf_memory.html).

## Steps

1. Stop PingFederate.

2. Edit the `<pf_install>/pingfederate/bin/run.properties` file.

   |   |                                             |
   | - | ------------------------------------------- |
   |   | Consider making a backup copy of this file. |

3. Go to the following section, and change the thread number.

   ```
   # HTTP Server Thread Pool Settings
   # --------------------------------
   # The following properties control the minimum and the maximum number of threads used to configure PingFederate thread pools.
   #
   # Please refer to the performance tuning guide for further tuning guidance.
   pf.admin.threads.min=1
   pf.admin.threads.max=10
   pf.runtime.threads.min=10
   pf.runtime.threads.max=200
   ```

4. Save your changes and restart PingFederate.

5. For a clustered PingFederate environment, repeat the previous steps on each engine node as needed.
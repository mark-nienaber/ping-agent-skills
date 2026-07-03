---
title: Drop-in software update
description: Perform a drop-in software update of PingAM Java Agent for Tomcat, JBoss, Jetty, and WebLogic, and roll back if needed.
component: java-agents
version: 2026
page_id: java-agents:upgrade:drop-in-upgrade
canonical_url: https://docs.pingidentity.com/java-agents/2026/upgrade/drop-in-upgrade.html
section_ids:
  drop-in-software-update-tomcat: Tomcat Java Agent software update
  drop-in-software-update-jboss: JBoss and WildFly Java Agent software update
  drop-in-software-update-jetty: Jetty Java Agent software update
  drop-in-software-update-weblogic: WebLogic Java Agent software update
  roll_back_from_a_drop_in_software_update: Roll back from a drop-in software update
---

# Drop-in software update

The examples in this section assume that the agent is installed in `/path/to/java_agents/agent_type`, and the update is from the minor version 2025.3 to the minor version 2025.11.

## Tomcat Java Agent software update

1. Read the [release notes](https://docs.pingidentity.com/java-agents/release-notes/preface.html) for information about changes in Java Agent.

2. Download the agent binaries from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads) and extract them to a temporary directory.

   The example in this section is extracted to `/tmp`, and the .jar files are in `/tmp/tomcat_agent/lib`.

3. Back up the directories for the agent installation and the web application container configuration:

   * In [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode):

     ```bash
     $ cp -r /path/to/java_agents/tomcat_agent /path/to/backup
     $ cp -r /path/to/tomcat/webapps/agentapp /path/to/backup
     ```

   * In [remote configuration mode](../user-guide/glossary.html#def-remote-configuration-mode), back up as described in AM's [Maintenance guide](https://docs.pingidentity.com/pingam/8.1/maintenance-guide/backup-restore.html).

4. Redirect client traffic away from protected web applications.

5. Stop the web applications where the agent is installed.

6. Locate the following files in the container:

   * `agent.jar`

   * `jee-agents-sdk-version.jar`

   The following example finds `./lib/jee-agents-sdk-2025.3.jar`:

   * Unix

   * Windows

   ```
   $ cd /opt/container
   $ find . -type f -name 'jee-agents-*.jar' -print
   ./lib/jee-agents-sdk-2025.3.jar
   ```

   ```
   C:\> cd C:\opt\container
   C:\opt\container> dir /s jee-agents-*.jar

   ...
     Directory of C:\opt\container\lib

     date  time          ... jee-agents-sdk-2025.3.jar
   ...
   ```

7. If `agent.jar` is present in the container, delete it.

8. Replace `jee-agents-sdk-version.jar` with the newer downloaded version. The following example replaces `jee-agents-sdk-2025.3.jar`:

   * Unix

   * Windows

   ```
   $ cd /opt/container
   $ rm -f lib/jee-agents-sdk-2025.3.jar
   $ cp /tmp/tomcat_agent/lib/jee-agents-sdk-2025.11.jar lib
   ```

   ```
   C:\opt\container> del lib\jee-agents-sdk-2025.3.jar
   C:\opt\container> copy C:\tmp\tomcat_agent\lib\jee-agents-sdk-2025.11.jar lib
   ```

9. (Optional) Update the .jar files outside the container.

   1. Using the `.amAgentLocator` file, find the directory in which the agent was originally installed:

      * Unix

      * Windows

      ```
      $ cd /opt/container
      $ cat .amAgentLocator; echo

      /path/to/java_agents/tomcat_agent
      ```

      ```
      C:\opt\container> type .amAgentLocator

      C:/path/to/java_agents/tomcat_agent
      ```

   2. View the content of the `lib` subdirectory:

      * Unix

      * Windows

      ```
      $ cd /path/to/java_agents/tomcat_agent/lib
      $ ls -F

      agent.jar
      jee-agents-installtools-2025.3.jar
      jee-agents-sdk-2025.3.jar
      ```

      ```
      C:\opt\container> cd C:\path\to\java_agents\tomcat_agent\lib
      C:\path\to\java_agents\tomcat_agent\lib> dir

      Directory of C:\path\to\java_agents\tomcat_agent\lib
      ... agent.jar
      ... jee-agents-installtools-2025.3.jar
      ... jee-agents-sdk-2025.3.jar
      ```

   3. Replace the files with the newer downloaded version:

      * Unix

      * Windows

      ```
      $ rm -f * 
      $ cp /tmp/java_agents/tomcat_agent/lib/*.jar .
      $ ls -F

      agent.jar
      jee-agents-installtools-2025.11.jar
      jee-agents-sdk-2025.11.jar
      ```

      ```
      C:\path\to\java_agents\tomcat_agent\lib> del *.jar 
      C:\path\to\java_agents\tomcat_agent\lib> copy C:\temp\java_agents\tomcat_agent\lib\*.jar .

      C:\tmp\tomcat_agent\lib\agent.jar
      C:\tmp\tomcat_agent\lib\jee-agents-installtools-2025.11.jar
      C:\tmp\tomcat_agent\lib\jee-agents-sdk-2025.11.jar
      ```

10. Replace the current `agentadmin` file with the newer downloaded version:

    * Unix

    * Windows

    ```
    $ cd /path/to/java_agents/tomcat_agent/bin 
    $ rm agentadmin
    $ cp /tmp/tomcat_agent/bin/agentadmin . 
    ```

    ```
    C:\> cd C:\path\to\java_agents\tomcat_agent\bin
    C:\path\to\java_agents\tomcat_agent\bin> del agentadmin agentadmin.bat
    C:\path\to\java_agents\tomcat_agent\bin> copy C:\tmp\tomcat_agent\bin\agentadmin .
    C:\path\to\java_agents\tomcat_agent\bin> copy C:\tmp\tomcat_agent\bin\agentadmin.bat .
    ```

11. Start the web applications where the agent is installed.

12. Check that the agent is performing as expected:

    1. Check the correct version of the agent is running:

       * Set the log level to `trace`, as described in [Manage logs](../maintenance-guide/logging.html).

       * In `/path/to/java_agents/agent_type/Agent_n/logs/debug`, search for lines containing the string `X-ForgeRock-Edge-Metadata`. The version number is given in the header.

         For example, the log file can contain the following header: `--header "X-ForgeRock-Edge-Metadata: JPA 2025.11`.

    2. Navigate to a protected page on the website and confirm whether you can access it according to your configuration.

    3. Check logs files for warnings and errors.

13. Allow client traffic to flow to the protected web applications.

## JBoss and WildFly Java Agent software update

1. Read the [release notes](https://docs.pingidentity.com/java-agents/release-notes/preface.html) for information about changes in Java Agent.

2. Download the agent binaries from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads) and extract them to a temporary directory.

   The example in this section is extracted to `/tmp`, and the .jar files are in `/tmp/jboss_agent/lib`.

3. Back up the directories for the agent installation and the web application container configuration:

   * In [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode):

     ```bash
     $ cp -r /path/to/java_agents/jboss_agent /path/to/backup
     $ cp -r /path/to/jboss/webapps/agentapp /path/to/backup
     ```

   * In [remote configuration mode](../user-guide/glossary.html#def-remote-configuration-mode), back up as described in AM's [Maintenance guide](https://docs.pingidentity.com/pingam/8.1/maintenance-guide/backup-restore.html).

4. Redirect client traffic away from protected web applications.

5. Stop the web applications where the agent is installed.

6. Update the `module.xml` file.

   1. Locate the path to the installation, for example, at `/path/to/jboss/modules/org/forgerock/openam/agent/main/modules/org/forgerock/openam/agent/main`.

   2. If any of the following files are listed, remove the resource for the file:

      * `tyrus-standalone-client-2.1.3.jar`

      * `jee-agents-jboss-common-2025.3.jar`

      * `agent.jar`

   3. Update the resource for `jee-agents-sdk-version.jar` to use the absolute path and the newer downloaded version agent version. For example, change

      ```
      <resource-root path="jee-agents-sdk-2025.3.jar"/>
      ```

      to

      ```
      <resource-root path="/path/to/java_agents/jboss_agent/lib/jee-agents-sdk-2025.11.jar"/>
      ```

7. Update the .jar files outside the container.

   1. Using the `.amAgentLocator` file, find the directory in which the agent was originally installed:

      ```
      $ cd /opt/container
      $ cat .amAgentLocator; echo

      /path/to/java_agents/jboss_agent
      ```

   2. View the content of the `lib` subdirectory:

      ```
      $ cd /path/to/java_agents/jboss_agent/lib
      $ ls -F

      agent.jar
      jee-agents-jboss-common-version.jar
      jee-agents-sdk-version.jar
      tyrus-standalone-client-version.jar
      ```

   3. Replace the files with the newer downloaded version:

      ```
      $ rm -f * 
      $ cp /tmp/java_agents/jboss_agent/lib/*.jar .
      $ ls -F

      agent.jar
      jee-agents-jboss-common-version.jar
      jee-agents-sdk-version.jar
      tyrus-standalone-client-version.jar
      ```

8. Replace the current `agentadmin` file with the newer downloaded version:

   ```
   $ cd /path/to/java_agents/jboss_agent/bin 
   $ rm agentadmin
   $ cp /tmp/jboss_agent/bin/agentadmin . 
   ```

9. Start the web applications where the agent is installed.

10. Check that the agent is performing as expected:

    1. Check the correct version of the agent is running:

       * Set the log level to `trace`, as described in [Manage logs](../maintenance-guide/logging.html).

       * In `/path/to/java_agents/agent_type/Agent_n/logs/debug`, search for lines containing the string `X-ForgeRock-Edge-Metadata`. The version number is given in the header.

         For example, the log file can contain the following header: `--header "X-ForgeRock-Edge-Metadata: JPA 2025.11`.

    2. Navigate to a protected page on the website and confirm whether you can access it according to your configuration.

    3. Check logs files for warnings and errors.

11. Allow client traffic to flow to the protected web applications.

## Jetty Java Agent software update

1. Read the [release notes](https://docs.pingidentity.com/java-agents/release-notes/preface.html) for information about changes in Java Agent.

2. Download the agent binaries from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads) and extract them to a temporary directory.

   The example in this section is extracted to `/tmp`, and the .jar files are in `/tmp/jetty_agent/lib`.

3. Back up the directories for the agent installation and the web application container configuration:

   * In [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode):

     ```bash
     $ cp -r /path/to/java_agents/jetty_agent /path/to/backup
     $ cp -r /path/to/jetty/webapps/agentapp /path/to/backup
     ```

   * In [remote configuration mode](../user-guide/glossary.html#def-remote-configuration-mode), back up as described in AM's [Maintenance guide](https://docs.pingidentity.com/pingam/8.1/maintenance-guide/backup-restore.html).

4. Redirect client traffic away from protected web applications.

5. Stop the web applications where the agent is installed.

6. Replace the following files with the newer downloaded versions.

   * `agent.jar`

   * `jee-agents-installtools-version.jar`

   * `jee-agents-sdk-version.jar`

   The following example replaces `jee-agents-sdk-2025.3.jar`:

   ```
   $ cd /path/to/java_agents/jetty_agent/lib
   $ rm -f jee-agents-sdk-2025.3.jar
   $ cp /tmp/jetty_agent/lib/jee-agents-sdk-2025.11.jar .
   ```

7. Update the Jetty configuration:

   1. Go to the Jetty base directory.

      ```
      $ cd /path/to/jetty-base/modules
      ```

   2. In `amlogin.mod`, delete the line for `/path/to/java_agents/jetty_agent/lib/agent.jar` if it is present. This file isn't required from Java Agent 2023.9.

   3. In `amlogin.mod`, update the version number for `jee-agents-sdk-version.jar`. The following example includes `jee-agents-sdk-2025.11.jar`:

      ```none
      # Jetty AM module
      #
      [depend]
      server
      security
      jndi
      webapp
      plus
      [xml]
      etc/amlogin.xml
      [lib]
      /path/to/java_agents/jetty_agent/Agent_001/config
      /path/to/java_agents/jetty_agent/locale
      /path/to/java_agents/jetty_agent/lib/jee-agents-sdk-2025.3.jar
      ```

8. Replace the current `agentadmin` file with the newer downloaded version:

   ```
   $ cd /path/to/java_agents/jetty_agent/bin 
   $ rm agentadmin
   $ cp /tmp/jetty_agent/bin/agentadmin . 
   ```

9. Start the web applications where the agent is installed.

10. Check that the agent is performing as expected:

    1. Check the correct version of the agent is running:

       * Set the log level to `trace`, as described in [Manage logs](../maintenance-guide/logging.html).

       * In `/path/to/java_agents/agent_type/Agent_n/logs/debug`, search for lines containing the string `X-ForgeRock-Edge-Metadata`. The version number is given in the header.

         For example, the log file can contain the following header: `--header "X-ForgeRock-Edge-Metadata: JPA 2025.11`.

    2. Navigate to a protected page on the website and confirm whether you can access it according to your configuration.

    3. Check logs files for warnings and errors.

11. Allow client traffic to flow to the protected web applications.

## WebLogic Java Agent software update

1. Read the [release notes](https://docs.pingidentity.com/java-agents/release-notes/preface.html) for information about changes in Java Agent.

2. Download the agent binaries from the [Ping Identity Download Center](https://backstage.pingidentity.com/downloads) and extract them to a temporary directory.

   The example in this section is extracted to `/tmp`, and the .jar files are in `/tmp/weblogic_agent/lib`.

3. Back up the directories for the agent installation and the web application container configuration:

   * In [local configuration mode](../user-guide/glossary.html#def-local-configuration-mode):

     ```bash
     $ cp -r /path/to/java_agents/weblogic_agent /path/to/backup
     ```

   * In [remote configuration mode](../user-guide/glossary.html#def-remote-configuration-mode), back up as described in AM's [Maintenance guide](https://docs.pingidentity.com/pingam/8.1/maintenance-guide/backup-restore.html).

4. Add the following file to the backup:

   * `/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/setAgentEnv_AdminServer.sh`

5. Redirect client traffic away from protected web applications.

6. Stop the web applications where the agent is installed.

7. Update the .jar files in the installation directory.

   1. Using the `.amAgentLocator` file, find the directory in which the agent was originally installed:

      ```
      $ cd /opt/container
      $ cat .amAgentLocator; echo

      /path/to/java_agents/weblogic_agent
      ```

   2. View the content of the `lib` subdirectory:

      ```
      $ cd /path/to/java_agents/weblogic_agent/lib
      $ ls -F

      agent.jar
      jee-agents-installtools-2025.3.jar
      jee-agents-sdk-2025.3.jar
      ```

   3. Replace the files with the newer downloaded version:

      ```
      $ rm -f * 
      $ cp /tmp/java_agents/weblogic_agent/lib/*.jar .
      $ ls -F

      agent.jar
      jee-agents-installtools-2025.11.jar
      jee-agents-sdk-2025.11.jar
      ```

8. Update the environment settings:

   1. Locate the `setAgentEnv_AdminServer.sh` file. The file can be in a directory such as `/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/`.

   2. If any of the following files are listed, remove the information for the file:

      * `/path/to/java_agents/weblogic_agent/lib/agent.jar`.

      * `/path/to/java_agents/weblogic_agent/lib/jee-agents-installtools-launcher-version`. The installation launcher was removed in Java Agent 2023.6.

      * `/path/to/java_agents/weblogic_agent/lib/jee-agents-installtools-version.jar`.

   3. Change the version of `jee-agents-sdk-version.jar` to the newer downloaded version:

      ```bash
      ...
      # Append AGENT_CLASSPATH to the WebLogic server classpath
      AGENT_CLASSPATH="/path/to/java_agents/weblogic_agent/lib/jee-agents-sdk-2025.11.jar:/path/to/java_agents/weblogic_agent/locale:/path/to/java_agents/weblogic_agent/Agent_001/config"
      CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${AGENT_CLASSPATH}"
      export CLASSPATH
      ...
      ```

   4. Save the file.

9. Replace the current `agentadmin` file with the newer downloaded version:

   ```
   $ cd /path/to/java_agents/weblogic_agent/bin 
   $ rm agentadmin
   $ cp /tmp/weblogic_agent/bin/agentadmin . 
   ```

10. Start the web applications where the agent is installed.

11. Check that the agent is performing as expected:

    1. Check the correct version of the agent is running:

       * Set the log level to `trace`, as described in [Manage logs](../maintenance-guide/logging.html).

       * In `/path/to/java_agents/agent_type/Agent_n/logs/debug`, search for lines containing the string `X-ForgeRock-Edge-Metadata`. The version number is given in the header.

         For example, the log file can contain the following header: `--header "X-ForgeRock-Edge-Metadata: JPA 2025.11`.

    2. Navigate to a protected page on the website and confirm whether you can access it according to your configuration.

    3. Check logs files for warnings and errors.

12. Allow client traffic to flow to the protected web applications.

## Roll back from a drop-in software update

|   |                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you roll back to an earlier version of Java Agent, consider whether any change to the configuration during or since upgrade could be incompatible with the previous version. |

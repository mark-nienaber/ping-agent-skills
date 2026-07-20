---
title: Asynchronous reconciliation using workflow
description: Run asynchronous PingIDM reconciliation using a workflow that requires administrator approval before creating new users from a CSV file
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:sync-asynchronous
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/sync-asynchronous.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Asynchronous", "Reconciliation", "Workflows"]
section_ids:
  run-asynchronous-recon: Run the sample
---

# Asynchronous reconciliation using workflow

This sample demonstrates asynchronous reconciliation using workflows.

The data for this sample is in the file `samples/sync-asynchronous/data/csvConnectorData.csv`. That file contains two users, as follows:

```csv
"description", "uid", "username", "firstname", "lastname", "email", "mobile..."
"Created ...", "bjensen", "bjensen@example.com", "Barbara", "Jensen", "bjensen@example.com", 1234..."
"Created ...", "scarter", "scarter@example.com", "Steven", "Carter", "scarter@example.com", 1234..."
```

During the sample, you will reconcile the users in the CSV file with the managed user repository. Instead of creating each user immediately, the reconciliation operation generates an approval request for each ABSENT user (users who are not found in the repository). The configuration for this action is defined in the `conf/sync.json` file, which specifies that an `ABSENT` condition should launch the `managedUserApproval` workflow:

```json
...
    {
        "situation" : "ABSENT",
        "action" : {
            "workflowName" : "managedUserApproval",
            "type" : "text/javascript",
            "file" : "workflow/triggerWorkflowFromSync.js"
        }
    },
 ...
```

When each request is approved by an administrator, an asynchronous reconciliation operation is launched, that ultimately creates the users in the repository.

## Run the sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

Before you start, prepare IDM as described in [Prepare IDM](start-here.html#preparing-openidm).

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Workflows are not supported with a DS repository. Before you test this sample, [install a JDBC repository](../install-guide/chap-repository.html). |

1. Edit the `/path/to/openidm/samples/sync-asynchronous/conf/datasource.jdbc-default.json` file with the details of your JDBC repository. For more information, refer to [Select a repository](../install-guide/chap-repository.html).

2. Start IDM with the configuration for this sample:

   ```
   /path/to/openidm/startup.sh -p samples/sync-asynchronous
   ```

3. The sample is configured to assign new workflow tasks to an admin account named `async.admin`. Create this account before you begin:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
    "userName": "async.admin",
    "givenName": "async",
    "sn" : "admin",
    "password" : "Passw0rd",
    "displayName" : "async admin",
    "mail" : "async.admin@example.com",
    "authzRoles": [
        { "_ref": "internal/role/openidm-admin" },
        { "_ref": "internal/role/openidm-authorized" }
    ],
    "_id" : "asyncadmin"
    }' \
   "http://localhost:8080/openidm/managed/user?_action=create"
   {
     "_id":"asyncadmin",
     "_rev":"00000000e8f502db",
     "userName":"async.admin",
     "givenName":"async",
     "sn":"admin",
     "displayName":"async admin",
     "mail":"async.admin@example.com",
     "accountStatus":"active",
     "effectiveRoles":[],
     "effectiveAssignments":[]
   }
   ```

4. Run reconciliation over the REST interface:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/recon?_action=recon&mapping=systemCsvfileAccounts_managedUser"
   {
     "_id": "98d7f3c5-684e-4ef0-b4f9-f2e816a339cf-32",
     "state": "ACTIVE"
   }
   ```

   The reconciliation operation returns a reconciliation run ID, and the status of the operation.

   This reconciliation launches a workflow that generates an approval process for each ABSENT user. The approval processes must be approved by an administrator before the workflow can continue.

5. Review the approval tasks launched by the reconciliation.

   * To review the tasks in the admin UI, log in to the admin UI at `https://localhost:8443/admin/` using an administrator account (either `openidm-admin` or `async.admin` will work) and select Manage > Tasks.

     You should see two task instances launched by the Managed User Approval Workflow.

   * To view the approval tasks over REST run the following command:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request GET \
     "http://localhost:8080/openidm/workflow/taskinstance?_queryFilter=true&_fields=_id,processDefinitionId"
     ```

     The request returns two task instances, each with a process ID (`_id`) and a process definition ID.

     ```json
     {
       "result": [
         {
           "_id": "38",
           "processDefinitionId": "managedUserApproval:1:5"
         },
         {
           "_id": "39",
           "processDefinitionId": "managedUserApproval:1:5"
         }
       ],
       ...
     }
     ```

6. Complete each approval task.

   * To complete the approval tasks using the UI, sign on to the end-user UI at `https://localhost:8443/#/login` as user `async.admin` with password `Passw0rd`.

     You should see two Evaluate request tasks under My Tasks on the Dashboard.

     For each task, select Edit, and then click Approve to add the noted users.

     |   |                                                                                                                           |
     | - | ------------------------------------------------------------------------------------------------------------------------- |
     |   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

   * To approve the requests over REST, set `requestApproved` to `true` for each task instance, and use the `complete` action. Specify the `_id` of each task in the URL.

     For example, to approve the first request:

     ```
     curl \
     --header "X-OpenIDM-Username: async.admin" \
     --header "X-OpenIDM-Password: Passw0rd" \
     --header "Accept-API-Version: resource=1.0" \
     --header "Content-Type: application/json" \
     --request POST \
     --data '{"requestApproved": "true"}' \
     "http://localhost:8080/openidm/workflow/taskinstance/38?_action=complete"
     {
       "Task action performed": "complete"
     }
     ```

     Repeat this command for each task ID.

7. When the requests have been approved, select Manage > User in the admin UI to view the new users in the repository, or query the managed users over REST as follows:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/user?_queryFilter=true&_fields=_id"
   {
     "result": [
       {
          "_id": "asyncadmin",
          "_rev": "00000000e8f502db"
       }, {
          "_id": "scarter",
          "_rev": "000000007e120780"
       }, {
          "_id": "bjensen",
          "_rev": "00000000d9390751"
       }
     ],
    ...
   }
   ```

---

---
title: Connect to a MySQL database with ScriptedSQL
description: Use the ScriptedSQL Groovy connector to synchronize PingIDM managed users with an external MySQL database, including support for complex objects
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:scripted-sql-with-mysql
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/scripted-sql-with-mysql.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "MySQL", "ScriptedSQL"]
section_ids:
  scripted-sql-mysql-setup: Configure the external MySQL database
  sample-scripted-sql-running: Run the sample
  scriptedsql-event-hooks: Test the event hooks
  scriptedsql-sample-paging: Run the sample with paging
---

# Connect to a MySQL database with ScriptedSQL

This sample uses the Groovy Connector Toolkit bundled with IDM (`openidm/connectors/groovy-connector-1.5.20.31.jar` ) to implement a ScriptedSQL connector that interacts with an external MySQL database (HRDB), and also demonstrates the following functionality:

* Complex data types.

  Complex data types can be stored, retrieved and synchronized like any other object property. They are stored in the managed data as JSON objects, represented as a string, but can be mapped to external resources in any format required. You can customize the mapping to do additional work with or transformations on the complex data types.

  This sample defines one complex data type, `cars`, discussed in more detail later in this section.

* [Event hooks](#scriptedsql-event-hooks) to perform actions.

  The mapping from the internal repository to the external `hrdb` database includes two script hooks. The first hook is for an `onCreate` event and the second is for an `onUpdate` event.

* [Custom scripted endpoints](../scripting-guide/script-custom-endpoints.html).

  Custom scripted endpoints are configured in the provisioner configuration file and allow you to execute custom scripts over REST. This sample uses a custom scripted endpoint to reset the database and populate it with data.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because MySQL cannot "un-hash" user passwords there is no way for a reconciliation operation to retrieve the password from MySQL and store it in the managed user object. This issue might impact configurations that support multiple external resources in that passwords might not be synchronized immediately after reconciliation from MySQL to the managed user repository. Users who are missing in the repository will be created by reconciliation but their passwords will be empty. When those users are synchronized to other external resources, they will have empty passwords in those resources. Additional scripting might be required to handle this situation, depending on the requirements of your deployment. |

The Groovy scripts required for the sample are located in the `samples/scripted-sql-with-mysql/tools` directory. Note that the power of the Groovy connector is in the associated Groovy scripts, and their application in your particular deployment. The scripts provided with this sample are specific to the sample. You must customize these scripts to address the requirements of your specific deployment. The sample scripts are a good starting point on which to base your customization.

## Configure the external MySQL database

This sample assumes a database running on the localhost.

1. Download [MySQL Connector/J](https://dev.mysql.com/downloads/connector/j/) version 8.0 or later.

2. Unpack the downloaded file, and copy the .jar file to `openidm/lib` :

   ```
   cp mysql-connector-java-version-bin.jar /path/to/openidm/lib/
   ```

   |   |                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are running this sample with an SQL database other than MySQL, download the corresponding driver and place it in the `openidm/lib` directory. It is not necessary to create an OSGi bundle for the driver. |

3. Set up MySQL to listen on localhost, port `3306`. IDM will connect to the `hrdb` database as user `root` with password `password`.

   To use an existing MySQL instance that runs on a different host or port, or to change the database credentials, edit the `configurationProperties` in the connector configuration file (`samples/scripted-sql-with-mysql/conf/provisioner.openicf-hrdb.json`) before you start the sample. The default configuration is as follows:

   ```json
   "configurationProperties" : {
       "username" : "root",
       "password" : "password",
       "driverClassName" : "com.mysql.cj.jdbc.Driver",
       "url" : "jdbc:mysql://localhost:3306/hrdb?serverTimezone=UTC",
       ...
   ```

   |   |                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The default configuration expects SSL, *which is strongly advised in a production environment*. If you are running this in a test environment, you can bypass the SSL requirement:- Add `&useSSL=false` to the end of the `url`.

   - If you are running MySQL 8.0.11+, add `&allowPublicKeyRetrieval=true` to the end of the `url`. |

4. Set up the `hrdb` database, with which IDM will synchronize its managed user repository:

   ```
   mysql -u root -p
   Enter password:
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 3
   Server version: 5.7.13 MySQL Community Server (GPL)

   Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

   Oracle is a registered trademark of Oracle Corporation and/or its
   affiliates. Other names may be trademarks of their respective
   owners.

   Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

   mysql> CREATE DATABASE hrdb CHARACTER SET utf8 COLLATE utf8_bin;
   Query OK, 1 row affected (0.00 sec)
   ```

5. Configure your GRANT permissions:

   ```
   CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'password';
   GRANT ALL PRIVILEGES ON hrdb.* TO 'root'@'%' WITH GRANT OPTION;
   ```

## Run the sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

The mapping configuration file (`sync.json`) for this sample includes the mapping `systemHrdb_managedUser`. You will use this mapping to synchronize users from the source `hrdb` database with the target IDM repository.

1. Start IDM with the configuration for the ScriptedSQL sample:

   ```
   /path/to/openidm/startup.sh -p samples/scripted-sql-with-mysql
   ```

2. Run the custom script (`samples/scripted-sql-with-mysql/tools/ResetDatabaseScript.groovy`) to reset the database and populate it with sample data.

   |   |                                                                    |
   | - | ------------------------------------------------------------------ |
   |   | You can run the script again, at any point, to reset the database. |

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/system/hrdb?_action=script&scriptId=ResetDatabase"
   {
     "actions": [
       {
         "result": "Database reset successful."
       }
     ]
   }
   ```

   The `hrdb` database should now be populated with sample data.

3. Review the contents of the database:

   ```
   mysql -u root -p
   Enter password:
   mysql > use hrdb;
   Reading table information for completion of table and column names
   You can turn off this feature to get a quicker startup with -A

   Database changed
   mysql > select * from users;
   ----------------------------------------------------------------------...
   | id | uid    | password     | firstname | lastname | fullname      | email  ...
   +------------------------------------------------------------------------...
   |  1 | bob    | e38ad2149... | Bob       | Fleming  | Bob Fleming   | Bob.Fle...
   |  2 | rowley | 2aa60a8ff... | Rowley    | Birkin   | Rowley Birkin | Rowley....
   |  3 | louis  | 1119cfd37... | Louis     | Balfour  | Louis Balfour | Louis.B...
   |  4 | john   | a1d7584da... | John      | Smith    | John Smith    | John.Sm...
   |  5 | jdoe   | edba955d0... | John      | Doe      | John Doe      | John.Do...
   +-----------------------------------------------------------------+-------...
   5 rows in set (0.00 sec)
   ```

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The passwords in the above output are SHA-1 hashed because they cannot be read into IDM as cleartext. The SHA-1 Hash function is used for compatibility reasons. Use a more secure algorithm in a production database. |

4. Reconcile the hrdb database with the managed user repository.

   1. To reconcile the repository by using the Administration UI:

      1. Log in to the admin UI at the URL `https://localhost:8443/admin` as the default administrative user (`openidm-admin`) with password `openidm-admin`.

      2. Select Configure > Mappings.

         The Mappings page shows two mappings, one from the `hrdb` database to the IDM managed user repository (`managed/user`), and one in the opposite direction.

      3. Click Reconcile on the first mapping (systemHrdb\_managedUser).

   2. To reconcile the repository by using the command-line, launch the reconciliation operation with the following command:

      ```
      curl \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request POST \
      "http://localhost:8080/openidm/recon?_action=recon&mapping=systemHrdb_managedUser&waitForCompletion=true"
      {
        "state": "SUCCESS",
        "_id": "f3c618aa-cc3b-49ed-9a3a-00b012db2513"
      }
      ```

   The reconciliation operation creates the five users from the MySQL database in the IDM repository.

5. Retrieve the list of users from the repository.

   1. To retrieve the users in the repository from the admin UI:

      1. Select Manage > User to display the *User List*.

         The five users from the `hrdb` database have been reconciled to the OpenIDM repository.

      2. To retrieve the details of a specific user, click that user entry.

   2. To retrieve the users from the repository by using the command-line, query the IDs in the repository as follows:

      ```
      curl \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request GET \
      "http://localhost:8080/openidm/managed/user?_queryId=query-all-ids"
      {
        "result": [
          {
            "_id": "1b379e4d-3b8d-47e7-93d5-a72c4b483e39",
            "_rev": "000000002d93e471"
          },
          {
            "_id": "a658f751-d6e9-4b5d-af56-071a9b05c3af",
            "_rev": "000000003c83d48a"
          },
          {
            "_id": "5b31027b-09f8-4c7f-abfa-c6bc86ae3943",
            "_rev": "00000000b042e559"
          },
          {
            "_id": "1b3f6b06-1752-4c40-ba34-51d30b184b9d",
            "_rev": "0000000092bdda6d"
          },
          {
            "_id": "9c62f0d2-47e2-4fc5-89d1-b50b782b1022",
            "_rev": "0000000025cdd3c6"
          }
        ],
        "resultCount": 5,
        "pagedResultsCookie": null,
        "totalPagedResultsPolicy": "NONE",
        "totalPagedResults": -1,
        "remainingPagedResults": -1
      }
      ```

      To retrieve a complete user record, query the userName of the individual user entry. The following query returns the record for the user `Rowley Birkin`:

      ```
      curl \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request GET \
      "http://localhost:8080/openidm/managed/user/?_queryId=for-userName&uid=rowley"
      "result": [
          {
            "_id": "1b379e4d-3b8d-47e7-93d5-a72c4b483e39",
            "_rev": "000000002d93e471",
            "mail": "Rowley.Birkin@example.com",
            "userName": "rowley",
            "sn": "Birkin",
            "organization": "SALES",
            "givenName": "Rowley",
            "cars": [
              {
                "year": "2013",
                "make": "BMW",
                "model": "328ci"
              },
              {
                "year": "2010",
                "make": "Lexus",
                "model": "ES300"
              }
            ],
            "accountStatus": "active",
            "effectiveRoles": [],
            "effectiveAssignments": []
          }
        ],
        ...
      }
      ```

   Regardless of how you have retrieved Rowley Birkin's entry, note the `cars` property in this user's entry. This property demonstrates a complex object, stored in JSON format in the user entry, as a list that contains multiple objects. In the MySQL database, the `car` table joins to the `users` table through a `cars.users_id` column. The Groovy scripts read this data from MySQL and repackage it in a way that IDM can understand. With support for complex objects, the data is passed through to IDM as a list of `car` objects. Data is synchronized from IDM to MySQL in the same way. Complex objects can also be nested to any depth.

Group membership (not demonstrated here) is maintained with a traditional "join table" in MySQL (`groups_users`). IDM does not maintain group membership in this way, so the Groovy scripts do the work to translate membership between the two resources.

## Test the event hooks

This sample uses the `onCreate` and `onUpdate` hooks to log messages when a user is created or updated in the external database.

The sample's `conf/sync.json` file defines these event hooks as follows:

```none
...
    {
        "name" : "managedUser_systemHrdb",
        "source" : "managed/user",
        "target" : "system/hrdb/account",
        "links" : "systemHrdb_managedUser",
        "correlationQuery" : {
            "type" : "text/javascript",
            "source" : "({'_queryFilter': 'uid eq \"' + source.userName + '\"'});"
        },
        "onCreate" : {
            "type" : "text/javascript",
            "source" : "logger.info(\"Creating new user in external repo\")"
        },
        "onUpdate" : {
            "type" : "text/javascript",
            "source" : "logger.info(\"Updating existing user in external repo\")"
        },
...
```

Using these event hooks, IDM logs a message when a user is created or updated in the external database. In this sample, the script source is included in the mapping. However, a script can also be called from an external file. For more information about event hooks, refer to [Script triggers](../scripting-guide/script-triggers.html).

To test the event hooks, create a new managed user as follows:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request POST \
--data '{
    "mail":"fdoe@example.com",
    "sn":"Doe",
    "telephoneNumber":"555-1234",
    "userName":"fdoe",
    "givenName":"Felicitas",
    "description":"Felicitas Doe",
    "displayName":"fdoe"}' \
"http://localhost:8080/openidm/managed/user?_action=create"
{
  "_id": "2e5e9748-77e6-4019-90e1-abe9ab897343",
  "_rev": "0000000015b2d4ba",
  "mail": "fdoe@example.com",
  "sn": "Doe",
  "telephoneNumber": "555-1234",
  "userName": "fdoe",
  "givenName": "Felicitas",
  "description": "Felicitas Doe",
  "displayName": "fdoe",
  "accountStatus": "active",
  "effectiveRoles": [],
  "effectiveAssignments": []
}
```

The implicit synchronization between the managed user repository and the HRDB database creates that user in the database automatically.

Check the latest log file at `path/to/openidm/logs/openidm0.log.0`. You should see the following message at the end of the log:

```
INFO: Creating new user in external repo
```

Query the new user entry in the HRDB database:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/hrdb/account?_queryFilter=uid+eq+'fdoe'"
{
  "result": [
    {
      "_id": "6",
      "cars": [],
      "firstName": "Felicitas",
      "uid": "fdoe",
      "lastName": "Doe",
      "organization": "IDM",
      "fullName": "Felicitas Doe",
      "email": "fdoe@example.com"
    }
  ],
  ...
}
```

Update fdoe's entry in the HRDB database with a patch request. The following request updates the user's `organization` field:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--request PATCH \
--data '[ {
   "operation" : "replace",
   "field" : "organization",
   "value" : "example.com"
} ]' \
"http://localhost:8080/openidm/system/hrdb/account/6"
{
  "_id": "6",
  "cars": [],
  "firstName": "Felicitas",
  "uid": "fdoe",
  "lastName": "Doe",
  "organization": "example.com",
  "fullName": "Felicitas Doe",
  "email": "fdoe@example.com"
}
```

Note that this update does not reference the `onUpdate` script hook so this change is not logged in `openidm0.log.0`.

## Run the sample with paging

The following command indicates that only two records should be returned (`_pageSize=2`) and that the records should be sorted according to their `timestamp` and `_id` (`_sortKeys=timestamp,_id`). Including the `timestamp` in the sort ensures that, as you page through the set, changes to records that have already been visited are not lost. Instead, those records are pushed onto the last page:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/hrdb/account?_queryFilter=true&_pageSize=2&_sortKeys=timestamp,_id"
{
  "result": [
    {
      "_id": "1",
      "firstName": "Bob",
      "cars": [
        {
          "year": "1979",
          "make": "Ford",
          "model": "Pinto"
        }
      ],
      "fullName": "Bob Fleming",
      "email": "Bob.Fleming@example.com",
      "uid": "bob",
      "lastName": "Fleming",
      "organization": "HR"
    },
    {
      "_id": "2",
      "firstName": "Rowley",
      "cars": [
        {
          "year": "2013",
          "make": "BMW",
          "model": "328ci"
        }
      ],
      "fullName": "Rowley Birkin",
      "email": "Rowley.Birkin@example.com",
      "uid": "rowley",
      "lastName": "Birkin",
      "organization": "SALES"
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": "2018-04-05+16%3A30%3A22.0%2C2",
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

The `pagedResultsCookie` is used by the server to keep track of the position in the search results. You can ignore the `"remainingPagedResults": -1` in the output. The real value of this property is not returned because the scripts that the connector uses do not do any counting of the records in the resource.

Using the `pagedResultsCookie` from the previous step, run a similar query, to retrieve the following set of records in the database:

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
"http://localhost:8080/openidm/system/hrdb/account?_queryId=query-all-ids&_pageSize=2&_sortKeys=timestamp,_id&_pagedResultsCookie=2018-04-05+16%3A30%3A22.0%2C2"
{
  "result": [
    {
      "_id": "3",
    },
    {
      "_id": "4",
    }
  ],
  "resultCount": 2,
  "pagedResultsCookie": "2018-04-05+16%3A30%3A22.0%2C4",
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": -1
}
```

For more information about paging, refer to [Page Query Results](../objects-guide/queries.html#paging-query-results).

---

---
title: Connect to Active Directory with the PowerShell connector
description: Use the PowerShell Connector Toolkit to perform CRUD operations on Active Directory from PingIDM using PowerShell scripts
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:scripted-powershell-with-ad
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/scripted-powershell-with-ad.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Scripts", "Active Directory", "PowerShell"]
section_ids:
  powershell-sample-overview: Sample overview
  powershell-ad-setup: Prepare the sample
  powershell-ad-test: Run the sample
---

# Connect to Active Directory with the PowerShell connector

This sample shows an implementation of the [PowerShell Connector toolkit](https://docs.pingidentity.com/openicf/connector-reference/powershell.html) and provides a number of PowerShell scripts that let you perform basic CRUD (create, read, update, delete) operations on an Active Directory server.

The sample uses the [MS Active Directory PowerShell module](https://docs.microsoft.com/en-us/powershell/module/activedirectory).

## Sample overview

The generic *PowerShell Connector Toolkit* enables you to run PowerShell scripts on any external resource. The PowerShell Connector Toolkit isn't a complete connector in the traditional sense. It's a framework where you must write your own PowerShell scripts to address the requirements of your Microsoft Windows ecosystem. You can use the PowerShell Connector Toolkit to create connectors that can provision any Microsoft system.

The latest PowerShell connector toolkit is bundled with the .NET RCS and is available from the [Backstage download site](https://backstage.forgerock.com/downloads/browse/idm/all/productId:idm-connector-servers/minorVersion:1.5/version:1.5.7.0/language:dot-net).

This sample assumes that IDM is running on a Windows system on the localhost. It also assumes that Active Directory and the ICF .NET connector server run on a remote Windows server. The PowerShell connector runs on the .NET connector server.

To use this sample for IDM instances installed on UNIX systems, adjust the relevant commands shown with PowerShell prompts.

## Prepare the sample

Run the commands in this procedure from the PowerShell command line. The continuation character used in the command is the back-tick (\`).

1. Install, configure, and start the .NET connector server on the machine that's running an Active Directory Domain Controller or on a workstation where the Microsoft Active Directory PowerShell module is installed.

   Refer to the [instructions on installing the .NET connector server](https://docs.pingidentity.com/openicf/connector-reference/dotnet-server-reference.html).

2. [Configure IDM to connect to the .NET connector server](https://docs.pingidentity.com/openicf/connector-reference/configure-server.html).

3. Extract the `MsPowerShell.Connector.dll` from the .NET RCS archive (`openicf-1.5.7.0-dotnet.zip`) to the same directory as `connectorserver.exe`.

4. Copy the PowerShell scripts and the ADSISearch module from the `samples\scripted-powershell-with-ad\tools` directory, to the machine where the connector server is installed.

   ```
   dir \path\to\openidm\samples\scripted-powershell-with-ad\tools
   Directory: C:\path\to\openidm\samples\scripted-powershell-with-ad\tools

   Mode                LastWriteTime         Length Name
   ----                -------------         ------ ----
   -a----         4/3/2018   3:26 AM           4279 ADAuthenticate.ps1
   -a----         4/3/2018   3:26 AM           9055 ADCreate.ps1
   -a----         4/3/2018   3:26 AM           3717 ADDelete.ps1
   -a----         4/3/2018   3:26 AM          10756 ADSchema.ps1
   -a----         4/3/2018   3:26 AM           4625 ADSearch.ps1
   -a----         4/3/2018   3:26 AM           8064 ADSISearch.psm1
   -a----         4/3/2018   3:26 AM           5918 ADSync.ps1
   -a----         4/3/2018   3:26 AM           2408 ADTest.ps1
   -a----         4/3/2018   3:26 AM          18406 ADUpdate.ps1
   PS C:\path\to\openidm>
   ```

5. Copy the sample connector configuration for the PowerShell connector to your project's `conf` directory:

   ```
   cp \path\to\openidm\samples\example-configurations\provisioners\provisioner.openicf-adpowershell.json \path\to\openidm\conf
   ```

   The following excerpt of the sample connector configuration shows the configuration properties:

   ```json
   "configurationProperties" : {
       "AuthenticateScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADAuthenticate.ps1",
       "CreateScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADCreate.ps1",
       "DeleteScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADDelete.ps1",
       "SchemaScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADSchema.ps1",
       "SearchScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADSearch.ps1",
       "SyncScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADSync.ps1",
       "TestScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADTest.ps1",
       "UpdateScriptFileName" : "C:/openidm/samples/scripted-powershell-with-ad/tools/ADUpdate.ps1",
       "VariablesPrefix" : "Connector",
       "QueryFilterType" : "Ldap",
       "ReloadScriptOnExecution" : true,
       "UseInterpretersPool" : true,
       "SubstituteUidAndNameInQueryFilter" : true,
       "UidAttributeName" : "ObjectGUID",
       "NameAttributeName" : "DistinguishedName",
       "PsModulesToImport" : [
           "ActiveDirectory",
           "C:/openidm/samples/scripted-powershell-with-ad/tools/ADSISearch.psm1"
       ],
       "Host" : "",
       "Port" : null,
       "Login" : "",
       "Password" : null,
       "CustomProperties" : ["baseContext = CN=Users,DC=example,DC=com" ],
       "MinInterpretersPoolSize" : 1,
       "MaxInterpretersPoolSize" : 10
   },
   ```

   The sample connector configuration assumes that the scripts are located in `C:/openidm/samples/scripted-powershell-with-ad/tools/`. If you copied your scripts to a different location or you're using a different base context for search and synchronization operations, such as `DC=example,DC=org`, adjust your connector configuration file accordingly.

   |   |                                                                                                                                               |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The ICF framework requires the path to use forward slash characters and not the backslash characters that you would expect in a Windows path. |

   The host, port, login, and password of the machine where Active Directory runs don't need to be specified here. By default, the Active Directory cmdlets pick up the first available domain controller. In addition, the scripts are run using the credentials of the .Net connector server.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `ReloadScriptOnExecution` property is set to `true` in this sample configuration. This setting causes script files to be reloaded each time the script is invoked. Having script files reloaded each time is suitable for debugging purposes. However, this property should be set to `false` in production environments because the script reloading can have a negative performance impact. |

6. Make sure that the value of the `connectorHostRef` property in the connector configuration file matches the value that you specified in the remote connector configuration file in step 2 of this procedure. For example:

   ```json
   "connectorHostRef" : "dotnet",
   ```

7. [Set up DS](start-here.html#ldap-server-config) without importing any LDIF file or [select another repository](../install-guide/chap-repository.html) for the sample.

## Run the sample

Because you have copied all required configuration files into the default IDM project, you can start IDM with the default configuration (without the `-p` option):

```
\path\to\openidm\startup.bat
```

When IDM has started, test the sample by using the `curl` command-line utility. The following examples test the scripts provided in the `tools` directory.

1. Test the connector configuration and whether IDM is able to connect to the .NET connector server with the following request:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --request POST `
   "http://localhost:8080/openidm/system?_action=test"
   [
     {
       "ok": true,
       "connectorRef": {
         "bundleVersion": "[1.4.2.0,1.5.0.0)",
         "bundleName": "MsPowerShell.Connector",
         "connectorName": "Org.ForgeRock.OpenICF.Connectors.MsPowerShell.MsPowerShellConnector"
       },
       "objectTypes": [
         "__ALL__",
         "group",
         "account"
       ],
       "config": "config/provisioner.openicf/adpowershell",
       "enabled": true,
       "name": "adpowershell"
     }
   ]
   ```

2. Query the users in your Active Directory with the following request:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --request GET `
   "http://localhost:8080/openidm/system/adpowershell/account?_queryId=query-all-ids"
   {
     "remainingPagedResults": -1,
     "pagedResultsCookie": null,
     "resultCount": 1257,
     "result": [
       {
         "_id": "7c41496a-9898-4074-a537-bed696b6be92"
       },
       {
         "_id": "f2e08a5c-473f-4798-a2d5-d5cc27c862a9"
       },
       {
         "_id": "6feef4a0-b121-43dc-be68-a96703a49aba"
       },
   ...
   ```

3. To return the complete record of a specific user, include the ID of the user in the URL. The following request returns the record for `Steven Carter`:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --request GET `
   "http://localhost:8080/openidm/system/adpowershell/account/6feef4a0-b121-43dc-be68-a96703a49aba"
   {
     "_id": "6feef4a0-b121-43dc-be68-a96703a49aba",
     "postalCode": null,
     "passwordNotRequired": false,
     "cn": "Steven Carter",
     "name": "Steven Carter",
     "trustedForDelegation": false,
     "uSNChanged": "47219",
     "manager": null,
     "objectGUID": "6feef4a0-b121-43dc-be68-a96703a49aba",
     "modifyTimeStamp": "11/27/2014 3:37:16 PM",
     "employeeNumber": null,
     "sn": "Carter",
     "userAccountControl": 512,
     "passwordNeverExpires": false,
     "displayName": "Steven Carter",
     "initials": null,
     "pwdLastSet": "130615726366949784",
     "scriptPath": null,
     "badPasswordTime": "0",
     "employeeID": null,
     "badPwdCount": "0",
     "accountExpirationDate": null,
     "userPrincipalName": "steve.carter@ad0.example.com",
     "sAMAccountName": "steve.carter",
     "mail": "steven.carter@example.com",
     "logonCount": "0",
     "cannotChangePassword": false,
     "division": null,
     "streetAddress": null,
     "allowReversiblePasswordEncryption": false,
     "description": null,
     "whenChanged": "11/27/2014 3:37:16 PM",
     "title": null,
     "lastLogon": "0",
     "company": null,
     "homeDirectory": null,
     "whenCreated": "6/23/2014 2:50:48 PM",
     "givenName": "Steven",
     "telephoneNumber": "555-2518",
     "homeDrive": null,
     "uSNCreated": "20912",
     "smartcardLogonRequired": false,
     "distinguishedName": "CN=Steven Carter,CN=Users,DC=example,DC=com",
     "createTimeStamp": "6/23/2014 2:50:48 PM",
     "department": null,
     "memberOf": [
       "CN=employees,DC=example,DC=com"
     ],
     "homePhone": null
   }
   ```

4. Test that you can authenticate as one of the users in your Active Directory. The username that you specify here can be either an ObjectGUID, UPN, sAMAccountname or CN:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --header "Content-Type: application/json" `
   --request POST `
   --data "{
        \"username\" : \"Steven Carter\",
        \"password\" : \"Passw0rd\"
        }" `
   "http://localhost:8080/openidm/system/adpowershell/account?_action=authenticate"
   {
     "_id": "6feef4a0-b121-43dc-be68-a96703a49aba"
   }
   ```

   The request returns the ObjectGUID if the authentication is successful.

5. You can return the complete record for a specific user, using the query filter syntax described in [Construct Queries](../objects-guide/queries.html#constructing-queries).

   The following query returns the record for the guest user:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --request GET `
   "http://localhost:8080/openidm/system/adpowershell/account?_queryFilter=cn+eq+'guest'"
   {
     "remainingPagedResults": -1,
     "pagedResultsCookie": null,
     "resultCount": 1,
     "result": [
       {
         "_id": "f2e08a5c-473f-4798-a2d5-d5cc27c862a9",
         "postalCode": null,
         "passwordNotRequired": true,
         "cn": "Guest",
         "name": "Guest",
         "trustedForDelegation": false,
         "uSNChanged": "8197",
         "manager": null,
         "objectGUID": "f2e08a5c-473f-4798-a2d5-d5cc27c862a9",
         "modifyTimeStamp": "6/9/2014 12:35:16 PM",
         "employeeNumber": null,
         "userAccountControl": 66082,
         "whenChanged": "6/9/2014 12:35:16 PM",
         "initials": null,
         "pwdLastSet": "0",
         "scriptPath": null,
         "badPasswordTime": "0",
         "employeeID": null,
         "badPwdCount": "0",
         "accountExpirationDate": null,
         "sAMAccountName": "Guest",
         "logonCount": "0",
         "cannotChangePassword": true,
         "division": null,
         "streetAddress": null,
         "allowReversiblePasswordEncryption": false,
         "description": "Built-in account for guest access to the computer/domain",
         "userPrincipalName": null,
         "title": null,
         "lastLogon": "0",
         "company": null,
         "homeDirectory": null,
         "whenCreated": "6/9/2014 12:35:16 PM",
         "givenName": null,
         "homeDrive": null,
         "uSNCreated": "8197",
         "smartcardLogonRequired": false,
         "distinguishedName": "CN=Guest,CN=Users,DC=example,DC=com",
         "createTimeStamp": "6/9/2014 12:35:16 PM",
         "department": null,
         "memberOf": [
           "CN=Guests,CN=Builtin,DC=example,DC=com"
         ],
         "homePhone": null,
         "displayName": null,
         "passwordNeverExpires": true
       }
     ]
   }
   ```

6. Test that you can create a user on the Active Directory server by sending a POST request with the `create` action.

   The following request creates the user `Jane Doe` on the Active Directory server:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --header "Content-Type: application/json" `
   --request POST `
   --data '{
     \"distinguishedName\" : \"CN=Jane Doe,CN=Users,DC=EXAMPLE,DC=COM\",
     \"sn\" : \"Doe\",
     \"cn\" : \"Jane Doe\",
     \"sAMAccountName\" : \"sample\",
     \"userPrincipalName\" : \"janedoe@example.com\",
     \"enabled\" : true,
     \"password\" : \"Passw0rd\",
     \"telephoneNumber\" : \"0052-611-091\"
    }' `
   "http://localhost:8080/openidm/system/adpowershell/account?_action=create"
   {
     "_id": "42725210-8dce-4fdf-b0e0-393cf0377fdf",
     "title": null,
     "uSNCreated": "47244",
     "pwdLastSet": "130615892934093041",
     "cannotChangePassword": false,
     "telephoneNumber": "0052-611-091",
     "smartcardLogonRequired": false,
     "badPwdCount": "0",
     "department": null,
     "distinguishedName": "CN=Jane Doe,CN=Users,DC=example,DC=com",
     "badPasswordTime": "0",
     "employeeID": null,
     "cn": "Jane Doe",
     "division": null,
     "description": null,
     "userPrincipalName": "janedoe@example.com",
     "passwordNeverExpires": false,
     "company": null,
     "memberOf": [],
     "givenName": null,
     "streetAddress": null,
     "sn": "Doe",
     "initials": null,
     "logonCount": "0",
     "homeDirectory": null,
     "employeeNumber": null,
     "objectGUID": "42725210-8dce-4fdf-b0e0-393cf0377fdf",
     "manager": null,
     "lastLogon": "0",
     "trustedForDelegation": false,
     "scriptPath": null,
     "allowReversiblePasswordEncryption": false,
     "modifyTimeStamp": "11/27/2014 8:14:53 PM",
     "whenCreated": "11/27/2014 8:14:52 PM",
     "whenChanged": "11/27/2014 8:14:53 PM",
     "accountExpirationDate": null,
     "name": "Jane Doe",
     "displayName": null,
     "homeDrive": null,
     "passwordNotRequired": false,
     "createTimeStamp": "11/27/2014 8:14:52 PM",
     "uSNChanged": "47248",
     "sAMAccountName": "sample",
     "userAccountControl": 512,
     "homePhone": null,
     "postalCode": null
   }
   ```

7. Test that you can update a user object on the Active Directory server by sending a PUT request with the complete object, including the user ID in the URL.

   The following request updates user `Jane Doe`'s entry, including her ID in the request. The update sends the same information that was sent in the `create` request, but adds an `employeeNumber`:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --header "Content-Type: application/json" `
   --header "If-Match: *" `
   --request PUT `
   --data '{
     \"distinguishedName\" : \"CN=Jane Doe,CN=Users,DC=EXAMPLE,DC=COM\",
     \"sn\" : \"Doe\",
     \"cn\" : \"Jane Doe\",
     \"userPrincipalName\" : \"janedoe@example.com\",
     \"enabled\" : true,
     \"password\" : \"Passw0rd\",
     \"telephoneNumber\" : \"0052-611-091\",
     \"employeeNumber\": \"567893\"
    }' `
   "http://localhost:8080/openidm/system/adpowershell/account/42725210-8dce-4fdf-b0e0-393cf0377fdf"
   {
     "_id": "42725210-8dce-4fdf-b0e0-393cf0377fdf",
     "title": null,
     "uSNCreated": "47244",
     "pwdLastSet": "130615906375709689",
     "cannotChangePassword": false,
     "telephoneNumber": "0052-611-091",
     "smartcardLogonRequired": false,
     "badPwdCount": "0",
     "department": null,
     "distinguishedName": "CN=Jane Doe,CN=Users,DC=example,DC=com",
     "badPasswordTime": "0",
     "employeeID": null,
     "cn": "Jane Doe",
     "division": null,
     "description": null,
     "userPrincipalName": "janedoe@example.com",
     "passwordNeverExpires": false,
     "company": null,
     "memberOf": [],
     "givenName": null,
     "streetAddress": null,
     "sn": "Doe",
     "initials": null,
     "logonCount": "0",
     "homeDirectory": null,
     "employeeNumber": "567893",
     "objectGUID": "42725210-8dce-4fdf-b0e0-393cf0377fdf",
     "manager": null,
     "lastLogon": "0",
     "trustedForDelegation": false,
     "scriptPath": null,
     "allowReversiblePasswordEncryption": false,
     "modifyTimeStamp": "11/27/2014 8:37:17 PM",
     "whenCreated": "11/27/2014 8:14:52 PM",
     "whenChanged": "11/27/2014 8:37:17 PM",
     "accountExpirationDate": null,
     "name": "Jane Doe",
     "displayName": null,
     "homeDrive": null,
     "passwordNotRequired": false,
     "createTimeStamp": "11/27/2014 8:14:52 PM",
     "uSNChanged": "47253",
     "sAMAccountName": "sample",
     "userAccountControl": 512,
     "homePhone": null,
     "postalCode": null
   }
   ```

8. Test whether you're able to delete a user object on the Active Directory server by sending a DELETE request with the user ID in the URL.

   The following request deletes user `Jane Doe`'s entry:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --request DELETE `
   "http://localhost:8080/openidm/system/adpowershell/account/42725210-8dce-4fdf-b0e0-393cf0377fdf"
   ```

   The response includes the complete user object that was deleted.

9. You can attempt to query the user object to confirm that it's deleted:

   ```
   curl.exe `
   --header "X-OpenIDM-Username: openidm-admin" `
   --header "X-OpenIDM-Password: openidm-admin" `
   --header "Accept-API-Version: resource=1.0"  `
   --request GET `
   "http://localhost:8080/openidm/system/adpowershell/account/42725210-8dce-4fdf-b0e0-393cf0377fdf"
   {
     "message": "",
     "reason": "Not Found",
     "code": 404
   }
   ```

---

---
title: Connect to DS with ScriptedREST
description: Use the ScriptedREST connector and Groovy scripts to reconcile and sync users and groups between PingIDM and PingDS using the REST API
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:scripted-rest-with-dj
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/scripted-rest-with-dj.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Scripts", "Directory Server", "ScriptedREST"]
section_ids:
  sample-scripted-rest-ds: Set up DS
  sample-scripted-rest-running: Run the sample
---

# Connect to DS with ScriptedREST

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | The PingDS (DS) Rest2ldap HTTP endpoint has been removed from DS. You can use this sample with DS 7.4. |

This sample uses the scripted REST connector and Groovy scripts to interact with the DS REST API. It demonstrates reconciliation, implicit sync, and liveSync between the IDM repository and a DS instance.

The scripted REST connector is bundled with IDM in the JAR `openidm/connectors/scriptedrest-connector-1.5.20.31.jar`.

The Groovy scripts for this sample are in the `samples/scripted-rest-with-dj/tools` directory. Use the scripts as a starting point that you can customize for your deployment.

## Set up DS

1. [Set up DS](start-here.html#ldap-server-config), but remove the line `--set ds-user-data/ldifFile:Example.ldif`.

2. Optionally, [enable an HTTP access logger on the DS server](https://docs.pingidentity.com/pingds/8.1/logging-guide/http-access.html#log-http-access).

3. Import the data required for the sample:

   ```
   /path/to/opendj/bin/ldapmodify \
   --port 1636 \
   --useSSL \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDN uid=admin \
   --bindPassword password \
   --filename /path/to/openidm/samples/scripted-rest-with-dj/data/ldap.ldif
   # ADD operation successful for DN dc=example,dc=com

   # ADD operation successful for DN ou=Administrators,dc=example,dc=com

   # ADD operation successful for DN uid=idm,ou=Administrators,dc=example,dc=com

   # ADD operation successful for DN ou=People,dc=example,dc=com

   # ADD operation successful for DN ou=Groups,dc=example,dc=com
   ```

4. Set up the access control instructions (ACIs) that enable the IDM administrator user to read the DS external change log:

   ```
   /path/to/opendj/bin/dsconfig set-access-control-handler-prop \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDN uid=admin \
   --bindPassword password \
   --add global-aci:"(target=\"ldap:///cn=changelog\")(targetattr=\"*||+\") \
   (version 3.0; acl \"IDM can access cn=changelog\"; \
   allow (read,search,compare) \
   userdn=\"ldap:///uid=idm,ou=Administrators,dc=example,dc=com\";)" \
   --no-prompt
   ```

   ```
   /path/to/opendj/bin/dsconfig set-access-control-handler-prop \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDN uid=admin \
   --bindPassword password \
   --add global-aci:"(targetcontrol=\"1.3.6.1.4.1.26027.1.5.4\") \
   (version 3.0; acl \"IDM changelog control access\"; \
   allow (read) \
   userdn=\"ldap:///uid=idm,ou=Administrators,dc=example,dc=com\";)" \
   --no-prompt
   ```

5. Enable the DS changelog:

   ```
   /path/to/opendj/bin/dsconfig set-replication-server-prop \
   --provider-name Multimaster\ Synchronization \
   --set changelog-enabled:enabled \
   --hostname localhost \
   --port 4444 \
   --bindDn uid=admin \
   --bindPassword password \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --no-prompt
   ```

6. Enable the default Rest2ldap HTTP endpoint:

   ```
   /path/to/opendj/bin/dsconfig set-http-endpoint-prop \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDN uid=admin \
   --bindPassword password \
   --endpoint-name /api \
   --set authorization-mechanism:"HTTP Basic" \
   --set config-directory:config/rest2ldap/endpoints/api \
   --set enabled:true \
   --no-prompt
   ```

   Learn more about [DS HTTP User APIs](https://docs.pingidentity.com/pingds/7.3/config-guide/http-access.html#setup-rest2ldap-endpoint).

7. Replace the default DS REST to LDAP configuration with the configuration for this sample:

   ```
   cp /path/to/openidm/samples/scripted-rest-with-dj/data/example-v1.json /path/to/opendj/config/rest2ldap/endpoints/api/
   ```

8. Restart DS to apply the configuration changes.

   ```
   /path/to/opendj/bin/stop-ds --restart
   Stopping Server...
   ...
   The Directory Server has started successfully
   ```

## Run the sample

This section illustrates the basic CRUD operations on users and groups using the ScriptedREST connector and the DS REST API. Note that the power of the Groovy connector is in the associated Groovy scripts, and their application in your particular deployment. The scripts provided with this sample are specific to the sample and customization of the scripts is required.

1. Start IDM with the configuration for the ScriptedREST sample:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/scripted-rest-with-dj
   ```

2. Check that the scripted REST connector can reach the DS instance by obtaining the connector status over REST:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/system/scriptedrest?_action=test"
   {
     "name": "scriptedrest",
     "enabled": true,
     "config": "config/provisioner.openicf/scriptedrest",
     "connectorRef": {
       "bundleVersion": "[1.5.0.0,1.6.0.0)",
       "bundleName": "org.forgerock.openicf.connectors.scriptedrest-connector",
       "connectorName": "org.forgerock.openicf.connectors.scriptedrest.ScriptedRESTConnector"
     },
     "displayName": "Scripted REST Connector",
     "objectTypes": [
       "__ALL__",
       "account",
       "group"
     ],
     "ok": true
   }
   ```

3. Create a group entry on the DS server:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "cn": "group1"
   }' \
   "http://localhost:8080/openidm/system/scriptedrest/group?_action=create"
   {
     "_id": "group1",
     "members": null,
     "created": "2020-07-21T23:04:25Z",
     "cn": "group1",
     "displayName": "group1"
   }
   ```

4. Create a user entry on the DS server. This command creates a user with the `uid` `scarter`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "givenName": "Steven",
     "familyName": "Carter",
     "emailAddress": "scarter@example.com",
     "telephoneNumber": "444-444-4444",
     "password": "5up35tr0ng",
     "displayName": "Steven.Carter",
     "uid": "scarter"
   }' \
   "http://localhost:8080/openidm/system/scriptedrest/account?_action=create"
   {
     "_id": "scarter",
     "givenName": "Steven",
     "groups": null,
     "displayName": "Steven.Carter",
     "emailAddress": "scarter@example.com",
     "uid": "scarter",
     "created": "2020-07-21T23:07:13Z",
     "familyName": "Carter",
     "telephoneNumber": "444-444-4444"
   }
   ```

   Notice that the user is not a member of any group.

5. Reconcile the DS server with the managed user repository:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   "http://localhost:8080/openidm/recon?_action=recon&mapping=systemRestLdapUser_managedUser&waitForCompletion=true"
   {
     "_id": "ee7534bd-ccfd-4f6a-bdc3-49caa6d2043c-547",
     "state": "SUCCESS"
   }
   ```

6. The reconciliation creates a managed user with a server-assigned ID. To retrieve the ID, run the following query:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request GET \
   "http://localhost:8080/openidm/managed/user?_queryFilter=true&_fields=_id"
   {
     "result": [
       {
         "_id": "4657a420-6608-410e-baa7-f64668cc500c",
         "_rev": "000000007995f006"
       }
     ],
     ...
   }
   ```

7. To initialize liveSync set the sync token by running one liveSync operation over REST:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/system/scriptedrest/account?_action=liveSync"
   {
     "connectorData": {
       "nativeType": "string",
       "syncToken": "8"
     }
   }
   ```

8. Update the `scarter` managed user entry by changing the telephone number. Specify the user ID that you retrieved previously:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PATCH \
   --data '[
     {
       "operation": "replace",
       "field": "telephoneNumber",
       "value": "555-555-5555"
     }
   ]' \
   "http://localhost:8080/openidm/managed/user/4657a420-6608-410e-baa7-f64668cc500c"
   {
     "_id": "4657a420-6608-410e-baa7-f64668cc500c",
     "_rev": "0000000096edf021",
     "userName": "scarter",
     "mail": "scarter@example.com",
     "displayName": "Steven.Carter",
     "telephoneNumber": "555-555-5555",
     "givenName": "Steven",
     "sn": "Carter",
     "accountStatus": "active",
     "effectiveRoles": [],
     "effectiveAssignments": []
   }
   ```

9. Implicit synchronization propagates the change to DS. You can verify this change by reading the `scarter` user entry in DS and noting the new `telephoneNumber`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/scriptedrest/account/scarter"
   {
     "_id": "scarter",
     "familyName": "Carter",
     "givenName": "Steven",
     "created": "2018-02-07T10:14:31Z",
     "uid": "scarter",
     "groups": null,
     "emailAddress": "scarter@example.com",
     "displayName": "Steven.Carter",
     "telephoneNumber": "555-555-5555"
   }
   ```

10. Now, update the `scarter` entry on the DS server by changing the `givenName`:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --header "Content-Type: application/json" \
    --request PATCH \
    --data '[
      {
        "operation": "replace",
        "field": "givenName",
        "value": "Steve"
      }
    ]' \
    "http://localhost:8080/openidm/system/scriptedrest/account/scarter"
    {
      "_id": "scarter",
      "givenName": "Steve",
      "groups": null,
      "displayName": "Steven.Carter",
      "emailAddress": "scarter@example.com",
      "uid": "scarter",
      "created": "2020-07-21T23:07:13Z",
      "familyName": "Carter",
      "telephoneNumber": "555-555-5555"
    }
    ```

11. To propagate the change from DS to the managed user entry, run a liveSync operation. You can define a schedule for liveSync, or run it over REST as shown in the following command:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request POST \
    "http://localhost:8080/openidm/system/scriptedrest/account?_action=liveSync"
    {
      "connectorData": {
        "nativeType": "string",
        "syncToken": "9"
      },
      "_rev": "000000000a585336",
      "_id": "SYSTEMSCRIPTEDRESTACCOUNT"
    }
    ```

12. Verify that the changes propagated by reading scarter's managed user entry and noting the changed `givenName`:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/managed/user/4657a420-6608-410e-baa7-f64668cc500c"
    {
      "_id": "4657a420-6608-410e-baa7-f64668cc500c",
      "_rev": "000000007937efb7",
      "userName": "scarter",
      "mail": "scarter@example.com",
      "displayName": "Steven.Carter",
      "telephoneNumber": "555-555-5555",
      "givenName": "Steve",
      "sn": "Carter",
      "accountStatus": "active",
      "effectiveRoles": [],
      "effectiveAssignments": []
    }
    ```

13. Add user `scarter` to the group you created previously, by updating the group entry:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --header "Content-Type: application/json" \
    --header "If-Match: *" \
    --request PUT \
    --data '{
      "_id": "group1",
      "members": [{"_id": "scarter"}]
    }' \
    "http://localhost:8080/openidm/system/scriptedrest/group/group1"
    {
      "_id": "group1",
      "displayName": "group1",
      "created": "2018-02-07T10:14:12Z",
      "members": [
        {
          "_id": "scarter",
          "displayName": "Steven.Carter"
        }
      ],
      "cn": "group1",
      "lastModified": "2018-02-07T10:20:22Z"
    }
    ```

14. Read the `scarter` user entry in DS to verify that the user is now a member of `group1`:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/system/scriptedrest/account/scarter"
    {
      "_id": "scarter",
      "givenName": "Steve",
      "groups": [
        {
          "_id": "group1"
        }
      ],
      "displayName": "Steven.Carter",
      "emailAddress": "scarter@example.com",
      "uid": "scarter",
      "created": "2020-07-21T23:07:13Z",
      "familyName": "Carter",
      "telephoneNumber": "555-555-5555"
    }
    ```

15. Read the group entry to verify its members:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/system/scriptedrest/group/group1"
    {
      "_id": "group1",
      "lastModified": "2020-07-21T23:17:09Z",
      "members": [
        {
          "_id": "scarter",
          "displayName": "Steven.Carter"
        }
      ],
      "created": "2020-07-21T23:04:25Z",
      "cn": "group1",
      "displayName": "group1"
    }
    ```

16. Reconcile the DS groups with the managed group repository:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request POST \
    "http://localhost:8080/openidm/recon?_action=recon&mapping=systemRestLdapGroup_managedGroup&waitForCompletion=true"
    {
      "_id": "ee7534bd-ccfd-4f6a-bdc3-49caa6d2043c-1477",
      "state": "SUCCESS"
    }
    ```

17. The reconciliation creates a managed group with a server-assigned ID. To retrieve the group ID, run the following query:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --header "Content-Type: application/json" \
    --request GET \
    "http://localhost:8080/openidm/managed/group?_queryId=query-all-ids"
    {
      "result": [
        {
          "_id": "67b5ec50-d5a6-4bfa-bb19-17965447ad00",
          "_rev": "00000000b0e95e9b"
        }
      ],
      ...
    }
    ```

18. Read the managed group to verify that the DS group and its members were reconciled. Specify the ID that you retrieved in the previous step:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/managed/group/67b5ec50-d5a6-4bfa-bb19-17965447ad00"
    {
      "_id": "67b5ec50-d5a6-4bfa-bb19-17965447ad00",
      "_rev": "00000000b0e95e9b",
      "members": [
        {
          "_id": "scarter",
          "displayName": "Steven.Carter"
        }
      ],
      "displayName": "group1"
    }
    ```

19. Delete the user and group entries from DS to return the server to its initial state.

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request DELETE \
    "http://localhost:8080/openidm/system/scriptedrest/account/scarter"
    {
      "_id": "scarter",
      "givenName": "Steve",
      "groups": [
        {
          "_id": "group1"
        }
      ],
      "displayName": "Steven.Carter",
      "emailAddress": "scarter@example.com",
      "uid": "scarter",
      "created": "2020-07-21T23:07:13Z",
      "familyName": "Carter",
      "telephoneNumber": "555-555-5555"
    }
    ```

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request DELETE \
    "http://localhost:8080/openidm/system/scriptedrest/group/group1"
    {
      "_id": "group1",
      "lastModified": "2020-07-21T23:17:09Z",
      "members": null,
      "created": "2020-07-21T23:04:25Z",
      "cn": "group1",
      "displayName": "group1"
    }
    ```

---

---
title: Create a custom endpoint
description: Configure and test a PingIDM custom REST endpoint using Groovy or JavaScript scripts that return request details for each HTTP method
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:custom-endpoint
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/custom-endpoint.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Customization", "Endpoints"]
section_ids:
  run_the_sample: Run the sample
---

# Create a custom endpoint

Scriptable custom endpoints let you launch arbitrary scripts using the IDM REST URI. For information about how custom endpoints are configured, refer to [Create custom endpoints to launch scripts](../scripting-guide/script-custom-endpoints.html).

The example endpoint provided in `/path/to/openidm/samples/example-configurations/custom-endpoint` illustrates the configuration of a custom endpoint, and the structure of custom endpoint scripts.

The purpose of this custom endpoint is to return a list of variables available to each method used in a script. The scripts show the complete set of methods that can be used. These methods map to the standard HTTP verbs - create, read, update, delete, patch, query, and action. A sample JavaScript and Groovy script are provided.

## Run the sample

1. Copy the endpoint configuration file (`samples/example-configurations/custom-endpoint/conf/endpoint-echo.json` ) to your project's `conf` directory.

2. Copy either the JavaScript file (`samples/example-configurations/custom-endpoint/script/echo.js` ) or Groovy script file (`samples/example-configurations/custom-endpoint/script/echo.groovy` ) to your project's `script` directory.

3. Open the endpoint configuration file in a text editor:

   ```json
   {
       "file" : "echo.groovy",
       "type" : "groovy",
       "_file" : "echo.js",
       "_type" : "text/javascript",
       ...
   }
   ```

   The configuration file contains a reference to the endpoint scripts. In this case, the JavaScript script is commented out (with an underscore before the `file` and `type` properties). If you want to use the JavaScript endpoint script, uncomment these lines and comment out the lines that correspond to the Groovy script in the same way.

   Endpoint configuration files can include a `context` property that specifies the route to the endpoint, for example:

   ```json
   "context" : "endpoint/linkedView/*"
   ```

   If no `context` is specified, the route to the endpoint is taken from the file name, in this case `endpoint/echo`.

4. Test each method in succession to return the expected request structure of that method. The following examples show the request structure of the read, create and patch methods. The configuration file has been edited to use the JavaScript file, rather than the Groovy file. The output shown in these examples has been cropped for legibility. For a description of each parameter, refer to [Custom Endpoint Scripts](../scripting-guide/script-custom-endpoints.html#custom-endpoint-scripts).

   * The following command performs a read on the echo endpoint and returns the request structure of a read request:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request GET \
     "http://localhost:8080/openidm/endpoint/echo"
     {
       "_id": "",
       "method": "read",
       "context": {
         "class": "org.forgerock.http.routing.ApiVersionRouterContext",
         "name": "apiVersionRouter",
         "defaultVersionBehaviour": "LATEST",
         "warningEnabled": false,
         "resourceVersion": "1.0",
         "parent": {
           "class": "org.forgerock.http.routing.UriRouterContext",
           "name": "router",
           ...
         }
       },
       "resourceName": "",
       "parameters": {}
     }
     ```

   * The following command performs a query on the echo endpoint and returns the request structure of a query request:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request GET \
     "http://localhost:8080/openidm/endpoint/echo?_queryFilter=true"
     {
       "result": [
         {
           "method": "query",
           "pageSize": 0,
           "queryFilter": "true",
           "resourceName": "",
           "pagedResultsOffset": 0,
           "pagedResultsCookie": null,
           "parameters": {},
           "content": null,
           "queryId": null
           "content": null,
           "context": {
           ...
           }
         }
       ],
       ...
     }
     ```

   * The following command sends a create request to the echo endpoint. No user is actually created. The endpoint script merely returns the request structure of a create request. The `content` parameter in this case provides the JSON object that was sent with the request:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --header "Content-Type: application/json" \
     --data '{
            "userName":"steve",
            "givenName":"Steve",
            "sn":"Carter",
            "telephoneNumber":"0828290289",
            "mail":"scarter@example.com",
            "password":"Passw0rd"
            }' \
     --request POST \
     "http://localhost:8080/openidm/endpoint/echo?_action=create"
     {
       "_id": "",
       "method": "create",
       "resourceName": "",
       "newResourceId": null,
       "parameters": {},
       "content": {
         "userName": "steve",
         "givenName": "Steve",
         "sn": "Carter",
         "telephoneNumber": "0828290289",
         "mail": "scarter@example.com",
         "password": "Passw0rd"
       },
       "context": {
       ...
       }
     }
     ```

   * The following command sends a patch request to the echo endpoint.

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --header "Content-Type: application/json" \
     --data '[
         {
           "operation":"replace",
           "field":"/givenName",
           "value":"Steven"
         }
      ]' \
     --request PATCH \
     "http://localhost:8080/openidm/endpoint/echo"
     {
       "_id": "",
       "method": "patch",
       "resourceName": "",
       "revision": null,
       "patch": [
         {
           "operation": "replace",
           "field": "/givenName",
           "value": "Steven"
         }
       ],
       "parameters": {},
       "context": {
       ...
       }
     }
     ```

---

---
title: Direct audit information to a JMS broker
description: (Deprecated; JMS handler deprecated) Configure PingIDM to publish audit events to a JMS broker using Apache ActiveMQ Artemis
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:audit-jms
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/audit-jms.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "JMS", "Audit"]
section_ids:
  dependencies_for_jms_messaging: Dependencies for JMS messaging
  configure_ssl_for_apache_activemq_artemis: Configure SSL for Apache ActiveMQ Artemis
  audit-jms-secure-secure: Configure a secure port for JMS messages
  jms-sample-start: Start the ActiveMQ Artemis broker and IDM
  jms-sample-consume: Configure and use a JMS consumer application
---

# Direct audit information to a JMS broker

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](../audit-guide/configuring-topic-handlers.html#audit-jms-handler), [Repository](../audit-guide/configuring-topic-handlers.html#audit-repo-handler), [Router](../audit-guide/configuring-topic-handlers.html#audit-router-handler), and [Syslog](../audit-guide/configuring-topic-handlers.html#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

This sample shows how to configure a Java Message Service (JMS) audit event handler to direct audit information to a JMS broker.

JMS is an API that supports Java-based peer-to-peer messages between clients. The JMS API can create, send, receive, and read messages, reliably and asynchronously. You can set up a JMS audit event handler to publish messages that comply with the [Java Message Service Specification Final Release 1.1](https://download.oracle.com/otndocs/jcp/7195-jms-1.1-fr-spec-oth-JSpec/).

This sample demonstrates the use of the JMS audit event handler. In the sample you will set up communication between IDM and an external JMS Message Broker, as well as [Apache ActiveMQ Artemis](http://activemq.apache.org/) as the JMS provider and message broker.

|   |                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | JMS topics are not related to Ping audit event topics. The Ping implementation of JMS topics uses the [publish/subscribe messaging domain](https://docs.oracle.com/javaee/6/tutorial/doc/bncdx.html#bnced) to direct messages to the JMS audit event handler. In contrast, Ping audit event topics specify categories of events. |

## Dependencies for JMS messaging

The JMS audit event handler requires Apache ActiveMQ Artemis and additional dependencies bundled with the ActiveMQ Artemis delivery. This section lists the dependencies, and where they must be installed in the IDM instance. If you use a different ActiveMQ version, you may need to download the corresponding dependencies separately.

1. Download the following files:

   * [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis/download/).

     |   |                                             |
     | - | ------------------------------------------- |
     |   | This sample was tested with version 2.20.0. |

   * The most recent `bnd` JAR file from <https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/>.

     |   |                                                                                                                   |
     | - | ----------------------------------------------------------------------------------------------------------------- |
     |   | The [bnd](https://bnd.bndtools.org/) utility lets you create OSGi bundles for libraries that do not support OSGi. |

2. Unpack the ActiveMQ Artemis archive. For example:

   ```
   tar -xvf ~/Downloads/apache-artemis-2.20.0-bin.tar.gz
   ```

3. Create a temporary directory, and then change to that directory:

   ```
   mkdir ~/Downloads/tmp
   cd ~/Downloads/tmp/
   ```

4. Move the ActiveMQ Artemis Client and `bnd` JAR files to the temporary directory.

   ```
   mv ~/Downloads/apache-artemis-2.20.0/lib/client/artemis-jms-client-all-2.20.0.jar ~/Downloads/tmp/
   mv ~/Downloads/biz.aQute.bnd-version.jar ~/Downloads/tmp/
   ```

5. Create an OSGi bundle:

   1. In a text editor, create a BND file named `activemq.bnd` with the following contents, and save it to the current directory:

      ```
      version=2.20.0
      Export-Package: *;version=${version}
      Import-Package: !org.apache.log4j.*,!org.apache.log.*,!org.apache.avalon.framework.logger.*,!org.apache.avalon.framework.logger.*,!org.glassfish.json.*,!org.conscrypt.*,!org.apache.logging.*,!org.bouncycastle.jsse.*,!org.eclipse.*,!sun.security.*,!reactor.*,!org.apache.activemq.artemis.shaded.*,!com.aayushatharva.*,!com.github.luben.zstd,!com.jcraft.jzlib,!com.ning.compress,!com.ning.compress.lzf,!com.ning.compress.lzf.util,!com.oracle.svm.core.annotate,!lzma.*,!net.jpountz.*,*
      Bundle-Name: ActiveMQArtemis :: Client
      Bundle-SymbolicName: org.apache.activemq
      Bundle-Version: ${version}
      ```

      Your `tmp/` directory should now contain the following files:

      ```
      ls -1 ~/Downloads/tmp/
      activemq.bnd
      artemis-jms-client-all-2.20.0.jar
      biz.aQute.bnd-version.jar
      ```

   2. In the same directory, create the OSGi bundle archive file. For example:

      ```
      java -jar biz.aQute.bnd-version.jar wrap \
      --properties activemq.bnd \
      --output artemis-jms-client-all-2.20.0-osgi.jar \
      artemis-jms-client-all-2.20.0.jar
      ```

6. Copy the resulting `artemis-jms-client-all-2.20.0-osgi.jar` file to the `openidm/bundle` directory:

   ```
   cp artemis-jms-client-all-2.20.0-osgi.jar /path/to/openidm/bundle/
   ```

## Configure SSL for Apache ActiveMQ Artemis

For information on configuring Apache ActiveMQ Artemis security features, including SSL, download [ActiveMQ Artemis 2.2.0](https://archive.apache.org/dist/activemq/activemq-artemis/2.2.0/) and view the included documentation.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also view the [latest Apache Artemis documentation](https://artemis.apache.org/components/artemis/documentation/latest/index.html), but the features described might differ from the version tested with IDM. |

### Configure a secure port for JMS messages

If you configured SSL for ActiveMQ Artemis, edit `/path/to/openidm/samples/audit-jms/conf/audit.json`, and replace the `java.naming.provider.url`:

```json
"java.naming.provider.url" : "ssl://localhost:61617?daemon=true"
```

## Start the ActiveMQ Artemis broker and IDM

With the appropriate bundles in the `/path/to/openidm/bundle/` directory, you can start the ActiveMQ Artemis message broker, and then start IDM with the configuration for this sample.

|   |                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a full list of ActiveMQ Artemis setup options, refer to [Using the Server](https://activemq.apache.org/components/artemis/documentation/latest/using-server.html) in the *ActiveMQ Artemis Documentation*. |

1. Navigate to the directory where you unpacked the ActiveMQ Artemis binary and run the following command to create the Artemis broker:

   ```
   cd ~/Downloads/apache-artemis-2.20.0/bin
   ./artemis create fr-audit
   Creating ActiveMQ Artemis instance at: /path/to/Downloads/apache-artemis-2.20.0/bin/fr-audit
   ...
   ```

2. Start the newly created ActiveMQ Artemis broker:

   ```
   ./fr-audit/bin/artemis run
   ```

3. [Set up DS](start-here.html#ldap-server-config) without importing any LDIF file or [select another repository](../install-guide/chap-repository.html) for the sample.

4. Start IDM with the sample configuration:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/audit-jms
   ```

   |   |                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you see the following error in the OSGi console, make sure that you have installed all the required dependencies and that you have started the ActiveMQ Artemis broker.```
   SEVERE: Unable to create JmsAuditEventHandler 'jms': null
   ``` |

## Configure and use a JMS consumer application

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

To take advantage of the ActiveMQ Artemis event broker, the JMS audit sample includes a Java consumer in the following directory: `/path/to/openidm/samples/audit-jms/consumer/`

1. Assuming you have Apache Maven installed on the local system, you can compile the sample consumer with the following commands:

   ```
   cd /path/to/openidm/samples/audit-jms/consumer/
   mvn clean install
   ```

   When the build process is complete, you'll see a `BUILD SUCCESS` message:

   ```none
   [INFO] ------------------------------------------------------------------------
   [INFO] BUILD SUCCESS
   [INFO] ------------------------------------------------------------------------
   [INFO] Total time: 22.852 s
   [INFO] Finished at: 2017-02-17T17:21:35+02:00
   [INFO] Final Memory: 18M/148M
   [INFO] ------------------------------------------------------------------------
   ```

   |   |                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You might see `[WARNING]` messages during the build. As long as the messages end with `BUILD SUCCESS`, you can proceed with the JMS consumer application. |

2. When the consumer is compiled, run one of the following commands in the same directory to output audit messages related to IDM actions:

   * If you *haven't* configured ActiveMQ Artemis on a secure port:

     ```
     mvn \
     exec:java \
     -Dexec.mainClass="consumer.src.main.java.SimpleConsumer" \
     -Dexec.args="org.apache.activemq.artemis.jndi.ActiveMQInitialContextFactory tcp://localhost:61616"
     ```

   * If you've configured ActiveMQ Artemis on a secure port:

     ```
     MAVEN_OPTS="-Djavax.net.ssl.trustStore=/path/to/openidm/security/truststore" \
     mvn \
     exec:java \
     -Dexec.mainClass="consumer.src.main.java.SimpleConsumer" \
     -Dexec.args="org.apache.activemq.artemis.jndi.ActiveMQInitialContextFactory ssl://localhost:61617?daemon=true"
     ```

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | Look for the message `READY, listening for messages`. |

3. Try some actions on IDM, either in a different console or in the admin UI. Watch the output in the `SimpleConsumer` console. For example:

   ```json
   --------Message Wed 2022.05.11 at 15:47:07.007 PDT--------
   {"auditTopic":"authentication","event":{"_id":"1c25a7d3-e04b-4e4f-ba02-dfca7b2b0dbd-2883","timestamp":"2022-05-11T22:47:06.375Z","eventName":"SESSION","transactionId":"1c25a7d3-e04b-4e4f-ba02-dfca7b2b0dbd-2880","trackingIds":["d7cd0e66-4d48-4e71-90ec-357c93938c82","1cab8896-9af1-431a-aee8-45b5696e8e52"],"userId":"openidm-admin","principal":["openidm-admin"],"entries":[{"moduleId":"JwtSession","result":"SUCCESSFUL","info":{"org.forgerock.authentication.principal":"openidm-admin"}}],"result":"SUCCESSFUL","provider":null,"method":"JwtSession"},"_topic":"authentication"}
   ----------------------------------------------------------
   ```

---

---
title: Direct audit information to MySQL
description: Configure PingIDM to route audit event logs to a MySQL database using the ScriptedSQL Groovy Connector and CSV reconciliation
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:audit-jdbc
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/audit-jdbc.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "MySQL", "Audit"]
section_ids:
  audit-config-files: About the configuration files
  external-audit-mysql-sample: Configure the MySQL database
  run-audit-jdbc: Run the sample
---

# Direct audit information to MySQL

The sample includes an external CSV file and a mapping between objects in that file and the managed user repository. The reconciliations across this mapping generate the audit records that will be directed to the MySQL database. The connection to the MySQL database is through a ScriptedSQL implementation of the Groovy Connector Toolkit.

## About the configuration files

The files that demonstrate the functionality of this sample are located under `/path/to/openidm/samples/audit-jdbc/`, in the `conf/` and `data/` directories.

The following files play important roles in this sample:

* `conf/provisioner.openicf-auditdb.json`

  This file provides the configuration for the Scripted SQL implementation of the Groovy Connector. The file specifies, among other things, the connection details to the MySQL database, the connector version information, and the object types that are supported for this connection. For more information, refer to [Groovy Connector Toolkit](https://docs.pingidentity.com/openicf/connector-reference/groovy.html).

* `conf/provisioner.openicf-csvfile.json`

  This file provides the configuration for this instance of the CSV connector. It includes, among other things, the location of the CSV file resource.

* `conf/sync.json`

  Provides the mapping between managed users and the data set in the CSV file.

* `conf/audit.json`

  This file configures the router as the [audit event handler](../audit-guide/audit.html#configuring-topic-handlers), and routes audit logs to a remote system, identified as `auditdb`.

* `data/csvConnectorData.csv`

  This file contains the sample data set that will be reconciled to the managed user repository.

* `data/sample_audit_db.mysql`

  This file sets up the schema for the MySQL database that will contain the audit logs.

* `tools/*.groovy`

  The Groovy scripts in this directory allow the connector to perform operations on the MySQL database.

## Configure the MySQL database

The sample assumes the following MySQL configuration:

* The database is available on the local host.

* The database listens on the standard MySQL port, 3306.

* You can connect to the MySQL database, as user `root` with password `password`.

Before you start this sample, MySQL must be installed and running, and must include the database required for the sample. In addition, IDM must include the connector JAR required to connect to the MySQL database.

1. Install and configure MySQL.

2. This step sets up an `audit` database with tables that correspond to the various audit events. When MySQL is up and running, import the database schema to set up the database required for the sample:

   ```
   mysql -u root -p < /path/to/openidm/samples/audit-jdbc/data/sample_audit_db.mysql
   Enter password:password
   ```

3. To view the tables in the audit database, use the following command:

   ```
   mysql -u root -p
   Enter password:password
   mysql> use audit
   Reading table information for completion of table and column names
   You can turn off this feature to get a quicker startup with -A

   Database changed
   mysql> show tables;
   +---------------------+
   | Tables_in_audit     |
   +---------------------+
   | auditaccess         |
   | auditactivity       |
   | auditauthentication |
   | auditconfig         |
   | auditrecon          |
   | auditsync           |
   +---------------------+
   6 rows in set (0.00 sec)
   ```

4. Download [MySQL Connector/J](https://dev.mysql.com/downloads/connector/j/), version 8.0 or later from the MySQL website. Unpack the delivery, and copy the .jar into the `openidm/bundle` directory:

   ```
   cp mysql-connector-java-version-bin.jar /path/to/openidm/bundle/
   ```

5. Edit the `url` property in the SQL connector configuration file (`openidm/samples/audit-jdbc/conf/provisioner.openicf-auditdb.json`) to match the host and port of your MySQL instance. The default configuration is as follows:

   ```
   "url" : "jdbc:mysql://localhost:3306/audit?serverTimezone=UTC",
   ```

   |   |                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The default configuration expects SSL, *which is strongly advised in a production environment*. If you are running this in a test environment, you can bypass the SSL requirement:- Add `&useSSL=false` to the end of the `url`.

   - If you are running MySQL 8.0.11+, add `&allowPublicKeyRetrieval=true` to the end of the `url`. |

## Run the sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

In this section, you will start IDM, then run a reconciliation between the CSV file and the managed user repository. After the reconciliation, you should be able to read the audit logs in the `audit` database on your MySQL instance.

1. [Set up DS](start-here.html#ldap-server-config) without importing any LDIF file or [select another repository](../install-guide/chap-repository.html) for the sample.

2. Prepare IDM as described in [Prepare IDM](start-here.html#preparing-openidm), then start the server with the configuration for this sample:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/audit-jdbc
   ```

3. Reconcile the two data sources.

   * To run the reconciliation over REST, use the following command:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request POST \
     "http://localhost:8080/openidm/recon?_action=recon&mapping=systemCsvfileAccounts_managedUser&waitForCompletion=true"
     {
       "_id": "a3664c26-bf82-4100-b411-19edc248c306-7",
       "state": "SUCCESS"
     }
     ```

   * To run the reconciliation from the admin UI, select Configure > Mappings, select the `systemCsvfileAccounts_managedUser` mapping, and then select Reconcile.

4. Inspect the tables in the `audit` database to see how the logs have been routed to that location.

   The following example displays the reconciliation audit logs:

   ```
   mysql -u root -p
   Enter password:password...
   mysql> use audit;...
   mysql> show tables;
   +---------------------+
   +---------------------+
   | Tables_in_audit     |
   +---------------------+
   | auditaccess         |
   | auditactivity       |
   | auditauthentication |
   | auditconfig         |
   | auditrecon          |
   | auditsync           |
   +---------------------+
   6 rows in set (0.00 sec)
   mysql> select * from auditactivity;

   +----+-------------+--------------------------+-------------+----------------+---------------+...+
   | id | objectid    | activitydate             | eventname   | transactionid  | userid        |...|
   +----+-------------+--------------------------+-------------+----------------+---------------+...+
   |  1 | 9927b8db*   | 2021-01-25T12:53:00.800Z | activity    | 9927b8db*      | openidm-admin |...|
   ```

   You can inspect the other audit logs in the same way.

5. By default, the audit configuration in this sample uses the router audit handler for queries, as indicated in the following line from the `conf/audit.json` file:

   ```json
   "handlerForQueries" : "router",
   ```

   With this configuration, when you query the audit logs over REST, the audit data is returned from the router handler (in this case the MySQL database). The following example shows how to query the activity audit log:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/audit/activity?_queryFilter=true"
   {
     "result": [
       {
         "_id": "9927b8db-4537-467f-a077-dbe8cab2a4c8-1187",
         "timestamp": "2021-01-25T12:53:00.800Z",
         "userId": "openidm-admin",
         "operation": "CREATE",
         "changedFields": null,
         "objectId": "managed/user/47527af8-f7d5-4b4b-9d8e-af45169016d4",
         "eventName": "activity",
         "trackingIds": null,
         "transactionId": "9927b8db-4537-467f-a077-dbe8cab2a4c8-1109",
         "runAs": "openidm-admin",
         "passwordChanged": false,
         "message": "create",
         "status": "SUCCESS"
       },
     ],
    ...
   }
   ```

   You can query the other [audit logs](../audit-guide/querying-audit-over-rest.html) in the same way.

---

---
title: Link historical accounts
description: Retain and track inactive linked LDAP accounts for PingIDM managed users using custom scripts that record link dates and account state
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:historical-account-linking
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/historical-account-linking.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Link", "Historical Accounts"]
section_ids:
  historical-accounts-overview: Sample overview
  run-sample-historical-accounts: Run the sample
---

# Link historical accounts

This sample demonstrates the retention of inactive (historical) LDAP accounts that have been linked to a corresponding managed user account. The sample builds on [Two-way synchronization between LDAP and IDM](sync-with-ldap-bidirectional.html) and uses the LDAP connector to connect to a PingDS (DS) instance. You can use any LDAP-v3 compliant directory server.

## Sample overview

In this sample, IDM is the source resource. Managed users in the IDM repository maintain a list of the accounts to which they have been linked on the local LDAP server. This list is stored in the `historicalAccounts` field of the managed user entry. The list contains a reference to all past and current LDAP accounts. Each LDAP account in the list is represented as a [relationship](../objects-guide/relationships.html) and includes information about the date the accounts were linked or unlinked, and whether the account is currently active.

This sample includes the following custom scripts, in its `script` directory:

* `onLink-managedUser_systemLdapAccounts.js`

  When a managed user object is linked to a target LDAP object, this script creates the relationship entry in the managed user's `historicalAccounts` property. The script adds two relationship properties:

  * `linkDate`: Specifies the date that the link was created.

  * `active`: Boolean true/false. When set to true, this property indicates that the target object is *currently* linked to the managed user account.

* `onUnlink-managedUser_systemLdapAccounts.js`

  When a managed user object is unlinked from a target LDAP object, this script updates that relationship entry's properties with an `unlinkDate` that specifies when the target was unlinked, and sets the `active` property to false, indicating that the target object is no longer linked.

* `check_account_state_change.js`

  During liveSync or reconciliation, this script checks if the LDAP account state has changed. If the state has changed, the script updates the historical account properties to indicate the new state (enabled or disabled), and the date that the state was changed. This date can only be approximated and is set to the time that the change was detected by the script.

* `ldapBackCorrelationQuery.js`

  This script correlates entries in the LDAP directory with managed user identities in IDM.

## Run the sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

This section walks you through each step of the sample to demonstrate how historical accounts are stored.

1. [Set up DS](start-here.html#ldap-server-config) using `/path/to/openidm/samples/historical-account-linking/data/Example.ldif`.

2. In the `/path/to/opendj/bin/dsconfig` directory, use the `set-replication-server-prop` command to set `changelog-enabled` to `enabled` in DS:

   ```
   /path/to/opendj/bin/dsconfig set-replication-server-prop \
   --provider-name Multimaster\ Synchronization \
   --set changelog-enabled:enabled \
   --hostname localhost \
   --port 4444 \
   --bindDn uid=admin \
   --bindPassword password \
   --trustAll \
   --no-prompt
   ```

3. Use the `get-replication-server-prop` command to verify the server properties:

   ```
   /path/to/opendj/bin/dsconfig get-replication-server-prop \
   --provider-name Multimaster\ Synchronization \
   --hostname localhost \
   --port 4444 \
   --bindDn uid=admin \
   --bindPassword password \
   --trustAll \
   --no-prompt
   ```

   | `Property`                           | `Values`                                                                                                                                                  |
   | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `advertised-listen-address`          | `localhost`                                                                                                                                               |
   | `changelog-enabled`                  | `enabled`                                                                                                                                                 |
   | `changelog-enabled-excluded-domains` | `When changelog is enabled, searches using "change numbers" are available for all domains (in other words, change number indexing includes all domains).` |
   | `confidentiality-enabled`            | `false`                                                                                                                                                   |
   | `listen-address`                     | `0.0.0.0`                                                                                                                                                 |
   | `replication-db-directory`           | `changelogDb`                                                                                                                                             |
   | `replication-port`                   | `8989`                                                                                                                                                    |
   | `weight`                             | `1`                                                                                                                                                       |

4. [Prepare IDM](start-here.html#preparing-openidm), and start the server using the sample configuration:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/historical-account-linking
   ```

5. Create a user, Joe Smith, in IDM:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "userName": "joe.smith",
     "givenName": "Joe",
     "sn" : "Smith",
     "password" : "Passw0rd",
     "displayName" : "Joe Smith",
     "mail" : "joe.smith@example.com"
   }' \
   "http://localhost:8080/openidm/managed/user?_action=create"
   {
     "_id": "24356bf0-f026-4dc1-9f68-2a571b0a236f",
     "_rev": "00000000c8dc2137",
     "userName": "joe.smith",
     "givenName": "Joe",
     "sn": "Smith",
     "displayName": "Joe Smith",
     "mail": "joe.smith@example.com",
     "accountStatus": "active",
     "effectiveRoles": [],
     "effectiveAssignments": []
   }
   ```

   Record Joe Smith's system-generated `_id`.

6. Verify that the user Joe Smith was created in DS.

   Because implicit synchronization is enabled by default, any change to the managed/user repository should be propagated to DS. Learn more about implicit synchronization in [Synchronization types](../synchronization-guide/sync-types.html).

   The following command returns all users in DS and shows that user joesmith was created successfully:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/ldap/account?_queryFilter=true&_fields=_id,dn"
   {
     "result": [
       {
         "_id": "0da50512-79bb-3461-bd04-241ee4c785bf",
         "dn": "uid=jdoe,ou=People,dc=example,dc=com"
       },
       {
         "_id": "887732e8-3db2-31bb-b329-20cd6fcecc05",
         "dn": "uid=bjensen,ou=People,dc=example,dc=com"
       },
       {
         "_id": "da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
         "dn": "uid=joe.smith0,ou=People,dc=example,dc=com"
       }
     ],
     ...
   }
   ```

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Joe Smith's `uid` in DS is appended with a `0`. The `onCreate` script, defined in the mapping (`sync.json`), increments the `uid` each time a new DS entry is linked to the same managed user object. |

7. Verify that the historical account *relationship object* that corresponds to this linked LDAP account was created in the IDM repository.

   The following command queries Joe Smith's managed user entry and returns all of the `historicalAccounts` for that entry:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/user/24356bf0-f026-4dc1-9f68-2a571b0a236f/historicalAccounts?_queryFilter=true"
   {
     "result": [
       {
         "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
         "_rev": "00000000c2beced4",
         "_ref": "system/ldap/account/da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
         "_refResourceCollection": "system/ldap/account",
         "_refResourceId": "da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
         "_refProperties": {
           "active": true,
           "stateLastChanged": "Mon May 18 2020 13:47:18 GMT+0200 (SAST)",
           "state": "enabled",
           "linkDate": "Mon May 18 2020 13:47:18 GMT+0200 (SAST)",
           "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
           "_rev": "00000000c2beced4"
         }
       }
     ],
     ...
   }
   ```

   At this stage, Joe Smith has only one historical account link—the link to `system/ldap/account/da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa`, which corresponds to the DN `"dn": "uid=joe.smith0,ou=People,dc=example,dc=com"`. Note that the relationship properties (`_refProperties`) show the following information about the linked accounts:

   * The date the accounts were linked.

   * This link is currently active.

   * The account state in DS (`enabled`).

8. Enable the liveSync schedule to propagate changes made in DS to the managed user repository.

   To start liveSync, set `enabled` to `true` in the `conf/schedule-liveSync.json` file:

   ```
   more /path/to/openidm/samples/historical-account-linking/conf/schedule-liveSync.json
   {
       "enabled" : true,
       "type" : "simple",
       "repeatInterval" : 15000,
   ...
   ```

9. Use the `manage-account` command in the `opendj/bin` directory to disable Joe Smith's account in DS:

   ```
   /path/to/opendj/bin/manage-account set-account-is-disabled \
   --port 4444 \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDN uid=admin \
   --bindPassword password \
   --operationValue true \
   --targetDN uid=joe.smith0,ou=people,dc=example,dc=com
   Account Is Disabled:  true
   ```

   Within 15 seconds, according to the configured schedule, liveSync should pick up the change. IDM should then adjust the `state` property in Joe Smith's managed user account.

10. To make sure that the linked account state has changed, request Joe Smith's historical accounts:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/managed/user/24356bf0-f026-4dc1-9f68-2a571b0a236f/historicalAccounts?_queryFilter=true"
    {
      "result": [
        {
          "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
          "_rev": "00000000d430e15a",
          "_ref": "system/ldap/account/da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
          "_refResourceCollection": "system/ldap/account",
          "_refResourceId": "da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
          "_refProperties": {
            "active": true,
            "stateLastChanged": "Mon May 18 2020 13:51:06 GMT+0200 (SAST)",
            "state": "disabled",
            "linkDate": "Mon May 18 2020 13:47:18 GMT+0200 (SAST)",
            "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
            "_rev": "00000000d430e15a"
          }
        }
      ],
      ...
    }
    ```

11. Now, deactivate Joe Smith's managed user account by setting his `accountStatus` property to `inactive`.

    To do this using the admin UI, select Manage > User, select Joe Smith's account, and change the Status to *inactive* on the Details tab.

    This command deactivates Joe Smith's account over REST:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --header "Content-Type: application/json" \
    --request PATCH \
    --data '[
      { "operation" : "replace",
        "field" : "accountStatus",
        "value" : "inactive" }
    ]' \
    "http://localhost:8080/openidm/managed/user/24356bf0-f026-4dc1-9f68-2a571b0a236f"
    {
      "_id": "24356bf0-f026-4dc1-9f68-2a571b0a236f",
      "_rev": "000000004cc82207",
      "userName": "joe.smith",
      "givenName": "Joe",
      "sn": "Smith",
      "displayName": "Joe Smith",
      "mail": "joe.smith@example.com",
      "accountStatus": "inactive",
      "effectiveRoles": [],
      "effectiveAssignments": []
    }
    ```

12. Request Joe Smith's historical accounts:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/managed/user/24356bf0-f026-4dc1-9f68-2a571b0a236f/historicalAccounts?_queryFilter=true"
    {
      "result": [
        {
          "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
          "_rev": "0000000037beefe7",
          "_ref": "system/ldap/account/da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
          "_refResourceCollection": "system/ldap/account",
          "_refResourceId": "da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
          "_refProperties": {
            "active": false,
            "stateLastChanged": "Mon May 18 2020 13:51:06 GMT+0200 (SAST)",
            "state": "disabled",
            "linkDate": "Mon May 18 2020 13:47:18 GMT+0200 (SAST)",
            "unlinkDate": "Mon May 18 2020 13:52:33 GMT+0200 (SAST)",
            "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
            "_rev": "0000000037beefe7"
          }
        }
      ]
      ...
    }
    ```

13. Activate Joe Smith's managed user account by setting his `accountStatus` property to active. This action should create a new entry in DS (with `uid=joe.smith1`) and a new link from Joe Smith's managed user object to that DS entry.

    You can activate the account over the REST interface or by using the admin UI, as described previously.

    This command activates Joe Smith's account over REST:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --header "Content-Type: application/json" \
    --request PATCH \
    --data '[
      { "operation" : "replace",
        "field" : "accountStatus",
        "value" : "active" }
    ]' \
    "http://localhost:8080/openidm/managed/user/24356bf0-f026-4dc1-9f68-2a571b0a236f"
    {
      "_id": "24356bf0-f026-4dc1-9f68-2a571b0a236f",
      "_rev": "00000000c8d52133",
      "userName": "joe.smith",
      "givenName": "Joe",
      "sn": "Smith",
      "displayName": "Joe Smith",
      "mail": "joe.smith@example.com",
      "accountStatus": "active",
      "effectiveRoles": [],
      "effectiveAssignments": []
    }
    ```

14. Verify that a new LDAP entry for user Joe Smith was created in DS.

    This command returns all IDs in DS and shows that two entries now exist for Joe Smith: `uid=joe.smith0` and `uid=joe.smith1`:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/system/ldap/account?_queryFilter=true&_fields=_id,dn"
    {
      "result": [
        {
          "_id": "0da50512-79bb-3461-bd04-241ee4c785bf",
          "dn": "uid=jdoe,ou=People,dc=example,dc=com"
        },
        {
          "_id": "887732e8-3db2-31bb-b329-20cd6fcecc05",
          "dn": "uid=bjensen,ou=People,dc=example,dc=com"
        },
        {
          "_id": "da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
          "dn": "uid=joe.smith0,ou=People,dc=example,dc=com"
        },
        {
          "_id": "52821eec-e00d-4321-8857-f46a870afc45",
          "dn": "uid=joe.smith1,ou=People,dc=example,dc=com"
        }
      ],
      ...
    }
    ```

15. Request Joe Smith's historical accounts:

    ```
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/managed/user/24356bf0-f026-4dc1-9f68-2a571b0a236f/historicalAccounts?_queryFilter=true"
    {
      "result": [
        {
          "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
          "_rev": "0000000037beefe7",
          "_ref": "system/ldap/account/da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
          "_refResourceCollection": "system/ldap/account",
          "_refResourceId": "da7c8fe9-4959-4dc9-9cd5-60c0ead9b0aa",
          "_refProperties": {
            "active": false,
            "stateLastChanged": "Mon May 18 2020 13:51:06 GMT+0200 (SAST)",
            "state": "disabled",
            "linkDate": "Mon May 18 2020 13:47:18 GMT+0200 (SAST)",
            "unlinkDate": "Mon May 18 2020 13:52:33 GMT+0200 (SAST)",
            "_id": "3f193422-156b-4b66-adcf-447db1b7d770",
            "_rev": "0000000037beefe7"
          }
        },
        {
          "_id": "8850640c-2233-4ddc-9725-6b4b2d59605f",
          "_rev": "000000000843ce68",
          "_ref": "system/ldap/account/52821eec-e00d-4321-8857-f46a870afc45",
          "_refResourceCollection": "system/ldap/account",
          "_refResourceId": "52821eec-e00d-4321-8857-f46a870afc45",
          "_refProperties": {
            "active": true,
            "stateLastChanged": "Mon May 18 2020 13:54:52 GMT+0200 (SAST)",
            "state": "enabled",
            "linkDate": "Mon May 18 2020 13:54:52 GMT+0200 (SAST)",
            "_id": "8850640c-2233-4ddc-9725-6b4b2d59605f",
            "_rev": "000000000843ce68"
          }
        }
      ],
      ...
    }
    ```

    Joe Smith's entry now shows two DS accounts, but only the link to `uid=joe.smith1` (`"_ref": "system/ldap/account/52821eec-e00d-4321-8857-f46a870afc45",`) is `enabled` and `active`.

---

---
title: Link Multiple Accounts to a Single Identity
description: Link multiple LDAP accounts to a single PingIDM managed user identity using link qualifiers and role-based assignments
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:multi-account-linking
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/multi-account-linking.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Link", "Multiple Accounts"]
section_ids:
  multiaccount-background: Sample Overview
  prepare-multiaccount-sample: Prepare the Sample
  install-sample-multiaccount: Run the Sample
  create_the_users_roles_and_assignments: Create the Users, Roles, and Assignments
  multiaccountlinking-recon: Reconcile Managed Users to the LDAP Server
---

# Link Multiple Accounts to a Single Identity

This sample illustrates how IDM handles links from multiple accounts to a single identity.

The sample is based on a common use case in the insurance industry, where a company (Example.com) employs agents to sell policies to their insured customers. Most of their agents are also insured, which means that they have two distinct *roles* within the company - customers, and agents. With minor changes, this sample works for other use cases. For example, a hospital employs doctors who treat patients, and some of those same doctors are also patients of the hospital.

## Sample Overview

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

You define mappings between source and target accounts in your project's `sync.json` file. As part of a mapping, you can create a link between a single source account and multiple target accounts using a *link qualifier*, that enables one-to-many relationships in mappings and policies. For more information about mappings and link qualifiers, refer to [Resource mapping](../synchronization-guide/mappings.html) and [Map a Single Source Object to Multiple Target Objects](../synchronization-guide/linking-multiple-targets.html).

This sample uses two link qualifiers:

* `Insured` represents the accounts associated with Example.com's Insured customers, created under the LDAP container `ou=Customers,dc=example,dc=com`.

* `Agent` represents agent accounts, considered independent contractors, and created under the LDAP container `ou=Contractors,dc=example,dc=com`.

Assume that agents and insured customers connect using two different portals, and that each group has access to different features, depending on the portal.

Agents might have two separate accounts; one each for professional and personal use. Although the accounts are different, the identity information for each agent should be the same for both accounts.

This sample therefore uses link qualifiers to distinguish the two *categories* of users. The link qualifiers are named `insured` and `agent`, and are defined as part of the `managedUser_systemLdapAccounts` mapping in the `sync.json` file:

```json
{
  "name" : "managedUser_systemLdapAccounts",
  "source" : "managed/user",
  "target" : "system/ldap/account",
  "linkQualifiers" : [
    "insured",
    "agent"
  ],
  ...
}
```

You can check this configuration in the admin UI. Click Configure > Mappings > `managedUser_systemLdapAccounts` > Properties > Link Qualifiers. You should see `insured` and `agent` in the list of configured link qualifiers.

In addition, the sample uses a transformation script that determines the LDAP Distinguished Name (`dn`) from the user category. The following excerpt of the `sync.json` file shows that script:

```json
{
   "target" : "dn",
   "transform" : {
      "type" : "text/javascript",
      "globals" : { },
      "source" :
         "if (linkQualifier === 'agent') {
            'uid=' + source.userName + ',ou=Contractors,dc=example,dc=com';
         } else if (linkQualifier === 'insured') {
            'uid=' + source.userName + ',ou=Customers,dc=example,dc=com';
         }"
},
```

Finally, the following `validSource` script assesses the effective roles of a managed user to determine if that user has an `Agent` or `Insured` role. The script then assigns a link qualifier based on the assessed role.

```json
"validSource" : {
  "type" : "text/javascript",
  "globals" : { },
  "source" : "var res = false;
    var i=0;

    while (!res && i < source.effectiveRoles.length) {
      var roleId = source.effectiveRoles[i]._ref;
      if (roleId != null && roleId.indexOf("/") != -1) {
        var roleInfo = openidm.read(roleId);
        res = (((roleInfo.name === 'Agent') &&(linkQualifier ==='agent'))
        || ((roleInfo.name === 'Insured') &&(linkQualifier ==='insured')));
      }
      i++;
    }
    res"
}
```

## Prepare the Sample

1. [Set up DS](start-here.html#ldap-server-config) using `/path/to/openidm/samples/multi-account-linking/data/Example.ldif` .

2. [Prepare IDM](start-here.html#preparing-openidm), and start the server using the sample configuration:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/multi-account-linking
   ```

## Run the Sample

### Create the Users, Roles, and Assignments

1. Create the managed users for John Doe and Barbara Jensen.

   To set up these managed users using the admin UI, select Manage > User > New User; otherwise, using the REST interface:

   ```
   curl \
   --header "Content-Type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "displayName" : "Barbara Jensen",
     "description" : "Created for OpenIDM",
     "givenName" : "Barbara",
     "mail" : "bjensen@example.com",
     "telephoneNumber" : "1-360-229-7105",
     "sn" : "Jensen",
     "userName" : "bjensen",
     "accountStatus" : "active"
   }' \
   "http://localhost:8080/openidm/managed/user?_action=create"
   {
     "_id": "580f1441-ff8e-434b-9605-90e10a6fbdf6",
     "_rev": "00000000792afa08",
     "displayName": "Barbara Jensen",
     "description": "Created for OpenIDM",
     "givenName": "Barbara",
     "mail": "bjensen@example.com",
     "telephoneNumber": "1-360-229-7105",
     "sn": "Jensen",
     "userName": "bjensen",
     "accountStatus": "active",
     "effectiveRoles": [],
     "effectiveAssignments": []
   }
   ```

   ```
   curl \
   --header "Content-Type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "displayName" : "John Doe",
     "description" : "Created for OpenIDM",
     "givenName" : "John",
     "mail" : "jdoe@example.com",
     "telephoneNumber" : "1-415-599-1100",
     "sn" : "Doe",
     "userName" : "jdoe",
     "accountStatus" : "active"
   }' \
   "http://localhost:8080/openidm/managed/user?_action=create"
   {
     "_id": "02632173-e413-4af1-8495-f749d5880226",
     "_rev": "000000001298f6a6",
     "displayName": "John Doe",
     "description": "Created for OpenIDM",
     "givenName": "John",
     "mail": "jdoe@example.com",
     "telephoneNumber": "1-415-599-1100",
     "sn": "Doe",
     "userName": "jdoe",
     "accountStatus": "active",
     "effectiveRoles": [],
     "effectiveAssignments": []
   }
   ```

   |   |                                                              |
   | - | ------------------------------------------------------------ |
   |   | Make sure to record the unique `_id` for both managed users. |

2. Set up the managed roles Agent and Insured, to distinguish between the two user types.

   To set up these roles using the admin UI, select Manage > Role > New Role; otherwise, using the REST interface:

   ```
   curl \
   --header "Content-Type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "name" : "Agent",
     "description" : "Role assigned to insurance agents."
   }' \
   "http://localhost:8080/openidm/managed/role?_action=create"
   {
     "_id": "1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f",
     "_rev": "000000005b3d5ebd",
     "name": "Agent",
     "description": "Role assigned to insurance agents."
   }
   ```

   ```
   curl \
   --header "Content-Type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "name" : "Insured",
     "description" : "Role assigned to insured customers."
   }' \
   "http://localhost:8080/openidm/managed/role?_action=create"
   {
     "_id": "617368f2-fa4e-44a2-a25a-f0a86e16ef00",
     "_rev": "000000002b845f24",
     "name": "Insured",
     "description": "Role assigned to insured customers."
   }
   ```

   |   |                                                              |
   | - | ------------------------------------------------------------ |
   |   | Make sure to record the unique `_id` for both managed roles. |

3. Grant the managed roles to the users. In this sample, jdoe is an agent and customer, and bjensen is only a customer.

   To grant the roles, you need the `_id`s you recorded when you created the users and roles.

   1. The following command grants the Agent role to jdoe:

      ```
      curl \
      --header "Content-type: application/json" \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request PATCH \
      --data '[
        {
          "operation": "add",
          "field": "/roles/-",
          "value": {
            "_ref": "managed/role/1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f"
          }
        }
      ]' \
      "http://localhost:8080/openidm/managed/user/02632173-e413-4af1-8495-f749d5880226"
      {
        "_id": "02632173-e413-4af1-8495-f749d5880226",
        "_rev": "00000000dc6160c8",
        "displayName": "John Doe",
        "description": "Created for OpenIDM",
        "givenName": "John",
        "mail": "jdoe@example.com",
        "telephoneNumber": "1-415-599-1100",
        "sn": "Doe",
        "userName": "jdoe",
        "accountStatus": "active",
        "effectiveAssignments": [],
        "effectiveRoles": [
          {
          "_refResourceCollection": "managed/role",
          "_refResourceId": "1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f",
          "_ref": "managed/role/1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f"
          }
        ]
      }
      ```

   2. The following command grants the Insured role to user bjensen:

      ```
      curl \
      --header "Content-type: application/json" \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request PATCH \
      --data '[
        {
          "operation": "add",
          "field": "/roles/-",
          "value": {
            "_ref": "managed/role/617368f2-fa4e-44a2-a25a-f0a86e16ef00"
          }
        }
      ]' \
      "http://localhost:8080/openidm/managed/user/580f1441-ff8e-434b-9605-90e10a6fbdf6"
      {
        "_id": "580f1441-ff8e-434b-9605-90e10a6fbdf6",
        "_rev": "000000004cab60c8",
        "displayName": "Barbara Jensen",
        "description": "Created for OpenIDM",
        "givenName": "Barbara",
        "mail": "bjensen@example.com",
        "telephoneNumber": "1-360-229-7105",
        "sn": "Jensen",
        "userName": "bjensen",
        "accountStatus": "active",
        "effectiveAssignments": [],
        "effectiveRoles": [
          {
            "_refResourceCollection": "managed/role",
            "_refResourceId": "617368f2-fa4e-44a2-a25a-f0a86e16ef00",
            "_ref": "managed/role/617368f2-fa4e-44a2-a25a-f0a86e16ef00"
          }
        ]
      }
      ```

   3. The following command grants the Insured role to jdoe:

      ```
      curl \
      --header "Content-type: application/json" \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request PATCH \
      --data '[
        {
          "operation": "add",
          "field": "/roles/-",
          "value": {
            "_ref": "managed/role/617368f2-fa4e-44a2-a25a-f0a86e16ef00"
          }
        }
      ]' \
      "http://localhost:8080/openidm/managed/user/02632173-e413-4af1-8495-f749d5880226"
      {
        "_id": "02632173-e413-4af1-8495-f749d5880226",
        "_rev": "00000000a92657c7",
        "displayName": "John Doe",
        "description": "Created for OpenIDM",
        "givenName": "John",
        "mail": "jdoe@example.com",
        "telephoneNumber": "1-415-599-1100",
        "sn": "Doe",
        "userName": "jdoe",
        "accountStatus": "active",
        "effectiveAssignments": []
        "effectiveRoles": [
          {
            "_refResourceCollection": "managed/role",
            "_refResourceId": "1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f",
            "_ref": "managed/role/1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f"
          },
          {
            "_refResourceCollection": "managed/role",
            "_refResourceId": "617368f2-fa4e-44a2-a25a-f0a86e16ef00",
            "_ref": "managed/role/617368f2-fa4e-44a2-a25a-f0a86e16ef00"
          }
        ]
      }
      ```

      Notice jdoe now has two managed roles, as shown by the multiple `effectiveRoles`.

4. Create the managed assignments.

   *Assignments* specify what a role actually does on a target system. A single account frequently has different functions on a system. For example, while agents might be members of the Contractor group, insured customers might be part of a Chat Users group (possibly for access to customer service). The following commands create two managed assignments that will be attached to the agent and insured roles. Note the `_id` of each assignment because you will need these when you attach the assignment to its corresponding role.

   The following command creates an `ldapAgent` assignment. Users who have this assignment will have their `ldapGroups` property in DS set to `cn=Contractors,ou=Groups,dc=example,dc=com`. The assignment is associated with the `agent` link qualifier:

   ```
   curl \
   --header "Content-Type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "name": "ldapAgent",
     "description": "LDAP Agent Assignment",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "ldapGroups",
         "value": [
           "cn=Contractors,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ],
     "linkQualifiers": ["agent"]
   }' \
   "http://localhost:8080/openidm/managed/assignment?_action=create"
   {
     "_id": "cc0dbcdc-64a4-4f5b-aade-648fc012e2b5",
     "_rev": "00000000c7554e13",
     "name": "ldapAgent",
     "description": "LDAP Agent Assignment",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "ldapGroups",
         "value": [
           "cn=Contractors,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ],
     "linkQualifiers": [
       "agent"
     ]
   }
   ```

   The following command creates an `ldapCustomer` assignment. Users who have this assignment will have their `ldapGroups` property in DS set to `cn=Chat Users,ou=Groups,dc=example,dc=com`. The assignment is associated with the `insured` link qualifier:

   ```
   curl \
   --header "Content-Type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "name": "ldapCustomer",
     "description": "LDAP Customer Assignment",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "ldapGroups",
         "value": [
           "cn=Chat Users,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ],
     "linkQualifiers": ["insured"]
   }' \
   "http://localhost:8080/openidm/managed/assignment?_action=create"
   {
     "_id": "56b1f300-7156-4110-9b23-2052c16dd2aa",
     "_rev": "000000000cde398e",
     "name": "ldapCustomer",
     "description": "LDAP Customer Assignment",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "ldapGroups",
         "value": [
           "cn=Chat Users,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ],
     "linkQualifiers": [
       "insured"
     ]
   }
   ```

5. Add the assignments to their respective roles.

   1. Add the `ldapCustomer` assignment to the Insured customer role:

      ```
      curl \
      --header "Content-type: application/json" \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request PATCH \
      --data '[
        {
          "operation": "add",
          "field": "/assignments/-",
          "value": {
            "_ref": "managed/assignment/56b1f300-7156-4110-9b23-2052c16dd2aa"
          }
        }
      ]' \
      "http://localhost:8080/openidm/managed/role/617368f2-fa4e-44a2-a25a-f0a86e16ef00"
      {
        "_id": "617368f2-fa4e-44a2-a25a-f0a86e16ef00",
        "_rev": "0000000050c62938",
        "name": "Insured",
        "description": "Role assigned to insured customers."
      }
      ```

   2. Add the `ldapAgent` assignment to the Agent role:

      ```
      curl \
      --header "Content-type: application/json" \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request PATCH \
      --data '[
        {
          "operation": "add",
          "field": "/assignments/-",
          "value" : {
            "_ref": "managed/assignment/cc0dbcdc-64a4-4f5b-aade-648fc012e2b5"
          }
        }
      ]' \
      "http://localhost:8080/openidm/managed/role/1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f"
      {
        "_id": "1b58ec8d-fae2-4b28-a5cf-b63567e4cf3f",
        "_rev": "0000000013e50a6b",
        "name": "Agent",
        "description": "Role assigned to insurance agents."
      }
      ```

### Reconcile Managed Users to the LDAP Server

1. With the managed roles and assignments set up, reconcile the managed user repository with the DS data store:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/recon?_action=recon&mapping=managedUser_systemLdapAccounts"
   {
     "_id": "a6b46fc6-0731-47d8-83b5-89cca8963512-11550",
     "state": "ACTIVE"
   }
   ```

   This reconciliation creates three new accounts in DS:

   * Two accounts under `ou=Customers,dc=example,dc=com` (one for each user who has the insured customers role), `bjensen` and `jdoe`.

   * One account under `ou=Contractors,dc=example,dc=com` (for the use who has the agents role), `jdoe`.

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | Both users already exist in DS, from the `Example.ldif` file that you imported during the setup. |

2. Query the list of users in DS to see the multiple accounts created for jdoe and bjensen as a result of the reconciliation:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/ldap/account?_queryId=query-all-ids"
   {
     "result": [
       {
         "_id": "3bbf1f43-e120-4d34-a4c9-05bd02be23bd"
       },
       {
         "_id": "d6c73ea1-fd05-4b80-8625-c50303755c91"
       },
       {
         "_id" : "0acc77a5-0f38-473b-b533-e37ca1d4fd4c"
       },
       {
         "_id" : "3310b29a-0d7f-4ed5-aa0d-795d2780e002"
       },
       {
         "_id" : "3c8e3c3d-f748-44c1-8cfc-172f5b0a9b5e"
       }
     ],
     ...
   }
   ```

---

---
title: LiveSync with an LDAP server
description: Configure PingIDM liveSync to push changes from Active Directory or a simulated AD instance to a PingDS LDAP directory
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:livesync-with-ad
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/livesync-with-ad.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "LiveSync", "Active Directory"]
section_ids:
  livesync-with-ad-setting-up-ldap: Set up the LDAP resources
  running-livesync-with-ad: Run the sample
  run-reconciliation: Reconcile the two LDAP data stores
  configuring-livesync: Configure liveSync
  test-live-sync: Test liveSync
---

# LiveSync with an LDAP server

This sample resembles the sample described in [Synchronize data between two external resources](sync-two-external-resources.html). However, this sample demonstrates *liveSync* from one external LDAP resource to another. LiveSync is the mechanism by which changes are pushed from an external resource to IDM and then, optionally, to another external resource. For more information, refer to [Synchronization types](../synchronization-guide/sync-types.html).

The sample assumes a scenario where changes in an Active Directory server are synchronized, using LiveSync, with a PingDS (DS) server.

The sample provides a configuration for two scenarios, depending on whether you are using a live Active Directory (AD) service, or whether you are simulating the AD service with a DS server. Each scenario is associated with a file in the `livesync-with-ad/alternatives` directory. Depending on your scenario, copy the corresponding file to the `livesync-with-ad/conf` directory:

* Live AD Instance

  If you have an AD instance to test with, use that AD instance as the first LDAP resource. For the second LDAP resource, configure DS as described in [Set Up the LDAP Resources](#livesync-with-ad-setting-up-ldap). The data for the DS instance is contained in the file `samples/livesync-with-ad/data/Example.ldif`.

  For the connection to Active Directory, copy the `provisioner.openicf-realad.json` file from `livesync-with-ad/alternatives` to the `conf/` directory and rename it `provisioner.openicf-ad.json`.

  Because this sample demonstrates synchronization *from* the AD server *to* DS, data on the AD server is not changed.

* Simulated AD Instance

  If you are simulating the AD instance with a DS server, copy the `provisioner.openicf-fakead.json` file from `livesync-with-ad/alternatives` to the `conf/` directory and rename it `provisioner.openicf-ad.json`.

  This sample simulates an AD server on the same instance of DS, using a different base DN (`dc=fakead,dc=com`). You can also simulate the AD server with a separate DS instance, running on the same host, as long as the two instances communicate on different ports. The data for the simulated AD instance is contained in the file `samples/livesync-with-ad/data/AD.ldif`. The data for the DS instance is contained in the file `samples/livesync-with-ad/data/Example.ldif`.

## Set up the LDAP resources

Whether you use a simulated Active Directory server, or a live Active Directory server, you must still set up a DS instance as the second LDAP resource.

[Set up DS](start-here.html#ldap-server-config) using `/path/to/openidm/samples/livesync-with-ad/data/Example.ldif` , and do one of the following:

> **Collapse: Configure the Connection to a Live AD Instance**
>
> To configure the connection to a live AD instance, open the connector configuration file (`provisioner.openicf-ad.json`) in a text editor. Update the file as required to reflect your AD instance. At a minimum, check and update the following parameters:
>
> * `host`
>
>   The hostname or IP address of the AD server.
>
> * `port`
>
>   The LDAP port; 389 by default.
>
> * `ssl`
>
>   Whether the connection to the AD instance is secured over SSL; false by default.
>
> * `principal`
>
>   The full DN of the account that is used to bind to the server, for example, "CN=Administrator,CN=Users,DC=example,DC=com".
>
> * `credentials`
>
>   If a password is used, replace null with that password. When IDM starts, it encrypts that password in the `provisioner.openicf-ad.conf` file.
>
> * `baseContexts`
>
>   A list of DNs for account containers, for example, "CN=Users,DC=Example,DC=com".
>
> * `baseContextsToSynchronize`
>
>   Set to the same value as `baseContexts`.
>
> * `accountSearchFilter`
>
>   The LDAP search filter to locate accounts; only user accounts by default.
>
> * `accountSynchronizationFilter`
>
>   The LDAP search filter to synchronize user accounts; only user accounts by default.
>
> If you do not want to filter out computer and disabled user accounts, set the `accountSearchFilter` and `accountSynchronizationFilter` to `null`.

> **Collapse: Configure the Connection to a Simulated AD Instance**
>
> If you do not have a testable instance of AD available, you can simulate an AD instance in a separate suffix on the existing DS instance. The `data/AD.ldif` file includes LDIF data for a simulated AD instance.
>
> 1. If you have not already done so, copy the `samples/livesync-with-ad/alternatives/provisioner.openicf-fakead.json` to the `conf` subdirectory and rename it `provisioner.openicf-ad.json`.
>
>    This file sets up the connection to the DS server, targeting the suffix (`dc=fakead,dc=com`) that is simulating an AD server.
>
> 2. Load the simulated data into that suffix:
>
>    ```
>    /path/to/opendj/bin/ldapmodify \
>    --port 1636 \
>    --useSSL \
>    --usePkcs12TrustStore /path/to/opendj/config/keystore \
>    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
>    --hostname localhost \
>    --bindDN uid=admin \
>    --bindPassword password \
>    --filename /path/to/openidm/samples/livesync-with-ad/data/AD.ldif
>    # ADD operation successful for DN dc=fakead,dc=com
>
>    # ADD operation successful for DN ou=People,dc=fakead,dc=com
>
>    # ADD operation successful for DN uid=bobf,ou=People,dc=fakead,dc=com
>
>    # ADD operation successful for DN uid=stony,ou=People,dc=fakead,dc=com
>    ```

## Run the sample

When both DS and a real or simulated AD server are configured, prepare IDM as described in [Prepare IDM](start-here.html#preparing-openidm). Then start IDM with the configuration for this sample:

```
cd /path/to/openidm/
./startup.sh -p samples/livesync-with-ad
```

The following sections show how to synchronize the two external LDAP data stores by running a reconciliation operation, how to configure scheduled liveSync.

### Reconcile the two LDAP data stores

Review the entries in the DS server (imported from the `Example.ldif` file). When you run reconciliation, any entries that share the same `uid` with the AD data store will be updated with the contents from AD.

If you have set up the simulated AD data store as described in [Simulated AD Instance](#setting-up-simulated-ad), compare the entries in the `AD.ldif` and `Example.ldif` files. Note that each file has two different users—after importing the data, the AD instance has users bobf and stony, and the DS instance has users jdoe and bjensen.

1. Run reconciliation over the REST interface:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/recon?_action=recon&mapping=systemAdAccounts_managedUser&waitForCompletion=true"
   ```

   The reconciliation operation returns a reconciliation run ID, and the status of the operation.

   ```json
   {
     "state": "SUCCESS",
     "_id": "985ee939-fbe1-4607-a757-00b404b4ef77"
   }
   ```

   The reconciliation operation synchronizes the data in the AD server with the IDM repository (managed/user). *Implicit synchronization* then pushes those changes out to the DS server. For more information about implicit synchronization, refer to [Synchronization types](../synchronization-guide/sync-types.html).

2. List all the users in the DS server:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/ldap/account?_queryFilter=true&_fields=_id,dn"
   ```

   Your DS server should now contain four users:

   ```json
   {
     "result": [
       {
         "_id": "0da50512-79bb-3461-bd04-241ee4c785bf",
         "dn": "uid=jdoe,ou=People,dc=example,dc=com"
       },
       {
         "_id": "887732e8-3db2-31bb-b329-20cd6fcecc05",
         "dn": "uid=bjensen,ou=People,dc=example,dc=com"
       },
       {
         "_id": "fc4feff0-11ae-430f-858d-338b1b05d66a",
         "dn": "uid=bobf,ou=People,dc=example,dc=com"
       },
       {
         "_id": "ba07d4f4-0e2b-4c53-aecb-4b234e1fec1c",
         "dn": "uid=stony,ou=People,dc=example,dc=com"
       }
     ],
     ...
   }
   ```

   The two users from the AD server have been added to the DS server.

### Configure liveSync

LiveSync pushes changes made in an external system to the IDM repository. You can launch a liveSync operation over REST, or configure a schedule to poll for changes. This sample includes a liveSync schedule (`conf/schedule-activeSynchroniser_systemAdAccount.json`) that is disabled by default. When the schedule is enabled, a liveSync operation is launched every 15 seconds.

To activate liveSync, change the value of the `enabled` property in the schedule configuration from `false` to `true`:

```json
{
    "enabled" : true,
    "type" : "simple",
    "repeatInterval" : 15000,
    "persisted" : true,
    "concurrentExecution" : false,
    "invokeService" : "provisioner",
    "invokeContext" : {
        "action" : "liveSync",
        "source" : "system/ad/account"
    },
    "invokeLogLevel" : "debug"
}
```

### Test liveSync

Test liveSync as follows:

1. Create an LDIF file with a new user entry (`uid=bsmith`) that will be added to the AD directory.

   You can use the following LDIF file (`bsmith.ldif`) as an example. This sample file assumes the simulated AD instance. Adjust the DN if you are using a live AD instance:

   ```ldif
   dn: uid=bsmith,ou=People,dc=fakead,dc=com
   objectClass: person
   objectClass: inetOrgPerson
   objectClass: organizationalPerson
   objectClass: top
   givenName: Barry
   description: Created to see liveSync work
   uid: bsmith
   cn: Barry
   sn: Smith
   mail: bsmith@example.com
   telephoneNumber: 1-415-523-0772
   userPassword: 5up35tr0ng
   ```

2. Use the `ldapmodify` command to add the new user to the AD directory:

   ```
   /path/to/opendj/bin/ldapmodify \
   --port 1636 \
   --useSSL \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDN uid=admin \
   --bindPassword password \
   --filename /path/to/bsmith.ldif
   # ADD operation successful for DN uid=bsmith,ou=People,dc=fakead,dc=com
   ```

3. Within 15 seconds, liveSync should create the user in the IDM repository.

   Test that the liveSync has worked by viewing the new user in IDM.

   One way to do this is by signing on to the [end-user UI](../setup-guide/idm-enduser-ui.html) as user `bsmith`, with password `5up35tr0ng`. If you can sign on as this new user, liveSync has synchronized the user from the AD directory to the managed/user repository.

4. Implicit synchronization pushes this change out to the DS server. To test this synchronization operation, search the DS baseDN for the new user entry.

   ```
   /path/to/opendj/bin/ldapsearch \
   --port 1636 \
   --useSSL \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --bindDN uid=admin \
   --bindPassword password \
   --baseDN ou=people,dc=example,dc=com \
   "(uid=bsmith)"
   ```

---

---
title: One-way synchronization from LDAP to IDM
description: Configure one-way reconciliation from a PingDS LDAP directory to the PingIDM managed user repository
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:sync-with-ldap
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/sync-with-ldap.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Synchronization", "LDAP", "One-Way"]
section_ids:
  prepare-sync-with-ldap: Prepare the sample
  run-sync-with-ldap: Run the sample
---

# One-way synchronization from LDAP to IDM

This sample demonstrates one-way synchronization from an LDAP directory to an IDM repository and shows how IDM detects new or changed objects from an external resource.

The sample has been tested with PingDS (DS) but should work with any LDAPv3-compliant server. The configuration includes one mapping, from the LDAP resource to the IDM repository. The sample does not push any changes made to IDM managed user objects out to the LDAP server.

The mapping configuration file (`conf/sync.json`) for this sample includes one mapping, `systemLdapAccounts_managedUser`, which synchronize users from the source LDAP server with the target IDM repository.

## Prepare the sample

1. [Set up DS](start-here.html#ldap-server-config) using `/path/to/openidm/samples/sync-with-ldap/data/Example.ldif`.

2. [Prepare IDM](start-here.html#preparing-openidm), and start the server using the sample configuration:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/sync-with-ldap
   ```

## Run the sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

You can work through the sample using the command line or admin UI:

> **Collapse: Use the command line**
>
> 1. Reconcile the repository:
>
>    ```
>    curl \
>    --header "X-OpenIDM-Username: openidm-admin" \
>    --header "X-OpenIDM-Password: openidm-admin" \
>    --header "Accept-API-Version: resource=1.0" \
>    --request POST \
>    "http://localhost:8080/openidm/recon?_action=recon&mapping=systemLdapAccounts_managedUser&waitForCompletion=true"
>    {
>      "_id": "b1394d10-29b0-4ccf-81d8-c88948ea121c-4",
>      "state": "SUCCESS"
>    }
>    ```
>
>    The reconciliation operation creates the two users from the LDAP server in the IDM repository and assigns the new objects random unique IDs.
>
> 2. Retrieve the users from the repository:
>
>    ```
>    curl \
>    --header "X-OpenIDM-Username: openidm-admin" \
>    --header "X-OpenIDM-Password: openidm-admin" \
>    --header "Accept-API-Version: resource=1.0" \
>    --request GET \
>    "http://localhost:8080/openidm/managed/user?_queryFilter=true&_fields=id,userName"
>    {
>      "result": [
>        {
>          "_id": "0326cbff-8f6e-4531-97dd-7b1a4c04b23a",
>          "_rev": "00000000657c9a27",
>          "userName": "bjensen"
>        },
>        {
>          "_id": "9afbf2bc-0323-4cbe-89b3-92f2f47742c3",
>          "_rev": "0000000015ae92f5",
>          "userName": "jdoe"
>        }
>      ],
>      ...
>    }
>    ```
>
> 3. To retrieve an individual user object, include their ID in the URL. For example:
>
>    ```
>    curl \
>    --header "X-OpenIDM-Username: openidm-admin" \
>    --header "X-OpenIDM-Password: openidm-admin" \
>    --header "Accept-API-Version: resource=1.0" \
>    --request GET \
>    "http://localhost:8080/openidm/managed/user/0326cbff-8f6e-4531-97dd-7b1a4c04b23a"
>    {
>      "_id": "0326cbff-8f6e-4531-97dd-7b1a4c04b23a",
>      "_rev": "00000000657c9a27",
>      "displayName": "Barbara Jensen",
>      "description": "Created for OpenIDM",
>      "givenName": "Barbara",
>      "mail": "bjensen@example.com",
>      "sn": "Jensen",
>      "telephoneNumber": "1-360-229-7105",
>      "userName": "bjensen",
>      "accountStatus": "active",
>      "effectiveAssignments": [],
>      "effectiveRoles": []
>    }
>    ```

> **Collapse: Use the admin UI**
>
> 1. Log in to the admin UI at `http://localhost:8080/admin` as the default administrative user: `openidm-admin` with password `openidm-admin`.
>
> 2. Select Configure > Mappings .
>
>    The Mappings page displays one mapping, from the `ldap` server to the IDM repository (`managed/user`).
>
> 3. Select the mapping, and click Reconcile .
>
>    The reconciliation operation creates the two users from the LDAP server in the IDM repository.
>
> 4. To verify the new users exist in the repository:
>
>    1. From the navigation bar, click Manage > User .
>
>       IDM displays the two users.
>
>    2. To view the details for a user account, from the User List page, click any username row.
>
>       The User details page displays.

---

---
title: Provision users with roles
description: "Use PingIDM roles and assignments to provision LDAP attributes and group membership based on a managed user's role"
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:provisioning-with-roles
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/provisioning-with-roles.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Provisioning", "Roles"]
section_ids:
  overview-provisioning-with-roles: Sample overview
  install-sample-roles-prov: Prepare the sample
  run-sample-roles-prov: Run the sample
  provrole-add-assignments: Add assignments to a role definition
  provrole-effective-assignments: Grant a role to a user and observe that user's role assignments
  provrole-propagate-assignments: Propagate assignments to an external system
  provrole-remove-role: Remove a role grant from a user and observe that user's role assignments
---

# Provision users with roles

This sample demonstrates how attributes are provisioned to an external system (an LDAP directory), based on role membership. This sample uses PingDS (DS) as the LDAP directory, but you can use any LDAP v3-compliant server.

## Sample overview

IDM supports two types of roles:

* *Provisioning roles* specify how objects are provisioned to an external system.

* *Authorization roles* specify the authorization rights of a managed object internally, within IDM.

Both provisioning roles and authorization roles use [relationships](../objects-guide/relationships.html) to link the role object, and the managed object to which the role applies. For information about managing roles, refer to [Managed Roles](../objects-guide/roles.html#managed-roles).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

The main purpose of IDM roles is to provision a set of attributes, based on a managed user's role membership.

The sample assumes a company, example.com. As an *Employee* of example.com, a user should be added to two groups in DS - the Employees group and the Chat Users group (presumably to access certain internal applications). As a *Contractor*, a user should be added only to the Contractors group in DS. A user's employee type must also be set correctly in DS, based on the role that is granted to the user.

## Prepare the sample

This section sets up the scenario by performing the following tasks:

1. Start IDM with the configuration for this sample.

2. Create two managed roles, Employee and Contractor.

3. Reconcile the managed user repository with the user entries in the LDAP server.

1) Configure the LDAP server as shown in [LDAP Server Configuration](start-here.html#ldap-server-config). The LDAP user must have write access to create users from IDM on the LDAP server. When you set up the LDAP server, import the LDIF file for this sample (`openidm/samples/provisioning-with-roles/data/Example.ldif)`.

2) [Set up DS](start-here.html#ldap-server-config) without importing any LDIF file or [select another repository](../install-guide/chap-repository.html) for the sample.

3) [Prepare IDM](start-here.html#preparing-openidm), and start the server using the sample configuration:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/provisioning-with-roles
   ```

4) Create two managed roles, Employee and Contractor, either by using the admin UI, or by running the following commands:

   ```
   curl \
   --header "Content-type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "name" : "Employee",
     "description": "Role granted to workers on the payroll."
   }' \
   "http://localhost:8080/openidm/managed/role?_action=create"
   {
     "_id": "d4f6b571-7e71-4901-8033-090a15098867",
     "_rev": "00000000ba0f5c8d",
     "name": "Employee",
     "description": "Role granted to workers on the payroll."
   }
   ```

   ```
   curl \
   --header "Content-type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "name": "Contractor",
     "description": "Role granted to contract workers."
   }' \
   "http://localhost:8080/openidm/managed/role?_action=create"
   {
     "_id": "95899c38-e483-4d89-8aec-a88baab0603a",
     "_rev": "00000000c7cb5c0f",
     "name": "Contractor",
     "description": "Role granted to contract workers."
   }
   ```

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | Make sure to record these two role IDs, as they are required to complete the sample. |

5) Reconcile the repository.

   The `sync.json` configuration file for this sample includes two mappings:

   * `systemLdapAccounts_managedUser`, which synchronizes users from the source LDAP server with the target IDM repository.

   * `managedUser_systemLdapAccounts`, which synchronizes changes from the repository with the LDAP server.

   Run a reconciliation operation for the first mapping, either by using the admin UI, or over the REST interface:

   * To use the admin UI, select Configure > Mapping, click on the first mapping (System/Ldap/Account → Managed User), and click Reconcile.

   * To use the REST interface, run the following command:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request POST \
     "http://localhost:8080/openidm/recon?_action=recon&mapping=systemLdapAccounts_managedUser&waitForCompletion=true"
     {
       "_id": "61abc9a3-a9cb-4d4b-b063-17891c3b355c-2541",
       "state": "SUCCESS"
     }
     ```

The sample is now ready to demonstrate provisioning roles.

## Run the sample

This section assumes that you have reconciled the managed user repository to populate it with the users from the LDAP server, and that you have created the Employee and Contractor roles.

This part of the sample demonstrates the following features of the roles implementation:

* [Add Assignments to a Role Definition](#provrole-add-assignments)

* [Grant a Role to a User and Observe that User's Role Assignments](#provrole-effective-assignments)

* [Propagate Assignments to an External System](#provrole-propagate-assignments)

* [Remove a Role Grant From a User and Observe That User's Role Assignments](#provrole-remove-role)

### Add assignments to a role definition

An [assignment](../objects-guide/roles.html#working-with-role-assignments) is the logic that provisions a managed user to an external system, based on some criteria. The most common use case of an assignment is the provisioning of specific attributes to an external system, based on the role or roles that the managed user has been granted. Assignments are sometimes called *entitlements*.

In this section, you will create an assignment and add it to the Employee role that you created previously. This section assumes the following scenario:

example.com's policy requires that every employee has the correct value for their `employeeType` in their corporate directory (DS).

1. Display the roles that you created in the previous section:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/role?_queryFilter=true"
   {
     "result": [
       {
         "_id": "d4f6b571-7e71-4901-8033-090a15098867",
         "_rev": "00000000ba0f5c8d",
         "name": "Employee",
         "description": "Role granted to workers on the payroll."
       },
       {
         "_id": "95899c38-e483-4d89-8aec-a88baab0603a",
         "_rev": "00000000c7cb5c0f",
         "name": "Contractor",
         "description": "Role granted to contract workers."
       }
     ],
     ...
   }
   ```

   |   |                                                               |
   | - | ------------------------------------------------------------- |
   |   | Display the roles in the admin UI by selecting Manage > Role. |

2. Create a new managed assignment named Employee.

   The assignment is specifically for the mapping from the managed user repository to the LDAP server. The assignment sets the value of the `employeeType` attribute on the LDAP server to `Employee`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-type: application/json" \
   --request POST \
   --data '{
      "name" : "Employee",
      "description": "Assignment for employees.",
      "mapping" : "managedUser_systemLdapAccounts",
      "attributes": [
        {
          "name": "employeeType",
          "value": [
            "Employee"
          ],
          "assignmentOperation" : "mergeWithTarget",
          "unassignmentOperation" : "removeFromTarget"
        }
      ]
    }' \
   "http://localhost:8080/openidm/managed/assignment?_action=create"
   {
     "_id": "1bbda95c-2a89-4e09-9719-8957849febeb",
     "_rev": "00000000ca15975d",
     "name": "Employee",
     "description": "Assignment for employees.",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "employeeType",
         "value": [
           "Employee"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ]
   }
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Create the assignment using the admin UI:1) From the navigation bar, click Manage > Assignment.

   2) On the Assignment List page, click New Assignment.

   3) On the New Assignment page, do the following:

      1. Enter the Assignment Name.

      2. Enter the Description.

      3. From the Mapping drop-down list, select the mapping for which the assignment is applied (`managedUser_systemLdapAccounts`).

      4. Click Save.

   4) Select the Attributes tab, and click Add an Attribute.

   5) From the drop-down list, select employeeType.

   6) In the adjacent *attribute value* area, click item.

   7) From the item 1 drop-down list, select string, and enter the value `Employee`.

   8) Click Save. |

3. Add the assignment to the Employee role that you created previously.

   Assignments are implemented as *relationship objects*. This means that you add an assignment to a role by *referencing* the assignment in the role's `assignments` field:

   This command patches the Employee role to update its `assignments` field:

   ```
   curl \
   --header "Content-type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request PATCH \
   --data '[
      {
        "operation" : "add",
        "field" : "/assignments/-",
        "value" : { "_ref": "managed/assignment/1bbda95c-2a89-4e09-9719-8957849febeb"}
      }
    ]' \
   "http://localhost:8080/openidm/managed/role/d4f6b571-7e71-4901-8033-090a15098867"
   {
     "_id": "d4f6b571-7e71-4901-8033-090a15098867",
     "_rev": "00000000ba0f5c8d",
     "name": "Employee",
     "description": "Role granted to workers on the payroll."
   }
   ```

   |   |                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Add the assignment to the role in the admin UI:1) Select Manage > Role, and select the Employee role.

   2) On the Managed Assignments tab, click Add Managed Assignments.

   3) Select the Employee assignment and click Add. |

### Grant a role to a user and observe that user's role assignments

When a role is granted to a user (by updating the users `roles` property), any assignments that are referenced by the role are automatically referenced in the user's `assignments` property.

In this section, we will grant the Employee role we created previously to the user Barbara Jensen, who was created in the managed/user repository during the reconciliation from DS.

1. Before you can update Barbara Jensen's entry, determine the identifier of her entry by querying her username, `bjensen`, and requesting only her `_id` field:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/user?_queryFilter=/userName+eq+'bjensen'&_fields=_id"
   {
     "result": [
       {
         "_id": "57356103-a1d5-4aaa-bcc5-a640147704e0",
         "_rev": "000000006688d203"
       }
     ],
     ...
   }
   ```

   From the output, observe that bjensen's `_id` is `57356103-a1d5-4aaa-bcc5-a640147704e0`.

2. Update bjensen's entry by adding a reference to the ID of the Employee role as a value of her `roles` attribute. Make sure to use the unique ID from your command output.

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-type: application/json" \
   --request PATCH \
   --data '[
     {
       "operation": "add",
       "field": "/roles/-",
       "value": { "_ref": "managed/role/d4f6b571-7e71-4901-8033-090a15098867" }
     }
   ]' \
   "http://localhost:8080/openidm/managed/user/57356103-a1d5-4aaa-bcc5-a640147704e0"
   {
     "_id": "57356103-a1d5-4aaa-bcc5-a640147704e0",
     "_rev": "000000005498d7b5",
     "displayName": "Barbara Jensen",
     "description": "Created for OpenIDM",
     "givenName": "Barbara",
     "mail": "bjensen@example.com",
     "telephoneNumber": "1-360-229-7105",
     "sn": "Jensen",
     "userName": "bjensen",
     "accountStatus": "active",
     "effectiveAssignments": [
       {
         "_rev": "00000000ca15975d",
         "_id": "1bbda95c-2a89-4e09-9719-8957849febeb",
         "_refResourceCollection": "managed/assignment",
         "_refResourceId": "1bbda95c-2a89-4e09-9719-8957849febeb",
         "_ref": "managed/assignment/1bbda95c-2a89-4e09-9719-8957849febeb"
         "name": "Employee",
         "description": "Assignment for employees.",
         "mapping": "managedUser_systemLdapAccounts",
         "attributes": [
           {
             "name": "employeeType",
             "value": [
               "Employee"
             ],
             "assignmentOperation": "mergeWithTarget",
             "unassignmentOperation": "removeFromTarget"
           }
         ]
       }
     ],
     "effectiveRoles": [
       {
         "_refResourceCollection": "managed/role",
         "_refResourceId": "d4f6b571-7e71-4901-8033-090a15098867",
         "_ref": "managed/role/d4f6b571-7e71-4901-8033-090a15098867"
       }
     ]
   }
   ```

   |   |                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Assign the role to bjensen by using the admin UI:1) Select Manage > User, and click bjensen's entry.

   2) On the Provisioning Roles tab, click Add Provisioning Roles.

   3) Select the Employee role, and click Add. |

3. Take a closer look at bjensen's entry, specifically at her roles, effective roles and effective assignments:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/user?_queryFilter=/userName+eq+'bjensen'&_fields=_id,userName,roles,effectiveRoles,effectiveAssignments"
   {
     "result": [
       {
         "_id": "57356103-a1d5-4aaa-bcc5-a640147704e0",
         "_rev": "000000005498d7b5",
         "userName": "bjensen",
         "effectiveAssignments": [
           {
             "_rev": "00000000ca15975d",
             "_id": "1bbda95c-2a89-4e09-9719-8957849febeb",
             "name": "Employee",
             "description": "Assignment for employees.",
             "mapping": "managedUser_systemLdapAccounts",
             "attributes": [
               {
                 "name": "employeeType",
                 "value": [
                   "Employee"
                 ],
                 "assignmentOperation": "mergeWithTarget",
                 "unassignmentOperation": "removeFromTarget"
               }
             ],
             "_refResourceCollection": "managed/assignment",
             "_refResourceId": "1bbda95c-2a89-4e09-9719-8957849febeb",
             "_ref": "managed/assignment1bbda95c-2a89-4e09-9719-8957849febeb"
           }
         ],
         "effectiveRoles": [
           {
             "_refResourceCollection": "managed/role",
             "_refResourceId": "d4f6b571-7e71-4901-8033-090a15098867",
             "_ref": "managed/role/d4f6b571-7e71-4901-8033-090a15098867"
           }
         ],
         "roles": [
           {
             "_ref": "managed/role/d4f6b571-7e71-4901-8033-090a15098867",
             "_refResourceCollection": "managed/role",
             "_refResourceId": "d4f6b571-7e71-4901-8033-090a15098867",
             "_refProperties": {
               "_id": "75441276-4ede-4655-855c-e13ed4b47e8e",
               "_rev": "00000000ccc59e6c"
             }
           }
         ]
       }
     ],
     ...
   }
   ```

   bjensen now has the calculated property `effectiveAssignments`, which includes the set of assignments that pertains to any user with the Employee role. Currently, the assignment lists the `employeeType` attribute.

   In the next section, you will see how the assignment is used to set the value of the `employeeType` attribute in the LDAP server.

### Propagate assignments to an external system

This section provides a number of steps that show how effective assignments propagate to the external systems associated with their mappings.

1. Verify that bjensen's `employeeType` has been set correctly in DS.

   Because implicit synchronization is enabled by default, any changes made to a managed user object are pushed out to all the external systems for which mappings are configured.

   Because bjensen has an effective assignment that sets an attribute in her LDAP entry, you should immediately see the resulting change in her LDAP entry.

   To verify that her entry has changed, run an `ldapsearch` on her entry and check the value of her `employeeType` attribute:

   ```
   /path/to/opendj/bin/ldapsearch \
   --port 1636 \
   --useSSL \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --baseDN "dc=example,dc=com" \
   --bindDN uid=admin \
   --bindPassword password \
   --searchScope sub \
   "(uid=bjensen)" dn uid employeeType isMemberOf
   dn: uid=bjensen,ou=People,dc=example,dc=com
   employeeType: Employee
   uid: bjensen
   isMemberOf: cn=openidm2,ou=Groups,dc=example,dc=com
   ```

   bjensen's `employeeType` attribute is correctly set to `Employee`.

2. To observe how a managed user's roles can be used to provision group membership in an external directory, we add the groups that an Employee and a Contractor should have in the corporate directory (DS) as assignment attributes of the respective roles.

   First, look at the current `assignments` of the Employee role again:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/role/d4f6b571-7e71-4901-8033-090a15098867?_fields=assignments,name"
   {
     "_id": "d4f6b571-7e71-4901-8033-090a15098867",
     "_rev": "00000000ba0f5c8d",
     "name": "Employee",
     "assignments": [
       {
         "_ref": "managed/assignment/1bbda95c-2a89-4e09-9719-8957849febeb",
         "_refResourceCollection": "managed/assignment",
         "_refResourceId": "1bbda95c-2a89-4e09-9719-8957849febeb",
         "_refProperties": {
           "_id": "94cb5abd-5358-42d7-ab96-0e6808a157aa",
           "_rev": "00000000cf18a2b6"
         }
       }
     ]
   }
   ```

   To update the `groups` attribute in bjensen's LDAP entry, you do not need to create a *new* assignment. You simply need to add the attribute for LDAP groups to the Employee assignment (`1bbda95c-2a89-4e09-9719-8957849febeb`):

   ```
   curl \
   --header "Content-type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request PATCH \
   --data '[
     {
       "operation": "add",
       "field": "/attributes/-",
       "value": {
         "name": "ldapGroups",
         "value": [
           "cn=Employees,ou=Groups,dc=example,dc=com",
           "cn=Chat Users,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     }
   ]' \
   "http://localhost:8080/openidm/managed/assignment/1bbda95c-2a89-4e09-9719-8957849febeb"
   {
     "_id": "1bbda95c-2a89-4e09-9719-8957849febeb",
     "_rev": "000000007248f2bc",
     "name": "Employee",
     "description": "Assignment for employees.",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "employeeType",
         "value": [
           "Employee"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       },
       {
         "name": "ldapGroups",
         "value": [
           "cn=Employees,ou=Groups,dc=example,dc=com",
           "cn=Chat Users,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ]
   }
   ```

   So, the Employee assignment now sets two attributes on the LDAP system - the `employeeType` attribute, and the `ldapGroups` attribute.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To add more attributes to the Employee assignment in the admin UI:1) Select Manage > Assignment, and click the Employee assignment.

   2) On the Attributes tab, select Add an attribute, and select the ldapGroups attribute.

   3) Enter the following values, and click Save:

      ```
      cn=Employees,ou=Groups,dc=example,dc=com
      ```

      ```
      cn=Chat Users,ou=Groups,dc=example,dc=com
      ``` |

3. With the implicit synchronization between the managed user repository and DS, bjensen should now be a member of the `cn=Employees` and `cn=Chat Users` groups in LDAP.

   You can verify this with the following `ldapsearch` command. This command returns bjensen's group membership, in her `isMemberOf` attribute:

   ```
   /path/to/opendj/bin/ldapsearch \
   --port 1636 \
   --useSSL \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --baseDN "dc=example,dc=com" \
   --bindDN uid=admin \
   --bindPassword password \
   --searchScope sub \
   "(uid=bjensen)" dn uid employeeType isMemberOf
   dn: uid=bjensen,ou=People,dc=example,dc=com
   employeeType: Employee
   uid: bjensen
   isMemberOf: cn=Employees,ou=Groups,dc=example,dc=com
   isMemberOf: cn=openidm2,ou=Groups,dc=example,dc=com
   isMemberOf: cn=Chat Users,ou=Groups,dc=example,dc=com
   ```

   You can also check bjensen's group membership by querying her object in the LDAP system, using the REST interface:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/ldap/account?_queryFilter=/uid+sw+'bjensen'&_fields=dn,uid,employeeType,ldapGroups"
   {
     "result": [
       {
         "_id": "887732e8-3db2-31bb-b329-20cd6fcecc05",
         "dn": "uid=bjensen,ou=People,dc=example,dc=com",
         "uid": "bjensen",
         "employeeType": [
           "Employee"
         ],
         "ldapGroups": [
           "cn=Chat Users,ou=Groups,dc=example,dc=com",
           "cn=openidm2,ou=Groups,dc=example,dc=com",
           "cn=Employees,ou=Groups,dc=example,dc=com"
         ]
       }
     ],
     ...
   }
   ```

   In the original LDIF file, bjensen was already a member of the openidm2 group. You can ignore this group for the purposes of this sample.

   |   |                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the admin UI to view bjensen's LDAP groups as follows:1) Select Manage > User, and select bjensen.

   2) On the Linked Systems tab, scroll down to the ldapGroups item. |

4. Now, create a new assignment that will apply to Contract employees, and add that assignment to the Contractor role.

   Create the Contractor assignment with the following command. This assignment sets the value of the `employeeType` attribute to `Contractor`, and updates the user's `ldapGroups` attribute to include the `cn=Contractors` group:

   ```
   curl \
   --header "Content-type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   --data '{
     "name": "Contractor",
     "description": "Contractor assignment for contract workers.",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "ldapGroups",
         "value": [
           "cn=Contractors,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       },
       {
         "name": "employeeType",
         "value": [
           "Contractor"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ]
   }' \
   "http://localhost:8080/openidm/managed/assignment?_action=create"
   {
     "_id": "30323ed3-d885-4d09-94ca-c8f3b3408296",
     "_rev": "00000000db43da70",
     "name": "Contractor",
     "description": "Contractor assignment for contract workers.",
     "mapping": "managedUser_systemLdapAccounts",
     "attributes": [
       {
         "name": "ldapGroups",
         "value": [
           "cn=Contractors,ou=Groups,dc=example,dc=com"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       },
       {
         "name": "employeeType",
         "value": [
           "Contractor"
         ],
         "assignmentOperation": "mergeWithTarget",
         "unassignmentOperation": "removeFromTarget"
       }
     ]
   }
   ```

   Note the ID of the Contractor assignment (`30323ed3-d885-4d09-94ca-c8f3b3408296` in this example).

   |   |                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------ |
   |   | To create the assignment using the admin UI, refer to [Add Assignments to a Role Definition](#provrole-add-assignments). |

5. Add the Contractor assignment to the Contractor role:

   ```
   curl \
   --header "Content-type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request PATCH \
   --data '[
     {
       "operation": "add",
       "field": "/assignments/-",
       "value": {
         "_ref": "managed/assignment/30323ed3-d885-4d09-94ca-c8f3b3408296"
       }
     }
   ]' \
   "http://localhost:8080/openidm/managed/role/95899c38-e483-4d89-8aec-a88baab0603a"
   {
     "_id": "95899c38-e483-4d89-8aec-a88baab0603a",
     "_rev": "00000000c7cb5c0f",
     "name": "Contractor",
     "description": "Role granted to contract workers."
   }
   ```

   |   |                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Add the Contractor assignment to the Contractor role in the admin UI, as follows:1) Select Manage > Role, and select the Contractor role.

   2) On the Managed Assignments tab, click Add Managed Assignment.

   3) Select the Contractor assignment from the dropdown list, and click Add. |

6. Next, we need to grant the Contractor role to user jdoe. Before we can patch jdoe's entry, we need to know their system-generated ID. To obtain the ID, query jdoe's entry as follows:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/user?_queryFilter=/userName+eq+'jdoe'&_fields=_id"
   {
     "result": [
       {
         "_id": "0d8a1d10-62e0-43aa-9892-ec51258771d0",
         "_rev": "000000005daacae0"
       }
     ],
     ...
   }
   ```

   For this example, you can see that jdoe's `_id` is `0d8a1d10-62e0-43aa-9892-ec51258771d0`.

7. Update jdoe's entry by adding a reference to the ID of the Contractor role as a value of their `roles` attribute:

   ```
   curl \
   --header "Content-type: application/json" \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request PATCH \
   --data '[
     {
       "operation": "add",
       "field": "/roles/-",
       "value": {
         "_ref": "managed/role/95899c38-e483-4d89-8aec-a88baab0603a"
       }
     }
   ]' \
   "http://localhost:8080/openidm/managed/user/0d8a1d10-62e0-43aa-9892-ec51258771d0"
   {
     "_id": "0d8a1d10-62e0-43aa-9892-ec51258771d0",
     "_rev": "00000000aa64591e",
     "displayName": "John Doe",
     "description": "Created for OpenIDM",
     "givenName": "John",
     "mail": "jdoe@example.com",
     "telephoneNumber": "1-415-599-1100",
     "sn": "Doe",
     "userName": "jdoe",
     "accountStatus": "active",
     "effectiveAssignments": [
       {
         "_rev": "00000000db43da70",
         "_id": "30323ed3-d885-4d09-94ca-c8f3b3408296",
         "_refResourceCollection": "managed/assignment",
         "_refResourceId": "30323ed3-d885-4d09-94ca-c8f3b3408296",
         "_ref": "managed/assignment/30323ed3-d885-4d09-94ca-c8f3b3408296"
         "name": "Contractor",
         "description": "Contractor assignment for contract workers.",
         "mapping": "managedUser_systemLdapAccounts",
         "attributes": [
           {
             "name": "ldapGroups",
             "value": [
               "cn=Contractors,ou=Groups,dc=example,dc=com"
             ],
             "assignmentOperation": "mergeWithTarget",
             "unassignmentOperation": "removeFromTarget"
           },
           {
             "name": "employeeType",
             "value": [
               "Contractor"
             ],
             "assignmentOperation": "mergeWithTarget",
             "unassignmentOperation": "removeFromTarget"
           }
         ]
       }
     ],
     "effectiveRoles": [
       {
         "_refResourceCollection": "managed/role",
         "_refResourceId": "95899c38-e483-4d89-8aec-a88baab0603a",
         "_ref": "managed/role/95899c38-e483-4d89-8aec-a88baab0603a"
       }
     ]
   }
   ```

   |   |                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Grant the Contractor role to jdoe by using the admin UI, as follows:1) Select Manage > User, and click jdoe.

   2) On the Provisioning Roles tab, click Add Provisioning Roles.

   3) Select the Contractor role, and click Add. |

8. Check jdoe's entry on the LDAP system.

   With the implicit synchronization between the managed user repository and DS, jdoe should now be a member of the `cn=Contractors` group in LDAP. In addition, his `employeeType` should have been set to `Contractor`.

   You can verify this with the following REST query. This command returns jdoes's group membership, in his `isMemberOf` attribute, and his `employeeType`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/ldap/account?_queryFilter=/uid+sw+'jdoe'&_fields=dn,uid,employeeType,ldapGroups"
   {
     "result": [
       {
         "_id": "0da50512-79bb-3461-bd04-241ee4c785bf",
         "dn": "uid=jdoe,ou=People,dc=example,dc=com",
         "uid": "jdoe",
         "employeeType": [
           "Contractor"
         ],
         "ldapGroups": [
           "cn=openidm,ou=Groups,dc=example,dc=com",
           "cn=Contractors,ou=Groups,dc=example,dc=com"
         ]
       }
     ],
     ...
   }
   ```

   |   |                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the admin UI to view jdoe's LDAP groups as follows:1) Select Manage > User, and select jdoe.

   2) On the Linked Systems tab, scroll down to the ldapGroups item. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When working with large groups in LDAP services such as DS, you should use dynamic groups instead of static groups. The steps laid out above for setting assignments and roles work with the exception of how you add a user to a group: in dynamic groups, membership is determined by whether a user has an attribute the group is configured to search for.For example, if the Employees group was a dynamic group, membership might be set based on the `employeeType` attribute directly, by setting the `memberURL` in the group to `ldap:///ou=People,dc=example,dc=com??sub?(employeeType=Employee)`. You would then remove the `ldapGroups` attribute from the Employee assignment, since group membership is handled by `employeeType`.This membership won't be listed in the `ldapGroups` attribute in IDM (since it is no longer set there), but can be verified by querying DS directly:```
/path/to/opendj/bin/ldapsearch \
--port 1636 \
--useSSL \
--usePkcs12TrustStore /path/to/opendj/config/keystore \
--trustStorePassword:file /path/to/opendj/config/keystore.pin \
--hostname localhost \
--baseDN "dc=example,dc=com" \
--bindDN uid=admin \
--bindPassword password \
--searchScope sub \
"(uid=bjensen)" dn uid employeeType isMemberOf
dn: uid=bjensen,ou=People,dc=example,dc=com
employeeType: Employee
uid: bjensen
isMemberOf: cn=Employees,ou=Groups,dc=example,dc=com
isMemberOf: cn=openidm2,ou=Groups,dc=example,dc=com
isMemberOf: cn=Chat Users,ou=Groups,dc=example,dc=com
```For more information about dynamic groups in DS, refer to [Dynamic Groups](https://docs.pingidentity.com/pingds/8.1/config-guide/groups.html#dynamic-groups) in the *Configuration Guide* for PingDS. |

### Remove a role grant from a user and observe that user's role assignments

In this section, you will remove the Contractor role from jdoe's managed user entry and observe the subsequent change to jdoe's managed assignments, and to the corresponding attributes in DS.

1. Before you change jdoe's roles, view his entry again to examine his current roles:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/managed/user?_queryFilter=/userName+eq+'jdoe'&_fields=_id,roles"
   {
     "result": [
       {
         "_id": "0d8a1d10-62e0-43aa-9892-ec51258771d0",
         "_rev": "00000000aa64591e",
         "roles": [
           {
             "_ref": "managed/role/95899c38-e483-4d89-8aec-a88baab0603a",
             "_refResourceCollection": "managed/role",
             "_refResourceId": "95899c38-e483-4d89-8aec-a88baab0603a",
             "_refProperties": {
               "_id": "de68f5d9-baf9-49ca-8db5-96f0a382946d",
               "_rev": "00000000e299a021"
             }
           }
         ]
       }
     ],
     ...
   }
   ```

   Note the following IDs in this example output, you need them in the next step:

   * The ID of jdoe's user object is `0d8a1d10-62e0-43aa-9892-ec51258771d0`.

   * The ID of the contractor role (`_refResourceId`) is `95899c38-e483-4d89-8aec-a88baab0603a`.

   * The ID of the *relationship* that expresses the role grant is `de68f5d9-baf9-49ca-8db5-96f0a382946d`.

   |   |                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | View jdoe's current roles in the admin UI:1) Select Manage > User, and select jdoe.

   2) The Provisioning Roles tab lists the current roles. |

2. Remove the Contractor role from jdoe's entry by sending a DELETE request to his user entry, specifying the *relationship ID*:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request DELETE \
   "http://localhost:8080/openidm/managed/user/0d8a1d10-62e0-43aa-9892-ec51258771d0/roles/de68f5d9-baf9-49ca-8db5-96f0a382946d"
   {
     "_id": "de68f5d9-baf9-49ca-8db5-96f0a382946d",
     "_rev": "00000000e299a021",
     "_ref": "managed/role/95899c38-e483-4d89-8aec-a88baab0603a",
     "_refResourceCollection": "managed/role",
     "_refResourceId": "95899c38-e483-4d89-8aec-a88baab0603a",
     "_refProperties": {
       "_id": "de68f5d9-baf9-49ca-8db5-96f0a382946d",
       "_rev": "00000000e299a021"
     }
   }
   ```

   The output shows that the *relationship* between the user and the role was deleted.

   |   |                                                                                                                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Use the admin UI to remove the Contractor role from jdoe's entry as follows:1) Select Manage > User, and select jdoe.

   2) On the Provisioning Roles tab, check the box next to the Contractor role and click Remove Selected Provisioning Roles. |

3. Verify jdoe's `employeeType` and `ldapGroups`.

   The removal of the Contractor role causes a synchronization operation to be run on jdoe's entry. His `employeeType` and `ldapGroups` attributes in DS should be reset to what they were before he was granted the Contractor role.

   Check jdoe's attributes by querying his object in the LDAP directory, over the REST interface:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/ldap/account?_queryFilter=/uid+sw+'jdoe'&_fields=dn,uid,employeeType,ldapGroups"
   {
     "result": [
       {
         "_id": "0da50512-79bb-3461-bd04-241ee4c785bf",
         "dn": "uid=jdoe,ou=People,dc=example,dc=com",
         "uid": "jdoe",
         "employeeType": [],
         "ldapGroups": [
           "cn=openidm,ou=Groups,dc=example,dc=com"
         ]
       }
     ],
     ...
   }
   ```

   |   |                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Use the admin UI to view jdoe's LDAP groups as follows:1) Select Manage > User, and select jdoe's entry.

   2) On the Linked Systems tab, scroll down to the ldapGroups item. |

Learn more about [managed roles, assignments, and how to manipulate them](../objects-guide/managed-roles.html).

---

---
title: Provision users with workflow
description: Use a PingIDM workflow to onboard contractors through a manager-approval process and end-user UI registration
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:provisioning-with-workflow
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/provisioning-with-workflow.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Provisioning", "Workflows"]
section_ids:
  provisioning-sample-prepare: Prepare the sample
  provisioning-sample-running: Run the sample
---

# Provision users with workflow

This sample demonstrates a typical workflow use case, provisioning new users.

The sample uses the admin UI to set up the initial users and roles, then shows how users can complete their registration process in the end-user UI.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

The sample simulates the following scenario:

* An existing employee requests that an outside contractor be granted access to an organization's system.

* The *system* in this case, is the IDM managed user repository and a remote HR data source, represented by a CSV file (`hr.csv` ).

* User roles are stored separately, in a second CSV file (`roles.csv` ).

The sample has three mappings—two for the bidirectional synchronization of the managed user repository and the HR data store, and one for the synchronization of the roles data to the managed repository.

## Prepare the sample

In this section, you start IDM and reconcile user and role data. The reconciliation operations create two managed users, `user1` and `manager1`, and two managed roles, `employee` (assigned to `user1`) and `manager` (assigned to `manager1`).

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Workflows are not supported with a DS repository. Before you test this sample, [install a JDBC repository](../install-guide/chap-repository.html). |

1. Edit the `/path/to/openidm/samples/provisioning-with-workflow/conf/datasource.jdbc-default.json` file with the details of your JDBC repository. For more information, refer to [Select a repository](../install-guide/chap-repository.html).

2. Start IDM with the configuration for the provisioning sample:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/provisioning-with-workflow
   ```

3. Sign on to the admin UI.

4. Reconcile the role and user data:

   1. From the navigation bar, click Configure > Mappings.

   2. Select the first mapping (systemRolesFileRole\_internalRole), and click Reconcile.

   3. To verify the reconciliation:

      1. From the navigation bar, click Manage > Role.

      2. On the Roles page, click the Internal tab.

         IDM displays the two roles created in the previous step:

         * `employee`

         * `manager`

   4. From the navigation bar, click Configure > Mappings.

   5. Select the second mapping (systemCsvfileAccounts\_managedUser), and click Reconcile.

      The reconciliation operation creates the top-level managers (users who do not have their own `manager` property) in the managed user repository. In this sample, there is only one top-level manager (`manager1`).

   6. Select the second mapping again (systemCsvfileAccounts\_managedUser), and click Reconcile.

      This reconciliation operation creates the employees of the managers that were created by the previous reconciliation. In this sample, there is only one employee (`employee1`).

   7. From the navigation bar, click Manage > User, and verify the users `manager1` and `user1` exist.

5. Verify the relationships between the new user and role objects:

   1. Click user1.

      The Manager field displays `manager1` for this user.

   2. Click the Authorization Roles tab.

      `user1` has two roles, `openidm-authorized` and `employee`.

   3. From the breadcrumb link at the top of the page, click User, and select `manager1`.

      The Manager field is empty for this user.

   4. Click the Authorization Roles tab.

      `manager1` has three roles: `manager`, `openidm-authorized`, and `openidm-tasks-manager`.

6. Verify the available workflows:

   1. From the navigation bar, click Manage > Processes.

   2. On the Workflow Processes page, select the Definitions tab.

   3. From the Definitions list, click Contractor onboarding process.

      IDM displays a diagram similar to the following:

      ![contractorOnboarding-diag](_images/contractorOnboarding-diag.png)

7. Sign off of the admin UI.

## Run the sample

During this part of the sample, an existing employee initiates a *Contractor Onboarding* process. This process is a request to add a contractor to the managed user repository, with an option to include the contractor in the original HR data source (`hr.csv`).

When the employee has completed the required form, the request is sent to the manager for approval. Any user with the role `manager` can claim the approval task. If a request was made to add the contractor to the original HR data source, this is done when the manager approves the request.

1. Sign on to the end-user UI (`https://localhost:8443/`) as the user you created in the previous section (`user1`) with password `Welcome1`.

2. Navigate to the dashboard, with the Dashboard icon ([icon: tachometer-alt, set=fas]). Alternatively, select the Menu icon ([icon: bars, set=fas]), and select Dashboard.

3. Initiate the provisioning workflow as `user1`:

   1. Scroll down to the Start a Process menu, and click Edit adjacent to Contractor onboarding process.

   2. Complete the form for the sample user you will be creating. Use an accessible email address, as you'll need the email message to complete this workflow.

   3. Enable Create in CSV File. This option enables implicit synchronization from the managed user repository to the `hr.csv` file.

      |   |                                                                                                                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | `user1` does not provide a password for this user. A password reset request is sent to the email address provided on this form to ensure that only the actual contractor can sign on with this account. |

   4. Select Submit to initiate the process.

   5. Sign off of the end-user UI.

4. Approve the workflow task as `manager1`:

   1. Sign on to the end-user UI as `manager1` with password `Welcome1`.

   2. Navigate to the dashboard, with the Dashboard icon ([icon: tachometer-alt, set=fas]). Alternatively, select the Menu icon ([icon: bars, set=fas]), and select Dashboard.

   3. Under Unassigned Tasks, locate the Approve Contractor task, select Assign, and click Assign to Me.

      Approve Contractor is now listed under My Tasks.

   4. Click Edit adjacent to the task name.

   5. Review the form content, and click Accept.

      |   |                                                   |
      | - | ------------------------------------------------- |
      |   | This is the same content you provided as `user1`. |

   6. Sign off of the end-user UI.

5. Verify that the contractor has been created in the HR data source (`/path/to/openidm/samples/provisioning-with-workflow/data/hr.csv` ):

   ```csv
   "username","firstname","lastname","manager", "department","jobTitle",     ...
   "user1",   "Ordinary", "Employee","manager1","dep1",      "job1",         ...
   "manager1","Big",      "Manager", "",        "dep1",      "Manager",      ...
   "bjensen", "Barbara",  "Jensen",  "user1",   "Payroll",   "Payroll clerk",...
   ```

   Note the addition of the new contractor entry, `bjensen`.

---

---
title: Samples
description: "Provides a number of \"sample deployments\" that walk you through the essential features of PingIDM software, as they would be implemented"
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples"]
page_aliases: ["index.adoc"]
---

# Samples

> Provides a number of "sample deployments" that walk you through the essential features of PingIDM software, as they would be implemented.

These samples demonstrate the core functionality of PingIDM software. The samples correspond to the configurations provided in the `openidm/samples` directory. They cover a number of PingIDM features, often including multiple features in a single sample.

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Samples are provided as a starting point, using default configuration where appropriate. They will most likely need further customization to address the specific requirements of your deployment. |

You don't need a complete understanding of PingIDM software to learn something from these topics, although a background in identity management and maintaining web application software can help. You do need some background in managing services on your operating systems and in your web application containers. You can nevertheless get started with these samples, and then learn more as you go along.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

[icon: cubes, set=fad, size=3x]

#### [Samples Summary](samples-provided.html)

Get a summary of all the samples in this guide.

[icon: play-circle, set=fad, size=3x]

#### [Start Here](start-here.html)

Setup that applies to all samples.

[icon: file-csv, set=fad, size=3x]

#### [Sync With CSV](sync-with-csv.html)

A basic sample showing one-way synchronization from a CSV file to IDM.

[icon: database, set=fad, size=3x]

#### [Sync With LDAP](sync-with-ldap.html)

A basic sample showing one-way synchronization from an LDAP directory to IDM.

[icon: link, set=fad, size=3x]

#### [Sync Two External Resources](sync-two-external-resources.html)

Synchronize two resources without storing data in IDM.

[icon: sync-alt, set=fad, size=3x]

#### [liveSync](livesync-with-ad.html)

*liveSync* between external LDAP resources.

---

---
title: Samples provided with IDM
description: "Overview of all samples provided with PingIDM, with descriptions and links to each sample's documentation page"
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:samples-provided
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/samples-provided.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "High Level"]
---

# Samples provided with IDM

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

This section lists the samples provided with IDM (in the `openidm/samples` directory), with a high-level overview of each sample.

* Example Configurations

  In addition to the samples listed here, IDM provides example configuration and data files that you can use to set up your own project. These files are in the `samples/example-configurations` directory. Each file in this directory is documented in the section that corresponds to the purpose of the file. For example, the `conf/external.email.json` file is described in [Outbound email service](../external-services-guide/email.html).

* Synchronize Data From a CSV File to IDM

  The [`sync-with-csv`](sync-with-csv.html) sample demonstrates one-way synchronization from an external resource to an IDM repository. The external resource in this case is a simple CSV file. User objects in that file are synchronized with the managed users in the IDM repository.

* One-Way Synchronization From LDAP to IDM

  The [`sync-with-ldap`](sync-with-ldap.html) sample uses the generic LDAP connector to connect to an LDAP directory. The sample includes one mapping from the LDAP directory to the managed user repository, and demonstrates reconciliation from the external resource to the repository.

* Two-Way Synchronization Between LDAP and IDM

  The [`sync-with-ldap-bidirectional`](sync-with-ldap-bidirectional.html) sample uses the generic LDAP connector to connect to an LDAP directory. The sample includes two mappings: one from the LDAP directory to the managed user repository, and one in the opposite direction. The sample demonstrates reconciliation from the LDAP directory to the repository and implicit synchronization from the managed user repository to the LDAP directory.

* Synchronize LDAP Groups

  The [`sync-with-ldap-groups`](sync-with-ldap-groups.html) sample uses the generic LDAP connector to connect to an LDAP directory. The sample builds on the [`sync-with-ldap-bidirectional`](sync-with-ldap-bidirectional.html) sample by providing an additional mapping, from the LDAP groups object, to the managed groups object. The sample illustrates a new managed object type (groups) and shows how this object type is synchronized with group containers in LDAP.

* Synchronize LDAP Group Membership

  The [`sync-with-ldap-group-membership`](sync-with-ldap-group-membership.html) sample uses the generic LDAP connector to connect to an LDAP directory. The sample includes two mappings, one from the LDAP directory to the managed user repository, and one from the repository to the LDAP directory. The sample demonstrates synchronization of group membership; that is, how the value of the `ldapGroups` property in a managed user object is mapped to the corresponding user object in LDAP.

* Synchronize Data Between Two External Resources

  The [`sync-two-external-resources`](sync-two-external-resources.html) sample demonstrates synchronization between two external resources, routed through IDM. The resources are named `LDAP` and `AD`, and represent two separate LDAP directories. In the sample both resources are simulated with simple CSV files.

* Asynchronous Reconciliation Using Workflow

  The [`sync-asynchronous`](sync-asynchronous.html) sample shows how you can use workflows to launch an asynchronous reconciliation operation.

* LiveSync With an LDAP Server

  The [`livesync-with-ad`](livesync-with-ad.html) sample shows the liveSync mechanism that pushes changes from an external resource to the IDM repository. The sample uses an LDAP connector to connect to an LDAP directory, either PingDS (DS) or Active Directory.

* Synchronize Accounts With the Google Apps Connector

  The [`sync-with-google`](sync-with-google.html) sample uses the Google Apps Connector to create users and groups on an external Google system, and to reconcile those accounts with the IDM managed user repository.

* Synchronize Users Between Salesforce and IDM

  The [`sync-with-salesforce`](sync-with-salesforce.html) sample demonstrates how to create and update users in Salesforce, using the Salesforce Connector. The sample also shows synchronization of users between Salesforce and the IDM managed user repository.

* Synchronize Kerberos User Principals

  The [`sync-with-kerberos`](sync-with-kerberos.html) sample demonstrates how to use the scripted Kerberos connector to manage Kerberos user principals and to reconcile user principals with IDM managed user objects.

* Store Multiple Passwords For Managed Users

  The [`multiple-passwords`](multiple-passwords.html) sample demonstrates how to set up multiple passwords for managed users, and how to synchronize separate passwords to different external resources. The sample includes two target LDAP servers, each with different password policy and encryption requirements. The sample also shows how to extend the password history policy to apply to multiple password fields.

* Link Multiple Accounts to a Single Identity

  The [`multi-account-linking`](multi-account-linking.html) sample illustrates how IDM addresses links from multiple accounts to one identity. The sample shows how you can create links between a single source account and multiple target accounts, using *link qualifiers* that enable one-to-many relationships in mappings and policies.

* Link Historical Accounts

  The [`historical-account-linking`](historical-account-linking.html) sample demonstrates the retention of inactive (historical) LDAP accounts that have been linked to a corresponding managed user account.

* Connect to DS With ScriptedREST

  The [`scripted-rest-with-dj`](scripted-rest-with-dj.html) sample uses the Groovy Connector Toolkit to implement a ScriptedREST connector that interacts with the DS REST API.

* Connect to MySQL With ScriptedSQL

  The [`scripted-sql-with-mysql`](scripted-sql-with-mysql.html) sample uses the Groovy Connector Toolkit to implement a ScriptedSQL connector that interacts with an external MySQL database.

* Synchronize Users Between IDM and AzureAD

  The [`sync-with-azuread`](sync-with-azuread.html) sample uses the MS Graph API connector to synchronize users between IDM and Azure AD.

* Connect to Active Directory With the PowerShell Connector

  The [`scripted-powershell-with-ad`](scripted-powershell-with-ad.html) sample uses the MS Active Directory PowerShell module to demonstrate how you can synchronize managed objects with a Microsoft Active Directory deployment. The sample provides a number of PowerShell scripts that let you perform basic CRUD (create, read, update, delete) operations on an Active Directory server.

* Provision Users With Roles

  The [`provisioning-with-roles`](provisioning-with-roles.html) sample builds on the sample described in [One-way synchronization from LDAP to IDM](sync-with-ldap.html), and demonstrates how attributes are provisioned to an external system (an LDAP directory), based on role membership.

* Provision Users With Workflow

  The [`provisioning-with-workflow`](provisioning-with-workflow.html) sample demonstrates a typical use case of a workflow, provisioning new users. The sample demonstrates the use of the end-user UI to let users complete a registration process.

  |   |                                                                                                                           |
  | - | ------------------------------------------------------------------------------------------------------------------------- |
  |   | The end-user UI is not bundled with PingIDM. Learn more in [Install the end-user UI](../setup-guide/idm-enduser-ui.html). |

* Direct Audit Information To MySQL

  The [`audit-jdbc`](audit-jdbc.html) sample uses a ScriptedSQL implementation of the Groovy Connector Toolkit to direct audit information to a MySQL database.

* Direct Audit Information to a JMS Broker

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The [JMS](../audit-guide/configuring-topic-handlers.html#audit-jms-handler), [Repository](../audit-guide/configuring-topic-handlers.html#audit-repo-handler), [Router](../audit-guide/configuring-topic-handlers.html#audit-router-handler), and [Syslog](../audit-guide/configuring-topic-handlers.html#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

  The [`audit-jms`](audit-jms.html) sample demonstrates how the JMS audit event handler can publish messages that comply with the [Java™ Message Service Specification Final Release 1.1](https://download.oracle.com/otndocs/jcp/7195-jms-1.1-fr-spec-oth-JSpec/).

* Synchronize Data Between MongoDB and IDM

  The [`sync-with-mongodb`](sync-with-mongodb.html) sample uses the Groovy Connector Toolkit to implement a scripted connector that interacts with a MongoDB Database. The connector can be used for provisioning MongoDB database users and roles from an IDM managed repository.

* Synchronize Data Between HubSpot and IDM

  The [`sync-with-hubspot`](sync-with-hubspot.html) sample demonstrates bidirectional synchronization between IDM managed users and HubSpot contacts.

* Synchronize Data Between a SCIM Provider and IDM

  The [`sync-with-scim`](sync-with-scim.html) sample demonstrates bidirectional synchronization between IDM managed users and roles with corresponding users and roles from a SCIM provider.

* Subscribe to JMS Messages

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The [JMS](../audit-guide/configuring-topic-handlers.html#audit-jms-handler), [Repository](../audit-guide/configuring-topic-handlers.html#audit-repo-handler), [Router](../audit-guide/configuring-topic-handlers.html#audit-router-handler), and [Syslog](../audit-guide/configuring-topic-handlers.html#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

  The [`scripted-jms-subscriber`](scripted-jms-subscriber.html) sample demonstrates the scripted JMS message handler and how it performs Ping REST operations.

* Create a Custom Endpoint

  IDM supports scriptable custom endpoints that let you launch arbitrary scripts through an IDM REST URI. The [`example-configurations/custom-endpoint`](custom-endpoint.html) sample shows how custom endpoints are configured and returns a list of variables available to each method used in a custom endpoint script.

---

---
title: Start here
description: Prerequisites and setup instructions for PingIDM samples, including how to prepare the server and configure PingDS as the LDAP resource
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:start-here
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/start-here.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Configuration"]
section_ids:
  running-samples: Run the samples
  preparing-openidm: Prepare IDM
  ldap-server-config: LDAP server configuration
  start_ds_using_sample_ldif_data: Start DS using sample LDIF data
---

# Start here

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

Before you try any of the samples read [Run the Samples](#running-samples) and [Prepare IDM](#preparing-openidm). For any samples that require an LDAP server, refer to [LDAP Server Configuration](#ldap-server-config).

## Run the samples

Each sample directory in `openidm/samples/` contains a number of subdirectories, such as `conf/` and `script/`. To start IDM with a sample configuration, navigate to the `/path/to/openidm` directory and use the `-p` option of the `startup` command to point to the sample whose configuration you want to use. Some samples require additional software, such as an external LDAP server or database.

Many of the procedures in this guide refer to paths such as `samples/sample-name`. In each of these cases, the complete path is assumed to be `/path/to/openidm/samples/sample-name`.

When you move from one sample to the next, you are changing the IDM configuration. For more information, refer to [Configuration changes](../setup-guide/changing-configuration.html).

The command-line examples in the IDM documentation assume a UNIX shell. To run the samples on Windows, adjust the commands, as necessary.

## Prepare IDM

Install an instance of IDM specifically to experiment with the samples and easily discard the result when you finish.

If you are using the same IDM instance for multiple samples, clear the repository between samples. To do so, shut down IDM and delete the `openidm/db/openidm` directory:

```bash
rm -rf /path/to/openidm/db/openidm
```

## LDAP server configuration

For samples in this guide that require an LDAP server, Ping recommends using PingDS (DS).

> **Collapse: Sample LDAP Server Configuration**
>
> * The LDAP server runs on the local host.
>
> * The LDAP server listens on port 1389.
>
> * The replication port is 8989.
>
>   Servers with replication ports maintain a changelog for their own use. The changelog is exposed over LDAP under the base DN, `cn=changelog`. For samples that demonstrate liveSync with an LDAP server, you *must* configure a replication port when you set up DS. For ease of use, all the LDAP samples assume that you have configured a replication port, even if you don't use liveSync.
>
> * A user with DN `uid=admin` and password `password` has read access to the LDAP server.
>
> * Directory data for that server is stored under base DN `dc=com`.
>
> * User objects for that server are stored under base DN `ou=People,dc=example,dc=com`.
>
> * User objects have the object class `inetOrgPerson`.
>
> * User objects have the following attributes:
>
>   * `cn`
>
>   * `description`
>
>   * `givenName`
>
>   * `mail`
>
>   * `sn`
>
>   * `telephoneNumber`
>
>   * `uid`
>
>   * `userPassword`
>
>   > **Collapse: Example User Object**
>   >
>   > ```ldif
>   > dn: uid=bjensen,ou=People,dc=example,dc=com
>   > objectClass: person
>   > objectClass: organizationalPerson
>   > objectClass: inetOrgPerson
>   > objectClass: top
>   > givenName: Barbara
>   > uid: bjensen
>   > cn: Barbara Jensen
>   > telephoneNumber: 1-360-229-7105
>   > sn: Jensen
>   > mail: bjensen@example.com
>   > description: Created for OpenIDM
>   > userPassword: password
>   > ```

|   |                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you are using the same DS instance for multiple samples, delete the DS configuration between samples:1) Shutdown DS:

   ```
   /path/to/opendj/bin/stop-ds --quiet
   ```

2) Delete the `opendj/db` directory:

   ```
   rm -rf /path/to/opendj/db
   ```

3) Delete the `opendj/config` directory:

   ```
   rm -rf /path/to/opendj/config
   ``` |

### Start DS using sample LDIF data

Samples that use an LDAP server require existing user data. The example procedure below corresponds to the `sync-with-ldap` sample and imports user data (`openidm/samples/sync-with-ldap/data/Example.ldif`) during DS setup. For other samples, replace or remove the path to the sample data, as necessary.

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The following procedure provides setup instructions for DS 8.1. For older versions of DS, or an alternative LDAP server, modify the instructions, as necessary. |

1. Download the [DS and IDM .zip archives](https://backstage.forgerock.com/downloads).

2. Extract the .zip archives.

3. Generate a DS *deploymentId* for DS setup and deployment management:

   ```
   /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
   your-deployment-ID
   ```

4. Start DS:

   ```
   /path/to/opendj/setup \
   --serverId evaluation-only \
   --deploymentId your-deployment-ID \
   --deploymentIdPassword password \
   --rootUserDN uid=admin \
   --rootUserPassword password \
   --hostname localhost \
   --adminConnectorPort 4444 \
   --ldapPort 1389 \
   --enableStartTls \
   --ldapsPort 1636 \
   --replicationPort 8989 \
   --httpPort 8090 \
   --profile ds-user-data:7.0.0 \
   --set ds-user-data/baseDn:dc=com \
   --set ds-user-data/ldifFile:/path/to/openidm/samples/sync-with-ldap/data/Example.ldif \
   --acceptLicense \
   --start
   <License Agreement>...

   Validating parameters..... Done
   Configuring certificates..... Done
   Configuring server..... Done
   Configuring profile DS user data store......... Done
   Starting directory server............... Done

   To see basic server status and configuration, you can launch
   /path/to/opendj/bin/status
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Every DS deployment requires a *deploymentId* and a *deploymentIdPassword* to secure network connections. The deploymentId is a random string generated by DS software. The deploymentIdPassword is a secret string that you choose. It must be at least 8 characters long. The deploymentId and deploymentIdPassword automate key pair generation and signing without storing the CA private key. For more information, refer to [Deployment IDs](https://docs.pingidentity.com/pingds/8.1/security-guide/pki.html#about-deployment-keys) in the *DS Security Guide*. |

5. Import the DS CA certificate into the IDM truststore:

   ```
   /path/to/opendj/bin/dskeymgr \
   export-ca-cert \
   --deploymentId your-deployment-ID \
   --deploymentIdPassword password \
   --alias dscert \
   --keyStoreFile /path/to/openidm/security/truststore \
   --keyStorePassword:file /path/to/openidm/security/storepass
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Because each new deployment of DS has a unique deploymentId, the same certificate does not work from one sample to the next. To handle this scenario, do one of the following:- Give each subsequent sample certificate a unique alias. For example:

     * `--alias dscert1`

     * `--alias dscert2`

     * `--alias dscert3`

   - Delete the old certificate from the trust store:

     ```bash
     keytool \
     -delete \
     -keystore /path/to/openidm/security/truststore \
     -alias dscert
     ``` |

---

---
title: Store multiple passwords for managed users
description: Store and synchronize multiple passwords for PingIDM managed users with separate password policies across two LDAP target systems
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:multiple-passwords
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/multiple-passwords.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Multiple Passwords", "Storage"]
section_ids:
  multiple-passwords-config: Configure the multiple passwords sample
  multiple-passwords-history-policy: Password history policy
  ldap-config-multiple-passwords: LDAP server configuration
  run-sample-multiple-passwords: Show multiple accounts
  run-sample-multiple-passwords-history: Show the password history policy
---

# Store multiple passwords for managed users

This sample demonstrates how to set up multiple passwords for managed users and how to synchronize separate passwords to different external resources.

|   |                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You cannot run this sample through the admin UI. To make the sample work with the admin UI, set the `viewable` and `required` fields of the `password` property in the `conf/managed.json` file as follows:```json
"password" : {
    "title" : "Password",
    "type" : "string",
    "viewable" : true,
...
``` |

## Configure the multiple passwords sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

This sample assumes the following scenario:

* The managed/user repository is the source system.

* There are two target LDAP servers—`ldap` and `ldap2`.

  For the purposes of this sample, the two servers are represented by two separate organizational units on a single PingDS (DS) instance.

* Managed user objects have two additional password fields, each mapped to one of the two LDAP servers.

* Both LDAP servers have a requirement for a password history policy, but the history size differs for the two policies.

  The sample shows how to extend the password history policy described in [Password history policy](../security-guide/passwords.html#password-history) to apply to multiple password fields.

* The value of a managed user's `password` field is used by default for the additional passwords *unless* the CREATE, UPDATE, or PATCH requests on the managed user explicitly contain a value for these additional passwords.

The sample includes several customized configuration files in the `samples/multiple-passwords/conf/` directory. These customizations are crucial to the sample functionality and are described in detail in the following list:

* `provisioner.openicf-ldap.json`

  Configures the connection to the first LDAP directory.

* `provisioner.openicf-ldap2.json`

  Configures the connection to the second LDAP directory.

* `sync.json`

  Provides the mappings from the IDM managed user repository to the respective LDAP servers. The file includes two mappings:

  * A mapping from IDM managed users to the LDAP user objects at the `system/ldap/account` endpoint. This endpoint represents the `ou=People` subtree.

  * A mapping from IDM managed users to the LDAP user objects at the `system/ldap2/account` endpoint. This endpoint represents the `ou=Customers` subtree.

  Both mappings include an explicit mapping from `ldapPassword` and `ldap2Password` to `userPassword` in the standard property mappings. Because these passwords are encrypted, a transform script is defined which uses `openidm.decrypt()` to set the value on the target object.

* `managed.json`

  Contains a customized schema for managed users that includes the additional password fields.

  This file has been customized as follows:

  * The schema includes an `ldapPassword` field that is mapped to the accounts in the `system/ldap/accounts` target. This field is subject to the standard policies associated with the `password` field of a managed user. In addition, the `ldapPassword` must contain two capital letters instead of the usual one capital letter requirement.

  * The schema includes an `ldap2Password` field that is mapped to the accounts in the `system/ldap2/accounts` target. This field is subject to the standard policies associated with the `password` field of a managed user. In addition, the `ldap2Password` must contain two numbers instead of the usual one number requirement.

  * A custom password history policy (`"policyId" : "is-new"`) applies to each of the two mapped password fields `ldapPassword`, and `ldap2Password`.

* `router.json`

  A scripted filter on `managed/user` and `policy/managed/user` that populates the values of the additional password fields with the value of the main `password` field if the additional fields are not included in the request content.

The sample includes the following customized scripts in the `script` directory:

* `onCreate-user-custom.js` and `onUpdate-user-custom.js` are used for validation of the password history policy when a user is created or updated.

* `pwpolicy.js` is an additional policy script for the password history policy.

* `set-additional-passwords.js` populates the values of the additional password fields with the value of the main `password` field if the additional fields are not included in the request content.

## Password history policy

The sample includes a custom password history policy. Although the sample demonstrates the history of password attributes only, you can use this policy to enforce history validation on any managed object property.

The following configuration changes set up the password history policy:

* A `fieldHistory` property is added to managed users. The value of this field is a map of field names to a list of historical values for that field. These lists of values are used by the policy to determine if a new value has previously been used.

  The `fieldHistory` property is not accessible over REST by default, and cannot be modified.

* The `onCreate-user-custom.js` script performs the standard `onCreate` tasks for a managed user object but also stores the initial value of each of the fields for which IDM should keep a history. The script is passed the following configurable properties:

  |                 |                                           |
  | --------------- | ----------------------------------------- |
  | `historyFields` | a list of the fields to store history on. |
  | `historySize`   | the number of historical fields to store. |

* The `onUpdate-user-custom.js` script compares the old and new values of the historical fields on update events to determine if the values have changed. When a new value is detected, it is stored in the list of historical values for that field.

  This script also contains logic to deal with the comparison of encrypted field values. The script is passed the following configurable properties:

  |                 |                                           |
  | --------------- | ----------------------------------------- |
  | `historyFields` | a list of the fields to store history on. |
  | `historySize`   | the number of historical fields to store. |

* The `pwpolicy.js` script contains the additional policy definition for the password history policy. This script compares the new field value with the list of historical values for each field.

  The policy configuration (`policy.json`) references this script in its `additionalFiles` list, so that the policy service loads the policy definition. The new policy takes a `historyLength` parameter, which indicates the number of historical values to enforce the policy on. This number must not exceed the `historySize` specified in the `onCreate` and `onUpdate` scripts.

* The `ldapPassword` and `ldap2Password` fields in the managed user schema have been updated with the policy. For the purposes of this sample the `historySize` has been set to 2 for `ldapPassword` and to 4 for `ldap2Password`.

## LDAP server configuration

1. [Set up DS](start-here.html#ldap-server-config) using `/path/to/openidm/samples/multiple-passwords/data/Example.ldif` .

2. Perform an `ldapsearch` on the LDAP directory, and take note of the organizational units:

   ```
   /path/to/opendj/bin/ldapsearch \
   --port 1636 \
   --useSSL \
   --usePkcs12TrustStore /path/to/opendj/config/keystore \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --hostname localhost \
   --baseDN "dc=example,dc=com" \
   --bindDN uid=admin \
   --bindPassword password \
   "ou=*" \
   ou
   dn: ou=People,dc=example,dc=com
   ou: People

   dn: ou=Customers,dc=example,dc=com
   ou: people
   ou: Customers
   ```

   The organizational units, `ou=People` and `ou=Customers`, represent the two different target LDAP systems that our mappings point to.

## Show multiple accounts

This section starts IDM with the sample configuration, then creates a user with multiple passwords, adhering to the different policies in the configured password policy. The section tests that the user was synchronized to two separate LDAP directories, with the different required passwords, and that the user can bind to each of these LDAP directories.

1. Prepare IDM as described in [Prepare IDM](start-here.html#preparing-openidm), then start the server with the configuration for the multiple passwords sample:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/multiple-passwords
   ```

2. Create a user, jdoe, providing individual values for each of the different password fields, that comply with the three different password policies:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "userName": "jdoe",
     "givenName": "John",
     "sn": "Doe",
     "displayName": "John Doe",
     "mail": "john.doe@example.com",
     "password": "Secretpw1",
     "ldapPassword": "S3cretPw",
     "ldap2Password": "Secr3tpw1"
   }' \
   "http://localhost:8080/openidm/managed/user?_action=create"
   {
     "_id": "5ce188f6-252b-429e-aad1-4d8754d77de5",
     "_rev": "00000000d2d76089",
     "userName": "jdoe",
     "givenName": "John",
     "sn": "Doe",
     "displayName": "John Doe",
     "mail": "john.doe@example.com",
     "ldapPassword": {
       "$crypto": {
         "type": "x-simple-encryption",
         "value": {
           "cipher": "AES/CBC/PKCS5Padding",
           "stableId": "openidm-sym-default",
           "salt": "lkackh...",
           "data": "T0mljk...",
           "keySize": 16,
           "purpose": "idm.password.encryption",
           "iv": "ehSMbdNn...",
           "mac": "PssPOsW..."
         }
       }
     },
     "ldap2Password": {
       "$crypto": {
         "type": "x-simple-encryption",
         "value": {
           "cipher": "AES/CBC/PKCS5Padding",
           "stableId": "openidm-sym-default",
           "salt": "lSzMTU54...",
           "data": "UWlQo5Ws...",
           "keySize": 16,
           "purpose": "idm.password.encryption",
           "iv": "ehSMbdN...",
           "mac": "PssPOs..."
         }
       }
     },
     "accountStatus": "active",
     "effectiveRoles": [],
     "effectiveAssignments": [],
     "roles": []
   }
   ```

   The user has been created with three different passwords that comply with three distinct password policies. The passwords have been encrypted as defined in the `managed.json` file.

   |   |                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In this example, the user has been created with ID `5ce188f6-252b-429e-aad1-4d8754d77de5`. You will need the user ID when you update the entry later in this procedure. |

3. As a result of implicit synchronization, two separate LDAP accounts should have been created for user jdoe on our two simulated LDAP servers. For more information about implicit synchronization, refer to [Synchronization types](../synchronization-guide/sync-types.html).

4. Query the IDs in the LDAP directory as follows:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/ldap/account?_queryId=query-all-ids"
   {
     "result": [
       {
         "_id": "00452010-a164-4065-9f84-3e4636a3ee20",
       },
       {
         "_id": "e5b35587-2d7c-4faa-b3e5-962f5a4ada5c",
       }
     ],
     ...
   }
   ```

   jdoe has two entries—one in `ou=People` and one in `ou=Customers`.

5. To verify the passwords propagated correctly, perform an LDAP search, bound using each of the jdoe accounts, against the rootDSE.

   |   |                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For the following commands, make sure to enter 2 or 3 at the following prompt:```
   Do you trust this server certificate?

     1) No
     2) Yes, for this session only
     3) Yes, also add it to a truststore
     4) View certificate details

   Enter choice [1]: 2
   ``` |

   ```
   /path/to/opendj/bin/ldapsearch \
   --hostname localhost \
   --port 1636 \
   --useSSL \
   --bindDN uid=jdoe,ou=People,dc=example,dc=com \
   --bindPassword S3cretPw \
   --searchScope base \
   --baseDN "" "(objectClass=*)"
   dn:
   objectClass: top
   objectClass: ds-root-dse
   ```

   ```
   /path/to/opendj/bin/ldapsearch \
   --hostname localhost \
   --port 1636 \
   --useSSL \
   --bindDN uid=jdoe,ou=Customers,dc=example,dc=com \
   --bindPassword Secr3tpw1 \
   --searchScope base \
   --baseDN "" "(objectClass=*)"
   dn:
   objectClass: top
   objectClass: ds-root-dse
   ```

6. Patch jdoe's managed user entry (`5ce188f6-252b-429e-aad1-4d8754d77de5`) to change his `ldapPassword`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PATCH \
   --data '[ {
     "operation": "replace",
     "field": "ldapPassword",
     "value": "TTestw0rd"
   } ]' \
   "http://localhost:8080/openidm/managed/user/5ce188f6-252b-429e-aad1-4d8754d77de5"
   {
     "_id": "5ce188f6-252b-429e-aad1-4d8754d77de5",
     "_rev": "000000001298f6a6",
     "userName": "jdoe",
     "givenName": "John",
     "sn": "Doe",
     "displayName": "John Doe",
     ...
     "ldapPassword": {
       "$crypto": {
         "type": "x-simple-encryption",
         "value": {
           "cipher": "AES/CBC/PKCS5Padding",
           "stableId": "openidm-sym-default",
           "salt": "Vlco8e...",
           "data": "INj9lk...",
           "keySize": 16,
           "purpose": "idm.password.encryption",
           "iv": "ehSMbdNn...",
           "mac": "PssPOsW..."
         }
       }
     },
     ...
   }
   ```

7. To verify the password change propagated correctly, perform an LDAP search, bound using jdoe from the People organizational unit, against the rootDSE.

   |   |                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For the following command, make sure to enter `2` or `3` at the following prompt:```
   Do you trust this server certificate?

     1) No
     2) Yes, for this session only
     3) Yes, also add it to a truststore
     4) View certificate details

   Enter choice [1]: 2
   ``` |

   ```
   /path/to/opendj/bin/ldapsearch \
   --hostname localhost \
   --port 1636 \
   --useSSL \
   --bindDN uid=jdoe,ou=People,dc=example,dc=com \
   --bindPassword TTestw0rd \
   --searchScope base \
   --baseDN "" "(objectClass=*)"
   dn:
   objectClass: top
   objectClass: ds-root-dse
   ```

## Show the password history policy

This section demonstrates the password history policy by patching jdoe's managed user entry, changing his `ldapPassword` multiple times.

1. Send the following patch requests, changing the value of jdoe's `ldapPassword` each time:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PATCH \
   --data '[ {
     "operation": "replace",
     "field": "ldapPassword",
     "value": "TTestw0rd1"
   } ]' \
   "http://localhost:8080/openidm/managed/user/5ce188f6-252b-429e-aad1-4d8754d77de5"
   {
     "_id": "5ce188f6-252b-429e-aad1-4d8754d77de5",
     "_rev": "00000000a92657c7",
     "userName": "jdoe",
     "givenName": "John",
     "sn": "Doe",
     "displayName": "John Doe",
     "mail": "john.doe@example.com",
     ...
     "ldapPassword": {
       "$crypto": {
         "type": "x-simple-encryption",
         "value": {
           "cipher": "AES/CBC/PKCS5Padding",
           "stableId": "openidm-sym-default",
           "salt": "TjolL7...",
           "data": "Unbalo...",
           "keySize": 16,
           "purpose": "idm.password.encryption",
           "iv": "ehSMbdNn...",
           "mac": "PssPOsW..."
         }
       }
     },
     ...
   }
   ```

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PATCH \
   --data '[ {
     "operation": "replace",
     "field": "ldapPassword",
     "value": "TTestw0rd2"
   } ]' \
   "http://localhost:8080/openidm/managed/user/5ce188f6-252b-429e-aad1-4d8754d77de5"
   {
     "_id": "5ce188f6-252b-429e-aad1-4d8754d77de5",
     "_rev": "00000000dc6160c8",
     "userName": "jdoe",
     "givenName": "John",
     "sn": "Doe",
     "displayName": "John Doe",
     ...
     "ldapPassword": {
       "$crypto": {
         "type": "x-simple-encryption",
         "value": {
           "cipher": "AES/CBC/PKCS5Padding",
           "stableId": "openidm-sym-default",
           "salt": "Ynio9n...",
           "data": "R0ol2b...",
           "keySize": 16,
           "purpose": "idm.password.encryption",
           "iv": "ehSMbdNn...",
           "mac": "PssPOsW..."
         }
       }
     },
     ...
   }
   ```

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PATCH \
   --data '[ {
     "operation": "replace",
     "field": "ldapPassword",
     "value": "TTestw0rd3"
   } ]' \
   "http://localhost:8080/openidm/managed/user/5ce188f6-252b-429e-aad1-4d8754d77de5"
   {
     "_id": "5ce188f6-252b-429e-aad1-4d8754d77de5",
     "_rev": "00000000a92657c7",
     "userName": "jdoe",
     "givenName": "John",
     "sn": "Doe",
     "displayName": "John Doe",
     ...
     "ldapPassword": {
       "$crypto": {
         "type": "x-simple-encryption",
         "value": {
           "cipher": "AES/CBC/PKCS5Padding",
           "stableId": "openidm-sym-default",
           "salt": "9kilajT...",
           "data": "Hnkja98...",
           "keySize": 16,
           "purpose": "idm.password.encryption",
           "iv": "ehSMbdNn...",
           "mac": "PssPOsW..."
         }
       }
     },
     ...
   }
   ```

   User jdoe now has a *history* of `ldapPassword` values, that contains `TTestw0rd3`, `TTestw0rd2`, `TTestw0rd1`, and `TTestw0rd`, in that order.

2. The history size for the `ldapPassword` policy is set to 2. To demonstrate the history policy, attempt to patch jdoe's entry with a password value that was used in his previous 2 password changes: `TTestw0rd2`:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PATCH \
   --data '[ {
     "operation": "replace",
     "field": "ldapPassword",
     "value": "TTestw0rd2"
   } ]' \
   "http://localhost:8080/openidm/managed/user/5ce188f6-252b-429e-aad1-4d8754d77de5"
   {
     "code": 403,
     "reason": "Forbidden",
     "message": "Failed policy validation",
     "detail": {
       "result": false,
       "failedPolicyRequirements": [
         {
           "policyRequirements": [
             {
               "policyRequirement": "IS_NEW"
             }
           ],
           "property": "ldapPassword"
         }
       ]
     }
   }
   ```

   The password change fails the `IS_NEW` policy requirement.

3. Change jdoe's `ldapPassword` to a value not used in the previous two updates:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PATCH \
   --data '[ {
     "operation": "replace",
     "field": "ldapPassword",
     "value": "TTestw0rd"
   } ]' \
   "http://localhost:8080/openidm/managed/user/5ce188f6-252b-429e-aad1-4d8754d77de5"
   {
     "_id": "5ce188f6-252b-429e-aad1-4d8754d77de5",
     "_rev": "00000000792afa08",
     "userName": "jdoe",
     "givenName": "John",
     "sn": "Doe",
     "displayName": "John Doe",
     ...
     "ldapPassword": {
       "$crypto": {
         "type": "x-simple-encryption",
         "value": {
           "cipher": "AES/CBC/PKCS5Padding",
           "stableId": "openidm-sym-default",
           "salt": "Ivmal5...",
           "data": "0mkywe...",
           "keySize": 16,
           "purpose": "idm.password.encryption",
           "iv": "ehSMbdNn...",
           "mac": "PssPOsW..."
         }
       }
     },
     ...
   }
   ```

   The password change succeeds.

---

---
title: Subscribe to JMS messages
description: (Deprecated; JMS handler deprecated) Configure PingIDM as a JMS subscriber using ActiveMQ Artemis to receive and process REST operation payloads
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:scripted-jms-subscriber
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/scripted-jms-subscriber.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Subscriptions", "JMS"]
section_ids:
  scripted-jms-overview: Sample overview
  dependencies_for_jms_messaging: Dependencies for JMS messaging
  configure_ssl_for_apache_activemq_artemis: Configure SSL for Apache ActiveMQ Artemis
  jms-scripted-sample-secure: Configure a secure port for JMS messages
  jms-scripted-sample-start: Start the ActiveMQ Artemis broker and IDM
  scripted-artemis-start-messages: Use the ActiveMQ Artemis UI to access the REST interface
  customizing-jms-scripted: Customize the scripted JMS sample
---

# Subscribe to JMS messages

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The [JMS](../audit-guide/configuring-topic-handlers.html#audit-jms-handler), [Repository](../audit-guide/configuring-topic-handlers.html#audit-repo-handler), [Router](../audit-guide/configuring-topic-handlers.html#audit-router-handler), and [Syslog](../audit-guide/configuring-topic-handlers.html#audit-syslog-handler) audit event handlers are [deprecated](../release-notes/deprecated-functionality.html#deprecation-audit-event-handlers) and will be removed in a future release of IDM. Use the [JSON audit event handler](../audit-guide/configuring-topic-handlers.html#audit-json-handler) or similar to export your data to a third-party audit framework, such as [Elastic Stack](https://www.elastic.co/elastic-stack). |

IDM can subscribe to Java Messaging Service (JMS) messages using the Messaging Service's JMS Subscriber. In an event-driven architecture, also known as a message-driven architecture, there are publishers and subscribers. When a publisher sends a message over JMS, that message is broadcast. All active and subscribed clients receive that message. This sample shows how IDM can act as a JMS message subscriber, using the ActiveMQ Artemis JMS message broker.

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For more information on how IDM can publish JMS messages using the JMS Audit Event Handler, refer to [Direct audit information to a JMS broker](audit-jms.html) |

## Sample overview

With the scripted message handler shown in this sample, you can configure scripts to parse the contents of JMS messages, and act on that content.

The script in this sample, `crudpaqTextMessageHandler.js`, shows how JMS can handle Ping REST operations. If you customize a script to manage JMS messages, you must also modify the `conf/messaging.json` file.

This sample uses ActiveMQ Artemis, a JMS message broker. With the ActiveMQ Artemis UI, you can act as the JMS message provider. This sample demonstrates how you can input REST payloads using the Artemis UI.

## Dependencies for JMS messaging

The JMS audit event handler requires Apache ActiveMQ Artemis and additional dependencies bundled with the ActiveMQ Artemis delivery. This section lists the dependencies, and where they must be installed in the IDM instance. If you use a different ActiveMQ version, you may need to download the corresponding dependencies separately.

1. Download the following files:

   * [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis/download/).

     |   |                                             |
     | - | ------------------------------------------- |
     |   | This sample was tested with version 2.20.0. |

   * The most recent `bnd` JAR file from <https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/>.

     |   |                                                                                                                   |
     | - | ----------------------------------------------------------------------------------------------------------------- |
     |   | The [bnd](https://bnd.bndtools.org/) utility lets you create OSGi bundles for libraries that do not support OSGi. |

2. Unpack the ActiveMQ Artemis archive. For example:

   ```
   tar -xvf ~/Downloads/apache-artemis-2.20.0-bin.tar.gz
   ```

3. Create a temporary directory, and then change to that directory:

   ```
   mkdir ~/Downloads/tmp
   cd ~/Downloads/tmp/
   ```

4. Move the ActiveMQ Artemis Client and `bnd` JAR files to the temporary directory.

   ```
   mv ~/Downloads/apache-artemis-2.20.0/lib/client/artemis-jms-client-all-2.20.0.jar ~/Downloads/tmp/
   mv ~/Downloads/biz.aQute.bnd-version.jar ~/Downloads/tmp/
   ```

5. Create an OSGi bundle:

   1. In a text editor, create a BND file named `activemq.bnd` with the following contents, and save it to the current directory:

      ```
      version=2.20.0
      Export-Package: *;version=${version}
      Import-Package: !org.apache.log4j.*,!org.apache.log.*,!org.apache.avalon.framework.logger.*,!org.apache.avalon.framework.logger.*,!org.glassfish.json.*,!org.conscrypt.*,!org.apache.logging.*,!org.bouncycastle.jsse.*,!org.eclipse.*,!sun.security.*,!reactor.*,!org.apache.activemq.artemis.shaded.*,!com.aayushatharva.*,!com.github.luben.zstd,!com.jcraft.jzlib,!com.ning.compress,!com.ning.compress.lzf,!com.ning.compress.lzf.util,!com.oracle.svm.core.annotate,!lzma.*,!net.jpountz.*,*
      Bundle-Name: ActiveMQArtemis :: Client
      Bundle-SymbolicName: org.apache.activemq
      Bundle-Version: ${version}
      ```

      Your `tmp/` directory should now contain the following files:

      ```
      ls -1 ~/Downloads/tmp/
      activemq.bnd
      artemis-jms-client-all-2.20.0.jar
      biz.aQute.bnd-version.jar
      ```

   2. In the same directory, create the OSGi bundle archive file. For example:

      ```
      java -jar biz.aQute.bnd-version.jar wrap \
      --properties activemq.bnd \
      --output artemis-jms-client-all-2.20.0-osgi.jar \
      artemis-jms-client-all-2.20.0.jar
      ```

6. Copy the resulting `artemis-jms-client-all-2.20.0-osgi.jar` file to the `openidm/bundle` directory:

   ```
   cp artemis-jms-client-all-2.20.0-osgi.jar /path/to/openidm/bundle/
   ```

## Configure SSL for Apache ActiveMQ Artemis

For information on configuring Apache ActiveMQ Artemis security features, including SSL, download [ActiveMQ Artemis 2.2.0](https://archive.apache.org/dist/activemq/activemq-artemis/2.2.0/) and view the included documentation.

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can also view the [latest Apache Artemis documentation](https://artemis.apache.org/components/artemis/documentation/latest/index.html), but the features described might differ from the version tested with IDM. |

### Configure a secure port for JMS messages

If you configured SSL for ActiveMQ Artemis, edit `/path/to/openidm/samples/scripted-jms-subscriber/conf/messaging.json`, and replace the `java.naming.provider.url`:

```json
"java.naming.provider.url" : "ssl://localhost:61617?daemon=true"
```

## Start the ActiveMQ Artemis broker and IDM

With the appropriate bundles in the `/path/to/openidm/bundles` directory, you're ready to start the ActiveMQ Artemis message broker, as well as IDM with the JMS Audit Sample.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a full list of ActiveMQ Artemis setup options, refer to [Using the Server](https://activemq.apache.org/components/artemis/documentation/latest/using-server.html) in the *Artemis Documentation*. |

1. Navigate to the directory where you unpacked the ActiveMQ Artemis binary and run the following command to create the Artemis broker:

   ```
   cd ~/Downloads/apache-artemis-2.20.0/bin
   ./artemis create fr-scripted-jms
   Creating ActiveMQ Artemis instance at: /path/to/Downloads/apache-artemis-2.20.0/bin/fr-scripted-jms
   ...
   ```

2. Start the newly created ActiveMQ Artemis broker:

   ```
   ./fr-scripted-jms/bin/artemis run
   ```

3. [Set up DS](start-here.html#ldap-server-config) without importing any LDIF file or [select another repository](../install-guide/chap-repository.html) for the sample.

4. Start IDM, with the configuration for this sample:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/scripted-jms-subscriber
   ```

5. Verify you can access the [Artemis management console](https://activemq.apache.org/components/artemis/documentation/latest/management-console.html) at `http://localhost:8161/console`.

## Use the ActiveMQ Artemis UI to access the REST interface

In this section, you will use the ActiveMQ Artemis UI to send REST requests.

1. Log in to the Artemis management console (`http://localhost:8161/console`).

2. From the navigation menu, click Artemis.

   ![Artemis navigation menu](_images/artemisNav.png)

3. From the tree view, select the addresses node.

   ![Artemis addresses node](_images/artemisAddressesNode.png)

4. On the addresses page, click the Create address tab.

   ![Artemis create address tab](_images/artemisCreateAddressTab.png)

   |   |                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on your window size, the Create address tab may be located under the More [icon: angle-down, set=fas]menu. |

5. Fill out the Create Address form, and then click Create Address:

   ![Artemis create address form](_images/artemisCreateAddressForm.png)

   * Address name: `idmQ`

   * Routing type: `Anycast`

6. From the tree view, expand the addresses node, and click idmQ.

   ![Artemis addresses > idmQ](_images/artemisAddressNodeidmQ.png)

7. On the idmQ page, click the Send message tab.

   ![Artemis send message tab](_images/artemisSendMessageTab.png)

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | Depending on your window size, the Send message tab may be located under the More [icon: angle-down, set=fas]menu. |

8. On the Send Message page, paste the following text into the Body field. This request creates a new user with a user ID of `mgr1`:

   ```json
   {
     "operation" : "CREATE",
     "resourceName" : "/managed/user",
     "newResourceId" : "mgr1",
     "content" : {
       "mail" : "mgr1@example.com",
       "sn" : "Sanchez",
       "givenName" : "Jane",
       "password" : "Password1",
       "employeenumber" : 100,
       "accountStatus" : "active",
       "roles" : [ ],
       "userName" : "mgr1"
     },
     "params" : {},
     "fields" : [ ]
   }
   ```

   ![Artemis send message page](_images/artemisSendMessagePage.png)

   For comparison, the following equivalent REST call would create the same user:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "mail" : "mgr1@example.com",
     "sn" : "Sanchez",
     "givenName" : "Jane",
     "password" : "Password1",
     "employeenumber" : 100,
     "accountStatus" : "active",
     "roles" : [ ],
     "userName" : "mgr1",
     "params" : {},
     "fields" : [ ]
   }' \
   "http://localhost:8080/openidm/managed/user?_action=create"
   ```

9. Click Send Message.

   The OSGi console displays the message request and response:

   ```json
   **************request received*************
   Parsed JMS JSON =
   {
       "operation": "CREATE",
       "resourceName": "/managed/user",
       "newResourceId": "mgr1",
       "content": {
           "mail": "mgr1@example.com",
           "sn": "Sanchez",
           "givenName": "Jane",
           "password": "Password1",
           "employeenumber": 100,
           "accountStatus": "active",
           "roles": [],
           "userName": "mgr1"
       },
       "params": {},
       "fields": []
   }
   Message response is...
   {
       "accountStatus": "active",
       "password": {
           "$crypto": {
               "type": "x-simple-encryption",
               "value": { <encryptedValue> }
           }
       },
       "mail": "mgr1@example.com",
       "employeenumber": 100,
       "givenName": "Jane",
       "sn": "Sanchez",
       "userName": "mgr1",
       "effectiveRoles": [],
       "memberOfOrgIDs": [],
       "effectiveAssignments": [],
       "_rev": "17273eca-d14b-4647-b850-1e3733ba1830-116",
       "_id": "mgr1"
   }
   **************END MESSAGE*************
   ```

10. Confirm the user details:

    ```json
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/managed/user/mgr1"
    {
      "_id": "mgr1",
      "_rev": "17273eca-d14b-4647-b850-1e3733ba1830-116",
      "accountStatus": "active",
      "mail": "mgr1@example.com",
      "employeenumber": 100,
      "givenName": "Jane",
      "sn": "Sanchez",
      "userName": "mgr1",
      "effectiveRoles": [],
      "memberOfOrgIDs": [],
      "effectiveAssignments": []
    }
    ```

11. You can repeat the process using different REST operations in the Artemis UI. For example, enter the following payload on the Send Message page to change the first name (`givenName`) of the `mgr1` user to `Donna`:

    ```json
    {
      "operation": "PATCH",
      "resourceName": "/managed/user/mgr1",
      "value": [
        {
          "operation": "replace",
          "field": "/givenName",
          "value": "Donna"
        }
      ]
    }
    ```

12. Confirm the updated `givenName` for `mgr1`:

    ```json
    curl \
    --header "X-OpenIDM-Username: openidm-admin" \
    --header "X-OpenIDM-Password: openidm-admin" \
    --header "Accept-API-Version: resource=1.0" \
    --request GET \
    "http://localhost:8080/openidm/managed/user/mgr1"
    {
      "_id": "mgr1",
      "_rev": "17273eca-d14b-4647-b850-1e3733ba1830-315",
      "accountStatus": "active",
      "mail": "mgr1@example.com",
      "employeenumber": 100,
      "givenName": "Donna",
      "sn": "Sanchez",
      "userName": "mgr1",
      "effectiveRoles": [],
      "memberOfOrgIDs": [],
      "effectiveAssignments": []
    }
    ```

## Customize the scripted JMS sample

If you set up a custom script to parse and process JMS messages, store that script in the `script/` subdirectory. Assume the script is named `myCustomScript.js`.

Edit the `messaging.json` file in the `conf/` subdirectory, and point it to the custom file:

```json
{
  "subscribers" : [
    {
      "name" : "IDM CREST Queue Subscriber",
      "instanceCount": 3,
      "enabled" : true,
      "type" : "JMS",
      "handler" : {
        "type" : "SCRIPTED",
        "properties" : {
          "script" : {
            "type" : "text/javascript",
            "file" : "myCustomScript.js"
          }
        }
      },
      "properties" : {
        "sessionMode" : "CLIENT",
        "jndi" : {
          "contextProperties" : {
            "java.naming.factory.initial" : "org.apache.activemq.artemis.jndi.ActiveMQInitialContextFactory",
            "java.naming.provider.url" : "tcp://127.0.0.1:61616?daemon=true",
            "queue.idmQ" : "idmQ"
          },
          "destinationName" : "idmQ",
          "connectionFactoryName" : "ConnectionFactory"
        }
      }
    }
  ]
}
```

You'll find some of these properties in [JMS audit event handler properties](../audit-guide/audit-config-prop-jms.html). Despite the name of the table and the different configuration file, the properties are the same.

Other `messaging.json` notable properties:

**JMS messaging.json Configuration Properties**

| `messaging.json` Property | Description                                                                                                                                                                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subscribers`             | Needed to subscribe to incoming JMS message requests.                                                                                                                                                                                                                                                   |
| `name`                    | Arbitrary name for the subscriber.                                                                                                                                                                                                                                                                      |
| `instanceCount`           | Each `instanceCount` manages a single connection between IDM and the messaging channel. Supports multithreading throughput. If subscribing to a queue, such as `queue.idmQ`, the message is handled by a single instance. If subscribing to a topic, all instances receive and handle the same message. |
| `handler`                 | Parses the JMS message, then processes it, possibly through a script.                                                                                                                                                                                                                                   |
| `queue.idmQ`              | One of the JNDI context properties. Name of the JMS queue in the Artemis UI.                                                                                                                                                                                                                            |
| `destinationName`         | JNDI lookup name for message delivery.                                                                                                                                                                                                                                                                  |

---

---
title: Synchronize accounts with the Google Apps connector
description: Use the Google Apps connector to create and synchronize users and groups between PingIDM and Google Workspace
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:sync-with-google
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/sync-with-google.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Synchronization", "Google", "Applications", "Connectors"]
section_ids:
  google-apps-prepare: Prepare the sample
  configure-google-apps-connector: Configure the Google Apps connector
  running-the-google-apps-sample: Run the sample
---

# Synchronize accounts with the Google Apps connector

The Google Apps Connector lets you interact with Google's web applications.

This sample shows how to create users and groups on an external Google system and how to synchronize those accounts with the IDM managed user repository. The sample requires a [Google Apps account](https://support.google.com/a/answer/53926?hl=en).

## Prepare the sample

To set up IDM to connect to your Google Apps account, you must have a Google Apps project that authorizes consent for IDM.

1. Log in to the [Google Apps Developers Console](https://console.developers.google.com/start) and update your existing project or create a new project.

2. [Enable the following APIs](https://support.google.com/googleapi/answer/6158841) for your project:

   * [Admin SDK API](https://console.cloud.google.com/apis/library/admin.googleapis.com)

   * [Enterprise License Manager API](https://console.cloud.google.com/apis/library/licensing.googleapis.com)

   |   |                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Failure to enable the specified APIs results in the following depending on the Google Apps connector version:* For version 1.5.20.19 and lower, connector requests hang indefinitely with no error message.

   * For version 1.5.20.20 and higher, the connector logs an error. |

3. Set up an OAuth2 Client.

   The Google Apps connector uses OAuth2 to authorize the connection to the Google service:

   1. In the Google Apps Developers Console, select Credentials > Create Credentials > OAuth client ID.

   2. Click Configure Consent Screen, select Internal, and click Create.

   3. On the OAuth consent screen, enter an Application name; for example, `IDM`, and click Save.

      This name displays for all applications registered in this project.

   4. Select Credentials > Create Credentials > OAuth client ID > Web application, and enter information in the following fields:

      * Authorized JavaScript origins

        The URI that clients use to access your application. The default URI is `https://localhost:8443`.

        |   |                                                                                                                                                                                              |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | The URI that you enter here must be the same URI you use to access IDM. If you enter `https://localhost:8443` here, but use `http://localhost:8080` to access IDM, the sample will not work. |

      * Authorized redirect URIs

        The OAuth redirect URI, `https://localhost:8443/admin/oauth.html` by default.

   5. Click Create.

   6. On the OAuth client created pop-up, make a note of your Client ID and Client Secret.

4. Add IDM to the Trusted Apps list:

   1. Log in to the [Google Admin Console](https://admin.google.com/).

   2. From the top left menu, select Security > API Controls.

   3. Select MANAGE THIRD-PARTY APP ACCESS, click Change Access, and change the IDM app settings to Trusted.

## Configure the Google Apps connector

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

This procedure uses the admin UI to configure the Google Apps connector.

1. [Set up DS](start-here.html#ldap-server-config) without importing any LDIF file or [select another repository](../install-guide/chap-repository.html) for the sample.

2. Start IDM with the Google Apps sample configuration:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/sync-with-google
   Executing ./startup.sh...
   Using OPENIDM_HOME:   /path/to/openidm
   Using PROJECT_HOME:   /path/to/openidm/samples/sync-with-google/
   Using OPENIDM_OPTS:   -Xmx2048m -Xms2048m
   ...
   Using boot properties at /path/to/openidm/resolver/boot.properties
   -> OpenIDM ready
   ```

3. Log in to the admin UI at the URL `https://localhost:8443/admin` as the default administrative user (`openidm-admin`) with password `openidm-admin`.

   This URL reflects the host on which IDM is installed, and must be the same as the `Authorized JavaScript origin` URI that you set in your Google app.

4. Select Configure > Connectors, and click the Google Apps connector.

5. On the Details tab, enable the connector.

6. In the Base Connector Details area, enter the Client ID and Client Secret that you obtained in the previous section.

7. Click Save.

   IDM redirects you to a Sign in with Google page.

8. Log in.

   After you log in, Google requests that you allow access from your project; in this case, IDM.

   ![google-apps-allow](_images/google-apps-allow.png)

9. Click Allow.

   |   |                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------- |
   |   | If you click Deny, you must return to the Connector Configuration > Details tab in the admin UI, and save your changes again. |

   After you allow access, you are redirected to the Connectors page in the admin UI, where the Google Apps Connector should now be Active.

   ![google-apps-active](_images/google-apps-active.png)

## Run the sample

This procedure uses create, read, update, and delete (CRUD) operations on the Google resource, to verify that the connector is working as expected. The procedure uses a combination of REST commands, to manage objects on the Google system, and the admin UI, to reconcile users from the Google system to the manage user repository.

The sample configuration has one mapping *from* the Google system *to* the managed user repository.

The commands shown here assume that your domain is `example.com`. Adjust the examples to match your domain.

1. Create a user entry on your Google resource, over REST.

   |   |                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------- |
   |   | When you create resources for Google, the equals (`=`) character cannot be used in any attribute value. |

   The following command creates an entry for user `Sam Carter`:

   ```none
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "__NAME__": "samcarter@example.com",
     "__PASSWORD__"  : "password",
     "givenName" : "Sam",
     "familyName": "Carter",
     "agreedToTerms": true,
     "changePasswordAtNextLogin" : false
   }' \
   "http://localhost:8080/openidm/system/google/__ACCOUNT__?_action=create"
   ```

   Which returns:

   ```json
   {
     "_id": "103567435255251233551",
     "_rev": "\"iwpzoDgSq9BJw-XzORg0bILYPVc/LWHPMXXG8M0cjQAPITM95Y636cM\"",
     "orgUnitPath": "/",
     "isAdmin": false,
     "fullName": "Sam Carter",
     "customerId": "C02rsqddz",
     "relations": null,
     "nonEditableAliases": null,
     "suspensionReason": null,
     "includeInGlobalAddressList": true,
     "givenName": "Sam",
     "addresses": null,
     "isDelegatedAdmin": false,
     "changePasswordAtNextLogin": false,
     "isMailboxSetup": true,
     "__NAME__": "samcarter@example.com",
     "agreedToTerms": true,
     "externalIds": null,
     "ipWhitelisted": false,
     "aliases": null,
     "lastLoginTime": [
       "1970-01-01T00:00:00.000Z"
     ],
     "organizations": null,
     "suspended": false,
     "deletionTime": null,
     "familyName": "Carter",
     "ims": null,
     "creationTime": [
       "2016-02-02T12:52:30.000Z"
     ],
     "thumbnailPhotoUrl": null,
     "emails": [
       {
         "address": "samcarter@example.com",
         "primary": true
       }
     ],
     "phones": null
   }
   ```

   Note the `_id` of the new user (`103567435255251233551` in this example). You will need this ID for the update commands in this section.

2. Reconcile the Google resource with the managed user repository.

   This step should create the new user, Sam Carter (and any other users in your Google resource) in the managed user repository.

   1. In the admin UI, select Configure > Mappings.

   2. Click on the sourceGoogle\_\_ACCOUNT\_\_\_managedUser mapping, and click Reconcile.

   3. Select Manage > User and verify that the user Sam Carter has been created in the repository.

3. Update Sam Carter's phone number in your Google resource by sending a PUT request with the updated data, and specifying the user `_id` in the request:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request PUT \
   --header "If-Match: *" \
   --data '{
     "__NAME__": "samcarter@example.com",
     "givenName" : "Sam",
     "familyName": "Carter",
     "agreedToTerms": true,
     "changePasswordAtNextLogin" : false,
     "phones" : [
       {
         "value": "1234567890",
         "type": "home"
       },
       {
         "value": "0987654321",
         "type": "work"
       }
     ]
   }' \
   "http://localhost:8080/openidm/system/google/__ACCOUNT__/103567435255251233551"
   {
     "_id": "103567435255251233551",
     "_rev": "\"iwpzoDgSq9BJw-XzORg0bILYPVc/vfSJgHt-STUUto4lM_4ESO9izR4\"",
     ...
     "emails": [
       {
         "address": "samcarter@example.com",
         "primary": true
       }
     ],
     "phones": [
       {
         "value": "1234567890",
         "type": "home"
       },
       {
         "value": "0987654321",
         "type": "work"
       }
     ]
   }
   ```

4. Read Sam Carter's entry from your Google resource by including his `_id` in the URL:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/google/__ACCOUNT__/103567435255251233551"
   {
     "_id": "103567435255251233551",
     "__NAME__": "samcarter@example.com",
     ...
     "phones": [
       {
         "value": "1234567890",
         "type": "home"
       },
       {
         "value": "0987654321",
         "type": "work"
       }
     ]
   }
   ```

5. Create a group entry on your Google resource:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   --request POST \
   --data '{
     "__NAME__": "testGroup@example.com",
     "__DESCRIPTION__": "Group used for google-connector sample.",
     "name": "TestGroup"
   }' \
   "http://localhost:8080/openidm/system/google/__GROUP__?_action=create"
   {
     "_id": "00meukdy40gpg98",
     "_rev": "\"iwpzoDgSq9BJw-XzORg0bILYPVc/LLhHx2plMJPKeY1-h6eX_OVDi4c\"",
     "adminCreated": true,
     "__NAME__": "testgroup@example.com",
     "aliases": null,
     "nonEditableAliases": null,
     "__DESCRIPTION__": "Group used for google-connector sample.",
     "name": "TestGroup",
     "directMembersCount": 0
   }
   ```

6. Add Sam Carter to the test group you have just created. Include the `Member` endpoint, and Sam Carter's `_id` in the URL. Specify the `_id` of the group you created as the value of the `groupKey` in the JSON payload:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --header "Content-Type: application/json" \
   -H 'If-Match: "iwpzoDgSq9BJw-XzORg0bILYPVc/LLhHx2plMJPKeY1-h6eX_OVDi4c"' \
   --request PUT \
   --data '{
     "__MEMBERS__": [
       {
         "role": "MEMBER",
         "email": "samcarter@example.com"
       }
     ]
   }' \
   "http://localhost:8080/openidm/system/google/__GROUP__/00meukdy40gpg98"
   {
     "_id": "00meukdy40gpg98/samcarter@example.com",
     "_rev": "iwpzoDgSq9BJw-XzORg0bILYPVc/CPNpkRnowkGWRvNQvUK9ev6gQ90",
     "__NAME__": "00meukdy40gpg98/samcarter@example.com",
     "role": "MEMBER",
     "email": "samcarter@example.com",
     "type": "USER",
     "groupKey": "103567435255251233551"
   }
   ```

7. Read the group entry by specifying the group `_id` in the request URL. Notice that the group has one member (`"directMembersCount": 1`):

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   "http://localhost:8080/openidm/system/google/__GROUP__/00meukdy40gpg98"
   {
     "_id": "00meukdy40gpg98",
     "_rev": "iwpzoDgSq9BJw-XzORg0bILYPVc/chUdq5m5_cycV2G4sdl7ZKAF75A",
     "adminCreated": true,
     "__NAME__": "testgroup@example.com",
     "aliases": null,
     "nonEditableAliases": [
       "testGroup@example.test-google-a.com"
     ],
     "__DESCRIPTION__": "Group used for google-connector sample.",
     "name": "TestGroup",
     "directMembersCount": 1
   }
   ```

8. Delete the group entry:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request DELETE \
   "http://localhost:8080/openidm/system/google/__GROUP__/00meukdy40gpg98"
   {
     "_id": "00meukdy40gpg98",
     "_rev": "iwpzoDgSq9BJw-XzORg0bILYPVc/chUdq5m5_cycV2G4sdl7ZKAF75A",
     "adminCreated": true,
     "__NAME__": "testgroup@example.com",
     "aliases": null,
     "nonEditableAliases": [
       "testGroup@example.com.test-google-a.com"
     ],
     "__DESCRIPTION__": "Group used for google-connector sample.",
     "name": "TestGroup",
     "directMembersCount": 1
   }
   ```

   The delete request returns the complete group object.

9. Delete Sam Carter, to return your Google resource to its original state:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request DELETE \
   "http://localhost:8080/openidm/system/google/__ACCOUNT__/103567435255251233551"
   {
     "_id": "103567435255251233551",
     "_rev": "iwpzoDgSq9BJw-XzORg0bILYPVc/ah6xBLujMAHieSWSisPa1CV6T3Q",
     "orgUnitPath": "/",
     "isAdmin": false,
     "fullName": "Sam Carter",
     "customerId": "C02rsqddz",
     "relations": null,
     "nonEditableAliases": [
       "samcarter@example.com.test-google-a.com"
     ],
     "suspensionReason": null,
     "includeInGlobalAddressList": true,
     "givenName": "Sam",
     "addresses": null,
     "isDelegatedAdmin": false,
     "changePasswordAtNextLogin": false,
     "isMailboxSetup": true,
     "__NAME__": "samcarter@example.com",
     "agreedToTerms": true,
     "externalIds": null,
     "ipWhitelisted": false,
     "aliases": null,
     "lastLoginTime": [
       "1970-01-01T00:00:00.000Z"
     ],
     "organizations": null,
     "suspended": false,
     "deletionTime": null,
     "familyName": "Carter",
     "ims": null,
     "creationTime": [
       "2016-02-02T12:52:30.000Z"
     ],
     "thumbnailPhotoUrl": null,
     "emails": [
       {
         "address": "samcarter@example.com",
         "primary": true
       }
     ],
     "phones": [
       {
         "value": "1234567890",
         "type": "home"
       },
       {
         "value": "0987654321",
         "type": "work"
       }
     ]
   }
   ```

In this sample, you used the Google Apps connector to add and delete user and group objects in your Google application and to reconcile users from your Google application to the managed user repository. You can expand on this sample by customizing the connector configuration to provide additional synchronization functionality between IDM and your Google applications. For more information on configuring connectors, refer to [Google Apps connector](https://docs.pingidentity.com/openicf/connector-reference/google.html).

---

---
title: Synchronize data between IDM and a SCIM provider
description: Configure bidirectional synchronization of users and roles between PingIDM and a third-party SCIM provider
component: pingidm
version: 8.1
page_id: pingidm:samples-guide:sync-with-scim
canonical_url: https://docs.pingidentity.com/pingidm/8.1/samples-guide/sync-with-scim.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Samples", "Synchronization", "SCIM"]
section_ids:
  sample-scim-running: Run the sample
---

# Synchronize data between IDM and a SCIM provider

This sample demonstrates bidirectional synchronization between IDM and accounts configured to the [System for Cross-domain Identity Management](http://www.simplecloud.info/). As noted on their website, "The System for Cross-domain Identity Management (SCIM) specification is designed to make managing user identities in cloud-based applications and services easier."

While this sample has been built to comply with SCIM 2.0 standards, it's been tested with a SCIM 1.1 provider.

This sample assumes you've configured SCIM on a third-party system. From that system you'll need the following configuration properties:

* OAuth 2.0 Client ID

* OAuth 2.0 Client Secret

* OAuth 2.0 Token

* SCIM Endpoint

* SCIM Version

* Properties that you want to reconcile from the SCIM provider

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Depending on your provider, you may want to modify the `sync.json` file for this sample to match the properties from the SCIM provider to appropriate properties for IDM. |

For more information on the SCIM connector, including properties for the `provisioner.openicf-scim.json` file, refer to [SCIM connector](https://docs.pingidentity.com/openicf/connector-reference/scim.html#scim).

## Run the sample

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

In this section, you will do the following:

* Start IDM with the sample configuration.

* Configure the SCIM connector and test your connection to the third-party SCIM provider.

* Reconcile your SCIM accounts with the IDM managed user repository.

* Change a user in IDM and reconcile the changes back to the third-party SCIM provider.

* Reconcile your SCIM roles with the IDM managed role repository.

The mapping configuration file (`sync.json`) for this sample includes four mappings, which you'll use to reconcile users and roles:

* `systemScimAccount_managedUser`

* `managedUser_systemScimAccount`

* `systemScimGroup_managedRole`

* `managedRole_systemScimGroup`

1. [Set up DS](start-here.html#ldap-server-config) without importing any LDIF file or [select another repository](../install-guide/chap-repository.html) for the sample.

2. Start IDM with the configuration for the SCIM sample:

   ```
   cd /path/to/openidm/
   ./startup.sh -p samples/sync-with-scim
   ```

3. Configure the SCIM connector, in the following configuration file: `samples/sync-with-scim/conf/provisioner.openicf-scim.json` .

   |   |                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Depending on the requirements of your third-party SCIM provider, it may be acceptable to have a `null` value for properties such as `user`, `password`, and `tokenEndpoint`. |

4. Test the connection to your third-party SCIM provider with the following command:

   ```
   curl \
   --header "X-OpenIDM-Username: openidm-admin" \
   --header "X-OpenIDM-Password: openidm-admin" \
   --header "Accept-API-Version: resource=1.0" \
   --request POST \
   "http://localhost:8080/openidm/system?_action=test"
   [
     {
       "name": "scim",
       "enabled": true,
       "config": "config/provisioner.openicf/scim",
       "connectorRef": {
         "bundleVersion": "1.5.20.31",
         "bundleName": "org.forgerock.openicf.connectors.scim-connector",
         "connectorName": "org.forgerock.openicf.connectors.scim.ScimConnector"
       },
       "displayName": "Scim Connector",
       "objectTypes": [
         "__ALL__",
         "account",
         "group"
       ],
       "ok": true
     }
   ]
   ```

   A status of `"ok": true` indicates that the connector can connect to your third-party SCIM provider.

5. To reconcile your existing third-party SCIM users with the IDM managed user repository, do one of the following:

   * Run the command:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request POST \
     "http://localhost:8080/openidm/recon?_action=recon&mapping=systemScimAccount_managedUser&waitForCompletion=true"
     {
       "_id": "bdba3003-0c8a-4543-9efb-26269c78fa8b-96949",
       "state": "SUCCESS"
     }
     ```

   * In the admin UI, select Configure > Mappings, and select Reconcile on the `systemScimAccount_managedUser` mapping.

6. In the admin UI, select Manage > User and verify that the users from the third-party SCIM provider have been created as IDM managed users.

7. In the admin UI, select Manage > User, select a user to edit, and change one of the user properties.

8. To reconcile the users in the managed user repository with your SCIM users, do one of the following:

   * Run the command:

     ```
     curl \
     --header "X-OpenIDM-Username: openidm-admin" \
     --header "X-OpenIDM-Password: openidm-admin" \
     --header "Accept-API-Version: resource=1.0" \
     --request POST \
     "http://localhost:8080/openidm/recon?_action=recon&mapping=managedUser_systemScimAccount&waitForCompletion=true"
     {
       "_id": "bdba3003-0c8a-4543-9efb-26269c78fa8b-104117",
       "state": "SUCCESS"
     }
     ```

   * In the admin UI, select Configure > Mappings, and then select Reconcile on the `managedUser_systemScimAccount` mapping.

9. Verify that the contact was updated on your third-party SCIM provider.

10. Repeat the process with roles. To reconcile existing third-party SCIM roles with IDM managed roles, do one of the following:

    * Run the command:

      ```
      curl \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request POST \
      "http://localhost:8080/openidm/recon?_action=recon&mapping=systemScimGroup_managedRole&waitForCompletion=true"
      {
        "_id": "7dac3ea9-c6be-4ff9-ae46-d8a0431949b3-7745",
        "state": "SUCCESS"
      }
      ```

    * In the admin UI, select Configure > Mappings, and select Reconcile on the `systemScimGroup_managedRole` mapping.

11. In the admin UI, select Manage > Role, select a role to edit, and add a user to that role.

12. To reconcile the roles in the managed user repository with your SCIM users, do one of the following:

    * Run the command::

      ```
      curl \
      --header "X-OpenIDM-Username: openidm-admin" \
      --header "X-OpenIDM-Password: openidm-admin" \
      --header "Accept-API-Version: resource=1.0" \
      --request POST \
      "http://localhost:8080/openidm/recon?_action=recon&mapping=managedRole_systemScimGroup&waitForCompletion=true"
      {
        "_id": "bdba3003-0c8a-4543-9efb-26269c78fa8b-112074",
        "state": "SUCCESS"
      }
      ```

    * In the admin UI, select Configure > Mappings, and select Reconcile on the `managedRole_systemScimGroup` mapping.

13. Verify that the role was updated on your third-party SCIM provider.
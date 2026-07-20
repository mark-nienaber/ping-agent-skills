---
description: Explains how to build a PingFederate server profile from a running deployment using bulk API export or configuration archive, plus the bulk config tool
component: devops
page_id: devops::how-to/buildPingFederateProfile
canonical_url: https://developer.pingidentity.com/devops/how-to/buildPingFederateProfile.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-build-a-pingfederate-profile-from-your-current-deployment: Build a PingFederate Profile From Your Current deployment
  devops-before-you-begin: Before you begin
  devops-overview-of-profile-methods: Overview of profile methods
  devops-the-bulk-api-export-profile-method: The Bulk API Export Profile Method
  devops-about-this-method: About this method
  devops-steps: Steps
  devops-result: Result
  devops-making-the-bulk-api-export-profile-worthy: "Making the bulk API export \"profile-worthy\""
  devops-example: Example
  devops-using-bulk-config-tool: Using Bulk Config Tool
  devops-prerequisites: Prerequisites
  example: Example
  devops-configure-bulk-tool: Configure Bulk Tool
  change-value: change-value
  devops-remove-config: remove-config
  devops-expose-parameters: expose-parameters
  devops-config-aliases: config-aliases
  devops-sort-arrays: sort-arrays
  devops-additional-notes: Additional Notes
  the-configuration-archive-profiles-method: The Configuration Archive Profiles Method
  devops-about-configuration-archive-based-profiles: About configuration archive-based profiles
  devops-about-this-method-2: About this method
  devops-installing-pingfederate-integration-kits: Installing PingFederate Integration Kits
---

## Build a PingFederate Profile From Your Current deployment

The term "profile" can vary in many instances. Here we will focus on two types of profiles for PingFederate: configuration archive, and bulk export. We will discuss the similarities and differences between two as well as how to build either from a running PingFederate environment.

### Before you begin

You must:

* Complete [Get Started](../get-started/introduction.html) to set up your DevOps environment and run a test deployment of the products

* Understand our [Product Container Anatomy](../reference/config.html)

You should:

* Review [Customizing Server Profiles](profiles.html)

### Overview of profile methods

There are two file-based profile methods that we cover:

* Bulk API Export

  * The resulting `.json` from the admin API at /bulk/export

  * Typically saved as `data.json`

* Configuration Archive

  * Pulled either from the admin UI - Server > Configuration Archive or from the admin API at `/configArchive`

  * We call the result of this output `data.zip` or the `/data` folder

A file-based profile means a "complete profile" looks like a **subset** of files that you would typically find in a running PingFederate filesystem.

This subset of files represents the minimal number of files needed to achieve your PingFederate configuration. All additional files that are not specific to your configuration should be left out because the PingFederate Docker image fills them in. For more information, see [Container Anatomy](containerAnatomy.html).

Familiarity with the PingFederate filesystem will help you achieve the optimal profile. For more information, see [profile structures](../reference/profileStructures.html).

|   |                                                                                              |
| - | -------------------------------------------------------------------------------------------- |
|   | You should save every file outside of `pingfederate/server/default/data` that you've edited. |

Additionally, all files that are included in the profile should also be environment agnostic. This typically means turning hostnames and secrets into variables that can be delivered from the [Orchestration Layer](profilesSubstitution.html).

### The Bulk API Export Profile Method

#### About this method

You will:

1. Export a `data.json` from /bulk/export

2. Configure and run bulkconfig tool

3. Export Key Pairs

4. base64 encode exported key pairs

5. Add `data.json.subst` to your profile at `instance/bulk-config/data.json.subst`

> In this guide, we will look at the above steps in detail to understand the purpose and flow. Use the steps for reference as needed.

A PingFederate Admin Console imports a `data.json` on startup if it finds it in `instance/bulk-config/data.json`.

The PF admin API `/bulk/export` endpoint outputs a large .json blob that is representative of the entire `pingfederate/server/default/data` folder, PingFederate 'core config', or a representation of anything you would configure from the PingFedera0te UI. This file can be considered as "the configuration archive in .json format".

##### Steps

1. On a running PingFederate instance or pod, run:

   ```shell
   curl \
     --location \
     --request GET 'https://pingfederate-admin.ping-devops.com/pf-admin-api/v1/bulk/export' \
     --header 'X-XSRF-Header: PingFederate' \
     --user "administrator:${passsword}" > data.json
   ```

2. Save data.json into a profile at `instance/bulk-config/data.json`.

3. Delete everything except `pf.jwk` in `instance/server/default/data`.

##### Result

You have a bulk API export "profile". This file is useful because the entire config is in a single file and if you store it in source control, then you only have to compare differences in one file. However, there is more value than being in one file.

#### Making the bulk API export "profile-worthy"

By default, the resulting `data.json` from the export contains encrypted values, and to import this file, your PingFederate needs to have the corresponding master key (`pf.jwk`) in `pingfederate/server/default/data`.

|   |                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the DevOps world, we call this folder `instance/server/default/data`. However, each of the encrypted values also have the option to be replaced with an unencrypted form and, when required, a corresponding password. |

##### Example

The SSL Server Certificate from the [PingFederate Baseline Profile](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/baseline/pingfederate) when exported to data.json has the following syntax:

```shell
{
    "resourceType": "/keyPairs/sslServer",
    "operationType": "SAVE",
    "items": [
        {
            "id": "sslservercert",
            "fileData": "MIIRBwIBAzCCEMAGCSqGSIb3DQEHAaCCELEEghCtMIIQqTCCCeUGCSqGSIb3DQEHAaCCCdYEggnSMIIJzjCCCcoGCyqGSIb3DQEMCgECoIIJezCCCXcwKQYKKoZIhvcNAQwBAzAbBBQu6vDERQZX3uujWa7v_q3sYN4Q0gIDAMNQBIIJSFtdWbvLhzYrTqeKKiJqiqROgE0E4mkVvmEC6NwhhPbcH37IDNvVLu0umm--CDZnEmlyPpUucO345-U-6z-cskw4TbsjYIzM10MwS6JdsyYFTC3GwqioqndVgBUzDh8xGnfzx52zEehX8d-ig1F6xYsbEc01gTbh4lF5MA7E7VfoTa4hWqtceV8PQeqzJNarlZyDSaS5BLn1J6G9BYUze-M1xGhATz7F2l-aAt6foi0mwIBlc2fwsdEPuAALZgdG-q_V4gOJW2K0ONnmWhMgMLpCL42cmSb            ... more encrypted text ...            Yxpzp_srpy4LHNdgHqhVBhqtDrjeKJDRfc1yk21P5PpfEBxn5MD4wITAJBgUrDgMCGgUABBQLBpq8y79Pq1TzG1Xf6OAjZzBZaQQUC4kD4CkcrH-WTQhJHud850ddn08CAwGGoA==",
            "encryptedPassword": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiRW1JY1UxOVdueSIsInZlcnNpb24iOiIxMC4xLjEuMCJ9..l6PJ55nSSvKHl0vSWTpkOA.i7hpnnu2yIByhyq_aGBCdaqS3u050yG8eMRGnLRx2Yk.Mo4WSkbbJyLISHq6i4nlVA"
        }
    ]
}
```

You can convert this master key dependent form to:

```shell
{
    "operationType": "SAVE",
    "items": [{
        "password": "2FederateM0re",
        "fileData": "MIIRCQIBAzCCEM8GCSqGSIb3DQEHAaCCEMAEghC8MIIQuDCCC28GCSqGSIb3DQEHBqCCC2AwggtcAgEAMIILVQYJKoZIhvcNAQcBMBwGCiqGSIb3DQEMAQYwDgQIjXWLRGuGNIQCAggAgIILKOgCQ9onDqBPQsshsaS50OjWtj/7s47BUYal1YhO70fBup1a82WGHGhAvb/SY1yOhqQR+TloEBOPI5cExoGN/Gvw2Mw5/wkQZZMSHqxjz68KhN4B0hrsOf4rqShB7jsz9ebSml3r2w0sUZWR73GBtBt1Y3wIlXLS2WtqdtHra9VnUqp1eOk+xenjuWM+u2ndDD43GgKB3n8mNBSSVBqx6ne7aSRJRuAUd+HAzLvSeXjTPMObI1Jod2F+7        ... more base64 encoded exported .p12 ...        5QJ15OJp2iEoVBWxogKf64s2F0iIYPoo6yjNvlidZCevP564FwknWrHoD7R8cIBrhlCJQbEOpOhPg66r4MK1CeJ2poaKRlMS8HGcMRaTpaqD+pIlgmUS6xFw49vr9Kwfb7KteRsTkNR+I8A7HjUpuCMSUwIwYJKoZIhvcNAQkVMRYEFOb7g1xwDka5fJ4sqngEvzTyuWnpMDEwITAJBgUrDgMCGgUABBRlJ+D+FR/vQbaTGbKDFiBK/xDbqQQIAjLc+GgRg44CAggA",
        "id": "sslservercert"
    }],
    "resourceType": "/keyPairs/sslServer"
}
```

The process:

1. You exported the private key+cert of the server cert with alias `sslservercert`. When exported, a password is requested and `2FederateM0re` was used. This action results in the download of a password protected `.p12` file.

2. The data.json key name `encryptedPassword` converted to simply `password`.

3. The value for `fileData` is replaced with a base64 encoded version of the exported `.p12` file.

This process can be used for all encrypted items and environment specific items:

* Key Pairs (.p12)

* Trusted Certs (x509)

* Admin Password

* Data Store Passwords

* Integration Kit Properties

* Hostnames

Leaving these confidential items as unencrypted text in source control is unacceptable. The next logical step is to abstract the unencrypted values and replace them with variables. By doing this, the values can be stored in a secrets management tool (such as Hashicorp Vault) and the variablized file can be in source control.

Converting each of the encrypted keys for their unencrypted counterparts and hostnames with variables is cumbersome and can be automated. As we know in DevOps, if it *can* be automated, it *must* be automated. For more information, see [Using Bulk Config Tool](#devops-using-bulk-config-tool).

A variablized `data.json.subst` is a good candidate for committing to source control after removing any unencrypted text.

#### Using Bulk Config Tool

The [ping-bulkconfig-tool](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/99-helper-scripts/ping-bulkconfigtool) reads your data.json and can optionally:

* Search and replace (e.g. hostnames)

* Clean, add, and remove json members as required.

* Tokenize the configuration and maintain environment variables.

The bulk export tool can process a bulk `data.json` export according to a configuration file with functions above. After running the tool, you are left with a `data.json.subst` and a list of environment variables waiting to be filled.

The `data.json.subst` form of our previous example will look like:

```shell
{
    "operationType": "SAVE",
    "items": [{
        "password": "${keyPairs_sslServer_items_sslservercert_sslservercert_password}",
        "fileData": "${keyPairs_sslServer_items_sslservercert_sslservercert_fileData}",
        "id": "sslservercert"
    }],
    "resourceType": "/keyPairs/sslServer"
}
```

|   |                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The bulk config tool can manipulate data.json but it cannot populate the resulting password or fileData variables because there is no API available on PingFederate to extract these. These variables can be filled using with externally generated certs and keys using tools like openssl, but that is out of scope for this document. |

The resulting `env_vars` file can be used as a guideline for secrets that should be managed externally and only delivered to the container/image as needed for its specific environment.

##### Prerequisites

1. The bulk export utility comes in pre-compiled source code. Build a Docker image by running:

   ```shell
   docker build -t ping-bulkexport-tools:latest .
   ```

2. Copy the [data.json](#devops-steps) to: `pingidentity-devops-getting-started/99-helper-scripts/ping-bulkconfigtool/shared/data.json`

##### Example

A sample command of the ping-bulkconfig-tool

```shell
docker run --rm -v $PWD/shared:/shared ping-bulkexport-tools:latest /shared/pf-config.json /shared/data.json /shared/env_vars /shared/data.json.subst > ./shared/convert.log
```

Where:

* `-v $PWD/shared:/shared` - bind mounts `ping-bulkconfigtool/shared` folder to /shared in the container

* `/shared/pf-config.json` - input path to [config file](#devops-configure-bulk-tool) which defines how to process the bulk export `data.json` file from PingFederate.

* `/shared/data.json` - input path to data.json result of /pf-admin-api/v1/bulk/export PingFederate API endpoint.

* `/shared/env_vars` - output path to store environment variables generated from processing

* `/shared/data.json.subst` - output path to processed data.json

After running the above command, you will see `env_vars` and `data.json.subst` in the `ping-bulkconfigtool/shared` folder.

##### Configure Bulk Tool

Instructions to the bulk config tool are sent by the `pf-config.json` file.

When using the `pf-config.json` file, any unused functions will require an empty array in the file. For example, notice the **add-config** block at the top of this sample:

```shell
{
  "add-config":[],
  "config-aliases":[
  ],
  "expose-parameters":[
  ]
  ,
  "remove-config":[
    {
    "key": "id",
    "value": "ProvisionerDS"
    }
  ]
}
```

In this file, available commands include:

search-replace - A utility to search and replace string values in a bulk config json file. - Can expose environment variables.

Example: replacing an expected base hostname with a substitution:

```shell
  "search-replace":[
    {
      "search": "data-holder.local",
      "replace": "${BASE_HOSTNAME}",
      "apply-env-file": false
    }
  ]
```

##### change-value

* Searches for elements with a matching identifier, and updates a parameter with a new value.

Example: update keyPairId against an element with name=ENGINE:

```shell
  "change-value":[
    {
          "matching-identifier":
          {
            "id-name": "name",
            "id-value": "ENGINE"
          },
      "parameter-name": "keyPairId",
      "new-value": 8
    }
  ]
```

##### remove-config

* Remove configuration objects from the bulk export

Example:

```shell
  "remove-config":[
    {
      "key": "id",
      "value": "ProvisionerDS"
    }
  ]
```

Example:

```shell
  "remove-config":[
    {
      "key": "resourceType",
      "value": "/idp/spConnections"
    }
  ]
```

This tool works with both PingFederate and PingAccess. This example adds the CONFIG QUERY http listener in PingAccess:

```shell
  "add-config":[
      {
        "resourceType": "httpsListeners",
        "item":
            {
                "id": 4,
                "name": "CONFIG QUERY",
                "keyPairId": 5,
                "useServerCipherSuiteOrder": true,
                "restartRequired": false
            }
      }
  ]
```

Example: Add an SP connection:

```shell
  "add-config":[
      {
        "resourceType": "/idp/spConnections",
        "item":
        {
                    "name": "httpbin3.org",
                    "active": false,
            ...
        }
      }
  ]
```

###### expose-parameters

* Navigates through the JSON and exchanges values for substitions.

* Exposed substition names will be automatically created based on the json path.

  * E.g. ${oauth\_clients\_items\_clientAuth\_testclient\_secret}

* Can convert encrypted/obfuscated values into clear text inputs (e.g. "encryptedValue" to "value") prior to substituting it. Doing so enables the injection of values in their raw form.

Example: replace the "encryptedPassword" member with a substitution-enabled "password" member for any elements with "id" or "username" members. The following will remove "encryptedPassword" and create "password":

```shell
    {
      "parameter-name": "encryptedPassword",
      "replace-name": "password",
      "unique-identifiers": [
          "id",
          "username"
      ]
    }
```

###### config-aliases

* The bulk config tool generates substitution names. However, there might be times you wish to simplify them or reuse existing environment variables.

Example: Rename the Administrator's substitution name using the PING\_IDENTITY\_PASSWORD environment variable:

```shell
  "config-aliases":[
    {
      "config-names":[
        "administrativeAccounts_items_Administrator_password"
      ],
      "replace-name": "PING_IDENTITY_PASSWORD",
      "is-apply-envfile": false
    }
  ]
```

###### sort-arrays

* Configure the array members that need to be sorted. This function ensures the array is created consistently, simplifying git diff analysis.

Example: Sort the roles and scopes arrays:

```shell
 "sort-arrays":[
        "roles","scopes"
  ]
```

#### Additional Notes

* The bulk API export is intended to be used as a *bulk* import. The `/bulk/import` endpoint is destructive and overwrites the entire current admin config.

* If you are in a clustered environment, the PingFederate image imports the `data.json` and replicates the configuration to engines in the cluster.

* Your data.json.subst `"metadata": {"pfVersion": "10.1.2.0"}` should match the PingFederate profile version.

## The Configuration Archive Profiles Method

### About configuration archive-based profiles

You should weigh the pros and cons of configuration archive-based profiles compared to bulk API export profiles. While not fully aligning with pur DevOps principles, many users prefer using bulk API export profiles in most scenarios.

Pros: \* The `/data` folder, as opposed to a `data.json` file, is better for [profile layering](profilesLayered.html). \* Configuration is available on engines at startup, which: \* lowers dependency on the admin at initial cluster startup

Cons:

* The `/data` folder contains key pairs in a `.jks` file , which makes externally managing keys very difficult.

* Encrypted data is scattered throughout the folder, creating a dependency on the master encryption key.

#### About this method

You will:

1. Export a `data.zip` archive

2. Optionally, variablize

3. Replace the data folder

### Installing PingFederate Integration Kits

By default, PingFederate is shipped with a handful of integration kits and adapters. If you need other integration kits or adapters in the deployment, manually download them and place them inside the `server/default/deploy` directory of the server profile. You can find these resources in the product download page [here](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

---

---
title: Adding a Message of the Day (MOTD)
description: Create and test a message-of-the-day JSON file that displays custom messages when Ping Identity product containers start
component: devops
page_id: devops::how-to/addMOTD
canonical_url: https://developer.pingidentity.com/devops/how-to/addMOTD.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-before-you-begin: Before you begin
  devops-using-a-motd-file: Using a MOTD file
  devops-testing-the-motd-file: Testing the MOTD file
  devops-example-motd-json: Example motd.json
---

# Adding a Message of the Day (MOTD)

You can create a message of the day (MOTD) JSON file to be provide an MOTD file to our product containers when they start.

## Before you begin

You must:

* Complete the [Get Started](../get-started/introduction.html) example to set up your DevOps environment and run a test deployment of the products.

### Using a MOTD file

To employ a MOTD file:

1. Edit the existing `motd.json` file:

   1. Edit the motd/motd.json file located in your local `pingidentity-devops-getting-started/motd` folder.

2. Create a `motd.json` file in the location of your server profile:

   1. Create a `motd.json` file in the root of the server profile directory being referenced.

   This `motd.json` file will be appended to the `/etc/motd` file used by the provided image.

### Testing the MOTD file

Test the new messages in the `motd.json` file using the `test-motd.sh` script. The script supplies the `JQ_EXPR` value used to pass the message data to the container.

1. To test the `motd.json` file locally for our example use cases, from the `pingidentity-devops-getting-started/motd` directory, enter:

   ```shell
   ./test-motd.sh local
   ```

2. To test the `motd.json` file you created in your server profile directory:

   1. Copy the `test-motd.sh` script located in the `pingidentity-devops-getting-started/motd` directory to your server profile directory.

   2. Enter:

      ```shell
      ./test-motd.sh local
      ```

3. To test the `motd.json` with a server profile located in a Github repository:

   1. Ensure the `test-motd.sh` script is located in the local, cloned repository.

   2. From the local, cloned repository, enter:

      ```shell
      ./test-motd.sh github
      ```

### Example motd.json

The example below shows the messages that are displayed for all product images.

For this example, the messages are only shown from the `validFrom` to `validTo` dates:

```json
{
    "devops" : [
        {
            "validFrom": 20220701,
            "validTo": 20220730,
            "subject": "General Message 1",
            "message": [
                "This is line # 1",
                "",
                "This is line # 3"
            ]
        },
        {
            "validFrom": 20220801,
            "validTo": 20220830,
            "subject": "General Message 2",
            "message": ["Message goes here"]
        }
    ],
    "pingfederate" : [
        {
            "validFrom": 20220701,
            "validTo": 20220830,
            "subject": "PingFederate Message 1",
            "message": ["Message goes here"]
        }
    ]
}
```

---

---
title: Assigning a Provisioner Node ID for PingFederate Pods
description: Explains how to assign a unique PingFederate provisioner node ID per pod using a StatefulSet pod ordinal, for provisioning failover
component: devops
page_id: devops::how-to/assignPFNodeId
canonical_url: https://developer.pingidentity.com/devops/how-to/assignPFNodeId.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Assigning a Provisioner Node ID for PingFederate Pods

The PingFederate provisioner node id is set in the run.properties file used to configure the server. This value is used to set up [failover for provisioning](https://docs.pingidentity.com/pingfederate/latest/server_clustering_guide/pf_deploy_provis_failover.html).

When using failover, each provisioning server must be given a unique index. By default with no server profile, the `PF_PROVISIONER_NODE_ID` environment variable is used to set the node id, with a default value of 1.

If it is necessary to set node ids for PingFederate servers, a StatefulSet can be used to provide consistent hostnames for individual Pods. The node id can then be parsed from these hostnames.

|   |                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The use of a StatefulSet instead of a Deployment for PingFederate has some consequences. In particular, updates to the StatefulSet will be done as a rolling update, which can increase the time needed for an update. |

In the Pod spec for the StatefulSet:

```yaml
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
```

Then, a hook script can be used to parse the pod ordinal, which can then be set as the node id. Note that this will overwrite the default `PF_PROVISIONER_NODE_ID` value.

In your server profile, create a `02-get-remote-server-profiles.sh.post` script to update the environment variable:

```shell
#!/usr/bin/env sh
. "${HOOKS_DIR}/pingcommon.lib.sh"

# Parse the pod ordinal
PF_PROVISIONER_NODE_ID=${POD_NAME##*-}

# Add one to the ordinal so that node id starts at 1 instead of 0
PF_PROVISIONER_NODE_ID=$((PF_PROVISIONER_NODE_ID+1))

# Save the node id to the environment used by the hook scripts
export_container_env PF_PROVISIONER_NODE_ID
```

Ensure your server profile uses this environment variable if you are providing a custom `instance/bin/run.properties.subst` file:

```properties
provisioner.node.id=${PF_PROVISIONER_NODE_ID}
```

---

---
title: Build a Docker Product Image Locally
description: Explains how to build a Ping Identity product Docker image locally using the pingidentity-docker-builds repository and a product zip archive
component: devops
page_id: devops::how-to/buildLocal
canonical_url: https://developer.pingidentity.com/devops/how-to/buildLocal.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-cloning-a-build-repository: Cloning a build repository
  devops-download-a-product-zip-archive: Download a product .zip archive
  devops-build-the-docker-image: Build the Docker image
  devops-re-tagging-the-local-image: Re-tagging the local image
---

# Build a Docker Product Image Locally

This page describes the process to build a Docker image of our products with the build tools found in our [Docker Builds](https://github.com/pingidentity/pingidentity-docker-builds) repository and a local copy of a product .zip archive.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a video demonstration of this process, visit [this link](https://videos.pingidentity.com/detail/videos/devops/video/6313573601112/build-a-product-image). |

[![GitHub Logo](../_images/logos/github.png)](https://github.com/pingidentity/pingidentity-docker-builds)

[Docker Builds](https://github.com/pingidentity/pingidentity-docker-builds)

## Cloning a build repository

Open a terminal and clone the `pingidentity-docker-builds` repo:

```shell
git clone https://github.com/pingidentity/pingidentity-docker-builds.git
```

## Download a product .zip archive

1. Go to [Product Downloads](https://www.pingidentity.com/en/resources/downloads.html) and download the product to be used to build a Docker image.

   |   |                                                                                          |
   | - | ---------------------------------------------------------------------------------------- |
   |   | Ensure you download the product distribution .zip archive and not the Windows installer. |

2. When the download has finished, rename the file to `product.zip`:

   ```shell
   mv pingfederate-11.0.3.zip product.zip
   ```

3. Move `product.zip` to the Build Directory.

   In the `pingidentity-docker-builds` repository directory for each product, move the `product.zip` file to the `<product>/tmp` directory, where /\<product> is the name of one of our available products. For example:

   ```shell
   mv ~/Downloads/product.zip \
      ~/pingidentity/devops/pingidentity-docker-builds/pingfederate/tmp
   ```

## Build the Docker image

Before building the image, display the `versions.json` file in the product directory. You must specify a valid version for the build script. Since the product .zip archive is being provided, it does not matter which version you select as long as it is valid. For example, you can see that `11.0.3` is a valid product version for PingFederate.

```text
{
    "latest": "11.0.3",
    "versions": [
        {
            "version": "11.0.3",
            "preferredShim": "alpine:3.15.4",
            "shims": [
                {
                    "shim": "alpine:3.15.4",
                    "preferredJVM": "al11",
                    "jvms": [
                        {
                            "jvm": "al11",
                            "build": true,
                            "deploy": true,
                            "registries": [
                                "DockerHub",
                                "Artifactory"
                            ]
                        }
                    ]
                },
```

1. Go to the base of the pingidentity-docker-builds repo. For example:

   ```shell
   cd ~/pingidentity/devops/pingidentity-docker-builds
   ```

2. Run the serial\_build.sh script with the appropriate options. For example:

   ```shell
   ./ci_scripts/serial_build.sh \
       -p pingfederate \
       -v 11.0.3 \
       -s alpine:3.15.4 \
       -j al11
   ```

   When the build is completed, the product and base images are displayed. For example:

   ```shell
   REPOSITORY                     TAG                                                       IMAGE ID       CREATED              SIZE
   pingidentity/pingfederate      11.0.3-fsoverride-alpine_3.15.4-al11-master-f1ba-x86_64   404a2b14df0c   7 seconds ago        759MB
   pingidentity/pingbase          master-f1ba-x86_64                                        eb7648692b55   About a minute ago   0B
   pingidentity/pingjvm           al11-alpine_3.15.4-master-f1ba-x86_64                     af0e87d8fafd   About a minute ago   108MB
   pingidentity/pingcommon        master-f1ba-x86_64                                        2e82b239e9bb   About a minute ago   997kB
   pingidentity/pingdatacommon    master-f1ba-x86_64                                        13f35b12a918   About a minute ago   1.11MB
   ```

   Our Docker images are built using common foundational layers required by the product layer such as the Java virtual machine (JVM), pingcommon, and pingdatacommon.

   As it is unlikely you will have the foundational layers on your local system, build the first time using the serial\_build.sh script. This script will create the foundational images, and if you want to use the same foundational layers for other builds, you need only run the build\_product.sh script to build the product layer.

   You must specify the appropriate options when you run serial\_build.sh. For PingFederate, the options might look like this:

   * -p (Product): pingfederate

   * -v (Version): 11.0.3

     * NOTE: this is the version retrieved from the versions.json file

   * -s (Shim): alpine

   * -j (Java): al11

|   |                                                                                   |
| - | --------------------------------------------------------------------------------- |
|   | It is important to build from the base of the repository as shown in the example. |

## Re-tagging the local image

To change the tag of the created image and push it to your own Docker registry, use the `docker tag` command:

```shell
docker tag [image id] \
  [Docker Registry]/[Organization]/[Image Name]:[tag]
```

For example:

```shell
docker tag 404a2b14df0c \
  gcp.io/pingidentity/pingfederate:localbuild
# Display new tag
docker image ls
# Output snippet
pingidentity/pingfederate            11.0.3-fsoverride-alpine_3.15.4-al11-master-f1ba-x86_64   404a2b14df0c   4 minutes ago   759MB
gcp.io/pingidentity/pingfederate     localbuild
```

---

---
title: Building a profile from Your Current Deployment
description: Explains how to generate a PingDirectory server profile from a running instance using the manage-profile generate-profile command
component: devops
page_id: devops::how-to/buildPingDirectoryProfile
canonical_url: https://developer.pingidentity.com/devops/how-to/buildPingDirectoryProfile.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-before-you-begin: Before you begin
  devops-start-building: Start Building
  devops-generating-a-profile: Generating a profile
  devops-extracting-the-generated-profile: Extracting the generated profile
  devops-storing-a-profile: Storing a profile
  devops-including-other-files: Including other files
  devops-profile-structure: Profile structure
---

# Building a profile from Your Current Deployment

PingDirectory is built for [GitOps](https://www.gitops.tech/) through [native tools for building profiles](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_server_profiles.html). To find the latest tools and profiles, search for "DevOps" in PingDirectory Docs. You can find details of the server profile structure there.

A well-formed PingDirectory profile includes all the configuration details needed for starting up a server in a **new** or **existing** replication topology as a representation of what is actually running.

Use this guide to build a PingDirectory profile from a running instance.

## Before you begin

You must:

* Complete [Get Started](../get-started/introduction.html)

* Have a running PingDirectory instance of 8.0.0.0 or later with shell access on the machine or in the container

* Understand [Product Container Anatomy](containerAnatomy.html)

You should:

* Review [Customizing Server Profiles](profiles.html)

### Start Building

#### Generating a profile

To generate a profile, run `manage-profile generate-profile`.

This can be called on a running container in Kubernetes like so:

```shell
kubectl exec -it <pod-name> \
  -- manage-profile generate-profile \
  --profileRoot /tmp/pd.profile

kubectl exec -it pingdirectory-0 \
  -- manage-profile generate-profile \
  --profileRoot /tmp/pd.profile
```

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although you don't have to name your profile `pd.profile`, the default location (the variable `PD_PROFILE`) that PingDirectory looks at is `PD_PROFILE="/opt/staging/pd.profile"`. |

Sample Output:

```text
Defaulted container "pingdirectory" out of: pingdirectory, telegraf, vault-agent-init (init)
Generating server profile

...

Variables such as PING_INSTANCE_NAME in setup-arguments.txt and in any other
files in the profile will need to be provided through environment variables or
through a profile variables file when using the generated profile with the
manage-profile tool. The PING_SERVER_ROOT and PING_PROFILE_ROOT variables are
provided by manage-profile

Some changes may need to be made to the generated profile. Any desired LDIF
files will need to be added to the profile. Any additional server root files,
server SDK extensions, and dsconfig commands can be manually added, and
variables-ignore.txt can be updated to ignore certain files during variable
substitution. See the README file at /tmp/pd.profile/misc-files/README for
more information on the manual steps that must be taken for the generated
profile to be used with the manage-profile tool

The following files and directories in the server root were excluded from the
generated profile, and can be manually added if necessary. These files can
also be included by generate-profile with the --includePath argument:
config/truststore
config/ads-truststore
config/encryption-settings.pin
config/tools.properties.orig
config/encryption-settings/encryption-settings-db
config/keystore.p12
config/tools.properties
config/encryption-settings/encryption-settings-db.old
config/keystore.pin
config/keystore
config/ads-truststore.pin
config/truststore.p12
config/truststore.pin

The generated profile can be found at /tmp/pd.profile
```

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `manage-profile generate-profile` command outputs valuable information about what is and isn't included in the generated profile. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Secrets should *\*not\** be included in your profile, so they are not included in the profile generation by default. However, if you have not already added encryption secrets or keystores to your environment, you can use the `--includePath` argument to collect items from the running server. These items should then be provided to the server on its next restart through some secrets management tool. |

#### Extracting the generated profile

Following the Kubernetes example, you can copy out the generated profile with:

```shell
kubectl cp pingdirectory-0:/tmp/pd.profile pd.profile
```

Sample output:

```shell
% tree
.
└── pd.profile
    ├── dsconfig
    │  └── 00-config.dsconfig
    ├── ldif
    │  └── userRoot
    ├── misc-files
    │  └── README
    ├── server-root
    │  ├── post-setup
    │  └── pre-setup
    │      ├── PingDirectory.lic
    │      ├── README.md
    │      └── config
    │          ├── encryption-settings.pin ## Added via --includePath
    │          ├── keystore.pin ## Added via --includePath
    │          └── schema
    │              ├── 80-format-counter-metrics.ldif
    │              ├── 87-local-identities.ldif
    │              ├── 88-grants.ldif
    │              ├── 89-sessions.ldif
    │              └── 90-oauth-clients.ldif
    ├── server-sdk-extensions
    ├── setup-arguments.txt ## REMOVE this
    └── variables-ignore.txt
11 directories, 13 files
```

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | You might notice that userRoot data (i.e. users) isn't included. Profiles should contain *configuration* only, not data. |

#### Storing a profile

To store the profile, at the [root of your profile](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/baseline/pingdirectory):

Choose from:

* For an unmounted profile, add to `pd.profile`.

* For a mounted profile, add to `/opt/in/pd.profile`.

#### Including other files

In addition to what's generated with `manage-profile generate-profile`, you might want to include other files. These files should be siblings to `pd.profile` at the root of the profile.

For an example structure, see [baseline](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/baseline/pingdirectory).

### Profile structure

"A good PingDirectory profile includes all the **configuration** needed for starting up a server in a **new** or **existing** replication topology."

Review the following elements to see what to include in your profile.

**dsconfig commands**

Because this is how the PingDirectory server is configured, dsconfig commands belong in your profile.

* `manage-profile generate-profile` outputs all of the dsconfig commands of a running server into one file: \` 00-config.dsconfig\`.

Keeping dsconfig commands in one file makes sense because they are ingested together but run in order by the server's inherent dependency knowledge of itself. You can work on PingDirectory in a dev environment and make many changes while working toward your desired configuration.

* `generate-profile` exports a representation of your work.

|   |                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You might see multiple files containing dsconfig commands in our profiles, which serves to show logical separation in our demos. Additionally, our demos might be built of multiple layers coming form different repositories so this prevents overwriting. |

**users**

Data is expected to change at runtime, so this information does *not* belong in your profile structure.

There is built-in protection to enforce this. `ldif/userRoot/`** is only imported on `GENESIS` - The first start of the \*first** PingDirectory in a topology.

The exceptions to this rule are ephemeral dev and demo environments. This is why you see user files in our sample profiles. These files are intended for bootstrapping demo and test instances.

If you are in this category and wanted to include users, you could use:

```shell
kubectl exec -it pingdirectory-0 \
  -- export-ldif \
  --backendID userRoot \
  --ldifFile /tmp/userRoot.ldif \
  --doNotEncrypt

kubectl cp pingdirectory-0:/tmp/userRoot.ldif \
  pd.profile/ldif/userRoot/00-users.ldif
```

**schema**

Schema belongs in your profile structure because you might want to manage your schema as code, and `pd.profile/server-root/pre-setup/config/schema` is where to do that.

**java.properties**

The `config/java.properties` file in the server root is used by PingDirectory to manage arguments passed to Java for the server process and for any command-line utilities. If you need to set any custom values in this file, provide the entire file in your server profile at `instance/config/java.properties`. Note that this is outside of the `pd.profile` folder.

**encryption keys, keystores, truststores, and other secrets**

Any and all secrets should be provided by some sort of secrets management (Vault, bitnami sealed secrets, or at least kubernetes secrets), and as such, these do *not* belong in your profile structure.

PingDirectory allows you to define file paths to secrets so they don't need to be in the profile.

---

---
title: Customizing Server Profiles
description: Explains how to customize Ping Identity server profiles by changing environment variables or modifying profiles via a GitHub repository or local directories
component: devops
page_id: devops::how-to/profiles
canonical_url: https://developer.pingidentity.com/devops/how-to/profiles.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-before-you-begin: Before you begin
  devops-about-this-task: About this task
  devops-adding-or-changing-environment-variables: Adding or Changing Environment Variables
  devops-modifying-a-server-profile: Modifying a Server Profile
  devops-using-your-github-repository: Using Your Github Repository
  devops-using-local-directories: Using Local Directories
---

# Customizing Server Profiles

When you deployed the full stack of product containers in [Getting Started](../get-started/introduction.html), you used the server profiles associated with each of our products. In the YAML files, you'll see entries like the following for each product instance:

```yaml
environment:
  - SERVER_PROFILE_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
  - SERVER_PROFILE_PATH=baseline/pingaccess
```

Our [pingidentity-server-profiles](https://github.com/pingidentity/pingidentity-server-profiles) repository, indicated by the `SERVER_PROFILE_URL` environment variable, contains the server profiles we use for our DevOps deployment examples. The `SERVER_PROFILE_PATH` environment variable indicates the location of the product profile data to use. In the previous example, the PingAccess profile data is located in the `baseline/pingaccess` directory.

We use environment variables for certain startup and runtime configuration settings of both standalone and orchestrated deployments. You can find environment variables that are common to all product images in the [PingBase Image Directory](../docker-images/pingbase/README.html). There are also product-specific environment variables. You can find these in the [Docker Image Information](../docker-images/dockerImagesRef.html) for each available product.

## Before you begin

You must:

* Complete [Get Started](../get-started/introduction.html) to set up your DevOps environment and run a test deployment of the products.

* Understand the [Anatomy of the Product Containers](containerAnatomy.html).

### About this task

You will:

* Add or change the environment variables used for any of our server profiles to better fit your purposes.

  You can find these variables in the [Server Profiles Repository](https://github.com/pingidentity/pingidentity-server-profiles) for each product.

  For example, the location for the `env_vars` file for PingAccess is located in the [baseline/pingaccess server profile](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/baseline/pingaccess).

* Modify one of our server profiles to reflect an existing Ping Identity product installation in your organization.

  You can do this by either:

  * Forking our server profiles repository (`https://github.com/pingidentity/pingidentity-server-profiles`) to your Github repository

  * Using local directories

### Adding or Changing Environment Variables

1. Select any environment variables to add from either:

   * The product-specific environment variables in the [Docker Images Information](../docker-images/dockerImagesRef.html)

   * The environment variables common to all of our products in the [PingBase Image Directory](../docker-images/pingbase/README.html)

2. From the `baseline`, `getting-started`, or `simple-sync` directories in the [Server Profiles Repository](https://github.com/pingidentity/pingidentity-server-profiles), select the product whose profile you want to modify.

3. Open the `env_vars` file associated with the product and either:

   * Add any of the environment variables you've selected.

   * Change the existing environment variables to fit your purpose.

### Modifying a Server Profile

You can modify one of our server profiles based on data from your existing Ping Identity product installation.

Modify a server profile by either:

* Using your Github repository

* Using local directories

#### Using Your Github Repository

In this example PingFederate installation, using the Github Repository uses a server profile provided through a Github URL and assigned to the `SERVER_PROFILE_PATH` environment variable, such as `--env SERVER_PROFILE_PATH=getting-started/pingfederate`).

1. Export a [configuration archive](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html) as a \*.zip file from a PingFederate installation to a local directory.

   > Make sure this is *exported* as a .zip rather than compressing it yourself.

2. Sign on to Github and fork <https://github.com/pingidentity/pingidentity-server-profiles> into your own GitHub repository.

3. Open a terminal, create a new directory, and clone your Github repository to a local directory. For example:

   ```shell
   mkdir /tmp/pf_to_docker
   cd /tmp/pf_to_docker
   git clone https://github.com/<github-username>/pingidentity-server-profiles.git
   ```

   Where `<github-username>` is the name you used to sign on to the Github account.

4. Go to the location where you cloned your fork of our `pingidentity-server-profiles` repository, and replace the `/data` directory in `getting-started/pingfederate/instance/server/default` with the `data` directory you exported from your existing PingFederate installation. For example:

   ```shell
   cd pingidentity-server-profiles/getting-started/pingfederate/instance/server/default
   rm -rf data
   unzip -qd data <path_to_your_configuration_archive>/data.zip
   ```

   Where `<path_to_your_configuration_archive>` is the location for your exported PingFederate configuration archive.

   You now have a local server profile based on your existing PingFederate installation.

   |   |                                                                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You should push to GitHub only what's necessary for your customizations. Our Docker images create the `/opt/out` directory using a product's base install and layering a profile (set of files) on top. |

5. Push your changes (your local server profile) to the Github repository where you forked our server profile repository.

   You now have a server profile available through a Github URL.

6. Deploy the PingFederate container.

   |   |                                                                                                                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To save any changes you make after the container is running, add the entry `--volume <local-path>:/opt/out` to the `docker run` command, where `<local-path>` is a directory you haven't already created. For more information, see [Saving Your Changes](saveConfigs.html). |

   As in this example, the environment variables `SERVER_PROFILE_URL` and `SERVER_PROFILE_PATH` direct Docker to use the server profile you've modified and pushed to Github:

   ```shell
   docker run \
     --name pingfederate \
     --publish 9999:9999 \
     --publish 9031:9031 \
     --detach \
     --env SERVER_PROFILE_URL=https://github.com/<your_username>/pingidentity-server-profiles.git \
     --env SERVER_PROFILE_PATH=getting-started/pingfederate \
     --env-file ~/.pingidentity/config \
     pingidentity/pingfederate:edge
   ```

   |   |                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your GitHub server-profile repo is private, use the `username:token` format so the container can access the repository. For example, `https://github.com/<your_username>:<your_access_token>/pingidentity-server-profiles.git`. For more information, see [Using Private GitHub Repositories](privateRepos.html). |

7. To display the logs as the container starts up, enter:

   ```shell
   docker container logs -f pingfederate
   ```

8. In a browser, go to <https://localhost:9999/pingfederate/app> to display the PingFederate console.

#### Using Local Directories

This method is particularly helpful when developing locally and the configuration isn't ready to be distributed (using Github, for example).

We'll use PingFederate as an example. The local directories used by our containers to persist state and data, `/opt/in` and `/opt/out`, will be bound to another local directory and mounted as Docker volumes. This is our infrastructure for modifying the server profile.

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Docker recommends that you never use bind mounts in a production environment. This method is solely for developing server profiles. For more information, see the [Docker Documentation](https://docs.docker.com/storage/volumes/). |

* The `/opt/out` directory

  All configurations and changes during our container runtimes (persisted data) are captured here. For example, the PingFederate image `/opt/out/instance` contains much of the typical PingFederate root directory:

```text
.
├── README.md
├── SNMP
├── bin
├── connection_export_examples
├── etc
├── legal
├── lib
├── log
├── modules
├── sbin
├── sdk
├── server
├── tools
└── work
```

* The `/opt/in` directory

  If a mounted `opt/in` directory exists, our containers reference this directory at startup for any server profile structures or other relevant files. This method is in contrast to a server profile provided using a Github URL assigned to the `SERVER_PROFILE_PATH` environment variable, such as, `--env SERVER_PROFILE_PATH=getting-started/pingfederate`.

  > For the data each product writes to a mounted `/opt/in` directory, see [Server profile structures](../reference/profileStructures.html).

  These directories are useful for building and working with local server-profiles. The `/opt/in` directory is particularly valuable if you don't want your containers to access Github for data (the default for our server profiles).

The following example deployment uses PingFederate.

1. Deploy PingFederate using our sample [getting-started Server Profile](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/getting-started/pingfederate), and mount `/opt/out` to a local directory:

   ```shell
   docker run \
     --name pingfederate \
     --publish 9999:9999 \
     --detach \
     --env SERVER_PROFILE_URL=https://github.com/pingidentity/pingidentity-server-profiles.git \
     --env SERVER_PROFILE_PATH=getting-started/pingfederate \
     --env-file ~/.pingidentity/config \
     --volume /tmp/docker/pf:/opt/out \
     pingidentity/pingfederate:edge
   ```

   > Make sure the local directory (in this case, `/tmp/docker/pf`) isn't already created. Docker needs to create this directory for the mount to `/opt/out`.

2. Go to the mounted local directory (in this case, `/tmp/docker/pf`), then make and save some configuration changes to PingFederate using the management console.

   As you save the changes, you'll be able to see the files in the mounted directory change. For PingFederate, an `instance` directory is created. This is a PingFederate server profile.

3. Stop and remove the container and start a new container, adding another `/tmp/docker/pf` bind mounted volume, this time to `/opt/in`:

   ```shell
   docker container rm pingfederate

   docker run \
     --name pingfederate-local \
     --publish 9999:9999 \
     --detach \
     --volume /tmp/docker/pf:/opt/out \
     --volume /tmp/docker/pf:/opt/in \
     pingidentity/pingfederate:edge
   ```

---

---
title: Enhanced Utility Sidecar Examples
description: Redirects to the DevOps Helm Charts documentation for enhanced utility sidecar examples formerly hosted on this page
component: devops
page_id: devops::how-to/enhanced-sidecar
canonical_url: https://developer.pingidentity.com/devops/how-to/enhanced-sidecar.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Enhanced Utility Sidecar Examples

The enhanced utility sidecar content has moved to the DevOps Helm Charts docs.

Use the current pages here:

* [Enhanced Utility Sidecar Examples](https://developer.pingidentity.com/helm/examples/enhanced-sidecar.html)

* [Helm Chart Examples](https://developer.pingidentity.com/helm/examples/index.html)

If you bookmarked this page, update your links to the Helm docs section.

---

---
title: Environment Substitution
description: Parameterize server profile configuration files with environment variable substitution using the .subst file extension
component: devops
page_id: devops::how-to/profilesSubstitution
canonical_url: https://developer.pingidentity.com/devops/how-to/profilesSubstitution.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-passing-values-to-containers: Passing Values to Containers
  devops-how-it-works: How it Works
---

# Environment Substitution

In a typical environment, a product configuration is moved from server to server. Hostnames, endpoints, DNS information, and more need a way to be easily modified.

By removing literal values and replacing them with environment variables, configurations can be deployed in multiple environments with minimal change.

> When templating profiles with variables that reference other products, use the conventions defined in [PingBase Image Directory](../docker-images/pingbase/README.html).

All of our configuration files can be parameterized by adding variables using the syntax: `${filename.ext}.subst`.

![run.properties.subst](../_images/CONFIG_SUBSTITUTION.png)

## Passing Values to Containers

Within the environment section of your container definition, declare the variable and the value for the product instance.

Values can be defined in many sources, such as inline, env\_vars files, and Kubernetes ConfigMaps.

![docker compose environment variables](../_images/COMPOSE_SUBSTITUTION.png)

### How it Works

1. A container startup is initiated.

2. The configuration pulls a server profile from Git or from a bind mounted `/opt/in` volume.

3. All files with a `.subst` extension are identified.

4. The environment variables in the identified `.subst` files are replaced with the actual environment values.

5. The `.subst` extension is removed from all the identified files.

6. The product instance for the container is started.

![profile start up sequence](../_images/PROFILES_PROCESS.png)

---

---
title: Forwarding Logs
description: Demonstrates forwarding PingFederate and PingAccess logs to Splunk using a Splunk Universal Forwarder sidecar in a Kubernetes deployment
component: devops
page_id: devops::how-to/splunkLogging
canonical_url: https://developer.pingidentity.com/devops/how-to/splunkLogging.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-forwarding-pingfederate-and-pingaccess-logs-to-splunk: Forwarding PingFederate and PingAccess logs to Splunk
  devops-components-used: Components Used
  devops-prerequisites: Prerequisites
  devops-overall-process: Overall Process
  devops-cluster-preparation: Cluster preparation
  devops-splunk-server-deployment: Splunk Server deployment
  devops-configure-splunk: Configure Splunk
  devops-create-an-index: Create an index
  devops-create-an-http-event-collector-hec: Create an HTTP Event Collector (HEC)
  devops-add-the-ping-product-applications-to-splunk: Add the Ping product applications to Splunk
  devops-create-a-configmap: Create a configmap
  devops-deploy-the-ping-stack-with-splunk-uf-as-a-sidecar: Deploy the Ping stack with Splunk UF as a sidecar
  devops-confirm-in-splunk: Confirm in Splunk
  devops-references: References
---

# Forwarding Logs

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

## Forwarding PingFederate and PingAccess logs to Splunk

This page provides an example of how PingFederate and PingAccess logs can be shipped to Splunk. The principle of using a container for a single purpose is followed, and a sidecar for log collection and forwarding is placed in the appropriate Ping product pods.

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a video demonstration of this process, visit [this link](https://videos.pingidentity.com/detail/videos/devops/video/6323662641112/splunk-logging-demonstration). |

|   |                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This guide is for demonstration purposes only, but the principles will apply to a production implementation. In addition, the process for other logging solutions will be similar. |

### Components Used

1. Ping DevOps Helm Chart

2. Ping server-profiles repository

3. Splunk Deployment

4. Splunk Universal Forwarder Docker image

### Prerequisites

* Access to a Kubernetes cluster. For this guide, a local Kubernetes cluster with the nginx-ingress controller and the MetalLB load balancer was used. You might have to adjust how you access the product interface URLs, depending on your environment.

* Helm pingidentity/ping-devops chart >= 0.9.11

### Overall Process

1. Configure the cluster environment

2. Deploy Splunk Enterprise

3. Configure Splunk and generate an HTTP Event Collector (HEC) token

4. Create a configmap with the token for use by the Splunk Universal Forwarder (UF) sidecar

5. Use Helm to deploy PingFederate and PingAccess with the sidecar attached to the engine pods

6. Confirm logs and activity are visible in Splunk

### Cluster preparation

```shell
# Create the namespace
kubectl create ns splunk

# Set the kubectl context to the namespace
kubectl config set-context --current --namespace=splunk

# Confirm
kubectl config view --minify | grep namespace:
```

### Splunk Server deployment

Deploy the Splunk application:

```shell
# Clone the `pingidentity-devops-getting-started` repository to a local directory
git clone \
  https://github.com/pingidentity/pingidentity-devops-getting-started.git

cd pingidentity-devops-getting-started

# Deploy Splunk
# The splunk.yaml file assumes a load balancer is available in the cluster
kubectl apply -f 20-kubernetes/splunk/splunk.yaml

# Determine IP address assigned
# 8000 is HTTP; 8088 is HTTPS
kubectl get svc

NAME     TYPE           CLUSTER-IP     EXTERNAL-IP       PORT(S)
splunk   LoadBalancer   10.105.171.4   192.168.163.172   8000:30416/TCP,8088:30364/TCP,9997:31770/TCP,9990:32292/UDP

# Create corresponding entry in /etc/hosts
# If your cluster has publicly-accessible IPs and DNS support, this step is not necessary
# You would use the DNS entry assigned to the service.
192.168.163.172 splunk.pingdemo.example
```

### Configure Splunk

In this section, you will prepare Splunk for the logs from the products.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In this demo, there is no data persistence for Splunk. If you restart the Splunk pod, you will lose everything that is configured in the following steps. |

* Navigate to the UI in a browser at `http://splunk.pingdemo.example:8000/en-US/account`.

* Login with the credentials **admin / 2FederateM0re!**

#### Create an index

* Navigate to **Settings > Indexes** and click the **New Index** button at the upper-right.

* Provide **pinglogs** as the Index Name.

* Accept all defaults and click **Save**.

#### Create an HTTP Event Collector (HEC)

* Navigate to **Settings > Data inputs** and click Add New in the HTTP Event Collector row.

* A wizard is launched and you are taken to the **Select Source** step. Type `pinglogs` as the name and click the **Next** button in the upper panel.

* In the **Input Settings** step, add the `pinglogs` index to the **Selected item(s)** box by clicking on it in the **Available item(s)** list, then click the **Review** button in the upper panel.

* Confirm your entries and click the **Submit** button in the upper panel.

* A token is generated. Save this token to a scratch file or buffer for use in configuring Splunk in a moment.

#### Add the Ping product applications to Splunk

* Navigate to **Apps > Find More Apps**. The Apps link is at the upper-left of the UI.

* Filter the list of applications using `Ping`. Add the **PingFederate** and **PingAccess** Apps for Splunk.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | You will need valid credentials from Splunk to install the applications. You can use a free trial if necessary. |

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While not shown in this example, Ping also provides a Splunk App for PingDirectory. You would need to attach the Splunk UF sidecar to your PingDirectory pods as done here for PingFederate and PingAccess. |

#### Create a configmap

Use the HEC token generated earlier to update the file `20-kubernetes/splunk/splunk-config-init.yaml` (search for **#CHANGEME**).

Apply the file:

```shell
kubectl apply -f 20-kubernetes/splunk/splunk-config-init.yaml
```

### Deploy the Ping stack with Splunk UF as a sidecar

```shell
# Create the DevOps secret for temporary Ping license
kubectl create secret generic devops-secret \
  --from-literal=PING_IDENTITY_DEVOPS_USER="$PING_IDENTITY_DEVOPS_USER" \
  --from-literal=PING_IDENTITY_DEVOPS_KEY="$PING_IDENTITY_DEVOPS_KEY" \
  --from-literal=PING_IDENTITY_ACCEPT_EULA="$PING_IDENTITY_ACCEPT_EULA" \
  --type=Opaque \
  --dry-run=client -o yaml | kubectl apply -f -

# Install Ping and Ingress
helm upgrade --install myping pingidentity/ping-devops -f 20-kubernetes/splunk/values.yaml -f 30-helm/ingress-demo.yaml
```

This command deploys PingDirectory, PingFederate, and PingAccess with:

* Baseline Server Profiles

* Splunk Logs Profile layer for the PingAccess and PingFederate engine pods

* Splunk UF sidecar for the PingAccess and PingFederate engine pods

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `values.yaml` file in this guide uses a directory in the [Ping server profiles repository](https://github.com/pingidentity/pingidentity-server-profiles). That profile folder has log4j configuration files that format the logs from the PingAccess and PingFederate product containers for use in Splunk. These files are also in the [backing repository for this portal](https://github.com/pingidentity/pingidentity-devops-getting-started) under the `20-kubernetes/splunk/pingaccess` and `20-kubernetes/splunk/pingfederate` directories, respectively. |

### Confirm in Splunk

Eventually you should see product logs in Splunk by searching: `index="main"`. The first logs will appear when the PingFederate engine has launched fully.

![Splunk logs](../_images/splunkLogs.png)

To see the Splunk App dashboards in operation, generate some traffic in the products to populate them. For example, for PingAccess, you can access <https://myping-pingaccess-engine.pingdemo.example/anything>, which will be rejected, but you will see the activity populated. Also, you can login to the administrative console at <http://myping-pingaccess-admin.pingdemo.example> with the credentials **administrator / 2FederateM0re**.

![Splunk PA Dashboard](../_images/splunkPA.png)

### References

This list includes some of the references used in the creation of this document:

* [PingFederate Logs formatting for Splunk](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_writin_audit_log_splunk.html)

* [PingFederate Dashboard reference](https://docs.pingidentity.com/pingfederate/latest/pingfederate_monitoring_guide/pf_splunk_dashboard_audit_log.html)

* [Splunk Universal Forwarder (SUF) in Kubernetes](https://computingforgeeks.com/send-logs-to-splunk-using-splunk-forwarder/)

* [Splunk configuration for inputs via HTTP](https://faun.pub/logging-in-kubernetes-using-splunk-c2785948fdc0)

---

---
title: Including Extensions in PingData Server Profiles
description: Explains how to include PingData Server SDK extension zip files in a server profile directly or by pulling them from a remote URL
component: devops
page_id: devops::how-to/profilesPingDataExtensions
canonical_url: https://developer.pingidentity.com/devops/how-to/profilesPingDataExtensions.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-the-pd-profileserver-sdk-extensions-directory: The pd.profile/server-sdk-extensions/ directory
  devops-pulling-extension-zip-files-from-an-external-url: Pulling extension zip files from an external URL
---

# Including Extensions in PingData Server Profiles

Server SDK extension zip files can be included in your server profile for PingData products (PingAuthorize, PingDataSync, PingDirectory, and PingDirectoryProxy). The zip files can be included directly, or can be pulled from a remote URL when the container starts up.

## The pd.profile/server-sdk-extensions/ directory

Any desired extension zip files should be included in the pd.profile/server-sdk-extensions/ directory of your server profile. Extension zip files in this directory will be installed during the setup process.

## Pulling extension zip files from an external URL

The hook scripts support pulling down extension zip files from a defined URL, to avoid having to commit zip archives to a Git repository. To do this, a `remote.list` file should be included in the extensions/ directory of your server profile. Any file with a name ending in `remote.list` in the extensions/ directory will be treated as a list of extensions.

|   |                                               |
| - | --------------------------------------------- |
|   | **Ensure extensions are in the right folder** |

When listing extensions to pull down via curl, the list must be placed in the `extensions/` directory of the server profile. When directly including extension zip files, the zip files must be placed in the `pd.profile/server-sdk-extensions/` directory of the server profile.

For an example, see the extension list included in our [baseline PingDirectory server profile](https://github.com/pingidentity/pingidentity-server-profiles/blob/master/baseline/pingdirectory/extensions/baseline.remote.list).

Separate multiple extensions with line breaks.

A URL can also be specified in the downloaded zip file. To do this, add a space between the extension zip URL and the URL that will provide the SHA1 hash. For example:

```shell
https://example.com/extension.zip https://example.com/extension/sha1
```

Set the `ENABLE_INSECURE_REMOTE_EXTENSIONS` environment variable to `true` to allow installing extensions without the SHA1 hash check. By default the SHA1 check will be required. If a SHA1 URL is provided and the SHA does not match or the URL cannot be reached, the extension will not be installed.

---

---
title: Layering Server Profiles
description: Build a layered PingFederate server profile that combines license, extension, and base configuration layers using SERVER_PROFILE_PARENT variables
component: devops
page_id: devops::how-to/profilesLayered
canonical_url: https://developer.pingidentity.com/devops/how-to/profilesLayered.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-before-you-begin: Before you begin
  devops-about-this-task: About this task
  devops-creating-a-layered-server-profile: Creating a layered server profile
  devops-creating-the-base-directories: Creating the base directories
  devops-constructing-the-license-layer: Constructing the license layer
  devops-building-the-extensions-layer: Building the extensions layer
  devops-assigning-environment-variables: Assigning environment variables
  devops-deploying-the-layered-profile: Deploying the layered profile
---

# Layering Server Profiles

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

One of the benefits of our Docker images is the ability to layer product configuration. By using small, discrete portions of your configuration, you can build and assemble a server profile based on multiple installations of a product.

A typical organization can have multiple installations of our products, each using different configurations. By layering the server profiles, you can reuse the configurations that are common across environments, leading to fewer configurations to manage.

You can have as many layers as needed. Each layer of the configuration is *copied* on top of the container's filesystem (not merged).

|   |                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------ |
|   | The profile layers are applied starting at the top layer and ending at the base layer. This ordering might not be apparent at first. |

## Before you begin

You must:

* Complete [Get Started](../get-started/introduction.html) to set up your DevOps environment and run a test deployment of the products.

### About this task

You will:

* Create a layered server profile.

* Assign the environment variables for the deployment.

* Deploy the layered server profile.

### Creating a layered server profile

For this guide, PingFederate is used along with the server profile located in the [pingidentity-server-profiles](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/getting-started/pingfederate) repository. You should fork this repository to your Github repository, then pull your Github repository to a local directory. After you have finished creating the layered profile, you can push your updates to your Github repository and reference it as an environment variable to run the deployment.

You will create separate layers for:

* Product license

* Extensions (such as, Integration Kits and Connectors)

For this example, these layers will be applied on top of the PingFederate server profile. However, you can span configurations across multiple repositories if you want.

You can find the complete working, layered server profile of the PingFederate example from this guide in the [pingidentity-server-profiles/layered-profiles](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/layered-profiles) directory.

Because PingFederate's configuration is file-based, the layering works by copying configurations on top of the PingFederate container's file system.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | Files are copied, not merged. It's best practice to only layer items that won't be impacted by other configuration files. |

#### Creating the base directories

Create a working directory named `layered_profiles` and within that directory create `license` and `extensions` directories. When completed, your directory structure should be:

```text
└── layered_profiles
   ├── extensions
   └── license
```

#### Constructing the license layer

1. Go to the `license` directory and create a `pingfederate` subdirectory.

2. Create the PingFederate license file directory path under the `pingfederate` directory.

   The PingFederate license file resides in the `/instance/server/default/conf/` path.

   ```shell
   mkdir -p instance/server/default/conf/
   ```

   Your license profile path should look like this:

   ```text
   └── license
      └── pingfederate
         └── instance
            └── server
                  └── default
                     └── conf
                        └── pingfederate.lic
   ```

3. Copy your `pingfederate.lic` file to `license/pingfederate/instance/server/default/conf`.

   Using the DevOps evaluation license, when the PingFederate container is running, you can find the license in the container file system `/opt/out/instance/server/default/conf` directory.

   You can copy the `pingfederate.lic` file from the Docker file system using the syntax: `docker cp <container> <source-location> <target-location>`

   For example:

   ```shell
   docker cp \
     pingfederate \
     /opt/in/instance/server/default/conf/pingfederate.lic \
     ${HOME}/projects/devops/layered_profiles/license/pingfederate/instance/server/default/conf
   ```

   Using the `pingctl` tool (update product and version accordingly):

   ```shell
   sh pingctl license pingfederate 11.1 > \
     ${HOME}/projects/devops/layered_profiles/license/pingfederate/instance/server/default/conf
   ```

#### Building the extensions layer

1. Go to the `layered-profiles/extensions` directory and create a `pingfederate` subdirectory.

2. Create the PingFederate extensions directory path under the `pingfederate` directory.

   The PingFederate extensions reside in the `/instance/server/default/deploy` directory path.

   ```shell
   mkdir -p instance/server/default/deploy
   ```

3. Copy the extensions you want to be available to PingFederate to the `layered-profiles/extensions/pingfederate/instance/server/default/deploy` directory .

   The extensions profile path should look similar to the following (extensions will vary based on your requirements):

   ```text
   └── extensions
      └── pingfederate
         └── instance
               └── server
                  └── default
                     └── deploy
                           ├── pf-aws-quickconnection-2.0.jar
                           ├── pf-azure-ad-pcv-1.2.jar
                           └── pf-slack-quickconnection-3.0.jar
   ```

### Assigning environment variables

Although this deployment assigns the environment variables for use in a Docker Compose YAML file, you can use the following technique with any Docker or Kubernetes deployment.

If you want to use your own Github repository for the deployment in the following examples, replace:

```shell
SERVER_PROFILE_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
```

with:

```shell
SERVER_PROFILE_URL=https://github.com/<your-username>/pingidentity-server-profiles.git
```

!!! note "Private Github Repo" If your GitHub server-profile repo is private, use the `username:token` format so the container can access the repository. For example, `https://github.com/<your_username>:<your_access_token>/pingidentity-server-profiles.git`. For more information, see [Using Private Github Repositories](privateRepos.html).

1. Create a new `docker-compose.yaml` file.

2. Add your license profile to the YAML file.

   For example:

   ```yaml
   - SERVER_PROFILE_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
   - SERVER_PROFILE_PATH=layered-profiles/license/pingfederate
   ```

   > `SERVER_PROFILE` supports `URL`, `PATH`, `BRANCH` and `PARENT` variables.

3. Using `SERVER_PROFILE_PARENT`, instruct the container to retrieve its parent configuration by specifying the `extensions` profile as the parent:

   ```yaml
   - SERVER_PROFILE_PARENT=EXTENSIONS
   ```

   `SERVER_PROFILE` can be extended to reference additional profiles. Because we specified the license profile's parent as `EXTENSIONS`, we can extend `SERVER_PROFILE` by referencing the `EXTENSIONS` profile (prior to the `URL` and `PATH` variables):

   ```yaml
   - SERVER_PROFILE_EXTENSIONS_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
   - SERVER_PROFILE_EXTENSIONS_PATH=layered-profiles/extensions/pingfederate
   ```

4. Set `GETTING_STARTED` as the `EXTENSIONS` parent and declare the `URL` and `PATH`:

   ```yaml
   - SERVER_PROFILE_EXTENSIONS_PARENT=GETTING_STARTED
   - SERVER_PROFILE_GETTING_STARTED_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
   - SERVER_PROFILE_GETTING_STARTED_PATH=getting-started/pingfederate
   ```

   > Because the `GETTING_STARTED` profile is the last profile to add, it will not have a parent.

   Your `environment` section of the `docker-compose.yaml` file should look similar to this:

   ```shell
   environment:# **** SERVER PROFILES BEGIN ****
   # Server Profile - Product License
   - SERVER_PROFILE_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
   - SERVER_PROFILE_PATH=layered-profiles/license/pingfederate
   - SERVER_PROFILE_PARENT=EXTENSIONS
   # Server Profile - Extensions
   - SERVER_PROFILE_EXTENSIONS_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
   - SERVER_PROFILE_EXTENSIONS_PATH=layered-profiles/extensions/pingfederate
   - SERVER_PROFILE_EXTENSIONS_PARENT=GETTING_STARTED
   # Base Server Profile
   - SERVER_PROFILE_GETTING_STARTED_URL=https://github.com/pingidentity/pingidentity-server-profiles.git
   - SERVER_PROFILE_GETTING_STARTED_PATH=getting-started/pingfederate
   # **** SERVER PROFILE END ****
   ```

### Deploying the layered profile

1. Push your profiles and updated `docker-compose.yaml` file to your GitHub repository.

2. Deploy the stack with the layered profiles.

To view this example in its entirety, including the profile layers and `docker-compose.yaml` file, see the [pingidentity-server-profiles/layered-profiles](https://github.com/pingidentity/pingidentity-server-profiles/tree/master/layered-profiles) directory.

---

---
title: Managing Deployments
description: Overview of maintaining Ping Identity DevOps deployments over time, including applying new product versions and retuning configurations
component: devops
page_id: devops::how-to/manage
canonical_url: https://developer.pingidentity.com/devops/how-to/manage.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Managing Deployments

In addition to [Customizing Deployments](../reference/config.html), you must maintain your deployments over time as new versions of our products are released and as you tune your deployments to better reflect your changing needs.

---

---
title: Migrating from privileged images to unprivileged-by-default images
description: Covers tips for migrating from privileged (root) Ping Identity product images to unprivileged-by-default images, including port and volume changes
component: devops
page_id: devops::how-to/migratingRootToUnprivileged
canonical_url: https://developer.pingidentity.com/devops/how-to/migratingRootToUnprivileged.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-checklist-before-migration: Checklist before migration
  devops-potential-issues: Potential issues
  persistent-volumes: Persistent volumes
  devops-default-ports: Default ports
  devops-running-as-root-with-the-unprivileged-by-default-images: Running as root with the unprivileged-by-default images
---

# Migrating from privileged images to unprivileged-by-default images

In the [2103 release](https://devops.pingidentity.com/release-notes/relnotes-2103/), our product images were updated to run with an unprivileged user by default. Before this release, images ran as root by default. This document describes some important tips when moving from privileged to unprivileged images.

## Checklist before migration

* To ensure that any configuration of the pods is maintained, build and commit a server profile from your current workload into a git repository.

  * See the [Server Profile Structures](https://devops.pingidentity.com/reference/profileStructures/) page, and/or the product-specific guides for [PingFederate](https://devops.pingidentity.com/how-to/buildPingFederateProfile/) and [PingDirectory](https://devops.pingidentity.com/how-to/buildPingDirectoryProfile/).

* For PingDirectory, export your user data that will be imported into the new server(s). You can include the basic DIT structure in the server profile (in the `pd.profile/ldif/userRoot/` directory), but actual user data should be left out; the server profile should store configuration, not data. You can save the actual user data elsewhere and manually import it after the new pods have started.

  * You can use the `export-ldif` command to export user data, or you can schedule a task via LDAP. The exported ldif file will be written to the pod filesystem.

  * You can use the `import-ldif` command to import user data, or you can schedule a task via LDAP. For the import to run, the file to be imported must exist on the pod filesystem.

### Potential issues

### Persistent volumes

In Kubernetes, persistent volumes created with our older containers have files owned by the root user. When the default non-privileged user attempts to use these existing volumes, there might be file permission errors.

To avoid this, you can either:

* Create a fresh deployment that doesn't use the old volumes.

* Continue to run the containers as root.

Additionally, the containers using persistent volume claims need to set the securityContext `fsGroup` to a value allowing the container can write to the PVCs. An example of setting this value in the statefulSet workload needs to include the following fsGroup setting.

This example uses the same default groupId set by the image. The [Ping Identity Helm Charts](https://helm.pingidentity.com) already provide this setting by default for the containers.

```yaml
spec:
  template:
    spec:
      securityContext:
        fsGroup:9999
```

#### Default ports

In our older images, certain default ports (`LDAP_PORT`, `LDAPS_PORT`, `HTTPS_PORT`, and `JMX_PORT`) were set to privileged values (`389`, `636`, `443`, and `689`, respectively). The newer images don't use these values because they run as a non-privileged user. The updated default ports are `1389`, `1636`, `1443`, and `1689`.

If you need, you can maintain the old values by setting the corresponding environment variables and running the container as root.

For our PingDirectory images, port changes aren't allowed on restart. If you're using a volume from an older image you may encounter an error due to changing port values.

You must either:

* Create a fresh deployment for PingDirectory with the new images and import your data from the old deployment.

* Set the environment variables to match the original privileged values and continue to run the container as root.

### Running as root with the unprivileged-by-default images

To run as root as mentioned in the two previous examples, you must use your container orchestrator:

* For pure Docker, the `-u` flag allows specifying the user the container should use.

* For Docker Compose, you can define a `user:`.

* In Kubernetes, you can set up a security context for the container to specify the user. To run as root, a user and group ID of `0:0` should be used.

---

---
title: Mount Existing Product License
description: Explains how to mount an existing product license file into Ping Identity containers using Docker, Kubernetes secrets, or Helm
component: devops
page_id: devops::how-to/existingLicense
canonical_url: https://developer.pingidentity.com/devops/how-to/existingLicense.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-example-mounts: Example Mounts
  devops-volume-mount-syntax: Volume Mount Syntax
  devops-docker: Docker
  devops-kubernetes: Kubernetes
  devops-helm: Helm
  devops-note-on-updating-the-product-license-when-mounting-it-as-a-file: Note on updating the product license when mounting it as a file
---

# Mount Existing Product License

You can pass the license file to a container via mounting to the container's `/opt/in` directory.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You do not need to do this if you are using your DevOps User/Key. If you have provided license files via the volume mount and a DevOps User/Key, it will ignore the DevOps User/Key. |

The `/opt/in` directory overlays files onto the products runtime filesystem, the license needs to be named correctly and mounted in the exact location the product checks for valid licenses.

## Example Mounts

| Product            | File Name         | Mount Path                                                 |
| ------------------ | ----------------- | ---------------------------------------------------------- |
| PingFederate       | pingfederate.lic  | /opt/in/instance/server/default/conf/pingfederate.lic      |
| PingAccess         | pingaccess.lic    | /opt/in/instance/conf/pingaccess.lic                       |
| PingDirectory      | PingDirectory.lic | /opt/in/pd.profile/server-root/pre-setup/PingDirectory.lic |
| PingDirectoryProxy | PingDirectory.lic | /opt/in/pd.profile/server-root/pre-setup/PingDirectory.lic |
| PingDataSync       | PingDirectory.lic | /opt/in/pd.profile/server-root/pre-setup/PingDirectory.lic |
| PingAuthorize      | PingAuthorize.lic | /opt/in/pd.profile/server-root/pre-setup/PingAuthorize.lic |
| PingAuthorize PAP  | PingAuthorize.lic | /opt/in/pd.profile/server-root/pre-setup/PingAuthorize.lic |
| PingCentral        | pingcentral.lic   | /opt/in/instance/conf/pingcentral.lic                      |

## Volume Mount Syntax

### Docker

Sample docker run command with mounted license:

```shell
docker run \
  --name pingfederate \
  --volume <local/path/to/pingfederate.lic>:/opt/in/instance/server/default/conf/pingfederate.lic \
  pingidentity/pingfederate:edge
```

Sample docker-compose.yaml with mounted license:

```yaml
version: "2.4"
services:
  pingfederate:
    image: pingidentity/pingfederate:edge
    volumes:
      - path/to/pingfederate.lic:/opt/in/instance/server/default/conf/pingfederate.lic
```

### Kubernetes

Create a Kubernetes secret from the license file

```shell
kubectl create secret generic pingfederate-license \
  --from-file=./pingfederate.lic
```

Then mount it to the pod

```yaml
spec:
  containers:
  - name: pingfederate
    image: pingidentity/pingfederate
    volumeMounts:
      - name: pingfederate-license-volume
        mountPath: "/opt/in/instance/server/default/conf/pingfederate.lic"
        subPath: pingfederate.lic
  volumes:
  - name: pingfederate-license-volume
    secret:
      secretName: pingfederate-license
```

### Helm

Create a Kubernetes secret from the license file

```shell
kubectl create secret generic pingfederate-license \
  --from-file=./pingfederate.lic
```

Add the secretVolumes within your values.yaml deployment file

```yaml
pingfederate-admin:
  secretVolumes:
    pingfederate-license:
      items:
        pingfederate.lic: /opt/in/instance/server/default/conf/pingfederate.lic
```

#### Note on updating the product license when mounting it as a file

If you are updating the license file for a product, simply replacing the file on the filesystem may not update the license of the running server.

For PingData products (PingDirectory, PingDataSync, PingAuthorize, and PingDirectoryProxy) the license can be updated by copying the new license to the expected location in the server profile - `pd.profile/server-root/pre-setup`. After doing so, dsconfig can be used to update the license on the running server. Ensure that the updated license file is still present in the server profile on subsequent restarts of the container.

For example, for PingDirectory:

```shell
 dsconfig set-license-prop \
   --set "directory-platform-license-key<input-file.lic"
```

The exact name of the license property in the above example will depend on which PingData product is being used.

For non-PingData products, the license can be updated on the product with the typical method. This process will depend on the product, but will generally be done either through the administrative console or using an API call. See the product documentation for details.

---

---
title: Ping Identity DevOps Registration
description: Register for the Ping Identity DevOps Program to obtain credentials for deploying and evaluating Ping products with trial licenses
component: devops
page_id: devops::how-to/devopsRegistration
canonical_url: https://developer.pingidentity.com/devops/how-to/devopsRegistration.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-ping-identity-devops-registration: Ping Identity DevOps Registration
  devops-saving-your-devops-user-and-key: Saving Your DevOps User and Key
  devops-resending-your-devops-user-and-key: Resending your DevOps User and Key
---

# Ping Identity DevOps Registration

|   |                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `pingctl` utility referenced here has been deprecated and is no longer being maintained. It is recommended to use the [Ping CLI](https://developer.pingidentity.com/pingcli/pingcli_landing_page.html) utility under active development and support.With few exceptions, many `pingctl` commands can be replicated using the `pingcli` utility, with gaps being addressed based on prioritization. |

|   |                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The team responsible for the Ping DevOps program doesn't have access to the user account system on the Ping Identity website. If you have trouble with your account and are unable to follow these instructions to enroll, the issue is likely with your credentials in our system. Please contact your sales representative at [Ping Identity Support](https://support.pingidentity.com/s/). |

## Ping Identity DevOps Registration

Registering for Ping Identity's DevOps Program provides you with credentials that enable you to easily deploy and evaluate Ping Identity products using trial licenses automatically using tools and platforms like Helm or Kubernetes.

To register for the DevOps Program:

* Make sure you have a registered account with Ping Identity. If you're not sure, click the link to [Sign On](https://www.pingidentity.com/en/account/sign-on.html) and follow the instructions to access your account.

  * If you don't have an account, create one [here](https://www.pingidentity.com/en/account/register.html).

  * When signing on, select **Support and Community** in the **Select Account** list.

  * After you're signed on, you're directed to your profile [page](https://support.pingidentity.com/s/).

  * In the right-side menu, click **Register for DevOps Program**.

    ![Register for DevOps](../_images/DEVOPS_REGISTRATION.png)

A confirmation message will be shown and the DevOps credentials will be forwarded to the email address associated with your Ping Identity account.

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | When you receive your key, follow the instructions below for saving them with the `pingctl` utility. |

Example:

* `PING_IDENTITY_DEVOPS_USER=jsmith@example.com`

* `PING_IDENTITY_DEVOPS_KEY=e9bd26ac-17e9-4133-a981-d7a7509314b2`

### Saving Your DevOps User and Key

The recommended way to save your DevOps User/Key is to use the Ping Identity DevOps utility `pingctl`.

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | You can find installation instructions for `pingctl` in the [pingctl Tool](../tools/pingctlUtil.html) document. |

To save your DevOps credentials, run `pingctl config` and supply your credentials when prompted.

When `pingctl` is installed and configured, it places your DEVOPS USER/KEY into a Ping Identity property file found at `~/.pingidentity/config` with the following variable names set (see the following example).

```shell
PING_IDENTITY_DEVOPS_USER=jsmith@example.com
PING_IDENTITY_DEVOPS_KEY=e9bd26ac-17e9-4133-a981-d7a7509314b2
```

After you've configured these settings, you can view them with the `pingctl info` command (credential values are masked by default, use `pingctl info -v` to show unmasked).

### Resending your DevOps User and Key

If you have misplaced or lost your DevOps User/Key, there are two convenient ways to recover it.

* If you have configured `pingctl`, the `PING_IDENTITY_DEVOPS_USER` and `PING_IDENTITY_DEVOPS_KEY` can be printed by entering the following command:

```shell
pingctl info -v
```

* If you did not save the credentials in the `pingctl` tool, you can recover your credentials by logging in to your Ping Identity account.

* Navigate to [Sign On](https://www.pingidentity.com/en/account/sign-on.html) and follow the instructions to access your account.

* When signing on, select **Support and Community** in the **Select Account** list.

* After you're signed on, you're directed to your profile [page](https://support.pingidentity.com/s/).

* In the right-side menu, click **Register for DevOps Program** again. A confirmation message will be shown and the same DevOps credentials will be resent to the email address associated with your Ping Identity account.

---

---
title: PingDirectory Metrics with Prometheus
description: Explains how to enable the PingDirectory Prometheus HTTP servlet extension to expose server metrics using dsconfig commands in a server profile
component: devops
page_id: devops::how-to/prometheus
canonical_url: https://developer.pingidentity.com/devops/how-to/prometheus.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# PingDirectory Metrics with Prometheus

In the past, enabling metrics for PingDirectory required a manual process to setup the **statsd** configuration to enable the data to be made available to Prometheus. However, PingDirectory now includes an HTTP servlet extension that can be enabled to expose metrics in Prometheus format.

You can refer to the [documentation](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_monitor_server_metrics_prometheus.html) for the `dsconfig` commands to enable the Prometheus metrics.

These `dsconfig` commands can be included in a server profile to ensure that the configuration is applied when the server is started. See [here](https://github.com/pingidentity/pingidentity-server-profiles/blob/master/monitoring/pingdirectory/jolokia/pd.profile/dsconfig/15-prometheus.dsconfig) for an example.

---

---
title: Re-encrypting backend data for a set of PingDirectory pods
description: Re-encrypt PingDirectory backend data across a set of pods with a new encryption settings definition in a Kubernetes environment
component: devops
page_id: devops::how-to/reEncryptPingDirectoryData
canonical_url: https://developer.pingidentity.com/devops/how-to/reEncryptPingDirectoryData.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-example-starting-helm-values-using-the-ping-devops-helm-chart: Example starting Helm values using the ping-devops Helm chart
  devops-updating-the-encryption-settings-database-with-the-new-preferred-definition: Updating the encryption settings database with the new preferred definition
  devops-disabling-replication-and-deleting-the-replication-database: Disabling replication and deleting the replication database
  devops-scaling-down-to-one-pod-and-re-importing-the-data: Scaling down to one pod and re-importing the data
  devops-scaling-back-up: Scaling back up
---

# Re-encrypting backend data for a set of PingDirectory pods

PingDirectory uses encryption settings definitions to manage how data is encrypted in the database. When setting a new preferred encryption settings definition, the new definition will be used for all subsequent data encryption, but existing data remains encrypted with an older key.

In many cases this is acceptable, and no additional work needs to be done. However in cases such as when an existing key might have been compromised, you will want to completely transition to using the new definition. This page describes the steps necessary to do this.

For more information on this scenario, refer to the [PingDirectory documentation](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_security_guide/pd_sec_re_encrypt_database.html).

This page will describe how to follow the steps listed on the above page in a Kubernetes environment with several PingDirectory pods.

## Example starting Helm values using the ping-devops Helm chart

For demonstration, we will be using these Helm values with the ping-devops Helm chart:

```yaml
pingdirectory:
  enabled: true
  container:
    replicaCount: 3
  envs:
    SERVER_PROFILE_URL: https://path/to/profile.git
    SERVER_PROFILE_PATH: my-profiles/pingdirectory
    ENCRYPTION_PASSWORD_FILE: /opt/staging/.sec/encryption-passphrase1.txt
```

### Updating the encryption settings database with the new preferred definition

The first step is to update the encryption settings database with your new preferred encryptions settings definition. For details on doing this manually, refer to the [PingDirectory documentation](https://docs.pingidentity.com/pingdirectory/latest/pingdirectory_security_guide/pd_sec_manage_encrypt_settings.html).

If you are using the `ENCRYPTION_PASSWORD_FILE` environment variable to control encryption for your pods, you can simply point that variable to a different file with a new passphrase and restart the pods. After the restart, the pods will use the new definition based on the `ENCRYPTION_PASSWORD_FILE` value. For example, with the environment variable updated:

```yaml
pingdirectory:
  enabled: true
  container:
    replicaCount: 3
  envs:
    SERVER_PROFILE_URL: https://path/to/profile.git
    SERVER_PROFILE_PATH: my-profiles/pingdirectory
    ENCRYPTION_PASSWORD_FILE: /opt/staging/.sec/encryption-passphrase2.txt
```

Whatever method you use to update the encryption settings database, ensure that each pod has the new definition in the encryption settings database before continuing. Use the `encryption-settings` command-line tool to view the contents of the encryption settings database.

### Disabling replication and deleting the replication database

Now replication must be disabled between the pods before the data is exported and re-imported, and the replication database must be deleted to ensure there are no remaining entries encrypted with the old definition.

Exec into one of the pods and use the `dsreplication disable` command to disable replication between each of the servers. Ensure that each server is in its own single-server topology using the `dsreplication status` command.

Run `rm -r /opt/out/instance/changelogDb/` on each of the pods individually, to remove any lingering entries from the replication database that may have been encrypted with the old definition.

### Scaling down to one pod and re-importing the data

The data must now be exported and re-imported with the server offline. To do this, we will scale down to a single pod (however we *do not* need to delete the persistent volumes of the other pods). We will also force the final pod to export and re-import its data so that it is encrypted with the new preferred definition. The `PD_FORCE_DATA_REIMPORT` environment variable can be used to force an export and re-import of the data before the server starts up.

Note that the `PD_FORCE_DATA_REIMPORT` was added in the `2307` docker image release for PingDirectory. Prior to this a custom hook script would be needed to force the data export and re-import.

```yaml
pingdirectory:
  enabled: true
  container:
    replicaCount: 1
  envs:
    SERVER_PROFILE_URL: https://path/to/profile.git
    SERVER_PROFILE_PATH: my-profiles/pingdirectory
    ENCRYPTION_PASSWORD_FILE: /opt/staging/.sec/encryption-passphrase2.txt
    PD_FORCE_DATA_REIMPORT: "true"
```

### Scaling back up

Now we can scale back up to the full number of pods, and stop forcing the data export and re-import. When the removed pods restart, they will rejoin the topology and will initialize their data from the seed pod (pod 0), which will be encrypted with the new preferred definition.

```yaml
pingdirectory:
  enabled: true
  container:
    replicaCount: 3
  envs:
    SERVER_PROFILE_URL: https://path/to/profile.git
    SERVER_PROFILE_PATH: my-profiles/pingdirectory
    ENCRYPTION_PASSWORD_FILE: /opt/staging/.sec/encryption-passphrase2.txt
```

The backend data will now be encrypted with the new preferred definition.

Note that in some cases an encryption settings definition may be used for more than encrypting backend data. For example, files can be encrypted using encryption settings definitions. By default some pin files in the server root will be encrypted if encryption was enabled during the first setup of the server, such as `config/keystore.pin`. If you need to manage how files are encrypted with encryption settings definitions, run `encrypt-file --help` for more information.

---

---
title: S3 Archive of a PingDirectory Backup
description: Configure a sidecar container to back up PingDirectory data and archive it to Amazon S3, and restore from S3 backups
component: devops
page_id: devops::how-to/s3Archive
canonical_url: https://developer.pingidentity.com/devops/how-to/s3Archive.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-before-you-begin: Before you begin
  devops-high-level-backup-steps: High-level backup steps
  devops-file-exploration: File exploration
  devops-dockerfile: Dockerfile
  devops-pd-archive-backup-to-s3-yaml: pd-archive-backup-to-s3.yaml
  devops-backup-operation: Backup Operation
  devops-restore-operation: Restore Operation
---

# S3 Archive of a PingDirectory Backup

|   |                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This guide is for demonstration purposes only and is not intended for production use and is just one of many ways of archiving files to S3. Other storage options might be available, depending on your provider. |

## Before you begin

Prior to attempting these steps, you must:

* Complete the [Getting Started](../get-started/introduction.html) steps to set up your DevOps environment and run a test deployment of the products

* Have some means of authenticating the sidecar container to S3. This authentication can use an IAM role or another method and is left for the user to implement.

### High-level backup steps

* Configure some means of creating a backup of PingDirectory. For this guide, an extension of the [PingDirectory Backup and Sidecar](https://raw.githubusercontent.com/pingidentity/pingidentity-devops-getting-started/master/30-helm/pingdirectory-backup/pingdirectory-periodic-backup.yaml) is used.

* After the backup is made, use an archive script to upload the backup to S3.

* (Optional) Clean up the image filesystem of backups.

### File exploration

In the `30-helm/s3-sidecar` directory of this repository, you will find the following files:

#### Dockerfile

This file extends the PingToolkit image, adding the AWS CLI and a few other utilities for demonstration purposes. You can use any platform that meets your requirements.

```dockerfile
## Dockerfile for AWS CLI
## For demonstration purposes only
## Not intended for production use
FROM pingidentity/pingtoolkit:latest

USER root
# Install AWS CLI
RUN apk add --no-cache \
    aws-cli \
    bash \
    curl \
    less \
    groff \
    shadow \
    sudo \
    unzip

USER 9031:0
```

To build a multi-architecture image, you can use the following command. In order to create an image for a different architecture, you will need to have the `buildx` plugin installed and configured, and the image will have to be pushed at build time:

```shell
docker buildx build --platform linux/arm64,linux/amd64 -t <registry>/<image>:<tag> --push .
```

|   |                                                                   |
| - | ----------------------------------------------------------------- |
|   | Ensure that the registry is accessible to the Kubernetes cluster. |

#### pd-archive-backup-to-s3.yaml

This file will not be repeated in full here. The top section creates ConfigMaps that define four sample scripts:

* **archive.sh** - This demonstration script is called by the *backup.sh* script to archive the backup to S3. The bucket name and path will need to be updated to match your environment.

* **fetch.sh** - This demonstration script is called by the *restore.sh* script to fetch backup files from S3. The bucket name and path will need to be updated to match your environment.

* **backup.sh** - This demonstration script is called by the sidecar container to create a backup of PingDirectory. It then calls the *archive.sh* script (with no error handling or testing).

* **restore.sh** - This demonstration script would be executed either by a job or in the sidecar container to restore a backup of PingDirectory.

These scripts are placed into the sidecar image under the */opt/in* directory.

Lines 222 and 223 will need modification to point to the registry and tag for the image that has the AWS cli installed as in the `buildx` command above.

### Backup Operation

If this demonstration is implemented, the process is straightforward. As per the crontab entry, every 6 hours:

* A backup of the PingDirectory data is created

* The backup is archived to S3

PingDirectory handles the removal of old backups based on the parameters set in the backup script.

If you are observing the cluster at the time the backup takes place, an additional pod launches to execute the cronjob. This pod terminates after the backup is complete.

Over time, the S3 bucket will appear similar to the following screenshot. To create this image, the backup and archive process ran every 2 minutes:

![S3 archive contents](../_images/s3Sample.png)

### Restore Operation

In the event that a restore operation is needed, the **restore.sh** script can be used. This script will:

* Download the backup from S3

* Restore the backup to the PingDirectory data directory

A sample run of the script is shown below:

```shell
PingToolkit:demo-pingdirectory-0:/opt
> /opt/in/restore.sh <admin-password>
download: s3://<bucket-name>/<folder>/userRoot/backup.info to ../tmp/restore/userRoot/backup.info
download: s3://<bucket-name>/<folder>/userRoot/backup.info.save to ../tmp/restore/userRoot/backup.info.save
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421213402Z to ../tmp/restore/userRoot/userRoot-backup-20250421213402Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421213202Z to ../tmp/restore/userRoot/userRoot-backup-20250421213202Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421213002Z to ../tmp/restore/userRoot/userRoot-backup-20250421213002Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421213602Z to ../tmp/restore/userRoot/userRoot-backup-20250421213602Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421213802Z to ../tmp/restore/userRoot/userRoot-backup-20250421213802Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421212802Z to ../tmp/restore/userRoot/userRoot-backup-20250421212802Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421214202Z to ../tmp/restore/userRoot/userRoot-backup-20250421214202Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421214802Z to ../tmp/restore/userRoot/userRoot-backup-20250421214802Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421214402Z to ../tmp/restore/userRoot/userRoot-backup-20250421214402Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421215002Z to ../tmp/restore/userRoot/userRoot-backup-20250421215002Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421214602Z to ../tmp/restore/userRoot/userRoot-backup-20250421214602Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421215202Z to ../tmp/restore/userRoot/userRoot-backup-20250421215202Z
download: s3://<bucket-name>/<folder>/userRoot/userRoot-backup-20250421214002Z to ../tmp/restore/userRoot/userRoot-backup-20250421214002Z
Replication is not enabled
userRoot
Restoring to the latest backups under /tmp/restore
Restore order of backups: /tmp/restore/userRoot

----- Doing a restore from /tmp/restore/userRoot -----
Restore task 2025042121535304 scheduled to start immediately

NOTE:  This tool is running as a task.  Killing or interrupting this tool will not have an impact on the task
If you wish to cancel the running task, that may be accomplished using the command:  manage-tasks --no-prompt --hostname localhost --port 1636 --bindDN "cn=administrator" --bindPassword "********" --cancel "2025042121535304"

[21/Apr/2025:21:53:53 +0000] severity="SEVERE_WARNING" msgCount=0 msgID=1880227932 message="Administrative alert type=backend-disabled id=fc5694f2-7b52-4cf9-8214-89edb41708bb class=com.unboundid.directory.server.core.BackendConfigManager msg='Backend userRoot is disabled'"
[21/Apr/2025:21:53:53 +0000] severity="NOTICE" msgCount=1 msgID=1880555611 message="Administrative alert type=config-change id=71fc9c87-4030-427a-ab9c-cf631157d210 class=com.unboundid.directory.server.admin.util.ConfigAuditLog msg='A configuration change has been made in the Directory Server:  [21/Apr/2025:21:53:53.124 +0000] conn=-4 op=7407 dn='cn=Internal Client,cn=Internal,cn=Root DNs,cn=config' authtype=[Internal] from=internal to=internal command='dsconfig set-backend-prop --backend-name userRoot --set enabled:false''"
[21/Apr/2025:21:53:54 +0000] severity="NOTICE" msgCount=2 msgID=8847445 message="Restored: .environment-open from backup with id '20250421215202Z' (size 76)"
[21/Apr/2025:21:53:54 +0000] severity="NOTICE" msgCount=3 msgID=8847445 message="Restored: 00000000.jdb from backup with id '20250421215202Z' (size 12997816)"
[21/Apr/2025:21:53:54 +0000] severity="NOTICE" msgCount=4 msgID=8847445 message="Restored: esTokenizer.ping from backup with id '20250421215202Z' (size 39)"
[21/Apr/2025:21:53:54 +0000] severity="SEVERE_WARNING" msgCount=5 msgID=1880227932 message="Administrative alert type=je-environment-not-closed-cleanly id=8f35bade-1f67-42ca-a506-79ee377a0ace class=com.unboundid.directory.server.backends.jeb.RootContainer msg='The server has detected that the Berkeley DB JE environment located in directory '/opt/out/instance/db/userRoot' may not have been closed cleanly the last time it was opened (or that the backend has just been restored from a backup taken with the server online).  The database environment may need to replay changes from the end of the transaction log to guarantee the integrity of the data, and in some cases this may take a significant amount of time to complete'"
[21/Apr/2025:21:53:54 +0000] severity="NOTICE" msgCount=6 msgID=8847402 message="The database backend userRoot using Berkeley DB Java Edition 7.5.12 and containing 20008 entries has started"
[21/Apr/2025:21:53:54 +0000] severity="NOTICE" msgCount=7 msgID=1879507338 message="Starting group processing for backend userRoot"
[21/Apr/2025:21:53:54 +0000] severity="NOTICE" msgCount=8 msgID=1879507339 message="Completed group processing for backend userRoot"
[21/Apr/2025:21:53:54 +0000] severity="INFORMATION" msgCount=9 msgID=1891631108 message="Starting access control processing for backend userRoot"
[21/Apr/2025:21:53:54 +0000] severity="INFORMATION" msgCount=10 msgID=12582962 message="Added 2 Access Control Instruction (ACI) attribute types found in context 'dc=example,dc=com' to the access control evaluation engine"
[21/Apr/2025:21:53:54 +0000] severity="NOTICE" msgCount=11 msgID=1880555611 message="Administrative alert type=config-change id=550d224f-f8f9-45f5-ace3-4933ca74a76d class=com.unboundid.directory.server.admin.util.ConfigAuditLog msg='A configuration change has been made in the Directory Server:  [21/Apr/2025:21:53:54.939 +0000] conn=-4 op=7415 dn='cn=Internal Client,cn=Internal,cn=Root DNs,cn=config' authtype=[Internal] from=internal to=internal command='dsconfig set-backend-prop --backend-name userRoot --set enabled:true''"
Restore task 2025042121535304 has been successfully completed
Restore complete
```

---

---
title: Saving Your Configuration Changes
description: Describes how to mount a Docker volume to the /opt/out directory to persist configuration changes for standalone containers and Docker Compose stacks
component: devops
page_id: devops::how-to/saveConfigs
canonical_url: https://developer.pingidentity.com/devops/how-to/saveConfigs.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-bind-mounting-for-a-stack: Bind mounting for a stack
  devops-bind-mounting-for-a-standalone-container: Bind mounting for a standalone container
  devops-getting-started-with-docker-compose-mounts: Getting started with Docker Compose mounts
---

# Saving Your Configuration Changes

To save any configuration changes you make when using the products in the stack, you must set up a local Docker volume to persist state and data for the stack. If you don't do this, whenever you bring the stack down, your configuration changes will be lost.

Mount a Docker volume location to the Docker `/opt/out` directory for the container. The location must be to a directory you haven't already created. Our Docker containers use the `/opt/out` directory to store application data.

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | Make sure the local directory isn't already created. Docker needs to create this directory for the mount to `/opt/out`. |

You can mount a Docker volume for containers in a stack or for standalone containers.

## Bind mounting for a stack

1. Add a `volumes` section under the container entry for each product in the `docker-compose.yaml` file you're using for the stack.

2. Under the `volumes` section, add a location to persist your data. For example:

   ```yaml
   pingfederate:...volumes:- /tmp/compose/pingfederate_1:/opt/out
   ```

3. In the `environment` section, comment out the `SERVER_PROFILE_PATH` setting.

   The container then uses your `volumes` entry to supply the product state and data, including your configuration changes.

   When the container starts, this mounts `/tmp/compose/pingfederate_1` to the `/opt/out` directory in the container. You can also view the product logs and data in the `/tmp/compose/pingfederate_1` directory.

4. Repeat this process for the remaining container entries in the stack.

### Bind mounting for a standalone container

Add a `volume` entry to the `docker run` command:

```shell
docker run \
  --name pingfederate \
  --volume <local-path>:/opt/out \
  pingidentity/pingfederate:edge
```

### Getting started with Docker Compose mounts

Within many of the docker-compose.yaml files in the Getting-Started [repository](https://github.com/pingidentity/pingidentity-devops-getting-started/tree/master/11-docker-compose), volume mounts to `opt/out` have been included to persist your configuration across container restarts.

* To view the list of persisted volumes, enter:

  ```shell
  docker volume list
  ```

* To view the contents of the /opt/out/ volume when the container is running, enter:

  ```shell
  docker container exec -it <container id> sh
  cd out
  ```

* To view the contents of the /opt/out/ volume when the container is stopped, enter:

  ```shell
  docker run --rm -i -v=<volume name>:/opt/out alpine ls
  ```

* To remove a volume, enter:

  ```shell
  docker volume rm <volume name>
  ```

* To copy files from the container to your local filesystem, enter:

  ```shell
  docker cp \
    <container id>:<source path> \
    <destination path>
  eg.
  docker cp \
    b867054293a1:/opt/out \
    ~/pingfederate/
  ```

* To copy files from your local filesystem to the container, enter:

  ```shell
  docker cp \
    <source path> \
    <container id>:<destination path>
  eg.
  docker cp \
    myconnector.jar \
    bb867054293a186:/opt/out/instance/server/default/deploy/
  ```

---

---
title: Securing the Containers
description: "Links to Docker and Kubernetes container security best practices and Ping Identity's Docker image hardening guide"
component: devops
page_id: devops::how-to/secureContainers
canonical_url: https://developer.pingidentity.com/devops/how-to/secureContainers.html
llms_txt: https://developer.pingidentity.com/devops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  devops-docker-best-practices: Docker Best Practices
  devops-kubernetes-best-practices: Kubernetes Best Practices
  devops-ping-identitys-docker-image-hardening-guide: Ping Identity's Docker Image Hardening Guide
---

# Securing the Containers

## Docker Best Practices

Please visit the [Docker](https://docs.docker.com/engine/security/) website for more information on best practices to secure a container.

### Kubernetes Best Practices

Please visit the [Kubernetes](https://kubernetes.io/blog/2016/08/security-best-practices-kubernetes-deployment/) website for more information on best practices to secure a deployment.

### Ping Identity's Docker Image Hardening Guide

For best practices on securing your product Docker image, see Ping Identity's [Hardening Guide](https://support.pingidentity.com/s/article/Docker-Image-Hardening-Deployment-Guide).
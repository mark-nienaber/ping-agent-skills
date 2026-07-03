---
description: "The term \"profile\" can vary in many instances. Here we will focus on two types of profiles for PingFederate: configuration archive, and bulk export. We will discuss the similarities and differences between two as well as how to build either from a running PingFederate environment."
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

---
title: Using the Cloud Acceleration Toolset
description: The Cloud Acceleration Toolset is a cloud migration tool that helps accelerate the migration to PingOne.
component: pingone
page_id: pingone:migration-tools:p1_cloud_acceleration_toolset
canonical_url: https://docs.pingidentity.com/pingone/migration-tools/p1_cloud_acceleration_toolset.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 16,2025
section_ids:
  target-audience: Target audience
  getting-started-with-cloud-migration: Getting started with cloud migration
  how-do-i-generate-an-assessment-report: How do I generate an Assessment Report?
  step-1-meet-the-prerequisites: "Step 1: Meet the prerequisites"
  pingfederate-to-pingone: PingFederate to PingOne
  step-2-export-the-configuration-from-the-source: "Step 2: Export the configuration from the source"
  step-3-import-configuration-into-the-cloud-acceleration-toolset: "Step 3: Import configuration into the Cloud Acceleration Toolset"
  how-do-i-migrate-applications-to-pingone-cloud: How do I migrate applications to PingOne cloud?
  step-1-validate-the-destination-tenant: "Step 1: Validate the destination tenant"
  step-2-define-the-authentication-experience: "Step 2: Define the authentication experience"
  step-3-migrate-applications-using-terraform: "Step 3: Migrate applications using Terraform"
---

# Using the Cloud Acceleration Toolset

The Cloud Acceleration Toolset is a cloud migration tool and part of PingOne. It helps accelerate motion to the PingOne cloud. The aim is to make migration to Ping's cloud as easy and seamless as possible. To address this, the Cloud Acceleration Toolset comprises the following tools.

![A block diagram with descriptions of the three tools included in the Cloud Acceleration Toolset](_images/cloud_migration_tools.png)

* **Discover**: This is a sales discovery tool that the field organization uses. The tool provides the following services:

  * Identifies the current state and the possible source of migration

  * Asks discovery questions

  * Proposes a migration path

  * Stores the discovery for future use

  * Generates a discovery report

* **Assess**: This tool connects to the customer's environment using a script downloaded to the customer's environment. The customer's migration source (for example, PingFederate) configuration is exported in JSON format and imported into the Assessment tool. The tool analyzes the configuration and generates an assessment. The assessment identifies and categorizes SAML and OAuth apps from the source as:

  * **Migratable** using the migration tool

  * **Change Required** before it can be migrated using the migration tool

  * **Reimagine** the application before it can be migrated, often manually

  The assessment is stored for future use, and a report is generated in a CSV format. You can download and use the report in customer conversations or to generate Statement of Work documents to estimate migration effort.

* **Migrate**: The Migration tool picks up the assessment as an input. When the customer is ready to migrate, they can select the apps they want to migrate from the assessment. A Terraform plan is generated for the selected apps and downloaded to the customer environment. When applied to the destination (for example, PingOne), the script creates the SAML apps and OAuth clients along with all the dependent resources. A migration report is also generated for audit purposes.

## Target audience

The Cloud Migration Toolset is part of PingOne and is freely available to the target audience. It caters to a diverse range of personas, each with unique needs and use cases:

* **Internal users**: Internal teams (Account Executives, Sales Engineering, Customer Success, Professional Services) leverage the Cloud Acceleration Toolset to accelerate delivery and ensure consistency through best-practice configurations.

* **Partners**: Partners can use this tool free of charge to deliver migration services to Ping customers.

* **Prospects**: Prospects can explore and use the Cloud Acceleration Toolset with guidance from Ping's Field Account Teams to take stock of what they own and their current state and to understand the effort involved in moving to Ping's cloud.

* **Customers**: Customers can use this tool in guidance with either Ping Professional Services or a Partner to accelerate migrations and achieve time to value.

## Getting started with cloud migration

The cloud migration flow is defined at a high level in the following flow diagram.

![A flow chart of the cloud migration process](_images/cloud_migration_flow.png)

1. Configuration is exported from the source (for example, PingFederate) in JSON format.

2. It's imported into the Cloud Acceleration Toolset for assessment.

   |   |                                                           |
   | - | --------------------------------------------------------- |
   |   | The Cloud Acceleration Toolset supports JSON format only. |

3. The assessment module parses the config and separates the different resources into categories displayed in a UI. The categories include:

   * **Migratable** using the migration tool.

   * **Change Required** before it can be migrated using the migration tool.

   * **Reimagine** the application before it can be migrated, often manually.

4. A dependency check is run for the resources marked for migration.

5. After dependencies are reconciled, a Terraform plan of the resources is generated and applied to the destination.

6. Resources marked as **Migratable** or **Change Required** will be migrated to the destination.

7. Resources marked as **Reimagine** will be addressed by PS or Partner-led engagements.

The migration is typically a phased approach, so the previous steps will be carried out in phases for subsets of the apps until all applications and resources are migrated to the destination, tested, and approved for go-live.

## How do I generate an Assessment Report?

You can perform a cloud migration assessment by completing these steps:

1. Meet the prerequisites

2. Export the configuration from the source

3. Import the configuration into the Cloud Acceleration Toolset

### Step 1: Meet the prerequisites

The Cloud Acceleration Toolset today supports PingFederate as a source and PingOne cloud as the destination. Over time, the Cloud Acceleration Toolset will support additional sources and destinations.

#### PingFederate to PingOne

To run a cloud migration from PingFederate to PingOne, the following prerequisites must be met:

* The PingFederate version must be 10.3 or later.

* PingFederate admin credentials are required to export configuration.

* A PingOne tenant as a source to migrate to.

* A PingOne worker app must be set up on the destination tenant. The app must have the Environment Admin role. The worker app's client ID and secret are used to migrate apps to PingOne.

* The PingOne tenant must have the Cloud Migration feature flag enabled.

### Step 2: Export the configuration from the source

1. Sign on to the admin console for the destination PingOne tenant and go to **Migration > Cloud Migration**.

2. Click **+** to start an assessment.

   ![An image of the Assessments screen](_images/cloud_migration_start_assessment.png)

3. Enter an assessment name and download the script.

   ![An image of the Provide Configuration screen and the Assessment Name field](_images/cloud_migration_assessment_name.png)

4. Run the script in the customer's tenant. You must have the following details to run the script:

   * **Hostname**: The host name of the PingFederate admin console (for example, pingfederate.example.com).

   * **Port**: The port of the PingFederate administrative console (for example, 443).

   * **Username**: The admin username (for example, api-admin).

   * **Password**: The admin password. Cloud Migration Key: A key to encrypt the exported configuration.

     |   |                                                   |
     | - | ------------------------------------------------- |
     |   | This should be different from the admin password. |

The script outputs the configuration `.zip` archive and the Cloud Migration Key, which you will need for step 3.

### Step 3: Import configuration into the Cloud Acceleration Toolset

The configuration `.zip` archive from an export can be imported into the Cloud Acceleration Tool by clicking **Upload .zip** as shown in the following image.

![An image of the Provide Configuration screen with the Upload zip button](_images/cloud_migration_assessment_name.png)

While uploading the file, you're prompted for the Cloud Migration Key. This key is required to decrypt the configuration file. After it's decrypted, the configuration is imported into the tool, and an assessment is created. The assessment:

* Generates a summary of all the apps and dependent resources

* Categorizes apps into what is migratable, what needs to change, and what needs reimagination

* Provides reasoning for the categorization

You can download a copy of this assessment in a CSV format.

## How do I migrate applications to PingOne cloud?

Before you can migrate applications to PingOne, you must first run an assessment. An assessment is a required input to start the migration process. Post assessment, applications can be migrated to PingOne by completing the following steps:

1. Validate the destination tenant (for example, PingOne)

2. Define the authentication experience

3. Migrate applications using Terraform

### Step 1: Validate the destination tenant

Validating the destination tenant is the first step in migrating applications to PingOne.

1. Sign on to admin console for the destination PingOne tenant and go to **Migration > Cloud Migration**.

2. On the **Migrations** tab, click the **[icon: plus, set=fa]**icon to create a new migration.

   ![An image of the Migrations screen](_images/cloud_migration_start_migration.png)

3. Select an existing assessment and, in the **Enter config password** field, enter the configuration key.

   ![An image of the Select Assessment for Migration screen](_images/cloud_migration_select_assessment.png)

4. Validate the destination tenant. To do this, you must provide the following details:

   |   |                                                                                       |
   | - | ------------------------------------------------------------------------------------- |
   |   | You can also find this information on the **Settings > Environment** Properties page. |

   * **PingOne Region**: The region where the PingOne tenant resides (for example, Europe)

   * **PingOne Environment ID**: Identifies the destination tenant

   * **PingOne Worker App Client Id**: Required to run the migration

     ![An image of the Validate Environment screen](_images/cloud_migration_validate.png)

After the details are provided, click **Validate Environment**, which should validate the tenant and provide a success or failed response. If the validation is a success, continue with the migration process. If you encounter a failure, check the following items for accuracy:

1. The PingOne tenant has the following services enabled at a minimum:

   * PingOne SSO

   * PingOne DaVinci

2. The client ID and the client secret for the worker app used for validation are correct.

3. The worker app is assigned the Environment Admin role for the target PingOne environment where the customer is migrating to.

### Step 2: Define the authentication experience

After the destination tenant is validated successfully, you must provide input about how the authentication experience should be configured. This isn't limited to just the logo, but also includes aspects such as:

* Is account recovery required?

* Is account registration required?

* Should [PingOne MFA](https://docs.pingidentity.com/pingone/authentication/p1_mfa_policies.html) be configured?

* Should adaptive authentication using [PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_introduction.html) be configured?

![An image of the Sign On Details screen](_images/cloud_migration_sign_on.png)

### Step 3: Migrate applications using Terraform

The Cloud Acceleration toolset uses Terraform to migrate applications to PingOne. This is a two-step process.

1. Click **Download Migration Zip** to download the migration `.zip` archive from the PingOne tenant.

   ![An image of the Migrate screen with Download Migration Zip button](_images/cloud_migration_download_zip.png)

2. Extract the file and run the `cloud-migration.sh` script. Follow the script prompts to migrate applications to PingOne.

   ![An image of the script screen](_images/cloud_migration_script.png)
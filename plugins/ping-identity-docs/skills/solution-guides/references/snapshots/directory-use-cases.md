---
title: Configuring virtual attributes in PingDirectory
description: To enable direct application access to a subset of groups in PingDirectory, configure conditional virtual attributes. This use case configures a virtual attribute based on a custom group class.
component: solution-guides
page_id: solution-guides:directory_use_cases:htg_config_virtual_attrs_pd
canonical_url: https://docs.pingidentity.com/solution-guides/directory_use_cases/htg_config_virtual_attrs_pd.html
revdate: July 25, 2025
page_aliases: ["directory_use_cases:htg_config_virtual_attrs_pd_declare_ismemberof.adoc", "directory_use_cases:htg_config_virtual_attrs_pd_create_virtual.adoc", "directory_use_cases:htg_config_virtual_attrs_pd_declare_new_attribute.adoc", "directory_use_cases:htg_config_virtual_attrs_pd_declare_new_attribute_ldif.adoc", "directory_use_cases:htg_config_virtual_attrs_pd_create_virtual_console.adoc", "directory_use_cases:htg_config_virtual_attrs_pd_create_virtual_cli.adoc"]
section_ids:
  component: Component
  before-you-begin: Before you begin
  declaring-a-new-attribute-that-is-equivalent-to-ismemberof: Declaring a new attribute that is equivalent to isMemberOf
  declaring-a-new-attribute-in-the-pingdata-administrative-console: Declaring a new attribute in the PingData administrative console
  steps: Steps
  using-an-ldif-file-to-declare-a-new-attribute-type-in-pingdirectory: Using an LDIF file to declare a new attribute type in PingDirectory
  steps-2: Steps
  example: Example:
  creating-a-virtual-attribute: Creating a virtual attribute
  creating-a-virtual-attribute-in-the-pingdata-administrative-console: Creating a virtual attribute in the PingData administrative console
  steps-3: Steps
  result: Result
  using-the-command-line-to-create-a-virtual-attribute-in-pingdirectory: Using the command line to create a virtual attribute in PingDirectory
  steps-4: Steps
---

# Configuring virtual attributes in PingDirectory

To enable direct application access to a subset of groups in PingDirectory, configure conditional virtual attributes. This use case configures a virtual attribute based on a custom group class.

## Component

PingDirectory 8.2

## Before you begin

You must have:

* A PingDirectory administrator account

* Access to the PingData administrative console

* A custom group class in place based on the default groupOfNames

## Declaring a new attribute that is equivalent to isMemberOf

You can declare a new attribute that is equivalent to `isMemberOf` using one of two methods. Click the tab of the method you want to use to see instructions.

* Admin console

* LDIF file

### Declaring a new attribute in the PingData administrative console

Use the PingData administrative console to declare a new attribute in PingDirectory.

### Steps

1. From the PingData administrative console, go to **LDAP Schema → Attribute Types**.

2. **Optional:** In the **Attribute Types** list, search for `isMemberOf` to filter.

   ![A screen capture of the PingData Administrative console LDAP Schema section. The Attribute Types list is being filtered by entering 'isM' into the search bar. There is a filter for the list that is set on All Schema Files and an unselected checkbox that say Modifiable Only.](_images/qxb1609193296683.png)

3. In the **isMemberOf** row, from the **Actions** list, select **Copy As**.

   ![A screen capture of the Attribute Types list. The Actions list next to isMemberOf is highlighted with a red arrow and Copy As is selected.](_images/nsh1609193793357.png)

4. In the **Basic Properties** section, complete the fields for a new attribute type:

   1. In the **Name** field, enter a name for the new attribute type.

   2. In the **Description** field, enter a description for the new attribute type

   3. In the **Stored in File** field, enter a unique filename for the new attribute type.

      |   |                                                                                                          |
      | - | -------------------------------------------------------------------------------------------------------- |
      |   | In the **Syntax** field, keep the default settings. The **Multivalued** checkbox should remain selected. |

5. Click **Save**.

6. Restart PingDirectory.

### Using an LDIF file to declare a new attribute type in PingDirectory

Use an LDIF file to declare a new attribute type in PingDirectory.

#### Steps

1. Create an LDIF file that contains the following information.

   Provide your own information in the angled brackets based on your configuration.

   ##### Example:

   ```
   dn: cn=schema
   attributeTypes: (<isMemberOfSupport>-OID NAME '<isMemberOfSupport>'
   DESC'<custom attribute>'
   SYNTAX 1.3.6.1.4.1.1466.115.121.1.12
   NO-USER-MODIFICATION USAGE directoryOperation
   X-ORIGIN 'Sun Java System Directory Server'
   X-SCHEMA-FILE '<Your file name>.ldif')
   ```

2. Copy the file in `<pingdirectory>/config/schema`.

3. Restart PingDirectory.

## Creating a virtual attribute

You can create a virtual attribute using one of two methods. Click the tab of the method you want to use to see instructions.

* Admin console

* Command line

### Creating a virtual attribute in the PingData administrative console

Use the PingData administrative console to create a virtual attribute in PingDirectory.

#### Steps

1. From the PingData administrative console, go to **Configuration**.

2. From the **Core** list, select **Virtual Attributes**.

3. In the **isMemberOf** row, from the **Actions** list, select **Copy**.

4. Complete the required fields for **New Is Member Of Virtual Attribute**:

   1. In the **Name** field, enter a name.

   2. In the **Description** field, enter a description.

   3. Select the **Enabled** checkbox.

   4. In the **Attribute Type** field, enter the attribute type you created in step 4 of the admin console tab for *Declaring a new attribute that is equivalent to isMemberOf*.

   5. In the **Included Group Filter**, enter `(objectClass=<your custom class name>)`.

      |   |                                                                |
      | - | -------------------------------------------------------------- |
      |   | Keep the default settings for all other fields and selections. |

5. Click **Save**.

   |   |                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------- |
   |   | This new attribute is an operational attribute. Ensure you retrieve the attribute when you call the directory. |

### Result

Your new attribute is ready for testing.

### Using the command line to create a virtual attribute in PingDirectory

Use your computer's command line to perform commands to create a virtual attribute in PingDirectory.

#### Steps

* In your computer's command line, enter the following commands with your information.

  Provide your own information in the angled brackets based on your configuration.

  ```
  dsconfig create-virtual-attribute --name  <isMemberOfSupport>  \
  --type is-member-of \
  --set enabled:true \
  --set attribute-type:<isMemberOfSupport>  \
  --set "included-group-filter:(objectClass=<groupSupport>)"
  ```

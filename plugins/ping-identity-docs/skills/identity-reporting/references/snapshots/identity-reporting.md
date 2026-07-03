---
title: Configuration
description: Ping Identity Reporting allows reporting administrators to customize the reporting experience with a few general, system-wide configurations. Administrators also have the option to import report bundles that contain single or multiple report definitions, allowing for simple migration from one environment to the next.
component: identity-reporting
page_id: identity-reporting:identity-reporting:chap-report-configuration
canonical_url: https://docs.pingidentity.com/identity-reporting/identity-reporting/chap-report-configuration.html
section_ids:
  report_template: Report template
  email: Email
  report_bundle: Report bundle
---

# Configuration

Ping Identity Reporting allows reporting administrators to customize the reporting experience with a few general, system-wide configurations. Administrators also have the option to import report bundles that contain single or multiple report definitions, allowing for simple migration from one environment to the next.

![Configuration screen for reports](_images/report-configuration.png)

## Report template

The report template section of the configuration allows an administrator to view, upload or remove a branding image used for PDF reports. Supported image formats are jpeg and png.

Upload New Logo:

|   |                                                               |
| - | ------------------------------------------------------------- |
|   | This process overwrites any existing logo with the new image. |

1. At the top of the dashboard page, in the navigation bar, select Upload Logo under Configuration menu.

2. Click Browse to open the Choose File dialog box and select an image to upload. The supported image formats are jpeg and png.

3. Once a valid image has been selected, it displays in the Selected Logo area for validation

4. Click Upload to complete the upload process. The new logo displays in the Current Logo area.

Delete current logo:

1. At the top of the dashboard page, in the navigation bar, select Report Template under the Configure menu.

2. Click Delete Current Logo. The image disappears from the Current Logo area.

## Email

The email section of the configuration allows an administrator to modify the contents of the email notification that is sent out with every scheduled report.

![Email template configuration](_images/report-email-template-configuration.png)

Modify email notification:

1. At the top of the dashboard page, in the navigation bar, select Email Template under the Configuration menu.

2. On the Email Template Configuration page, fill in each of the required fields. Additional details on the available fields are given below:

   * Subject: (Required) Subject of email notification.

   * Type: (Required) Content-Type of email body can be set to text/HTML or text/plain.

   * Body: (Required) Body of email notification.

## Report bundle

The report bundle section of the configuration allows an administrator to import sets of pre-configured report definitions. The following guidelines can be used when creating bundles:

* Report bundles are required to be .json files that contain a "reportDefinitions" array in a JSON string

* The "reportDefinitions" array contains one or more JSON objects that represent individual report definitions

* Each object can specify all attributes available to a report definition, as described in [Creating New Resource Definitions](chap-report-definitions.html#create-new-report-definitions). All required attributes must be provided at a minimum. The Data Source selection box is available within the interface to allow you to choose which data source the reports are being uploaded to. To upload reports for multiple data sources, use the API endpoint instead.

![report bundle](_images/report-bundle.png)

Upload report bundle:

1. At the top of the dashboard page, in the navigation bar, select Report Bundle under Configure.

2. Click Browse to open the Choose File dialog box and select an image to upload. The bundle must be a .json file and contain valid JSON syntax

   ![Report bundle configuration](_images/report-bundle-upload.png)

3. Once a valid bundle has been selected, contents are loaded into the preview area for validation. The administrator is then able to navigate among multiple report definitions using the Previous and Next buttons.

4. Click Upload Reports to complete the upload process.

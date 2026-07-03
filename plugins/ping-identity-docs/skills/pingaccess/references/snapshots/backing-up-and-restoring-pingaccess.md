---
title: Backing up and restoring PingAccess
description: This section provides instructions for backing up and restoring PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:backing_up_and_restoring_pingaccess:pa_backing_up_and_restoring_pa
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/pa_backing_up_and_restoring_pa.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Backing up and restoring PingAccess

This section provides instructions for backing up and restoring PingAccess.

The tools in this section let you create backups of your PingAccess environment and restore your environment from them. You should back up your environment regularly.

* If you need disaster recovery, see [Backing up and restoring PingAccess using a `.zip` archive](pa_backing_up_and_restoring_pa_using_a_zip_archive.html).

* If you need to restore an environment's configuration or to test in a new environment, see [Backing up and restoring PingAccess using a JSON file](pa_backing_up_and_restoring_pa_using_a_json_file.html).

---

---
title: "Backing up and restoring PingAccess using a <code class=\"filepath\">.zip</code> archive"
description: Use a .zip archive to back up and restore PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:backing_up_and_restoring_pingaccess:pa_backing_up_and_restoring_pa_using_a_zip_archive
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/pa_backing_up_and_restoring_pa_using_a_zip_archive.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
---

# Backing up and restoring PingAccess using a `.zip` archive

Use a `.zip` archive to back up and restore PingAccess.

Using a `.zip` archive is appropriate for disaster recovery because it uses automatically generated backups and restores the entire PingAccess configuration.

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The system on which you are restoring must have the same major and minor version of PingAccess installed before you begin the restoration. |

---

---
title: Backing up and restoring PingAccess using a JSON file
description: Use a JavaScript Object Notation (JSON) file to back up and restore PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:backing_up_and_restoring_pingaccess:pa_backing_up_and_restoring_pa_using_a_json_file
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/pa_backing_up_and_restoring_pa_using_a_json_file.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
---

# Backing up and restoring PingAccess using a JSON file

Use a JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* file to back up and restore PingAccess.

This method is appropriate for reverting to a prior configuration or testing a configuration in a new environment. It uses manually-generated backups and restores the PingAccess database configuration.

---

---
title: "Backing up PingAccess using a <code class=\"filepath\">.zip</code> archive"
description: Back up your PingAccess configuration by copying a zip archive and additional customized files to another system.
component: pingaccess
version: 9.1
page_id: pingaccess:backing_up_and_restoring_pingaccess:pa_backing_up_pa_using_a_zip_archive
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/pa_backing_up_pa_using_a_zip_archive.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Backing up PingAccess using a `.zip` archive

Back up your PingAccess configuration by copying a `zip` archive and additional customized files to another system.

## About this task

To back up your PingAccess configuration using a `.zip` archive for disaster recovery purposes:

## Steps

1. In the PingAccess system, go to `<PA_HOME>/data/archive` and copy the most recent `.zip` archive to another system.

   These archives are automatically created when an administrative user authenticates to the administrative console. The maximum number of backups is specified by the `pa.backup.filesToKeep` property in the `run.properties` file.

2. **Optional:** If you have created or customized templates, copy the contents of the `<PA_HOME>/conf/template` directory to another system.

3. **Optional:** If you have created custom plugins, copy the contents of the `<PA_HOME>/deploy` directory to another system.

4. **Optional:** If you have created or customized localization, copy the contents of the `<PA_HOME>/conf/localization` directory to another system.

---

---
title: Backing up PingAccess using a JSON file
description: Back up your PingAccess configuration by copying a JavaScript Object Notation (JSON) file to another system.
component: pingaccess
version: 9.1
page_id: pingaccess:backing_up_and_restoring_pingaccess:pa_backing_up_pa_using_a_json_file
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/pa_backing_up_pa_using_a_json_file.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Backing up PingAccess using a JSON file

Back up your PingAccess configuration by copying a JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* file to another system.

## About this task

Back up your PingAccess configuration by copying a JSON file to another system.

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Large PingAccess configurations can take upwards of 30 minutes to export. During an export, you cannot modify the PingAccess configuration. |

## Steps

1. Click **Settings**, then go to **System > Configuration Export/Import**.

2. Click **Export Configuration**.

   The downloaded file name is `pa-data-<timestamp>.json`.

   |   |                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The *\<timestamp>* value is formatted `MM-DD-YYYY.hh.mm.ss`. For example, a date and time of January 31, 2020 1:35 PM would be encoded as `01-31-2020.13.35.00` in the file name. |

3. Copy the generated file to another system.

4. If you plan to restore PingAccess in a new environment, copy the `<PA_Home>/conf/pa.jwk` file, and save it with the generated JSON file.

---

---
title: "Restoring PingAccess using a <code class=\"filepath\">.zip</code> archive"
description: Restore your PingAccess configuration using a .zip archive and additional customized files.
component: pingaccess
version: 9.1
page_id: pingaccess:backing_up_and_restoring_pingaccess:pa_restoring_pa_using_a_zip_archive
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/pa_restoring_pa_using_a_zip_archive.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 17, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Restoring PingAccess using a `.zip` archive

Restore your PingAccess configuration using a `.zip` archive and additional customized files.

## About this task

This procedure restores the PingAccess configuration using a `.zip` archive and additional customization files. You can use this method for disaster recovery because it uses an automatically-generated file and restores the entire PingAccess configuration.

To restore your PingAccess configuration using a `.zip` archive and additional customized files:

## Steps

1. If PingAccess is not installed on the system, install the same version of PingAccess used to create the backup.

   |   |                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------- |
   |   | The maintenance version does not have to be identical. For example, a backup made on PingAccess 6.3.0 could be restored on 6.3.1. |

2. Stop PingAccess.

3. Extract the backup `.zip` archive to `<PA_HOME>`.

4. **Optional:** If you backed up custom templates, copy the backed up content to the `<PA_HOME>/conf/template` directory.

5. **Optional:** If you backed up custom plugins, copy the backed up content to the `<PA_HOME>/deploy` directory.

6. **Optional:** If you backed up custom localization, copy the backed up content to the `<PA_HOME>/conf/localization` directory.

7. Restart PingAccess.

   ### Result:

   Your PingAccess configuration is reverted to the configuration in the backup archive.

---

---
title: Restoring PingAccess using a JSON file
description: Restore your PingAccess configuration using a JavaScript Object Notation (JSON) file.
component: pingaccess
version: 9.1
page_id: pingaccess:backing_up_and_restoring_pingaccess:pa_restoring_pa_using_a_json_file
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/backing_up_and_restoring_pingaccess/pa_restoring_pa_using_a_json_file.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  troubleshooting: Troubleshooting:
---

# Restoring PingAccess using a JSON file

Restore your PingAccess configuration using a JavaScript Object Notation (JSON) *(tooltip: \<div class="paragraph">
\<p>An open, lightweight data-interchange format that uses human-readable text to store and transmit data.\</p>
\</div>)* file.

## About this task

The **Import Configuration** option is a version-specific tool for importing a previously exported configuration. PingAccess checks the exported JSON file to ensure that the file is not from a later version of PingAccess and is compatible with application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* v3 (PingAccess 5.0 or later).

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | This operation is destructive and overwrites any existing PingAccess configuration. |

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Large PingAccess configurations can take several hours to import. During an import, you cannot modify or read the PingAccess configuration. |

To restore your PingAccess configuration using a JSON file:

## Steps

1. If you are restoring on a new environment, copy the saved `pa.jwk` file to the `<PA_Home>/conf/` directory.

2. Click **Settings**, then go to **System > Configuration Export/Import**.

3. Click **Import Configuration** and select the local file that you want to use.

4. Click **Import**.

5. Click **Confirm** and make any changes indicated by the import process.

   ### Troubleshooting:

   If the import fails, click **View failures from last import** to view all of the errors logged during the import.

6. If the Agent or Admin listener key pairs change as a result of the import operation, restart PingAccess.

7. If the environment is clustered, ensure that the replica administrative node and engine nodes are using the proper engine keys, and if they aren't, re-save them to generate a new public key, and reconfigure them to use the newly generated key.

   For more information, see [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html).
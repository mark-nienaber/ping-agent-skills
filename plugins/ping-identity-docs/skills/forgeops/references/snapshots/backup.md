---
title: "<span class=\"command\">dsbackup</span> utility"
description: This page provides instructions for backing up and restoring DS data in a ForgeOps deployment using the dsbackup utility.
component: forgeops
version: 2026.2
page_id: forgeops:backup:dsbackup
canonical_url: https://docs.pingidentity.com/forgeops/2026.2/backup/dsbackup.html
llms_txt: https://docs.pingidentity.com/forgeops/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Backup &amp; Restore", "Directory Server", "dsbackup"]
section_ids:
  dsbackup-backup: Back up using the dsbackup utility
  setup-cloud-storage: Set up cloud storage
  schedule-backups: Schedule backups
  dsbackup-restore: Restore
  new-deployment: New ForgeOps deployment using DS backup
  restore-all-directories: Restore all DS directories
  restore-one-directory: Restore one DS directory
  dr-restore: Restore a PingDS deployment after a disaster
  restore-best-practices: Best practices for restoring directories
  using_cloud_storage_locally_for_backup_and_restore: Using cloud storage locally for backup and restore
---

# dsbackup utility

This page provides instructions for backing up and restoring DS data in a ForgeOps deployment using the dsbackup utility.

## Back up using the dsbackup utility

Before you can back up DS data using the dsbackup utility, you must [set up a cloud storage container](#setup-cloud-storage) in Google Cloud Storage, Amazon S3, or Azure Blob Storage and configure a Kubernetes secret with the container's credentials in your ForgeOps deployment. Then, you [schedule backups](#schedule-backups) by running the ds-backup.sh script.

### Set up cloud storage

Cloud storage setup varies depending on your cloud provider. Expand one of the following sections for provider-specific setup instructions:

> **Collapse: Google Cloud**
>
> Set up a Google Cloud Storage (GCS) bucket for the DS data backup and configure the ForgeOps deployment with the credentials for the bucket:
>
> 1. Create a Google Cloud service account with required privileges to write objects in a GCS bucket. For example, Storage Object Creator.
>
> 2. Add a key to the service account, and then download the JSON file containing the new key.
>
> 3. Configure a multi-region GCS bucket for storing DS backups:
>
>    1. Create a new bucket, or identify an existing bucket to use.
>
>    2. Note the bucket's Link for gsutil value.
>
>    3. Grant permissions on the bucket to the service account you created in step 1.
>
> 4. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.
>
> 5. Create the `cloud-storage-credentials` secret that contains credentials to write to cloud storage. The DS pods use this secret when performing backups.
>
>    For `my-sa-credential.json`, specify the JSON file containing the service account's key:
>
>    ```
>    $ kubectl create secret generic cloud-storage-credentials \
>     --from-file=GOOGLE_CREDENTIALS_JSON=/path/to/my-sa-credential.json
>    ```
>
> 6. Restart the pods that perform backups so that DS can get the credentials needed to write to the backup location:
>
>    ```
>    $ kubectl delete pods ds-cts-0
>    $ kubectl delete pods ds-idrepo-0
>    ```
>
> After the pods have restarted, you can [schedule backups](#schedule-backups).

> **Collapse: AWS**
>
> Set up an S3 bucket for the DS data backup and configure the ForgeOps deployment with the credentials for the bucket:
>
> 1. Create or identify an existing S3 bucket for storing the DS data backup and note the S3 link of the bucket.
>
> 2. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.
>
> 3. Create the `cloud-storage-credentials` secret that contains credentials to write to the cloud storage. The DS pods use this secret when performing backups:
>
>    ```
>    $ kubectl create secret generic cloud-storage-credentials \
>     --from-literal=AWS_ACCESS_KEY_ID=my-access-key \
>     --from-literal=AWS_SECRET_ACCESS_KEY=my-secret-access-key
>    ```
>
> 4. Restart the pods that perform backups so that DS can get the credentials needed to write to the backup location:
>
>    ```
>    $ kubectl delete pods ds-cts-0
>    $ kubectl delete pods ds-idrepo-0
>    ```
>
> After the pods have restarted, you can [schedule backups](#schedule-backups).

> **Collapse: Azure**
>
> Set up an Azure Blob Storage container for the DS data backup and configure the ForgeOps deployment with the credentials for the container:
>
> 1. Create or identify an existing Azure Blob Storage container for the DS data backup. Learn more about how to create and use Azure Blob Storage in [Quickstart: Create, download, and list blobs with Azure CLI](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-cli).
>
> 2. Log in to Azure Container Registry:
>
>    ```
>    $ az acr login --name my-acr-name
>    ```
>
> 3. Get the full Azure Container Registry ID:
>
>    ```
>    $ ACR_ID=$(az acr show --name my-acr-name --query id | tr -d '"')
>    ```
>
>    With the full registry ID, you can connect to a container registry even if you are logged in to a different Azure subscription.
>
> 4. Add permissions to connect your AKS cluster to the container registry:
>
>    ```
>    $ az aks update --name my-aks-cluster-name --resource-group my-cluster-resource-group --attach-acr $ACR_ID
>    ```
>
> 5. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.
>
> 6. Create secrets that contain credentials to write to cloud storage. The DS pods use these when performing backups:
>
>    1. Get the name and access key of the Azure storage account for your storage container\[[1](#_footnotedef_1 "View footnote.")].
>
>    2. Create the `cloud-storage-credentials` secret:
>
>    ```
>    $ kubectl create secret generic cloud-storage-credentials \
>     --from-literal=AZURE_STORAGE_ACCOUNT_NAME=my-storage-account-name \
>     --from-literal=AZURE_ACCOUNT_KEY=my-storage-account-access-key
>    ```
>
> 7. Restart the pods that perform backups so that DS can get the credentials needed to write to the backup location:
>
>    ```
>    $ kubectl delete pods ds-cts-0
>    $ kubectl delete pods ds-idrepo-0
>    ```
>
> After the pods have restarted, you can [schedule backups](#schedule-backups).

### Schedule backups

1. Make sure you've [set up cloud storage for your cloud provider platform](#setup-cloud-storage).

2. Make sure your current Kubernetes context references the cluster and namespace where the DS pods are running.

3. Make sure you've backed up and saved the shared master key and TLS key for the ForgeOps deployment.

4. Set variable values in the /path/to/forgeops/bin/ds-backup.sh script:

   | Variable Name             | Default                   | Notes                                                                                                                                                                                                                           |
   | ------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `HOSTS`                   | `ds-idrepo-2`             | The `ds-idrepo` or `ds-cts` replica or replicas to back up. Specify a comma-separated list to back up more than one replica. For example, to back up the `ds-idrepo-2` and `ds-cts-2` replicas, specify `ds-idrepo-2,ds-cts-2`. |
   | `BACKUP_SCHEDULE_IDREPO`  | On the hour and half hour | How often to run backups of the `ds-idrepo` directory. Specify using [cron job format](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules).                                                                 |
   | `BACKUP_DIRECTORY_IDREPO` | n/a                       | Where the `ds-idrepo` directory is backed up. Specify:- `gs://bucket/path` to back up to Google Cloud Storage

   - `s3://bucket/path` to back up to Amazon S3

   - `az://container/path` to back up to Azure Blob Storage           |
   | `BACKUP_SCHEDULE_CTS`     | On the hour and half hour | How often to run backups of the `ds-cts` directory. Specify using [cron job format](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules).                                                                    |
   | `BACKUP_DIRECTORY_CTS`    | n/a                       | Where the `ds-cts` directory is backed up. Specify:- `gs://bucket/path` to back up to Google Cloud Storage

   - `s3://bucket/path` to back up to Amazon S3

   - `az://container/path` to back up to Azure Blob Storage              |

5. Run the ds-backup.sh create command to schedule backups:

   ```
   $  /path/to/forgeops/bin/ds-backup.sh create
   ```

   The first backup is a full backup; all later backups are incremental from the previous backup.

   By default, the ds-backup.sh create command configures:

   * The backup task name to be `recurringBackupTask`

   * The backup tasks to back up all DS backends

   If you want to change either of these defaults, configure variable values in the ds-backup.sh script.

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | To cancel a backup schedule, run the ds-backup.sh cancel command. |

## Restore

This section covers three options to restore data from dsbackup backups:

* [New ForgeOps deployment using DS backup](#new-deployment)

* [Restore all DS directories](#restore-all-directories)

* [Restore one DS directory](#restore-one-directory)

### New ForgeOps deployment using DS backup

Creating new instances from previously backed up DS data is useful when a system disaster occurs or when directory services are lost. It is also useful when you want to port test environment data to a production deployment.

To create new DS instances with data from a previous backup:

1. Make sure your current Kubernetes context references the new ForgeOps cluster. Also make sure that the namespace of your Kubernetes context contains the DS pods into which you plan to load data from backup.

2. Create Kubernetes secrets containing your cloud storage credentials:

   > **Collapse: On Google Cloud**
   >
   > ```
   > $ kubectl create secret generic cloud-storage-credentials \
   >  --from-file=GOOGLE_CREDENTIALS_JSON=/path/to/my-sa-credential.json
   > ```
   >
   > In this example, specify the path and file name of the JSON file containing the Google service account key for my-sa-credential.json.

   > **Collapse: On AWS**
   >
   > ```
   > $ kubectl create secret generic cloud-storage-credentials \
   >  --from-literal=AWS_ACCESS_KEY_ID=my-access-key \
   >  --from-literal=AWS_SECRET_ACCESS_KEY=my-secret-access-key
   >  --from-literal=AWS_REGION=my-region
   > ```

   > **Collapse: On Azure**
   >
   > ```
   > $ kubectl create secret generic cloud-storage-credentials \
   >  --from-literal=AZURE_STORAGE_ACCOUNT_NAME=my-storage-account-name \
   >  --from-literal=AZURE_ACCOUNT_KEY=my-storage-account-access-key
   > ```

3. Configure the backup bucket location and enable the automatic restore capability:

* In a Kustomize-based deployment

* In a Helm-based deployment

1. Change to the /path/to/forgeops/kustomize/base/kustomizeConfig directory.

2. Open the kustomization.yaml file.

3. Set the `DSBACKUP_DIRECTORY` parameter to the location of the backup bucket. For example:

   > **Collapse: On Google Cloud**
   >
   > `DSBACKUP_DIRECTORY="gs://my-backup-bucket"`

   > **Collapse: On AWS**
   >
   > `DSBACKUP_DIRECTORY="s3://my-backup-bucket"`

   > **Collapse: On Azure**
   >
   > `DSBACKUP_DIRECTORY="az://my-backup-bucket"`

4. Set the `AUTORESTORE_FROM_DSBACKUP` parameter to `"true"`.

1) Change to the /path/to/forgeops/charts/identity-platform directory.

2) Edit values.yaml file and set up `autoRestore`, `backupLocation`, and `backupHosts` parameters for `ds-idrepo` and `ds-cts`. For example to restore `ds-idrepo-2`:

   > **Collapse: On Google Cloud**
   >
   > ```
   > ...
   > ds_restore:
   >   autoRestore: true
   >   backupLocation: "gs://my-backup-bucket"
   >   backupHosts: "ds-idrepo-2"
   > ...
   > ```

   > **Collapse: On AWS**
   >
   > ```
   > ...
   > ds_restore:
   >   autoRestore: true
   >   backupLocation: "s3://my-backup-bucket"
   >   backupHosts: "ds-idrepo-2"
   > ...
   > ```

   > **Collapse: On Azure**
   >
   > ```
   > ...
   > ds_restore:
   >   autoRestore: true
   >   backupLocation: "az://my-backup-bucket"
   >   backupHosts: "ds-idrepo-2"
   > ...
   > ```

4. Then [Deploy the platform](../deploy/deploy.html).

   When the platform is deployed, new DS pods are created, and the data is automatically restored from the most recent backup available in the cloud storage location you configured.

To verify that the data has been restored:

* Use the IDM UI or platform UI.

* Review the logs for the DS pods' `init` container. For example:

  ```
  $ kubectl logs --container init ds-idrepo-0
  ```

### Restore all DS directories

To restore all the DS directories in your ForgeOps deployment from backup:

1. Delete all the PVCs attached to DS pods using the kubectl delete pvc command.

2. Because PVCs might not get deleted immediately when the pods to which they're attached are running, stop the DS pods.

   Using separate terminal windows, stop every DS pod using the kubectl delete pod command. This deletes the pods and their attached PVCs.

   Kubernetes automatically restarts the DS pods after you delete them. The automatic restore feature of ForgeOps deployments recreates the PVCs as the pods restart by retrieving backup data from cloud storage and restoring the DS directories from the latest backup.

3. After the DS pods come up, restart IDM pods to reconnect IDM to the restored PVCs:

   1. List all the pods in the namespace.

   2. Delete all the pods running IDM.

### Restore one DS directory

In a ForgeOps deployment with automatic restore enabled, you can recover a failed DS pod if the latest backup is within the [replication purge delay](https://docs.pingidentity.com/pingds/8/configref/objects-replication-synchronization-provider.html#replication-purge-delay):

1. Delete the PVC attached to the failed DS pod using the kubectl delete pvc command.

2. Because the PVC might not get deleted immediately if the attached pod is running, stop the failed DS pod.

   In another terminal window, stop the failed DS pod using the kubectl delete pod command. This deletes the pod and its attached PVC.

   Kubernetes automatically restarts the DS pod after you delete it. The automatic restore feature recreates the PVC as the pod restarts by retrieving backup data from cloud storage and restoring the DS directory from the latest backup.

3. If the DS instance you restored was the `ds-idrepo` instance, restart IDM pods to reconnect IDM to the restored PVC:

   1. List all the pods in the namespace.

   2. Delete all the pods running IDM.

For information about manually restoring DS where the latest available backup is older than the replication purge delay, refer to the [Restore](https://docs.pingidentity.com/pingds/8/maintenance-guide/backup-restore.html#restore) section in the DS documentation.

### Restore a PingDS deployment after a disaster

The PingDS disaster recovery involves additional steps beyond restoring a complete PingDS environment from backup. The dsrepl disaster-recovery must be run after a normal restore and before the PingDS server starts.

The disaster recovery process resets replication metadata to allow the newly restored version of the PingDS topology. A disaster recovery ID identifies the new topology. The data pods not being restored have a different disaster recovery ID and don't exchange data with pods already recovered.

The disaster recovery process is automated in Forgeops. When a restore is initiated, the disaster recovery is also initiated using the disaster recovery ID defined in the configuration. If the disaster recovery ID matches the contents of the restored backup, the disaster recovery is stopped; otherwise, the data is disaster recovered.

The disaster recovery ID is configured in the `platform-config` configmap as follows:

* For Helm: update `ds_restore.disasterRecoveryId` in your custom values file

* For Kustomize: update DISASTER\_RECOVERY\_ID in your custom overlay in base/platform-config.yaml

### Best practices for restoring directories

* Use a backup newer than the last replication purge.

* When you restore a single DS replica, the backup must be recent. Learn more at [DS README](https://github.com/ForgeRock/forgeops/blob/dev/docker/ds/README.md#restore-of-a-single-instance-rest-of-topology-still-valid).

## Using cloud storage locally for backup and restore

In DS version 8.1.0 you can use cloud storage mounted locally for backup and restore. This is useful for local testing of backup and restore. You can mount cloud storage as local filesystem and use the local mount point as a local backup location. Learn more about mounting cloud storage locally in the [Cloud storage section](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html#cloud-storage) of DS documentation.

***

[1](#_footnoteref_1). To get the access key from the Azure portal, go to your storage account. Under Security + networking on the left navigation menu, select Access keys

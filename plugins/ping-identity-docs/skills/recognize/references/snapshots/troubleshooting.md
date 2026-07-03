---
title: Troubleshooting guide
description: This document contains a list of errors that can occur when running PingOne Recognize on-premises and approaches for resolving each one.
component: recognize
page_id: recognize:troubleshooting:troubleshooting
canonical_url: https://docs.pingidentity.com/recognize/troubleshooting/troubleshooting.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  core-backend-services: Core (backend services)
  core-daemon: Core daemon
  operations-service: Operations service
  node-persistence: Node persistence
  circuit-storage: Circuit storage
  auth-vault: Auth vault
  pingone-recognize-offline-enrollment-agent: PingOne Recognize offline enrollment agent
  mobile-sdk: Mobile SDK
  alerts: Alerts
  scaling-the-cluster: Scaling the cluster
---

# Troubleshooting guide

This document contains a list of errors that can occur when running PingOne Recognize on-premises and approaches for resolving each one.

It includes sections for backend services, mobile SDKs, alerts, and information on scaling the production cluster.

## Core (backend services)

### Core daemon

The core daemon is a Spring Boot service that provides an API for communication between the client SDK and the PingOne Recognize protocol. HTTP and REST errors for this API are listed in the core daemon Swagger file.

| Error                                                                                       | Cause                                                     | Next steps                                                                           |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `[SERVICE-NAME] service returned error: *`                                                  | The specified internal service failed.                    | Check the logs of the service that failed.                                           |
| `node-persistence.default.svc.cluster.local/circuit-storage-2.default.svc.cluster.local/…​` | Connection error                                          | Check whether the system is configured properly and all services are up and running. |
| `Cannot deserialize value of type java.time.LocalDateTime…​`                                | The request body could not be parsed.                     | Check the Swagger documentation for the correct request format.                      |
| `ServletOutputStream failed to flush: java.nio.channels.ClosedChannelException`             | The connection between the client and the service failed. | Retry the operation.                                                                 |

### Operations service

The operations service is a Spring Boot service that provides an API for server-to-server communication. HTTP and REST errors for this API are listed in the operations service Swagger file.

### Node persistence

The node persistence component is an internal Spring Boot service that provides an abstraction layer for database storage. HTTP and REST errors for this API are listed in the node persistence Swagger file.

| Error                                                 | Cause                                                                       | Next steps                                   |
| ----------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------- |
| `Application run failed`                              | The node persistence service could not start.                               | Check the node persistence logs for details. |
| `HikariPool-1 - Exception during pool initialization` | A Hikari error always indicates a problem related to the database instance. | Check the database logs for details.         |

### Circuit storage

The circuit storage component is an internal Spring Boot service that stores and retrieves garbled circuits used by the PingOne Recognize protocol. It uses a PostgreSQL database for metadata storage and an Amazon S3 bucket for circuit payload storage. HTTP and REST errors for this API are listed in the circuit storage Swagger file.

| Error                                                                     | Cause                                        | Next steps                                                               |
| ------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| `HHH100501: Exception executing batch/Batch entry/Error: duplicate key…​` | SQL error                                    | Check the database logs for details.                                     |
| `Persisting circuit on S3 failed. [circuitId=*]`                          | Circuit storage cannot connect to Amazon S3. | If the configuration is correct, check for a network or provider outage. |
| `Error while deleting some circuits`                                      | Database error                               | Check logs for details.                                                  |

### Auth vault

The auth vault component is an internal Spring Boot service that verifies headers and signatures and releases authentication tokens. It uses Amazon Key Management Service (KMS) for cryptographic operations. HTTP and REST errors for this API are listed in the auth vault Swagger file.

| Error                                                                           | Cause                                         | Next steps                                                                                                                      |
| ------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `Node persistence returned an unexpected status 500`                            | Misconfiguration in the Node Persistence URL. | Check logs for details.                                                                                                         |
| `Node persistence thrown exception: node-persistence.default.svc.cluster.local` | Connection error                              | Check logs for details.                                                                                                         |
| `Failed JWT token sign`                                                         | Auth vault failed to use Amazon KMS.          | Check the configuration of signature keys passed to the service and the KMS configuration. If the problem persists, check logs. |

### PingOne Recognize offline enrollment agent

The PingOne Recognize offline enrollment agent takes an image and generates a client state and server state, which are sent to the client SDK and the operations service respectively.

| Error | Cause                                                                                                       | Next steps                                                                                                                                                                                               |
| ----- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400` | Invalid image format                                                                                        | Provide a valid JPEG image.                                                                                                                                                                              |
| `422` | The biometric pipeline rejected the image as low quality, lacking a detectable face, or for another reason. | The response body contains `detail` for the rejection reason and `stats` with structured data about the pipeline run. This data can be shared with PingOne Recognize to understand the rejection reason. |
| `500` | Internal server error                                                                                       | Check the response body for details.                                                                                                                                                                     |

## Mobile SDK

All SDK errors below should be handled within the application and never shown directly to the user.

| Code    | Error             | Explanation                                                                                                   | Guidelines for integrators                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------- | ----------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `30000` | `spoofing`        | The liveness pipeline from the biometric SDK could not confirm that the authentication attempt was genuine.   | Ask the user to retry authentication and make sure they are in an environment with proper lighting and no obstruction.                                                                                                                                                                                                                                                                                                     |
| `30001` | `timeout`         | The liveness pipeline from the biometric SDK could not confirm that a real person was in front of the camera. | Ask the user to retry authentication and make sure they are in an environment with proper lighting and no obstruction.                                                                                                                                                                                                                                                                                                     |
| `30002` | `maskDetected`    | The biometric SDK detected that the user was wearing a mask or covering parts of their face.                  | Ask the user to retry authentication and make sure they are in an environment with proper lighting and no obstruction.                                                                                                                                                                                                                                                                                                     |
| `30003` | `userCancelled`   | The user canceled the action.                                                                                 | Avoid showing this as an error because the user canceled authentication voluntarily. Return the user to the screen from which the PingOne Recognize SDK was started.                                                                                                                                                                                                                                                       |
| `30004` | `faceNotMatching` | The biometric SDK could not confirm that the presented face matches the face of the enrolled user.            | Ask the user to retry authentication. If the problem persists, re-enroll the user on the mobile SDK client side. If you use client shared state, synchronize the original user face again with `withTemporaryState` (see [Client State](../mobile-sdk/mobile-sdk-enrollment.html)). If you do not use client state, re-enroll the user with plain enrollment (see [Enrollment](../mobile-sdk/mobile-sdk-enrollment.html)). |
| `30006` | `deviceTampered`  | The user's device is rooted or jailbroken.                                                                    | Inform the user that a non-official operating system was detected. Optionally, disable this check or require a non-modified device.                                                                                                                                                                                                                                                                                        |
| `30007` | `User lockedOut`  | The user failed too many consecutive authentication attempts.                                                 | Inform the user that they reached the rate limit. The SDK provides the remaining lockout time. The rate limiting policy is configurable through the [Lockout Policy](../mobile-sdk/mobile-sdk-lockout-policy.html).                                                                                                                                                                                                        |

| Code               | Error                               | Explanation                                                                                                            | Guidelines for integrators                                                              |
| ------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `20000`            | `userNotEnrolled`                   | The integrator tried to start an action requiring authentication, or to de-enroll, without being enrolled.             | Make sure an enrolled user exists before calling authentication and de-enrollment.      |
| `20001`            | `userAlreadyEnrolled`               | A device already connected to an enrolled user was used to enroll another user.                                        | Use `validateUserAndDeviceActive` to check if a user is already enrolled on the device. |
| `20002` on iOS     | `storageFailed`                     | FileManager failed to handle the PingOne Recognize folder.                                                             | Make sure device storage can be read and written.                                       |
| `20002` on Android | `sdkNotConfigured`                  | The integrator did not call `Keyless.configure`.                                                                       | Repeat the action after configuring the mobile SDK.                                     |
| `20003` on iOS     | `keychainFailed`                    | Keychain failed to delete the device key (`coreDatabaseSymmetricKey`).                                                 | If the issue persists, contact PingOne Recognize support.                               |
| `20003` on Android | `invalidBackupData`                 | Invalid `backupData` returned from Core during `generate_backup`, or an issue reading saved data from iCloud or Drive. | Try re-generating the backup to verify it can be parsed correctly.                      |
| `20004` on iOS     | `extractingEmbeddingsFailed`        | Generic error used to wrap biometric SDK errors.                                                                       | Repeat the action.                                                                      |
| `20004` on Android | `invalidBackupKey`                  | Invalid `backupKey` returned from Core during `generate_backup`, or an issue reading saved data from Drive or iCloud.  | Make sure a valid backup key is passed to the mobile SDK.                               |
| `20005` on iOS     | `configurationFailed`               | Configuration failed.                                                                                                  | Make sure enough disk space is available to write the configuration file.               |
| `20006`            | `invalidAPIKey`                     | The API key is not valid.                                                                                              | Make sure you are using a valid SDK key.                                                |
| `20007` on iOS     | `notEnoughAPIKeySeats`              | The API key is not valid.                                                                                              | Make sure you are using a valid SDK key.                                                |
| `20008`            | `operationFailed`                   | The core action dequeue failed.                                                                                        | Check service logs and retry.                                                           |
| `20010` on Android | `configurationFailed`               | Configuration failed.                                                                                                  | Make sure enough disk space is available to write the configuration file.               |
| `20010` on iOS     | `invalidUserInfo`                   | `userInfo` is not readable or is invalid.                                                                              | Validate the user info payload before calling the SDK.                                  |
| `20012`            | `invalidAPIKey`                     | The API key is not valid.                                                                                              | Make sure you are using a valid SDK key.                                                |
| `20013` on Android | `notEnoughAPIKeySeats`              | The API key was misused.                                                                                               | Make sure you are using a valid SDK key.                                                |
| `20017`            | `deviceDataCorrupted`               | Misconfiguration in a multidevice field.                                                                               | If the issue persists, remove and re-add the second device.                             |
| `20019` on Android | `invalidUserInfo`                   | `userInfo` is not readable or is invalid.                                                                              | Validate the user info payload and retry.                                               |
| `20150`            | `sdkDynamicLinkingMalformedPayload` | The payload does not conform to the JSON schema.                                                                       | Validate payload shape before sending it to the SDK.                                    |

## Alerts

PingOne Recognize recommends the following alerts to monitor an on-premises instance:

* `{{service.name}} Production alert`: Trigger when the error log count over a specific period exceeds a configurable threshold. Example: more than 20 error logs over 5 minutes.

* `Cannot start {{service.name}} on {{host.name}}`: Trigger when the application instance fails to start.

* `AuthVault - isSignatureValid error`: Trigger when a signature format in auth vault is valid but the signature cannot be validated. This indicates possible key tampering and should theoretically never trigger.

## Scaling the cluster

The PingOne Recognize system was tested on the following setup:

* Google Cloud Platform (GCP)

* OCP 4.14.5

* PingOne Recognize 1.0.3

* Two `n2-standard-4` worker nodes

* One `n2-standard-4` master node

A `c2-standard-8` machine was used to generate load from the benchmarking tool. It was created inside the VPC to neutralize latency and networking variables.

Kubernetes pods for each service were configured with the following limits:

* circuit-storage: `cpu: 1`, `memory: 2000Mi`

* auth-vault: `cpu: 1800m`, `memory: 2Gi`

* core-daemon: `cpu: 1800m`, `memory: 2Gi`

* node-persistence: `cpu: 1800m`, `memory: 2Gi`

* operations-service: `cpu: 1500m`, `memory: 2Gi`

Deployments were configured to scale up to a maximum of 3 pods per service.

The cluster was running only PingOne Recognize code and OCP standard tools.

The scaling test simulated 10 users performing 30 consecutive authentications. Overall concurrency was set to 8.

```text
END AUTH AT 20240528_102705
Device auth time: NumEntries=240 Average=1.562500 Median=1.000000 StDev=0.729138 Min=1.000000 Max=4.000000 P95=3.000000 P99=4.000000
User auth time: NumEntries=240 Average=220.683333 Median=202.500000 StDev=57.430618 Min=149.000000 Max=561.000000 P95=341.950000 P99=395.000000
Send circ time: NumEntries=240 Average=1070.458333 Median=1068.000000 StDev=100.111352 Min=875.000000 Max=1380.000000 P95=1257.850000 P99=1339.390000
Total time: NumEntries=240 Average=1293.916667 Median=1275.500000 StDev=127.563953 Min=1059.000000 Max=1686.000000 P95=1536.800000 P99=1650.390000
Num Auth OK: 8
Num Auth FAIL: 0
```

The previous results show a p95 under 500 msec for `User auth time`, which is the duration experienced by the simulated end user.

Also consider database connections. Services are currently configured to use 4 connections each. When scaling to 3 pods, total connections are:

`4 (connections) * 3 (pods) * 2 (services) = 24`

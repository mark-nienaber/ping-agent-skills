---
title: AWS Secrets Manager Connector
description: Configure the AWS Secrets Manager connector in PingOne DaVinci to retrieve, create, update, and delete secrets stored in AWS Secrets Manager
component: connectors
page_id: connectors::aws_secrets_manager_connector
canonical_url: https://docs.pingidentity.com/connectors/aws_secrets_manager_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-01T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-aws-secrets-manager-connector: Configuring the AWS Secrets Manager connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  retrieving-a-secret: Retrieving a secret
  creating-a-secret: Creating a secret
  updating-a-secret: Updating a secret
  deleting-a-secret: Deleting a secret
  capabilities: Capabilities
  getSecret: Get Secret
  createSecret: Create Secret
  updateSecret: Update Secret
  deleteSecret: Delete Secret
---

# AWS Secrets Manager Connector

The AWS Secrets Manager connector lets you retrieve, create, update, and delete secrets stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) in your PingOne DaVinci flow.

You can use the connector to externalize secrets such as API keys and client credentials, so you don't need to store them directly in your flow configuration. For example, use the connector to retrieve a secret and pass it into the **Make REST API Call** capability of the HTTP connector instead of hardcoding the credential in the flow.

## Setup

### Resources

You can find more information and setup help in the following:

* AWS documentation:

  * [Getting started with AWS Secrets Manager](https://aws.amazon.com/secrets-manager/getting-started/)

  * [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager)

  * [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

  * [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

  * [Permissions to access secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html#auth-and-access_secrets)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An AWS account with access to AWS Secrets Manager.

* An AWS IAM access key ID and secret access key with permissions to read and, optionally, create, update, and delete the secrets you plan to use. Follow AWS guidance to use least-privilege permissions, avoid root credentials, and store access keys securely.

* The AWS Region your secrets are stored in.

* Optionally, a second AWS access key ID, secret access key, and region if you want the connector to fail over to a secondary AWS account or region when the primary request fails.

### Configuring the AWS Secrets Manager connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                         | Description                                                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **AWS Access Key**              | The AWS IAM access key ID used to authenticate with AWS Secrets Manager.                                         |
| **AWS Access Secret**           | The AWS IAM secret access key paired with the **AWS Access Key**.                                                |
| **AWS Region**                  | The AWS Region your secrets are stored in.                                                                       |
| **Secondary AWS Access Key**    | Optional. A fallback AWS IAM access key ID the connector uses if the primary request times out or can't connect. |
| **Secondary AWS Access Secret** | Optional. The AWS IAM secret access key paired with the **Secondary AWS Access Key**.                            |
| **Secondary AWS Region**        | Optional. A fallback AWS Region the connector uses if the primary request times out or can't connect.            |

## Using the connector in a flow

### Retrieving a secret

Use the **Get Secret** capability to retrieve the current value of a secret by its name or ARN. If a secondary AWS configuration is set and the primary request fails, the connector retries the request using the secondary AWS Access Key, AWS Access Secret, and AWS Region. Treat secret values as sensitive data. Do not log them, expose them in user-facing responses, or return them from a flow unless required for the intended integration. The capability outputs whether the primary or secondary configuration was used.

### Creating a secret

Use the **Create Secret** capability to create a new secret. You can optionally set a description, encrypt the secret with a specific **KMS Key ID**, overwrite an existing secret of the same name, and recover a soft-deleted secret before setting its new value.

### Updating a secret

Use the **Update Secret** capability to update the value, description, or KMS key of an existing secret.

### Deleting a secret

Use the **Delete Secret** capability to mark a secret for deletion. The secret remains recoverable during AWS's configured recovery window, which defaults to 30 days.

## Capabilities

### Get Secret

Fetch the stored value of a secret

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Secret Name / ARN textField required
>
>   The name or ARN of the secret
>
> * default object
>
>   * properties object
>
>     * secretName string required
>
>       The name of the secret to get
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "secretName": "MySecret"
>   }
> }
> ```
>
> * output object
>
>   * secret string
>
>   * usedPrimaryConfiguration boolean
>
>   * response object
>
>     * $metadata object
>
>       * httpStatusCode integer
>
>       * requestId string
>
>       * attempts integer
>
>       * totalRetryDelay integer
>
>     * ARN string
>
>     * CreatedDate string
>
>     * Name string
>
>     * SecretString string
>
>     * VersionId string
>
>     * VersionStages array
>
>       * Array Item Schema string

### Create Secret

Create a new secret

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Secret Name / ARN textField required
>
>   The name or ARN of the secret
>
> - Secret Value textField required
>
>   The secret value
>
> - Description textField
>
>   A description of the secret
>
> - KMS Key ID textField
>
>   The KMS Key ID, or ARN/alias ARN of the KMS key used to encrypt the secret
>
> - Overwrite if exists toggleSwitch
>
>   Whether to overwrite the secret if it already exists.
>
> - Recover Soft Delete toggleSwitch
>
>   Whether to recover the secret first if it has been deleted and is still recoverable.
>
> * default object
>
>   * properties object
>
>     * secretName string required
>
>       The name of the secret to create
>
>     * secretValue string required
>
>       The value of the secret to create
>
>     * secretDescription string
>
>       The description of the secret
>
>     * kmsKeyId string
>
>       The KMS Key ID, or ARN/alias ARN of the KMS key used to encrypt the secret
>
>     * overwriteIfExists boolean
>
>       Whether to overwrite an existing secret with the same name.
>
>     * recoverFromSoftDelete boolean
>
>       Whether to recover the secret first if it has been soft-deleted and is still recoverable.
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "secretName": "MySecret",
>     "secretValue": "ThisIsASecret",
>     "secretDescription": "I need to store the MySecret secret, overwrite it if it already exists, and not recover it if it has been deleted.",
>     "kmsKeyId": "MyKeyID",
>     "overwriteIfExists": true,
>     "recoverFromSoftDelete": false
>   }
> }
> ```
>
> * output object
>
>   * usedPrimaryConfiguration boolean
>
>   * response object
>
>     * $metadata object
>
>       * httpStatusCode integer
>
>       * requestId string
>
>       * attempts integer
>
>       * totalRetryDelay integer
>
>     * ARN string
>
>     * Name string
>
>     * VersionId string

### Update Secret

Updates the description, value, or KMS key of an existing secret

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Secret Name / ARN textField required
>
>   The name or ARN of the secret
>
> - Secret Value textField required
>
>   The secret value
>
> - Description textField
>
>   A description of the secret
>
> - KMS Key ID textField
>
>   The KMS Key ID, or ARN/alias ARN of the KMS key used to encrypt the secret
>
> * default object
>
>   * properties object
>
>     * secretName string required
>
>       The name of the secret to update
>
>     * secretValue string required
>
>       The value of the secret to store
>
>     * secretDescription string
>
>       The description of the secret
>
>     * kmsKeyId string
>
>       The KMS Key ID, or ARN/alias ARN of the KMS key used to encrypt the secret
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "secretName": "MySecret",
>     "secretValue": "ThisIsAnUpdatedSecret",
>     "secretDescription": "I need to update the value and description of MySecret"
>   }
> }
> ```
>
> * output object
>
>   * usedPrimaryConfiguration boolean
>
>   * response object
>
>     * $metadata object
>
>       * httpStatusCode integer
>
>       * requestId string
>
>       * attempts integer
>
>       * totalRetryDelay integer
>
>     * ARN string
>
>     * Name string
>
>     * VersionId string

### Delete Secret

Schedules a secret for deletion. The secret remains recoverable during AWS's configured recovery window, which defaults to 30 days.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Secret Name / ARN textField required
>
>   The name or ARN of the secret
>
> * default object
>
>   * properties object
>
>     * secretName string required
>
>       The name of the secret to delete
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "secretName": "MySecret"
>   }
> }
> ```
>
> * output object
>
>   * usedPrimaryConfiguration boolean
>
>   * response object
>
>     * $metadata object
>
>       * httpStatusCode integer
>
>       * requestId string
>
>       * attempts integer
>
>       * totalRetryDelay integer
>
>     * ARN string
>
>     * DeletionDate string
>
>     * Name string
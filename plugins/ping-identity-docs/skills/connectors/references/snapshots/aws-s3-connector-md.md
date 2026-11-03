---
title: AWS S3 Connector
description: Configure the AWS S3 connector in PingOne DaVinci to upload, retrieve, and delete objects in an Amazon S3 bucket
component: connectors
page_id: connectors::aws_s3_connector
canonical_url: https://docs.pingidentity.com/connectors/aws_s3_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-01T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-aws-s3-connector: Configuring the AWS S3 connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  storing-an-object-in-a-bucket: Storing an object in a bucket
  retrieving-an-object-from-a-bucket: Retrieving an object from a bucket
  deleting-an-object-from-a-bucket: Deleting an object from a bucket
  capabilities: Capabilities
  getObject: Get Object
  putObject: Put Object
  deleteObject: Delete Object
---

# AWS S3 Connector

The AWS S3 connector lets you manage objects in [Amazon S3](https://aws.amazon.com/s3/) buckets, including uploading, retrieving, and deleting them from your PingOne DaVinci flow.

The connector authenticates by exchanging a PingOne access token for temporary AWS credentials, so you don't need to store long-term AWS access keys.

## Setup

### Resources

You can find more information and setup help in the following:

* AWS documentation:

  * [Amazon S3 API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

  * [AWS SDK for JavaScript S3Client Reference](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A PingOne application configured for the client credentials grant type. The connector uses this application's client ID and client secret to request an access token from PingOne.

* An AWS IAM role that trusts your PingOne environment as a web identity provider and grants the permissions required for the actions you plan to use, such as s3:GetObject, s3:PutObject, or s3:DeleteObject.

* The Amazon Resource Name (ARN) of that IAM role.

* The AWS Region where your S3 bucket is located.

### Configuring the AWS S3 connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                   | Description                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------- |
| **PingOne Client ID**     | The client ID of the PingOne application the connector uses to request an access token.     |
| **PingOne Client Secret** | The client secret of the PingOne application the connector uses to request an access token. |
| **PingOne Region**        | The PingOne region for your environment.                                                    |
| **AWS Role ARN**          | The ARN of the AWS IAM role the connector assumes using the PingOne access token.           |
| **AWS Region**            | The AWS Region where your S3 bucket is located.                                             |

## Using the connector in a flow

### Storing an object in a bucket

Use the **Put Object** capability to upload an object to your S3 bucket. Set the **Content Type Selection** so the connector encodes the **Object Data** correctly: image content as base64 and text content as plain text.

### Retrieving an object from a bucket

Use the **Get Object** capability to download an object from your S3 bucket. The connector returns image content as base64 and text content as plain text. It doesn't retrieve objects larger than 10 MB.

### Deleting an object from a bucket

Use the **Delete Object** capability to remove an object from your S3 bucket.

## Capabilities

### Get Object

Retrieves an object from a specified bucket.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Bucket Name textField required
>
>   Name of the AWS bucket
>
> - Object Key textField
>
>   Key associated with the corresponding object
>
> * default object
>
>   * properties object
>
>     * pingOneClientId string required
>
>       PingOne Client ID
>
>     * pingOneClientSecret string required
>
>       PingOne Client Secret
>
>     * pingOneRegion string required
>
>       PingOne Region
>
>     * awsRoleARN string required
>
>       The ARN of the AWS IAM role that will be assumed using STS with the PingOne issued OIDC Token.
>
>     * awsRegion string required
>
>       AWS Region
>
>     * bucket string required
>
>       Name of bucket
>
>     * key string required
>
>       Key associated with the corresponding Object
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * bucketObject object

### Put Object

Uploads an object to a specified bucket.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Bucket Name textField required
>
>   Name of the AWS bucket
>
> - Object Key textField
>
>   Key associated with the corresponding object
>
> - Object Data textField
>
>   Content that will be uploaded to the S3 bucket
>
> - Content Type Selection dropDown required
>
>   The MIME type of the object being uploaded
>
>   * image/jpeg
>
>   * image/png
>
>   * text/plain
>
>   * text/html
>
> * default object
>
>   * properties object
>
>     * pingOneClientId string required
>
>       PingOne Client ID
>
>     * pingOneClientSecret string required
>
>       PingOne Client Secret
>
>     * pingOneRegion string required
>
>       PingOne Region
>
>     * awsRoleARN string required
>
>       The ARN of the AWS IAM role that will be assumed using STS with the PingOne issued OIDC Token.
>
>     * awsRegion string required
>
>       AWS Region
>
>     * bucket string required
>
>       Name of bucket
>
>     * key string required
>
>       Key associated with the corresponding Object
>
>     * content string required
>
>       Uploads object to S3 bucket
>
>     * contentTypeSelection string required
>
>       Content Type selection
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number

### Delete Object

Deletes an object from a specified bucket.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Bucket Name textField required
>
>   Name of the AWS bucket
>
> - Object Key textField
>
>   Key associated with the corresponding object
>
> * default object
>
>   * properties object
>
>     * pingOneClientId string required
>
>       PingOne Client ID
>
>     * pingOneClientSecret string required
>
>       PingOne Client Secret
>
>     * pingOneRegion string required
>
>       PingOne Region
>
>     * awsRoleARN string required
>
>       The ARN of the AWS IAM role that will be assumed using STS with the PingOne issued OIDC Token.
>
>     * awsRegion string required
>
>       AWS Region
>
>     * bucket string required
>
>       Name of bucket
>
>     * key string required
>
>       Key associated with the corresponding Object
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
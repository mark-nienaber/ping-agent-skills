---
title: identitycloud-go-client (Go)
description: Use the PingOne Advanced Identity Cloud Go SDK to connect your Go application to your Advanced Identity Cloud deployment.
component: config-automation-management-sdks
page_id: config-automation-management-sdks::products/pingone_advanced_identity_cloud/languages/go/getting_started
canonical_url: https://developer.pingidentity.com/config-automation-management-sdks/products/pingone_advanced_identity_cloud/languages/go/getting_started.html
revdate: March 19, 2025
section_ids:
  prerequisites: Prerequisites
  getting-started: Getting started
  connect-to-the-service: Connect to the service
  service-account: Service account
  more-information: More information
---

# identitycloud-go-client (Go)

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `identitycloud-go-client` SDK has not yet been released to version 1.0.0. Although general use of the SDK is not expected to change and is stable, later versions could contain minor changes to package and function names. |

Use the PingOne Advanced Identity Cloud Go SDK to connect your Go application to your Advanced Identity Cloud deployment.

The [identitycloud-go-client](https://github.com/pingidentity/identitycloud-go-client) module provides API bindings to the Advanced Identity Cloud configuration API, allowing developers to invoke API services simply using strongly typed request and response payloads. The module can be included as a dependency in developer code.

|   |                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `identitycloud-go-client` module currently only supports tenant management APIs described at [Advanced Identity Cloud API](https://docs.pingidentity.com/pingoneaic/latest/_attachments/api/) documentation. |

## Prerequisites

The `identitycloud-go-client` module requires a valid Advanced Identity Cloud tenant to be provisioned and accessible.

## Getting started

The following example shows how to include the `identitycloud-go-client` module in a developer project.

If you haven't done so already, initialize a new Go module project:

```
go mod init github.com/mygithubuser/my-go-project
```

Use the standard Go commands to install `identitycloud-go-client` to the project:

```
go get github.com/pingidentity/identitycloud-go-client
```

## Connect to the service

The following sections describe the available options to connect the configuration management SDK to the Advanced Identity Cloud service.

### Service account

When connecting to the Advanced Identity Cloud service, a service account that has been provisioned access the required API features must be used.

Learn more about the Identity Cloud REST API, how to configure access using service accounts and find the complete list of available scopes at the [Advanced Identity Cloud Service accounts](https://docs.pingidentity.com/pingoneaic/latest/tenants/service-accounts.html) documentation.

When initiating the Go client SDK, the service account credentials should be provided with the list of scopes the application needs, as shown in the following example:

```go
package main

import (
	"context"
	"fmt"

	"github.com/pingidentity/identitycloud-go-client/identitycloud"
)

func main() {

	aicEnvironmentFqdn := "my-aic-fqdn.id.forgerock.io"
	aicServiceAccountId := "service-account-id-value"
	aicServiceAccountPrivateKey := `{"keys":[{"alg":"RS256","e":"AQAB","n":"....","kty":"RSA","use":"sig"}]}`
	aicServiceAccountScopes := []string{
		"fr:idc:certificate:*",
		"fr:idc:content-security-policy:*",
		"fr:idc:cookie-domain:*",
		"fr:idc:custom-domain:*",
		"fr:idc:esv:*",
		"fr:idc:promotion:*",
		"fr:idc:sso-cookie:*",
	}

	// Initialize the API client
	clientConfig := identitycloud.NewConfiguration()
	clientConfig.Servers = identitycloud.ServerConfigurations{
		{
			URL: fmt.Sprintf("https://%s", aicEnvironmentFqdn),
		},
	}

	apiClient := identitycloud.NewAPIClient(clientConfig)

	// Set OAuth 2.0 credentials in the Go context
	oauth2AuthContext := context.WithValue(context.Background(), identitycloud.ContextOAuth2, identitycloud.ServiceAccountTokenSource{
		TenantFqdn:               aicEnvironmentFqdn,
		ServiceAccountId:         aicServiceAccountId,
		ServiceAccountPrivateKey: aicServiceAccountPrivateKey,
		Scopes:                   aicServiceAccountScopes,
	})

	// Call an API from the `apiClient` object
	readResponse, httpResponse, err := apiClient.PromotionAPI.CheckLock(oauth2AuthContext).Execute()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Response HTTP Code: %d", httpResponse.StatusCode)
	fmt.Printf("Response: %v", readResponse)
}
```

## More information

* [PingOne Advanced Identity Cloud documentation](https://docs.pingidentity.com/pingoneaic/latest/overview.html)

* [`identitycloud-go-client` on the Go Package Repository](https://pkg.go.dev/github.com/pingidentity/identitycloud-go-client/identitycloud)

* [`identitycloud-go-client` on GitHub](https://github.com/pingidentity/identitycloud-go-client)

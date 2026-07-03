---
title: Advanced Identity Cloud REST API custom headers
description: in the X-Client-Region header to enforce MFA in a sign-on journey for clients originating from a specific country or set of countries.
component: pingoneaic-api
page_id: pingoneaic-api::api-custom-headers
canonical_url: https://developer.pingidentity.com/pingoneaic-api/api-custom-headers.html
revdate: you might use the country code
section_ids:
  debugging: Debugging
  client-ip-addresses: Client IP addresses
  client-geolocation: Client geolocation
  other: Other
---

# Advanced Identity Cloud REST API custom headers

in the [X-Client-Region](#x-client-region) header to enforce MFA in a sign-on journey for clients originating from a specific country or set of countries.

## Debugging

* X-ForgeRock-TransactionID

  This header contains a unique value, such as `f89da9de-22f4-4e0b-8527-26b8d9c53d7b-request-1/0`, that can be used to identify the current request and correlate it with Advanced Identity Cloud log entries from all log sources. Learn more in [Filter logs for a specific request](https://docs.pingidentity.com/pingoneaic/latest/tenants/audit-debug-logs.html#filter-logs-for-a-specific-request).

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud adds a similar header `X-Cloud-Trace-Context` for tracing requests. This is used internally by the Ping Identity support team. It's also deprecated, so you shouldn't use this header in your integrations. |

## Client IP addresses

* X-Forwarded-For

  This header contains a comma-separated list of originating IP addresses for the client.

  * If the request doesn't have an `X-Forwarded-For` header set before it connects to the tenant environment load balancer, the header is added to the request and contains the following IP addresses:

    ```
    X-Forwarded-For: <client-ip-address>, <load-balancer-ip-address>
    ```

    * `<client-ip-address>` is the IP address of the client when it connects to the tenant environment load balancer.

    * `<load-balancer-ip-address>` is the IP address of the tenant environment load balancer.

  * If the request already has an `X-Forwarded-For` header set before it connects to the tenant environment load balancer, the header is modified to contain the following IP addresses:

    ```
    X-Forwarded-For: <existing-ip-address>, <client-ip-address>, <load-balancer-ip-address>
    ```

    * `<existing-ip-address>` is the IP address the `X-Forwarded-For` header contains when the client connects to the tenant environment load balancer.

    * `<client-ip-address>` is the IP address of the client when it connects to the tenant environment load balancer.

    * `<load-balancer-ip-address>` is the IP address of the tenant environment load balancer.

  |   |                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | There are security and privacy concerns associated with the use of this header. Learn more in the MDN doc [X-Forwarded-For](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For). |

- X-Trusted-Forwarded-For

  This header contains a comma-separated list of trusted IP addresses for the client:

  ```
  X-Trusted-Forwarded-For: <trusted-ip-address>, <client-ip-address>, <load-balancer-ip-address>
  ```

  * `<trusted-ip-address>` is a trusted client IP address, verified by Ping Identity.

  * `<client-ip-address>` is the IP address of the client when it connects to the tenant environment load balancer.

  * `<load-balancer-ip-address>` is the IP address of the tenant environment load balancer.

* X-Real-IP

  This header contains a trusted client IP address, verified by Ping Identity:

  ```
  X-Real-IP: <trusted-ip-address>
  ```

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For the `X-Trusted-Forwarded-For` and `X-Real-IP` headers, if the client is behind a reverse proxy, the trusted client IP address contains the real IP address of the reverse proxy, not the client. |

Learn more in [Identify originating client IP addresses](https://docs.pingidentity.com/pingoneaic/latest/planning/plan-security.html#identify-originating-client-ip-addresses).

## Client geolocation

* X-Client-Region

  This header contains the country (or region) associated with the client's IP address in the form of a two-letter region code, such as `US` or `FR`. For most countries, these region codes correspond directly to ISO-3166-2 codes.

- X-Client-City

  This header contains the name of the city where the client request originated. For example, `Mountain View` for Mountain View, California. There's no canonical list of valid values for this header. The city names can contain ASCII letters, numbers, spaces, and the following characters: ``"!#$%&'*+-.^_`|~"``.

* X-Client-City-Lat-Long

  This header contains the latitude and longitude of the city where the client request originated. For example, `37.386051,-122.083851` for a request from Mountain View.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For the `X-Client-Region`, `X-Client-City` and `X-Client-City-Lat-Long` headers, if the client is behind a reverse proxy, the geolocation information represents the reverse proxy, not the client. If you require greater accuracy, Ping Identity recommends that you integrate an IP lookup service into your end-user journeys. |

Learn more in [Identify client geolocation](https://docs.pingidentity.com/pingoneaic/latest/planning/plan-security.html#identify-client-geolocation).

## Other

* X-Forwarded-Proto

  This header contains the HTTP protocol the client used to connect to the tenant environment load balancer. Possible values are `http` or `https`. Learn more in the MDN doc [X-Forwarded-Proto](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For).

- X-Requested-With

  This header contains the name of the originating web technology or platform. For example, most JavaScript frameworks set the value as `XMLHttpRequest`. The header can be used to influence application behavior. For example, returning HTML data by default but returning JSON data for requests that set the value as `XMLHttpRequest`. The header can also be used to protect against CSRF attacks. Learn more in [CSRF attacks](https://docs.pingidentity.com/pingoneaic/latest/planning/plan-security.html#csrf-attacks).

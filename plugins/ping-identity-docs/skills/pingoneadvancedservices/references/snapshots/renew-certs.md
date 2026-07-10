---
title: Renewing Let&#8217;s Encrypt certificates
description: To ensure that communications between PingOne Advanced Services products and services remain encrypted and secure, Let's Encrypt certificate chains are used by default. These chains verify that the sender and all certificate authority (CA) certificates in the chain are trustworthy. Learn more about how these certificate chains work in How it Works in the Let's Encrypt documentation.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:renew_certs:p1as_renew_cert
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/renew_certs/p1as_renew_cert.html
revdate: January 23, 2025
section_ids:
  adding-the-root-ca-to-the-client-truststore: Adding the root CA to the client truststore
  on-premise-non-ping-identity-client-applications: On-premise, non-Ping Identity client applications
  on-premise-pingdirectory-pingdirectoryproxy-and-pingdatasync: On-premise PingDirectory, PingDirectoryProxy, and PingDataSync
  on-premise-pingaccess-agent: On-premise PingAccess Agent
---

# Renewing Let's Encrypt certificates

To ensure that communications between PingOne Advanced Services products and services remain encrypted and secure, Let's Encrypt certificate chains are used by default. These chains verify that the sender and all certificate authority (CA) certificates in the chain are trustworthy. Learn more about how these certificate chains work in [How it Works](https://letsencrypt.org/how-it-works/) in the Let's Encrypt documentation.

For PingOne Advanced Services, the Let's Encrypt certificate chain consists of three different certificates:

* The Advanced Services end-entity certificate

  The chain begins with an RSA 2048-bit end-entity certificate issued by Let's Encrypt, which is signed by the intermediate CA.

  This certificate expires every 90 days, but PingOne Advanced Services rotates every 60 days to avoid expiration overlap, by default. Avoid adding this certificate to your truststore because it rotates so often.

* The R10 or R11 intermediate CA

  This certificate, next in the chain, is signed by the root CA.

  These certificates expire every 3 years. Avoid adding them to your truststore as well. Because they sign the end-entity certificate, and that certificate rotates every 60 days, you would have to maintain both versions of the certificates for the chain to work.

* The ISRG Root X1 root CA

  The chain ends with the root CA certificate, which is self-signed.

  This certificate will expire in 2035, and every 20 years after that, so you don't need to worry about renewing it for several years.

  |   |                                                                                           |
  | - | ----------------------------------------------------------------------------------------- |
  |   | You'll receive many updates regarding the ISRG Root X1 Root CA before it expires in 2035. |

You must add the root CA to your client truststore for the certificate chain to work. You can find instructions below.

Learn more about how these certificates keep customer client applications and PingOne Advanced Services server applications secure in this network diagram:

> **Collapse: Network diagram**
>
> ![A network diagram that displays the customer client applications and the PingOne Advanced Services server applications.](_images/p1as_server_apps.bmp)

## Adding the root CA to the client truststore

Add the root CA to your client truststore to ensure the certificate chain will work.

### On-premise, non-Ping Identity client applications

To add the root CA to your on-premise, non-Ping Identity client application:

1. Download the [ISRG Root X1 Certificate](https://letsencrypt.org/certs/isrgrootx1.pem) from Let's Encrypt.

2. Add the root CA to your truststore. Refer to your application documentation for instructions.

### On-premise PingDirectory, PingDirectoryProxy, and PingDataSync

To add the root CA to your on-premise PingDirectory application and its PingDirectory instance clients, open a terminal window and enter the following:

```
# 1) Download "ISRG Root X1" Root CA from Let's Encrypt to /tmp directory
$ curl https://letsencrypt.org/certs/isrgrootx1.pem -o /tmp/pingone-advanced-services-root-ca.pem
# 2) Add "ISRG Root X1" Root CA to truststore
$ bin/manage-certificates \
  import-certificate \
  --keystore config/truststore \
  --keystore-password-file config/truststore.pin \
  --alias "pingone-advanced-services-isrg-root-x1-ca-expires-2035" \
  --certificate-file /tmp/pingone-advanced-services-root-ca.pem --no-prompt
# 3) Remove "ISRG Root X1" Root CA resource from server /tmp directory
$ rm -o /tmp/pingone-advanced-services-root-ca.pem
```

### On-premise PingAccess Agent

To add the root CA to your on-premise, PingAccess Agent application:

1. Download the [ISRG Root X1 Certificate](https://letsencrypt.org/certs/isrgrootx1.pem) from Let's Encrypt.

2. Add the root CA to your truststore. You can find instructions in [Rotating a CA](https://docs.pingidentity.com/pingaccess/latest/agents_and_integrations/pa_nginx_rotating_a_ca.html) in the PingAccess documentation.
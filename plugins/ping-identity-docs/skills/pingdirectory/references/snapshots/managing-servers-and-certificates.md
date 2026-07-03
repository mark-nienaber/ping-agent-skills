---
title: About representing certificates, private keys, and certificate signing requests
description: X.509 is an encoding format that uses the ASN.1 distinguished encoding rules (DER), which exist in binary format. When writing a certificate to a file, either a raw DER format or a plain-text format called PEM can be used.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_servers_and_certificates:pd_ds_rep_certs_pvt_keys_cert_signing_reqs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_servers_and_certificates/pd_ds_rep_certs_pvt_keys_cert_signing_reqs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# About representing certificates, private keys, and certificate signing requests

X.509 is an encoding format that uses the ASN.1 distinguished encoding rules (DER), which exist in binary format. When writing a certificate to a file, either a raw DER format or a plain-text format called PEM can be used.

PEM encoding consists of a line that contains the text `-----BEGIN CERTIFICATE-----`, followed by a set of lines that contains the base64-encoded representation of the raw DER bytes (typically with no more than 64 characters per line), followed by a line that contains the text `-----END CERTIFICATE-----`.

The X.509 encoding contains a certificate's public key, but not its private key. The PKCS #8 specification in [RFC 5958](https://www.ietf.org/rfc/rfc5958.txt) describes the encoding for private keys. This approach uses a DER encoding with a PEM variant that instead uses the following header and footer, respectively.

```
 -----BEGIN PRIVATE KEY-----
-----END PRIVATE KEY-----
```

RFC 5958 also describes an encrypted representation of the private key, but that format is currently unsupported.

The PKCS #10 specification in [RFC 2986](https://www.ietf.org/rfc/rfc2986.txt) describes the CSR format. This format uses a DER encoding with a PEM variant that uses the following header and footer, respectively.

```
-----BEGIN CERTIFICATE REQUEST-----
-----END CERTIFICATE REQUEST-----
```

Some implementations use the following alternate, nonstandard forms.

```
-----BEGIN NEW CERTIFICATE REQUEST-----
-----END NEW CERTIFICATE REQUEST-----
```

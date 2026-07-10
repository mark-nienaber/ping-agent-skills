---
title: About this reference
description: This reference covers PingDS tools, which are bundled with the software. For the dsconfig command, also see the Configuration reference.
component: pingds
version: 8.1
page_id: pingds:tools-reference:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# About this reference

This reference covers PingDS tools, which are bundled with the software. For the `dsconfig` command, also see the [Configuration reference](../configref/preface.html).

* [addrate](addrate.html)

* [authrate](authrate.html)

* [backendstat](backendstat.html)

* [base64](base64.html)

* [changelogstat](changelogstat.html)

* [create-rc-script](create-rc-script.html)

* [dsbackup](dsbackup.html)

* [dsconfig](dsconfig.html)

* [dskeymgr](dskeymgr.html)

* [dsrepl](dsrepl.html)

* [encode-password](encode-password.html)

* [export-ldif](export-ldif.html)

* [import-ldif](import-ldif.html)

* [ldapcompare](ldapcompare.html)

* [ldapdelete](ldapdelete.html)

* [ldapmodify](ldapmodify.html)

* [ldappasswordmodify](ldappasswordmodify.html)

* [ldapsearch](ldapsearch.html)

* [ldifdiff](ldifdiff.html)

* [ldifmodify](ldifmodify.html)

* [ldifsearch](ldifsearch.html)

* [makeldif-template](makeldif-template.html)

* [makeldif](makeldif.html)

* [manage-account](manage-account.html)

* [manage-tasks](manage-tasks.html)

* [modrate](modrate.html)

* [rebuild-index](rebuild-index.html)

* [searchrate](searchrate.html)

* [setup-profile](setup-profile.html)

* [setup](setup.html)

* [start-ds](start-ds.html)

* [status](status.html)

* [stop-ds](stop-ds.html)

* [supportextract](supportextract.html)

* [upgrade](upgrade.html)

* [verify-index](verify-index.html)

* [windows-service](windows-service.html)

---

---
title: addrate
description: addrate — measure add and delete throughput and response time
component: pingds
version: 8.1
page_id: pingds:tools-reference:addrate
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/addrate.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  addrate-description: Description
  addrate-options: Options
  exit_codes: Exit codes
  addrate-examples: Examples
---

# addrate

`addrate` — measure add and delete throughput and response time

## Synopsis

`addrate {options} template-file-path`

## Description

This utility can be used to measure add and optionally delete throughput and response time of a directory server using user-defined entries. The {template-file-path} argument identifies a template file that has the same form as a template file for the makeldif command.

Examples:

This example adds entries and randomly deletes them while the number of entries added is greater than 10,000:

addrate -p 1636 -Z -X -D uid=admin -w password -f -c 10 -C random -s 10000 addrate.template

This example adds entries and starts to delete them in the same order if their age is greater than a certain time:

addrate -p 1636 -Z -X -D uid=admin -w password -f -c 10 -C fifo -a 2 addrate.template

For details about the template file, see the documentation.

When you do not use the `-f` option to keep connections open and rebind on the connections, the tool can exhaust its available ports, causing the tool to crash. You can work around this problem on test systems by changing TCP settings on the system.

For example, on Linux systems, set the following parameters in the `/etc/sysctl.conf` file:

```
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
```

The parameter `net.ipv4.tcp_fin_timeout` sets the length of time in seconds to wait for a final FIN packet before forcing a close of the socket. The default is 60 (seconds).

The parameter `net.ipv4.tcp_tw_recycle` enables fast recycling of TIME\_WAIT sockets. The default is 0 (false). Enabling this can cause Network Address Translation (NAT) issues.

The parameter `net.ipv4.tcp_tw_reuse` enables reuse of TIME\_WAIT sockets for new connections. The default is 0 (false).

These settings are recommended only for testing, and *not for production systems* .

After making the changes to `/etc/sysctl.conf` , reload the configuration with the `sysctl` command:

```
# sysctl -p
```

## Options

The `addrate` command takes the following options:

Command options:

* `-a | --deleteAgeThreshold {seconds}`

  Specifies the age at which added entries will become candidates for deletion.

* `-B | --warmUpDuration {warmUpDuration}`

  Warm up duration in seconds. Default: 0

* `-c | --numConnections {numConnections}`

  Number of connections. Default: 1

* `-C | --deleteMode {fifo | random | off}`

  The algorithm used for selecting entries to be deleted which must be one of "fifo", "random", or "off". Default: FIFO

* `-d | --maxDuration {maxDuration}`

  Maximum duration in seconds, or unlimited if not specified. Default: 0

* `-e | --percentile {percentile}`

  Calculate max response time for a percentile of operations.

* `-f | --keepConnectionsOpen`

  Keep connections open. Default: false

* `-F | --noRebind`

  Keep connections open and do not rebind. Default: false

* `-g | --constant {name=value}`

  A constant that overrides the value set in the template file.

* `-i | --statInterval {statInterval}`

  Display results each specified number of seconds. Default: 5

* `-m | --maxIterations {maxIterations}`

  Max iterations, 0 for unlimited. Default: 0

* `-M | --targetThroughput {targetThroughput}`

  Target average throughput to achieve. Default: 0

* `-n | --noPurge`

  Disable the purge phase when the tool stops. Default: false

* `-r | --resourcePath {path}`

  Path to look for template resources (e.g. data files). The utility looks for resources in the following locations in this order:

  1. The current directory where the command is run.

  2. The resource path directory.

  3. The built-in files.

* `-R | --randomSeed {seed}`

  The seed to use for initializing the random number generator. To always generate the same data with the same command, use the same non-zero seed value. A value of zero (the default) results in different data each time the tool is run. Default: 0

* `-s | --deleteSizeThreshold {count}`

  Specifies the number of entries to be added before deletion begins. Default: 10000

* `-S | --scriptFriendly`

  Use script-friendly mode. Default: false

* `-t | --numConcurrentRequests {numConcurrentRequests}`

  Number of concurrent requests per connection. Default: 1

* `-Y | --proxyAs {authzID}`

  Use the proxied authorization control with the given authorization ID.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default:

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server port number.

* `-q | --useStartTls`

  Use StartTLS to secure communication with the server. Default: false

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

* `-Z | --useSsl`

  Use SSL for secure communication with the server. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* 80

  The command could not complete due to an input/output error.

* 89

  An error occurred while parsing the command-line arguments.

## Examples

The following example adds entries, and then randomly deletes them when more than 10,000 entries have been added:

```
$ addrate \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --usePkcs12TrustStore /path/to/opendj/config/keystore \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=admin \
 --bindPassword password \
 --numConnections 10 \
 --keepConnectionsOpen \
 --deleteMode random \
 --deleteSizeThreshold 10,000 \
 --maxDuration 30 \
 /path/to/opendj/config/MakeLDIF/addrate.template
--------------------------------------------------------------------------------------
|     Throughput    |                 Response Time                |    Additional   |
|    (ops/second)   |                (milliseconds)                |    Statistics   |
|   recent  average |   recent  average    99.9%   99.99%  99.999% |  err/sec   Add% |
--------------------------------------------------------------------------------------
|    499.7    499.7 |   13.666   13.666   141.56   212.86   212.86 |      0.0 100.00 |
|   1114.4    807.0 |    6.340    8.608    98.04   167.77   212.86 |      0.0 100.00 |
|   1441.8   1018.6 |    4.946    6.880    72.35   167.77   212.86 |      0.0  63.36 |
|   1554.5   1152.6 |    4.615    6.116    53.74   167.77   212.86 |      0.0  49.98 |
|   1708.2   1263.7 |    4.176    5.592    49.55   141.56   212.86 |      0.0  49.96 |
|   1112.6   1238.5 |    6.455    5.721    51.38   203.42   212.86 |      0.0  50.02 |
|    611.1   1238.2 |    9.125    5.722    51.38   203.42   212.86 |      0.0   0.00 |
Purge phase...
9999 entries have been successfully purged
```

The following example also adds entries, and then deletes them in the order they were added after they are 10 seconds old:

```
$ addrate \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --usePkcs12TrustStore /path/to/opendj/config/keystore \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=admin \
 --bindPassword password \
 --numConnections 10 \
 --keepConnectionsOpen \
 --deleteMode fifo \
 --deleteAgeThreshold 10 \
 --maxDuration 30 \
 /path/to/opendj/config/MakeLDIF/addrate.template
--------------------------------------------------------------------------------------
|     Throughput    |                 Response Time                |    Additional   |
|    (ops/second)   |                (milliseconds)                |    Statistics   |
|   recent  average |   recent  average    99.9%   99.99%  99.999% |  err/sec   Add% |
--------------------------------------------------------------------------------------
|   1489.6   1489.6 |    4.585    4.585    28.70    31.20    51.64 |      0.0 100.00 |
|   1262.8   1376.2 |    5.698    5.096    41.68    52.69    55.31 |      0.0 100.00 |
|   1596.2   1449.5 |    4.430    4.851    36.18    52.43    55.31 |      0.0  50.71 |
|   1237.8   1396.6 |    5.859    5.075    44.56   115.34   119.01 |      0.0  50.00 |
|   1156.0   1348.5 |    6.195    5.267    44.83   115.34   119.01 |      0.0  49.96 |
|   1373.3   1352.6 |    5.226    5.260    46.40   114.82   119.01 |      0.0  49.99 |
Purge phase...
Purge in progress:  8195/13885 entries deleted (1638.2 ops/sec). ETA 00:00:03
```

These examples use the following options:

* `--hostname localhost` , `--port 1636` , `--useSsl` , `--usePkcs12TrustStore /path/to/opendj/config/keystore` , `--trustStorePassword:file /path/to/opendj/config/keystore.pin`

  Access the server running on the local system over a secure LDAPS connection to port 1636.

* `--bindDn uid=admin` , `--bindPassword password`

  Authenticate as the directory root user `uid=admin` with the bind password that is literally `password` . This user is not subject to access control, so rates may be higher than what you observe with a regular user.

* `--numConnections 10`

  Open 10 connections to the server.

* `--keepConnectionsOpen`

  Keep the connections open to reuse them during the operation.

* `--deleteMode (random | fifo)`

  After adding entries, delete them in random order, or in first-in-first-out order.

* `--deleteSizeThreshold 10,000`

  Add 10,000 entries before starting to delete them.

* `--deleteAgeThreshold 10`

  Begin to delete entries when they are 10 seconds old.

* `/path/to/opendj/config/MakeLDIF/addrate.template`

  When building entries to add, use this file as the template.

* `--maxDuration 30`

  Run for a maximum of 30 seconds.

Notice the following characteristics of the output:

* The first two columns show the throughput in operations completed per second. The recent column shows the average rate for operations reflected in this row of output. The average column shows the average rate since the beginning of the run.

* The response time columns indicate characteristics of response latency in milliseconds. The recent column shows the average latency for operations reflected in this row of output. The average column shows the average latency since the beginning of the run. The "99.9%" column shows the latency after which 99.9% of operations have completed. Only 1 operation in 1000 took longer than this. The "99.99%" column shows the latency after which 99.99% of operations have completed. Only 1 operation in 10,000 took longer than this. The "99.999%" column shows the latency after which 99.999% of operations have completed. Only 1 operation in 100,000 took longer than this.

* The additional statistics columns show information about what is happening during the run. The "err/sec" column shows the rate of error results per second for this row of output. Unless you have intentionally set up the command to generate errors, this column should indicate `0.0` . Check that this column matches your expectations before looking at any other columns. The "Add%" column shows the percentage of operations performed that were adds. The rest are delete operations. Notice that the percentage of add operations drops as the command begins to delete entries.

---

---
title: authrate
description: authrate — measure bind throughput and response time
component: pingds
version: 8.1
page_id: pingds:tools-reference:authrate
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/authrate.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  authrate-description: Description
  authrate-options: Options
  exit_codes: Exit codes
  authrate-examples: Examples
  simple_binds: Simple binds
  random_user_identifiers: Random user identifiers
---

# authrate

`authrate` — measure bind throughput and response time

## Synopsis

`authrate {options} [filter template string] [attributes …​]`

## Description

This utility can be used to measure bind throughput and response time of a directory service using user-defined bind or search-then-bind operations.

Template strings may be used in the bind DN option as well as the authid and authzid SASL bind options. A search operation may be used to retrieve the bind DN by specifying the base DN and a filter. The retrieved entry DN will be appended as the last argument in the argument list when evaluating template strings.

Example (bind only):

authrate -p 1636 -Z -X -D 'uid=user.{},ou=people,dc=example,dc=com' \\

-w password -f -c 10 -g 'rand(0,2000)'

Example (search then bind):

authrate -p 1636 -Z -X -D '{2}' -w password -f -c 10 \\

-b 'ou=people,dc=example,dc=com' -s one -g 'rand(0,2000)' '(uid=user.{1})'

Before trying the example, import 2000 randomly generated users.

When you do not use the `-f` option to keep connections open and rebind on the connections, the tool can exhaust its available ports, causing the tool to crash. You can work around this problem on test systems by changing TCP settings on the system.

For example, on Linux systems, set the following parameters in the `/etc/sysctl.conf` file:

```
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
```

The parameter `net.ipv4.tcp_fin_timeout` sets the length of time in seconds to wait for a final FIN packet before forcing a close of the socket. The default is 60 (seconds).

The parameter `net.ipv4.tcp_tw_recycle` enables fast recycling of TIME\_WAIT sockets. The default is 0 (false). Enabling this can cause Network Address Translation (NAT) issues.

The parameter `net.ipv4.tcp_tw_reuse` enables reuse of TIME\_WAIT sockets for new connections. The default is 0 (false).

These settings are recommended only for testing, and *not for production systems* .

After making the changes to `/etc/sysctl.conf` , reload the configuration with the `sysctl` command:

```
# sysctl -p
```

## Options

The `authrate` command takes the following options:

Command options:

* `-a | --dereferencePolicy {dereferencePolicy}`

  Alias dereference policy ('never', 'always', 'search', or 'find'). Default: never

* `-b | --baseDn {baseDN}`

  Base DN template string.

* `-B | --warmUpDuration {warmUpDuration}`

  Warm up duration in seconds. Default: 0

* `-c | --numConnections {numConnections}`

  Number of connections. Default: 1

* `-d | --maxDuration {maxDuration}`

  Maximum duration in seconds, or unlimited if not specified. Default: 0

* `-e | --percentile {percentile}`

  Calculate max response time for a percentile of operations.

* `-f | --keepConnectionsOpen`

  Keep connections open. Default: false

* `-g | --argument {generator function or static string}`

  Argument used to evaluate the template strings in program parameters (ie. Base DN, Search Filter). The set of all arguments provided form the argument list in order. Besides static string arguments, they can be generated per iteration with the following functions:

  "inc({filename})" Consecutive, incremental line from file

  "inc({min},{max})" Consecutive, incremental number

  "rand({filename})" Random line from file

  "rand({min},{max})" Random number

  "randstr({length},*charSet*)" Random string of specified length and optionally from characters in the charSet string. A range of characters can be specified with \[start-end] charSet notation. If no charSet is specified, the default charSet of \[A-Z]\[a-z]\[0-9] will be used.

  "xrand({min},{max})" Random number, where each iteration always returns a different number from the specified range until the number of iterations exceeds the range. When the number of iterations is a multiple of the range, number of iterations = N x range, this returns each number in the range N times.

  These functions do not support formatted integers with comma due to the ambiguity between a comma used to separate function arguments and a comma used to separate digits in a formatted integer.

* `-i | --statInterval {statInterval}`

  Display results each specified number of seconds. Default: 5

* `-I | --invalidPassword {invalidPassword}`

  Percentage of requests that will send an invalid password (between 0 and 100). Default: 0

* `-m | --maxIterations {maxIterations}`

  Max iterations, 0 for unlimited. Default: 0

* `-M | --targetThroughput {targetThroughput}`

  Target average throughput to achieve. Default: 0

* `-s | --searchScope {searchScope}`

  Search scope ('base', 'one', 'sub', or 'subordinates'). Note: 'subordinates' is an LDAP extension that might not work with all LDAP servers. Default: sub

* `-S | --scriptFriendly`

  Use script-friendly mode. Default: false

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default:

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server port number.

* `-q | --useStartTls`

  Use StartTLS to secure communication with the server. Default: false

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

* `-Z | --useSsl`

  Use SSL for secure communication with the server. Default: false

Utility input/output options:

* `-n | --no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* 89

  An error occurred while parsing the command-line arguments.

## Examples

### Simple binds

The following example demonstrates measuring simple bind performance:

```
$ authrate \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --usePkcs12TrustStore /path/to/opendj/config/keystore \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --argument "rand(0,2000)" --bindDn "uid=user.{},ou=people,dc=example,dc=com" \
 --bindPassword password \
 --numConnections 10 \
 --maxDuration 30 \
 --keepConnectionsOpen
-------------------------------------------------------------------------------
|     Throughput    |                 Response Time                |          |
|    (ops/second)   |                (milliseconds)                |          |
|   recent  average |   recent  average    99.9%   99.99%  99.999% |  err/sec |
-------------------------------------------------------------------------------
|  20306.0  20306.0 |    0.469    0.469    11.40    38.01    55.05 |      0.0 |
|  27672.6  23989.3 |    0.352    0.401     8.52    24.12    50.33 |      0.0 |
|  27410.0  25129.5 |    0.355    0.385     7.60    18.35    43.78 |      0.0 |
|  27082.2  25617.7 |    0.359    0.378     7.21    17.43    43.25 |      0.0 |
|  28027.4  26099.6 |    0.347    0.371     6.62    17.17    42.99 |      0.0 |
|  26805.7  26217.2 |    0.361    0.370     6.32    16.65    42.99 |      0.0 |
```

This example uses the following options:

* `--hostname localhost` , `--port 1636` , `--useSsl` , `--usePkcs12TrustStore /path/to/opendj/config/keystore` , `--trustStorePassword:file /path/to/opendj/config/keystore.pin`

  Access the server running on the local system over a secure LDAPS connection to port 1636.

* `--argument "rand(0,2000)" --bindDn "uid=user.{},ou=people,dc=example,dc=com"`

  Authenticate as a user with bind DN `uid=user.number,ou=people,dc=example,dc=com` , where *number* is a random number between 0 and 2000, inclusive.

* `--bindPassword password`

  Authenticate with the bind password that is literally `password` .

* `--numConnections 10`

  Open 10 connections to the server.

* `--maxDuration 30`

  Run for a maximum of 30 seconds.

* `--keepConnectionsOpen`

  Keep the connections open to reuse them during the operation.

Notice the following characteristics of the output:

* The first two columns show the throughput in operations completed per second. The recent column shows the average rate for operations reflected in this row of output. The average column shows the average rate since the beginning of the run.

* The response time columns indicate characteristics of response latency in milliseconds. The recent column shows the average latency for operations reflected in this row of output. The average column shows the average latency since the beginning of the run. The "99.9%" column shows the latency after which 99.9% of operations have completed. Only 1 operation in 1000 took longer than this. The "99.99%" column shows the latency after which 99.99% of operations have completed. Only 1 operation in 10,000 took longer than this. The "99.999%" column shows the latency after which 99.999% of operations have completed. Only 1 operation in 100,000 took longer than this.

* The "err/sec" column show the rate of error results per second for this row of output. Unless you have intentionally set up the command to generate errors, this column should indicate `0.0` . Check that this column matches your expectations before looking at any other columns.

### Random user identifiers

The following example reflects a platform deployment with random `fr-idm-uuid` user identifiers.

For this example, the directory server runs in a Docker container with hostname `ds-idrepo-0.ds-idrepo` . It is installed under `/opt/opendj` and has user entries under `ou=identities` . Each user entry has the same password.

The current working directory is `/opt/opendj` :

```
# Get the user DNs with the ldapsearch command and write the identifiers to a file:
$ ./bin/ldapsearch \
--hostname ds-idrepo-0.ds-idrepo \
--port 1636 \
--useSsl \
--usePkcs12TrustStore /opt/opendj/config/keystore \
--trustStorePassword:file /opt/opendj/config/keystore.pin \
--bindDn uid=admin \
--bindPassword password \
--sizeLimit 1000 \
--baseDn 'ou=identities' \
"(uid=*user*)" dn | awk '/^dn: / { print substr($0, 5) }' > dns.txt

# Iterate over random user identifiers to run the authrate command:
$ ./bin/authrate \
--hostname ds-idrepo-0.ds-idrepo \
--port 1636 \
--useSsl \
--usePkcs12TrustStore /opt/opendj/config/keystore \
--trustStorePassword:file /opt/opendj/config/keystore.pin \
--bindDn 'fr-idm-uuid={1},ou=People,ou=identities' \
--bindPassword password \
--keepConnectionsOpen \
--numConnections 100 \
--argument 'rand(dns.txt)'
```

---

---
title: backendstat
description: backendstat — gather PingDS backend debugging information
component: pingds
version: 8.1
page_id: pingds:tools-reference:backendstat
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/backendstat.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  backendstat-description: Description
  backendstat-options: Options
  backendstat-subcommands: Subcommands
  backendstat_dump_index: backendstat dump-index
  options: Options
  backendstat_dump_raw_db: backendstat dump-raw-db
  options_2: Options
  backendstat_list_base_dns: backendstat list-base-dns
  backendstat_list_indexes: backendstat list-indexes
  options_3: Options
  backendstat_list_raw_dbs: backendstat list-raw-dbs
  options_4: Options
  backendstat_show_index_status: backendstat show-index-status
  options_5: Options
  exit_codes: Exit codes
---

# backendstat

`backendstat` — gather PingDS backend debugging information

## Synopsis

`backendstat {subcommand} {options}`

## Description

This utility can be used to debug a backend.

## Options

The `backendstat` command takes the following options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Subcommands

The `backendstat` command supports the following subcommands:

### backendstat dump-index

`backendstat dump-index {options} {indexName}`

Dump records from an index, decoding keys and values. Depending on index size, this subcommand can generate lots of output.

When you run the `show-index-status` subcommand, the result is a table, followed by a "Total", which is the total number of indexes, followed by a list of indexes with "Over index-entry-limit keys" to show the values for which the number of entries exceeded the index entry limit.

The table has the following columns:

* (No label)

  If the index needs rebuilding, its row starts with `!` . Otherwise, its row starts with a space.

* Index Name

  Name of the index, where the format depends on the index. For example, `givenName.caseIgnoreSubstringsMatch:6` :

  * Attribute indexes: *attr.type* . *type*

  * Big indexes: *attr.type* .big. *type*

  * VLV indexes: vlv. *type*

* Secure

  `+` means confidentiality is enabled for the index. `-` means confidentiality is disabled.

* Size

  The size on disk.

* Key Count

  Number of indexed keys. Use the `backendstat dump-tree` command to see how many entry IDs correspond to each key.

* Over

  Number of keys for which there are too many values to maintain an index, based on the `index-entry-limit` . This is recorded as `-` for VLV indexes. In other words, with the default index entry limit of 4000, if every user in your large directory has an email address ending in `@example.com` , and a substring index with default substring length of 6 is maintained for `mail` , then the directory server does not maintain indexes for keys corresponding to substrings in `@example.com` . As a result, an LDAP search with the filter `"(mail=*@example.com)"` becomes an unindexed search even though a substring index exists for the mail attribute. By default, the directory server does not allow unindexed searches except by privileged users. This is usually exactly the behavior you want in order to prevent client applications from sending searches that return every user in the directory for example. Clients should refine their search filters instead.

* Entry Limit

  The `index-entry-limit` setting that applies to this index. Default: `4000`

* Mean

  Average number of values per key for this index.

* Median

  Median number of values per key for this index.

* 80th, 95th, 99th

  Percentage of keys having at most the specified number of values. This is a measure of how full the entry ID lists are.

#### Options

In addition to the global `backendstat` options, the `backendstat dump-index` subcommand takes the following options:

* `-b | --baseDn {baseDN}`

  The base DN.

* `-k | --minKeyValue {minKeyValue}`

  Only show records with keys that should be ordered after the provided value using the comparator for the database container.

* `-K | --maxKeyValue {maxKeyValue}`

  Only show records with keys that should be ordered before the provided value using the comparator for the database container.

* `-p | --skipDecode`

  Do not try to decode backend data to their appropriate types. Default: false

* `-q | --statsOnly`

  Do not display backend data, just statistics. Default: false

* `-s | --minDataSize {minDataSize}`

  Only show records whose data is no smaller than the provided value. Default: -1

* `-S | --maxDataSize {maxDataSize}`

  Only show records whose data is no larger than the provided value. Default: -1

* `-x | --minHexKeyValue {minKeyValue}`

  Only show records with keys that should be ordered after the provided value using the comparator for the database container.

* `-X | --maxHexKeyValue {maxKeyValue}`

  Only show records with keys that should be ordered before the provided value using the comparator for the database container.

### backendstat dump-raw-db

`backendstat dump-raw-db {options} {databaseName}`

Dump the raw records in hexadecimal format for a low-level database within the pluggable backend's storage engine. Depending on index size, this subcommand can generate lots of output.

When you run the `show-index-status` subcommand, the result is a table, followed by a "Total", which is the total number of indexes, followed by a list of indexes with "Over index-entry-limit keys" to show the values for which the number of entries exceeded the index entry limit.

The table has the following columns:

* (No label)

  If the index needs rebuilding, its row starts with `!` . Otherwise, its row starts with a space.

* Index Name

  Name of the index, where the format depends on the index. For example, `givenName.caseIgnoreSubstringsMatch:6` :

  * Attribute indexes: *attr.type* . *type*

  * Big indexes: *attr.type* .big. *type*

  * VLV indexes: vlv. *type*

* Secure

  `+` means confidentiality is enabled for the index. `-` means confidentiality is disabled.

* Size

  The size on disk.

* Key Count

  Number of indexed keys. Use the `backendstat dump-tree` command to see how many entry IDs correspond to each key.

* Over

  Number of keys for which there are too many values to maintain an index, based on the `index-entry-limit` . This is recorded as `-` for VLV indexes. In other words, with the default index entry limit of 4000, if every user in your large directory has an email address ending in `@example.com` , and a substring index with default substring length of 6 is maintained for `mail` , then the directory server does not maintain indexes for keys corresponding to substrings in `@example.com` . As a result, an LDAP search with the filter `"(mail=*@example.com)"` becomes an unindexed search even though a substring index exists for the mail attribute. By default, the directory server does not allow unindexed searches except by privileged users. This is usually exactly the behavior you want in order to prevent client applications from sending searches that return every user in the directory for example. Clients should refine their search filters instead.

* Entry Limit

  The `index-entry-limit` setting that applies to this index. Default: `4000`

* Mean

  Average number of values per key for this index.

* Median

  Median number of values per key for this index.

* 80th, 95th, 99th

  Percentage of keys having at most the specified number of values. This is a measure of how full the entry ID lists are.

#### Options

In addition to the global `backendstat` options, the `backendstat dump-raw-db` subcommand takes the following options:

* `-b | --baseDn {baseDN}`

  The base DN.

* `-k | --minKeyValue {minKeyValue}`

  Only show records with keys that should be ordered after the provided value using the comparator for the database container.

* `-K | --maxKeyValue {maxKeyValue}`

  Only show records with keys that should be ordered before the provided value using the comparator for the database container.

* `-l | --singleLine`

  Write hexadecimal data on a single line instead of pretty format. Default: false

* `-n | --backendId {backendName}`

  The backend ID of the backend.

* `-q | --statsOnly`

  Do not display backend data, just statistics. Default: false

* `-s | --minDataSize {minDataSize}`

  Only show records whose data is no smaller than the provided value. Default: -1

* `-S | --maxDataSize {maxDataSize}`

  Only show records whose data is no larger than the provided value. Default: -1

* `-x | --minHexKeyValue {minKeyValue}`

  Only show records with keys that should be ordered after the provided value using the comparator for the database container.

* `-X | --maxHexKeyValue {maxKeyValue}`

  Only show records with keys that should be ordered before the provided value using the comparator for the database container.

### backendstat list-base-dns

`backendstat list-base-dns`

List the base DNs in a backend.

### backendstat list-indexes

`backendstat list-indexes {options}`

List the indexes associated with a pluggable backend. This subcommand may take a long time to complete depending on the size of the backend.

#### Options

In addition to the global `backendstat` options, the `backendstat list-indexes` subcommand takes the following options:

* `-b | --baseDn {baseDN}`

  The base DN.

### backendstat list-raw-dbs

`backendstat list-raw-dbs {options}`

List the low-level databases within a pluggable backend's storage engine. This subcommand may take a long time to complete depending on the size of the backend.

#### Options

In addition to the global `backendstat` options, the `backendstat list-raw-dbs` subcommand takes the following options:

* `-n | --backendId {backendName}`

  The backend ID of the backend.

* `-u | --useSiUnits`

  Uses SI Units for printing sizes. Default: false

### backendstat show-index-status

`backendstat show-index-status {options}`

Shows the status of indexes for a backend base DN. This subcommand can take a long time to complete, as it reads all indexes of the backend.

When you run the `show-index-status` subcommand, the result is a table, followed by a "Total", which is the total number of indexes, followed by a list of indexes with "Over index-entry-limit keys" to show the values for which the number of entries exceeded the index entry limit.

The table has the following columns:

* (No label)

  If the index needs rebuilding, its row starts with `!` . Otherwise, its row starts with a space.

* Index Name

  Name of the index, where the format depends on the index. For example, `givenName.caseIgnoreSubstringsMatch:6` :

  * Attribute indexes: *attr.type* . *type*

  * Big indexes: *attr.type* .big. *type*

  * VLV indexes: vlv. *type*

* Secure

  `+` means confidentiality is enabled for the index. `-` means confidentiality is disabled.

* Size

  The size on disk.

* Key Count

  Number of indexed keys. Use the `backendstat dump-tree` command to see how many entry IDs correspond to each key.

* Over

  Number of keys for which there are too many values to maintain an index, based on the `index-entry-limit` . This is recorded as `-` for VLV indexes. In other words, with the default index entry limit of 4000, if every user in your large directory has an email address ending in `@example.com` , and a substring index with default substring length of 6 is maintained for `mail` , then the directory server does not maintain indexes for keys corresponding to substrings in `@example.com` . As a result, an LDAP search with the filter `"(mail=*@example.com)"` becomes an unindexed search even though a substring index exists for the mail attribute. By default, the directory server does not allow unindexed searches except by privileged users. This is usually exactly the behavior you want in order to prevent client applications from sending searches that return every user in the directory for example. Clients should refine their search filters instead.

* Entry Limit

  The `index-entry-limit` setting that applies to this index. Default: `4000`

* Mean

  Average number of values per key for this index.

* Median

  Median number of values per key for this index.

* 80th, 95th, 99th

  Percentage of keys having at most the specified number of values. This is a measure of how full the entry ID lists are.

#### Options

In addition to the global `backendstat` options, the `backendstat show-index-status` subcommand takes the following options:

* `-b | --baseDn {baseDN}`

  The base DN.

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

---

---
title: base64
description: base64 — encode and decode base64 strings
component: pingds
version: 8.1
page_id: pingds:tools-reference:base64
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/base64.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  base64-description: Description
  base64-options: Options
  base64-subcommands: Subcommands
  base64_decode: base64 decode
  options: Options
  base64_encode: base64 encode
  options_2: Options
  exit_codes: Exit codes
---

# base64

`base64` — encode and decode base64 strings

## Synopsis

`base64 {subcommand} {options}`

## Description

This utility can be used to encode and decode information using base64.

## Options

The `base64` command takes the following options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Subcommands

The `base64` command supports the following subcommands:

### base64 decode

`base64 decode {options}`

Decode base64-encoded information into raw data. When no options are specified, this subcommand reads from standard input and writes to standard output.

#### Options

In addition to the global `base64` options, the `base64 decode` subcommand takes the following options:

* `-d | --encodedData {data}`

  The base64-encoded data to be decoded.

* `-f | --encodedDataFile {path}`

  The path to a file containing the base64-encoded data to be decoded.

* `-o | --toRawFile {path}`

  The path to a file to which the raw base64-decoded data should be written.

### base64 encode

`base64 encode {options}`

Encode raw data using base64. When no options are specified, this subcommand reads from standard input and writes to standard output.

#### Options

In addition to the global `base64` options, the `base64 encode` subcommand takes the following options:

* `-d | --rawData {data}`

  The raw data to be base64 encoded.

* `-f | --rawDataFile {path}`

  The path to a file containing the raw data to be base64 encoded.

* `-o | --toEncodedFile {path}`

  The path to a file to which the base64-encoded data should be written.

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

---

---
title: changelogstat
description: changelogstat — debug changelog and changenumber files
component: pingds
version: 8.1
page_id: pingds:tools-reference:changelogstat
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/changelogstat.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  changelogstat-description: Description
  changelogstat-options: Options
  changelogstat-subcommands: Subcommands
  changelogstat_dump_change_number_db: changelogstat dump-change-number-db
  options: Options
  changelogstat_dump_replica_db: changelogstat dump-replica-db
  options_2: Options
  changelogstat_dump_replica_db_file: changelogstat dump-replica-db-file
  options_3: Options
  exit_codes: Exit codes
  changelogstat-examples: Examples
---

# changelogstat

`changelogstat` — debug changelog and changenumber files

## Synopsis

`changelogstat {subcommand} {options}`

## Description

This utility can be used to debug changelog and changenumber files.

## Options

The `changelogstat` command takes the following options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Subcommands

The `changelogstat` command supports the following subcommands:

### changelogstat dump-change-number-db

`changelogstat dump-change-number-db {options}`

Dump the change number DB.

#### Options

In addition to the global `changelogstat` options, the `changelogstat dump-change-number-db` subcommand takes the following options:

* `--from {change number}`

  The lower bound of the range of change numbers to dump.

* `--outputDir {directory}`

  The output directory for the dump files.

* `--to {change number}`

  The upper bound of the range of change numbers to dump.

### changelogstat dump-replica-db

`changelogstat dump-replica-db {options} baseDN replicaID`

Dump the replica DB for a given domain and replica.

#### Options

In addition to the global `changelogstat` options, the `changelogstat dump-replica-db` subcommand takes the following options:

* `--from {csn}`

  The lower bound of the range of changes to dump.

* `--outputDir {directory}`

  The output directory for the dump files.

* `--to {csn}`

  The upper bound of the range of changes to dump.

### changelogstat dump-replica-db-file

`changelogstat dump-replica-db-file {options} file`

Dump a replica DB file.

#### Options

In addition to the global `changelogstat` options, the `changelogstat dump-replica-db-file` subcommand takes the following options:

* `--baseDn {base dn}`

  The base-dn of the changes contained in the provided replica DB file. Default:

* `--from {csn}`

  The lower bound of the range of changes to dump.

* `--to {csn}`

  The upper bound of the range of changes to dump.

## Exit codes

* 0

  The command completed successfully.

* 1

  An error occurred.

## Examples

To dump the records for change numbers 10 to 15:

```
$ changelogstat dump-change-number-db --from 10 --to 15
{ "changeNumber": 10, "baseDn": "dc=example,dc=com", "csn": { "value": "010f017f87c4135d00025abdevaluation-only", "serverId": "evaluation-only", "timestamp": "...", "seqnum": 154301 } }
{ "changeNumber": 11, "baseDn": "dc=example,dc=com", "csn": { "value": "010f017f87c4135d00025abeevaluation-only", "serverId": "evaluation-only", "timestamp": "...", "seqnum": 154302 } }
{ "changeNumber": 12, "baseDn": "dc=example,dc=com", "csn": { "value": "010f017f87c4135d00025abfevaluation-only", "serverId": "evaluation-only", "timestamp": "...", "seqnum": 154303 } }
{ "changeNumber": 13, "baseDn": "dc=example,dc=com", "csn": { "value": "010f017f87c4135d00025ac0evaluation-only", "serverId": "evaluation-only", "timestamp": "...", "seqnum": 154304 } }
{ "changeNumber": 14, "baseDn": "dc=example,dc=com", "csn": { "value": "010f017f87c4135d00025ac1evaluation-only", "serverId": "evaluation-only", "timestamp": "...", "seqnum": 154305 } }
{ "changeNumber": 15, "baseDn": "dc=example,dc=com", "csn": { "value": "010f017f87c4135d00025ac2evaluation-only", "serverId": "evaluation-only", "timestamp": "...", "seqnum": 154306 } }
```

To dump the replica DB for the domain `dc=example,dc=com` and the server with ID `ds-1` :

```
$ changelogstat dump-replica-db --outputDir myOutputDir dc=example,dc=com ds-1
$ cat myOutputDir/010d018fdcbb887700000086ds-1.cdb.txt
{ "msgType": "AddMsg", "dn": "uid=newuser,ou=People,dc=example,dc=com", "csn": { "value": "010d018fdcbb887700000086ds-1", "serverId": "ds-1", "...": "time", "seqnum": 134 }, "uniqueId": "477f0607-ba42-4d8f-93a2-639c668b8d83" }
{ "msgType": "DeleteMsg", "dn": "uid=newuser,ou=People,dc=example,dc=com", "csn": { "value": "010d018fdcbb998800000097ds-1", "serverId": "ds-1", "timestamp": "...", "seqnum": 151 }, "uniqueId": "477f0607-ba42-4d8f-93a2-639c668b8d83" }
{ "msgType": "ReplicaOfflineMsg", "csn": { "value": "010d018fdcbc45400000011bds-1", "serverId": "ds-1", "timestamp": "...", "seqnum": 283 } }
```

To dump a specific replica DB file:

```
$ changelogstat dump-replica-db-file changelogDb/2.dom/1.server/01010166aaf2a3e3000002bd1.cdb

{ "msgType": "ModifyMsg", "dn": "uid=user.84614,ou=people", "csn": "010f017f87c42baa0002f04fevaluation-only", "uniqueId": "83719220-5de4-3271-a2a1-49f719778533" }
{ "msgType": "ModifyMsg", "dn": "uid=user.67749,ou=people", "csn": "010f017f87c42baa0002f050evaluation-only", "uniqueId": "981f226e-5dff-35b3-b95f-6cfd582633ab" }
{ "msgType": "ModifyMsg", "dn": "uid=user.15128,ou=people", "csn": "010f017f87c42baa0002f051evaluation-only", "uniqueId": "d0146ad4-ae04-3c93-b0e1-92c627f0bdae" }
{ "msgType": "ModifyMsg", "dn": "uid=user.56721,ou=people", "csn": "010f017f87c42baa0002f052evaluation-only", "uniqueId": "3a578584-5e9d-3835-a7d4-1f5c78e41325" }
...
{ "msgType": "ModifyMsg", "dn": "uid=user.58621,ou=people", "csn": "010f017f87c439c900035566evaluation-only", "uniqueId": "0281f279-b441-3018-9036-f6f97bf3903a" }
{ "msgType": "ModifyMsg", "dn": "uid=user.6745,ou=people", "csn": "010f017f87c439c900035567evaluation-only", "uniqueId": "90853018-3abb-3e88-9fb2-0477919c067d" }
{ "msgType": "ModifyMsg", "dn": "uid=user.28215,ou=people", "csn": "010f017f87c439c900035568evaluation-only", "uniqueId": "abfe1a55-5c64-36e8-8714-7d6e1f6d67aa" }
{ "msgType": "ModifyMsg", "dn": "uid=user.86811,ou=people", "csn": "010f017f87c439c900035569evaluation-only", "uniqueId": "0810f7af-94ea-3f34-a455-c22432ad9429" }
```

---

---
title: create-rc-script
description: create-rc-script — script to manage PingDS as a service on UNIX
component: pingds
version: 8.1
page_id: pingds:tools-reference:create-rc-script
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/create-rc-script.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  create-rc-script-description: Description
  create-rc-script-options: Options
  exit_codes: Exit codes
---

# create-rc-script

`create-rc-script` — script to manage PingDS as a service on UNIX

## Synopsis

`create-rc-script {options}`

## Description

Create an RC script or systemd service that may be used to start, stop, and restart the Directory Server on UNIX-based systems.

## Options

The `create-rc-script` command takes the following options:

Command options:

* `-g | --groupName {groupName}`

  The name of the group account under which the server should run.

* `-j | --javaHome {path}`

  The path to the Java installation that should be used to run the server.

* `-J | --javaArgs {args}`

  A set of arguments that should be passed to the JVM when running the server.

* `-r | --rcScript {path}`

  The path to the RC script to create.

* `-s | --systemdService {path}`

  The path to the systemd service file to create.

* `-u | --userName {userName}`

  The name of the user account under which the server should run.

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

---

---
title: dsbackup
description: dsbackup — Backup and restore backends
component: pingds
version: 8.1
page_id: pingds:tools-reference:dsbackup
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/dsbackup.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  dsbackup-description: Description
  dsbackup-options: Options
  dsbackup-subcommands: Subcommands
  dsbackup_create: dsbackup create
  options: Options
  dsbackup_list: dsbackup list
  options_2: Options
  dsbackup_purge: dsbackup purge
  options_3: Options
  dsbackup_restore: dsbackup restore
  options_4: Options
  exit_codes: Exit codes
---

# dsbackup

`dsbackup` — Backup and restore backends

## Synopsis

`dsbackup {subcommand} {options}`

## Description

Backup and restore backends, manage backup files.

## Options

The `dsbackup` command takes the following options:

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Subcommands

The `dsbackup` command supports the following subcommands:

### dsbackup create

`dsbackup create {options}`

Take encrypted and signed backups of individual backends and send them to the desired location.

#### Options

In addition to the global `dsbackup` options, the `dsbackup create` subcommand takes the following options:

SubCommand Options:

* `-d | --backupLocation {backup location}`

  Backup file-system path or URI for alternative storage mechanisms. File-system paths may be expressed as absolute or relative paths and are resolved relative to the current working directory when the tool is run in offline mode, or relative to the server instance directory when the tool is run in task mode. Read the documentation for further information regarding alternative backup storage mechanisms.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-n | --backendName {backendName}`

  The name of the backend to back up. Specify this option multiple times to backup multiple backends or skip this option to backup all the enabled backends that support backups.

* `--offline`

  Indicates that the command will operate independently of the server process. It will run regardless of whether the server is started or stopped. When using this option with the restore sub-command, the server must be stopped; also as the command will write to server files, you should run the command as a user having the same filesystem permissions as the user running the server. Using this option with the create sub-command when the server is running is possible and supported. With JE Backends, the integrity of the backup is ensured by the process. With LDIF backends, avoid simultaneous changes to the backends. Default: false

* `--storageProperty {PROP:VALUE}`

  Assigns a value to a storage property where PROP is the name of the property and VALUE is the single value to be assigned. Specify the same property multiple times in order to assign more than one value to it.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

Task Scheduling Options

* `--completionNotify {emailAddress}`

  Email address of a recipient to be notified when the task completes. This option may be specified more than once.

* `--dependency {taskID}`

  ID of a task upon which this task depends. A task will not start execution until all its dependencies have completed execution.

* `--description {description}`

  Gives a description to the task.

* `--errorNotify {emailAddress}`

  Email address of a recipient to be notified if an error occurs when this task executes. This option may be specified more than once.

* `--failedDependencyAction {action}`

  Action this task will take should one if its dependent tasks fail. The value must be one of PROCESS, CANCEL, DISABLE. If not specified defaults to CANCEL.

* `--recurringTask {schedulePattern}`

  Indicates the task is recurring and will be scheduled according to the value argument expressed in crontab(5) compatible time/date pattern. The schedule pattern for a recurring task supports only the following `crontab` features:

| Field        | Allowed Values    |
| ------------ | ----------------- |
| minute       | 0-59              |
| hour         | 0-23              |
| day of month | 1-31              |
| month        | 1-12              |
| day of week  | 0-6 (0 is Sunday) |

A field can contain an asterisk, `*` . An asterisk stands for `first-last` .

Fields can include ranges of numbers. A range is two numbers separated by a hyphen, and is inclusive. For example, `8-10` for an "hour" field means execution at hours 8, 9, and 10.

Fields can include lists. A list is a set of numbers or ranges separated by commas. For example, `4,8-10` for an "hour" field means execution at hours 4, 8, 9, and 10.

* `-t | --start {startTime}`

  Indicates the date/time at which this operation will start when scheduled as a server task expressed in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the task to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* `--taskId {taskID}`

  Gives an ID to the task.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

### dsbackup list

`dsbackup list {options}`

List the backups at the specified location.

#### Options

In addition to the global `dsbackup` options, the `dsbackup list` subcommand takes the following options:

* `-d | --backupLocation {backup location}`

  Location containing backups: file-system path or URI for alternative storage mechanisms. File-system paths may be expressed as absolute or relative paths and are resolved relative to the current working directory when the tool is run in offline mode, or relative to the server instance directory when the tool is run in task mode. Read the documentation for further information regarding alternative backup storage mechanisms.

* `--last`

  Show only the last backup for each backend. Default: false

* `-n | --backendName {backendName}`

  Show only backups taken from the provided backend.

* `--serverId {server ID}`

  Show only backups taken from the provided server.

* `--storageProperty {PROP:VALUE}`

  Assigns a value to a storage property where PROP is the name of the property and VALUE is the single value to be assigned. Specify the same property multiple times in order to assign more than one value to it.

* `--verify`

  Verify backups completeness, integrity and whether they can be decrypted. Default: false

### dsbackup purge

`dsbackup purge {options}`

Delete one or more backups.

#### Options

In addition to the global `dsbackup` options, the `dsbackup purge` subcommand takes the following options:

SubCommand Options:

* `--backupId {backup ID}`

  The ID of the backup that should be deleted. Specify this option multiple times to purge multiple backups.

* `-d | --backupLocation {backup location}`

  Location containing backups: file-system path or URI for alternative storage mechanisms. File-system paths may be expressed as absolute or relative paths and are resolved relative to the current working directory when the tool is run in offline mode, or relative to the server instance directory when the tool is run in task mode. Read the documentation for further information regarding alternative backup storage mechanisms.

* `--force`

  Must be used with the '--olderThan' option, indicates that the last backup of each backend can be deleted if older than the provided duration. Default: false

* `--keepCount {number of backups}`

  The number of backups to keep per backend. Use this option to keep the n latest backups of each backend and delete the others. If n=0, all the backups will be removed.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-n | --backendName {backend name}`

  Purge only backups of the specified backend. Specify this option multiple times to allow purging backups of different backends. Skip this option to allow purging backups of all backends. This can only be used with options '--keepCount' or '--olderThan'.

* `--offline`

  Indicates that the command will operate independently of the server process. It will run regardless of whether the server is started or stopped. When using this option with the restore sub-command, the server must be stopped; also as the command will write to server files, you should run the command as a user having the same filesystem permissions as the user running the server. Using this option with the create sub-command when the server is running is possible and supported. With JE Backends, the integrity of the backup is ensured by the process. With LDIF backends, avoid simultaneous changes to the backends. Default: false

* `--olderThan {duration}`

  Delete backups that are older than the provided duration. The latest backup of each backend will always be kept unless the '--force' option is also provided. Duration examples: '12 hours', '3 days', '1y'.

* `--storageProperty {PROP:VALUE}`

  Assigns a value to a storage property where PROP is the name of the property and VALUE is the single value to be assigned. Specify the same property multiple times in order to assign more than one value to it.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

Task Scheduling Options

* `--completionNotify {emailAddress}`

  Email address of a recipient to be notified when the task completes. This option may be specified more than once.

* `--dependency {taskID}`

  ID of a task upon which this task depends. A task will not start execution until all its dependencies have completed execution.

* `--description {description}`

  Gives a description to the task.

* `--errorNotify {emailAddress}`

  Email address of a recipient to be notified if an error occurs when this task executes. This option may be specified more than once.

* `--failedDependencyAction {action}`

  Action this task will take should one if its dependent tasks fail. The value must be one of PROCESS, CANCEL, DISABLE. If not specified defaults to CANCEL.

* `--recurringTask {schedulePattern}`

  Indicates the task is recurring and will be scheduled according to the value argument expressed in crontab(5) compatible time/date pattern. The schedule pattern for a recurring task supports only the following `crontab` features:

| Field        | Allowed Values    |
| ------------ | ----------------- |
| minute       | 0-59              |
| hour         | 0-23              |
| day of month | 1-31              |
| month        | 1-12              |
| day of week  | 0-6 (0 is Sunday) |

A field can contain an asterisk, `*` . An asterisk stands for `first-last` .

Fields can include ranges of numbers. A range is two numbers separated by a hyphen, and is inclusive. For example, `8-10` for an "hour" field means execution at hours 8, 9, and 10.

Fields can include lists. A list is a set of numbers or ranges separated by commas. For example, `4,8-10` for an "hour" field means execution at hours 4, 8, 9, and 10.

* `-t | --start {startTime}`

  Indicates the date/time at which this operation will start when scheduled as a server task expressed in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the task to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* `--taskId {taskID}`

  Gives an ID to the task.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

### dsbackup restore

`dsbackup restore {options}`

Restore one or more backends. In order to decrypt and verify signatures on backup files, the server must have access to the master key pair used to encrypt and sign the files when they were created.

#### Options

In addition to the global `dsbackup` options, the `dsbackup restore` subcommand takes the following options:

SubCommand Options:

* `--backupId {backup ID}`

  Restore the backup having the provided ID. Specify this option multiple times to restore multiple backends.

* `-d | --backupLocation {backup location}`

  Location containing backups: file-system path or URI for alternative storage mechanisms. File-system paths may be expressed as absolute or relative paths and are resolved relative to the current working directory when the tool is run in offline mode, or relative to the server instance directory when the tool is run in task mode. Read the documentation for further information regarding alternative backup storage mechanisms.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-n | --backendName {backendName}`

  Restore the last backup of the provided backend. Specify this option multiple times to restore multiple backends.

* `--offline`

  Indicates that the command will operate independently of the server process. It will run regardless of whether the server is started or stopped. When using this option with the restore sub-command, the server must be stopped; also as the command will write to server files, you should run the command as a user having the same filesystem permissions as the user running the server. Using this option with the create sub-command when the server is running is possible and supported. With JE Backends, the integrity of the backup is ensured by the process. With LDIF backends, avoid simultaneous changes to the backends. Default: false

* `--storageProperty {PROP:VALUE}`

  Assigns a value to a storage property where PROP is the name of the property and VALUE is the single value to be assigned. Specify the same property multiple times in order to assign more than one value to it.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

Task Scheduling Options

* `--completionNotify {emailAddress}`

  Email address of a recipient to be notified when the task completes. This option may be specified more than once.

* `--dependency {taskID}`

  ID of a task upon which this task depends. A task will not start execution until all its dependencies have completed execution.

* `--description {description}`

  Gives a description to the task.

* `--errorNotify {emailAddress}`

  Email address of a recipient to be notified if an error occurs when this task executes. This option may be specified more than once.

* `--failedDependencyAction {action}`

  Action this task will take should one if its dependent tasks fail. The value must be one of PROCESS, CANCEL, DISABLE. If not specified defaults to CANCEL.

* `--recurringTask {schedulePattern}`

  Indicates the task is recurring and will be scheduled according to the value argument expressed in crontab(5) compatible time/date pattern. The schedule pattern for a recurring task supports only the following `crontab` features:

| Field        | Allowed Values    |
| ------------ | ----------------- |
| minute       | 0-59              |
| hour         | 0-23              |
| day of month | 1-31              |
| month        | 1-12              |
| day of week  | 0-6 (0 is Sunday) |

A field can contain an asterisk, `*` . An asterisk stands for `first-last` .

Fields can include ranges of numbers. A range is two numbers separated by a hyphen, and is inclusive. For example, `8-10` for an "hour" field means execution at hours 8, 9, and 10.

Fields can include lists. A list is a set of numbers or ranges separated by commas. For example, `4,8-10` for an "hour" field means execution at hours 4, 8, 9, and 10.

* `-t | --start {startTime}`

  Indicates the date/time at which this operation will start when scheduled as a server task expressed in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the task to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* `--taskId {taskID}`

  Gives an ID to the task.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

---

---
title: dsconfig
description: dsconfig — manage PingDS server configuration
component: pingds
version: 8.1
page_id: pingds:tools-reference:dsconfig
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/dsconfig.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  dsconfig-description: Description
  dsconfig-options: Options
  dsconfig-subcommands: Subcommands
  exit_codes: Exit codes
  dsconfig-examples: Examples
---

# dsconfig

`dsconfig` — manage PingDS server configuration

## Synopsis

`dsconfig {subcommand} {options}`

## Description

This utility can be used to define a base configuration for the Directory Server.

The `dsconfig` command is the primary command-line tool for viewing and editing the server configuration. When started without arguments, `dsconfig` prompts you for administration connection information, including the host name, administration port number, administrator bind DN and administrator password. The `dsconfig` command then connects securely to the directory server over the administration port. Once connected it presents you with a menu-driven interface to the server configuration.

When you pass connection information, subcommands, and additional options to `dsconfig` , the command runs in script mode and so is not interactive, though it can prompt you to ask whether to apply changes and whether to trust certificates (unless you use the `--no-prompt` and `--trustAll` options, respectively).

You can prepare `dsconfig` batch scripts by running the tool with the `--commandFilePath` option in interactive mode, then reading from the batch file with the `--batchFilePath` option in script mode. Batch files can be useful when you have many `dsconfig` commands to run and want to avoid starting the JVM for each command. Alternatively, you can read commands from standard input by using the `--batch` option.

The `dsconfig` command categorizes directory server configuration into *components* , also called *managed objects* . Actual components often inherit from a parent component type. For example, one component is a Connection Handler. An LDAP Connection Handler is a type of Connection Handler. You configure the LDAP Connection Handler component to specify how the server handles LDAP connections coming from client applications.

Configuration components have *properties* . For example, the LDAP Connection Handler component has properties such as `listen-port` and `allow-start-tls` . You can set the component's `listen-port` property to `389` to use the default LDAP port number. You can set the component's `allow-start-tls` property to `true` to permit LDAP client applications to use StartTLS. Much of the configuration you do with `dsconfig` involves setting component properties.

## Options

The `dsconfig` command takes the following options:

Command options:

* `--batch`

  Reads from standard input a set of commands to be executed. Default: false

* `--commandFilePath {path}`

  The full path to the file where the equivalent non-interactive commands will be written when this command is run in interactive mode.

* `--configFile {configFile}`

  Path to the Directory Server configuration file. Default: /path/to/opendj/config/config.ldif

* `--help-all`

  Display all subcommands. Default: false

* `--help-core-server`

  Display subcommands relating to core server. Default: false

* `--help-database`

  Display subcommands relating to caching and backends. Default: false

* `--help-logging`

  Display subcommands relating to logging. Default: false

* `--help-proxy`

  Display subcommands relating to directory proxy. Default: false

* `--help-replication`

  Display subcommands relating to replication. Default: false

* `--help-security`

  Display subcommands relating to authentication and authorization. Default: false

* `--help-service-discovery`

  Display subcommands relating to service discovery mechanism. Default: false

* `--help-user-management`

  Display subcommands relating to user management. Default: false

* `--offline`

  Indicates that the command must be run in offline mode. Default: false

Configuration Options

* `--advanced`

  Allows the configuration of advanced components and properties. Default: false

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

Utility input/output options:

* `-F | --batchFilePath {batchFilePath}`

  Path to a batch file containing a set of commands to be executed.

* `-n | --no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-Q | --quiet`

  Use quiet mode. Default: false

* `-s | --script-friendly`

  Use script-friendly mode. Default: false

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Subcommands

The `dsconfig` command provides many subcommands.

Subcommands let you create, list, and delete entire configuration components, and get and set component properties. Subcommands have names that reflect these five actions:

* create- *component*

* list- *component* s

* delete- *component*

* get- *component* -prop

* set- *component* -prop

Here, *component* names are names of managed object types. Subcommand *component* names are lower-case, hyphenated versions of the friendly names. When you act on an actual configuration component, you provide the name of the component as an option argument.

For example, the Log Publisher component has these corresponding subcommands.

* `create-log-publisher`

* `list-log-publishers`

* `delete-log-publisher`

* `get-log-publisher-prop`

* `set-log-publisher-prop`

When you create or delete Log Publisher components and when you get and set their configuration properties, you provide the name of the actual log publisher, which you can find by using the `list-log-publishers` subcommand:

```
# Get the log publishers' names:
$ dsconfig \
 list-log-publishers \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --usePkcs12TrustStore /path/to/opendj/config/keystore \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
Log Publisher                      : Type                   : enabled
-----------------------------------:------------------------:--------
...
Json File-Based Access Logger      : json-file-access       : true
...

# Use the name to read a property:
$ dsconfig \
 get-log-publisher-prop \
 --publisher-name "Json File-Based Access Logger" \
 --property rotation-policy \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --usePkcs12TrustStore /path/to/opendj/config/keystore \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
Property        : Value(s)
----------------:--------------------------------------------------------------
rotation-policy : 24 Hours Time Limit Rotation Policy, Size Limit Rotation
                : Policy
```

Many subcommands let you set property values. Notice in the reference for the subcommands below that specific options are available for handling multi-valued properties. Whereas you can assign a single property value by using the `--set` option, you assign multiple values to a multi-valued property by using the `--add` option. You can reset the values of the multi-valued property by using the `--reset` option.

Some property values take a time duration. Durations are expressed as numbers followed by units. For example `1 s` means one second, and `2 w` means two weeks. Some durations have minimum granularity or maximum units, so you cannot necessary specify every duration in milliseconds or weeks for example. Some durations allow you to use a special value to mean unlimited. Units are specified as follows.

* `ms` : milliseconds

* `s` : seconds

* `m` : minutes

* `h` : hours

* `d` : days

* `w` : weeks

* `y` : years

Use the `--help*` options described above to view help for subcommands.

For help with individual subcommands, either use `dsconfig subcommand --help` , or start `dsconfig` in interactive mode, without specifying a subcommand.

To view all component properties, use the `dsconfig list-properties` command.

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

## Examples

The following example starts the `dsconfig` command in interactive, menu-driven mode:

```
$ dsconfig \
 --hostname localhost \
 --port 4444 \
 --bindDn "uid=admin" \
 --bindPassword password \
 --usePkcs12TrustStore /path/to/opendj/config/keystore \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin

>>>> OpenDJ configuration console main menu

What do you want to configure?

    1)   Access Control Handler               21)  Log Publisher
    2)   Access Log Filtering Criteria        22)  Log Retention Policy
    3)   Account Status Notification Handler  23)  Log Rotation Policy
    4)   Administration Connector             24)  Mail Server
    5)   Alert Handler                        25)  Password Generator
    6)   Backend                              26)  Password Policy
    7)   Backend Index                        27)  Password Storage Scheme
    8)   Backend VLV Index                    28)  Password Validator
    9)   Certificate Mapper                   29)  Plugin
    10)  Connection Handler                   30)  Plugin Root
    11)  Crypto Manager                       31)  Replication Domain
    12)  Debug Target                         32)  Replication Server
    13)  Entry Cache                          33)  Root DSE Backend
    14)  Extended Operation Handler           34)  SASL Mechanism Handler
    15)  Global Access Control Policy         35)  Schema Provider
    16)  Global Configuration                 36)  Service Discovery Mechanism
    17)  HTTP Authorization Mechanism         37)  Synchronization Provider
    18)  HTTP Endpoint                        38)  Trust Manager Provider
    19)  Identity Mapper                      39)  Virtual Attribute
    20)  Key Manager Provider                 40)  Work Queue

    a)   show advanced components and properties
    q)   quit

Enter choice:
```

Use the interactive mode to discover the commands that you can reuse to script configuration changes. When you apply a change in interactive mode, the `dsconfig` command displays the corresponding command.

When the server is stopped, you can run the commands offline, and batch them together. The following example sets global properties, and creates a logger that writes messages to the console:

```
dsconfig --offline --no-prompt --batch << END_OF_COMMAND_INPUT
set-global-configuration-prop --set "server-id:&{ds.server.id|evaluation-only}"
set-global-configuration-prop --set "group-id:&{ds.group.id|default}"
set-global-configuration-prop --set "advertised-listen-address:&{ds.advertised.listen.address|localhost}"
create-log-publisher --type console-error --publisher-name "Console Error Logger" --set enabled:true
END_OF_COMMAND_INPUT
```

---

---
title: dskeymgr
description: dskeymgr — manage public key infrastructure in private deployments
component: pingds
version: 8.1
page_id: pingds:tools-reference:dskeymgr
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/dskeymgr.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  dskeymgr-description: Description
  dskeymgr-options: Options
  dskeymgr-subcommands: Subcommands
  dskeymgr_create_deployment_id: dskeymgr create-deployment-id
  options: Options
  dskeymgr_create_tls_key_pair: dskeymgr create-tls-key-pair
  options_2: Options
  dskeymgr_export_ca_cert: dskeymgr export-ca-cert
  options_3: Options
  dskeymgr_export_master_key_pair: dskeymgr export-master-key-pair
  options_4: Options
  dskeymgr_show_deployment_id: dskeymgr show-deployment-id
  exit_codes: Exit codes
  dskeymgr-examples: Examples
---

# dskeymgr

`dskeymgr` — manage public key infrastructure in private deployments

## Synopsis

`dskeymgr {subcommand} {options}`

## Description

This utility can be used for provisioning and managing TLS certificates for use in private deployments.

Subcommands easily allow to:

* Create a deployment CA certificate

* Distribute the CA certificate to all deployed applications

* Provision each application with a TLS key pair signed by the deployment CA

* Rotate the TLS key pairs

Subcommands take several seconds to run because the tool uses a computationally expensive algorithm for hashing the deployment ID password.

## Options

The `dskeymgr` command takes the following options:

Utility input/output options:

* `-n | --no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Subcommands

The `dskeymgr` command supports the following subcommands:

### dskeymgr create-deployment-id

`dskeymgr create-deployment-id {options}`

Creates a new deployment ID.

#### Options

In addition to the global `dskeymgr` options, the `dskeymgr create-deployment-id` subcommand takes the following options:

* `-f | --outputFile {outputFile}`

  Optional path to a file where the deployment ID will be written, overwriting the file if it already exists.

* `-v | --validity {validity}`

  The duration for which the CA certificate associated with the deployment ID will be valid. Examples: '20years', '1days'. Default: 10 y

* `-w | --deploymentIdPassword[:env|:file] {deploymentIdPassword}`

  The deployment ID password.

### dskeymgr create-tls-key-pair

`dskeymgr create-tls-key-pair {options}`

Creates a TLS key-pair signed by the CA associated with a deployment ID and exports it to a keystore or as a PEM file.

#### Options

In addition to the global `dskeymgr` options, the `dskeymgr create-tls-key-pair` subcommand takes the following options:

* `-a | --alias {alias}`

  The TLS key-pair alias, any entry with the same alias will be overwritten. Default: ssl-key-pair

* `-f | --outputFile {pemFile}`

  Optional path to a file with a .pem extension. The command writes the key(s) to the file in PEM format, overwriting the file if it exists.

* `-h | --hostname {hostname}`

  The hostname(s) that will be added to the TLS certificate alternative name extension. Multiple hostnames may be given by providing this argument multiple times. Hostnames can start with a wildcard. Default: localhost

* `-k | --deploymentId {deploymentId}`

  The deployment ID.

* `-K | --keyStoreFile {keyStoreFile}`

  Optional path to an existing PKCS12 keystore file or a path indicating where a new keystore file should be created.

* `-r | --writableReplica`

  Indicates that the server using the certificate is specifically allowed to send updates to other servers. Default: false

* `-s | --subjectDn {subjectDn}`

  The TLS certificate subject DN.

* `-v | --validity {validity}`

  The duration for which the TLS certificate will be valid. Examples: '1days', '12hours', '1d 12h'. Default: 1 y

* `-w | --deploymentIdPassword[:env|:file] {deploymentIdPassword}`

  The deployment ID password.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

### dskeymgr export-ca-cert

`dskeymgr export-ca-cert {options}`

Exports the CA certificate associated with a deployment ID to a keystore or as a PEM file.

#### Options

In addition to the global `dskeymgr` options, the `dskeymgr export-ca-cert` subcommand takes the following options:

* `-a | --alias {alias}`

  The CA certificate alias, must not already exist in the keystore. Default: ca-cert

* `-f | --outputFile {pemFile}`

  Optional path to a file with a .pem extension. The command writes the key(s) to the file in PEM format, overwriting the file if it exists.

* `-k | --deploymentId {deploymentId}`

  The deployment ID.

* `-K | --keyStoreFile {keyStoreFile}`

  Optional path to an existing PKCS12 keystore file or a path indicating where a new keystore file should be created.

* `-w | --deploymentIdPassword[:env|:file] {deploymentIdPassword}`

  The deployment ID password.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

### dskeymgr export-master-key-pair

`dskeymgr export-master-key-pair {options}`

Exports the master key pair associated with a deployment ID to a keystore or as a PEM file.

#### Options

In addition to the global `dskeymgr` options, the `dskeymgr export-master-key-pair` subcommand takes the following options:

* `-a | --alias {alias}`

  The master key pair alias, must not already exist in the keystore. Default: master-key

* `-f | --outputFile {pemFile}`

  Optional path to a file with a .pem extension. The command writes the key(s) to the file in PEM format, overwriting the file if it exists.

* `-k | --deploymentId {deploymentId}`

  The deployment ID.

* `-K | --keyStoreFile {keyStoreFile}`

  Optional path to an existing PKCS12 keystore file or a path indicating where a new keystore file should be created.

* `-w | --deploymentIdPassword[:env|:file] {deploymentIdPassword}`

  The deployment ID password.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

### dskeymgr show-deployment-id

`dskeymgr show-deployment-id deployment-id`

Displays the deployment ID details.

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

## Examples

The following example shows how to create a deployment ID for managing the public key infrastructure of a private deployment:

```
$ dskeymgr \
 create-deployment-id \
 --deploymentIdPassword password \
 --validity "10 years"
AFPxL0RlmdMZHeVkkcC3GYFsAHNlNQ5CBVN1bkVDM7FyW2gWxnvQdQ
```

The following examples show how to use a deployment ID to obtain the deployment CA certificate:

* Export the CA certificate to a file in PEM format:

```
$ dskeymgr \
 export-ca-cert \
 --deploymentId AFPxL0RlmdMZHeVkkcC3GYFsAHNlNQ5CBVN1bkVDM7FyW2gWxnvQdQ \
 --deploymentIdPassword password \
 > ca.pem
```

* Export the CA certificate to a PKCS#12 truststore, creating the truststore if it does not exist:

```
$ dskeymgr \
 export-ca-cert \
 --deploymentId AFPxL0RlmdMZHeVkkcC3GYFsAHNlNQ5CBVN1bkVDM7FyW2gWxnvQdQ \
 --deploymentIdPassword password \
 --keyStoreFile keystore \
 --keyStorePassword secret12 \
 --alias ca-cert
```

The following example shows how to use a deployment ID to generate a TLS key pair signed by the deployment CA certificate and add it to a PKCS#12 keystore, creating the keystore if the keystore file does not exist. In this example, the key pair must be used by an application hosted on `*.example.com` and the application's entry has the DN `cn=test account,cn=service` .

```
$ dskeymgr \
 create-tls-key-pair \
 --deploymentId AFPxL0RlmdMZHeVkkcC3GYFsAHNlNQ5CBVN1bkVDM7FyW2gWxnvQdQ \
 --deploymentIdPassword password \
 --subjectDn "cn=test account,cn=service" \
 --hostname "*.example.com" \
 --validity "1 days" \
 --keyStoreFile keystore \
 --keyStorePassword secret12 \
 --alias tls-key-pair
```

In the example above, the key pair is only valid for one day. When it is about to expire, run the same command again to replace the old key pair having the alias `tls-key-pair` with a new one.

The following example shows how to display important information about a deployment ID:

```
$ dskeymgr show-deployment-id AFPxL0RlmdMZHeVkkcC3GYFsAHNlNQ5CBVN1bkVDM7FyW2gWxnvQdQ

Not before: 2019-06-27T12:42:29Z
Not after: 2029-06-24T12:42:29Z
Version: 0
Serial number: 33B1725B6816C67BD075
Provider name: SunEC
```

---

---
title: dsrepl
description: dsrepl — Manages data synchronization between servers
component: pingds
version: 8.1
page_id: pingds:tools-reference:dsrepl
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/dsrepl.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  dsrepl-description: Description
  dsrepl-options: Options
  dsrepl-subcommands: Subcommands
  dsrepl_add_local_server_to_pre_7_0_topology: dsrepl add-local-server-to-pre-7-0-topology
  options: Options
  dsrepl_cleanup_migrated_pre_7_0_topology: dsrepl cleanup-migrated-pre-7-0-topology
  options_2: Options
  dsrepl_clear_changelog: dsrepl clear-changelog
  dsrepl_decode_csn: dsrepl decode-csn
  dsrepl_disaster_recovery: dsrepl disaster-recovery
  options_3: Options
  dsrepl_initialize: dsrepl initialize
  options_4: Options
  dsrepl_purge_meta_data: dsrepl purge-meta-data
  options_5: Options
  dsrepl_status: dsrepl status
  options_6: Options
  exit_codes: Exit codes
---

# dsrepl

`dsrepl` — Manages data synchronization between servers

## Synopsis

`dsrepl {subcommand} {options}`

## Description

This tool manages data synchronization between servers. For replication to work you must initialize the contents of one of the servers with the contents of the others using the 'initialize' subcommand.

## Options

The `dsrepl` command takes the following options:

Utility input/output options:

* `-n | --no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Subcommands

The `dsrepl` command supports the following subcommands:

### dsrepl add-local-server-to-pre-7-0-topology

`dsrepl add-local-server-to-pre-7-0-topology {options}`

Adds the local server (with version 7.0 or more) to a topology with older server versions (prior to 7.0).

#### Options

In addition to the global `dsrepl` options, the `dsrepl add-local-server-to-pre-7-0-topology` subcommand takes the following options:

SubCommand Options:

* `-b | --baseDn {baseDN}`

  Base DN(s) to replicate.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: cn=admin,cn=Administrators,cn=admin data

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

### dsrepl cleanup-migrated-pre-7-0-topology

`dsrepl cleanup-migrated-pre-7-0-topology {options}`

Clean all the servers (with version 7.0 or more) that have been migrated from a topology of older servers (version prior to 7.0).

#### Options

In addition to the global `dsrepl` options, the `dsrepl cleanup-migrated-pre-7-0-topology` subcommand takes the following options:

SubCommand Options:

* `--bootstrapServer {serverSource}`

  Server ID of the server containing the source data.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

### dsrepl clear-changelog

`dsrepl clear-changelog`

Clears all replication server changelog data for the offline local server; the other replication servers in the topology will transfer any needed data when the server restarts.

### dsrepl decode-csn

`dsrepl decode-csn csn [csn …​]`

Decodes one or more CSNs and displays them in a human readable JSON format.

### dsrepl disaster-recovery

`dsrepl disaster-recovery {options}`

Performs disaster recovery on the local server. The subcommand has two forms.

The first form verifies each replica has the same data after recovery: on a replica, run

dsrepl disaster-recovery --baseDn dc=example,dc=com --generate-recovery-id

The command prints the identifier to use on all other servers with the --generated-id option:

dsrepl disaster-recovery --baseDn dc=example,dc=com --generated-id {identifier}

The second form uses an identifier you provide. It lets you automate the recovery process when you cannot use the first form. Do not use this form if the topology has standalone replication servers. With this form of the subcommand, you must ensure you recover each replica with the same data. Run the same subcommand on all servers.

Example:

dsrepl disaster-recovery --baseDn dc=example,dc=com --user-generated-id Recovery\_Date\_20240101

Read the documentation on disaster recovery carefully before using this command.

#### Options

In addition to the global `dsrepl` options, the `dsrepl disaster-recovery` subcommand takes the following options:

* `-b | --baseDn {baseDN}`

  Base DN of the domain to be recovered.

* `--generate-recovery-id`

  Generate a disaster recovery identifier during recovery. Use this for the first directory server in a replication topology with standalone RS servers. For all subsequent servers to recover, omit this option and use --generated-id {generatedRecoveryId} with the generated identifier. Default: false

* `--generated-id {generatedRecoveryId}`

  Use the disaster recovery identifier generated on the first server. You must use the same identifier for all servers involved in the same disaster recovery procedure.

* `--user-generated-id {userGeneratedRecoveryId}`

  Set the identifier for this recovery to {userGeneratedRecoveryId}, a string of your choice. Do not use this option if the replication topology has standalone RS servers. You must use the same identifier for all servers involved in the same disaster recovery procedure.

### dsrepl initialize

`dsrepl initialize {options}`

Initialize replication data for the server.

#### Options

In addition to the global `dsrepl` options, the `dsrepl initialize` subcommand takes the following options:

SubCommand Options:

* `-b | --baseDn {baseDN}`

  Base DN(s) to use. Multiple base DNs can be provided by using this option multiple times.

* `--fromServer {serverSource}`

  Server ID of the server containing the source data.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `--toAllServers`

  Initialize all the other servers in the topology. Default: false

* `--toServer {serverToInitialize}`

  Server ID of the server to be initialized.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

### dsrepl purge-meta-data

`dsrepl purge-meta-data {options}`

Purges old replication meta-data from application data.

#### Options

In addition to the global `dsrepl` options, the `dsrepl purge-meta-data` subcommand takes the following options:

SubCommand Options:

* `-b | --baseDn {baseDN}`

  Base DN(s) to use. Multiple base DNs can be provided by using this option multiple times.

* `--completionNotify {emailAddress}`

  Email address of a recipient to be notified when the task completes. This option may be specified more than once.

* `--dependency {taskID}`

  ID of a task upon which this task depends. A task will not start execution until all its dependencies have completed execution.

* `--description {description}`

  Gives a description to the task.

* `--errorNotify {emailAddress}`

  Email address of a recipient to be notified if an error occurs when this task executes. This option may be specified more than once.

* `--failedDependencyAction {action}`

  Action this task will take should one if its dependent tasks fail. The value must be one of PROCESS, CANCEL, DISABLE. If not specified defaults to CANCEL.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `--maximumDuration {maximum duration in seconds}`

  Maximum duration of the command in seconds. Default: 3600

* `--recurringTask {schedulePattern}`

  Indicates the task is recurring and will be scheduled according to the value argument expressed in crontab(5) compatible time/date pattern. The schedule pattern for a recurring task supports only the following `crontab` features:

| Field        | Allowed Values    |
| ------------ | ----------------- |
| minute       | 0-59              |
| hour         | 0-23              |
| day of month | 1-31              |
| month        | 1-12              |
| day of week  | 0-6 (0 is Sunday) |

A field can contain an asterisk, `*` . An asterisk stands for `first-last` .

Fields can include ranges of numbers. A range is two numbers separated by a hyphen, and is inclusive. For example, `8-10` for an "hour" field means execution at hours 8, 9, and 10.

Fields can include lists. A list is a set of numbers or ranges separated by commas. For example, `4,8-10` for an "hour" field means execution at hours 4, 8, 9, and 10.

* `-t | --start {startTime}`

  Indicates the date/time at which this operation will start when scheduled as a server task expressed in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the task to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* `--taskId {taskID}`

  Gives an ID to the task.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

### dsrepl status

`dsrepl status {options}`

Displays the status of the replication service and various diagnostics about it. The information is derived from reading cn=monitor on all the servers in the replication topology.

The status of a server is one of the following.

* BAD - DATA MISMATCH: either the fractional replication configuration does not match the backend data, or the initial state of the replicated data does not match other servers and this server must be re-initialized;

* BAD - TOO LATE: the server has fallen further behind than the replication purge delay and must be re-initialized;

* GOOD: normal operation, nothing to do;

* SLOW: the server's replay delay is greater than five seconds;

* UNHEALTHY: read the server health errors in the server monitoring data for details.

#### Options

In addition to the global `dsrepl` options, the `dsrepl status` subcommand takes the following options:

SubCommand Options:

* `-b | --baseDn {baseDN}`

  Base DN(s) to display. Multiple base DNs can be provided by using this option multiple times. If no base DNs are provided, then all the base DNs will be displayed.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `--showChangelogs`

  Displays individual changelog servers in the output. Default: false

* `--showGroups`

  Display replication group information in the output. Default: false

* `--showReplicas`

  Displays individual replicas in the output. Default: false

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=monitor

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

---

---
title: encode-password
description: encode-password — encode a password with a storage scheme
component: pingds
version: 8.1
page_id: pingds:tools-reference:encode-password
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/encode-password.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  encode-password-description: Description
  encode-password-options: Options
  exit_codes: Exit codes
---

# encode-password

`encode-password` — encode a password with a storage scheme

## Synopsis

`encode-password {options}`

## Description

This utility can be used to encode user passwords with a specified storage scheme, or to determine whether a given clear-text value matches a provided encoded password.

## Options

The `encode-password` command takes the following options:

Command options:

* `-a | --authPasswordSyntax`

  Use the authentication password syntax rather than the user password syntax. Default: false

* `-c | --clearPassword[:env|:file] {clearPW}`

  Clear-text password to encode or to compare against an encoded password.

* `-e | --encodedPassword[:env|:file] {encodedPW}`

  Encoded password to compare against the clear-text password.

* `-i | --interactivePassword`

  The password to encode or to compare against an encoded password is interactively asked to the user. Default: false

* `-l | --listSchemes`

  List available password storage schemes. Default: false

* `-r | --useCompareResultCode`

  Use the LDAP compare result as an exit code for the password comparison. Default: false

* `-s | --storageScheme {scheme}`

  Scheme to use for the encoded password.

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* 5

  The `-r` option was used, and the compare did not match.

* 6

  The `-r` option was used, and the compare did match.

* other

  An error occurred.

---

---
title: export-ldif
description: export-ldif — export directory data in LDIF
component: pingds
version: 8.1
page_id: pingds:tools-reference:export-ldif
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/export-ldif.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  export-ldif-description: Description
  export-ldif-options: Options
  exit_codes: Exit codes
---

# export-ldif

`export-ldif` — export directory data in LDIF

## Synopsis

`export-ldif {options}`

## Description

This utility can be used to export data from a Directory Server backend in LDIF form.

## Options

The `export-ldif` command takes the following options:

Command options:

* `-a | --appendToLdif`

  Append an existing LDIF file rather than overwriting it. Default: false

* `-b | --includeBranch {branchDN}`

  Base DN of a branch to include in the LDIF export.

* `-B | --excludeBranch {branchDN}`

  Base DN of a branch to exclude from the LDIF export.

* `-c | --compress`

  Compress the LDIF data as it is exported. Default: false

* `-e | --excludeAttribute {attribute}`

  Attribute to exclude from the LDIF export.

* `--excludeFilter {filter}`

  Filter to identify entries to exclude from the LDIF export.

* `-i | --includeAttribute {attribute}`

  Attribute to include in the LDIF export.

* `--includeFilter {filter}`

  Filter to identify entries to include in the LDIF export.

* `-l | --ldifFile {ldifFile}`

  Path to the LDIF file to write. All paths are relative to the server's installation directory, which can be remote.

* `-n | --backendId {backendName}`

  Backend ID for the backend to export.

* `-O | --excludeOperational`

  Exclude operational attributes from the LDIF export. Default: false

* `--offline`

  Indicates that the command must be run in offline mode. Default: false

Task Scheduling Options

* `--completionNotify {emailAddress}`

  Email address of a recipient to be notified when the task completes. This option may be specified more than once.

* `--dependency {taskID}`

  ID of a task upon which this task depends. A task will not start execution until all its dependencies have completed execution.

* `--description {description}`

  Gives a description to the task.

* `--errorNotify {emailAddress}`

  Email address of a recipient to be notified if an error occurs when this task executes. This option may be specified more than once.

* `--failedDependencyAction {action}`

  Action this task will take should one if its dependent tasks fail. The value must be one of PROCESS, CANCEL, DISABLE. If not specified defaults to CANCEL.

* `--recurringTask {schedulePattern}`

  Indicates the task is recurring and will be scheduled according to the value argument expressed in crontab(5) compatible time/date pattern. The schedule pattern for a recurring task supports only the following `crontab` features:

| Field        | Allowed Values    |
| ------------ | ----------------- |
| minute       | 0-59              |
| hour         | 0-23              |
| day of month | 1-31              |
| month        | 1-12              |
| day of week  | 0-6 (0 is Sunday) |

A field can contain an asterisk, `*` . An asterisk stands for `first-last` .

Fields can include ranges of numbers. A range is two numbers separated by a hyphen, and is inclusive. For example, `8-10` for an "hour" field means execution at hours 8, 9, and 10.

Fields can include lists. A list is a set of numbers or ranges separated by commas. For example, `4,8-10` for an "hour" field means execution at hours 4, 8, 9, and 10.

* `-t | --start {startTime}`

  Indicates the date/time at which this operation will start when scheduled as a server task expressed in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the task to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* `--taskId {taskID}`

  Gives an ID to the task.

Task Backend Connection Options

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `--wrapColumn {wrapColumn}`

  Column at which to wrap long lines (0 for no wrapping). Default: 0

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

---

---
title: import-ldif
description: import-ldif — import directory data from LDIF
component: pingds
version: 8.1
page_id: pingds:tools-reference:import-ldif
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/import-ldif.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  import-ldif-description: Description
  import-ldif-options: Options
  exit_codes: Exit codes
---

# import-ldif

`import-ldif` — import directory data from LDIF

## Synopsis

`import-ldif {options}`

## Description

This utility can be used to import LDIF data into a Directory Server backend, overwriting existing data. It cannot be used to append data to the backend database.

## Options

The `import-ldif` command takes the following options:

Command options:

* `-A | --templateFile {templateFile}`

  Path to a MakeLDIF template to use to generate the import data.

* `-b | --includeBranch {branchDN}`

  Base DN of a branch to include in the LDIF import.

* `-B | --excludeBranch {branchDN}`

  Base DN of a branch to exclude from the LDIF import.

* `-c | --isCompressed`

  LDIF file is compressed. Default: false

* `--countRejects`

  Count the number of entries rejected by the server and return that value as the exit code (values > 255 will be reduced to 255 due to exit code restrictions). Default: false

* `-e | --excludeAttribute {attribute}`

  Attribute to exclude from the LDIF import.

* `--excludeFilter {filter}`

  Filter to identify entries to exclude from the LDIF import.

* `-F | --clearBackend`

  Remove all entries for all base DNs in the backend before importing. Default: false

* `-i | --includeAttribute {attribute}`

  Attribute to include in the LDIF import.

* `--includeFilter {filter}`

  Filter to identify entries to include in the LDIF import.

* `-l | --ldifFile {ldifFile}`

  Path to the LDIF file to import. All paths are relative to the server's installation directory, which can be remote.

* `-n | --backendId {backendName}`

  Backend ID for the backend to import.

* `-O | --overwrite`

  Overwrite an existing rejects and/or skip file rather than appending to it. Default: false

* `--offline`

  Indicates that the command must be run in offline mode. When using this option, the command writes to server files. Run the command as a user having the same filesystem permissions as the user running the server. Default: false

* `-R | --rejectFile {rejectFile}`

  Write rejected entries to the specified file.

* `-s | --randomSeed {seed}`

  Seed for the MakeLDIF random number generator. To always generate the same data with the same command, use the same non-zero seed value. A value of zero (the default) results in different data each time the tool is run. Default: 0

* `-S | --skipSchemaValidation`

  Skip schema validation during the LDIF import. Default: false

* `--skipFile {skipFile}`

  Write skipped entries to the specified file.

* `--threadCount {count}`

  Number of threads used to read LDIF files during import. If 0, the number of threads will be set to twice the number of CPUs. Default: 0

* `--tmpDirectory {directory}`

  Path to temporary directory for index scratch files during LDIF import. Default: import-tmp

Task Scheduling Options

* `--completionNotify {emailAddress}`

  Email address of a recipient to be notified when the task completes. This option may be specified more than once.

* `--dependency {taskID}`

  ID of a task upon which this task depends. A task will not start execution until all its dependencies have completed execution.

* `--description {description}`

  Gives a description to the task.

* `--errorNotify {emailAddress}`

  Email address of a recipient to be notified if an error occurs when this task executes. This option may be specified more than once.

* `--failedDependencyAction {action}`

  Action this task will take should one if its dependent tasks fail. The value must be one of PROCESS, CANCEL, DISABLE. If not specified defaults to CANCEL.

* `--recurringTask {schedulePattern}`

  Indicates the task is recurring and will be scheduled according to the value argument expressed in crontab(5) compatible time/date pattern. The schedule pattern for a recurring task supports only the following `crontab` features:

| Field        | Allowed Values    |
| ------------ | ----------------- |
| minute       | 0-59              |
| hour         | 0-23              |
| day of month | 1-31              |
| month        | 1-12              |
| day of week  | 0-6 (0 is Sunday) |

A field can contain an asterisk, `*` . An asterisk stands for `first-last` .

Fields can include ranges of numbers. A range is two numbers separated by a hyphen, and is inclusive. For example, `8-10` for an "hour" field means execution at hours 8, 9, and 10.

Fields can include lists. A list is a set of numbers or ranges separated by commas. For example, `4,8-10` for an "hour" field means execution at hours 4, 8, 9, and 10.

* `-t | --start {startTime}`

  Indicates the date/time at which this operation will start when scheduled as a server task expressed in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the task to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* `--taskId {taskID}`

  Gives an ID to the task.

Task Backend Connection Options

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default: uid=admin

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server administration port number.

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-Q | --quiet`

  Use quiet mode (no output). Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* \> 0

  An error occurred.

---

---
title: ldapcompare
description: ldapcompare — perform LDAP compare operations
component: pingds
version: 8.1
page_id: pingds:tools-reference:ldapcompare
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/ldapcompare.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  ldapcompare-description: Description
  ldapcompare-options: Options
  ldapcompare-exit-codes: Exit codes
  files: Files
---

# ldapcompare

`ldapcompare` — perform LDAP compare operations

## Synopsis

`ldapcompare {options} attribute:value DN`

## Description

This utility can be used to perform LDAP compare operations in the Directory Server.

## Options

The `ldapcompare` command takes the following options:

Command options:

* `--assertionFilter {filter}`

  Use the LDAP assertion control with the provided filter.

* `-J | --control {controloid[:criticality[:value|::b64value|:<filePath]]}`

  Use a request control with the provided information. For some *controloid* values, you can replace object identifiers with user-friendly strings. The values are not case-sensitive:

  * `Assertion` , `LdapAssertion`

    Assertion Request Control, Object Identifier: 1.3.6.1.1.12

  * `AccountUsable` , `AccountUsability`

    Account Usability Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.8

  * `AuthzId` , `AuthorizationIdentity`

    Authorization Identity Request Control, Object Identifier: 2.16.840.1.113730.3.4.16

  * `Csn` , `ChangeSequenceNumber`

    Change Sequence Number Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.9 This is an internal DS server control.

  * `EffectiveRights` , `GetEffectiveRights`

    Get Effective Rights Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.2

  * `ManageDsaIt`

    Manage DSAIT Request Control, Object Identifier: 2.16.840.1.113730.3.4.2

  * `Noop` , `No-Op`

    No-Op Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.2

  * `PwdPolicy` , `PasswordPolicy`

    Password Policy Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.8.5.1

  * `PasswordQualityAdvice`

    Password Quality Advice Request Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.5

  * `PermissiveModify`

    Permissive Modify Request Control, Object Identifier: 1.2.840.113556.1.4.1413

  * `PSearch` , `PersistentSearch`

    Persistent Search Request Control, Object Identifier: 2.16.840.1.113730.3.4.3

  * `PostRead`

    Post Read Request Control, Object Identifier: 1.3.6.1.1.13.2

  * `PreRead`

    Pre Read Request Control, Object Identifier: 1.3.6.1.1.13.1

  * `ProxiedAuthV1`

    Proxied Authorization Request Control V1, Object Identifier: 2.16.840.1.113730.3.4.12

  * `ProxiedAuth` , `ProxiedAuthV2`

    Proxied Authorization Request Control V2, Object Identifier: 2.16.840.1.113730.3.4.18

  * `RealAttrsOnly` , `RealAttributesOnly`

    Real Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.17

  * `RelaxRules`

    Relax Rules Request Control, Object Identifier: 1.3.6.1.4.1.4203.666.5.12

  * `TreeDelete` , `SubTreeDelete`

    Subtree Delete Request Control, Object Identifier: 1.2.840.113556.1.4.805

  * `Sort` , `ServerSideSort`

    Server Side Sort Request Control, Object Identifier: 1.2.840.113556.1.4.473

  * `PagedResults` , `SimplePagedResults`

    Simple Paged Results Control, Object Identifier: 1.2.840.113556.1.4.319

  * `SubEntries`

    Sub-Entries Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.1

  * `TxnId` , `TransactionId`

    Transaction ID Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.1 This is an internal ForgeRock control.

  * `VirtualAttrsOnly` , `VirtualAttributesOnly`

    Virtual Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.19

  * `Vlv` , `VirtualListView`

    Virtual List View Request Control, Object Identifier: 2.16.840.1.113730.3.4.9

* `-m | --useCompareResultCode`

  Use the LDAP compare result as an exit code for the LDAP compare operations. Default: false

* `-n | --dry-run`

  Show what would be done but do not perform any operation and do not contact the server. Default: false

* `-S | --scriptFriendly`

  Use script-friendly mode. Default: false

* `-Y | --proxyAs {authzID}`

  Use the proxied authorization control with the given authorization ID.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default:

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server port number.

* `-q | --useStartTls`

  Use StartTLS to secure communication with the server. Default: false

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

* `-Z | --useSsl`

  Use SSL for secure communication with the server. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* 5

  The LDAP compare operation did not match.

* 6

  The `-m` option was used, and the LDAP compare operation did match.

* ldap-error

  An LDAP error occurred while processing the operation. LDAP result codes are described in [RFC 4511](https://www.rfc-editor.org/rfc/rfc4511.html#appendix-A) . Also see the additional information for details.

* 89

  An error occurred while parsing the command-line arguments.

## Files

You can use `~/.opendj/tools.properties` to set the defaults for bind DN, host name, and port number as in the following example:

```
hostname=directory.example.com
port=1389
bindDN=uid=kvaughan,ou=People,dc=example,dc=com

ldapcompare.port=1389
ldapdelete.port=1389
ldapmodify.port=1389
ldappasswordmodify.port=1389
ldapsearch.port=1389
```

---

---
title: ldapdelete
description: ldapdelete — perform LDAP delete operations
component: pingds
version: 8.1
page_id: pingds:tools-reference:ldapdelete
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/ldapdelete.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  ldapdelete-description: Description
  ldapdelete-options: Options
  exit_codes: Exit codes
  files: Files
---

# ldapdelete

`ldapdelete` — perform LDAP delete operations

## Synopsis

`ldapdelete {options} [DN]`

## Description

This utility can be used to perform LDAP delete operations in the Directory Server.

If standard input is used to specify entries to remove, end your input with EOF (Ctrl+D on UNIX, Ctrl+Z on Windows).

## Options

The `ldapdelete` command takes the following options:

Command options:

* `-c | --continueOnError`

  Continue processing even if there are errors. Default: false

* `-J | --control {controloid[:criticality[:value|::b64value|:<filePath]]}`

  Use a request control with the provided information. For some *controloid* values, you can replace object identifiers with user-friendly strings. The values are not case-sensitive:

  * `Assertion` , `LdapAssertion`

    Assertion Request Control, Object Identifier: 1.3.6.1.1.12

  * `AccountUsable` , `AccountUsability`

    Account Usability Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.8

  * `AuthzId` , `AuthorizationIdentity`

    Authorization Identity Request Control, Object Identifier: 2.16.840.1.113730.3.4.16

  * `Csn` , `ChangeSequenceNumber`

    Change Sequence Number Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.9 This is an internal DS server control.

  * `EffectiveRights` , `GetEffectiveRights`

    Get Effective Rights Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.2

  * `ManageDsaIt`

    Manage DSAIT Request Control, Object Identifier: 2.16.840.1.113730.3.4.2

  * `Noop` , `No-Op`

    No-Op Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.2

  * `PwdPolicy` , `PasswordPolicy`

    Password Policy Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.8.5.1

  * `PasswordQualityAdvice`

    Password Quality Advice Request Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.5

  * `PermissiveModify`

    Permissive Modify Request Control, Object Identifier: 1.2.840.113556.1.4.1413

  * `PSearch` , `PersistentSearch`

    Persistent Search Request Control, Object Identifier: 2.16.840.1.113730.3.4.3

  * `PostRead`

    Post Read Request Control, Object Identifier: 1.3.6.1.1.13.2

  * `PreRead`

    Pre Read Request Control, Object Identifier: 1.3.6.1.1.13.1

  * `ProxiedAuthV1`

    Proxied Authorization Request Control V1, Object Identifier: 2.16.840.1.113730.3.4.12

  * `ProxiedAuth` , `ProxiedAuthV2`

    Proxied Authorization Request Control V2, Object Identifier: 2.16.840.1.113730.3.4.18

  * `RealAttrsOnly` , `RealAttributesOnly`

    Real Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.17

  * `RelaxRules`

    Relax Rules Request Control, Object Identifier: 1.3.6.1.4.1.4203.666.5.12

  * `TreeDelete` , `SubTreeDelete`

    Subtree Delete Request Control, Object Identifier: 1.2.840.113556.1.4.805

  * `Sort` , `ServerSideSort`

    Server Side Sort Request Control, Object Identifier: 1.2.840.113556.1.4.473

  * `PagedResults` , `SimplePagedResults`

    Simple Paged Results Control, Object Identifier: 1.2.840.113556.1.4.319

  * `SubEntries`

    Sub-Entries Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.1

  * `TxnId` , `TransactionId`

    Transaction ID Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.1 This is an internal ForgeRock control.

  * `VirtualAttrsOnly` , `VirtualAttributesOnly`

    Virtual Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.19

  * `Vlv` , `VirtualListView`

    Virtual List View Request Control, Object Identifier: 2.16.840.1.113730.3.4.9

* `-n | --dry-run`

  Show what would be done but do not perform any operation and do not contact the server. Default: false

* `--numConnections {numConnections}`

  Number of connections. Default: 1

* `-x | --deleteSubtree`

  Delete the specified entry and all entries below it. Default: false

* `-Y | --proxyAs {authzID}`

  Use the proxied authorization control with the given authorization ID.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default:

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server port number.

* `-q | --useStartTls`

  Use StartTLS to secure communication with the server. Default: false

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

* `-Z | --useSsl`

  Use SSL for secure communication with the server. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* ldap-error

  An LDAP error occurred while processing the operation. LDAP result codes are described in [RFC 4511](https://www.rfc-editor.org/rfc/rfc4511.html#appendix-A) . Also see the additional information for details.

* 89

  An error occurred while parsing the command-line arguments.

## Files

You can use `~/.opendj/tools.properties` to set the defaults for bind DN, host name, and port number as in the following example:

```
hostname=directory.example.com
port=1389
bindDN=uid=kvaughan,ou=People,dc=example,dc=com

ldapcompare.port=1389
ldapdelete.port=1389
ldapmodify.port=1389
ldappasswordmodify.port=1389
ldapsearch.port=1389
```

---

---
title: ldapmodify
description: ldapmodify — perform LDAP modify, add, delete, mod DN operations
component: pingds
version: 8.1
page_id: pingds:tools-reference:ldapmodify
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/ldapmodify.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  ldapmodify-description: Description
  ldapmodify-options: Options
  exit_codes: Exit codes
  files: Files
---

# ldapmodify

`ldapmodify` — perform LDAP modify, add, delete, mod DN operations

## Synopsis

`ldapmodify {options} [changes_files …​]`

## Description

This utility can be used to perform LDAP modify, add, delete, and modify DN operations in the Directory Server. When not using file(s) to specify modifications, end your input with EOF (Ctrl+D on UNIX, Ctrl+Z on Windows).

## Options

The `ldapmodify` command takes the following options:

Command options:

* `--assertionFilter {filter}`

  Use the LDAP assertion control with the provided filter.

* `-c | --continueOnError`

  Continue processing even if there are errors. Default: false

* `-J | --control {controloid[:criticality[:value|::b64value|:<filePath]]}`

  Use a request control with the provided information. For some *controloid* values, you can replace object identifiers with user-friendly strings. The values are not case-sensitive:

  * `Assertion` , `LdapAssertion`

    Assertion Request Control, Object Identifier: 1.3.6.1.1.12

  * `AccountUsable` , `AccountUsability`

    Account Usability Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.8

  * `AuthzId` , `AuthorizationIdentity`

    Authorization Identity Request Control, Object Identifier: 2.16.840.1.113730.3.4.16

  * `Csn` , `ChangeSequenceNumber`

    Change Sequence Number Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.9 This is an internal DS server control.

  * `EffectiveRights` , `GetEffectiveRights`

    Get Effective Rights Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.2

  * `ManageDsaIt`

    Manage DSAIT Request Control, Object Identifier: 2.16.840.1.113730.3.4.2

  * `Noop` , `No-Op`

    No-Op Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.2

  * `PwdPolicy` , `PasswordPolicy`

    Password Policy Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.8.5.1

  * `PasswordQualityAdvice`

    Password Quality Advice Request Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.5

  * `PermissiveModify`

    Permissive Modify Request Control, Object Identifier: 1.2.840.113556.1.4.1413

  * `PSearch` , `PersistentSearch`

    Persistent Search Request Control, Object Identifier: 2.16.840.1.113730.3.4.3

  * `PostRead`

    Post Read Request Control, Object Identifier: 1.3.6.1.1.13.2

  * `PreRead`

    Pre Read Request Control, Object Identifier: 1.3.6.1.1.13.1

  * `ProxiedAuthV1`

    Proxied Authorization Request Control V1, Object Identifier: 2.16.840.1.113730.3.4.12

  * `ProxiedAuth` , `ProxiedAuthV2`

    Proxied Authorization Request Control V2, Object Identifier: 2.16.840.1.113730.3.4.18

  * `RealAttrsOnly` , `RealAttributesOnly`

    Real Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.17

  * `RelaxRules`

    Relax Rules Request Control, Object Identifier: 1.3.6.1.4.1.4203.666.5.12

  * `TreeDelete` , `SubTreeDelete`

    Subtree Delete Request Control, Object Identifier: 1.2.840.113556.1.4.805

  * `Sort` , `ServerSideSort`

    Server Side Sort Request Control, Object Identifier: 1.2.840.113556.1.4.473

  * `PagedResults` , `SimplePagedResults`

    Simple Paged Results Control, Object Identifier: 1.2.840.113556.1.4.319

  * `SubEntries`

    Sub-Entries Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.1

  * `TxnId` , `TransactionId`

    Transaction ID Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.1 This is an internal ForgeRock control.

  * `VirtualAttrsOnly` , `VirtualAttributesOnly`

    Virtual Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.19

  * `Vlv` , `VirtualListView`

    Virtual List View Request Control, Object Identifier: 2.16.840.1.113730.3.4.9

* `-n | --dry-run`

  Show what would be done but do not perform any operation and do not contact the server. Default: false

* `--numConnections {numConnections}`

  Number of connections. Default: 1

* `--postReadAttributes {attrList}`

  Use the LDAP ReadEntry post-read control.

* `--preReadAttributes {attrList}`

  Use the LDAP ReadEntry pre-read control.

* `-Y | --proxyAs {authzID}`

  Use the proxied authorization control with the given authorization ID.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default:

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server port number.

* `-q | --useStartTls`

  Use StartTLS to secure communication with the server. Default: false

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

* `-Z | --useSsl`

  Use SSL for secure communication with the server. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* ldap-error

  An LDAP error occurred while processing the operation. LDAP result codes are described in [RFC 4511](https://www.rfc-editor.org/rfc/rfc4511.html#appendix-A) . Also see the additional information for details.

* 89

  An error occurred while parsing the command-line arguments.

## Files

You can use `~/.opendj/tools.properties` to set the defaults for bind DN, host name, and port number as in the following example:

```
hostname=directory.example.com
port=1389
bindDN=uid=kvaughan,ou=People,dc=example,dc=com

ldapcompare.port=1389
ldapdelete.port=1389
ldapmodify.port=1389
ldappasswordmodify.port=1389
ldapsearch.port=1389
```

---

---
title: ldappasswordmodify
description: ldappasswordmodify — perform LDAP password modifications
component: pingds
version: 8.1
page_id: pingds:tools-reference:ldappasswordmodify
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/ldappasswordmodify.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  ldappasswordmodify-description: Description
  ldappasswordmodify-options: Options
  exit_codes: Exit codes
  files: Files
---

# ldappasswordmodify

`ldappasswordmodify` — perform LDAP password modifications

## Synopsis

`ldappasswordmodify {options}`

## Description

This utility can be used to perform LDAP password modify operations in the Directory Server.

## Options

The `ldappasswordmodify` command takes the following options:

Command options:

* `-a | --authzId {authzID}`

  Authorization ID for the user entry whose password should be changed. The authorization ID is a string having either the prefix "dn:" followed by the user's distinguished name, or the prefix "u:" followed by a user identifier that depends on the identity mapping used to match the user identifier to an entry in the directory. Examples include "dn:uid=bjensen,ou=People,dc=example,dc=com", and, if we assume that "bjensen" is mapped to Barbara Jensen's entry, "u:bjensen".

* `-c | --currentPassword[:env|:file] {currentPassword}`

  Current password for the target user.

* `-J | --control {controloid[:criticality[:value|::b64value|:<filePath]]}`

  Use a request control with the provided information. For some *controloid* values, you can replace object identifiers with user-friendly strings. The values are not case-sensitive:

  * `Assertion` , `LdapAssertion`

    Assertion Request Control, Object Identifier: 1.3.6.1.1.12

  * `AccountUsable` , `AccountUsability`

    Account Usability Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.8

  * `AuthzId` , `AuthorizationIdentity`

    Authorization Identity Request Control, Object Identifier: 2.16.840.1.113730.3.4.16

  * `Csn` , `ChangeSequenceNumber`

    Change Sequence Number Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.9 This is an internal DS server control.

  * `EffectiveRights` , `GetEffectiveRights`

    Get Effective Rights Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.2

  * `ManageDsaIt`

    Manage DSAIT Request Control, Object Identifier: 2.16.840.1.113730.3.4.2

  * `Noop` , `No-Op`

    No-Op Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.2

  * `PwdPolicy` , `PasswordPolicy`

    Password Policy Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.8.5.1

  * `PasswordQualityAdvice`

    Password Quality Advice Request Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.5

  * `PermissiveModify`

    Permissive Modify Request Control, Object Identifier: 1.2.840.113556.1.4.1413

  * `PSearch` , `PersistentSearch`

    Persistent Search Request Control, Object Identifier: 2.16.840.1.113730.3.4.3

  * `PostRead`

    Post Read Request Control, Object Identifier: 1.3.6.1.1.13.2

  * `PreRead`

    Pre Read Request Control, Object Identifier: 1.3.6.1.1.13.1

  * `ProxiedAuthV1`

    Proxied Authorization Request Control V1, Object Identifier: 2.16.840.1.113730.3.4.12

  * `ProxiedAuth` , `ProxiedAuthV2`

    Proxied Authorization Request Control V2, Object Identifier: 2.16.840.1.113730.3.4.18

  * `RealAttrsOnly` , `RealAttributesOnly`

    Real Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.17

  * `RelaxRules`

    Relax Rules Request Control, Object Identifier: 1.3.6.1.4.1.4203.666.5.12

  * `TreeDelete` , `SubTreeDelete`

    Subtree Delete Request Control, Object Identifier: 1.2.840.113556.1.4.805

  * `Sort` , `ServerSideSort`

    Server Side Sort Request Control, Object Identifier: 1.2.840.113556.1.4.473

  * `PagedResults` , `SimplePagedResults`

    Simple Paged Results Control, Object Identifier: 1.2.840.113556.1.4.319

  * `SubEntries`

    Sub-Entries Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.1

  * `TxnId` , `TransactionId`

    Transaction ID Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.1 This is an internal ForgeRock control.

  * `VirtualAttrsOnly` , `VirtualAttributesOnly`

    Virtual Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.19

  * `Vlv` , `VirtualListView`

    Virtual List View Request Control, Object Identifier: 2.16.840.1.113730.3.4.9

* `-n | --newPassword[:env|:file] {newPassword}`

  New password to provide for the target user.

* `-Y | --proxyAs {authzID}`

  Use the proxied authorization control with the given authorization ID.

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default:

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server port number.

* `-q | --useStartTls`

  Use StartTLS to secure communication with the server. Default: false

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

* `-Z | --useSsl`

  Use SSL for secure communication with the server. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  The command completed successfully.

* ldap-error

  An LDAP error occurred while processing the operation. LDAP result codes are described in [RFC 4511](https://www.rfc-editor.org/rfc/rfc4511.html#appendix-A) . Also see the additional information for details.

* 89

  An error occurred while parsing the command-line arguments.

## Files

You can use `~/.opendj/tools.properties` to set the defaults for bind DN, host name, and port number as in the following example:

```
hostname=directory.example.com
port=1389
bindDN=uid=kvaughan,ou=People,dc=example,dc=com

ldapcompare.port=1389
ldapdelete.port=1389
ldapmodify.port=1389
ldappasswordmodify.port=1389
ldapsearch.port=1389
```

---

---
title: ldapsearch
description: ldapsearch — perform LDAP search operations
component: pingds
version: 8.1
page_id: pingds:tools-reference:ldapsearch
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/ldapsearch.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  ldapsearch-description: Description
  ldapsearch-options: Options
  filters: Filters
  ldapsearch-attributes: Attributes
  exit_codes: Exit codes
  files: Files
---

# ldapsearch

`ldapsearch` — perform LDAP search operations

## Synopsis

`ldapsearch {options} filter [attributes …​]`

## Description

This utility can be used to perform LDAP search operations in the Directory Server.

## Options

The `ldapsearch` command takes the following options:

Command options:

* `-a | --dereferencePolicy {dereferencePolicy}`

  Alias dereference policy ('never', 'always', 'search', or 'find'). Default: never

* `-A | --typesOnly`

  Only retrieve attribute names but not their values. Default: false

* `--assertionFilter {filter}`

  Use the LDAP assertion control with the provided filter.

* `-b | --baseDn {baseDN}`

  Search base DN.

* `-c | --continueOnError`

  Continue processing even if there are errors. Default: false

* `-C | --persistentSearch ps[:changetype[:changesonly[:entrychgcontrols]]]`

  Use the persistent search control.

  A persistent search allows the client to continue receiving new results whenever changes are made to data that is in the scope of the search, thus using the search as a form of change notification.

  The optional `changetype` setting defines the kinds of updates that result in notification. If you do not set the `changetype` , the default behavior is to send notifications for all updates.

  * `add`

    Send notifications for LDAP add operations.

  * `del` , `delete`

    Send notifications for LDAP delete operations.

  * `mod` , `modify`

    Send notifications for LDAP modify operations.

  * `moddn` , `modrdn` , `modifydn`

    Send notifications for LDAP modify DN (rename and move) operations.

  * `all` , `any`

    Send notifications for all LDAP update operations.

  The optional `changesonly` setting defines whether the server returns existing entries as well as changes.

  * `true`

    Do not return existing entries, but instead only notifications about changes. This is the default setting.

  * `false`

    Also return existing entries.

  The optional `entrychgcontrols` setting defines whether the server returns an Entry Change Notification control with each entry notification. The Entry Change Notification control provides additional information about the change that caused the entry to be returned by the search. In particular, it indicates the change type, the change number if available, and the previous DN if the change type was a modify DN operation.

  * `true`

    Do request the Entry Change Notification control. This is the default setting.

  * `false`

    Do not request the Entry Change Notification control.

* `--countEntries`

  Count the number of entries returned by the server. Default: false

* `-e | --getEffectiveRightsAttribute {attribute}`

  Specifies geteffectiverights control specific attribute list.

* `-g | --getEffectiveRightsAuthzId {authzID}`

  Use geteffectiverights control with the provided authzid.

* `-G | --virtualListView {before:after:index:count | before:after:value}`

  Use the virtual list view control to retrieve the specified results page.

* `-J | --control {controloid[:criticality[:value|::b64value|:<filePath]]}`

  Use a request control with the provided information. For some *controloid* values, you can replace object identifiers with user-friendly strings. The values are not case-sensitive:

  * `Assertion` , `LdapAssertion`

    Assertion Request Control, Object Identifier: 1.3.6.1.1.12

  * `AccountUsable` , `AccountUsability`

    Account Usability Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.8

  * `AuthzId` , `AuthorizationIdentity`

    Authorization Identity Request Control, Object Identifier: 2.16.840.1.113730.3.4.16

  * `Csn` , `ChangeSequenceNumber`

    Change Sequence Number Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.9 This is an internal DS server control.

  * `EffectiveRights` , `GetEffectiveRights`

    Get Effective Rights Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.9.5.2

  * `ManageDsaIt`

    Manage DSAIT Request Control, Object Identifier: 2.16.840.1.113730.3.4.2

  * `Noop` , `No-Op`

    No-Op Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.2

  * `PwdPolicy` , `PasswordPolicy`

    Password Policy Request Control, Object Identifier: 1.3.6.1.4.1.42.2.27.8.5.1

  * `PasswordQualityAdvice`

    Password Quality Advice Request Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.5

  * `PermissiveModify`

    Permissive Modify Request Control, Object Identifier: 1.2.840.113556.1.4.1413

  * `PSearch` , `PersistentSearch`

    Persistent Search Request Control, Object Identifier: 2.16.840.1.113730.3.4.3

  * `PostRead`

    Post Read Request Control, Object Identifier: 1.3.6.1.1.13.2

  * `PreRead`

    Pre Read Request Control, Object Identifier: 1.3.6.1.1.13.1

  * `ProxiedAuthV1`

    Proxied Authorization Request Control V1, Object Identifier: 2.16.840.1.113730.3.4.12

  * `ProxiedAuth` , `ProxiedAuthV2`

    Proxied Authorization Request Control V2, Object Identifier: 2.16.840.1.113730.3.4.18

  * `RealAttrsOnly` , `RealAttributesOnly`

    Real Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.17

  * `RelaxRules`

    Relax Rules Request Control, Object Identifier: 1.3.6.1.4.1.4203.666.5.12

  * `TreeDelete` , `SubTreeDelete`

    Subtree Delete Request Control, Object Identifier: 1.2.840.113556.1.4.805

  * `Sort` , `ServerSideSort`

    Server Side Sort Request Control, Object Identifier: 1.2.840.113556.1.4.473

  * `PagedResults` , `SimplePagedResults`

    Simple Paged Results Control, Object Identifier: 1.2.840.113556.1.4.319

  * `SubEntries`

    Sub-Entries Request Control, Object Identifier: 1.3.6.1.4.1.4203.1.10.1

  * `TxnId` , `TransactionId`

    Transaction ID Control, Object Identifier: 1.3.6.1.4.1.36733.2.1.5.1 This is an internal ForgeRock control.

  * `VirtualAttrsOnly` , `VirtualAttributesOnly`

    Virtual Attributes Only Request Control, Object Identifier: 2.16.840.1.113730.3.4.19

  * `Vlv` , `VirtualListView`

    Virtual List View Request Control, Object Identifier: 2.16.840.1.113730.3.4.9

* `-l | --timeLimit {timeLimit}`

  Maximum length of time in seconds to allow for the search. Default: 0

* `--matchedValuesFilter {filter}`

  Use the LDAP matched values control with the provided filter.

* `-n | --dry-run`

  Show what would be done but do not perform any operation and do not contact the server. Default: false

* `-s | --searchScope {searchScope}`

  Search scope ('base', 'one', 'sub', or 'subordinates'). Note: 'subordinates' is an LDAP extension that might not work with all LDAP servers. Default: sub

* `-S | --sortOrder {sortOrder}`

  Use the server side sort control to have the server sort the results using the provided sort order. You can provide multiple comma separated sort keys. Sort key must respect the following pattern: "\[-] attributeType \[:OrderingRuleNameOrOID]". Minus character represent a descending sort order.

* `--simplePageSize {numEntries}`

  Use the simple paged results control with the given page size. Default: 1000

* `--subEntries`

  Use subentries control to specify that subentries are visible and normal entries are not. Default: false

* `-Y | --proxyAs {authzID}`

  Use the proxied authorization control with the given authorization ID.

* `-z | --sizeLimit {sizeLimit}`

  Maximum number of entries to return from the search. Default: 0

LDAP connection options:

* `--connectTimeout {timeout}`

  Maximum length of time (in milliseconds) that can be taken to establish a connection. Use '0' to specify no time out. Default: 30000

* `-D | --bindDn {bindDN}`

  DN to use to bind to the server. Default:

* `-E | --reportAuthzId`

  Use the authorization identity control. Default: false

* `-h | --hostname {host}`

  Fully-qualified server host name or IP address. Default: localhost.localdomain

* `--keyStorePath {keyStorePath}`

  The keystore containing the certificate which should be used for SSL client authentication.

* `--keyStoreProviderArg {argument}`

  Configuration argument for the key store provider.

* `--keyStoreProviderClass {class}`

  Full class name of the key store provider.

* `--keyStoreProviderName {name}`

  Name of the key store provider.

* `--keyStoreType {keyStoreType}`

  The type of the keystore (e.g. \[JKS|JCEKS|PKCS12|PKCS11|\<other>]).

* `-N | --certNickname {nickname}`

  Nickname of the certificate that should be sent to the server for SSL client authentication.

* `-o | --saslOption {name=value}`

  SASL bind options.

* `-p | --port {port}`

  Directory server port number.

* `-q | --useStartTls`

  Use StartTLS to secure communication with the server. Default: false

* `-T | --trustStorePassword[:env|:file] {trustStorePassword}`

  Truststore password which will be used as the cleartext configuration value.

* `--trustStorePath {trustStorePath}`

  Use this truststore for validating server certificate.

* `--trustStoreProviderArg {argument}`

  Configuration argument for the trust store provider.

* `--trustStoreProviderClass {class}`

  Full class name of the trust store provider.

* `--trustStoreProviderName {name}`

  Name of the trust store provider.

* `--trustStoreType {trustStoreType}`

  The type of the truststore (e.g. \[JKS|JCEKS|JVM|PKCS12|\<other>]).

* `--usePasswordPolicyControl`

  Use the password policy request control. Default: false

* `-w | --bindPassword[:env|:file] {bindPassword}`

  Password to use to bind to the server. Omit this option while providing the bind DN to ensure that the command prompts for the password, rather than entering the password as a command argument.

* `-W | --keyStorePassword[:env|:file] {keyStorePassword}`

  Keystore password which will be used as the cleartext configuration value.

* `-X | --trustAll`

  Trust all server SSL certificates. Default: false

* `-Z | --useSsl`

  Use SSL for secure communication with the server. Default: false

Utility input/output options:

* `--no-prompt`

  Use non-interactive mode. If data in the command is missing, the user is not prompted and the tool will fail. Default: false

* `--noPropertiesFile`

  No properties file will be used to get default command line argument values. Default: false

* `--propertiesFilePath {propertiesFilePath}`

  Path to the file containing default property values used for command line arguments.

* `-t | --wrapColumn {wrapColumn}`

  Maximum length of an output line (0 for no wrapping). Default: 0

* `-v | --verbose`

  Use verbose mode. Default: false

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Filters

The filter argument is a string representation of an LDAP search filter as in `(cn=Babs Jensen)` , `(&(objectClass=Person)(|(sn=Jensen)(cn=Babs J*)))` , or `(cn:caseExactMatch:=Fred Flintstone)` .

## Attributes

The optional attribute list specifies the attributes to return in the entries found by the search. In addition to identifying attributes by name such as `cn sn mail` and so forth, you can use the following notations, too.

* `*`

  Return all user attributes such as `cn` , `sn` , and `mail` .

* `+`

  Return all operational attributes such as `etag` and `pwdPolicySubentry` .

* `@objectclass`

  Return all attributes of the specified object class, where *objectclass* is one of the object classes on the entries returned by the search.

* `1.1`

  Return no attributes, only the DNs of matching entries.

## Exit codes

* 0

  The command completed successfully.

* ldap-error

  An LDAP error occurred while processing the operation. LDAP result codes are described in [RFC 4511](https://www.rfc-editor.org/rfc/rfc4511.html#appendix-A) . Also see the additional information for details.

* 89

  An error occurred while parsing the command-line arguments.

## Files

You can use `~/.opendj/tools.properties` to set the defaults for bind DN, host name, and port number as in the following example:

```
hostname=directory.example.com
port=1389
bindDN=uid=kvaughan,ou=People,dc=example,dc=com

ldapcompare.port=1389
ldapdelete.port=1389
ldapmodify.port=1389
ldappasswordmodify.port=1389
ldapsearch.port=1389
```

---

---
title: ldifdiff
description: ldifdiff — compare small LDIF files
component: pingds
version: 8.1
page_id: pingds:tools-reference:ldifdiff
canonical_url: https://docs.pingidentity.com/pingds/8.1/tools-reference/ldifdiff.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  synopsis: Synopsis
  ldifdiff-description: Description
  ldifdiff-options: Options
  ldifdiff-exit-codes: Exit codes
---

# ldifdiff

`ldifdiff` — compare small LDIF files

## Synopsis

`ldifdiff {options} source target`

## Description

This utility can be used to compare two LDIF files and report the differences in LDIF format.

If standard input is used to specify source or target, end your input with EOF (Ctrl+D on UNIX, Ctrl+Z on Windows).

## Options

The `ldifdiff` command takes the following options:

Command options:

* `-B | --excludeBranch {branchDN}`

  Base DN of a branch to exclude when comparing entries.

* `-e | --excludeAttribute {attribute}`

  Attribute to ignore when comparing entries.

* `-o | --outputLdif {file}`

  Write differences to {file} instead of stdout. Default: stdout

* `-x | --exactMatch`

  Match values byte-for-byte instead of using equality matching rules, which can be useful when comparing schema files. Default: false

Utility input/output options:

* `-t | --wrapColumn {wrapColumn}`

  Maximum length of an output line (0 for no wrapping). Default: 0

General options:

* `-V | --version`

  Display Directory Server version information. Default: false

* `-H | --help`

  Display this usage information. Default: false

## Exit codes

* 0

  No differences were found.

* 1

  Differences were found.

* other

  An error occurred.
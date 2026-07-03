---
title: Log message reference
description: This document covers server messages, such as those in logs/errors.
component: pingds
version: 8.1
page_id: pingds:log-reference:index
canonical_url: https://docs.pingidentity.com/pingds/8.1/log-reference/index.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  ids_1_500: "IDs: 1-500"
  ids_501_1000: "IDs: 501-1000"
  ids_1001_1500: "IDs: 1001-1500"
  ids_1501_2000: "IDs: 1501-2000"
  ids_2001_2500: "IDs: 2001-2500"
  ids_2501_3000: "IDs: 2501-3000"
  ids_3001_3500: "IDs: 3001-3500"
  ids_3501_4000: "IDs: 3501-4000"
---

# Log message reference

This document covers server messages, such as those in logs/errors.

## IDs: 1-500

* []()ID: 1

  Severity: WARNING\
  Message: The provided string "%s" could not be parsed as a valid Access Control Instruction (ACI) because it failed general ACI syntax evaluation.

* []()ID: 2

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) version value "%s" is invalid, only the version 3.0 is supported.

* []()ID: 3

  Severity: WARNING\
  Message: The provided Access Control Instruction access type value "%s" is invalid. A valid access type value is either allow or deny.

* []()ID: 4

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) rights values "%s" are invalid. The rights must be a list of 1 to 6 comma-separated keywords enclosed in parentheses.

* []()ID: 5

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) rights keyword values "%s" are invalid. The valid rights keyword values are one or more of the following: read, write, add, delete, search, compare or the single value all.

* []()ID: 6

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule value "%s" is invalid because it is missing a close parenthesis that corresponded to the initial open parenthesis.

* []()ID: 7

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule value "%s" is invalid. A valid bind rule value must be in the following form: keyword operator "expression".

* []()ID: 8

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule keyword value "%s" is invalid. A valid keyword value is one of the following: userdn, groupdn, roledn, userattr,ip, dns, dayofweek, timeofday or authmethod.

* []()ID: 9

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule operator value "%s" is invalid. A valid bind rule operator value is either '=' or "!=".

* []()ID: 10

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule expression value corresponding to the keyword value "%s" is missing an expression. A valid bind rule value must be in the following form: keyword operator "expression".

* []()ID: 11

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule boolean operator value "%s" is invalid. A valid bind rule boolean operator value is either "OR" or "AND".

* []()ID: 12

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule keyword string "%s" is invalid for the bind rule operator string "%s".

* []()ID: 13

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userdn expression failed to URL decode for the following reason: %s.

* []()ID: 14

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule groupdn expression value "%s" is invalid. A valid groupdn keyword expression value requires one or more LDAP URLs in the following format: ldap\:///groupdn \[|| ldap\:///groupdn] …​ \[|| ldap\:///groupdn].

* []()ID: 15

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule groupdn expression value failed to URL decode for the following reason: %s.

* []()ID: 16

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule ip expression value "%s" is invalid. A valid ip keyword expression requires one or more comma-separated elements of a valid IP address list expression.

* []()ID: 17

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule dns expression value "%s" is invalid. A valid dns keyword expression value requires a valid fully qualified DNS domain name.

* []()ID: 18

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule dns expression value "%s" is invalid, because a wild-card pattern was found in the wrong position. A valid dns keyword wild-card expression value requires the '\*' character only be in the leftmost position of the domain name.

* []()ID: 19

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule dayofweek expression value "%s" is invalid, because of an invalid day of week value. A valid dayofweek value is one of the following English three-letter abbreviations for the days of the week: sun, mon, tue, wed, thu, fri, or sat.

* []()ID: 20

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule timeofday expression value "%s" is invalid. A valid timeofday value is expressed as four digits representing hours and minutes in the 24-hour clock (0 to 2359).

* []()ID: 21

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule timeofday expression value "%s" is not in the valid range. A valid timeofday value is expressed as four digits representing hours and minutes in the 24-hour clock (0 to 2359).

* []()ID: 22

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule authmethod expression value "%s" is invalid. A valid authmethod value is one of the following: none, simple,SSL, or "sasl mechanism", where mechanism is one of the supported SASL mechanisms including CRAM-MD5, DIGEST-MD5, and GSSAPI.

* []()ID: 23

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userattr expression value "%s" is invalid.

* []()ID: 24

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userattr expression inheritance pattern value "%s" is invalid. A valid inheritance pattern value must have the following format: parent\[inheritance\_level].attribute#bindType.

* []()ID: 25

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userattr expression inheritance pattern value "%s" is invalid. The inheritance level value cannot exceed the max level limit of %s.

* []()ID: 26

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userattr expression inheritance pattern value "%s" is invalid because it is non-numeric.

* []()ID: 27

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) target rule value "%s" is invalid. A valid target rule value must be in the following form: keyword operator "expression".

* []()ID: 28

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) target keyword value "%s" is invalid. A valid target keyword value is one of the following: target, targetscope, targetfilter, targetattr or targattrfilters.

* []()ID: 29

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) target operator value "%s" is invalid. The only valid target operator value for the "%s" keyword is '='.

* []()ID: 30

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) target keyword value "%s" was seen multiple times in the ACI "%s".

* []()ID: 31

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) target keyword operator value "%s" is invalid. A valid target keyword operator value is either '=' or "!=".

* []()ID: 32

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targetscope expression operator value "%s" is invalid. A valid targetscope expression value is one of the following: one, onelevel, subtree or subordinate.

* []()ID: 33

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) target expression value "%s" is invalid. A valid target keyword expression value requires a LDAP URL in the following format: ldap\:///distinguished\_name\_pattern.

* []()ID: 34

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) target expression DN value "%s" is invalid. The target expression DN value must be a descendant of the ACI entry DN "%s", if no wild-card is specified in the target expression DN.

* []()ID: 35

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targetattr expression value "%s" is invalid. A valid targetattr keyword expression value requires one or more valid attribute type names in the following format: attribute1 \[|| attribute2] …​ \[|| attributeN]. Attribute options are not supported.

* []()ID: 36

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targetfilter expression value "%s" is invalid because it is not a valid LDAP filter.

* []()ID: 37

  Severity: INFO\
  Message: An attempt to add the entry "%s" containing an aci attribute type failed, because the authorization DN "%s" lacked modify-acl privileges.

* []()ID: 38

  Severity: INFO\
  Message: An attempt to modify an aci attribute type in the entry "%s" failed, because the authorization DN "%s" lacked modify-acl privileges.

* []()ID: 39

  Severity: WARNING\
  Message: An attempt to add the entry "%s" containing an aci attribute type failed because of the following reason: %s.

* []()ID: 40

  Severity: WARNING\
  Message: An attempt to modify an aci attribute type in the entry "%s" failed because of the following reason: %s.

* []()ID: 41

  Severity: WARNING\
  Message: "%s", located in the entry "%s", because of the following reason: %s.

* []()ID: 42

  Severity: INFO\
  Message: Added %s Access Control Instruction (ACI) attribute types found in context "%s" to the access control evaluation engine.

* []()ID: 43

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targattrfilter expression value %s is invalid because it is not in the correct format. A valid targattrsfilters expression value must be in the following format: "add=attr1: F1 && attr2: F2 …​ && attrN: FN,del= attr1: F1 && attr2: F2 …​ && attrN: FN".

* []()ID: 44

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targattrfilter expression value %s is invalid because the both operation tokens match in the two filter lists.

* []()ID: 45

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targattrfilters expression value %s is invalid because there are more than two filter list statements.

* []()ID: 46

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targattrfilters expression value %s is invalid because the provided filter list string is in the wrong format. A valid targattrfilters filter list must be in the following format: add=attr1: F1 && attr2: F2 …​ && attrN: FN.

* []()ID: 47

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targattrfilters expression value %s is invalid because one or more of the specified filters are invalid for the following reason: %s.

* []()ID: 48

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targattrfilters expression value %s is invalid because one or more of the specified filters are invalid because of non-matching attribute type names in the filter.

* []()ID: 49

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) attribute name value %s is invalid. A valid attribute type name must begin with an ASCII letter and must contain only ASCII letters,digits or the "-" character.

* []()ID: 50

  Severity: NOTICE\
  Message: The SASL mechanism "%s" provided in the Access Control Instruction (ACI) bind rule authmethod expression is not one of the currently registered mechanisms in the server.

* []()ID: 51

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule dns expression value "%s" references hostname %s, but the canonical representation for that hostname is configured to be %s. The server will attempt to automatically interpret the correct localhost value.

* []()ID: 52

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule dns expression value "%s" references hostname %s, which resolves to IP address %s, but the canonical hostname for that IP address is %s. This likely means that the provided hostname will never match any clients.

* []()ID: 53

  Severity: WARNING\
  Message: An error occurred while attempting to determine whether hostname %s referenced in dns expression bind rule "%s" used the correct canonical representation: %s. This likely means that the provided hostname will never match any clients.

* []()ID: 54

  Severity: INFO\
  Message: Added %s Global Access Control Instruction (ACI) attribute types to the access control evaluation engine.

* []()ID: 55

  Severity: INFO\
  Message: An unexpected error occurred while processing the ds-cfg-global-aci attribute in configuration entry %s: %s.

* []()ID: 56

  Severity: INFO\
  Message: An unexpected error occurred while processing the aci attributes in the configuration system: %s.

* []()ID: 57

  Severity: WARNING\
  Message: The pattern DN %s is not valid because it contains two consecutive wildcards in an attribute value.

* []()ID: 58

  Severity: WARNING\
  Message: The pattern DN %s is not valid because it uses wildcards for substring matching on an attribute type. A single wildcard is allowed in place of an attribute type.

* []()ID: 59

  Severity: WARNING\
  Message: The pattern DN %s is not valid because it contains a wildcard in an attribute type in a multi-valued RDN.

* []()ID: 60

  Severity: WARNING\
  Message: Selfwrite check skipped because an attribute "%s" with a distinguished name syntax was not a valid DN.

* []()ID: 61

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targetattr expression value "%s" is invalid because the expression contains invalid or duplicate tokens.

* []()ID: 62

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) expression value "%s" is invalid because it contains the roledn keyword, which is not supported, replace it with the groupdn keyword.

* []()ID: 63

  Severity: WARNING\
  Message: Failed to decode the Access Control Instruction (ACI)%s.

* []()ID: 64

  Severity: WARNING\
  Message: The server is being put into lockdown mode because invalid ACIs rules were detected either when the server was started or during a backend initialization.

* []()ID: 65

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userattr expression value failed to URL decode for the following reason: %s.

* []()ID: 66

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userattr expression value failed to parse because the ldap URL "%s" contains an empty base DN.

* []()ID: 67

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule userattr expression value failed to parse because the attribute field of the ldap URL "%s" either contains more than one description or the field is empty.

* []()ID: 68

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the prefix part of the expression "%s" has an invalid format.

* []()ID: 69

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the prefix value of the expression "%s" was an invalid value. All values must greater than or equal to 0 and either less than or equal 32 for IPV4 addresses or less than or equal to 128 for IPV6 addresses.

* []()ID: 70

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the prefix part of the expression "%s" has an non-numeric value.

* []()ID: 71

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the IPv4 address expression "%s" format was invalid.

* []()ID: 72

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the IPv4 address expression "%s" contains an invalid value. All values of the address must be between 0 and 255.

* []()ID: 73

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the IPv4 address expression "%s" contains a non-numeric value.

* []()ID: 74

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the IPv6 address expression "%s" contains an illegal wildcard character. Wildcards are not supported when using IPv6 addresses in a IP bind rule expression.

* []()ID: 75

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression "%s" failed to parse for the following reason: "%s".

* []()ID: 76

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the netmask part of the expression "%s" has an invalid format.

* []()ID: 77

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule IP address expression failed to parse because the netmask part of the expression "%s" has an invalid value.

* []()ID: 78

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targetcontrol expression value "%s" is invalid. A valid targetcontrol keyword expression value requires one or more valid control OID strings in the following format: oid \[|| oid1] …​ \[|| oidN].

* []()ID: 79

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targetcontrol OID value "%s" could not be parsed because the value contained an illegal character %c at position %d.

* []()ID: 80

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) targetcontrol OID value "%s" could not be parsed because the numeric OID contained two consecutive periods at position %d.

* []()ID: 81

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) extop expression value "%s" is invalid. A valid extop keyword expression value requires one or more valid extended operation request OID strings in the following format: oid \[|| oid1] …​ \[|| oidN].

* []()ID: 82

  Severity: WARNING\
  Message: Backend %s does not have a presence index defined for attribute type %s. Access control initialization may take a very long time to complete in this backend.

* []()ID: 83

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule SSF expression "%s" failed to parse for the following reason: "%s".

* []()ID: 84

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule ssf expression value "%s" is not in the valid range. A valid ssf value is in the range of 1 to 1024.

* []()ID: 85

  Severity: WARNING\
  Message: The provided Access Control Instruction (ACI) bind rule timeofday expression "%s" failed to parse for the following reason: "%s".

* []()ID: 86

  Severity: NOTICE\
  Message: The global access control policy '%s' has been added.

* []()ID: 87

  Severity: NOTICE\
  Message: The global access control policy '%s' has been removed.

* []()ID: 88

  Severity: NOTICE\
  Message: The global access control policy '%s' has been modified.

* []()ID: 89

  Severity: NOTICE\
  Message: The global access control engine has been initialized with %d policies.

* []()ID: 90

  Severity: ERROR\
  Message: The global access control policy defined in "%s" could not be parsed because it contains an invalid target DN pattern "%s".

* []()ID: 91

  Severity: ERROR\
  Message: The global access control policy defined in "%s" could not be parsed because it contains an invalid user DN pattern "%s".

* []()ID: 92

  Severity: ERROR\
  Message: The global access control policy defined in "%s" could not be parsed because it contains an unrecognized control alias "%s".

* []()ID: 93

  Severity: ERROR\
  Message: The global access control policy defined in "%s" could not be parsed because it contains an unrecognized extended operation alias "%s".

* []()ID: 94

  Severity: INFO\
  Message: This utility can be used to display basic server information.

* []()ID: 95

  Severity: INFO\
  Message: Adds the local server (with version 7.0 or more) to a topology with older server versions (prior to 7.0).

* []()ID: 96

  Severity: INFO\
  Message: Establishing connections.

* []()ID: 97

  Severity: INFO\
  Message: Checking registration information.

* []()ID: 98

  Severity: INFO\
  Message: %s entries processed (%s %% complete).

* []()ID: 99

  Severity: INFO\
  Message: %s entries processed.

* []()ID: 100

  Severity: INFO\
  Message: %s remaining to be processed.

* []()ID: 101

  Severity: ERROR\
  Message: A target server must be specified either by using LDAP connection options or the --%s option.

* []()ID: 102

  Severity: ERROR\
  Message: An error occurred while reading the server configuration: %s.

* []()ID: 103

  Severity: ERROR\
  Message: An error occurred while printing server status script friendly output: %s.

* []()ID: 104

  Severity: INFO\
  Message: Run status.

* []()ID: 105

  Severity: INFO\
  Message: Started.

* []()ID: 106

  Severity: INFO\
  Message: Stopped.

* []()ID: 107

  Severity: INFO\
  Message: Open connections.

* []()ID: 108

  Severity: INFO\
  Message: General details.

* []()ID: 109

  Severity: INFO\
  Message: Host name.

* []()ID: 110

  Severity: INFO\
  Message: Server ID.

* []()ID: 111

  Severity: INFO\
  Message: Administration port (LDAPS).

* []()ID: 112

  Severity: INFO\
  Message: Version.

* []()ID: 113

  Severity: INFO\
  Message: Installation path.

* []()ID: 114

  Severity: INFO\
  Message: Instance path.

* []()ID: 115

  Severity: INFO\
  Message: Installation and instance path.

* []()ID: 116

  Severity: INFO\
  Message: Running server Java details.

* []()ID: 117

  Severity: INFO\
  Message: Java version.

* []()ID: 118

  Severity: INFO\
  Message: Java vendor.

* []()ID: 119

  Severity: INFO\
  Message: JVM available CPUs.

* []()ID: 120

  Severity: INFO\
  Message: JVM max heap size.

* []()ID: 121

  Severity: INFO\
  Message: Connection handlers.

* []()ID: 122

  Severity: INFO\
  Message: Name.

* []()ID: 123

  Severity: INFO\
  Message: Port.

* []()ID: 124

  Severity: INFO\
  Message: Protocol.

* []()ID: 125

  Severity: INFO\
  Message: Load m1 rate.

* []()ID: 126

  Severity: INFO\
  Message: Load m5 rate.

* []()ID: 127

  Severity: INFO\
  Message: Local backends.

* []()ID: 128

  Severity: INFO\
  Message: Proxy backends.

* []()ID: 129

  Severity: INFO\
  Message: Backend.

* []()ID: 130

  Severity: INFO\
  Message: Type.

* []()ID: 131

  Severity: INFO\
  Message: Active cache.

* []()ID: 132

  Severity: INFO\
  Message: Base DN.

* []()ID: 133

  Severity: INFO\
  Message: Entries.

* []()ID: 134

  Severity: INFO\
  Message: Replication.

* []()ID: 135

  Severity: INFO\
  Message: Receive delay.

* []()ID: 136

  Severity: INFO\
  Message: Replay delay.

* []()ID: 137

  Severity: INFO\
  Message: Disk space.

* []()ID: 138

  Severity: INFO\
  Message: State.

* []()ID: 139

  Severity: INFO\
  Message: Free space.

* []()ID: 140

  Severity: INFO\
  Message: There are no connection handlers setup in the server.

* []()ID: 141

  Severity: INFO\
  Message: There are no local backends setup in the server.

* []()ID: 142

  Severity: INFO\
  Message: There are no proxy backends setup in the server.

* []()ID: 143

  Severity: INFO\
  Message: No disks are monitored by the server.

* []()ID: 144

  Severity: INFO\
  Message: Connect to the server to obtain JVM information.

* []()ID: 145

  Severity: INFO\
  Message: Connect to the server to obtain disk space information.

* []()ID: 146

  Severity: ERROR\
  Message: Unable to perform the search on the monitor backend. To display information, the status tool requires the remote server monitor backend to be enabled.

* []()ID: 147

  Severity: INFO\
  Message: The folder into which the files will be placed into.

* []()ID: 148

  Severity: INFO\
  Message: {directory}.

* []()ID: 149

  Severity: INFO\
  Message: The instance is running.

* []()ID: 150

  Severity: INFO\
  Message: The instance is not running.

* []()ID: 151

  Severity: INFO\
  Message: Password to use to bind to the server.

* []()ID: 152

  Severity: INFO\
  Message: {password}.

* []()ID: 153

  Severity: INFO\
  Message: Path to the JDK utility binaries directory such as jstack.

* []()ID: 154

  Severity: INFO\
  Message: {directory}.

* []()ID: 155

  Severity: INFO\
  Message: Specifies whether audit files are excluded.

* []()ID: 156

  Severity: INFO\
  Message: Specifies whether keystore files are excluded.

* []()ID: 157

  Severity: INFO\
  Message: Specifies that the tool should not interact with the server, that is no LDAP operation, and no jstack sampling.

* []()ID: 158

  Severity: INFO\
  Message: Specifies whether a Java Heap Dump (using jmap) should be produced. The binary file is generated at the same location as the ZIP archive before being added to it; please make sure that the target directory's volume has sufficient capacity.

* []()ID: 159

  Severity: INFO\
  Message: Maximum number of log files to collect. Ignored if --logsAfterDate is provided.

* []()ID: 160

  Severity: INFO\
  Message: {number}.

* []()ID: 161

  Severity: INFO\
  Message: Collect log files after this date. Format "YYYYMMDDhhmmss" like "20161123143612" = 23 November 2016, 14:36 12s. Overrides --maxLogFiles.

* []()ID: 162

  Severity: INFO\
  Message: {date}.

* []()ID: 163

  Severity: INFO\
  Message: When the server is embedded in OpenAM, there is no PID file. Therefore this option indicates the server PID of the OpenAM application server.

* []()ID: 164

  Severity: INFO\
  Message: {pid}.

* []()ID: 165

  Severity: INFO\
  Message: This tool collects support data from the PingDS instance it is bound to.

* []()ID: 166

  Severity: NOTICE\
  Message: \<xinclude:include href="description-supportextract.xml" />.

* []()ID: 167

  Severity: NOTICE\
  Message: extract support data.

* []()ID: 168

  Severity: ERROR\
  Message: Error: %s.

* []()ID: 169

  Severity: ERROR\
  Message: The output directory "%s" could not be found.

* []()ID: 170

  Severity: ERROR\
  Message: The number argument for "maxLogFiles" is invalid.

* []()ID: 171

  Severity: ERROR\
  Message: The date argument for "logsAfterDate" is invalid.

* []()ID: 172

  Severity: ERROR\
  Message: The serverPID argument is not a valid number.

* []()ID: 173

  Severity: ERROR\
  Message: The --bindDN and/or --bindPassword arguments are missing.

* []()ID: 174

  Severity: ERROR\
  Message: Could not collect monitoring data from the directory server: %s.

* []()ID: 175

  Severity: ERROR\
  Message: Could not collect all the files.

* []()ID: 176

  Severity: ERROR\
  Message: An error occurred while parsing the command-line arguments: The argument --outputDirectory is required to have a value but none was provided in the argument list and no default value is available.

* []()ID: 177

  Severity: INFO\
  Message: Continuing data gathering though there was an error: %s.

* []()ID: 178

  Severity: INFO\
  Message: The following archive has been created : %s.

* []()ID: 179

  Severity: NOTICE\
  Message: Could not find "java.properties".

* []()ID: 180

  Severity: NOTICE\
  Message: Error while loading "java.properties": %s.

* []()ID: 181

  Severity: INFO\
  Message: No monitoring data can be collected when the server is not running or no server interaction is allowed.

* []()ID: 182

  Severity: INFO\
  Message: No JVM stack dump can be produced when the server is not running or no server interaction is allowed.

* []()ID: 183

  Severity: ERROR\
  Message: Could not find the "%s" command in "%s".

* []()ID: 184

  Severity: ERROR\
  Message: Skipping log "%s" (unsupported config).

* []()ID: 185

  Severity: INFO\
  Message: Collecting the configuration files.

* []()ID: 186

  Severity: INFO\
  Message: Collecting process statistics.

* []()ID: 187

  Severity: INFO\
  Message: Making copy of the %s file before collecting process statistics.

* []()ID: 188

  Severity: INFO\
  Message: Removing file copy %s.

* []()ID: 189

  Severity: INFO\
  Message: Skipping backup of %s log (file not found).

* []()ID: 190

  Severity: INFO\
  Message: Collecting JVM heap dump : using %s.

* []()ID: 191

  Severity: INFO\
  Message: Collecting the log files.

* []()ID: 192

  Severity: INFO\
  Message: Collecting backend statistics.

* []()ID: 193

  Severity: INFO\
  Message: Collecting the GC log files.

* []()ID: 194

  Severity: INFO\
  Message: Skipping GC logs collection because GC logging is not enabled.

* []()ID: 195

  Severity: INFO\
  Message: Collecting ChangelogDb information.

* []()ID: 196

  Severity: INFO\
  Message: No changelogDb data found (is a DS or is not replicated).

* []()ID: 197

  Severity: INFO\
  Message: Collecting the monitoring info from cn=monitor.

* []()ID: 198

  Severity: INFO\
  Message: Collecting process thread information, sample number : %d.

* []()ID: 199

  Severity: INFO\
  Message: Generating stack dump, sample number : %d using %s for pid %d.

* []()ID: 200

  Severity: INFO\
  Message: Processor information.

* []()ID: 201

  Severity: INFO\
  Message: OS information.

* []()ID: 202

  Severity: INFO\
  Message: Extract environment variables.

* []()ID: 203

  Severity: INFO\
  Message: DS /proc files.

* []()ID: 204

  Severity: INFO\
  Message: VM environment information.

* []()ID: 205

  Severity: INFO\
  Message: Disk information.

* []()ID: 206

  Severity: INFO\
  Message: Network information.

* []()ID: 207

  Severity: INFO\
  Message: Linux release.

* []()ID: 208

  Severity: INFO\
  Message: Linux /proc info files.

* []()ID: 209

  Severity: INFO\
  Message: Collecting system node information.

* []()ID: 210

  Severity: INFO\
  Message: Listing the security stores.

* []()ID: 211

  Severity: INFO\
  Message: Adding %s.

* []()ID: 212

  Severity: INFO\
  Message: Skipping %s.

* []()ID: 213

  Severity: INFO\
  Message: Skipping java security stores.

* []()ID: 214

  Severity: INFO\
  Message: Skipping audit files.

* []()ID: 215

  Severity: ERROR\
  Message: There was at least one error during the tasks execution: %s.

* []()ID: 216

  Severity: INFO\
  Message: No value was provided for %s, JDK tool directory is set to %s.

* []()ID: 217

  Severity: INFO\
  Message: Cannot extract process statistics (by running "top" command) on OS '%s'. Only %s dump samples will be collected.

* []()ID: 218

  Severity: INFO\
  Message: This tool manages data synchronization between servers. For replication to work you must initialize the contents of one of the servers with the contents of the others using the '%s' subcommand.

* []()ID: 219

  Severity: NOTICE\
  Message: Manages data synchronization between servers.

* []()ID: 220

  Severity: ERROR\
  Message: An unexpected error has been raised during execution of the tool: '%s'.

* []()ID: 221

  Severity: INFO\
  Message: Initialize replication data for the server.

* []()ID: 222

  Severity: INFO\
  Message: Starting initialization from '%s' to '%s' for base DNs: %s.

* []()ID: 223

  Severity: INFO\
  Message: Starting initialization from '%s' to all replicas for base DNs: %s.

* []()ID: 224

  Severity: INFO\
  Message: Starting initialization for base DN: '%s'.

* []()ID: 225

  Severity: NOTICE\
  Message: An error occurred when launching initialization: %s.

* []()ID: 226

  Severity: INFO\
  Message: Base DN(s) to use. Multiple base DNs can be provided by using this option multiple times.

* []()ID: 227

  Severity: INFO\
  Message: Server ID of the server containing the source data.

* []()ID: 228

  Severity: INFO\
  Message: {serverSource}.

* []()ID: 229

  Severity: INFO\
  Message: Server ID of the server to be initialized.

* []()ID: 230

  Severity: INFO\
  Message: {serverToInitialize}.

* []()ID: 231

  Severity: INFO\
  Message: Initialize all the other servers in the topology.

* []()ID: 232

  Severity: NOTICE\
  Message: A mandatory argument is missing. Choose one and only one argument from '--toServer', '--fromServer' and '--toAllServers'.

* []()ID: 233

  Severity: NOTICE\
  Message: Invalid combination of arguments. Choose one and only one argument from '--toServer', '--fromServer' and '--toAllServers'.

* []()ID: 234

  Severity: NOTICE\
  Message: An error occurred during initialization. Last log details: %s. Task state: %s.

* []()ID: 235

  Severity: NOTICE\
  Message: An error occurred during initialization. Task state: %s.

* []()ID: 236

  Severity: NOTICE\
  Message: Error during the processing of the reset generationID task. Last log details: %s. Task state: %s.

* []()ID: 237

  Severity: NOTICE\
  Message: Error during the processing of the reset generationID task. Task state: %s.

* []()ID: 238

  Severity: INFO\
  Message: Cannot extract the master key pair certificate with alias '%s' because the crypto-manager's key manager provider of the local server does not contain such key or does not support extracting certificates.

* []()ID: 239

  Severity: INFO\
  Message: Cannot find a CA certificate in the replication trust managers of the local server. Please verify the %s trust-manager-provider configuration value.

* []()ID: 240

  Severity: INFO\
  Message: Base DN(s) to replicate.

* []()ID: 241

  Severity: ERROR\
  Message: Inappropriate server ID '%s' for the local server: it does not represent a numeric value as required to communicate with pre 7.0 servers. Use an integer server ID without leading zeros.

* []()ID: 242

  Severity: ERROR\
  Message: Inappropriate group ID '%s' for the local server: it cannot be converted to an integer, but this is required to communicate with pre 7.0 servers. Use a group ID that can be converted into an integer, or use 'default' if you do not want to set a group ID.

* []()ID: 243

  Severity: ERROR\
  Message: Cannot use server ID '%s' for the local server because it is already used by server '%s' (configuration object %s).

* []()ID: 244

  Severity: ERROR\
  Message: Cannot read the configuration of the local server. The error was: %s.

* []()ID: 245

  Severity: ERROR\
  Message: Cannot read 'cn=admin data' in server '%s'. The error was: %s.

* []()ID: 246

  Severity: ERROR\
  Message: Error when reading the server IDs from all the servers in the old topology. The error was: %s.

* []()ID: 247

  Severity: ERROR\
  Message: Cannot discover the configuration of the local server. The error was: %s.

* []()ID: 248

  Severity: ERROR\
  Message: Cannot add an entry describing the new server to 'cn=admin data' in the remote server '%s' in the existing topology. The error was: %s.

* []()ID: 249

  Severity: ERROR\
  Message: Cannot add '%s' to the bootstrap replication server list on server '%s'. The error was: %s.

* []()ID: 250

  Severity: ERROR\
  Message: Cannot add '%s' to the configuration of replication server on server '%s'. The error was: %s.

* []()ID: 251

  Severity: ERROR\
  Message: Cannot add '%s' to the configuration of replication domain '%s' on server '%s'. The error was: %s.

* []()ID: 252

  Severity: ERROR\
  Message: Cannot retrieve the replication port from server '%s'. The error was: %s.

* []()ID: 253

  Severity: ERROR\
  Message: Cannot configure the local server so it can replicate with the servers in the existing topology. The error was: %s.

* []()ID: 254

  Severity: ERROR\
  Message: Cannot read server ID from server '%s' on DNs '%s' and '%s'. The errors were: %s.

* []()ID: 255

  Severity: ERROR\
  Message: Cannot determine server ID for server '%s' on DNs '%s' and '%s'.

* []()ID: 256

  Severity: ERROR\
  Message: Cannot obtain a connection to server '%s' from the existing topology. The error was: %s.

* []()ID: 257

  Severity: ERROR\
  Message: Cannot obtain a connection for one of the servers in the existing topology. The error was: %s.

* []()ID: 258

  Severity: ERROR\
  Message: Cannot configure all the servers in the existing topology to replicate with the new server. The error was: %s.

* []()ID: 259

  Severity: ERROR\
  Message: An error occurred opening (or closing) a connection to change the configuration of the local server. The error was: %s.

* []()ID: 260

  Severity: ERROR\
  Message: An error occurred opening connections to the server in the existing topology or the new server. The error was: %s.

* []()ID: 261

  Severity: ERROR\
  Message: Once done, restart the server for the changes to take effect.

* []()ID: 262

  Severity: ERROR\
  Message: Cannot read the server ID or the group ID for the local server. The error(s) are: %s.

* []()ID: 263

  Severity: ERROR\
  Message: Cannot add the entry '%s' to the server '%s'. The error was: %s.

* []()ID: 264

  Severity: ERROR\
  Message: Cannot read the entry '%s' on server '%s'. The error was: %s.

* []()ID: 265

  Severity: ERROR\
  Message: Cannot modify the entry '%s' on server '%s' to reconcile it with what is expected by the tool. The error was: %s.

* []()ID: 266

  Severity: INFO\
  Message: Adding server instances keys from the existing topology into 'cn=admin data' in the new server.

* []()ID: 267

  Severity: ERROR\
  Message: Cannot add server instance keys to the new server. The error was: %s.

* []()ID: 268

  Severity: INFO\
  Message: Enabling 'cn=admin data' backend.

* []()ID: 269

  Severity: INFO\
  Message: Creating the trust manager '%s' to be used by replication connections in the local server.

* []()ID: 270

  Severity: INFO\
  Message: Updating replication configuration on local server.

* []()ID: 271

  Severity: INFO\
  Message: Updating replication configuration for baseDN '%s' on local server.

* []()ID: 272

  Severity: INFO\
  Message: Configuring the servers in the topology to talk to the local server.

* []()ID: 273

  Severity: INFO\
  Message: Replication has been successfully configured on the local server. Note that for replication to work you must initialize the contents of the base DNs that are being replicated. Run the following command(s) to do so:.

* []()ID: 276

  Severity: NOTICE\
  Message: An error occurred while attempting to monitor the task progress. The error was: %s.

* []()ID: 289

  Severity: INFO\
  Message: Check the server error logs for additional details.

* []()ID: 290

  Severity: INFO\
  Message: Purges old replication meta-data from application data.

* []()ID: 291

  Severity: INFO\
  Message: Maximum duration of the command in seconds.

* []()ID: 292

  Severity: INFO\
  Message: {maximum duration in seconds}.

* []()ID: 293

  Severity: INFO\
  Message: Purging old replication meta-data for server '%s' for base DNs: %s.

* []()ID: 294

  Severity: NOTICE\
  Message: An error occurred while purging old replication meta-data: %s.

* []()ID: 295

  Severity: NOTICE\
  Message: An error occurred while purging old replication meta-data. Last log details: %s. Task state: %s.

* []()ID: 296

  Severity: NOTICE\
  Message: An error occurred while purging old replication meta-data. Task state: %s.

* []()ID: 316

  Severity: INFO\
  Message: Displays the status of the replication service and various diagnostics about it. The information is derived from reading cn=monitor on all the servers in the replication topology. The status of a server is one of the following.

  * BAD - DATA MISMATCH: either the fractional replication configuration does not match the backend data, or the initial state of the replicated data does not match other servers and this server must be re-initialized;

  * BAD - TOO LATE: the server has fallen further behind than the replication purge delay and must be re-initialized;

  * GOOD: normal operation, nothing to do;

  * SLOW: the server's replay delay is greater than five seconds;

  * UNHEALTHY: read the server health errors in the server monitoring data for details.

* []()ID: 317

  Severity: INFO\
  Message: Base DN.

* []()ID: 318

  Severity: INFO\
  Message: Base DN / DS.

* []()ID: 319

  Severity: INFO\
  Message: Base DN / RS.

* []()ID: 320

  Severity: INFO\
  Message: Base DN / RS / DS.

* []()ID: 321

  Severity: INFO\
  Message: Status.

* []()ID: 322

  Severity: INFO\
  Message: Group.

* []()ID: 323

  Severity: INFO\
  Message: Receive delay (ms).

* []()ID: 324

  Severity: INFO\
  Message: Replay delay (ms).

* []()ID: 325

  Severity: INFO\
  Message: Entry count.

* []()ID: 326

  Severity: INFO\
  Message: Server / host port.

* []()ID: 327

  Severity: INFO\
  Message: Error or diagnostic.

* []()ID: 328

  Severity: INFO\
  Message: Displays individual replicas in the output.

* []()ID: 329

  Severity: INFO\
  Message: Displays individual changelog servers in the output.

* []()ID: 330

  Severity: INFO\
  Message: Display replication group information in the output.

* []()ID: 331

  Severity: ERROR\
  Message: An error occurred while reading cn=monitor on server %s: %s.

* []()ID: 332

  Severity: ERROR\
  Message: Error while reading cn=monitor: %s.

* []()ID: 333

  Severity: ERROR\
  Message: Cannot contact server: no admin port could be discovered in its entry %s.

* []()ID: 334

  Severity: ERROR\
  Message: Server is not healthy: %s.

* []()ID: 335

  Severity: ERROR\
  Message: General error: %s.

* []()ID: 336

  Severity: INFO\
  Message: Base DN(s) to display. Multiple base DNs can be provided by using this option multiple times. If no base DNs are provided, then all the base DNs will be displayed.

* []()ID: 337

  Severity: INFO\
  Message: Clears all replication server changelog data for the offline local server; the other replication servers in the topology will transfer any needed data when the server restarts.

* []()ID: 338

  Severity: ERROR\
  Message: A problem occurred while clearing the changelog data: %s.

* []()ID: 339

  Severity: INFO\
  Message: Clearing all replication server changelog data for the local server.

* []()ID: 340

  Severity: INFO\
  Message: Nothing to do: this server does not keep any replication server changelog data.

* []()ID: 341

  Severity: ERROR\
  Message: Cannot obtain a connection for one of the servers in the topology. The error was: %s.

* []()ID: 342

  Severity: ERROR\
  Message: Cannot obtain a connection to server '%s' from the topology. The error was: %s.

* []()ID: 343

  Severity: ERROR\
  Message: An error occurred opening (or closing) a connection to read or change the configuration of the local server. The error was: %s.

* []()ID: 344

  Severity: INFO\
  Message: This server has already been cleaned, there is nothing left to do.

* []()ID: 345

  Severity: INFO\
  Message: The remaining cleanup on this server cannot be performed because the administrator user '%s' in the admin backend was used to bind to the server. You should run again this command using a bind DN, such as "uid=admin", which lies outside the "cn=admin data" backend to be able to complete the cleanup on this server.

* []()ID: 346

  Severity: ERROR\
  Message: Cannot disable admin backend on the local server. The error was: %s.

* []()ID: 347

  Severity: ERROR\
  Message: Cannot update configuration for server '%s'. The error was: %s.

* []()ID: 348

  Severity: ERROR\
  Message: Cannot read monitor entries under '%s' on the local server. The error was: %s.

* []()ID: 349

  Severity: ERROR\
  Message: Cannot delete entries under '%s' in admin backend. The error was: %s.

* []()ID: 350

  Severity: INFO\
  Message: All servers have been cleaned.

* []()ID: 351

  Severity: INFO\
  Message: All servers have been cleaned. The admin backend will remain enabled because it contains secret keys that may be used by reversible password storage schemes.

* []()ID: 352

  Severity: INFO\
  Message: The server %s has now been cleaned.

* []()ID: 353

  Severity: INFO\
  Message: Servers have been cleaned, however the administrator user '%s' in the admin backend was not removed because it was used to bind to the server. To remove it, you should run the following commands on all servers using a bind DN, such as "uid=admin", which lies outside the "cn=admin data" backend:.

* []()ID: 354

  Severity: INFO\
  Message: Removing servers from admin backend.

* []()ID: 355

  Severity: INFO\
  Message: Removing instance keys from admin backend.

* []()ID: 356

  Severity: INFO\
  Message: Removing administrators from admin backend.

* []()ID: 357

  Severity: INFO\
  Message: Cleaning and updating configuration of server %s.

* []()ID: 358

  Severity: INFO\
  Message: Set bootstrap servers configuration for server %s.

* []()ID: 359

  Severity: INFO\
  Message: Disable admin backend for server %s.

* []()ID: 360

  Severity: WARNING\
  Message: Some reversible password storage schemes are enabled in the configuration, note that it won't be possible to use them in password policies since the admin data backend has been disabled.

* []()ID: 361

  Severity: INFO\
  Message: Clean all the servers (with version 7.0 or more) that have been migrated from a topology of older servers (version prior to 7.0).

* []()ID: 362

  Severity: ERROR\
  Message: An attempt was made to configure the root DSE backend without providing a configuration entry. This is not allowed.

* []()ID: 363

  Severity: WARNING\
  Message: Base DN "%s" is configured as one of the subordinate base DNs to use for searches below the root DSE. However, this base DN is not handled by any suffix registered with the Directory Server and will therefore not be used.

* []()ID: 364

  Severity: ERROR\
  Message: Unwilling to update entry "%s" because modify operations are not supported in the root DSE backend. If you wish to alter the contents of the root DSE itself, then it may be possible to do so by modifying the "%s" entry in the configuration.

* []()ID: 365

  Severity: ERROR\
  Message: Unwilling to perform a search (connection ID %d, operation ID %d) with a base DN of "%s" in the root DSE backend. The base DN for searches in this backend must be the DN of the root DSE itself.

* []()ID: 366

  Severity: ERROR\
  Message: Unable to process the search with connection ID %d and operation ID %d because it had an invalid scope of %s.

* []()ID: 367

  Severity: ERROR\
  Message: An unexpected error occurred while trying to open the LDIF writer for the root DSE backend: %s.

* []()ID: 368

  Severity: ERROR\
  Message: An unexpected error occurred while trying to export the root DSE entry to the specified LDIF target: %s.

* []()ID: 369

  Severity: INFO\
  Message: The root DSE configuration has been updated so that it will now use a new set of user-defined attributes.

* []()ID: 370

  Severity: ERROR\
  Message: An attempt was made to configure the monitor backend without providing a configuration entry. This is not allowed, and no monitor information will be available over protocol.

* []()ID: 371

  Severity: ERROR\
  Message: Unwilling to add entry "%s" because add operations are not supported in the "%s" backend.

* []()ID: 372

  Severity: ERROR\
  Message: Unwilling to remove entry "%s" because delete operations are not supported in the "%s" backend.

* []()ID: 373

  Severity: ERROR\
  Message: Unwilling to update entry "%s" because modify operations are not supported in the monitor backend. If you wish to alter the contents of the base monitor entry itself, then it may be possible to do so by modifying the "%s" entry in the configuration.

* []()ID: 374

  Severity: ERROR\
  Message: Unwilling to rename entry "%s" because modify DN operations are not supported in the "%s" backend.

* []()ID: 375

  Severity: ERROR\
  Message: An error occurred while attempting to export the base monitor entry: %s.

* []()ID: 376

  Severity: ERROR\
  Message: An error occurred while attempting to export the monitor entry for monitor provider %s: %s.

* []()ID: 377

  Severity: ERROR\
  Message: The "%s" backend does not support LDIF import operations.

* []()ID: 378

  Severity: INFO\
  Message: The monitor configuration has been updated so that it will now use a new set of user-defined attributes.

* []()ID: 380

  Severity: ERROR\
  Message: Unable to retrieve the requested entry %s from the monitor backend because the DN is not below the monitor base of %s.

* []()ID: 381

  Severity: ERROR\
  Message: An attempt was made to configure the schema backend without providing a configuration entry. This is not allowed, and no schema information will be available over protocol.

* []()ID: 382

  Severity: ERROR\
  Message: An error occurred while attempting to export the base schema entry: %s.

* []()ID: 383

  Severity: ERROR\
  Message: Unable to retrieve the requested entry %s from the schema backend because the DN is equal to one of the schema entry DNs.

* []()ID: 384

  Severity: ERROR\
  Message: An unexpected error occurred while trying to open the LDIF writer for the schema backend: %s.

* []()ID: 386

  Severity: ERROR\
  Message: The Directory Server was unable to obtain a lock on entry %s after multiple attempts. This could mean that the entry is already locked by a long-running operation or that the entry has previously been locked but was not properly unlocked.

* []()ID: 387

  Severity: ERROR\
  Message: The task defined in entry %s is invalid because it has an invalid state %s.

* []()ID: 388

  Severity: ERROR\
  Message: An error occurred while trying to parse the scheduled start time value %s from task entry %s.

* []()ID: 389

  Severity: ERROR\
  Message: An error occurred while trying to parse the actual start time value %s from task entry %s.

* []()ID: 390

  Severity: ERROR\
  Message: An error occurred while trying to parse the completion time value %s from task entry %s.

* []()ID: 391

  Severity: ERROR\
  Message: Task entry %s is missing required attribute %s.

* []()ID: 394

  Severity: ERROR\
  Message: An error occurred while executing the task defined in entry %s: %s.

* []()ID: 403

  Severity: ERROR\
  Message: An error occurred while attempting to load class %s specified in attribute %s of the provided recurring task entry: %s. Does this class exist in the Directory Server classpath?.

* []()ID: 404

  Severity: ERROR\
  Message: An error occurred while trying to create an instance of class %s as a Directory Server task. Is this class a subclass of %s?.

* []()ID: 405

  Severity: ERROR\
  Message: An error occurred while attempting to perform internal initialization on an instance of class %s with the information contained in the provided entry: %s.

* []()ID: 406

  Severity: ERROR\
  Message: The specified task data backing file %s already exists and the Directory Server will not attempt to overwrite it. Please delete or rename the existing file before attempting to use that path for the new backing file, or choose a new path.

* []()ID: 407

  Severity: ERROR\
  Message: The specified path %s for the new task data backing file appears to be an invalid path. Please choose a new path for the task data backing file.

* []()ID: 408

  Severity: ERROR\
  Message: The parent directory %s for the new task data backing file %s does not exist. Please create this directory before attempting to use this path for the new backing file or choose a new path.

* []()ID: 409

  Severity: ERROR\
  Message: The parent directory %s for the new task data backing file %s exists but is not a directory. Please choose a new path for the task data backing file.

* []()ID: 410

  Severity: ERROR\
  Message: An error occurred while attempting to determine the new path to the task data backing file: %s.

* []()ID: 411

  Severity: INFO\
  Message: The completed task retention time has been updated to %d seconds. This will take effect immediately.

* []()ID: 412

  Severity: INFO\
  Message: The path to the task data backing file has been changed to %s. A snapshot of the current task configuration has been written to that file and it will continue to be used for future updates.

* []()ID: 413

  Severity: ERROR\
  Message: New entries in the task backend may only be added immediately below %s for scheduled tasks or immediately below %s for recurring tasks.

* []()ID: 414

  Severity: INFO\
  Message: This file contains the data used by the Directory Server task scheduler backend. Do not edit this file directly, as there is a risk that those changes will be lost. Scheduled and recurring task definitions should only be edited using the administration utilities provided with the Directory Server.

* []()ID: 415

  Severity: ERROR\
  Message: Unable to add recurring task %s to the task scheduler because another recurring task already exists with the same ID.

* []()ID: 416

  Severity: ERROR\
  Message: Unable to schedule task %s because another task already exists with the same ID.

* []()ID: 417

  Severity: WARNING\
  Message: Unable to add completed task %s to the task scheduler because another task already exists with the same ID.

* []()ID: 418

  Severity: ERROR\
  Message: An error occurred while attempting to schedule the next iteration of recurring task %s: %s.

* []()ID: 419

  Severity: ERROR\
  Message: An error occurred while attempting to read an entry from the tasks backing file %s on or near line %d: %s. This is not a fatal error, so the task scheduler will attempt to continue parsing the file and schedule any additional tasks that it contains.

* []()ID: 420

  Severity: ERROR\
  Message: An error occurred while attempting to read an entry from the tasks backing file %s on or near line %d: %s. This is an unrecoverable error, and parsing cannot continue.

* []()ID: 421

  Severity: ERROR\
  Message: Entry %s read from the tasks backing file is invalid because it has no parent and does not match the task root DN of %s.

* []()ID: 422

  Severity: ERROR\
  Message: An error occurred while attempting to parse entry %s as a recurring task and add it to the scheduler: %s.

* []()ID: 423

  Severity: ERROR\
  Message: An error occurred while attempting to parse entry %s as a task and add it to the scheduler: %s.

* []()ID: 424

  Severity: ERROR\
  Message: Entry %s read from the tasks backing file %s has a DN which is not valid for a task or recurring task definition and will be ignored.

* []()ID: 425

  Severity: ERROR\
  Message: An error occurred while attempting to read from the tasks data backing file %s: %s.

* []()ID: 426

  Severity: ERROR\
  Message: An error occurred while attempting to create a new tasks backing file %s for use with the task scheduler: %s.

* []()ID: 427

  Severity: ERROR\
  Message: The provided task entry does not contain attribute %s which is needed to specify the fully-qualified name of the class providing the task logic.

* []()ID: 428

  Severity: ERROR\
  Message: The provided task entry contains multiple attributes with type %s, which is used to hold the task class name, but only a single instance is allowed.

* []()ID: 429

  Severity: ERROR\
  Message: The provided task entry does not contain any values for the %s attribute, which is used to specify the fully-qualified name of the class providing the task logic.

* []()ID: 430

  Severity: ERROR\
  Message: The provided task entry contains multiple values for the %s attribute, which is used to specify the task class name, but only a single value is allowed.

* []()ID: 431

  Severity: ERROR\
  Message: An error occurred while attempting to load class %s specified in attribute %s of the provided task entry: %s. Does this class exist in the Directory Server classpath?.

* []()ID: 432

  Severity: ERROR\
  Message: An error occurred while trying to create an instance of class %s as a Directory Server task. Is this class a subclass of %s?.

* []()ID: 433

  Severity: ERROR\
  Message: An error occurred while attempting to perform internal initialization on an instance of class %s with the information contained in the provided entry: %s.

* []()ID: 434

  Severity: WARNING\
  Message: An error occurred while attempting to rename the current tasks backing file from %s to %s: %s. The previous task configuration (which does not reflect the latest update) may be lost.

* []()ID: 435

  Severity: ERROR\
  Message: An error occurred while attempting to rename the new tasks backing file from %s to %s: %s. If the Directory Server is restarted, then the task scheduler may not work as expected.

* []()ID: 436

  Severity: ERROR\
  Message: An error occurred while attempting to write the new tasks data backing file %s: %s. Configuration information reflecting the latest update may be lost.

* []()ID: 437

  Severity: INFO\
  Message: The tasks backend is being shut down.

* []()ID: 438

  Severity: INFO\
  Message: The root DSE configuration has been updated so that configuration attribute %s will now use a value of %s.

* []()ID: 439

  Severity: ERROR\
  Message: Unable to remove pending task %s because no such task exists.

* []()ID: 440

  Severity: ERROR\
  Message: Unable to remove pending task %s because the task is no longer pending.

* []()ID: 441

  Severity: ERROR\
  Message: Unable to remove completed task %s because no such task exists in the list of completed tasks.

* []()ID: 442

  Severity: ERROR\
  Message: Unable to remove entry %s from the task backend because its DN is either not appropriate for that backend or it is not below the scheduled or recurring tasks base entry.

* []()ID: 443

  Severity: ERROR\
  Message: Unable to remove entry %s from the task backend because there is no scheduled task associated with that entry DN.

* []()ID: 444

  Severity: ERROR\
  Message: Unable to delete entry %s from the task backend because the associated task is currently running.

* []()ID: 445

  Severity: ERROR\
  Message: Unable to remove entry %s from the task backend because there is no recurring task associated with that entry DN.

* []()ID: 446

  Severity: ERROR\
  Message: Unable to process the search operation in the task backend because the provided base DN %s is not valid for entries in the task backend.

* []()ID: 447

  Severity: ERROR\
  Message: Unable to process the search operation in the task backend because there is no scheduled task associated with the provided search base entry %s.

* []()ID: 448

  Severity: ERROR\
  Message: Unable to process the search operation in the task backend because there is no recurring task associated with the provided search base entry %s.

* []()ID: 449

  Severity: ERROR\
  Message: Unwilling to update entry "%s" because modify operations are not supported in the "%s" backend.

* []()ID: 450

  Severity: ERROR\
  Message: Exactly one base DN must be provided for use with the memory-based backend.

* []()ID: 451

  Severity: ERROR\
  Message: Entry %s already exists in the memory-based backend.

* []()ID: 452

  Severity: ERROR\
  Message: Entry %s does not belong in the memory-based backend.

* []()ID: 453

  Severity: ERROR\
  Message: Unable to add entry %s because its parent entry %s does not exist in the memory-based backend.

* []()ID: 454

  Severity: ERROR\
  Message: Entry %s does not exist in the "%s" backend.

* []()ID: 455

  Severity: ERROR\
  Message: Cannot delete entry %s because it has one or more subordinate entries.

* []()ID: 456

  Severity: ERROR\
  Message: Unable to create an LDIF writer: %s.

* []()ID: 457

  Severity: ERROR\
  Message: Cannot write entry %s to LDIF: %s.

* []()ID: 458

  Severity: ERROR\
  Message: Unable to create an LDIF reader: %s.

* []()ID: 459

  Severity: ERROR\
  Message: An unrecoverable error occurred while reading from LDIF: %s.

* []()ID: 460

  Severity: ERROR\
  Message: An unexpected error occurred while processing the import: %s.

* []()ID: 461

  Severity: ERROR\
  Message: Cannot rename entry %s because it has one or more subordinate entries.

* []()ID: 462

  Severity: ERROR\
  Message: Cannot rename entry %s because the target entry is in a different backend.

* []()ID: 463

  Severity: ERROR\
  Message: Cannot rename entry %s because the new parent entry %s doesn't exist.

* []()ID: 464

  Severity: ERROR\
  Message: An error occurred while attempting to register the base DNs %s in the Directory Server: %s.

* []()ID: 465

  Severity: ERROR\
  Message: The schema backend does not support the %s modification type.

* []()ID: 466

  Severity: ERROR\
  Message: The schema backend does not support the modification of the %s attribute type. Only attribute types, object classes, ldap syntaxes, name forms, DIT content rules, DIT structure rules, and matching rule uses may be modified.

* []()ID: 467

  Severity: ERROR\
  Message: An error occurred while attempting to write the updated schema: %s.

* []()ID: 468

  Severity: ERROR\
  Message: The server will not allow removing all values for the %s attribute type in the server schema.

* []()ID: 469

  Severity: ERROR\
  Message: Circular reference detected for attribute type %s in which the superior type chain references the attribute type itself.

* []()ID: 470

  Severity: ERROR\
  Message: Circular reference detected for objectclass %s in which the superior class chain references the objectclass itself.

* []()ID: 471

  Severity: ERROR\
  Message: Circular reference detected for DIT structure rule %s in which the superior rule chain references the DIT structure rule itself.

* []()ID: 472

  Severity: ERROR\
  Message: An error occurred while attempting to create copies of the existing schema files before applying the updates: %s. The server was able to restore the original schema configuration, so no additional cleanup should be required.

* []()ID: 473

  Severity: ERROR\
  Message: An error occurred while attempting to create copies of the existing schema files before applying the updates: %s. A problem also occurred when attempting to restore the original schema configuration, so the server may be left in an inconsistent state and could require manual cleanup.

* []()ID: 474

  Severity: ERROR\
  Message: An error occurred while attempting to write new versions of the server schema files: %s. The server was able to restore the original schema configuration, so no additional cleanup should be required.

* []()ID: 475

  Severity: ERROR\
  Message: An error occurred while attempting to write new versions of the server schema files: %s. A problem also occurred when attempting to restore the original schema configuration, so the server may be left in an inconsistent state and could require manual cleanup.

* []()ID: 476

  Severity: ERROR\
  Message: Unable to remove attribute type %s from the server schema because no such attribute type is defined.

* []()ID: 477

  Severity: ERROR\
  Message: Unable to remove objectclass %s from the server schema because no such objectclass is defined.

* []()ID: 478

  Severity: ERROR\
  Message: Unable to remove name form %s from the server schema because no such name form is defined.

* []()ID: 479

  Severity: ERROR\
  Message: Unable to remove DIT content rule %s from the server schema because no such DIT content rule is defined.

* []()ID: 480

  Severity: ERROR\
  Message: Unable to remove DIT structure rule %s from the server schema because no such DIT structure rule is defined.

* []()ID: 481

  Severity: ERROR\
  Message: Unable to remove matching rule use %s from the server schema because no such matching rule use is defined.

* []()ID: 482

  Severity: ERROR\
  Message: You do not have sufficient privileges to modify the Directory Server schema.

* []()ID: 483

  Severity: ERROR\
  Message: Unable to find a file containing concatenated schema element definitions in order to determine if any schema changes were made with the server offline. The file was expected in the %s directory and should have been named either %s or %s.

* []()ID: 484

  Severity: ERROR\
  Message: An error occurred while attempting to determine whether any schema changes had been made by directly editing the schema files with the server offline: %s.

* []()ID: 485

  Severity: ERROR\
  Message: An error occurred while attempting to write file %s containing a concatenated list of all server schema elements: %s. The server may not be able to accurately identify any schema changes made with the server offline.

* []()ID: 486

  Severity: ERROR\
  Message: The Directory Server is not configured to allow task %s to be invoked.

* []()ID: 488

  Severity: ERROR\
  Message: Indexes are not supported in the "%s" backend.

* []()ID: 489

  Severity: ERROR\
  Message: LDIF import and export operations are not supported in the "%s" backend.

* []()ID: 490

  Severity: ERROR\
  Message: The root container for backend %s has not been initialized preventing this backend from processing the requested operation.

* []()ID: 491

  Severity: ERROR\
  Message: Entry %s cannot be modified because it does not represent a task entry. Only task entries may be modified in the task backend.

* []()ID: 492

  Severity: ERROR\
  Message: Entry %s cannot be modified because it does not represent a valid task in the server.

* []()ID: 493

  Severity: ERROR\
  Message: Entry %s cannot be modified because the associated task has completed running. Completed tasks cannot be modified.

* []()ID: 494

  Severity: ERROR\
  Message: Entry %s cannot be modified because the server does not currently support modifying recurring task entries.

* []()ID: 495

  Severity: ERROR\
  Message: The task associated with entry %s is currently running. The only modification allowed for running tasks is to replace the value of the ds-task-state attribute with "cancel".

* []()ID: 496

  Severity: INFO\
  Message: Task processing was interrupted by a modify request to cancel the task.

* []()ID: 497

  Severity: ERROR\
  Message: The LDIF backend defined in configuration entry %s only supports a single base DN, but was configured for use with multiple base DNs.

* []()ID: 498

  Severity: ERROR\
  Message: LDIF file %s configured for use with the LDIF backend defined in configuration entry %s has multiple entries with a DN of %s.

* []()ID: 499

  Severity: ERROR\
  Message: LDIF file %s configured for use with the LDIF backend defined in configuration entry %s includes entry %s which is not below the base DN defined for that backend.

* []()ID: 500

  Severity: ERROR\
  Message: LDIF file %s configured for use with the LDIF backend defined in configuration entry %s contains entry %s but its parent entry has not yet been read.

## IDs: 501-1000

* []()ID: 501

  Severity: ERROR\
  Message: An error occurred while trying to create file %s to write an updated version of the data for the LDIF backend defined in configuration entry %s: %s.

* []()ID: 502

  Severity: ERROR\
  Message: An error occurred while trying to write updated data to file %s for the LDIF backend defined in configuration entry %s: %s.

* []()ID: 503

  Severity: ERROR\
  Message: An error occurred while attempting to rename file %s to %s while writing updated data for the LDIF backend defined in configuration entry %s: %s.

* []()ID: 504

  Severity: ERROR\
  Message: Entry %s already exists in the LDIF backend.

* []()ID: 505

  Severity: ERROR\
  Message: The parent for entry %s does not exist.

* []()ID: 506

  Severity: ERROR\
  Message: Entry %s does not exist.

* []()ID: 507

  Severity: ERROR\
  Message: Entry %s has one or more subordinate entries and cannot be deleted until all of its subordinate entries are removed first.

* []()ID: 508

  Severity: ERROR\
  Message: Entry %s does not exist.

* []()ID: 509

  Severity: ERROR\
  Message: Source entry %s does not exist.

* []()ID: 510

  Severity: ERROR\
  Message: Target entry %s already exists.

* []()ID: 511

  Severity: ERROR\
  Message: The new parent DN %s does not exist.

* []()ID: 512

  Severity: ERROR\
  Message: Entry %s specified as the search base DN does not exist.

* []()ID: 513

  Severity: ERROR\
  Message: An error occurred while trying to create the writer for the LDIF export operation: %s.

* []()ID: 514

  Severity: ERROR\
  Message: An error occurred while trying to write entry %s during the LDIF export: %s.

* []()ID: 515

  Severity: ERROR\
  Message: An error occurred while trying to create the reader for the LDIF import operation: %s.

* []()ID: 516

  Severity: ERROR\
  Message: An unrecoverable error occurred while attempting to read data from the import file: %s. The LDIF import cannot continue.

* []()ID: 517

  Severity: INFO\
  Message: The change to the LDIF file path will not take effect until the backend is disabled and re-enabled.

* []()ID: 518

  Severity: INFO\
  Message: The change to the LDIF backend base DN will not take effect until the backend is disabled and re-enabled.

* []()ID: 519

  Severity: ERROR\
  Message: The target entry %s does not exist.

* []()ID: 520

  Severity: ERROR\
  Message: The target entry %s does not exist.

* []()ID: 521

  Severity: ERROR\
  Message: This backend does not provide support for the numSubordinates operational attribute.

* []()ID: 522

  Severity: NOTICE\
  Message: The backend %s is now taken offline.

* []()ID: 523

  Severity: ERROR\
  Message: The provided recurring task entry attribute %s holding the recurring task schedule has invalid number of tokens.

* []()ID: 524

  Severity: ERROR\
  Message: The provided recurring task entry attribute %s holding the recurring task schedule has invalid minute token.

* []()ID: 525

  Severity: ERROR\
  Message: The provided recurring task entry attribute %s holding the recurring task schedule has invalid hour token.

* []()ID: 526

  Severity: ERROR\
  Message: The provided recurring task entry attribute %s holding the recurring task schedule has invalid day of the month token.

* []()ID: 527

  Severity: ERROR\
  Message: The provided recurring task entry attribute %s holding the recurring task schedule has invalid month of the year token.

* []()ID: 528

  Severity: ERROR\
  Message: The provided recurring task entry attribute %s holding the recurring task schedule has invalid day of the week token.

* []()ID: 529

  Severity: ERROR\
  Message: The provided recurring task entry attribute %s holding the recurring task schedule has invalid tokens combination yielding a nonexistent calendar date.

* []()ID: 530

  Severity: ERROR\
  Message: An error occurred while attempting to export task backend data: %s.

* []()ID: 533

  Severity: ERROR\
  Message: Unable to schedule task %s because its dependency task %s is missing.

* []()ID: 534

  Severity: NOTICE\
  Message: %s task %s started execution.

* []()ID: 535

  Severity: NOTICE\
  Message: %s task %s finished execution in the state %s.

* []()ID: 536

  Severity: ERROR\
  Message: Unable to remove ldap syntax description %s from the server schema because no such ldap syntax description is defined.

* []()ID: 537

  Severity: ERROR\
  Message: An error occurred while attempting to decode the ldapsyntax description "%s": %s.

* []()ID: 538

  Severity: ERROR\
  Message: The provided recurring task schedule value has an invalid number of tokens.

* []()ID: 539

  Severity: ERROR\
  Message: The provided recurring task schedule value has an invalid minute token.

* []()ID: 540

  Severity: ERROR\
  Message: The provided recurring task schedule value has an invalid hour token.

* []()ID: 541

  Severity: ERROR\
  Message: The provided recurring task schedule value has an invalid day of the month token.

* []()ID: 542

  Severity: ERROR\
  Message: The provided recurring task schedule value has an invalid month of the year token.

* []()ID: 543

  Severity: ERROR\
  Message: The provided recurring task schedule value has an invalid day of the week token.

* []()ID: 544

  Severity: ERROR\
  Message: The schema backend does not support the Replace modification type for the %s attribute type.

* []()ID: 545

  Severity: ERROR\
  Message: An error occurred while trying to close file %s for the LDIF backend defined in configuration entry %s: %s.

* []()ID: 546

  Severity: ERROR\
  Message: The file %s written for the LDIF backend defined in configuration entry %s is 0 bytes long and unusable.

* []()ID: 547

  Severity: ERROR\
  Message: Configuration attribute ds-cfg-db-cache-size has a value of %d but the JVM has only %d available. Consider using ds-cfg-db-cache-percent.

* []()ID: 548

  Severity: ERROR\
  Message: Configuration attribute ds-cfg-db-cache-percent has a value of %d%% but the JVM has only %d%% available.

* []()ID: 549

  Severity: ERROR\
  Message: Unable to process the virtual list view request because the target assertion could not be decoded as a valid value for the '%s' attribute type.

* []()ID: 550

  Severity: WARNING\
  Message: Disk free space of %d bytes for directory %s is now below low threshold of %d bytes. Backend %s is now locked down and will no longer accept any operations from clients until sufficient disk space is restored.

* []()ID: 551

  Severity: WARNING\
  Message: Disk free space of %d bytes for directory %s is now below disk low threshold of %d bytes. Backend %s is now offline and will no longer accept any operations until sufficient disk space is restored.

* []()ID: 552

  Severity: ERROR\
  Message: An error occurred while trying to list the files to backup for backend '%s': %s.

* []()ID: 553

  Severity: ERROR\
  Message: Insufficient free memory (%d bytes) to perform import. At least %d bytes of free memory is required.

* []()ID: 554

  Severity: ERROR\
  Message: Index for attribute '%s' cannot be created for matching rule '%s' because it cannot be found in the schema. Fix the matching rule name in the config or add the matching rule to the schema.

* []()ID: 555

  Severity: ERROR\
  Message: Unable to process the virtual list view request because the target start position was before the beginning of the result set.

* []()ID: 556

  Severity: ERROR\
  Message: The entry database does not contain a record for ID %s.

* []()ID: 557

  Severity: ERROR\
  Message: Execution error during backend operation: %s.

* []()ID: 558

  Severity: ERROR\
  Message: The backend database directory could not be created: %s.

* []()ID: 559

  Severity: WARNING\
  Message: This platform does not support setting file permissions %s to the database directory %s.

* []()ID: 560

  Severity: WARNING\
  Message: An error occurred while setting file permissions for the backend database directory %s: %s.

* []()ID: 561

  Severity: NOTICE\
  Message: The change to the DB directory will not take effect until the backend is restarted. The DB files from the previous directory %s must be moved to the new directory %s after shutting down the backend to retain the existing data.

* []()ID: 562

  Severity: ERROR\
  Message: The backend database directory '%s' is not a valid directory.

* []()ID: 563

  Severity: ERROR\
  Message: The entry '%s' cannot be added because an entry with that name already exists.

* []()ID: 564

  Severity: ERROR\
  Message: The entry '%s' cannot be added because its parent entry does not exist.

* []()ID: 565

  Severity: ERROR\
  Message: There is no index configured for attribute type '%s'.

* []()ID: 566

  Severity: ERROR\
  Message: An error occurred while attempting to decode an attribute description token from the compressed schema definitions: %s.

* []()ID: 567

  Severity: ERROR\
  Message: An error occurred while attempting to decode an object class set token from the compressed schema definitions: %s.

* []()ID: 568

  Severity: ERROR\
  Message: An error occurred while attempting to store compressed schema information in the database: %s.

* []()ID: 569

  Severity: ERROR\
  Message: An error occurred while parsing the search filter %s defined for VLV index %s: %s.

* []()ID: 570

  Severity: ERROR\
  Message: Sort attribute %s for VLV index %s is not defined in the server schema.

* []()ID: 571

  Severity: ERROR\
  Message: Database exception: %s.

* []()ID: 572

  Severity: ERROR\
  Message: A plugin caused the delete operation to be aborted while deleting a subordinate entry %s.

* []()ID: 573

  Severity: ERROR\
  Message: The entry '%s' cannot be removed because it has subordinate entries.

* []()ID: 574

  Severity: ERROR\
  Message: The entry '%s' cannot be removed because it does not exist.

* []()ID: 575

  Severity: ERROR\
  Message: An entry container named '%s' is already registered for base DN '%s'.

* []()ID: 576

  Severity: ERROR\
  Message: The entry database does not contain a valid record for ID %s.

* []()ID: 577

  Severity: ERROR\
  Message: I/O error occurred while exporting entry: %s.

* []()ID: 578

  Severity: ERROR\
  Message: The backend must be disabled before the import process can start.

* []()ID: 579

  Severity: ERROR\
  Message: Unable to create the temporary directory %s.

* []()ID: 580

  Severity: ERROR\
  Message: The import has been aborted because the entry '%s' does not have a parent entry.

* []()ID: 581

  Severity: ERROR\
  Message: Entry record is not compatible with this version of the backend database. Entry version: %x.

* []()ID: 582

  Severity: ERROR\
  Message: An error occurred while reading from index %s. The index seems to be corrupt and is no longer trusted. The index must be rebuilt before it can return to normal operation.

* []()ID: 583

  Severity: ERROR\
  Message: The following paged results control cookie value was not recognized: %s.

* []()ID: 584

  Severity: ERROR\
  Message: A plugin caused the modify DN operation to be aborted while moving and/or renaming an entry from %s to %s.

* []()ID: 585

  Severity: ERROR\
  Message: The entry cannot be renamed to '%s' because an entry with that name already exists.

* []()ID: 586

  Severity: ERROR\
  Message: The entry '%s' cannot be renamed because it does not exist.

* []()ID: 587

  Severity: ERROR\
  Message: The entry '%s' cannot be modified because it does not exist.

* []()ID: 588

  Severity: ERROR\
  Message: The entry cannot be moved because the new parent entry '%s' does not exist.

* []()ID: 589

  Severity: ERROR\
  Message: The database environment could not be opened: %s.

* []()ID: 590

  Severity: ERROR\
  Message: Rebuilding system index(es) must be done with the backend containing the base DN disabled.

* []()ID: 591

  Severity: ERROR\
  Message: The backend database files could not be removed: %s.

* []()ID: 592

  Severity: ERROR\
  Message: The requested search operation included both the simple paged results control and the virtual list view control. These controls are mutually exclusive and cannot be used together.

* []()ID: 593

  Severity: ERROR\
  Message: The search results cannot be sorted because the given search request is not indexed.

* []()ID: 594

  Severity: ERROR\
  Message: The search base entry '%s' does not exist.

* []()ID: 595

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform an unindexed search.

* []()ID: 596

  Severity: ERROR\
  Message: Unchecked exception during database transaction: %s.

* []()ID: 597

  Severity: ERROR\
  Message: There is no VLV index configured with name '%s'.

* []()ID: 598

  Severity: INFO\
  Message: The filter value exceeded the index entry limit for the %s index.

* []()ID: 599

  Severity: INFO\
  Message: %s index is invalid and needs to be rebuilt.

* []()ID: 600

  Severity: INFO\
  Message: %s index type is disabled for the %s attribute.

* []()ID: 601

  Severity: INFO\
  Message: Average number of entries referenced is %.2f/record.

* []()ID: 602

  Severity: INFO\
  Message: Free memory = %d MB, Cache miss rate = %.1f/record.

* []()ID: 603

  Severity: INFO\
  Message: Number of records that exceed the entry limit: %d.

* []()ID: 604

  Severity: INFO\
  Message: Statistics for records that have exceeded the entry limit:.

* []()ID: 605

  Severity: INFO\
  Message: File %s has %d such record(s) min=%d max=%d median=%d.

* []()ID: 606

  Severity: INFO\
  Message: Maximum number of entries referenced by any record is %d.

* []()ID: 607

  Severity: INFO\
  Message: Number of records referencing more than one entry: %d.

* []()ID: 608

  Severity: NOTICE\
  Message: The database backend %s containing %d entries has started.

* []()ID: 609

  Severity: NOTICE\
  Message: Some index keys have already exceeded the previous index entry limit in index %s. This index must be rebuilt before it can use the new limit.

* []()ID: 610

  Severity: NOTICE\
  Message: Exported %d entries and skipped %d in %d seconds (average rate %.1f/sec).

* []()ID: 611

  Severity: NOTICE\
  Message: Exported %d records and skipped %d (recent rate %.1f/sec).

* []()ID: 612

  Severity: NOTICE\
  Message: Flushing data to disk.

* []()ID: 613

  Severity: NOTICE\
  Message: Processed %d entries, imported %d, skipped %d and rejected %d in %d seconds (average rate %.1f/sec).

* []()ID: 614

  Severity: NOTICE\
  Message: Setting DB cache size to %d bytes and phase one buffer size to %d bytes.

* []()ID: 615

  Severity: NOTICE\
  Message: Index %s phase two processing completed.

* []()ID: 616

  Severity: NOTICE\
  Message: Index %s phase two started processing %d buffers in %d batches.

* []()ID: 617

  Severity: NOTICE\
  Message: Index %s %d%% complete: remaining = %d KB, rate = %d KB/s; batch %d/%d.

* []()ID: 618

  Severity: NOTICE\
  Message: Import LDIF environment close took %d seconds.

* []()ID: 619

  Severity: NOTICE\
  Message: The amount of free memory available to the import task is %d bytes. The number of phase one buffers required is %d buffers.

* []()ID: 620

  Severity: NOTICE\
  Message: Total import time was %d seconds. Phase one processing completed in %d seconds, phase two processing completed in %d seconds.

* []()ID: 621

  Severity: NOTICE\
  Message: Processed %d entries, skipped %d and rejected %d (recent rate %.1f/sec).

* []()ID: 622

  Severity: NOTICE\
  Message: %s starting import (build %s, R%s).

* []()ID: 623

  Severity: NOTICE\
  Message: Import Thread Count: %d threads.

* []()ID: 624

  Severity: NOTICE\
  Message: Due to changes in the configuration, index %s is currently untrusted and must be rebuilt before it can be used.

* []()ID: 625

  Severity: NOTICE\
  Message: Rebuild of all indexes started with %d total entries to process.

* []()ID: 627

  Severity: NOTICE\
  Message: Rebuild of all untrusted indexes started with %d total entries to process.

* []()ID: 628

  Severity: NOTICE\
  Message: Rebuild complete. Processed %d entries in %d seconds (average rate %.1f/sec).

* []()ID: 629

  Severity: NOTICE\
  Message: %.1f%% Completed. Processed %d/%d entries. (recent rate %.1f/sec).

* []()ID: 630

  Severity: NOTICE\
  Message: Rebuild of index(es) %s started with %d total entries to process.

* []()ID: 631

  Severity: NOTICE\
  Message: A referral entry %s indicates that the operation must be processed at a different server.

* []()ID: 632

  Severity: NOTICE\
  Message: Checked %d records and found %d error(s) in %d seconds (average rate %.1f/sec).

* []()ID: 633

  Severity: NOTICE\
  Message: Checked %d entries and found %d error(s) in %d seconds (average rate %.1f/sec).

* []()ID: 634

  Severity: NOTICE\
  Message: Processed %d out of %d records and found %d error(s) (recent rate %.1f/sec).

* []()ID: 635

  Severity: WARNING\
  Message: The requested operation is not supported by this backend.

* []()ID: 636

  Severity: WARNING\
  Message: Unable to determine the total number of entries in the container: %s.

* []()ID: 637

  Severity: ERROR\
  Message: The database logging level string '%s' provided for configuration entry '%s' is invalid. The value must be one of OFF, SEVERE, WARNING, INFO, CONFIG, FINE, FINER, FINEST, or ALL. Note that these values are case sensitive.

* []()ID: 638

  Severity: ERROR\
  Message: Configuration attribute ds-cfg-db-cache-size has a value of %d which is less than the minimum: %d.

* []()ID: 639

  Severity: ERROR\
  Message: Missing ID %d%n%s.

* []()ID: 640

  Severity: ERROR\
  Message: Reference to unknown entry ID %s%n%s.

* []()ID: 641

  Severity: ERROR\
  Message: The entry with ID %s is associated with the wrong key%n%s.

* []()ID: 642

  Severity: ERROR\
  Message: Empty ID set: %n%s.

* []()ID: 643

  Severity: ERROR\
  Message: Duplicate reference to ID %d%n%s.

* []()ID: 644

  Severity: ERROR\
  Message: Reference to unknown ID %d%n%s.

* []()ID: 645

  Severity: ERROR\
  Message: Reference to entry <%s> which does not match the value%n%s.

* []()ID: 646

  Severity: ERROR\
  Message: File dn2id is missing key %s.

* []()ID: 647

  Severity: ERROR\
  Message: File dn2id has ID %d instead of %d for key %s.

* []()ID: 648

  Severity: ERROR\
  Message: File dn2id has DN <%s> referencing unknown ID %d.

* []()ID: 649

  Severity: ERROR\
  Message: File dn2id has DN <%s> referencing entry with wrong DN <%s>.

* []()ID: 650

  Severity: ERROR\
  Message: The stored entry count in id2entry (%d) does not agree with the actual number of entry records found (%d).

* []()ID: 651

  Severity: ERROR\
  Message: File id2childrenCount has wrong number of children for DN <%s> (got %d, expecting %d).

* []()ID: 652

  Severity: ERROR\
  Message: File id2ChildrenCount references non-existing EntryID <%d>.

* []()ID: 653

  Severity: NOTICE\
  Message: Rebuilding index finished: no indexes to rebuild.

* []()ID: 655

  Severity: ERROR\
  Message: Ignoring schema definition '%s' because the following error occurred while it was being parsed: %s.

* []()ID: 656

  Severity: ERROR\
  Message: Schema definition could not be parsed as valid attribute value.

* []()ID: 657

  Severity: ERROR\
  Message: Attribute %s is set as confidential on a backend whose entries are still cleartext. Enable confidentiality on the backend first.

* []()ID: 658

  Severity: ERROR\
  Message: The attribute '%s' cannot enable confidentiality for keys and values at the same time.

* []()ID: 659

  Severity: ERROR\
  Message: Cannot encode entry for writing on storage: %s.

* []()ID: 660

  Severity: ERROR\
  Message: Input stream ended unexpectedly while decoding entry.

* []()ID: 661

  Severity: ERROR\
  Message: Confidentiality cannot be disabled on suffix '%s' because the following indexes have confidentiality still enabled: %s.

* []()ID: 662

  Severity: NOTICE\
  Message: Changing confidentiality for index '%s' requires the index to be rebuilt before it can be used again.

* []()ID: 663

  Severity: ERROR\
  Message: Error while enabling confidentiality with cipher %s, %d bits: %s.

* []()ID: 664

  Severity: ERROR\
  Message: The import has been aborted because the data to be imported contains duplicate copies of entry '%s'.

* []()ID: 665

  Severity: ERROR\
  Message: Proxy backend '%s' could not discover remote servers capabilities: %s.

* []()ID: 666

  Severity: INFO\
  Message: Proxy backend '%s' successfully configured failover via the service discovery mechanism '%s': primary servers are %s and secondary servers are %s.

* []()ID: 667

  Severity: WARNING\
  Message: Proxy backend '%s' cannot failover: only primary servers have been discovered via the service discovery mechanism '%s'. Primary servers are %s.

* []()ID: 668

  Severity: WARNING\
  Message: Proxy backend '%s' cannot failover: only secondary servers have been discovered via the service discovery mechanism '%s'. Secondary servers are %s.

* []()ID: 669

  Severity: ERROR\
  Message: Proxy backend '%s' is non functional because it could not find any primary nor secondary servers via the service discovery mechanism '%s'.

* []()ID: 670

  Severity: ERROR\
  Message: Proxy backend '%s' cannot find the configured service discovery mechanism '%s'.

* []()ID: 671

  Severity: NOTICE\
  Message: Connection options have changed for the proxy backend '%s'. The existing connections are being closed immediately. New ones are being opened.

* []()ID: 672

  Severity: NOTICE\
  Message: Connection pool options have changed for the proxy backend '%s'. The existing connections are being closed and re-opened.

* []()ID: 673

  Severity: NOTICE\
  Message: Service discovery mechanism has changed from '%s' to '%s' for proxy backend '%s'. The existing connections are being closed immediately.

* []()ID: 674

  Severity: NOTICE\
  Message: Remote servers changed for the proxy backend '%s'. The proxy was using: primary servers=%s, secondary servers=%s; and it will now be using: primary servers=%s, secondary servers=%s.

* []()ID: 675

  Severity: INFO\
  Message: Proxy backend '%s' automatically registered itself against the base DNs %s. It was previously registered against the base DNs %s.

* []()ID: 677

  Severity: ERROR\
  Message: Proxy backend '%s' cannot register itself against base DN %s because this base DN is already registered against backend '%s'.

* []()ID: 678

  Severity: ERROR\
  Message: Proxy backend '%s' is being deregistered from base DN %s because local backend '%s' is registering against it. Local backends take precedence over proxy backends.

* []()ID: 679

  Severity: INFO\
  Message: The change to the LDIF backend visibility will not take effect until the backend is disabled and re-enabled.

* []()ID: 680

  Severity: INFO\
  Message: The primary servers for proxy backend '%s' are now available and will be used for proxying requests.

* []()ID: 681

  Severity: INFO\
  Message: The secondary servers for proxy backend '%s' are now available and will be used if the primary servers are unavailable.

* []()ID: 682

  Severity: WARNING\
  Message: The primary servers for proxy backend '%s' are unavailable. The secondary servers, if available, will be used for processing requests until the primary servers become available again. The last failure that prevented the primary servers from being used was: %s.

* []()ID: 683

  Severity: WARNING\
  Message: The secondary servers for proxy backend '%s' are unavailable. If the primary servers are unavailable, or become unavailable, then it will no longer be possible to proxy requests. The last failure that prevented the secondary servers from being used was: %s.

* []()ID: 684

  Severity: INFO\
  Message: The server '%s' for proxy backend '%s' is available and will be used for proxying requests.

* []()ID: 685

  Severity: WARNING\
  Message: The server '%s' for proxy backend '%s' is unavailable. The last failure that prevented the server from being used was: %s.

* []()ID: 686

  Severity: ERROR\
  Message: The partition base DN '%s' should be subordinate to one of the base DNs %s of proxy backend '%s'.

* []()ID: 687

  Severity: ERROR\
  Message: Backend database cache preload for backend '%s' is not supported in this release.

* []()ID: 688

  Severity: INFO\
  Message: Configuration of proxy backend '%s' with service discovery mechanism '%s' is in progress. Requests will not be proxied until configuration completes.

* []()ID: 689

  Severity: WARNING\
  Message: The server is performing an unindexed internal search request with base DN '%s', scope '%s', and filter '%s'. Unindexed internal searches are usually unexpected and could impact performance. Please verify that this backend's indexes are configured correctly for these search parameters.

* []()ID: 691

  Severity: ERROR\
  Message: There are insufficient resources to perform the operation.

* []()ID: 692

  Severity: ERROR\
  Message: The time-to-live (TTL) feature can only be enabled for generalized time ordering indexes.

* []()ID: 693

  Severity: ERROR\
  Message: An unexpected error occurred while purging expired entries: %s.

* []()ID: 694

  Severity: WARNING\
  Message: Unable to locate all expired entries on backend '%s' because the ttl-enabled index '%s' has reached the configured index-entry-limit.

* []()ID: 695

  Severity: ERROR\
  Message: The partition base DN '%s' shouldn't be subordinate to one of the other partition base DNs %s of proxy backend '%s'.

* []()ID: 696

  Severity: WARNING\
  Message: The proxy backend '%s' will ignore the discovered servers '%s' from shard '%s' because they do not expose the required base DNs '%s'.

* []()ID: 697

  Severity: WARNING\
  Message: Property '%s' contains value '%s' which cannot be parsed as a long. Defaulting to '%s' bytes for small DB size.

* []()ID: 698

  Severity: ERROR\
  Message: An error occurred while trying to retrieve the key managers from the key manager provider `%s`.

* []()ID: 699

  Severity: ERROR\
  Message: Could not stop export-ldif threads after 30 seconds. Now forcing stop by interrupting them.

* []()ID: 700

  Severity: WARNING\
  Message: The file system used by '%s' backend does not support last file modification time. Backups will still work but will take longer and consume more space in the backup storage.

* []()ID: 701

  Severity: ERROR\
  Message: The index(es) cannot be rebuilt because the server failed to obtain a write lock for the entry '%s' after multiple attempts.

* []()ID: 702

  Severity: ERROR\
  Message: VLV index '%s' must be configured with at least one sort attribute.

* []()ID: 703

  Severity: ERROR\
  Message: Missing entry %s in index %s.

* []()ID: 704

  Severity: ERROR\
  Message: Big index for attribute '%s' cannot be created for matching rule '%s' because it is not an equality matching rule.

* []()ID: 705

  Severity: WARNING\
  Message: The subtree delete against '%s' is being performed non-atomically because it is deleting more than %s subordinate entries. To prevent inconsistency across replicas, the client must retry this same delete operation until it succeeds.

* []()ID: 706

  Severity: ERROR\
  Message: A Server Side Sort control must be specified whenever a Virtual List View control is present.

* []()ID: 707

  Severity: ERROR\
  Message: Counter of %s reports wrong number of entries for key <%s> (got %d, expecting %d).

* []()ID: 708

  Severity: ERROR\
  Message: An error occurred while attempting to send an email for the completion of %s task: Task ID: %s, Task State: %s, Scheduled Start Time: %s, Actual Start Time: %s, Completion Time: %s. The error was: %s.

* []()ID: 709

  Severity: ERROR\
  Message: Index for attribute '%s' cannot be created because the configuration contains an included attribute value '%s' which appears to be invalid according to the schema: %s.

* []()ID: 710

  Severity: ERROR\
  Message: The VLV request cannot be processed because the search is not indexed. Configure a VLV index matching the request.

* []()ID: 711

  Severity: NOTICE\
  Message: Both equality and presence index types are defined for attribute '%s'. When no presence index exists, presence search filters are processed using the equality index. Therefore, consider deleting the presence index for attribute '%s'.

* []()ID: 712

  Severity: ERROR\
  Message: An internal error occurred when accessing backend '%s': %s.

* []()ID: 713

  Severity: ERROR\
  Message: An internal error was detected when accessing backend '%s'.

* []()ID: 714

  Severity: NOTICE\
  Message: Starting backup for backend '%s'.

* []()ID: 715

  Severity: NOTICE\
  Message: Starting restore for backend '%s' with backup ID '%s'.

* []()ID: 716

  Severity: NOTICE\
  Message: Backup completed for backend '%s' with backup ID '%s'.

* []()ID: 717

  Severity: NOTICE\
  Message: Restore completed for backend '%s' with backup ID '%s'.

* []()ID: 718

  Severity: NOTICE\
  Message: An error occurred while attempting to backup backend '%s': %s.

* []()ID: 719

  Severity: NOTICE\
  Message: The backup process failed with one or more errors.

* []()ID: 720

  Severity: NOTICE\
  Message: The restore process failed with one or more errors.

* []()ID: 721

  Severity: NOTICE\
  Message: An error occurred while attempting to restore backend '%s' with backup ID '%s': %s.

* []()ID: 722

  Severity: NOTICE\
  Message: There are no enabled backends that support backup operation.

* []()ID: 723

  Severity: NOTICE\
  Message: The backup command was interrupted.

* []()ID: 724

  Severity: NOTICE\
  Message: Cannot read backup directory content: %s.

* []()ID: 725

  Severity: NOTICE\
  Message: Backup still in progress, new files have been created.

* []()ID: 726

  Severity: NOTICE\
  Message: Backing up file (%d/%d) '%s'.

* []()ID: 727

  Severity: NOTICE\
  Message: Verifying file (%d/%d) '%s'.

* []()ID: 728

  Severity: NOTICE\
  Message: Restoring file (%d/%d) '%s'.

* []()ID: 729

  Severity: NOTICE\
  Message: Purging backup (%d/%d) '%s'.

* []()ID: 730

  Severity: NOTICE\
  Message: The following backends do not exist or are disabled: %s. Here is the list of enabled backends that support backups: %s.

* []()ID: 731

  Severity: NOTICE\
  Message: The following backends do not support backups: %s. Here is the list of enabled backends that support backups: %s.

* []()ID: 732

  Severity: NOTICE\
  Message: The backends %s cannot be restored because they do not exist or are disabled.

* []()ID: 733

  Severity: NOTICE\
  Message: Cannot find backup with ID %s.

* []()ID: 734

  Severity: NOTICE\
  Message: There are no backups for backends %s.

* []()ID: 735

  Severity: NOTICE\
  Message: The backends %s cannot be restored while the server is running. Please stop the server first and try again with the --offline option.

* []()ID: 736

  Severity: NOTICE\
  Message: '%s' is not a valid name for a directory.

* []()ID: 737

  Severity: NOTICE\
  Message: Found backup IDs that correspond to the same backend name: %s. Make sure each backup ID corresponds to a distinct backend.

* []()ID: 738

  Severity: NOTICE\
  Message: Either the --%s or --%s argument must be provided.

* []()ID: 739

  Severity: NOTICE\
  Message: Cannot delete corrupted file '%s'.

* []()ID: 740

  Severity: NOTICE\
  Message: Deleting corrupted file from backend directory.

* []()ID: 741

  Severity: NOTICE\
  Message: Deleting corrupted file from backup storage.

* []()ID: 742

  Severity: NOTICE\
  Message: signature does not match.

* []()ID: 743

  Severity: NOTICE\
  Message: unexpected content.

* []()ID: 744

  Severity: NOTICE\
  Message: Problem with file '%s' : %s.

* []()ID: 745

  Severity: NOTICE\
  Message: IO error: %s.

* []()ID: 746

  Severity: NOTICE\
  Message: Operation was interrupted.

* []()ID: 747

  Severity: NOTICE\
  Message: File '%s' is corrupted: %s.

* []()ID: 748

  Severity: NOTICE\
  Message: File '%s' is missing.

* []()ID: 749

  Severity: NOTICE\
  Message: The directory does not exist.

* []()ID: 750

  Severity: NOTICE\
  Message: Not a directory.

* []()ID: 751

  Severity: NOTICE\
  Message: Cannot read backend files in directory '%s': %s.

* []()ID: 752

  Severity: NOTICE\
  Message: Cannot delete backend files from directory '%s': %s.

* []()ID: 753

  Severity: NOTICE\
  Message: The '%s' backend files have been removed after restore failed. The backend is now empty.

* []()ID: 754

  Severity: NOTICE\
  Message: Cannot create the backend directory '%s' before restoring: %s.

* []()ID: 755

  Severity: NOTICE\
  Message: The attempt to remove backend files from directory '%s' has failed, backend '%s' may contain corrupted data, please remove the files manually.

* []()ID: 756

  Severity: NOTICE\
  Message: The backup ID '%s' already exists.

* []()ID: 757

  Severity: NOTICE\
  Message: Cannot compute the fingerprint for backend file '%s': %s.

* []()ID: 758

  Severity: NOTICE\
  Message: Unable to access the backup storage: %s.

* []()ID: 759

  Severity: NOTICE\
  Message: No plugin found to handle the storage scheme '%s'.

* []()ID: 760

  Severity: NOTICE\
  Message: Cannot delete the backup lock file '%s', please remove this file manually: %s.

* []()ID: 761

  Severity: NOTICE\
  Message: Cannot acquire a shared lock for backend '%s': %s. This generally means that some other process has exclusive access to this backend (e.g., a restore or an LDIF import).

* []()ID: 762

  Severity: NOTICE\
  Message: Cannot release the shared lock for backend '%s': %s. This lock should automatically be cleared when the backup process exits, so no further action should be required.

* []()ID: 763

  Severity: NOTICE\
  Message: Cannot acquire an exclusive lock for backend '%s': %s. This generally means some other process is still using this backend (e.g., it is in use by the Directory Server or a backup or LDIF export is in progress).

* []()ID: 764

  Severity: NOTICE\
  Message: Cannot release the exclusive lock for backend '%s': %s. This lock should automatically be cleared when the restore process exits, so no further action should be required.

* []()ID: 765

  Severity: NOTICE\
  Message: Cannot enable backend '%s' after restoring: %s.

* []()ID: 766

  Severity: NOTICE\
  Message: Backup ID: %s.

* []()ID: 767

  Severity: NOTICE\
  Message: Backup Date: %s.

* []()ID: 768

  Severity: NOTICE\
  Message: Backend name: %s.

* []()ID: 769

  Severity: NOTICE\
  Message: Server ID: %s.

* []()ID: 770

  Severity: NOTICE\
  Message: Status: %s.

* []()ID: 771

  Severity: NOTICE\
  Message: Error: %s.

* []()ID: 772

  Severity: NOTICE\
  Message: Verified.

* []()ID: 773

  Severity: NOTICE\
  Message: Bad.

* []()ID: 774

  Severity: NOTICE\
  Message: Found %s backup(s) with the requested characteristics.

* []()ID: 775

  Severity: NOTICE\
  Message: There are no backups with the requested characteristics.

* []()ID: 776

  Severity: NOTICE\
  Message: %s backup(s) cannot be restored.

* []()ID: 777

  Severity: NOTICE\
  Message: Found %s backup(s) that cannot be fully identified due to the following error(s):.

* []()ID: 778

  Severity: NOTICE\
  Message: Backup and restore backends, manage backup files.

* []()ID: 779

  Severity: NOTICE\
  Message: Backup and restore backends.

* []()ID: 780

  Severity: NOTICE\
  Message: {backup location}.

* []()ID: 781

  Severity: NOTICE\
  Message: Indicates that the command will operate independently of the server process. It will run regardless of whether the server is started or stopped. When using this option with the %1$s sub-command, the server must be stopped; also as the command will write to server files, you should run the command as a user having the same filesystem permissions as the user running the server. Using this option with the %2$s sub-command when the server is running is possible and supported. With JE Backends, the integrity of the backup is ensured by the process. With LDIF backends, avoid simultaneous changes to the backends.

* []()ID: 782

  Severity: NOTICE\
  Message: Backup file-system path or URI for alternative storage mechanisms. File-system paths may be expressed as absolute or relative paths and are resolved relative to the current working directory when the tool is run in offline mode, or relative to the server instance directory when the tool is run in task mode. Read the documentation for further information regarding alternative backup storage mechanisms.

* []()ID: 783

  Severity: NOTICE\
  Message: Location containing backups: file-system path or URI for alternative storage mechanisms. File-system paths may be expressed as absolute or relative paths and are resolved relative to the current working directory when the tool is run in offline mode, or relative to the server instance directory when the tool is run in task mode. Read the documentation for further information regarding alternative backup storage mechanisms.

* []()ID: 784

  Severity: NOTICE\
  Message: {PROP:VALUE}.

* []()ID: 785

  Severity: NOTICE\
  Message: Assigns a value to a storage property where PROP is the name of the property and VALUE is the single value to be assigned. Specify the same property multiple times in order to assign more than one value to it.

* []()ID: 786

  Severity: NOTICE\
  Message: List the backups at the specified location.

* []()ID: 787

  Severity: NOTICE\
  Message: Show only backups taken from the provided backend.

* []()ID: 788

  Severity: NOTICE\
  Message: Show only backups taken from the provided server.

* []()ID: 789

  Severity: NOTICE\
  Message: {server ID}.

* []()ID: 790

  Severity: NOTICE\
  Message: Show only the last backup for each backend.

* []()ID: 791

  Severity: NOTICE\
  Message: Verify backups completeness, integrity and whether they can be decrypted.

* []()ID: 792

  Severity: NOTICE\
  Message: Take encrypted and signed backups of individual backends and send them to the desired location.

* []()ID: 793

  Severity: NOTICE\
  Message: The name of the backend to back up. Specify this option multiple times to backup multiple backends or skip this option to backup all the enabled backends that support backups.

* []()ID: 794

  Severity: NOTICE\
  Message: {backup ID}.

* []()ID: 795

  Severity: NOTICE\
  Message: Restore one or more backends. In order to decrypt and verify signatures on backup files, the server must have access to the master key pair used to encrypt and sign the files when they were created.

* []()ID: 796

  Severity: NOTICE\
  Message: Restore the backup having the provided ID. Specify this option multiple times to restore multiple backends.

* []()ID: 797

  Severity: NOTICE\
  Message: Restore the last backup of the provided backend. Specify this option multiple times to restore multiple backends.

* []()ID: 798

  Severity: NOTICE\
  Message: Delete one or more backups.

* []()ID: 799

  Severity: NOTICE\
  Message: The ID of the backup that should be deleted. Specify this option multiple times to purge multiple backups.

* []()ID: 800

  Severity: NOTICE\
  Message: At least one of these options must be declared: %s.

* []()ID: 801

  Severity: NOTICE\
  Message: The option '--%s' can only be used with the option '--%s'.

* []()ID: 802

  Severity: NOTICE\
  Message: {number of backups}.

* []()ID: 803

  Severity: NOTICE\
  Message: The number of backups to keep per backend. Use this option to keep the n latest backups of each backend and delete the others. If n=0, all the backups will be removed.

* []()ID: 804

  Severity: NOTICE\
  Message: {duration}.

* []()ID: 805

  Severity: NOTICE\
  Message: Delete backups that are older than the provided duration. The latest backup of each backend will always be kept unless the '--%s' option is also provided. Duration examples: '12 hours', '3 days', '1y'.

* []()ID: 806

  Severity: NOTICE\
  Message: Must be used with the '--%s' option, indicates that the last backup of each backend can be deleted if older than the provided duration.

* []()ID: 807

  Severity: NOTICE\
  Message: {backend name}.

* []()ID: 808

  Severity: NOTICE\
  Message: Purge only backups of the specified backend. Specify this option multiple times to allow purging backups of different backends. Skip this option to allow purging backups of all backends. This can only be used with options '--%s' or '--%s'.

* []()ID: 809

  Severity: NOTICE\
  Message: '%d' is not allowed: the value must be equal or greater than 0.

* []()ID: 810

  Severity: NOTICE\
  Message: Invalid value for '%s': %s.

* []()ID: 811

  Severity: NOTICE\
  Message: An error occurred while attempting to purge the backup '%s': %s.

* []()ID: 812

  Severity: NOTICE\
  Message: An error occurred while attempting to purge backup files starting with '%s': %s.

* []()ID: 813

  Severity: NOTICE\
  Message: Backup purge process failed with one or more errors.

* []()ID: 814

  Severity: NOTICE\
  Message: Purge completed successfully.

* []()ID: 815

  Severity: NOTICE\
  Message: The storage property '%s' has several values while it can have only one. The provided properties string was: "%s".

* []()ID: 816

  Severity: ERROR\
  Message: Backup id '%s' is invalid: expected to find an underscore in it.

* []()ID: 817

  Severity: ERROR\
  Message: Backup id '%s' is invalid: cannot parse '%s' as a timestamp.

* []()ID: 818

  Severity: NOTICE\
  Message: Access denied to file '%s'.

* []()ID: 819

  Severity: ERROR\
  Message: Credential file '%s' not found.

* []()ID: 820

  Severity: ERROR\
  Message: Failed to parse the credential file '%s'.

* []()ID: 821

  Severity: ERROR\
  Message: Invalid plugin type '%s', a backup plugin must be of type '%s'.

* []()ID: 822

  Severity: ERROR\
  Message: A problem occurred while connecting to cloud provider '%s' using the provided credentials: %s.

* []()ID: 823

  Severity: ERROR\
  Message: No value found for property '%s'.

* []()ID: 824

  Severity: ERROR\
  Message: No environment value '%s' found for property '%s'. If you are running the tool in offline mode, make sure the command has access to this variable, or else make sure the directory server has access to it.

* []()ID: 825

  Severity: ERROR\
  Message: Could not find file '%s' in cloud bucket '%s'.

* []()ID: 826

  Severity: ERROR\
  Message: An error occurred while uploading the file to the cloud storage: the host '%s' is an unknown host.

* []()ID: 827

  Severity: ERROR\
  Message: An error occurred while uploading the file to the cloud storage. The cloud provider returned the following error message: '%s'.

* []()ID: 828

  Severity: ERROR\
  Message: Unable to set the value for Boolean configuration attribute %s because the provided value %s was not either 'true' or 'false'.

* []()ID: 829

  Severity: ERROR\
  Message: Unable to set the value for integer configuration attribute %s because the provided value %s cannot be interpreted as an integer value: %s.

* []()ID: 830

  Severity: ERROR\
  Message: Unable to set the value for configuration attribute %s because the provided value %d is less than the lowest allowed value of %d.

* []()ID: 831

  Severity: ERROR\
  Message: Unable to set the value for configuration attribute %s because the provided value %d is greater than the largest allowed value of %d.

* []()ID: 832

  Severity: ERROR\
  Message: The specified configuration file %s does not exist or is not readable.

* []()ID: 833

  Severity: ERROR\
  Message: An error occurred while attempting to open the configuration file %s for reading: %s.

* []()ID: 834

  Severity: ERROR\
  Message: The first entry read from LDIF configuration file %s had a DN of "%s" rather than the expected "%s" which should be used as the Directory Server configuration root.

* []()ID: 835

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to process the Directory Server configuration file %s: %s.

* []()ID: 837

  Severity: ERROR\
  Message: An unexpected error occurred while trying to write configuration entry %s to LDIF: %s.

* []()ID: 838

  Severity: ERROR\
  Message: The Directory Server configuration may not be altered by importing a new configuration from LDIF.

* []()ID: 839

  Severity: WARNING\
  Message: There are no active access loggers defined in the Directory Server configuration. No access logging will be performed.

* []()ID: 840

  Severity: WARNING\
  Message: There are no active error loggers defined in the Directory Server configuration. No error logging will be performed.

* []()ID: 841

  Severity: ERROR\
  Message: An error occurred while attempting to create a Directory Server logger from the information in configuration entry %s: %s.

* []()ID: 842

  Severity: ERROR\
  Message: Configuration entry %s does not contain a valid objectclass for a Directory Server access, error, or debug logger definition.

* []()ID: 843

  Severity: ERROR\
  Message: Class %s specified in attribute ds-cfg-java-class of configuration entry %s cannot be instantiated as a Directory Server access logger: %s.

* []()ID: 844

  Severity: ERROR\
  Message: Class %s specified in attribute ds-cfg-java-class of configuration entry %s cannot be instantiated as a Directory Server error logger: %s.

* []()ID: 846

  Severity: ERROR\
  Message: Configuration entry %s does not contain attribute %s (or that attribute exists but is not accessible using JMX).

* []()ID: 847

  Severity: ERROR\
  Message: There is no method %s for any invokable component registered with configuration entry %s.

* []()ID: 848

  Severity: ERROR\
  Message: The Directory Server could not register a JMX MBean for the component associated with configuration entry %s: %s.

* []()ID: 849

  Severity: ERROR\
  Message: An unexpected error occurred while trying to export the Directory Server configuration to LDIF: %s.

* []()ID: 851

  Severity: ERROR\
  Message: An unexpected error occurred while trying to register the configuration handler base DN "%s" as a private suffix with the Directory Server: %s.

* []()ID: 852

  Severity: ERROR\
  Message: The entry cn=Backends,cn=config does not appear to exist in the Directory Server configuration. This is a required entry.

* []()ID: 853

  Severity: INFO\
  Message: The backend defined in configuration entry %s is marked as disabled and therefore will not be used.

* []()ID: 854

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to determine whether the backend associated with configuration entry %s should be enabled or disabled: %s. It will be disabled.

* []()ID: 855

  Severity: ERROR\
  Message: The Directory Server was unable to load class %s and use it to create a backend instance as defined in configuration entry %s. The error that occurred was: %s. This backend will be disabled.

* []()ID: 856

  Severity: ERROR\
  Message: An error occurred while trying to initialize a backend loaded from class %s with the information in configuration entry %s: %s. This backend will be disabled.

* []()ID: 857

  Severity: NOTICE\
  Message: The requested change to configuration entry %s would cause the class for the associated backend to change from %s to %s. This change will not take effect until the backend is disabled and re-enabled, or until the Directory Server is restarted.

* []()ID: 858

  Severity: ERROR\
  Message: An error occurred while trying to initialize a connection handler loaded from class %s with the information in configuration entry %s: %s. This connection handler will be disabled.

* []()ID: 859

  Severity: ERROR\
  Message: Unable to read the Directory Server schema definitions because the schema directory %s does not exist.

* []()ID: 860

  Severity: ERROR\
  Message: Unable to read the Directory Server schema definitions because the schema directory %s exists but is not a directory.

* []()ID: 861

  Severity: ERROR\
  Message: Unable to read the Directory Server schema definitions from directory %s because an unexpected error occurred while trying to list the files in that directory: %s.

* []()ID: 862

  Severity: WARNING\
  Message: Schema configuration file %s in directory %s cannot be parsed because an unexpected error occurred while trying to open the file for reading: %s.

* []()ID: 863

  Severity: WARNING\
  Message: Schema configuration file %s in directory %s cannot be parsed because an unexpected error occurred while trying to read its contents as an LDIF entry: %s.

* []()ID: 864

  Severity: ERROR\
  Message: An unexpected error occurred that prevented the server from installing its default entry cache framework: %s.

* []()ID: 865

  Severity: WARNING\
  Message: The entry cache configuration entry "cn=Entry Caches,cn=config" does not exist in the Directory Server configuration. No entry cache will be available until this entry is created with a valid entry cache configuration.

* []()ID: 866

  Severity: ERROR\
  Message: An error occurred while attempting to initialize an instance of class %s for use as the Directory Server entry cache: %s. As a result, the entry cache will be disabled.

* []()ID: 867

  Severity: ERROR\
  Message: The configuration for the entry cache defined in configuration entry %s was not acceptable: %s.

* []()ID: 868

  Severity: ERROR\
  Message: The configuration for the entry cache defined in configuration entry %s was not acceptable: the entry cache level %d is already in use.

* []()ID: 869

  Severity: ERROR\
  Message: An error occurred while attempting to initialize an instance of class %s as a Directory Server plugin using the information in configuration entry %s: %s. This plugin will be disabled.

* []()ID: 870

  Severity: ERROR\
  Message: Class %s specified in configuration entry %s does not contain a valid extended operation handler implementation: %s.

* []()ID: 871

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as an extended operation handler as defined in configuration entry %s: %s.

* []()ID: 872

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as a SASL mechanism handler as defined in configuration entry %s: %s.

* []()ID: 873

  Severity: ERROR\
  Message: Entry %s cannot be removed from the Directory Server configuration because that DN does not have a parent.

* []()ID: 874

  Severity: ERROR\
  Message: Entry %s cannot be added to the Directory Server configuration because another configuration entry already exists with that DN.

* []()ID: 875

  Severity: ERROR\
  Message: Entry %s cannot be added to the Directory Server configuration because that DN does not have a parent.

* []()ID: 876

  Severity: ERROR\
  Message: Entry %s cannot be added to the Directory Server configuration because its parent entry %s does not exist.

* []()ID: 877

  Severity: ERROR\
  Message: The Directory Server is unwilling to add configuration entry %s because one of the add listeners registered with the parent entry %s rejected this change with the message: %s.

* []()ID: 878

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to add configuration entry %s as a child of entry %s: %s.

* []()ID: 879

  Severity: ERROR\
  Message: Entry %s cannot be removed from the Directory Server configuration because the specified entry does not exist.

* []()ID: 880

  Severity: ERROR\
  Message: Entry %s cannot be removed from the Directory Server configuration because the specified entry has one or more subordinate entries.

* []()ID: 881

  Severity: ERROR\
  Message: Entry %s cannot be removed from the Directory Server configuration because the entry does not have a parent and removing the configuration root entry is not allowed.

* []()ID: 882

  Severity: ERROR\
  Message: Entry %s cannot be removed from the Directory Server configuration because one of the delete listeners registered with the parent entry %s rejected this change with the message: %s.

* []()ID: 883

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to remove configuration entry %s as a child of entry %s: %s.

* []()ID: 884

  Severity: ERROR\
  Message: Entry %s cannot be modified because the specified entry does not exist.

* []()ID: 885

  Severity: ERROR\
  Message: Entry %s cannot be modified because one of the configuration change listeners registered for that entry rejected the change: %s.

* []()ID: 886

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to modify configuration entry %s as a child of entry %s: %s.

* []()ID: 887

  Severity: ERROR\
  Message: An error occurred while attempting to export the new Directory Server configuration to file %s: %s.

* []()ID: 888

  Severity: ERROR\
  Message: An error occurred while attempting to rename the new Directory Server configuration from file %s to %s: %s.

* []()ID: 889

  Severity: ERROR\
  Message: Modify DN operations are not allowed in the Directory Server configuration.

* []()ID: 890

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as a password storage scheme as defined in configuration entry %s: %s.

* []()ID: 891

  Severity: ERROR\
  Message: Unable to add a new password storage scheme entry with DN %s because there is already a storage scheme registered with that DN.

* []()ID: 892

  Severity: WARNING\
  Message: The backend defined in configuration entry %s has a backend ID of %s that conflicts with the backend ID for another backend in the server. The backend will be disabled.

* []()ID: 893

  Severity: ERROR\
  Message: The Directory Server was unable to acquire a shared lock for backend %s: %s. This generally means that the backend is in use by a process that requires an exclusive lock (e.g., importing from LDIF or restoring a backup). This backend will be disabled.

* []()ID: 894

  Severity: WARNING\
  Message: An error occurred while attempting to release a shared lock for backend %s: %s. This may interfere with operations that require exclusive access, including LDIF import and restoring a backup.

* []()ID: 895

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as an identity mapper as defined in configuration entry %s: %s.

* []()ID: 896

  Severity: ERROR\
  Message: An error occurred while attempting to instantiate class %s referenced in synchronization provider configuration entry %s: %s.

* []()ID: 897

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the Directory Server synchronization provider referenced in configuration entry %s: %s.

* []()ID: 898

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as a password validator as defined in configuration entry %s: %s.

* []()ID: 899

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as a password generator as defined in configuration entry %s: %s.

* []()ID: 900

  Severity: ERROR\
  Message: No password policies have been defined below the cn=Password Policies,cn=config entry in the Directory Server configuration. At least one password policy configuration must be defined.

* []()ID: 901

  Severity: ERROR\
  Message: The password policy defined in configuration entry %s is invalid: %s.

* []()ID: 902

  Severity: ERROR\
  Message: The Directory Server default password policy is defined as %s, but that entry does not exist or is not below the password policy configuration base cn=Password Policies,cn=config.

* []()ID: 903

  Severity: WARNING\
  Message: The specified entry %s is currently defined as the configuration entry for the default password policy. The default password policy configuration entry may not be removed.

* []()ID: 904

  Severity: INFO\
  Message: Password policy entry %s has been removed from the Directory Server configuration. Any user entries that explicitly reference this password policy will no longer be allowed to authenticate.

* []()ID: 905

  Severity: WARNING\
  Message: Access control has been disabled.

* []()ID: 906

  Severity: NOTICE\
  Message: Access control has been enabled and will use the %s implementation.

* []()ID: 907

  Severity: ERROR\
  Message: An error occurred while attempting to instantiate class %s referenced in the access control configuration entry %s: %s.

* []()ID: 908

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as an account status notification handler as defined in configuration entry %s: %s.

* []()ID: 909

  Severity: ERROR\
  Message: Unable to add a new account status notification handler entry with DN %s because there is already a notification handler registered with that DN.

* []()ID: 910

  Severity: ERROR\
  Message: An error occurred while attempting to apply the changes contained in file %s to the server configuration at startup: %s.

* []()ID: 911

  Severity: ERROR\
  Message: One or more errors occurred while applying changes on server startup: %s.

* []()ID: 912

  Severity: ERROR\
  Message: Configuration entry %s does not contain a valid value for configuration attribute ds-cfg-db-directory-permissions (It should be an UNIX permission mode in three-digit octal notation.).

* []()ID: 913

  Severity: ERROR\
  Message: Invalid UNIX file permissions %s does not allow read and write access to the backend database directory by the backend.

* []()ID: 914

  Severity: ERROR\
  Message: No default password policy is configured for the Directory Server. The default password policy must be specified by the ds-cfg-default-password-policy attribute in the cn=config entry.

* []()ID: 915

  Severity: WARNING\
  Message: An error occurred while attempting to register backend %s with the Directory Server: %s.

* []()ID: 916

  Severity: ERROR\
  Message: An error occurred while trying to create the configuration archive directory %s: %s.

* []()ID: 917

  Severity: ERROR\
  Message: An error occurred while trying to write the current configuration to the configuration archive: %s.

* []()ID: 918

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform add operations in the Directory Server configuration.

* []()ID: 919

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform delete operations in the Directory Server configuration.

* []()ID: 920

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform modify operations in the Directory Server configuration.

* []()ID: 921

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform modify DN operations in the Directory Server configuration.

* []()ID: 922

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform search operations in the Directory Server configuration.

* []()ID: 923

  Severity: ERROR\
  Message: You do not have sufficient privileges to change the set of default root privileges.

* []()ID: 924

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as a certificate mapper as defined in configuration entry %s: %s.

* []()ID: 925

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as a key manager provider as defined in configuration entry %s: %s.

* []()ID: 926

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as a trust manager provider as defined in configuration entry %s: %s.

* []()ID: 928

  Severity: ERROR\
  Message: %s.%s returned a result of null for entry %s.

* []()ID: 929

  Severity: ERROR\
  Message: %s.%s failed for entry %s: result code=%s, admin action required=%b, messages="%s".

* []()ID: 930

  Severity: WARNING\
  Message: %s.%s indicated that administrative action is required for entry %s: messages="%s".

* []()ID: 931

  Severity: INFO\
  Message: %s.%s succeeded but generated the following messages for entry %s: %s.

* []()ID: 932

  Severity: ERROR\
  Message: Unable to parse value "%s" from config entry "%s" as a valid search filter: %s.

* []()ID: 933

  Severity: ERROR\
  Message: An error occurred while trying to load an instance of class %s referenced in configuration entry %s as a virtual attribute provider: %s.

* []()ID: 934

  Severity: ERROR\
  Message: The virtual attribute configuration in entry "%s" is not valid because attribute type %s is single-valued but provider %s may generate multiple values.

* []()ID: 935

  Severity: ERROR\
  Message: The virtual attribute configuration in entry "%s" is not valid because attribute type %s is single-valued but the conflict behavior is configured to merge real and virtual values.

* []()ID: 936

  Severity: ERROR\
  Message: Configuration entry %s cannot be modified because the change would alter its structural object class.

* []()ID: 937

  Severity: ERROR\
  Message: An error occurred while attempting to calculate a SHA-1 digest of file %s: %s.

* []()ID: 938

  Severity: WARNING\
  Message: The Directory Server has detected that one or more external changes have been made to the configuration file %s while the server was online, but another change has caused the server configuration to be overwritten. The manual changes have not been applied, but they have been preserved in file %s.

* []()ID: 939

  Severity: ERROR\
  Message: The Directory Server encountered an error while attempting to determine whether the configuration file %s has been externally edited with the server online, and/or trying to preserve such changes: %s. Any manual changes made to that file may have been lost.

* []()ID: 940

  Severity: ERROR\
  Message: Class %s specified in attribute ds-cfg-java-class of configuration entry %s cannot be instantiated as a Directory Server log rotation policy: %s.

* []()ID: 941

  Severity: ERROR\
  Message: Class %s specified in attribute ds-cfg-java-class of configuration entry %s cannot be instantiated as a Directory Server log retention policy: %s.

* []()ID: 942

  Severity: ERROR\
  Message: An error occurred while attempting to create a Directory Server log rotation policy from the information in configuration entry %s: %s.

* []()ID: 943

  Severity: ERROR\
  Message: An error occurred while attempting to create a Directory Server log retention policy from the information in configuration entry %s: %s.

* []()ID: 944

  Severity: ERROR\
  Message: An error occurred while attempting to create a text writer for a Directory Server logger from the information in configuration entry %s: %s.

* []()ID: 945

  Severity: WARNING\
  Message: Schema configuration file %s in directory %s contains more than one entry. Only the first entry will be examined, and the additional entries will be ignored.

* []()ID: 946

  Severity: WARNING\
  Message: The plugin order definition for plugins of type %s contains an empty element. This may cause the plugin order to be evaluated incorrectly.

* []()ID: 947

  Severity: WARNING\
  Message: The plugin order definition for plugins of type %s contains multiple wildcard characters. All plugin definitions should contain exactly one wildcard element to indicate where unmatched plugins should be included in the order, and including multiple wildcards may cause the plugin order to be evaluated incorrectly.

* []()ID: 948

  Severity: WARNING\
  Message: The plugin order definition for plugins of type %s includes multiple references to the '%s' plugin. This may cause the plugin order to be evaluated incorrectly.

* []()ID: 949

  Severity: WARNING\
  Message: The plugin order definition for plugins of type %s does not include a wildcard element to indicate where unmatched plugins should be included in the order. The server will default to invoking all unnamed plugins after set of named plugins.

* []()ID: 950

  Severity: ERROR\
  Message: Unable to initialize an instance of class %s as a work queue as specified in configuration entry %s: %s.

* []()ID: 951

  Severity: INFO\
  Message: The class used to provide the Directory Server work queue implementation has been changed from %s to %s, but this change will not take effect until the server is restarted.

* []()ID: 952

  Severity: ERROR\
  Message: The attempt to apply the configuration add failed. The preliminary checks were all successful and the entry was added to the server configuration, but at least one of the configuration add listeners reported an error when attempting to apply the change: %s.

* []()ID: 953

  Severity: ERROR\
  Message: The attempt to apply the configuration delete failed. The preliminary checks were all successful and the entry was removed from the server configuration, but at least one of the configuration delete listeners reported an error when attempting to apply the change: %s.

* []()ID: 954

  Severity: ERROR\
  Message: The attempt to apply the configuration modification failed. The preliminary checks were all successful and the modified entry was written to the server configuration, but at least one of the configuration change listeners reported an error when attempting to apply the change: %s.

* []()ID: 955

  Severity: ERROR\
  Message: The configuration for the key manager provider defined in configuration entry %s was not acceptable: %s.

* []()ID: 956

  Severity: ERROR\
  Message: The configuration for the trust manager provider defined in configuration entry %s was not acceptable: %s.

* []()ID: 957

  Severity: ERROR\
  Message: The configuration for the trust manager provider defined in configuration entry %s was not acceptable: %s.

* []()ID: 958

  Severity: ERROR\
  Message: The configuration for the account status notification handler defined in configuration entry %s was not acceptable: %s.

* []()ID: 959

  Severity: ERROR\
  Message: The configuration for the certificate mapper defined in configuration entry %s was not acceptable: %s.

* []()ID: 960

  Severity: ERROR\
  Message: The configuration for the identity mapper defined in configuration entry %s was not acceptable: %s.

* []()ID: 961

  Severity: ERROR\
  Message: The configuration for the password generator defined in configuration entry %s was not acceptable: %s.

* []()ID: 962

  Severity: ERROR\
  Message: The configuration for the password storage scheme defined in configuration entry %s was not acceptable: %s.

* []()ID: 963

  Severity: ERROR\
  Message: The configuration for the password validator defined in configuration entry %s was not acceptable: %s.

* []()ID: 964

  Severity: ERROR\
  Message: The configuration for the plugin defined in configuration entry %s was not acceptable: %s.

* []()ID: 965

  Severity: ERROR\
  Message: The configuration for the SASL mechanism handler defined in configuration entry %s was not acceptable: %s.

* []()ID: 966

  Severity: ERROR\
  Message: The configuration for the virtual attribute provider defined in configuration entry %s was not acceptable: %s.

* []()ID: 967

  Severity: ERROR\
  Message: The configuration for the alert handler defined in configuration entry %s was not acceptable: %s.

* []()ID: 968

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as an alert handler as defined in configuration entry %s: %s.

* []()ID: 969

  Severity: ERROR\
  Message: An error occurred while attempting to open the current configuration file %s for reading in order to copy it to the ".startok" file: %s.

* []()ID: 970

  Severity: ERROR\
  Message: An error occurred while attempting to copy the current configuration from file %s into temporary file %s for use as the ".startok" configuration file: %s.

* []()ID: 971

  Severity: ERROR\
  Message: An error occurred while attempting to rename file %s to %s for use as the ".startok" configuration file: %s.

* []()ID: 972

  Severity: NOTICE\
  Message: The Directory Server is starting using the last known good configuration file %s rather than the active configuration file %s.

* []()ID: 973

  Severity: WARNING\
  Message: No last known good configuration file %s exists. The server will attempt to start using the active configuration file %s.

* []()ID: 974

  Severity: ERROR\
  Message: An error occurred while trying to parse and validate Berkeley DB JE property %s: %s.

* []()ID: 975

  Severity: ERROR\
  Message: An error occurred while trying to parse and validate Berkeley DB JE property %s: the property does not follow a singular property=value form.

* []()ID: 976

  Severity: ERROR\
  Message: An error occurred while trying to parse and validate Berkeley DB JE property %s: the property shadows configuration attribute %s.

* []()ID: 977

  Severity: ERROR\
  Message: An error occurred while trying to parse and validate Berkeley DB JE property %s: the property is already defined for this component.

* []()ID: 978

  Severity: ERROR\
  Message: An error occurred while attempting to open the configured log file %s for logger %s: %s.

* []()ID: 979

  Severity: ERROR\
  Message: Invalid UNIX file permissions %s does not allow write access to the log file by the log publisher.

* []()ID: 980

  Severity: ERROR\
  Message: Invalid UNIX file permissions %s: %s.

* []()ID: 981

  Severity: ERROR\
  Message: The configuration entry '%s' is currently defined to be the default password policy, however it is not a password policy.

* []()ID: 982

  Severity: ERROR\
  Message: The default password policy value '%s' is invalid because it refers to an authentication policy which is not a password policy.

* []()ID: 983

  Severity: ERROR\
  Message: The timestamp format string "%s" is not a valid format string. The format string should conform to the syntax described in the documentation for the "java.text.SimpleDateFormat" class.

* []()ID: 984

  Severity: ERROR\
  Message: The access log filtering criteria defined in "%s" could not be parsed because it contains an invalid user DN pattern "%s".

* []()ID: 985

  Severity: ERROR\
  Message: The access log filtering criteria defined in "%s" could not be parsed because it contains an invalid target DN pattern "%s".

* []()ID: 986

  Severity: WARNING\
  Message: There are no active HTTP access loggers defined in the Directory Server configuration. No HTTP access logging will be performed.

* []()ID: 987

  Severity: ERROR\
  Message: Class %s specified in attribute ds-cfg-java-class of configuration entry %s cannot be instantiated as a Directory Server HTTP access logger: %s.

* []()ID: 988

  Severity: WARNING\
  Message: The log format for %s contains the following unsupported fields: %s. Their output will be replaced with a dash ("-") character.

* []()ID: 989

  Severity: ERROR\
  Message: An error occurred while attempting to update a Directory Server logger from the information in configuration entry %s: %s.

* []()ID: 990

  Severity: ERROR\
  Message: Cannot configure java.util.logging root logger level: %s. java.util.logging support is now disabled.

* []()ID: 991

  Severity: ERROR\
  Message: An error occurred while trying to initialize an instance of class %s as an HTTP endpoint as defined in configuration entry %s: %s.

* []()ID: 992

  Severity: ERROR\
  Message: An error occurred while starting the HTTP endpoint as defined in configuration entry %s: %s.

* []()ID: 993

  Severity: ERROR\
  Message: The HTTP endpoint configuration defined in %s is invalid: %s.

* []()ID: 994

  Severity: ERROR\
  Message: Cannot initialize the configuration framework: %s.

* []()ID: 995

  Severity: ERROR\
  Message: Unable to retrieve children of configuration entry with dn: %s.

* []()ID: 996

  Severity: ERROR\
  Message: Unable to load the configuration-enabled schema: %s.

* []()ID: 997

  Severity: ERROR\
  Message: Backend config error when trying to delete an entry: %s.

* []()ID: 998

  Severity: ERROR\
  Message: The HTTP endpoint configuration defined in %s is referencing a non existing authorization DN %s.

* []()ID: 999

  Severity: ERROR\
  Message: The HTTP endpoint configuration defined in %s is referencing mutually exclusive authorization DNs %s and %s.

## IDs: 1001-1500

* []()ID: 1003

  Severity: ERROR\
  Message: The OAuth2 authorization mechanism defined in %s contains an invalid JSON Pointer %s: %s.

* []()ID: 1004

  Severity: ERROR\
  Message: The authorization mechanism defined in %s is referencing a non-existing or non-readable directory: %s.

* []()ID: 1005

  Severity: ERROR\
  Message: The authorization mechanism defined in %s is referencing a non existing DN: %s.

* []()ID: 1006

  Severity: ERROR\
  Message: The authorization mechanism defined in %s is referencing an invalid URL %s: %s.

* []()ID: 1007

  Severity: ERROR\
  Message: Unable to configure the authorization mechanism defined in %s: %s.

* []()ID: 1008

  Severity: ERROR\
  Message: The requested admin API version '%s' is unsupported. This endpoint only supports the following admin API version(s): %s.

* []()ID: 1009

  Severity: ERROR\
  Message: The configuration of schema provider '%s' is not acceptable for the following reasons: %s.

* []()ID: 1010

  Severity: ERROR\
  Message: The schema provider class '%s' could not be instantiated or initialized with the configuration '%s' : %s.

* []()ID: 1011

  Severity: ERROR\
  Message: The core schema provider defined by '%s' has been disabled. The core schema must always be enabled.

* []()ID: 1012

  Severity: WARNING\
  Message: The config schema file '%s' generated warning when trying to update schema with its content: %s.

* []()ID: 1013

  Severity: WARNING\
  Message: The config schema file '%s' generated warning when trying to update schema with its content, despite allowing to overwrite definitions: %s.

* []()ID: 1014

  Severity: ERROR\
  Message: Unable to configure the backend '%s' because one of its base DNs is the empty DN.

* []()ID: 1015

  Severity: ERROR\
  Message: Cannot configure new SSL protocols because the following protocols are not supported: %s. Look for supported protocols in 'cn=jvm,cn=monitor'.

* []()ID: 1016

  Severity: ERROR\
  Message: Cannot configure new SSL cipher suites because the following cipher suites are not supported: %s. Look for supported cipher suites in 'cn=jvm,cn=monitor'.

* []()ID: 1017

  Severity: ERROR\
  Message: The metric name pattern to exclude '%s' cannot be parsed as a valid regular expression due to the following error: '%s'.

* []()ID: 1018

  Severity: ERROR\
  Message: The metric name pattern to include '%s' cannot be parsed as a valid regular expression due to the following error: '%s'.

* []()ID: 1019

  Severity: ERROR\
  Message: The list of keys defined for the JSON matching rule contains an invalid JSON pointer : %s.

* []()ID: 1020

  Severity: ERROR\
  Message: Cannot create the property resolver due to the following error: '%s'.

* []()ID: 1021

  Severity: ERROR\
  Message: Error creating SSL socket factory: %s.

* []()ID: 1022

  Severity: ERROR\
  Message: The smtp-server value '%s' is invalid: %s.

* []()ID: 1023

  Severity: ERROR\
  Message: Unable to resolve the host for the listen address '%s' of the LDAP connection handler %s.

* []()ID: 1024

  Severity: WARNING\
  Message: The latest archived configuration file %s appears to be invalid. Forcing creation of a new one.

* []()ID: 1025

  Severity: WARNING\
  Message: '%s' is DEPRECATED for removal since %s. Its usage is highly discouraged.

* []()ID: 1026

  Severity: WARNING\
  Message: '%s' is LEGACY since %s. Its usage is highly discouraged.

* []()ID: 1027

  Severity: ERROR\
  Message: Abandon requests cannot be canceled.

* []()ID: 1028

  Severity: ERROR\
  Message: Bind requests cannot be canceled.

* []()ID: 1029

  Severity: ERROR\
  Message: Unbind requests cannot be canceled.

* []()ID: 1030

  Severity: INFO\
  Message: Client Unbind.

* []()ID: 1031

  Severity: INFO\
  Message: Client Disconnect.

* []()ID: 1032

  Severity: INFO\
  Message: Client Connection Rejected.

* []()ID: 1034

  Severity: INFO\
  Message: Protocol Error.

* []()ID: 1035

  Severity: INFO\
  Message: Server Shutdown.

* []()ID: 1036

  Severity: INFO\
  Message: Administrative Termination.

* []()ID: 1039

  Severity: INFO\
  Message: Administrative Limit Exceeded.

* []()ID: 1040

  Severity: INFO\
  Message: Idle Time Limit Exceeded.

* []()ID: 1041

  Severity: INFO\
  Message: I/O Timeout.

* []()ID: 1042

  Severity: INFO\
  Message: Connection Closed by Plugin.

* []()ID: 1043

  Severity: INFO\
  Message: Unknown Closure Reason.

* []()ID: 1044

  Severity: INFO\
  Message: Operations Error.

* []()ID: 1047

  Severity: ERROR\
  Message: %s encountered an uncaught exception while processing operation %s: %s.

* []()ID: 1053

  Severity: INFO\
  Message: Server Error.

* []()ID: 1054

  Severity: ERROR\
  Message: The Directory Server is currently running. The configuration may not be bootstrapped while the server is online.

* []()ID: 1055

  Severity: ERROR\
  Message: The Directory Server may not be started before the configuration has been bootstrapped.

* []()ID: 1056

  Severity: ERROR\
  Message: The Directory Server may not be started while it is already running. Please stop the running instance before attempting to start it again.

* []()ID: 1057

  Severity: INFO\
  Message: The Directory Server is beginning the configuration bootstrapping process.

* []()ID: 1058

  Severity: NOTICE\
  Message: %s (build %s, revision number %s) starting up.

* []()ID: 1059

  Severity: NOTICE\
  Message: The Directory Server has started successfully.

* []()ID: 1060

  Severity: ERROR\
  Message: An error occurred while attempting to create the JMX MBean server that will be used for monitoring, notification, and configuration interaction within the Directory Server: %s.

* []()ID: 1061

  Severity: NOTICE\
  Message: The Directory Server has sent an alert notification generated by class %s (alert type %s, alert ID %s): %s.

* []()ID: 1062

  Severity: ERROR\
  Message: An uncaught exception during processing for thread "%s" has caused it to terminate abnormally. The stack trace for that exception is: %s.

* []()ID: 1063

  Severity: NOTICE\
  Message: The Directory Server has started the shutdown process. The shutdown was initiated by an instance of class %s and the reason provided for the shutdown was %s.

* []()ID: 1064

  Severity: ERROR\
  Message: The Directory Server shutdown hook detected that the JVM is shutting down. This generally indicates that JVM received an external request to stop (e.g., through a kill signal).

* []()ID: 1065

  Severity: ERROR\
  Message: An error occurred while trying to retrieve the root DSE configuration entry (cn=Root DSE,cn=config) from the Directory Server configuration: %s.

* []()ID: 1066

  Severity: WARNING\
  Message: Entry "%1$s" contains a value "%3$s" for attribute %2$s that is invalid according to the syntax for that attribute: %4$s.

* []()ID: 1067

  Severity: WARNING\
  Message: Entry "%s" does not contain any values for attribute "%s".

* []()ID: 1068

  Severity: WARNING\
  Message: Entry "%s" does not contain any values for attribute "%s" with the specified set of options.

* []()ID: 1069

  Severity: NOTICE\
  Message: The Directory Server is now stopped.

* []()ID: 1071

  Severity: INFO\
  Message: Processing on this operation has been canceled because the Directory Server received a bind request on this connection, which requires that all operations in progress to be abandoned.

* []()ID: 1072

  Severity: ERROR\
  Message: Unable to bind to the Directory Server because no such user exists in the server.

* []()ID: 1074

  Severity: ERROR\
  Message: Unable to bind to the Directory Server using simple authentication because that user does not have a password.

* []()ID: 1075

  Severity: ERROR\
  Message: Unable to process the bind request because it attempted to use an unknown SASL mechanism %s that is not available in the Directory Server.

* []()ID: 1076

  Severity: ERROR\
  Message: The specified entry %s does not exist in the Directory Server.

* []()ID: 1077

  Severity: INFO\
  Message: The operation was canceled because the client issued an abandon request (message ID %d) for this operation.

* []()ID: 1078

  Severity: ERROR\
  Message: The provided entry cannot be added because it contains a null DN. This DN is reserved for the root DSE, and that entry may not be added over protocol.

* []()ID: 1079

  Severity: ERROR\
  Message: The provided entry %s cannot be added because it does not have a parent and is not defined as one of the suffixes within the Directory Server.

* []()ID: 1080

  Severity: ERROR\
  Message: Entry %s cannot be added because its parent entry %s does not exist in the server.

* []()ID: 1081

  Severity: ERROR\
  Message: Entry %s cannot be added because the server failed to obtain a write lock for this entry after multiple attempts.

* []()ID: 1082

  Severity: ERROR\
  Message: Entry %s cannot be removed because the server failed to obtain a write lock for this entry after multiple attempts.

* []()ID: 1083

  Severity: ERROR\
  Message: The maximum time limit of %d seconds for processing this search operation has expired.

* []()ID: 1084

  Severity: ERROR\
  Message: This search operation has sent the maximum of %d entries to the client.

* []()ID: 1085

  Severity: ERROR\
  Message: The entry %s specified as the search base does not exist in the Directory Server.

* []()ID: 1086

  Severity: ERROR\
  Message: Entry %s does not exist in the Directory Server.

* []()ID: 1087

  Severity: ERROR\
  Message: Entry %s cannot be removed because the backend that should contain that entry has a subordinate backend with a base DN of %s that is below the target DN.

* []()ID: 1088

  Severity: ERROR\
  Message: A modify DN operation cannot be performed on entry %s because the new RDN would not have a parent DN.

* []()ID: 1090

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because no backend is registered to handle the new DN %s.

* []()ID: 1091

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because the backend holding the current entry is different from the backend used to handle the new DN %s. Modify DN operations may not span multiple backends.

* []()ID: 1092

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because the server was unable to obtain a write lock for that DN.

* []()ID: 1093

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because the server was unable to obtain a write lock for the new DN %s.

* []()ID: 1094

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because that entry does not exist in the server.

* []()ID: 1095

  Severity: ERROR\
  Message: Entry %s cannot be modified because the server failed to obtain a write lock for this entry after multiple attempts.

* []()ID: 1096

  Severity: ERROR\
  Message: Entry %s cannot be modified because no such entry exists in the server.

* []()ID: 1097

  Severity: ERROR\
  Message: Entry %s cannot be modified because the modification contained an add component for attribute %s but no values were provided.

* []()ID: 1098

  Severity: ERROR\
  Message: When attempting to modify entry %1$s to add one or more values for attribute %2$s, value "%3$s" was found to be invalid according to the associated syntax: %4$s.

* []()ID: 1099

  Severity: ERROR\
  Message: Entry %s cannot be modified because it would have resulted in one or more duplicate values for attribute %s: %s.

* []()ID: 1100

  Severity: ERROR\
  Message: Entry %s cannot be modified because the change to attribute %s would have removed a value used in the RDN.

* []()ID: 1101

  Severity: ERROR\
  Message: Entry %s cannot be modified because the attempt to update attribute %s would have removed one or more values from the attribute that were not present: %s.

* []()ID: 1102

  Severity: ERROR\
  Message: Entry %s cannot be modified because an attempt was made to remove one or more values from attribute %s but this attribute is not present in the entry.

* []()ID: 1103

  Severity: ERROR\
  Message: When attempting to modify entry %1$s to replace the set of values for attribute %2$s, value "%3$s" was found to be invalid according to the associated syntax: %4$s.

* []()ID: 1104

  Severity: ERROR\
  Message: Entry %s cannot be modified because an attempt was made to increment the value of attribute %s which is used as an RDN attribute for the entry.

* []()ID: 1105

  Severity: ERROR\
  Message: Entry %s cannot be modified because an attempt was made to increment the value of attribute %s but the request did not include a value for that attribute specifying the amount by which to increment the value.

* []()ID: 1106

  Severity: ERROR\
  Message: Entry %s cannot be modified because an attempt was made to increment the value of attribute %s but the request contained multiple values, where only a single integer value is allowed.

* []()ID: 1107

  Severity: ERROR\
  Message: Entry %s cannot be modified because an attempt was made to increment the value of attribute %s but that attribute did not have any values in the target entry.

* []()ID: 1108

  Severity: ERROR\
  Message: Entry %s cannot be modified because an attempt was made to increment the value of attribute %s but the value "%s" could not be parsed as an integer.

* []()ID: 1109

  Severity: ERROR\
  Message: Entry %s cannot be modified because the resulting entry would have violated the server schema: %s.

* []()ID: 1110

  Severity: ERROR\
  Message: There is no extended operation handler registered with the Directory Server for handling extended operations with a request OID of %s.

* []()ID: 1112

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because the change would have violated the server schema: %s.

* []()ID: 1113

  Severity: ERROR\
  Message: Object class %s cannot be added to entry %s because that class is not defined in the Directory Server schema.

* []()ID: 1114

  Severity: ERROR\
  Message: The password provided by the user did not match any password(s) stored in the user's entry.

* []()ID: 1115

  Severity: INFO\
  Message: Display general system information.

* []()ID: 1116

  Severity: ERROR\
  Message: An error occurred while attempting to parse the provided set of command line arguments: %s.

* []()ID: 1117

  Severity: ERROR\
  Message: An error occurred while attempting to bootstrap the Directory Server: %s.

* []()ID: 1118

  Severity: ERROR\
  Message: An error occurred while trying to start the Directory Server: %s.

* []()ID: 1119

  Severity: ERROR\
  Message: The attempt to obtain a shared lock on file %s was rejected because an exclusive lock was already held on that file.

* []()ID: 1120

  Severity: ERROR\
  Message: The attempt to obtain a shared lock on file %s was rejected because the attempt to create the lock file failed: %s.

* []()ID: 1121

  Severity: ERROR\
  Message: The attempt to obtain a shared lock on file %s was rejected because the attempt to open the lock file failed: %s.

* []()ID: 1122

  Severity: ERROR\
  Message: The attempt to obtain a shared lock on file %s was rejected because an error occurred while attempting to acquire the lock: %s.

* []()ID: 1123

  Severity: ERROR\
  Message: The shared lock requested for file %s was not granted, which indicates that another process already holds an exclusive lock on that file.

* []()ID: 1124

  Severity: ERROR\
  Message: The attempt to obtain an exclusive lock on file %s was rejected because an exclusive lock was already held on that file.

* []()ID: 1125

  Severity: ERROR\
  Message: The attempt to obtain an exclusive lock on file %s was rejected because a shared lock was already held on that file.

* []()ID: 1126

  Severity: ERROR\
  Message: The attempt to obtain an exclusive lock on file %s was rejected because the attempt to create the lock file failed: %s.

* []()ID: 1127

  Severity: ERROR\
  Message: The attempt to obtain an exclusive lock on file %s was rejected because the attempt to open the lock file failed: %s.

* []()ID: 1128

  Severity: ERROR\
  Message: The attempt to obtain an exclusive lock on file %s was rejected because an error occurred while attempting to acquire the lock: %s.

* []()ID: 1129

  Severity: ERROR\
  Message: The exclusive lock requested for file %s was not granted, which indicates that another process already holds a shared or exclusive lock on that file.

* []()ID: 1130

  Severity: ERROR\
  Message: The attempt to release the exclusive lock held on %s failed: %s.

* []()ID: 1131

  Severity: ERROR\
  Message: The attempt to release the shared lock held on %s failed: %s.

* []()ID: 1132

  Severity: ERROR\
  Message: The attempt to release the lock held on %s failed because no record of a lock on that file was found.

* []()ID: 1133

  Severity: WARNING\
  Message: An error occurred while attempting to release a shared lock for backend %s: %s. This lock should be automatically cleaned when the Directory Server process exits, so no additional action should be necessary.

* []()ID: 1134

  Severity: ERROR\
  Message: The Directory Server could not acquire an exclusive lock on file %s: %s. This generally means that another instance of this server is already running.

* []()ID: 1135

  Severity: ERROR\
  Message: Entry %s cannot be modified because the modification attempted to update attribute %s which is defined as NO-USER-MODIFICATION in the server schema.

* []()ID: 1136

  Severity: ERROR\
  Message: Entry %s cannot be added because it includes attribute %s which is defined as NO-USER-MODIFICATION in the server schema.

* []()ID: 1137

  Severity: ERROR\
  Message: Entry %s cannot be renamed because the current DN includes attribute %s which is defined as NO-USER-MODIFICATION in the server schema and the deleteOldRDN flag was set in the modify DN request.

* []()ID: 1138

  Severity: ERROR\
  Message: Entry %s cannot be renamed because the new RDN includes attribute %s which is defined as NO-USER-MODIFICATION in the server schema, and the target value for that attribute is not already included in the entry.

* []()ID: 1139

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because a pre-operation plugin modified the entry in a way that caused it to violate the server schema: %s.

* []()ID: 1140

  Severity: ERROR\
  Message: Entry %s cannot be modified because the request contained an LDAP assertion control and the associated filter did not match the contents of the entry.

* []()ID: 1141

  Severity: ERROR\
  Message: Entry %s cannot be modified because the request contained a critical control with OID %s that is not supported by the Directory Server for this type of operation.

* []()ID: 1142

  Severity: ERROR\
  Message: Entry %s cannot be removed because the request contained an LDAP assertion control and the associated filter did not match the contents of the entry.

* []()ID: 1143

  Severity: ERROR\
  Message: Entry %s cannot be removed because the request contained a critical control with OID %s that is not supported by the Directory Server for this type of operation.

* []()ID: 1144

  Severity: ERROR\
  Message: Entry %s cannot be renamed because the request contained an LDAP assertion control and the associated filter did not match the contents of the entry.

* []()ID: 1145

  Severity: ERROR\
  Message: Entry %s cannot be renamed because the request contained a critical control with OID %s that is not supported by the Directory Server for this type of operation.

* []()ID: 1146

  Severity: ERROR\
  Message: Entry %s cannot be added because the request contained an LDAP assertion control and the associated filter did not match the contents of the provided entry.

* []()ID: 1147

  Severity: ERROR\
  Message: Entry %s cannot be added because the request contained a critical control with OID %s that is not supported by the Directory Server for this type of operation.

* []()ID: 1148

  Severity: ERROR\
  Message: The search request cannot be processed because it contains an LDAP assertion control and an error occurred while trying to retrieve the base entry to compare it against the assertion filter: %s.

* []()ID: 1149

  Severity: ERROR\
  Message: The search request cannot be processed because it contains an LDAP assertion control but the search base entry does not exist.

* []()ID: 1150

  Severity: ERROR\
  Message: The search request cannot be processed because it contains an LDAP assertion control and the assertion filter did not match the contents of the base entry.

* []()ID: 1151

  Severity: ERROR\
  Message: The search request cannot be processed because it contains a critical control with OID %s that is not supported by the Directory Server for this type of operation.

* []()ID: 1152

  Severity: ERROR\
  Message: Cannot perform the compare operation on entry %s because the request contained an LDAP assertion control and the associated filter did not match the contents of the entry.

* []()ID: 1153

  Severity: ERROR\
  Message: Cannot perform the compare operation on entry %s because the request contained a critical control with OID %s that is not supported by the Directory Server for this type of operation.

* []()ID: 1154

  Severity: INFO\
  Message: The add operation was not actually performed in the Directory Server backend because the LDAP no-op control was present in the request.

* []()ID: 1155

  Severity: INFO\
  Message: The delete operation was not actually performed in the Directory Server backend because the LDAP no-op control was present in the request.

* []()ID: 1156

  Severity: INFO\
  Message: The modify operation was not actually performed in the Directory Server backend because the LDAP no-op control was present in the request.

* []()ID: 1157

  Severity: INFO\
  Message: The modify DN operation was not actually performed in the Directory Server backend because the LDAP no-op control was present in the request.

* []()ID: 1158

  Severity: ERROR\
  Message: Entry %s cannot be added because it is missing attribute %s that is contained in the entry's RDN. All attributes used in the RDN must also be provided in the attribute list for the entry.

* []()ID: 1159

  Severity: ERROR\
  Message: Unable to process the bind request because it contained a control with OID %s that was marked critical but this control is not supported for the bind operation.

* []()ID: 1161

  Severity: WARNING\
  Message: The user-specific size limit value %s contained in user entry %s could not be parsed as an integer. The default server size limit will be used.

* []()ID: 1163

  Severity: WARNING\
  Message: The user-specific time limit value %s contained in user entry %s could not be parsed as an integer. The default server time limit will be used.

* []()ID: 1177

  Severity: ERROR\
  Message: Unable to add entry %s because the Directory Server is configured in read-only mode.

* []()ID: 1178

  Severity: ERROR\
  Message: Unable to add entry %s because the backend that should hold that entry is configured in read-only mode.

* []()ID: 1179

  Severity: ERROR\
  Message: Unable to delete entry %s because the Directory Server is configured in read-only mode.

* []()ID: 1180

  Severity: ERROR\
  Message: Unable to delete entry %s because the backend that holds that entry is configured in read-only mode.

* []()ID: 1181

  Severity: ERROR\
  Message: Unable to modify entry %s because the Directory Server is configured in read-only mode.

* []()ID: 1182

  Severity: ERROR\
  Message: Unable to modify entry %s because the backend that holds that entry is configured in read-only mode.

* []()ID: 1183

  Severity: ERROR\
  Message: Unable to rename entry %s because the Directory Server is configured in read-only mode.

* []()ID: 1184

  Severity: ERROR\
  Message: Unable to rename entry %s because the backend that holds that entry is configured in read-only mode.

* []()ID: 1185

  Severity: ERROR\
  Message: Unable to process the simple bind request because it contained a bind DN but no password, which is forbidden by the server configuration.

* []()ID: 1186

  Severity: ERROR\
  Message: The password policy definition contained in configuration entry "%s" is invalid because the specified password attribute "%s" is not defined in the server schema.

* []()ID: 1187

  Severity: ERROR\
  Message: The password policy definition contained in configuration entry "%s" is invalid because the specified password attribute "%s" has a syntax OID of %s. The password attribute must have a syntax OID of either 1.3.6.1.4.1.26027.1.3.1 (for the user password syntax) or 1.3.6.1.4.1.4203.1.1.2 (for the authentication password syntax).

* []()ID: 1188

  Severity: ERROR\
  Message: An error occurred while attempting to determine the value for attribute ds-cfg-require-change-by-time in configuration entry %s: %s.

* []()ID: 1189

  Severity: ERROR\
  Message: The password policy definition contained in configuration entry "%s" is invalid because the specified last login time format "%s" is not a valid format string The last login time format string should conform to the syntax described in the API documentation for the 'java.text.SimpleDateFormat' class.

* []()ID: 1190

  Severity: ERROR\
  Message: The password policy definition contained in configuration entry "%s" is invalid because the specified previous last login time format "%s" is not a valid format string The previous last login time format strings should conform to the syntax described in the API documentation for the 'java.text.SimpleDateFormat' class.

* []()ID: 1191

  Severity: ERROR\
  Message: Attribute options are not allowed for the password attribute %s.

* []()ID: 1192

  Severity: ERROR\
  Message: Only a single value may be provided for the password attribute %s.

* []()ID: 1193

  Severity: ERROR\
  Message: Pre-encoded passwords are not allowed for the password attribute %s.

* []()ID: 1194

  Severity: ERROR\
  Message: The password value for attribute %s was found to be unacceptable: %s.

* []()ID: 1195

  Severity: ERROR\
  Message: The password policy defined in configuration entry %s is configured to always send at least one warning notification before the password is expired, but no warning interval has been set. If configuration attribute ds-cfg-expire-passwords-without-warning is set to "false", then configuration attribute ds-cfg-password-expiration-warning-interval must have a positive value.

* []()ID: 1196

  Severity: ERROR\
  Message: A bind operation is currently in progress on the associated client connection. No other requests may be made on this client connection until the bind processing has completed.

* []()ID: 1197

  Severity: ERROR\
  Message: A StartTLS operation is currently in progress on the associated client connection. No other requests may be made on this client connection until the StartTLS processing has completed.

* []()ID: 1198

  Severity: ERROR\
  Message: A SASL bind operation is currently in progress on the associated client connection. No other requests may be made on this client connection until the SASL bind processing has completed.

* []()ID: 1199

  Severity: ERROR\
  Message: %s must change their password before it will be allowed to request any other operations.

* []()ID: 1200

  Severity: ERROR\
  Message: An error occurred while attempting to decode the ds-pwp-password-policy-dn value "%s" in user entry "%s" as a DN: %s.

* []()ID: 1201

  Severity: ERROR\
  Message: User entry %s is configured to use a password policy subentry of %s but no such password policy has been defined in the server configuration.

* []()ID: 1202

  Severity: ERROR\
  Message: An error occurred while attempting to decode value "%s" for attribute %s in user entry %s in accordance with the generalized time format: %s.

* []()ID: 1203

  Severity: ERROR\
  Message: Unable to decode value "%s" for attribute %s in user entry %s as a Boolean value.

* []()ID: 1204

  Severity: ERROR\
  Message: The entry %s cannot be added due to insufficient access rights.

* []()ID: 1205

  Severity: ERROR\
  Message: The user cannot bind due to insufficient access rights.

* []()ID: 1206

  Severity: ERROR\
  Message: The entry %s cannot be compared due to insufficient access rights.

* []()ID: 1207

  Severity: ERROR\
  Message: The entry %s cannot be deleted due to insufficient access rights.

* []()ID: 1208

  Severity: ERROR\
  Message: The extended operation %s cannot be performed due to insufficient access rights.

* []()ID: 1209

  Severity: ERROR\
  Message: The entry %s cannot be renamed due to insufficient access rights.

* []()ID: 1210

  Severity: ERROR\
  Message: The entry %s cannot be modified due to insufficient access rights.

* []()ID: 1211

  Severity: ERROR\
  Message: The entry %s cannot be searched due to insufficient access rights.

* []()ID: 1212

  Severity: ERROR\
  Message: Rejecting a simple bind request because the password policy requires secure authentication.

* []()ID: 1213

  Severity: ERROR\
  Message: Rejecting a bind request because the account has been administratively disabled.

* []()ID: 1214

  Severity: ERROR\
  Message: Rejecting a bind request because the account has been locked due to too many failed authentication attempts.

* []()ID: 1215

  Severity: ERROR\
  Message: Rejecting a bind request because the account has been locked after the user's password was not changed in a timely manner after an administrative reset.

* []()ID: 1216

  Severity: ERROR\
  Message: Rejecting a bind request because the account has been locked after remaining idle for too long.

* []()ID: 1217

  Severity: ERROR\
  Message: Rejecting a bind request because that user's password is expired.

* []()ID: 1218

  Severity: ERROR\
  Message: An error occurred while attempting to update password policy state information for user %s: %s.

* []()ID: 1219

  Severity: ERROR\
  Message: Rejecting a SASL %s bind request for user %s because the password policy requires secure authentication.

* []()ID: 1220

  Severity: ERROR\
  Message: Rejecting a bind request because the account has expired.

* []()ID: 1221

  Severity: ERROR\
  Message: Attributes used to hold user passwords are not allowed to have any attribute options.

* []()ID: 1222

  Severity: ERROR\
  Message: Users are not allowed to change their own passwords.

* []()ID: 1223

  Severity: ERROR\
  Message: Password changes must be performed over a secure authentication channel.

* []()ID: 1224

  Severity: ERROR\
  Message: The password cannot be changed because it has not been long enough since the last password change.

* []()ID: 1225

  Severity: ERROR\
  Message: Multiple password values are not allowed in user entries.

* []()ID: 1226

  Severity: ERROR\
  Message: User passwords may not be provided in pre-encoded form.

* []()ID: 1227

  Severity: ERROR\
  Message: Invalid modification type %s attempted on password attribute %s.

* []()ID: 1228

  Severity: ERROR\
  Message: The user entry does not have any existing passwords to remove.

* []()ID: 1229

  Severity: ERROR\
  Message: The provided user password does not match any password in the user's entry.

* []()ID: 1230

  Severity: ERROR\
  Message: The password policy requires that user password changes include the current password in the request.

* []()ID: 1231

  Severity: ERROR\
  Message: The password change would result in multiple password values in the user entry, which is not allowed.

* []()ID: 1232

  Severity: ERROR\
  Message: The provided password value was rejected by a password validator: %s.

* []()ID: 1233

  Severity: ERROR\
  Message: %s must change their password before it will be allowed to perform any other operations.

* []()ID: 1234

  Severity: WARNING\
  Message: The user password is about to expire (time to expiration: %s).

* []()ID: 1235

  Severity: ERROR\
  Message: The account has been locked as a result of too many failed authentication attempts (time to unlock: %s).

* []()ID: 1236

  Severity: ERROR\
  Message: The account has been locked as a result of too many failed authentication attempts. It may only be unlocked by an administrator.

* []()ID: 1237

  Severity: INFO\
  Message: The user password has been changed.

* []()ID: 1238

  Severity: INFO\
  Message: The user password has been administratively reset.

* []()ID: 1239

  Severity: INFO\
  Message: The user account has been administratively enabled.

* []()ID: 1240

  Severity: INFO\
  Message: The user account has been administratively disabled.

* []()ID: 1241

  Severity: INFO\
  Message: The user account has been administratively unlocked.

* []()ID: 1242

  Severity: ERROR\
  Message: The specified password value already exists in the user entry.

* []()ID: 1244

  Severity: INFO\
  Message: Do not detach from the terminal and continue running in the foreground. This option cannot be used with the -t, --timeout option.

* []()ID: 1245

  Severity: INFO\
  Message: This utility can be used to start the Directory Server, as well as to obtain the server version and other forms of general server information.

* []()ID: 1246

  Severity: ERROR\
  Message: Unable to process the request for extended operation %s because it contained an unsupported critical control with OID %s.

* []()ID: 1247

  Severity: ERROR\
  Message: Unable to register backend %s with the Directory Server because another backend with the same backend ID is already registered.

* []()ID: 1248

  Severity: ERROR\
  Message: Unable to register base DN %s with the Directory Server for backend %s because that base DN is already registered for backend %s.

* []()ID: 1249

  Severity: ERROR\
  Message: Unable to register base DN %s with the Directory Server for backend %s because that backend already contains another base DN %s that is within the same hierarchical path.

* []()ID: 1250

  Severity: ERROR\
  Message: Unable to register base DN %s with the Directory Server for backend %s because that backend already contains another base DN %s that is not subordinate to the same base DN in the parent backend.

* []()ID: 1251

  Severity: ERROR\
  Message: Unable to register base DN %s with the Directory Server for backend %s because that backend already contains one or more other base DNs that are subordinate to backend %s but the new base DN is not.

* []()ID: 1252

  Severity: WARNING\
  Message: Backend %s already contains entry %s which has just been registered as the base DN for backend %s. These conflicting entries can cause unexpected or errant search results, and both backends should be reinitialized to ensure that each has the correct content.

* []()ID: 1253

  Severity: ERROR\
  Message: Unable to de-register base DN %s with the Directory Server because that base DN is not registered for any active backend.

* []()ID: 1254

  Severity: WARNING\
  Message: Base DN %s has been deregistered from the Directory Server for backend %s. This base DN had both superior and subordinate entries in other backends, and there might be inconsistent or unexpected behavior when accessing entries in this portion of the hierarchy because of the missing entries that had been held in the de-registered backend.

* []()ID: 1255

  Severity: ERROR\
  Message: Rejecting the requested operation because the connection has not been authenticated.

* []()ID: 1256

  Severity: WARNING\
  Message: Entry "%s" cannot be added because it contains attribute type %s which is declared OBSOLETE in the server schema.

* []()ID: 1257

  Severity: WARNING\
  Message: Entry "%s" cannot be added because it contains objectclass %s which is declared OBSOLETE in the server schema.

* []()ID: 1258

  Severity: ERROR\
  Message: Entry %s cannot be modified because the modification attempted to set one or more new values for attribute %s which is marked OBSOLETE in the server schema.

* []()ID: 1259

  Severity: ERROR\
  Message: Object class %s added to entry %s is marked OBSOLETE in the server schema.

* []()ID: 1260

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because the new RDN includes attribute type %s which is declared OBSOLETE in the server schema.

* []()ID: 1261

  Severity: WARNING\
  Message: Terminating the client connection because its associated authentication or authorization entry %s has been deleted.

* []()ID: 1262

  Severity: ERROR\
  Message: You do not have sufficient privileges to reset user passwords.

* []()ID: 1263

  Severity: ERROR\
  Message: You do not have sufficient privileges to access the server configuration.

* []()ID: 1264

  Severity: ERROR\
  Message: You do not have sufficient privileges to add entries that include privileges.

* []()ID: 1265

  Severity: ERROR\
  Message: You do not have sufficient privileges to modify the set of privileges contained in an entry.

* []()ID: 1266

  Severity: ERROR\
  Message: You do not have sufficient privileges to use the proxied authorization control.

* []()ID: 1267

  Severity: ERROR\
  Message: PingDS is configured to run as a Windows service and it cannot run in no-detach mode.

* []()ID: 1268

  Severity: ERROR\
  Message: Unable to decode an entry because it had an unsupported entry version byte value of %s.

* []()ID: 1269

  Severity: ERROR\
  Message: Unable to decode an entry because an unexpected exception was caught during processing: %s.

* []()ID: 1270

  Severity: ERROR\
  Message: The request control with Object Identifier (OID) "%s" cannot be used due to insufficient access rights.

* []()ID: 1271

  Severity: ERROR\
  Message: The connection handler %s is trying to use the listener %s which is already in use by another connection handler.

* []()ID: 1272

  Severity: ERROR\
  Message: No enabled connection handler available.

* []()ID: 1273

  Severity: ERROR\
  Message: Could not start connection handlers.

* []()ID: 1274

  Severity: ERROR\
  Message: Unable to process the non-root bind because the server is in lockdown mode.

* []()ID: 1275

  Severity: WARNING\
  Message: The Directory Server is entering lockdown mode, in which clients will only be allowed to connect via a loopback address, and only root users will be allowed to process operations.

* []()ID: 1276

  Severity: NOTICE\
  Message: The Directory Server is leaving lockdown mode and will resume normal operation.

* []()ID: 1277

  Severity: NOTICE\
  Message: Rejecting the requested operation because the server is in lockdown mode and will only accept requests from root users over loopback connections.

* []()ID: 1278

  Severity: ERROR\
  Message: Unable to decode the provided attribute because it used an undefined attribute description token %s.

* []()ID: 1279

  Severity: ERROR\
  Message: Unable to decode the provided object class set because it used an undefined token %s.

* []()ID: 1280

  Severity: ERROR\
  Message: Unable to decode the provided entry encode configuration element because it has an invalid length.

* []()ID: 1281

  Severity: ERROR\
  Message: Rejecting a bind request for user %s because either the entire server or the user's backend has a writability mode of 'disabled' and password policy state updates would not be allowed.

* []()ID: 1282

  Severity: ERROR\
  Message: The provided new password was found in the password history for the user.

* []()ID: 1284

  Severity: WARNING\
  Message: The user-specific idle time limit value %s contained in user entry %s could not be parsed as an integer. The default server idle time limit will be used.

* []()ID: 1285

  Severity: INFO\
  Message: This connection has been terminated because it has remained idle for too long.

* []()ID: 1286

  Severity: ERROR\
  Message: The password policy configuration entry "%s" is invalid because if a maximum password age is configured, then the password expiration warning interval must be shorter than the maximum password age.

* []()ID: 1287

  Severity: ERROR\
  Message: The password policy configuration entry "%s" is invalid because if both a minimum password age and a maximum password age are configured, then the sum of the minimum password age and the password expiration warning interval must be shorter than the maximum password age.

* []()ID: 1288

  Severity: ERROR\
  Message: An error occurred while attempting to disconnect client connection %d: %s.

* []()ID: 1292

  Severity: ERROR\
  Message: The specified schema configuration directory '%s' is invalid. The specified path must exist and must be a directory.

* []()ID: 1293

  Severity: ERROR\
  Message: The Directory Server is currently running. The environment configuration can not be altered while the server is online.

* []()ID: 1294

  Severity: ERROR\
  Message: An error occurred while attempting to initialize a SSL context for server to server communication: %s.

* []()ID: 1295

  Severity: INFO\
  Message: Attempt to start using the configuration that was in place at the last successful startup (if it is available) rather than using the current active configuration.

* []()ID: 1296

  Severity: INFO\
  Message: Error while searching base %s to synchronize the trust store: %s.

* []()ID: 1297

  Severity: ERROR\
  Message: An error occurred in the trust store synchronization thread: %s.

* []()ID: 1298

  Severity: INFO\
  Message: Error while trying to add entry %s to the trust store: %s.

* []()ID: 1299

  Severity: ERROR\
  Message: The password storage scheme defined in configuration entry %s does not support the auth password syntax, which is used by password attribute %s.

* []()ID: 1300

  Severity: ERROR\
  Message: Password policy configuration entry %s references deprecated password storage scheme DN %s which does not support the auth password syntax.

* []()ID: 1301

  Severity: WARNING\
  Message: The search filter "%s" used by group implementation %s is not indexed in backend %s. Backend initialization for this group implementation might take a very long time to complete.

* []()ID: 1302

  Severity: ERROR\
  Message: CryptoManager cannot get the requested digest %s: %s.

* []()ID: 1303

  Severity: ERROR\
  Message: CryptoManager cannot get the requested MAC engine %s: %s.

* []()ID: 1304

  Severity: ERROR\
  Message: CryptoManager cannot get the requested encryption cipher %s: %s.

* []()ID: 1305

  Severity: ERROR\
  Message: CryptoManager cannot get the preferred key wrapping cipher: %s.

* []()ID: 1306

  Severity: ERROR\
  Message: CryptoManager failed to retrieve the collection of instance-key-pair public-key-certificates from ADS container "%s": %s.

* []()ID: 1307

  Severity: ERROR\
  Message: CryptoManager failed to encode symmetric key attribute value: %s.

* []()ID: 1308

  Severity: ERROR\
  Message: CryptoManager symmetric key attribute value "%s" syntax is invalid: incorrect number of fields.

* []()ID: 1309

  Severity: ERROR\
  Message: CryptoManager symmetric key attribute value "%s" syntax is invalid. Parsing failed in field "%s" at offset %d.

* []()ID: 1310

  Severity: ERROR\
  Message: CryptoManager failed to decipher the wrapped secret-key value: %s.

* []()ID: 1311

  Severity: ERROR\
  Message: CryptoManager cannot find the public-key-certificate (identifier "%s") requested for symmetric key re-encoding.

* []()ID: 1312

  Severity: ERROR\
  Message: CryptoManager failed to decode the key entry identifier "%s": %s.

* []()ID: 1313

  Severity: ERROR\
  Message: CryptoManager passed invalid MAC algorithm "%s": %s.

* []()ID: 1314

  Severity: ERROR\
  Message: CryptoManager failed to initialize MAC engine: %s.

* []()ID: 1315

  Severity: ERROR\
  Message: CryptoManager passed invalid Cipher transformation "%s": %s.

* []()ID: 1316

  Severity: ERROR\
  Message: CryptoManager cannot initialize Cipher: %s.

* []()ID: 1317

  Severity: ERROR\
  Message: CryptoManager failed to write the stream prologue: %s.

* []()ID: 1318

  Severity: ERROR\
  Message: CryptoManager failed to decrypt the supplied data because it could not read the symmetric key identifier in the data prologue: %s.

* []()ID: 1319

  Severity: ERROR\
  Message: CryptoManager failed to decrypt the supplied data because the symmetric key identifier in the data prologue does not match any known key entries.

* []()ID: 1320

  Severity: ERROR\
  Message: CryptoManager failed to decrypt the supplied data because it could not read the cipher initialization vector in the data prologue.

* []()ID: 1321

  Severity: ERROR\
  Message: CryptoManager failed to decrypt the supplied data because there was an error reading from the input stream: %s.

* []()ID: 1322

  Severity: ERROR\
  Message: CryptoManager failed to import the symmetric key entry "%s" because it could not obtain a symmetric key attribute value that can be decoded by this instance.

* []()ID: 1323

  Severity: ERROR\
  Message: CryptoManager detected a field mismatch between the key entry to be imported and an entry in the key cache that share the key identifier "%s".

* []()ID: 1324

  Severity: ERROR\
  Message: CryptoManager failed to import the symmetric key entry "%s": %s.

* []()ID: 1325

  Severity: ERROR\
  Message: CryptoManager failed to import the symmetric key entry "%s" because it could not add a symmetric key attribute value that can be decoded by this instance.

* []()ID: 1326

  Severity: ERROR\
  Message: CryptoManager failed to instantiate a KeyGenerator for algorithm "%s": %s.

* []()ID: 1327

  Severity: ERROR\
  Message: CryptoManager failed to add locally produced symmetric key entry "%s": %s.

* []()ID: 1328

  Severity: ERROR\
  Message: CryptoManager cipher transformation specification "%s" is invalid: it must be of the form "algorithm/mode/padding".

* []()ID: 1329

  Severity: ERROR\
  Message: CryptoManager cipher transformation specification "%s" is invalid: it must be of the form "algorithm/mode/padding".

* []()ID: 1330

  Severity: ERROR\
  Message: CryptoManager failed to decrypt the supplied data because it could not read the version number in the data prologue: %s.

* []()ID: 1331

  Severity: ERROR\
  Message: CryptoManager failed to decrypt the supplied data because the version "%d" in the data prologue is unknown.

* []()ID: 1332

  Severity: ERROR\
  Message: CryptoManager failed to sign the wrapped key entry: %s.

* []()ID: 1333

  Severity: ERROR\
  Message: The wrapped key entry is missing the following attributes: %s. This PingDS version is not compatible with the backup contents, verify the PingDS version where the backup was created.

* []()ID: 1334

  Severity: ERROR\
  Message: The server failed to find the master key pair with ID '%s' in its key store. Make sure that the server has access to the master key pair that was used when the key was wrapped.

* []()ID: 1335

  Severity: ERROR\
  Message: The wrapped key entry signature does not match the entry content.

* []()ID: 1336

  Severity: ERROR\
  Message: CryptoManager failed to verify the wrapped key entry signature: %s.

* []()ID: 1338

  Severity: NOTICE\
  Message: %s.

* []()ID: 1339

  Severity: NOTICE\
  Message: Build ID: %s.

* []()ID: 1340

  Severity: ERROR\
  Message: Start TLS extended operations cannot be canceled.

* []()ID: 1341

  Severity: ERROR\
  Message: Cancel extended operations can not be canceled.

* []()ID: 1342

  Severity: ERROR\
  Message: The modify DN operation for entry %s cannot be performed because the new superior entry %s is equal to or a subordinate of the entry to be moved.

* []()ID: 1343

  Severity: INFO\
  Message: Unable to process operation because this search scope is not allowed in this network group.

* []()ID: 1344

  Severity: ERROR\
  Message: Entry %s can not be added because BER encoding of %s attribute is not supported.

* []()ID: 1345

  Severity: INFO\
  Message: No worker queue thread pool size specified: sizing automatically to use %d threads.

* []()ID: 1346

  Severity: INFO\
  Message: Maximum time (in seconds) to wait before the command returns (the server continues the startup process, regardless). A value of '0' indicates an infinite timeout, which means that the command returns only when the server startup is completed. The default value is 60 seconds. This option cannot be used with the -N, --nodetach option.

* []()ID: 1347

  Severity: ERROR\
  Message: In no-detach mode, the 'timeout' option cannot be used.

* []()ID: 1348

  Severity: WARNING\
  Message: The search filter "%s" used by subentry manager is not indexed in backend %s. Backend initialization for subentry manager processing might take a very long time to complete.

* []()ID: 1349

  Severity: ERROR\
  Message: The subentry %s must have either the pwdPolicy or ds-pwp-password-policy objectclasses, which is required for the Directory Server password policy.

* []()ID: 1350

  Severity: ERROR\
  Message: CryptoManager failed to initialize because the specified cipher key length "%d" is beyond the allowed cryptography strength "%d" in jurisdiction policy files.

* []()ID: 1351

  Severity: ERROR\
  Message: Failed to update free disk space for directory %s: %s.

* []()ID: 1352

  Severity: ERROR\
  Message: The directory server is not accepting a new persistent search request because the server has already reached its limit.

* []()ID: 1353

  Severity: ERROR\
  Message: This operation involves LDAP subentries which you do not have sufficient privileges to administer.

* []()ID: 1354

  Severity: INFO\
  Message: Invalid Credentials.

* []()ID: 1355

  Severity: WARNING\
  Message: Entry "%s" contains a value for attribute %s that is invalid according to the syntax for that attribute: %s.

* []()ID: 1356

  Severity: ERROR\
  Message: When attempting to modify entry %s, one value for attribute %s was found to be invalid according to the associated syntax: %s.

* []()ID: 1357

  Severity: ERROR\
  Message: When attempting to modify entry %s to replace the set of values for attribute %s, one value was found to be invalid according to the associated syntax: %s.

* []()ID: 1358

  Severity: ERROR\
  Message: The password policy definition contained in configuration entry "%s" is invalid because the password validator "%s" specified in attribute "%s" cannot be found.

* []()ID: 1359

  Severity: ERROR\
  Message: The password could not be validated because of misconfiguration. Please contact the administrator.

* []()ID: 1360

  Severity: ERROR\
  Message: The password for user %s could not be validated because the password policy subentry %s is referring to an unknown password validator (%s). Please make sure the password policy subentry only refers to validators that exist on all replicas.

* []()ID: 1361

  Severity: ERROR\
  Message: Could not get filesystem for directory %s: %s.

* []()ID: 1362

  Severity: ERROR\
  Message: The free space (%s) on the disk containing directory "%s" is between low and full threshold for the following subsystems: %s. Write operations are only permitted by a user with the BYPASS\_LOCKDOWN privilege until the free space rises above the threshold. Replication updates are still allowed.

* []()ID: 1363

  Severity: ERROR\
  Message: The free space (%s) on the disk containing directory "%s" is below full threshold for the following subsystems: %s. Write operations to the backend, replication updates included, will fail until the free space rises above the threshold.

* []()ID: 1364

  Severity: NOTICE\
  Message: The free space (%s) on the disk containing directory "%s" is now above the low threshold for the following subsystems: %s.

* []()ID: 1367

  Severity: ERROR\
  Message: An error occurred while adding Service Discovery Mechanism '%s': %s.

* []()ID: 1368

  Severity: ERROR\
  Message: Registering Service Discovery Manager's listener failed : %s.

* []()ID: 1369

  Severity: ERROR\
  Message: Discovery mechanism '%s' initialization failed : %s.

* []()ID: 1370

  Severity: WARNING\
  Message: Replication server '%s' references server '%s' that could not be parsed correctly; the definition will be skipped.

* []()ID: 1371

  Severity: ERROR\
  Message: Error occurred while creating an SSL context for service discovery mechanism '%s' : %s.

* []()ID: 1372

  Severity: ERROR\
  Message: Could not retrieve the list of replicas from replication server '%s' for replication server group '%s'. Exception : %s.

* []()ID: 1373

  Severity: ERROR\
  Message: Could not retrieve auto-configuration data from directory server '%s' for replication server group '%s'. Exception : %s".

* []()ID: 1374

  Severity: ERROR\
  Message: Service discovery mechanism '%s' failed to refresh the partition information. Exception : %s",.

* []()ID: 1375

  Severity: WARNING\
  Message: Settings for Replica '%s' should provide a hostname.

* []()ID: 1376

  Severity: WARNING\
  Message: Cannot connect to replica '%s' for replication service discovery mechanism '%s'. The replica entry is: %s.

* []()ID: 1377

  Severity: WARNING\
  Message: Cannot gather naming contexts from server %s: %s.

* []()ID: 1378

  Severity: WARNING\
  Message: Scheduled discovery '%s' failed : %s.

* []()ID: 1379

  Severity: ERROR\
  Message: Service discovery mechanism '%s' failed to refresh the connection options. Exception : %s",.

* []()ID: 1380

  Severity: ERROR\
  Message: "%s" (low=%s, full=%s).

* []()ID: 1381

  Severity: ERROR\
  Message: You do not have sufficient privileges to read directory server monitoring information.

* []()ID: 1382

  Severity: WARNING\
  Message: The user-specific lookthrough limit value '%s' contained in user entry '%s' could not be parsed as an integer. The default server lookthrough limit will be used.

* []()ID: 1383

  Severity: WARNING\
  Message: The user-specific maximum candidate set size value '%s' contained in user entry '%s' could not be parsed as an integer. The default server maximum candidate set size will be used.

* []()ID: 1384

  Severity: ERROR\
  Message: Entry %s cannot be added because its parent entry %s is a subentry.

* []()ID: 1385

  Severity: INFO\
  Message: Server in lockdown mode.

* []()ID: 1386

  Severity: ERROR\
  Message: The master key with alias '%s' does not exist in the '%s' key manager. Please check that the correct key manager has been configured and that it contains the specified master keys.

* []()ID: 1387

  Severity: ERROR\
  Message: The CryptoManager could not encode a symmetric key because the master key with alias '%s' does not exist in the '%s' key manager. Please check that the correct key manager has been configured and that it contains the specified master keys.

* []()ID: 1388

  Severity: ERROR\
  Message: The CryptoManager could was not able to obtain the deployment's pepper. Please check that the CryptoManager has a correctly configured key manager and preferred digest mechanism.

* []()ID: 1389

  Severity: ERROR\
  Message: No enabled password storage schemes in '%s' in subentry '%s'.

* []()ID: 1390

  Severity: ERROR\
  Message: Cannot use both pwdValidatorPolicy and ds-pwp-validator in subentry '%s'.

* []()ID: 1391

  Severity: ERROR\
  Message: The dictionary data could not be decompressed: %s.

* []()ID: 1392

  Severity: ERROR\
  Message: The dictionary validator configuration is invalid.

* []()ID: 1393

  Severity: WARNING\
  Message: Found %d conflicting password policy subentries for user %s, used %s.

* []()ID: 1394

  Severity: ERROR\
  Message: Requested cipher for a non existing cipher key: cryptographic services were not properly initialized, programming error.

* []()ID: 1395

  Severity: ERROR\
  Message: Type %d is not a valid secret key type. The Valid type is '0' for a cipher key. Secret key initialization cannot continue, check the data source and re-initialize if needed.

* []()ID: 1396

  Severity: ERROR\
  Message: The subentry %s cannot use both %s and %s objectclasses.

* []()ID: 1397

  Severity: ERROR\
  Message: The subentry %s using the %s objectclass cannot define validators using the old %s objectclass.

* []()ID: 1398

  Severity: ERROR\
  Message: The subentry %s using the %s objectclass cannot define validators using the new %s objectclass.

* []()ID: 1399

  Severity: ERROR\
  Message: The value for the '%s' attribute is not a valid duration.

* []()ID: 1400

  Severity: ERROR\
  Message: The value for the '%s' attribute is not a valid integer.

* []()ID: 1401

  Severity: ERROR\
  Message: The value for the '%s' attribute is not a valid boolean.

* []()ID: 1402

  Severity: ERROR\
  Message: The value for the '%s' attribute is not a valid time.

* []()ID: 1403

  Severity: ERROR\
  Message: The value for the '%s' attribute is not a valid string.

* []()ID: 1404

  Severity: ERROR\
  Message: The value for the '%s' attribute is not a valid attribute.

* []()ID: 1405

  Severity: ERROR\
  Message: The values for the '%s' attribute are not valid strings.

* []()ID: 1406

  Severity: ERROR\
  Message: The value for the '%s' attribute is not a valid state update failure policy.

* []()ID: 1407

  Severity: ERROR\
  Message: A values for the '%s' attribute is not a valid attribute name.

* []()ID: 1408

  Severity: ERROR\
  Message: Could not start connection handler %s with listen addresses "%s". The error was: %s.

* []()ID: 1409

  Severity: INFO\
  Message: Registered %d static groups, %d dynamic groups and %d virtual static groups. The static group cache is using %s of memory (%d bytes).

* []()ID: 1411

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the message digest generator for the %s algorithm: %s.

* []()ID: 1412

  Severity: ERROR\
  Message: An error occurred while attempting to base64-decode the password value %s: %s.

* []()ID: 1413

  Severity: ERROR\
  Message: The %s password storage scheme is not reversible, so it is impossible to recover the plaintext version of an encoded password.

* []()ID: 1414

  Severity: ERROR\
  Message: An error occurred while trying to register the JMX alert handler with the MBean server: %s.

* []()ID: 1415

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to encode a password using the storage scheme defined in class %s: %s.

* []()ID: 1416

  Severity: ERROR\
  Message: The ds-cfg-include-filter attribute of configuration entry %s, which specifies a set of search filters that may be used to control which entries are included in the cache, has an invalid value of "%s": %s.

* []()ID: 1417

  Severity: ERROR\
  Message: The ds-cfg-exclude-filter attribute of configuration entry %s, which specifies a set of search filters that may be used to control which entries are excluded from the cache, has an invalid value of "%s": %s.

* []()ID: 1418

  Severity: ERROR\
  Message: A fatal error occurred while trying to initialize fifo entry cache: %s.

* []()ID: 1419

  Severity: ERROR\
  Message: A fatal error occurred while trying to initialize soft reference entry cache: %s.

* []()ID: 1420

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to decode the password modify extended request sequence: %s.

* []()ID: 1421

  Severity: ERROR\
  Message: The password modify extended request cannot be processed because it does not contain an authorization ID and the underlying connection is not authenticated.

* []()ID: 1422

  Severity: ERROR\
  Message: The password modify extended request cannot be processed because the server was unable to obtain a write lock on user entry %s after multiple attempts.

* []()ID: 1423

  Severity: ERROR\
  Message: The password modify extended request cannot be processed because the server cannot decode "%s" as a valid DN for use in the authorization ID for the operation.

* []()ID: 1424

  Severity: ERROR\
  Message: The password modify extended request cannot be processed because it contained an invalid userIdentity field. The provided userIdentity string was "%s".

* []()ID: 1425

  Severity: ERROR\
  Message: The password modify extended request cannot be processed because it was not possible to identify the user entry to update based on the authorization DN of "%s".

* []()ID: 1426

  Severity: ERROR\
  Message: The password modify extended operation cannot be processed because the current password provided for the user is invalid.

* []()ID: 1427

  Severity: ERROR\
  Message: The keystore file %s specified in attribute ds-cfg-key-store-file of configuration entry %s does not exist.

* []()ID: 1428

  Severity: ERROR\
  Message: An error occurred while trying to load the keystore contents from file %s: %s.

* []()ID: 1429

  Severity: ERROR\
  Message: The keystore type %s specified in attribute ds-cfg-key-store-type of configuration entry %s is not valid: %s.

* []()ID: 1430

  Severity: ERROR\
  Message: An error occurred while trying to access the PKCS#11 key manager: %s.

* []()ID: 1431

  Severity: ERROR\
  Message: An error occurred while trying to create a key manager factory to access the contents of keystore file %s: %s.

* []()ID: 1432

  Severity: ERROR\
  Message: An error occurred while trying to create a key manager factory to access the contents of the PKCS#11 keystore: %s.

* []()ID: 1433

  Severity: ERROR\
  Message: The trust store file %s specified in attribute ds-cfg-trust-store-file of configuration entry %s does not exist.

* []()ID: 1434

  Severity: ERROR\
  Message: An error occurred while trying to load the trust store contents from file %s: %s.

* []()ID: 1435

  Severity: ERROR\
  Message: An error occurred while trying to create a trust manager factory to access the contents of trust store file %s: %s.

* []()ID: 1436

  Severity: ERROR\
  Message: The trust store type %s specified in attribute ds-cfg-trust-store-type of configuration entry %s is not valid: %s.

* []()ID: 1437

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user entry because no peer certificate was available.

* []()ID: 1438

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because the peer certificate was not an X.509 certificate (peer certificate format was %s).

* []()ID: 1439

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because the peer certificate subject "%s" could not be decoded as an LDAP DN: %s.

* []()ID: 1440

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because an error occurred while attempting to retrieve the user entry with DN "%s": %s.

* []()ID: 1441

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because no user entry exists with a DN of %s.

* []()ID: 1442

  Severity: ERROR\
  Message: The SASL EXTERNAL bind request could not be processed because the associated bind request does not have a reference to the client connection.

* []()ID: 1444

  Severity: ERROR\
  Message: The SASL EXTERNAL bind request could not be processed because the client did not present a certificate chain during SSL/TLS negotiation.

* []()ID: 1445

  Severity: ERROR\
  Message: The SASL EXTERNAL bind request failed because the certificate chain presented by the client during SSL/TLS negotiation could not be mapped to a user entry in the Directory Server.

* []()ID: 1447

  Severity: ERROR\
  Message: StartTLS cannot be used on this client connection because this connection type is not capable of using StartTLS to protect its communication.

* []()ID: 1448

  Severity: ERROR\
  Message: Unable to authenticate via SASL EXTERNAL because the mapped user entry %s does not have any certificates with which to verify the presented peer certificate.

* []()ID: 1449

  Severity: ERROR\
  Message: Unable to authenticate via SASL EXTERNAL because the mapped user entry %s did not contain the peer certificate presented by the client.

* []()ID: 1450

  Severity: ERROR\
  Message: An error occurred while attempting to validate the peer certificate presented by the client with a certificate from the user's entry %s: %s.

* []()ID: 1451

  Severity: ERROR\
  Message: SASL PLAIN authentication requires that SASL credentials be provided but none were included in the bind request.

* []()ID: 1452

  Severity: ERROR\
  Message: The SASL PLAIN bind request did not include any NULL characters. NULL characters are required as delimiters between the authorization ID and authentication ID, and also between the authentication ID and the password.

* []()ID: 1453

  Severity: ERROR\
  Message: The SASL PLAIN bind request did not include a second NULL character in the credentials, which is required as a delimiter between the authentication ID and the password.

* []()ID: 1454

  Severity: ERROR\
  Message: The authentication ID contained in the SASL PLAIN bind request had a length of zero characters, which is not allowed. SASL PLAIN authentication does not allow an empty string for use as the authentication ID.

* []()ID: 1455

  Severity: ERROR\
  Message: The password contained in the SASL PLAIN bind request had a length of zero characters, which is not allowed. SASL PLAIN authentication does not allow an empty string for use as the password.

* []()ID: 1456

  Severity: ERROR\
  Message: An error occurred while attempting to decode the SASL PLAIN authentication ID "%s" because it appeared to contain a DN but DN decoding failed: %s.

* []()ID: 1457

  Severity: ERROR\
  Message: The authentication ID in the SASL PLAIN bind request appears to be an empty DN. This is not allowed.

* []()ID: 1458

  Severity: ERROR\
  Message: An error occurred while attempting to retrieve user entry %s as specified in the DN-based authentication ID of a SASL PLAIN bind request: %s.

* []()ID: 1459

  Severity: ERROR\
  Message: The server was not able to find any user entries for the provided authentication ID of %s.

* []()ID: 1460

  Severity: ERROR\
  Message: The provided password is invalid.

* []()ID: 1461

  Severity: INFO\
  Message: An unsupported or unexpected callback was provided to the SASL server for use during %s authentication: %s.

* []()ID: 1462

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to determine the value of the ds-cfg-server-fqdn attribute in configuration entry %s: %s.

* []()ID: 1463

  Severity: ERROR\
  Message: An unexpected error occurred while trying to create an %s context: %s.

* []()ID: 1464

  Severity: ERROR\
  Message: An error occurred while attempting to decode the SASL %s username "%s" because it appeared to contain a DN but DN decoding failed: %s.

* []()ID: 1465

  Severity: ERROR\
  Message: The username in the SASL %s bind request appears to be an empty DN. This is not allowed.

* []()ID: 1466

  Severity: ERROR\
  Message: An error occurred while attempting to retrieve user entry %s as specified in the DN-based username of a SASL %s bind request: %s.

* []()ID: 1467

  Severity: ERROR\
  Message: The username contained in the SASL %s bind request had a length of zero characters, which is not allowed. %s authentication does not allow an empty string for use as the username.

* []()ID: 1468

  Severity: ERROR\
  Message: The server was not able to find any user entries for the provided username of %s.

* []()ID: 1469

  Severity: ERROR\
  Message: The provided authorization ID %s contained an invalid DN: %s.

* []()ID: 1470

  Severity: ERROR\
  Message: The entry %s specified as the authorization identity does not exist.

* []()ID: 1471

  Severity: ERROR\
  Message: The entry %s specified as the authorization identity could not be retrieved: %s.

* []()ID: 1472

  Severity: ERROR\
  Message: The server was unable to find any entry corresponding to authorization ID %s.

* []()ID: 1473

  Severity: ERROR\
  Message: An error occurred while attempting to retrieve the clear-text password(s) for user %s in order to perform SASL %s authentication: %s.

* []()ID: 1474

  Severity: ERROR\
  Message: SASL %s authentication is not possible for user %s because none of the passwords in the user entry are stored in a reversible form.

* []()ID: 1475

  Severity: ERROR\
  Message: SASL %s protocol error: %s.

* []()ID: 1476

  Severity: ERROR\
  Message: The authenticating user %s does not have sufficient privileges to assume a different authorization identity.

* []()ID: 1477

  Severity: ERROR\
  Message: The authenticating user %s does not have sufficient access to assume a different authorization identity.

* []()ID: 1478

  Severity: ERROR\
  Message: The server was unable to find any entry corresponding to authentication ID %s.

* []()ID: 1479

  Severity: ERROR\
  Message: The server was unable to because both the ds-cfg-kdc-address and ds-cfg-realm attributes must be defined or neither defined.

* []()ID: 1480

  Severity: ERROR\
  Message: An error occurred while attempting to map authorization ID %s to a user entry: %s.

* []()ID: 1481

  Severity: ERROR\
  Message: An error occurred while attempting to write a temporary JAAS configuration file for use during GSSAPI processing: %s.

* []()ID: 1482

  Severity: ERROR\
  Message: An error occurred while attempting to create the JAAS login context for GSSAPI authentication: %s.

* []()ID: 1483

  Severity: INFO\
  Message: GSSAPI mechanism using a principal name of: %s.

* []()ID: 1484

  Severity: INFO\
  Message: GSSAPI SASL mechanism using a server fully qualified domain name of: %s.

* []()ID: 1485

  Severity: INFO\
  Message: DIGEST-MD5 SASL mechanism using a realm of: %s.

* []()ID: 1486

  Severity: NOTICE\
  Message: DIGEST-MD5 SASL mechanism using a server fully qualified domain name of: %s.

* []()ID: 1488

  Severity: ERROR\
  Message: ID string %s could not be mapped to exactly one user. It maps at least to both '%s' and '%s'.

* []()ID: 1489

  Severity: ERROR\
  Message: The internal search based on ID string %s could not be processed efficiently: %s. Check the server configuration to ensure that all associated backends are properly configured for these types of searches.

* []()ID: 1490

  Severity: ERROR\
  Message: An internal failure occurred while attempting to resolve ID string %s to a user entry: %s.

* []()ID: 1491

  Severity: ERROR\
  Message: ID string %s mapped to multiple users.

* []()ID: 1492

  Severity: ERROR\
  Message: An error occurred while attempting to map username %s to a Directory Server entry: %s.

* []()ID: 1493

  Severity: ERROR\
  Message: An error occurred while attempting to map username %s to a Directory Server entry: %s.

* []()ID: 1494

  Severity: ERROR\
  Message: Unable to process the cancel request because the extended operation did not include a request value.

* []()ID: 1495

  Severity: ERROR\
  Message: An error occurred while attempting to decode the value of the cancel extended request: %s.

* []()ID: 1496

  Severity: INFO\
  Message: Processing on this operation was terminated as a result of receiving a cancel request (message ID %d).

* []()ID: 1497

  Severity: ERROR\
  Message: Password storage scheme %s does not support use with the authentication password attribute syntax.

* []()ID: 1498

  Severity: ERROR\
  Message: The configured minimum password length of %d characters is greater than the configured maximum password length of %d.

* []()ID: 1499

  Severity: ERROR\
  Message: The provided password is shorter than the minimum required length of %d characters.

* []()ID: 1500

  Severity: ERROR\
  Message: The provided password is longer than the maximum allowed length of %d characters.

## IDs: 1501-2000

* []()ID: 1501

  Severity: ERROR\
  Message: Configuration entry "%s" does not contain attribute ds-cfg-password-character-set which specifies the sets of characters that should be used when generating the password. This is a required attribute.

* []()ID: 1502

  Severity: ERROR\
  Message: Configuration entry "%s" contains multiple definitions for the %s character set.

* []()ID: 1503

  Severity: ERROR\
  Message: An error occurred while attempting to decode the value(s) of the configuration attribute ds-cfg-password-character-set, which is used to hold the character set(s) for use in generating the password: %s.

* []()ID: 1504

  Severity: ERROR\
  Message: The password format string "%s" references an undefined character set "%s".

* []()ID: 1505

  Severity: ERROR\
  Message: The password format string "%s" contains an invalid syntax. This value should be a comma-delimited sequence of elements, where each element is the name of a character set followed by a colon and the number of characters to choose at random from that character set.

* []()ID: 1506

  Severity: ERROR\
  Message: An error occurred while attempting to decode the value for configuration attribute ds-cfg-password-format, which is used to specify the format for the generated passwords: %s.

* []()ID: 1508

  Severity: ERROR\
  Message: The current password must be provided for self password changes.

* []()ID: 1509

  Severity: ERROR\
  Message: Password modify operations that supply the user's current password must be performed over a secure communication channel.

* []()ID: 1510

  Severity: ERROR\
  Message: End users are not allowed to change their passwords.

* []()ID: 1511

  Severity: ERROR\
  Message: Password changes must be performed over a secure communication channel.

* []()ID: 1512

  Severity: ERROR\
  Message: The password cannot be changed because the previous password change was too recent.

* []()ID: 1513

  Severity: ERROR\
  Message: The password cannot be changed because it is expired.

* []()ID: 1514

  Severity: ERROR\
  Message: No new password was provided, and no password generator has been defined that may be used to automatically create a new password.

* []()ID: 1515

  Severity: ERROR\
  Message: An error occurred while attempting to create a new password using the password generator: %s.

* []()ID: 1516

  Severity: ERROR\
  Message: The password policy does not allow users to supply pre-encoded passwords.

* []()ID: 1517

  Severity: ERROR\
  Message: The provided new password failed the validation checks defined in the server: %s.

* []()ID: 1518

  Severity: ERROR\
  Message: Unable to encode the provided password using the default scheme(s): %s.

* []()ID: 1519

  Severity: ERROR\
  Message: An error occurred while attempting to determine the identity mapper to use in conjunction with the password modify extended operation defined in configuration entry %s: %s. The password modify extended operation will not be enabled for use in the server.

* []()ID: 1520

  Severity: ERROR\
  Message: The provided authorization ID string "%s" could not be mapped to any user in the directory.

* []()ID: 1521

  Severity: ERROR\
  Message: An error occurred while attempting to map authorization ID string "%s" to a user entry: %s.

* []()ID: 1522

  Severity: NOTICE\
  Message: Account-Status-Notification type='%s' userdn='%s' id=%d msg='%s'.

* []()ID: 1523

  Severity: ERROR\
  Message: An error occurred while attempting to verify the password for user %s during SASL PLAIN authentication: %s.

* []()ID: 1524

  Severity: WARNING\
  Message: The password modify operation was not actually performed in the Directory Server because the LDAP no-op control was present in the request.

* []()ID: 1525

  Severity: ERROR\
  Message: The user account has been administratively disabled.

* []()ID: 1526

  Severity: ERROR\
  Message: The user account is locked.

* []()ID: 1528

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform password reset operations.

* []()ID: 1529

  Severity: ERROR\
  Message: The provided authorization ID was empty, which is not allowed for DIGEST-MD5 authentication.

* []()ID: 1530

  Severity: ERROR\
  Message: The provided authorization ID %s contained an invalid DN: %s.

* []()ID: 1531

  Severity: ERROR\
  Message: The authenticating user %s does not have sufficient privileges to specify an alternate authorization ID.

* []()ID: 1532

  Severity: ERROR\
  Message: The entry corresponding to authorization DN %s does not exist in the Directory Server.

* []()ID: 1533

  Severity: ERROR\
  Message: An error occurred while attempting to retrieve entry %s specified as the authorization ID: %s.

* []()ID: 1534

  Severity: ERROR\
  Message: No entry corresponding to authorization ID %s was found in the server.

* []()ID: 1535

  Severity: ERROR\
  Message: An error occurred while attempting to map authorization ID %s to a user entry: %s.

* []()ID: 1536

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user entry because no peer certificate was available.

* []()ID: 1537

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because the peer certificate was not an X.509 certificate (peer certificate format was %s).

* []()ID: 1538

  Severity: ERROR\
  Message: The certificate with subject %s could not be mapped to exactly one user. It maps at least to both '%s' and '%s'.

* []()ID: 1539

  Severity: ERROR\
  Message: Configuration entry %s has value '%s' which violates the format required for attribute mappings. The expected format is 'certattr:userattr'.

* []()ID: 1540

  Severity: ERROR\
  Message: Configuration entry %s contains multiple mappings for certificate attribute %s.

* []()ID: 1541

  Severity: ERROR\
  Message: Mapping %s in configuration entry %s references attribute %s which is not defined in the server schema.

* []()ID: 1542

  Severity: ERROR\
  Message: Configuration entry %s contains multiple mappings for user attribute %s.

* []()ID: 1543

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user entry because no peer certificate was available.

* []()ID: 1544

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because the peer certificate was not an X.509 certificate (peer certificate format was %s).

* []()ID: 1545

  Severity: ERROR\
  Message: Unable to decode peer certificate subject %s as a DN: %s.

* []()ID: 1546

  Severity: ERROR\
  Message: Peer certificate subject %s does not contain any attributes for which a mapping has been established.

* []()ID: 1547

  Severity: ERROR\
  Message: The certificate with subject %s could not be mapped to exactly one user. It maps at least to both '%s' and '%s'.

* []()ID: 1548

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user entry because no peer certificate was available.

* []()ID: 1549

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because the peer certificate was not an X.509 certificate (peer certificate format was %s).

* []()ID: 1550

  Severity: ERROR\
  Message: An error occurred while attempting to calculate the fingerprint for the peer certificate with subject %s: %s.

* []()ID: 1551

  Severity: ERROR\
  Message: The certificate with fingerprint '%s' could not be mapped to exactly one user. It maps at least to both '%s' and '%s'.

* []()ID: 1552

  Severity: ERROR\
  Message: Unable to decode value "%s" in entry "%s" as an LDAP URL: %s.

* []()ID: 1554

  Severity: WARNING\
  Message: Base DN %s specified in dynamic group %s does not exist in the server.

* []()ID: 1555

  Severity: ERROR\
  Message: An error occurred while attempting to perform an internal search with base DN %s and filter %s to resolve the member list for dynamic group %s: result code %s, error message %s.

* []()ID: 1556

  Severity: ERROR\
  Message: The provided password differs less than the minimum required difference of %d characters.

* []()ID: 1557

  Severity: ERROR\
  Message: The provided password contained too many instances of the same character appearing consecutively. The maximum number of times the same character may appear consecutively in a password is %d.

* []()ID: 1558

  Severity: ERROR\
  Message: The provided password does not contain enough unique characters. The minimum number of unique characters that may appear in a user password is %d.

* []()ID: 1560

  Severity: ERROR\
  Message: The provided password contained a word from the server's dictionary.

* []()ID: 1561

  Severity: ERROR\
  Message: The specified dictionary file %s does not exist.

* []()ID: 1562

  Severity: ERROR\
  Message: An error occurred while attempting to load the dictionary from file %s: %s.

* []()ID: 1563

  Severity: ERROR\
  Message: The provided password was found in another attribute in the user entry.

* []()ID: 1564

  Severity: ERROR\
  Message: The provided password contained character '%s' which is not allowed for use in passwords.

* []()ID: 1565

  Severity: ERROR\
  Message: The provided password did not contain enough characters from the character set '%s'. The minimum number of characters from that set that must be present in user passwords is %d.

* []()ID: 1566

  Severity: ERROR\
  Message: The provided character set definition '%s' is invalid because it does not contain a colon to separate the minimum count from the character set.

* []()ID: 1567

  Severity: ERROR\
  Message: The provided character set definition '%s' is invalid because the provided character set is empty.

* []()ID: 1568

  Severity: ERROR\
  Message: The provided character set definition '%s' is invalid because the value before the colon must be an integer greater or equal to zero.

* []()ID: 1569

  Severity: ERROR\
  Message: The provided character set definition '%s' is invalid because it contains character '%s' which has already been used.

* []()ID: 1570

  Severity: ERROR\
  Message: The virtual static group defined in entry %s contains multiple target group DNs, but only one is allowed.

* []()ID: 1571

  Severity: ERROR\
  Message: Unable to decode "%s" as the target DN for group %s: %s.

* []()ID: 1572

  Severity: ERROR\
  Message: The virtual static group defined in entry %s does not contain a target group definition.

* []()ID: 1573

  Severity: ERROR\
  Message: Target group %s referenced by virtual static group %s does not exist.

* []()ID: 1575

  Severity: ERROR\
  Message: Virtual static group %s references target group %s which is itself a virtual static group. One virtual static group is not allowed to reference another as its target group.

* []()ID: 1576

  Severity: ERROR\
  Message: You do not have sufficient privileges to use the password policy state extended operation.

* []()ID: 1577

  Severity: ERROR\
  Message: The provided password policy state extended request did not include a request value.

* []()ID: 1578

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to decode password policy state extended request value: %s.

* []()ID: 1579

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to decode an operation from the password policy state extended request: %s.

* []()ID: 1580

  Severity: ERROR\
  Message: No value was provided for the password policy state operation intended to set the disabled state for the user. Exactly one value (either 'true' or 'false') must be given.

* []()ID: 1581

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to set the disabled state for the user. Exactly one value (either 'true' or 'false') must be given.

* []()ID: 1582

  Severity: ERROR\
  Message: The value provided for the password policy state operation intended to set the disabled state for the user was invalid. The value must be either 'true' or 'false'.

* []()ID: 1583

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to set the account expiration time for the user. Exactly one value must be given.

* []()ID: 1584

  Severity: ERROR\
  Message: The value %s provided for the password policy state operation used to set the account expiration time was invalid: %s. The value should be specified using the generalized time format.

* []()ID: 1585

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to set the password changed time for the user. Exactly one value must be given.

* []()ID: 1586

  Severity: ERROR\
  Message: The value %s provided for the password policy state operation used to set the password changed time was invalid: %s. The value should be specified using the generalized time format.

* []()ID: 1587

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to set the password warned time for the user. Exactly one value must be given.

* []()ID: 1588

  Severity: ERROR\
  Message: The value %s provided for the password policy state operation used to set the password warned time was invalid: %s. The value should be specified using the generalized time format.

* []()ID: 1589

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to add an authentication failure time for the user. Exactly one value must be given.

* []()ID: 1590

  Severity: ERROR\
  Message: The value %s provided for the password policy state operation used to update the authentication failure times was invalid: %s. The value should be specified using the generalized time format.

* []()ID: 1591

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to set the last login time for the user. Exactly one value must be given.

* []()ID: 1592

  Severity: ERROR\
  Message: The value %s provided for the password policy state operation used to set the last login time was invalid: %s. The value should be specified using the generalized time format.

* []()ID: 1593

  Severity: ERROR\
  Message: No value was provided for the password policy state operation intended to set the reset state for the user. Exactly one value (either 'true' or 'false') must be given.

* []()ID: 1594

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to set the reset state for the user. Exactly one value (either 'true' or 'false') must be given.

* []()ID: 1595

  Severity: ERROR\
  Message: The value provided for the password policy state operation intended to set the reset state for the user was invalid. The value must be either 'true' or 'false'.

* []()ID: 1596

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to add a grace login use time for the user. Exactly one value must be given.

* []()ID: 1597

  Severity: ERROR\
  Message: The value %s provided for the password policy state operation used to update the grace login use times was invalid: %s. The value should be specified using the generalized time format.

* []()ID: 1598

  Severity: ERROR\
  Message: Multiple values were provided for the password policy state operation intended to set the required change time for the user. Exactly one value must be given.

* []()ID: 1599

  Severity: ERROR\
  Message: The value %s provided for the password policy state operation used to set the required change time was invalid: %s. The value should be specified using the generalized time format.

* []()ID: 1600

  Severity: ERROR\
  Message: The password policy state extended request included an operation with an invalid or unsupported operation type of %s.

* []()ID: 1601

  Severity: WARNING\
  Message: An error occurred while attempting to update the password policy state information for user %s as part of a password modify extended operation (result code='%s', error message='%s').

* []()ID: 1602

  Severity: ERROR\
  Message: The provided new password was already contained in the password history.

* []()ID: 1603

  Severity: ERROR\
  Message: The Directory Server is not configured with any SMTP servers. The SMTP alert handler cannot be used unless the Directory Server is configured with information about at least one SMTP server.

* []()ID: 1604

  Severity: WARNING\
  Message: An error occurred when trying to send an e-mail message for administrative alert with type %s and message %s: %s.

* []()ID: 1605

  Severity: ERROR\
  Message: The provided match pattern "%s" could not be parsed as a regular expression: %s.

* []()ID: 1606

  Severity: ERROR\
  Message: The processed ID string %s could not be mapped to exactly one user. It maps at least to both '%s' and '%s'.

* []()ID: 1607

  Severity: ERROR\
  Message: The internal search based on processed ID string %s could not be processed efficiently: %s. Check the server configuration to ensure that all associated backends are properly configured for these types of searches.

* []()ID: 1608

  Severity: ERROR\
  Message: An internal failure occurred while attempting to resolve processed ID string %s to a user entry: %s.

* []()ID: 1609

  Severity: ERROR\
  Message: The processed ID string %s mapped to multiple users.

* []()ID: 1611

  Severity: ERROR\
  Message: The SMTP account status notification handler defined in configuration entry %s cannot be enabled unless the Directory Server is with information about one or more SMTP servers.

* []()ID: 1612

  Severity: ERROR\
  Message: SMTP account status notification handler configuration entry '%s' does not include any email address attribute types or recipient addresses. At least one of these must be provided.

* []()ID: 1613

  Severity: ERROR\
  Message: Unable to parse message subject value '%s' from configuration entry '%s' because the value does not contain a colon to separate the notification type from the subject.

* []()ID: 1614

  Severity: ERROR\
  Message: Unable to parse message subject value '%s' from configuration entry '%s' because '%s' is not a valid account status notification type.

* []()ID: 1615

  Severity: ERROR\
  Message: The message subject definitions contained in configuration entry '%s' have multiple subjects defined for notification type %s.

* []()ID: 1616

  Severity: ERROR\
  Message: Unable to parse message template file path value '%s' from configuration entry '%s' because the value does not contain a colon to separate the notification type from the template file path.

* []()ID: 1617

  Severity: ERROR\
  Message: Unable to parse message template file path value '%s' from configuration entry '%s' because '%s' is not a valid account status notification type.

* []()ID: 1618

  Severity: ERROR\
  Message: The message template file path definitions contained in configuration entry '%s' have multiple template file paths defined for notification type %s.

* []()ID: 1619

  Severity: ERROR\
  Message: The message template file '%s' referenced in configuration entry '%s' does not exist.

* []()ID: 1620

  Severity: ERROR\
  Message: An unclosed token was found starting at column %d of line %d.

* []()ID: 1621

  Severity: ERROR\
  Message: The notification-user-attr token starting at column %d of line %d references undefined attribute type %s.

* []()ID: 1622

  Severity: ERROR\
  Message: The notification-property token starting at column %d of line %d references undefined notification property %s.

* []()ID: 1623

  Severity: ERROR\
  Message: An unrecognized token %s was found at column %d of line %d.

* []()ID: 1624

  Severity: ERROR\
  Message: An error occurred while attempting to parse message template file '%s' referenced in configuration entry '%s': %s.

* []()ID: 1625

  Severity: INFO\
  Message: Directory Account Status Notification.

* []()ID: 1626

  Severity: ERROR\
  Message: An error occurred while attempting to send an account status notification message for notification type %s for user entry %s: %s.

* []()ID: 1627

  Severity: ERROR\
  Message: An error occurred while trying to encrypt a value using password storage scheme %s: %s.

* []()ID: 1628

  Severity: ERROR\
  Message: An error occurred while trying to decrypt a value using password storage scheme %s: %s.

* []()ID: 1629

  Severity: ERROR\
  Message: Cannot decode the provided symmetric key extended operation because it does not have a value.

* []()ID: 1630

  Severity: ERROR\
  Message: Cannot decode the provided symmetric key extended request: %s.

* []()ID: 1631

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to decode the symmetric key extended request sequence: %s.

* []()ID: 1632

  Severity: WARNING\
  Message: The exact match identity mapper defined in configuration entry %s references attribute type %s which does not have an equality index defined in backend %s.

* []()ID: 1633

  Severity: WARNING\
  Message: The regular expression identity mapper defined in configuration entry %s references attribute type %s which does not have an equality index defined in backend %s.

* []()ID: 1634

  Severity: WARNING\
  Message: The subject attribute to user attribute certificate mapper defined in configuration entry %s references attribute type %s which does not have an equality index defined in backend %s.

* []()ID: 1635

  Severity: ERROR\
  Message: Failed to create a SASL server for SASL mechanism %s.

* []()ID: 1636

  Severity: ERROR\
  Message: GSSAPI SASL mechanism handler initialization failed because the keytab file %s does not exist.

* []()ID: 1637

  Severity: INFO\
  Message: The GSSAPI SASL mechanism handler initialization was successful.

* []()ID: 1638

  Severity: INFO\
  Message: The GSSAPI SASL mechanism handler has been stopped.

* []()ID: 1639

  Severity: ERROR\
  Message: The password value %s has been base64-decoded but is too short to be valid.

* []()ID: 1640

  Severity: ERROR\
  Message: The provided minimum required number of character sets '%d' is invalid because it must at least include all mandatory character sets.

* []()ID: 1641

  Severity: ERROR\
  Message: The provided minimum required number of character sets '%d' is invalid because it is greater than the total number of defined character sets.

* []()ID: 1642

  Severity: ERROR\
  Message: The provided password did not contain characters from at least %d of the following character sets or ranges: %s.

* []()ID: 1643

  Severity: ERROR\
  Message: SASL %s authentication is not supported for user %s because the account is not managed locally.

* []()ID: 1644

  Severity: ERROR\
  Message: Password modification is not supported for user %s because the account is not managed locally.

* []()ID: 1645

  Severity: ERROR\
  Message: The password policy state extended operation is not supported for user %s because the account is not managed locally.

* []()ID: 1646

  Severity: ERROR\
  Message: The user "%s" could not be authenticated using LDAP PTA policy "%s" because the following mapping attributes were not found in the user's entry: %s.

* []()ID: 1647

  Severity: ERROR\
  Message: The user "%s" could not be authenticated using LDAP PTA policy "%s" because the search of base DN "%s" returned more than one entry matching the filter "%s".

* []()ID: 1648

  Severity: ERROR\
  Message: The user "%s" could not be authenticated using LDAP PTA policy "%s" because the search did not return any entries matching the filter "%s".

* []()ID: 1649

  Severity: ERROR\
  Message: The user "%s" could not be authenticated using LDAP PTA policy "%s" because the search failed unexpectedly for the following reason: %s.

* []()ID: 1650

  Severity: ERROR\
  Message: The user "%s" could not be authenticated using LDAP PTA policy "%s" because the bind failed unexpectedly for the following reason: %s.

* []()ID: 1651

  Severity: ERROR\
  Message: The configuration of LDAP PTA policy "%s" is invalid because it does not specify a means for obtaining the mapped search bind password.

* []()ID: 1652

  Severity: ERROR\
  Message: The certificate with subject %s mapped to multiple users.

* []()ID: 1653

  Severity: ERROR\
  Message: The internal search based on the certificate with subject %s could not be processed efficiently: %s. Check the server configuration to ensure that all associated backends are properly configured for these types of searches.

* []()ID: 1654

  Severity: ERROR\
  Message: An internal failure occurred while attempting to map the certificate with subject %s to a user entry: %s.

* []()ID: 1655

  Severity: ERROR\
  Message: The certificate with subject %s mapped to multiple users.

* []()ID: 1656

  Severity: ERROR\
  Message: The internal search based on the certificate with subject %s could not be processed efficiently: %s. Check the server configuration to ensure that all associated backends are properly configured for these types of searches.

* []()ID: 1657

  Severity: ERROR\
  Message: An internal failure occurred while attempting to map the certificate with subject %s to a user entry: %s.

* []()ID: 1658

  Severity: ERROR\
  Message: The certificate with fingerprint %s mapped to multiple users.

* []()ID: 1659

  Severity: ERROR\
  Message: The internal search based on the certificate with fingerprint %s could not be processed efficiently: %s. Check the server configuration to ensure that all associated backends are properly configured for these types of searches.

* []()ID: 1660

  Severity: ERROR\
  Message: An internal failure occurred while attempting to map the certificate with fingerprint %s to a user entry: %s.

* []()ID: 1661

  Severity: ERROR\
  Message: The provided password did not contain enough characters from the character range '%s'. The minimum number of characters from that range that must be present in user passwords is %d.

* []()ID: 1662

  Severity: ERROR\
  Message: The provided character range definition '%s' is invalid because it does not contain a colon to separate the minimum count from the character range.

* []()ID: 1663

  Severity: ERROR\
  Message: The provided character range definition '%s' is invalid because it does not contain a colon to separate the minimum count from the character range.

* []()ID: 1664

  Severity: ERROR\
  Message: The provided character range definition '%s' is invalid because the value before the colon must be an integer greater or equal to zero.

* []()ID: 1665

  Severity: ERROR\
  Message: The provided character range definition '%s' is invalid because the range '%s' is reversed.

* []()ID: 1666

  Severity: ERROR\
  Message: The provided character range definition '%s' is invalid because the range '%s' is missing the minus.

* []()ID: 1667

  Severity: ERROR\
  Message: The provided character range definition '%s' is invalid because the range '%s' is too short.

* []()ID: 1668

  Severity: ERROR\
  Message: There is no private key entry in keystore '%s' used by file based key manager provider '%s'. TLS connections which rely on this key manager provider may fail. Ensure that keystore file contains at least one private key.

* []()ID: 1669

  Severity: ERROR\
  Message: An error occurred while attempting to match a bcrypt hashed password value: %s.

* []()ID: 1670

  Severity: ERROR\
  Message: The mapped search filter template "%s" could not be parsed as a valid LDAP filter.

* []()ID: 1671

  Severity: ERROR\
  Message: An error occurred while trying to create a key manager factory to access the contents of LDAP keystore with base DN '%s': %s.

* []()ID: 1672

  Severity: ERROR\
  Message: An error occurred while trying to create a trust manager factory to access the contents of LDAP keystore with base DN '%s': %s.

* []()ID: 1673

  Severity: ERROR\
  Message: An error occurred while trying to create a trust manager factory to access the contents of the PKCS#11 keystore: %s.

* []()ID: 1674

  Severity: ERROR\
  Message: An error occurred while trying to access the PKCS#11 trust manager: %s.

* []()ID: 1675

  Severity: ERROR\
  Message: Unable to load JVM default keystore from system properties: %s.

* []()ID: 1676

  Severity: ERROR\
  Message: An error occurred while reading information contained within key manager provider from configuration: "%s".

* []()ID: 1677

  Severity: ERROR\
  Message: Unable to get the JVM default truststore: %s.

* []()ID: 1678

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user becausethe peer certificate issuer "%s" could not be decoded as an LDAP DN: %s.

* []()ID: 1679

  Severity: ERROR\
  Message: Could not map the provided certificate chain to a user because the matching user entry with DN '%s' does not contain an issuer DN matching the certificate issuer DN '%s'.

* []()ID: 1680

  Severity: ERROR\
  Message: The baseDN '%s' specified as match base DN in the exact match identity mapper defined in configuration entry '%s', does not belong to a local backend.

* []()ID: 1681

  Severity: ERROR\
  Message: The baseDN '%s' specified as match base DN in the regular expression identity mapper defined in configuration entry '%s', does not belong to a local backend.

* []()ID: 1682

  Severity: ERROR\
  Message: The processed ID string %s is mapped to multiple users.

* []()ID: 1683

  Severity: ERROR\
  Message: File based key manager provider '%s' failed to load content from file '%s'. TLS connections which rely on this key manager provider may fail. Ensure that keystore file contains at least one private key compatible with the security providers. Security providers available in the running JVM are '%s'. The security provider used for loading key manager will be the first in the list which is compatible with the algorithm '%s'.

* []()ID: 1684

  Severity: WARNING\
  Message: File based key manager provider '%s' has loaded multiple key manager from keystore file '%s'. Only one will be used for securing TLS connections which rely on this key manager provider. Security providers available in the running JVM are %s. The security provider used for loading key manager will be the first in the list which is compatible with the algorithm '%s'.

* []()ID: 1685

  Severity: ERROR\
  Message: File based key manager provider '%s' cannot load an X509 extended key manager from keystore file '%s'. TLS connections which rely on this key manager provider may fail. Security providers available in the running JVM are %s. The security provider used for loading key manager will be the first in the list which is compatible with the algorithm '%s'.

* []()ID: 1686

  Severity: ERROR\
  Message: File based key manager provider '%s' cannot load content from keystore file '%s'. TLS connections which rely on this key manager provider may fail. Restarting the server or the impacted connection handler may resolve this problem. Error detail: %s.

* []()ID: 1687

  Severity: ERROR\
  Message: File based trust manager provider '%s' cannot load content from truststore file '%s'. TLS connections which rely on this trust manager provider may fail. Restarting the server or the impacted connection handler may resolve this problem. Error detail: %s.

* []()ID: 1688

  Severity: ERROR\
  Message: File based trust manager provider '%s' failed to load content from file '%s'. TLS connections which rely on this trust manager provider may fail. Ensure that truststore file contains at least one private key compatible with the security providers. Security providers available in the running JVM are '%s'. The security provider used for loading trust manager will be the first in the list which is compatible with the algorithm '%s'.

* []()ID: 1689

  Severity: WARNING\
  Message: File based trust manager provider '%s' has loaded multiple trust manager from truststore file '%s'. Only one will be used for securing TLS connections which rely on this trust manager provider. Security providers available in the running JVM are %s. The security provider used for loading trust manager will be the first in the list which is compatible with the algorithm '%s'.

* []()ID: 1690

  Severity: ERROR\
  Message: File based trust manager provider '%s' cannot load an X509 extended trust manager from truststore file '%s'. TLS connections which rely on this trust manager provider may fail. Security providers available in the running JVM are %s. The security provider used for loading trust manager will be the first in the list which is compatible with the algorithm '%s'.

* []()ID: 1691

  Severity: ERROR\
  Message: The %s SCRAM password storage scheme could not be initialized because the algorithm is not supported by the JVM.

* []()ID: 1692

  Severity: ERROR\
  Message: An error occurred while attempting to decode the SCRAM credential value %s: %s.

* []()ID: 1693

  Severity: ERROR\
  Message: SASL %s authentication is not possible for user '%s' because the user entry does not contain any SCRAM credentials.

* []()ID: 1694

  Severity: ERROR\
  Message: An error occurred while attempting to retrieve the SCRAM credentials for user '%s' in order to perform SASL %s authentication: %s.

* []()ID: 1695

  Severity: ERROR\
  Message: The %s SCRAM SASL mechanism handler could not be initialized because the algorithm is not supported by the JVM.

* []()ID: 1696

  Severity: ERROR\
  Message: Error loading dictionary: %s.

* []()ID: 1697

  Severity: ERROR\
  Message: An error occurred while trying to create a trust manager factory to access the certificates in "cn=admin data": %s.

* []()ID: 1698

  Severity: ERROR\
  Message: '%s' cannot list the secret files in directory '%s', all the secrets will be ignored: %s.

* []()ID: 1699

  Severity: WARNING\
  Message: '%s' cannot read the secret file '%s': %s.

* []()ID: 1700

  Severity: ERROR\
  Message: The file '%s' exceeds max size '%s'.

* []()ID: 1701

  Severity: ERROR\
  Message: '%s' cannot decode the secret file '%s': %s.

* []()ID: 1702

  Severity: WARNING\
  Message: '%s' has ignored the file '%s' either because the certificate does not contain the key usage extension '%s', or because the file does not contain the appropriate key types.

* []()ID: 1703

  Severity: ERROR\
  Message: Invalid excluded file name pattern: %s.

* []()ID: 1704

  Severity: ERROR\
  Message: The Argon2 password storage scheme could not be configured because it requires %s kB of memory, exceeding the maximum available of %s kB. Configure a bigger heap or reduce the Argon2 memory requirements.

* []()ID: 1705

  Severity: ERROR\
  Message: An unexpected error occurred while accessing the instance keys in "cn=admin data": %s.

* []()ID: 1706

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to read the instance key '%s' in "cn=admin data": %s.

* []()ID: 1707

  Severity: ERROR\
  Message: A new Argon2 password storage scheme can only be added by running dsconfig in offline mode.

* []()ID: 1708

  Severity: INFO\
  Message: %s.

* []()ID: 1709

  Severity: INFO\
  Message: %s with exception: %s.

* []()ID: 1710

  Severity: ERROR\
  Message: Error occurred while writing log record for logger %s: %s. Any further write errors will be ignored.

* []()ID: 1711

  Severity: ERROR\
  Message: Error occurred while opening log file %s for logger %s: %s.

* []()ID: 1712

  Severity: ERROR\
  Message: Error occurred while closing log file for logger %s: %s.

* []()ID: 1713

  Severity: ERROR\
  Message: Error occurred while flushing writer buffer for logger %s: %s.

* []()ID: 1714

  Severity: WARNING\
  Message: Invalid error log severity "%s".

* []()ID: 1715

  Severity: WARNING\
  Message: Invalid error log category "%s".

* []()ID: 1716

  Severity: WARNING\
  Message: Invalid override of severity level "%s".

* []()ID: 1717

  Severity: WARNING\
  Message: Error occurred while setting file permissions for the log file %s: %s.

* []()ID: 1718

  Severity: WARNING\
  Message: This platform does not support setting file permissions %s to the log file %s.

* []()ID: 1719

  Severity: ERROR\
  Message: Error occurred while listing log files named by policy with initial file name %s.

* []()ID: 1720

  Severity: ERROR\
  Message: Error occurred while obtaining free disk space in the partition containing log file %s: %s.

* []()ID: 1721

  Severity: ERROR\
  Message: Error occurred while enforcing retention policy %s for logger %s: %s.

* []()ID: 1722

  Severity: ERROR\
  Message: Error while creating or updating common audit log publisher %s: %s.

* []()ID: 1724

  Severity: ERROR\
  Message: Error while reading JSON configuration file %s while creating common audit external log publisher %s: %s.

* []()ID: 1725

  Severity: ERROR\
  Message: Error while creating common audit external log publisher %s: %s.

* []()ID: 1726

  Severity: ERROR\
  Message: Error while creating common audit log publisher %s: %s.

* []()ID: 1727

  Severity: ERROR\
  Message: Error while adding common audit log publisher %s, the publisher defines an unsupported log rotation policy %s.

* []()ID: 1728

  Severity: ERROR\
  Message: Error while adding common audit log publisher %s, the publisher defines an unsupported log retention policy %s.

* []()ID: 1732

  Severity: ERROR\
  Message: Error while processing common audit log publisher %s, time of the day value '%s' for fixed time log rotation policy is not valid, it should use a 24-hour format "HHmm" : %s.

* []()ID: 1733

  Severity: ERROR\
  Message: Error while processing a log event for common audit: %s.

* []()ID: 1740

  Severity: ERROR\
  Message: The log file %s unexpectedly disappeared. It looks like an external system is also trying to manage the log files retention (either deleting or moving files away). This system configuration is incorrect: either PingDS manages the log file retention OR the external system does. Pick one only.

* []()ID: 1741

  Severity: ERROR\
  Message: The message with ID %d has been generated %d times in the last second: %s.

* []()ID: 1742

  Severity: WARNING\
  Message: Invalid error log severity "%s", only one severity must be provided, the highest one at which logging should occur.

* []()ID: 1743

  Severity: ERROR\
  Message: The LDAP attribute description list plugin instance defined in configuration entry %s does not list any plugin types. This plugin must be configured to operate as a pre-parse search plugin.

* []()ID: 1744

  Severity: ERROR\
  Message: The LDAP attribute description list plugin instance defined in configuration entry %s lists an invalid plugin type %s. This plugin can only be used as a pre-parse search plugin.

* []()ID: 1745

  Severity: ERROR\
  Message: The startup plugin defined in configuration entry %s threw an exception when it was invoked during the Directory Server startup process: %s. The server startup process has been aborted.

* []()ID: 1748

  Severity: ERROR\
  Message: The shutdown plugin defined in configuration entry %s threw an exception when it was invoked during the Directory Server shutdown process: %s.

* []()ID: 1749

  Severity: ERROR\
  Message: The post-connect plugin defined in configuration entry %s threw an exception when it was invoked for connection %d from %s: %s. The connection will be terminated.

* []()ID: 1751

  Severity: ERROR\
  Message: The post-disconnect plugin defined in configuration entry %s threw an exception when it was invoked for connection %d from %s: %s.

* []()ID: 1753

  Severity: ERROR\
  Message: The pre-parse %s plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s. Processing on this operation will be terminated.

* []()ID: 1755

  Severity: ERROR\
  Message: The pre-operation %s plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s. Processing on this operation will be terminated.

* []()ID: 1757

  Severity: ERROR\
  Message: The post-operation %s plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s. Processing on this operation will be terminated.

* []()ID: 1759

  Severity: ERROR\
  Message: The post-response %s plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s. Processing on this operation will be terminated.

* []()ID: 1761

  Severity: ERROR\
  Message: The search result entry plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d with entry %s: %s. Processing on this search operation will be terminated.

* []()ID: 1763

  Severity: ERROR\
  Message: The search result reference plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d with referral URL(s) %s: %s. Processing on this search operation will be terminated.

* []()ID: 1765

  Severity: ERROR\
  Message: An attempt was made to register the LastMod plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1766

  Severity: ERROR\
  Message: The LDIF import plugin defined in configuration entry %s threw an exception when it was invoked on entry %s: %s.

* []()ID: 1768

  Severity: ERROR\
  Message: An attempt was made to register the EntryUUID plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1769

  Severity: ERROR\
  Message: An attempt was made to register the password policy import plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1770

  Severity: ERROR\
  Message: An error occurred while attempting to encode a password value stored in attribute %s of user entry %s: %s. Password values for this user will not be encoded.

* []()ID: 1771

  Severity: ERROR\
  Message: The plugin defined in configuration entry %s does not support the %s plugin type.

* []()ID: 1772

  Severity: ERROR\
  Message: The password policy import plugin is not configured any default auth password schemes, and the server does not support the %s auth password scheme.

* []()ID: 1773

  Severity: ERROR\
  Message: Auth password storage scheme %s referenced by the password policy import plugin is not configured for use in the server.

* []()ID: 1774

  Severity: ERROR\
  Message: The password policy import plugin is not configured any default user password schemes, and the server does not support the %s auth password scheme.

* []()ID: 1775

  Severity: ERROR\
  Message: User password storage scheme %s referenced by the password policy import plugin is not configured for use in the server.

* []()ID: 1776

  Severity: WARNING\
  Message: Entry '%s' indicates that it uses custom password policy '%s', but no such policy is defined in the server. Any passwords contained in the entry will be encoded using the default storage schemes, but authentication as this user might not be possible.

* []()ID: 1777

  Severity: WARNING\
  Message: An error occurred while attempting to decode the value of the custom password policy attribute in entry '%s': %s. Any passwords contained in the entry will be encoded using the default storage schemes, but authentication as this user might not be possible.

* []()ID: 1778

  Severity: ERROR\
  Message: The subordinate modify DN plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s. Processing on this operation will be terminated.

* []()ID: 1780

  Severity: ERROR\
  Message: An attempt was made to register the Unique Attribute plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1781

  Severity: ERROR\
  Message: An attempt was made to register the Referential Integrity plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1782

  Severity: ERROR\
  Message: An error occurred during Referential Integrity plugin initialization because log file creation failed: %s.

* []()ID: 1783

  Severity: ERROR\
  Message: An error occurred closing the Referential Integrity plugin update log file: %s.

* []()ID: 1784

  Severity: ERROR\
  Message: An error occurred replacing the Referential Integrity plugin update log file: %s.

* []()ID: 1785

  Severity: INFO\
  Message: The file name that the Referential Integrity plugin logs changes to during background processing has been changed from %s to %s, but this change will not take effect until the server is restarted.

* []()ID: 1786

  Severity: INFO\
  Message: The Referential Integrity plugin background processing update interval has been changed from %s to %s, the new value will now be used during background processing.

* []()ID: 1787

  Severity: INFO\
  Message: The Referential Integrity plugin background processing has been stopped.

* []()ID: 1788

  Severity: INFO\
  Message: The Referential Integrity plugin has started background processing using the update interval %s.

* []()ID: 1789

  Severity: ERROR\
  Message: The Referential Integrity plugin failed when performing an internal search: %s.

* []()ID: 1790

  Severity: ERROR\
  Message: The Referential Integrity plugin failed when performing an internal modify on entry %s: %s.

* []()ID: 1791

  Severity: ERROR\
  Message: The Referential Integrity plugin failed to decode a entry DN from the update log: %s.

* []()ID: 1792

  Severity: INFO\
  Message: The Referential Integrity plugin failed when performing a search because the base DN %s does not exist.

* []()ID: 1793

  Severity: ERROR\
  Message: An error occurred in the Referential Integrity plugin while attempting to configure the attribute type %s which has a syntax OID of %s. A Referential Integrity attribute type must have a syntax OID of either 1.3.6.1.4.1.1466.115.121.1.12 (for the distinguished name syntax) or 1.3.6.1.4.1.1466.115.121.1.34 (for the name and optional uid syntax) or 1.3.6.1.4.1.36733.2.1.3.12 (for the name and json syntax).

* []()ID: 1794

  Severity: ERROR\
  Message: The 7-bit clean plugin is configured with invalid plugin type %s. Only the ldifImport, preOperationAdd, preOperationModify, and preOperationModifyDN plugin types are allowed.

* []()ID: 1795

  Severity: ERROR\
  Message: The modify DN operation would have resulted in a value for attribute %s that was not 7-bit clean.

* []()ID: 1796

  Severity: ERROR\
  Message: The entry included a value for attribute %s that was not 7-bit clean.

* []()ID: 1797

  Severity: ERROR\
  Message: The password policy import plugin references default auth password storage scheme %s which is not available for use in the server.

* []()ID: 1798

  Severity: ERROR\
  Message: The post-synchronization %s plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s.

* []()ID: 1799

  Severity: ERROR\
  Message: A unique attribute conflict was detected for attribute %s: value %s already exists in entry %s.

* []()ID: 1800

  Severity: ERROR\
  Message: A unique attribute conflict was detected for attribute %s during synchronization (connID=%d, opID=%d): value %s in entry %s conflicts with an existing value in entry %s. Manual interaction is required to eliminate the conflict.

* []()ID: 1801

  Severity: ERROR\
  Message: An internal error occurred while attempting to determine whether the operation would have resulted in a unique attribute conflict (result %s, message %s).

* []()ID: 1802

  Severity: ERROR\
  Message: An internal error occurred while attempting to determine whether the synchronization operation (connID=%d, opID=%d) for entry %s would have resulted in a unique attribute conflict (result %s, message %s).

* []()ID: 1803

  Severity: ERROR\
  Message: The referential integrity plugin defined in configuration entry %s is configured to operate on attribute %s but there is no equality index defined for this attribute in backend %s.

* []()ID: 1804

  Severity: ERROR\
  Message: The unique attribute plugin defined in configuration entry %s is configured to operate on attribute %s but there is no equality index defined for this attribute in backend %s.

* []()ID: 1805

  Severity: ERROR\
  Message: An attempt was made to register the Change Number Control plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1806

  Severity: ERROR\
  Message: An attempt was made to register the Change Number Control plugin with the following plugin types : %s. However this plugin must be configured with all of the following plugin types : %s.

* []()ID: 1807

  Severity: ERROR\
  Message: The subordinate delete plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s. Processing on this operation will be terminated.

* []()ID: 1809

  Severity: ERROR\
  Message: An attempt was made to register the Samba password synchronization plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1810

  Severity: ERROR\
  Message: The Samba password synchronization plugin could not encode a password for the following reasons: %s.

* []()ID: 1811

  Severity: ERROR\
  Message: The Samba password synchronization plugin could not process a modification for the following reason: %s.

* []()ID: 1812

  Severity: ERROR\
  Message: Invalid plugin type '%s' for the Attribute Cleanup plugin.

* []()ID: 1813

  Severity: ERROR\
  Message: Attribute '%s' is not defined in the directory schema.

* []()ID: 1814

  Severity: ERROR\
  Message: The attribute '%s' has already been defined in the configuration.

* []()ID: 1815

  Severity: ERROR\
  Message: The mapping '%s:%s' maps the attribute to itself.

* []()ID: 1816

  Severity: ERROR\
  Message: The property 'check-references-filter-criteria' specifies filtering criteria for attribute '%s', but this attribute is not listed in the 'attribute-type' property.

* []()ID: 1817

  Severity: ERROR\
  Message: The filtering criteria '%s' specified in property 'check-references-filter-criteria' is invalid because the filter could not be decoded: '%s'.

* []()ID: 1818

  Severity: ERROR\
  Message: The entry referenced by the value '%s' of the attribute '%s' in the entry '%s' does not exist in any of the configured naming contexts.

* []()ID: 1819

  Severity: ERROR\
  Message: The entry referenced by the value '%s' of the attribute '%s' in the entry '%s' does not match the filter '%s'.

* []()ID: 1820

  Severity: ERROR\
  Message: The entry referenced by the value '%s' of the attribute '%s' in the entry '%s' does not belong to any of the configured naming contexts.

* []()ID: 1821

  Severity: ERROR\
  Message: The operation could not be processed due to an unexpected exception: '%s'.

* []()ID: 1822

  Severity: ERROR\
  Message: An attempt was made to register the Graphite Monitor Reporter Plugin plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1823

  Severity: ERROR\
  Message: Unable to report metrics to Graphite server '%s' because the Graphite server hostname resolution has failed. Ensure that the plugin configuration is correct and that the Graphite server is reachable. The Graphite plugin will be disabled until a change is performed in its configuration or the server restart.

* []()ID: 1824

  Severity: ERROR\
  Message: The referential integrity plugin defined in configuration entry %s is configured to operate on attribute %s but there is no %s extensible matching rule index defined for this attribute in backend %s.

* []()ID: 1825

  Severity: ERROR\
  Message: An attempt was made to register the Entity Tag plugin to be invoked as a %s plugin. This plugin type is not allowed for this plugin.

* []()ID: 1826

  Severity: ERROR\
  Message: The post-commit %s plugin defined in configuration entry %s threw an exception when it was invoked for connection %d operation %d: %s.

* []()ID: 1829

  Severity: INFO\
  Message: The Directory Server is closing the connection to this client.

* []()ID: 1830

  Severity: WARNING\
  Message: The Directory Server is currently in the process of closing this client connection.

* []()ID: 1831

  Severity: ERROR\
  Message: The connection attempt from client %s to %s has been rejected because the client was included in one of the denied address ranges.

* []()ID: 1832

  Severity: ERROR\
  Message: The connection attempt from client %s to %s has been rejected because the client was not included in one of the allowed address ranges.

* []()ID: 1834

  Severity: ERROR\
  Message: Terminating this connection because the client sent an invalid message of type %s (LDAP message ID %d) that is not allowed for request messages.

* []()ID: 1841

  Severity: ERROR\
  Message: The Directory Server has been configured to deny access to LDAPv2 clients. This connection will be closed.

* []()ID: 1842

  Severity: ERROR\
  Message: The client with connection ID %d authenticated to the Directory Server using LDAPv2, but attempted to send an extended operation request (LDAP message ID %d), which is not allowed for LDAPv2 clients. The connection will be terminated.

* []()ID: 1843

  Severity: ERROR\
  Message: The attempt to register this connection with the Directory Server was rejected. This indicates that the server already has the maximum allowed number of concurrent connections established.

* []()ID: 1844

  Severity: INFO\
  Message: You have to rebuild the '%s' index(es) manually to get a fully functional server.

* []()ID: 1845

  Severity: NOTICE\
  Message: Started listening for new connections on %s.

* []()ID: 1846

  Severity: NOTICE\
  Message: Stopped listening for new connections on %s.

* []()ID: 1847

  Severity: ERROR\
  Message: User %s specified in the proxied authorization V1 control does not exist in the Directory Server.

* []()ID: 1848

  Severity: ERROR\
  Message: Unable to process proxied authorization V2 control because it contains an authorization ID based on a username and no proxied authorization identity mapper is configured in the Directory Server.

* []()ID: 1849

  Severity: ERROR\
  Message: The authorization ID "%s" contained in the proxied authorization V2 control is invalid because it does not start with "dn:" to indicate a user DN or "u:" to indicate a username.

* []()ID: 1850

  Severity: ERROR\
  Message: User %s specified in the proxied authorization V2 control does not exist in the Directory Server.

* []()ID: 1851

  Severity: WARNING\
  Message: The Directory Server is already processing another request on the same client connection with the same message ID of %d.

* []()ID: 1852

  Severity: ERROR\
  Message: Use of the proxied authorization V1 control for user %s is not allowed by the password policy configuration.

* []()ID: 1853

  Severity: INFO\
  Message: Unable to process the provided server-side sort request control because it included attribute %s which does not have a default ordering matching rule and no ordering rule was specified in the sort key.

* []()ID: 1854

  Severity: ERROR\
  Message: LDAPv2 clients are not allowed to use request controls.

* []()ID: 1857

  Severity: ERROR\
  Message: User %s does not exist in the directory.

* []()ID: 1858

  Severity: WARNING\
  Message: The value %s specified as the LDIF directory path for the LDIF connection handler defined in configuration entry %s exists but is not a directory. The specified path must be a directory. The LDIF connection handler will start, but will not be able to proces any changes until this path is changed to a directory.

* []()ID: 1859

  Severity: WARNING\
  Message: The directory %s referenced by the LDIF connection handler defined in configuration entry %s does not exist. The LDIF connection handler will start, but will not be able to process any changes until this directory is created.

* []()ID: 1860

  Severity: ERROR\
  Message: An error occurred while trying to read a change record from the LDIF file: %s. This change will be skipped but processing on the LDIF file will continue.

* []()ID: 1861

  Severity: ERROR\
  Message: An error occurred while trying to read a change record from the LDIF file: %s. No further processing on this LDIF file can be performed.

* []()ID: 1862

  Severity: INFO\
  Message: Result Code: %d (%s).

* []()ID: 1863

  Severity: INFO\
  Message: Additional Info: %s.

* []()ID: 1864

  Severity: INFO\
  Message: Matched DN: %s.

* []()ID: 1865

  Severity: INFO\
  Message: Referral URL: %s.

* []()ID: 1866

  Severity: ERROR\
  Message: An I/O error occurred while the LDIF connection handler was processing LDIF file %s: %s.

* []()ID: 1867

  Severity: ERROR\
  Message: An error occurred while the LDIF connection handler was attempting to rename partially-processed file from %s to %s: %s.

* []()ID: 1868

  Severity: ERROR\
  Message: An error occurred while the LDIF connection handler was attempting to delete processed file %s: %s.

* []()ID: 1869

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the SSL context for use in the %s Connection Handler: %s.

* []()ID: 1870

  Severity: ERROR\
  Message: The Directory Server does not support LDAP protocol version %d. This connection will be closed.

* []()ID: 1871

  Severity: ERROR\
  Message: Cannot decode the provided control %s because an error occurred while attempting to decode the control value: %s.

* []()ID: 1875

  Severity: ERROR\
  Message: The server received configuration changes that require a restart of the %s connection handler to take effect.

* []()ID: 1876

  Severity: ERROR\
  Message: Authorization as '%s' specified in the proxied authorization control is not permitted.

* []()ID: 1877

  Severity: ERROR\
  Message: The key with alias '%s' used by '%s' could not be found, which may cause subsequent SSL connections to fail. Verify that the underlying keystore is properly configured.

* []()ID: 1878

  Severity: ERROR\
  Message: No usable key was found for '%s', which may cause subsequent SSL connections to fail. Verify that the underlying keystore is properly configured.

* []()ID: 1879

  Severity: ERROR\
  Message: Use of the proxied authorization V2 control for user %s is not allowed: the account is disabled.

* []()ID: 1880

  Severity: ERROR\
  Message: Use of the proxied authorization V2 control for user %s is not allowed: the account is expired.

* []()ID: 1881

  Severity: ERROR\
  Message: Use of the proxied authorization V2 control for user %s is not allowed: the account is locked.

* []()ID: 1882

  Severity: ERROR\
  Message: Use of the proxied authorization V2 control for user %s is not allowed: the account's password is expired.

* []()ID: 1889

  Severity: ERROR\
  Message: Unable to process the provided internal modifications request control because it did not contain an origin.

* []()ID: 1890

  Severity: ERROR\
  Message: Unable to process the provided internal modifications request control because it did not contain modifications.

* []()ID: 1891

  Severity: ERROR\
  Message: Unable to process the provided replication context request control because it did not contain a CSN.

* []()ID: 1892

  Severity: ERROR\
  Message: Unable to process the provided replication context request control because it did not contain an entry UUID.

* []()ID: 1895

  Severity: ERROR\
  Message: No result received after completion for request '%s' received for internal client connection.

* []()ID: 1896

  Severity: INFO\
  Message: Internal operations can't be cancelled.

* []()ID: 1902

  Severity: ERROR\
  Message: Could not write data to the client for %s.

* []()ID: 1903

  Severity: ERROR\
  Message: The connection attempt from client %s to %s has been rejected because there are too many open connections from this client.

* []()ID: 1904

  Severity: ERROR\
  Message: Unable to process the provided server-side sort request control: %s.

* []()ID: 1905

  Severity: ERROR\
  Message: An error occurred during multi-stage authentication: '%s'.

* []()ID: 1906

  Severity: ERROR\
  Message: Unable to process HTTP request '%s': %s.

* []()ID: 1907

  Severity: ERROR\
  Message: Unable to write HTTP response to the client '%s': %s.

* []()ID: 1908

  Severity: ERROR\
  Message: Error while starting the HTTP application: %s.

* []()ID: 1912

  Severity: ERROR\
  Message: LDAP connection %s has been closed because the LDAP connection handler %s is shutting down.

* []()ID: 1913

  Severity: ERROR\
  Message: The key with alias '%s' used by '%s' is not valid yet. The key will be used, but SSL connections may fail depending on the validation performed by the peer. Verify that the underlying keystore is properly configured with a valid key.

* []()ID: 1914

  Severity: ERROR\
  Message: The key with alias '%s' used by '%s' has expired. The key will be used, but SSL connections may fail depending on the validation performed by the peer. Verify that the underlying keystore is properly configured with a valid key.

* []()ID: 1915

  Severity: ERROR\
  Message: The connection attempt from client '%s' to '%s' has been rejected because the proxy protocol header indicated that the client used SSL but the header does not specify which SSL cipher was used. The proxy should be configured to transmit all SSL headers.

* []()ID: 1916

  Severity: ERROR\
  Message: The configured DN is already used by another domain.

* []()ID: 1917

  Severity: ERROR\
  Message: Replication Server failed to start : could not bind to the listen port : %d. Error : %s.

* []()ID: 1918

  Severity: ERROR\
  Message: Unknown operation type : %s.

* []()ID: 1919

  Severity: ERROR\
  Message: Internal Error : Operation %s change number %s was not found in local change list.

* []()ID: 1920

  Severity: ERROR\
  Message: Internal Error : Operation %s change number %s was not found in remote change list.

* []()ID: 1921

  Severity: ERROR\
  Message: The replication server failed to start because the database %s could not be read : %s.

* []()ID: 1922

  Severity: ERROR\
  Message: An Exception was caught while replaying operation %s %s (%s) : %s.

* []()ID: 1923

  Severity: NOTICE\
  Message: Error %s when updating server state %s : %s base dn : %s.

* []()ID: 1924

  Severity: ERROR\
  Message: Error %s when searching for server state %s : %s base dn : %s.

* []()ID: 1925

  Severity: ERROR\
  Message: Caught IOException while sending topology info (for update) on domain %s for %s server %s : %s.

* []()ID: 1926

  Severity: ERROR\
  Message: Error when searching old changes from the database for base DN %s: %s.

* []()ID: 1927

  Severity: ERROR\
  Message: Error trying to replay %s, operation could not be decoded: %s.

* []()ID: 1928

  Severity: ERROR\
  Message: Error during the Replication Server database trimming or flush process. The Changelog service is going to shutdown: %s.

* []()ID: 1929

  Severity: ERROR\
  Message: An unexpected error happened handling connection with %s. This connection is going to be closed.

* []()ID: 1930

  Severity: ERROR\
  Message: A loop was detected while replaying operation: %s %s (%s) error %s.

* []()ID: 1931

  Severity: ERROR\
  Message: An Exception was caught while testing existence or trying to create the directory for the Replication Server database : %s %s.

* []()ID: 1932

  Severity: ERROR\
  Message: The current request is rejected due to an import or an export already in progress for the same data.

* []()ID: 1933

  Severity: ERROR\
  Message: On domain %s, initialization of server with serverId:%s has been requested from a server with an invalid serverId:%s. %s.

* []()ID: 1934

  Severity: ERROR\
  Message: Invalid target for the export.

* []()ID: 1935

  Severity: ERROR\
  Message: Domain %s: the server with serverId=%s is unreachable.

* []()ID: 1936

  Severity: ERROR\
  Message: No domain matches the provided base DN '%s'.

* []()ID: 1937

  Severity: ERROR\
  Message: Multiple domains match the base DN provided.

* []()ID: 1938

  Severity: ERROR\
  Message: The provider class does not allow the operation requested.

* []()ID: 1939

  Severity: NOTICE\
  Message: Exception when reading messages from %s: %s.

* []()ID: 1940

  Severity: ERROR\
  Message: Duplicate server IDs found: replica '%s' for domain '%s' tried to connect from '%s', but replica '%s' is already connected from '%s'. Make sure the two replicas are configured with different server IDs.

* []()ID: 1941

  Severity: ERROR\
  Message: Duplicate server IDs found: replication server '%s' tried to connect from '%s', but replication server '%s' is already connected from '%s'. Make sure the two replication servers are configured with different server IDs.

* []()ID: 1942

  Severity: ERROR\
  Message: Entry %s was containing some unknown historical information, This may cause some inconsistency for this entry.

* []()ID: 1943

  Severity: ERROR\
  Message: A conflict was detected but the conflict information could not be added to entry %s. Conflict with %s %s, Result: %s.

* []()ID: 1944

  Severity: ERROR\
  Message: An error happened trying to rename a conflicting entry. DN: %s, Operation: %s, Result: %s.

* []()ID: 1945

  Severity: ERROR\
  Message: The Replication is configured for suffix %s but was not able to connect to any Replication Server.

* []()ID: 1946

  Severity: ERROR\
  Message: An unexpected error occurred while sending an Error Message to %s. This connection is going to be closed and reopened.

* []()ID: 1947

  Severity: ERROR\
  Message: An unexpected error occurred while sending a Message to %s. This connection is going to be closed and reopened.

* []()ID: 1948

  Severity: ERROR\
  Message: Could not replay operation %s %s with ChangeNumber %s error %s %s.

* []()ID: 1949

  Severity: ERROR\
  Message: The entry %s has historical information for attribute %s which is not defined in the schema. This information will be ignored.

* []()ID: 1950

  Severity: ERROR\
  Message: The Replication Server socket could not be closed : %s.

* []()ID: 1951

  Severity: ERROR\
  Message: The thread listening on the replication server port could not be stopped : %s.

* []()ID: 1952

  Severity: ERROR\
  Message: An unexpected error occurred when loading the generation id of domain "%s": %s.

* []()ID: 1953

  Severity: ERROR\
  Message: An unexpected error occurred when looking for the replicated backend : %s. It may be not configured or disabled.

* []()ID: 1954

  Severity: ERROR\
  Message: An unexpected error occurred when searching in %s for the generation ID : %s.

* []()ID: 1955

  Severity: ERROR\
  Message: An unexpected error occurred when updating generation ID for domain "%s": %s.

* []()ID: 1956

  Severity: ERROR\
  Message: The following error has been received : %s.

* []()ID: 1957

  Severity: ERROR\
  Message: Initialization cannot be done because import is not supported by the backend %s.

* []()ID: 1958

  Severity: ERROR\
  Message: Initialization cannot be done because export is not supported by the backend %s.

* []()ID: 1959

  Severity: ERROR\
  Message: Initialization cannot be done because the following error occurred while locking the backend %s : %s.

* []()ID: 1960

  Severity: ERROR\
  Message: Replication server caught exception while listening for client connections: %s.

* []()ID: 1961

  Severity: ERROR\
  Message: While clearing the database %s, the following error happened: %s.

* []()ID: 1962

  Severity: ERROR\
  Message: An unexpected error occurred when testing existence or creating the replication backend : %s.

* []()ID: 1963

  Severity: ERROR\
  Message: An error occurred when searching for %s : %s.

* []()ID: 1964

  Severity: ERROR\
  Message: The base DN %s is not stored by any of the Directory Server backend.

* []()ID: 1965

  Severity: ERROR\
  Message: An Exception was caught while replaying replication message : %s.

* []()ID: 1966

  Severity: ERROR\
  Message: Caught exception publishing fake operations for domain %s : %s.

* []()ID: 1967

  Severity: NOTICE\
  Message: ServerState recovery for domain %s, updated with changeNumber %s.

* []()ID: 1968

  Severity: ERROR\
  Message: For replicated domain %s, in server with serverId=%s, the generation ID could not be set to value %s in the rest of the topology because this server is NOT connected to any replication server. You should check in the configuration that the domain is enabled and that there is one replication server up and running.

* []()ID: 1969

  Severity: ERROR\
  Message: DN sent by remote replication server: %s does not match local replication server one: %s.

* []()ID: 1970

  Severity: ERROR\
  Message: DN sent by replication server: %s does not match local directory server one: %s.

* []()ID: 1971

  Severity: ERROR\
  Message: Caught IOException while forwarding ResetGenerationIdMsg to peer replication servers for domain %s : %s.

* []()ID: 1972

  Severity: ERROR\
  Message: Replication server received invalid initial status: %s for replication domain %s from server id %s.

* []()ID: 1973

  Severity: ERROR\
  Message: Received invalid requested status %s in DS replication domain %s with server id %s.

* []()ID: 1974

  Severity: ERROR\
  Message: Could not compute new status in RS replication domain %s for server id %s. Was in %s status and received %s event.

* []()ID: 1975

  Severity: ERROR\
  Message: Could not compute new status in DS replication domain %s with server id %s. Was in %s status and received %s event.

* []()ID: 1976

  Severity: ERROR\
  Message: Caught IOException while changing status for domain %s and serverId: %s after reset for generation id: %s.

* []()ID: 1977

  Severity: ERROR\
  Message: Received change status message does not come from a directory server (dn: %s, server id: %s, msg: %s).

* []()ID: 1978

  Severity: ERROR\
  Message: Received invalid new status %s in RS for replication domain %s and directory server id %s.

* []()ID: 1979

  Severity: WARNING\
  Message: Connected to a replication server with wrong group id. We have group id %s and replication server id %s %s has group id %s. This is for domain %s in directory server %s.

* []()ID: 1980

  Severity: ERROR\
  Message: Replication broker with dn %s and server id %s failed to signal status change because of: %s.

* []()ID: 1982

  Severity: NOTICE\
  Message: Ignoring reset generation ID request from '%s' to '%s' for replica '%s' because the replica is being re-initialized.

* []()ID: 1983

  Severity: ERROR\
  Message: The generation ID could not be reset for domain %s.

* []()ID: 1984

  Severity: NOTICE\
  Message: Cannot change the configuration while a total update is in progress.

* []()ID: 1985

  Severity: ERROR\
  Message: The Replication was not started on base-dn %s : %s.

* []()ID: 1986

  Severity: ERROR\
  Message: Replication protocol error. Bad message type. %s received, %s required.

* []()ID: 1987

  Severity: NOTICE\
  Message: Wrong fractional replication configuration: could not find object class definition for %s in schema.

* []()ID: 1988

  Severity: NOTICE\
  Message: Wrong fractional replication configuration : could not find attribute type definition for %s in schema.

* []()ID: 1989

  Severity: NOTICE\
  Message: Wrong fractional replication configuration : attribute %s is not optional in class %s.

* []()ID: 1990

  Severity: NOTICE\
  Message: Wrong fractional replication configuration : wrong format : %s (need at least \[\<className>|\*],attributeName).

* []()ID: 1991

  Severity: NOTICE\
  Message: Wrong fractional replication configuration : cannot use both exclusive and inclusive modes.

* []()ID: 1992

  Severity: NOTICE\
  Message: Wrong fractional replication configuration : prohibited attribute %s usage.

* []()ID: 1993

  Severity: NOTICE\
  Message: Fractional replication : exception for domain : %s : %s.

* []()ID: 1994

  Severity: NOTICE\
  Message: Warning : domain %s fractional replication configuration is inconsistent with backend data set : need resynchronization or fractional configuration to be changed.

* []()ID: 1995

  Severity: ERROR\
  Message: The fractional replication ldif import plugin is configured with invalid plugin type %s. Only the ldifImport plugin type is allowed.

* []()ID: 1996

  Severity: NOTICE\
  Message: The online full update for importing suffix %s data from remote directory server %s has been stopped due to fractional configuration inconsistency between destination and source server : imported data set has not the same fractional configuration.

* []()ID: 1997

  Severity: NOTICE\
  Message: The online full update for importing suffix %s data from remote directory server %s has been stopped due to fractional configuration inconsistency between destination and source server : imported data set has some fractional configuration but not destination server.

* []()ID: 1998

  Severity: NOTICE\
  Message: The following operation has been forbidden in suffix %s due to inconsistency with the fractional replication configuration : %s.

* []()ID: 1999

  Severity: NOTICE\
  Message: The export of domain %s from server %s to all other servers of the topology is forbidden as the source server has some fractional configuration : only fractional servers in a replicated topology does not make sense.

* []()ID: 2000

  Severity: ERROR\
  Message: An error occurred when accessing the change number database : %s.

## IDs: 2001-2500

* []()ID: 2001

  Severity: ERROR\
  Message: The initialization failed because the domain %s is not connected to a replication server.

* []()ID: 2002

  Severity: ERROR\
  Message: Could not retrieve the configuration for a replication domain matching the entry %s.

* []()ID: 2003

  Severity: NOTICE\
  Message: The LDIF import for importing suffix %s data has been stopped due to fractional configuration inconsistency : imported data set has not the same fractional configuration as local server.

* []()ID: 2004

  Severity: NOTICE\
  Message: The LDIF import for importing suffix %s data has been stopped due to fractional configuration inconsistency : imported data set has some fractional configuration but not local server.

* []()ID: 2005

  Severity: WARNING\
  Message: A transient problem occurred while Directory Server %s was connecting to this Replication Server %s. The peer server may try to establish a connection again. The problem was: %s.

* []()ID: 2006

  Severity: WARNING\
  Message: A transient problem occurred while Replication Server %s was connecting to this Replication Server %s. The Replication Server should try to reconnect later. The problem was: %s.

* []()ID: 2007

  Severity: NOTICE\
  Message: Error when loading a virtual attribute for external change log: Attribute: %s , Error: %s.

* []()ID: 2008

  Severity: ERROR\
  Message: Full resync required. Reason: The provided cookie contains unknown replicated domain %s. Current starting cookie <%s>.

* []()ID: 2009

  Severity: ERROR\
  Message: Full resync required. Reason: The provided cookie is older than the start of historical in the server for the replicated domain : %s.

* []()ID: 2010

  Severity: ERROR\
  Message: Invalid syntax for the provided cookie '%s'.

* []()ID: 2011

  Severity: ERROR\
  Message: Domain %s (server id: %s) : remote exporter server disconnection (server id: %s ) detected during initialization.

* []()ID: 2012

  Severity: ERROR\
  Message: During initialization from a remote server, the following error occurred : %s.

* []()ID: 2013

  Severity: ERROR\
  Message: Connection failure with Replication Server %s during import.

* []()ID: 2014

  Severity: ERROR\
  Message: Bad msg id sequence during import. Expected:%s Actual:%s.

* []()ID: 2015

  Severity: ERROR\
  Message: The following servers did not acknowledge initialization in the expected time for domain %s. They are potentially down or too slow. Servers list: %s.

* []()ID: 2016

  Severity: ERROR\
  Message: The following servers did not end initialization being connected with the right generation (%s). They are potentially stopped or too slow. Servers list: %s.

* []()ID: 2017

  Severity: ERROR\
  Message: When initializing remote server(s), connection to Replication Server with serverId=%s is lost.

* []()ID: 2018

  Severity: ERROR\
  Message: When initializing remote server(s), the initialized server with serverId=%s is potentially stopped or too slow.

* []()ID: 2019

  Severity: ERROR\
  Message: When sending a new initialization request for an initialization from a remote server, the following error occurred %s. The initial error was : %s.

* []()ID: 2020

  Severity: NOTICE\
  Message: Resending a new initialization request for an initialization from a remote server due to the root error : %s.

* []()ID: 2021

  Severity: ERROR\
  Message: Error while trying to solve conflict with DN : %s ERROR : %s.

* []()ID: 2022

  Severity: NOTICE\
  Message: Replication server RS(%s) started listening for new connections on address %s port %d.

* []()ID: 2023

  Severity: INFO\
  Message: Replication server RS(%s) has connected to replication server RS(%s) for domain "%s" at %s.

* []()ID: 2024

  Severity: INFO\
  Message: Replication server RS(%s) has accepted a connection from replication server RS(%s) for domain "%s" at %s.

* []()ID: 2025

  Severity: INFO\
  Message: Replication server RS(%s) has accepted a connection from directory server DS(%s) for domain "%s" at %s.

* []()ID: 2026

  Severity: NOTICE\
  Message: Directory server DS(%s) has connected to replication server RS(%s) for domain "%s" at %s with generation ID %s.

* []()ID: 2027

  Severity: WARNING\
  Message: Directory server DS(%s) has connected to replication server RS(%s) for domain "%s" at %s, but the generation IDs do not match, indicating that a full re-initialization is required. The local (DS) generation ID is %s and the remote (RS) generation ID is %s.

* []()ID: 2028

  Severity: WARNING\
  Message: Directory server DS(%s) was unable to connect to any of the following replication servers for domain "%s": %s.

* []()ID: 2029

  Severity: WARNING\
  Message: Directory server DS(%s) was unable to connect to any replication servers for domain "%s".

* []()ID: 2030

  Severity: WARNING\
  Message: Replication server RS(%s) at %s has closed the connection to this directory server DS(%s). This directory server will now try to connect to another replication server in order to receive changes for the domain "%s".

* []()ID: 2031

  Severity: WARNING\
  Message: Directory server DS(%s) encountered an error while receiving changes for domain "%s" from replication server RS(%s) at %s. The connection will be closed, and this directory server will now try to connect to another replication server. The error was: %s.

* []()ID: 2032

  Severity: NOTICE\
  Message: Directory Server DS(%s) is switching from replication server RS(%s) at %s to RS(%s) for domain "%s" because it is more suitable. The previous replication server evaluation was: "%s", and the new replication server evaluation was: "%s".

* []()ID: 2033

  Severity: NOTICE\
  Message: Starting total update: importing domain "%s" from remote directory server DS(%s) to this directory server DS(%s).

* []()ID: 2034

  Severity: NOTICE\
  Message: Finished total update: imported domain "%s" from remote directory server DS(%s) to this directory server DS(%s). %s.

* []()ID: 2035

  Severity: NOTICE\
  Message: Starting total update: exporting %d entries in domain "%s" from this directory server DS(%s) to remote directory server DS(%s).

* []()ID: 2036

  Severity: NOTICE\
  Message: Starting total update: exporting %d entries in domain "%s" from this directory server DS(%s) to all remote directory servers.

* []()ID: 2037

  Severity: NOTICE\
  Message: Finished total update: exported domain "%s" from this directory server DS(%s) to remote directory server DS(%s). %s.

* []()ID: 2038

  Severity: NOTICE\
  Message: Finished total update: exported domain "%s" from this directory server DS(%s) to all remote directory servers. %s.

* []()ID: 2039

  Severity: NOTICE\
  Message: Directory server DS(%s) for domain "%s" has changed its status to %s.

* []()ID: 2040

  Severity: WARNING\
  Message: Directory server DS(%s) is closing its connection to replication server RS(%s) at %s for domain "%s" because it could not detect a heart beat.

* []()ID: 2041

  Severity: WARNING\
  Message: Replication server RS(%s) at %s presented generation ID %s for domain "%s", but the generation ID of this replication server RS(%s) is %s. This usually indicates that one or more directory servers in the replication topology have not been initialized with the same data, and re-initialization is required.

* []()ID: 2042

  Severity: NOTICE\
  Message: The generation ID for domain "%s" has been reset to %s.

* []()ID: 2043

  Severity: WARNING\
  Message: Timed out while trying to acquire the domain lock for domain "%s". The connection attempt from replication server RS(%s) at %s to this replication server RS(%s) will be aborted. This is probably benign and a result of a simultaneous cross connection attempt.

* []()ID: 2044

  Severity: WARNING\
  Message: Directory server DS(%s) at %s presented generation ID %s for domain "%s", but the generation ID of this replication server RS(%s) is %s. This usually indicates that one or more directory servers in the replication topology have not been initialized with the same data, and re-initialization is required.

* []()ID: 2045

  Severity: NOTICE\
  Message: Replication server RS(%s) ignoring update %s for domain "%s" from replication server RS(%s) at %s because its generation ID %s is different to the local generation ID %s.

* []()ID: 2046

  Severity: WARNING\
  Message: Replication server RS(%s) not sending update %s for domain "%s" to replication server RS(%s) at %s because its generation ID %s is different to the local generation ID %s.

* []()ID: 2047

  Severity: WARNING\
  Message: Replication server RS(%s) ignoring update %s for domain "%s" from directory server DS(%s) at %s because its generation ID %s is different to the local generation ID %s.

* []()ID: 2048

  Severity: WARNING\
  Message: Replication server RS(%s) not sending update %s for domain "%s" to directory server DS(%s) at %s because its generation ID %s is different to the local generation ID %s.

* []()ID: 2049

  Severity: WARNING\
  Message: Replication server RS(%s) ignoring update %s for domain "%s" from directory server DS(%s) at %s because it is currently performing a full update.

* []()ID: 2050

  Severity: WARNING\
  Message: Replication server RS(%s) not sending update %s for domain "%s" to directory server DS(%s) at %s because it is currently performing a full update.

* []()ID: 2051

  Severity: ERROR\
  Message: The connection from this replication server RS(%s) to replication server RS(%s) at %s for domain "%s" has failed.

* []()ID: 2052

  Severity: ERROR\
  Message: The connection from this replication server RS(%s) to directory server DS(%s) at %s for domain "%s" has failed.

* []()ID: 2053

  Severity: WARNING\
  Message: Directory server DS(%s) was unable to connect to replication server %s for domain "%s". Please check that there is a replication server listening at this address.

* []()ID: 2054

  Severity: WARNING\
  Message: Directory server DS(%s) timed out while connecting to replication server %s for domain "%s".

* []()ID: 2055

  Severity: ERROR\
  Message: Directory server DS(%s) encountered an unexpected error while connecting to replication server %s for domain "%s": %s.

* []()ID: 2056

  Severity: WARNING\
  Message: Directory server DS(%s) encountered a transient problem while connecting to replication server %s for domain "%s". Directory server will try to connect to a replication server again. The problem was: %s.

* []()ID: 2057

  Severity: INFO\
  Message: Replication server accepted a connection from %s to local address %s but the SSL handshake failed. This is probably benign, but may indicate a transient network outage or a misconfigured client application connecting to this replication server. The error was: %s.

* []()ID: 2058

  Severity: NOTICE\
  Message: Directory Server DS(%s) is disconnecting from replication server RS(%s) at %s for domain "%s" in order to find another replication server in the topology and distribute load more equally.

* []()ID: 2059

  Severity: WARNING\
  Message: The attribute value '%s' is not a valid synchronization history value.

* []()ID: 2060

  Severity: WARNING\
  Message: Cannot open database %s because shutdown was requested from replication server RS(%s).

* []()ID: 2061

  Severity: NOTICE\
  Message: RS(%s) has no generation Id, but at least one other RS has the same generation Id %s as DS(%s).

* []()ID: 2062

  Severity: NOTICE\
  Message: RS(%s) generation Id %s does not match DS(%s) generation Id %s, but at least another RS does.

* []()ID: 2063

  Severity: NOTICE\
  Message: RS(%s) groupId '%s' does not match DS(%s) groupId '%s', but at least one other RS does.

* []()ID: 2064

  Severity: NOTICE\
  Message: RS(%s) newest change %s is behind DS(%s) newest change %s, but at least another RS is at the same point or ahead of the DS.

* []()ID: 2065

  Severity: NOTICE\
  Message: RS(%s) newest change %s is behind another RS which is ahead of DS(%s) newest change %s.

* []()ID: 2066

  Severity: NOTICE\
  Message: RS(%s) is not on the same virtual machine as DS(%s) but another RS is.

* []()ID: 2067

  Severity: NOTICE\
  Message: RS(%s) is on a different host than DS(%s), but at least another RS is on the same host.

* []()ID: 2068

  Severity: NOTICE\
  Message: DS(%s) disconnected from overloaded RS(%s).

* []()ID: 2069

  Severity: NOTICE\
  Message: DS(%s) not disconnected from overloaded RS(%s), other DSs will disconnect.

* []()ID: 2070

  Severity: NOTICE\
  Message: DS(%s) not disconnected from current RS(%s), since there is no need to rebalance all directory servers to other replication servers in the topology.

* []()ID: 2071

  Severity: NOTICE\
  Message: DS(%s) not disconnected from current RS(%s), because RS is underloaded or its load goal is reached.

* []()ID: 2072

  Severity: NOTICE\
  Message: DS(%s) will connect to RS(%s) because it has the biggest weight among all the replication servers.

* []()ID: 2073

  Severity: NOTICE\
  Message: DS(%s) stayed connected to RS(%s) to avoid the yoyo effect.

* []()ID: 2074

  Severity: NOTICE\
  Message: RS(%s) has been evaluated to be the best replication server for DS(%s) to connect to because it was the only one standing after all tests.

* []()ID: 2075

  Severity: NOTICE\
  Message: RS(%s) could not be contacted by DS(%s).

* []()ID: 2076

  Severity: ERROR\
  Message: Could not create replica database because the changelog database is shutting down.

* []()ID: 2077

  Severity: ERROR\
  Message: Could not add change %s to replicaDB %s %s because flushing thread is shutting down.

* []()ID: 2078

  Severity: ERROR\
  Message: Error when retrieving changelog state from root path '%s' : IO error on domain directory '%s' when retrieving list of server ids.

* []()ID: 2079

  Severity: ERROR\
  Message: Could not get or create replica DB for base DN '%s', serverId '%s', generationId '%s': %s.

* []()ID: 2080

  Severity: ERROR\
  Message: Could not get or create change number index DB in root path '%s', using path '%s': %s.

* []()ID: 2081

  Severity: ERROR\
  Message: Could not delete generation id file '%s' for DN '%s': %s.

* []()ID: 2082

  Severity: ERROR\
  Message: Could not create directory '%s' for server id %s: %s.

* []()ID: 2083

  Severity: ERROR\
  Message: Could not create generation id file '%s': %s.

* []()ID: 2084

  Severity: ERROR\
  Message: Could not read server id filename because it uses a wrong format, expecting '\[id].server' where \[id] is numeric but got '%s'.

* []()ID: 2085

  Severity: ERROR\
  Message: Could not read generation id because it uses a wrong format, expecting a number but got '%s'.

* []()ID: 2086

  Severity: ERROR\
  Message: Could not open log file '%s' for write: %s.

* []()ID: 2087

  Severity: ERROR\
  Message: Could not open a reader on log file '%s': %s.

* []()ID: 2088

  Severity: ERROR\
  Message: Could not decode a record from data read in log file '%s'.

* []()ID: 2089

  Severity: ERROR\
  Message: Could not delete log files: %s.

* []()ID: 2090

  Severity: ERROR\
  Message: Could not create log file '%s': %s.

* []()ID: 2091

  Severity: WARNING\
  Message: The changelog '%s' has been opened in read-only mode, it is not enabled for write.

* []()ID: 2092

  Severity: ERROR\
  Message: Could not add record '%s' in log file '%s': %s.

* []()ID: 2093

  Severity: ERROR\
  Message: Could not synchronize written records to file system for log file '%s': %s.

* []()ID: 2094

  Severity: ERROR\
  Message: Could not seek to position %d for reader on log file '%s'.

* []()ID: 2095

  Severity: ERROR\
  Message: Could not create root directory '%s' for log file: %s.

* []()ID: 2096

  Severity: ERROR\
  Message: Could not decode DN from domain state file '%s', from line '%s'.

* []()ID: 2097

  Severity: ERROR\
  Message: Could not read domain state file '%s'. The replication server cannot continue, it should be restored from a backup. Cause was : %s.

* []()ID: 2098

  Severity: ERROR\
  Message: There is a mismatch between domain state file and actual domain directories found in file system. Expected domain ids : %s. Actual domain ids found in file system: %s.

* []()ID: 2099

  Severity: ERROR\
  Message: Could not create a new domain id %s for domain DN %s and save it in the domain state file. Replication will continue, but if the domain state file cannot be written when stopping the server, it should be restored from backup. Cause was : %s.

* []()ID: 2100

  Severity: ERROR\
  Message: Could not decode the key from string \[%s].

* []()ID: 2101

  Severity: ERROR\
  Message: Could not initialize the log '%s' : %s.

* []()ID: 2102

  Severity: ERROR\
  Message: Could not retrieve key bounds from log file '%s': %s.

* []()ID: 2103

  Severity: ERROR\
  Message: Could not retrieve read-only log files from log '%s': %s.

* []()ID: 2104

  Severity: ERROR\
  Message: While purging log, could not delete log file(s): '%s'.

* []()ID: 2106

  Severity: ERROR\
  Message: Could not read replica offline state file '%s' for domain %s, it should contain exactly one line corresponding to the offline CSN.

* []()ID: 2107

  Severity: ERROR\
  Message: Could not read content of replica offline state file '%s' for domain %s.

* []()ID: 2108

  Severity: ERROR\
  Message: Could not retrieve file length of log file '%s'.

* []()ID: 2109

  Severity: ERROR\
  Message: An error occurred while recovering the replication change log file '%s'. The recovery has been aborted and this replication server will be removed from the replication topology. The change log file system may be read-only, full, or corrupt and must be fixed before this replication server can be used. The underlying error was: %s.

* []()ID: 2110

  Severity: INFO\
  Message: Log file '%s' was successfully recovered by removing unreadable records. The file changed size from %d to %d bytes.

* []()ID: 2111

  Severity: NOTICE\
  Message: You do not have sufficient privileges to perform a search request on cn=changelog.

* []()ID: 2112

  Severity: ERROR\
  Message: An error occurred when searching base DN '%s' with filter '%s' in changelog backend : %s.

* []()ID: 2113

  Severity: ERROR\
  Message: An error occurred when retrieving attribute value for attribute '%s' for entry DN '%s' in changelog backend : %s.

* []()ID: 2114

  Severity: ERROR\
  Message: Could not create file '%s' to store last log rotation time %d.

* []()ID: 2115

  Severity: ERROR\
  Message: Could not delete file '%s' that stored the previous last log rotation time.

* []()ID: 2116

  Severity: ERROR\
  Message: Cursor on log '%s' has been aborted after a purge.

* []()ID: 2117

  Severity: ERROR\
  Message: Could not position and read newest record from log file '%s'. Current thread is '%s'. Error was: %s.

* []()ID: 2121

  Severity: ERROR\
  Message: Cannot decode change-log record with version %x.

* []()ID: 2122

  Severity: ERROR\
  Message: Cannot start total update in domain "%s" from this directory server DS(%s): no remote directory servers found.

* []()ID: 2123

  Severity: ERROR\
  Message: Cannot start total update in domain "%s" from this directory server DS(%s): cannot find remote directory server DS(%s).

* []()ID: 2124

  Severity: ERROR\
  Message: New replication connection from %s started with unexpected message %s and is being closed.

* []()ID: 2125

  Severity: ERROR\
  Message: The directory server %s can no longer keep up with changes coming from replication server %s for base DN %s. Some missing changes have been purged by this replication server and the connection will be terminated. The directory server may fail-over to another replication server that has not purged the changes that it needs. If there is no replication server containing the missing changes then it will fail to connect to any replication server and will need to be reinitialized. (Underlying error is: %s).

* []()ID: 2126

  Severity: ERROR\
  Message: The replication server %s can no longer keep up with changes coming from replication server %s for base DN %s. Some missing changes have been purged by this replication server and the connection will be terminated. The directory servers connected to this replication server may fail-over to another replication server that has not purged the changes that it needs. If there is no replication server containing the missing changes then the directory servers will fail to connect to any replication server and will need to be reinitialized. (Underlying error is: %s).

* []()ID: 2127

  Severity: WARNING\
  Message: Error while setting replication listener socket timeout to 1 second for domain '%s', server state may be reported as being a bit late with respect to other servers. Cause was: %s.

* []()ID: 2128

  Severity: ERROR\
  Message: Invalid operator '%s' specified in historicalCsnRangeMatch extensible matching rule assertion.

* []()ID: 2129

  Severity: ERROR\
  Message: Specified assertion '%s' for historicalCsnRangeMatch extensible matching rule does not conform to expected syntax. The assertion must specify a CSN range.

* []()ID: 2130

  Severity: ERROR\
  Message: Specified CSNs '%s' and '%s' have two different server ids. The historicalCsnRangeMatch extensible matching rule requires CSNs to have the same server id.

* []()ID: 2131

  Severity: ERROR\
  Message: Specified operators '%s' and '%s' do not specify a range for historicalCsnRangeMatch extensible matching rule.

* []()ID: 2132

  Severity: ERROR\
  Message: Could not restart the Replication Server, bind to listen port %d failed : %s.

* []()ID: 2133

  Severity: ERROR\
  Message: The replication server has detected that the file system containing the changelog is full. In order to prevent further problems, the replication server will disconnect from the replication topology and wait for sufficient disk space to be recovered, at which point it will reconnect.

* []()ID: 2134

  Severity: WARNING\
  Message: Disk space for the replication changelog is getting low. The replication server will continue to operate, but will stop in the event of a full disk.

* []()ID: 2135

  Severity: WARNING\
  Message: The replication server has detected that the file system containing the changelog has sufficient disk space to resume operation. It is now reconnecting to the rest of the replication topology.

* []()ID: 2136

  Severity: NOTICE\
  Message: An I/O error occurred while reading replication messages from %s. The connection will close and replication server (%s) will not process any more updates from it. Reported error is: %s.

* []()ID: 2137

  Severity: NOTICE\
  Message: %s is disconnecting from this replication server %s.

* []()ID: 2138

  Severity: ERROR\
  Message: The replication server connector thread could not be stopped : %s.

* []()ID: 2139

  Severity: ERROR\
  Message: Unable to position reader to key '%s' using strategy '%s' on log '%s'. Changelog may be corrupted. Directory servers connected to this replication server may need to be reinitialized.

* []()ID: 2140

  Severity: ERROR\
  Message: Assured replication is not supported anymore, it should be disabled on the topology.

* []()ID: 2141

  Severity: ERROR\
  Message: Replication Server '%s' expected to negotiate with another Replication Server but got information for Directory Server '%s' instead. The connection will be closed.

* []()ID: 2142

  Severity: WARNING\
  Message: Replication delay for '%s' is above %dms, current delay: %dms.

* []()ID: 2143

  Severity: WARNING\
  Message: The replication server has detected that the file system containing the changelog has sufficient disk space to resume operation.

* []()ID: 2144

  Severity: ERROR\
  Message: Detected one or more corrupted records in log file '%s', this replication server will be removed from the replication topology. Recover the server from a valid filesystem backup if available or re-create it.

* []()ID: 2145

  Severity: ERROR\
  Message: An error occurred while verifying integrity of log file '%s' : %s.

* []()ID: 2146

  Severity: ERROR\
  Message: Cannot enable replication to server '%s' as this server's ID '%s' is not a number between 1 and 32767.

* []()ID: 2147

  Severity: ERROR\
  Message: An error occurred in session '%s' when trying to send a message to the socket: %s.

* []()ID: 2148

  Severity: ERROR\
  Message: Could not convert value '%s' to long.

* []()ID: 2149

  Severity: ERROR\
  Message: Could not find replica update message matching the index record. No more replica update messages with a csn newer than %s exist in domain '%s'.

* []()ID: 2150

  Severity: ERROR\
  Message: An exception was encountered while trying to encode a replication %s message for entry "%s" into an External Change Log entry: %s.

* []()ID: 2151

  Severity: ERROR\
  Message: Unexpected message type when trying to create changelog entry for dn %s: '%s'.

* []()ID: 2152

  Severity: ERROR\
  Message: %s in Replication Server=%s, an initialization message of type %s cannot be sent to its destination server. Details: routing table is empty.

* []()ID: 2153

  Severity: ERROR\
  Message: %s message of type %s cannot be routed. Details: %s.

* []()ID: 2154

  Severity: ERROR\
  Message: Error when trying to publish a message in '%s'. The connection is going to be closed and reopened.

* []()ID: 2155

  Severity: ERROR\
  Message: Error when trying to publish a message in '%s'. The connection is going to be closed and reopened. Error: %s.

* []()ID: 2158

  Severity: ERROR\
  Message: Directory server %s was attempting to connect to replication server %s but an error occurred in handshake phase. Error: %s.

* []()ID: 2159

  Severity: ERROR\
  Message: Replication server %s was attempting to connect to replication server %s but an error occurred in handshake phase. Error: %s.

* []()ID: 2160

  Severity: ERROR\
  Message: Error when enabling external changelog: %s.

* []()ID: 2161

  Severity: WARNING\
  Message: Directory server %s stopped the handshake process with replication server %s because it received the unexpected message '%s'.

* []()ID: 2162

  Severity: INFO\
  Message: Cursor on replica '%s' invalidated.

* []()ID: 2163

  Severity: ERROR\
  Message: The domain state file cannot be written. The server will shutdown but it should be restored from backup. Cause was : %s.

* []()ID: 2164

  Severity: ERROR\
  Message: Some data in the domain state file '%s' in not of the form \<domainId>\[csn:csn]:\<domainDN>, the replication server cannot start. Restore the server from backup.

* []()ID: 2165

  Severity: INFO\
  Message: Task '%s' to initialize domain '%s' failed to contact the source server. The task will be retried because the current server may be in the process of re-connecting to the best replication server for itself.

* []()ID: 2166

  Severity: INFO\
  Message: The server '%s' may retry the initialization process because the server '%s' in domain '%s' is temporarily unreachable.

* []()ID: 2167

  Severity: ERROR\
  Message: Error when purging historical information for entry %s: %s.

* []()ID: 2168

  Severity: ERROR\
  Message: Replication server failed to start because setting socket timeout on port %d caused error %s.

* []()ID: 2169

  Severity: WARNING\
  Message: A transient problem occurred while DS(%s) was connecting to RS(%s), Directory Server will try to connect again. Problem was: %s.

* []()ID: 2170

  Severity: ERROR\
  Message: %s for domain %s cannot route message of type %s to all the replicas in the topology because none are reachable.

* []()ID: 2171

  Severity: ERROR\
  Message: %s for domain '%s' cannot route message of type %s to replica %s because it is unreachable. Reachable replicas: %s.

* []()ID: 2172

  Severity: ERROR\
  Message: Server %s should be initialized but is not connected to the topology.

* []()ID: 2174

  Severity: ERROR\
  Message: Changelog file %s should be version %d, but found version %d. Likely causes for this error: the server binaries were accidentally downgraded, data was restored from a file system backup taken on a more recent version of the server, or the changelog file was corrupted. If the server was downgraded, upgrade it. If the data was restored from a file system backup, restore it again from a recent, valid file system backup taken on the same version of the server. Otherwise, as last resort, remove the changelog by running the 'dsrepl clear-changelog' command and restart the server.

* []()ID: 2175

  Severity: NOTICE\
  Message: An unresolved conflict was detected in CSN %s replaying a DELETE of "%s" as child entries exist (renaming child "%s" to "%s"). Consider restoring the parent entry, or deleting the renamed child entries.

* []()ID: 2176

  Severity: NOTICE\
  Message: An unresolved conflict was detected in CSN %s replaying an ADD of "%s" as the parent entry is missing (adding as "%s"). Consider restoring the parent entry, or deleting the new entry.

* []()ID: 2177

  Severity: NOTICE\
  Message: An unresolved conflict was detected in CSN %s replaying an ADD of "%s" which already exists (adding as "%s"). Consider reviewing both entries and either merge the contents manually or delete one.

* []()ID: 2178

  Severity: NOTICE\
  Message: An unresolved conflict was detected in CSN %s replaying a MODIFYDN of "%s" as the new parent entry "%s" does not exist. Consider restoring the parent entry, or deleting this entry.

* []()ID: 2179

  Severity: NOTICE\
  Message: An unresolved conflict was detected in CSN %s replaying a MODIFYDN of "%s" to "%s" which already exists (renaming as "%s"). Consider merging the two entries manually, or deleting one of them.

* []()ID: 2181

  Severity: NOTICE\
  Message: RS(%s) groupId '%s' has lower priority than groupId '%s' which matched at least one other RS.

* []()ID: 2182

  Severity: ERROR\
  Message: Peer '%s' has sent an update, but it is not allowed to do so by the configuration of this replication server. This update will be discarded. Check the configuration of both this replication server and its peer to determine if they have to be adjusted.

* []()ID: 2183

  Severity: ERROR\
  Message: Replication peer certificate verification failed with error: %s.

* []()ID: 2184

  Severity: ERROR\
  Message: Digest algorithm '%s' of fingerprint '%s' is not supported by the JVM.

* []()ID: 2185

  Severity: ERROR\
  Message: The following replication server listener threads were unexpectedly stopped: %s. A server restart may be needed.

* []()ID: 2186

  Severity: ERROR\
  Message: Cursor on log '%s' has been aborted after a clear.

* []()ID: 2187

  Severity: ERROR\
  Message: Initialization of domain '%s' interrupted: no data received from the remote exporter '%s' for %s.

* []()ID: 2189

  Severity: WARNING\
  Message: The replication server domain connection for '%s' will be forcibly closed because the peer replication server '%s' is unresponsive.

* []()ID: 2190

  Severity: WARNING\
  Message: The replication domain connection for '%s' will be forcibly closed because the peer replication server '%s' is unresponsive.

* []()ID: 2191

  Severity: WARNING\
  Message: ChangeTime Heartbeat publisher '%s' for domain '%s' will be forcibly stopped because the peer server is unresponsive.

* []()ID: 2192

  Severity: ERROR\
  Message: Publish of a replication message to server '%s' was interrupted.

* []()ID: 2193

  Severity: ERROR\
  Message: Changelog on replication server '%s' no longer contains changes for domain '%s' which are required by replica '%s'. The replica will no longer receive replicated changes and must be re-initialized.

* []()ID: 2195

  Severity: WARNING\
  Message: Replication server RS(%s) is not sending update %s for domain '%s' to directory server DS(%s) at %s because the replica is too late and must be re-initialized.

* []()ID: 2196

  Severity: WARNING\
  Message: Replication server RS(%s) is ignoring update %s for domain "%s" from directory server DS(%s) at %s because the replica is too late and must be re-initialized.

* []()ID: 2197

  Severity: WARNING\
  Message: Replication server RS(%s) is closing its connection to %s at %s for domain '%s' because it could not detect a heartbeat: time since last message (%s) is greater than the timeout interval %s ms (heartbeat interval is %s ms).

* []()ID: 2200

  Severity: ERROR\
  Message: Replica '%s' seems to have disconnected from the topology while it was being re-initialized, initialization will stop.

* []()ID: 2201

  Severity: ERROR\
  Message: Initialization of replication domain '%s' interrupted because the domain is shutting down. The domain still needs to be re-initialized.

* []()ID: 2203

  Severity: WARNING\
  Message: Directory server DS(%s) was unable to connect to replication server at %s for domain '%s': unknown host.

* []()ID: 2204

  Severity: INFO\
  Message: Directory server DS(%s) did not find a generation ID for domain '%s'. A new generation ID will be computed by exporting the first %d entries in the domain.

* []()ID: 2205

  Severity: WARNING\
  Message: Replica '%s' for domain '%s' tried to connect but the replication server is still processing messages from the previous replication session and considers the replica already connected. The connection will be closed, the replica will connect again.

* []()ID: 2207

  Severity: NOTICE\
  Message: This replica `%s` has received a notification from its replication server `%s` to stop processing updates for domain `%s` as part of a disaster recovery procedure. This replica must be reinitialized as part of the recovery procedure.

* []()ID: 2209

  Severity: ERROR\
  Message: The search cannot be processed because the external changelog is not configured to generate change numbers. Change the replication server configuration if change numbers are needed.

* []()ID: 2210

  Severity: INFO\
  Message: The purge delay has been set to: %s.

* []()ID: 2211

  Severity: INFO\
  Message: Purging is disabled (delay set to 0).

* []()ID: 2212

  Severity: ERROR\
  Message: An unexpected error occurred when loading the fractional replication configuration of domain "%s": %s.

* []()ID: 2213

  Severity: WARNING\
  Message: Replication server RS(%s) ignoring update %s for domain "%s" from directory server DS(%s) at %s because the peer DS reported to be in BAD\_DATA status. The generation ID matches, (DS is %s, RS is %s), there may be a problem with fractional replication configuration. Check the DS error logs for more details.

* []()ID: 2214

  Severity: WARNING\
  Message: Replication server RS(%s) not sending update %s for domain "%s" to directory server DS(%s) at %s because the peer DS reported to be in BAD\_DATA status. The generation ID matches, (DS is %s, RS is %s), there may be a problem with fractional replication configuration. Check the DS error logs for more details.

* []()ID: 2215

  Severity: NOTICE\
  Message: JAVA Version: %s.

* []()ID: 2216

  Severity: NOTICE\
  Message: JAVA Vendor: %s.

* []()ID: 2217

  Severity: NOTICE\
  Message: JVM Version: %s.

* []()ID: 2218

  Severity: NOTICE\
  Message: JVM Vendor: %s.

* []()ID: 2219

  Severity: NOTICE\
  Message: JAVA Home: %s.

* []()ID: 2220

  Severity: NOTICE\
  Message: Class Path: %s.

* []()ID: 2221

  Severity: NOTICE\
  Message: Current Directory: %s.

* []()ID: 2222

  Severity: NOTICE\
  Message: Operating System: %s.

* []()ID: 2223

  Severity: NOTICE\
  Message: JVM Architecture: %s.

* []()ID: 2224

  Severity: NOTICE\
  Message: System Name: %s.

* []()ID: 2225

  Severity: NOTICE\
  Message: Available Processors: %d.

* []()ID: 2226

  Severity: NOTICE\
  Message: Max Available Memory: %d.

* []()ID: 2227

  Severity: NOTICE\
  Message: Currently Used Memory: %d.

* []()ID: 2228

  Severity: NOTICE\
  Message: Currently Free Memory: %d.

* []()ID: 2229

  Severity: NOTICE\
  Message: JVM Information: PID(%d) %s by %s, %s architecture, %d bytes heap size.

* []()ID: 2230

  Severity: NOTICE\
  Message: JVM Host: %s, running %s, %d bytes physical memory size, number of processors available %d.

* []()ID: 2231

  Severity: NOTICE\
  Message: JVM Arguments: %s.

* []()ID: 2232

  Severity: NOTICE\
  Message: JVM Host: %s, running %s, unknown physical memory size, number of processors available %d.

* []()ID: 2233

  Severity: NOTICE\
  Message: Installation Directory: %s.

* []()ID: 2235

  Severity: NOTICE\
  Message: Instance Directory: %s.

* []()ID: 2237

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because the last non-space character was a comma or semicolon.

* []()ID: 2238

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because character '%c' at position %d is not allowed in an attribute name.

* []()ID: 2239

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because the hyphen character is not allowed as the first character of an attribute name.

* []()ID: 2240

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because it contained an RDN containing an empty attribute name.

* []()ID: 2241

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because the parsed attribute name %s included a period but that name did not appear to be a valid OID.

* []()ID: 2242

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because the last non-space character was part of the attribute name '%s'.

* []()ID: 2243

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because the next non-space character after attribute name "%s" should have been an equal sign but instead was '%c'.

* []()ID: 2244

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because character '%c' at position %d is not valid.

* []()ID: 2245

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because an attribute value started with an octothorpe (#) but was not followed by a positive multiple of two hexadecimal digits.

* []()ID: 2246

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because an attribute value started with an octothorpe (#) but contained a character %c that was not a valid hexadecimal digit.

* []()ID: 2247

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because an unexpected failure occurred while attempting to parse an attribute value from one of the RDN components: "%s".

* []()ID: 2248

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because one of the RDN components included a quoted value that did not have a corresponding closing quotation mark.

* []()ID: 2249

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid distinguished name because one of the RDN components included a value with an escaped hexadecimal digit that was not followed by a second hexadecimal digit.

* []()ID: 2251

  Severity: ERROR\
  Message: The provided value "%s" could not be parsed as a valid subtree specification.

* []()ID: 2252

  Severity: NOTICE\
  Message: A schema element could not be imported: %s, %s.

* []()ID: 2253

  Severity: ERROR\
  Message: There should be no warnings on the schema, but instead got %d warnings: %s.

* []()ID: 2254

  Severity: ERROR\
  Message: Unable to parse the OID from the provided definition of objectclass: '%s'.

* []()ID: 2255

  Severity: ERROR\
  Message: Unable to parse the OID from the provided definition of attribute type: '%s'.

* []()ID: 2256

  Severity: ERROR\
  Message: Unable to parse the OID from the provided definition of ldap syntax: '%s'.

* []()ID: 2257

  Severity: ERROR\
  Message: Unable to parse the OID from the provided definition of matching rule use: '%s'.

* []()ID: 2258

  Severity: ERROR\
  Message: Unable to parse the OID from the provided definition of name form: '%s'.

* []()ID: 2259

  Severity: ERROR\
  Message: Unable to parse the OID from the provided definition of DIT content rule: '%s'.

* []()ID: 2260

  Severity: ERROR\
  Message: Unable to parse the rule ID from the provided definition of DIT structure rule: '%s'.

* []()ID: 2268

  Severity: ERROR\
  Message: There is already a server instance configured in the directory %s. Please make sure there is no configuration (config) or data (db) directory in the server instance path.

* []()ID: 2269

  Severity: INFO\
  Message: You have chosen to combine an evaluation profile with another profile that is intended for production. Applying an evaluation profile after others can compromise the security of your server. Review the server configuration carefully before deployment.

* []()ID: 2270

  Severity: ERROR\
  Message: The file '%s' is referring to an invalid instance (%s). You must remove this file before setting up a new instance in the directory %s. Please use either the --%s option in non interactive mode or the interactive mode to setup an instance elsewhere.

* []()ID: 2271

  Severity: ERROR\
  Message: A server instance (%s) has already been setup in the directory %s.

* []()ID: 2272

  Severity: WARNING\
  Message: Setup has failed, see the errors in the messages below. The process also failed to automatically remove the files that it created during setup. Please manually remove the 'db' and 'config' directories from the instance directory before trying to run the setup again.

* []()ID: 2273

  Severity: WARNING\
  Message: Setup has failed, see the errors in the messages below. The process also failed to automatically remove the files that it created during setup. Please manually remove the 'db' and 'config' directories from the instance directory and the '%s' file before trying to run the setup again.

* []()ID: 2274

  Severity: ERROR\
  Message: The file based keystore password cannot be empty.

* []()ID: 2275

  Severity: ERROR\
  Message: You must specify the keystore password of the file based keystore. You can use either --%s or --%s options to specify it.

* []()ID: 2276

  Severity: INFO\
  Message: Path of a JCEKS keystore containing the certificate(s) that the server should use when negotiating secure connections using StartTLS or SSL.

* []()ID: 2277

  Severity: INFO\
  Message: Path of a JKS keystore containing the certificate(s) that the server should use when negotiating secure connections using StartTLS or SSL.

* []()ID: 2278

  Severity: ERROR\
  Message: You must specify a valid port number.

* []()ID: 2279

  Severity: INFO\
  Message: Trust remote server certificates.

* []()ID: 2283

  Severity: INFO\
  Message: Truststore file.

* []()ID: 2284

  Severity: INFO\
  Message: Truststore password.

* []()ID: 2288

  Severity: INFO\
  Message: Truststore password (leave empty if the truststore has no password, mandatory for a file based truststore):.

* []()ID: 2289

  Severity: INFO\
  Message: Choose how the server should trust certificates from SSL peers:.

* []()ID: 2290

  Severity: INFO\
  Message: Use the JVM truststore.

* []()ID: 2294

  Severity: INFO\
  Message: Blindly trust all certificates (evaluation only - unsafe for production).

* []()ID: 2295

  Severity: INFO\
  Message: No password provided.

* []()ID: 2296

  Severity: INFO\
  Message: Use existing PKCS12 truststore file for validating peer SSL certificates.

* []()ID: 2297

  Severity: INFO\
  Message: Use existing JCEKS truststore file for validating peer SSL certificates.

* []()ID: 2298

  Severity: INFO\
  Message: Use existing JKS truststore file for validating peer SSL certificates.

* []()ID: 2299

  Severity: INFO\
  Message: Blindly trust peer SSL certificates.

* []()ID: 2300

  Severity: ERROR\
  Message: The provided password file '%s' must be an existing readable file.

* []()ID: 2301

  Severity: ERROR\
  Message: Unable to read password in file '%s'. A password file must contain a single line with the keystore password, details: %s.

* []()ID: 2302

  Severity: ERROR\
  Message: Invalid content for password file '%s'. A password file must contain a single line with the password.

* []()ID: 2303

  Severity: ERROR\
  Message: password is empty.

* []()ID: 2304

  Severity: ERROR\
  Message: An error occurred while storing provided password in the instance file '%s', details: %s.

* []()ID: 2305

  Severity: ERROR\
  Message: Could not access the %s truststore '%s'. Check that the content of the file corresponds to a valid truststore, that you have access rights to it and that a valid password has been provided if needed. Error details: %s.

* []()ID: 2306

  Severity: ERROR\
  Message: clear-text password cannot be empty.

* []()ID: 2307

  Severity: ERROR\
  Message: An error occurred while creating the file based trust manager provider: %s.

* []()ID: 2308

  Severity: ERROR\
  Message: An error occurred while enabling the %s trust manager provider: %s.

* []()ID: 2309

  Severity: ERROR\
  Message: The provided truststore file '%s' must be an existing readable file.

* []()ID: 2310

  Severity: ERROR\
  Message: An error occurred while creating the PKCS#11 key manager provider: %s.

* []()ID: 2311

  Severity: ERROR\
  Message: Could not read the %s keystore '%s' entries. Check that the content of the file corresponds to a valid keystore, that you have access rights to it and that a valid password has been provided if needed. Error details: %s.

* []()ID: 2312

  Severity: ERROR\
  Message: Could not access the PKCS#11 keystore. Check that the JVM security settings have been configured to use a PKCS#11 keystore and that a valid password has been provided if needed. Error details: %s.

* []()ID: 2313

  Severity: ERROR\
  Message: No private key entry found in keystore '%s'. Keystores used for securing client connections must contain at least one private key entry. Beware: you may need to provide the keystore password to access keystore private entries.

* []()ID: 2314

  Severity: INFO\
  Message: Provide the server's fully qualified host name.

* []()ID: 2315

  Severity: INFO\
  Message: Welcome to the PingDS %s interactive setup.%n%nInteractive mode helps you quickly set up a PingDS server.%nProvide all required options to set up the server in non-interactive mode,%nor use the command shown at the end of your interactive session.

* []()ID: 2316

  Severity: ERROR\
  Message: License not accepted, %s will exit.

* []()ID: 2317

  Severity: ERROR\
  Message: Invalid input: keystore path cannot be empty.

* []()ID: 2318

  Severity: ERROR\
  Message: Invalid configuration: you must use at least one certificate nickname.

* []()ID: 2319

  Severity: INFO\
  Message: The keystore contains the following certificate nicknames: %s.%nYou will be prompted for the nickname(s) to use.

* []()ID: 2320

  Severity: ERROR\
  Message: The number of entries to import must be a positive integer.

* []()ID: 2321

  Severity: ERROR\
  Message: Value '%s' must be a valid number.

* []()ID: 2322

  Severity: ERROR\
  Message: Value '%s' must be a valid version (two or three digits separated with a dot).

* []()ID: 2323

  Severity: ERROR\
  Message: Please select at least version %s.

* []()ID: 2324

  Severity: INFO\
  Message: Listening on port %d.

* []()ID: 2325

  Severity: INFO\
  Message: Customize Server With Profiles.

* []()ID: 2326

  Severity: INFO\
  Message: Server security.

* []()ID: 2327

  Severity: INFO\
  Message: Keystore file.

* []()ID: 2328

  Severity: INFO\
  Message: Use existing PKCS#11 keystore.

* []()ID: 2332

  Severity: INFO\
  Message: Keystore password.

* []()ID: 2333

  Severity: INFO\
  Message: Certificate nickname(s) to use.

* []()ID: 2334

  Severity: INFO\
  Message: LDAP (cleartext).

* []()ID: 2335

  Severity: INFO\
  Message: LDAPS (secure).

* []()ID: 2336

  Severity: INFO\
  Message: HTTP (cleartext).

* []()ID: 2337

  Severity: INFO\
  Message: HTTPS (secure).

* []()ID: 2338

  Severity: INFO\
  Message: How would you like to secure your deployment?.

* []()ID: 2339

  Severity: INFO\
  Message: You already have a CA certificate for the deployment and an SSL key-pair for this server.

* []()ID: 2340

  Severity: INFO\
  Message: Provide the SSL certificate in the keystore that will be used for securing server connections:.

* []()ID: 2341

  Severity: INFO\
  Message: Generate a CA certificate and SSL key-pair using the deployment ID (easier to deploy, but not suitable for public facing services).

* []()ID: 2342

  Severity: INFO\
  Message: Provide the deployment ID:.

* []()ID: 2343

  Severity: INFO\
  Message: Server instance path.

* []()ID: 2344

  Severity: INFO\
  Message: Provide the server instance path.

* []()ID: 2345

  Severity: INFO\
  Message: Provide the directory root user DN.

* []()ID: 2346

  Severity: INFO\
  Message: Provide the password for root user (leave empty to use the deployment ID password):.

* []()ID: 2347

  Severity: INFO\
  Message: Confirm the password for root user:.

* []()ID: 2348

  Severity: INFO\
  Message: Enable HTTP?.

* []()ID: 2349

  Severity: INFO\
  Message: HTTP port.

* []()ID: 2350

  Severity: INFO\
  Message: Enable HTTPS?.

* []()ID: 2351

  Severity: INFO\
  Message: HTTPS port.

* []()ID: 2352

  Severity: INFO\
  Message: Start server after setup.

* []()ID: 2353

  Severity: INFO\
  Message: Run as Windows service.

* []()ID: 2354

  Severity: INFO\
  Message: Server's fully qualified host name.

* []()ID: 2355

  Severity: INFO\
  Message: Root user password.

* []()ID: 2356

  Severity: INFO\
  Message: Enable LDAP?.

* []()ID: 2357

  Severity: INFO\
  Message: LDAP port.

* []()ID: 2358

  Severity: INFO\
  Message: Enable LDAPS?.

* []()ID: 2359

  Severity: INFO\
  Message: LDAPS port.

* []()ID: 2360

  Severity: INFO\
  Message: Administration connector port.

* []()ID: 2361

  Severity: INFO\
  Message: Start the server when setup is complete? Note: starting with version 7.0, it is advised to only start the server once it is customized for the intended deployment. If more configuration is needed, then select 'no'.

* []()ID: 2362

  Severity: INFO\
  Message: Global Parameters.

* []()ID: 2363

  Severity: INFO\
  Message: Network Parameters.

* []()ID: 2364

  Severity: INFO\
  Message: All Server Parameters.

* []()ID: 2365

  Severity: INFO\
  Message: Set up the server with the specified settings.

* []()ID: 2366

  Severity: INFO\
  Message: Start over.

* []()ID: 2367

  Severity: INFO\
  Message: Quit.

* []()ID: 2368

  Severity: INFO\
  Message: Equivalent non-interactive command:.

* []()ID: 2369

  Severity: INFO\
  Message: Accept these choices and continue?.

* []()ID: 2370

  Severity: ERROR\
  Message: Unable to encode provided password because '%s'.

* []()ID: 2371

  Severity: ERROR\
  Message: The fully qualified host name must be a non blank string.

* []()ID: 2372

  Severity: ERROR\
  Message: The provided keystore file '%s' must be an existing readable file.

* []()ID: 2373

  Severity: INFO\
  Message: Launch external process: '%s'.

* []()ID: 2374

  Severity: ERROR\
  Message: External process contains errors: %s.

* []()ID: 2375

  Severity: INFO\
  Message: External process standard output: %s.

* []()ID: 2376

  Severity: ERROR\
  Message: External process has been interrupted: '%s'.

* []()ID: 2377

  Severity: ERROR\
  Message: Unable to display license because '%s'.

* []()ID: 2378

  Severity: ERROR\
  Message: Unable to enable windows service (return code '%d'): %s.

* []()ID: 2379

  Severity: INFO\
  Message: Enable windows service command (return code '%d') output: %s.

* []()ID: 2380

  Severity: ERROR\
  Message: Unable to create server instance directory '%s'.

* []()ID: 2381

  Severity: ERROR\
  Message: The instance parent (%s) must be a valid existing directory.

* []()ID: 2382

  Severity: ERROR\
  Message: The instance path must be a directory.

* []()ID: 2384

  Severity: ERROR\
  Message: An error occurred while trying to write instance.loc file: %s.

* []()ID: 2385

  Severity: ERROR\
  Message: You cannot provide a keystore password without providing an existing keystore.

* []()ID: 2386

  Severity: ERROR\
  Message: You cannot specify certificate aliases without providing an existing keystore.

* []()ID: 2387

  Severity: ERROR\
  Message: You cannot specify truststore without providing an existing keystore.

* []()ID: 2389

  Severity: ERROR\
  Message: Unable to enable the file based HTTP access logger because: %s.

* []()ID: 2390

  Severity: ERROR\
  Message: An error occurred while writing password in configuration file: '%s'.

* []()ID: 2391

  Severity: ERROR\
  Message: An error occurred while attempting to update the HTTP connector port: '%s'.

* []()ID: 2392

  Severity: ERROR\
  Message: An error occurred while attempting to update the HTTPS connector: '%s'.

* []()ID: 2393

  Severity: ERROR\
  Message: An error occurred while attempting to update the port on which to listen for LDAP communication: %s.

* []()ID: 2394

  Severity: ERROR\
  Message: Unable to write configuration file '%s' (%s).

* []()ID: 2395

  Severity: ERROR\
  Message: Unable to write the upgrade version in '%s' file (%s).

* []()ID: 2396

  Severity: ERROR\
  Message: Unable to parse the version in '%s' file in order to initialize the content of the '%s' file.

* []()ID: 2397

  Severity: ERROR\
  Message: Unable to write file '%s' because: '%s'.

* []()ID: 2398

  Severity: ERROR\
  Message: Unable to edit runtime settings file because '%s'.

* []()ID: 2399

  Severity: ERROR\
  Message: An error occurred while copying file '%s' into '%s': '%s'.

* []()ID: 2400

  Severity: ERROR\
  Message: An error occurred while creating directory '%s'.

* []()ID: 2401

  Severity: ERROR\
  Message: Unable to set access permissions to allow write operations on file '%s'. Ensure that you have enough rights to change the access permissions on instance files.

* []()ID: 2402

  Severity: INFO\
  Message: Configuring server.

* []()ID: 2403

  Severity: INFO\
  Message: Validating parameters.

* []()ID: 2404

  Severity: ERROR\
  Message: The server can only be enabled as a windows service on a Windows operating system.

* []()ID: 2405

  Severity: INFO\
  Message: Port on which the server should listen for HTTP communication.

* []()ID: 2406

  Severity: INFO\
  Message: Port on which the server should listen for HTTPS communication.

* []()ID: 2407

  Severity: INFO\
  Message: Path were the instance should be set up.

* []()ID: 2408

  Severity: NOTICE\
  Message: /path/to/opendj.

* []()ID: 2409

  Severity: ERROR\
  Message: The provided certificate nickname '%s' could not be found. The keystore contains the following certificate nicknames: %s.

* []()ID: 2410

  Severity: ERROR\
  Message: The keystore contains the following certificate nicknames: %s.%nYou have to provide the nickname of the certificate you want to use.

* []()ID: 2411

  Severity: ERROR\
  Message: Could not access the %s keystore '%s'. Check that the content of the file corresponds to a valid keystore, that you have access rights to it and that a valid password has been provided if needed. Error details: %s.

* []()ID: 2412

  Severity: ERROR\
  Message: You must accept the product license to run setup. Either use interactive mode or the '--%s' option.

* []()ID: 2413

  Severity: ERROR\
  Message: The provided server install path '%s' must reference an existing directory.

* []()ID: 2414

  Severity: ERROR\
  Message: An unexpected error has been raised during setup: '%s'.

* []()ID: 2415

  Severity: ERROR\
  Message: Administration connector port '%d' is not in allowed range %d, %d.

* []()ID: 2416

  Severity: ERROR\
  Message: LDAP port '%d' is not in allowed range %d, %d.

* []()ID: 2417

  Severity: ERROR\
  Message: LDAPS port '%d' is not in allowed range %d, %d.

* []()ID: 2418

  Severity: ERROR\
  Message: HTTP port '%d' is not in allowed range %d, %d.

* []()ID: 2419

  Severity: ERROR\
  Message: HTTPS port '%d' is not in allowed range %d, %d.

* []()ID: 2420

  Severity: ERROR\
  Message: Replication port '%d' is not in allowed range %d, %d.

* []()ID: 2421

  Severity: ERROR\
  Message: Port '%d' is not in allowed range %d, %d.

* []()ID: 2422

  Severity: ERROR\
  Message: Value '%d' has been specified for different ports.

* []()ID: 2423

  Severity: ERROR\
  Message: The administrator user bind DN '%s' is invalid. %s.

* []()ID: 2424

  Severity: ERROR\
  Message: The root user DN cannot be empty.

* []()ID: 2425

  Severity: ERROR\
  Message: DN for the monitor user cannot be empty.

* []()ID: 2426

  Severity: ERROR\
  Message: Monitor user DN value '%s' is invalid because: %s.

* []()ID: 2427

  Severity: NOTICE\
  Message: This utility sets up a PingDS server. Use the %s option to list available profiles.

* []()ID: 2428

  Severity: INFO\
  Message: Done.

* []()ID: 2429

  Severity: INFO\
  Message: Enabling Windows service.

* []()ID: 2430

  Severity: INFO\
  Message: Error.

* []()ID: 2431

  Severity: INFO\
  Message: …​..

* []()ID: 2432

  Severity: INFO\
  Message: Starting directory server.

* []()ID: 2433

  Severity: INFO\
  Message: Configuring certificates.

* []()ID: 2434

  Severity: INFO\
  Message: An error occurred creating the temporary file.

* []()ID: 2435

  Severity: INFO\
  Message: Error Enabling Windows service.

* []()ID: 2436

  Severity: INFO\
  Message: Error Starting Directory Server.

* []()ID: 2437

  Severity: INFO\
  Message: Error Starting Directory Server. Error code: %s.

* []()ID: 2438

  Severity: INFO\
  Message: See %s for a detailed log of the failed operation.%nPlease report this error and provide the log file mentioned above.

* []()ID: 2439

  Severity: INFO\
  Message: An error occurred while configuring the certificates: %s.

* []()ID: 2440

  Severity: INFO\
  Message: Administration connector port.

* []()ID: 2441

  Severity: INFO\
  Message: Please read the License Agreement above.%nYou must accept the terms of the agreement before continuing with the installation.

* []()ID: 2442

  Severity: INFO\
  Message: Root user DN.

* []()ID: 2443

  Severity: ERROR\
  Message: The --%s option should only be provided when using a file based trust store option.

* []()ID: 2444

  Severity: INFO\
  Message: Provide the DN for the default monitor user.

* []()ID: 2445

  Severity: INFO\
  Message: Provide the password for the default monitor user:.

* []()ID: 2446

  Severity: INFO\
  Message: Confirm the password for the default monitor user:.

* []()ID: 2447

  Severity: INFO\
  Message: Define and enable a default user for querying monitoring information?.

* []()ID: 2448

  Severity: INFO\
  Message: Monitor user.

* []()ID: 2449

  Severity: INFO\
  Message: Monitor user password.

* []()ID: 2450

  Severity: INFO\
  Message: {monitorUserDn}.

* []()ID: 2451

  Severity: INFO\
  Message: {monitorUserPassword}.

* []()ID: 2452

  Severity: INFO\
  Message: DN of the default user allowed to query monitoring information.

* []()ID: 2453

  Severity: INFO\
  Message: Password of the default user allowed to query monitoring information.

* []()ID: 2454

  Severity: ERROR\
  Message: When specifying a default user for monitoring a password should also be provided.

* []()ID: 2455

  Severity: ERROR\
  Message: An error occurred while attempting to write the monitor user entry: %s.

* []()ID: 2456

  Severity: ERROR\
  Message: An error occurred while attempting to configure the backend for the monitor user: %s.

* []()ID: 2457

  Severity: ERROR\
  Message: Folder '%s' of the setup profile '%s' must be a readable existing folder.

* []()ID: 2458

  Severity: ERROR\
  Message: Last folder of profile '%s' path '%s' must be the profile version (two or three digits separated by either dot or hyphen, e.g /path/to/profile/6.5.0).

* []()ID: 2459

  Severity: ERROR\
  Message: Folder of the setup profile '%s' must contain a '%s' readable regular file.

* []()ID: 2460

  Severity: ERROR\
  Message: File '%s' from the setup profile '%s' must be a readable regular file.

* []()ID: 2461

  Severity: INFO\
  Message: Configuring profile %s.

* []()ID: 2462

  Severity: ERROR\
  Message: The '%s' setup profile failed: %s.

* []()ID: 2463

  Severity: INFO\
  Message: {name\[:version]}.

* []()ID: 2464

  Severity: INFO\
  Message: Setup profile to apply when initially configuring the server. If the version is not specified, the most recent version older or equal to this PingDS version is used. Use this option multiple times to apply multiple profiles. This option cannot be combined with data import options. %s.

* []()ID: 2465

  Severity: INFO\
  Message: There are no setup profiles available for this PingDS version.

* []()ID: 2466

  Severity: INFO\
  Message: Available setup profiles: %s.

* []()ID: 2467

  Severity: INFO\
  Message: {\[profileName/]parameterName:value}.

* []()ID: 2468

  Severity: INFO\
  Message: Assign a value to a setup profile parameter. Profile name must be provided if multiple profiles are provided, indicate the profile that a parameter applies to by using the profileName/parameterName format.

* []()ID: 2469

  Severity: INFO\
  Message: Display all available profiles.

* []()ID: 2470

  Severity: INFO\
  Message: Display profile parameters.

* []()ID: 2471

  Severity: INFO\
  Message: Profiles available with this PingDS version are:.

* []()ID: 2472

  Severity: INFO\
  Message: Use %s %s to list profile parameters.

* []()ID: 2473

  Severity: NOTICE\
  Message: Parameter(s) '%s' provided for profile '%s' is (are) not used in the profile.

* []()ID: 2474

  Severity: NOTICE\
  Message: Parameter '%s' is provided without any profile specification which is not allowed when multiple profiles are used.

* []()ID: 2475

  Severity: ERROR\
  Message: The parameter '%s' is required by profile '%s', but no value has been provided.

* []()ID: 2476

  Severity: ERROR\
  Message: Error in profile '%s': the default value for parameter '%s' cannot be derived from the SetupConfiguration method '%s' because no such method exists.

* []()ID: 2477

  Severity: ERROR\
  Message: Error in profile '%s': the default value for parameter '%s' cannot be derived from the SetupConfiguration method '%s' because the method invocation threw an error: %s.

* []()ID: 2478

  Severity: ERROR\
  Message: Invalid profile parameter value '%s'. Supported format is '%s'.

* []()ID: 2479

  Severity: ERROR\
  Message: Option to setup profile parameters have been provided but not the profile name. If you want to use a setup profile, please provide its name with the '%s' option.

* []()ID: 2480

  Severity: ERROR\
  Message: Setup profile '%s' cannot be found. %s.

* []()ID: 2481

  Severity: ERROR\
  Message: Profile '%s' has been specified multiple times. It is not possible to configure the server for multiple versions of the same profile. Please choose one version for this profile.

* []()ID: 2482

  Severity: ERROR\
  Message: Setup profile parameter '%s' has been provided multiple times with different values. Please either choose one value or prefix the option values with a profile name.

* []()ID: 2483

  Severity: ERROR\
  Message: Setup profile parameter '%s' references the profile '%s' which has not been provided on the command line. Setup profiles can be added on the command line with the '%s' option.

* []()ID: 2484

  Severity: ERROR\
  Message: Unable to read template file '%s'. Please ensure that the file exists and that you have appropriate permissions to read the file.

* []()ID: 2485

  Severity: ERROR\
  Message: Unable to read file '%s'. Please ensure that the file exists and that you have appropriate permissions to read the file.

* []()ID: 2486

  Severity: WARNING\
  Message: An error occurred while attempting to remove content of directory '%s': %s.

* []()ID: 2487

  Severity: ERROR\
  Message: An error occurred while substituting properties from profile '%s' resource file '%s': %s.

* []()ID: 2488

  Severity: ERROR\
  Message: An IO error occurred while running profile '%s': '%s'.

* []()ID: 2489

  Severity: ERROR\
  Message: Unable to create '%s' backend (%s).

* []()ID: 2490

  Severity: ERROR\
  Message: Unable to create replication domain for base DN '%s' (%s).

* []()ID: 2491

  Severity: ERROR\
  Message: No backend has been created in the profile.

* []()ID: 2492

  Severity: ERROR\
  Message: '%s' setup profile failed to import data contained in '%s' file(s) into '%s' backend. Import LDIF tool options: '%s'. Exception message:'%s'. Tool output: %s.

* []()ID: 2493

  Severity: ERROR\
  Message: Unable to import data.

* []()ID: 2494

  Severity: ERROR\
  Message: Unable to import data (%s).

* []()ID: 2495

  Severity: ERROR\
  Message: Unable to import generated users (%s).

* []()ID: 2496

  Severity: ERROR\
  Message: Unable to import data because some entries have been rejected.

* []()ID: 2497

  Severity: ERROR\
  Message: Unable to import data because some entries have been skipped.

* []()ID: 2498

  Severity: ERROR\
  Message: '%s' setup profile failed to import data contained in '%s' file(s) into '%s' backend because of rejected entries (listed in '%s'). Import LDIF tool options: '%s'. Tool output: %s.

* []()ID: 2499

  Severity: ERROR\
  Message: '%s' setup profile failed to import data contained in '%s' file(s) into '%s' backend because of skipped entries (listed in '%s'). Import LDIF tool options: '%s'. Tool output: %s.

* []()ID: 2500

  Severity: ERROR\
  Message: Unable to update server configuration.

## IDs: 2501-3000

* []()ID: 2501

  Severity: ERROR\
  Message: '%s' setup profile failed to update server configuration file, dsconfig tool options: '%s'. Exception message:'%s'. Tool output: %s.

* []()ID: 2502

  Severity: ERROR\
  Message: Unable to add index for attribute '%s' (%s).

* []()ID: 2503

  Severity: INFO\
  Message: Available profiles:.

* []()ID: 2504

  Severity: INFO\
  Message: Enter profile number(s) separated by comma (leave empty to skip this step):.

* []()ID: 2505

  Severity: INFO\
  Message: Enter profile number(s) separated by comma \[%s]:.

* []()ID: 2506

  Severity: INFO\
  Message: No profiles configured or data to be imported.

* []()ID: 2507

  Severity: INFO\
  Message: Confirm the %s:.

* []()ID: 2508

  Severity: INFO\
  Message: Provide a value for '%s'.

* []()ID: 2509

  Severity: INFO\
  Message: Value set for '%s'.

* []()ID: 2510

  Severity: INFO\
  Message: Configure server for profile '%s'.

* []()ID: 2511

  Severity: INFO\
  Message: Configure server for profile '%s (%s)'.

* []()ID: 2512

  Severity: ERROR\
  Message: Please provide a value having the following syntax: %s.

* []()ID: 2513

  Severity: ERROR\
  Message: The value '%s' for parameter '%s' in profile '%s' is invalid. Please provide a value having the following syntax: %s.

* []()ID: 2514

  Severity: ERROR\
  Message: The value '%s' for parameter '%s' in profile '%s' is invalid because it does not match any allowed values (%s).

* []()ID: 2515

  Severity: ERROR\
  Message: The value for password parameter '%s' of profile '%s' is invalid (%s).

* []()ID: 2516

  Severity: ERROR\
  Message: Unable to encode password associated to parameter '%s' of profile '%s' (%s).

* []()ID: 2517

  Severity: ERROR\
  Message: The value for domain parameter '%s' of profile '%s' cannot be blank.

* []()ID: 2518

  Severity: ERROR\
  Message: The value '%s' for domain parameter '%s' of profile '%s' is invalid (%s).

* []()ID: 2519

  Severity: ERROR\
  Message: The value for DN parameter '%s' of profile '%s' cannot be empty.

* []()ID: 2520

  Severity: WARNING\
  Message: Version %s not found, best match is %s.

* []()ID: 2521

  Severity: INFO\
  Message: Profile '%s (%s)' does not have any parameters.

* []()ID: 2522

  Severity: INFO\
  Message: %s (%s) parameters.

* []()ID: 2523

  Severity: INFO\
  Message: Parameter:.

* []()ID: 2524

  Severity: INFO\
  Message: Syntax:.

* []()ID: 2525

  Severity: INFO\
  Message: %s or configuration expression.

* []()ID: 2526

  Severity: INFO\
  Message: String.

* []()ID: 2527

  Severity: INFO\
  Message: Number.

* []()ID: 2528

  Severity: INFO\
  Message: Decimal number.

* []()ID: 2529

  Severity: INFO\
  Message: Password.

* []()ID: 2530

  Severity: INFO\
  Message: Domain name.

* []()ID: 2531

  Severity: INFO\
  Message: File or directory path.

* []()ID: 2532

  Severity: INFO\
  Message: One of the following values:.

* []()ID: 2533

  Severity: INFO\
  Message: host:port.

* []()ID: 2534

  Severity: INFO\
  Message: DN.

* []()ID: 2535

  Severity: INFO\
  Message: Description:.

* []()ID: 2536

  Severity: INFO\
  Message: Default:.

* []()ID: 2537

  Severity: INFO\
  Message: Derived from the setup global options.

* []()ID: 2538

  Severity: ERROR\
  Message: Unable to bootstrap the Directory Server configuration because of the following error: %s.

* []()ID: 2539

  Severity: ERROR\
  Message: Unable to find resource '%s' of profile '%s' in profile version folders.

* []()ID: 2540

  Severity: INFO\
  Message: Which version of '%s' do you want to use (minimum %s)?.

* []()ID: 2541

  Severity: INFO\
  Message: Specify the server ID for this server. An acceptable ID is an ASCII alpha-numeric string; it may also contain underscore and hyphen characters provided they are not the first character.

* []()ID: 2542

  Severity: INFO\
  Message: {serverId}.

* []()ID: 2543

  Severity: INFO\
  Message: Unique server ID (used for identifying the server in the topology).

* []()ID: 2544

  Severity: INFO\
  Message: Server ID.

* []()ID: 2545

  Severity: ERROR\
  Message: An error occurred while configuring the server ID or the advertised listen address in global configuration: %s.

* []()ID: 2546

  Severity: ERROR\
  Message: Server ID '%s' is not valid. A Server ID is an ASCII alpha-numeric string possibly containing underscore and hyphen characters.

* []()ID: 2547

  Severity: INFO\
  Message: Do you want to set a value for parameter '%s'?.

* []()ID: 2548

  Severity: INFO\
  Message: No value specified for '%s'.

* []()ID: 2549

  Severity: INFO\
  Message: Do you want to add another value for parameter '%s'?.

* []()ID: 2550

  Severity: INFO\
  Message: Provide hostname for '%s'.

* []()ID: 2551

  Severity: INFO\
  Message: Provide port for '%s'.

* []()ID: 2552

  Severity: INFO\
  Message: This utility configures profiles in an offline PingDS server instance. %s.

* []()ID: 2554

  Severity: INFO\
  Message: Name of the profile to be configured. If the version is not specified, the most recent version older or equal to this PingDS version is used. Use this option multiple times to apply multiple profiles.

* []()ID: 2555

  Severity: INFO\
  Message: configure profiles in an offline PingDS server instance.

* []()ID: 2556

  Severity: ERROR\
  Message: You must select at least one profile by using the option '%s'. %s.

* []()ID: 2557

  Severity: ERROR\
  Message: Instance path '%s' is not a valid existing directory.

* []()ID: 2558

  Severity: ERROR\
  Message: Instance path '%s' does not contain a PingDS instance.

* []()ID: 2560

  Severity: ERROR\
  Message: Profiles can be setup only when the server is offline, please stop the server and retry.

* []()ID: 2561

  Severity: ERROR\
  Message: An error occurred while reading file '%s': %s.

* []()ID: 2562

  Severity: ERROR\
  Message: Unable to setup the profile '%s' because it is already configured in the server.

* []()ID: 2563

  Severity: ERROR\
  Message: Unable to setup profiles '%s' because they are already configured in the server.

* []()ID: 2564

  Severity: INFO\
  Message: The deployment ID which should be used for securing the deployment. If no existing certificates are specified using the key-store and trust-store options then the deployment ID will also be used for securing all TLS network communication.

* []()ID: 2565

  Severity: INFO\
  Message: {deploymentId}.

* []()ID: 2566

  Severity: ERROR\
  Message: This deployment ID is using a key-pair generator which is not available in this Java environment. Retry the command with the Java environment that was used for generating this deployment ID.

* []()ID: 2567

  Severity: ERROR\
  Message: Unable to add certificates derived from deployment ID in keystore: %s.

* []()ID: 2568

  Severity: ERROR\
  Message: An error occurred while configuring replication: %s.

* []()ID: 2569

  Severity: INFO\
  Message: Deployment ID password.

* []()ID: 2570

  Severity: INFO\
  Message: {deploymentIdPassword}.

* []()ID: 2571

  Severity: INFO\
  Message: Provide the deployment ID password:.

* []()ID: 2572

  Severity: INFO\
  Message: Use deployment ID.

* []()ID: 2573

  Severity: ERROR\
  Message: An error occurred while attempting to update the administration connector port: %s.

* []()ID: 2574

  Severity: ERROR\
  Message: An error occurred while attempting to update the crypto manager in the Directory Server: %s.

* []()ID: 2575

  Severity: ERROR\
  Message: An error occurred while attempting to update the port on which to listen for LDAPS communication: %s.

* []()ID: 2576

  Severity: ERROR\
  Message: An error occurred while attempting to update the entry for the initial Directory Server root user: %s.

* []()ID: 2577

  Severity: ERROR\
  Message: Unable to bind to port %d. This port may already be in use, or you may not have permission to bind to it.

* []()ID: 2578

  Severity: ERROR\
  Message: Unable to bind to port %d. This port may already be in use, or you may not have permission to bind to it. On UNIX-based operating systems, non-root users may not be allowed to bind to ports 1 through 1024.

* []()ID: 2579

  Severity: ERROR\
  Message: Unable to write a required file. Make sure that the %s tool has sufficient permissions to create and write the file: %s.

* []()ID: 2580

  Severity: ERROR\
  Message: The root user password is missing, provide it with the --%s option.

* []()ID: 2581

  Severity: INFO\
  Message: install PingDS server.

* []()ID: 2582

  Severity: ERROR\
  Message: The provided password values do not match.

* []()ID: 2587

  Severity: INFO\
  Message: What would you like to do?.

* []()ID: 2588

  Severity: INFO\
  Message: Use nickname %s?.

* []()ID: 2589

  Severity: INFO\
  Message: Enable the server to run as a Windows Service?.

* []()ID: 2592

  Severity: INFO\
  Message: Keystore password:.

* []()ID: 2594

  Severity: ERROR\
  Message: Input tries limit reached (%d).

* []()ID: 2596

  Severity: ERROR\
  Message: An error occurred while attempting to enable key manager provider entry: %s.

* []()ID: 2597

  Severity: INFO\
  Message: To see basic server status and configuration, you can launch %s.

* []()ID: 2598

  Severity: INFO\
  Message: Disabled.

* []()ID: 2599

  Severity: INFO\
  Message: Enabled.

* []()ID: 2600

  Severity: INFO\
  Message: Port on which the Administration Connector should listen for communication.

* []()ID: 2601

  Severity: INFO\
  Message: Nickname of a keystore entry containing a certificate that the server should use when negotiating secure connections using StartTLS or SSL. Multiple keystore entries may be provided by using this option multiple times.

* []()ID: 2602

  Severity: INFO\
  Message: Start the server when the configuration is completed.

* []()ID: 2603

  Severity: INFO\
  Message: Enable StartTLS to allow secure communication with the server using the LDAP port.

* []()ID: 2604

  Severity: INFO\
  Message: Enable the server to run as a Windows Service.

* []()ID: 2605

  Severity: INFO\
  Message: The fully-qualified directory server host name that will be used when generating certificates for LDAP SSL/StartTLS, the administration connector, and replication.

* []()ID: 2606

  Severity: INFO\
  Message: Port on which the Directory Server should listen for LDAP communication.

* []()ID: 2607

  Severity: INFO\
  Message: Port on which the Directory Server should listen for LDAPS communication. The LDAPS port will be configured and SSL will be enabled only if this option is explicitly specified.

* []()ID: 2608

  Severity: INFO\
  Message: DN for the initial root user for the Directory Server.

* []()ID: 2609

  Severity: INFO\
  Message: Password for the initial root user for the Directory Server.

* []()ID: 2610

  Severity: INFO\
  Message: Skip the check to determine whether the specified ports are usable.

* []()ID: 2611

  Severity: INFO\
  Message: Use certificate(s) in a PKCS#11 token that the server should use when accepting SSL-based connections or performing StartTLS negotiation.

* []()ID: 2612

  Severity: INFO\
  Message: Path of a PKCS#12 keystore containing the certificate(s) that the server should use when negotiating secure connections using StartTLS or SSL.

* []()ID: 2613

  Severity: INFO\
  Message: {path}.

* []()ID: 2614

  Severity: INFO\
  Message: Path of the file containing the keystore password. The specified path will be used as the configuration value in the new server.

* []()ID: 2615

  Severity: INFO\
  Message: {nickname}.

* []()ID: 2616

  Severity: INFO\
  Message: {rootUserDN}.

* []()ID: 2617

  Severity: INFO\
  Message: {rootUserPassword}.

* []()ID: 2618

  Severity: INFO\
  Message: {path}.

* []()ID: 2619

  Severity: INFO\
  Message: Path of the file containing the truststore password. The specified path will be used as the configuration value in the new server.

* []()ID: 2620

  Severity: ERROR\
  Message: The deployment ID password is missing, provide it with the --%s option.

* []()ID: 2621

  Severity: INFO\
  Message: Same as deployment ID password.

* []()ID: 2622

  Severity: INFO\
  Message: The addresses of one or more replication servers within the topology which the server should connect to for discovering the rest of the topology. Use syntax "hostname:port" or "\[IPv6Address]:port" for IPv6 addresses.

* []()ID: 2623

  Severity: INFO\
  Message: {bootstrapReplicationServer}.

* []()ID: 2624

  Severity: INFO\
  Message: Port used for replication protocol communications with other servers. Use this option to configure a local replication server. When this option is not used, this server is configured as a standalone DS (no local replication server).

* []()ID: 2625

  Severity: INFO\
  Message: Replication port.

* []()ID: 2626

  Severity: INFO\
  Message: Replication (secure).

* []()ID: 2627

  Severity: INFO\
  Message: What are the hostname and port number of the server to replicate with? (e.g ds.example.com on port 8989).

* []()ID: 2628

  Severity: INFO\
  Message: Replication server hostname.

* []()ID: 2629

  Severity: ERROR\
  Message: '%s' is not a valid hostname.

* []()ID: 2630

  Severity: INFO\
  Message: Replication port on %s.

* []()ID: 2631

  Severity: INFO\
  Message: Do you want to add another replication server.

* []()ID: 2632

  Severity: INFO\
  Message: Do you want to specify a server to replicate with? This step can be skipped if this is the first server in the topology.

* []()ID: 2633

  Severity: INFO\
  Message: Replicate with server.

* []()ID: 2634

  Severity: INFO\
  Message: Error Installing Backup Cloud Extension for Directory Server: %s.

* []()ID: 2635

  Severity: INFO\
  Message: The Directory Server shutdown process has been initiated by task %s.

* []()ID: 2636

  Severity: INFO\
  Message: The Directory Server shutdown process has been initiated by task %s: %s.

* []()ID: 2637

  Severity: ERROR\
  Message: Unable to add one or more files to the server schema because no schema file names were provided in attribute %s of task entry %s.

* []()ID: 2638

  Severity: ERROR\
  Message: Unable to add one or more files to the server schema because the specified schema file %s does not exist in schema directory %s.

* []()ID: 2639

  Severity: ERROR\
  Message: Unable to add one or more files to the server schema because an error occurred while attempting to determine whether file %s exists in schema directory %s: %s.

* []()ID: 2640

  Severity: ERROR\
  Message: An error occurred while attempting to load the contents of schema file %s into the server schema: %s.

* []()ID: 2641

  Severity: ERROR\
  Message: Unable to add one or more files to the server schema because the server was unable to obtain a write lock on the schema entry %s after multiple attempts.

* []()ID: 2642

  Severity: ERROR\
  Message: You do not have sufficient privileges to modify the server schema.

* []()ID: 2643

  Severity: ERROR\
  Message: You do not have sufficient privileges to initiate a Directory Server backup or backup purge.

* []()ID: 2644

  Severity: ERROR\
  Message: You do not have sufficient privileges to initiate a Directory Server restore.

* []()ID: 2645

  Severity: ERROR\
  Message: You do not have sufficient privileges to initiate an LDIF import.

* []()ID: 2646

  Severity: ERROR\
  Message: You do not have sufficient privileges to initiate an LDIF export.

* []()ID: 2647

  Severity: ERROR\
  Message: You do not have sufficient privileges to initiate a Directory Server restart.

* []()ID: 2648

  Severity: ERROR\
  Message: You do not have sufficient privileges to initiate a Directory Server shutdown.

* []()ID: 2649

  Severity: ERROR\
  Message: An error occurred while attempting to notify a synchronization provider of type %s about the schema changes made by the add schema file task: %s.

* []()ID: 2650

  Severity: ERROR\
  Message: You do not have sufficient privileges to initiate an index rebuild.

* []()ID: 2651

  Severity: ERROR\
  Message: Invalid DN provided to the Initialize task: %s.

* []()ID: 2652

  Severity: ERROR\
  Message: Only users with the SERVER\_LOCKDOWN privilege may place the server in lockdown mode.

* []()ID: 2653

  Severity: ERROR\
  Message: Only users with the SERVER\_LOCKDOWN privilege connected from a loopback address may place the server in lockdown mode.

* []()ID: 2654

  Severity: ERROR\
  Message: Only users with the SERVER\_LOCKDOWN privilege may cause the server to leave lockdown mode.

* []()ID: 2655

  Severity: ERROR\
  Message: Only users with the SERVER\_LOCKDOWN privilege connected from a loopback address may cause the server to leave lockdown mode.

* []()ID: 2656

  Severity: ERROR\
  Message: You do not have sufficient privileges to terminate client connections.

* []()ID: 2657

  Severity: ERROR\
  Message: Unable to decode value %s as an integer connection ID.

* []()ID: 2658

  Severity: ERROR\
  Message: Attribute %s must be provided to specify the connection ID for the client to disconnect.

* []()ID: 2659

  Severity: ERROR\
  Message: Unable to decode value %s as an indication of whether to notify the client before disconnecting it. The provided value should be either 'true' or 'false'.

* []()ID: 2660

  Severity: INFO\
  Message: An administrator has terminated this client connection.

* []()ID: 2661

  Severity: ERROR\
  Message: There is no client connection with connection ID %s.

* []()ID: 2662

  Severity: INFO\
  Message: Add Schema File.

* []()ID: 2663

  Severity: INFO\
  Message: Backup.

* []()ID: 2664

  Severity: INFO\
  Message: Disconnect Client.

* []()ID: 2665

  Severity: INFO\
  Message: Lockdown.

* []()ID: 2666

  Severity: INFO\
  Message: Export.

* []()ID: 2667

  Severity: INFO\
  Message: Import.

* []()ID: 2668

  Severity: INFO\
  Message: Initialize Backend.

* []()ID: 2669

  Severity: INFO\
  Message: Initialize From Replica.

* []()ID: 2670

  Severity: INFO\
  Message: Leave Lockdown.

* []()ID: 2671

  Severity: INFO\
  Message: Rebuild Index.

* []()ID: 2672

  Severity: INFO\
  Message: Restore.

* []()ID: 2673

  Severity: INFO\
  Message: Set Generation ID.

* []()ID: 2674

  Severity: INFO\
  Message: Shutdown.

* []()ID: 2675

  Severity: INFO\
  Message: Unscheduled.

* []()ID: 2676

  Severity: INFO\
  Message: Disabled.

* []()ID: 2677

  Severity: INFO\
  Message: Waiting on start time.

* []()ID: 2678

  Severity: INFO\
  Message: Waiting on dependency.

* []()ID: 2679

  Severity: INFO\
  Message: Running.

* []()ID: 2680

  Severity: INFO\
  Message: Completed successfully.

* []()ID: 2681

  Severity: INFO\
  Message: Completed with errors.

* []()ID: 2682

  Severity: INFO\
  Message: Stopped by shutdown.

* []()ID: 2683

  Severity: INFO\
  Message: Stopped by error.

* []()ID: 2684

  Severity: INFO\
  Message: Stopped by administrator.

* []()ID: 2685

  Severity: INFO\
  Message: Canceled before starting.

* []()ID: 2686

  Severity: INFO\
  Message: Backend ID(s).

* []()ID: 2687

  Severity: INFO\
  Message: Backup Location.

* []()ID: 2688

  Severity: INFO\
  Message: LDIF File.

* []()ID: 2689

  Severity: INFO\
  Message: Backend ID.

* []()ID: 2690

  Severity: INFO\
  Message: Append To LDIF.

* []()ID: 2691

  Severity: INFO\
  Message: Compress LDIF.

* []()ID: 2692

  Severity: INFO\
  Message: Encrypt LDIF.

* []()ID: 2693

  Severity: INFO\
  Message: Sign Hash.

* []()ID: 2694

  Severity: INFO\
  Message: Include Attribute.

* []()ID: 2695

  Severity: INFO\
  Message: Exclude Attribute.

* []()ID: 2696

  Severity: INFO\
  Message: Include Filter.

* []()ID: 2697

  Severity: INFO\
  Message: Exclude Filter.

* []()ID: 2698

  Severity: INFO\
  Message: Include Branch.

* []()ID: 2699

  Severity: INFO\
  Message: Exclude Branch.

* []()ID: 2700

  Severity: INFO\
  Message: Wrap Column.

* []()ID: 2701

  Severity: INFO\
  Message: Backup Directory.

* []()ID: 2702

  Severity: INFO\
  Message: Backup ID.

* []()ID: 2703

  Severity: INFO\
  Message: LDIF File.

* []()ID: 2704

  Severity: INFO\
  Message: Backend ID.

* []()ID: 2705

  Severity: INFO\
  Message: Include Attribute.

* []()ID: 2706

  Severity: INFO\
  Message: Exclude Attribute.

* []()ID: 2707

  Severity: INFO\
  Message: Include Filter.

* []()ID: 2708

  Severity: INFO\
  Message: Exclude Filter.

* []()ID: 2709

  Severity: INFO\
  Message: Include Branch.

* []()ID: 2710

  Severity: INFO\
  Message: Exclude Branch.

* []()ID: 2711

  Severity: INFO\
  Message: Reject File.

* []()ID: 2712

  Severity: INFO\
  Message: Skip File.

* []()ID: 2713

  Severity: INFO\
  Message: Overwrite.

* []()ID: 2714

  Severity: INFO\
  Message: Skip Schema Validation.

* []()ID: 2715

  Severity: INFO\
  Message: Is Compressed.

* []()ID: 2716

  Severity: INFO\
  Message: Is Encrypted.

* []()ID: 2717

  Severity: INFO\
  Message: Clear Backend.

* []()ID: 2718

  Severity: INFO\
  Message: Process.

* []()ID: 2719

  Severity: INFO\
  Message: Cancel.

* []()ID: 2720

  Severity: INFO\
  Message: Disable.

* []()ID: 2721

  Severity: INFO\
  Message: Task was stopped by an administrator: %s.

* []()ID: 2723

  Severity: INFO\
  Message: Template File.

* []()ID: 2724

  Severity: INFO\
  Message: Random Seed.

* []()ID: 2725

  Severity: INFO\
  Message: Recurring.

* []()ID: 2726

  Severity: ERROR\
  Message: Index option cannot be specified when the --rebuildAll or --rebuildUntrusted option is used.

* []()ID: 2727

  Severity: INFO\
  Message: Purge conflicts historical.

* []()ID: 2728

  Severity: ERROR\
  Message: Attribute %s has an invalid value. Reason: %s.

* []()ID: 2734

  Severity: ERROR\
  Message: The changes made by the add schema file task failed schema validation: %s.

* []()ID: 2735

  Severity: INFO\
  Message: Retrying.

* []()ID: 2736

  Severity: INFO\
  Message: Storage property.

* []()ID: 2737

  Severity: INFO\
  Message: Purge backup(s).

* []()ID: 2738

  Severity: INFO\
  Message: Backup location.

* []()ID: 2739

  Severity: INFO\
  Message: Backup ID(s).

* []()ID: 2740

  Severity: INFO\
  Message: Keep count.

* []()ID: 2741

  Severity: INFO\
  Message: Remove older than.

* []()ID: 2742

  Severity: INFO\
  Message: Force.

* []()ID: 2743

  Severity: INFO\
  Message: Backend name(s).

* []()ID: 2744

  Severity: ERROR\
  Message: Invalid DN provided to the Initialize Target task: %s.

* []()ID: 2745

  Severity: ERROR\
  Message: Invalid DN provided to the Purge Conflicts Historical task: %s.

* []()ID: 2746

  Severity: ERROR\
  Message: Invalid DN provided to the Reset Generation ID task: %s.

* []()ID: 2747

  Severity: INFO\
  Message: List available password storage schemes.

* []()ID: 2748

  Severity: INFO\
  Message: Clear-text password to encode or to compare against an encoded password.

* []()ID: 2749

  Severity: INFO\
  Message: Encoded password to compare against the clear-text password.

* []()ID: 2750

  Severity: INFO\
  Message: Scheme to use for the encoded password.

* []()ID: 2751

  Severity: ERROR\
  Message: An error occurred while parsing the command-line arguments: %s.

* []()ID: 2752

  Severity: ERROR\
  Message: No clear-text password was specified. Use --%s, --%s or --%s to specify the password to encode.

* []()ID: 2753

  Severity: ERROR\
  Message: No password storage scheme was specified. Use the --%s argument to specify the storage scheme.

* []()ID: 2755

  Severity: ERROR\
  Message: An error occurred while trying to load the Directory Server configuration: %s.

* []()ID: 2756

  Severity: ERROR\
  Message: An error occurred while trying to load the Directory Server schema: %s.

* []()ID: 2757

  Severity: ERROR\
  Message: An error occurred while trying to initialize the core Directory Server configuration: %s.

* []()ID: 2758

  Severity: ERROR\
  Message: An error occurred while trying to initialize the Directory Server password storage schemes: %s.

* []()ID: 2759

  Severity: ERROR\
  Message: No password storage schemes have been configured for use in the Directory Server.

* []()ID: 2760

  Severity: ERROR\
  Message: Password storage scheme "%s" is not configured for use in the Directory Server.

* []()ID: 2761

  Severity: INFO\
  Message: The provided clear-text and encoded passwords match.

* []()ID: 2762

  Severity: INFO\
  Message: The provided clear-text and encoded passwords do not match.

* []()ID: 2763

  Severity: ERROR\
  Message: An error occurred while attempting to encode the clear-text password: %s.

* []()ID: 2764

  Severity: INFO\
  Message: Path to the LDIF file to write. All paths are relative to the server's installation directory, which can be remote.

* []()ID: 2765

  Severity: INFO\
  Message: Append an existing LDIF file rather than overwriting it.

* []()ID: 2766

  Severity: INFO\
  Message: Backend ID for the backend to export.

* []()ID: 2767

  Severity: INFO\
  Message: Base DN of a branch to exclude from the LDIF export.

* []()ID: 2768

  Severity: INFO\
  Message: Attribute to include in the LDIF export.

* []()ID: 2769

  Severity: INFO\
  Message: Attribute to exclude from the LDIF export.

* []()ID: 2770

  Severity: INFO\
  Message: Filter to identify entries to include in the LDIF export.

* []()ID: 2771

  Severity: INFO\
  Message: Filter to identify entries to exclude from the LDIF export.

* []()ID: 2772

  Severity: INFO\
  Message: Column at which to wrap long lines (0 for no wrapping).

* []()ID: 2773

  Severity: INFO\
  Message: Compress the LDIF data as it is exported.

* []()ID: 2774

  Severity: ERROR\
  Message: Unable to decode exclude filter string "%s" as a valid search filter: %s.

* []()ID: 2775

  Severity: ERROR\
  Message: Unable to decode include filter string "%s" as a valid search filter: %s.

* []()ID: 2776

  Severity: ERROR\
  Message: Unable to decode base DN string "%s" as a valid distinguished name: %s.

* []()ID: 2777

  Severity: ERROR\
  Message: Multiple Directory Server backends are configured with the requested backend ID "%s".

* []()ID: 2778

  Severity: ERROR\
  Message: None of the Directory Server backends are configured with the requested backend ID "%s".

* []()ID: 2779

  Severity: ERROR\
  Message: Unable to decode exclude branch string "%s" as a valid distinguished name: %s.

* []()ID: 2780

  Severity: ERROR\
  Message: Unable to decode wrap column value "%s" as an integer.

* []()ID: 2781

  Severity: ERROR\
  Message: An error occurred while attempting to process the LDIF export: %s.

* []()ID: 2782

  Severity: ERROR\
  Message: Unable to load class %s referenced in configuration entry %s for use as a Directory Server backend: %s.

* []()ID: 2783

  Severity: ERROR\
  Message: Unable to create an instance of class %s referenced in configuration entry %s as a Directory Server backend: %s.

* []()ID: 2784

  Severity: INFO\
  Message: Path to the LDIF file to import. All paths are relative to the server's installation directory, which can be remote.

* []()ID: 2785

  Severity: INFO\
  Message: Backend ID for the backend to import.

* []()ID: 2786

  Severity: INFO\
  Message: Base DN of a branch to exclude from the LDIF import.

* []()ID: 2787

  Severity: INFO\
  Message: Attribute to include in the LDIF import.

* []()ID: 2788

  Severity: INFO\
  Message: Attribute to exclude from the LDIF import.

* []()ID: 2789

  Severity: INFO\
  Message: Filter to identify entries to include in the LDIF import.

* []()ID: 2790

  Severity: INFO\
  Message: Filter to identify entries to exclude from the LDIF import.

* []()ID: 2791

  Severity: INFO\
  Message: Write rejected entries to the specified file.

* []()ID: 2792

  Severity: INFO\
  Message: Overwrite an existing rejects and/or skip file rather than appending to it.

* []()ID: 2793

  Severity: INFO\
  Message: LDIF file is compressed.

* []()ID: 2794

  Severity: ERROR\
  Message: Unable to decode exclude filter string "%s" as a valid search filter: %s.

* []()ID: 2795

  Severity: ERROR\
  Message: Unable to decode include filter string "%s" as a valid search filter: %s.

* []()ID: 2796

  Severity: ERROR\
  Message: Imported branches or backend IDs can not span across multiple Directory Server backends.

* []()ID: 2797

  Severity: ERROR\
  Message: None of the Directory Server backends are configured with the requested backend ID or base DNs that include the specified branches.

* []()ID: 2798

  Severity: ERROR\
  Message: Unable to decode exclude branch string "%s" as a valid distinguished name: %s.

* []()ID: 2799

  Severity: ERROR\
  Message: An error occurred while trying to open the rejects file %s for writing: %s.

* []()ID: 2800

  Severity: ERROR\
  Message: An error occurred while attempting to process the LDIF import: %s.

* []()ID: 2801

  Severity: INFO\
  Message: Base DN of a backend supporting indexing. Verification is performed on indexes within the scope of the given base DN.

* []()ID: 2802

  Severity: INFO\
  Message: Name of an index to be verified. For an attribute index this is simply an attribute name. Multiple indexes may be verified for completeness, or all indexes if no indexes are specified. An index is complete if each index value references all entries containing that value.

* []()ID: 2803

  Severity: INFO\
  Message: Specifies that a single index should be verified to ensure it is clean. An index is clean if each index value references only entries containing that value. Only one index at a time may be verified in this way.

* []()ID: 2804

  Severity: ERROR\
  Message: An error occurred while attempting to perform index verification: %s.

* []()ID: 2805

  Severity: ERROR\
  Message: Only one index at a time may be verified for cleanliness.

* []()ID: 2806

  Severity: ERROR\
  Message: The backend does not support indexing.

* []()ID: 2807

  Severity: ERROR\
  Message: The Directory Server backend with backend ID "%s" does not provide a mechanism for performing LDIF exports.

* []()ID: 2808

  Severity: ERROR\
  Message: The Directory Server backend with backend ID %s does not provide a mechanism for performing LDIF imports.

* []()ID: 2809

  Severity: INFO\
  Message: Base DN of a branch to include in the LDIF import.

* []()ID: 2810

  Severity: ERROR\
  Message: Unable to decode include branch string "%s" as a valid distinguished name: %s.

* []()ID: 2811

  Severity: ERROR\
  Message: Provided include base DN "%s" is not handled by the backend with backend ID %s.

* []()ID: 2812

  Severity: ERROR\
  Message: Multiple Directory Server backends are configured to support base DN "%s".

* []()ID: 2813

  Severity: ERROR\
  Message: None of the Directory Server backends are configured to support the requested base DN "%s".

* []()ID: 2814

  Severity: INFO\
  Message: Base DN of a branch to include in the LDIF export.

* []()ID: 2815

  Severity: ERROR\
  Message: Provided include base DN "%s" is not handled by the backend with backend ID %s.

* []()ID: 2816

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the crypto manager: %s.

* []()ID: 2817

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the subentry manager: %s.

* []()ID: 2818

  Severity: ERROR\
  Message: An error occurred while attempting to acquire an exclusive lock for backend %s: %s. This generally means some other process is still using this backend (e.g., it is in use by the Directory Server or a backup or LDIF export is in progress). The LDIF import cannot continue.

* []()ID: 2819

  Severity: WARNING\
  Message: An error occurred while attempting to release the exclusive lock for backend %s: %s. This lock should automatically be cleared when the import process exits, so no further action should be required.

* []()ID: 2820

  Severity: ERROR\
  Message: An error occurred while attempting to acquire a shared lock for backend %s: %s. This generally means that some other process has an exclusive lock on this backend (e.g., an LDIF import or a restore). The LDIF export cannot continue.

* []()ID: 2821

  Severity: WARNING\
  Message: An error occurred while attempting to release the shared lock for backend %s: %s. This lock should automatically be cleared when the export process exits, so no further action should be required.

* []()ID: 2822

  Severity: ERROR\
  Message: An error occurred while attempting to acquire a shared lock for backend %s: %s. This generally means that some other process has an exclusive lock on this backend (e.g., an LDIF import or a restore). The index verification cannot continue.

* []()ID: 2823

  Severity: WARNING\
  Message: An error occurred while attempting to release the shared lock for backend %s: %s. This lock should automatically be cleared when the verification process exits, so no further action should be required.

* []()ID: 2824

  Severity: INFO\
  Message: Skip schema validation during the LDIF import.

* []()ID: 2825

  Severity: INFO\
  Message: Use the authentication password syntax rather than the user password syntax.

* []()ID: 2826

  Severity: ERROR\
  Message: Authentication password storage scheme "%s" is not configured for use in the Directory Server.

* []()ID: 2827

  Severity: ERROR\
  Message: The provided password is not a valid encoded authentication password value: %s.

* []()ID: 2828

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the password policy components: %s.

* []()ID: 2829

  Severity: INFO\
  Message: Reason the server is being stopped or restarted.

* []()ID: 2830

  Severity: INFO\
  Message: Indicates the date/time at which the shutdown operation will begin as a server task expressed in format YYYYMMDDhhmmssZ for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the shutdown to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* []()ID: 2831

  Severity: ERROR\
  Message: ERROR: Unable to decode the provided stop time. It should be in the form YYYYMMDDhhmmssZ for UTC time or YYYYMMDDhhmmss for local time.

* []()ID: 2832

  Severity: ERROR\
  Message: ERROR: An I/O error occurred while attempting to communicate with the Directory Server: %s.

* []()ID: 2833

  Severity: INFO\
  Message: Use quiet mode (no output).

* []()ID: 2834

  Severity: INFO\
  Message: Path to a MakeLDIF template to use to generate the import data.

* []()ID: 2835

  Severity: ERROR\
  Message: Neither the %s nor the %s argument was provided. One of these arguments must be given to specify the source for the LDIF data to be imported.

* []()ID: 2836

  Severity: ERROR\
  Message: Unable to parse the specified file %s as a MakeLDIF template file: %s.

* []()ID: 2837

  Severity: INFO\
  Message: Seed for the MakeLDIF random number generator. To always generate the same data with the same command, use the same non-zero seed value. A value of zero (the default) results in different data each time the tool is run.

* []()ID: 2838

  Severity: INFO\
  Message: Path to the file to watch for deletion.

* []()ID: 2839

  Severity: INFO\
  Message: Path to a file containing log output to monitor.

* []()ID: 2840

  Severity: INFO\
  Message: Maximum length of time in seconds to wait for the target file to be deleted before exiting.

* []()ID: 2841

  Severity: WARNING\
  Message: WARNING: Unable to open log file %s for reading: %s.

* []()ID: 2842

  Severity: INFO\
  Message: This utility can be used to encode user passwords with a specified storage scheme, or to determine whether a given clear-text value matches a provided encoded password.

* []()ID: 2843

  Severity: INFO\
  Message: This utility can be used to export data from a Directory Server backend in LDIF form.

* []()ID: 2844

  Severity: INFO\
  Message: This utility can be used to import LDIF data into a Directory Server backend, overwriting existing data. It cannot be used to append data to the backend database.

* []()ID: 2845

  Severity: INFO\
  Message: This utility can be used to request that the Directory Server stop running or perform a restart. When run without explicit connection options, this utility sends a signal to the PingDS process to stop the server. When run with explicit connection options, this utility connects to the PingDS administration port and creates a shutdown task to stop the server.

* []()ID: 2846

  Severity: INFO\
  Message: This utility ensures that index data is consistent within an indexed backend database.

* []()ID: 2847

  Severity: INFO\
  Message: This utility can be used to wait for a file to be removed from the filesystem.

* []()ID: 2848

  Severity: ERROR\
  Message: The provided password is not a valid encoded user password value: %s.

* []()ID: 2849

  Severity: INFO\
  Message: Use the LDAP compare result as an exit code for the password comparison.

* []()ID: 2850

  Severity: INFO\
  Message: Exclude operational attributes from the LDIF export.

* []()ID: 2851

  Severity: INFO\
  Message: Server already stopped.

* []()ID: 2852

  Severity: INFO\
  Message: Stopping Server…​

* []()ID: 2853

  Severity: ERROR\
  Message: Could not find the service name for the server.

* []()ID: 2854

  Severity: ERROR\
  Message: An unexpected error occurred starting the server as a windows service.

* []()ID: 2855

  Severity: ERROR\
  Message: An unexpected error occurred stopping the server windows service.

* []()ID: 2856

  Severity: INFO\
  Message: This utility can be used to configure the server as a Windows service.

* []()ID: 2857

  Severity: INFO\
  Message: Enables the server as a Windows service.

* []()ID: 2858

  Severity: INFO\
  Message: Disables the server as a Windows service and stops the server.

* []()ID: 2859

  Severity: INFO\
  Message: Provides information about the state of the server as a Windows service.

* []()ID: 2860

  Severity: ERROR\
  Message: You can only provide one of the following arguments: enableService, disableService, serviceState or cleanupService.

* []()ID: 2861

  Severity: ERROR\
  Message: You must provide at least one of the following arguments: enableService, disableService or serviceState or cleanupService.

* []()ID: 2862

  Severity: INFO\
  Message: %s.

* []()ID: 2863

  Severity: INFO\
  Message: Next Generation Directory Server. Installation path: %s.

* []()ID: 2864

  Severity: INFO\
  Message: The server was successfully enabled to run as a Windows service.

* []()ID: 2865

  Severity: INFO\
  Message: The server was already enabled to run as a Windows service.

* []()ID: 2866

  Severity: ERROR\
  Message: The server could not be enabled to run as a Windows service. The service name is already in use.

* []()ID: 2867

  Severity: ERROR\
  Message: An unexpected error occurred trying to enable the server as a Windows service.%nCheck that you have administrator rights (only Administrators can enable the server to run as a Windows Service).

* []()ID: 2868

  Severity: INFO\
  Message: The server was successfully disabled as a Windows service.

* []()ID: 2869

  Severity: INFO\
  Message: The server was already disabled as a Windows service.

* []()ID: 2870

  Severity: WARNING\
  Message: The server has been marked for deletion as a Windows Service.

* []()ID: 2871

  Severity: ERROR\
  Message: An unexpected error occurred trying to disable the server as a Windows service%nCheck that you have administrator rights (only Administrators can disable the server as a Windows Service).

* []()ID: 2872

  Severity: INFO\
  Message: The server is enabled as a Windows service. The service name for the server is: %s.

* []()ID: 2873

  Severity: INFO\
  Message: The server is disabled as a Windows service.

* []()ID: 2874

  Severity: ERROR\
  Message: An unexpected error occurred trying to retrieve the state of the server as a Windows service.

* []()ID: 2875

  Severity: INFO\
  Message: Path to a file to which the command will write the output.

* []()ID: 2876

  Severity: WARNING\
  Message: WARNING: Unable to open output file %s for writing: %s.

* []()ID: 2877

  Severity: INFO\
  Message: Disables the server as a Windows service and removes the Windows registry information associated with the specified service.

* []()ID: 2878

  Severity: INFO\
  Message: Clean up of service %s was successful.

* []()ID: 2879

  Severity: ERROR\
  Message: Could not find the service with name %s.

* []()ID: 2880

  Severity: WARNING\
  Message: Service %s has been marked for deletion.

* []()ID: 2881

  Severity: ERROR\
  Message: An unexpected error occurred cleaning up the service %s.

* []()ID: 2882

  Severity: INFO\
  Message: This utility can be used to rebuild index data within an indexed backend database.

* []()ID: 2883

  Severity: INFO\
  Message: Base DN of a backend supporting indexing. Rebuild is performed on indexes within the scope of the given base DN.

* []()ID: 2884

  Severity: INFO\
  Message: Names of index(es) to rebuild. For an attribute index this is simply an attribute name. At least one index must be specified for rebuild. Cannot be used with the "--rebuildAll" option.

* []()ID: 2885

  Severity: ERROR\
  Message: An error occurred while attempting to perform index rebuild: %s.

* []()ID: 2886

  Severity: ERROR\
  Message: The backend does not support rebuilding of indexes.

* []()ID: 2887

  Severity: ERROR\
  Message: At least one index must be specified for the rebuild process.

* []()ID: 2888

  Severity: ERROR\
  Message: An error occurred while attempting to acquire a exclusive lock for backend %s: %s. This generally means that some other process has an lock on this backend or the server is running with this backend online. The rebuild process cannot continue.

* []()ID: 2889

  Severity: WARNING\
  Message: An error occurred while attempting to release the shared lock for backend %s: %s. This lock should automatically be cleared when the rebuild process exits, so no further action should be required.

* []()ID: 2890

  Severity: ERROR\
  Message: An error occurred while attempting to acquire a shared lock for backend %s: %s. This generally means that some other process has an exclusive lock on this backend (e.g., an LDIF import or a restore). The rebuild process cannot continue.

* []()ID: 2891

  Severity: ERROR\
  Message: The specified LDIF file %s cannot be read.

* []()ID: 2892

  Severity: INFO\
  Message: Count the number of entries rejected by the server and return that value as the exit code (values > 255 will be reduced to 255 due to exit code restrictions).

* []()ID: 2893

  Severity: INFO\
  Message: Write skipped entries to the specified file.

* []()ID: 2894

  Severity: ERROR\
  Message: An error occurred while trying to open the skip file %s for writing: %s.

* []()ID: 2895

  Severity: INFO\
  Message: Count the number of errors found during the verification and return that value as the exit code (values > 255 will be reduced to 255 due to exit code restrictions).

* []()ID: 2896

  Severity: INFO\
  Message: Remove all entries for all base DNs in the backend before importing.

* []()ID: 2897

  Severity: ERROR\
  Message: Neither the %s nor the %s argument was provided. One of these arguments must be given to specify the backend for the LDIF data to be imported to.

* []()ID: 2898

  Severity: INFO\
  Message: %s task %s scheduled to start immediately.

* []()ID: 2899

  Severity: ERROR\
  Message: This tool may only be used on UNIX-based systems.

* []()ID: 2900

  Severity: INFO\
  Message: Create an RC script or systemd service that may be used to start, stop, and restart the Directory Server on UNIX-based systems.

* []()ID: 2901

  Severity: INFO\
  Message: The path to the RC script to create.

* []()ID: 2903

  Severity: ERROR\
  Message: An error occurred while attempting to generate the RC script: %s.

* []()ID: 2904

  Severity: INFO\
  Message: List the base DNs in a backend.

* []()ID: 2905

  Severity: INFO\
  Message: The backend ID of the backend.

* []()ID: 2906

  Severity: INFO\
  Message: The base DN.

* []()ID: 2908

  Severity: INFO\
  Message: Do not try to decode backend data to their appropriate types.

* []()ID: 2909

  Severity: INFO\
  Message: Shows the status of indexes for a backend base DN. This subcommand can take a long time to complete, as it reads all indexes of the backend.

* []()ID: 2910

  Severity: INFO\
  Message: Only show records with keys that should be ordered before the provided value using the comparator for the database container.

* []()ID: 2911

  Severity: INFO\
  Message: Only show records with keys that should be ordered after the provided value using the comparator for the database container.

* []()ID: 2912

  Severity: INFO\
  Message: Only show records whose data is no larger than the provided value.

* []()ID: 2913

  Severity: INFO\
  Message: Only show records whose data is no smaller than the provided value.

* []()ID: 2914

  Severity: INFO\
  Message: Backend ID.

* []()ID: 2915

  Severity: INFO\
  Message: Base DN.

* []()ID: 2916

  Severity: ERROR\
  Message: None of the Directory Server JE backends are configured with the requested backend ID %s.

* []()ID: 2917

  Severity: ERROR\
  Message: None of the entry containers are configured with the requested base DN '%s' in backend '%s'.

* []()ID: 2918

  Severity: ERROR\
  Message: Unable to decode base DN string '%s' as a valid distinguished name: %s.

* []()ID: 2919

  Severity: INFO\
  Message: Median.

* []()ID: 2920

  Severity: INFO\
  Message: Key Count.

* []()ID: 2921

  Severity: INFO\
  Message: Size.

* []()ID: 2922

  Severity: INFO\
  Message: Records.

* []()ID: 2923

  Severity: INFO\
  Message: Index Name.

* []()ID: 2924

  Severity: INFO\
  Message: Type.

* []()ID: 2925

  Severity: INFO\
  Message: Secure.

* []()ID: 2926

  Severity: INFO\
  Message: Entry Limit.

* []()ID: 2927

  Severity: INFO\
  Message: Mean.

* []()ID: 2928

  Severity: WARNING\
  Message: An error occurred while attempting to release the shared lock for backend %s: %s. This lock should automatically be cleared when the process exits, so no further action should be required.

* []()ID: 2929

  Severity: ERROR\
  Message: An error occurred while attempting to acquire a shared lock for backend %s: %s. This generally means that some other process has exclusive access to this backend (e.g., a restore or an LDIF import).

* []()ID: 2930

  Severity: INFO\
  Message: Over.

* []()ID: 2931

  Severity: INFO\
  Message: 80th.

* []()ID: 2932

  Severity: INFO\
  Message: 95th.

* []()ID: 2933

  Severity: INFO\
  Message: 99th.

* []()ID: 2934

  Severity: ERROR\
  Message: A sub-command must be specified.

* []()ID: 2935

  Severity: INFO\
  Message: The name of the user account under which the server should run.

* []()ID: 2936

  Severity: INFO\
  Message: The path to the Java installation that should be used to run the server.

* []()ID: 2937

  Severity: INFO\
  Message: A set of arguments that should be passed to the JVM when running the server.

* []()ID: 2938

  Severity: ERROR\
  Message: The directory %s specified as the DS\_JAVA\_HOME path does not exist or is not a directory.

* []()ID: 2939

  Severity: ERROR\
  Message: The argument '%s' is incompatible with '%s'.

* []()ID: 2940

  Severity: INFO\
  Message: This utility can be used to obtain a list of tasks scheduled to run within the Directory Server as well as information about individual tasks.

* []()ID: 2941

  Severity: INFO\
  Message: Print a summary of tasks.

* []()ID: 2942

  Severity: INFO\
  Message: ID of a particular task about which this tool will display information.

* []()ID: 2943

  Severity: INFO\
  Message: refresh.

* []()ID: 2944

  Severity: INFO\
  Message: cancel task.

* []()ID: 2945

  Severity: INFO\
  Message: view logs.

* []()ID: 2946

  Severity: INFO\
  Message: Enter the number of a task to cancel.

* []()ID: 2947

  Severity: ERROR\
  Message: Invalid menu item or task number '%s'.

* []()ID: 2948

  Severity: INFO\
  Message: ID.

* []()ID: 2949

  Severity: INFO\
  Message: Type.

* []()ID: 2950

  Severity: INFO\
  Message: Status.

* []()ID: 2951

  Severity: INFO\
  Message: Scheduled Start Time.

* []()ID: 2952

  Severity: INFO\
  Message: Actual Start Time.

* []()ID: 2953

  Severity: INFO\
  Message: Completion Time.

* []()ID: 2954

  Severity: INFO\
  Message: Dependencies.

* []()ID: 2955

  Severity: INFO\
  Message: Failed Dependency Action.

* []()ID: 2956

  Severity: INFO\
  Message: Log Message(s).

* []()ID: 2957

  Severity: INFO\
  Message: Last Log Message.

* []()ID: 2958

  Severity: INFO\
  Message: Email Upon Completion.

* []()ID: 2959

  Severity: INFO\
  Message: Email Upon Error.

* []()ID: 2960

  Severity: INFO\
  Message: Task %s canceled.

* []()ID: 2961

  Severity: ERROR\
  Message: Error retrieving task entry %s: %s.

* []()ID: 2962

  Severity: ERROR\
  Message: There are no tasks with ID %s.

* []()ID: 2963

  Severity: INFO\
  Message: Task Details.

* []()ID: 2964

  Severity: INFO\
  Message: %s Options.

* []()ID: 2965

  Severity: INFO\
  Message: No tasks exist.

* []()ID: 2966

  Severity: INFO\
  Message: None.

* []()ID: 2967

  Severity: INFO\
  Message: None Specified.

* []()ID: 2968

  Severity: INFO\
  Message: Immediate execution.

* []()ID: 2969

  Severity: INFO\
  Message: Error connecting to the directory server: '%s'. Verify that the connection options are correct and that the server is running.

* []()ID: 2970

  Severity: INFO\
  Message: ID of a particular task to cancel.

* []()ID: 2971

  Severity: INFO\
  Message: Show only tasks of this type.

* []()ID: 2972

  Severity: INFO\
  Message: {taskType}.

* []()ID: 2973

  Severity: INFO\
  Message: Show only tasks with this status.

* []()ID: 2974

  Severity: INFO\
  Message: {taskStatus}.

* []()ID: 2975

  Severity: ERROR\
  Message: Error canceling task '%s': %s.

* []()ID: 2976

  Severity: ERROR\
  Message: Error accessing logs for task '%s': %s.

* []()ID: 2977

  Severity: ERROR\
  Message: Task at index %d is not cancelable.

* []()ID: 2978

  Severity: INFO\
  Message: There are currently no cancelable tasks.

* []()ID: 2979

  Severity: ERROR\
  Message: There are no tasks defined with ID '%s'.

* []()ID: 2980

  Severity: ERROR\
  Message: Task '%s' has finished and cannot be canceled.

* []()ID: 2981

  Severity: ERROR\
  Message: State for task '%s' cannot be determined.

* []()ID: 2982

  Severity: INFO\
  Message: Indicates the date/time at which this operation will start when scheduled as a server task expressed in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time. A value of '0' will cause the task to be scheduled for immediate execution. When this option is specified the operation will be scheduled to start at the specified time after which this utility will exit immediately.

* []()ID: 2983

  Severity: ERROR\
  Message: The start date/time must in YYYYMMDDhhmmssZ format for UTC time or YYYYMMDDhhmmss for local time.

* []()ID: 2984

  Severity: INFO\
  Message: %s task %s scheduled to start %s.

* []()ID: 2985

  Severity: ERROR\
  Message: You have provided options for scheduling this operation as a task but options provided for connecting to the server's tasks backend resulted in the following error: '%s'.

* []()ID: 2986

  Severity: INFO\
  Message: Task Scheduling Options.

* []()ID: 2987

  Severity: INFO\
  Message: Task Backend Connection Options.

* []()ID: 2988

  Severity: INFO\
  Message: Email address of a recipient to be notified when the task completes. This option may be specified more than once.

* []()ID: 2989

  Severity: INFO\
  Message: Email address of a recipient to be notified if an error occurs when this task executes. This option may be specified more than once.

* []()ID: 2990

  Severity: INFO\
  Message: ID of a task upon which this task depends. A task will not start execution until all its dependencies have completed execution.

* []()ID: 2991

  Severity: INFO\
  Message: Action this task will take should one if its dependent tasks fail. The value must be one of %s. If not specified defaults to %s.

* []()ID: 2992

  Severity: ERROR\
  Message: The option %s is only applicable when scheduling this operation as a task.

* []()ID: 2993

  Severity: ERROR\
  Message: The value %s for option %s is not a valid email address.

* []()ID: 2994

  Severity: ERROR\
  Message: The failed dependency action value %s is invalid. The value must be one of %s.

* []()ID: 2995

  Severity: ERROR\
  Message: The failed dependency action option is to be used in conjunction with one or more dependencies.

* []()ID: 2996

  Severity: ERROR\
  Message: Error: task %s is not in a cancelable state.

* []()ID: 2997

  Severity: INFO\
  Message: {ldifFile}.

* []()ID: 2998

  Severity: INFO\
  Message: {seed}.

* []()ID: 2999

  Severity: INFO\
  Message: {host}.

* []()ID: 3000

  Severity: INFO\
  Message: {baseDN}.

## IDs: 3001-3500

* []()ID: 3001

  Severity: INFO\
  Message: {path}.

* []()ID: 3002

  Severity: INFO\
  Message: {filter}.

* []()ID: 3003

  Severity: INFO\
  Message: {backendName}.

* []()ID: 3004

  Severity: INFO\
  Message: {startTime}.

* []()ID: 3005

  Severity: INFO\
  Message: {emailAddress}.

* []()ID: 3006

  Severity: INFO\
  Message: {taskID}.

* []()ID: 3007

  Severity: INFO\
  Message: {action}.

* []()ID: 3008

  Severity: INFO\
  Message: {serviceName}.

* []()ID: 3009

  Severity: INFO\
  Message: {userName}.

* []()ID: 3010

  Severity: INFO\
  Message: {args}.

* []()ID: 3011

  Severity: INFO\
  Message: {databaseName}.

* []()ID: 3012

  Severity: INFO\
  Message: {maxKeyValue}.

* []()ID: 3013

  Severity: INFO\
  Message: {minKeyValue}.

* []()ID: 3014

  Severity: INFO\
  Message: {maxDataSize}.

* []()ID: 3015

  Severity: INFO\
  Message: {minDataSize}.

* []()ID: 3016

  Severity: INFO\
  Message: {clearPW}.

* []()ID: 3017

  Severity: INFO\
  Message: {encodedPW}.

* []()ID: 3018

  Severity: INFO\
  Message: {scheme}.

* []()ID: 3019

  Severity: INFO\
  Message: {branchDN}.

* []()ID: 3020

  Severity: INFO\
  Message: {attribute}.

* []()ID: 3021

  Severity: INFO\
  Message: {wrapColumn}.

* []()ID: 3022

  Severity: INFO\
  Message: {templateFile}.

* []()ID: 3023

  Severity: INFO\
  Message: {rejectFile}.

* []()ID: 3024

  Severity: INFO\
  Message: {skipFile}.

* []()ID: 3025

  Severity: INFO\
  Message: {index}.

* []()ID: 3026

  Severity: INFO\
  Message: {stopReason}.

* []()ID: 3027

  Severity: INFO\
  Message: {stopTime}.

* []()ID: 3028

  Severity: INFO\
  Message: {seconds}.

* []()ID: 3029

  Severity: INFO\
  Message: %s task %s has been successfully completed.

* []()ID: 3030

  Severity: INFO\
  Message: %s task %s did not complete successfully.

* []()ID: 3031

  Severity: INFO\
  Message: {schedulePattern}.

* []()ID: 3032

  Severity: ERROR\
  Message: An error occurred while attempting to initialize server components to run the tool: %s.

* []()ID: 3033

  Severity: ERROR\
  Message: The %s argument is not supported for online imports.

* []()ID: 3034

  Severity: INFO\
  Message: Indicates the task is recurring and will be scheduled according to the value argument expressed in crontab(5) compatible time/date pattern.

* []()ID: 3035

  Severity: INFO\
  Message: Recurring %s task %s scheduled successfully.

* []()ID: 3036

  Severity: INFO\
  Message: Exporting to %s.

* []()ID: 3037

  Severity: INFO\
  Message: yes.

* []()ID: 3038

  Severity: INFO\
  Message: y.

* []()ID: 3039

  Severity: INFO\
  Message: no.

* []()ID: 3040

  Severity: INFO\
  Message: n.

* []()ID: 3041

  Severity: ERROR\
  Message: The specified start time '%s' has already passed.

* []()ID: 3042

  Severity: ERROR\
  Message: The specified stop time '%s' has already passed.

* []()ID: 3043

  Severity: INFO\
  Message: r.

* []()ID: 3044

  Severity: INFO\
  Message: c.

* []()ID: 3045

  Severity: INFO\
  Message: l.

* []()ID: 3046

  Severity: ERROR\
  Message: The timeout of '%d' seconds has been reached. You can use the argument '--%s' to increase this timeout.

* []()ID: 3047

  Severity: INFO\
  Message: Path to temporary directory for index scratch files during LDIF import.

* []()ID: 3048

  Severity: INFO\
  Message: {directory}.

* []()ID: 3049

  Severity: INFO\
  Message: Number of threads used to read LDIF files during import. If 0, the number of threads will be set to twice the number of CPUs.

* []()ID: 3050

  Severity: INFO\
  Message: {count}.

* []()ID: 3051

  Severity: ERROR\
  Message: The value %s for threadCount cannot be parsed: %s.

* []()ID: 3052

  Severity: INFO\
  Message: The password to encode or to compare against an encoded password is interactively asked to the user.

* []()ID: 3053

  Severity: INFO\
  Message: Please enter the password :.

* []()ID: 3054

  Severity: INFO\
  Message: Please renter the password:.

* []()ID: 3055

  Severity: ERROR\
  Message: Provided passwords don't matched.

* []()ID: 3056

  Severity: ERROR\
  Message: Cannot read password from the input: %s.

* []()ID: 3057

  Severity: INFO\
  Message: Rebuild all indexes, including any DN2ID, DN2URI, VLV and extensible indexes. Cannot be used with the "-i" option or the "--rebuildUntrusted" option.

* []()ID: 3058

  Severity: INFO\
  Message: {directory}.

* []()ID: 3059

  Severity: INFO\
  Message: Path to temporary directory for index scratch files during index rebuilding.

* []()ID: 3060

  Severity: INFO\
  Message: {period}.

* []()ID: 3061

  Severity: INFO\
  Message: When this argument is specified, the status command will display its contents periodically. Used to specify the period (in seconds) between two displays of the status.

* []()ID: 3062

  Severity: ERROR\
  Message: The Windows Service was successfully configured but there was an error starting it. Error code starting Windows Service: %d.

* []()ID: 3063

  Severity: INFO\
  Message: Do not display backend data, just statistics.

* []()ID: 3064

  Severity: ERROR\
  Message: The provided schedule value has an invalid format. The schedule must be expressed using a crontab(5) format. Error details: %s.

* []()ID: 3065

  Severity: INFO\
  Message: Rebuild all untrusted indexes, including any DN2ID, DN2URI, VLV and extensible indexes. Cannot be used with the "-i" option or the "--rebuildAll" option.

* []()ID: 3067

  Severity: ERROR\
  Message: The version of the installed PingDS could not be determined because the version file '%s' could not be found. Restore it from backup before continuing.

* []()ID: 3068

  Severity: ERROR\
  Message: The version of the installed PingDS could not be determined because the version file '%s' exists but contains invalid data. Restore it from backup before continuing.

* []()ID: 3069

  Severity: ERROR\
  Message: The PingDS binary version '%s' does not match the installed configuration version '%s'. Please run upgrade before continuing.

* []()ID: 3070

  Severity: INFO\
  Message: Ignores any errors which occur during the upgrade. This option should be used with caution and may be useful in automated deployments where potential errors are known in advance and resolved after the upgrade has completed.

* []()ID: 3071

  Severity: INFO\
  Message: Forces a non-interactive upgrade to continue even if it requires user interaction. In particular, long running or critical upgrade tasks, such as re-indexing, which require user confirmation will be performed automatically. This option may only be used with the '%s' option.

* []()ID: 3072

  Severity: INFO\
  Message: Upgrades only application data. PingDS configuration must have been upgraded before.

* []()ID: 3073

  Severity: INFO\
  Message: Upgrades PingDS configuration and application data so that it is compatible with the installed binaries.%n%nThis tool should be run immediately after upgrading the PingDS binaries and before restarting the server.%n%nNOTE: this tool does not provide backup or restore capabilities. Therefore, it is the responsibility of the PingDS administrator to take necessary precautions before performing the upgrade.

* []()ID: 3074

  Severity: ERROR\
  Message: The upgrade failed to complete for the following reason: %s.

* []()ID: 3075

  Severity: INFO\
  Message: Performing upgrade.

* []()ID: 3076

  Severity: INFO\
  Message: PingDS Upgrade Utility.

* []()ID: 3077

  Severity: ERROR\
  Message: PingDS cannot be upgraded because the server is currently running. Please stop the server and try again.

* []()ID: 3078

  Severity: ERROR\
  Message: PingDS has already been upgraded to version %s.

* []()ID: 3079

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to display a notification: %s.

* []()ID: 3080

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to display a confirmation : %s.

* []()ID: 3081

  Severity: INFO\
  Message: …​Change(s) done in %s (x%s).

* []()ID: 3082

  Severity: INFO\
  Message: …​No change applied in %s.

* []()ID: 3083

  Severity: ERROR\
  Message: An error occurred while performing an upgrade task: %s.

* []()ID: 3084

  Severity: INFO\
  Message: %s.%nDo you want to make this change?.

* []()ID: 3085

  Severity: INFO\
  Message: The upgrade is ready to proceed. Do you wish to continue?.

* []()ID: 3086

  Severity: INFO\
  Message: The upgrade has been canceled.

* []()ID: 3087

  Severity: ERROR\
  Message: No %s with OID %s exists in the schema.

* []()ID: 3088

  Severity: ERROR\
  Message: An error occurred when trying to upgrade the config/upgrade folder: %s.

* []()ID: 3089

  Severity: INFO\
  Message: Preparing to upgrade.

* []()ID: 3090

  Severity: INFO\
  Message: This tool cannot be used for upgrading versions of PingDS which are older than '%s'. Please upgrade to the latest 6.5 revision first before attempting further upgrades.

* []()ID: 3092

  Severity: INFO\
  Message: Do you accept the License Agreement?.

* []()ID: 3093

  Severity: INFO\
  Message: An error occurred while copying the file '%s' to '%s'.

* []()ID: 3094

  Severity: INFO\
  Message: An error occurred while deleting directory '%s'. Check that you have the rights to delete this directory and that there is no other application using it. Error was: %s.

* []()ID: 3095

  Severity: INFO\
  Message: An error occurred while deleting file '%s': %s. Check that you have the rights to delete this file and that there is no other application using it.

* []()ID: 3096

  Severity: ERROR\
  Message: The upgrade failed because %d errors were encountered. Please check log for further details.

* []()ID: 3097

  Severity: ERROR\
  Message: An error occurred while copying the schema file '%s': %s.

* []()ID: 3098

  Severity: ERROR\
  Message: An error occurred while adding one or more attributes to the schema file '%s': %s.

* []()ID: 3099

  Severity: INFO\
  Message: See '%s' for a detailed log of this operation.

* []()ID: 3100

  Severity: INFO\
  Message: Replacing schema file '%s'.

* []()ID: 3101

  Severity: INFO\
  Message: Archiving concatenated schema.

* []()ID: 3102

  Severity: INFO\
  Message: Adding '%s' configuration file.

* []()ID: 3103

  Severity: ERROR\
  Message: An error occurred while adding configuration file '%s': %s.

* []()ID: 3104

  Severity: INFO\
  Message: Rebuilding index(es) %s for base dn(s): %s.

* []()ID: 3105

  Severity: INFO\
  Message: Rebuild index task ends.

* []()ID: 3106

  Severity: INFO\
  Message: Performing post upgrade tasks.

* []()ID: 3107

  Severity: INFO\
  Message: Post upgrade tasks complete.

* []()ID: 3108

  Severity: ERROR\
  Message: An error occurred during post upgrade task. Process aborted. Please check log for further details.

* []()ID: 3110

  Severity: INFO\
  Message: You have to rebuild all indexes manually to get a fully functional server.

* []()ID: 3111

  Severity: ERROR\
  Message: Invalid log file %s.

* []()ID: 3112

  Severity: INFO\
  Message: The rebuild index tool arguments are %s.

* []()ID: 3113

  Severity: INFO\
  Message: Rebuilding all indexes.

* []()ID: 3114

  Severity: INFO\
  Message: End of the upgrade process.

* []()ID: 3115

  Severity: ERROR\
  Message: '%s' is missing or empty, it is probably corrupted.

* []()ID: 3116

  Severity: INFO\
  Message: No indexes to rebuild for backend '%s'.

* []()ID: 3117

  Severity: INFO\
  Message: The classes folder has been renamed to '%s' to avoid compatibility issues.

* []()ID: 3119

  Severity: INFO\
  Message: List the low-level databases within a pluggable backend's storage engine. This subcommand may take a long time to complete depending on the size of the backend.

* []()ID: 3120

  Severity: INFO\
  Message: List the indexes associated with a pluggable backend. This subcommand may take a long time to complete depending on the size of the backend.

* []()ID: 3121

  Severity: INFO\
  Message: Dump records from an index, decoding keys and values. Depending on index size, this subcommand can generate lots of output.

* []()ID: 3122

  Severity: INFO\
  Message: Dump the raw records in hexadecimal format for a low-level database within the pluggable backend's storage engine. Depending on index size, this subcommand can generate lots of output.

* []()ID: 3123

  Severity: INFO\
  Message: Raw DB Name.

* []()ID: 3124

  Severity: ERROR\
  Message: An error occurred while listing the base DNs: %s.

* []()ID: 3125

  Severity: ERROR\
  Message: An error occurred while listing indexes: %s.

* []()ID: 3126

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to initialize the backend '%s': %s.

* []()ID: 3127

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to read and/or decode records from index %s: %s.

* []()ID: 3128

  Severity: ERROR\
  Message: No index exists with the requested name '%s' in base DN '%s' and backend '%s'.

* []()ID: 3129

  Severity: ERROR\
  Message: Cannot specify a minimum key both as a string and as an hexadecimal string.

* []()ID: 3130

  Severity: ERROR\
  Message: Cannot specify a maximum key both as a string and as an hexadecimal string.

* []()ID: 3131

  Severity: ERROR\
  Message: An error occurred while processing arguments: %s.

* []()ID: 3132

  Severity: ERROR\
  Message: An error occurred while trying to execute %s: %s.

* []()ID: 3133

  Severity: INFO\
  Message: Total Keys.

* []()ID: 3134

  Severity: INFO\
  Message: Keys Size.

* []()ID: 3135

  Severity: INFO\
  Message: Values Size.

* []()ID: 3136

  Severity: INFO\
  Message: Total Size.

* []()ID: 3137

  Severity: INFO\
  Message: Uses SI Units for printing sizes.

* []()ID: 3138

  Severity: INFO\
  Message: Write hexadecimal data on a single line instead of pretty format.

* []()ID: 3139

  Severity: INFO\
  Message: %nTotal: %d%n.

* []()ID: 3140

  Severity: INFO\
  Message: %nIndex: %s%n.

* []()ID: 3141

  Severity: INFO\
  Message: Over index-entry-limit keys: %s%n.

* []()ID: 3142

  Severity: INFO\
  Message: %nTotal Records: %d%n.

* []()ID: 3143

  Severity: INFO\
  Message: Total / Average Key Size: %d bytes / %d bytes%n.

* []()ID: 3144

  Severity: INFO\
  Message: Total / Average Data Size: %d bytes / %d bytes%n.

* []()ID: 3145

  Severity: ERROR\
  Message: At key number %d, %s:.

* []()ID: 3146

  Severity: INFO\
  Message: Key (len %d):.

* []()ID: 3147

  Severity: INFO\
  Message: Value (len %d):.

* []()ID: 3148

  Severity: ERROR\
  Message: Data decoder for printing is not available, should use hex dump.

* []()ID: 3149

  Severity: ERROR\
  Message: No storage index exists with the requested name %s in backend %s.

* []()ID: 3150

  Severity: INFO\
  Message: This utility can be used to debug a backend.

* []()ID: 3151

  Severity: INFO\
  Message: {indexName}.

* []()ID: 3153

  Severity: ERROR\
  Message: An error occurred while initializing server backends: %s.

* []()ID: 3154

  Severity: ERROR\
  Message: An error occurred while initializing plugins: %s.

* []()ID: 3155

  Severity: ERROR\
  Message: Subsystem %s should be initialized first.

* []()ID: 3156

  Severity: INFO\
  Message: PingDS configuration will be upgraded from version %s to %s.

* []()ID: 3157

  Severity: INFO\
  Message: PingDS data can't be upgraded because the configuration has not been upgraded yet. Upgrade the configuration first before upgrading the data.

* []()ID: 3158

  Severity: INFO\
  Message: PingDS data will be upgraded from version %s to %s.

* []()ID: 3159

  Severity: INFO\
  Message: PingDS data will be upgraded to version %s.

* []()ID: 3160

  Severity: INFO\
  Message: PingDS data was successfully upgraded to version %s.

* []()ID: 3161

  Severity: ERROR\
  Message: PingDS data has already been upgraded to version %s.

* []()ID: 3162

  Severity: INFO\
  Message: PingDS configuration was successfully upgraded to version %s.

* []()ID: 3163

  Severity: ERROR\
  Message: The PingDS binary version '%s' does not match the installed data version '%s'. Please run 'upgrade --dataOnly' before continuing.

* []()ID: 3164

  Severity: INFO\
  Message: Upgrade failed to delete the obsolete file '%s'. Reason: %s.

* []()ID: 3165

  Severity: INFO\
  Message: This utility can be used to debug changelog and changenumber files.

* []()ID: 3166

  Severity: INFO\
  Message: Dump the change number DB.

* []()ID: 3167

  Severity: INFO\
  Message: Dump the replica DB for a given domain and replica.

* []()ID: 3168

  Severity: INFO\
  Message: Dump a replica DB file.

* []()ID: 3169

  Severity: INFO\
  Message: The output directory for the dump files.

* []()ID: 3170

  Severity: INFO\
  Message: The lower bound of the range of change numbers to dump.

* []()ID: 3171

  Severity: INFO\
  Message: The upper bound of the range of change numbers to dump.

* []()ID: 3172

  Severity: INFO\
  Message: The lower bound of the range of changes to dump.

* []()ID: 3173

  Severity: INFO\
  Message: The upper bound of the range of changes to dump.

* []()ID: 3174

  Severity: INFO\
  Message: {directory}.

* []()ID: 3175

  Severity: INFO\
  Message: {change number}.

* []()ID: 3176

  Severity: INFO\
  Message: {csn}.

* []()ID: 3177

  Severity: INFO\
  Message: The base-dn of the changes contained in the provided replica DB file.

* []()ID: 3178

  Severity: INFO\
  Message: {base dn}.

* []()ID: 3179

  Severity: ERROR\
  Message: An error occurred when reading the replication server configuration entry '%s': %s.

* []()ID: 3180

  Severity: ERROR\
  Message: The replication domain '%s' is not found. Make sure the domain is replicated.

* []()ID: 3181

  Severity: ERROR\
  Message: Replica DB folder '%s' not found.

* []()ID: 3182

  Severity: ERROR\
  Message: The provided change number '%s' is not valid.

* []()ID: 3183

  Severity: ERROR\
  Message: The provided CSN '%s' is not valid.

* []()ID: 3184

  Severity: ERROR\
  Message: The output folder '%s' cannot be created.

* []()ID: 3185

  Severity: ERROR\
  Message: The provided output folder '%s' doesn't exist.

* []()ID: 3186

  Severity: ERROR\
  Message: The provided DN '%s' is invalid.

* []()ID: 3187

  Severity: ERROR\
  Message: Cannot list the changelog files in '%s': %s.

* []()ID: 3188

  Severity: ERROR\
  Message: Cannot convert the filename '%s' to a valid change number.

* []()ID: 3189

  Severity: ERROR\
  Message: Cannot convert the filename '%s' to a valid CSN.

* []()ID: 3190

  Severity: ERROR\
  Message: Error while decoding the changelog file '%s' : %s.

* []()ID: 3191

  Severity: INFO\
  Message: Arguments for changelogstat: %s.

* []()ID: 3192

  Severity: ERROR\
  Message: The PingDS binary version '%s' is older than the configuration version '%s', it usually means that an older version has been unzipped over the previous binaries. Unzip a more recent version than the configuration version and run upgrade again.

* []()ID: 3193

  Severity: ERROR\
  Message: The PingDS binary version '%s' is older than the data version '%s', it usually means that an older version has been unzipped over the previous binaries. Unzip a more recent version than the data version and run upgrade again.

* []()ID: 3194

  Severity: INFO\
  Message: PingDS will be upgraded from version %s to %s.

* []()ID: 3195

  Severity: INFO\
  Message: PingDS was successfully upgraded to version %s.

* []()ID: 3196

  Severity: INFO\
  Message: The upgrade will not be performed because the configuration file config.ldif could not be parsed.

* []()ID: 3197

  Severity: INFO\
  Message: Removing file '%s'.

* []()ID: 3198

  Severity: ERROR\
  Message: Unable to access the LDIF file %s to import. Please check that the file is local to the server and the path correct.

* []()ID: 3199

  Severity: INFO\
  Message: Removing configuration entries for the monitor providers.

* []()ID: 3200

  Severity: INFO\
  Message: Setting global server ID.

* []()ID: 3201

  Severity: INFO\
  Message: Setting new global server ID.

* []()ID: 3202

  Severity: ERROR\
  Message: Could not find a server ID to set for the server. Verify the configuration references a valid server ID for domain cn=admin data.

* []()ID: 3203

  Severity: INFO\
  Message: Setting global group ID and removing per domain values.

* []()ID: 3204

  Severity: WARNING\
  Message: Unable to find configuration for truststore backend "%s", using default values instead.

* []()ID: 3205

  Severity: WARNING\
  Message: Unable to find configuration for crypto manager "%s", replication SSL configuration will use default values.

* []()ID: 3206

  Severity: INFO\
  Message: Update replication SSL configuration from crypto manager and trust store backend to dedicated key and trust manager provider configuration elements.

* []()ID: 3207

  Severity: INFO\
  Message: Update replication SSL configuration.

* []()ID: 3208

  Severity: INFO\
  Message: Move SSL protocols and cipher suites configuration from crypto manager into each configuration element where they are used.

* []()ID: 3209

  Severity: INFO\
  Message: Removing global server ID from replication domains and replication server.

* []()ID: 3210

  Severity: INFO\
  Message: Adding Mail Servers.

* []()ID: 3211

  Severity: INFO\
  Message: Consolidating bootstrap replication servers from replication server and replication domains into Multimaster Synchronization provider.

* []()ID: 3212

  Severity: INFO\
  Message: Migrating truststore backend configuration to crypto manager.

* []()ID: 3213

  Severity: INFO\
  Message: Migrating truststore backend configuration.

* []()ID: 3214

  Severity: INFO\
  Message: Migrating security settings.

* []()ID: 3215

  Severity: ERROR\
  Message: Crypto manager configuration entry not found.

* []()ID: 3216

  Severity: NOTICE\
  Message: script to manage PingDS as a service on UNIX.

* []()ID: 3217

  Severity: NOTICE\
  Message: encode a password with a storage scheme.

* []()ID: 3218

  Severity: NOTICE\
  Message: export directory data in LDIF.

* []()ID: 3219

  Severity: NOTICE\
  Message: import directory data from LDIF.

* []()ID: 3220

  Severity: NOTICE\
  Message: manage server administration tasks.

* []()ID: 3221

  Severity: NOTICE\
  Message: rebuild index after configuration change.

* []()ID: 3222

  Severity: NOTICE\
  Message: start PingDS server.

* []()ID: 3223

  Severity: NOTICE\
  Message: display basic PingDS server information.

* []()ID: 3224

  Severity: NOTICE\
  Message: stop PingDS server.

* []()ID: 3225

  Severity: NOTICE\
  Message: upgrade PingDS configuration and application data.

* []()ID: 3226

  Severity: NOTICE\
  Message: check index for consistency or errors.

* []()ID: 3227

  Severity: NOTICE\
  Message: register PingDS server as a Windows Service.

* []()ID: 3228

  Severity: NOTICE\
  Message: gather PingDS backend debugging information.

* []()ID: 3229

  Severity: NOTICE\
  Message: debug changelog and changenumber files.

* []()ID: 3230

  Severity: NOTICE\
  Message: \<xinclude:include href="description-upgrade.xml" />.

* []()ID: 3231

  Severity: ERROR\
  Message: The server has not been configured. Please run the 'setup' command first.

* []()ID: 3232

  Severity: NOTICE\
  Message: \<xinclude:include href="variablelist-backendstat-index-status.xml" />.

* []()ID: 3233

  Severity: ERROR\
  Message: Rebuild index aborted: an error has occurred while rebuilding indexes for base DN '%s'.

* []()ID: 3234

  Severity: NOTICE\
  Message: \<xinclude:include href="description-recurring-task-info.xml" />.

* []()ID: 3235

  Severity: ERROR\
  Message: An error occurred while reading configuration file: %s.

* []()ID: 3236

  Severity: ERROR\
  Message: An error occurred while copying data from '%s' to the server instance configuration directory. Error details: %s.

* []()ID: 3238

  Severity: INFO\
  Message: Reconfiguring PDB backends to JE backends.

* []()ID: 3239

  Severity: INFO\
  Message: Renaming PDB backend directory '%s' to '%s'.

* []()ID: 3240

  Severity: INFO\
  Message: You must reimport all your data into the JE backends in order to have a fully functional server.

* []()ID: 3241

  Severity: INFO\
  Message: Replacing low durability settings in JE backends.

* []()ID: 3242

  Severity: INFO\
  Message: Replacing high durability settings in JE backends.

* []()ID: 3243

  Severity: INFO\
  Message: Replacing medium durability settings in JE backends.

* []()ID: 3244

  Severity: INFO\
  Message: Renaming 'ds-cfg-json-schema' object class to 'ds-cfg-json-query-equality-matching-rule'.

* []()ID: 3245

  Severity: ERROR\
  Message: An error occurred while copying OpenDMK jar file '%s' to '%s': %s.

* []()ID: 3246

  Severity: INFO\
  Message: Migrating root DN '%s'.

* []()ID: 3247

  Severity: INFO\
  Message: Removing root DN users from configuration.

* []()ID: 3248

  Severity: ERROR\
  Message: Root DNs could not be migrated because the '%s' directory could not be created: %s.

* []()ID: 3249

  Severity: INFO\
  Message: PingDS 6.0.0 drops support for Root DNs and replaces them with standard user entries which are stored in LDIF backends. The root DN '%s' does not have an alias name so it must be renamed to '%s' so that it no longer resides inside the configuration. Do you want to proceed with the upgrade?.

* []()ID: 3250

  Severity: INFO\
  Message: PingDS 6.0.0 drops support for Root DNs and replaces them with standard user entries which are stored in LDIF backends. The root DN '%s' has multiple alias names, but only the alias name '%s' will be kept. Do you want to proceed with the upgrade?.

* []()ID: 3251

  Severity: INFO\
  Message: The upgrade will not be performed because some Root DNs need to be migrated.

* []()ID: 3252

  Severity: INFO\
  Message: Segregating mutable and immutable files.

* []()ID: 3253

  Severity: ERROR\
  Message: The directory '%s' could not be created: %s.

* []()ID: 3254

  Severity: ERROR\
  Message: The file '%s' could not be renamed to '%s': %s.

* []()ID: 3255

  Severity: INFO\
  Message: Update admin-backend.ldif file location.

* []()ID: 3256

  Severity: INFO\
  Message: Update tasks backend file location.

* []()ID: 3257

  Severity: INFO\
  Message: Replacing all pin related configuration attributes by a single pin configuration attribute.

* []()ID: 3258

  Severity: INFO\
  Message: The attribute has been removed because it was referring to a file that does not exist. You should replace it with the attribute %s before being able to enable the object corresponding to the configuration entry.

* []()ID: 3259

  Severity: INFO\
  Message: Removing send and receive window size configuration in replication.

* []()ID: 3260

  Severity: ERROR\
  Message: tool exit with error return code '%d'.

* []()ID: 3261

  Severity: INFO\
  Message: Migrating replication changelog files to 6.5.0 format.

* []()ID: 3262

  Severity: ERROR\
  Message: An error occurred reading the changelog files: %s.

* []()ID: 3263

  Severity: ERROR\
  Message: An error occurred while renaming the changelog files: %s.

* []()ID: 3264

  Severity: ERROR\
  Message: An error occurred while migrating replicas' offline states to the changelog files: %s.

* []()ID: 3265

  Severity: INFO\
  Message: Adding configuration entry '%s'.

* []()ID: 3266

  Severity: ERROR\
  Message: An error occurred while trying to modify %s : %s.

* []()ID: 3267

  Severity: INFO\
  Message: Replacing compute change number setting in replication server.

* []()ID: 3268

  Severity: INFO\
  Message: PingDS 6.5.0 changed the indexing algorithm for replication metadata. Its index must be rebuilt which may take a long time; without a working index every server start will take longer than normal. Do you want to rebuild the index automatically at the end of the upgrade?.

* []()ID: 3269

  Severity: INFO\
  Message: Replacing "reject unauthenticated requests" policy in global configuration.

* []()ID: 3270

  Severity: INFO\
  Message: Removing configuration for assured replication.

* []()ID: 3271

  Severity: INFO\
  Message: Removing generation-id data from configuration.

* []()ID: 3272

  Severity: INFO\
  Message: Removing synchronization state data from configuration.

* []()ID: 3273

  Severity: INFO\
  Message: Renaming the proxy backend configuration property 'service discovery mechanism' to 'shard'.

* []()ID: 3274

  Severity: INFO\
  Message: Adding objectClass to JSON, CSV, and External access logger configurations.

* []()ID: 3275

  Severity: ERROR\
  Message: Server is running. Please stop the server before running this tool.

* []()ID: 3276

  Severity: INFO\
  Message: Removing configuration for replication monitoring.

* []()ID: 3277

  Severity: ERROR\
  Message: An error occurred when trying to read the configuration version in %s : %s.

* []()ID: 3279

  Severity: INFO\
  Message: Set the proxy backend configuration property 'hash-function' to MD5.

* []()ID: 3280

  Severity: INFO\
  Message: Use the old JE backend caches instead of the new shared cache.

* []()ID: 3281

  Severity: INFO\
  Message: Renaming ds-cfg-connection-pool-\* attributes to ds-cfg-bind-connection-pool-\*.

* []()ID: 3282

  Severity: INFO\
  Message: Set the database cache mode 'ds-cfg-db-cache-mode' to 'cache-ln'.

* []()ID: 3283

  Severity: INFO\
  Message: Add 'inheritFromDNParent' attribute type to the 'inheritedCollectiveAttributeSubentry' object class.

* []()ID: 3284

  Severity: NOTICE\
  Message: Could not find 'ads-certificate' entry in the truststore '%s'. This entry is required for the correct behavior of the directory server.

* []()ID: 3285

  Severity: WARNING\
  Message: Unable to retrieve the keys from the truststore.

* []()ID: 3286

  Severity: WARNING\
  Message: Unable to look up server key id '%s' in the admin backend.

* []()ID: 3287

  Severity: WARNING\
  Message: Unable to retrieve the hostname from the admin backend using the truststore as source of keys; 'advertised-listen-address' attribute in global configuration will use the local hostname as value. Cause: %s.

* []()ID: 3288

  Severity: NOTICE\
  Message: Unable to retrieve the local hostname, the 'advertised-listen-address' attribute in global configuration must be set manually.

* []()ID: 3289

  Severity: INFO\
  Message: Adding 'listen-address' and 'advertised-listen-address' attributes to the global configuration.

* []()ID: 3290

  Severity: INFO\
  Message: Removing 'listen-address' attributes that are redundant with default value provided by the global configuration.

* []()ID: 3291

  Severity: NOTICE\
  Message: An error occurred while removing some 'listen-address' attribute values from the configuration.

* []()ID: 3292

  Severity: INFO\
  Message: PingDS 7.0.0 changed the indexing algorithm for TelephoneNumber equality and substring matching rules. All TelephoneNumber syntax based attribute indexes must be rebuilt which may take a long time. Do you want to rebuild the indexes automatically at the end of the upgrade?.

* []()ID: 3293

  Severity: INFO\
  Message: Add ACI to make Root DSE fullVendorVersion operational attribute user visible.

* []()ID: 3294

  Severity: INFO\
  Message: Removing references to 'backup' backend.

* []()ID: 3295

  Severity: INFO\
  Message: Removing 'backup' backend.

* []()ID: 3296

  Severity: INFO\
  Message: Remove External change log domain configuration entries and migrate information to the domains and the replication server configuration entries.

* []()ID: 3297

  Severity: INFO\
  Message: Migrate source address attribute from replication server configuration to replication synchronization provider configuration.

* []()ID: 3298

  Severity: INFO\
  Message: Migrate common replication domain configuration attributes to replication synchronization provider configuration.

* []()ID: 3299

  Severity: NOTICE\
  Message: Configuration attribute %s has distinct values in replication domain configuration entries. Migration to replication synchronization provider configuration will keep only one value, '%s' and discarded '%s'.

* []()ID: 3300

  Severity: INFO\
  Message: Removing '%s' attribute(s) from backup tasks.

* []()ID: 3301

  Severity: ERROR\
  Message: '%s' attributes couldn't be removed from backup tasks.

* []()ID: 3302

  Severity: INFO\
  Message: Removing restore tasks.

* []()ID: 3303

  Severity: ERROR\
  Message: The restore tasks couldn't be removed.

* []()ID: 3304

  Severity: INFO\
  Message: DS 7.0.0 breaks restore tasks compatibility, all existing restore tasks will be removed.

* []()ID: 3305

  Severity: INFO\
  Message: Migrate isolation policy attribute to replication synchronization provider configuration.

* []()ID: 3306

  Severity: INFO\
  Message: Merge replication-purge-delay and conflicts-historical-purge-delay attribute into a single replication-purge-delay attribute in replication synchronizer provider configuration.

* []()ID: 3307

  Severity: ERROR\
  Message: An error occured when trying to read the configuration file %s: %s.

* []()ID: 3308

  Severity: WARNING\
  Message: Unable to find the task backend file location in the configuration file %s, entry '%s' or attribute '%s' is missing.

* []()ID: 3309

  Severity: INFO\
  Message: Removing profiler plugins.

* []()ID: 3310

  Severity: INFO\
  Message: Removing max-work-queue-capacity.

* []()ID: 3311

  Severity: INFO\
  Message: Migrating encrypted replication changelog files.

* []()ID: 3312

  Severity: ERROR\
  Message: An error occurred while migrating encrypted changelog files: %s.

* []()ID: 3313

  Severity: INFO\
  Message: Rename attribute 'ds-backup-directory-path' to 'ds-backup-location' in entries of objectClass '%s'.

* []()ID: 3314

  Severity: ERROR\
  Message: Attribute 'ds-backup-directory-path' could not be renamed to 'ds-backup-location' in entries of objectclass '%s'.

* []()ID: 3315

  Severity: INFO\
  Message: Renaming the 'use-mutual-tls' configuration property to 'use-sasl-external'.

* []()ID: 3316

  Severity: INFO\
  Message: Renaming the 'replication-server' configuration property to 'bootstrap-replication-server'.

* []()ID: 3317

  Severity: INFO\
  Message: The path to the systemd service file to create.

* []()ID: 3318

  Severity: ERROR\
  Message: An error occurred while attempting to generate the systemd service file: %s.

* []()ID: 3319

  Severity: INFO\
  Message: Gives an ID to the task.

* []()ID: 3320

  Severity: INFO\
  Message: {description}.

* []()ID: 3321

  Severity: INFO\
  Message: Gives a description to the task.

* []()ID: 3322

  Severity: INFO\
  Message: Description.

* []()ID: 3323

  Severity: INFO\
  Message: Allowing dsbackup purge tasks.

* []()ID: 3324

  Severity: INFO\
  Message: Removing empty configuration for groups.

* []()ID: 3325

  Severity: INFO\
  Message: Replacing non allowed comma in groupID definition with a dot.

* []()ID: 3326

  Severity: INFO\
  Message: Removing 'ds-cfg-load-balancing-algorithm' attribute from the proxy backend.

* []()ID: 3327

  Severity: INFO\
  Message: Renaming 'ds-cfg-bind-connection-pool-**' attributes to 'ds-cfg-connection-pool-**'.

* []()ID: 3328

  Severity: INFO\
  Message: Removing 'ds-cfg-request-connection-pool-size' attribute,'ds-cfg-connection-pool-size' will be used instead.

* []()ID: 3329

  Severity: INFO\
  Message: Add 'ldapSyntaxes' to attribute list which can be read in the schema access global access control policies.

* []()ID: 3330

  Severity: INFO\
  Message: Renaming replication changelog files from .log to .cdb suffix.

* []()ID: 3331

  Severity: ERROR\
  Message: Invalid sequence for task version: task %s tried to register for version %s but the previous task used a higher version: %s. This suggests there is a copy/paste error in the version number.

* []()ID: 3332

  Severity: INFO\
  Message: Renaming proxy 'ds-cfg-heartbeat-**' attributes to 'ds-cfg-keep-alive-**\`.

* []()ID: 3333

  Severity: ERROR\
  Message: "Error parsing existing schema file '%s' - %s".

* []()ID: 3334

  Severity: INFO\
  Message: PingDS 7.2.0 fixed an indexing bug that may cause searches to return duplicate entries in certain circumstances. All indexes have to be rebuilt. This could take a long time to proceed. Do you want to launch this process automatically at the end of the upgrade?.

* []()ID: 3335

  Severity: INFO\
  Message: Removing look through limit from the configuration.

* []()ID: 3336

  Severity: INFO\
  Message: Renaming 'ds-cfg-cursor-entry-limit' to 'ds-cfg-max-candidate-set-size'.

* []()ID: 3337

  Severity: INFO\
  Message: Removing VLV indexes with base-object scope from the configuration.

* []()ID: 3338

  Severity: INFO\
  Message: Migrating JE environment properties to configuration attributes.

* []()ID: 3339

  Severity: INFO\
  Message: Removing replica degraded status threshold configuration.

* []()ID: 3340

  Severity: INFO\
  Message: Remove LDIF change record remnants from the configuration.

* []()ID: 3341

  Severity: INFO\
  Message: Changes in Unicode string normalization require that all indexes are rebuilt. Do you want to rebuild the indexes automatically at the end of the upgrade?.

* []()ID: 3342

  Severity: INFO\
  Message: Removing LDAP send reject notification configuration.

* []()ID: 3343

  Severity: INFO\
  Message: Removing debug logging configuration.

* []()ID: 3344

  Severity: INFO\
  Message: Replace multiple severity values by a single one in logging configurations.

* []()ID: 3345

  Severity: INFO\
  Message: Changing syntax for 'inheritAttribute' attribute type to IA5String.

* []()ID: 3346

  Severity: INFO\
  Message: OPENDJ-9550 on 7.3.0 caused static groups to lose their operational attributes on modify operations, corrupting data and the entryUUID index which needs to be rebuilt. Do you want to rebuild the indexes automatically at the end of the upgrade?.

* []()ID: 3347

  Severity: INFO\
  Message: The name of the group account under which the server should run.

* []()ID: 3348

  Severity: INFO\
  Message: {groupName}.

* []()ID: 3349

  Severity: ERROR\
  Message: You must provide either the --%s or the --%s argument.

* []()ID: 3350

  Severity: INFO\
  Message: Make the File-Based Error Loggers perform asynchronous logging for optimal performance after merging the debug and error logger.

* []()ID: 3351

  Severity: INFO\
  Message: Enabling change numbers in the replication changelog.

* []()ID: 3352

  Severity: INFO\
  Message: Removing 'ds-cfg-argon2-migration-memory' and adding 'ds-cfg-argon2-memory-pool-size' which specifies the size of the memory pool allocated for concurrent Argon2 password hashing computations.

* []()ID: 3353

  Severity: INFO\
  Message: Adding 'ds-cfg-exclude-values-of-attributes' with the list the attribute names which values will be excluded from the list of requested modifications.

* []()ID: 3354

  Severity: INFO\
  Message: Continue to allow invalid certificate lists, certificate pairs and postal addresses.

* []()ID: 3355

  Severity: INFO\
  Message: Renaming 'ds-cfg-big-index-matching-rule' attribute to 'ds-cfg-big-index-extensible-matching-rule\`.

* []()ID: 3358

  Severity: ERROR\
  Message: Unable to parse line %d ("%s") from the LDIF source because the line started with a space but there were no previous lines in the entry to which this line could be appended.

* []()ID: 3359

  Severity: ERROR\
  Message: Unable to parse LDIF entry starting at line %d because the line "%s" does not include an attribute name.

* []()ID: 3360

  Severity: ERROR\
  Message: Unable to parse LDIF entry starting at line %d because the first line does not contain a DN (the first line was "%s".

* []()ID: 3361

  Severity: ERROR\
  Message: Unable to parse LDIF entry starting at line %d because an error occurred while trying to parse the value of line "%s" as a distinguished name: %s.

* []()ID: 3362

  Severity: ERROR\
  Message: Unable to parse LDIF entry starting at line %d because it was not possible to base64-decode the DN on line "%s": %s.

* []()ID: 3363

  Severity: ERROR\
  Message: Unable to parse LDIF entry %s starting at line %d because it was not possible to base64-decode the attribute on line "%s": %s.

* []()ID: 3364

  Severity: WARNING\
  Message: Entry %s read from LDIF starting at line %d includes a duplicate attribute %s with value %s. The second occurrence of that attribute value has been skipped.

* []()ID: 3365

  Severity: ERROR\
  Message: Entry %s starting at line %d includes multiple values for single-valued attribute %s.

* []()ID: 3366

  Severity: ERROR\
  Message: Entry %s read from LDIF starting at line %d is not valid because it violates the server's schema configuration: %s.

* []()ID: 3367

  Severity: ERROR\
  Message: The specified LDIF file %s already exists and the export configuration indicates that no attempt should be made to append to or replace the file.

* []()ID: 3368

  Severity: ERROR\
  Message: Unable to parse LDIF entry %s starting at line %d because the value of attribute %s was to be read from a URL but the URL was invalid: %s.

* []()ID: 3369

  Severity: ERROR\
  Message: Unable to parse LDIF entry %s starting at line %d because the value of attribute %s was to be read from URL %s but an error occurred while trying to read that content: %s.

* []()ID: 3370

  Severity: ERROR\
  Message: The specified reject file %s already exists and the import configuration indicates that no attempt should be made to append to or replace the file.

* []()ID: 3371

  Severity: ERROR\
  Message: An error occurred while attempting to determine whether LDIF entry "%s" starting at line %d should be imported as a result of the include and exclude filter configuration: %s.

* []()ID: 3372

  Severity: ERROR\
  Message: The provided sender address %s is invalid: %s.

* []()ID: 3373

  Severity: ERROR\
  Message: The provided recipient address %s is invalid: %s.

* []()ID: 3374

  Severity: ERROR\
  Message: The specified e-mail message could not be sent using any of the configured mail servers.

* []()ID: 3375

  Severity: ERROR\
  Message: The provided string "%s" cannot be decoded as an LDAP URL because it does not contain the necessary :// component to separate the scheme from the rest of the URL.

* []()ID: 3376

  Severity: ERROR\
  Message: The provided string "%s" cannot be decoded as an LDAP URL because it does not contain a protocol scheme.

* []()ID: 3377

  Severity: ERROR\
  Message: The provided string "%s" cannot be decoded as an LDAP URL because it does not contain a host before the colon to specify the port number.

* []()ID: 3378

  Severity: ERROR\
  Message: The provided string "%s" cannot be decoded as an LDAP URL because it does not contain a port number after the colon following the host.

* []()ID: 3379

  Severity: ERROR\
  Message: The provided string "%s" cannot be decoded as an LDAP URL because the port number portion %s cannot be decoded as an integer.

* []()ID: 3380

  Severity: ERROR\
  Message: The provided string "%s" cannot be decoded as an LDAP URL because the provided port number %d is not within the valid range between 1 and 65535.

* []()ID: 3381

  Severity: ERROR\
  Message: The provided string "%s" cannot be decoded as an LDAP URL because the scope string %s was not one of the allowed values of base, one, sub, or subordinate.

* []()ID: 3382

  Severity: ERROR\
  Message: The provided URL component "%s" could not be decoded because the percent character at byte %d was not followed by two hexadecimal digits.

* []()ID: 3383

  Severity: ERROR\
  Message: The provided URL component "%s" could not be decoded because the character at byte %d was not a valid hexadecimal digit.

* []()ID: 3384

  Severity: ERROR\
  Message: Cannot decode value "%s" as a named character set because it does not contain a colon to separate the name from the set of characters.

* []()ID: 3385

  Severity: ERROR\
  Message: The named character set is invalid because it does not contain a name.

* []()ID: 3386

  Severity: ERROR\
  Message: The named character set is invalid because the provide name "%s" has an invalid character at position %d. Only ASCII alphabetic characters are allowed in the name.

* []()ID: 3387

  Severity: ERROR\
  Message: Cannot decode value "%s" as a named character set because it does not contain a name to use for the character set.

* []()ID: 3388

  Severity: ERROR\
  Message: Cannot decode value "%s" as a named character set because there are no characters to include in the set.

* []()ID: 3389

  Severity: INFO\
  Message: %d seconds.

* []()ID: 3390

  Severity: INFO\
  Message: %d minutes, %d seconds.

* []()ID: 3391

  Severity: INFO\
  Message: %d hours, %d minutes, %d seconds.

* []()ID: 3392

  Severity: INFO\
  Message: %d days, %d hours, %d minutes, %d seconds.

* []()ID: 3393

  Severity: ERROR\
  Message: Unable to set permissions for file %s because it does not exist.

* []()ID: 3394

  Severity: ERROR\
  Message: One or more exceptions were thrown in the process of updating the file permissions for %s. Some of the permissions for the file may have been altered.

* []()ID: 3395

  Severity: ERROR\
  Message: The provided string %s does not represent a valid UNIX file mode. UNIX file modes must be a three-character string in which each character is a numeric digit between zero and seven.

* []()ID: 3396

  Severity: WARNING\
  Message: Entry %s read from LDIF starting at line %d includes value "%s" for attribute %s that is invalid according to the associated syntax: %s.

* []()ID: 3397

  Severity: ERROR\
  Message: The specified skip file %s already exists and the import configuration indicates that no attempt should be made to append to or replace the file.

* []()ID: 3398

  Severity: ERROR\
  Message: Skipping entry %s because the DN is not one that should be included based on the include and exclude branches/filters.

* []()ID: 3399

  Severity: ERROR\
  Message: The embedded server with server root '%s' cannot be started because it is already running.

* []()ID: 3400

  Severity: ERROR\
  Message: Skipping entry %s because the DN is excluded by the exclude branch "%s".

* []()ID: 3401

  Severity: ERROR\
  Message: Skipping entry %s because the DN is excluded by the exclude filter "%s".

* []()ID: 3402

  Severity: ERROR\
  Message: Skipping entry %s because the DN is not included by any include branches.

* []()ID: 3403

  Severity: ERROR\
  Message: Skipping entry %s because the DN is not included by any include filters.

* []()ID: 3404

  Severity: ERROR\
  Message: Rejecting entry %s because it was rejected by a plugin.

* []()ID: 3405

  Severity: ERROR\
  Message: Rejecting entry %s because it was rejected by a plugin: %s.

* []()ID: 3406

  Severity: ERROR\
  Message: Unable to parse LDIF entry %s starting at line %d because it has an invalid binary option for attribute %s.

* []()ID: 3407

  Severity: ERROR\
  Message: Skipping entry %s because the following error was received when reading its attributes: %s.

* []()ID: 3408

  Severity: ERROR\
  Message: An error occurred while attempting to obtain a list of the files in directory %s to include in the backup: %s.

* []()ID: 3409

  Severity: ERROR\
  Message: An error occurred while attempting to extract server archive '%s' before setup of embedded server with install path '%s': %s.

* []()ID: 3410

  Severity: ERROR\
  Message: An error occurred while attempting to rebuild index of embedded server with instance path '%s': %s.

* []()ID: 3411

  Severity: ERROR\
  Message: An error occurred while attempting to start the embedded server with instance path '%s' : %s.

* []()ID: 3412

  Severity: ERROR\
  Message: An error occurred while attempting to upgrade the embedded server with instance path '%s' : %s.

* []()ID: 3414

  Severity: ERROR\
  Message: The setup from an archive can only be done with a install path directory named after the root directory contained in the archive: '%s'. The provided install path was: '%s'.

* []()ID: 3415

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the configuration framework or to read the configuration file '%s'.

* []()ID: 3416

  Severity: ERROR\
  Message: An error occurred while attempting to import LDIF file '%s' into embedded server with instance path '%s'. Import LDIF task state was '%s'. You can look at the task logs printed on the embedded server output stream for more details.

* []()ID: 3417

  Severity: ERROR\
  Message: An error occurred while attempting to import LDIF file '%s' into embedded server with instance path '%s': '%s'.

* []()ID: 3418

  Severity: ERROR\
  Message: An error occurred while attempting to rebuild index of embedded server with instance path '%s'. Rebuild task state was '%s'. You can look at the task logs printed on the embedded server output stream for more details.

* []()ID: 3421

  Severity: ERROR\
  Message: An error occurred while initializing configuration of embedded server with instance path '%s': %s.

* []()ID: 3422

  Severity: ERROR\
  Message: The directory to move %s does not exist.

* []()ID: 3423

  Severity: ERROR\
  Message: The directory to move %s exists but is a file.

* []()ID: 3424

  Severity: ERROR\
  Message: The target directory %s already exists.

* []()ID: 3425

  Severity: ERROR\
  Message: Configuration error: an LDAP port or an LDAPS port must be configured before finishing configuring the embedded server.

* []()ID: 3426

  Severity: WARNING\
  Message: Embedded Directory Servers are NOT SUPPORTED in production.

* []()ID: 3427

  Severity: ERROR\
  Message: The Directory server DS(%s) and Replication server RS(%s) are working on different dataset regarding the domain '%s' : the Directory server DS(%s) will reject all modification operations and must be re-initialized.

* []()ID: 3428

  Severity: ERROR\
  Message: You do not have sufficient privileges to perform the sort request.

* []()ID: 3430

  Severity: INFO\
  Message: Renaming 'ds-cfg-log-control-oids' attribute to 'ds-cfg-log-controls'.

* []()ID: 3431

  Severity: INFO\
  Message: Removing SNMP support.

* []()ID: 3432

  Severity: INFO\
  Message: Performs disaster recovery on the local server. The subcommand has two forms.

The first form verifies each replica has the same data after recovery: on a replica, run dsrepl disaster-recovery --baseDn dc=example,dc=com --generate-recovery-id

The command prints the identifier to use on all other servers with the --generated-id option: dsrepl disaster-recovery --baseDn dc=example,dc=com --generated-id {identifier}

The second form uses an identifier you provide. It lets you automate the recovery process when you cannot use the first form. Do not use this form if the topology has standalone replication servers. With this form of the subcommand, you must ensure you recover each replica with the same data. Run the same subcommand on all servers. Example: dsrepl disaster-recovery --baseDn dc=example,dc=com --user-generated-id Recovery\_Date\_20240101

Read the documentation on disaster recovery carefully before using this command. []()ID: 3433:: Severity: INFO\
Message: Generate a disaster recovery identifier during recovery. Use this for the first directory server in a replication topology with standalone RS servers. For all subsequent servers to recover, omit this option and use --generated-id {generatedRecoveryId} with the generated identifier. []()ID: 3434:: Severity: INFO\
Message: Use the disaster recovery identifier generated on the first server. You must use the same identifier for all servers involved in the same disaster recovery procedure. []()ID: 3435:: Severity: NOTICE\
Message: A mandatory argument is missing. Choose one and only one argument from '--generate-recovery-id', '--generated-id' and '--user-generated-id'. []()ID: 3436:: Severity: INFO\
Message: {generatedRecoveryId}. []()ID: 3437:: Severity: ERROR\
Message: Disaster recovery must be started on a directory server or a combined directory/replication server. []()ID: 3438:: Severity: ERROR\
Message: An error occurred while computing the disaster recovery id for base DN '%s': %s. []()ID: 3439:: Severity: INFO\
Message: Disaster recovery for base DN '%s' ended successfully on this server. []()ID: 3440:: Severity: INFO\
Message: The disaster recovery process completed successfully for the first server. The next step is to restore the same data using the same procedure on all the remaining servers in the topology and run the following command on each server:. []()ID: 3441:: Severity: ERROR\
Message: The disaster recovery procedure cannot be continued on this server because the domain '%s' does not contain the expected data. Make sure the server has been restored using exactly the same procedure used on the first server. []()ID: 3442:: Severity: ERROR\
Message: An error occurred while rewriting the base entry of the domain '%s'. This server will not be able to connect to the servers which already have received the disaster recovery procedure. Make sure the filesystem is writeable and there is some free disk space, and try again. The error is: %s. []()ID: 3443:: Severity: ERROR\
Message: An error occurred while clearing the changelog for the domain '%s'. This server will not be able to connect to the servers which have already completed the disaster recovery procedure. Make sure the filesystem at '%s' is readable with delete permissions and try again. The error is: %s. []()ID: 3444:: Severity: ERROR\
Message: An error occurred while rewriting replication data for the domain '%s'. This server will not be able to connect to the servers which already have received the disaster recovery procedure. Make sure the filesystem at '%s' is writeable and there is some free disk space and try again. The error is: %s. []()ID: 3445:: Severity: ERROR\
Message: An error occurred while clearing the change number index. The change number index on this server will expose erroneous data. Make sure the filesystem at '%s' is readable with delete permissions and try again. The error is: %s. []()ID: 3446:: Severity: ERROR\
Message: The server is neither a replica nor a replication server for base DN '%s'. []()ID: 3447:: Severity: ERROR\
Message: Disaster recovery for base DN '%s' failed on this server. []()ID: 3448:: Severity: WARNING\
Message: The local replication server never received changes for base DN '%s'. Make sure you are running the disaster recovery on the right server. []()ID: 3449:: Severity: INFO\
Message: Base DN of the domain to be recovered. []()ID: 3450:: Severity: ERROR\
Message: The disaster recovery id '%s' is invalid. Verify the value of the disaster recovery id parameter matches the value printed when '--generate-recovery-id' was run on the first server. []()ID: 3451:: Severity: ERROR\
Message: The provided base DN '%s' does not match the disaster recovery id '%s'. Please verify that the base DN and disaster recovery id correspond to the base DN and id from the first recovered server. []()ID: 3452:: Severity: INFO\
Message: Starting disaster recovery on local server for base DN '%s'. []()ID: 3453:: Severity: ERROR\
Message: The replication changelog file '%s' could not be deleted. Check file permissions and filesystem status. The error is: %s. []()ID: 3454:: Severity: ERROR\
Message: The replication changelog files could not be retrieved. Check file permissions and filesystem status. The error is: %s. []()ID: 3455:: Severity: INFO\
Message: Disaster recovery will erase replication metadata on this server. This server will then only be able to replicate changes with other recovered servers. You will have to run the recovery procedure on every other server of the topology. Servers which have not been recovered will not be able to connect to recovered servers anymore. []()ID: 3456:: Severity: INFO\
Message: Continue the disaster recovery procedure. []()ID: 3457:: Severity: INFO\
Message: dsrepl disaster-recovery --baseDn '%s' --generated-id %s. []()ID: 3458:: Severity: INFO\
Message: Disaster recovery id: %s. []()ID: 3459:: Severity: INFO\
Message: The disaster recovery process has been canceled, no operation was performed. This server may still not be operational. []()ID: 3460:: Severity: INFO\
Message: Decodes one or more CSNs and displays them in a human readable JSON format. []()ID: 3461:: Severity: INFO\
Message: csn \[csn …​]. []()ID: 3462:: Severity: ERROR\
Message: The CSN cannot be parsed as a valid CSN. []()ID: 3463:: Severity: NOTICE\
Message: The current 7.4.0 server is configured to use an incompatible confidentiality setting which prevents automated upgrade from working. Follow the procedure detailed in the Upgrade Guide to upgrade this server. []()ID: 3464:: Severity: WARNING\
Message: Peer replica '%s' is too late compared to changelog '%s' for domain '%s'. It asked for changes that are not present in the changelog or have been purged. The peer replica will no longer receive replicated changes and must be re-initialized. Diagnostic information follows: %s. []()ID: 3465:: Severity: WARNING\
Message: Peer replica asked for changes from replica '%1$s' starting from %2$s (CSN '%3$s'), but changelog DB only contains changes starting from %4$s (CSN '%5$s'). The last recorded purge information in 'domains.state' is: last update CSN: %6$s, last message CSN: %7$s. The replica DB description is: number of files: %8$d, replica offline: %9$b. The replica DB newest file content is: oldest CSN: %10$s, newest CSN: %11$s, number of updates: %12$d, number of ReplicaOfflineMsg: %13$d. []()ID: 3466:: Severity: WARNING\
Message: Peer replica asked for changes from replica '%s' starting from %s (CSN '%s'), but the changelog DB has purged this change, and the last known generated change timestamp is %s (CSN '%s'). The last recorded purge information in 'domains.state' is: last update CSN: %s, last message CSN: %s. []()ID: 3468:: Severity: ERROR\
Message: The provided disaster recovery id had version %d, but only version 1 is supported. Verify the value of the disaster recovery id parameter matches the value printed when '--generate-recovery-id' was run on the first server. []()ID: 3469:: Severity: WARNING\
Message: Replication domain '%s' status '%s' is not healthy. []()ID: 3470:: Severity: INFO\
Message: Updating existing Prometheus endpoints to keep using the legacy format. []()ID: 3471:: Severity: WARNING\
Message: Property '%s' in %s '%s' is DEPRECATED for removal since %s. Its usage is highly discouraged. []()ID: 3472:: Severity: WARNING\
Message: Property '%s' in %s '%s' is LEGACY since %s. Its usage is highly discouraged. []()ID: 3473:: Severity: ERROR\
Message: There is no data in domain '%s' to run disaster recovery on. []()ID: 3474:: Severity: INFO\
Message: Set the identifier for this recovery to {userGeneratedRecoveryId}, a string of your choice. Do not use this option if the replication topology has standalone RS servers. You must use the same identifier for all servers involved in the same disaster recovery procedure. []()ID: 3475:: Severity: INFO\
Message: {userGeneratedRecoveryId}. []()ID: 3476:: Severity: ERROR\
Message: Base Dn '%s' is not a replicated domain on this server. Disaster recovery must be run on a directory server or a combined directory/replication server. []()ID: 3477:: Severity: INFO\
Message: Disaster recovery for domain '%s' has already been run with recovery ID '%s'. Verify all servers in the topology are being recovered with the same recovery ID. []()ID: 3478:: Severity: WARNING\
Message: An error occurred while decoding a replicated request control: %s. []()ID: 3479:: Severity: WARNING\
Message: An error occurred while decoding a internal modification control: %s. []()ID: 3480:: Severity: INFO\
Message: Add a new HDAP authorization mechanism '%s'. []()ID: 3481:: Severity: INFO\
Message: Replace the authentication mechanism of the '/hdap' endpoint '%s' with the new HDAP authorization mechanism '%s'. []()ID: 3482:: Severity: INFO\
Message: Removing deprecated HTTP Basic DN and JWT authorization mechanisms. The HDAP authorization mechanism '%s' replaces them. []()ID: 3483:: Severity: ERROR\
Message: The entry '%s' specified in the request does not exist in the Directory Server. []()ID: 3484:: Severity: ERROR\
Message: The requested search operation included the persistent search control together with either the simple paged results control or the virtual list view control. These controls are mutually exclusive and cannot be used together. []()ID: 3486:: Severity: NOTICE\
Message: Cannot continue the restore process, errors were encountered while reading the list of available backups: %s. []()ID: 3487:: Severity: NOTICE\
Message: Cannot continue purging backups, errors were encountered while reading the list of available backups: %s. []()ID: 3488:: Severity: ERROR\
Message: This server received a replication message to signal a disaster recovery. This means that this server is part of a mixed topology where the deprecated start-disaster-recovery command is used. The operation will continue, but it is not supported anymore and the disaster recovery procedure for mixed topologies must be used instead. []()ID: 3489:: Severity: INFO\
Message: Hostname. []()ID: 3490:: Severity: ERROR\
Message: This tool exited as a safety measure because the server is running low on disk space. This is possibly because this tool might be preventing the server to clean-up obsolete data. Free some disk space or stop the server before trying to run this tool again. []()ID: 3491:: Severity: ERROR\
Message: An attempt was made to register the '%s' plugin to be invoked as a plugin for %s ; but such plugin type(s) are not allowed for this plugin. []()ID: 3492:: Severity: ERROR\
Message: Before executing request '%s', an OpenTelemetry context is already present in thread-local storage while it should not. This indicates a context leak: some code is not properly closing the OpenTelemetry Scope. Check the code and make sure to use a try-with-resources where the scope is used. Leaked context is: '%s'. []()ID: 3493:: Severity: ERROR\
Message: Worker thread '%s': after executing request '%s', an OpenTelemetry context is still present in thread-local storage while it should not. This indicates a context leak: some code is not properly closing the OpenTelemetry Scope. Check the code and make sure to use a try-with-resources where the scope is used. Leaked context is: '%s'. []()ID: 3494:: Severity: ERROR\
Message: An OpenTelemetry plugin is already configured, cannot configure a second one. []()ID: 3495:: Severity: INFO\
Message: Update object classes for PBKDF2 and BCrypt storage schemes. []()ID: 3496:: Severity: INFO\
Message: Removing rarely used JE backend tuning settings. []()ID: 3497:: Severity: ERROR\
Message: Some servers for domain '%s' have different generation IDs from others in the topology (Status: %s), and therefore cannot replicate with the other servers. If the status is due to a disaster recovery in progress, ignore the present status and run this command again after the procedure is complete to confirm the final status. []()ID: 3498:: Severity: INFO\
Message: Generation ID. []()ID: 3499:: Severity: INFO\
Message: RS servers using this generation ID. []()ID: 3500:: Severity: INFO\
Message: %s.

## IDs: 3501-4000

* []()ID: 3501

  Severity: ERROR\
  Message: If no disaster recovery is in progress, first check the contents of a replica with each generation ID to determine which generation ID corresponds to the correct data for your deployment. Next, reinitialize the data whose generation ID does not reflect the correct data. Finally, run the dsrepl status command again. If any remaining RS servers still have the wrong generation ID, stop them, run the dsrepl clear-changelog to remove their changelog data, and start them again to let replication reset their generation IDs to the correct value.

* []()ID: 3502

  Severity: INFO\
  Message: Bcrypt and PBKDF2 password storage schemes using a rehash policy of 'always' have been changed to use 'only-increase'.

* []()ID: 3503

  Severity: ERROR\
  Message: The backend '%s' data format is incompatible with the version of this server, which may be due to an attempt to restore a backup from a more recent version of the server. Please upgrade this server to a newer version. The backend data has format version '%s' whereas this server supports format version '%s".

* []()ID: 3504

  Severity: ERROR\
  Message: Invalid backend data format '%s'.

* []()ID: 3505

  Severity: ERROR\
  Message: Before running request '%s', Thread %s already has an OpenTelemetry context, but none should have been there. It is the indication of a context leak: some code is not properly closing the OpenTelemetry Scope.

* []()ID: 3506

  Severity: INFO\
  Message: Removing virtual threads feature flag.

* []()ID: 3507

  Severity: INFO\
  Message: Removing JMX connection handlers.

* []()ID: 3508

  Severity: ERROR\
  Message: An error occurred while trying to initialize the synchronization provider '%s': %s.

* []()ID: 3509

  Severity: ERROR\
  Message: Write timeout exceeded for persistent search.

* []()ID: 3510

  Severity: ERROR\
  Message: You do not have sufficient privileges to create or delete temporary base DNs.

* []()ID: 3511

  Severity: ERROR\
  Message: The maximum number of temporary base DNs has been reached.

* []()ID: 3512

  Severity: ERROR\
  Message: The temporary base DN partition DN '%s' is not valid as it is not a subordinate of this backend's base DNs'.

* []()ID: 3513

  Severity: INFO\
  Message: Failback to the primary servers for proxy backend '%s' for requests proxying.

* []()ID: 3514

  Severity: INFO\
  Message: Failover to the secondary servers for proxy backend '%s'. They will be used for processing requests until the primary servers become available again.

* []()ID: 3515

  Severity: ERROR\
  Message: Skipping entry %s because the DN is a temporary base DN or a subordinate of a temporary base DN.

* []()ID: 3516

  Severity: ERROR\
  Message: A record from replica '%s' in the replication changelog of domain '%s' cannot be decoded because its format (%x) is invalid.

* []()ID: 3518

  Severity: INFO\
  Message: Removing off-heap memory configuration.

* []()ID: 3519

  Severity: INFO\
  Message: Preserving lack of attribute name normalization in HDAP.

* []()ID: 3521

  Severity: ERROR\
  Message: The trust store pin must be specified for the configuration entry %s.

* []()ID: 3522

  Severity: NOTICE\
  Message: The changelog in path '%s' specifies new crypto parameters which are incompatible with already configured parameters. Check the replication server configuration.

* []()ID: 3523

  Severity: NOTICE\
  Message: Fetching batch %.1f%% completed.

* []()ID: 3524

  Severity: NOTICE\
  Message: Setting state of index(es) %s to untrusted.

* []()ID: 3526

  Severity: INFO\
  Message: Setting state of all indexes to untrusted.

* []()ID: 3527

  Severity: INFO\
  Message: Setting state of index(es) %s to untrusted for base dn(s): %s.

* []()ID: 3528

  Severity: ERROR\
  Message: Setting state of index(es) to untrusted must be done with the backend containing the base DN disabled.

* []()ID: 3529

  Severity: ERROR\
  Message: Invalid double value: %s.

* []()ID: 3530

  Severity: ERROR\
  Message: max-export-batch-size %d must be smaller or equal to max-queue-size %d.

* []()ID: 3531

  Severity: INFO\
  Message: Removing deprecated REST to LDAP, admin and metrics endpoints.

* []()ID: 3532

  Severity: INFO\
  Message: Removing deprecated loggers and support files.

* []()ID: 3533

  Severity: INFO\
  Message: Enabling entry compression in JE backends.

* []()ID: 3534

  Severity: NOTICE\
  Message: Index %s is implicitly trusted because base DN %s is empty.

* []()ID: 3535

  Severity: NOTICE\
  Message: Index %s is implicitly trusted because base DN %s does not contain any entries using the indexed attribute(s).

* []()ID: 3536

  Severity: NOTICE\
  Message: This search operation has exceeded the lookthrough limit %d.

* []()ID: 3537

  Severity: WARNING\
  Message: The directory server has accepted %d persistent search requests, exceeding the configured limit of %d.

* []()ID: 3538

  Severity: ERROR\
  Message: The %s backend is unavailable due to an internal error: %s. The server must be restarted and, depending on the cause, the backend may need to be restored from backup.

* []()ID: 3539

  Severity: ERROR\
  Message: There is an internal error in backend %s that prevents to perform the operation.

* []()ID: 3540

  Severity: INFO\
  Message: Removing support for OpenAPI descriptors.

* []()ID: 3541

  Severity: ERROR\
  Message: An error occurred while trying to open the database in read-only mode, probably because of a lack of memory. Increase Java heap memory for this tool and try again.

* []()ID: 3542

  Severity: ERROR\
  Message: Error while persisting data state for domain %s: %s.

* []()ID: 3543

  Severity: ERROR\
  Message: Error while loading data state for domain %s: %s.

* []()ID: 3544

  Severity: ERROR\
  Message: Replica '%s' is TOO\_OLD for domain %s: the local changelog or the topology combined changelog does not contain changes which are required by the replica. The replica must be re-initialized.

* []()ID: 3545

  Severity: INFO\
  Message: Renaming 'HdapEndpoint' Java class name.

* []()ID: 3546

  Severity: ERROR\
  Message: HTTP connection %s has been closed because the HTTP connection handler %s is shutting down.

* []()ID: 3547

  Severity: INFO\
  Message: Collecting JFR files.

* []()ID: 3548

  Severity: ERROR\
  Message: Could not collect JFR data from the directory server: %s.

* []()ID: 3549

  Severity: INFO\
  Message: Generating JFR dump for pid %d.

* []()ID: 3550

  Severity: INFO\
  Message: Path to the JFR log directory.

* []()ID: 3551

  Severity: INFO\
  Message: No value was provided for %s, JFR directory is set to %s.

* []()ID: 3552

  Severity: INFO\
  Message: {jfr\_directory}.

* []()ID: 3553

  Severity: ERROR\
  Message: Unsupported search scope: %s.

* []()ID: 3554

  Severity: ERROR\
  Message: A new Scrypt password storage scheme can only be added by running dsconfig in offline mode.

* []()ID: 3555

  Severity: ERROR\
  Message: The value of the 'n' parameter for the Scrypt password storage scheme must be between 1 and 30.

* []()ID: 3556

  Severity: ERROR\
  Message: The value of the 'n' and 'r' parameters for the Scrypt password storage scheme must be such that 128 \* r \* n < 2^30.

* []()ID: 3557

  Severity: ERROR\
  Message: The value of the 'r' parameter for the Scrypt password storage scheme is too large.

* []()ID: 3558

  Severity: ERROR\
  Message: The Scrypt password storage scheme could not be configured because it requires %s kB of memory, exceeding the maximum available of %s kB. Configure a bigger heap or reduce the Scrypt memory requirements.

* []()ID: 3559

  Severity: INFO\
  Message: Set backwards compatible algorithm version for BCRYPT password schemes.

* []()ID: 3560

  Severity: WARNING\
  Message: Changelog file '%s' has missing data between keys '%s' and '%s'. When the two keys are CSNs, this indicates a hole in the changelog. The server may have missed changes and may need to be re-initialized. Verify the changelog in the originating server.

* []()ID: 3561

  Severity: INFO\
  Message: Removing deprecated OAuth2 authorization mechanisms.

* []()ID: 3562

  Severity: INFO\
  Message: Rename Get Connection ID Extended Operation class.

* []()ID: 3563

  Severity: INFO\
  Message: Rename Start TLS Extended Operation class.

* []()ID: 3564

  Severity: ERROR\
  Message: An error occurred while initializing extended operations: %s.

* []()ID: 3565

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to decode the registration to core extended request sequence: %s.

* []()ID: 3566

  Severity: ERROR\
  Message: An unexpected error occurred while attempting to decode the registration to core extended request sequence: value is null.

* []()ID: 3567

  Severity: INFO\
  Message: Rename LDIF Backend class.

* []()ID: 3568

  Severity: INFO\
  Message: Rename LDIF Connection Handler class.

* []()ID: 3569

  Severity: INFO\
  Message: Rename Fractional LDIF Import Plugin class.

* []()ID: 3570

  Severity: ERROR\
  Message: An error occurred while trying to initialize RegistrationToCore extended operation handler: %s.

* []()ID: 3572

  Severity: INFO\
  Message: Adding new objectClass to UNIFIED connection handlers.

* []()ID: 3573

  Severity: INFO\
  Message: Rename LDAP Connection Handler.

* []()ID: 3574

  Severity: INFO\
  Message: Rename HTTP Connection Handler.

* []()ID: 3575

  Severity: ERROR\
  Message: %s connection %s has been closed because the connection handler %s is shutting down.

* []()ID: 3576

  Severity: NOTICE\
  Message: Skipping verification for base DN '%s' because the suffix is empty.

* []()ID: 3577

  Severity: ERROR\
  Message: The network protocol could not be determined because the first network message contained an unrecognized byte 0x%02X.

* []()ID: 3578

  Severity: ERROR\
  Message: The server is too busy to service the operation.

* []()ID: 3579

  Severity: ERROR\
  Message: Either a backendId or a base DN must be specified to run this command.

* []()ID: 3580

  Severity: ERROR\
  Message: Backend '%s' is not configured in any of the backends of this server.

* []()ID: 3581

  Severity: ERROR\
  Message: The raw database name '%s' is not specific enough, either use a full raw database name, from the 'list-raw-dbs' subcommand, or specify a base DN.

* []()ID: 3584

  Severity: ERROR\
  Message: The paged results control value has an unexpected format. Expected cookie format: %s.

* []()ID: 3585

  Severity: ERROR\
  Message: The paged results control value starts cursoring outside the expected search base DN subtree, which is not allowed.

* []()ID: 3586

  Severity: ERROR\
  Message: The signing key with alias '%s' does not exist in the '%s' key manager. Please check that the correct key manager has been configured and that it contains the specified signing key.

* []()ID: 3587

  Severity: ERROR\
  Message: The CryptoManager could not find the signing key with alias '%s' to compute a signature in the '%s' key manager. Please check that the correct key manager has been configured and that it contains the specified signing keys.

* []()ID: 3588

  Severity: ERROR\
  Message: An error occurred while attempting to initialize the SSL context for use in leader based replication LDAP traffic.

* []()ID: 3589

  Severity: ERROR\
  Message: The certificate with alias '%s' could not be found in the keystore.

* []()ID: 3590

  Severity: ERROR\
  Message: The certificate with alias '%s' is not an X.509 certificate. Its type is '%s'.

* []()ID: 3591

  Severity: ERROR\
  Message: The replication user DN cannot be empty.

* []()ID: 3592

  Severity: ERROR\
  Message: The replication user DN '%s' is invalid. %s.

* []()ID: 3593

  Severity: ERROR\
  Message: An error occurred while attempting to write the replication user entry: %s.

* []()ID: 3594

  Severity: ERROR\
  Message: An error occurred while attempting to configure the backend for the replication user: %s.

* []()ID: 3595

  Severity: INFO\
  Message: DN for the replication service account.

* []()ID: 3596

  Severity: INFO\
  Message: {replicationUserDN}.

* []()ID: 3597

  Severity: INFO\
  Message: The replication service account certificate alias to use for replication LDAP traffic.

* []()ID: 3598

  Severity: INFO\
  Message: {replicationUserCertificateAlias}.

* []()ID: 3599

  Severity: INFO\
  Message: Migrate the replication changelog configuration.

* []()ID: 3600

  Severity: ERROR\
  Message: An error occurred while fetching entries from remote peer(s): result code is %s, message is %s.

* []()ID: 3601

  Severity: ERROR\
  Message: An error occurred in replica changelog: %s.

* []()ID: 3602

  Severity: ERROR\
  Message: An error occurred while appending an user request to the changelog: %s.

* []()ID: 3603

  Severity: ERROR\
  Message: An error occurred while appending a remote change to the changelog: %s.

* []()ID: 3604

  Severity: INFO\
  Message: Use an existing certificate in another type of keystore.

* []()ID: 3605

  Severity: INFO\
  Message: Keystore type (one of PKCS11, PKCS12, JCEKS, JKS, or freeform for custom keystores like BCFKS, BKS, …​):.

* []()ID: 3606

  Severity: INFO\
  Message: Keystore path:.

* []()ID: 3607

  Severity: INFO\
  Message: Use an existing %s keystore.

* []()ID: 3608

  Severity: ERROR\
  Message: Invalid input: keystore type cannot be empty.

* []()ID: 3609

  Severity: INFO\
  Message: Do you want to specify the Java security provider for the store file?.

* []()ID: 3610

  Severity: INFO\
  Message: Store security provider:.

* []()ID: 3611

  Severity: INFO\
  Message: Provider name (leave empty if none):.

* []()ID: 3612

  Severity: INFO\
  Message: Provider class (leave empty if none):.

* []()ID: 3613

  Severity: INFO\
  Message: Provider argument (leave empty if none):.

* []()ID: 3614

  Severity: ERROR\
  Message: You may not provide both the provider name and the provider class arguments.

* []()ID: 3615

  Severity: INFO\
  Message: Use another type of truststore.

* []()ID: 3616

  Severity: INFO\
  Message: Use an existing %s truststore.

* []()ID: 3617

  Severity: INFO\
  Message: Truststore type (one of JVM, PKCS11, PKCS12, JCEKS, JKS, BLIND\_TRUST (evaluation only), or freeform for custom truststores like BCFKS, BKS, …​):.

* []()ID: 3618

  Severity: INFO\
  Message: Truststore path:.

* []()ID: 3619

  Severity: ERROR\
  Message: The server failed to find the signing key pair with ID '%s' in its key store. Make sure that the server has access to the signing key pair that was used when the signature was created.

* []()ID: 3620

  Severity: ERROR\
  Message: An error occurred while creating the PKCS11 based trust manager provider: %s.

* []()ID: 3621

  Severity: ERROR\
  Message: Could not access the %s truststore. Check that the provided arguments correspond to a valid truststore, that you have access rights to it and that a valid password has been provided if needed. Error details: %s.

* []()ID: 3622

  Severity: WARNING\
  Message: The cloud storage plugin is deprecated and will be removed in a future release.Find alternative ways to use cloud storage for backup in the product documentation.

* []()ID: 3626

  Severity: ERROR\
  Message: You must specify the truststore password of the file based truststore. You can use either --%s or --%s options to specify it.

* []()ID: 3627

  Severity: ERROR\
  Message: The file based truststore password cannot be empty.

* []()ID: 3628

  Severity: ERROR\
  Message: The deployment ID options are incompatible with the use of PKCS11.

* []()ID: 3629

  Severity: ERROR\
  Message: The deployment ID is missing, provide it with the --%s option.

* []()ID: 3630

  Severity: INFO\
  Message: Warning: the use of a PKCS11 keystore is incompatible with the use of a deployment ID. If you confirm the use of a PKCS11 keystore, the deployment ID will be ignored and you must ensure the PKCS11 keystore holds a master-key. For further information, refer to the documentation. Do you want to continue using a PKCS11 keystore?.

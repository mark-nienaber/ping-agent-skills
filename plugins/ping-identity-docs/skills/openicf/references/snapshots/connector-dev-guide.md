---
title: About ICF and ICF connectors
description: Overview of the Identity Connector Framework (ICF), its capabilities, and how to build, use, and deploy ICF connectors with PingIDM
component: openicf
page_id: openicf:connector-dev-guide:about-icf
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/about-icf.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  openicf-functionality: Overview of ICF functionality
---

# About ICF and ICF connectors

The OpenICF (ICF) provides interoperability between identity, compliance, and risk management solutions. An ICF connector enables provisioning software, such as PingIDM, to manage the identities that are maintained by a specific identity provider.

ICF connectors provide a consistent layer between identity applications and target resources, and expose a set of operations for the complete lifecycle of an identity. The connectors provide a way to decouple applications from the target resources to which data is provisioned.

ICF focuses on provisioning and identity management, but also provides general purpose capabilities, including authentication, create, read, update, delete, search, scripting, and synchronization operations. Connector bundles rely on the ICF Framework, but applications remain completely separate from the connector bundles. This lets you change and update connectors without changing your application or its dependencies.

Many connectors have been built within the ICF framework, and are maintained and supported by Ping and by the ICF community. However, you can also develop your own ICF connector, to address a requirement that is not covered by one of the existing connectors. In addition, ICF provides two *scripted connector toolkits*, that let you write your own connectors based on Groovy or PowerShell scripts.

The ICF framework can use IDM, Sun Identity Manager, and Oracle Waveset connectors (version 1.1), and can use ConnID connectors up to version 1.4.

This guide provides the following information:

* An overview of the ICF framework and its components

* Information on how to use the ICF existing connectors in your application (both locally and remotely)

* Information on how to write your own Java and .NET connectors, scripted Groovy connectors, or scripted PowerShell connectors

## Overview of ICF functionality

ICF provides many capabilities, including the following:

* Connector pooling

* Timeouts on all operations

* Search filtering

* Search and synchronization buffering and result streaming

* Scripting with Groovy, JavaScript, shell, and PowerShell

* Classloader isolation

* An independent logging API/SPI

* Java and .NET platform support

* Opt-in operations that support both simple and advanced implementations for the same CRUD operation

* A logging proxy that captures all API calls

* A Maven connector archetype to create connectors

---

---
title: API configuration object
description: "Describes the ICF API configuration object and its components: object pool, results handler, configuration properties, and timeout settings"
component: openicf
page_id: openicf:connector-dev-guide:api-config-object
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/api-config-object.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# API configuration object

The API configuration object holds the runtime configuration of the connector facade instance. The ICF framework creates a default API configuration object inside the Connector Info object. The application creates a copy of the API configuration object and customizes it according to its requirements. The API configuration object includes the following components:

* Object Pool Configuration

  The object pool configuration specifies the pool configuration for poolable connectors only. Non-poolable connectors ignore this parameter. The object pool configuration includes the following parameters:

  * maxObjects

    The maximum number of idle and active instances of the connector.

  * maxIdle

    The maximum number of idle instances of the connector.

  * maxWait

    The maximum time, in milliseconds, that the pool waits for an object before timing out. A value of `0` means that there is no timeout.

  * minEvictableIdleTimeMillis

    The maximum time, in milliseconds, that an object can be idle before it's removed. A value of `0` means there is no idle timeout.

  * minIdle

    The minimum number of idle instances of the connector.

* Results Handler Configuration

  The results handler configuration defines how the ICF framework chains together the different results handlers to filter search results.

  * enableNormalizingResultsHandler

    boolean

    If the connector implements the attribute normalizer interface, you can enable this interface by setting this configuration property to `true`. If the connector does not implement the attribute normalizer interface, the value of this property has no effect.

  * enableFilteredResultsHandler

    boolean

    If the connector uses the filtering and search capabilities of the remote connected system, you can set this property to `false`. If the connector does not use the remote system's filtering and search capabilities (for example, the CSV file connector), you *must* set this property to `true`, otherwise the connector performs an additional, case-sensitive search, which can cause problems.

  * enableCaseInsensitiveFilter

    boolean

    By default, the filtered results handler (described previously) is case sensitive. If the filtered results handler is enabled this property lets you enable case-insensitive filtering. When case-insensitive filtering is not enabled, a search will not return results unless the case matches exactly. For example, a search for `lastName = "Jensen"` will not match a stored user with `lastName : jensen`.

  * enableAttributesToGetSearchResultsHandler

    boolean

    By default, IDM determines which attributes that should be retrieved in a search. If the `enableAttributesToGetSearchResultsHandler` property is set to `true`, the ICF framework removes all attributes from the READ/QUERY response, except for those that are specifically requested. For performance reasons, it is recommended that you set this property to `false` for local connectors, and to `true` for remote connectors.

* Configuration Properties

  The Configuration Properties object is built and populated by the framework as it parses the connectors configuration class.

* Timeout Configuration

  The timeout configuration enables you to configure timeout values per operation type. By default, there is no timeout configured for any operation type.

---

---
title: Authenticate operation
description: How to use and implement the ICF authenticate operation in a connector, including exception handling and unit testing
component: openicf
page_id: openicf:connector-dev-guide:operations/operation-authenticate
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/operations/operation-authenticate.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  AuthenticationApiOp-api-level-rules: Use the ICF authenticate operation
  AuthenticateOp-spi-level-rules: Implement the authenticate operation
---

# Authenticate operation

The authenticate operation authenticates an object on the target system, based on two parameters, usually a unique identifier (username) and a password. If possible, your connector should try to authenticate these credentials natively.

If authentication fails, the connector should throw a runtime exception. The exception must be an `IllegalArgumentException` or, if a native exception is available and is of type `RuntimeException`, that native runtime exception. If the native exception is not a `RuntimeException`, it should be wrapped in a `RuntimeException`, and then thrown.

The exception should provide as much detail as possible for logging problems and failed authentication attempts. Several exceptions are provided in the `exceptions` package, for this purpose. For example, one of the most common authentication exceptions is the `InvalidPasswordException`.

For more information about the common exceptions provided in the OpenICF framework, refer to [Common exceptions](../common-exceptions.html).

## Use the ICF authenticate operation

This section shows how your application can use the framework's `authentication` operation, and how to write a unit test for this operation, when you are developing your connector.

The `authentication` operation throws a `RuntimeException` if the credentials do not pass authentication, otherwise returns the `UID`.

Sample Unit Test for the Authentication Operation (Java)

```java
@Test
public void authenticateTest() {
    logger.info("Running Authentication Test");
    final ConnectorFacade facade = createConnectorFacade(BasicConnector.class, null);
    final OperationOptionsBuilder builder = new OperationOptionsBuilder();
    Uid uid =
        facade.authenticate(ObjectClass.ACCOUNT, "username", new GuardedString("Passw0rd"
        .toCharArray()), builder.build());
    Assert.assertEquals(uid.getUidValue(), "username");
}
```

## Implement the authenticate operation

To implement the `authenticate` operation in your connector, add the `AuthenticateOp` interface to your connector class, for example:

```java
@ConnectorClass(
    displayNameKey = "Sample.connector.display",
    configurationClass = SampleConfiguration.class)
public class SampleConnector implements Connector, AuthenticateOp...
```

For more information, refer to the [AuthenticateOp JavaDoc](../../_attachments/apidocs/org/identityconnectors/framework/spi/operations/AuthenticateOp.html).

The SPI provides the following detailed exceptions:

* UnknownUidException - the UID does not exist on the resource.

  `(org.identityconnectors.framework.common.exceptions.UnknownUidException)`

* ConnectorSecurityException - base exception for all security-related exceptions.

  `(org.identityconnectors.framework.common.exceptions.ConnectorSecurityException)`

* InvalidCredentialException - generic invalid credential exception that should be used if the specific error cannot be obtained.

  `(org.identityconnectors.framework.common.exceptions.UnknownUidException)`

* InvalidPasswordException - the password provided is incorrect.

  `(org.identityconnectors.framework.common.exceptions.InvalidPasswordException)`

* PasswordExpiredException - the password is correct, but has expired.

  `(org.identityconnectors.framework.common.exceptions.PasswordExpiredException)`

* PermissionDeniedException - the user can be identified but does not have permission to authenticate.

  `(org.identityconnectors.framework.common.exceptions.PermissionDeniedException)`

Implementation of the Authentication Operation, at the SPI Level

```java
public Uid authenticate(final ObjectClass objectClass, final String userName,
        final GuardedString password, final OperationOptions options) {
    if (ObjectClass.ACCOUNT.equals(objectClass)) {
        return new Uid(userName);
    } else {
        logger.warn("Authenticate of type {0} is not supported", configuration
                .getConnectorMessages().format(objectClass.getDisplayNameKey(),
                        objectClass.getObjectClassValue()));
        throw new UnsupportedOperationException("Authenticate of type"
                + objectClass.getObjectClassValue() + " is not supported");
    }
}
```

---

---
title: Authenticate script
description: How to implement the authenticate script for ICF connectors to enable pass-through authentication, including required input variables and return values
component: openicf
page_id: openicf:connector-dev-guide:scripts/script-authenticate
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/scripts/script-authenticate.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Authenticate script

An authenticate script is *required* if you want to use pass-through authentication to the backend resource. If your connector does not need to authenticate to the resource, the authenticate script should allow the `authId` to pass through by default.

A sample authenticate script for an SQL database is provided in `openidm/samples/scripted-sql-with-mysql/tools/AuthenticateScript.groovy`.

The following connectors support pass-through authentication using the [`AuthenticateOp` interface](../operations/operation-authenticate.html) by default:

* [LDAP connector](../../connector-reference/ldap.html)

* [CSV file connector](../../connector-reference/csv.html)

* [Database Table connector](../../connector-reference/dbtable.html)

* [Microsoft Graph API connector](../../connector-reference/ms-graph-api.html)

* [Scripted SQL connector](../../connector-reference/scripted-sql.html)

|   |                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All [Scripted Groovy](../../connector-reference/groovy.html)-based connectors are capable of pass-through authentication if the `AuthenticateScript.groovy` script is implemented, but the only default implementation is the ScriptedSQL connector. |

* Input variables

  The following variables are available to the authenticate script:

  * configuration

    A handler to the connector's configuration object.

  * options

    A handler to the Operation Options.

  * operation

    An OperationType that corresponds to the action (`AUTHENTICATE`).

  * objectClass

    The object class being used to authenticate, such as `__ACCOUNT__` or `__GROUP__`.

  * username

    A string that provides the username to authenticate.

  * password

    A guarded string that provides the password with which to authenticate.

  * log

    A logger instance for the connector.

* Returns

  The user unique ID (ICF `__UID__`). The `type` of the returned UID must be a `string` or a `Uid`. The script must throw an exception in the case of failure.

Authenticate Script

```groovy
def operation = operation as OperationType
def configuration = configuration as ScriptedConfiguration
def username = username as String
def log = log as Log
def objectClass = objectClass as ObjectClass
def options = options as OperationOptions
def password = password as GuardedString;

if (username.equals("TEST")) {
    def clearPassword = SecurityUtil.decrypt(password)
    if ("Passw0rd".equals(clearPassword)) {
        return new Uid(username);
    }
}
```

---

---
title: Common exceptions
description: "Reference for ICF connector framework exceptions: when each is thrown and how they map to Common REST exceptions"
component: openicf
page_id: openicf:connector-dev-guide:common-exceptions
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/common-exceptions.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  openicf-crest-exceptions: Mapping ICF Exceptions to Common REST Exceptions
---

# Common exceptions

The following sections describe the commonly used exceptions that can be thrown, depending on the operation.

* AlreadyExistsException

  The `AlreadyExistsException` is thrown if a create operation attempts to create an object that exists prior to the method execution, or if an update operation attempts to rename an object to that exists prior to the method execution.

- ConfigurationException

  A `ConfigurationException` is thrown if a configuration problem is encountered when the connector bundles are loaded. A `ConfigurationException` can also be thrown during validation operations in the SPI.

* ConnectionBrokenException

  A `ConnectionBrokenException` is thrown when a connection to a target resource instance fails during an operation. An instance of the `ConnectionBrokenException` generally wraps the native exception (or describes the native error) that is returned by the target resource.

- ConnectionFailedException

  A `ConnectionFailedException` is thrown when a connector cannot reach the target resource. An instance of the `ConnectionFailedException` generally wraps the native exception (or describes the native error) that is returned by the target resource.

* ConnectorException

  This is the base exception for the connector framework. The framework only throws exceptions that extend `ConnectorException`.

- ConnectorIOException

  This is the base exception for all Input-Output (I/O-related) exceptions, including instance connection failure, socket error, and so forth.

* ConnectorSecurityException

  This is the base exception for all security-related exceptions.

- InvalidAttributeValueException

  An `InvalidAttributeValueException` is thrown when an attempt is made to add to an attribute a value that conflicts with the attribute's schema definition. This might happen, for example, in the following situations:

  * The connector attempts to add an attribute with no value when the attribute is required to have at least one value.

  * The connector attempts to add more than one value to a single valued-attribute.

  * The connector attempts to add a value that conflicts with the attribute type.

  * The connector attempts to add a value that conflicts with the attribute syntax.

* InvalidCredentialException

  An `InvalidCredentialException` indicates that user authentication has failed. This exception is thrown by the connector when authentication fails, and when the specific reason for the failure is not known. For example, the connector might throw this exception if a user has entered an incorrect password, or username.

- InvalidPasswordException

  An `InvalidPasswordException` is thrown when a password credential is invalid.

* OperationTimeoutException

  An `OperationTimeoutException` is thrown when an operation times out. The framework cancels an operation when the corresponding method has been executing for longer than the limit specified in `APIConfiguration`.

- PasswordExpiredException

  A `PasswordExpiredException` indicates that a user password has expired. This exception is thrown by the connector when it can determine that a password has expired. For example, after successfully authenticating a user, the connector might determine that the user's password has expired. The connector throws this exception to notify the application, which can then take the appropriate steps to notify the user.

* PermissionDeniedException

  A `PermissionDeniedException` is thrown when the target resource will not allow a connector to perform a particular operation. An instance of the `PermissionDeniedException` generally describes a native error (or wraps a native exception) that is returned by the target resource.

- PreconditionFailedException

  A `PreconditionFailedException` is thrown to indicate that a resource's current version does not match the version provided. This exception is equivalent to the HTTP status: `412 Precondition Failed`.

* PreconditionRequiredException

  A `PreconditionRequiredException` is thrown to indicate that a resource requires a version, but that no version was supplied in the request. This exception is equivalent to the HTTP status: `428 Precondition Required`.

- RetryableException

  A `RetryableException` indicates that the failure might be temporary, and that retrying the same request might succeed in the future.

* UnknownUidException

  An `UnknownUidException` is thrown when a UID that is specified as input to a connector operation identifies no object on the target resource. When you implement the `AuthenticateOp`, your connector can throw this exception if it is unable to locate the account necessary to perform authentication.

- NullPointerException (c# NullReferenceException)

  Generic native exception

* UnsupportedOperationException (c# NotSupportedException)

  Generic native exception

- IllegalStateException (c# InvalidOperationException)

  Generic native exception

* IllegalArgumentException (c# ArgumentException)

  Generic native exception

## Mapping ICF Exceptions to Common REST Exceptions

The following table maps the errors that are thrown by the OpenICF framework to the errors that are returned by the Common REST implementation.

| ICF Exception                  | Common REST Exception                            |
| ------------------------------ | ------------------------------------------------ |
| AlreadyExistsException         | ConflictException                                |
| ConfigurationException         | InternalServerErrorException                     |
| ConnectionBrokenException      | InternalServerErrorException                     |
| ConnectionFailedException      | ConnectionFailedException                        |
| ConnectorException             | InternalServerErrorException                     |
| ConnectorIOException           | InternalServerErrorException                     |
| ConnectorSecurityException     | ForbiddenException                               |
| InvalidAttributeValueException | BadRequestException                              |
| InvalidCredentialException     | ForbiddenException                               |
| InvalidPasswordException       | ForbiddenException                               |
| OperationTimeoutException      |                                                  |
| PasswordExpiredException       | ForbiddenException                               |
| PermissionDeniedException      | ForbiddenException                               |
| PreconditionFailedException    | PreconditionFailedException                      |
| PreconditionRequiredException  | PreconditionRequiredException                    |
| RetryableException             | RetryableException (ServiceUnavailableException) |
| UnknownUidException            | NotFoundException                                |
| UnsupportedOperationException  | NotSupportedException                            |
| IllegalArgumentException       | InternalServerErrorException                     |
| NullPointerException           | InternalServerErrorException                     |

---

---
title: Configuration interface
description: How to implement the ICF configuration interface for connector development, including ConfigurationProperty annotations, the validate operation, and supported property types
component: openicf
page_id: openicf:connector-dev-guide:configuration-implementation
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/configuration-implementation.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  operation-validate: Validate operation
  ValidateApiOp-api-level-rules: ValidateApiOp
  validate-spi-level-rules: Validate SPI implementation
  configuration-properties-implementation: Supported configuration types
---

# Configuration interface

The ICF connector framework uses the configuration interface implementation to build the *configuration properties* inside the API configuration.

The configuration interface implementation includes the required information to enable the connector to connect to the target system, and to perform its operations. The configuration interface implements getters and setters for each of its defined properties. It also provides a validate method that your application can use to check whether all the required properties are available, and valid, before passing them to the connector.

The configuration interface has three methods:

* `setConnectorMessages(ConnectorMessages messages)` sets the message catalog instance, and lets the connector provide localized messages.

  The message catalog is defined in the file `Messages.properties`, and can be localized as required by appending the locale to the file name, for example, `Messages_fr.properties`. For more information on the message catalog, refer to [Connector messages object](message-catalog.html).

* `getConnectorMessages()` returns the message catalog that is set by setConnectorMessages(ConnectorMessages).

* `validate()` checks that all the required properties have been set and that their values are valid.

  The purpose of this method is to test that the configuration that the application provides to your connector is valid.

Each property that is declared is not necessarily required. If a property is required, it must be included in the `ConfigurationProperty` annotation.

The `ConfigurationProperty` annotation (Java) or attribute (.NET) lets you add custom meta information to properties. The ICF framework scans the meta information and collects this information to build the `ConfigurationProperties` object inside the `APIConfiguration`. The following meta information can be provided:

| Element           | Description                                                                                                             | Implementation in Java | Implementation in C#   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------------- |
| order             | The order in which this property is displayed                                                                           |                        |                        |
| helpMessageKey    | Lets you change the default help message key                                                                            | `propertyName.help`    | `help_propertyName`    |
| displayMessageKey | Lets you change the default display message key                                                                         | `propertyName.display` | `display_propertyName` |
| groupMessageKey   | Lets you change the default group message key                                                                           | `propertyName.group`   | `group_propertyName`   |
| confidential      | Indicates that this is a confidential property and that its value should be encrypted by the application when persisted |                        |                        |
| required          | Boolean, indicates whether the property is required                                                                     |                        |                        |
| operations        | The array of operations that require this property                                                                      |                        |                        |

The following examples show how the meta information is provided, in both Java and C#.

* Java

* C#

Stateless Configuration Implementation (Java)

```java
public class SampleConfiguration extends AbstractConfiguration  {

    /**
     * {@inheritDoc}
     */
    public void validate() {
    }

    @ConfigurationProperty(
        order = 1,
        helpMessageKey = "passwordFieldName.help",
        displayMessageKey = "passwordFieldName.display",
        groupMessageKey = "authenticateOp.group",
        confidential = false,
        required = false,
        operations = {AuthenticateOp.class,CreateOp.class}
    )
    public String getPasswordFieldName() {
        return passwordFieldName;
    }

    public void setPasswordFieldName(String value) {
        passwordFieldName = value;
    }
}
```

Stateless Configuration Implementation (C#)

```csharp
public class ActiveDirectoryConfiguration : AbstractConfiguration
    {

        [ConfigurationProperty(
            Order = 1,
            HelpMessageKey = "help_PasswordFieldName",
            DisplayMessageKey = "display_PasswordFieldName",
            GroupMessageKey = "group_PasswordFieldName",
            Confidential = false,
            Required = false,
            OperationTypes = new[] { typeof(AuthenticateOp) })
        ]
        public String PasswordFieldName
        { get; set; }

        public override void Validate()
        {
            throw new NotImplementedException();
        }
    }
```

* Java

* C#

Stateful Configuration Implementation (Java)

```java
public class SampleConfiguration extends AbstractConfiguration
    implements StatefulConfiguration {

    /**
     * {@inheritDoc}
     */
    public void release() {
    }

    /**
     * {@inheritDoc}
     */
    public void validate() {
    }
}
```

Stateful Configuration Implementation (C#)

```csharp
public class ActiveDirectoryConfiguration : AbstractConfiguration,
    StatefulConfiguration
    {

        public override void Validate()
        {
            throw new NotImplementedException();
        }

        public void Release()
        {
            throw new NotImplementedException();
        }
    }
```

## Validate operation

The validate operation validates the connector configuration. A valid configuration is one that is *ready to be used* by the connector.

A configuration that is *ready*, has the following characteristics:

* It is complete, that is, all required properties are present and have values.

* All property values are well-formed, that is, they are in the expected range and have the expected format.

### ValidateApiOp

The validate operation returns a `ConfigurationException` in the following situations:

* The Framework version is not compatible with the connector.

* The connector does not have the required attributes in `MANIFEST.MF`.

* The `ConfigurationProperties` cannot be merged into the configuration.

Implementation of the valid operation, at the API Level

```java
@Test
public void ValidateTest() {
    logger.info("Running Validate Test");
    final ConnectorFacade facade = createConnectorFacade(BasicConnector.class, null);
    facade.validate();
}
```

## Validate SPI implementation

The `validate()` method of the configuration operation must return one of the following:

* `RuntimeException` if the configuration is not valid.

* `NullPointerException` if a required configuration property is null.

* `IllegalArgumentException` if a required configuration property is blank.

Implementation of the validate method

```java
public void validate() {
    if (StringUtil.isBlank(host)) {
        throw new IllegalArgumentException("Host User cannot be null or empty.");
    }

    Assertions.blankCheck(remoteUser, "remoteUser");

    Assertions.nullCheck(password, "password");
}
```

## Supported configuration types

The ICF framework supports a limited number of configuration property types. This limitation is necessary, because ICF must serialise and deserialize the configuration property values when sending them over the network.

You can use any of the following types, or an array of these types. Lists of types are not supported.

```
String.class
long.class
Long.class
char.class
Character.class
double.class
Double.class
float.class
Float.class
int.class
Integer.class
boolean.class
Boolean.class
URI.class
File.class
GuardedByteArray.class
GuardedString.class
Script.class
```

```
typeof(string),
typeof(long),
typeof(long?),
typeof(char),
typeof(char?),
typeof(double),
typeof(double?),
typeof(float),
typeof(float?),
typeof(int),
typeof(int?),
typeof(bool),
typeof(bool?),
typeof(Uri),
typeof(FileName),
typeof(GuardedByteArray),
typeof(GuardedString),
typeof(Script)
```

The framework introspects the implemented configuration class and adds all properties that have a `set/get` method to the `ConfigurationProperties` object.

The `ConfigurationClass` annotation (Java) or attribute (.NET) provides additional information to the ICF framework about the configuration class. The following information is provided:

| Element         | Description                                                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| privateProperty | If this is set, the property is hidden from the application, and the application cannot set the property through the `APIConfiguration`.                    |
| skipUnsupported | If the type of an added property is not supported, the framework throws an exception. To avoid the exception, set the value of `skipUnsupported` to `true`. |

* Java

* C#

ConfigurationClass Annotation (Java)

```java
@ConfigurationClass(ignore = { "privateProperty", "internalProperty" }, skipUnsupported = true)
```

ConfigurationClass Attribute (C#)

```csharp
[ConfigurationClass(Ignore = { "privateProperty", "internalProperty" }, SkipUnsupported = true)]
```

---

---
title: Connector archetype
description: How to use the ICF Maven connector archetype to scaffold a new connector project, configure Maven credentials, and build the connector
component: openicf
page_id: openicf:connector-dev-guide:connector-archetype
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/connector-archetype.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  java-connector-operations: Implement ICF operations
  java-connector-bundling: Build the Java connector
---

# Connector archetype

ICF provides a Maven connector archetype that lets you get started with connector development.

The connector archetype assumes that you have Apache Maven installed on your system. Before you use the connector archetype, add the following to your Maven `settings.xml` file, replacing `backstage-username` and `backstage-password` with your Backstage credentials:

```xml
<servers>
 ...
 <server>
    <username>backstage-username</username>
    <password>backstage-password</password>
    <id>archetype</id>
  </server>
</servers>
...
<profiles>
  <profile>
    <id>test</id>
    <activation>
      <activeByDefault>true</activeByDefault>
    </activation>
    <repositories>
      <repository>
         <id>archetype</id>
         <url>https://maven.forgerock.org/artifactory/private-releases</url>
       </repository>
    </repositories>
  </profile>
</profiles>
```

To start building a connector by using the connector archetype, execute the following command, customizing these options to describe your new connector:

* `-DartifactId=sample-connector`

* `-Dversion=0.0-SNAPSHOT`

* `-Dpackage=org.forgerock.openicf.connectors.sample`

* `-DconnectorName=Sample`

This command imports the connector archetype and generates a new connector project:

```
mvn archetype:generate \
 -DarchetypeGroupId=org.forgerock.openicf \
 -DarchetypeArtifactId=connector-archetype \
 -DarchetypeVersion=1.4.0 \
 -DremoteRepositories=https://maven.forgerock.org/artifactory/private-releases \
 -DarchetypeRepository=https://maven.forgerock.org/artifactory/private-releases \
 -DgroupId=org.forgerock.openicf.connectors \
 -DartifactId=sample-connector \
 -Dversion=0.0-SNAPSHOT \
 -Dpackage=org.forgerock.openicf.connectors.sample \
 -DconnectorName=Sample
[INFO] Scanning for projects...
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] Building Maven Stub Project (No POM) 1
[INFO] ------------------------------------------------------------------------
[INFO]
[INFO] >>> maven-archetype-plugin:3.0.1:generate (default-cli) > generate-sources @ standalone-pom >>>
[INFO]
[INFO] <<< maven-archetype-plugin:3.0.1:generate (default-cli) < generate-sources @ standalone-pom <<<
[INFO]
[INFO] --- maven-archetype-plugin:3.0.1:generate (default-cli) @ standalone-pom ---
[INFO] Generating project in Interactive mode
...
ALL_OPERATIONS: n
OP_AUTHENTICATE: n
OP_CREATE: y
OP_DELETE: y
OP_RESOLVEUSERNAME: n
OP_SCHEMA: n
OP_SCRIPTONCONNECTOR: n
OP_SCRIPTONRESOURCE: n
OP_SEARCH: y
OP_SYNC: n
OP_TEST: y
OP_UPDATE: y
OP_UPDATEATTRIBUTEVALUES: n
attributeNormalizer: n
compatibility_version: 1.1
connectorName: Sample
framework_version: 1.0
jira_componentId: 10191
jira_fixVersionIds: 0
poolableConnector: n
 Y: :
```

At this point, you can enter `Y` (YES) to accept the default project, or `N` (NO) to customize the project for your connector.

You will notice in the preceding output that the default connector supports only the `create`, `delete`, `search`, `test`, and `update` operations, and is not a poolable connector. To add support for additional operations, or to change any of the connector parameters, enter `N` (NO). The archetype then prompts you to set values for each additional parameter.

After you have imported the archetype once, you can use the local version of the archetype, as follows:

```
mvn archetype:generate -DarchetypeCatalog=local
```

## Implement ICF operations

When you have generated the archetype, implement the ICF operations that your connector will support.

For information about implementing operations, and examples for a Java connector, refer to [OpenICF SPI](openicf-spi.html).

## Build the Java connector

To build the connector, run:

```
cd /path/to/sample-connector/
mvn install
```

---

---
title: Connector development
description: Hands-on guide to developing connectors using the OpenICF (ICF). ICF provides connectors for a consistent generic layer between applications and target resources
component: openicf
page_id: openicf:connector-dev-guide:preface
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/preface.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# Connector development

> Hands-on guide to developing connectors using the OpenICF (ICF). ICF provides connectors for a consistent generic layer between applications and target resources.

Quick Start

[icon: book, set=fas, size=3x]

#### [About ICF](about-icf.html)

Learn about the OpenICF and ICF connectors.

[icon: share-alt, set=fas, size=3x]

#### [ICF API](openicf-api.html)

Learn about the ICF API.

[icon: share-alt, set=fas, size=3x]

#### [ICF SPI](openicf-spi.html)

Learn about the ICF Service Provider Interface (SPI).

[icon: coffee, set=fas, size=3x]

#### [Java Connectors](java-connectors.html)

Write Java connectors.

[icon: code, set=fas, size=3x]

#### [Groovy Connectors](groovy-connectors.html)

Write scripted Groovy connectors.

[icon: windows, set=fab, size=3x]

#### [PowerShell Connectors](powershell.html)

Write scripted PowerShell connectors.

[icon: question-circle, set=far, size=3x]

#### [Troubleshoot Connectors](troubleshooting.html)

Troubleshoot ICF and connector problems.

---

---
title: Connector info manager
description: How to create a ConnectorInfoManager and ConnectorKey to retrieve local or remote connector info objects when building ICF connectors
component: openicf
page_id: openicf:connector-dev-guide:connector-info-manager
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/connector-info-manager.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Connector info manager

You need to create a `ConnectorInfoManager` and a `ConnectorKey` for your connector.

The `ConnectorKey` uniquely identifies the connector instance. The `ConnectorKey` class takes a `bundleName` (the name of the Connector bundle), a `bundleVersion` (the version of the Connector bundle) and a connectorName (the name of the Connector).

The `ConnectorInfoManager` retrieves a `ConnectorInfo` object for the connector by its connector key.

You must initiate a specific connector info manager type, depending on whether your connector is local or remote. The following samples show how to create a local connector info manager and a remote connector info manager.

Acquiring a Local Connector Info Object (Java)

```java
ConnectorInfoManagerFactory fact = ConnectorInfoManagerFactory.getInstance();
File bundleDirectory = new File("/connectorDir/bundles/myconnector");
URL url = IOUtil.makeURL(bundleDirectory,
     "/dist/org.identityconnectors.myconnector-1.0.jar");
ConnectorInfoManager manager = fact.getLocalManager(url);
ConnectorKey key = new ConnectorKey("org.identityconnectors.myconnector",
     "1.0", "MyConnector");
```

Acquiring a Remote Connector Info Object (Java)

```java
ConnectorInfoManagerFactory fact = ConnectorInfoManagerFactory.getInstance();
File bundleDirectory = new File("/connectorDir/bundles/myconnector");
URL url = IOUtil.makeURL(bundleDirectory,
     "/dist/org.identityconnectors.myconnector-1.0.jar");
ConnectorInfoManager manager = fact.getLocalManager(url);
ConnectorKey key = new ConnectorKey("org.identityconnectors.myconnector",
     "1.0", "MyConnector");
```

---

---
title: Connector instance management
description: How the ICF framework instantiates stateless, poolable, stateful, and stateful-poolable connector types, including object pool and lifecycle details
component: openicf
page_id: openicf:connector-dev-guide:framework-connector-instantiation
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/framework-connector-instantiation.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  connector-instantiation-basic: Instantiate a stateless, non-poolable connector
  connector-instantiation-pooled: Instantiate a stateless, poolable connector
  connector-instantiation-stateful: Instantiate a stateful, non-poolable connector
  connector-instantiation-pooled-stateful: Instantiate a stateful, poolable connector
---

# Connector instance management

The ICF framework supports multiple *connector types*, based on the implementation of the `connector` interface, and the `configuration` interface. These two interfaces determine the following:

* Whether the connector instance is obtained from a pool or whether a new instance is created *for each operation*.

* Whether the connector configuration instance is retained and reused for each operation (stateful configuration), or a new configuration instance is created for each operation (stateless).

Connector developers determine which type of connector to implement, assessing the best match for the resource to which they are connecting. The interaction between the `connector` and `configuration` interface implementations is described in detail in [Connector types](connector-types.html). This section illustrates how the ICF framework manages connector instantiation, depending on the connector type.

## Instantiate a stateless, non-poolable connector

The most basic connector has a stateless configuration, and is not pooled. A basic connector is initialized as follows:

1. The application calls an operation (for example, CREATE) on the connector facade.

2. The ICF framework creates a new *configuration instance*, and initializes it with its configuration properties.

3. When the framework has the configuration instance, with all the attributes in the configuration set, the framework creates a new *connector instance*, and initializes it, with the configuration that has been set.

4. The framework executes the operation (for example, CREATE) on the connector instance.

5. The connector instance executes the operation on the resource.

6. The framework calls the `dispose()` method to release all resources that the connector instance was using.

The following illustration shows the initialization process for a basic connector, and references the numbered steps in the preceding list.

![connector-init-1](_images/connector-init-1.png)

## Instantiate a stateless, poolable connector

The second connector type has a stateless configuration, but can be pooled. A stateless, poolable connector is instantiated as follows:

1. The application calls an operation (for example, CREATE) on the connector facade.

2. The ICF framework calls on the object pool, to borrow a *live* connector instance to execute the operation.

   If the object pool has an idle connector instance available, the framework *borrows* that one instance (step 5a in the illustration that follows).

   The framework calls the `checkAlive` method on the customized connector instance with its configuration, to check if the instance that was borrowed from the pool is still alive, and ready to execute the operation. If the instance is no longer alive and ready, the framework disposes of the instance and borrows another one.

   The thread that borrows the object has exclusive access to that connector instance; that is, it is thread-safe.

3. If the object pool has no idle connector instances, the pool creates a new connector instance.

4. The framework creates a new *configuration instance*, and initializes it with its configuration properties.

5. The framework initializes the borrowed connector instance, with the configuration that has been set.

6. The framework executes the operation (for example, CREATE) on the connector instance.

7. The connector instance executes the operation on the resource.

8. When the operation is complete, the framework releases the connector instance back into the pool. No `dispose()` method is called.

The following illustration shows the initialization process for a stateless, poolable connector, and references the numbered steps in the preceding list.

![connector-init-2](_images/connector-init-2.png)

## Instantiate a stateful, non-poolable connector

The third connector type has a stateful configuration, and cannot be pooled. A stateful, non-poolable connector is instantiated as follows:

1. The ICF framework creates a new *configuration instance*, initializes it with its configuration properties, and stores it in the connector facade, before any operations are called.

   This single configuration instance is shared between multiple threads. The framework does not guarantee isolation, so connector developers must ensure that their implementation is thread-safe.

2. The application calls an operation (for example, CREATE) on the connector facade.

3. The ICF framework creates a new connector instance, and calls the `init()` method on that connector instance, with the stored configuration. The framework initializes the connector with the single configuration instance stored within the connector facade.

4. The framework executes the operation (for example, CREATE) on the connector instance.

5. The connector instance executes the operation on the resource.

6. The framework calls the `dispose()` method to release all resources that the connector instance was using.

   Note that the customized config instance remains in the connector facade, and is reused for the next operation.

The following illustration shows the initialization process for a non-poolable connector, with a stateful configuration. The illustration references the numbered steps in the preceding list.

![connector-init-3](_images/connector-init-3.png)

## Instantiate a stateful, poolable connector

The fourth connector type has a stateful configuration, and can be pooled. A stateful, poolable connector is instantiated as follows:

1. The ICF framework creates a new *configuration instance*, initializes it with its configuration properties, and stores it in the connector facade, before any operations are called.

   This single configuration instance is shared between multiple threads. The framework does not guarantee isolation, so connector developers must ensure that their implementation is thread-safe.

2. The application calls an operation (for example, CREATE) on the connector facade.

3. The framework calls on the object pool, to borrow a *live* connector instance to execute the operation.

   If the object pool has an idle connector instance available, the framework *borrows* that one instance (step 5a in the illustration that follows).

   The framework calls the `checkAlive` method on the customized connector instance with its configuration, to check if the instance that was borrowed from the pool is still alive, and ready to execute the operation. If the instance is no longer alive and ready, the framework disposes of the instance and borrows another one.

   The thread that borrows the object has exclusive access to that connector instance; that is, it is thread-safe.

4. If the object pool has no idle connector instances, the pool creates a new connector instance.

5. The framework initializes the borrowed connector instance, with the stored configuration.

6. The framework executes the operation (for example, CREATE) on the connector instance.

7. The connector instance executes the operation on the resource.

8. When the operation is complete, the framework releases the connector instance back into the pool. No `dispose()` method is called.

The following illustration shows the initialization process for a stateful, poolable connector, and references the numbered steps in the preceding list.

![connector-init-4](_images/connector-init-4.png)

---

---
title: Connector interface
description: Guide to implementing the ICF connector interface and poolable connector interface in Java and C#, including connection pool configuration parameters
component: openicf
page_id: openicf:connector-dev-guide:connector-implementation
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/connector-implementation.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  implement_a_poolable_connector_interface: Implement a poolable connector interface
---

# Connector interface

The connector interface declares a connector, and manages its life cycle. You *must* implement the `connector` interface. A typical connector lifecycle is as follows:

* The connector creates a connection to the target system.

* Any operations implemented in the connector are called.

* The connector discards the connection and disposes of any resources it has used.

The `connector` interface has only three methods:

* `init(Configuration)` initializes the connector with its configuration

* `getConfiguration()` returns the configuration that was passed to `init(Configuration)`

* `dispose()` disposes of any resources that the connector uses.

The `ConnectorClass`, which is the implementation of the connector interface, must have the `ConnectorClass` annotation (Java) or attribute (.NET) so that the ICF framework can find the connector class. The following table shows the elements within the connector class.

| Element             | Description                                                                                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| configurationClass  | The configuration class for the connector.                                                                                                                                                                |
| displayNameKey      | A key in the message catalog that holds a human readable name for the connector.                                                                                                                          |
| categoryKey         | The category to which the connector belongs, such as LDAP, or DB.                                                                                                                                         |
| messageCatalogPaths | The resource path(s) to the message catalog. If multiple paths are provided, the message catalogs are collated. By default, if no path is specified, the `connector-package.Messages.properties` is used. |

The following examples show the connector interface implementation, in Java and C#.

* Java

* C#

Connector Interface Implementation in Java

```java
@ConnectorClass(
    displayNameKey = "Sample.connector.display",
    configurationClass = SampleConfiguration.class)
public class SampleConnector implements Connector...
```

Connector Interface Implementation in C#

```csharp
[ConnectorClass(
    "connector_displayName",
    typeof (SampleConfiguration)
    ]
public class SampleConnector : Connector ...
```

## Implement a poolable connector interface

Certain connectors support the ability to be pooled. For a pooled connector, ICF maintains a pool of connector instances and reuses these instances for multiple provisioning and reconciliation operations. When an operation must be executed, an existing connector instance is taken from the connector pool. If no connector instance exists, a new instance is initialized. When the operation has been executed, the connector instance is released back into the connector pool, ready to be used for a subsequent operation.

For an unpooled connector, a new connector instance is initialized for every operation. When the operation has been executed, ICF disposes of the connector instance. Because the initialization of a connector is an expensive operation, reducing the number of connector initializations can substantially improve performance.

The following connection pooling configuration parameters can be set:

* maxObjects

  The maximum number of connector instances in the pool (both idle and active). The default value is 10 instances.

* maxIdle

  The maximum number of idle connector instances in the pool. The default value is 10 idle instances.

* maxWait

  The maximum period to wait for a free connector instance to become available before failing. The default period is 150000 milliseconds, or 15 seconds.

* minEvictableIdleTimeMillis

  The minimum period to wait before evicting an idle connector instance from the pool. The default period is 120000 milliseconds, or 2 minutes.

  A connection pool cleaner thread runs every minute and closes connections whose `lastUsed` time is larger than the `minEvictableIdleTimeMillis`.

* minIdle

  The minimum number of idle connector instances in the pool. The default value is 1 instance.

A `PoolableConnector` extends the connector interface with the `checkAlive()` method. You should use a `PoolableConnector` when the `init(Configuration)` method is so expensive that it is worth keeping the connector instance in a pool and reusing it between operations. When an existing connector instance is pooled, the framework calls the `checkAlive()` method. If this method throws an error, the framework discards it from the pool and obtains another instance, or creates a new connector instance and calls the `init()` method. The `checkAlive()` method is used to make sure that the instance in the pool is still operational.

---

---
title: Connector messages object
description: Reference for the Connector Messages interface, which sets the message catalog for a connector and enables localization using the format() method
component: openicf
page_id: openicf:connector-dev-guide:message-catalog
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/message-catalog.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Connector messages object

The Connector Messages interface sets the message catalog for each connector, and enables localization of messages. The interface has one method (`format()`), which formats a given message key in the current locale.

For more information, refer to the corresponding [Javadoc](../_attachments/apidocs/org/identityconnectors/framework/common/objects/ConnectorMessages.html).

---

---
title: Connector troubleshooting
description: Troubleshooting guidance for ICF connectors, covering log analysis across framework and application layers, and custom connector version pattern requirements
component: openicf
page_id: openicf:connector-dev-guide:troubleshooting
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/troubleshooting.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Logs", "Troubleshooting"]
section_ids:
  logs: Logs
  custom_connector_required_version_pattern: Custom connector required version pattern
---

# Connector troubleshooting

## Logs

It can be difficult to determine if the root cause of a problem is at the ICF or connector level, or at the application level.

The ICF API sets the `LoggingProxy` at a very high level. You can consider the Logging Proxy as the *border* between the application (IDM) and the ICF framework.

For more information about logging, refer to [Connector logs](../connector-reference/icf-logs.html).

## Custom connector required version pattern

If your custom connector configuration fails to display in the admin UI, make sure that it's using 4-digit versioning. The admin UI expects this type of version pattern. For example:

```
1.5.0.0
```

---

---
title: Connector types
description: "Describes ICF connector types: basic and poolable connectors, stateful and non-stateful configurations, and how they combine to affect connector instantiation"
component: openicf
page_id: openicf:connector-dev-guide:connector-types
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/connector-types.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Connector types

OpenICF supports multiple connector types based on the implementation of the `connector` interface and the `configuration` interface. These two interfaces determine whether the connector can be pooled and whether its configuration is stateful. Before you begin developing your connector, decide on the *connector type* based on the system to which you are connecting. Learn more about how the OpenICF framework manages each connector type in [Connector instance management](framework-connector-instantiation.html).

This section outlines the different connector types.

* Connector

  The basic connector is a *non-poolable* connector. Each operation is executed on a new instance of the connector. OpenICF creates a new instance of the connector class and uses a new or existing instance of the connector configuration to initialize the instance before the operation is started. After the operation completes, OpenICF disposes of the connector instance.

* Poolable Connector

  Before an operation is started, an existing connector instance is pulled from the connector pool. If there's no existing instance, a new instance is created. After the operation runs, the connector instance is released and placed back into the pool.

  The OpenICF framework pools *instances* of a poolable connector, rather than pooling connections within the connector. Learn more about pooling in [Connection pooling configuration](../connector-reference/pooling.html).

* Configuration

  For a basic non-stateful configuration, a new configuration instance is created and configured with the configuration properties each time the configuration is used when an operation is validated or when a new connector instance is initialized.

* Stateful Configuration

  With a stateful configuration, the configuration instance is created only once and is used until the facade or connector pool associated with the configuration is disposed of.

The following table illustrates how these elements combine to determine the connector type.

**Connector Types**

|                            | Connector                                                                                                                                  | Poolable Connector                                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Configuration**          | Entirely stateless combination. A new configuration and connector instance are created for each operation.                                 | It's preferable to keep connector instances in a pool. A new configuration is required only when a new connector instance is added to the pool. |
| **Stateful Configuration** | The configuration can be used to make the heavy resource initialization. The less intensive connector instance can then run the operation. | The configuration must be shared between the instances in the same pool and the connector initialization is expensive.                          |

Learn how the OpenICF framework manages each connector type in [Connector instance management](framework-connector-instantiation.html).

---

---
title: ConnectorFacade interface
description: "Explains the ConnectorFacade interface: how ICF applications use ConnectorFacade to interact with connectors, and how to instantiate and configure it"
component: openicf
page_id: openicf:connector-dev-guide:connector-facade
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/connector-facade.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  create-connector-facade: Creating a ConnectorFacade
---

# ConnectorFacade interface

An application interacts with a connector through an instance of the `ConnectorFacade` class. The following diagram shows the creation and configuration of the connector facade. The components shown here are described in more detail in the sections that follow.

![connector-info](_images/connector-info.png)

The connector facade is instantiated and configured in the following steps:

1. The application creates a `LocalConnectorInfoManager` instance (or instances) and adds the individual connector bundles (or assemblies).

   The `LocalConnectorInfoManager` processes these bundles or assemblies to instantiate a `ConnectorInfo` object.

   To be processed by the connector info manager, the connector bundle or assembly must have the following characteristics:

   * Java Connector Bundle

     The `META-INF/MANIFEST.MF` file *must* include the following entries:

     * `ConnectorBundle-FrameworkVersion` - Minimum required ICF Framework version (either 1.1, 1.4, or 1.5)

     * `ConnectorBundle-Name` - Unique name of the connector bundle

     * `ConnectorBundle-Version` - Version of the connector bundle

     The combination of the `ConnectorBundle-Name` and the `ConnectorBundle-Version` must be unique.

     The connector bundle JAR must contain at least one class, that has the `ConnectorClass` annotation and implements the `Connector` interface.

   * .NET Connector Assembly

     The `AssemblyInfo.cs` is used to determine the bundle version, from the `AssemblyVersion` property.

     The bundle name is derived from the `Name` property of the assembly. For more information, refer to the corresponding [Microsoft documentation](https://msdn.microsoft.com/en-us/library/system.reflection.assemblyname.name\(v=vs.110\).aspx).

     |   |                                                                                                                                       |
     | - | ------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you change the name of your assembly, you must adjust the `bundleName` property in your connector configuration file, accordingly. |

     The connector assembly DLL must contain at least one class, that has the `ConnectorClassAttribute` attribute and implements the `Connector` interface.

2. For each connector, the `LocalConnectorInfoManager` processes the `MessageCatalog`, which contains the localized help and description messages for the configuration, and any log or error messages for the connector.

   Your application can use this information to provide additional help during the connector configuration process.

3. For each connector, the `LocalConnectorInfoManager` then processes the `ConfigurationClass`, to build the configuration properties for the connector.

4. Your application finds the connector info by its *connector key*. When the application has the connector info, it creates an API Configuration object that customizes the following components:

   * Object pool configuration

   * Result handler configuration

   * Configuration properties

   * Timeout configuration

   The API Configuration object is described in more detail in [OpenICF API](openicf-api.html).

5. The `ConnectorFacade` takes this customized API configuration object, determines which connector to use and how to configure it, and implements all of the ICF API operations.

## Creating a ConnectorFacade

Applications access the connector API through a `ConnectorFacade` class, and interact with the connector through a `ConnectorFacade` instance.

The following steps describe how to create a `ConnectorFacade` in your application.

1. Create a `ConnectorInfoManager` and acquire the `ConnectorInfo` object for your connector, as described in the previous section.

2. From the `ConnectorInfo` object, create the default `APIConfiguration`.

   ```java
   APIConfiguration apiConfig = info.createDefaultAPIConfiguration();
   ```

3. Use the default `APIConfiguration` to set the `ObjectPoolConfiguration`, `ResultsHandlerConfiguration`, `ConfigurationProperties`, and `TimeoutConfiguration`.

   ```java
   ConfigurationProperties properties = apiConfig.getConfigurationProperties();
   ```

4. Set all of the `ConfigurationProperties` that you need for the connector, using `setPropertyValue()`.

   ```java
   properties.setPropertyValue("host", SAMPLE_HOST);
   properties.setPropertyValue("adminName", SAMPLE_ADMIN);
   properties.setPropertyValue("adminPassword", SAMPLE_PASSWORD);
   properties.setPropertyValue("usessl", false);
   ```

5. Use the `newInstance()` method of the `ConnectorFacadeFactory` to create a new instance of the connector.

   ```java
   ConnectorFacade conn = ConnectorFacadeFactory.getInstance()
           .newInstance(apiConfig);
   ```

6. Validate that you have set up the connector configuration correctly.

   ```java
   conn.validate();
   ```

7. Use the new connector with the supported operations (described in the following sections).

   ```java
   conn.[authenticate|create|update|delete|search|...]
   ```

---

---
title: Create operation
description: How to implement the ICF create operation in a connector, including the create() method, API-level rules, and SPI-level exceptions
component: openicf
page_id: openicf:connector-dev-guide:operations/operation-create
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/operations/operation-create.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  CreateApiOp-api-level-rules: Use the ICF create operation
  CreateOp-spi-level-rules: Implement the create operation
---

# Create operation

The create operation interface enables the connector to create objects on the target system. The operation includes one method (`create()`). The method takes an `ObjectClass`, and any provided attributes, and creates the object and its UID. The connector must return the UID so that the caller can refer to the created object.

The connector should make a best effort to create the object, and should throw an informative `RuntimeException`, indicating to the caller why the operation could not be completed. Defaults can be used for any required attributes, as long as the defaults are documented.

The UID is never passed in with the attribute set for this method. If the resource supports a mutable UID, you can create a resource-specific attribute for the ID, such as `unix_uid`.

If the `create` operation is only partially successful, the connector should attempt to roll back the partial change. If the target system does not allow this, the connector should report the partial success of the create operation and throw a `RetryableException`. For example:

```java
public static RetryableException wrap(final String message, final Uid uid) {
    return new RetryableException(message, new AlreadyExistsException().initUid(Assertions
    .nullChecked(uid, "Uid")));
}
```

## Use the ICF create operation

The following exceptions are thrown by the Create API operation:

* `IllegalArgumentException` - if `ObjectClass` is missing, or if elements of the set produce duplicate values of `Attribute#getName()`

* `NullPointerException` - if the `createAttributes` parameter is `null`

* `RuntimeException` - if the `Connector` SPI throws a native exception

Consumption of the Create Operation, at the API Level

```java
@Test
public void createTest() {
    logger.info("Running Create Test");
    final ConnectorFacade facade = createConnectorFacade(BasicConnector.class, null);
    final OperationOptionsBuilder builder = new OperationOptionsBuilder();
    Set<Attribute> createAttributes = new HashSet<Attribute>();
    createAttributes.add(new Name("Foo"));
    createAttributes.add(AttributeBuilder.buildPassword("Password".toCharArray()));
    createAttributes.add(AttributeBuilder.buildEnabled(true));
    Uid uid = facade.create(ObjectClass.ACCOUNT, createAttributes, builder.build());
    Assert.assertEquals(uid.getUidValue(), "foo");
}
```

## Implement the create operation

The SPI provides the following detailed exceptions:

* `UnsupportedOperationException` - the create operation is not supported for the specified object class

* `InvalidAttributeValueException` - a required attribute is missing, an attribute is present that cannot be created, or a provided attribute has an invalid value

* `AlreadyExistsException` - an object with the specified `Name` already exits on the target system

* `PermissionDeniedException` - the target resource will not allow the connector to perform the specified operation

* `ConnectorIOException, ConnectionBrokenException, ConnectionFailedException` - a problem as occurred with the connection

* `RuntimeException` - thrown if anything else goes wrong. You should try to throw a native exception in this case.

Implementation of the Create Operation, at the SPI Level

```java
public Uid create(final ObjectClass objectClass, final Set<Attribute> createAttributes,
        final OperationOptions options) {
    if (ObjectClass.ACCOUNT.equals(objectClass) || ObjectClass.GROUP.equals(objectClass)) {
        Name name = AttributeUtil.getNameFromAttributes(createAttributes);
        if (name != null) {
            // do real create here
            return new Uid(AttributeUtil.getStringValue(name).toLowerCase());
        } else {
            throw new InvalidAttributeValueException("Name attribute is required");
        }
    } else {
        logger.warn("Delete of type {0} is not supported", configuration.getConnectorMessages()
                .format(objectClass.getDisplayNameKey(), objectClass.getObjectClassValue()));
        throw new UnsupportedOperationException("Delete of type"
                + objectClass.getObjectClassValue() + " is not supported");
    }
}
```

---

---
title: Create script
description: "Reference for the ICF connector Create script: input variables, return value, and a Groovy example for creating objects on an external resource"
component: openicf
page_id: openicf:connector-dev-guide:scripts/script-create
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/scripts/script-create.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Create script

A create script creates a new object on the external resource. If your connector does not support creating an object, this script should throw an `UnsupportedOperationException`.

A sample create script for an SQL database is provided in `openidm/samples/scripted-sql-with-mysql/tools/CreateScript.groovy`.

* Input variables

  The following variables are available to a create script:

  * configuration

    A handler to the connector's configuration object.

  * options

    A handler to the Operation Options.

  * operation

    An OperationType that corresponds to the action (`CREATE`).

  * objectClass

    The object class that is created, such as `__ACCOUNT__` or `__GROUP__`.

  * attributes

    The set of attributes that describe the object to be created.

  * id

    The UID of the object to be created, if specified. If the UID is `null`, the UID should be generated by the server. The UID corresponds to the ICF `__NAME__` attribute if it is provided as part of the attribute set.

  * log

    A logger instance for the connector.

* Returns

  The user unique ID (ICF `__UID__`) of the newly created object. The `type` of the returned UID must be a `string` or a `Uid`. If a null value or an object type other than `string` or `Uid` is returned, the script must throw an exception.

Create Script

```groovy
def operation = operation as OperationType
 def configuration = configuration as SapConfiguration
 def log = log as Log
 def objectClass = objectClass as ObjectClass
 def createAttributes = new AttributesAccessor(attributes as Set<Attribute>)
 def name = id as String
 def options = options as OperationOptions

 log.info("Entering {0} script",operation);


 assert operation == OperationType.CREATE, 'Operation must be a CREATE'
 // We only deal with users
 assert objectClass.getObjectClassValue() == ObjectClass.ACCOUNT_NAME


 def password = createAttributes.getPassword() as GuardedString;
 assert password != null, 'Password must be provided on create'


 //...
 def uid = createTheUser(createAttributes);
 return uid
```

---

---
title: Custom configuration initialization
description: How to customize Groovy connector toolkit configuration initialization using CustomizerScript.groovy closures such as init, decorate, and release
component: openicf
page_id: openicf:connector-dev-guide:advanced-custom-config
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/advanced-custom-config.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Custom configuration initialization

Connectors created with the Groovy connector toolkit are stateful connectors by default. This means the connector configuration instance is created only once.

The Groovy connector toolkit is precompiled code and connector configurations are initialized in a specific way. If you have specific initialization requirements, you can customize how the connector configuration instance is initialized before the first script is evaluated. The `CustomizerScript.groovy` file lets you define custom closures to interact with the default implementation.

The `CustomizerScript.groovy` file, provided with each compiled connector implementation, defines closures, such as `init {}`, `decorate {}`, and `release {}`. These closures are called during the lifecycle of the configuration.

When you unpack the Groovy connector toolkit JAR file, the `CustomizerScript.groovy` file is located at `org/forgerock/openicf/connectors/connector-implementation`.

---

---
title: Delete operation
description: Reference for implementing the ICF delete operation in a connector, covering the DeleteOp SPI interface, Uid-based removal, and API-level usage
component: openicf
page_id: openicf:connector-dev-guide:operations/operation-delete
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/operations/operation-delete.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  DeleteApiOp-api-level-rules: Use the ICF delete operation
  DeleteOp-spi-level-rules: Implement the delete operation
---

# Delete operation

The delete operation interface enables the connector to delete an object on the target system. The operation includes one method (`delete()`). The method takes an `ObjectClass`, a `Uid`, and any operation options.

The connector should call the native delete methods to remove the object, specified by its unique ID.

## Use the ICF delete operation

The following exceptions are thrown by the Delete API operation:

* `UnknownUidException` - the UID does not exist on the resource

Consumption of the Delete Operation, at the API Level

```java
@Test
public void deleteTest() {
    logger.info("Running Delete Test");
    final ConnectorFacade facade = createConnectorFacade(BasicConnector.class, null);
    final OperationOptionsBuilder builder = new OperationOptionsBuilder();
    facade.delete(ObjectClass.ACCOUNT, new Uid("username"), builder.build());
}
```

## Implement the delete operation

Implementation of the Delete Operation, at the SPI Level

```java
public void delete(final ObjectClass objectClass, final Uid uid, final OperationOptions options) {
    if (ObjectClass.ACCOUNT.equals(objectClass) || ObjectClass.GROUP.equals(objectClass)) {
        // do real delete here
    } else {
        logger.warn("Delete of type {0} is not supported", configuration.getConnectorMessages()
                .format(objectClass.getDisplayNameKey(), objectClass.getObjectClassValue()));
        throw new UnsupportedOperationException("Delete of type"
                + objectClass.getObjectClassValue() + " is not supported");
    }
}
```

---

---
title: Delete script
description: "Reference for the ICF connector delete script: input variables, expected behavior, and return value for delete operations"
component: openicf
page_id: openicf:connector-dev-guide:scripts/script-delete
canonical_url: https://docs.pingidentity.com/openicf/connector-dev-guide/scripts/script-delete.html
llms_txt: https://docs.pingidentity.com/openicf/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Delete script

A delete script deletes an object in the external resource. Connectors that do not support delete operations should throw an `UnsupportedOperationException`.

A sample delete script for an SQL database is provided in `openidm/samples/scripted-sql-with-mysql/tools/DeleteScript.groovy`.

* Input variables

  The following variables are available to an update script:

  * configuration

    A handler to the connector's configuration object.

  * options

    A handler to the Operation Options.

  * operation

    An OperationType that corresponds to the action (`DELETE`).

  * objectClass

    The object class that is deleted, such as `__ACCOUNT__` or `__GROUP__`.

  * uid

    The UID of the object to be deleted. The UID corresponds to the OpenICF `__UID__` attribute.

  * log

    A logger instance for the connector.

* Returns

  This script has no return value but should throw an exception if the delete is unsuccessful.
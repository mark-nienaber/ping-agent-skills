---
title: Install and update on Linux
description: Ping CLI is available for Linux using multiple package managers and as a standalone binary download. Choose the installation method that best fits your environment.
component: pingcli
version: 1.11
page_id: pingcli:install:linux
canonical_url: https://developer.pingidentity.com/pingcli/1.11/install/linux.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 24, 2026
section_ids:
  verify-the-installation: Verify the installation
  upgrading-the-cli-binary: Upgrading the CLI binary
  configuration-migration: Configuration migration
  uninstalling-ping-cli: Uninstalling Ping CLI
  removing-configuration-files-optional: Removing configuration files (optional)
  verify-signatures-optional: Verify signatures (optional)
  verify-using-checksum: Verify using checksum
  verify-using-gpg-signature: Verify using GPG signature
  next-steps: Next steps
---

# Install and update on Linux

Ping CLI is available for Linux using multiple package managers and as a standalone binary download. Choose the installation method that best fits your environment.

* Homebrew

* Debian/Ubuntu (.deb)

* CentOS/Fedora/RHEL (.rpm)

* Alpine (.apk)

* Manual

If you have Homebrew installed on your Linux system, you can use Ping Identity's Homebrew tap to install Ping CLI. As of June 2026, Homebrew requires you to explicitly trust third-party taps before installing their formulae. Trust the Ping Identity tap:

```console
brew trust pingidentity/tap
```

Install Ping CLI:

```console
brew install pingidentity/tap/pingcli
```

Alternatively, if you prefer to add the tap explicitly before installing:

```console
brew tap pingidentity/tap
brew install pingcli
```

Download and install Ping CLI for your architecture (amd64 or arm64) in one step:

```console
RELEASE_VERSION=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/pingidentity/pingcli/releases/latest)); \
DEB_ARCH=$(dpkg --print-architecture); \
DEB_FILE="/tmp/pingcli_${RELEASE_VERSION#v}_linux_${DEB_ARCH}.deb"; \
curl -fLs -o "${DEB_FILE}" "https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_${RELEASE_VERSION#v}_linux_${DEB_ARCH}.deb"; \
sudo apt-get install -y "${DEB_FILE}"; \
rm -f "${DEB_FILE}"
```

Alternatively, download the appropriate package from [the latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) and install using apt:

```console
sudo apt-get install ./pingcli_<version>_linux_amd64.deb
```

Or for ARM64:

```console
sudo apt-get install ./pingcli_<version>_linux_arm64.deb
```

Download the appropriate package from [the latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) and install using yum or dnf:

```console
sudo yum install pingcli_<version>_linux_amd64.rpm
```

Or for ARM64:

```console
sudo yum install pingcli_<version>_linux_arm64.rpm
```

If you're using dnf (Fedora 22+):

```console
sudo dnf install pingcli_<version>_linux_amd64.rpm
```

Download the appropriate package from [the latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) and install using apk:

```console
sudo apk add --allow-untrusted pingcli_<version>_linux_amd64.apk
```

Or for ARM64:

```console
sudo apk add --allow-untrusted pingcli_<version>_linux_arm64.apk
```

To install Ping CLI directly into `/usr/local/bin` using a single command:

```console
RELEASE_VERSION=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/pingidentity/pingcli/releases/latest)); \
OS_NAME=$(uname -s); \
HARDWARE_PLATFORM=$(uname -m | sed s/aarch64/arm64/ | sed s/x86_64/amd64/); \
URL="https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_${RELEASE_VERSION#v}_${OS_NAME}_${HARDWARE_PLATFORM}"; \
curl -Ls -o pingcli "${URL}"; \
sudo mv pingcli /usr/local/bin/pingcli; \
sudo chmod +x /usr/local/bin/pingcli
```

To install a specific version, visit [the GitHub releases page](https://github.com/pingidentity/pingcli/releases) and download a particular version's binary directly.

## Verify the installation

After installation, verify that Ping CLI is properly installed and accessible by checking its version:

```console
pingcli --version
```

You should see output similar to:

```console
pingcli version 1.0.0
```

If the command is not found, ensure that `/usr/local/bin` is in your system's `PATH` environment variable:

```console
echo $PATH
```

## Upgrading the CLI binary

When you upgrade Ping CLI, your existing configuration files are automatically migrated to the new format on first run. This process is safe and includes automatic backups.

* Homebrew

* Debian/Ubuntu

* CentOS/Fedora/RHEL

* Manual

If you installed Ping CLI using Homebrew, upgrading is straightforward. As mentioned above, Homebrew requires trust before upgrading formulae from third-party taps. Trust the Ping Identity tap:

```console
brew trust pingidentity/tap
```

Then upgrade:

```console
brew upgrade pingcli
```

Then verify the upgrade:

```console
pingcli --version
```

Download and install the latest `.deb` over your existing version in one step:

```console
RELEASE_VERSION=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/pingidentity/pingcli/releases/latest)); \
DEB_ARCH=$(dpkg --print-architecture); \
DEB_FILE="/tmp/pingcli_${RELEASE_VERSION#v}_linux_${DEB_ARCH}.deb"; \
curl -fLs -o "${DEB_FILE}" "https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_${RELEASE_VERSION#v}_linux_${DEB_ARCH}.deb"; \
sudo apt-get install -y "${DEB_FILE}"; \
rm -f "${DEB_FILE}"
```

Or download the new `.deb` package and upgrade:

```console
sudo apt-get install --upgrade ./pingcli_<new_version>_linux_amd64.deb
```

```console
sudo yum upgrade pingcli
```

Or with dnf:

```console
sudo dnf upgrade pingcli
```

Download the new binary from [the latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) and replace the existing binary:

```console
RELEASE_VERSION=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/pingidentity/pingcli/releases/latest)); \
OS_NAME=$(uname -s); \
HARDWARE_PLATFORM=$(uname -m | sed s/aarch64/arm64/ | sed s/x86_64/amd64/); \
URL="https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_${RELEASE_VERSION#v}_${OS_NAME}_${HARDWARE_PLATFORM}"; \
curl -Ls -o pingcli "${URL}"; \
sudo mv pingcli /usr/local/bin/pingcli; \
sudo chmod +x /usr/local/bin/pingcli
```

### Configuration migration

When you run Ping CLI after upgrading, the tool automatically detects the old configuration format and creates a migration plan. If you're running interactively, you'll be prompted to approve the migration. The CLI will:

1. Back up your existing config file (with a timestamp, for example, `config.yaml.backup.20260605T123456Z`).

2. Show you what changes will be made.

3. Apply the migration safely (atomic write).

For non-interactive environments (CI/CD scripts), set the following environment variable to auto-approve migration:

```console
export PINGCLI_CONFIG_MIGRATION_POLICY=yes
```

Then run your Ping CLI command as usual.

## Uninstalling Ping CLI

* Homebrew

* Debian/Ubuntu

* CentOS/Fedora/RHEL

* Manual

If you installed Ping CLI using Homebrew:

```console
brew uninstall pingcli
```

```console
sudo apt-get remove pingcli
```

```console
sudo yum remove pingcli
```

Or with dnf:

```console
sudo dnf remove pingcli
```

If you installed Ping CLI manually:

```console
sudo rm /usr/local/bin/pingcli
```

### Removing configuration files (optional)

Ping CLI configuration files are stored in your user's home directory and are not automatically removed when you uninstall the binary. To manually remove them:

```console
rm -rf ~/.pingcli
```

## Verify signatures (optional)

For enhanced security, you can verify the integrity and authenticity of Ping CLI downloads by checking GPG signatures and checksums.

### Verify using checksum

Download the `checksums.txt` file from the [latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) and verify your binary:

```console
sha256sum -c checksums.txt
```

### Verify using GPG signature

Add the Ping Identity public GPG key:

```console
gpg --keyserver keys.openpgp.org --recv-key 0x6703FFB15B36A7AC
```

Then verify the artifact signature:

```console
gpg --verify pingcli_<version>_linux_amd64.sig pingcli_<version>_linux_amd64
```

## Next steps

Now that Ping CLI is installed, proceed to:

* [Configuration settings](../settings_reference/configuration-settings-reference.html) — Learn how to configure Ping CLI

* [Connect Ping Identity services](../using_pingcli/connecting-ping-services.html) — Set up connections to your Ping Identity products

* [Authentication overview](../using_pingcli/authenticating-to-services.html) — Understand authentication methods

---

---
title: Install and update on macOS
description: Ping CLI is available for macOS using Homebrew and as a standalone binary download. Choose the installation method that best fits your environment. Homebrew is the recommended installation method for macOS users.
component: pingcli
version: 1.11
page_id: pingcli:install:macos
canonical_url: https://developer.pingidentity.com/pingcli/1.11/install/macos.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 23, 2026
section_ids:
  verify-the-installation: Verify the installation
  compatibility: Compatibility
  upgrading-the-cli-binary: Upgrading the CLI binary
  configuration-migration: Configuration migration
  uninstalling-ping-cli: Uninstalling Ping CLI
  removing-configuration-files-optional: Removing configuration files (optional)
  next-steps: Next steps
---

# Install and update on macOS

Ping CLI is available for macOS using Homebrew and as a standalone binary download. Choose the installation method that best fits your environment. Homebrew is the recommended installation method for macOS users.

* Homebrew

* Manual

The easiest way to install Ping CLI on macOS is using Homebrew. Homebrew will automatically handle platform detection (Intel or Apple Silicon) and install the appropriate binary.

As of June 2026, Homebrew requires you to explicitly trust third-party taps before installing their formulae. Trust the Ping Identity tap:

```console
brew trust pingidentity/tap
```

Install Ping CLI:

```console
brew install pingidentity/tap/pingcli
```

Alternatively, add the tap explicitly first:

```console
brew tap pingidentity/tap
brew install pingcli
```

To view Ping CLI's installation details:

```console
brew info pingidentity/tap/pingcli
```

If you prefer not to use Homebrew, you can download and install Ping CLI directly into `/usr/local/bin` using this single-line command:

```console
RELEASE_VERSION=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/pingidentity/pingcli/releases/latest)); \
OS_NAME=$(uname -s); \
HARDWARE_PLATFORM=$(uname -m | sed s/aarch64/arm64/ | sed s/x86_64/amd64/); \
URL="https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_${RELEASE_VERSION#v}_${OS_NAME}_${HARDWARE_PLATFORM}"; \
curl -Ls -o pingcli "${URL}"; \
mv pingcli /usr/local/bin/pingcli; \
chmod +x /usr/local/bin/pingcli
```

To install a specific version, visit [the GitHub releases page](https://github.com/pingidentity/pingcli/releases) and download the binary you need.

## Verify the installation

After installation, verify that Ping CLI is properly installed by checking its version:

```console
pingcli --version
```

You should see output similar to:

```console
pingcli version 1.0.0
```

## Compatibility

Ping CLI is available for both Intel and Apple Silicon (ARM64) processors. Homebrew automatically detects your system architecture and installs the appropriate version.

## Upgrading the CLI binary

When you upgrade Ping CLI, your existing configuration files are automatically migrated to the new format on first run. This process is safe and includes automatic backups.

* Homebrew

* Manual

If you installed Ping CLI using Homebrew, upgrading is straightforward. As mentioned above, Homebrew requires trust before upgrading formulae from third-party taps. Trust the Ping Identity tap:

```console
brew trust pingidentity/tap
```

Then upgrade:

```console
brew upgrade pingcli
```

Then verify the upgrade:

```console
pingcli --version
```

If you installed Ping CLI manually, download the new binary from [the latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) and replace the existing binary:

```console
RELEASE_VERSION=$(basename $(curl -Ls -o /dev/null -w %{url_effective} https://github.com/pingidentity/pingcli/releases/latest)); \
OS_NAME=$(uname -s); \
HARDWARE_PLATFORM=$(uname -m | sed s/aarch64/arm64/ | sed s/x86_64/amd64/); \
URL="https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_${RELEASE_VERSION#v}_${OS_NAME}_${HARDWARE_PLATFORM}"; \
curl -Ls -o pingcli "${URL}"; \
mv pingcli /usr/local/bin/pingcli; \
chmod +x /usr/local/bin/pingcli
```

### Configuration migration

When you run Ping CLI after upgrading, the tool automatically detects the old configuration format and creates a migration plan. If you're running interactively, you'll be prompted to approve the migration. The CLI will:

1. Back up your existing config file (with a timestamp, for example, `config.yaml.backup.20260605T123456Z`).

2. Show you what changes will be made.

3. Apply the migration safely (atomic write).

For non-interactive environments (CI/CD scripts), set the following environment variable to auto-approve migration:

```console
export PINGCLI_CONFIG_MIGRATION_POLICY=yes
```

Then run your Ping CLI command as usual.

## Uninstalling Ping CLI

* Homebrew

* Manual

If you installed Ping CLI using Homebrew:

```console
brew uninstall pingcli
```

If you installed Ping CLI manually:

```console
rm /usr/local/bin/pingcli
```

### Removing configuration files (optional)

Ping CLI configuration files are stored in your user's home directory and are not automatically removed when you uninstall the binary. To manually remove them:

```console
rm -rf ~/.pingcli
```

## Next steps

Now that Ping CLI is installed, proceed to:

* [Configuration settings](../settings_reference/configuration-settings-reference.html) — Learn how to configure Ping CLI

* [Connect Ping Identity services](../using_pingcli/connecting-ping-services.html) — Set up connections to your Ping Identity products

---

---
title: Install and update on Windows
description: Ping CLI is available for Windows as a standalone executable. This page covers downloading and installing Ping CLI on Windows systems.
component: pingcli
version: 1.11
page_id: pingcli:install:windows
canonical_url: https://developer.pingidentity.com/pingcli/1.11/install/windows.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  system-requirements: System requirements
  installation: Installation
  verify-the-installation: Verify the installation
  upgrading-the-cli-binary: Upgrading the CLI binary
  configuration-migration: Configuration migration
  uninstalling-ping-cli: Uninstalling Ping CLI
  uninstall-manual-installation: Uninstall manual installation
  removing-configuration-files-optional: Removing configuration files (optional)
  next-steps: Next steps
---

# Install and update on Windows

Ping CLI is available for Windows as a standalone executable. This page covers downloading and installing Ping CLI on Windows systems.

## System requirements

* Windows 7 or later

* PowerShell 5.1 or later

## Installation

Download and install Ping CLI using PowerShell. Visit [the latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) to download the Windows executable.

Alternatively, use this PowerShell command to download and install the latest version:

```powershell
$latestReleaseUrl = Invoke-WebRequest -Uri "https://github.com/pingidentity/pingcli/releases/latest" -MaximumRedirection 0 -ErrorAction Ignore -UseBasicParsing -SkipHttpErrorCheck; `
$RELEASE_VERSION = [System.IO.Path]::GetFileName($latestReleaseUrl.Headers.Location); `
$URL = "https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_windows_amd64.exe"; `
Invoke-WebRequest -Uri $URL -OutFile "pingcli.exe"
```

Move the executable to a location on your system PATH, or add the directory to your system PATH environment variable.

## Verify the installation

After installation, open a PowerShell window and verify that Ping CLI is properly installed:

```powershell
pingcli --version
```

You should see output similar to:

```powershell
pingcli version 1.0.0
```

## Upgrading the CLI binary

When you upgrade Ping CLI, your existing configuration files are automatically migrated to the new format on first run. This process is safe and includes automatic backups.

Download the new executable from [the latest GitHub release](https://github.com/pingidentity/pingcli/releases/latest) and replace the existing one, or use this PowerShell command to download and install the latest version:

```powershell
$latestReleaseUrl = Invoke-WebRequest -Uri "https://github.com/pingidentity/pingcli/releases/latest" -MaximumRedirection 0 -ErrorAction Ignore -UseBasicParsing -SkipHttpErrorCheck; `
$RELEASE_VERSION = [System.IO.Path]::GetFileName($latestReleaseUrl.Headers.Location); `
$URL = "https://github.com/pingidentity/pingcli/releases/download/${RELEASE_VERSION}/pingcli_windows_amd64.exe"; `
Invoke-WebRequest -Uri $URL -OutFile "pingcli.exe"
```

Replace the old executable with this new version and verify the upgrade:

```powershell
pingcli --version
```

### Configuration migration

When you run Ping CLI after upgrading, the tool automatically detects the old configuration format and creates a migration plan. If you're running interactively, you'll be prompted to approve the migration. The CLI will:

1. Back up your existing config file (with a timestamp, for example, `config.yaml.backup.20260605T123456Z`)

2. Show you what changes will be made

3. Apply the migration safely (atomic write)

For non-interactive environments (CI/CD scripts), set the following environment variable to auto-approve migration:

```powershell
$env:PINGCLI_CONFIG_MIGRATION_POLICY = "yes"
```

Then run your Ping CLI command as usual.

## Uninstalling Ping CLI

### Uninstall manual installation

To remove Ping CLI, delete the executable from your system PATH:

```powershell
Remove-Item -Path "C:\path\to\pingcli.exe"
```

Or if you placed it in a directory on your PATH, use File Explorer to navigate to that location and delete `pingcli.exe`.

### Removing configuration files (optional)

Ping CLI configuration files are stored in your user's home directory and are not automatically removed when you uninstall the binary. To manually remove them:

```powershell
Remove-Item -Path $env:USERPROFILE\.pingcli -Recurse -Force
```

## Next steps

Now that Ping CLI is installed, proceed to:

* [Configuration settings](../settings_reference/configuration-settings-reference.html) — Learn how to configure Ping CLI

* [Connect Ping Identity services](../using_pingcli/connecting-ping-services.html) — Set up connections to your Ping Identity products

---

---
title: Installation
description: Ping CLI is a unified Command Line Interface (CLI) tool for developers to manage Ping Identity product deployments and is available on macOS, Linux, and Windows through multiple installation methods, and as a Docker image. Select your platform to get started.
component: pingcli
version: 1.11
page_id: pingcli:install:install
canonical_url: https://developer.pingidentity.com/pingcli/1.11/install/install.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
---

# Installation

Ping CLI is a unified Command Line Interface (CLI) tool for developers to manage Ping Identity product deployments and is available on macOS, Linux, and Windows through multiple installation methods, and as a Docker image. Select your platform to get started.

[icon: apple, set=fab, size=3x]

#### [macOS](macos.html)

Install using Homebrew (recommended) or as a standalone binary.

[icon: linux, set=fab, size=3x]

#### [Linux](linux.html)

Install using Homebrew, a native package (.apk, .deb, .rpm), or a standalone binary.

[icon: windows, set=fab, size=3x]

#### [Windows](windows.html)

Install using a standalone binary download using PowerShell.

[icon: docker, set=fab, size=3x]

#### [Docker](docker.html)

Pull the official Ping CLI Docker image from Docker Hub.

---

---
title: Run as a Docker container
description: Ping CLI is available as a Docker image, allowing you to run it in containerized environments without installing it directly on your system.
component: pingcli
version: 1.11
page_id: pingcli:install:docker
canonical_url: https://developer.pingidentity.com/pingcli/1.11/install/docker.html
llms_txt: https://developer.pingidentity.com/pingcli/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2026
section_ids:
  before-you-begin: Before you begin
  pull-the-ping-cli-docker-image: Pull the Ping CLI Docker image
  verify-the-installation: Verify the installation
  running-ping-cli-in-docker: Running Ping CLI in Docker
  basic-usage: Basic usage
  interactive-shell: Interactive shell
  mounting-local-directories: Mounting local directories
  using-ping-cli-in-cicd-pipelines: Using Ping CLI in CI/CD pipelines
  configuration-migration-in-cicd: Configuration migration in CI/CD
  upgrading-the-docker-image: Upgrading the Docker image
  removing-the-docker-image: Removing the Docker image
  next-steps: Next steps
---

# Run as a Docker container

Ping CLI is available as a Docker image, allowing you to run it in containerized environments without installing it directly on your system.

## Before you begin

You must have:

* Docker installed and running on your system.

* Basic familiarity with Docker commands.

You can find installation instructions in the [Docker documentation](https://docs.docker.com/get-docker/).

## Pull the Ping CLI Docker image

Pull the latest Ping CLI image from Docker Hub:

```console
docker pull pingidentity/pingcli:latest
```

To pull a specific version:

```console
docker pull pingidentity/pingcli:1.0.0
```

## Verify the installation

Verify that the Docker image was pulled successfully:

```console
docker run pingidentity/pingcli:latest --version
```

You should see output similar to:

```console
pingcli version 1.0.0
```

## Running Ping CLI in Docker

### Basic usage

Run Ping CLI commands inside the container:

```console
docker run pingidentity/pingcli:latest --help
```

### Interactive shell

To run Ping CLI interactively inside the container:

```console
docker run -it pingidentity/pingcli:latest
```

### Mounting local directories

To work with configuration files stored on your host system, mount a local directory:

```console
docker run -v /path/to/local/config:/app/config pingidentity/pingcli:latest config list
```

## Using Ping CLI in CI/CD pipelines

Docker makes it easy to use Ping CLI in continuous integration and continuous delivery (CI/CD) workflows. Use the image in GitHub Actions, Docker Compose, or other orchestration tools.

### Configuration migration in CI/CD

When you upgrade the Ping CLI Docker image and use it for the first time, the tool automatically detects the old configuration format and creates a migration plan. For non-interactive environments, set the following environment variable to auto-approve migration:

```console
docker run -e PINGCLI_CONFIG_MIGRATION_POLICY=yes \
  -v /path/to/local/config:/app/config \
  pingidentity/pingcli:latest pingone groups list
```

## Upgrading the Docker image

To upgrade to a newer version of the Ping CLI Docker image:

```console
docker pull pingidentity/pingcli:latest
```

Or pull a specific version:

```console
docker pull pingidentity/pingcli:1.0.0
```

When you run the new image, your configuration files are automatically migrated to the new format on first use. The process is safe and includes automatic backups (stored within the container or mounted volume).

## Removing the Docker image

To remove the Ping CLI Docker image from your system:

```console
docker rmi pingidentity/pingcli:latest
```

Or remove a specific version:

```console
docker rmi pingidentity/pingcli:1.0.0
```

To remove unused images (including dangling ones):

```console
docker image prune
```

## Next steps

Now that you're familiar with running Ping CLI in Docker, proceed to:

* [Configuration settings](../settings_reference/configuration-settings-reference.html) — Learn how to configure Ping CLI

* [Connect Ping Identity services](../using_pingcli/connecting-ping-services.html) — Set up connections to your Ping Identity products
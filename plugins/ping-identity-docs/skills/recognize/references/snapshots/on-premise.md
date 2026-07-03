---
title: Checking the installation completed successfully
description: This page describes how to check that the installation of PingOne Recognize on-premise was successful.
component: recognize
page_id: recognize:on-premise:on-premise-checking-installation-successful
canonical_url: https://docs.pingidentity.com/recognize/on-premise/on-premise-checking-installation-successful.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  execution-of-the-diagnostic: Execution of the diagnostic
  configurable-options: Configurable options
---

# Checking the installation completed successfully

After the installation is complete, the state of the system can be tested using the `cct` testing tool.

As with other assets, access to this tool is provided during the initial setup phase.

## Execution of the diagnostic

This tool is containerized and can be run from anywhere, provided a connection to the `core-daemon` service is available. The most convenient way to run it is with a `kubectl run` command:

```bash
kubectl run -i cct --rm --image=quay.io/keyless_technologies/kl-cct-tester:master --env="APIKEY=some_valid_api_key" --env="HOST=http://core-daemon" --env="FULL_LOG=0" --image-pull-policy="IfNotPresent"
```

Example result:

```text
If you don't see a command prompt, try pressing enter.
Starting tests..
> Performing ENROLL...
> ENROLL completed successfully!
> Performing AUTH...
> AUTH completed successfully!

All tests passed.
Goodbye.
pod "cct" deleted
```

This indicates that the system is running correctly.

## Configurable options

* `APIKEY`

  Must be set to a valid API key recognized by the current installation.

* `HOST`

  Must point to the `core-daemon` host.

* `FULL_LOG`

  `0` for minimal logging, `1` for verbose logging (useful for debugging).

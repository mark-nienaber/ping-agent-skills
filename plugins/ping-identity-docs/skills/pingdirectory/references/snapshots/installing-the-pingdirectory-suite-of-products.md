---
title: Adjusting system memory allocation
description: You can adjust system memory allocation to improve overall performance by setting the /proc/sys/vm/max_map_count kernel tuning parameter. Doing this can prevent problems such as the slowing down of batch execution and a continuous increase of memory used by the JVM.
component: pingdirectory
version: 11.1
page_id: pingdirectory:installing_the_pingdirectory_suite_of_products:pd_ds_adjust_system_memory_alloc
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/installing_the_pingdirectory_suite_of_products/pd_ds_adjust_system_memory_alloc.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Adjusting system memory allocation

You can adjust system memory allocation to improve overall performance by setting the `/proc/sys/vm/max_map_count` kernel tuning parameter. Doing this can prevent problems such as the slowing down of batch execution and a continuous increase of memory used by the JVM.

## About this task

A good setting to use is four times the number of megabytes of system memory. For example, if you're running on a system with 128 gigabytes of memory, then calculate (128\*1024=131072 megabytes) times 4, which is 524288.

## Steps

1. Sign on as root user.

2. Add the line `vm.max_map_count = <megabytes>` to the file `/etc/sysctl.conf`. For example:

   ```
   vm.max_map_count = 524288
   ```

3. Restart the system to apply the change.

4. (Optional) If you need to tune performance further after setting the `max_map_count` parameter, do the following:

   1. Clone the existing performance profile.

   2. Run the `tuned` command.

   3. Add the line `vm.max_map_count = <megabytes>` to the file `/usr/lib/tuned/profile-name/tuned.conf`.

   4. To select the updated profile, run `tuned-adm profile customized_profile`.

   5. Restart the system to apply the changes.

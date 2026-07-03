---
title: Arrays and lists
description: Use arrays and lists in the PingOne Expression Language.
component: pingone
page_id: pingone:pingone_expression_language:p1_expressionlang_arrays_lists
canonical_url: https://docs.pingidentity.com/pingone/pingone_expression_language/p1_expressionlang_arrays_lists.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 3, 2024
---

# Arrays and lists

You can build arrays for the following primitives:

* byte

* short

* int

* long

* float

* double

* char

* boolean

For example, `new <type>[<size>]` or `new <type>[] {<comma-separated values>}`.

You can use lists such as `{<comma-separated values>}`.

|   |                                                       |
| - | ----------------------------------------------------- |
|   | Lists can contain both non-primitives and primitives. |

Access arrays and lists using `[index]`.

| Array or list type                            | Example                               |
| --------------------------------------------- | ------------------------------------- |
| int array                                     | `new long[4]`                         |
| float array                                   | `new float[4]`                        |
| Array initializer                             | `new int[] {1,2,3,4}`                 |
| 2-dimensional array (cannot have initializer) | `new int[2][2]`                       |
| Initializing and accessing array              | `new int[] {1,2,3,4} [0]`             |
| Accessing array property                      | `contacts[0]`                         |
| Empty list                                    | `{}`                                  |
| Integer list                                  | `{1,2,3,4}`                           |
| String list                                   | `{'List', 'of', 'Strings'}`           |
| Accessing list element                        | `{'List', 'of', 'Strings'}[1]`        |
| List with property references                 | `{user.name.given, user.name.family}` |

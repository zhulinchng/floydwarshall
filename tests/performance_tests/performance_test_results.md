---
date created: 2022-07-05 21:17
date updated: 2022-07-05 21:18
---

# Terminal output of tests/performance_test.py

- [Timeit results](#Timeit_results)
- [cProfile results](#cProfile_results)
    * [fw_iterative](#fw_iterative)
    * [fw_recursive](#fw_recursive)
    * [fw_recursive_memo](#fw_recursive_memo)
- [Glossary](##Glossary)

## Timeit results

```
Time taken for fw_iterative is 0.0042489 seconds
Time taken for fw_recursive is 6.431353099999999 seconds
Time taken for fw_recursive_memo is 0.011658500000002903 seconds
```

## cProfile results

### fw_iterative

- Running cprofile for fw_iterative
- 4828 function calls in 0.002 seconds
- Ordered by: cumulative time

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function)                            |
| ------ | ------- | ------- | ------- | ------- | ---------------------------------------------------- |
| 1      | 0       | 0       | 0.002   | 0.002   | {built-in method builtins.exec}                      |
| 1      | 0       | 0       | 0.002   | 0.002   | <string>:2(<module>)                                 |
| 1      | 0       | 0       | 0.002   | 0.002   | performance_test.py:11(perf_test)                    |
| 11     | 0.001   | 0       | 0.001   | 0       | fw_algo.py:7(fw_iterative)                           |
| 11     | 0       | 0       | 0.001   | 0       | tc_generator.py:9(graph_generator)                   |
| 2640   | 0       | 0       | 0       | 0       | {built-in method builtins.min}                       |
| 241    | 0       | 0       | 0       | 0       | random.py:334(randint)                               |
| 241    | 0       | 0       | 0       | 0       | random.py:290(randrange)                             |
| 241    | 0       | 0       | 0       | 0       | random.py:237(_randbelow_with_getrandbits)           |
| 11     | 0       | 0       | 0       | 0       | random.py:126(seed)                                  |
| 11     | 0       | 0       | 0       | 0       | {function Random.seed at 0x0000016ED0B4F940}         |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:221(dirname)                               |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:180(split)                                 |
| 440    | 0       | 0       | 0       | 0       | {method 'append' of 'list' objects}                  |
| 330    | 0       | 0       | 0       | 0       | {method 'random' of '_random.Random' objects}        |
| 4      | 0       | 0       | 0       | 0       | ntpath.py:124(splitdrive)                            |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:524(abspath)                               |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:450(normpath)                              |
| 312    | 0       | 0       | 0       | 0       | {method 'getrandbits' of '_random.Random' objects}   |
| 241    | 0       | 0       | 0       | 0       | {method 'bit_length' of 'int' objects}               |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:77(join)                                   |
| 33     | 0       | 0       | 0       | 0       | {built-in method builtins.isinstance}                |
| 1      | 0       | 0       | 0       | 0       | <frozen importlib._bootstrap>:1033(_handle_fromlist) |
| 1      | 0       | 0       | 0       | 0       | {built-in method nt._getfullpathname}                |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:34(_get_bothseps)                          |
| 5      | 0       | 0       | 0       | 0       | {method 'replace' of 'str' objects}                  |
| 26     | 0       | 0       | 0       | 0       | {built-in method builtins.len}                       |
| 2      | 0       | 0       | 0       | 0       | {method 'startswith' of 'str' objects}               |
| 1      | 0       | 0       | 0       | 0       | {method 'split' of 'str' objects}                    |
| 7      | 0       | 0       | 0       | 0       | {built-in method nt.fspath}                          |
| 4      | 0       | 0       | 0       | 0       | {built-in method builtins.hasattr}                   |
| 1      | 0       | 0       | 0       | 0       | {method 'join' of 'str' objects}                     |
| 1      | 0       | 0       | 0       | 0       | {method 'lstrip' of 'str' objects}                   |
| 1      | 0       | 0       | 0       | 0       | {method 'insert' of 'list' objects}                  |
| 1      | 0       | 0       | 0       | 0       | {method 'rstrip' of 'str' objects}                   |
| 1      | 0       | 0       | 0       | 0       | {method 'disable' of '_lsprof.Profiler' objects}     |

## fw_recursive

- Running cprofile for fw_recursive
- 14439334 function calls (3611722 primitive calls) in 2.631 seconds
- Ordered by: cumulative time

| ncalls       | tottime | percall | cumtime | percall | filename:lineno(function)                            |
| ------------ | ------- | ------- | ------- | ------- | ---------------------------------------------------- |
| 1            | 0       | 0       | 2.631   | 2.631   | {built-in method builtins.exec}                      |
| 1            | 0       | 0       | 2.631   | 2.631   | <string>:2(<module>)                                 |
| 1            | 0       | 0       | 2.631   | 2.631   | performance_test.py:11(perf_test)                    |
| 11           | 0       | 0       | 2.63    | 0.239   | fw_algo.py:29(fw_recursive)                          |
| 10827942/330 | 2.283   | 0       | 2.63    | 0.008   | 008 fw_algo.py:41(min_path)                          |
| 3609204      | 0.347   | 0       | 0.347   | 0       | {built-in method builtins.min}                       |
| 11           | 0       | 0       | 0.001   | 0       | tc_generator.py:9(graph_generator)                   |
| 241          | 0       | 0       | 0       | 0       | random.py:334(randint)                               |
| 241          | 0       | 0       | 0       | 0       | random.py:290(randrange)                             |
| 241          | 0       | 0       | 0       | 0       | random.py:237(_randbelow_with_getrandbits)           |
| 11           | 0       | 0       | 0       | 0       | random.py:126(seed)                                  |
| 11           | 0       | 0       | 0       | 0       | {function Random.seed at 0x0000016ED0B4F940}         |
| 440          | 0       | 0       | 0       | 0       | {method 'append' of 'list' objects}                  |
| 330          | 0       | 0       | 0       | 0       | {method 'random' of '_random.Random' objects}        |
| 1            | 0       | 0       | 0       | 0       | ntpath.py:524(abspath)                               |
| 1            | 0       | 0       | 0       | 0       | ntpath.py:221(dirname)                               |
| 1            | 0       | 0       | 0       | 0       | ntpath.py:180(split)                                 |
| 312          | 0       | 0       | 0       | 0       | {method 'getrandbits' of '_random.Random' objects}   |
| 1            | 0       | 0       | 0       | 0       | ntpath.py:450(normpath)                              |
| 241          | 0       | 0       | 0       | 0       | {method 'bit_length' of 'int' objects}               |
| 4            | 0       | 0       | 0       | 0       | ntpath.py:124(splitdrive)                            |
| 33           | 0       | 0       | 0       | 0       | {built-in method builtins.isinstance}                |
| 1            | 0       | 0       | 0       | 0       | ntpath.py:77(join)                                   |
| 1            | 0       | 0       | 0       | 0       | <frozen importlib._bootstrap>:1033(_handle_fromlist) |
| 1            | 0       | 0       | 0       | 0       | {built-in method nt._getfullpathname}                |
| 26           | 0       | 0       | 0       | 0       | {built-in method builtins.len}                       |
| 1            | 0       | 0       | 0       | 0       | ntpath.py:34(_get_bothseps)                          |
| 5            | 0       | 0       | 0       | 0       | {method 'replace' of 'str' objects}                  |
| 1            | 0       | 0       | 0       | 0       | {method 'split' of 'str' objects}                    |
| 2            | 0       | 0       | 0       | 0       | {method 'startswith' of 'str' objects}               |
| 4            | 0       | 0       | 0       | 0       | {built-in method builtins.hasattr}                   |
| 7            | 0       | 0       | 0       | 0       | {built-in method nt.fspath}                          |
| 1            | 0       | 0       | 0       | 0       | {method 'insert' of 'list' objects}                  |
| 1            | 0       | 0       | 0       | 0       | {method 'join' of 'str' objects}                     |
| 1            | 0       | 0       | 0       | 0       | {method 'disable' of '_lsprof.Profiler' objects}     |
| 1            | 0       | 0       | 0       | 0       | {method 'lstrip' of 'str' objects}                   |
| 1            | 0       | 0       | 0       | 0       | {method 'rstrip' of 'str' objects}                   |

## fw_recursive_memo

- Running cprofile for fw_recursive_memo
- 13738 function calls (5323 primitive calls) in 0.004 seconds
- Ordered by: cumulative time

| ncalls   | tottime | percall | cumtime | percall | filename:lineno(function)                            |
| -------- | ------- | ------- | ------- | ------- | ---------------------------------------------------- |
| 1        | 0       | 0       | 0.004   | 0.004   | {built-in method builtins.exec}                      |
| 1        | 0       | 0       | 0.004   | 0.004   | <string>:2(<module>)                                 |
| 1        | 0       | 0       | 0.004   | 0.004   | performance_test.py:11(perf_test)                    |
| 11       | 0       | 0       | 0.003   | 0       | fw_algo.py:63(fw_recursive_memo)                     |
| 8745/330 | 0.003   | 0       | 0.003   | 0       | fw_algo.py:76(min_path)                              |
| 11       | 0       | 0       | 0.001   | 0       | tc_generator.py:9(graph_generator)                   |
| 2805     | 0       | 0       | 0       | 0       | {built-in method builtins.min}                       |
| 241      | 0       | 0       | 0       | 0       | random.py:334(randint)                               |
| 241      | 0       | 0       | 0       | 0       | random.py:290(randrange)                             |
| 241      | 0       | 0       | 0       | 0       | random.py:237(_randbelow_with_getrandbits)           |
| 11       | 0       | 0       | 0       | 0       | random.py:126(seed)                                  |
| 11       | 0       | 0       | 0       | 0       | {function Random.seed at 0x0000016ED0B4F940}         |
| 440      | 0       | 0       | 0       | 0       | {method 'append' of 'list' objects}                  |
| 330      | 0       | 0       | 0       | 0       | {method 'random' of '_random.Random' objects}        |
| 1        | 0       | 0       | 0       | 0       | ntpath.py:524(abspath)                               |
| 1        | 0       | 0       | 0       | 0       | ntpath.py:221(dirname)                               |
| 312      | 0       | 0       | 0       | 0       | {method 'getrandbits' of '_random.Random' objects}   |
| 1        | 0       | 0       | 0       | 0       | ntpath.py:180(split)                                 |
| 1        | 0       | 0       | 0       | 0       | ntpath.py:450(normpath)                              |
| 241      | 0       | 0       | 0       | 0       | {method 'bit_length' of 'int' objects}               |
| 4        | 0       | 0       | 0       | 0       | ntpath.py:124(splitdrive)                            |
| 1        | 0       | 0       | 0       | 0       | ntpath.py:77(join)                                   |
| 1        | 0       | 0       | 0       | 0       | <frozen importlib._bootstrap>:1033(_handle_fromlist) |
| 33       | 0       | 0       | 0       | 0       | {built-in method builtins.isinstance}                |
| 1        | 0       | 0       | 0       | 0       | {built-in method nt._getfullpathname}                |
| 26       | 0       | 0       | 0       | 0       | {built-in method builtins.len}                       |
| 1        | 0       | 0       | 0       | 0       | ntpath.py:34(_get_bothseps)                          |
| 1        | 0       | 0       | 0       | 0       | {method 'split' of 'str' objects}                    |
| 7        | 0       | 0       | 0       | 0       | {built-in method nt.fspath}                          |
| 5        | 0       | 0       | 0       | 0       | {method 'replace' of 'str' objects}                  |
| 1        | 0       | 0       | 0       | 0       | {method 'rstrip' of 'str' objects}                   |
| 2        | 0       | 0       | 0       | 0       | {method 'startswith' of 'str' objects}               |
| 4        | 0       | 0       | 0       | 0       | {built-in method builtins.hasattr}                   |
| 1        | 0       | 0       | 0       | 0       | {method 'insert' of 'list' objects}                  |
| 1        | 0       | 0       | 0       | 0       | {method 'join' of 'str' objects}                     |
| 1        | 0       | 0       | 0       | 0       | {method 'lstrip' of 'str' objects}                   |
| 1        | 0       | 0       | 0       | 0       | {method 'disable' of '_lsprof.Profiler' objects}     |

## Glossary

| col name                  | description                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ncalls                    | for the number of calls.                                                                                                                     |
| tottime                   | for the total time spent in the given function (and excluding time made in calls to sub-functions)                                           |
| percall                   | is the quotient of tottime divided by ncalls                                                                                                 |
| cumtime                   | is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions. |
| percall                   | is the quotient of cumtime divided by primitive calls                                                                                        |
| filename:lineno(function) | provides the respective data of each function                                                                                                |

- When there are two numbers in the first column (for example `3/1`), it means that the function recursed.
- The second value is the number of primitive calls and the former is the total number of calls.
- Note that when the function does not recurse, these two values are the same, and only the single figure is printed.

[Python Documentation](https://docs.python.org/3/library/profile.html)

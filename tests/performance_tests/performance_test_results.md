---
date created: 2022-07-05 21:17
date updated: 2022-07-05 21:18
---

# Performance test results

- [Performance test results](#performance-test-results)
  - [Timeit results](#timeit-results)
  - [cProfile results](#cprofile-results)
    - [fw_iterative](#fw_iterative)
    - [fw_recursive](#fw_recursive)
    - [fw_recursive_memo](#fw_recursive_memo)
  - [Test environment](#test-environment)
  - [Glossary](#glossary)

## Timeit results

Each function was run 5 times, for 11 different test cases ranging from 0x0 to 10x10 square matrices each time.

This was repeated for another 5 times, the minimum time was then recorded for each function.

```python
Time taken for fw_iterative is 0.0033771999878808856 seconds
Time taken for fw_recursive is 4.942898500012234 seconds
Time taken for fw_recursive_memo is 0.010060300002805889 seconds
```

## cProfile results

Each function was run 1 time, for 11 different test cases ranging from 0x0 to 10x10 square matrices each time.

The profile shows the total time and calls taken by each function to run the 11 different test cases.

### fw_iterative

```python
Running cprofile for fw_iterative
        5556 function calls in 0.002 seconds

    Ordered by: cumulative time
```

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function)                            |
|--------|---------|---------|---------|---------|------------------------------------------------------|
| 1      | 0       | 0       | 0.002   | 0.002   | {built-in method builtins.exec}                      |
| 1      | 0       | 0       | 0.002   | 0.002   | <string>:1(<module>)                                 |
| 1      | 0       | 0       | 0.002   | 0.002   | performance_test.py:9(perf_test)                     |
| 11     | 0.001   | 0       | 0.001   | 0       | fw_algo.py:5(fw_iterative)                           |
| 11     | 0       | 0       | 0.001   | 0       | tc_generator.py:7(graph_generator)                   |
| 241    | 0       | 0       | 0       | 0       | random.py:366(randint)                               |
| 241    | 0       | 0       | 0       | 0       | random.py:292(randrange)                             |
| 2640   | 0       | 0       | 0       | 0       | {built-in method builtins.min}                       |
| 241    | 0       | 0       | 0       | 0       | random.py:239(_randbelow_with_getrandbits)           |
| 11     | 0       | 0       | 0       | 0       | random.py:128(seed)                                  |
| 723    | 0       | 0       | 0       | 0       | {built-in method _operator.index}                    |
| 11     | 0       | 0       | 0       | 0       | {function Random.seed at 0x0000021700990310}         |
| 440    | 0       | 0       | 0       | 0       | {method 'append' of 'list' objects}                  |
| 330    | 0       | 0       | 0       | 0       | {method 'random' of '_random.Random' objects}        |
| 312    | 0       | 0       | 0       | 0       | {method 'getrandbits' of '_random.Random' objects}   |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:221(dirname)                               |
| 241    | 0       | 0       | 0       | 0       | {method 'bit_length' of 'int' objects}               |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:180(split)                                 |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:537(abspath)                               |
| 4      | 0       | 0       | 0       | 0       | ntpath.py:124(splitdrive)                            |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:463(normpath)                              |
| 11     | 0       | 0       | 0       | 0       | fw_algo.py:16(<listcomp>)                            |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:77(join)                                   |
| 1      | 0       | 0       | 0       | 0       | <frozen importlib._bootstrap>:1053(_handle_fromlist) |
| 33     | 0       | 0       | 0       | 0       | {built-in method builtins.isinstance}                |
| 1      | 0       | 0       | 0       | 0       | ntpath.py:34(_get_bothseps)                          |
| 20     | 0       | 0       | 0       | 0       | {built-in method builtins.len}                       |
| 1      | 0       | 0       | 0       | 0       | {built-in method nt._getfullpathname}                |
| 7      | 0       | 0       | 0       | 0       | {built-in method nt.fspath}                          |
| 5      | 0       | 0       | 0       | 0       | {method 'replace' of 'str' objects}                  |
| 2      | 0       | 0       | 0       | 0       | {method 'startswith' of 'str' objects}               |
| 4      | 0       | 0       | 0       | 0       | {built-in method builtins.hasattr}                   |
| 1      | 0       | 0       | 0       | 0       | {method 'split' of 'str' objects}                    |
| 1      | 0       | 0       | 0       | 0       | {method 'insert' of 'list' objects}                  |
| 1      | 0       | 0       | 0       | 0       | {method 'join' of 'str' objects}                     |
| 1      | 0       | 0       | 0       | 0       | {method 'lstrip' of 'str' objects}                   |
| 1      | 0       | 0       | 0       | 0       | {method 'rstrip' of 'str' objects}                   |
| 1      | 0       | 0       | 0       | 0       | {method 'disable' of '_lsprof.Profiler' objects}     |

### fw_recursive

```python
Running cprofile for fw_recursive
        14440062 function calls (3612450 primitive calls) in 2.675 seconds

    Ordered by: cumulative time
```

| ncalls       | tottime  | percall  | cumtime  | percall  | filename:lineno(function)                            |
|--------------|----------|----------|----------|----------|------------------------------------------------------|
| 1            | 0        | 0        | 2.675    | 2.675    | {built-in method builtins.exec}                      |
| 1            | 0        | 0        | 2.675    | 2.675    | <string>:1(<module>)                                 |
| 1            | 0        | 0        | 2.675    | 2.675    | performance_test.py:9(perf_test)                     |
| 11           | 0        | 0        | 2.674    | 0.243    | fw_algo.py:30(fw_recursive)                          |
| 10827942/330 | 2.309    | 0        | 2.674    | 0        | 008 fw_algo.py:45(min_path)                          |
| 3609204      | 0.365    | 0        | 0.365    | 0        | {built-in method builtins.min}                       |
| 11           | 0        | 0        | 0.001    | 0        | tc_generator.py:7(graph_generator)                   |
| 241          | 0        | 0        | 0        | 0        | random.py:366(randint)                               |
| 241          | 0        | 0        | 0        | 0        | random.py:292(randrange)                             |
| 241          | 0        | 0        | 0        | 0        | random.py:239(_randbelow_with_getrandbits)           |
| 11           | 0        | 0        | 0        | 0        | random.py:128(seed)                                  |
| 11           | 0        | 0        | 0        | 0        | {function Random.seed at 0x0000021700990310}         |
| 723          | 0        | 0        | 0        | 0        | {built-in method _operator.index}                    |
| 440          | 0        | 0        | 0        | 0        | {method 'append' of 'list' objects}                  |
| 330          | 0        | 0        | 0        | 0        | {method 'random' of '_random.Random' objects}        |
| 312          | 0        | 0        | 0        | 0        | {method 'getrandbits' of '_random.Random' objects}   |
| 1            | 0        | 0        | 0        | 0        | ntpath.py:221(dirname)                               |
| 1            | 0        | 0        | 0        | 0        | ntpath.py:537(abspath)                               |
| 1            | 0        | 0        | 0        | 0        | ntpath.py:180(split)                                 |
| 11           | 0        | 0        | 0        | 0        | fw_algo.py:41(<listcomp>)                            |
| 241          | 0        | 0        | 0        | 0        | {method 'bit_length' of 'int' objects}               |
| 1            | 0        | 0        | 0        | 0        | ntpath.py:463(normpath)                              |
| 4            | 0        | 0        | 0        | 0        | ntpath.py:124(splitdrive)                            |
| 33           | 0        | 0        | 0        | 0        | {built-in method builtins.isinstance}                |
| 1            | 0        | 0        | 0        | 0        | ntpath.py:77(join)                                   |
| 1            | 0        | 0        | 0        | 0        | <frozen importlib._bootstrap>:1053(_handle_fromlist) |
| 1            | 0        | 0        | 0        | 0        | {built-in method nt._getfullpathname}                |
| 1            | 0        | 0        | 0        | 0        | ntpath.py:34(_get_bothseps)                          |
| 20           | 0        | 0        | 0        | 0        | {built-in method builtins.len}                       |
| 7            | 0        | 0        | 0        | 0        | {built-in method nt.fspath}                          |
| 5            | 0        | 0        | 0        | 0        | {method 'replace' of 'str' objects}                  |
| 1            | 0        | 0        | 0        | 0        | {method 'split' of 'str' objects}                    |
| 2            | 0        | 0        | 0        | 0        | {method 'startswith' of 'str' objects}               |
| 4            | 0        | 0        | 0        | 0        | {built-in method builtins.hasattr}                   |
| 1            | 0        | 0        | 0        | 0        | {method 'disable' of '_lsprof.Profiler' objects}     |
| 1            | 0        | 0        | 0        | 0        | {method 'insert' of 'list' objects}                  |
| 1            | 0        | 0        | 0        | 0        | {method 'join' of 'str' objects}                     |
| 1            | 0        | 0        | 0        | 0        | {method 'lstrip' of 'str' objects}                   |
| 1            | 0        | 0        | 0        | 0        | {method 'rstrip' of 'str' objects}                   |

### fw_recursive_memo

```python
Running cprofile for fw_recursive_memo
        14466 function calls (6051 primitive calls) in 0.004 seconds

    Ordered by: cumulative time
```

| ncalls   | tottime  | percall  | cumtime  | percall  | filename:lineno(function)                            |
|----------|----------|----------|----------|----------|------------------------------------------------------|
| 1        | 0        | 0        | 0.004    | 0.004    | {built-in method builtins.exec}                      |
| 1        | 0        | 0        | 0.004    | 0.004    | <string>:1(<module>)                                 |
| 1        | 0        | 0        | 0.004    | 0.004    | performance_test.py:9(perf_test)                     |
| 11       | 0        | 0        | 0.004    | 0        | fw_algo.py:67(fw_recursive_memo)                     |
| 8745/330 | 0.003    | 0        | 0.003    | 0        | fw_algo.py:83(min_path)                              |
| 11       | 0        | 0        | 0.001    | 0        | tc_generator.py:7(graph_generator)                   |
| 241      | 0        | 0        | 0        | 0        | random.py:366(randint)                               |
| 241      | 0        | 0        | 0        | 0        | random.py:292(randrange)                             |
| 2805     | 0        | 0        | 0        | 0        | {built-in method builtins.min}                       |
| 241      | 0        | 0        | 0        | 0        | random.py:239(_randbelow_with_getrandbits)           |
| 11       | 0        | 0        | 0        | 0        | random.py:128(seed)                                  |
| 723      | 0        | 0        | 0        | 0        | {built-in method _operator.index}                    |
| 11       | 0        | 0        | 0        | 0        | {function Random.seed at 0x0000021700990310}         |
| 440      | 0        | 0        | 0        | 0        | {method 'append' of 'list' objects}                  |
| 330      | 0        | 0        | 0        | 0        | {method 'random' of '_random.Random' objects}        |
| 1        | 0        | 0        | 0        | 0        | ntpath.py:221(dirname)                               |
| 312      | 0        | 0        | 0        | 0        | {method 'getrandbits' of '_random.Random' objects}   |
| 1        | 0        | 0        | 0        | 0        | ntpath.py:180(split)                                 |
| 1        | 0        | 0        | 0        | 0        | ntpath.py:537(abspath)                               |
| 241      | 0        | 0        | 0        | 0        | {method 'bit_length' of 'int' objects}               |
| 1        | 0        | 0        | 0        | 0        | ntpath.py:463(normpath)                              |
| 4        | 0        | 0        | 0        | 0        | ntpath.py:124(splitdrive)                            |
| 1        | 0        | 0        | 0        | 0        | ntpath.py:77(join)                                   |
| 11       | 0        | 0        | 0        | 0        | fw_algo.py:78(<listcomp>)                            |
| 33       | 0        | 0        | 0        | 0        | {built-in method builtins.isinstance}                |
| 1        | 0        | 0        | 0        | 0        | <frozen importlib._bootstrap>:1053(_handle_fromlist) |
| 1        | 0        | 0        | 0        | 0        | {built-in method nt._getfullpathname}                |
| 1        | 0        | 0        | 0        | 0        | ntpath.py:34(_get_bothseps)                          |
| 20       | 0        | 0        | 0        | 0        | {built-in method builtins.len}                       |
| 1        | 0        | 0        | 0        | 0        | {method 'split' of 'str' objects}                    |
| 7        | 0        | 0        | 0        | 0        | {built-in method nt.fspath}                          |
| 2        | 0        | 0        | 0        | 0        | {method 'startswith' of 'str' objects}               |
| 5        | 0        | 0        | 0        | 0        | {method 'replace' of 'str' objects}                  |
| 4        | 0        | 0        | 0        | 0        | {built-in method builtins.hasattr}                   |
| 1        | 0        | 0        | 0        | 0        | {method 'insert' of 'list' objects}                  |
| 1        | 0        | 0        | 0        | 0        | {method 'join' of 'str' objects}                     |
| 1        | 0        | 0        | 0        | 0        | {method 'lstrip' of 'str' objects}                   |
| 1        | 0        | 0        | 0        | 0        | {method 'rstrip' of 'str' objects}                   |
| 1        | 0        | 0        | 0        | 0        | {method 'disable' of '_lsprof.Profiler' objects}     |

## Test environment

The tests are run with the following configuration:

- `Python` version 3.10.2
- `floydwarshall` package version 1.0.0
- `tests` package version 1.0.0

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

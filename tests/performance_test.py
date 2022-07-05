"""
Performance test on floyd warshall algorithm
"""
import timeit
import cProfile
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from floydwarshall import fw_iterative, fw_recursive, fw_recursive_memo, graph_generator

def perf_test(fn: callable) -> None:
    """
    Run performance test on the given function.
    Tested across a range of graph sizes from 0 to 10.

    :param fn: function to run performance test on
    :return: None
    """
    size = 10
    for i in range(size+1):
        kwargs = {'size': i,
                  'edgeprob': 0.8,
                  'minval': -2,
                  'maxval': 100,
                  'seed': 4} # this seed is specifically chosen to avoid negative cycles for these graphs
        fn(graph_generator(**kwargs))

def timeit_perf_test(fn) -> None:
    """
    Run timeit test on the given Floyd-Warshall algorithm.
    """
    setup = """
from __main__ import perf_test
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from floydwarshall import fw_iterative, fw_recursive, fw_recursive_memo, graph_generator
    """
    time = timeit.repeat(
        f'perf_test({fn.__name__})', setup=setup, repeat=5, number=5)
    print(f'Time taken for {fn.__name__} is {min(time)} seconds')

def cprofile_perf_test(fn) -> None:
    """
    Run cprofile test on the given Floyd-Warshall algorithm.
    """
    setup = """
from __main__ import perf_test
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from floydwarshall import fw_iterative, fw_recursive, fw_recursive_memo, graph_generator

    """
    print(f'Running cprofile for {fn.__name__}')
    cProfile.run(setup+f'\nperf_test({fn.__name__})', sort='cumtime')

if __name__ == '__main__':
    function_list = [fw_iterative, fw_recursive, fw_recursive_memo]
    for fn in function_list:
        timeit_perf_test(fn)
        cprofile_perf_test(fn)

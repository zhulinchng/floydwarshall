"""
Generate test cases for performance testing
"""
import sys
import pickle
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from floydwarshall import fw_iterative, graph_generator

perf_data_dir = 'tests/performance_tests/data'
size = 10
for i in range(size+1):
    kwargs = {'size' : i,
              'edgeprob' : 0.8,
              'minval' : -2,
              'maxval' : 100,
              'seed' : 4}
    input_graph = graph_generator(**kwargs)
    with open(f'{perf_data_dir}/case{i}_input.pkl', 'wb') as f:
        pickle.dump(input_graph, f)
    with open(f'{perf_data_dir}/case{i}_output.pkl', 'wb') as f:
        pickle.dump(fw_iterative(input_graph), f)
    print(f'Generated test case {i}')
print('Done')

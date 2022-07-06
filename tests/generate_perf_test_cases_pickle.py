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
tc_list = []
for i in range(size+1):
    kwargs = {'size' : i,
              'edgeprob' : 0.8,
              'minval' : -2,
              'maxval' : 100,
              'seed' : 4}
    input_graph = graph_generator(**kwargs)
    tc_list.append({'case' : 'case_'+str(i),
                    'input_graph' : input_graph,
                    'output_graph' : fw_iterative(input_graph)})
    print(f'Generated test case {i}')
with open(f'{perf_data_dir}/perf_data.pkl', 'wb') as f:
        pickle.dump(tc_list, f)
print('Done')

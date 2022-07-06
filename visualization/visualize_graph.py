"""
Creates html file with a graph of the given graph.
"""
import sys
import pickle
import numpy as np
from os import listdir
from os.path import isfile, dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from visualization import make_graph
from floydwarshall import read_dir

# Read the directory of the graph
destination_dir = 'visualization/files'
viz_unittest_dir = destination_dir + '/unit_tests'
viz_performance_test_dir = destination_dir + '/performance_tests'

# Visualize unit tests graphs
unit_tests_graphs = read_dir('tests/unit_tests/data')
for i in unit_tests_graphs:
    make_graph(i['input']).save_graph(
        f'{viz_unittest_dir}/{i["case"]}_input.html')
    make_graph(i['output']).save_graph(
        f'{viz_unittest_dir}/{i["case"]}_output.html')

# Load the performance tests data
file_path = 'tests/performance_tests/data/perf_data.pkl'
with open(file_path, 'rb') as f:
    tc_list = pickle.load(f)

# Visualize performance tests graphs
for i in tc_list:
    if np.array(i['input_graph']).ndim != 2:
        continue
    make_graph(i['input_graph']).save_graph(
        f'{viz_performance_test_dir}/{i["case"]}_input.html')
    make_graph(i['output_graph']).save_graph(
        f'{viz_performance_test_dir}/{i["case"]}_output.html')

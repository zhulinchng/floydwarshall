"""
Creates html file with a graph of the given graph.
"""
import sys
import pickle
import numpy as np
from os import listdir
from os.path import isfile, dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from floydwarshall import read_dir
from visualization import make_graph

# Read the directory of the graph
destination_dir = 'visualization/files'
viz_unittest_dir = destination_dir + '/unit_tests'
viz_performance_test_dir = destination_dir + '/performance_tests'

# Visualize unit tests graphs
unit_tests_graphs = read_dir('tests/unit_tests/data')
for i in unit_tests_graphs:
    make_graph(i['input']).save_graph(f'{viz_unittest_dir}/{i["case"]}_input.html')
    make_graph(i['output']).save_graph(f'{viz_unittest_dir}/{i["case"]}_output.html')

# Visualize performance tests graphs
folder_path = 'tests/performance_tests/data'
perf_tests_graphs = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
for graph in perf_tests_graphs:
    with open(f'{folder_path}/{graph}','rb') as f:
        graph_data = pickle.load(f)
    if np.array(graph_data).ndim != 2:
        continue
    make_graph(graph_data).save_graph(f'{viz_performance_test_dir}/{graph[:-4]}.html')
"""
Unit test functions for the floyd warshall algorithm
"""
import unittest
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from floydwarshall import fw_iterative, fw_recursive, fw_recursive_memo, read_dir


class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall_success(self):
        """
        Equality test the floyd warshall algorithm on a set of test cases
        """
        tests = read_dir('tests/unit_tests/data')
        fn_list = [fw_iterative, fw_recursive, fw_recursive_memo]
        for fn in fn_list:
            for test in tests:
                # As lists are mutable, this is to copy the input to another variable
                input_graph = [[c for c in r] for r in test['input']]
                with self.subTest(case=test['case'], fn=fn.__name__):
                    self.assertEqual(test['output'],
                                     fn(input_graph),
                                     f'Failed equality {test["case"]} with {fn.__name__}')

    def test_floyd_warshall_fail(self):
        """
        Inequality test the floyd warshall algorithm on a set of test case
        """
        tests = [{'case': 'test_1',
                  'input': [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                  'output': [[0, 2, 2], [2, 0, 2], [2, 2, 0]]}]
        fn_list = [fw_iterative, fw_recursive, fw_recursive_memo]
        for fn in fn_list:
            for test in tests:
                # As lists are mutable, this is to copy the input
                input_graph = [[c for c in r] for r in test['input']]
                with self.subTest(case=test['case'], fn=fn.__name__):
                    self.assertNotEqual(test['output'],
                                        fn(input_graph),
                                        f'Failed inequality test {test["case"]} with {fn.__name__}')


if __name__ == '__main__':
    unittest.main()

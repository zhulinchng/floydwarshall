"""Unit test functions for the floyd warshall algorithm."""
import unittest
import sys
from math import inf
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from floydwarshall import fw_iterative, fw_recursive, fw_recursive_memo


class TestFloydWarshall(unittest.TestCase):
    """Unit test functions for the floyd warshall algorithm."""

    def test_floyd_warshall_success(self):
        """Equality test the floyd warshall algorithm on a set of test cases."""
        tests = [{'case': 'case1',
                  'input': [[0.0, 25.0], [-1.0, 0.0]],
                  'output': [[0.0, 25.0], [-1.0, 0.0]]},
                 {'case': 'case2',
                  'input': [[0.0, 1.0, 43.0], [1.0, 0.0, 6.0], [-1.0, -1.0, 0.0]],
                  'output': [[0.0, 1.0, 7.0], [1.0, 0.0, 6.0], [-1.0, -1.0, 0.0]]},
                 {'case': 'case0',
                  'input': [[0.0, 5.0, inf, 10.0], [inf, 0.0, 3.0, inf], [inf, inf, 0.0, 1.0], [inf, inf, inf, 0.0]],
                  'output': [[0.0, 5.0, 8.0, 9.0], [inf, 0.0, 3.0, 4.0], [inf, inf, 0.0, 1.0], [inf, inf, inf, 0.0]]}]
        fn_list = [fw_iterative, fw_recursive, fw_recursive_memo]
        for fn in fn_list:
            for test in tests:
                with self.subTest(case=test['case'], fn=fn.__name__):
                    self.assertEqual(test['output'],
                                     fn(test['input']),
                                     f'Failed equality {test["case"]} with {fn.__name__}')

    def test_floyd_warshall_fail(self):
        """Inequality test the floyd warshall algorithm on a set of test case."""
        tests = [{'case': 'test_1',
                  'input': [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
                  'output': [[0, 2, 2], [2, 0, 2], [2, 2, 0]]}]
        fn_list = [fw_iterative, fw_recursive, fw_recursive_memo]
        for fn in fn_list:
            for test in tests:
                with self.subTest(case=test['case'], fn=fn.__name__):
                    self.assertNotEqual(test['output'],
                                        fn(test['input']),
                                        f'Failed inequality test {test["case"]} with {fn.__name__}')


if __name__ == '__main__':
    unittest.main()

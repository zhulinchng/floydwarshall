"""Package initialization file for the tests package."""
from .unit_test import TestFloydWarshall
from .performance_test import perf_test, timeit_perf_test, cprofile_perf_test
__version__ = '1.0.0'

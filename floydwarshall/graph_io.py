"""
Unit test functions for the floyd warshall algorithm
"""
import math
from os import listdir
from os.path import isfile, join


def read_graph(file_name: str) -> list:
    """
    Read the tests cases from text files separated by newlines for rows and commas for columns.
    
    :param file_name: name of the file containing the graph
    :return: list of lists representing the graph
    """
    def replace_number(input_string: str) -> float:
        """
        Replaces non-numeric characters with math.inf
        math.inf represents no paths between vertices
        :param input_string: string to be replaced
        :return: replaced string with float
        """
        try:
            return float(input_string)
        except ValueError:
            return math.inf

    def convert_to_2d_array(input_string: str) -> list:
        """
        Converts a string to a 2d array
        :param s: string to be converted
        :return: 2d array in the form of a list of lists
        """
        return [list(map(replace_number, line.split(','))) for line in input_string.splitlines()]

    with open(file_name, 'r', encoding='utf-8') as file:
        return convert_to_2d_array(file.read())


def read_dir(folder_path: str, read_graph=read_graph) -> list:
    """
    Read all the test cases from the folder directory.

    :param folder_path: folder directory containing the test cases
    :return: list of test cases list[dict]
    """
    # Get all filename in the directory
    data_files = [f for f in listdir(
        folder_path) if isfile(join(folder_path, f))]
    # Initialize the list of tests
    case_list = []
    for case in {i.split('_')[0] for i in data_files}:
        case_dict = {}
        case_dict['case'] = case
        case_dict['input'] = read_graph(join(folder_path, f'{case}_input.txt'))
        case_dict['output'] = read_graph(
            join(folder_path, f'{case}_output.txt'))
        case_list.append(case_dict)
    return case_list


def unit_test_dir(functions_list: list, case_list: list) -> None:
    """
    Run the unit test for the floyd warshall algorithm and prints the results.

    :param functions_list: list of functions to be tested
    :param case_list: list of test cases list[dict]
    :return: None
    """
    # Run the tests for all functions
    for fn in functions_list:
        print(f'Testing function {fn.__name__}')
        for case in case_list:
            # As list are mutable, we need to copy the input and output graph
            input_graph = [[c for c in r] for r in case['input']]
            output_graph = [[c for c in r] for r in case['output']]
            # Test the algorithm
            result = fn(input_graph)
            if result == output_graph:
                print(f'\to Passed {case["case"]}')
            else:
                print(f'\tx Failed {case["case"]}')
                print(f'\t\tExpected: {output_graph}')
                print(f'\t\tGot: {result}')

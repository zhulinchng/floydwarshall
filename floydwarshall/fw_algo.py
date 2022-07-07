"""Python implementation of the Floyd-Warshall algorithm."""
import itertools


def fw_iterative(input_graph: list) -> list:
    """
    Iterate over all pairs of vertices and update the shortest path between all pairs of vertices.

    Assumes input graph with NO negative cycles.

    :param distance: list of lists representing the distance between all pairs of vertices
    :return: shortest distance matrix (distance[i][j] = distance between vertex i and j)
    """
    # Initialize variables
    # List of lists are mutable, this is to copy the input
    distance = [row[:] for row in input_graph]
    size_range = range(len(distance))
    # Loop over all pairs of vertices
    for intermediate, start_node, end_node in itertools.product(size_range, size_range, size_range):
        if start_node == end_node:
            distance[start_node][end_node] = 0
        else:
            # assign the path with the minimum distance
            distance[start_node][end_node] = min(
                distance[start_node][end_node],
                distance[start_node][intermediate] + distance[intermediate][end_node])
    return distance


def fw_recursive(input_graph: list) -> list:
    """
    Recursively update the minimum path between all pairs of vertices.

    Assumes input graph with NO negative cycles.

    :param graph: list of lists representing the distance between all pairs of vertices
    :return: minimum distance matrix (distance[i][j] = distance between vertex i and j)
    """
    # Initialize variables
    # List of lists are mutable, this is to copy the input
    graph = [row[:] for row in input_graph]
    size = len(graph)
    size_range = range(size)

    def min_path(source: int, target: int, depth: int) -> int:
        """
        Recursively obtain the minimum path between two vertices.

        :param source: starting node
        :param target: target node
        :param depth: depth of the recursion/traversion, also act as intermediate node
        :return: minimum distance between source and target
        """
        if depth < 0:
            return graph[source][target]
        return min(min_path(source, target, depth-1),
                   min_path(source, depth, depth-1)+min_path(depth, target, depth-1))
    # Loop over all pairs of vertices
    for row, column in itertools.product(size_range, size_range):
        if row == column:
            graph[row][column] = 0
        else:
            graph[row][column] = min_path(row, column, size-1)
    return graph


def fw_recursive_memo(input_graph: list) -> list:
    """
    Recursively update with memoization the minimum path between all pairs of vertices.

    Assumes input graph with NO negative cycles.

    :param graph: list of lists representing the distance between all pairs of vertices
    :return: minimum distance matrix (distance[i][j] = distance between vertex i and j)
    """
    # Initialize variables
    # List of lists are mutable, this is to copy the input
    graph = [row[:] for row in input_graph]
    size = len(graph)
    size_range = range(size)
    memo = {}

    def min_path(source: int, target: int, depth: int, memo: dict) -> int:
        """
        Recursively obtain the minimum path between two vertices with memoization.

        :param source: starting node
        :param target: target node
        :param depth: depth of the recursion/traversion, also act as intermediate node
        :param memo: memoization table
        :return: minimum distance between source and target
        """
        if (source, target, depth) in memo:
            return memo[(source, target, depth)]
        memo[(source, target, depth)] = min(min_path(source, target, depth-1, memo),
                                            min_path(source, depth,
                                                     depth-1, memo)
                                            + min_path(depth, target, depth-1, memo))
        return memo[(source, target, depth)]
    # Initialize memoization table with default values
    for source, target in itertools.product(size_range, size_range):
        # -1 represents the input distance from the graph
        memo[(source, target, -1)] = graph[source][target]
    # Loop over all pairs of vertices
    for row, column in itertools.product(size_range, size_range):
        if row == column:
            graph[row][column] = 0
        else:
            graph[row][column] = min_path(row, column, size-1, memo)
    return graph

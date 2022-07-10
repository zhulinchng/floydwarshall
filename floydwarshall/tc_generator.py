"""Generates a random graph with the given size and edge probability."""
import random
import math
import itertools


def graph_generator(size: int = 5,
                    edgeprob: float = 0.8,
                    minval: float = 0,
                    maxval: float = 100,
                    seed: float = None) -> list:
    """
    Generate a random graph with the given size and edge probability.

    :param size: number of vertices
    :param edgeprob: probability of an edge between two vertices
    :param minval: minimum value of the edge weight
    :param maxval: maximum value of the edge weight
    :param seed: seed for the random generator
    :return: list of lists representing the distance between all pairs of vertices
    """
    # Initialize variables
    if seed is not None:
        random.seed(seed)
    graph = []
    size_range = range(size)
    # Generate graph
    for i in size_range:
        # Initialize row
        rowlist = []
        # Loop over all vertices in row
        for j in size_range:
            if i == j:
                # Set diagonal to 0
                rowlist.append(0)
            else:
                # Generate random value
                if edgeprob > random.random():
                    rowlist.append(random.randint(minval, maxval))
                else:
                    # Set edge to infinity
                    rowlist.append(math.inf)
        graph.append(rowlist)
    return graph


def fw_iterative_mod(input_graph: list) -> list:
    """
    Iterate over all pairs of vertices and update the shortest path between all pairs of vertices.

    :param distance: list of lists representing the distance between all pairs of vertices
    :return: shortest distance matrix (distance[i][j] = distance between vertex i and j)
    """
    # Initialize variables
    distance = [row[:] for row in input_graph]
    size_range = range(len(distance))
    # Loop over all pairs of vertices
    for intermediate, start_node, end_node in itertools.product(size_range, size_range, size_range):
        # assign the path with the minimum distance
        distance[start_node][end_node] = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node])
    return distance


def negative_loop_checker(graph: list, func=fw_iterative_mod) -> list:
    """
    Check if the graph has negative cycles using the Floyd-Warshall algorithm.

    If the graph has negative cycles,
    the diagonal of the graph that the algorithm will be different from the input graph.

    :param graph: list of lists representing the distance between all pairs of vertices
    :return: False if there is a negative cycle, True otherwise
    """
    # As list are mutable, we need to copy the graph
    output_graph = func(graph)
    # compare the diagonal of the output graph with the original graph
    for i, _ in enumerate(output_graph):
        if output_graph[i][i] < 0:
            return False
    return True

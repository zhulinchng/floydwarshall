"""
Functions to visualize a given graph.

Usage example:
make_graph(graph).show('example1.html')
make_graph(graph).save_graph('example2.html')
"""
from pyvis.network import Network
import networkx as nx
import numpy as np
import math


def make_graph(input_graph: list,
               shape: str = 'box',
               gravity: int = -2500,
               central_gravity: float = 0.5,
               physics: bool = True,
               overlap: float = 1,
               maxvalue: float = math.inf,
               mass: float = 1.8) -> Network:
    """
    Generates a pyvis network graph from a list of lists representing the distance between all pairs of vertices.

    :param input_graph: list of lists representing the distance between all pairs of vertices
    :param shape: shape of the nodes
    :param gravity: gravity of the nodes
    :param central_gravity: central gravity of the nodes
    :param physics: physics of the nodes
    :param overlap: overlap of the nodes
    :param maxvalue: maximum value of the nodes
    :param mass: mass of the nodes
    :return: pyvis network graph
    """

    def make_nxgraph(input_graph: list) -> nx.Graph:
        """
        Generates a networkx graph from a list of lists representing the distance between all pairs of vertices.

        :param input_graph: list of lists representing the distance between all pairs of vertices
        :return: networkx graph
        """
        G = nx.from_numpy_matrix(
            np.array(input_graph), create_using=nx.MultiDiGraph())
        labels2 = [(i, j, input_graph[i][j]) for i, j in G.edges()]
        G.add_weighted_edges_from(ebunch_to_add=labels2)
        return G

    # Validate graph to be a 2d list with np.dim
    if np.array(input_graph).ndim != 2:
        raise ValueError('Graph must be a 2d list')
    # Initialize variables
    net = Network(height='100%', width='100%', directed=True)
    # Generate networkx graph
    G = make_nxgraph(input_graph)
    # Generate pyvis network graph
    net.from_nx(G)
    # Set graph properties
    labels = [i for i in G.nodes()]
    labels2 = {(i, j): input_graph[i][j] for i, j in G.edges()}
    for i in labels:
        net.get_node(i)['label'] = 'Node '+str(i)
        net.get_node(i)['shape'] = shape
        net.get_node(i)['mass'] = mass
        net.get_node(i)['physics'] = physics
    net.edges = []
    for f, t in labels2:
        if labels2[(f, t)] < maxvalue:
            net.add_edge(f, t, label=str(labels2[(f, t)]))
    net.barnes_hut(gravity=gravity, central_gravity=central_gravity, spring_length=250,
                   spring_strength=0.001, damping=0.09, overlap=overlap)
    return net

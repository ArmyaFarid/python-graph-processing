import networkx as nx
import matplotlib.pyplot as plt
from graph.graph import Graph
import numpy as np
from matplotlib.patches import FancyArrowPatch
import pandas as pd


matrix_for_belman = [
    [float('inf'), 3, 2, float('inf'), float('inf'), float('inf'), float('inf'), ],
    [float('inf'), float('inf'), -2, 2, 2, float('inf'), float('inf'), ],
    [float('inf'), float('inf'), float('inf'), 4, float('inf'), 2, float('inf'), ],
    [float('inf'), float('inf'), float('inf'), float('inf'), 1, -1, float('inf'), ],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 3, ],
    [float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 4, ],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), ]
]

graph = Graph(len(matrix_for_belman), matrix_for_belman)
data = [[0, 4, 6], [3, 4, 8], [2, 3, 6], [5, 0, 5], [1, 5, 4]]


def draw_spanning_tree_graph(edges_lit):
    data = edges_lit
    # create a directed graph
    G = nx.DiGraph()

    # add edges and weights to the graph
    for row in data:
        origin = row[0]
        destination = row[1]
        weight = row[2]
        G.add_edge(origin, destination, weight=weight)

    # draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_labels(G, pos)
    plt.show()


def display_edges_as_table(edges_lit, is_weighted=True):
    data = edges_lit
    print("| Origin | Destination | Weight |")
    print("|--------|-------------|--------|")
    for row in data:
        origin = row[0]
        destination = row[1]
        weight = row[2] if is_weighted else None
        print(f"|   {origin}    |     {destination}      |   {weight}   |")

def display_adjacency_matrix_as_table(adj_matrix):
    n = len(adj_matrix)
    print("   ", end="")
    for i in range(n):
        print(f"{i:3d}", end="")
    print()
    print("  ┌" + "───" * n + "┐")
    for i in range(n):
        print(f"{i:2d}│", end="")
        for j in range(n):
            if adj_matrix[i][j] == float('inf'):
                print(" n ", end="")
            else:
                print(f"{adj_matrix[i][j]:3d}", end="")
        print(" │")
    print("  └" + "───" * n + "┘")


def display_edges_with_arrow(edges_lit, is_weighted=True):
    data = edges_lit
    for row in data:
        origin = row[0]
        destination = row[1]
        weight = row[2] if is_weighted else None
        print(f"|   {origin}    --->     {destination}     :(  {weight} )  |")


def draw_graph_from_edges_oriented(edges_list):
    data = edges_list

    # create a directed graph
    G = nx.DiGraph()

    # add edges and weights to the graph
    for row in data:
        origin = row[0]
        destination = row[1]
        weight = row[2]
        G.add_edge(origin, destination, weight=weight)

    # draw the graph
    pos = nx.spring_layout(G, scale=0.3)

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_labels(G, pos)
    plt.show()


def draw_graph_from_edges_oriented_with_label(edges_list, nodes_labels):
    data = edges_list
    # create a directed graph
    G = nx.DiGraph()

    # add edges and weights to the graph
    for row in data:
        origin = row[0]
        destination = row[1]
        # weight = row[2]
        G.add_edge(origin, destination)

    # draw the graph
    pos = nx.spring_layout(G, scale=0.3)
    # map node labels to string values
    labels = {i: str(nodes_labels[i]) for i in range(len(nodes_labels))}
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_labels(G, pos, labels=labels)
    plt.show()


def draw_graph_from_edges_non_oriented(edges_list):
    # create an undirected graph
    G = nx.Graph()

    # add edges and weights to the graph
    for edge in edges_list:
        origin = edge[0]
        destination = edge[1]
        weight = edge[2]
        G.add_edge(origin, destination, weight=weight)

    # draw the graph
    pos = nx.spring_layout(G, scale=0.3)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    nx.draw_networkx_labels(G, pos)
    plt.show()



def print_adjacency_matrix(adj_matrix):
    df = pd.DataFrame(adj_matrix)
    df.index.name = ""
    df.columns.name = ""
    print(df.to_string())

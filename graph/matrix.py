import numpy as np


def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def get_matrix_from_user(n, separator):
    n = int(input("Enter the number of nodes in the graph: "))

    # Initialize the adjacency matrix with None values
    adj_matrix = [[None for i in range(n)] for j in range(n)]

    # Read the adjacency matrix from user input
    for i in range(n):
        row = input(f"Enter the values for node {i + 1}, separated by commas (use 'nan' for missing values): ")
        row_values = row.split(",")
        for j in range(n):
            print(row_values[j])
            row_values[j] = row_values[j].replace(" ", "")
            if row_values[j].isnumeric():
                adj_matrix[i][j] = int(row_values[j])
            else:
                adj_matrix[i][j] = float('inf')

    return adj_matrix


def print_matrix(adj_matrix):
    n = len(adj_matrix)
    # Print the adjacency matrix
    print("Adjacency Matrix:")
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] is None:
                print("None", end="\t")
            else:
                print(adj_matrix[i][j], end="\t")
        print()


def to_binary_matrix(val_matrix):
    # Nombre de lignes et de colonnes de la matrice valuée
    num_rows = len(val_matrix)
    num_cols = len(val_matrix[0])

    # Initialisation de la matrice binaire
    bin_matrix = [[0] * num_cols for i in range(num_rows)]

    # Remplissage de la matrice binaire
    for i in range(num_rows):
        for j in range(num_cols):
            if val_matrix[i][j] != float('inf'):
                bin_matrix[i][j] = 1

    return bin_matrix


def get_edges_from_matrix(matrix, is_weighted=True):
    graph_edges = []
    adj_matrix = matrix
    n = len(matrix)
    if is_weighted:
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] != float('inf'):
                    graph_edges.append([i, j, adj_matrix[i][j]])
    else:
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] != float('inf'):
                    graph_edges.append([i, j ])
    return graph_edges

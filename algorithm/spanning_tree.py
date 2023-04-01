import sys


def has_cycle(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if dfs(adj_matrix, i, visited, -1):
                return True
    return False


def dfs(adj_matrix, v, visited, parent):
    visited[v] = True
    for i in range(len(adj_matrix)):
        if adj_matrix[v][i] == 1:
            if not visited[i]:
                if dfs(adj_matrix, i, visited, v):
                    return True
            elif i != parent:
                return True
    return False


def generate_adjacency_matrix(n, edges):
    matrix = [[0] * n for _ in range(n)]
    for edge in edges:
        i, j, w = edge
        matrix[i - 1][j - 1] = 1
        matrix[j - 1][i - 1] = 1
    return matrix


class Kruskal:
    def __init__(self, graph_matrix, size):
        self.size = size
        self.graph_matrix = graph_matrix
        self.graph_edges = []
        self.extract_edges_from_matrix()

    def add_edge(self, u, v, w):
        self.graph_edges.append([u, v, w])

    def extract_edges_from_matrix(self):
        for i in range(len(self.graph_matrix)):
            for j in range(i + 1, len(self.graph_matrix)):
                if self.graph_matrix[i][j] != float('inf'):
                    self.add_edge(i, j, self.graph_matrix[i][j])

    def is_containing_cycles(self, edges_involved, x, y):
        edges = edges_involved
        matrixtest = generate_adjacency_matrix(self.size, edges)
        return has_cycle(matrixtest)

    def kruskal_algo(self, _type):
        is_reverse = False
        if _type == "max":
            is_reverse = True

        graph_edges = sorted(self.graph_edges, key=lambda item: item[2], reverse=is_reverse)

        result_spanning_edge = []
        node_involved = set()

        for edge in graph_edges:
            result_spanning_edge.append(edge)
            if not self.is_containing_cycles(result_spanning_edge, edge[0], edge[1]):
                node_involved.add(edge[0])
                node_involved.add(edge[1])
            else:
                result_spanning_edge.pop()

        return result_spanning_edge

    def get_spanning_tree(self, _type):
        return self.kruskal_algo(_type)


class Prim:

    def __init__(self, graph_matrix, size):
        self.size = size
        self.graph_matrix = graph_matrix

    def get_spanning_tree(self, _type):
        if _type == "max":
            return self.prim_algo_max()
        return self.prim_algo_min()

    def prim_algo_max(self):
        graph_size = self.size
        nodes = [False] * graph_size
        tree_edges = []
        starting_node = 0
        max_weight = -sys.maxsize
        max_index = None
        for i in range(graph_size):
            if self.graph_matrix[starting_node][i] > max_weight and self.graph_matrix[starting_node][i] != float('inf'):
                max_weight = self.graph_matrix[starting_node][i]
                max_index = i
        nodes[starting_node] = True
        nodes[max_index] = True
        tree_edges.append([starting_node, max_index, max_weight])

        while all(nodes) is False:
            max_weight = -sys.maxsize
            origin_index = None
            destination_index = None
            for j in range(graph_size):
                if nodes[j]:
                    for i in range(graph_size):
                        if not nodes[i] and self.graph_matrix[i][j] != float('inf'):
                            if self.graph_matrix[i][j] > max_weight:
                                origin_index = i
                                destination_index = j
                                max_weight = self.graph_matrix[origin_index][destination_index]
            if max_weight is not float('inf'):
                new_tree_edge = [origin_index, destination_index, max_weight]
                nodes[origin_index] = True
                tree_edges.append(new_tree_edge)

        return tree_edges

    def prim_algo_min(self):
        graph_size = self.size
        nodes = [False] * graph_size
        tree_edges = []
        starting_node = 0

        min_weight = sys.maxsize
        min_index = None
        for i in range(graph_size):
            if self.graph_matrix[starting_node][i] < min_weight and self.graph_matrix[starting_node][i] != float('inf'):
                min_weight = self.graph_matrix[starting_node][i]
                min_index = i

        nodes[starting_node] = True
        nodes[min_index] = True
        tree_edges.append([starting_node, min_index, min_weight])
        # breakpoint()
        while all(nodes) is False:
            min_weight = sys.maxsize
            origin_index = None
            destination_index = None
            for j in range(graph_size):
                if nodes[j]:
                    for i in range(graph_size):
                        if not nodes[i] and self.graph_matrix[i][j] != float('inf'):
                            if self.graph_matrix[i][j] < min_weight:
                                origin_index = i
                                destination_index = j
                                min_weight = self.graph_matrix[origin_index][destination_index]
            if min_weight is not float('inf'):
                new_tree_edge = [origin_index, destination_index, min_weight]
                nodes[origin_index] = True
                tree_edges.append(new_tree_edge)
        return tree_edges


def max_key_index(key, mst_set):
    # Initialisation des valeurs minimales
    max = -sys.maxsize
    max_index = None

    # Parcourir toutes les clés pour trouver la valeur maximale
    for i in range(len(key)):
        if mst_set[i] == False and key[i] > max:
            max = key[i]
            max_index = i

    return max_index

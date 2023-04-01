from pprint import pprint
import algorithm.shortest_path as sp
import graph.matrix as matrix_utility
import algorithm.connexity as con
import algorithm.spanning_tree as spanning_algo


class Graph:
    def __init__(self, size, matrix):
        self.graph_edges = []
        self.size = size
        self.matrix = matrix
        self.binary_matrix = matrix_utility.to_binary_matrix(self.matrix)
        self.fill_edges()
        self.type = self.get_type()
        self.kruskal = spanning_algo.Kruskal(self.matrix, self.size)
        self.prim = spanning_algo.Prim(self.matrix, self.size)
        self.topo = con.TopologicalSort(self.matrix)

    def get_type(self):
        if matrix_utility.is_symmetric(self.matrix):
            return "unordered"
        else:
            return "ordered"

    def get_matrix(self):
        return self.matrix

    def fill_edges(self):
        adj_matrix = self.matrix
        n = self.size
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] != float('inf'):
                    self.graph_edges.append([i, j, adj_matrix[i][j]])

    def is_connexe(self):
        return con.dfs_perso(matrix_utility.to_binary_matrix(self.matrix), 0)

    def has_cycle(self):
        graph = self.matrix
        n = len(graph)
        visited = [False] * n
        stack = [False] * n

        def has_cycle_util(u):
            visited[u] = True
            stack[u] = True

            for v in range(n):
                if graph[u][v] != float('inf'):
                    if not visited[v]:
                        if has_cycle_util(v):
                            return True
                    elif stack[v]:
                        return True

            stack[u] = False
            return False

        for u in range(n):
            if not visited[u]:
                if has_cycle_util(u):
                    return True

        return False

    def has_negative_weight(self):
        graph = self.matrix
        for row in graph:
            for value in row:
                if value < 0:
                    return True
        return False

    def kruskal_mst(self, _type="min"):
        return self.kruskal.get_spanning_tree("_type")

    def get_spanning_tree(self, _type="max"):
        return self.prim.get_spanning_tree(_type)

    def get_scc(self):
        kosaraju = con.Kosaraju(matrix_utility.to_binary_matrix(self.matrix), self.size)
        return kosaraju.getscc()

    def get_root(self):
        this_matrix = matrix_utility.to_binary_matrix(self.matrix)
        return con.find_root_vertex(this_matrix)

    def add_value_to_edges(self, edges):
        edges_copie = edges
        for edge in edges_copie:
            edge.append(self.matrix[edge[0]][edge[1]])
        return edges_copie

    def get_shortest_tree(self, _type, root):
        if _type == 'BELLMAN':
            if self.has_cycle():
                raise ValueError("Contient un cycle")
            bm = sp.Bellman(self.matrix)
            return bm.bellman(root)
        if _type == 'DIJKSTRA':
            print(self.matrix)
            if self.has_negative_weight():
                raise ValueError("Poids negatif")
            dij = sp.Dijkstra(self.matrix)
            return dij.dijkstra2(root)
        if _type == 'BELLMANFORD':
            bm = sp.Bellman(self.matrix)
            return bm.bellman_ford2(root)

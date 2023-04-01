import heapq
import math
import numpy as np


# def bellman(matrice_adjacence, start):
#     # Nombre de sommets
#     nb_sommets = len(matrice_adjacence)
#
#     # Initialisation
#     pi = [float('inf')] * nb_sommets
#     pi[start] = 0
#     Z = {start}
#     A = set()
#
#     # Algorithme de Bellman
#     while len(Z) != nb_sommets:
#         # Recherche du sommet x à ajouter à Z
#         min_pi = float('inf')
#         min_x = None
#         for x in range(nb_sommets):
#             if x not in Z:
#                 pi_pred = [pi[i] for i in range(nb_sommets) if matrice_adjacence[i][x] != float('inf')]
#                 if all(p in Z for p in pi_pred):
#                     pi_x = min(pi_pred) + min(
#                         matrice_adjacence[i][x] for i in range(nb_sommets) if matrice_adjacence[i][x] != float('inf'))
#                     if pi_x < min_pi:
#                         min_pi = pi_x
#                         min_x = x
#
#         # Ajout du sommet x à Z
#         Z.add(min_x)
#         pi[min_x] = min_pi
#
#         # Ajout de l'arc dans A
#         for i in range(nb_sommets):
#             if matrice_adjacence[i][min_x] != float('inf') and pi[i] + matrice_adjacence[i][min_x] == min_pi:
#                 A.add((i, min_x))
#     return A

def bellman(matrice_adjacence, start):
    # Nombre de sommets
    nb_sommets = len(matrice_adjacence)

    # Initialisation
    pi = [float('inf')] * nb_sommets
    pi[start] = 0
    Z = {start}
    A = set()

    # Algorithme de Bellman
    while len(Z) != nb_sommets:
        print(Z)
        # Recherche du sommet x à ajouter à Z
        min_pi = float('inf')
        min_x = start
        for x in range(nb_sommets):
            if x not in Z:
                pi_pred = [pi[i] for i in range(nb_sommets) if matrice_adjacence[i][x] != float('inf')]
                if all(p in Z for p in pi_pred):
                    pi_x = min(pi_pred) + min(
                        matrice_adjacence[i][x] for i in range(nb_sommets) if matrice_adjacence[i][x] != float('inf'))
                    if pi_x < min_pi:
                        min_pi = pi_x
                        min_x = x

        # Ajout du sommet x à Z
        Z.add(min_x)
        pi[min_x] = min_pi

        # Ajout de l'arc dans A
        for i in range(nb_sommets):
            if matrice_adjacence[i][min_x] != float('inf') and pi[i] + matrice_adjacence[i][min_x] == min_pi:
                A.add((i, min_x))
    return A


def has_negative_weight(graph):
    for row in graph:
        for value in row:
            if value < 0:
                return True
    return False


class Bellman:

    def __init__(self, graph):
        self.graph = graph

    def bellman(self, root):
        graph = self.graph
        n = len(graph)
        visited = [False] * n
        A = []  # contient les arc de l'arboressence
        pi = [float('inf')] * n  # initialisation de pi

        # initialisation
        pi[root] = 0
        visited[root] = True
        Z = {root}

        # parcourir tanque tous les sommets ne sont pas traite
        while all(visited) is not True:
            for x in range(n):
                if not visited[x]:
                    preds = []
                    for j in range(n):
                        if graph[j][x] != float('inf'):
                            preds.append(j)

                    if set(preds).issubset(Z):
                        min = +math.inf
                        i_min = None
                        for i in preds:
                            if (pi[i] + graph[i][x]) < min:
                                min = pi[i] + graph[i][x]
                                i_min = i
                        pi[x] = min
                        A.append([i_min, x])
                        visited[x] = True
                        Z.add(x)
        return A

    def bellman_ford2(self, s):
        matrix = self.graph
        n = len(matrix)
        d = np.full(n, np.inf)
        d[s] = 0
        pi = np.zeros(n, dtype=int)
        pi[s] = -1
        for i in range(n - 1):
            for j in range(n):
                for k in range(n):
                    if matrix[k][j] != 0 and d[k] + matrix[k][j] < d[j]:
                        d[j] = d[k] + matrix[k][j]
                        pi[j] = k
        tree = []
        for i in range(n):
            if pi[i] != -1:
                tree.append([pi[i], i])
        return tree


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, root):
        graph = self.graph
        n = len(graph)
        visited = [False] * n
        distances = [float('inf')] * n
        parent = [-1] * n
        distances[root] = 0

        pq = [(0, root)]

        while pq:
            (dist, node) = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True

            for neighbor in range(n):
                if graph[node][neighbor] != float('inf'):
                    new_dist = dist + graph[node][neighbor]
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        parent[neighbor] = node
                        heapq.heappush(pq, (new_dist, neighbor))

        return parent, distances

    def dijkstra2(self, root):
        matrix = self.graph
        n = len(matrix)
        dist = [float('inf')] * n
        dist[root] = 0
        prev = [None] * n
        visited = [False] * n
        heap = [(0, root)]
        while heap:
            (d, u) = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v in range(n):
                if matrix[u][v] != float('inf'):
                    alt = dist[u] + matrix[u][v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        heapq.heappush(heap, (dist[v], v))
        arcs = []
        for i in range(n):
            if prev[i] is not None:
                arcs.append([prev[i], i])
        return arcs

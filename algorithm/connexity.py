import numpy as np


def dfs_perso(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in range(len(graph[vertex])):
                if graph[vertex][neighbor] and neighbor not in visited:
                    stack.append(neighbor)
    return len(visited) == len(graph)


def tarjan_strongly_connected_components(adj_matrix):
    """
    Vérifie si le graphe représenté par la matrice d'adjacence est fortement connexe en utilisant l'algorithme de Tarjan.
    Si le graphe n'est pas fortement connexe, retourne le graphe réduit.
    :param adj_matrix: matrice d'adjacence représentant le graphe orienté
    :return: la matrice d'adjacence du graphe réduit si le graphe n'est pas fortement connexe, None sinon
    """
    n = len(adj_matrix)
    index_counter = [0]
    lowlink = [-1] * n
    index = [-1] * n
    on_stack = [False] * n
    stack = []

    def strongconnect(v):
        index[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True

        for w in range(n):
            if adj_matrix[v][w] != 0:
                if index[w] == -1:
                    strongconnect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif on_stack[w]:
                    lowlink[v] = min(lowlink[v], index[w])

        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            if len(scc) == 1:
                return
            scc_matrix = [[0] * len(scc) for _ in range(len(scc))]
            for i in range(len(scc)):
                for j in range(len(scc)):
                    scc_matrix[i][j] = adj_matrix[scc[i]][scc[j]]
            scc_adj_matrix = tarjan_strongly_connected_components(scc_matrix)
            if scc_adj_matrix is not None:
                for i in range(n):
                    if i not in scc:
                        for j in range(n):
                            if j not in scc:
                                adj_matrix[i][j] = scc_adj_matrix[i][j]

    for i in range(n):
        if index[i] == -1:
            strongconnect(i)

    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] != adj_matrix[j][i]:
                return adj_matrix

    return None


def tarjan_algorithm(adj_matrix):
    n = len(adj_matrix)
    index_counter = [0]
    lowlink = [-1] * n
    index = [-1] * n
    on_stack = [False] * n
    stack = []
    scc = []

    def strongconnect(node):
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        on_stack[node] = True

        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1:
                if index[neighbor] == -1:
                    strongconnect(neighbor)
                    lowlink[node] = min(lowlink[node], lowlink[neighbor])
                elif on_stack[neighbor]:
                    lowlink[node] = min(lowlink[node], index[neighbor])

        if lowlink[node] == index[node]:
            scc_component = []
            while True:
                neighbor = stack.pop()
                on_stack[neighbor] = False
                scc_component.append(neighbor)
                if neighbor == node:
                    break
            scc.append(scc_component)

    for node in range(n):
        if index[node] == -1:
            strongconnect(node)

    return scc


def tarjan(graph):
    V = len(graph)
    visited = [False] * V
    disc = [float("inf")] * V
    low = [float("inf")] * V
    stackMember = [False] * V
    result = []

    def tarjanUtil(u):
        nonlocal time
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1
        stack.append(u)
        stackMember[u] = True

        for v in range(V):
            if graph[u][v] != 0:
                if not visited[v]:
                    tarjanUtil(v)
                    low[u] = min(low[u], low[v])
                elif stackMember[v]:
                    low[u] = min(low[u], disc[v])

        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = stack.pop()
                stackMember[w] = False
                result.append(w)

    time = 0
    stack = []

    for u in range(V):
        if not visited[u]:
            tarjanUtil(u)

    return result


class Kosaraju:
    def __init__(self, graph, size):
        self.graph = graph
        self.size = size

    def dfs(self, graph, start, visited, output):
        visited[start] = True
        for i in range(len(graph[start])):
            if graph[start][i] != 0 and not visited[i]:
                self.dfs(graph, i, visited, output)
        output.append(start)

    def getscc(self):
        graph = self.graph
        V = len(graph)

        # première passe dfs
        visited = [False] * V
        stack = []
        for i in range(V):
            if not visited[i]:
                self.dfs(graph, i, visited, stack)

        # renverser le graphe
        reversed_graph = [[0] * V for _ in range(V)]
        for i in range(V):
            for j in range(V):
                reversed_graph[i][j] = graph[j][i]

        # deuxième passe dfs
        visited = [False] * V
        scc = []
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                self.dfs(reversed_graph, v, visited, component)
                scc.append(component)

        return scc

    # def transpose(self, graph):
    #     n = len(graph)
    #     transposed_graph = [[float('inf')] * n for _ in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             if graph[i][j] != float('inf'):
    #                 transposed_graph[j][i] = graph[i][j]
    #     return transposed_graph
    #
    # def find_root_vertex(self):
    #     # Step 1: Find strongly connected components
    #     graph = self.graph
    #     n = len(graph)
    #     visited = [False] * n
    #     stack = []
    #     for u in range(n):
    #         if not visited[u]:
    #             self.dfs(graph, u, visited, stack)
    #
    #     transposed_graph = self.transpose(graph)
    #     visited = [False] * n
    #     scc = []
    #     while stack:
    #         u = stack.pop()
    #         if not visited[u]:
    #             component = []
    #             self.dfs(transposed_graph, u, visited, component)
    #             scc.append(component)
    #     # Step 2: Check if graph has multiple SCCs
    #     if len(scc) > 1:
    #         return None
    #
    #     # Step 3: Check if SCC has a cycle
    #     root = scc[0][0]
    #     visited = [False] * n
    #     stack = [(root, -1)]
    #     while stack:
    #         u, parent = stack.pop()
    #         visited[u] = True
    #         for v in range(n):
    #             if graph[u][v] != float('inf') and v != parent:
    #                 if visited[v]:
    #                     return None
    #                 stack.append((v, u))
    #
    #     # Step 4: Return root vertex
    #     return root


class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph

    def topological_sort(self, graph):
        n = len(graph)
        in_degree = [0] * n
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0:
                    in_degree[j] += 1
        queue = []
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        visited = []
        while queue:
            node = queue.pop(0)
            visited.append(node)
            for i in range(n):
                if graph[node][i] != 0:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)
        return visited

    def find_root_vertex(self):
        graph = self.graph
        print(graph)
        n = len(graph)
        # Calcul du tri topologique
        topological_order = self.topological_sort(graph)

        # Initialisation des distances et des prédécesseurs
        distance = [float('inf')] * n
        predecessor = [-1] * n
        # La racine est le sommet qui a une distance de 0
        print(topological_order)
        breakpoint()
        root_vertex = topological_order[0]
        distance[root_vertex] = 0
        # Parcours des sommets dans l'ordre topologique
        for u in topological_order:
            for v in range(n):
                if graph[u][v] != 0:
                    new_distance = distance[u] + graph[u][v]
                    if new_distance < distance[v]:
                        distance[v] = new_distance
                        predecessor[v] = u
        return root_vertex


# fonction pour réduire le graphe
def get_reduce_graph_matrix_from_reduced_graph_edges(adj_matrix, conn_comps):
    adj_matrix = np.array(adj_matrix)
    reduced_matrix = np.zeros((len(conn_comps), len(conn_comps)))
    for i, comp1 in enumerate(conn_comps):
        for j, comp2 in enumerate(conn_comps):
            # parcourir tous les sommets de chaque composante connexe
            for v1 in comp1:
                for v2 in comp2:
                    # si il existe une arête entre la composante 1 et la composante 2
                    if adj_matrix[v1][v2]:
                        reduced_matrix[i][j] = 1
                        break
                if reduced_matrix[i][j] == 1:
                    break
    return reduced_matrix


def reduce_graph_matrix(adj_matrix, components):
    n = len(components)
    reduced_matrix = np.zeros((n, n))
    adj_matrix = np.array(adj_matrix)

    for i, comp_i in enumerate(components):
        for j, comp_j in enumerate(components):
            if i == j:
                # self-edges have weight 0
                reduced_matrix[i, j] = 0
                continue
            for node_i in comp_i:
                for node_j in comp_j:
                    if adj_matrix[node_i, node_j] != float('inf'):
                        reduced_matrix[i, j] = 1
                        break
                if reduced_matrix[i, j] == 1:
                    break
    return reduced_matrix


def find_root_vertex(adj_matrix):
    # Step 1: Verify that the graph is directed
    n = len(adj_matrix)
    for i in range(n):
        if len(adj_matrix[i]) != n:
            raise ValueError("Adjacency matrix must be square")
        for j in range(n):
            if adj_matrix[i][j] not in [0, 1]:
                raise ValueError("Adjacency matrix must only contain 0's and 1's")

    # Step 2: Find all incoming vertices
    incoming = []
    for j in range(n):
        if all(adj_matrix[i][j] == 0 for i in range(n)):
            incoming.append(j)

    # Step 3: Check if any incoming vertex is also a root vertex
    for i in incoming:
        is_root_vertex = True
        for j in range(n):
            if adj_matrix[j][i] != 0:
                is_root_vertex = False
                break
        if is_root_vertex:
            return i

    # Step 4: If no root vertex was found, return None
    return None

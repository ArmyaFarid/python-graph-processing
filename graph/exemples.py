import random
import numpy as np


def generate_random_non_oriented_graph(n):
    n = 5  # nombre de sommets
    max_weight = 10  # poids maximum d'une arête

    # initialisation de la matrice d'adjacence à inf (non-connexion)
    adj_matrix = [[float('inf')] * n for i in range(n)]

    # boucle pour ajouter les arêtes (symétriques dans un graphe non-orienté)
    for i in range(n):
        for j in range(i + 1, n):
            if random.randint(0, 1):  # 50% de chance d'avoir une arête
                weight = random.randint(1, max_weight)  # poids aléatoire
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight
    return adj_matrix


def generate_random_non_oriented_connex_graph(num_nodes, probability):
    # Crée une matrice carrée de taille num_nodes x num_nodes remplie de float('inf')
    adj_matrix = np.full((num_nodes, num_nodes), float('inf'))
    is_connex = False
    if probability == 0:
        probability = 0.5
        is_connex = True

    # Génère les poids au hasard pour les connexions entre les nœuds
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if np.random.random() < probability:
                weight = np.random.randint(-11, 11)  # Génère un poids entier aléatoire entre 1 et 10
                adj_matrix[i][j] = weight
                adj_matrix[j][i] = weight

    if is_connex:
        # Divise le graphe en deux composants connexes distincts
        if np.random.random() < 0.5:
            mid = int(num_nodes / 2)
            adj_matrix[mid:, :mid] = float('inf')
            adj_matrix[:mid, mid:] = float('inf')

    return adj_matrix


def generate_random_oriented_strongly_connected_graph(num_nodes, probability):
    # Crée une matrice carrée de taille num_nodes x num_nodes remplie de float('inf')
    adj_matrix = np.full((num_nodes, num_nodes), float('inf'))

    # Si probability == 0, génération d'un graphe non-connexe
    if probability == 0:
        # Nombre de composantes connexes
        num_components = np.random.randint(2, num_nodes)
        # Génère une permutation aléatoire des nœuds
        nodes = np.random.permutation(num_nodes)
        # Nombre de nœuds par composante connexe
        component_size = num_nodes // num_components
        # Ajuste le nombre de nœuds si nécessaire
        if num_nodes % num_components != 0:
            component_size += 1
        # Indice de début de chaque composante connexe
        component_start = 0
        # Génère un sous-graphe connexe pour chaque composante
        for i in range(num_components):
            component_end = min(component_start + component_size, num_nodes)
            for j in range(component_start, component_end):
                # Connecte chaque nœud de la composante avec un autre nœud de la même composante
                k = np.random.randint(component_start, component_end)
                while k == j:
                    k = np.random.randint(component_start, component_end)
                weight = np.random.randint(1, 11)
                adj_matrix[nodes[j]][nodes[k]] = weight
            component_start = component_end
    else:
        # Génère les poids au hasard pour les connexions entre les nœuds
        for i in range(num_nodes):
            for j in range(num_nodes):
                if np.random.random() < probability:
                    weight = np.random.randint(1, 11)  # Génère un poids entier aléatoire entre 1 et 10
                    adj_matrix[i][j] = weight

    # Si le graphe est fortement connexe, s'assure qu'il n'y a pas de nœuds isolés
    if probability == 1:
        for i in range(num_nodes):
            if np.all(adj_matrix[:, i] == float('inf')):
                j = np.random.randint(num_nodes)
                while j == i:
                    j = np.random.randint(num_nodes)
                weight = np.random.randint(1, 11)
                adj_matrix[i][j] = weight

    return adj_matrix


def get_random_from_existing(n):
    matrix_list = [
        [[float('inf'), 3, float('inf'), float('inf'), 6, 5],
         [3, float('inf'), 1, float('inf'), float('inf'), 4],
         [float('inf'), 1, float('inf'), 6, float('inf'), 4],
         [float('inf'), float('inf'), 6, float('inf'), 8, 5],
         [6, float('inf'), float('inf'), 8, float('inf'), 2],
         [5, 4, 4, 5, 5, 2, float('inf')]],

        [[float('inf'), 3, float('inf'), float('inf'), 6, 5],
         [3, float('inf'), 1, float('inf'), float('inf'), 4],
         [float('inf'), 1, float('inf'), 6, float('inf'), 4],
         [float('inf'), float('inf'), 6, float('inf'), 8, 5],
         [6, float('inf'), float('inf'), 8, float('inf'), 2],
         [5, 4, 4, 5, 5, 2, float('inf')]],

        [
            [float('inf'), 3, 2, float('inf'), float('inf'), float('inf'), float('inf'), ],
            [float('inf'), float('inf'), -2, 2, 2, float('inf'), float('inf'), ],
            [float('inf'), float('inf'), float('inf'), 4, float('inf'), 2, float('inf'), ],
            [float('inf'), float('inf'), float('inf'), float('inf'), 1, -1, float('inf'), ],
            [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 3, ],
            [float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 4, ],
            [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), ]
        ],

        [[float('inf'), 3, float('inf'), float('inf'), 6, 5],
         [3, float('inf'), 1, float('inf'), float('inf'), 4],
         [float('inf'), 1, float('inf'), 6, float('inf'), 4],
         [float('inf'), float('inf'), 6, float('inf'), 8, 5],
         [6, float('inf'), float('inf'), 8, float('inf'), 2],
         [5, 4, 4, 5, 5, 2, float('inf')]],

        [[0, float('inf'), float('inf'), 6, float('inf')],
         [float('inf'), 3, 0, float('inf'), 7],
         [2, 0, 3, 8, 5],
         [6, 8, float('inf'), 0, 9],
         [6, float('inf'), 7, -9, 0]]
    ]
    random_int = random.randint(0, len(matrix_list)-1)

    if n == len(matrix_list[random_int]):
        return matrix_list[random_int]
    else:
        return False

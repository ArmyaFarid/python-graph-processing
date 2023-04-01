import graphe_non_oriented.connexity
from graph.graph import Graph
import graph.display as g_display
import graph.exemples as exemples
from graph.matrix import get_edges_from_matrix
from algorithm.connexity import reduce_graph_matrix, get_reduce_graph_matrix_from_reduced_graph_edges


def print_text(color, text):
    color_code = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
    }
    end_code = '\033[0m'
    if color in color_code:
        print(f'{color_code[color]}{text}{end_code}')
    else:
        print(text)


def welcome(color):
    msg = "Bienvenue dans graphe processing app"
    line = "=" * (len(msg) + 5)
    empty_line = " " * (len(msg) + 5)
    print_text(color, line)
    print_text(color, empty_line)
    print_text(color, msg)
    print_text(color, empty_line)
    print_text(color, line)


def get_integer(num_attempts):
    while num_attempts > 0:
        try:
            user_input = int(input("Veuillez saisir un entier : "))
            return user_input
        except ValueError:
            num_attempts -= 1
            print("Saisie invalide ! Il vous reste", num_attempts, "tentatives.")
    print("Nombre de tentatives atteint. Le programme s'arrête.")
    exit()


def show_non_oriented_graph(graph_edges):
    print_text('yellow', 'Vouslez vous vous le voir en dessin ?')
    response = input('\tY(oui)/sinon anuller. \nDefault[non]: \t')
    if response.upper() == 'Y':
        g_display.draw_graph_from_edges_non_oriented(graph_edges)


def show_oriented_graph(graph_edges):
    print_text('yellow', 'Vouslez vous vous le voir en dessin ?')
    response = input('\tY(oui)/sinon anuller. \nDefault[non]: \t')
    if response.upper() == 'Y':
        g_display.draw_graph_from_edges_oriented(graph_edges)


def show_oriented_graph_reduced_graph(graph_edges, nodes_labels):
    print_text('yellow', 'Vouslez vous vous le voir en dessin ?')
    response = input('\tY(oui)/sinon anuller. \nDefault[non]: \t')
    if response.upper() == 'Y':
        g_display.draw_graph_from_edges_oriented_with_label(graph_edges, nodes_labels)


def get_matrix_from_user(n, separator):
    # Initialize the adjacency matrix with None values
    adj_matrix = [[None for i in range(n)] for j in range(n)]

    # Read the adjacency matrix from user input
    for i in range(n):
        row = input(f"\t{i + 1}: ")
        row_values = row.split(separator)
        for j in range(n):
            row_values[j] = row_values[j].replace(" ", "")
            if row_values[j].isnumeric():
                adj_matrix[i][j] = int(row_values[j])
            else:
                adj_matrix[i][j] = float('inf')

    return adj_matrix


def get_matrix(n, is_random=False):
    pass
    if is_random:
        # vous pouvez changer de type de generation en utilisant une des fonction disponibles dans le modules graph.exemples
        if exemples.get_random_from_existing(n):
            return exemples.get_random_from_existing(n)
        else:
            def choisir_type_graphe():
                while True:
                    type_graphe = input("Choisissez le type de graphe :\n1. Non orienté\n2. Orienté\n")
                    if type_graphe in ['1', '2']:
                        break
                    else:
                        print("Choix invalide ! Veuillez saisir 1 ou 2.")
                type_graphe = int(type_graphe)

                while True:
                    proba_connexe = input("Saisissez la probabilité d'avoir un graphe connexe (en %) : ")
                    try:
                        proba_connexe = float(proba_connexe) / 100
                        if proba_connexe < 0 or proba_connexe > 1:
                            raise ValueError
                        break
                    except ValueError:
                        print("Choix invalide ! Veuillez saisir un nombre entre 0 et 100.")

                return (type_graphe, proba_connexe)

            type_graphe, proba_connexe = choisir_type_graphe()

            if type_graphe == 1:
                print_text('white', "\tGénération d'un graphe non orienté avec probabilite de connexite " + str(
                    proba_connexe) + ".....")
                return exemples.generate_random_non_oriented_connex_graph(n, proba_connexe)

            else:
                print_text('white', "\tGénération d'un graphe orienté avec probabilite de connexite " + str(
                    proba_connexe) + ".....")
                return exemples.generate_random_oriented_strongly_connected_graph(n, proba_connexe)
    else:
        print(
            f'Pour chaque sommet rentrer les adjacence correspondant aux autres sommets du graph dans l\'ordre {[i for i in range(n)]} et separee par des ","')
        print("\033[31mNb: La non connection sera marqué par 'nan' sinon le poids ou le cout\033[0m")
        return get_matrix_from_user(n, ',')


welcome('white')
print_text('white', 'Pour commencer veuillez saisir le nombre de sommet')
n = get_integer(3)
is_auto = False
print_text('magenta', 'Voulez vous generer automatiquement un graphe de test ?')
response = input('Y(oui)/sinon anuller. \nDefault[non]: \t')
if response.upper() == 'Y':
    is_auto = True

# used_matrix = get_matrix(n, is_auto)
used_matrix = [[float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 7.0],
               [float('inf'), float('inf'), 6.0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
               [float('inf'), 10.0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
               [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 10.0, float('inf')],
               [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 7.0, float('inf'), float('inf')],
               [float('inf'), float('inf'), float('inf'), float('inf'), 10.0, float('inf'), float('inf'), float('inf')],
               [float('inf'), float('inf'), float('inf'), 9.0, float('inf'), float('inf'), float('inf'), float('inf')],
               [5.0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
               ]

graph = Graph(len(used_matrix), used_matrix)

print_text('white', 'Voici la matrice du graphe')
g_display.print_adjacency_matrix(graph.matrix)

graphe_type = graph.get_type()
if graphe_type == 'ordered':
    show_oriented_graph(graph.graph_edges)
    scc = graph.get_scc()
    if len(scc) == 1:
        print_text('green', 'C\'est un graphe oriente et fortement connexe')
        root = graph.get_root()
        if root is not None:
            print(f'Il existe une racine qui est {root}')
            arbre_court_chemin = {}
            if not graph.has_cycle():
                print_text('white', 'BELLMAN est utilise pour trouver l\'arbre de plus court chemin')
                arbre_court_chemin = graph.get_shortest_tree('BELLMAN', root)
            else:
                if not graph.has_negative_weight():
                    print_text('white', 'DIJKSTRA est utilise pour trouver l\'arbre de plus court chemin')
                    arbre_court_chemin = graph.get_shortest_tree('DIJKSTRA', root)
                else:
                    print_text('white', 'BELLMANFORD est utilise pour trouver l\'arbre de plus court chemin')
                    arbre_court_chemin = graph.get_shortest_tree('BELLMANFORD', root)
            print_text('magenta', 'Voici un tableau illustrant l\'arbre de plus court chemin')
            g_display.display_edges_as_table(graph.add_value_to_edges(arbre_court_chemin))
            show_oriented_graph(graph.add_value_to_edges(arbre_court_chemin))

        else:
            print_text('red', 'aucune racine trouvé\t')
    elif len(scc) > 1:
        print_text('green', 'C\'est un graphe oriente et non fortement connexe')
        reduced_graph_edges = get_edges_from_matrix(reduce_graph_matrix(graph.matrix, scc), False)
        reduced_graph_edges_with_full_vertex_label = []
        for edge in reduced_graph_edges:
            reduced_graph_edges_with_full_vertex_label.append([scc[edge[0]], scc[edge[1]], 1])
        print_text('green', 'Voici les composants connexe')
        g_display.display_edges_with_arrow(reduced_graph_edges_with_full_vertex_label, False)
        show_oriented_graph_reduced_graph(reduced_graph_edges, scc)
    else:
        print_text('red', "Error")

elif graphe_type == 'unordered':
    show_non_oriented_graph(graph.graph_edges)
    if graph.is_connexe():
        print_text('green', 'C\'est un graphe non oriente connexe')

        min_spanning_tree = graph.get_spanning_tree('min')
        print("Voici l'arbre couvant de poids minimum")
        g_display.display_edges_as_table(min_spanning_tree)
        show_non_oriented_graph(min_spanning_tree)

        print('\n')
        max_spanning_tree = graph.get_spanning_tree('max')
        print("Voici l'arbre couvant de poids maximun")
        g_display.display_edges_as_table(max_spanning_tree)
        show_non_oriented_graph(max_spanning_tree)
    else:
        print_text('green', 'c\'est un graphe non oriente non connexe')

    print_text('red', 'Find du program bye bye')
else:
    print('Error')

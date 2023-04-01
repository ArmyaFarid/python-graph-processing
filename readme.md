#Introduction

Il s'agit d'un programme permettant de manipuler des graphes et d'effectuer des actions telles que la visualisation des graphes ou la recherche de connexité des graphes.
Installation

    Clonez ce dépôt sur votre machine locale.
    Assurez-vous d'avoir installé les bibliothèques suivantes :
        Matplotlib
        Numpy
    Lancez le fichier main.py pour utiliser le programme.

Utilisation

Après avoir lancé le programme, vous serez accueilli avec un message de bienvenue. Le programme vous offrira ensuite différentes options pour travailler sur les graphes.

    Créer un graphe à partir d'une matrice d'adjacence
    Créer un graphe aléatoire
    Rechercher la connexité d'un graphe
    Réduire un graphe à l'aide de l'algorithme de Warshall
    Quitter le programme

Le programme vous guidera à travers chaque option, vous demandant les informations nécessaires pour effectuer l'action sélectionnée.
Licence



#La documentation du code pour des utilisateurs avancés

##Nom du programme

Graphe Processing App


##Description

Graphe Processing App est une application Python qui permet de travailler avec des graphes, de les afficher et d'appliquer des algorithmes sur ces derniers.


##Fonctionnalités

    Créer un graphe à partir d'une matrice d'adjacence ou de liste d'arêtes
    Afficher un graphe non orienté ou orienté
    Réduire un graphe non orienté ou orienté
    Déterminer la connexité d'un graphe

##Installation

    Clonez le dépôt GitHub à l'aide de la commande suivante : git clone https://github.com/votre-nom/graphe-processing-app.git
    Assurez-vous que Python 3 est installé sur votre machine
    Installez les dépendances du programme en exécutant la commande suivante : pip install -r requirements.txt

##Utilisation

###Création d'un graphe

Le programme propose deux façons de créer un graphe : en entrant une matrice d'adjacence ou une liste d'arêtes.

Pour créer un graphe à partir d'une matrice d'adjacence, exécutez la commande suivante 
```
from graph.matrix import get_matrix_from_user

n = 5  # nombre de noeuds
separator = ","  # séparateur des éléments de la matrice

adj_matrix = get_matrix_from_user(n, separator)
```

Pour créer un graphe à partir d'une liste d'arêtes, exécutez la commande suivante :

```
from graph.graph import Graph

edges = [(1, 2), (2, 3), (3, 4), (4, 1), (4, 5)]

graph = Graph()
graph.add_edges_from_list(edges)
```
###Affichage d'un graphe

Pour afficher un graphe non orienté ou orienté, exécutez les commandes suivantes :


```
from graph.display import draw_graph_from_edges_non_oriented, draw_graph_from_edges_oriented

# pour un graphe non orienté
draw_graph_from_edges_non_oriented(graph.edges)

# pour un graphe orienté
draw_graph_from_edges_oriented(graph.edges)
```

###Réduction d'un graphe

Pour réduire un graphe non orienté ou orienté, exécutez les commandes suivantes :


```
from algorithm.connexity import reduce_graph_matrix, get_reduce_graph_matrix_from_reduced_graph_edges

# réduction d'un graphe non orienté
reduced_graph_edges, nodes_labels = reduce_graph_matrix(graph.adj_matrix)
print(reduced_graph_edges)
print(nodes_labels)

# réduction d'un graphe orienté
reduced_graph_edges, nodes_labels = get_reduce_graph_matrix_from_reduced_graph_edges(graph.edges)
print(reduced_graph_edges)
print(nodes_labels)
```

###Détermination de la connexité d'un graphe

Pour déterminer la connexité d'un graphe, exécutez les commandes suivantes :


```
from algorithm.connexity import is_graph_connected

# pour un graphe non orienté
print(is_graph_connected(graph.adj_matrix))

# pour un graphe orienté
print(is_graph_strongly_connected(graph.edges))
```

#Auteurs

    Farid BAKOUAN
    armyabakouan@gmail.com

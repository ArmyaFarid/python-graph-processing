Début

// Entrée de la matrice d'adjacence
Entrer la taille de la matrice n
Pour i de 1 à n
    Pour j de 1 à n
        Entrer le poids/cout de l'arc/arete entre les sommets i et j dans la matrice
    Fin Pour
Fin Pour

// Détermination du type de graphe
Pour i de 1 à n
    Pour j de 1 à n
        Si M[i,j] != M[j,i] alors
            Graphe orienté
        Fin Si
    Fin Pour
Fin Pour

// Vérification de la connexité
Si Graphe non orienté alors
    Vérifier la connexité
    Si le Graphe non orienté est connexe alors
        // Recherche d'un arbre couvrant de poids minimum
        Appliquer l'algorithme de PRIM pour trouver l'arbre couvrant de poids minimum:
                    Entrées:
                        self.graph_matrix : la matrice d'adjacence du graphe non orienté.
                        self.size : le nombre de sommets dans le graphe non orienté.
                    Sorties:
                        tree_edges : la liste des arêtes de l'arbre couvrant de poids minimum.
                        Initialisation :
                            graph_size <- self.size
                            nodes <- [False] * graph_size
                            tree_edges <- []
                            starting_node <- 0
                            min_weight <- inf
                            min_index <- None
                        Trouver le sommet avec le poids minimum de la première arête :
                            Pour i allant de 0 à graph_size :
                                Si le poids de l'arête entre le sommet starting_node et le sommet i est inférieur à min_weight
                                et différent de inf, alors :
                                    min_weight <- poids de l'arête
                                    min_index <- i
                            Mettre à jour nodes :
                                nodes[starting_node] <- True
                                nodes[min_index] <- True
                            Ajouter l'arête avec le poids minimum à tree_edges :
                                tree_edges.append([starting_node, min_index, min_weight])
                        Trouver le reste des arêtes :
                            Tant que tous les sommets ne sont pas dans nodes :
                                min_weight <- inf
                                origin_index <- None
                                destination_index <- None
                                Pour j allant de 0 à graph_size :
                                    Si nodes[j] :
                                        Pour i allant de 0 à graph_size :
                                            Si (non nodes[i] et poids de l'arête entre le sommet i et le sommet j est différent de inf) :
                                                Si le poids de l'arête est inférieur à min_weight :
                                                    origin_index <- i
                                                    destination_index <- j
                                                    min_weight <- poids de l'arête
                                Si min_weight est différent de inf :
                                    Ajouter la nouvelle arête à tree_edges :
                                        new_tree_edge <- [origin_index, destination_index, min_weight]
                                        nodes[origin_index] <- True
                                        tree_edges.append(new_tree_edge)
                        Retourner tree_edges
        // Recherche d'un arbre couvrant de poids maximum
        Appliquer l'algorithme de PRIM pour trouver l'arbre couvrant de poids maximum
            Entrées :
                self : une instance de la classe graphe représentant le graphe à analyser
            Sorties :
                tree_edges : la liste des arêtes de l'arbre couvrant maximum
            Initialisation des variables :
            graph_size : taille du graphe
            nodes : une liste de booléens indiquant si chaque noeud est dans l'arbre couvrant
            tree_edges : une liste vide représentant les arêtes de l'arbre couvrant maximum
            starting_node : l'indice du noeud de départ (on choisit 0 par défaut)
            max_weight : le poids maximum initialisé à -infini
            max_index : l'indice du noeud avec le poids maximum initialisé à None
            Trouver le noeud avec le poids maximum à partir du noeud de départ :
            Parcourir tous les noeuds i du graphe
            Si le poids entre le noeud de départ et i est plus grand que max_weight et que ce poids n'est pas infini, mettre à jour max_weight et max_index
            Ajouter le noeud de départ et le noeud avec le poids maximum à nodes et tree_edges :
            Mettre à True nodes[starting_node] et nodes[max_index]
            Ajouter [starting_node, max_index, max_weight] à la liste tree_edges
            Tant que tous les noeuds ne sont pas dans l'arbre couvrant :
            Initialiser max_weight à -infini, origin_index et destination_index à None
            Parcourir tous les noeuds j de nodes
            Si j est dans l'arbre couvrant :
                Parcourir tous les noeuds i qui ne sont pas dans l'arbre couvrant :
                    Si le poids entre i et j est plus grand que max_weight et que ce poids n'est pas infini, mettre à jour max_weight, origin_index et destination_index
            Si max_weight est différent de -infini :
                Ajouter [origin_index, destination_index, max_weight] à la liste tree_edges
                Mettre à True nodes[origin_index]
            Retourner tree_edges.
    Fin Si
Fin Si




Si Graphe orienté alors
    Vérifier la forte connexité:
        on cherche les composants connexe , j'utilise ici l'algorithme de Kosaraju:
            fonction getscc():
                graph ← le graphe orienté à traiter
                V ← nombre de sommets dans le graphe
                visited ← tableau de booléens initialisé à False de taille V
                stack ← une pile vide
                # Première passe dfs
                pour chaque sommet i allant de 0 à V-1 faire:
                    si visited[i] est False alors:
                        appeler la fonction dfs(graph, i, visited, stack)
                # Renverser le graphe
                reversed_graph ← un nouveau graphe de taille V avec toutes les arêtes inversées par rapport à graph
                # Deuxième passe dfs
                visited ← un nouveau tableau de booléens initialisé à False de taille V
                scc ← une liste vide
                tant que stack n'est pas vide faire:
                    v ← retirer un élément de la pile stack
                    si visited[v] est False alors:
                        component ← une liste vide
                        appeler la fonction dfs(reversed_graph, v, visited, component)
                        ajouter component à la liste scc
                retourner scc
    // Recherche de l'existence d'un sommet racine
    Si Graphe orienté est fortement connexe  c'est a dire il y'a une seule scc alors
        Vérifier l'existence d'un sommet racine on utilise une fonction qui parcoure le graphe et s'assure qu'il  y'a un somet sans precedants qui peut atteindre les autres sommets:
                fonction trouver_sommet_racine(matrice_adjacence):
                    # Etape 1: Vérifier que le graphe est dirigé
                    n = taille(matrice_adjacence)
                    pour i de 0 à n-1:
                        si longueur(matrice_adjacence[i]) != n:
                            Erreur("La matrice d'adjacence doit être carrée")
                        pour j de 0 à n-1:
                            si matrice_adjacence[i][j] n'est pas dans [0, 1]:
                                Erreur("La matrice d'adjacence ne doit contenir que des 0 et des 1")
                    # Etape 2: Trouver tous les sommets entrants
                    entrants = []
                    pour j de 0 à n-1:
                        si tous(matrice_adjacence[i][j] == 0 pour i de 0 à n-1):
                            entrants.append(j)
                    # Etape 3: Vérifier si un sommet entrant est aussi un sommet racine
                    pour i dans entrants:
                        est_sommet_racine = Vrai
                        pour j de 0 à n-1:
                            si matrice_adjacence[j][i] != 0:
                                est_sommet_racine = Faux
                                break
                        si est_sommet_racine:
                            retourner i
                    # Etape 4: Si aucun sommet racine n'a été trouvé, retourner None
                    retourner None
        // Recherche de l'arborescence de plus courts chemins
        Si sommet racine existe c'est a dire different de none alors
            Appliquer l'algorithme le plus approprié (Bellman, Dijkstra, Bellman-Ford):
                Si le graphe n'a pas de cycle :
                    Utiliser Bellman pour trouver l'arbre de plus court chemin depuis la racine:
                        fonction bellman(root)
                            graph = self.graph
                            n = longueur(graph)
                            visited = [False] * n
                            A = []  # contient les arcs de l'arborescence
                            pi = [infini] * n  # initialisation de pi
                            # initialisation
                            pi[root] = 0
                            visited[root] = True
                            Z = {root}
                            # parcourir tant que tous les sommets ne sont pas traités
                            tant_que tous les éléments de visited sont faux
                                pour x de 0 à n-1
                                    si visited[x] est faux alors
                                        preds = []
                                        pour j de 0 à n-1
                                            si graph[j][x] n'est pas infini alors
                                                ajouter j à la liste preds
                                        si preds est un sous-ensemble de Z alors
                                            min = +infini
                                            i_min = nul
                                            pour i dans preds
                                                si (pi[i] + graph[i][x]) est inférieur à min alors
                                                    min = pi[i] + graph[i][x]
                                                    i_min = i
                                            pi[x] = min
                                            ajouter [i_min, x] à la liste A
                                            visited[x] = True
                                            ajouter x à l'ensemble Z
                            retourner A
                Sinon si le graphe n'a pas de poids négatif :
                    Utiliser Dijkstra pour trouver l'arbre de plus court chemin depuis la racine:
                        fonction dijkstra(graph, root)
                            matrix = graph
                            n = longueur(matrix)
                            dist = tableau de n valeurs initialisées à infini
                            dist[root] = 0
                            prev = tableau de n valeurs initialisées à None
                            visited = tableau de n booléens initialisés à False
                            heap = [(0, root)]
                            tant que heap n'est pas vide :
                                (d, u) = extraire_min(heap)
                                si visited[u] est vrai :
                                    continuer
                                visited[u] = vrai
                                pour chaque v allant de 0 à n :
                                    si matrix[u][v] n'est pas égal à infini :
                                        alt = dist[u] + matrix[u][v]
                                        si alt est plus petit que dist[v] :
                                            dist[v] = alt
                                            prev[v] = u
                                            ajouter (dist[v], v) à heap
                            arcs = []
                            pour chaque i allant de 0 à n :
                                si prev[i] n'est pas égal à None :
                                    ajouter [prev[i], i] à arcs
                            retourner arcs
                Sinon :
                    Utiliser Bellman-Ford pour trouver l'arbre de plus court chemin depuis la racine:
                        fonction bellman_ford(s):
                            matrice = graphe.matrice_adjacence
                            n = longueur(matrice)
                            d = [infini] * n
                            d[s] = 0
                            pi = [None] * n
                            pi[s] = -1
                            pour i de 0 à n-2:
                                pour j de 0 à n-1:
                                    pour k de 0 à n-1:
                                        si matrice[k][j] != 0 et d[k] + matrice[k][j] < d[j]:
                                            d[j] = d[k] + matrice[k][j]
                                            pi[j] = k
                            arbre = []
                            pour i de 0 à n-1:
                                si pi[i] != -1:
                                    arbre.append([pi[i], i])
                            retourner arbre
                Fin si
        Fin Si
    Fin Si
    Sinon
        Fournir le graphe reduit a travers les composants connexe, on traite les scc pour generer le graphe reduit(voir le code)
Fin Si





Fin

import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    # ...
    
    # -------------{Se preparan los primeros parametros}-------------
    
    nodos_visibles = [first_node] # Lista de nodos visibles.
    distance[first_node] = 0
    q = Queue()
    q.enqueue(first_node)
    
    # -------------{Se realiza el bucle}-------------
    
    while not q.isEmpty():
        current_node = q.dequeue() # Se saca el nodo a procesar.
        
        for node in nx.neighbors(graph, current_node): # Se analizan los vecinos.
            if node not in nodos_visibles:
                nodos_visibles.append(node) # Se hace visible
                q.enqueue(node) # Se guarda en nodos por procesar.
                distance[node] = distance[current_node] + 1 # Se le suma un paso respecto al nodo anterior.

    return distance

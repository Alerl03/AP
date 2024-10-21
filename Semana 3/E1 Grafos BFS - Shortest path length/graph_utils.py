import networkx as nx

def build_graph():
    # Añade aqui el código que hiciste en el ejercicio de la 
    # semana anterior para crear un grafo no-dirigido.
    
    # ----------{Dimensiones del grafo}----------
    
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])
    
    # ----------{Se añaden los nodos}----------
    
    graph = nx.Graph()
    
    for i in range(1, num_nodes+1):
        graph.add_node(i)

    # ----------{Se añaden las aristas}----------
    
    for i in range(num_edges):
        line = input().split()
        graph.add_edge(int(line[0]), int(line[1]))
    

    return graph

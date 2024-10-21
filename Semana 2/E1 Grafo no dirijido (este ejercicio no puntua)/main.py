import networkx  as nx
from solve import *
import matplotlib.pyplot as ptl

graph = build_graph();

print("Number of nodes: " + str(graph.number_of_nodes()))
print("Nodes: ", graph.nodes())
print("Number of edges: " + str(graph.number_of_edges()))
print("Edges: ", graph.edges())

# Paso 3: Utilizando PyCharm añade aqui el código necesario para mostrar
#         gráficamente el grafo.
# ...
nx.draw(graph, with_labels=True, font_weight="bold")
ptl.show()

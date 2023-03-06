import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
num_of_nodes = int(input("Enter the number of nodes: "))
V = [i for i in range(1, num_of_nodes + 1)]

for v in V.__reversed__():
    G.add_node(v)

for i in range(1, num_of_nodes + 1):
    for j in range(1, num_of_nodes + 1):
        if i != j:
            G.add_edge(i, j)

nx.draw_circular(G, with_labels=True)
plt.axis('square')
plt.show()

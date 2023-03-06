import networkx as nx
import matplotlib.pyplot as plt
from random import uniform


G = nx.Graph()
num_of_nodes = int(input("Enter the number of nodes: "))
pos = {}

V = [i for i in range(1, num_of_nodes + 1)]
for v in V:
    G.add_node(v)
    pos[v] = [uniform(0, 20), uniform(0, 20)]

for i in range(1, num_of_nodes + 1):
    for j in range(1, num_of_nodes + 1):
        if i != j:
            G.add_edge(i, j)


nx.draw(G, pos, with_labels=True)
plt.axis('square')
plt.show()

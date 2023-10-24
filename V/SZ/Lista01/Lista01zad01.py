# Weights - number of characters in a message.
import networkx as nx
import matplotlib.pyplot as plt


graph = nx.Graph()

with open('fb_clean_data.txt') as f:
    data = f.readlines()


data = [line.replace("\n", "").split(" ") for line in data]
data = [[x, y, int(z)] for x, y, z in data]

nodes = set()
for edge in data:
    nodes.add(int(edge[0]))
    nodes.add(int(edge[1]))
graph.add_nodes_from(nodes)

graph.add_weighted_edges_from(data)

if __name__ == '__main__':
    pos = nx.spiral_layout(graph)
    nx.draw_networkx_edges(graph, pos, width=0.1, alpha=0.2)
    nx.draw_networkx_nodes(graph, pos, node_size=10, alpha=0.25)
    plt.show()

from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
from Lista10zad04 import Graph


class DisjointGraph(Graph):
    def __init__(self):
        super().__init__()
        self.sub_graphs = defaultdict(list)
        self.parent = []

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            self.parent[parent_y] = parent_x

    def find_subsets(self):
        self.parent = list(range(self.num_of_vertices))
        for x, y in self.list_of_edges:
            self.union(x, y)

        for idx, val in enumerate(self.parent):
            self.sub_graphs[self.find(val)].append(idx)


if __name__ == '__main__':
    g = DisjointGraph()
    g.generate_graph(10, 0.15)
    g.show()

    g.find_subsets()
    print(dict(g.sub_graphs))

    G = nx.Graph()
    G.add_nodes_from(range(g.num_of_vertices))
    G.add_edges_from(ebunch_to_add=g.list_of_edges)
    nx.draw(G, with_labels=True)
    plt.show()

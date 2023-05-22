from math import ceil
from random import randint

import numpy as np


class Graph:
    def __init__(self):
        self.num_of_vertices = 0
        self.num_of_edges = 0
        self.list_of_edges = []
        self.incidence_matrix = None
        self.adjacency_matrix = None

    def generate_graph(self, vertices, edge_ratio):
        if edge_ratio < 0 or edge_ratio > 1:
            raise ValueError("q has to be a value from range [0;1]")

        max_edges = (vertices * (vertices - 1)) / 2
        edges = ceil(edge_ratio * max_edges)

        self.num_of_vertices = vertices
        self.num_of_edges = edges
        self.incidence_matrix = np.array([[0 for _ in range(edges)]
                                          for _ in range(vertices)])

        self.adjacency_matrix = np.array([[0 for _ in range(vertices)]
                                          for _ in range(vertices)])

        for _ in range(self.num_of_edges):
            regenerate = True
            while regenerate:
                edge = (randint(0, vertices - 1), randint(0, vertices - 1))
                if edge not in self.list_of_edges and \
                        edge[::-1] not in self.list_of_edges and \
                        edge[0] != edge[1]:
                    self.list_of_edges.append(edge)
                    regenerate = False

        self.incidence_matrix = self.incidence_matrix.T
        for i in range(len(self.list_of_edges)):
            for vertex in self.list_of_edges[i]:
                self.incidence_matrix[i][vertex] += 1

        self.incidence_matrix = self.incidence_matrix.T

        for edge in self.list_of_edges:
            start, stop = edge
            self.adjacency_matrix[start][stop] += 1
            self.adjacency_matrix[stop][start] += 1

    def show(self):
        print("\nIncidence matrix:")
        print(self.incidence_matrix)
        print("\nAdjacency matrix:")
        print(self.adjacency_matrix)
        print("\nSize of the Graph:")
        print(f"\tNumber of vertices (V): {self.num_of_vertices}")
        print(f"\tNumber of edges (E): {self.num_of_edges}")


if __name__ == '__main__':
    num_of_vertices = int(input("Enter the number of vertices: "))
    q = float(input("Enter the desired ratio of edges: "))

    graph = Graph()
    graph.generate_graph(num_of_vertices, q)

    graph.show()

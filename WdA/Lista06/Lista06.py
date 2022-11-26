from random import randint
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    """Class representing an undirected, weighted graph data structure"""

    def __init__(self, num_of_vertices):
        """Should I even bother to docstring this?"""
        self.num_of_vertices = num_of_vertices
        self.adjacency_list = [[] for _ in range(num_of_vertices)]

    def get_num_of_edges(self):
        """Returns the number of edges in graph"""
        num_of_edges = 0
        for i in self.adjacency_list:
            for _ in i:
                num_of_edges += 1
        return num_of_edges / 2

    def generate_graph(self, num_of_edges):
        """Generates given number of edges between vertices (cannot be higher than n(n-1)/2)"""
        if num_of_edges > self.num_of_vertices * (self.num_of_vertices - 1) / 2:
            print("Cannot create this many edges")
        else:
            while self.get_num_of_edges() < num_of_edges:
                ver_1 = randint(0, self.num_of_vertices - 1)
                ver_2 = randint(0, self.num_of_vertices - 1)
                weight = randint(1, 15)
                ver_1_vertices = [i[0] for i in self.adjacency_list[ver_1]]
                ver_2_vertices = [i[0] for i in self.adjacency_list[ver_2]]
                if ver_1 == ver_2 or ver_2 in ver_1_vertices or ver_1 in ver_2_vertices:
                    continue
                graph.add_edge(ver_1, ver_2, weight)

    def add_edge(self, ver_1, ver_2, weight):
        """Adds an arc to the graph"""
        self.adjacency_list[ver_1].append([ver_2, weight])
        self.adjacency_list[ver_2].append([ver_1, weight])

    def __dfs_recurrent(self, temp, vertex, visited):
        """Well, basically it's one step of a dfs algorithm in its recurrent form"""
        visited[vertex] = True
        temp.append(vertex)

        for i in self.adjacency_list[vertex]:
            if not visited[i[0]]:
                temp = self.__dfs_recurrent(temp, i[0], visited)
        return temp

    def divide_into_connected(self):
        """If the graph is not connected, returns the list of lists of nodes being in one connected subgraph,
        the length of the 0 list being the number of subgraphs"""
        visited = []
        connected_subs = []
        for i in range(self.num_of_vertices):
            visited.append(False)
        for vertex in range(self.num_of_vertices):
            if not visited[vertex]:
                temp = []
                connected_subs.append(self.__dfs_recurrent(temp, vertex, visited))
        return connected_subs

    def print_adjacency_list(self):
        """Prints out the structure of the graph"""
        print("Adjacency list:")
        for i in range(len(self.adjacency_list)):
            print("\t", i, end=": ")
            for j in self.adjacency_list[i]:
                print(j, end=" ")
            print()

    def dijkstra(self, start, stop):
        """This is really getting unnecessary"""
        queue = []
        distances = {vertex: float('inf') for vertex in range(self.num_of_vertices)}
        visited = [False for _ in range(self.num_of_vertices)]
        distances[start] = 0

        queue.append(start)
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            visited[current_vertex] = True

            for neighbour in self.adjacency_list[current_vertex]:
                alt = distances[current_vertex] + neighbour[1]

                if alt < distances[neighbour[0]]:
                    distances[neighbour[0]] = alt

                if visited[neighbour[0]] is False:
                    visited[neighbour[0]] = True
                    queue.append(neighbour[0])

        print(distances)
        if distances[stop] != float('inf'):
            print(f"The shortest distance between vertex {start} and vertex {stop} is {distances[stop]}")
        else:
            print(f"There is no path between vertex {start} and vertex {stop}.")


# Task 1
graph = Graph(6)
graph.generate_graph(5)
print("---------------------------Task 1---------------------------")
graph.print_adjacency_list()
cs = graph.divide_into_connected()
print("\nFollowing are connected components")
for sub in cs:
    print(sub)


# Task 2
print("\n---------------------------Task 2---------------------------")
graph.dijkstra(0, 5)


# Task 3

edges_list = []
for i in range(len(graph.adjacency_list)):
    for edge in graph.adjacency_list[i]:
        edges_list.append([i, edge[0], edge[1]])

# print(edges_list)


class GraphVisualisation:
    def __init__(self):
        self.edges = edges_list

    def visualize(self):
        G = nx.Graph()
        G.add_weighted_edges_from(self.edges)
        nx.draw_networkx(G)
        plt.show()


G = GraphVisualisation()
G.visualize()

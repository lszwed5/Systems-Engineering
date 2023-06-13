import json
import networkx as nx
import matplotlib.pyplot as plt


class CustomGraph:
    def __init__(self, directed=False):
        self.V = 0
        self.adjacency_list = dict()
        self.adjacency_matrix = []
        self.nodes = []
        self.list_of_edges = []
        self.G = nx.Graph()
        if directed: self.G = self.G.to_directed()
        self.node_color_map = []
        self.edge_color_map = []
        self.visited = set()
        self.pos = dict()
        self.distances = dict()
        self._dijkstra_prevs = dict()
        self.colors = ['green', 'red', 'blue', 'yellow', 'grey']
        self.generator = (c for c in self.colors)
        self.labels = dict()
        self.path = []

    def load_from_json(self, json_path='conf.json'):
        with open(json_path, 'r') as f:
            self.adjacency_list = json.load(f)

        for u in self.adjacency_list.keys():
            for v in self.adjacency_list[u]:
                if len(v) == 1:
                    self.G.add_edge(u, v)
                    self.list_of_edges.append((u, v))
                else:
                    self.G.add_edge(u, v[0], weight=v[1])
                    self.list_of_edges.append((u, v[0], v[1]))

        self.nodes = [node for node in self.adjacency_list.keys()]
        self.adjacency_matrix = [[0 for _ in range(len(self.nodes))]
                                 for _ in range(len(self.nodes))]
        for i in range(len(self.nodes)):
            for edge in self.adjacency_list[self.nodes[i]]:
                if len(edge) > 1:
                    self.adjacency_matrix[i][self.nodes.index(edge[0])] = \
                        edge[1]
                else:
                    self.adjacency_matrix[i][self.nodes.index(edge[0])] = 1

        self.node_color_map = ['blue' for _ in range(
            len(self.adjacency_list.keys()))]
        self.edge_color_map = ['black' for _ in range(
            len(self.G.edges))]
        self.V = len(self.adjacency_list.keys())

    def visualise(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color=self.node_color_map)
        plt.show()

    def _dfs(self, node):
        if node in self.visited:
            return

        self.visited.add(node)
        index = list(self.pos.keys()).index(node)
        self.node_color_map[index] = "green"
        nx.draw(self.G, self.pos, with_labels=True,
                node_color=self.node_color_map)
        plt.pause(1)
        for neighbour in self.adjacency_list[node]:
            self._dfs(neighbour)

    def visual_dfs(self, node):
        self.visited.clear()
        self.pos = nx.spring_layout(self.G)
        self._dfs(node)
        plt.show()

    def _top_sort(self, v, stack):
        self.visited.add(v)

        for i in self.adjacency_list[v]:
            if i not in self.visited:
                self._top_sort(i, stack)

        index = list(self.pos.keys()).index(v)
        self.node_color_map[index] = "gray"
        nx.draw(self.G, self.pos, with_labels=True,
                node_color=self.node_color_map)
        plt.pause(1)
        stack.insert(0, v)

    def topological_sort(self):
        self.visited.clear()
        stack = []
        self.pos = nx.circular_layout(self.G)

        for v in self.adjacency_list.keys():
            if v not in self.visited:
                self._top_sort(v, stack)

        print(stack)
        plt.show()

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def visual_kruskal_algorithm(self):
        self.pos = nx.spring_layout(self.G)
        result = []
        i, e = 0, 0
        self.list_of_edges = sorted(self.list_of_edges,
                                    key=lambda item: item[2])
        parent = dict()
        rank = dict()
        for node in self.adjacency_list.keys():
            parent[node] = node
            rank[node] = 0
        while e < self.V - 1:
            u, v, w = self.list_of_edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
                if (u, v) in list(self.G.edges):
                    index = list(self.G.edges).index((u, v))
                else:
                    index = list(self.G.edges).index((v, u))

                self.edge_color_map[index] = "red"
                nx.draw(self.G, self.pos, with_labels=True,
                        edge_color=self.edge_color_map)
                labels = nx.get_edge_attributes(self.G, 'weight')
                nx.draw_networkx_edge_labels(self.G, self.pos,
                                             edge_labels=labels)
                plt.pause(1)

        res = 0
        for u, v, weight in result:
            res += weight
            print(f"{u} - {v}: {weight}")
        print(f"Size of the minimum spanning tree: {res}")
        plt.show()

    def _construct_shortest_path(self, end_node):
        path = []
        prev = end_node
        while self._dijkstra_prevs[prev]:
            path.append(prev)
            prev = self._dijkstra_prevs[prev]
        path.append(prev)
        path = path[::-1]
        edges_path = [(path[i], path[i + 1])
                      for i in range(len(path) - 1)]

        return edges_path

    def visual_dynamic_dijkstra(self, start, stop):
        self.pos = nx.spring_layout(self.G)
        labels = nx.get_edge_attributes(self.G, 'weight')
        queue = []
        self.distances = {vertex: float('inf') for vertex
                          in self.adjacency_list.keys()}
        self._dijkstra_prevs = {vertex: None for vertex in
                                self.adjacency_list.keys()}
        visited = set()
        self.distances[start] = 0

        queue.append(start)
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            visited.add(current_vertex)

            for neighbour in self.adjacency_list[current_vertex]:
                alt = self.distances[current_vertex] + neighbour[1]

                if alt < self.distances[neighbour[0]]:
                    self.distances[neighbour[0]] = alt
                    self._dijkstra_prevs[neighbour[0]] = current_vertex

                    if (current_vertex, neighbour[0]) in list(self.G.edges):
                        index = list(self.G.edges).index(
                            (current_vertex, neighbour[0]))
                    else:
                        index = list(self.G.edges).index(
                            (neighbour[0], current_vertex))
                    self.edge_color_map[index] = "red"
                    nx.draw(self.G, self.pos, with_labels=True,
                            edge_color=self.edge_color_map)
                    nx.draw_networkx_edge_labels(self.G, self.pos,
                                                 edge_labels=labels)
                    plt.pause(1)

                if neighbour[0] not in visited:
                    visited.add(neighbour[0])
                    queue.append(neighbour[0])

        print(self.distances)
        print(self._dijkstra_prevs)
        if self.distances[stop] != float('inf'):
            print(f"The shortest distance between vertex {start} "
                  f"and vertex {stop} is {self.distances[stop]}")
        else:
            print(f"There is no path between vertex {start} "
                  f"and vertex {stop}.")
        path = self._construct_shortest_path(stop)
        print(path)
        nx.draw_networkx_edges(self.G, self.pos,
                               edgelist=path, edge_color='green', width=3)
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=labels)
        plt.show()

    def _bfs_max_flow(self, s, t, parent):
        self.visited = set()
        queue = [s]

        self.visited.add(s)

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.adjacency_matrix[u]):
                if ind not in self.visited and val > 0:
                    queue.append(ind)
                    self.visited.add(ind)
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    def edmunds_karp(self, source, sink):
        self.pos = nx.circular_layout(self.G)
        self.labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw(self.G, self.pos, with_labels=True)
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=self.labels)
        source = self.nodes.index(source)
        sink = self.nodes.index(sink)
        parent = [-1] * len(self.nodes)
        max_flow = 0

        while self._bfs_max_flow(source, sink, parent):
            plt.waitforbuttonpress()
            path_flow = float('inf')
            s = sink
            path = [s]
            while s != source:
                path_flow = min(path_flow, self.adjacency_matrix[parent[s]][s])
                s = parent[s]
                path.append(s)

            path = path[::-1]
            path = [(path[i], path[i + 1])
                    for i in range(len(path) - 1)]
            path = [(self.nodes[i], self.nodes[j]) for i, j
                    in path]
            self.path = path

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.adjacency_matrix[u][v] -= path_flow
                self.adjacency_matrix[v][u] += path_flow
                v = parent[v]

            self.labels.clear()
            for i in range(len(self.nodes)):
                for j in range(len(self.nodes)):
                    u = self.nodes[i]
                    v = self.nodes[j]
                    for a, b, w in self.list_of_edges:
                        if (u, v) == (a, b):
                            self.labels[(u, v)] = self.adjacency_matrix[i][j]
                        elif (v, u) == (b, a):
                            self.labels[(v, u)] = self.adjacency_matrix[i][j]

            nx.draw_networkx_edges(self.G, self.pos,
                                   edgelist=self.path,
                                   edge_color=next(self.generator),
                                   width=3)
            nx.draw_networkx_edge_labels(self.G, self.pos,
                                         edge_labels=self.labels)

        plt.waitforbuttonpress()
        self.labels = nx.get_edge_attributes(self.G, 'weight')
        for u, v in self.labels.keys():
            self.labels[(u, v)] -= \
                self.adjacency_matrix[self.nodes.index(u)][self.nodes.index(v)]
        nx.draw(self.G, self.pos, with_labels=True,
                node_color=self.node_color_map)
        nx.draw_networkx_edge_labels(self.G, self.pos,
                                     edge_labels=self.labels)
        plt.show()

        return max_flow


if __name__ == '__main__':
    graph = CustomGraph()
    graph.load_from_json("conf.json")
    graph.visual_dfs("A")

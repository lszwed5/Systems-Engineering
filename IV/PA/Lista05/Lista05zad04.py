import math
import networkx as nx
from matplotlib import pyplot as plt


def dynamic_dijkstra(graph, source):
    dist, prev = {}, {}
    Q = []

    for v in graph.keys():
        dist[v] = math.inf
        prev[v] = None
        Q.append(v)
    dist[source] = 0

    while Q:
        for v in Q:
            u = v if dist[v] == min([dist[v] for v in Q]) else u
        if u:
            Q.remove(u)

        for v in Q:
            for neighbor in graph[v]:
                alt = dist[neighbor] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = neighbor

    return dist, prev


def recursive_dijkstra(graph, source, dist=None, prev=None, Q=None):
    if not dist and not prev and not Q:
        dist, prev = {}, {}
        Q = []

        for v in graph.keys():
            dist[v] = math.inf
            prev[v] = None
            Q.append(v)
        dist[source] = 0

    u = None
    for v in Q:
        u = v if dist[v] == min([dist[v] for v in Q]) else u
    if u:
        Q.remove(u)

    if Q:
        for v in Q:
            for neighbor in graph[v]:
                alt = dist[neighbor] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = neighbor

            return recursive_dijkstra(graph, v, dist, prev, Q)
    else:
        return dist, prev

    # Time complexity: O(n^2) n - number of vertices


def construct_shortest_path(dists, prevs, end_node):
    path = []
    prev = end_node
    for _ in range(dists[end_node] + 1):
        path.append(prev)
        prev = prevs[prev]
    path = path[::-1]

    return path


def print_dijkstra(dists, prevs):
    for d in dists.keys():
        print(f"{d}: {dists[d]}")

    print()

    for p in prevs.keys():
        print(f"{p}: {prevs[p]}")


def construct_graph(graph: dict):
    G = nx.Graph()
    for v in graph.keys():
        for con in graph[v]:
            G.add_edge(v, con)

    return G


def check_graph(graph):
    exception = False
    for v in graph.keys():
        for con in graph[v]:
            if v not in graph[con]:
                print(f"\n\nIncorrect graph: Edge ({v}, {con}) exists, "
                      f"but Edge ({con}, {v}) does not.")
                exception = True
    if exception:
        raise Exception("See above for info (or below, "
                        "I don't understand Python)")


# sample_graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'C', 'E'],
#     'C': ['A', 'D', 'B'],
#     'D': ['B', 'C', 'E'],
#     'E': ['D', 'F', 'G', 'B'],
#     'F': ['D', 'E'],
#     'G': ['F']
# }

sample_graph = {
    'A': ['D', 'B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'E'],
    'D': ['A', 'B', 'E', 'F'],
    'E': ['D', 'C', 'F'],
    'F': ['D', 'E'],
}

check_graph(sample_graph)


distances, prev_points = recursive_dijkstra(sample_graph, 'A')
print_dijkstra(distances, prev_points)
shortest_path = construct_shortest_path(distances, prev_points, 'F')

G = construct_graph(graph=sample_graph)

vis_path = [(shortest_path[i], shortest_path[i+1])
            for i in range(len(shortest_path) - 1)]
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(G, pos, edgelist=vis_path, edge_color='red')
plt.show()

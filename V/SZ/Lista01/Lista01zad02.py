from Lista01zad01 import graph
import networkx as nx


largest_cc = graph.subgraph(max(
    nx.connected_components(graph), key=len)).copy()
print(largest_cc)
print(graph)

print("\n" + 22*"-" + " Shortest path: " + 22*"-" + "\n")
print(nx.dijkstra_path(largest_cc, '4', '34'))

print("\n" + 26*"-" + " Euler: " + 26*"-" + "\n")
print(nx.is_eulerian(graph))
print(nx.is_eulerian(largest_cc))
largest_ec = nx.eulerize(largest_cc)
print(nx.is_eulerian(largest_ec))
eul_path_edges = list(nx.eulerian_path(largest_ec))
eul_path = [x for x, y in eul_path_edges]
eul_path.append(eul_path_edges[-1][-1])
print(eul_path)

print("\n" + 26*"-" + " Flow: " + 27*"-" + "\n")
print(nx.maximum_flow_value(largest_cc, '4', '34', capacity='weight'))

print("\n" + 60*"-")

with open('fb_data.txt', 'r') as f:
    data = f.readlines()


data = [line.replace("\n", "").split(" ")[2:] for line in data]
data = [[x, y, int(z)] for x, y, z in data]
data = [[i, edge] for i, edge in enumerate(data)]
new_data = []
new_data_connections = []

for i, edge_1 in data:
    new_edge = edge_1
    if new_edge[:2] in new_data_connections:
        continue
    for j, edge_2 in data:
        if i == j:
            continue
        if edge_1[0] == edge_2[0] and edge_1[1] == edge_2[1]:
            new_edge[2] += edge_2[2]
        if edge_1[0] == edge_2[1] and edge_1[1] == edge_2[0]:
            new_edge[2] += edge_2[2]
    new_data.append(new_edge)
    new_data_connections.append(new_edge[:2])

print(data)
print(new_data)
print(new_data_connections)
print(len(data))
print(len(new_data))

with open('fb_clean_data.txt', 'w') as f:
    for edge in new_data:
        f.write(edge[0] + " " + edge[1] + " " + str(edge[2]) + "\n")

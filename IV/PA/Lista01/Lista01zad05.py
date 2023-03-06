import networkx as nx
import matplotlib.pyplot as plt
from random import uniform
from math import sqrt


G = nx.Graph()
num_of_nodes = int(input("Enter the number of nodes: "))
radius = float(input("Enter the radius of the circles: "))
pos = {}
fig = plt.figure()
ax = fig.add_subplot()

V = [i for i in range(1, num_of_nodes + 1)]

for v in V:
    stop = 0
    while stop < 100:
        ok = 1
        vx = uniform(0, 100)
        vy = uniform(0, 100)
        if pos.values():
            for [x, y] in pos.values():
                if sqrt((x - vx)**2 + (y - vy)**2) <= 2*radius:
                    stop += 1
                    ok = 0
                    break
        if ok:
            G.add_node(v)
            pos[v] = [vx, vy]
            circle = plt.Circle((pos[v]), radius=radius, color='green')
            ax.add_patch(circle)
            break
    if not ok:
        circle = plt.Circle((pos[list(G.nodes)[-1]]),
                            radius=radius, color='red')
        ax.add_patch(circle)
        break


nx.draw(G, pos, with_labels=True)
plt.axis('square')
plt.show()

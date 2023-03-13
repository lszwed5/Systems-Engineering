import networkx as nx
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()
VV = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
WW = [('q0', 'q2'), ('q2', 'q6'), ('q2', 'q1'), ('q6', 'q3'), ('q3', 'q3'),
      ('q1', 'q0'), ('q1', 'q4'), ('q4', 'q0'), ('q4', 'q5'), ('q5', 'q4'),
      ('q1', 'q3')]
gpos = {'q0': (0, 5), 'q1': (4, 2), 'q2': (8, 5), 'q3': (12, 5),
        'q4': (4, -2), 'q5': (8, -2), 'q6': (12, 9)}
g = nx.Graph()
g = g.to_directed()

Q = ('q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6')
E = ("a", "b", "c")
inp = input('Enter the input string: ')
q = "q0"


for ch in inp:
    if ch not in E:
        raise ValueError("Wrong sequence - "
                         "the string contains characters that do not belong "
                         "to the alphabet")


for v in VV:
    g.add_node(v)

for v1 in VV:
    for v2 in VV:
        if (v1, v2) in WW:
            g.add_edges_from([(v1, v2)])

nx.draw_networkx(g, gpos, arrows=True, with_labels=True, node_color='green')
labels = {('q1', 'q0'): "b", ('q0', 'q2'): "a,b,c", ('q2', 'q1'): "a,b",
          ('q1', 'q4'): "a", ('q4', 'q0'): "a", ('q4', 'q5'): "b,c",
          ('q5', 'q4'): "a,b,c", ('q1', 'q3'): "c", ('q2', 'q6'): "c",
          ('q6', 'q3'): "a,b,c", ('q3', 'q3'): "a,b,c"}
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)


def draw_circle(n):
    circle = plt.Circle(gpos[n], radius=1, color='red')
    ax.add_patch(circle)
    ax.axis('equal')
    plt.draw()
    plt.pause(1)
    circle.remove()
    plt.pause(0.05)


def func(char):
    global q
    draw_circle(q)
    print(f"{q}({char}) --> ", end='')
    match q:
        case 'q0':
            q = 'q2'
        case 'q1':
            match char:
                case 'a': q = 'q4'
                case 'b': q = 'q0'
                case 'c': q = 'q3'
        case 'q2':
            q = 'q1' if char in ['a', 'b'] else 'q6'
        case 'q3':
            pass
        case 'q4':
            q = 'q5' if char in ['b', 'c'] else 'q0'
        case 'q5':
            q = 'q4'
        case 'q6':
            q = 'q3'
    print(q)


for char in inp:
    func(char)

if q in ('q0', 'q4', 'q5'):
    print("\nAccepted")
else:
    print("\nNot accepted")

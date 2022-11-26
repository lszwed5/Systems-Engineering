import numpy as np


def sym_distance(p, q):
    distance = 0
    for l in range(len(p)):
        for m in range(len(p[l])):
            distance += abs(p[l][m] - q[l][m])
    return distance


def short_sym_distance(p, q):
    return abs(np.array(p) - np.array(q)).sum()


print(sym_distance([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))
print(short_sym_distance([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))

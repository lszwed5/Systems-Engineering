import numpy as np
import random
from copy import deepcopy
from math import exp


class SimulatedAnnealing:
    def __init__(self, distances_):
        self.tank_capacity = 15
        self.num_of_cities = 17
        self.distances = distances_
        self.T = 10
        self.alpha = 0.98
        self.X = None
        self.U = None
        self.dists = []
        self._dijkstra_prevs = []

    def generate_x(self):
        x = np.array([[0] * self.num_of_cities] * self.num_of_cities)
        u = [0] * self.num_of_cities
        while not self.check_constraints(x, u) or np.sum(x) == 0:
            x = np.array([[0] * self.num_of_cities] * self.num_of_cities)
            v_k = random.randint(1, self.num_of_cities - 1)
            path = self.dynamic_dijkstra(0, v_k)
            for edge in path:
                v_start, v_stop = edge
                x[v_start][v_stop] = 1
            x[v_stop][0] = 1
            u = self._construct_u(x, 0)

        self.X = x
        self.U = u

    def _construct_shortest_path(self, start_node, end_node):
        path = []
        prev = end_node
        while self._dijkstra_prevs[prev]:
            path.append(prev)
            prev = self._dijkstra_prevs[prev]
        path.append(prev)
        path.append(start_node)
        path = path[::-1]
        edges_path = [(path[i], path[i + 1])
                      for i in range(len(path) - 1)]

        return edges_path

    def dynamic_dijkstra(self, start, stop):
        queue = []
        self.dists = [float('inf') for _ in range(self.num_of_cities)]
        self._dijkstra_prevs = [None for _ in range(self.num_of_cities)]
        visited = set()
        self.dists[start] = 0

        queue.append(start)
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            visited.add(current_vertex)

            for ind, val in enumerate(self.distances[current_vertex]):
                alt = self.dists[current_vertex] + val

                if alt < self.dists[ind]:
                    self.dists[ind] = alt
                    self._dijkstra_prevs[ind] = current_vertex

                if ind not in visited:
                    visited.add(ind)
                    queue.append(ind)

        path = self._construct_shortest_path(start, stop)
        return path

    def _construct_u(self, x, i, counter=1, u=None):
        if u is None:
            u = [0] * self.num_of_cities
        j = 0
        while j < self.num_of_cities:
            if x[i][j] == 1:
                break
            else:
                j += 1

        if j != 0 and j < self.num_of_cities:
            u[j] += counter
            counter += 1
            i = j
            return self._construct_u(x, i, counter, u)
        else:
            return u

    @staticmethod
    def obj_func_value(x):
        return np.sum(x)

    def step(self):
        while True:
            ones = []
            for i in range(self.num_of_cities):
                for j in range(self.num_of_cities):
                    if self.X[i][j] == 1:
                        ones.append([i, j])
            new_X = deepcopy(self.X)

            operation = random.choice(['add', 'add', 'add', 'sub'])
            if operation == 'add':
                ind = random.choice(range(len(ones) - 1))
                addition = random.choice(range(self.num_of_cities - 1))
                new_X[ones[ind][0]][ones[ind][1]] = 0
                new_X[ones[ind][0]][addition] = 1
                new_X[addition][ones[ind][1]] = 1
            elif len(ones) > 2:
                ind = random.choice(range(len(ones) - 1))
                new_X[ones[ind][0]][ones[ind][1]] = 0
                for edge in ones:
                    if edge[0] == ones[ind][1]:
                        new_X[edge[0]][edge[1]] = 0
                        new_X[ones[ind][0]][edge[1]] = 1

            try:
                new_U = self._construct_u(new_X, 0)
            except RecursionError:
                continue

            if self.check_constraints(new_X, new_U):
                break

        print(self.obj_func_value(new_X))
        new_obj_value = self.obj_func_value(new_X)
        old_obj_value = self.obj_func_value(self.X)
        if new_obj_value > old_obj_value:
            self.X = new_X
            self.U = new_U
            print('accepted')
        else:
            p_new = exp((new_obj_value - old_obj_value) / self.T)
            p = random.random()
            if p_new > p:
                self.X = new_X
                self.U = new_U
                print('Accepted with probabilities:')
            else:
                print('Rejected with probabilities:')
            print(f'New: {p_new}')
            print(f'Random: {p}')

        self.T = self.T * self.alpha

    def check_constraints(self, x, u):
        for i in range(self.num_of_cities):
            if x[i][i] != 0:
                return False

        gas_usage = 0
        for i in range(self.num_of_cities):
            for j in range(self.num_of_cities):
                gas_usage += x[i][j] * self.distances[i][j]

        if gas_usage > self.tank_capacity:
            return False

        for i in range(self.num_of_cities):
            if sum(x[i]) > 1:
                return False

        for j in range(self.num_of_cities):
            if sum(x.T[j]) > 1:
                return False

        for i in range(self.num_of_cities):
            if sum(x[i]) != sum(x.T[i]):
                return False

        for i in range(self.num_of_cities):
            for j in range(self.num_of_cities):
                if j != 0:
                    if u[i] + x[i][j] > \
                            u[j] + (self.num_of_cities - 1) * (1 - x[i][j]):
                        return False

        return True

    def run(self):
        iterations = 0
        while self.T > 1:
            print(f'Step {iterations}:')
            self.step()
            iterations += 1
        print(f'Iterations: {iterations}')
        gas_usage = 0
        for i in range(self.num_of_cities):
            for j in range(self.num_of_cities):
                gas_usage += self.X[i][j] * self.distances[i][j]
        print(f'\n\nGas usage: {gas_usage}')
        print(f'Final temperature: {self.T}')
        print(f'Objective function value: {self.obj_func_value(self.X)}')


distances = np.array([
    [9999, 3, 5, 48, 48, 8, 8, 5, 5, 3, 3, 0, 3, 5, 8, 8, 5],
    [3, 9999, 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 0, 3, 8, 8, 5],
    [5, 3, 9999, 72, 72, 48, 48, 24, 24, 3, 3, 5, 3, 0, 48, 48, 24],
    [48, 48, 74, 9999, 0, 6, 6, 12, 12, 48, 48, 48, 48, 74, 6, 6, 12],
    [48, 48, 74, 0, 9999, 6, 6, 12, 12, 48, 48, 48, 48, 74, 6, 6, 12],
    [8, 8, 50, 6, 6, 9999, 0, 8, 8, 8, 8, 8, 8, 50, 0, 0, 8],
    [8, 8, 50, 6, 6, 0, 9999, 8, 8, 8, 8, 8, 8, 50, 0, 0, 8],
    [5, 5, 26, 12, 12, 8, 8, 9999, 0, 5, 5, 5, 5, 26, 8, 8, 0],
    [5, 5, 26, 12, 12, 8, 8, 0, 9999, 5, 5, 5, 5, 26, 8, 8, 0],
    [3, 0, 3, 48, 48, 8, 8, 5, 5, 9999, 0, 3, 0, 3, 8, 8, 5],
    [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 9999, 3, 0, 3, 8, 8, 5],
    [0, 3, 5, 48, 48, 8, 8, 5, 5, 3, 3, 9999, 3, 5, 8, 8, 5],
    [3, 0, 3, 48, 48, 8, 8, 5, 5, 0, 0, 3, 9999, 3, 8, 8, 5],
    [5, 3, 0, 72, 72, 48, 48, 24, 24, 3, 3, 5, 3, 9999, 48, 48, 24],
    [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 9999, 0, 8],
    [8, 8, 50, 6, 6, 0, 0, 8, 8, 8, 8, 8, 8, 50, 0, 9999, 8],
    [5, 5, 26, 12, 12, 8, 8, 0, 0, 5, 5, 5, 5, 26, 8, 8, 9999]
])


if __name__ == '__main__':
    sn = SimulatedAnnealing(distances)
    sn.generate_x()
    sn.run()

from Lista08zad01 import FleetList
from timeit import timeit
import matplotlib.pyplot as plt


fleet = FleetList()
fleet.load_from_json("conf.json")
fleet.show_fleet()
fleet.robots.sort(key=lambda x: x.price)

iterations = 3
linear_times = []
binary_times = []
hash_times = []

cardinalities = [2 ** i for i in range(1, 6)]
# cardinalities = [10]

for c in cardinalities:
    fleet = FleetList()
    fleet.generate_robots(c)
    fleet.robots.sort(key=lambda x: x.price)

    linear_time = []
    binary_time = []
    hash_time = []

    for robot in fleet.robots:
        param = "price"
        params = [[None], [robot.price], [None], [None]]
        value = robot.price
        alpha = 0.8

        linear_time.append(timeit(lambda: fleet.search_linear(params),
                                  number=iterations) / iterations)

        binary_time.append(timeit(lambda: fleet.search_binary(param, params),
                                  number=iterations) / iterations)

        hash_time.append(timeit(lambda: fleet.search_hash(param, value, alpha),
                                number=iterations) / iterations)

    linear_times.append(sum(linear_time) / len(linear_time))
    binary_times.append(sum(binary_time) / len(binary_time))
    hash_times.append(sum(hash_time) / len(hash_time))


plt.figure()
plt.plot(cardinalities, linear_times, label='Linear Search')
plt.plot(cardinalities, binary_times, label='Binary Search')
plt.plot(cardinalities, hash_times, label='Hash Search')
plt.title(f'Comparison of searching algorithms')
plt.xlabel('Cardinality of Robots')
plt.ylabel('Time [s]')
plt.legend()
plt.show()

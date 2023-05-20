from random import choice, randint
from math import log10, ceil, floor
import json


class FleetList:
    robot_types = ["AGV", "AFV", "ASV", "AUV"]
    max_price = 10000
    max_range = 99
    robots = []
    past_robots = []

    def prGreen(self, skk, end="\n"):
        print("\033[92m {}\033[00m".format(skk), end=end)

    def generate_robots(self, N):
        for i in range(N):
            self.robots.append(Robot(
                choice(self.robot_types),
                randint(0, self.max_price * 100) / 100,
                randint(0, self.max_range),
                choice([True, False])
            ))

    def show_robot(self, i):
        print(6 * " " + self.robots[i].type, end="")
        print(6 * " " +
              (ceil(log10(self.max_price)) -
               ceil(log10(self.robots[i].price))) * "0" +
              f"{self.robots[i].price:0.2f}", end="")
        if self.robots[i].range == 0:
            print(6 * " " + ceil(log10(self.max_range) + 1) * "0",
                  end="")
        else:
            print(6 * " " +
                  (ceil(log10(self.max_range)) - floor(log10(
                      self.robots[i].range) + 1) + 1) * "0" +
                  str(self.robots[i].range), end="")
        print(6 * " " + str(self.robots[i].camera))

    def show_fleet(self):
        print("\n\n" + 20 * "-" + " The Fleet status:" + 20 * "-" + "\n")
        degree = int(ceil(log10(len(self.robots))))

        i = 0
        for d in range(degree + 1):
            for _ in range(10 ** (d + 1) - 10 ** d):
                if i >= len(self.robots):
                    break
                if len(self.past_robots) != 0 and \
                        self.past_robots[i] != self.robots[i]:
                    self.prGreen("Robot " + (degree - d) * "0" + f"{i + 1}:", end="")
                else:
                    print(" Robot " + (degree - d) * "0" + f"{i + 1}:", end="")
                self.show_robot(i)
                i += 1
        print("\n" + 60*"-")

    def load_from_json(self, filename):
        with open(filename, "r") as f:
            content = json.load(f)

        self.robots = []
        for i in range(len(content.keys())):
            self.robots.append(Robot(
                content[f"Robot {i}"]["type"],
                content[f"Robot {i}"]["price"],
                content[f"Robot {i}"]["range"],
                content[f"Robot {i}"]["camera"],
            ))

    def save_to_json(self, filename):
        data = {f"Robot {i}": {
            "type": self.robots[i].type,
            "price": self.robots[i].price,
            "range": self.robots[i].range,
            "camera": self.robots[i].camera
        } for i in range(len(self.robots))}

        with open(filename, "w") as f:
            json.dump(data, f)

    def heap_sort(self, param):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and getattr(arr[i], param) < getattr(arr[left], param):
                largest = left

            if right < n and \
                    getattr(arr[largest], param) < getattr(arr[right], param):
                largest = right

            if largest != i:
                (arr[i], arr[largest]) = (arr[largest], arr[i])

                self.show_fleet()
                self.past_robots = self.robots[:]
                heapify(arr, n, largest)

        n = len(self.robots)

        for i in range(n // 2 - 1, -1, -1):
            heapify(self.robots, n, i)

        for i in range(n - 1, 0, -1):
            (self.robots[i], self.robots[0]) = (self.robots[0], self.robots[i])
            heapify(self.robots, i, 0)

    def quicksort(self, arr, low, high):
        print([*[self.robots[i].price for i in range(len(self.robots))]],
              end="\n\n")
        if low < high:
            pi = self._partition(arr, low, high)
            self.quicksort(arr, low, pi - 1)
            self.quicksort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high].price
        i = low - 1

        for j in range(low, high):
            if arr[j].price <= pivot:
                i += 1
                arr[i].price, arr[j].price = arr[j].price, arr[i].price

        arr[i + 1].price, arr[high].price = arr[high].price, arr[i + 1].price

        return i + 1

    def counting_sort(self, param="range"):
        size = len(self.robots)
        output = [0] * size

        count = [0] * 100

        for i in range(0, size):
            count[int(getattr(self.robots[i], param))] += 1

        for i in range(1, 100):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            output[count[int(getattr(self.robots[i], param))] - 1] = self.robots[i]
            count[int(getattr(self.robots[i], param))] -= 1
            i -= 1

        for i in range(0, size):
            self.robots[i] = output[i]


class Robot:
    def __init__(self, robot_type: str, price: float,
                 robot_range: int, camera: bool):
        self.name = "Robot"
        self.type = robot_type
        self.price = price
        self.range = robot_range
        self.camera = camera


if __name__ == '__main__':
    fleet = FleetList()
    fleet.generate_robots(int(input("Enter the length of List: ")))
    fleet.show_fleet()

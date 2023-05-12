from random import choice, randint
from math import log10, ceil, floor
import json


class FleetList:
    robot_types = ["AGV", "AFV", "ASV", "AUV"]
    max_price = 10000
    max_range = 100
    robots = []

    def generate_robots(self, N):
        for i in range(N):
            self.robots.append(Robot(
                choice(self.robot_types),
                randint(0, self.max_price * 100) / 100,
                randint(0, self.max_range),
                choice([True, False])
            ))

    def show_fleet(self):
        print("\n\n" + 20 * "-" + " The Fleet status:" + 20 * "-" + "\n")
        degree = int(ceil(log10(len(self.robots))))

        i = 0
        for d in range(degree + 1):
            for _ in range(10 ** (d + 1) - 10 ** d):
                if i >= len(self.robots):
                    break
                print("Robot " + (degree - d) * "0" + f"{i + 1}:", end="")
                print(6 * " " + self.robots[i].type, end="")
                print(6 * " " +
                      (ceil(log10(self.max_price)) -
                       ceil(log10(self.robots[i].price))) * "0" +
                      f"{self.robots[i].price:0.2f}", end="")
                if self.robots[i].range == 0:
                    print(6*" " + ceil(log10(self.max_range) + 1)*"0",
                          end="")
                else:
                    print(6 * " " +
                          (ceil(log10(self.max_range)) - floor(log10(
                              self.robots[i].range) + 1) + 1) * "0" +
                          str(self.robots[i].range), end="")
                print(6 * " " + str(self.robots[i].camera))
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

    @staticmethod
    def get_search_parameters():
        print("Enter the acceptable types separated by a single space:")
        types = [type_ for type_ in input().split(" ")]
        if types == [""]:
            types = [None]

        print("Enter the acceptable prices separated by a single space:")
        prices = [price for price in input().split(" ")]
        prices = [float(price) for price in prices] if prices != [""] else [
            None]

        print("Enter the acceptable ranges separated by a single space:")
        ranges = [range_ for range_ in input().split(" ")]
        ranges = [int(range_) for range_ in ranges] if ranges != [""] else [
            None]

        print("Enter the acceptable camera options "
              "separated by a single space:")
        cameras = [camera for camera in input().split(" ")]
        cameras = [False if _ == "0" else True for _ in cameras] \
            if cameras != [""] else [None]

        return [types, prices, ranges, cameras]

    def search_linear(self, params):
        for i in range(len(self.robots)):
            if self.robots[i].type in params[0] or params[0] == [None]:
                if self.robots[i].price in params[1] or params[1] == [None]:
                    if self.robots[i].range in params[2] or \
                            params[2] == [None]:
                        if self.robots[i].camera in params[3] or \
                                params[3] == [None]:
                            return i
        return None

    def search_binary(self, param, params):
        match param:
            case "type":
                self.robots.sort(key=lambda x: x.type)
                params = params[0]

                low = 0
                high = len(self.robots) - 1

                while low <= high:
                    mid = (high + low) // 2

                    if self.robots[mid].type < min(params):
                        low = mid + 1

                    elif self.robots[mid].type > max(params):
                        high = mid - 1

                    else:
                        if self.robots[mid].type in params:
                            return mid

                return None

            case "price":
                self.robots.sort(key=lambda x: x.price)
                params = params[1]

                low = 0
                high = len(self.robots) - 1

                while low <= high:
                    mid = (high + low) // 2

                    if self.robots[mid].price < min(params):
                        low = mid + 1

                    elif self.robots[mid].price > max(params):
                        high = mid - 1

                    else:
                        if self.robots[mid].price in params:
                            return mid

                return None

            case "range":
                self.robots.sort(key=lambda x: x.range)
                params = params[2]

                low = 0
                high = len(self.robots) - 1

                while low <= high:
                    mid = (high + low) // 2

                    if self.robots[mid].range < min(params):
                        low = mid + 1

                    elif self.robots[mid].range > max(params):
                        high = mid - 1

                    else:
                        if self.robots[mid].range in params:
                            return mid

                return None

            case "camera":
                self.robots.sort(key=lambda x: x.camera)
                params = params[3]

                low = 0
                high = len(self.robots) - 1

                while low <= high:
                    mid = (high + low) // 2

                    if self.robots[mid].camera < min(params):
                        low = mid + 1

                    elif self.robots[mid].camera > max(params):
                        high = mid - 1

                    else:
                        if self.robots[mid].camera in params:
                            return mid

                return None

    def search_hash(self, param, value, alpha):
        table_size = int(len(self.robots) // alpha)
        hash_table = [None] * table_size

        def hash_function(value, rehash):
            value = str(value).replace(".", "")
            total = 0
            for j in range(1, len(value) + 1):
                char = str(value[j-1])
                total += ord(char)
            total += rehash**2

            return total % table_size

        rehash = 0
        value = float(value)
        for i in range(len(self.robots)):
            index = hash_function(getattr(self.robots[i], param), rehash)
            while hash_table[index] is not None:
                rehash += 1
                index = hash_function(getattr(self.robots[i], param), rehash)
            hash_table[index] = i
            rehash = 0

        sought_index = hash_function(value, rehash)

        flag = sought_index
        while hash_table[sought_index] is not None:
            if getattr(self.robots[hash_table[sought_index]], param) == value:
                return hash_table[sought_index] + 1

            rehash += 1
            sought_index = hash_function(value, rehash)
            if flag == sought_index:
                break

        return None


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
    fleet.save_to_json("conf.json")

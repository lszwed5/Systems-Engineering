class Robot:
    def __init__(self, robot_type: str, price: float,
                 robot_range: int, camera: bool, name="Robot"):
        self.name = name
        self.type = robot_type
        self.price = price
        self.range = robot_range
        self.camera = camera

    def __str__(self):
        return str(self.price)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ne__(self, other):
        if isinstance(other, Robot):
            if self.name == other.name and \
                    self.type == other.type and \
                    self.price == other.price and \
                    self.range == other.range and \
                    self.camera == other.camera:
                return False
        return True

    def show_info(self):
        print(self.name + ':', end="")
        print(6 * " " + self.type, end="")
        print(6 * " " + f"{self.price:0.2f}", end="")
        print(6 * " " + str(self.range), end="")
        print(6 * " " + str(self.camera))


if __name__ == '__main__':
    robot = Robot("AUV", 21.37, 65, True)
    robot.show_info()

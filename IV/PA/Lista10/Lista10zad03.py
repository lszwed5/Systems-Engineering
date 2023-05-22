import numpy as np
from Robots import Robot


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class FleetLinkedList:
    def __init__(self):
        self.linked_list = []

    def append_robot(self, robot):
        i = 0
        if len(self.linked_list) > 0:
            while self.linked_list[i][2] != "_":
                i += 1
            self.linked_list[i][2] = len(self.linked_list)
            self.linked_list.append([i, robot, "_"])
        else:
            self.linked_list = [["_", robot, "_"]]

    def prepend_robot(self, robot):
        i = 0
        if len(self.linked_list) > 0:
            while self.linked_list[i][0] != "_":
                i += 1
            self.linked_list[i][0] = len(self.linked_list)
            self.linked_list.append(["_", robot, i])
        else:
            self.linked_list = [["_", robot, "_"]]

    def remove_robot(self, robot):
        i = 0
        if len(self.linked_list) > 0:
            while self.linked_list[i][1] != robot and \
                    i <= len(self.linked_list):
                i += 1

            if self.linked_list[i][0] == "_" and self.linked_list[i][2] == 0:
                self.linked_list[i] = [None, None, None]

            elif self.linked_list[i][0] == "_":
                self.linked_list[self.linked_list[i][2]][0] = "_"
                self.linked_list[i] = [None, None, None]

            elif self.linked_list[i][2] == "_":
                self.linked_list[self.linked_list[i][2]][2] = "_"
                self.linked_list[i] = [None, None, None]

            else:
                self.linked_list[self.linked_list[i][0]][2] = \
                    self.linked_list[self.linked_list[i][2]]
                self.linked_list[i] = [None, None, None]
        else:
            print("The Fleet is empty")

    def find_robot(self, robot):
        if len(self.linked_list) > 0:
            i = 0
            while self.linked_list[i][1] != robot and \
                    i <= len(self.linked_list):
                i += 1
            return i
        else:
            print("The Fleet is empty")
            return -1

    def sort(self):
        sorted_list = []
        temp = list(np.array(self.linked_list).T[1])
        for x in temp:
            if x is not None:
                sorted_list.append(float(x.price))
        sorted_list.sort()
        # print(sorted_list)

        previous = "_"
        for j in range(len(sorted_list)):
            for i in range(len(self.linked_list)):
                if not isinstance(self.linked_list[i][1], Robot):
                    continue
                if self.linked_list[i][1].price == sorted_list[j]:
                    self.linked_list[i][0] = previous
                    previous = i

        next_ = "_"
        for j in range(len(sorted_list))[::-1]:
            for i in range(len(self.linked_list)):
                if not isinstance(self.linked_list[i][1], Robot):
                    continue
                if self.linked_list[i][1].price == sorted_list[j]:
                    self.linked_list[i][2] = next_
                    next_ = i


if __name__ == '__main__':
    fleet = FleetLinkedList()
    fleet.linked_list = [
            [None, None, None],
            [6, Robot("AFV", 1018.33, 87, False), 3],
            [None, None, None],
            [1, Robot("ASV", 6389.13, 97, False), "_"],
            ["_", Robot("AGV", 5349.77, 79, True), 6],
            [None, None, None],
            [4, Robot("AGV", 8087.83, 83, True), 1],
            [None, None, None],
        ]
    fleet.prepend_robot(Robot("AUV", 6622.7, 83, True))
    print(np.array(fleet.linked_list))
    fleet.remove_robot(Robot("AUV", 6622.7, 83, True))
    print()
    print(np.array(fleet.linked_list))
    print()
    print(fleet.find_robot(Robot("AGV", 8087.83, 83, True)))
    fleet.sort()
    print()
    print(np.array(fleet.linked_list))

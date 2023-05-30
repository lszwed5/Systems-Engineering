from IV.PA.Lista10.Robots import Robot
from math import log10, ceil, floor
import json


PARAMETER = input("Enter the attribute to construct BST from: ")


class FleetList:
    robot_types = ["AGV", "AFV", "ASV", "AUV"]
    max_price = 10000
    max_range = 99
    robots = []
    past_robots = []

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
                    self.prGreen("Robot " + (degree - d) * "0" + f"{i + 1}:",
                                 end="")
                else:
                    print(" Robot " + (degree - d) * "0" + f"{i + 1}:", end="")
                self.show_robot(i)
                i += 1
        print("\n" + 60 * "-")

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


class Node:
    parameter = PARAMETER

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(getattr(self.data, self.parameter))

    def __repr__(self):
        return self.__str__()

    def flatten(self):
        return {
            "data": self.data.__dict__,
            "left": self.left.flatten() if self.left else None,
            "right": self.right.flatten() if self.right else None,
        }

    @classmethod
    def from_dictionary(cls, d):
        obj = cls(Robot(
            *[*d["data"].values()][1:-1], [*d["data"].values()][0]
        ))

        if "left" in d and d["left"] is not None:
            obj.left = cls.from_dictionary(d["left"])

        if "right" in d and d["right"] is not None:
            obj.right = cls.from_dictionary(d["right"])

        return obj


class RobotBST:
    parameter = PARAMETER

    def __init__(self):
        self.root = None

    def draw_tree(self):
        print('\n\n' + 60*'-' + '\n\n')
        self.btree_print_indented()
        print('\n\n' + 60*'-' + '\n\n')

    def btree_print_indented(self, top='root', level=0):
        if top is None:
            return
        if top == 'root':
            top = self.root
            if self.root is None:
                return
        self.btree_print_indented(top.right, level + 1)
        print("{}* {}".format('       ' * level, top))
        self.btree_print_indented(top.left, level + 1)

    def insert(self, node):
        self.root = self._insert(self.root, node)

    def _insert(self, root, node):
        if root is None:
            return node
        else:
            if getattr(root.data, self.parameter) == \
                    getattr(node.data, self.parameter):
                return root
            elif getattr(root.data, self.parameter) < \
                    getattr(node.data, self.parameter):
                root.right = self._insert(root.right, node)
            else:
                root.left = self._insert(root.left, node)
        return root

    def search(self, node):
        return self._search(self.root, node)

    def _search(self, root, node):
        if root is None or getattr(root.data, self.parameter) == \
                getattr(node.data, self.parameter):
            return root
        if getattr(root.data, self.parameter) < \
                getattr(node.data, self.parameter):
            return self._search(root.right, node)
        return self._search(root.left, node)

    def _find_parent(self, root, node):
        if root is None:
            return root, None
        if (root.left is not None and
                getattr(root.left.data, self.parameter) ==
                getattr(node.data, self.parameter)):
            return root, 'left'
        if (root.right is not None and
                getattr(root.right.data, self.parameter) ==
                getattr(node.data, self.parameter)):
            return root, 'right'
        if getattr(root.data, self.parameter) < \
                getattr(node.data, self.parameter):
            return self._find_parent(root.right, node)
        return self._find_parent(root.left, node)

    def remove_node(self, node):
        parent, side = self._find_parent(self.root, node)
        setattr(parent, side, None)

    def generate_bst(self, robots):
        for robot in robots:
            self.insert(Node(robot))

    def save_to_json(self, filename='bst_tree.json'):
        json_structure = json.dumps(self.root.flatten(), indent=4)
        with open(filename, 'w') as f:
            f.write(json_structure)

    def load_from_json(self, json_path='bst_tree.json'):
        with open(json_path, 'r') as f:
            data = json.load(f)
        self.root = Node.from_dictionary(data)

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.preorder(node.left)
            print(node.data)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.data)


if __name__ == '__main__':
    fleet = FleetList()
    fleet.load_from_json(
        r"C:\Users\lukas\Desktop\Wszystko\Programy\INS\IV\PA\Lista09\conf10.json")
    fleet.show_fleet()
    bst = RobotBST()
    bst.generate_bst(fleet.robots)
    # bst.insert(Node(Robot("AUV", 21.37, 66, True, name='1')))
    # bst.insert(Node(Robot("AUV", 42.00, 43, True, name='2')))
    # bst.insert(Node(Robot("AUV", 66.60, 82, True, name='3')))
    bst.draw_tree()
    print(bst.search(Node(Robot("AGV", 5667.42, 99, True, name='Robot'))))
    bst.remove_node(Node(Robot("AGV", 5667.42, 99, True, name='Robot')))
    bst.draw_tree()
    bst.save_to_json()
    bst = RobotBST()
    bst.load_from_json()
    bst.draw_tree()

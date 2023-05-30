import json


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def flatten(self):
        return {
            "data": self.data,
            "left": self.left.flatten() if self.left else None,
            "right": self.right.flatten() if self.right else None,
        }

    @classmethod
    def from_dictionary(cls, d):
        obj = cls(d["data"])

        if "left" in d and d["left"] is not None:
            obj.left = cls.from_dictionary(d["left"])

        if "right" in d and d["right"] is not None:
            obj.right = cls.from_dictionary(d["right"])

        return obj


class BinaryTree:
    def __init__(self):
        self.head = None

    def draw_tree(self):
        print('\n\n' + 60*'-' + '\n\n')
        self.btree_print_indented()
        print('\n\n' + 60*'-' + '\n\n')

    def btree_print_indented(self, top='head', level=0):
        """Prints the binary tree to the console horizontally"""
        if top is None:
            return
        if top == 'head':
            top = self.head
            if self.head is None:
                return
        self.btree_print_indented(top.right, level + 1)
        print("{}* {}".format('   ' * level, top))
        self.btree_print_indented(top.left, level + 1)

    def bfs(self, node):
        visited = []
        queue = [self.head]
        while len(queue) != 0:
            cur_node = queue.pop(0)
            if cur_node.data == node.data:
                return cur_node
            visited.append(cur_node.data)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        print(visited)
        return None

    def _find_parent(self, child):
        visited = []
        queue = [self.head]
        while len(queue) != 0:
            cur_node = queue.pop(0)
            visited.append(cur_node.data)
            if cur_node.left:
                if cur_node.left.data == child.data:
                    return cur_node, 'left'
                queue.append(cur_node.left)
            if cur_node.right:
                if cur_node.right.data == child.data:
                    return cur_node, 'right'
                queue.append(cur_node.right)
        print(visited)
        return None

    def add_node(self, node, parent, side):
        parent_node = self.bfs(parent)
        if parent_node is None:
            print("There is no such parent node in the tree")
        if getattr(parent_node, side) is not None:
            print(f"There already exists a {side} child node for this "
                  f"parent")
        else:
            setattr(parent_node, side, node)

    def remove_node(self, node):
        node = self.bfs(node)
        if node is None:
            print("There is no such node in the tree")
        elif self._find_parent(node) is None:
            self.head = None
        else:
            parent, side = self._find_parent(node)
            setattr(parent, side, None)

    def save_to_json(self, filename='tree.json'):
        json_structure = json.dumps(self.head.flatten(), indent=4)
        with open(filename, 'w') as f:
            f.write(json_structure)


tree = BinaryTree()
tree.head = Node(1)
tree.head.left = Node(2)
tree.head.right = Node(3)
tree.head.left.left = Node(4)
tree.head.left.right = Node(5)
tree.head.right.left = Node(6)
tree.head.right.right = Node(7)
tree.head.left.left.left = Node(8)

tree.btree_print_indented()
print("\n\n\n")
# found = tree.bfs(Node(5))
# print(found)

# tree.add_node(Node(9), Node(8), 'right')
# tree.btree_print_indented()

# tree.remove_node(Node(2))
# tree.btree_print_indented()

json_data = json.dumps(tree.head.flatten())
tree.save_to_json()
bn_tree = BinaryTree()
bn_tree.head = Node.from_dictionary(json.loads(json_data))
bn_tree.btree_print_indented()

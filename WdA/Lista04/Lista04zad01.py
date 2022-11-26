from WdA.Lista03 import Lista03zad01


class Node:
    """Class representing a single Node"""
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)


class LinkedList(Lista03zad01.Queue):
    """Class representing a single Linked List structure"""
    def __init__(self, head=None):
        super(LinkedList, self).__init__(head)
        self.head = head

    def print_list(self):
        """Prints out all the nodes in a linked list to the console. Written in debugging purposes"""
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def pop(self):
        """Removes and returns the first item (index 0) from a Linked List"""
        if self.head:
            head = self.head
            self.head = self.head.next
            return head.data
        else:
            return None

    def is_empty(self):
        """Checks if there are no values in the Linked List"""
        if self.head:
            return False
        else:
            return True


def breadth_first_search(tree):
    """Visits every node of a binary tree using the Breadth First Search algorithm"""
    visited = []
    queue = LinkedList()
    queue.append(tree)
    while not queue.is_empty():
        node = queue.pop()
        visited.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(visited)


def depth_first_search(tree):
    """Visits every node of a binary tree using the Depth First Search algorithm"""
    visited = []
    stack = LinkedList()
    stack.prepend(tree)
    while not stack.is_empty():
        node = stack.pop()
        visited.append(node.data)
        if node.right:
            stack.prepend(node.right)
        if node.left:
            stack.prepend(node.left)
    print(visited)


def btree_print_indented(top, level=0):
    """Prints the binary tree to the console horizontally"""
    if top is None:
        return
    btree_print_indented(top.right, level + 1)
    print("{}* {}".format('   ' * level, top))
    btree_print_indented(top.left, level + 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)


if __name__ == '__main__':
    print("\n" + 70 * "-")

    print("\nList of visited nodes in chronological order using the BFS algorithm:")
    breadth_first_search(root)

    print("\nList of visited nodes in chronological order using the DFS algorithm:")
    depth_first_search(root)

    print("\n" + 70 * "-")

    btree_print_indented(root)

import Lista04zad01
import copy


def btree_print_indented(top, level=0):
    """Prints the binary tree to the console horizontally"""
    if top is None:
        return
    btree_print_indented(top.right, level + 1)
    print("{}* {}".format('   ' * level, top))
    btree_print_indented(top.left, level + 1)


def replace_node_with_depth(node, depth=0):
    """Reassigns each node's data value to its depth (number of branches from root)"""
    if not node:
        return
    node.data = depth
    replace_node_with_depth(node.left, depth + 1)
    replace_node_with_depth(node.right, depth + 1)


def count_level_nodes(tree):
    """Returns a list containing the number of nodes on each tree's level, the indexes being the nodes' depth"""
    tree = copy.deepcopy(tree)
    replace_node_with_depth(tree)
    visited = []
    stack = Lista04zad01.LinkedList()
    stack.prepend(tree)
    while not stack.is_empty():
        node = stack.pop()
        visited.append(node.data)
        if node.right:
            stack.prepend(node.right)
        if node.left:
            stack.prepend(node.left)
    set_ = set(visited)
    length = len(set_)
    counter = list(range(length))
    for level in set_:
        counter[level] = 0
        for occurrence in visited:
            if occurrence == level:
                counter[level] += 1
    return counter


def count_leaves(tree):
    """Returns the number of leaves in a binary tree"""
    visited = []
    leaves = 0
    queue = Lista04zad01.LinkedList()
    queue.append(tree)
    while not queue.is_empty():
        node = queue.pop()
        if not node.left and not node.right:
            leaves += 1
        visited.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return leaves


def find_closest_leaf(tree):
    """Returns the distance between the root and its closest leaf"""
    tree = copy.deepcopy(tree)
    replace_node_with_depth(tree)
    visited = []
    queue = Lista04zad01.LinkedList()
    queue.append(tree)
    while not queue.is_empty():
        node = queue.pop()
        if not node.left and not node.right:
            return node
        visited.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def print_k_distant_leaves(tree, k):
    """Prints out all the leaves whose distance from the root is equal to k"""
    if tree is None:
        return
    if k == 0 and not tree.left and not tree.right:
        print(tree.data, end=" ")
    else:
        print_k_distant_leaves(tree.left, k-1)
        print_k_distant_leaves(tree.right, k-1)


root = copy.deepcopy(Lista04zad01.root)
root.left.right.right = Lista04zad01.Node(9)
root.right.right.right = Lista04zad01.Node(10)


# Task 1
print("\n" + 30 * "-" + " Task 1 " + 30 * "-" + "\n")
btree_print_indented(root)


# Task 2
print("\n" + 30 * "-" + " Task 2 " + 30 * "-" + "\n")
level_nodes = count_level_nodes(root)
for i in range(len(level_nodes)):
    print(f"\tLevel {i}: {level_nodes[i]} node(s)")

print(f"\n\tNumber of leaves: {count_leaves(root)}")


# Task 3
print("\n" + 30 * "-" + " Task 3 " + 30 * "-" + "\n")
print(f"The shortest distance between the root and a leaf is {find_closest_leaf(root)}")
print()
print(f"The leaves whose distance from the root is equal to {find_closest_leaf(root)} are: ")
print_k_distant_leaves(root, find_closest_leaf(root).data)
print(2*"\n" + 70 * "-" + "\n")

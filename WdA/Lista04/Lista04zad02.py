import Lista04zad01
import copy


def btree_print_indented(top, level=0):
    """Prints the binary tree to the console horizontally"""
    if top is None:
        return
    btree_print_indented(top.right, level + 1)
    print("{}* {}".format('   ' * level, top))
    btree_print_indented(top.left, level + 1)


def assign_parents(tree):
    """Traverses through every node of a given tree (BFS) and assigns a proper parent to it"""
    queue = Lista04zad01.LinkedList()
    queue.append(tree)
    while not queue.is_empty():
        node = queue.pop()
        if node.left:
            queue.append(node.left)
            node.left.parent = node
        if node.right:
            queue.append(node.right)
            node.right.parent = node


def search_node(tree, data):
    """Returns a Node that has data equal to the given, or None if there is no such node in the tree"""
    if tree is None:
        return None
    if tree.data == data:
        return tree
    res1 = search_node(tree.left, data)
    if res1:
        return res1
    res2 = search_node(tree.right, data)
    return res2


def create_new_tree(tree, leaf):
    """Rearranges the tree so that the given leaf is the new root without altering any branches"""

    def helper(node, new_parent):
        if node == tree:
            node.parent = new_parent
            if node.left == new_parent:
                node.left = None
            if node.right == new_parent:
                node.right = None
            return tree
        if node.left:
            node.right = node.left
        if node.parent.left == node:
            node.parent.left = None
        node.left = helper(node.parent, node)
        node.parent = new_parent
        return node

    if leaf.left or leaf.right:
        return None
    else:
        return helper(leaf, None)


root = Lista04zad01.root
assign_parents(root)
root_copy = copy.deepcopy(root)

root2 = root_copy.left.right

print(2*"\n" + 20 * "-" + " Starting tree " + 20 * "-" + "\n")
Lista04zad01.breadth_first_search(root_copy)
print()
btree_print_indented(root_copy)

print(2*"\n" + 20 * "-" + " Rerooted tree " + 20 * "-" + "\n")
# tree2 = create_new_tree(root_copy, root2)
tree2 = create_new_tree(root_copy, search_node(root_copy, 6))
Lista04zad01.breadth_first_search(tree2)
print()
btree_print_indented(tree2)
print()

"""
W poleceniu napisane jest "nie dla każdego wierzchołka", a nie "nie dla każdego liscia". 
Dla dowolnego liścia zawsze możemy stworzyć "odwrócone" drzewo binarne, jest to nawet możliwe dla niektórych
wierzchołków. Jednkże, jeśli dany wierzchołek ma zarówno rodzica, jak i obydwoje dzieci, wtedy wierzchołek taki nie
może zostać korzeniem nowego drzewa binarnego, ponieważ musiałby mieć 3 dzieci.
"""

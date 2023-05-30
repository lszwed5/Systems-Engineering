from Lista11zad02 import FleetList, RobotBST, Node, Robot


class RotaryRobotBST(RobotBST):
    def rotate_right(self, node):
        x = self.search(node)
        parent, side = self._find_parent(self.root, node)

        y = x.left
        b = y.right

        y.right = x
        x.left = b

        setattr(parent, side, y)

    def rotate_left(self, node):
        x = self.search(node)
        parent, side = self._find_parent(self.root, node)

        y = x.right
        b = y.left

        y.left = x
        x.right = b

        setattr(parent, side, y)


fleet = FleetList()
fleet.load_from_json(
    r"C:\Users\lukas\Desktop\Wszystko\Programy\INS\IV\PA\Lista09\conf10.json")
fleet.show_fleet()
bst = RotaryRobotBST()
bst.generate_bst(fleet.robots)
bst.draw_tree()
bst.rotate_right(Node(Robot('ASV', 3753.44, 26, False)))
bst.draw_tree()
bst.rotate_left(Node(Robot('ASV', 5378.45, 57, True)))
bst.draw_tree()

from Lista11zad02 import FleetList, RobotBST


fleet = FleetList()
fleet.load_from_json(
    r"C:\Users\lukas\Desktop\Wszystko\Programy\INS\IV\PA\Lista09\conf10.json")
fleet.show_fleet()
bst = RobotBST()
bst.generate_bst(fleet.robots)
bst.draw_tree()

print("Preorder traversal:")
bst.preorder(bst.root)
print('\nInorder traversal:')
bst.inorder(bst.root)
print("\nPostorder traversal:")
bst.postorder(bst.root)

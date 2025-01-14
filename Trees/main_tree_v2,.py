from Node import Node
from Tree_V2 import TreePart2
from PrintTree import PrintTree

tree = TreePart2()

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(6)
root.right.right.left = Node(7)

# PrintTree(root)

print(f"1. Spiral / ZigZag traversal: {tree.SpiralTraversal(root)}")
print(f"2. Boundary Traversal: {tree.BoundaryTraversal(root)}")
print(f"3. Vertical Traversal: {tree.VerticalTraversal(root)}")
print(f"4. Top View: {tree.TopBottomView(root, 'top')}")
print(f"5. Bottom View: {tree.TopBottomView(root, 'bottom')}")
print(f"6. Left View: {tree.LeftRightView(root, 'left')}")
print(f"7. Right View: {tree.LeftRightView(root, 'right')}")
print(f"8. Is Tree Symmetrical: {tree.isSymmetrical(root)}")
# target = int(input("Enter Node: "))
target = 9
print(f"9. Path from root to node: {target} -> {tree.PathToNode(root, target)}")
# p, q = map(int, input("Enter p, q: ").split())
p, q = 2, 9
print(f"10. Lowest common ancestor of nodes: {p, q} -> {tree.LowestCommonAncestor(root, p, q).val}")
print(f"11. Maximum width of BT: {tree.GetMaximumWidth(root)}")
# new_root = tree.ChildrenSumProperty(root)
print("12. After Children Sum Property: DONE!")
# PrintTree(new_root)
# k, target = map(int, input("Enter k, target: ").split())
k, target = 1, 4
list_of_nodes = tree.NodesAtDistanceK(root, k, target)
print(f"13. List of nodes at a distance of k={k} from node:{target} -> {list_of_nodes}")
node = 3
timeTaken = tree.BurnTree(root, node)
print(f"14. Time taken to burn the tree from node: {node} -> {timeTaken}")
print(f"15. Constructing tree from inorder and preorder:")
# inorder = list(map(int, input("Enter inorder: ").split()))
# preorder = list(map(int, input("Enter preorder: ").split()))
inorder = [40,20,50,10,60,30]
preorder = [10,20,40,50,30,60]
builtTree = tree.ConstructTreeFromInPre(inorder, preorder)
PrintTree(builtTree)
print(f"16. Constructing tree from inorder and postorder:")
# inorder = list(map(int, input("Enter inorder: ").split()))
# postorder = list(map(int, input("Enter postorder: ").split()))
inorder = [40,20,50,10,60,30]
postorder = [40,50,20,60,30,10]
builtTree = tree.ConstructTreeFromInPost(inorder, postorder)
PrintTree(builtTree)
serialized_string = ', '.join(tree.Serialize(root))
print(f"17(i). Serializing the tree with root={root.val}: {serialized_string} ")
print(f"17(ii). Deserializing the string: {serialized_string}")
deserialedTree = tree.Deserialize(serialized_string)
PrintTree(deserialedTree)
print(f"18. Morris Traversal: {tree.MorrisTraversal(root)}")
print(f"19. Flattenting the Tree: ")

tree.FlattenTreeV1(root)
print("(i) Using Recursion: Done ")
PrintTree(root)

print("(ii) Using Stack: Done")
tree.FlattenTreeV2(root)
PrintTree(root)

print("(iii) Without Stack")
tree.FlattenTreeV3(root)
PrintTree(root)

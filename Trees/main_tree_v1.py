from PrintTree import PrintTree
from Node import Node
from Tree_V1 import TreePart1

tree = TreePart1()

root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

root2 = Node(10)
root2.left = Node(9)
root2.right = Node(20)
root2.right.left = Node(15)
root2.right.right = Node(7)

PrintTree(root)

preorder = tree.IterativePreorder(root)
print(f"\n1. Iterative Preorder Traversal: {preorder}")
inorder = tree.IterativeInorder(root)
print(f"2. Iterative Inorder Traversal: {inorder}")
postorder = tree.IterativePostorder(root)
print(f"3. Iterative Postorder Traversal: {postorder}")
levelorder = tree.LevelOrderTraversal(root)
print(f"4. LevelOrder: {levelorder}")
traversal = tree.GetTraversals(root)
print(f"5(i) Preorder: {traversal[0]}\n5(ii)Inorder: {traversal[1]}\n5(iii)Postorder: {traversal[2]}")
print(f"6. Max Depth of Binary Tree: {tree.MaxDepthOfBT(root)}")
print(f"7. Is the tree balanced: {tree.isBalanced(root)}")
print(f"8. Diameter of Binary Tree: {tree.DiameterOfBinaryTree(root)}")
print(f"9(i). Max Path Sum: {tree.MaxPathSum(root)}")
print(f"9(ii). Max Path Sum Leaf to Leaf: {tree.MaxPathSumLeaftoLeaf(root)}")
print(f"10. Is Tree1 with root: {root.val} and Tree2 with root: {root2.val} identical: {tree.isIdentical(root, root2)}")

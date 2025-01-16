from Node import Node
from Tree_V3 import BinarySearchTree, BSTIterator
from PrintTree import PrintTree

def findTarget(root: Node, targetSum: int):
	if not root: return False
	l = BSTIterator(root, False)        
	r = BSTIterator(root, True)
	i = l.next()
	j = r.next()
	
	while i < j:
		if i + j == targetSum: 
			return True
		elif i + j < targetSum: 
			i = l.next()
		else:
			j = r.next()
	return False

tree = BinarySearchTree()

root = Node(5)
root.left = Node(3)
root.left.left = Node(8)
root.left.left.left = Node(1)
root.left.right = Node(4)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)
root.right.right.left = Node(2)
root.right.right.right = Node(10)

PrintTree(root)

# searchNode = int(input("Enter Node to find: "))
searchNode = 5
node, nodeVal = tree.SearchBinaryTree(root, searchNode)
print(f"1. Node found: {node}, {nodeVal}")

# key = int(input("Enter key: "))
key = 8
ceil = tree.CeilBST(root, key)
print(f"2. Ceil value for key {key} -> {ceil}")

# key = int(input("Enter key: "))
key = 8
floor = tree.FloorBST(root, key)
print(f"3. FLoor value for key {key} -> {floor}")

# key = int(input("Enter key to insert: "))
# key = 12
# new_root = tree.InsertinBST(root, key)
print(f"4. After inserting {key} to the tree:")
# PrintTree(new_root)

# # key = int(input("Enter key to delete: "))
# key = 5
# new_root = tree.DeleteFromBST(root, key)
print(f"5. After deleting {key} from the tree:")
# PrintTree(new_root)

# k = int(input("Enter K: "))
k = 2
smallest = tree.KthSmallest(root, k)
print(f"6(i). Kth Smallest element with k={k} -> {smallest}")


# k = int(input("Enter K: "))
largest = tree.KthLargest(root, k)
print(f"6(ii). Kth largest element with k={k} -> {largest}")

print(f"7. Is the BST with root {root.val} valid? --> {tree.isValidBST(root)}")

# p = int(input("Enter node1: "))
# q = int(input("Enter node2: "))
p, q = 6, 8
lca_recursion = tree.LCARecursion(root, p, q)
# Print result
if lca_recursion:
	print(f"8(i) LCA Recursion of {p} and {q} is: {lca_recursion}")
else:
	print(f"No LCA found for {p} and {q}.")

lca_iteration = tree.LCAIterative(root, p, q)
print(f"8(ii) LCA Iteration of {p} and {q}: {lca_iteration}")

# inorder = list(map(int, input("Enter inorder: ").split()))
# preorder = list(map(int, input("Enter preorder: ").split()))
preorder = [8,5,1,7,10,12]
# inorder = preorder.sort()
new_root = tree.BuildTreePreIn(preorder)
print(f"9. Tree from the preorder: {preorder}:")
PrintTree(new_root)

keyNode = Node(8)
# keyNode = Node(int(input("Enter Node: ")))
succ = tree.GetSuccessor(root, keyNode)
pred = tree.GetPredecessor(root, keyNode)
print(f"10(i). Successor of node {keyNode.val} -> {succ.val}")
print(f"10(ii). Predecessor of node {keyNode.val} -> {pred.val}")
print(f"11. BST Iterator")
iterator_list = [
	"BSTIterator", 
	"next", 
	"next", 
	"hasNext", 
	"next", 
	"hasNext", 
	"next", 
	"hasNext", 
	"next", 
	"hasNext"
	]
bstIterator = BSTIterator(root, False)
for command in iterator_list[1:]:
	if command == "next":
		print(f"{command} -> {bstIterator.next()}")
	elif command == "hasNext":
		print(f"{command} -> {bstIterator.hasNext()}")

targetSum = 17
# targetSum = int(input("Enter Target Sum: "))
print(f"12. Pair exists with sum: {targetSum} -> {findTarget(root, targetSum)}")

print(f"13. Recovered BST: BEFORE")
PrintTree(root)
tree.RecoverBST(root)
print("[AFTER]")
PrintTree(root)

root1 = Node(20)
root1.left = Node(15)
root1.left.left = Node(14)
root1.left.left.right = Node(17)
root1.left.right = Node(18)
root1.left.right.left = Node(16)
root1.left.right.right = Node(19)
root1.right = Node(40)
root1.right.left = Node(30)
root1.right.right = Node(60)
root1.right.right.left = Node(50)

output = tree.LargestBST(root1)
print(f"14. Largesrt BST size: {output.maxSize}")

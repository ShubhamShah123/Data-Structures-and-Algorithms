# Problems 37 to 54
from Node import Node
from Stack import Stack
from collections import deque, defaultdict
from typing import Optional

def MorrisTraversal(root: Node):
		if not root: return None
		output = []
		currentNode = root
		while currentNode:
			if currentNode.left is None:
				output.append(currentNode.val)			
				currentNode = currentNode.right
			else:
				prev = currentNode.left
				while prev.right and prev.right != currentNode:
					prev = prev.right
				if prev.right is None:
					prev.right = currentNode
					currentNode = currentNode.left
				else:
					prev.right = None
					output.append(currentNode.val)
					currentNode = currentNode.right
		return output

class BSTIterator:
    def __init__(self, root: Node, reverse: bool):
        self.stack = Stack()
        self.reverse = reverse
        self.pushAll(root, reverse)

    def next(self) -> int:
        topStack = self.stack.pop()
        if not self.reverse:
            self.pushAll(topStack.right, False)
        else:
            self.pushAll(topStack.left, True)
        return topStack.val

    def hasNext(self) -> bool:
        return not self.stack.is_empty()

    def pushAll(self, root: Node, reverse: bool):
        while root is not None:
            self.stack.push(root)
            root = root.right if reverse else root.left

    def printStack(self):
        print([node.val for node in self.stack.stack])


class BinarySearchTree:
	def __init__(self):
		print("[+] Binary Search Trees.")

	def SearchBinaryTree(self, root: Node, searchNode: int):
		while root is not None and root.val != searchNode:
			if root.val < searchNode: root = root.right
			if root.val > searchNode: root = root.left
		return root, root.val
	
	def CeilBST(self, root: Node, key: int):
		ceil_val = -1
		while root:
			if root.val == key:
				ceil_val = root.val
				return ceil_val
			if root.val < key:
				root = root.right
			else:
				ceil_val = root.val
				root = root.left
		return ceil_val

	def FloorBST(self, root: Node, key: int):
		floor = -1
		while root:
			if root.val == key:
				floor = root.val
				return floor
			if root.val < key:
				floor = root.val
				root = root.right
			else:
				root = root.left
		return floor
	
	def InsertinBST(self, root: Node, key: int):
		if not root:
			return Node(key)  # If the tree is empty, create a new node and return it.
		
		curr = root
		while curr:
			if key <= curr.val:
				# Move to the left subtree
				if curr.left:
					curr = curr.left
				else:
					curr.left = Node(key)
					break
			else:
				# Move to the right subtree
				if curr.right:
					curr = curr.right
				else:
					curr.right = Node(key)
					break
		return root

	def DeleteFromBST(self, root: Node, key: int):
		if not root:
			return None  # If the tree is empty, return None.
		
		# If the key matches the root's value, delete the root.
		if root.val == key:
			return self.DeleteFromBSTHelper(root)
		
		curr = root
		while curr:
			# Traverse the left subtree.
			if key < curr.val:
				if curr.left and curr.left.val == key:
					curr.left = self.DeleteFromBSTHelper(curr.left)
					break
				else:
					curr = curr.left
			# Traverse the right subtree.
			elif key > curr.val:
				if curr.right and curr.right.val == key:
					curr.right = self.DeleteFromBSTHelper(curr.right)
					break
				else:
					curr = curr.right
		
		return root

	def DeleteFromBSTHelper(self, root: Node):
		if root.left is None: 
			return root.right
		elif root.right is None: 
			return root.left
		
		nodeRightChild = root.right
		lastRightOfSubTree = self.FindLastRight(root.left)
		lastRightOfSubTree.right = nodeRightChild
		return root.left
	
	def FindLastRight(self, root):
		if root.right is None:
			return root
		return self.FindLastRight(root.right)

	def KthSmallest(self, root: Node, k: int):
		morriesTraversal = MorrisTraversal(root)
		return morriesTraversal[k-1]
	
	def KthLargest(self, root: Node, k: int):
		"""
		Another approach:
		one traversal to count number of nodes in BST
		and Kthlargest -> Kthsmallest(root, N-k)
		"""
		morris = MorrisTraversal(root)
		return morris[-k]
	
	def isValidBST(self, root: Node) -> bool:
		MIN_VAL = -float('inf')
		MAX_VAL = float('inf')
		return self.isValidBSTHelper(root, MIN_VAL, MAX_VAL)
	
	def isValidBSTHelper(self, root: Node, minVal, maxVal):
		if not root: return True
		if root.val >= maxVal or root.val < minVal:
			return False
		leftTree = self.isValidBSTHelper(root.left, minVal, root.val)
		rightTree = self.isValidBSTHelper(root.right, root.val, maxVal)
		return leftTree and rightTree

	def LCARecursion(self, root: Optional[Node], p: int, q: int) -> Optional[Node]:
		if not root: return None
		if root.val > p and root.val > q:
			return self.LCARecursion(root.left, p, q)
		if root.val < p and root.val < q:
			return self.LCARecursion(root.right, p, q)
		return root.val

	def LCAIterative(self, root: Node, p: int, q: int):
		if not root: return None
		curr = root
		while curr:
			if curr.val > p and curr.val > q:
				curr = curr.left
			elif curr.val < p and curr.val < q:
				curr = curr.right
			else:
				return curr.val
		return None
	
	def BuildTreePreIn(self, preorder: list) -> Node:
		index = [0]
		return self.BuildTreePreInHelper(preorder, float('inf'), index)
	
	def BuildTreePreInHelper(self, preorder: list, bound, i: list) -> Node:
		if i[0] == len(preorder) or preorder[i[0]] > bound:
			return None
		root = Node(preorder[i[0]])
		i[0] += 1
		root.left = self.BuildTreePreInHelper(preorder, root.val, i)
		root.right = self.BuildTreePreInHelper(preorder, bound, i)
		return root
	
	def GetSuccessor(self, root: Node, target: Node):
		succ = None
		while root is not None:
			if target.val >= root.val:
				root = root.right
			else:
				succ = root
				root = root.left
		return succ
	
	def GetPredecessor(self, root: Node, target: Node):
		pred = None
		while root is not None:
			if target.val > root.val:
				pred = root
				root = root.right
			else:
				root = root.left
		return pred

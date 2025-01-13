# Problems 1 to 18

from Node import Node
from Stack import Stack
from collections import deque


class TreePart1:
	def IterativePreorder(self, root: Node):
		stack = Stack()
		if not root: return None
		stack.push(root)
		preorder = []
		while not stack.is_empty():
			curr = stack.pop()
			preorder.append(curr.val)        
			if curr.right:
				stack.push(curr.right)
			if curr.left:
				stack.push(curr.left)				
		return preorder
	
	def IterativeInorder(self, root: Node):
		inorder = []
		stack = Stack()
		curr = root
		while True:
			if curr is not None: 
				stack.push(curr)
				curr = curr.left
			else:
				if stack.is_empty():
					break
				curr = stack.pop()
				inorder.append(curr.val)
				curr = curr.right
		return inorder
	
	def IterativePostorder(self, root: Node):
		postorder = []
		curr = root
		stack = Stack()

		while curr is not None or not stack.is_empty():
			if curr is not None:
				stack.push(curr)
				curr = curr.left
			else:
				temp = stack.peek().right
				if temp is not None:
					curr = temp
				else:
					temp = stack.peek()
					stack.pop()
					postorder.append(temp.val)
					while not stack.is_empty() and temp == stack.peek().right:
						temp = stack.peek()
						stack.pop()
						postorder.append(temp.val)
		return postorder
	
	def LevelOrderTraversal(self, root: Node):
		if not root: return None
		result = []
		queue = deque([root])
		while queue:
			size = len(queue)
			level = []
			for _ in range(size):
				node = queue.popleft()
				level.append(node.val)
				if node.left: queue.append(node.left)
				if node.right: queue.append(node.right)
			result.append(level)
		return result
	
	def GetTraversals(self, root: Node):
		preorder, inorder, postorder = [], [], []
		stack = Stack()
		stack.push([root, 1])
		if not root: return None
		while not stack.is_empty():
			pair = stack.pop()
			if pair[1] == 1:
				preorder.append(pair[0].val)
				pair[1] += 1
				stack.push(pair)
				if pair[0].left is not None:
					stack.push([pair[0].left, 1])
			elif pair[1] == 2:
				inorder.append(pair[0].val)
				pair[1] += 1
				stack.push(pair)
				if pair[0].right is not None:
					stack.push([pair[0].right, 1])
			else:
				postorder.append(pair[0].val)
		return preorder, inorder, postorder
	
	def MaxDepthOfBT(self, root):
		if not root: return 0
		leftHeight = self.MaxDepthOfBT(root.left)
		rightHeight = self.MaxDepthOfBT(root.right)
		return 1 + max(leftHeight, rightHeight)

	def isBalanced(self, root) -> bool:
		return self.balancedChecker(root) != -1
	
	def balancedChecker(self, root: Node):
		if not root: return 0
		leftHeight = self.balancedChecker(root.left)
		rightHeight = self.balancedChecker(root.right)
		if leftHeight == -1 and rightHeight == -1: return -1
		if abs(leftHeight - rightHeight) > 1: return -1
		return 1 + max(leftHeight, rightHeight)
	
	def DiameterOfBinaryTree(self, root: Node) -> int:
		maxi = [-float('inf')]
		self.getDiameter(root, maxi)
		return maxi[0]

	def getDiameter(self, root: Node, maxi: list):
		if not root: return 0
		lh = self.getDiameter(root.left, maxi)
		rh = self.getDiameter(root.right, maxi)
		diam = lh + rh + 1
		temp = max(lh, rh) + 1
		maxi[0] = max(maxi[0], diam)
		return temp
	
	def MaxPathSum(self, root: Node):
		maxi = [-float('inf')]
		self.getMaxPath(root, maxi)
		return maxi[0]
	
	def getMaxPath(self, root: Node, maxi: list):
		if not root: return 0
		left = self.getMaxPath(root.left, maxi)
		right = self.getMaxPath(root.right, maxi)
		temp = max(max(left, right)+root.val, root.val)
		ans = max(temp, left+right+root.val)
		maxi[0] = max(maxi[0], ans)
		return temp
	
	def MaxPathSumLeaftoLeaf(self, root: Node):
		maxi = [-float('inf')]
		self.MaxPathSumLeaftoLeafHelper(root, maxi)
		return maxi[0]
	
	def MaxPathSumLeaftoLeafHelper(self, root: Node, maxi: list):
		if not root: return 0
		left = self.getMaxPath(root.left, maxi)
		right = self.getMaxPath(root.right, maxi)
		temp = max(left, right) + root.val
		if root.left is None and root.right is None:
			temp = max(temp, root.val)
		ans = max(temp, left+right+root.val)
		maxi[0] = max(maxi[0], ans)
		return temp
	
	def isIdentical(self, root: Node, root2: Node) -> bool:
		if not root or not root2: return root == root2
		return (root.val == root2.val) and \
				(self.isIdentical(root.left, root2.left)) and \
					(self.isIdentical(root.right, root2.right)) 

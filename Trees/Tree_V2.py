# Problems 19 to 36
from Node import Node
from Stack import Stack
from collections import deque, defaultdict

class TreePart2:
	def __init__(self):
		print("[+] Tree Part 2.")

	def SpiralTraversal(self, root: Node):
		result = []
		if not root: return result
		queue = deque([root])
		flag = 1
		while queue:
			size = len(queue)
			row = [0]*size
			for i in range(size):
				node = queue.popleft()
				row[size-i-1] = node.val
				if node.left: queue.append(node.left)
				if node.right: queue.append(node.right)
			if flag: row = row[::-1]
			flag = not flag
			result.append(row)
		return result
	
	def BoundaryTraversal(self, root: Node):
		result = []
		if not root: return None
		if not self.isLeaf(root): result.append(root.val)
		# left boundary
		result = self.addLeftBounday(root, result)
		# leaves
		result = self.addLeaves(root, result)
		# right boundary
		result = self.addRightBoundary(root, result)
		return result
	
	def isLeaf(self, root: Node) -> bool:
		return True if not root.left and not root.right else False
	
	def addLeftBounday(self, root: Node, result: list):
		curr = root.left
		while curr:
			if not self.isLeaf(curr):
				result.append(curr.val)
			if curr.left is not None:
				curr = curr.left
			else:
				curr = curr.right
		return result
	
	def addLeaves(self, root: Node, result: list):
		if self.isLeaf(root):
			result.append(root.val)
		if root.left is not None: 
			result = self.addLeaves(root.left, result)
		if root.right is not None:
			result = self.addLeaves(root.right, result)
		return result

	def addRightBoundary(self, root: Node, result: list):
		curr = root.right
		temp = []
		while curr:
			if not self.isLeaf(curr):
				temp.append(curr.val)
			if curr.right is not None:
				curr = curr.right
			else:
				curr = curr.left
		result.extend(temp[::-1])
		return result
	
	def VerticalTraversal(self, root: Node):
		if not root: return {}
		queue = deque()
		queue.append([root, 0, 0])
		result = defaultdict(lambda: defaultdict(list))
		while queue:
			node, x, y = queue.popleft()
			result[x][y].append(node.val)
			if node.left:
				queue.append([node.left, x-1, y+1])
			if node.right:
				queue.append([node.right, x+1, y+1])

		x_sorted = sorted(result.items())
		vert = []
		for x, levels in x_sorted:
			leves_sorted = sorted(levels.items())
			vertical = []
			for _, nodes in leves_sorted:
				vertical.extend(nodes)
			vert.append(vertical)
		return vert
	
	def TopBottomView(self, root: Node, flag: str):
		if not root: return {}
		queue = deque()
		queue.append([root, 0])
		result = {}
		while queue:
			node, x = queue.popleft()
			if flag == 'top':
				if not x in result.keys():
					result[x] = [node.val]
				else:
					continue
			elif flag == 'bottom':
				result[x] = [node.val]
			if node.left:
				queue.append([node.left, x-1])
			if node.right:
				queue.append([node.right, x+1])

		x_sorted = sorted(result.items())
		topView = [k[0] for j, k in x_sorted]
		return topView

	def LeftRightView(self, root: Node, flag: str):
		result = {}
		if not root: return result
		tempQueue = deque()
		tempQueue.append([root, 0])
		while tempQueue:
			node, y = tempQueue.popleft()
			if flag == 'left':
				if y not in result.keys():
					result[y] = [node.val]
			elif flag == 'right':
				result[y] = [node.val]
			if node.left: tempQueue.append([node.left, y+1])
			if node.right: tempQueue.append([node.right, y+1])
		ans = [value[0] for key, value in result.items()]
		return ans
	
	def isSymmetrical(self, root: Node) -> bool:
		return root == None or self.isSymmetricalHelper(root.left, root.right)
		
	def isSymmetricalHelper(self, left: Node, right: Node):
		if not left or not right:
			return left == right
		if left.val != right.val:
			return False
		return self.isSymmetricalHelper(left.left, right.right) and \
				self.isSymmetricalHelper(left.right, right.left) 
	
	def PathToNode(self, root: Node, target: int):
		arr = []
		if not root: return arr
		self.PathToNodeHelper(root, target, arr)
		return arr

	def PathToNodeHelper(self, root: Node, target: int, arr: list):
		if root is None:
			return False
		
		arr.append(root.val)

		if root.val == target:
			return True
		
		if self.PathToNodeHelper(root.left, target, arr) or self.PathToNodeHelper(root.right, target, arr):
			return True
		
		arr.pop()
		return False
	
	def LowestCommonAncestor(self, root: Node, node1: int, node2: int):
		if not root: return None
		if root.val == node1 or root.val == node2: return root
		left = self.LowestCommonAncestor(root.left, node1, node2)
		right = self.LowestCommonAncestor(root.right, node1, node2)
		if left and right: return root
		return left if left else right

	def GetMaximumWidth(self, root: Node):
		if not root:
			return 0
		
		# Initialize the queue with a tuple (node, index)
		queue = deque()
		queue.append((root, 0))
		ans = 0
		
		while queue:
			size = len(queue)
			mmin = queue[0][1]  # Get the minimum index at the current level to handle index offset
			first, last = 0, 0
			
			for i in range(size):
				node, curr_id = queue.popleft()
				curr_id -= mmin  # Normalize the index to prevent integer overflow
				if i == 0:
					first = curr_id
				if i == size - 1:
					last = curr_id
					
				if node.left:
					queue.append((node.left, 2 * curr_id + 1))
				if node.right:
					queue.append((node.right, 2 * curr_id + 2))
			
			# Update the maximum width
			ans = max(ans, last - first + 1)
		
		return ans
	
	def ChildrenSumProperty(self, root: Node):
		if not root: return None
		child = 0
		if root.left:
			child += root.left.val
		if root.right:
			child += root.right.val

		
		if child >= root.val:
			root.val = child
		else:
			if root.left: root.left.val = root.val
			elif root.right: root.right.val = root.val
		
		self.ChildrenSumProperty(root.left)
		self.ChildrenSumProperty(root.right)

		total = 0
		if root.left: total += root.left.val
		if root.right: total += root.right.val
		if root.left or root.right: root.val = total

		return root
	
	def NodesAtDistanceK(self, root: Node, k: int, target: int) -> list:
		list_of_nodes = []
		if not root:
			return list_of_nodes
		parentChild, parentChildVal, targetNode = self.getParents(root, target)
		# print("ParentChild DICT: \n", parentChildVal, targetNode, targetNode.val)
		self.searchNodes(targetNode, None, k, parentChild ,list_of_nodes)
		return list_of_nodes
	
	def searchNodes(self, root: Node, prev: Node, k: int, parentChild: dict, list_of_nodes: list):
		if not root: 
			return
		if k==0:
			list_of_nodes.append(root.val)
			return
		if root.left != prev:
			self.searchNodes(root.left, root, k-1, parentChild, list_of_nodes)
		if root.right!= prev:
			self.searchNodes(root.right, root, k-1, parentChild, list_of_nodes)
		if parentChild.get(root) != prev:
			self.searchNodes(parentChild[root], root, k-1, parentChild, list_of_nodes)
		
	def getParents(self, root: Node, target: int):
		targetNode = None
		parentChild = {}
		parentChildVal = {}
		queue = deque([root])
		parentChild[root] = None
		parentChildVal[root.val] = None
		while queue:
			curr = queue.popleft()
			if curr.left:
				parentChild[curr.left] = curr
				parentChildVal[curr.left.val] = curr.val
				queue.append(curr.left)
			if curr.right:
				parentChild[curr.right] = curr
				parentChildVal[curr.right.val] = curr.val
				queue.append(curr.right)
			if curr.val == target: targetNode = curr
				
		return parentChild, parentChildVal, targetNode
	
	def BurnTree(self, root: Node, target: int):
		if not root:
			return 0
		parentChild, parentChildVal, targetNode = self.getParents(root, target)
		visited = set()
		queue = deque()
		queue.append([targetNode, 0])
		maxi = 0
		while queue:
			node, time = queue.popleft()
			maxi = max(maxi, time)
			if node.left and node.left not in visited:
				visited.add(node.left)
				queue.append([node.left, time+1])
			if node.right and node.right not in visited:
				visited.add(node.right)
				queue.append([node.right, time+1])
			if parentChild[node] and parentChild[node] not in visited:
				visited.add(parentChild[node])
				queue.append([parentChild[node], time+1])
		return maxi
	
	def ConstructTreeFromInPre(self, inorder: list, preorder: list) -> Node:
		root = self.ConstructTreeFromInPreHelper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
		return root
	
	def ConstructTreeFromInPreHelper(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
		if preStart > preEnd or inStart > inEnd: return None
		tempNode = Node(preorder[preStart])
		tempNodeIndex = inorder.index(tempNode.val)
		numsLeft = tempNodeIndex - inStart
		tempNode.left = self.ConstructTreeFromInPreHelper(
			preorder, 
			preStart+1, 
			preStart+numsLeft,
			inorder,
			inStart,
			tempNodeIndex-1)
		tempNode.right = self.ConstructTreeFromInPreHelper(
			preorder,
			preStart+numsLeft+1,
			preEnd,
			inorder,
			tempNodeIndex+1,
			inEnd
		)
		return tempNode
	
	def ConstructTreeFromInPost(self, inorder: list, postorder: list) -> Node:
		# Ensure the inputs are valid
		if not inorder or not postorder or len(inorder) != len(postorder):
			return None
		
		# Call the helper function with appropriate parameters
		return self.ConstructTreeFromInPostHelper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

	def ConstructTreeFromInPostHelper(self, inorder: list, inStart: int, inEnd: int, postorder: list, postStart: int, postEnd: int) -> Node:
		if postStart > postEnd or inStart > inEnd:
			return None

		# Create the root node using the last element in postorder
		root_val = postorder[postEnd]
		root = Node(root_val)

		# Find the index of the root in the inorder list
		inorder_root_index = inorder.index(root_val)

		# Calculate the number of nodes in the left subtree
		left_tree_size = inorder_root_index - inStart

		# Recursively construct the left subtree
		root.left = self.ConstructTreeFromInPostHelper(
			inorder,
			inStart,
			inorder_root_index - 1,
			postorder,
			postStart,
			postStart + left_tree_size - 1
		)

		# Recursively construct the right subtree
		root.right = self.ConstructTreeFromInPostHelper(
			inorder,
			inorder_root_index + 1,
			inEnd,
			postorder,
			postStart + left_tree_size,
			postEnd - 1
		)
		
		return root

	def Serialize(self, root: Node) -> str:
		output_string = []
		if not root: return output_string
		queue = deque()
		queue.append(root)
		while queue:
			node = queue.popleft()
			if node is None:
				output_string.append('None')
				continue
			output_string.append(str(node.val)) 
			queue.append(node.left)
			queue.append(node.right)
		return output_string

	def Deserialize(self, string: str) -> Node:
		if not string or string == "None":
			return None

		# Split the input string into a list
		stringList = string.split(', ')

		# Create the root node
		root = Node(int(stringList[0])) if stringList[0] != 'None' else None
		queue = deque([root])
		index = 1

		# Build the tree level by level
		while queue and index < len(stringList):
			current_node = queue.popleft()

			if current_node is not None:
				# Assign the left child
				left_value = stringList[index]
				if left_value != 'None':
					current_node.left = Node(int(left_value))
					queue.append(current_node.left)
				else:
					current_node.left = None
				index += 1

				# Assign the right child
				if index < len(stringList):
					right_value = stringList[index]
					if right_value != 'None':
						current_node.right = Node(int(right_value))
						queue.append(current_node.right)
					else:
						current_node.right = None
					index += 1

		return root

	def MorrisTraversal(self, root: Node):
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

	def FlattenTreeV1(self, root: Node):
		# Approach 1
		prev = [None]
		self.FlattenTreeV1Helper(root, prev)
		return root

	def FlattenTreeV1Helper(self, root: Node, prev: list):
		if root is None: return
		self.FlattenTreeV1Helper(root.left, prev)
		self.FlattenTreeV1Helper(root.right, prev)
		root.right = prev[0]
		root.left = None
		prev[0] = root

	def FlattenTreeV2(self, root: Node):
		if root is None:
			return

		stack = Stack()
		stack.push(root)

		while not stack.is_empty():
			curr = stack.pop()

			# Push right child first so left child is processed next
			if curr.right:
				stack.push(curr.right)
			if curr.left:
				stack.push(curr.left)

			# If the stack is not empty, set the current node's right to the top of the stack
			if not stack.is_empty():
				curr.right = stack.peek()
			else:
				curr.right = None  # For the last node in the tree

			# Set the left pointer to None as part of flattening
			curr.left = None

	def FlattenTreeV3(self, root: Node):
		if not root: return None
		curr = root
		while curr is not None:
			if curr.left is not None:
				prev = curr.left
				while prev.right:
					prev = prev.right
				prev.right = curr.right
				curr.right = curr.left
				curr.left = None
			curr = curr.right
		

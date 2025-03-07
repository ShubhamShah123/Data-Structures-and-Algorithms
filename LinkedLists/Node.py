class Node:
	def __init__(self, data=0, next_node=None):
		self.data = data
		self.next = next_node
	
	def __lt__(self, other):
		return self.data < other.data

class DLLNode:
	def __init__(self, data=0, next_node=None, prev_node=None):
		self.data = data
		self.next = next_node
		self.back = prev_node

class ChildListNode:
	def __init__(self, data=0, child=None, next=None):
		self.data = data
		self.child = child
		self.next = next

class RandomNode:
	def __init__(self, data=0, rand=None, next=None):
		self.data = data
		self.random = rand
		self.next = next

		
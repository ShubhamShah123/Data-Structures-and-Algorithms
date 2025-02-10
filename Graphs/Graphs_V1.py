from collections import deque

class UndirectedGraph:
	def __init__(self, num_nodes: int, num_edges: int):
		print(f"[+] Undirected Graph Init: Node: {num_nodes}, Edges: {num_edges}")
		self.num_nodes = num_nodes
		self.num_edges = num_edges
		self.adj_list = [[] for _ in range(num_nodes+1)]
		self.adj_matrix = [[0 for _ in range(num_nodes+1)] for _ in range(num_nodes+1)]

	def AddEdges(self, node1: int, node2: int):
		self.adj_list[node1].append(node2)
		self.adj_list[node2].append(node1)
		self.adj_matrix[node1][node2] = 1
		self.adj_matrix[node2][node1] = 1

	def display(self):
		for i, itemIter in enumerate(self.adj_list):  # looping through row
			print(f"{i}: {itemIter}")

	def BFSTraversal(self, startingNode: int):
		bfs_output = []
		q = deque([startingNode])
		visitedList = [False] * (self.num_nodes + 1)
		visitedList[startingNode] = True
		while q:
			curr = q.popleft()
			bfs_output.append(curr)		
			for nodes in self.adj_list[curr]:
				if not visitedList[nodes]:
					visitedList[nodes] = True
					q.append(nodes)
		return bfs_output
	
	def DFSTraversal(self, startingNode: int):
		visitedList = [False] * (self.num_nodes + 1)  # 1-based indexing
		output = []
		self.DFSTraversalHelper(startingNode, visitedList, self.adj_list, output)
		return output

	def DFSTraversalHelper(self, node: int, visitedList: list, adjList: dict, output: list):
		visitedList[node] = True
		output.append(node)
		for neighbor in adjList[node]:
			if not visitedList[neighbor]:
				self.DFSTraversalHelper(neighbor, visitedList, adjList, output)

	def GetListFromMatrix(self, adj_matrix, numVertices):
		adjList = [[] for _ in range(numVertices+1)]
		for index, value in enumerate(adj_matrix):
			for j, k in enumerate(value):
				if adj_matrix[index][j] == 1:
					adjList[index].append(j)
		return adjList

	def NumberOfProvinces(self, adjMatrix, numVertices):
    # Convert adjacency matrix to adjacency list
		adjList = self.GetListFromMatrix(adjMatrix, numVertices)
		
		# Initialize visited list (1-based indexing)
		visitedList = [False] * (numVertices + 1)
		counter = 0
		
		# Iterate through nodes (1-based indexing)
		for node in range(1, numVertices + 1):
			if not visitedList[node]:
				counter += 1
				self.NumberOfProvincesHelper(node, visitedList, adjList)
		
		return counter

	def NumberOfProvincesHelper(self, node: int, vis: list, adjList: list):
		# Mark the current node as visited
		vis[node] = True
		
		# Visit all unvisited neighbors
		for neighbor in adjList[node]:
			if not vis[neighbor]:
				self.NumberOfProvincesHelper(neighbor, vis, adjList)

	def DetectCycleBFS(self, numNodes, adjList):
		visitedList = [False] * (numNodes + 1)
		for i in range(numNodes):
			if not visitedList[i]:
				if self.isCycle(i, numNodes, adjList, visitedList):
					return True
		return False
		
	def isCycle(self, src: int, numNodes: int, adjList: list, visitedList: list) -> bool:
		visitedList[src] = 1
		q = deque([(src, -1)])
		while q:
			node, parent = q.popleft()
			for neighbors in adjList[node]:
				if not visitedList[neighbors]:
					visitedList[neighbors] = 1
					q.append((neighbors, node))
				elif parent != neighbors:
					return True
		return False
	
	def DetectCycleDFS(self, numNodes, adjList):
		visitedList = [False] * (numNodes + 1)
		for i in range(numNodes):
			if not visitedList[i]:
				if self.DetectCycleDFSHelper(i, numNodes, adjList, visitedList):
					return True
		return False

	def DetectCycleDFSHelper(self, node: int, parent: int, visitedList: list, adjList: list):
		visitedList[node] = 1
		for it in adjList[node]:
			if visitedList[it] == 0:
				if self.DetectCycleDFSHelper(it, node, visitedList, adjList) == True:
					return True
				elif it != parent: return True
		return False
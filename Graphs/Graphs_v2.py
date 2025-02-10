from collections import deque
from typing import Optional
from Stack import Stack

class UndirectedGraph:
	def __init__(self, num_nodes: int, num_edges: int):
		print(f"[+] Graph Init - Undirected - V2\nNode: {num_nodes}, Edges: {num_edges}")
		self.num_nodes = num_nodes
		self.num_edges = num_edges
		self.adj_list = [[] for _ in range(num_nodes+1)]

	def AddEdges(self, node1: int, node2: int, w: Optional[int]):
		if w:
			self.adj_list[node1].append([node2, w])
			self.adj_list[node2].append([node1, w])
		else:
			self.adj_list[node1].append(node2)
			self.adj_list[node2].append(node1)
	
	def isBipartite(self, mode:str):
		color = [-1] * (self.num_nodes+1)
		for nodes in range(self.num_nodes+1):
			if color[nodes] == -1:
				if mode == 'bfs':
					if not self.isBipartiteBFSHelper(nodes, self.num_nodes, self.adj_list, color):
						return False
				if mode == 'dfs':
					if not self.isBipartiteDFSHelper(nodes, 0, color, self.adj_list): 
						return False
		return True
	
	def isBipartiteBFSHelper(self, start, numNodes, adj_list, color):
		q = deque([start])
		color[start] = 0
		while q:
			node = q.popleft()
			for it in adj_list[node]:
				if color[it] == -1:
					color[it] = 1 - color[node]
					q.append((it))
				elif color[it] == color[node]:
					return False
		return True
	
	def isBipartiteDFSHelper(self, node, col, color, adjList):
		color[node] = col
		for it in adjList[node]:
			if color[it] == -1:
				if not self.isBipartiteDFSHelper(it, 1-col, color, adjList):
					return False
			elif color[it] == col:
				return False
		return True
	
	def GetShortesPathUG(self, source: int):
		dist = [float('inf')] * self.num_nodes
		q = deque([(source, 0)])
		dist[source] = 0
		while q:
			node, dis = q.popleft()
			for adjNode, adjCost in self.adj_list[node]:
				if dist[node] + adjCost < dist[adjNode]:
					dist[adjNode] = dist[node] + adjCost
					q.append((adjNode, dist[adjNode]))
		return dist
	
class DirectedGraph():
	def __init__(self, num_nodes: int, num_edges: int):
		print(f"[+] Graph Init - Directed - V2\nNode: {num_nodes}, Edges: {num_edges}")
		self.num_nodes = num_nodes
		self.num_edges = num_edges
		self.adj_list = [[] for _ in range(num_nodes)]
		self.indegree = {i: 0 for i in range(num_nodes)}

	def AddEdges(self, node1: int, node2: int):
		self.adj_list[node1].append(node2)
		self.indegree[node2] += 1
		
	def DetectCycle(self):
		visited = [0] * (self.num_nodes+1)
		paths_visited = [0] * (self.num_nodes+1)
		for node in range(self.num_nodes):
			if not visited[node]:
				if self.DetectCycleDFSHelper(node, self.adj_list, visited, paths_visited):
					return True
		return False
	
	def DetectCycleDFSHelper(self, i: int, adjList: list, vis: list, pathVis: list, check: Optional[list] = None):
		vis[i] = 1
		pathVis[i] = 1

		for it in adjList[i]:
			if not vis[it]:
				if self.DetectCycleDFSHelper(it, adjList, vis, pathVis, check):
					if check is not None:
						check[i] = 0  # Mark as unsafe if part of a cycle
					return True
			elif pathVis[it]:  # Cycle detected
				if check is not None:
					check[i] = 0  # Mark as unsafe if part of a cycle
				return True

		pathVis[i] = 0  # Reset pathVis when backtracking
		if check is not None:
			check[i] = 1  # Mark as safe since no cycle detected
		return False

	def SafeNodes(self):
		visited = [0] * self.num_nodes
		paths_visited = [0] * self.num_nodes
		check = [0] * self.num_nodes

		for i in range(self.num_nodes):
			if not visited[i]:
				self.DetectCycleDFSHelper(i, self.adj_list, visited, paths_visited, check)

		safeNodes = [i for i in range(self.num_nodes) if check[i] == 1]
		return safeNodes

	def TopologicalSort(self):
		if self.DetectCycle():
			return "Not possible as a cycle is present in the graph."
		
		visited = [0] * self.num_nodes
		st = Stack()  # Use a list as a stack

		for node in range(self.num_nodes):
			if not visited[node]:
				self.TopologicalSortDFS(node, visited, self.adj_list, st)

		# Print topological order by reversing the stack
		output = []
		while not st.is_empty():
			output.append(st.pop())
		return output
	
	def TopologicalSortDFS(self, node, visited, adjList, stack):
		visited[node] = 1

		for adj in adjList[node]:
			if not visited[adj]:
				self.TopologicalSortDFS(adj, visited, adjList, stack)

		stack.push(node)  # Push to stack after processing all neighbors

	def KahnsAlgorithm(self):
		q = deque()
		topoSort = []
		for key, value in self.indegree.items():
			if value == 0:
				q.append((key))
		
		while q:
			node = q.popleft()
			topoSort.append(node)
			for adj in self.adj_list[node]:
				self.indegree[adj] -= 1
				if self.indegree[adj] == 0:
					q.append(adj)

		return topoSort		
	
	def DetectCycleBFS(self):
		q = deque()
		cnt = 0
		for key, value in self.indegree.items():
			if value == 0:
				q.append((key))
		
		while q:
			node = q.popleft()
			cnt += 1
			for adj in self.adj_list[node]:
				self.indegree[adj] -= 1
				if self.indegree[adj] == 0:
					q.append(adj)

		return cnt != self.num_nodes	
	
	def isPossibleCSI(self, n: int, p_list: list):
		adjList = [[] for _ in range(n)]
		inDegree = {i: 0 for i in range(n)}
		for edges in p_list:
			adjList[edges[1]].append(edges[0])
			inDegree[edges[0]] += 1
		
		q = deque()
		cnt = 0
		for key, value in inDegree.items():
			if value == 0:
				q.append((key))
		
		while q:
			node = q.popleft()
			cnt += 1
			for adj in adjList[node]:
				inDegree[adj] -= 1
				if inDegree[adj] == 0:
					q.append(adj)

		return cnt == n
	
	def isPossibleCSII(self, n: int, p_list: list):
		adjList = [[] for _ in range(n)]
		inDegree = {i: 0 for i in range(n)}
		for edges in p_list:
			adjList[edges[1]].append(edges[0])
			inDegree[edges[0]] += 1
		
		q = deque()
		cnt = 0
		topoSort = []
		for key, value in inDegree.items():
			if value == 0:
				q.append((key))
		
		while q:
			node = q.popleft()
			cnt += 1
			topoSort.append(node)
			for adj in adjList[node]:
				inDegree[adj] -= 1
				if inDegree[adj] == 0:
					q.append(adj)
		if cnt == n:
			return topoSort
		else:
			return
		
	def SafeNodesBFS(self, numNodes: int, adjList: list):
		# Reverse the adjacency list
		adjRev = [[] for _ in range(numNodes)]
		inDegree = {i: 0 for i in range(numNodes)}
		for node in range(numNodes):
			for neighbor in adjList[node]:
				adjRev[neighbor].append(node)  # Reverse the edge
				inDegree[node] += 1           # Increment in-degree of the original node

		# Queue for BFS
		q = deque()
		for node in range(numNodes):
			if inDegree[node] == 0:          # Terminal nodes (no outgoing edges)
				q.append(node)

		# BFS to find safe nodes
		safeNodes = []
		while q:
			curr = q.popleft()
			safeNodes.append(curr)
			for neighbor in adjRev[curr]:
				inDegree[neighbor] -= 1     # Decrease in-degree of the neighbor
				if inDegree[neighbor] == 0: # If in-degree becomes 0, it's safe
					q.append(neighbor)

		# Return sorted list of safe nodes
		return sorted(safeNodes)
	
	def AlienDict(self, k, tempList):
		# print(k, dic, type(dic))
		print(f">> Input Dict: {set(tempList)}")
		for i in range(len(tempList)-1):
			s1 = tempList[i]
			s2 = tempList[i+1]
			minLength = min(len(s1), len(s2))
			for j in range(minLength):
				if s1[j] != s2[j]:
					node1 = ord(s1[j]) - ord('a')
					node2 = ord(s2[j]) - ord('a')
					self.AddEdges(node1, node2)
					break
		q = deque()
		topoSort = []
		for key, value in self.indegree.items():
			if value == 0:
				q.append((key))
		
		while q:
			node = q.popleft()
			topoSort.append(node)
			for adj in self.adj_list[node]:
				self.indegree[adj] -= 1
				if self.indegree[adj] == 0:
					q.append(adj)

		topoSort = [chr(i+ord('a')) for i in topoSort]
		return topoSort
		
class DirectedWeigtedGraph():
	def __init__(self, num_nodes: int, num_edges: int):
		print(f"[+] Init Directed Weighted Graph: (u,v): {num_nodes, num_edges}")
		self.num_nodes = num_nodes
		self.num_edges = num_edges
		self.adj_list = [[] for _ in range(num_nodes)]
	
	def AddEdges(self, node1: int, node2: int, w: int):
		self.adj_list[node1].append([node2, w])

	def GetShortestPath(self, source: int):
		visited = [0] * self.num_nodes
		st = Stack()
		# Step 1 : Topological Sort
		for node in range(self.num_nodes):
			if not visited[node]:
				self.TopoSortHelper(node, visited, self.adj_list, st)

		# Step 2 : Popping out the nodes from stack and relaxing the nodes.
		dist = [float('inf')] * self.num_nodes
		dist[source] = 0
		
		while not st.is_empty():
			node = st.pop()
			for adj in self.adj_list[node]:
				adjNode, adjCost = adj
				if dist[node] + adjCost < dist[adjNode]:
					dist[adjNode] = dist[node] + adjCost
		return dist

	def TopoSortHelper(self, node, visited, adjList, stack):
		visited[node] = 1
		for adj in adjList[node]:
			if not visited[adj[0]]:
				self.TopoSortHelper(adj[0], visited, adjList, stack)

		stack.push(node)  # Push to stack after processing all neighbors
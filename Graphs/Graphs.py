from collections import deque
from typing import Optional
from Stack import Stack
from heapq import heappush, heappop, heapify

# -------------------- UNDIRECTED GRAPH ------------------------
class UndirectedGraph:
	def __init__(self, num_nodes: int, num_edges: int):
		# print(f"[+] Graph Init - Undirected - V2\nNode: {num_nodes}, Edges: {num_edges}")
		self.num_nodes = num_nodes
		self.num_edges = num_edges
		self.adj_list = [[] for _ in range(num_nodes+1)]
		self.adj_matrix = [[-1 for _ in range(num_nodes+1)] for _ in range(num_nodes+1)]

	def AddEdges(self, node1: int, node2: int, w: Optional[int] = None):
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
		visitedList = [0] * (numNodes + 1)
		for i in range(1, numNodes+1):
			if not visitedList[i]:
				# print(adjList)
				if self.DetectCycleDFSHelper(i, None, visitedList, adjList):
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

	def DijkstraAlgorithmMethod1(self, num_nodes: int, adjList: list, source: int):
		dist = [float('inf')] * num_nodes
		minH = []
		heapify(minH)
		heappush(minH, (0, source)) #(dist, node)
		dist[source] = 0
		while minH:
			dis, node = heappop(minH)
			for n, d in adjList[node]:
				if dis + d < dist[n]:
					dist[n] = dis + d
					heappush(minH, (dis+d, n))
		return dist
	
	def DijkstraAlgorithmMethod2(self, num_nodes: int, adjList: list, source: int):
		dist = [float('inf')] * num_nodes
		st = set()
		st.add((0, source))
		dist[source] = 0
		while st:
			node = min(st, key=lambda x: x[0])  # Extract the node with min distance
			st.remove(node)
			dis, nde = node
			for n, d in adjList[nde]:
				if dis + d < dist[n]:
					dist[n] = dis + d
					# heappush(minH, (dis+d, n))
					st.add((dis+d, n))
		return dist

	def GetShortestPathDijkstra(self, source, destination):
		dist = [float('inf')] * (self.num_nodes + 1)
		dist[source] = 0
		parent = [i for i in range(self.num_nodes +1)]
		minH = []
		heapify(minH)
		heappush(minH, (0, source))
		while minH:
			dis, node = heappop(minH)
			for n, d in self.adj_list[node]:
				if (dis + d < dist[n]):
					dist[n] = dis + d
					heappush(minH, (dis+d, n))
					parent[n] = node
		if dist[destination] == float('inf'): 
			return [-1]
		else:
			path = []
			node = destination
			while parent[node] != node:
				path.append(node)
				node = parent[node]
			path.append(source)
			output = path[::-1]
			return output
		
	def FloydMarshallUG(self, adj_matrix):
		n = len(adj_matrix)
		for i in range(n):
			for j in range(n):
				if adj_matrix[i][j] == -1:
					adj_matrix[i][j] = float('inf')
				if i == j:
					adj_matrix[i][j] = 0

		for via in range(n):
			for i in range(n):
				for j in range(n):
					adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

		for i in range(n):
			for j in range(n):
				if adj_matrix[i][j] == float('inf'):
					adj_matrix[i][j] = -1
		return adj_matrix
	
	def GetMSTPrims(self, n: int, adjList: list):
		visited = [0] * n
		mst_edges = []
		mst_weight_edges = []
		sum = 0
		minH = []
		heapify(minH)
		heappush(minH, [0, 0, -1])
		while minH:
			wt, node, parent = heappop(minH)
			if visited[node]: continue
			visited[node] = 1
			if parent != -1:
				mst_edges.append([parent, node])
				mst_weight_edges.append([parent, node, wt])
				sum += wt
			for adjNode, adjCost in adjList[node]:
				if not visited[adjNode]:
					heappush(minH, [adjCost, adjNode, node])
		return mst_edges, sum

	def ArticulationPoints(self, n: int, adj: list):
		visited = [0 for _ in range(n)]
		tin = [0 for _ in range(n)]
		low = [0 for _ in range(n)]
		mark = [0 for _ in range(n)]
		timer = 0
		for i in range(n):
			if not visited[i]:
				self.dfs_ap(i, -1, visited, tin, low, mark, adj, timer)
		ans = [i for i in range(n) if mark[i] == 1]
		if len(ans) == 0:
			return -1

		return ans

	def dfs_ap(self, node, parent,visited, tin, low, mark, adj, timer):
		visited[node] = 1
		tin[node] = timer
		low[node] = timer
		timer += 1
		child = 0
		for adjNode in adj[node]:
			if adjNode == parent: continue
			if not visited[adjNode]:
				self.dfs_ap(adjNode, node,visited, tin, low, mark, adj, timer)
				low[node] = min(low[node], low[adjNode])
				# reaching before the node and not computing for the parent
				if low[adjNode] >= tin[node] and parent != -1: 
					mark[node] = 1
				child += 1
			else:
				low[node] = min(low[node], tin[adjNode])
		if child > 1 and parent  == -1:
			mark[node] = 1		



# -------------------- DIRECTED GRAPH ------------------------
class DirectedGraph():
	def __init__(self, num_nodes: int, num_edges: int):
		# print(f"[+] Graph Init - Directed - V2\nNode: {num_nodes}, Edges: {num_edges}")
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
		print(f"\t>> Input Dict: {set(tempList)}")
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

	def KosarajuAlgorithm(self, V: int, adjList: list):
		print("Adjacency List:")
		[print(f"Node {i}: {row}") for i, row in enumerate(adjList)]
		visited = [0 for _ in range(V)]
		st = Stack()
		# Step 1: Sorting based on the finishing time.
		for i in range(V):
			if not visited[i]:
				self.__dfs_kosaraju(i, visited, adjList, st)
		
		# Step 2: Reversing the Graph.
		adjT = [[] for _ in range(V)]
		for i in range(V):
			visited[i] = 0
			for node in adjList[i]:
				adjT[node].append(i)

		# Step 3: Doing DFS
		scc = 0
		scc_list = []
		while not st.is_empty():
			node = st.pop()
			if not visited[node]:
				temp = []
				scc += 1
				self.__dfs_kosaraju_v2(node, visited, adjT, temp)
				scc_list.append(temp)

		print("Scc List: ")
		for i,scc_val in enumerate(scc_list):
			print(f" - SCC {i}: {scc_val}")
		return scc
	
	def __dfs_kosaraju(self, node, visited, adjList, st):
		visited[node] = 1
		for n in adjList[node]:
			if not visited[n]:
				self.__dfs_kosaraju(n, visited, adjList, st)
		st.push(node)
		
	def __dfs_kosaraju_v2(self, node, visited, adjT, temp):
		visited[node] = 1
		temp.append(node)
		for n in adjT[node]:
			if not visited[n]:
				self.__dfs_kosaraju_v2(n, visited, adjT, temp)

# -------------------- DIRECTED WEIGHTED GRAPH ------------------------
class DirectedWeigtedGraph():
	def __init__(self, num_nodes: int, num_edges:int):
		# print(f"[+] Init Directed Weighted Graph: (u,v): {num_nodes, num_edges}")
		self.num_nodes = num_nodes
		self.num_edges = num_edges
		self.adj_list = [[] for _ in range(num_nodes)]
		self.adj_matrix = [[-1 for _ in range(num_nodes)] for _ in range(num_nodes)]
	
	def AddEdges(self, node1: int, node2: int, w: int):
		self.adj_list[node1].append([node2, w])
		self.adj_matrix[node1][node2] = w
		self.adj_matrix[node1][node1] = 0
		self.adj_matrix[node2][node2] = 0


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

	def FloyedWardshall(self, adj_matrix):
		n = len(adj_matrix)
		for i in range(n):
			for j in range(n):
				if adj_matrix[i][j] == -1:
					adj_matrix[i][j] = float('inf')
				if i == j:
					adj_matrix[i][j] = 0

		for via in range(n):
			for i in range(n):
				for j in range(n):
					adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

		for i in range(n):
			for j in range(n):
				if adj_matrix[i][j] == float('inf'):
					adj_matrix[i][j] = -1
		return adj_matrix
	

# -------------------- DISJOINT SETS ------------------------
class DisjointSet():
	def __init__(self, n: int):
		self.rank = [0] * (n+1)
		self.size = [1] * (n+1)
		self.parent = [i for i in range(n+1)]

	def findUPar(self, node: int):
		if node == self.parent[node]: 
			return node
		temp = self.findUPar(self.parent[node])
		self.parent[node] = temp
		return temp
	
	def unionByRank(self, u: int, v: int):
		ulp_u = self.findUPar(u)
		ulp_v = self.findUPar(v)
		if ulp_u == ulp_v:
			return
		elif self.rank[ulp_u] < self.rank[ulp_v]:
			self.parent[ulp_u] = ulp_v
		elif self.rank[ulp_v] < self.rank[ulp_u]:
			self.parent[ulp_v] = ulp_u
		else:
			self.parent[ulp_v] = ulp_u
			self.rank[ulp_u] += 1

	def unionBySize(self, u: int, v: int):
		ulp_u = self.findUPar(u)
		ulp_v = self.findUPar(v)
		if ulp_u == ulp_v:
			return
		elif self.size[ulp_u] < self.size[ulp_v]:
			self.parent[ulp_u] = ulp_v
			self.size[ulp_v] += self.size[ulp_u]
		else:
			self.parent[ulp_v] = ulp_u
			self.size[ulp_u] += self.size[ulp_v]
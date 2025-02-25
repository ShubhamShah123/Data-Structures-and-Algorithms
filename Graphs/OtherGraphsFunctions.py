from collections import deque
import string
from typing import Optional
from heapq import heappush, heappop, heapify
from Graphs import DisjointSet

DIRECTIONS_LIST = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# 'd' for directed, 'u' for undirected
def getMatrixFromEdges(n: int, edges: list, flag: str):
	matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
	[print(r) for r in matrix]
	for u, v, w in edges:  # Assuming edges are given as (node1, node2, weight)
		matrix[u][v] = w
		matrix[u][u] = 0
		matrix[v][v] = 0
		if flag == 'u':  # For undirected graphs, set the reverse edge as well
			matrix[v][u] = w
	return matrix


# 'd' for directed, 'u' for undirected
def getMatrixFromEdgesV2(n: int, edges: list, flag: str):
	matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
	for u, v in edges:  # Assuming edges are given as (node1, node2, weight)
		matrix[u][v] = 1
		matrix[u][u] = 0
		matrix[v][v] = 0
		if flag == 'u':  # For undirected graphs, set the reverse edge as well
			matrix[v][u] = 1
	return matrix


def NumberOfIslands(grid):
	[print(row) for row in grid]
	n = len(grid)
	m = len(grid[0])
	visited = [[0 for _ in range(m)] for _ in range(n)]
	counter = 0
	for r in range(n):
		for c in range(m):
			if visited[r][c] == 0 and grid[r][c] == 1:
				counter += 1
				NumberOfIslandsHelper(r, c, visited, grid)
	return counter


def NumberOfIslandsHelper(row, col, visited, grid):
	visited[row][col] = 1
	q = deque([(row, col)])
	n = len(grid)
	m = len(grid[0])
	while q:
		ro, co = q.popleft()

		"""
		DIRECTIONS_LIST = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		
		Dirctions for only vertical and horizontal connections.
		
		for delRow, delCol in DIRECTIONS_LIST:  # Iterate over the four DIRECTIONS_LIST
			nRow = ro + delRow
			nCol = co + delCol
		"""
		for delRow in range(-1, 2):
			for delCol in range(-1, 2):
				nRow = ro + delRow
				nCol = co + delCol
				"""
				Now Check if the neigtbouring row and column are valid or not
				Meaning the number of row should be between 0 and grid row and so should be column.
				>> nRow >= 0 and nRow < n and nCol >= 0 and nCol < m

				Once checked. Verify that the grid element of that row and col is a land and not visited.
				>> grid[nRow][nCol] == 1 and visited[nRow][nCol] == 0

				if it is, mark them as visited and add it to the queue
				>> visited[nRow][nCol] = 1
				>> q.add([nRow, nCol])
				"""
				validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
				if validBoundary and grid[nRow][nCol] == 1 and visited[nRow][nCol] == 0:
					visited[nRow][nCol] = 1
					q.append((nRow, nCol))


def FloodFill(grid, sr, sc, newColor):
	[print(row) for row in grid]
	initColor = grid[sr][sc]
	grid[sr][sc] = newColor
	n = len(grid)
	m = len(grid[0])
	visited = [[0 for _ in range(m)] for _ in range(n)]
	return FloodFillHelper(grid, sr, sc, newColor, initColor, visited)


def FloodFillHelper(grid, sr, sc, newColor, initColor, visited):
	visited[sr][sc] = 1
	q = deque([(sr, sc)])
	n = len(grid)
	m = len(grid[0])
	while q:
		ro, co = q.popleft()
		for delRow, delCol in DIRECTIONS_LIST:
			nRow = ro + delRow
			nCol = co + delCol
			validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
			if validBoundary and grid[nRow][nCol] == initColor and visited[nRow][nCol] == 0:
				grid[nRow][nCol] = newColor
				q.append((nRow, nCol))
	return grid


def RottenOranges(grid):
	print("INPUT GRID:")
	[print(row) for row in grid]
	n, m = len(grid), len(grid[0])
	q = deque()
	visited = [[0 for _ in range(m)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 2:
				q.append((i, j, 0))
				visited[i][j] = 2
	tm = 0
	while q:
		ro, co, t = q.popleft()
		tm = max(tm, t)
		for delrow, delcol in DIRECTIONS_LIST:
			nRow = ro + delrow
			nCol = co + delcol
			validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
			if validBoundary and visited[nRow][nCol] != 2 and grid[nRow][nCol] == 1:
				q.append((nRow, nCol, t+1))
				visited[nRow][nCol] = 2

	for i in range(n):
		for j in range(m):
			if visited[i][j] != 2 and grid[i][j] == 1:
				return -1

	return tm


def NearestOnesDistance(grid: list):
	print("INPUT GRID: ")
	[print(row) for row in grid]
	n, m = len(grid), len(grid[0])
	visited = [[0]*m for _ in range(n)]
	outputDist = NearestOnesDistanceHelper(n, m, grid, visited)
	return outputDist


def NearestOnesDistanceHelper(n, m, grid, visited):
	dist = [[0]*m for _ in range(n)]
	q = deque()
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 1:
				q.append((i, j, 0))
				visited[i][j] = 1
	while q:
		x, y, d = q.popleft()
		dist[x][y] = d
		for delRow, delCol in DIRECTIONS_LIST:
			nRow = x + delRow
			nCol = y + delCol
			validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
			if validBoundary and not visited[nRow][nCol]:
				q.append((nRow, nCol, d+1))
				visited[nRow][nCol] = 1
	return dist


def ReplaceOX(grid):
	print("INPUT GRID")
	[print(row) for row in grid]
	n, m = len(grid), len(grid[0])
	visited = [[0]*m for _ in range(n)]
	delRow = [d for d, _ in DIRECTIONS_LIST]
	delCol = [d for _, d in DIRECTIONS_LIST]
	# First row and last row
	for j in range(m):
		if not visited[0][j] and grid[0][j] == 'O':
			ReplaceOXDFS(0, j, grid, visited, delRow, delCol)
		if not visited[n-1][j] and grid[n-1][j] == 'O':
			ReplaceOXDFS(n-1, j, grid, visited, delRow, delCol)
	# First col and last col
	for i in range(n):
		if not visited[i][0] and grid[i][0] == 'O':
			ReplaceOXDFS(i, 0, grid, visited, delRow, delCol)
		if not visited[i][n-1] and grid[i][n-1] == 'O':
			ReplaceOXDFS(i, n-1, grid, visited, delRow, delCol)

	for i in range(n):
		for j in range(m):
			if not visited[i][j] and grid[i][j] == 'O':
				grid[i][j] = 'X'


def ReplaceOXDFS(row, col, grid, visited, delRow, delCol):
	visited[row][col] = 1
	n, m = len(grid), len(grid[0])
	for i in range(4):  # 4 because of 4 DIRECTIONS_LIST -> Left, Top, Right, Bottom
		nRow = row + delRow[i]
		nCol = col + delCol[i]
		validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
		if validBoundary and not visited[nRow][nCol] and grid[nRow][nCol] == 'O':
			ReplaceOXDFS(nRow, nCol, grid, visited, delRow, delCol)


def GetNumberOfEnclaves(grid):
	print("INPUT GRID:")
	[print(row) for row in grid]
	n, m = len(grid), len(grid[0])
	visited = [[0]*m for _ in range(n)]
	q = deque()
	for i in range(n):
		for j in range(m):
			if i in [0, n-1] or j in [0, n-1]:
				if grid[i][j] == 1:
					q.append([i, j])
					visited[i][j] = 1
	while q:
		row, col = q.popleft()
		for delRow, delCol in DIRECTIONS_LIST:
			nRow = row + delRow
			nCol = col + delCol
			validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
			if validBoundary and not visited[nRow][nCol] and grid[nRow][nCol] == 1:
				q.append((nRow, nCol))
				visited[nRow][nCol] = 1

	counter = 0
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 1 and not visited[i][j]:
				counter += 1
	return counter


def GetDistinctIslands(grid):
	print("INPUT GRID:")
	[print(i) for i in grid]
	n, m = len(grid), len(grid[0])
	visited = [[0]*m for _ in range(n)]
	setList = set()
	for i in range(n):
		for j in range(m):
			if not visited[i][j] and grid[i][j]:
				tempList = []
				GetDistinctIslandsHelper(i, j, visited, grid, tempList, i, j)
				setList.add(tuple(tempList))
	return len(setList)


def GetDistinctIslandsHelper(row, col, visited, grid, tempList, baseRow, baseCol):
	visited[row][col] = 1
	tempList.append((row - baseRow, col - baseCol))
	n, m = len(grid), len(grid[0])
	for delRow, delCol in DIRECTIONS_LIST:
		nRow = row + delRow
		nCol = col + delCol
		validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
		if validBoundary and not visited[nRow][nCol] and grid[nRow][nCol]:
			GetDistinctIslandsHelper(
				nRow, nCol, visited, grid, tempList, baseRow, baseCol)


def WordLadder1(startWord, targetWord, wordList, mpp: Optional[dict] = None):
	q = deque([(startWord, 1)])
	st = set(wordList)  # Convert wordList to a set for O(1) lookups
	while q:
		word, steps = q.popleft()
		if word == targetWord:
			return steps

		for i in range(len(word)):
			for ch in string.ascii_lowercase:
				if ch != word[i]:  # Avoid replacing with the same letter
					newWord = word[:i] + ch + word[i+1:]  # Create a new word
					if newWord in st:
						st.remove(newWord)  # Prevent visiting again
						q.append((newWord, steps + 1))
	return 0  # If no transformation is found


def WordLadder2(startWord, targetWord, wordList):
	q = deque([[startWord]])  # Queue stores paths, not just words
	st = set(wordList)
	usedOnLevel = set()  # Store words used at the current level
	level = 1
	output = []

	while q:
		path = q.popleft()  # Get the current path
		lastWord = path[-1]

		if lastWord == targetWord:
			if not output or len(output[0]) == len(path):
				output.append(path)
			continue  # Continue to find all shortest paths

		# Remove words used in the previous level
		if len(path) > level:
			level += 1
			for word in usedOnLevel:
				st.discard(word)
			usedOnLevel.clear()

		# Generate transformations
		for i in range(len(lastWord)):
			for ch in string.ascii_lowercase:
				if ch != lastWord[i]:
					newWord = lastWord[:i] + ch + \
						lastWord[i+1:]  # Create a new word
					if newWord in st:
						newPath = path + [newWord]  # Create a new path
						q.append(newPath)
						usedOnLevel.add(newWord)

	return output


def WordLadder2_Optmized(startWord, targetWord, wordList):
	mpp = {}
	ans = []
	q = deque([(startWord, 1)])
	st = set(wordList)  # Convert wordList to a set for O(1) lookups
	mpp[startWord] = 1
	while q:
		word, steps = q.popleft()
		if word == targetWord:
			break
		for i in range(len(word)):
			for ch in string.ascii_lowercase:
				if ch != word[i]:  # Avoid replacing with the same letter
					newWord = word[:i] + ch + word[i+1:]  # Create a new word
					if newWord in st:
						st.remove(newWord)  # Prevent visiting again
						q.append((newWord, steps + 1))
						mpp[newWord] = steps + 1  # Store steps for newWord

	if targetWord in mpp.keys():
		seq = [targetWord]
		Wordladder2DFS(startWord, targetWord, seq, ans, mpp)
	return ans


def Wordladder2DFS(startWord, targetWord, seq, ans, mpp):
	if targetWord == startWord:
		ans.append(seq[::-1])
		return
	steps = mpp[targetWord]
	for i in range(len(targetWord)):
		for ch in string.ascii_lowercase:
			if ch != targetWord[i]:  # Avoid replacing with the same letter
				newWord = targetWord[:i] + ch + \
					targetWord[i+1:]  # Create a new word
				if newWord in mpp.keys() and mpp[newWord]+1 == steps:
					seq.append(newWord)
					Wordladder2DFS(startWord, newWord, seq, ans, mpp)
					seq.pop()


def ShortestDistanceBinaryMaze(grid, source, destination):
	print("INPUT GRID:")
	[print(row) for row in grid]
	src_x, src_y = source
	dst_x, dst_y = destination
	n = len(grid)
	m = len(grid[0])
	print(
		f">> Src: {source} | {grid[src_x][src_y]}, Dest: {destination} | {grid[dst_x][dst_y]}")
	distMatrix = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
	delRow = [d for d, _ in DIRECTIONS_LIST]
	delCol = [d for _, d in DIRECTIONS_LIST]
	q = deque([(0, src_x, src_y)])  # (dist, row, col)
	while q:
		dist, row, col = q.popleft()
		for i in range(4):
			nRow = row + delRow[i]
			nCol = col + delCol[i]
			validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
			if validBoundary and grid[nRow][nCol] and dist + 1 < distMatrix[nRow][nCol]:
				distMatrix[nRow][nCol] = dist + 1
				if nRow == dst_x and nCol == dst_y:
					return dist + 1
				q.append((dist+1, nRow, nCol))
	return -1


def MinimumPathEffort(grid, source, destination):
	print("INPUT GRID:")
	[print(row) for row in grid]
	src_x, src_y = source
	dst_x, dst_y = destination
	n = len(grid)
	m = len(grid[0])
	distMatrix = [[float('inf')] * m for _ in range(n)]
	delRow = [d for d, _ in DIRECTIONS_LIST]
	delCol = [d for _, d in DIRECTIONS_LIST]
	minH = []
	heapify(minH)
	heappush(minH, (0, src_x, src_y))
	distMatrix[src_x][src_y] = 0
	while minH:
		d, r, c = heappop(minH)
		if (r, c) == (dst_x, dst_y):
			return d
		for i in range(4):
			nRow = r + delRow[i]
			nCol = c + delCol[i]
			validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
			if validBoundary:
				diff = abs(grid[nRow][nCol] - grid[r][c])
				newEffort = max(diff, d)
				if newEffort < distMatrix[nRow][nCol]:
					distMatrix[nRow][nCol] = newEffort
					heappush(minH, (newEffort, nRow, nCol))
	return -1


def CheapestFlight(n, src, dest, flights, k):
	print("INPUT GRID: ")
	[print(row) for row in flights]
	print(f">> Src: {src} | Dest: {dest} | Stops: {k}")
	# Step 1: Build the adjacency list
	adjList = [[] for _ in range(n)]
	for u, v, w in flights:
		adjList[u].append((v, w))  # Store (destination, weight)

	# Step 2: Distance array (to track min cost within `k` stops)
	dist = [float('inf')] * n
	dist[src] = 0  # Source has 0 cost

	# Step 3: Parent array to track the path
	parent = [-1] * n
	parent[src] = src  # Root node points to itself

	# Step 4: Min-heap (Priority Queue) - Store (stops, node, cost)
	minH = []
	heapify(minH)
	heappush(minH, (0, src, 0))  # (stops, current node, cost, path)
	# Step 5: BFS-like traversal with at most `k` stops
	while minH:
		stops, node, cost = heappop(minH)

		if stops > k:
			continue  # Skip if stops exceed limit

		for adjNode, price in adjList[node]:
			newCost = cost + price

			# If a cheaper path is found within allowed stops
			if newCost < dist[adjNode] and stops <= k:
				dist[adjNode] = newCost
				heappush(minH, (stops + 1, adjNode, newCost))

	# Step 6: Path reconstruction
	return dist[dest]  # Return cost and path list


def MinNumberMultiplications(start: int, end: int, arr: list):
	dist = [float('inf')] * (10**5)
	dist[start] = 0
	minH = []
	heapify(minH)
	heappush(minH, [0, start])
	while minH:
		steps, num = heappop(minH)
		for it in arr:
			nNum = (it * num) % (10**5)
			if steps + 1 < dist[nNum]:
				dist[nNum] = steps + 1
				if nNum == end:
					return steps + 1
				heappush(minH, [steps + 1, nNum])

	return -1


def WaysToArrive(n: int, roads: list):
	print("INPUT GRAPH: ")
	[print(r) for r in roads]
	src, dst = 0, 8
	adjList = [[] for _ in range(n)]
	for u, v, w in roads:
		adjList[u].append((v, w))
		adjList[v].append((u, w))

	ways = [0] * n
	dist = [float('inf')] * n
	minH = []
	heapify(minH)
	heappush(minH, [0, src])
	ways[src] = 1
	dist[src] = 0
	while minH:
		dis, node = heappop(minH)
		for adjNode, adjDist in adjList[node]:
			newDis = adjDist + dis
			if newDis < dist[adjNode]:
				dist[adjNode] = newDis
				heappush(minH, [newDis, adjNode])
				ways[adjNode] = ways[node]
			elif newDis == dist[adjNode]:
				ways[adjNode] = ways[adjNode] + ways[node]
	return ways[dst]


def BellmanFord(N: int, edges: list, src: int):
	dist = [float('inf')] * N
	dist[src] = 0
	for _ in range(N-1):
		for u, v, w in edges:
			if dist[u] != float('inf') and dist[u] + w < dist[v]:
				dist[v] = dist[u] + w

	# Nth relaxation for negative cycles.
	for i in range(len(edges)-1):
		u, v, w = edges[i]
		if dist[u] != float('inf') and dist[u] + w < dist[v]:
			return [-1]
	return dist


def FloydMarshall(adj_matrix):
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
				adj_matrix[i][j] = min(
					adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

	for i in range(n):
		for j in range(n):
			if adj_matrix[i][j] == float('inf'):
				adj_matrix[i][j] = -1
	return adj_matrix


def findCity(n: int, m: int, edges: list, distanceThresold: int):
	matrix = getMatrixFromEdges(n, edges, 'u')
	print(">> Adjaceny Matrix: ")
	[print(row) for row in matrix]
	adjMatrix = FloydMarshall(matrix)

	city = -1
	cntMax = n
	for i in range(n):
		cnt = 0
		for j in range(n):
			if adjMatrix[i][j] <= distanceThresold:
				cnt += 1
		if cnt <= cntMax:
			cntMax = cnt
			city = i
	return city


def GetNumberOfProvinces(adjMatrix: list, V: int):
	ds = DisjointSet(V)
	for i in range(1, V+1):
		for j in range(1, V+1):
			if adjMatrix[i][j]:
				ds.unionBySize(i, j)

	cnt = 0
	for i in range(1, V+1):
		if ds.parent[i] == i:
			cnt += 1
	return cnt


def MinOperations(V: int, edges: list):
	ds = DisjointSet(V)
	cntExtras = 0
	cntC = 0
	for u, v in edges:
		if ds.findUPar(u) == ds.findUPar(v):
			cntExtras += 1
		else:
			ds.unionBySize(u, v)

	for i in range(V):
		if ds.parent[i] == i:
			cntC += 1

	ans = cntC - 1
	if cntExtras >= ans:
		return ans
	return -1


def MergeAccounts(N: int, details: list):
	ds = DisjointSet(N)
	mapMailNode = {}

	for i in range(N):
		for j in range(1, len(details[i])):
			mail = details[i][j]
			if mail not in mapMailNode:
				mapMailNode[mail] = i  # Store a single representative index
			else:
				# Use a single index, not a list
				ds.unionBySize(i, mapMailNode[mail])

	mergedMails = {}
	for it in mapMailNode.items():
		mail = it[0]
		node = ds.findUPar(it[1])
		if node not in mergedMails:
			mergedMails[node] = set()
		mergedMails[node].add(mail)

	mergedAccounts = []
	for node, emails in mergedMails.items():
		mergedAccounts.append([details[node][0]] + (sorted(emails)))

	return mergedAccounts


def NumberOfIslands2(n, m, operators):
	ds = DisjointSet(n * m)
	vis = [[0 for _ in range(m)] for _ in range(n)]
	cnt = 0
	output = []

	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

	for u, v in operators:
		if vis[u][v]:  # If already visited, append count and continue
			output.append(cnt)
			continue

		vis[u][v] = 1
		cnt += 1
		nodeNo = u * m + v

		for dr, dc in directions:
			nRow, nCol = u + dr, v + dc
			# Valid adjacent land
			if 0 <= nRow < n and 0 <= nCol < m and vis[nRow][nCol]:
				adjNodeNo = nRow * m + nCol
				if ds.findUPar(nodeNo) != ds.findUPar(adjNodeNo):
					cnt -= 1
					ds.unionBySize(nodeNo, adjNodeNo)

		output.append(cnt)

	return output

def isValid(newr, newc, n):
	return 0 <= newr < n and 0 <= newc < n

def MakeLargeIslands(grid):
	print(">> INPUT GRID")
	[print(row) for row in grid]
	n = len(grid)
	m = len(grid[0])
	ds = DisjointSet(n * m)

	dr = [-1, 0, 1, 0]
	dc = [0, -1, 0, 1]

	# Step 1: Connect components
	for r in range(n):
		for c in range(m):
			if grid[r][c] == 0:
				continue
			for ind in range(4):
				nRow = r + dr[ind]
				nCol = c + dc[ind]
				if 0 <= nRow < n and 0 <= nCol < m and grid[nRow][nCol] == 1:
					nodeNo = (r * m) + c  # Corrected indexing
					adjNodeNo = (nRow * m) + nCol  # Corrected indexing
					ds.unionBySize(nodeNo, adjNodeNo)

	# Step 2: Try flipping each '0' and find the largest island
	mx = 0
	for r in range(n):
		for c in range(m):
			if grid[r][c] == 1:
				continue
			comp = set()
			for ind in range(4):
				nRow = r + dr[ind]
				nCol = c + dc[ind]
				if 0 <= nRow < n and 0 <= nCol < m and grid[nRow][nCol] == 1:
					comp.add(ds.findUPar((nRow * m) + nCol))
			sizeTotal = 1  # Flipping 0 to 1
			for it in comp:
				sizeTotal += ds.size[it]
			mx = max(mx, sizeTotal)
	# Step 3: If no zeroes were flipped, return the largest connected component
	for cellNo in range(n * m):
		mx = max(mx, ds.size[ds.findUPar(cellNo)])

	return mx if mx > 0 else 1  # If no islands exist, return at least 1

def maxRemove(stones: list, n: int):
	maxRow, maxCol = 0, 0
	for row, col in stones:
		maxRow = max(maxRow, row)
		maxCol = max(maxCol, col)
	ds = DisjointSet(maxRow + maxCol + 1)
	stoneNodes = {}
	for x, y in stones:
		nodeRow = x
		nodeCol = y + maxRow + 1
		ds.unionBySize(nodeRow, nodeCol)
		stoneNodes[nodeRow] = 1
		stoneNodes[nodeCol] = 1 
	cnt = 0
	for stone, node in stoneNodes.items():
		if ds.findUPar(stone) == node:
			cnt += 1
	return n - cnt

def criticalConnections(N, connections):
	adj = [[] for _ in range(N)]
	visited = [0 for _ in range(N)]
	tin = [0 for _ in range(N)]
	low = [0 for _ in range(N)]
	bridges = []
	timer = 1
	for u, v in connections:
		adj[u].append(v)
		adj[v].append(u)
	print("Adjacency List: ")
	[print(f"Node: {i} -> {adjNodes}") for i, adjNodes in enumerate(adj)]
	dfs(0, -1, visited, adj ,tin, low, timer, bridges)
	return bridges
	
def dfs(node, parent, visited, adj, tin, low, timer, bridges):
	visited[node] = 1
	tin[node] = timer
	low[node] = timer
	timer += 1
	for it in adj[node]:
		if it == parent:
			continue
		if not visited[it]:
			# Not visited
			dfs(it, node, visited, adj, tin, low, timer, bridges)
			low[node] = min(low[node], low[it])
			# node -> it a bridge?
			if low[it] > tin[node]:
				bridges.append([node, it])

		else:
			# Visited
			low[node] = min(low[node], low[it])

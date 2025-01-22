from collections import deque

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
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		
		Dirctions for only vertical and horizontal connections.
		
		for delRow, delCol in directions:  # Iterate over the four directions
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
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	n = len(grid)
	m = len(grid[0])
	while q:
		ro, co = q.popleft()
		for delRow, delCol in directions:
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
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 2:
				q.append((i, j, 0))
				visited[i][j] = 2
	tm = 0
	while q:
		ro, co, t = q.popleft()
		tm = max(tm, t)
		for delrow, delcol in directions:
			nRow = ro + delrow
			nCol = co + delcol
			validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
			if validBoundary and visited[nRow][nCol] != 2 and grid[nRow][nCol] == 1:
				q.append((nRow, nCol, t+1))
				visited[nRow][nCol] = 2 

	for i in range(n):
		for j in range(m):
			if visited[i][j] != 2 and grid[i][j] == 1: return -1

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
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 1:
				q.append((i, j, 0))
				visited[i][j] = 1
	while q:
		x, y, d = q.popleft()
		dist[x][y] = d
		for delRow, delCol in directions:
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
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	delRow = [d for d,_ in directions]
	delCol = [d for _, d in directions]
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
	for i in range(4): # 4 because of 4 directions -> Left, Top, Right, Bottom
		nRow = row + delRow[i]
		nCol = col + delCol[i]
		validBoundary = nRow >= 0 and nRow < n and nCol >= 0 and nCol < m
		if validBoundary and not visited[nRow][nCol] and grid[nRow][nCol] == 'O':
			ReplaceOXDFS(nRow, nCol, grid, visited, delRow, delCol)
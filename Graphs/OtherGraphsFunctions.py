from collections import deque
import string

DIRECTIONS_LIST = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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
	delRow = [d for d,_ in DIRECTIONS_LIST]
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
	for i in range(4): # 4 because of 4 DIRECTIONS_LIST -> Left, Top, Right, Bottom
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
				tempList= []
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
			GetDistinctIslandsHelper(nRow, nCol, visited, grid, tempList, baseRow, baseCol)

def WordLadder1(startWord, targetWord, wordList):
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
                    newWord = lastWord[:i] + ch + lastWord[i+1:]  # Create a new word
                    if newWord in st:
                        newPath = path + [newWord]  # Create a new path
                        q.append(newPath)
                        usedOnLevel.add(newWord)

    return output

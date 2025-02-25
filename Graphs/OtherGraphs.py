import OtherGraphsFunctions as ft

def getInput():
    n, m = list(map(int(input().split())))
    grid = [list(map(int, input(f"Enter row {i+1} (space-separated): ").split())) for i in range(n)]
    return n, m, grid





# n, m, grid = getInput()
grid = [[0,1,1,0], [0,1,1,0], [0,0,1,0], [0,0,0,0], [1,1,0,1]]
numIslands = ft.NumberOfIslands(grid)
print(f"\n6. Number of Islands: {numIslands}")

n, m = 3, 3
sr, sc = 2, 0
grid = [[1,1,1], [2,2,0], [2,2,2]]
newColor = 3

print("\n7. Flood Fill Before Filling: ")
filledGrid = ft.FloodFill(grid, sr, sc, newColor)
print("\n>> OUTPUT GRID")
[print(f"{row}") for row in filledGrid]

print("\n8. Rotten Oranges")
timeTaken = ft.RottenOranges(grid)
print(f">> Time Taken to rotten all oranges: {timeTaken}")

print("\n9. Distance to nearest 1s.")
# n, m, grid = getInput()
grid = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
distGrid = ft.NearestOnesDistance(grid)
print("\n>> OUTPUT DISTANCES")
[print(row) for row in distGrid]

print(f"\n10. Repaces Os to Xs")
# n, m, grid = getInput()

grid = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'X', 'O'],
    ['X', 'O', 'X', 'O', 'X'],
    ['O', 'O', 'X', 'X', 'X'],
]

ft.ReplaceOX(grid)
print("\n>> OUTPUT GRID")
[print(row) for row in grid]

print(f"\n11. Number of enclaves for the below:")
# n, m, grid = getInput()
grid = [
    [0,0,0,1,1],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,1]
]
numEnclaves = ft.GetNumberOfEnclaves(grid)
print(f"\n>> Number of enclaves: {numEnclaves}")

print("\n12. Distinct Islands.")
# n, m, grid = getInput()

grid = [
    [1,1,0,1],
    [1,0,0,1],
    [0,0,0,0],
    [1,0,1,1],
    [1,0,1,0]
]
numDistincIslands = ft.GetDistinctIslands(grid)
print(f"\n>> Number of Distinct Islands: {numDistincIslands}")

startWord = 'hit'
endWord = 'cog'
wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

minLengh = ft.WordLadder1(startWord, endWord, wordList)
print(f"\n25. Word Ladder 1: Min number of transformation from '{startWord}' to '{endWord}': {minLengh}")

startWord = 'bat'
targetWord = 'coz'
wordList = ['pat', 'bot', 'pot', 'poz', 'coz']

print("\n26. Word Ladder 2: Sequences of transformations: ")
sequences = ft.WordLadder2(startWord, targetWord, wordList)
for i, seq in enumerate(sequences):
    print(f" - Seq {i+1}: {' -> '.join(seq)} ")


begin = 'hit'
end = 'cog'
list_of_words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print("\n26(ii). Word Ladder 2: Sequences of transformations - Optmized: ")
optimized_sequences = ft.WordLadder2_Optmized(begin, end, list_of_words)
for i, seq in enumerate(optimized_sequences):
    print(f" - Seq {i+1}: {' -> '.join(seq)} ")

# n,m,grid = get_input()
print("\n29. Shortest Distance in a Binary Maze:")
grid = [
    [1,1,1,1],
    [1,1,0,1],
    [1,1,1,1],
    [1,1,0,0],
    [1,0,0,0]
]
src = [0,1]
dst = [2,2]

dist = ft.ShortestDistanceBinaryMaze(grid, src, dst)
print(f">> Shorted distance from src: {src} to dst: {dst} -> {dist}")

print("\n30. Minimum Path Effort:")
grid = [
    [1,2,2],
    [3,8,2],
    [5,3,5]
]
src = [0,0]
dst = [len(grid)-1, len(grid[0])-1] # Destiantion is always the end of matrix
output = ft.MinimumPathEffort(grid, src, dst)
print(f">> Minimum Path effort from src: {src} to dst: {dst} -> {output}")


print(f"\n31. Cheapest Flights:")
flights = [
    [0,1,5],
    [1,2,5],
    [0,3,2],
    [3,1,2],
    [1,4,1],
    [4,2,1]
]
n = 5 # number of cities


src = 0
dest = 2
stops = 2
cost = ft.CheapestFlight(n, src, dest, flights, stops)
print(f">> Total Cost of flight: {cost} ")

start = 3
end = 75
arr = [2,5,7]
print(f"\n32. Min number of multiplications required to go from {start}->{end}: {ft.MinNumberMultiplications(start, end, arr)}")

roads = [
    [0,1,1],
    [0,2,2],
    [0,3,1],
    [0,4,2],
    [1,5,2],
    [2,5,1],
    [3,5,2],
    [3,7,3],
    [3,6,2],
    [4,6,1],
    [5,8,1],
    [7,8,1],
    [6,8,1]
]

print(f"\n33. No. of ways to arrive at dest from src: {ft.WaysToArrive(9, roads)}")

print("\n34. Bellman Ford Algorithm.")
v = 6
edges = [
    [3,2,6],
    [5,3,1],
    [0,1,5],
    [1,5,-3],
    [1,2,-2],
    [3,4,-2],
    [2,4,3]
]
src = 0
output = ft.BellmanFord(v, edges, src)
print(f">> Output: {output}")

n, m = 5,6
edgesList = [[0, 1, 2],
         [0, 4, 8],
         [1, 2, 3], 
         [1, 4, 2], 
         [2, 3, 1],
         [3, 4, 1]]

print("\n36. Find minimum number of city.")
city = ft.findCity(n, m, edgesList, 2)
print(f">> Minimum number of city reachable : {city}")

print("\n41. Find the number of provinces:")

V, E = 7, 4
edgesList = [
    [1,2],
    [2,3],
    [4,5],
    [6,7]
]
adjMatrix = ft.getMatrixFromEdgesV2(V, edgesList, 'u')
output = ft.GetNumberOfProvinces(adjMatrix, V)

[print(r) for r in adjMatrix]
print(f">> Total number of provinces using Disjoint Set: {output}")

print("\n42. Minimum no. of operations to make graph connected: ")
V, E = 9, 8
edgesList = [
    [0,1],
    [0,2],
    [0,3],
    [1,2],
    [2,3],
    [4,5],
    [5,6],
    [7,8]
]

output = ft.MinOperations(V, edgesList)
print(f">> Output: {output}")


print("\n43. Merge Accounts: ")
N = 6
details = [
    ["John","john1@m.co","john2@m.co","john3@m.co"],
    ["Raj","raj1@m.co","raj2@m.co"],
    ["John","john4@m.co"],
    ["John","john1@m.co","john5@m.co"],
    ["Raj","raj2@m.co","raj3@m.co"],
    ["Mary","mary1@m.co"]
]

mergedDetails = ft.MergeAccounts(N, details)
print(mergedDetails)

print("\n44. Number of Islands 2 or Online queries:")
edgesList = [
    [0,0], [0,0], [1,1], [1,0], [0,1], [0,3],
    [1,3], [0,4], [3,2], [2,2], [1,2], [0,2]
]
numIslands = ft.NumberOfIslands2(4, 5, edgesList)
print(f">> Output: {numIslands}")

print("\n45. Make a large island.")
grid = [
    [1,1,0,1,1],
    [1,1,0,1,1],
    [1,1,0,1,1],
    [0,0,1,0,0],
    [0,0,1,1,1],
    [0,0,1,1,1],
]

output = ft.MakeLargeIslands(grid)
print(f">> Output size of the largest island: {output}")

print("\n46.Removing Max number of stones.")
stones = [
    [0,0],
    [0,2],
    [1,3],
    [3,0],
    [3,2],
    [4,3]
]
n = 6
output = ft.maxRemove(stones, n)
print(f">> Output: {output}")

print("\n48. Cricitical Connections.")
N = 12
edgesList = [
    [0,1],
    [0,3],
    [1,2],
    [2,3],
    [3,4],
    [4,5],
    [5,6],
    [5,8],
    [6,7],
    [7,8],
    [7,9],
    [9,10],
    [9,11],
    [10,11]
]
output = ft.criticalConnections(N, edgesList)
print(f">> Output: {output}")

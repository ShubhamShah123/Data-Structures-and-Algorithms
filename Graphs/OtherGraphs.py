import OtherGraphsFunctions as ft

def getInput():
    n, m = list(map(int(input().split())))
    grid = [list(map(int, input(f"Enter row {i+1} (space-separated): ").split())) for i in range(n)]
    return n, m, grid

print("\n[6. NUMBER OF ISLANDS]")
# n, m, grid = getInput()
grid = [[0,1,1,0], [0,1,1,0], [0,0,1,0], [0,0,0,0], [1,1,0,1]]
numIslands = ft.NumberOfIslands(grid)
print(f"\n>> Total number of islands: {numIslands}")

print(f"\n[7. FLOOD FILL]")
# n, m = list(map(int, input().split()))
# sr, sc = list(map(int, input().split()))
# grid = [list(map(int, input(f"Enter row {i+1} (space-separated): ").split())) for i in range(n)]
# newColor = int(input())
n, m = 3, 3
sr, sc = 2, 0
grid = [[1,1,1], [2,2,0], [2,2,2]]
newColor = 3
neGrid = ft.FloodFill(grid, sr, sc, newColor)
print(">> After Filling: ")
[print(row) for row in neGrid]

print("\n[8. ROTTEN ORANGES]")
# print("Line1: Size of matrix.\nLIne2: Matrix onwards.")
# n, m, grid = getInput()
timeTaken = ft.RottenOranges(grid)
print(f">> Time Taken to rotten all oranges: {timeTaken}")

print("\n[9. DISTANCE TO NEAREST 1s]")
# n, m, grid = getInput()
grid = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
distGrid = ft.NearestOnesDistance(grid)
print(">> OUTPUT DISTANCES")
[print(row) for row in distGrid]

print(f"\n[10. REPLACE Os TO Xs]")
# n, m, grid = getInput()

grid = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X', 'O'],
    ['X', 'X', 'O', 'X', 'O'],
    ['X', 'O', 'X', 'O', 'X'],
    ['O', 'O', 'X', 'X', 'X'],
]

ft.ReplaceOX(grid)
print(">> OUTPUT GRID")
[print(row) for row in grid]

print(f"\n[11. NUMBER OF ENCLAVES]")
# n, m, grid = getInput()
grid = [
    [0,0,0,1,1],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,1]
]
numEnclaves = ft.GetNumberOfEnclaves(grid)
print(f">> Number of enclaves: {numEnclaves}")

print("\n[12. CALCULATE DISTINCT ISLANDS]")
# n, m, grid = getInput()

grid = [
    [1,1,0,1],
    [1,0,0,1],
    [0,0,0,0],
    [1,0,1,1],
    [1,0,1,0]
]
numDistincIslands = ft.GetDistinctIslands(grid)
print(f">> Number of Distinct Islands: {numDistincIslands}")

startWord = 'hit'
endWord = 'cog'
wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

minLengh = ft.WordLadder1(startWord, endWord, wordList)
print(f"\n25. Min number of transformation from '{startWord}' to '{endWord}': {minLengh}")

startWord = 'bat'
targetWord = 'coz'
wordList = ['pat', 'bot', 'pot', 'poz', 'coz']

sequences = ft.WordLadder2(startWord, targetWord, wordList)
print(sequences)
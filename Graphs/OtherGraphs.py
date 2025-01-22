import OtherGraphsFunctions as ft
print("\n[4. NUMBER OF ISLANDS]")
r, c = 5, 4
# grid = [list(map(int, input(f"Enter row {i+1} (space-separated): ").split())) for i in range(r)]
grid = [[0,1,1,0], [0,1,1,0], [0,0,1,0], [0,0,0,0], [1,1,0,1]]
numIslands = ft.NumberOfIslands(grid)
print(f"\n>> Total number of islands: {numIslands}")

print(f"\n[5. FLOOD FILL]")
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

print("\n[6. ROTTEN ORANGES]")
# print("Line1: Size of matrix.\nLIne2: Matrix onwards.")
# n, m = list(map(int, input().split()))
n, m = 3, 3
grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [list(map(int, input(f"Enter row {i+1} (space-separated): ").split())) for i in range(n)]
timeTaken = ft.RottenOranges(grid)
print(f">> Time Taken to rotten all oranges: {timeTaken}")

print("\n[7. DISTANCE TO NEAREST 1s]")
# n, m = list(map(int(input().split())))
# grid = [list(map(int, input(f"Enter row {i+1} (space-separated): ").split())) for i in range(n)]
grid = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
distGrid = ft.NearestOnesDistance(grid)
print(">> OUTPUT DISTANCES")
[print(row) for row in distGrid]

print(f"\n[8. REPLACE Os TO Xs]")
# n, m = list(map(int(input().split())))
# grid = [list(map(int, input(f"Enter row {i+1} (space-separated): ").split())) for i in range(n)]

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
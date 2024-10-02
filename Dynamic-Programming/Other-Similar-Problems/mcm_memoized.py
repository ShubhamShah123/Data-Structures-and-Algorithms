from MatrixChainClass import MatrixChain

n = int(input("Enter the number of elements in array: "))
array = [int(input(f"Enter element {i}: ")) for i in range(n)]

t = [[-1 for _ in range(n)] for _ in range(n)]
MC = MatrixChain()
matrix, cost = MC.MemoizedSolve(array, 1, n-1, t, flag=1)
print(f"Cost of MCM: {cost}")
MC.print_matrix(matrix)
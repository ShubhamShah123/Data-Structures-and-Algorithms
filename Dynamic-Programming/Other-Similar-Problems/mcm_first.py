from MatrixChainClass import MatrixChain

n = int(input("Enter the number of elements in array: "))
array = [int(input(f"Enter element {i}: ")) for i in range(n)]

MC = MatrixChain()
cost = MC.RecursionSolve(array, 1, n-1)
print(f"Cost of MCM: {cost}")
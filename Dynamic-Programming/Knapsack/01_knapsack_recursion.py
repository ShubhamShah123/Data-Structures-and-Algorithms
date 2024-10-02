import dp_functions as dp

N = int(input("Enter the total number of elements(N): "))
W = int(input("Enter the knapsack capacity(W): "))
print("\n")
weights = [int(input(f"Enter the weight for item {i}: ")) for i in range(N)]
print("\n")
values = [int(input(f"Enter the value for item {i}: ")) for i in range(N)]

profit = dp.KnapsackRecursion(weights, values, W, N)
print("Maximum Profit: ${:.2f}".format(profit))
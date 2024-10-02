import dp_functions as dp

N = int(input("Enter the total number of elements(N): "))
W = int(input("Enter the knapsack capacity(W): "))

weights = [int(input(f"Enter the weight for item {i}: ")) for i in range(N)]
values = [int(input(f"Enter the value for item {i}: ")) for i in range(N)]

maxProfit = dp.KnapsackTopDown(weights, values, W, N)
print("Max Profit: ${:.2f}".format(maxProfit))
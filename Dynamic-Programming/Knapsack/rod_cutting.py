import dp_functions as dp

N = int(input("Enter N: "))
length = [int(input(f"Enter the length for item {i}: ")) for i in range(N)]
price = [int(input(f"Enter the price for item {i}: ")) for i in range(N)]
maxLength = len(length)
maxProfit = dp.RodCutting(price, N,  maxLength, length)
print("Maximum Profit: ${:.2f}".format(maxProfit))
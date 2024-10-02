# Get maximum number of ways

import dp_functions as dp

N = int(input("Enter number of coins: "))
coins = [int(input(f"Enter value of coin {i}: ")) for i in range(N)]
sum = int(input("Enter the sum: "))

maxWays = dp.CoinChangeWays(coins, N, sum, True)
print(f"Max Number of ways: {maxWays}")
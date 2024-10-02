# Get minimum number of coins.
import dp_functions as dp

N = int(input("Enter number of coins: "))
coins = [int(input(f"Enter value of coin {i}: ")) for i in range(N)]
sum = int(input("Enter the sum: "))

numOfWays = dp.CoinChangeCoins(coins, N, sum, True)
print(f"Min number of ways: {numOfWays}")